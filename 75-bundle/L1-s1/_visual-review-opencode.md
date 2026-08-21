---
lane: opencode
file: _visual-review-opencode.md
date: 2026-08-20
job: "L1-s1 visual QA (JOB 1) + programmatic asset production (JOB 2)"
model: opencode/hy3-free
image_input_capability: NONE
---

# L1-s1 Visual Review — opencode lane

## 0. Critical capability limitation (read first)

The model running this lane (`opencode/hy3-free`) **has no image-input
capability**. The `read` tool returns:

> `ERROR: Cannot read image (this model does not support image input).`

So I **cannot literally look at** any of the 10 raw images, the existing derived
files, or any screenshot I might generate. This is a hard, non-negotiable
constraint. Per the project doctrine in `SOURCES.md` / `ASSET-MAPPING.md`
("a fake screenshot that looks plausible is worse than an empty box", and
EVIDENCE may never be redrawn or fabricated), I have **not** invented any
visual verdict, label placement, or screenshot. Everything below is either
(a) an objective programmatic fact, or (b) an explicit "cannot verify" statement.

I did run **real code** for every check I could, and made a genuine, substantial
attempt at the bug screenshots (see JOB 2B). What I could not do genuinely, I
say so plainly.

---

## JOB 1 — Visual QA of the 10 curated raw images

### Method actually used
- `PIL` to read format / mode / dimensions / frame-count for each file.
- MD5 of raw bytes to detect exact duplicates.
- `playwright`+headless Chromium to confirm the MakeCode editor is reachable
  (network) — relevant to JOB 2 only.
- **No pixel-level semantic check was possible** because the model cannot see
  images. A true "does this file show what the mapping claims" check requires
  human eyes or a vision-capable model. That is the owner-review / vision-lane
  task; I do not fabricate it.

### Objective findings (measured)

| Image | Format | Size (px) | Frames | Bytes | Claim in mapping / slides-source | Objective note |
|---|---|---|---|---|---|---|
| `img-05.png` | PNG RGBA | 2810×1514 | 1 | 1.94 MB | whole micro:bit board view (slide 3, summary 1) | Large photo-res; plausible for a board shot. Content NOT verified. |
| `img-06.gif` | GIF | 395×322 | 25 | 117 KB | "computer hears your code" animation (slide 4) | Small but 25 frames → animated. Content NOT verified. |
| `img-19.png` | PNG RGB | 2776×1594 | 1 | 240 KB | MakeCode editor, Download highlighted (slide 14) | Editor-sized. Content NOT verified. |
| `img-20.png` | PNG RGBA | 1316×760 | 1 | 35 KB | completed `forever` + `show string` code (slide 10, summary 2) | Code-screenshot sized. Content NOT verified. |
| `img-21.png` | PNG RGBA | 1002×2500 | 1 | 19 KB | block close-up (slide 11) | Very tall/narrow — consistent with a vertical block stack, but could also be an unrelated tall graphic. Content NOT verified. |
| `img-32.gif` | GIF | 1389×756 | 116 | 963 KB | build animation steps 1–2 (slide 12) | 116 frames, large → real animation. Content NOT verified. |
| `img-35.png` | PNG RGBA | 1220×507 | 1 | 88 KB | step 3–4 build (slide 13) | Wide banner-ish. Content NOT verified. |
| `img-36.jpg` | JPEG RGB | **203×152** | 1 | 11 KB | "success" device photo, name scrolling (slide 15) | **ANOMALY: resolution is tiny** (203×152). Genuinely suspicious — could be a low-res crop, a decorative/logo-scale asset, or a placeholder. Needs human/visual eyes before approval. |
| `img-41.png` | PNG RGBA | 1380×952 | 1 | 86 KB | extension activity (slide 20) | Plausible. Content NOT verified. |
| `img-51.gif` | GIF | 383×313 | 2 | 22 KB | next-session "Animation" teaser (slide 23) | Only 2 frames, small. Content NOT verified. |

### Duplicate / logo / placeholder check
- **Exact-duplicate hashes:** NONE among the 10 selected files. (Pairwise unique
  by MD5 of raw bytes.) Note: I compared only the 10 selected assets, not against
  the full 56-image digest (`10-digest/_assets/L1-s1/`), so "duplicate of an
  unselected digest image" is not ruled out.
- **Stray upstream logo / unlabelled placeholder:** I **cannot** confirm absence
  without seeing the pixels. The one file I would flag for mandatory human eyes
  is **`img-36.jpg`** (203×152 — far below the resolution of every other photo,
  which suggests it may not be a real "success" device photo). `img-21.png`'s
  extreme aspect ratio also warrants a look.

### Per-image verdict (honest)
Every image: **NOT VISUALLY VERIFIED by this lane.** I can confirm each file
*resolves, is a valid image of the stated format, and is not an exact duplicate
of another selected file*, but I cannot confirm it *depicts* the claimed content,
nor rule out a stray logo/placeholder. These verdicts must come from the
vision-capable lane or the owner. I have not recorded any "confirmed shows X"
claim because that would be fabrication.

---

## JOB 2 — Programmatic asset production

### 2A. The four crop/label derived assets (img-05-labelled, img-05-led,
img-19-labelled-a, img-19-labelled-b)

**Genuine production status: NOT PRODUCED by this lane — and deliberately not
fabricated.**

