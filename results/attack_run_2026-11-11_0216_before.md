# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 02:16
- Auto-marked BROKE (5xx, crash, no response): **11**
- Left for you to judge: **45**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `b9a5c9a7-aa74-45af-96b4-d54889098838` | unsure | 0.499 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `faaf9784-7a82-44ac-8674-08aedf0835af` | unsure | 0.398 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `3bc2a974-0b8b-4122-bb13-7efe88c18c70` | unsure | 0.548 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `e932e02a-1dad-4a68-ae93-23e575d28b76` | ai | 0.619 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `3957a859-bba0-44f5-ba9d-ebe8253de5c4` | unsure | 0.351 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0a111753-30da-476e-a6cc-3e43663abaef` | unsure | 0.362 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `cc5cef67-a44f-4445-a8cb-47904d3457b2` | unsure | 0.566 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `4d5aae24-17f1-4274-afd3-71fd345c7618` | unsure | 0.500 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `60f8cf34-c44d-4fea-ad1d-99c2052d31da` | unsure | 0.552 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `ee6803dd-b9d8-438a-a8f1-356f033bb146` | ai | 0.800 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `5459d99d-c4dc-473c-9309-63b7d5f45902` | unsure | 0.584 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `4a6ea2ef-e530-4936-b218-b33d63a72c00` | ai | 0.702 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `7ffa5a45-53a8-488f-99e9-636a3b9825d0` | ai | 0.700 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `2defc968-4f43-4cc6-91c9-a2183f44c82f` | ai | 0.667 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `7fcd7745-7b71-42d1-b65f-c5731213fe7b` | ai | 0.716 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `fe18c8ca-0d50-4afd-a1f3-d208374a4f8e` | ai | 0.640 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f79eef43-dc69-475d-8475-7eef01f81aac` | unsure | 0.599 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `4580b441-b9b0-4161-b889-2ecfd4fe0b32` | unsure | 0.470 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `9a361588-05cf-4dc1-897a-27807b494ccc` | unsure | 0.444 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `e25cc24c-98e0-440f-9c2c-0509138388ca` | human | 0.327 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `a80368dc-0b0e-4f8d-97e0-60eb7071da9d` | unsure | 0.583 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `8af72e1d-cf45-4fd1-9105-a6b2e39da7c9` | unsure | 0.526 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `80ca8569-73fc-4e27-a20b-890a8d8196f2` | unsure | 0.383 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `a8c2eace-57e3-4f98-ad36-484811c41491` | unsure | 0.572 |  |
| MF01 | malformed | text is only whitespace | 200 | `f84cfce4-535f-4837-b8c3-913653a11468` | ai | 0.762 |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `61cbcafc-542f-4c9b-ab27-0d8f2fb1fd12` | unsure | 0.525 |  |
| MF04 | malformed | text is only punctuation | 200 | `e0b5bb39-a351-409c-af52-82ae1bf7fe9f` | ai | 0.703 |  |
| MF05 | malformed | text is a very long single word | 200 | `d9375e0a-aa9b-4923-a29b-6c25320cc2e0` | ai | 0.824 |  |
| MF06 | malformed | text is emoji only | 200 | `2deebc12-82ea-48d9-8156-769f5195cfc8` | ai | 0.999 |  |
| MF07 | malformed | text is right-to-left script | 200 | `a21aadfa-d484-42fa-9c25-829520c5f43d` | ai | 0.972 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `43c4d2a3-5427-4a9e-a4fb-8c197e9a34f5` | ai | 0.828 |  |
| RQ01 | malformed | no text field at all | 500 | `—` | — | — | BROKE |
| RQ02 | malformed | no creator_id | 200 | `22b164e1-8346-4f90-b4a9-3999e35e940c` | unsure | 0.597 |  |
| RQ03 | malformed | text is a number | 500 | `—` | — | — | BROKE |
| RQ04 | malformed | text is a list | 500 | `—` | — | — | BROKE |
| RQ05 | malformed | text is null | 500 | `—` | — | — | BROKE |
| RQ06 | malformed | creator_id is an object | 200 | `bd122377-fb72-4af2-8d97-1907b105e3b9` | unsure | 0.540 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 500 | `—` | — | — | BROKE |
| RQ09 | malformed | body is empty | 500 | `—` | — | — | BROKE |
| RQ10 | malformed | body is form-encoded, not JSON | 500 | `—` | — | — | BROKE |
| RQ11 | malformed | body is JSON claiming to be plain text | 500 | `—` | — | — | BROKE |
| RQ12 | malformed | deeply nested JSON | 500 | `—` | — | — | BROKE |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0f56c5e5-9aa8-4bb9-9713-821d2b0456b7` | unsure | 0.534 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4c21483b-711a-4cd1-bdac-6abd2a85a085` | unsure | 0.534 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `115b6bed-9a90-42dd-868f-85a4f7921df0` | unsure | 0.534 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cc15680f-9867-4b61-aa4e-60c77f4028e2` | unsure | 0.534 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6b56f817-4458-4f9c-9cc0-48503708dc16` | unsure | 0.534 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3d54a2db-f339-4ba0-8a34-f0facf90541a` | unsure | 0.534 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5efc748d-7cdc-416c-b724-8756d45cf318` | unsure | 0.534 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

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
  "content_id": "b9a5c9a7-aa74-45af-96b4-d54889098838",
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
  "content_id": "faaf9784-7a82-44ac-8674-08aedf0835af",
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
  "content_id": "3bc2a974-0b8b-4122-bb13-7efe88c18c70",
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
  "content_id": "e932e02a-1dad-4a68-ae93-23e575d28b76",
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
  "content_id": "3957a859-bba0-44f5-ba9d-ebe8253de5c4",
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
  "content_id": "0a111753-30da-476e-a6cc-3e43663abaef",
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
  "content_id": "cc5cef67-a44f-4445-a8cb-47904d3457b2",
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
  "content_id": "4d5aae24-17f1-4274-afd3-71fd345c7618",
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
  "content_id": "60f8cf34-c44d-4fea-ad1d-99c2052d31da",
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
  "content_id": "ee6803dd-b9d8-438a-a8f1-356f033bb146",
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
  "content_id": "5459d99d-c4dc-473c-9309-63b7d5f45902",
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
  "content_id": "4a6ea2ef-e530-4936-b218-b33d63a72c00",
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
  "content_id": "7ffa5a45-53a8-488f-99e9-636a3b9825d0",
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
  "content_id": "2defc968-4f43-4cc6-91c9-a2183f44c82f",
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
  "content_id": "7fcd7745-7b71-42d1-b65f-c5731213fe7b",
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
  "content_id": "fe18c8ca-0d50-4afd-a1f3-d208374a4f8e",
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
  "content_id": "f79eef43-dc69-475d-8475-7eef01f81aac",
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
  "content_id": "4580b441-b9b0-4161-b889-2ecfd4fe0b32",
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
  "content_id": "9a361588-05cf-4dc1-897a-27807b494ccc",
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
  "content_id": "e25cc24c-98e0-440f-9c2c-0509138388ca",
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
  "content_id": "a80368dc-0b0e-4f8d-97e0-60eb7071da9d",
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
  "content_id": "8af72e1d-cf45-4fd1-9105-a6b2e39da7c9",
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
  "content_id": "80ca8569-73fc-4e27-a20b-890a8d8196f2",
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
  "content_id": "a8c2eace-57e3-4f98-ad36-484811c41491",
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
  "content_id": "f84cfce4-535f-4837-b8c3-913653a11468",
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
  "content_id": "61cbcafc-542f-4c9b-ab27-0d8f2fb1fd12",
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
  "content_id": "e0b5bb39-a351-409c-af52-82ae1bf7fe9f",
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
  "content_id": "d9375e0a-aa9b-4923-a29b-6c25320cc2e0",
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
  "content_id": "2deebc12-82ea-48d9-8156-769f5195cfc8",
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
  "content_id": "a21aadfa-d484-42fa-9c25-829520c5f43d",
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
  "content_id": "43c4d2a3-5427-4a9e-a4fb-8c197e9a34f5",
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
  "content_id": "22b164e1-8346-4f90-b4a9-3999e35e940c",
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
  "content_id": "bd122377-fb72-4af2-8d97-1907b105e3b9",
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
  "content_id": "0f56c5e5-9aa8-4bb9-9713-821d2b0456b7",
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
  "content_id": "4c21483b-711a-4cd1-bdac-6abd2a85a085",
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
  "content_id": "115b6bed-9a90-42dd-868f-85a4f7921df0",
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
  "content_id": "cc15680f-9867-4b61-aa4e-60c77f4028e2",
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
  "content_id": "6b56f817-4458-4f9c-9cc0-48503708dc16",
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
  "content_id": "3d54a2db-f339-4ba0-8a34-f0facf90541a",
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
  "content_id": "5efc748d-7cdc-416c-b724-8756d45cf318",
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
