"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # Ten pieces from criteria.md and the README.
        "texts": [
            "I allow at most 1 false positive in 10 because on a writing site a wrong accusation costs more than a missed detection. A trial with 2 misses still fails.",
            "In class, both signals scored a human poem near 0.5, and the combined score was near 0.5 too. I want 0.25 between those averages. The human average can still sit high, because my Milestone 1 trace has ordinary sentences at 0.71.",
            "If no input can reach a label, the ranges have a gap. Each guess has to show up once a trial.",
            "An appeal that leaves the status unchanged still shows the writer the original accusation. The log entry is the record. I am counting 5 of 5.",
            "Those are the missing, empty, and enormous cases. A crash fails this. A guess on empty text fails it too. The normal sentence shows the service is still answering.",
            "The combined score is 0.3 times the model score plus 0.7 times the style score. On the even AI paragraph the model score was 0.2337 and the style score was 0.8214, so the style score is the one that separates that paragraph from the human one.",
            "I burned the rice and ate cereal instead. The model score is 0.0673 and the style score is 0.75. The combined score is 0.5452.",
            "I asked why the rice curl returned a huge HTML page. The page was a Flask error. The bottom line was NameError: name 'detector' is not defined, on the model_signal call in app.py. The import detector line was missing. I added import detector inside submit, above the model_signal call. The next rice curl returned JSON, and model_score was 0.0673.",
            'FP05 is the one I would least want to explain to the person who wrote it. The target was technical documentation written by a person. The service returned guess ai, model_score 0.8005, style_score 0.6794, and combined score 0.7157. The label was "We think this was probably written by an AI." The input starts "To configure the service, edit the settings file in the installation directory."',
            "EV01 came back unsure at 0.4992. The style score stays 0.6431 when the misspellings are fixed, because the sentence lengths sit in a narrow band. detector.model_signal returned 0.1635. Those spellings are hard for gpt2 to predict. combine_signals weights the model score at 0.3, and the weighted score stays under 0.60 unless that score is near 0.50. The stage is signal one.",
        ],
    },
    {
        "name": "score spread",
        "criterion": 2,
        # Five even paragraphs listed as model-written, then five of mine.
        "texts": [
            "The system provides reliable results for users. The process supports clear results for teams. The design offers stable results for clients.",
            "The report presents clear findings for readers. The method supports stable findings for reviewers. The section offers useful findings for partners.",
            "The tool delivers consistent output for staff. The workflow maintains consistent output for managers. The update provides consistent output for clients.",
            "The model produces accurate scores for texts. The service returns accurate scores for users. The page shows accurate scores for writers.",
            "The check gives direct answers for authors. The log stores direct answers for appeals. The form sends direct answers for reviews.",
            "I allow at most 1 false positive in 10 because on a writing site a wrong accusation costs more than a missed detection. A trial with 2 misses still fails.",
            "In class, both signals scored a human poem near 0.5, and the combined score was near 0.5 too. I want 0.25 between those averages. The human average can still sit high, because my Milestone 1 trace has ordinary sentences at 0.71.",
            "Those are the missing, empty, and enormous cases. A crash fails this. A guess on empty text fails it too. The normal sentence shows the service is still answering.",
            "I asked why the rice curl returned a huge HTML page. The page was a Flask error. The bottom line was NameError: name 'detector' is not defined, on the model_signal call in app.py. The import detector line was missing. I added import detector inside submit, above the model_signal call. The next rice curl returned JSON, and model_score was 0.0673.",
            "EV01 came back unsure at 0.4992. The style score stays 0.6431 when the misspellings are fixed, because the sentence lengths sit in a narrow band. detector.model_signal returned 0.1635. Those spellings are hard for gpt2 to predict. combine_signals weights the model score at 0.3, and the weighted score stays under 0.60 unless that score is near 0.50. The stage is signal one.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # One input in each band. human, then unsure, then ai.
        "texts": [
            "Huh. The saucepan seized, the grains carbonized along the rim, and I ate the stale cereal instead of scraping that blackened pot again, since the market had already locked its gate.",
            "I burned the rice and ate cereal instead.",
            "The system provides reliable results for users. The process supports clear results for teams. The design offers stable results for clients.",
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        # run_eval.py posts /appeal after each submit when appeal is True.
        "appeal": True,
        "texts": [
            "I allow at most 1 false positive in 10 because on a writing site a wrong accusation costs more than a missed detection. A trial with 2 misses still fails.",
            "In class, both signals scored a human poem near 0.5, and the combined score was near 0.5 too. I want 0.25 between those averages. The human average can still sit high, because my Milestone 1 trace has ordinary sentences at 0.71.",
            "If no input can reach a label, the ranges have a gap. Each guess has to show up once a trial.",
            "An appeal that leaves the status unchanged still shows the writer the original accusation. The log entry is the record. I am counting 5 of 5.",
            "Those are the missing, empty, and enormous cases. A crash fails this. A guess on empty text fails it too. The normal sentence shows the service is still answering.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        # Missing field, empty text, enormous text, then one normal sentence.
        "bodies": [
            {"creator_id": "eval_bad_missing"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
            {"text": "I burned the rice and ate cereal instead.", "creator_id": "eval_bad_ok"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
