---
stage: generation
owner: claude
status: ready
usage: NotebookLM MCP, claude-run — two notebooks per session
contract: 00-contracts/brand-and-output.md §1, §1b, §1c
---

# NotebookLM Student Deck Prompts — L1-s1

Upload manifest: `75-bundle/L1-s1/SOURCES.md`. Upload exactly those sources.
Doctrine: *"NotebookLM works best when sources are focused. Do not overload
NotebookLM with too many files."*

## Notebook A — Student Slide Deck (23 slides, TWO passes)

```
Create a student slide deck for Techno Square Academy, micro:bit Level 1,
Session 1 "Name Badge".

Generate ONLY slides 1 to 14, ending at slide 14 "حمّل على الجهاز".
This is pass A of two; pass B will continue from slide 15 and be merged after.
Do not summarise or compress the later slides into this pass.

The file slides-source.md is the exact structure — one slide per "## Slide N"
heading, in that order. Do not add, merge, reorder, or drop slides. Do not
invent content that is not in the sources.

Per-slide bindings: each slide lists its own "**Asset:**" and "**TATA:**" lines.
Those name the image files uploaded with this notebook. Place each named image
on that slide and nowhere else. A slide with no TATA line gets no mascot.

Visual identity — follow Techno_Square_Branding_Rule.md:
- Techno Square logo on every slide
- dark/black with yellow and gold highlights
- large titles, icons, arrows, simple shapes
- clean and playful, never crowded
- one idea per slide

Mascot — follow Tata_Mascot_Usage_Guide.md. TATA is a guide, not decoration.
Use only the state named on each slide. Do not add TATA to other slides.

Language: keep the bilingual text exactly as written — roughly 30% English,
70% Egyptian-colloquial Arabic. English carries the technical terms
(micro:bit, forever, show string, algorithm, output, Toolbox, Simulator,
Download). Arabic carries the explanations and instructions. Do not
re-translate, re-balance, or "improve" any Arabic. Render Arabic right-to-left,
correctly shaped.

This deck is student-facing. It must contain no trainer timings, no facilitation
script, no assessment checklist, and no classroom management notes — even though
trainer-guide.md is uploaded as a source for context. That file is background
only; never quote it onto a slide.

There are no video links in this deck by design. Do not add any.
```

## Notebook B — Student Summary Deck (3 slides)

```
Create a 3-slide student summary deck for Techno Square Academy, micro:bit
Level 1, Session 1 "Name Badge". Exactly 3 slides — not 2, not 4.

home-summary.md is the exact structure:
- Slide 1: Today I Learned + New Words
- Slide 2: Review at Home + Mini Activity
- Slide 3: Parent Talk

This deck goes home with the student. Audience is the student AND the parent.
The parent is not assumed to know any programming.

Same brand rules as the main deck: Techno Square logo on every slide,
dark/black with yellow-gold highlights, large titles, visual, not text-heavy.

TATA only on the two slides that name it. Not on all three.

Language: keep the bilingual balance exactly as written. Arabic right-to-left,
correctly shaped. Do not re-translate.

No trainer content of any kind.
```

## After generation — required checks

1. Run the gates on the exported text (`arabic-ratio`, `trainer-boundary`,
   `brand-palette`).
2. **Human visual review (OCR-blind, cannot be automated):**
   - Is the Techno Square logo actually present and undistorted on every slide?
   - Is each TATA the correct pose, and absent where it should be absent?
   - Did any digest asset land on the wrong slide, or get duplicated?
   - Are there blank/placeholder image frames?
   - Is the Arabic shaped and right-to-left, not reversed or letter-separated?
   - Slide 7 (MakeCode editor): did the four labels/arrows survive?

## Notebook A — PASS B (slides 15–23)

Same notebook, same sources. Send after pass A is exported.

```
Continue the same Techno Square Academy micro:bit Level 1 Session 1 "Name Badge"
student deck.

Generate ONLY slides 15 to 23 from slides-source.md, starting at slide 15
"جرّب واتأكد" and ending at slide 23 "المرة الجاية".

This CONTINUES an existing deck. Do NOT create a title slide. Do NOT re-introduce
the session, the micro:bit, or the MakeCode editor. Do not recap earlier slides.
Start directly at slide 15.

Slides 17, 18 and 19 are the Debugging Lab — one broken program per slide, each
with its own image. Keep them as three separate slides. Do not combine them.

All other rules identical to pass A: per-slide Asset and TATA bindings, Techno
Square branding on every slide, one idea per slide, bilingual text kept exactly
as written, Arabic right-to-left. No video links.
```

Merge pass A then pass B, in order, into the final 23-slide deck.

**Why two passes:** 23 slides exceeds the ~21-slide NotebookLM cap. Per
`ethos-v2`, a cap is an external limit handled by split-and-merge, never by
cutting content. The split falls between the build and the evaluate/debug half so
no teaching beat is cut in two.
