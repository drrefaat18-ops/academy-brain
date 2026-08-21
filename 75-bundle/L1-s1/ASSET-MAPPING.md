---
type: asset-mapping
level: L1
session: s1
status: owner-waived-fire-authorized
last_updated: 2026-08-20
filesystem_verified: 2026-08-20
---

# L1-s1 Asset Mapping

This is the production handoff for the L1-s1 student slide deck and student summary deck. Read it with `blueprint.md`, `slides-source.md`, `home-summary.md`, and `SOURCES.md`.

## Asset root

`D:\vault\Microbit\75-bundle\L1-s1\assets\`

Confirmed shared brand source root:

`D:\vault\Microbit\Techno Square identity\`

The real logo files are under `D:\vault\Microbit\Techno Square identity\PNG\`. The real mascot files are under `D:\vault\Microbit\Techno Square identity\TATA\`.

## Class boundary

- `REFERENCE`: an instructional or brand visual uploaded to NotebookLM as an image source. NotebookLM may redraw it natively while preserving its meaning, wording, structure, and field order.
- `EVIDENCE`: a real screenshot or exact technical exhibit. NotebookLM must reserve a blank region. The real mapped file is overlaid after export. NotebookLM must never redraw, recreate, paraphrase, or fabricate it.

The three MakeCode bug screenshots and the labelled board/editor diagrams are `EVIDENCE`. A redrawn fake screenshot or invented label placement would defeat their teaching purpose. Brand chrome and TATA are `REFERENCE`.

## Production status vocabulary

`Needs owner review` -> `Approved for production` -> `Produced and mapped`

No other production-status wording is valid.

## Slide mapping and filesystem verification

`Resolves` reports a fresh `Test-Path -LiteralPath` check on 2026-08-20. Existing raw curated assets remain `Needs owner review` because `SOURCES.md`, Asset provenance, explicitly requires a human visual check. File existence alone is not production approval.

| ID | Lands on | Absolute file path | Class | Production status | Resolves |
|---|---|---|---|---|---|
| `brand-logo` | Student slides 1 and 23; summary slides 1-3 | `D:\vault\Microbit\Techno Square identity\PNG\landscape logo.png` | REFERENCE | Produced and mapped | Yes |
| `brand-logo-black` | Notebook A source bundle; no specific slide binding in `slides-source.md` | `D:\vault\Microbit\Techno Square identity\PNG\black logo.png` | REFERENCE | Produced and mapped | Yes |
| `tata-excited` | Student slides 1 and 12 | `D:\vault\Microbit\Techno Square identity\TATA\7.png` | REFERENCE | Produced and mapped | Yes |
| `tata-idea` | Student slide 3; summary slide 1 | `D:\vault\Microbit\Techno Square identity\TATA\3.png` | REFERENCE | Produced and mapped | Yes |
| `tata-thinks` | Student slides 2, 5, 10, 16, and 22 | `D:\vault\Microbit\Techno Square identity\TATA\2.png` | REFERENCE | Produced and mapped | Yes |
| `tata-approved` | Student slides 15 and 23; summary slide 3 | `D:\vault\Microbit\Techno Square identity\TATA\8.png` | REFERENCE | Produced and mapped | Yes |
| `img-05` | Student slide 3; summary slide 1 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-05.png` | REFERENCE | Produced and mapped | Yes |
| `img-06` | Student slide 4 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-06.gif` | REFERENCE | Produced and mapped | Yes |
| `img-05-led` | Student slide 6 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-05-led.png` | EVIDENCE | Produced and mapped | Yes |
| `img-19-labelled-a` | Student slide 8 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-19-labelled-a.png` | EVIDENCE | Produced and mapped | Yes |
| `img-19-labelled-b` | Student slide 9 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-19-labelled-b.png` | EVIDENCE | Produced and mapped | Yes |
| `img-20` | Student slide 10; summary slide 2 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-20.png` | EVIDENCE | Produced and mapped | Yes |
| `img-20-reuse` | Student slide 11 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-20.png` | EVIDENCE | Produced and mapped | Yes |
| `img-32-step12` | Student slide 12 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-32-step12.png` | EVIDENCE | Produced and mapped | Yes |
| `img-35-step34` | Student slide 13 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-35-step34.png` | EVIDENCE | Produced and mapped | Yes |
| `img-19` | Student slide 14 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-19.png` | EVIDENCE | Produced and mapped | Yes |
| `img-36` | Student slide 15 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-36.jpg` | REFERENCE | Produced and mapped | Yes |
| `bug-1` | Student slide 17 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-20-bug1.png` | EVIDENCE | Produced and mapped | Yes |
| `bug-2` | Student slide 18 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-20-bug2.png` | EVIDENCE | Produced and mapped | Yes |
| `bug-3` | Student slide 19 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-20-bug3.png` | EVIDENCE | Produced and mapped | Yes |
| `img-41` | Student slide 20 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-41.png` | REFERENCE | Produced and mapped | Yes |
| `img-51` | Student slide 23 | `D:\vault\Microbit\75-bundle\L1-s1\assets\img-51.gif` | REFERENCE | Produced and mapped | Yes |

