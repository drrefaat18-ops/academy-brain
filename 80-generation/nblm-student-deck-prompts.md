# NotebookLM student deck prompts

Read by `scripts/swarm/generate_session.py` (`parse_prompts`). Course-neutral:
no lesson content lives here, only the instructions NotebookLM follows to turn
a session's sources into slides. `generate_session.py` supplies the sources
(`slides-source.md`, `decisions.md`, brand files, reference images) and appends
the reserved-image-region clause for `EVIDENCE` assets automatically — do not
duplicate that here.

Section headings are load-bearing. The parser matches on substring, case-
insensitive: a heading containing "notebook a" is deck-a, "pass b" is deck-b
(optional — only sessions whose slide count exceeds NotebookLM's single-pass
cap need it), "notebook b" is the summary deck. Each heading's own body ends
at the next `## ` heading. The prompt text itself is the first fenced code
block under the heading — write it inside a fence, not as bare prose.

## Notebook A — Student Deck (Pass A)

```
Generate a student slide deck for this 120-minute session from the attached
sources. Follow slides-source.md's slide order and content exactly — do not
invent slides, do not omit slides, do not reorder them.

Rules, all binding:

- One idea per slide. Large titles, simple shapes, clear images. No crowded
  slides, no dense paragraphs.
- A slide whose only content is a video link is not allowed. If a source
  slide references a video, treat the video as an optional trainer resource
  and give the student slide real on-slide content instead.
- The academy logo appears on the FIRST slide and the LAST slide only. Do not
  place it on any other slide, and do not invent or redraw a logo — use only
  the logo file provided among the sources.
- The course mascot (TATA) appears on SOME slides, never on every slide and
  never on none. Use judgment for where it adds warmth without cluttering
  the slide.
- Where a slide's asset mapping reserves an image region, leave that region
  exactly as instructed elsewhere in this prompt — do not draw a substitute
  image over a reserved region.
- No trainer-only content: no trainer scripts, no timings, no internal notes,
  no assessment checklists. This deck is student-facing only.
- Content must be expanded to genuinely fill 120 minutes with substance
  (predict-before-run on build steps, test after every mechanic, real
  troubleshooting attempts), not padding or repetition.
```

## Notebook A — Student Deck (Pass B)

```
Continue the SAME student deck from Pass A, picking up exactly where Pass A's
slides ended per slides-source.md. Do not repeat any slide already produced
in Pass A. All rules from Pass A carry over unchanged, including the
first/last-slide-only logo rule — Pass B's slides are not "last" unless
slides-source.md says this pass ends the deck.
```

## Notebook B — Student Summary

```
Generate the student summary deck from home-summary.md and the attached
brand files. Fixed length: 3 slides for a teaching or revision session with
a home-summary.md written for 3 slides, 2 slides for one written for 2 —
follow whatever slide count home-summary.md's own structure implies; do not
add or drop slides.

Every mandatory section in home-summary.md must appear somewhere in the
deck: Today I Learned, New Words, Review at Home, Parent Talk, Mini Activity.
Must be parent-friendly and student-friendly: short, visual, no trainer-only
content, no timings, no assessment checklists.

The academy logo appears on the FIRST slide only. No other slide carries it.
```
