---
id: L1-s1
stage: bundle
type: educational-decision-note
owner: claude
status: ready
contract: 00-contracts/brand-and-output.md
---

# Educational Decision Note — L1-s1: Name Badge

NBLM source #3. Tells the generator *why* the session is shaped this way, so it
does not "helpfully" restore what was deliberately removed.

## Course output strategy

- **Track:** Kids hardware
- **Delivery:** in-person, trainer-led, one micro:bit per student
- **Teaching style:** interactive — build, predict, test. Not lecture, not video.
- **Language:** 30% English / 70% Egyptian-colloquial Arabic, RTL-correct
- **Session length:** 120 minutes (Techno Square standard, all courses)
- **Artifacts:** Student Slide Deck (NBLM, 23 slides, two passes), Student Summary deck
  (NBLM, 3 slides), Trainer Guide (Antigravity, one PDF for the whole level)

## Decisions binding on this session

1. **No passive video slides.** The upstream micro:bit deck was video-first.
   The academy is not. Five video/link-only slides were converted into hands-on
   beats. Video URLs survive only in the Trainer Guide as optional trainer prep.
   *Do not reinstate video slides.*

2. **Screen-free opener.** The "computers in disguise" slide runs with devices closed. It is the concrete
   anchor for the whole level — "computers are inside ordinary things" — and
   students who miss it struggle in the sensor sessions (S4–S6).

3. **Predict before reveal.** The "اتوقع الأول" slide asks what the code will do before it runs.
   Prediction beats demonstration for retention at this age.

4. **Chunked build, four checkable steps.** The build is split across two slides plus a
   separate download-to-hardware slide, so the trainer can verify the class at each
   step instead of losing half of them.

5. **Canonical code is `forever` + `show string`.** Verified against the official
   MakeCode Name Tag project. Do not "correct" it to `on start`.

6. **Differentiation is two-tier and optional.** Every student must reach the
   basic working badge — that is the floor, not the target. Support tier =
   step-by-step tutorial. Stretch tier = extra text or `show icon`.

7. **Observable success criterion, not open questions.** The "جرّب واتأكد" slide states what
   "done" looks like: the student's own name scrolling, and the student able to
   point at the block that scrolls it.

## Hard exclusions from student slides

No trainer timings. No trainer scripts. No assessment checklists. No classroom
management notes. No long pedagogical explanations. These live in the Trainer
Guide, which is internal-use only.

## TATA usage

Intentional only, per the four documented states. Not on every slide. See
`Tata_Mascot_Usage Guide.md`.

## Interaction-law changelog (vs 70-localized/L1-s1.md)

Five video/link-only slides removed per contract §7. Their URLs survive in
`trainer-guide.md` as trainer-only optional resources.

| Was | Now |
| --- | --- |
| Slide 3 — micro:bit intro video URL | folded into Slides 3–5 (device + LED, taught live) |
| Slide 5 — name badge intro video URL | Slide 8 — predict-before-reveal beat |
| Slide 9 — YouTube coding video URL | Slide 10 — students build step 1–2 |
| Slide 10 — coding animation GIF slide | asset reused inline on Slide 10 |
| Slide 11 — tutorial URL slide | Slide 11 — students build step 3–4 |

Slide count 15 → 15 (five passive slides became five active ones). Under the
~21-slide NBLM cap; single-pass generation, no split-and-merge.

## Decisions added for the 120-minute rebuild

8. **Hardware tour before any screen.** Students physically locate the LED
   display, buttons, USB port and battery connector on their own board. The
   upstream 60-minute deck skips this; a hardware track cannot.

9. **Debugging Lab is a taught segment, not a footnote.** Fifteen minutes, three
   seeded bugs, predict-then-fix. The academy's framework is
   `Think → Build → Test → Debug → Explain` — debugging is a named academy value.

   The seeded bugs must actually reproduce:
   - Bug 1 uses `on start` (genuinely runs once, then stops)
   - Bug 2 leaves the placeholder text `"Hello!"`
   - Bug 3 leaves `show string` unattached to any handler (nothing happens at all)

   A loose block was originally mislabelled as the "runs once" case. It is not —
   an unattached block never runs. Corrected.

10. **Every student explains their own code.** Per the academy's Evidence of
    Learning rule, explanation is weighted above a working project.

11. **Exit ticket closes every session.** Q3 discriminates loop-understanding
    from block-name recall.

## Slide count

23 slides, generated in two NBLM passes (1–14, then 15–23) and merged.

Owner ruling: the three Debugging Lab bugs get **one slide each**, because on
those slides the image is the exercise — three broken programs crammed side by
side is harder for a child to read than one at a time. They were briefly merged
onto a single slide to fit the ~21-slide cap; that was reverted. Per `ethos-v2`
a cap is an external limit handled by split-and-merge, never by cutting content.
