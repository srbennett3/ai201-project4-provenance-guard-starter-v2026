# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 02:17
- Auto-marked BROKE (5xx, crash, no response): **11**
- Held: 18
- Broke: 38
- Left for you to judge: **45**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

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

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 11 | 9 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "8cb9a7d0-4965-401c-ae9a-a703e0d5eaa5",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4992,
  "model_score": 0.1635,
  "style_score": 0.6431,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "a4717e92-daa1-4bc5-98a4-7bba4da8ed44",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3984,
  "model_score": 0.5943,
  "style_score": 0.3144,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "4dc85794-5d75-4c2b-8ad9-679685af59c8",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5483,
  "model_score": 0.6662,
  "style_score": 0.4977,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "de8db803-bbb4-4057-b7a7-0927f248055e",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.619,
  "model_score": 0.6114,
  "style_score": 0.6223,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "b972bcf7-37be-4fec-ab88-57e7d6ac63fb",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.3508,
  "model_score": 0.3212,
  "style_score": 0.3635,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "bdfddc1d-8d67-40d4-abee-cf44d9e14830",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.362,
  "model_score": 0.5727,
  "style_score": 0.2717,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "668cc875-d49d-4983-b9f7-f9bc9bb92ee1",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5655,
  "model_score": 0.5862,
  "style_score": 0.5567,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "6cb4d54b-9087-4d5e-b7c5-90649d28c870",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4996,
  "model_score": 0.2452,
  "style_score": 0.6086,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "8aae8685-8f2a-4fda-b718-4db508906355",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5521,
  "model_score": 0.7042,
  "style_score": 0.4869,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "cb4c5e94-0172-4c94-bda9-fddd7552506f",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7998,
  "model_score": 0.9792,
  "style_score": 0.7229,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "d7fa8bb7-5731-4822-a7de-ddb80a601633",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5841,
  "model_score": 0.6175,
  "style_score": 0.5698,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "cbae475b-f9ba-4b11-9c3d-3fee9660122d",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7016,
  "model_score": 0.7387,
  "style_score": 0.6857,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "a8e5beb8-9de9-4cee-85e9-bf44eacffbe5",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7002,
  "model_score": 0.8051,
  "style_score": 0.6552,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "15229190-e552-4463-8f1d-38698c21a478",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6671,
  "model_score": 0.8329,
  "style_score": 0.5961,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "2d32c4ed-9c12-43cc-bb42-723b425ed1bd",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7157,
  "model_score": 0.8005,
  "style_score": 0.6794,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "eea5b8c2-f713-4d66-80ec-98befc4cbab4",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6405,
  "model_score": 0.8814,
  "style_score": 0.5373,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "7d9b2dfa-0454-4ca3-a6d2-3c55b2121507",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5989,
  "model_score": 0.8816,
  "style_score": 0.4778,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "27d420bc-9469-4e05-abd7-661a582a3726",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4701,
  "model_score": 0.3223,
  "style_score": 0.5335,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "386afa58-322a-4fff-8f17-f54eb4780636",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4435,
  "model_score": 0.4625,
  "style_score": 0.4353,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "8d82395d-dbee-4136-b494-9ec8f33c3137",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.3271,
  "model_score": 0.2044,
  "style_score": 0.3797,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "8ea5d68c-1a89-42c3-a4ce-942b69c50a12",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5832,
  "model_score": 0.5943,
  "style_score": 0.5784,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "8ff5fc06-2311-426e-b349-080a0b690cba",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5258,
  "model_score": 0.4998,
  "style_score": 0.537,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "b93385ac-2479-4f48-b246-a8a65845626f",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.3829,
  "model_score": 0.6401,
  "style_score": 0.2726,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "9b181b9a-827d-4ac8-b556-d746d38ff66e",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5722,
  "model_score": 0.5583,
  "style_score": 0.5782,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 200,
  "content_id": "00b82683-29cf-4e3b-bcaa-2417d489940c",
  "creator_id": "attacker_MF01",
  "guess": "ai",
  "confidence": 0.7616,
  "model_score": 0.2053,
  "style_score": 1.0,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "cf7b9bdc-40a5-431b-89f7-ced99da7f470",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.525,
  "model_score": 0.0,
  "style_score": 0.75,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "9175e8f2-18fe-45bc-ae8a-da2ca37f7e88",
  "creator_id": "attacker_MF04",
  "guess": "ai",
  "confidence": 0.7034,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "54487ff2-a7ed-400b-93f1-262b569ceb8b",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8243,
  "model_score": 0.9976,
  "style_score": 0.75,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "3f92c1ae-374b-4015-8df3-097f9f016e80",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9991,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "a66fad20-d66a-4e53-b8fd-c2114e8407fe",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9719,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "1461ce5b-ba19-4d84-9386-545f7be34a13",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.8283,
  "model_score": 0.9876,
  "style_score": 0.7601,
  "label": "We think this was probably written by an AI.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "312428a8-5839-426f-b0f3-26391335569e",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.5968,
  "model_score": 0.2395,
  "style_score": 0.75,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: text input must be of type `str` (single example), `list[str]` (batch or single pretokenized example) or `list[list[str]]` (batch of pret",
  "verdict": "BROKE"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: You need to specify either `text` or `text_target`.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&amp;",
  "verdict": "BROKE"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "e09bc3fb-ef85-4f59-bd09-af29448686c2",
  "creator_id": {
    "id": "x"
  },
  "guess": "unsure",
  "confidence": 0.5398,
  "model_score": 0.0492,
  "style_score": 0.75,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: text input must be of type `str` (single example), `list[str]` (batch or single pretokenized example) or `list[list[str]]` (batch of pret",
  "verdict": "BROKE"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "98856b5b-f895-4d1d-b4a0-7f60905d7a5a",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5336,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "151c6b6c-ea6f-4ccd-98cf-1990bbeb7f07",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5336,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "c36b324b-f8fa-41dc-936f-416730790d25",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5336,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "b265d443-e713-4ea9-b6e8-5c2854fb6740",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5336,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "71d8acd8-b467-491c-a1b1-e47474f23d0b",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5336,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "f1fdc370-f74b-4bda-af5a-7f259b0ae4b6",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5336,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "d41dc83d-6b91-498f-bebc-2145c243665b",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5336,
  "model_score": 0.0287,
  "style_score": 0.75,
  "label": "We can't tell whether a person wrote this or an AI did.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