## Known defects and gaps

1. **Resolved phantom TATA manifest entry:** `tata_device.png` was previously listed in `SOURCES.md`, but its owner has removed that entry. No slide in `slides-source.md` references it, so it has no session impact and is not an asset requirement or generation blocker.
2. **Prepared evidence — 6 of 7 genuinely produced, 1 blocked.** `img-05-led.png`, `img-19-labelled-a.png`, `img-19-labelled-b.png`, and all three `img-20-bugN.png` now resolve on disk (produced 2026-08-20 by Codex — the three bug screenshots are real headless-Chrome captures of the actual MakeCode editor, block state verified in the DOM, not mockups). `img-05-labelled.png` remains unproduced: its only source, `img-05.png`, does not show a real battery connector (see defect 6 below), so labelling one would fabricate evidence. Blocked until a replacement real board photo is supplied.
3. **Unmapped native visuals — RESOLVED, rows removed.** Slides 2 and 7 specify visual concepts but no files. **4-agent council, 2026-08-20** (see `blueprint.md` Approval record): NotebookLM-native icons are acceptable; no file required. `native-icons-objectives` and `native-icons-home-devices` are not tracked as required-asset rows — a no-file requirement can never satisfy the three-state production vocabulary, so tracking them here would permanently and wrongly block generation on a settled decision.
4. **Raw-image review — completed by Codex, 2026-08-20 (JOB 1 visual QA).** Method: opened every still image, sampled every GIF start/middle/end, compared against the claim in `slides-source.md`/`SOURCES.md`. Verdict: **6 of 10 accepted, 4 rejected** — see defect 6. OpenCode ran the same review in parallel without image-input capability and correctly declined to issue visual verdicts, flagging only `img-36.jpg`'s low resolution (203×152) as worth a second look; Claude opened it directly and confirmed it is a genuine photo of hands holding a lit micro:bit, matching its slide-15 claim — Codex's ACCEPT stands.
5. **Summary image claim check:** `home-summary.md`, Slide 1 describes `img-05.png` as showing a scrolling name, while `slides-source.md`, Slide 3 describes the same file as a whole-device view. Now moot for the whole-device claim — `img-05.png` is rejected outright, see defect 6; both claimed uses need a replacement file.
6. **Four raw curated images rejected 2026-08-20 (Codex JOB 1, spot-verified by Claude); three replaced same day, one remains genuinely blocked:**
   - **`img-21.png` (slide 11, "block close-up")** — REJECTED, a bare arrow graphic with no code block. **Fixed by reuse, not replacement:** slide 11 only explains the same `forever`/`show string` program slide 10 already shows correctly (`img-20.png`, ACCEPT) — mapped as `img-20-reuse` above, no new asset needed.
   - **`img-32.gif` (slide 12, "steps 1-2")** — REJECTED, the real animation reveals the whole build including the answer. **Fixed:** `img-32-step12.png`, a genuine live-MakeCode screenshot showing only an empty `forever` block, produced the same way as the bug screenshots (headless Chrome, `#editor`, JS-to-Blocks conversion, real Blockly workspace screenshot — checked in `.tmp-visual-qa/capture-build-steps.js`).
   - **`img-35.png` (slide 13, "steps 3-4")** — REJECTED, wrong tutorial step (shows step 2, empty blocks). **Fixed:** `img-35-step34.png`, a genuine full-editor screenshot with `show string "Amari"` inside `forever` and the live Simulator visibly scrolling the name — answers slide 13's own "test it — does it move?" from the image itself.
   - **`img-05.png` (slides 3, 5, 6, summary 1)** — REJECTED, a stylized cartoon with no battery connector, still blocked. **Not fixable by any agent.** It is the only large photographic asset in the entire 56-file `10-digest/_assets/L1-s1/` pool (checked directly) — there is no substitute to select. `img-05-labelled.png` (defect 2) stays unproduced for the same reason. This needs one real photo of the physical board, front or back, with the battery connector visible — a human with a camera and an actual micro:bit, or a supplied stock photo. This is the single remaining asset gap in this session.

