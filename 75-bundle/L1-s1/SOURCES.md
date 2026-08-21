---
id: L1-s1
stage: bundle
type: nblm-upload-manifest
owner: claude
status: blocked-awaiting-assets
contract: 00-contracts/brand-and-output.md §1
---

# NBLM Upload Manifest — L1-s1

Two NotebookLM notebooks per session. Upload exactly these sources — no more
(doctrine: *"NotebookLM works best when sources are focused. Do not overload
NotebookLM with too many files."*).

## Notebook A — Student Slide Deck (23 slides, generated in TWO passes)

| # | Doctrine source type | File |
| --- | --- | --- |
| 1 | lesson material | `75-bundle/L1-s1/slides-source.md` |
| 2 | trainer guide | `75-bundle/L1-s1/trainer-guide.md` |
| 3 | educational decision note | `75-bundle/L1-s1/decisions.md` |
| 4 | branding rules | `.../Academy_Brain_OS/Techno_Square_Branding_Rule.md` |
| 5 | Tata guide | `.../Academy_Brain_OS/Tata_Mascot_Usage Guide.md` |
| 6 | key project images (REFERENCE only) | `75-bundle/L1-s1/assets/img-05.png`, `img-06.gif`, `img-36.jpg`, `img-41.png`, `img-51.gif` |
| + | brand chrome | `technosquare_logo.png`, `technosquare_logo_black.png` |
| + | mascot | `tata_excited.png`, `tata_idea.png`, `tata_thinks.png`, `tata_approved.png` |

**Never uploaded:** every EVIDENCE-class row in `ASSET-MAPPING.md` —
`img-19.png`, `img-20.png`, `img-21.png`, `img-32.gif`, `img-35.png`, the four
annotated crops, and the three bug screenshots. NotebookLM redraws any image it
is given. A redrawn screenshot looks right and is wrong. NotebookLM reserves a
blank region for these; the real file is overlaid after export.

## Notebook B — Student Summary Deck (3 slides)

| # | Source type | File |
| --- | --- | --- |
| 1 | summary material | `75-bundle/L1-s1/home-summary.md` |
| 2 | branding rules | `.../Academy_Brain_OS/Techno_Square_Branding_Rule.md` |
| 3 | Tata guide | `.../Academy_Brain_OS/Tata_Mascot_Usage Guide.md` |
| 4 | key project images (REFERENCE only) | `assets/img-05.png` |
| + | brand chrome | `technosquare_logo.png` |
| + | mascot | `tata_idea.png`, `tata_thinks.png`, `tata_approved.png` |

Do NOT upload to either notebook: `70-localized/*` raw, other sessions' files,
the full 56-image digest folder, `00-contracts/*` internals, `40-critique/*`.

## Asset provenance

All `img-NN` files are curated from `10-digest/_assets/L1-s1/` (56 total, 10
selected). Selection rule: dropped sub-3KB files — those are bullet glyphs and
decorative icons from the upstream deck, not content. Kept board photos, editor
screenshots, code screenshots, and build animations.

**Needs human visual check:** the 10 selected assets were chosen by filename,
source-slide, and byte size, not by looking at every one. Confirm none is a
duplicate, a stray upstream logo, or an unlabelled placeholder.

## Assets that must be CREATED before generation

Seven annotated assets are referenced by the deck but do not exist yet. All are
crops/annotations of files already in `assets/`. Annotate in Canva —
`AI_Tools_Workflow_Guide.md` sanctions Canva for exactly this kind of small edit.

| File | Derived from | What it must show |
| --- | --- | --- |
| `img-05-labelled.png` | `img-05.png` | board with **LED display**, **Buttons A/B**, **USB**, **battery connector** labelled |
| `img-05-led.png` | `img-05.png` | close crop of the 5×5 LED grid, lit |
| `img-19-labelled-a.png` | `img-19.png` | editor with arrows on **Toolbox** + **Workspace** only |
| `img-19-labelled-b.png` | `img-19.png` | editor with arrows on **Simulator** + **Download** only |
| `img-20-bug1.png` | `img-20.png` | `on start` + `show string` — runs once, then stops |
| `img-20-bug2.png` | `img-20.png` | `forever` + `show string "Hello!"` — wrong name |
| `img-20-bug3.png` | `img-20.png` | empty `forever`, `show string` loose outside it — nothing runs |

### The three bug screenshots must be genuinely broken

One slide per bug, so learners look at one problem at a time. Screenshot each as
actually built in MakeCode — do not mock them up, and do not combine them into a
single image.

Bug 1 must use `on start`, **not** a loose block. An unattached block never runs
at all — that is bug 3's symptom, not bug 1's.

**There is no fallback.** An earlier draft of this file offered one — uploading
the plain images and letting slide text carry the labels. That contradicted the
hard stop in `ASSET-MAPPING.md`, and it cannot work: bug 3's whole point is a
block sitting outside the loop, which a plain `img-20.png` does not show. If the
owner wants to ship without these, that is an explicit approved exception
recorded in `blueprint.md`, not a default this file grants.
