# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. The text arrives at POST /submit. That route adds a content_id.
2. detector.model_signal scores the text. It adds model_score.
3. stylometry.style_signal scores the shape of the text. It adds style_score.
4. scoring.combine_signals turns the two scores into one combined score.
5. scoring.score_to_label turns that score into a guess and a label. Guess is human, unsure, or ai, and label is the sentence the reader sees.
6. audit.log_decision writes that decision into the log.
7. The route sends the response back. The reader sees the label.

False positive trace: A person writing in common words and short sentences gets model_score 0.72 and style_score 0.70. The combined score is 0.71. The label says: We think this was probably written by an AI. They can send POST /appeal with the content_id and a reason. That 0.71 is why the AI line is 0.80.

Endpoint shape:
POST /submit
In: text (string), creator_id (string).
Out: content_id (string), guess (human, unsure, or ai), confidence (the combined score), label (the sentence), model_score (number), style_score (number).
POST /appeal
In: content_id (string), reasoning (string).
Out: content_id (string), status (under_review), message (Your appeal is recorded.).


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** 
Perplexity, how predictable the text is to gpt2. model_score is from 0 to 1. Higher means more likely AI.

**Why that might differ between human and AI writing:**
A model picks a likely next word, so text a model wrote is often easy to predict. Human writing wanders more.

**What it can't see:**
Common words in short, ordinary sentences. A real person writing that way would score like a machine.

### Signal two — the style signal

**What it measures:**
The shape of the text: sentence_length_spread, type_token_ratio, and punctuation_density. style_score is from 0 to 1. Higher means more likely AI.

**Why that might differ between human and AI writing:**
Generated sentences tend to stay even and mid-length, with a narrower vocabulary. Human sentences vary more in length.

**What it can't see:**
The meaning. Typos, broken-up sentences, and a pasted quotation would change the score.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
The combined score is 0.3 times the model score plus 0.7 times the style score. On the even AI paragraph the model score was 0.2337 and the style score was 0.8214, so the style score is the one that separates that paragraph from the human one.


**The numbers:**
WEIGHT_MODEL_SIGNAL is 0.3. WEIGHT_STYLE_SIGNAL is 0.7. The numbers are in config.py.


**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
"I burned the rice and ate cereal instead." The model score is 0.0673 and the style score is 0.75. The combined score is 0.5452.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. |
| unsure | 0.35 – 0.60 | We can't tell whether a person wrote this or an AI did. |
| high-confidence AI | 0.60 – 1.00 | We think this was probably written by an AI. |