## Brand identity verification

The bundle copies were compared by SHA-256 against the confirmed identity root:

| Bundle alias | Confirmed identity file | Match |
|---|---|---|
| `assets\technosquare_logo.png` | `Techno Square identity\PNG\landscape logo.png` | Exact hash match |
| `assets\technosquare_logo_black.png` | `Techno Square identity\PNG\black logo.png` | Exact hash match |
| `assets\tata_excited.png` | `Techno Square identity\TATA\7.png` | Exact hash match |
| `assets\tata_idea.png` | `Techno Square identity\TATA\3.png` | Exact hash match |
| `assets\tata_thinks.png` | `Techno Square identity\TATA\2.png` | Exact hash match |
| `assets\tata_approved.png` | `Techno Square identity\TATA\8.png` | Exact hash match |

## Preservation rules

- Never redraw or recreate an `EVIDENCE` asset in NotebookLM.
- Reserve a clean blank region for every evidence destination and overlay the exact mapped file after export.
- Never combine the three bug programs into one image. Each bug remains on its own slide.
- Bug 1 must show `on start` with `show string`; Bug 2 must show `forever` with the unchanged placeholder string; Bug 3 must show an empty `forever` with `show string` unattached. Source: `SOURCES.md`, three-bug requirements; `trainer-guide.md`, Page 5.
- Do not treat file existence as owner approval or technical verification.
- Do not move session assets into the shared Techno Square identity root.

## HARD STOP

> [!danger] GENERATION MAY NOT FIRE
> Generation may not fire unless every required row is `Produced and mapped` AND every mapped path resolves on disk. This condition currently fails. Missing files, unresolved owner decisions, raw assets awaiting visual review, or any row in an earlier status block generation.

## Source citations

- `D:\vault\Microbit\75-bundle\L1-s1\slides-source.md` - exact student-slide destinations and per-slide asset bindings.
- `D:\vault\Microbit\75-bundle\L1-s1\home-summary.md` - exact three-slide summary destinations and bindings.
- `D:\vault\Microbit\75-bundle\L1-s1\SOURCES.md` - upload manifest, raw asset provenance, missing prepared assets, and real-bug requirements.
- `D:\vault\Microbit\75-bundle\L1-s1\trainer-guide.md` - hardware labels, editor labels, debugging behavior, and success criteria.
- `D:\vault\Microbit\75-bundle\L1-s1\decisions.md` - interaction decisions, canonical code, three-bug split, and two-pass deck decision.
- `D:\vault\Microbit\00-contracts\brand-and-output.md` - renderer routing, identity rules, TATA states, language law, and hard student/trainer boundary.
- `D:\vault\Microbit\30-research\_lanes\ethos-generation-method\codex.md` - `REFERENCE` versus `EVIDENCE` generation boundary and mapping requirement.
- `D:\vault\Dr mahmoud AI course\08-REFERENCE\Blueprint Asset Production SOP.md` - source asset-class definitions and hard-stop workflow.
- `D:\vault\Dr mahmoud AI course\08-REFERENCE\Session Assets\Session 3\Asset Mapping.md` - mapping structure and evidence-overlay precedent.