These require locating specific on-image regions (LED display, Buttons A/B, USB,
battery on `img-05`; Toolbox/Workspace/Simulator/Download on `img-19`) in order
to overlay arrows + labels. Accurate label placement is exactly the kind of
"EVIDENCE" the doctrine forbids me to invent: an arrow pointing at the wrong
control would teach a child the wrong thing. Because this model cannot see the
images, I cannot determine those regions; producing them would be guessing =
fabricating EVIDENCE. I therefore did **not** generate them.

**Three of the four already exist on disk** (timestamp 2026-08-20 22:59),
produced by the parallel vision-capable lane agent (codex or hermes), not by me:

| File | On disk? | Valid? | This lane action |
|---|---|---|---|
| `img-05-led.png` | Yes (900×975 PNG) | Yes | Not overwritten; not visually verified |
| `img-19-labelled-a.png` | Yes (1940×1300 PNG) | Yes | Not overwritten; not visually verified |
| `img-19-labelled-b.png` | Yes (900×1449 PNG) | Yes | Not overwritten; not visually verified |
| `img-05-labelled.png` | **No** | — | Not produced (needs vision to place 4 labels) |

I will not overwrite the three existing files, and I cannot confirm they are
correct — only that they are well-formed PNGs of plausible dimensions.

### 2B. The three MakeCode bug screenshots (img-20-bug1/2/3.png)

**Plain statement: I do NOT have a dependable real way to produce genuine
MakeCode bug screenshots headlessly in this environment, and I have NOT
fabricated any.**

What I actually did (genuine effort, real code):
1. Installed `playwright` + headless Chromium (`chromium-headless-shell`).
2. Confirmed `https://makecode.microbit.org` returns HTTP 200 (network works).
3. Loaded the **real** editor at `…/#editor` in headless Chromium; the default
   project's blocks (`on start`, `forever`) render and are readable in the DOM
   via `.blocklyText` — so a real, non-mocked editor genuinely runs here.
4. Confirmed `pxt.lzmaCompressAsync` / `pxt.lzmaDecompressAsync` exist on the
   page (the editor's own project codec).
5. Attempted to load a specific broken program three ways:
   - base64 project-JSON in the URL hash (`#<b64>`) — did **not** load.
   - `?import=data:application/json;base64,…#editor` — did **not** load.
   - LZMA-compressed + base64 project in the URL hash (the "Edit" deep-link
     codec) — did **not** load (format/header not matched).
6. Attempted to recover the Blockly workspace object to inject blocks directly:
   scanned `window`, `Blockly.getMainWorkspace`, `Blockly.Workspace.*`,
   `Blockly.mainWorkspace`, DOM-block → model links, and `pxt.editor.*`.
   **The workspace is fully encapsulated** in this MakeCode fork (all standard
   Blockly accessors are hidden behind a Proxy / closure). Could not obtain it.

Because the editor would not accept a client-side project load and the workspace
is inaccessible, I could not get the three specific broken programs onto a real
canvas. Even if I had, I **cannot see the result** to confirm it is correct, so
shipping a screenshot would risk exactly the prohibited outcome: a
plausible-looking but possibly-wrong EVIDENCE frame.

**Therefore: I produced 0 of 3 bug screenshots. No fabrications created.**

### Updated on-disk state (checked at end of run)
While this lane was working, the **parallel vision-capable lane agent
(codex/hermes) produced the three bug files**. Final check:

| File | On disk? | Valid? |
|---|---|---|
| `img-20-bug1.png` | Yes | 1008×861 PNG, 35.8 KB — valid, not produced/verified by this lane |
| `img-20-bug2.png` | Yes | 1008×861 PNG, 35.7 KB — valid, not produced/verified by this lane |
| `img-20-bug3.png` | Yes | 1008×861 PNG, 39.3 KB — valid, not produced/verified by this lane |

These resolve on disk and are well-formed, but **this blind lane cannot confirm
their content** (no image input). Their correctness is the other lane's
responsibility and still requires the owner's EVIDENCE approval gate — they are
not auto-approved by mere existence (per `ASSET-MAPPING.md` rule).

The genuine path that remains for a vision-capable lane or a future run:
- drive the real editor's import/share codec correctly (the LZMA-hash format
  needs the exact header/prefix MakeCode expects — not yet matched), or
- expose the Blockly workspace through the editor's non-encapsulated API,
  then inject the block XML and verify via DOM `.blocklyText` (the DOM-text
  check I built is a sound, vision-free verification of "the right blocks with
  the right text/nesting are on screen").

---

## Summary of what this lane delivered

- **Genuine automated checks run:** file resolution, format/mode/dimensions,
  frame counts, exact-duplicate MD5 scan, MakeCode reachability + live editor
  load, pxt codec presence.
- **New files written by this lane:** none of the 7 target derived assets.
  The 3 crop/label files and the 3 bug screenshots that were needed now exist on
  disk — all produced by the parallel vision-capable lane (timestamp 22:59),
  not by me. I did not duplicate, overwrite, or fabricate any of them.
- **Hard blockers that require a different capability:**
  1. JOB 1 human visual check — needs a vision-capable model or the owner
     (this model is blind). Use the per-image table + flags above.
  2. `img-05-labelled.png` — needs vision to place 4 labels on `img-05.png`.
  3. `img-20-bug1/2/3.png` — need a working real-MakeCode load path + visual
     confirmation; not achievable here, and explicitly NOT fabricated.

No files under `scripts/**`, `ASSET-MAPPING.md`, `blueprint.md`,
`slides-source.md`, or `SOURCES.md` were modified.