**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
The person reading it may have written every word. The sentence says we can't tell, and it names a person and an AI as the two possibilities.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "The system provides reliable results for users. The process supports clear results for teams. The design offersstable results for clients.", "creator_id": "writer-1"}'
```

```json
{
  "confidence": 0.6451,
  "content_id": "3ddf66a9-fbc6-483c-8cc1-34950547cfe0",
  "guess": "ai",
  "label": "We think this was probably written by an AI.",
  "model_score": 0.2337,
  "style_score": 0.8214
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "3ddf66a9-fbc6-483c-8cc1-34950547cfe0", "reasoning": "I wrote this."}'
```

```json
{
  "content_id": "3ddf66a9-fbc6-483c-8cc1-34950547cfe0",
  "message": "Your appeal is recorded.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.5452,
      "content_id": "7ac108e3-7175-4877-a9bf-301b62dfcf1c",
      "creator_id": "writer-1",
      "guess": "unsure",
      "label": "We can't tell whether a person wrote this or an AI did.",
      "model_score": 0.0673,
      "status": "decided",
      "style_score": 0.75,
      "timestamp": "2026-11-04T09:52:25+00:00"
    },
    {
      "combined_score": 0.6451,
      "content_id": "3ddf66a9-fbc6-483c-8cc1-34950547cfe0",
      "creator_id": "writer-1",
      "guess": "ai",
      "label": "We think this was probably written by an AI.",
      "model_score": 0.2337,
      "status": "decided",
      "style_score": 0.8214,
      "timestamp": "2026-11-04T09:52:48+00:00"
    },
    {
      "content_id": "3ddf66a9-fbc6-483c-8cc1-34950547cfe0",
      "creator_id": "writer-1",
      "event": "appeal",
      "reasoning": "I wrote this.",
      "status": "under_review",
      "timestamp": "2026-11-04T10:13:35+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* 
I asked why the rice curl returned a huge HTML page.

- *What came back:*
The page was a Flask error. The bottom line was NameError: name 'detector' is not defined, on the model_signal call in app.py. The import detector line was missing.

- *What I changed:*
I added import detector inside submit, above the model_signal call. The next rice curl returned JSON, and model_score was 0.0673.


**Moment 2**

- *What I asked for:*
I asked for steps to fix the combining rule. The even AI paragraph had combined to 0.2337, and the lumpy human paragraph had combined to 0.3522.

- *What came back:*
Drop the rule that keeps the lower score when the two signals are 0.30 apart. Use 0.3 times the model score plus 0.7 times the style score.

- *What I changed:*
I set WEIGHT_MODEL_SIGNAL to 0.3 and WEIGHT_STYLE_SIGNAL to 0.7 in config.py, and combine_signals to that sum. A new submit put the even AI paragraph at 0.6451 and the lumpy human paragraph at 0.3113.


**Moment 3**

- *What I asked for:*
I asked for the one change after the diagnosis, then both reruns.

- *What came back:*
Check the text in submit before either score. A missing field, a non-string, under 10 characters once stripped, or over 10000 characters returns status 400 and no guess.

- *What I changed:*
I put that check in app.py. The after run held 31 and broke 25. Criterion 5 came back 400, 400, 400, unsure on all 3 trials.


<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 7 per minute, 140 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
I set 7 a minute and 140 a day. A writer submitting their own work a few times an hour stays under 7 a minute. A script sending a thousand variations to map the thresholds hits 7 in the first minute, and 140 a day stops the rest of that run.


**What a caller counts as:** 
<!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->
per creator_id. A script that keeps one creator_id shares one count. A script that changes creator_id on each request looks like a thousand callers. When creator_id is missing, the count uses the caller's address.


**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 429 429 429 429 429 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->
Held: 18. Broke: 38.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `8cb9a7d0-4965-401c-ae9a-a703e0d5eaa5` | unsure | 0.499 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `a4717e92-daa1-4bc5-98a4-7bba4da8ed44` | unsure | 0.398 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `4dc85794-5d75-4c2b-8ad9-679685af59c8` | unsure | 0.548 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `de8db803-bbb4-4057-b7a7-0927f248055e` | ai | 0.619 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `b972bcf7-37be-4fec-ab88-57e7d6ac63fb` | unsure | 0.351 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `bdfddc1d-8d67-40d4-abee-cf44d9e14830` | unsure | 0.362 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `668cc875-d49d-4983-b9f7-f9bc9bb92ee1` | unsure | 0.566 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `6cb4d54b-9087-4d5e-b7c5-90649d28c870` | unsure | 0.500 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `8aae8685-8f2a-4fda-b718-4db508906355` | unsure | 0.552 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `cb4c5e94-0172-4c94-bda9-fddd7552506f` | ai | 0.800 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `d7fa8bb7-5731-4822-a7de-ddb80a601633` | unsure | 0.584 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `cbae475b-f9ba-4b11-9c3d-3fee9660122d` | ai | 0.702 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `a8e5beb8-9de9-4cee-85e9-bf44eacffbe5` | ai | 0.700 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `15229190-e552-4463-8f1d-38698c21a478` | ai | 0.667 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `2d32c4ed-9c12-43cc-bb42-723b425ed1bd` | ai | 0.716 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `eea5b8c2-f713-4d66-80ec-98befc4cbab4` | ai | 0.640 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `7d9b2dfa-0454-4ca3-a6d2-3c55b2121507` | unsure | 0.599 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `27d420bc-9469-4e05-abd7-661a582a3726` | unsure | 0.470 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `386afa58-322a-4fff-8f17-f54eb4780636` | unsure | 0.444 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `8d82395d-dbee-4136-b494-9ec8f33c3137` | human | 0.327 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `8ea5d68c-1a89-42c3-a4ce-942b69c50a12` | unsure | 0.583 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `8ff5fc06-2311-426e-b349-080a0b690cba` | unsure | 0.526 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `b93385ac-2479-4f48-b246-a8a65845626f` | unsure | 0.383 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `9b181b9a-827d-4ac8-b556-d746d38ff66e` | unsure | 0.572 | HELD |
| MF01 | malformed | text is only whitespace | 200 | `00b82683-29cf-4e3b-bcaa-2417d489940c` | ai | 0.762 | BROKE |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `cf7b9bdc-40a5-431b-89f7-ced99da7f470` | unsure | 0.525 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `9175e8f2-18fe-45bc-ae8a-da2ca37f7e88` | ai | 0.703 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `54487ff2-a7ed-400b-93f1-262b569ceb8b` | ai | 0.824 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `3f92c1ae-374b-4015-8df3-097f9f016e80` | ai | 0.999 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `a66fad20-d66a-4e53-b8fd-c2114e8407fe` | ai | 0.972 | BROKE |
| MF08 | malformed | text is 60,000 characters | 200 | `1461ce5b-ba19-4d84-9386-545f7be34a13` | ai | 0.828 | BROKE |
| RQ01 | malformed | no text field at all | 500 | `—` | — | — | BROKE |
| RQ02 | malformed | no creator_id | 200 | `312428a8-5839-426f-b0f3-26391335569e` | unsure | 0.597 | HELD |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 500 | `—` | — | — | BROKE |
| RQ06 | malformed | creator_id is an object | 200 | `e09bc3fb-ef85-4f59-bd09-af29448686c2` | unsure | 0.540 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 500 | `—` | — | — | BROKE |
| RQ09 | malformed | body is empty | 500 | `—` | — | — | BROKE |
| RQ10 | malformed | body is form-encoded, not JSON | 500 | `—` | — | — | BROKE |
| RQ11 | malformed | body is JSON claiming to be plain text | 500 | `—` | — | — | BROKE |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `98856b5b-f895-4d1d-b4a0-7f60905d7a5a` | unsure | 0.534 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `151c6b6c-ea6f-4ccd-98cf-1990bbeb7f07` | unsure | 0.534 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c36b324b-f8fa-41dc-936f-416730790d25` | unsure | 0.534 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b265d443-e713-4ea9-b6e8-5c2854fb6740` | unsure | 0.534 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `71d8acd8-b467-491c-a1b1-e47474f23d0b` | unsure | 0.534 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f1fdc370-f74b-4bda-af5a-7f259b0ae4b6` | unsure | 0.534 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d41dc83d-6b91-498f-bebc-2145c243665b` | unsure | 0.534 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
[
  {
    "combined_score": 0.4992,
    "content_id": "8cb9a7d0-4965-401c-ae9a-a703e0d5eaa5",
    "creator_id": "attacker_EV01",
    "guess": "unsure",
    "label": "We can't tell whether a person wrote this or an AI did.",
    "model_score": 0.1635,
    "status": "decided",
    "style_score": 0.6431,
    "timestamp": "2026-11-11T10:17:07+00:00"
  },
  {
    "combined_score": 0.3508,
    "content_id": "b972bcf7-37be-4fec-ab88-57e7d6ac63fb",
    "creator_id": "attacker_EV05",
    "guess": "unsure",
    "label": "We can't tell whether a person wrote this or an AI did.",
    "model_score": 0.3212,
    "status": "decided",
    "style_score": 0.3635,
    "timestamp": "2026-11-11T10:17:07+00:00"
  },
  {
    "combined_score": 0.5521,
    "content_id": "8aae8685-8f2a-4fda-b718-4db508906355",
    "creator_id": "attacker_EV09",
    "guess": "unsure",
    "label": "We can't tell whether a person wrote this or an AI did.",
    "model_score": 0.7042,
    "status": "decided",
    "style_score": 0.4869,
    "timestamp": "2026-11-11T10:17:07+00:00"
  },
  {
    "combined_score": 0.7016,
    "content_id": "cbae475b-f9ba-4b11-9c3d-3fee9660122d",
    "creator_id": "attacker_FP02",
    "guess": "ai",
    "label": "We think this was probably written by an AI.",
    "model_score": 0.7387,
    "status": "decided",
    "style_score": 0.6857,
    "timestamp": "2026-11-11T10:17:07+00:00"
  },
  {
    "combined_score": 0.7002,
    "content_id": "a8e5beb8-9de9-4cee-85e9-bf44eacffbe5",
    "creator_id": "attacker_FP03",
    "guess": "ai",
    "label": "We think this was probably written by an AI.",
    "model_score": 0.8051,
    "status": "decided",
    "style_score": 0.6552,
    "timestamp": "2026-11-11T10:17:07+00:00"
  },
  {
    "combined_score": 0.7157,
    "content_id": "2d32c4ed-9c12-43cc-bb42-723b425ed1bd",
    "creator_id": "attacker_FP05",
    "guess": "ai",
    "label": "We think this was probably written by an AI.",
    "model_score": 0.8005,
    "status": "decided",
    "style_score": 0.6794,
    "timestamp": "2026-11-11T10:17:07+00:00"
  },
  {
    "combined_score": 0.3271,
    "content_id": "8d82395d-dbee-4136-b494-9ec8f33c3137",
    "creator_id": "attacker_PI02",
    "guess": "human",
    "label": "We think this was probably written by a person.",
    "model_score": 0.2044,
    "status": "decided",
    "style_score": 0.3797,
    "timestamp": "2026-11-11T10:17:07+00:00"
  },
  {
    "combined_score": 0.9991,
    "content_id": "3f92c1ae-374b-4015-8df3-097f9f016e80",
    "creator_id": "attacker_MF06",
    "guess": "ai",
    "label": "We think this was probably written by an AI.",
    "model_score": 0.9969,
    "status": "decided",
    "style_score": 1.0,
    "timestamp": "2026-11-11T10:17:08+00:00"
  },
  {
    "combined_score": 0.9719,
    "content_id": "a66fad20-d66a-4e53-b8fd-c2114e8407fe",
    "creator_id": "attacker_MF07",
    "guess": "ai",
    "label": "We think this was probably written by an AI.",
    "model_score": 0.9064,
    "status": "decided",
    "style_score": 1.0,
    "timestamp": "2026-11-11T10:17:08+00:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "7 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-11T10:17:08+00:00"
  }
]
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:
FP05 is the one I would least want to explain to the person who wrote it. The target was technical documentation written by a person. The service returned guess ai, model_score 0.8005, style_score 0.6794, and combined score 0.7157. The label was "We think this was probably written by an AI." The input starts "To configure the service, edit the settings file in the installation directory."


---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | at most 1 guess ai in 10 | 1 of 10 | 1 of 10 | 1 of 10 | MET |
| 2. Score spread | model average at least 0.25 above mine | 0.2576 | 0.2576 | 0.2576 | MET |
| 3. Label coverage | 1 human, 1 unsure, and 1 ai | human, unsure, ai | human, unsure, ai | human, unsure, ai | MET |
| 4. Appeal path | 5 of 5 status under_review, and 5 appeal log lines | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Bad input | 3 bad bodies have no guess, then 1 normal guess | null, null, ai, unsure | null, null, ai, unsure | null, null, ai, unsure | MISSED |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Trial 1 of each criterion is below. Trials 2 and 3 matched trial 1. run_eval.py main wrote results/run_2026-11-11_0258_before.md. app.py submit returned the submit JSON. I extended run_eval.py so that command calls app.py appeal after each submit in the appeal scenario. The 5 log lines under the appeal block are from logs/audit.jsonl.

**my own writing, trial 1**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2966,
    "model_score": 0.0603,
    "style_score": 0.3979,
    "label": "We think this was probably written by a person.",
    "sent": "I allow at most 1 false positive in 10 because on a writing site a wro"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3699,
    "model_score": 0.1311,
    "style_score": 0.4722,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "In class, both signals scored a human poem near 0.5, and the combined "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4639,
    "model_score": 0.1152,
    "style_score": 0.6133,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "If no input can reach a label, the ranges have a gap. Each guess has t"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.393,
    "model_score": 0.0696,
    "style_score": 0.5316,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "An appeal that leaves the status unchanged still shows the writer the "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4039,
    "model_score": 0.054,
    "style_score": 0.5539,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "Those are the missing, empty, and enormous cases. A crash fails this. "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6077,
    "model_score": 0.57,
    "style_score": 0.6238,
    "label": "We think this was probably written by an AI.",
    "sent": "The combined score is 0.3 times the model score plus 0.7 times the sty"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851,
    "model_score": 0.4518,
    "style_score": 0.6423,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "I burned the rice and ate cereal instead. The model score is 0.0673 an"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4461,
    "model_score": 0.2062,
    "style_score": 0.5489,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "I asked why the rice curl returned a huge HTML page. The page was a Fl"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.473,
    "model_score": 0.3127,
    "style_score": 0.5417,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "FP05 is the one I would least want to explain to the person who wrote "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3489,
    "model_score": 0.1545,
    "style_score": 0.4322,
    "label": "We think this was probably written by a person.",
    "sent": "EV01 came back unsure at 0.4992. The style score stays 0.6431 when the"
  }
]
```

**score spread, trial 1**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6451,
    "model_score": 0.2337,
    "style_score": 0.8214,
    "label": "We think this was probably written by an AI.",
    "sent": "The system provides reliable results for users. The process supports c"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.593,
    "model_score": 0.0602,
    "style_score": 0.8214,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "The report presents clear findings for readers. The method supports st"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6484,
    "model_score": 0.1891,
    "style_score": 0.8453,
    "label": "We think this was probably written by an AI.",
    "sent": "The tool delivers consistent output for staff. The workflow maintains "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.642,
    "model_score": 0.1677,
    "style_score": 0.8453,
    "label": "We think this was probably written by an AI.",
    "sent": "The model produces accurate scores for texts. The service returns accu"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.625,
    "model_score": 0.1108,
    "style_score": 0.8453,
    "label": "We think this was probably written by an AI.",
    "sent": "The check gives direct answers for authors. The log stores direct answ"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2966,
    "model_score": 0.0603,
    "style_score": 0.3979,
    "label": "We think this was probably written by a person.",
    "sent": "I allow at most 1 false positive in 10 because on a writing site a wro"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3699,
    "model_score": 0.1311,
    "style_score": 0.4722,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "In class, both signals scored a human poem near 0.5, and the combined "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4039,
    "model_score": 0.054,
    "style_score": 0.5539,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "Those are the missing, empty, and enormous cases. A crash fails this. "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4461,
    "model_score": 0.2062,
    "style_score": 0.5489,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "I asked why the rice curl returned a huge HTML page. The page was a Fl"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3489,
    "model_score": 0.1545,
    "style_score": 0.4322,
    "label": "We think this was probably written by a person.",
    "sent": "EV01 came back unsure at 0.4992. The style score stays 0.6431 when the"
  }
]
```

