# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

Of 10 pieces I wrote myself, at most 1 has guess ai on each of 3 trials.


**Why this target:** 
I allow at most 1 false positive in 10 because on a writing site a wrong accusation costs more than a missed detection. A trial with 2 misses still fails.



---

## 2.

On each of 3 trials, the average combined score of 5 pieces listed as model-written is at least 0.25 above the average combined score of 5 pieces listed as mine.




**Why this target:** 
In class, both signals scored a human poem near 0.5, and the combined score was near 0.5 too. I want 0.25 between those averages. The human average can still sit high, because my Milestone 1 trace has ordinary sentences at 0.71.




---

## 3.

On each of 3 trials, POST /submit responses include at least 1 guess human, at least 1 guess unsure, and at least 1 guess ai.



**Why this target:**
If no input can reach a label, the ranges have a gap. Each guess has to show up once a trial.



---

## 4.

I submit 5 pieces, then send POST /appeal for each content_id that comes back. All 5 responses have status under_review. The log then has 5 entries whose event is appeal, with those content_ids and status under_review.



**Why this target:**
An appeal that leaves the status unchanged still shows the writer the original accusation. The log entry is the record. I am counting 5 of 5.



---

## 5.

Each trial sends 3 bad bodies to POST /submit. One has no text field. One has text set to "". One has the word "word" repeated 50000 times. Each of those responses has no guess field. One normal sentence, sent right after, still comes back with guess set to human, unsure, or ai.


**Why this target:**
Those are the missing, empty, and enormous cases. A crash fails this. A guess on empty text fails it too. The normal sentence shows the service is still answering.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
