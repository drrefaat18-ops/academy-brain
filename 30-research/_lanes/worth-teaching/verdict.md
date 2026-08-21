---
cluster: worth-teaching
provider: claude
status: complete
question: >-
  Is micro:bit Level 1 worth teaching as-is, judged against the PictoBlox 2D ADV
  Level 1 that Techno Square Academy already ships?
evidence:
  - evidince/actual slide deck and trainer guides/PICTOBLOX-2D-ADV-L1-Trainer-Guide-v1.0.pdf (56 pages)
  - 10-digest/L1-s1.md .. L1-s6.md
  - 70-localized/L1-s1.md .. L1-s6.md
---

# Verdict — micro:bit L1 vs the academy's shipped PictoBlox L1

> **SUPERSEDED IN PART (owner ruling, same day).** The academy's level shape is
> s1–s6 teaching, s7 revision, s8 graduation project with no artifacts. The
> 6 teaching sessions are therefore CORRECT, not a gap. The "expand to 8
> sessions" recommendation below is withdrawn; only s7 needs authoring, and s8
> needs nothing. The session-length, assessment, capstone and rubric findings
> still stand and are unaffected.

## Short answer

**The content is worth teaching. The current packaging is not shippable.**

The concepts are sound and sequence correctly. But micro:bit L1 as scoped is
roughly **half the course** the academy sells, and it is missing the two things
the academy uses to prove learning happened. Ship it as-is and trainers will
notice immediately, because it breaks the shape they already teach.

## The academy standard, from its own trainer guide

| Dimension | PictoBlox 2D ADV L1 (shipped) | micro:bit L1 (ours) | Gap |
| --- | --- | --- | --- |
| Teaching sessions | 6 (of 8) | 6 | **none — matches ruling** |
| Session length | **120 min** | 60 min (upstream default) | −50% |
| Total contact time | **16 h** | 6 h | **−62%** |
| Age band | **11–13** | ~8–11 (upstream micro:bit) | mismatch |
| Review/Debugging session | **Session 7** | none | missing |
| Practical assessment | **Session 8** | none | missing |
| Weighted rubric | **7 criteria, pass ≥60%** | none | missing |
| Capstone project | **final playable game** | none | missing |
| Exit ticket per session | **required** | none | missing |
| Block-reference appendix | **Appendix A** | none | missing |
| Preflight checklist | **Appendix C** | none | missing |
| File-naming convention | **enforced** | not applied | missing |

Source: `PICTOBLOX-2D-ADV-L1-Trainer-Guide-v1.0.pdf` pp. 2–3, 54–56.

## What is genuinely fine

The **concept progression is legitimate and maps cleanly onto what PictoBlox L1
already teaches** — the same CS ideas, different hardware:

| micro:bit L1 | Concept | PictoBlox L1 equivalent |
| --- | --- | --- |
| S1 Name Badge | output, sequence | S1 Events, Motion |
| S2 Animation | loops, sequencing | S2 Costumes, Looks |
| S3 Emotion Badge | input, abstraction | S2–S3 events + state |
| S4 Step Counter | variables, sensors | S4 Lives, Score variables |
| S5 Nightlight | conditionals, logic | S3 Collision, If |
| S6 Rock/Paper/Scissors | random, compound logic | S6 AND/OR, Score, Timer |

Every concept the academy considers core to L1 appears somewhere in micro:bit L1.
Nothing is pedagogically wrong. A student finishing micro:bit L1 has met
sequence, iteration, selection, variables, sensors and randomness — a defensible
Level 1 in any curriculum.

**It also adds something PictoBlox cannot:** physical hardware. Real sensors,
a real device that runs untethered on a battery. That is a genuine differentiator
for a hardware track, not a substitute product.

## Why it is not shippable as-is

1. **Contact time.** 6 h vs 16 h. If the academy sells "Level 1" as a fixed
   product at a fixed price, this is a different product wearing the same label.
   Each micro:bit session needs roughly **double** its current content to fill a
   120-minute slot.

2. **No assessment.** The academy's L1 ends in a graded practical with a weighted
   rubric and explicit pass conditions (≥60%, playable artifact, student explains
   it unaided, debugging evidence shown). micro:bit L1 currently ends with
   "next time we'll make an animation." There is no moment where anyone
   establishes the student learned anything.

3. **No capstone.** PictoBlox L1 builds toward one final playable game the
   student designed. micro:bit L1 is six disconnected mini-projects. Nothing
   accumulates. This is the single biggest experiential difference a student
   would feel.

4. **No review/debugging session.** The academy dedicates a whole session to it,
   and its teaching framework is explicitly
   `Think → Build → Test → Debug → Explain`. Debugging is a named academy value.
   micro:bit L1 treats errors as trainer footnotes.

5. **Age band.** Academy L1 is 11–13. The micro:bit upstream material targets
   younger. Either the material moves up in complexity, or this is positioned as
   a *different, younger* track — which is a business decision, not a content one.

## Recommendation

**Teach it — after restructuring to 8 sessions.** Do not ship 6.

| # | Session | Status |
| --- | --- | --- |
| 1–6 | Existing content, each expanded to fill 120 min | needs ~2× depth |
| 7 | **Review & Debugging Lab** | must be written |
| 8 | **Practical Assessment** — student builds and explains their own micro:bit project | must be written |

Plus, to match academy standard: an L1 assessment rubric (mirror the 7-criterion
weighting), an exit ticket per session, a block-reference appendix, a preflight
checklist, and the file-naming convention.

**This is already anticipated by the vault** — `scripts/swarm/paths.py` defines
session IDs through `L1-s7`, and you told me the summary deck for session 7 is
2 slides rather than 3. The 7–8 session shape is the house standard; micro:bit L1
was scoped to the upstream micro:bit lesson count instead.

## Where each expansion hour should go

Rather than padding, use the 60 extra minutes per session on what the academy's
own teaching framework demands and the upstream micro:bit deck omits:

- **Predict-before-run** on every build step (already partly done in L1-s1)
- **Test after every mechanic**, not once at the end
- **Student explains their code** — the academy's stated primary evidence of
  learning, weighted above a working project
- **Deliberate debugging**: break the code on purpose, have students fix it
- **Extension challenges** for fast finishers (the academy's age-adaptation rule)
- **Exit ticket** in the closing 5 minutes

## Confidence and limits

- **High confidence** on the structural comparison — it is read directly from the
  academy's own trainer guide, not inferred.
- **Medium confidence** on the age-band claim. PictoBlox L1 states 11–13
  explicitly; the micro:bit target age is inferred from upstream material and
  was not stated in any vault document. **Confirm with the academy.**
- **Not assessed:** whether 120-minute sessions are viable with micro:bit
  hardware logistics (device handout, flashing time, battery management). That is
  an operational question for someone who has run a hardware lab.