**label coverage, trial 1**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.1391,
    "model_score": 0.0872,
    "style_score": 0.1613,
    "label": "We think this was probably written by a person.",
    "sent": "Huh. The saucepan seized, the grains carbonized along the rim, and I a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5452,
    "model_score": 0.0673,
    "style_score": 0.75,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "I burned the rice and ate cereal instead."
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6451,
    "model_score": 0.2337,
    "style_score": 0.8214,
    "label": "We think this was probably written by an AI.",
    "sent": "The system provides reliable results for users. The process supports c"
  }
]
```

**appeal path, trial 1**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2966,
    "model_score": 0.0603,
    "style_score": 0.3979,
    "label": "We think this was probably written by a person.",
    "sent": "I allow at most 1 false positive in 10 because on a writing site a wro",
    "content_id": "89f9d4ce-3b3e-4114-8768-ee05e771fbc8",
    "appeal_status": "under_review"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3699,
    "model_score": 0.1311,
    "style_score": 0.4722,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "In class, both signals scored a human poem near 0.5, and the combined ",
    "content_id": "6c8de2e2-0831-40b6-afa7-355a223486c3",
    "appeal_status": "under_review"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4639,
    "model_score": 0.1152,
    "style_score": 0.6133,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "If no input can reach a label, the ranges have a gap. Each guess has t",
    "content_id": "7488bd01-a556-4eef-afd5-a360aa8c0070",
    "appeal_status": "under_review"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.393,
    "model_score": 0.0696,
    "style_score": 0.5316,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "An appeal that leaves the status unchanged still shows the writer the ",
    "content_id": "8eecfa03-ec47-4feb-8e43-61c9b104b291",
    "appeal_status": "under_review"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4039,
    "model_score": 0.054,
    "style_score": 0.5539,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "Those are the missing, empty, and enormous cases. A crash fails this. ",
    "content_id": "d5db8614-1161-402c-b5a8-94a46607abf0",
    "appeal_status": "under_review"
  }
]
```

**appeal path, trial 1, from logs/audit.jsonl. audit.py log_appeal wrote these.**

```json
[
  {
    "timestamp": "2026-11-11T10:58:08+00:00",
    "content_id": "89f9d4ce-3b3e-4114-8768-ee05e771fbc8",
    "creator_id": "eval_appeal path_1",
    "event": "appeal",
    "status": "under_review",
    "reasoning": "I wrote this."
  },
  {
    "timestamp": "2026-11-11T10:58:09+00:00",
    "content_id": "6c8de2e2-0831-40b6-afa7-355a223486c3",
    "creator_id": "eval_appeal path_2",
    "event": "appeal",
    "status": "under_review",
    "reasoning": "I wrote this."
  },
  {
    "timestamp": "2026-11-11T10:58:09+00:00",
    "content_id": "7488bd01-a556-4eef-afd5-a360aa8c0070",
    "creator_id": "eval_appeal path_3",
    "event": "appeal",
    "status": "under_review",
    "reasoning": "I wrote this."
  },
  {
    "timestamp": "2026-11-11T10:58:09+00:00",
    "content_id": "8eecfa03-ec47-4feb-8e43-61c9b104b291",
    "creator_id": "eval_appeal path_4",
    "event": "appeal",
    "status": "under_review",
    "reasoning": "I wrote this."
  },
  {
    "timestamp": "2026-11-11T10:58:09+00:00",
    "content_id": "d5db8614-1161-402c-b5a8-94a46607abf0",
    "creator_id": "eval_appeal path_5",
    "event": "appeal",
    "status": "under_review",
    "reasoning": "I wrote this."
  }
]
```

**bad input, trial 1**

```json
[
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": null,
    "error": "JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
    "sent": "(empty text)"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9992,
    "model_score": 0.9975,
    "style_score": 1.0,
    "label": "We think this was probably written by an AI.",
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5452,
    "model_score": 0.0673,
    "style_score": 0.75,
    "label": "We can't tell whether a person wrote this or an AI did.",
    "sent": "I burned the rice and ate cereal instead."
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->
Criterion 1 held. Each of the 3 trials had 1 guess ai in 10, the combining-rule paragraph at 0.6077.

Criterion 2 held. Each of the 3 trials had a gap of 0.2576.

Criterion 3 held. Each of the 3 trials had guess human, unsure, and ai.

Criterion 4 held. Each of the 3 trials had 5 of 5 appeals at status under_review, with those content ids in the log.

Criterion 5 missed on all 3 trials. Each trial was null, null, ai, unsure. The missing field and the empty string are the route. detector.perplexity raises ValueError under 3 tokens, and the response is not JSON. The repeated word is signal two. style_signal is 1.0, and the 0.7 weight is already over 0.60. The normal sentence came back unsure.

EV01 came back unsure at 0.4992. The style score stays 0.6431 when the misspellings are fixed, because the sentence lengths sit in a narrow band. detector.model_signal returned 0.1635. Those spellings are hard for gpt2 to predict. combine_signals weights the model score at 0.3, and the weighted score stays under 0.60 unless that score is near 0.50. The stage is signal one.

EV02, EV03, EV06, EV07, and EV09 came back unsure. Broken-up sentences, a pasted quotation, one long sentence next to one short one, extra punctuation, and a human opening paragraph move style_signal down. combine_signals weights that score at 0.7, so the sum stays under 0.60. The stage is signal two.

EV05 came back unsure at 0.3508. model_signal was 0.3212 and style_signal was 0.3635, and the weighted sum stays under 0.60. The stage is signal one and signal two.

EV08 came back unsure at 0.4996. The text is under the token window, so model_signal is 0.2452 against style_signal 0.6086. At a 0.3 weight the combined score stays under 0.60. The stage is signal one.

FP02, FP03, FP04, FP05, and FP06 came back guess ai. The highest style score is 0.6857, and 0.7 times 0.6857 is 0.480, under 0.60. model_signal clears the line. The stage is signal one, because this formal and technical prose is predictable to gpt2.

PI02 came back guess human at 0.3271, from model_signal 0.2044 and style_signal 0.3797. score_to_label returns human at or under 0.35. The stage is the label mapping.

MF02, RQ01, RQ03, RQ04, RQ05, RQ07, RQ08, RQ09, RQ10, RQ11, and RQ12 came back status 500. The stage is the route. submit sends the body to detector.model_signal with no check. On MF02 the traceback was ValueError in detector.perplexity, "Text is too short to score".

MF01, MF04, MF06, and MF07 came back guess ai with style_score 1.0. The 0.7 weight on that is 0.70, over 0.60. Whitespace, punctuation, emoji, and right-to-left text leave few words and no sentence-length spread. The stage is signal two. MF01's model_score was 0.2053.

MF05 and MF08 came back guess ai. The style share is 0.525 and 0.532, under 0.60. model_signal was 0.9976 and 0.9876. A long repeated string is easy for gpt2 to predict. The stage is signal one.

FL01_01 through FL01_07 came back status 200. RATE_LIMIT_PER_MINUTE is 7, so the first 7 submissions from one creator are accepted. The stage is the route.


---

## The Improvement

**What I changed:**
submit checks the text before either score. If the text is not a string, is under 10 characters once stripped, or is over 10000 characters, the response is status 400 and has no guess.

**Which diagnosis pointed at it:**
Criterion 5 missed because a missing field and an empty string crashed in the route. MF02 and 10 other rows came back status 500 from that same call.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

Held: 31. Broke: 25.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `820bb89d-120b-45cf-b142-3705b5f7481f` | unsure | 0.499 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `402a1b06-ff0f-4f7e-95b6-29541a98b6d3` | unsure | 0.398 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `3efa0e50-5261-4676-9bd2-72709a41cb9e` | unsure | 0.548 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `52281113-6895-4f40-9422-1c338bcf205b` | ai | 0.619 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `6c2de394-6a5e-4254-8d14-78b75e7f6be6` | unsure | 0.351 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `e916765c-60d2-4dec-819f-a47d8a1060c9` | unsure | 0.362 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `49a9fb5e-ed24-47d0-a20a-3931b930afe9` | unsure | 0.566 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `6f58ebef-d1b9-41aa-8f32-690eeaf5b615` | unsure | 0.500 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b23fc639-6978-4b8b-a342-97c9abb79514` | unsure | 0.552 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `4f099cc0-8d3f-4f06-b4f7-fee89aae09e2` | ai | 0.800 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `8fbad5e9-7672-457f-a37f-627b315acd6f` | unsure | 0.584 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `565e237e-7c7b-419c-85fa-9dd44d47eec4` | ai | 0.702 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `f056d0b7-6dcc-448d-a970-16c33910c4db` | ai | 0.700 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `62e63310-ba6c-491b-b7d6-c35404ed4a07` | ai | 0.667 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `1f6135d2-8659-4509-8bb7-ba48b2ee58a6` | ai | 0.716 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `ee8df635-4c02-4fd0-835a-4f19b87150c5` | ai | 0.640 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `0366d319-f47a-4cac-ba65-7d655434f270` | unsure | 0.599 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `12103ee5-1b2a-4036-98cb-49e1a5ce58b9` | unsure | 0.470 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `d66fe10a-6c54-492e-847d-6e97858f0872` | unsure | 0.444 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c304a864-0616-470e-8da2-8cf8327671de` | human | 0.327 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `82cf8b47-1063-4140-98a6-94fa2ecdeebf` | unsure | 0.583 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `acb97f29-ac99-4588-b329-e8a879c6f3c9` | unsure | 0.526 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `20a00bb2-eeb5-48ff-918f-33e35565a42e` | unsure | 0.383 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `68d560c0-07e3-41c9-b6b1-2e3ff9af4571` | unsure | 0.572 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `89d3d5b8-54a1-4cc3-89d6-7670801c812e` | unsure | 0.525 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `ab39a020-9d2d-4d35-9758-7277310c580c` | ai | 0.703 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `03f9835e-543c-42d7-83f9-a71cfd596638` | ai | 0.824 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `f4300c44-ff9d-47a1-bfc7-101254521e46` | ai | 0.999 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `ce64f28f-0bdb-42f3-a693-ccce41a543d5` | ai | 0.972 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `9e48ae5a-7d91-44dd-883b-b43a4eb85532` | unsure | 0.597 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `d3095813-0fd5-40df-ab3f-5f6538cb4e1c` | unsure | 0.540 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `eb420404-9787-423c-8579-15eb12e151e8` | unsure | 0.534 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7c1129ff-370c-4223-afbc-7ef7a8c43519` | unsure | 0.534 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `54508c1b-684c-4930-bcfd-bb20c373af2c` | unsure | 0.534 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e1061010-c689-456e-b409-aab2a88884ef` | unsure | 0.534 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b15f75f0-b82a-4207-a4f9-2526c9a382b7` | unsure | 0.534 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `81798396-2009-4890-b8cd-6b8f2b2b8fdb` | unsure | 0.534 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dd623baf-0fc2-4f8c-9120-9d745337929b` | unsure | 0.534 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

**Did it help, and how do I know:**
The 11 rows that came back status 500, plus MF01 and MF08, now come back 400 with no guess. Held is 31 and broke is 25. The before run was 18 held and 38 broke. Evasion, the false positives, PI02, and the first 7 flood rows are the same. Criterion 5 is 400, 400, 400, unsure on all 3 trials. Criteria 1 through 4 matched the before run. MF04, MF05, MF06, and MF07 still come back guess ai.

| Criterion | Before | After |
|---|---|---|
| 1. False positives | MET, 1 of 10 | MET, 1 of 10 |
| 2. Score spread | MET, 0.2576 | MET, 0.2576 |
| 3. Label coverage | MET | MET |
| 4. Appeal path | MET, 5 of 5 | MET, 5 of 5 |
| 5. Bad input | MISSED, null, null, ai, unsure | MET, 400, 400, 400, unsure |



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

No criterion missed on the after run. All 5 held.

EV01, EV02, EV03, EV05, EV06, EV07, EV08, and EV09 still come back unsure. Raising the model weight catches EV03 at model score 0.6662. EV01 stays under 0.60 because its model score is 0.1635. I would add a check for the sentence shape. I stopped because the one change was the input check.

FP02, FP03, FP04, FP05, and FP06 still come back guess ai. FP05 is the highest at 0.7157. I would move the ai line above 0.72. I left that move because EV04 at 0.619 would come back unsure, and it is a second change.

PI02 still comes back human at 0.3271. I would move the human line under 0.3271. I left the human line where it is.

MF04, MF06, and MF07 still come back guess ai. I would refuse text with no words, which is what leaves style_score at 1.0. The length check was the change I made.

MF05 still comes back guess ai at 0.8243. model_score is 0.9976, and the text is one long word under the 10000-character cap. I would refuse a single repeated word. I left the cap at 10000.

FL01_01 through FL01_07 still come back status 200. I would drop the minute limit under 7. I left it at 7 because a writer submitting a few times an hour was the reason for that number. FL01_08 already returns 429.

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

I'd move the ai line above 0.72, so FP02 through FP06 would stop coming back guess ai. The readers pay, because EV04 at 0.619 would come back unsure.

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
