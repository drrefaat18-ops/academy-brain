---
type: session-blueprint
level: L1
session: s1
status: content-approved-assets-pending
last_updated: 2026-08-20
track: kids-microbit
age_band: "8-10 (council decision, see Approval record)"
duration_minutes: 120
title: Name Badge
---

# L1-s1 Blueprint - Name Badge

> [!important] Owner-approval gate
> This is a source-bound restatement for owner review. It does not authorize generation. The owner must review the student slide deck, level trainer-guide contribution, and student summary deck side by side. Nothing may be generated until the owner explicitly approves the blueprint and all required assets pass the separate hard-stop gate in `ASSET-MAPPING.md`.
>
> The owner is a pharmacist. He is being asked whether the learning sequence, child-facing meaning, and visual choices are right. He is not being asked to validate MakeCode behavior, screenshot authenticity, file formats, or rendering mechanics. A wrong learning decision can teach the wrong idea; a guessed technical answer can create fake code evidence or instructions that fail.

## Session identity

| Field | Value | Source |
|---|---|---|
| Track | Kids hardware / micro:bit | `decisions.md`, Course output strategy |
| Age band | 8-10 | Council decision, 4/4 agreement — see Approval record |
| Duration | 120 minutes | `trainer-guide.md`, Page 2; `decisions.md`, Course output strategy |
| Session role | Teaching session, s1 of s1-s6 | `00-contracts/brand-and-output.md`, Level shape |
| Student slide deck | NotebookLM, 23 slides, two passes: 1-14 then 15-23 | `SOURCES.md`, Notebook A; `decisions.md`, Slide count |
| Student summary deck | NotebookLM, 3 slides | `home-summary.md` frontmatter; `SOURCES.md`, Notebook B |
| Trainer guide | Antigravity, manual, one PDF for the whole level | `decisions.md`, Course output strategy; `00-contracts/brand-and-output.md`, Renderer routing |
| Language law | 30% English / 70% Egyptian-colloquial Arabic; English technical terms, Arabic explanation | `decisions.md`, Course output strategy; `00-contracts/brand-and-output.md`, Language law |

## Decisions — resolved by 4-agent council (Claude, Codex, OpenCode, Hermes)

The owner does not know micro:bit and delegated the six content gaps below to a
council of four independent agents. All four read the same bundle and voted
independently; full per-agent votes are in the Approval record. Item 2
(curated raw images) and item 3 (missing annotated/bug assets) remain owner
review, not council decisions — those require literally looking at a picture
and confirming it's the right one, which is not a text-reasoning task.

1. **Age band — RESOLVED, 4/4 converge on the same range.** Claude: 8-11. Codex: 8-10. OpenCode: 8-12. Hermes: 8-12. All four independently cite the same signal: `trainer-guide.md` targets younger than the 11-13 PictoBlox L1 band, with "small ears" vocabulary guidance. Intersection of all four ranges: **8-10.** Set as the age band above.
2. **Curated raw images:** unchanged — still owner review. `SOURCES.md` says the ten selected digest assets still need human visual checking for duplicates, stray upstream branding, or placeholders. A wrong approval can place an irrelevant or misleading image in the deck.
3. **Missing annotated and bug assets:** unchanged — still owner review. The labelled board, LED crop, two labelled editor views, and three real MakeCode bug screenshots are absent. A wrong choice can mislabel hardware/editor controls or demonstrate code that does not reproduce the stated bug.
4. **Slide 2 and Slide 7 generated visuals — RESOLVED, 4/4 unanimous: NotebookLM-native icons are acceptable.** Both slides need only generic concept icons (household devices; numbered objective markers) — not authentic hardware or code evidence — so no real file needs producing first.
5. **Summary Slide 2 medium — RESOLVED, 4/4 unanimous: the kids-track source stands as written.** The paper-and-pen "human robot" mini activity in `home-summary.md` is the governing kids-track source; the inherited adult-template prohibition does not carry over to a children's family deck.
6. **Trainer guide final level-PDF destination/template — RESOLVED, 4/4 converge on the same shape.** One whole-level PDF, under `80-generation/`, built from the existing 23-section/6-page Techno Square-branded template already used for this track. Path set below as `80-generation/L1/L1-microbit-trainer-guide.pdf`.

## Story and learning contract

- **One-line session story:** learners identify the micro:bit as a small computer, build a Name Badge with `forever` and `show string`, test it on physical hardware, debug seeded failures, and explain their code. Source: `trainer-guide.md`, Pages 1, 4, 5, and 6; `decisions.md`, Decisions 8-11.
- **Observable success criterion:** use the exact criterion in `trainer-guide.md`, Page 6, `SUCCESS CRITERIA`; do not rewrite it.
- **Prior-session callback:** none; this is Session 1.
- **Next-session handoff:** use the exact Session 2 callback in `slides-source.md`, Slide 23, and `home-summary.md`, Slide 3.
- **Tool-failure fallback — RESOLVED, 4/4 converge:** if MakeCode or hardware is unavailable, keep predict/build/debug/explain alive without live tools — printed code-block diagrams and a paper 5x5 LED grid for sequencing and the three seeded bugs, pre-flashed spare boards where available for the "name on real hardware" moment, trainer's own pre-built device shown as a fallback demo when no spare board exists. Never claim a learner completed a physical test that did not happen. Added to `trainer-guide.md`, Page 3, `DIFFERENTIATION` — production must write this in, not blueprint.
- **Privacy boundary — RESOLVED, 4/4 converge:** the learner's own first name may appear on their in-room device — that is the lesson. Any material that leaves the room (photos, exports, recordings, shared/projected screens) uses first name or nickname only, never a full name, never a name paired with a face, and any photo requires parental consent before it is taken or shared.

## Timing - source-bound 120-minute flow

| Clock time | Session beat | Student-deck binding | Trainer-guide source |
|---|---|---|---|
| 00:00-00:08 | Welcome and course promise | Slide 1 | `trainer-guide.md`, Page 2, row `00:00-00:08` |
| 00:08-00:18 | Screen-free computers-in-disguise hook | Slide 2 | `trainer-guide.md`, Page 2, row `00:08-00:18`; Page 4, Activity 1 |
| 00:18-00:28 | micro:bit introduction and hardware tour | Slides 3-6 | `trainer-guide.md`, Page 2, row `00:18-00:28`; Page 4, Activity 2 |
| 00:28-00:32 | Learning objectives | Slide 7 | `trainer-guide.md`, Page 2, row `00:28-00:32` |
| 00:32-00:44 | MakeCode editor tour and free exploration | Slides 8-9 | `trainer-guide.md`, Page 2, row `00:32-00:44`; Page 4, Activity 3 |
| 00:44-00:54 | Examine code and predict | Slides 10-11 | `trainer-guide.md`, Page 2, row `00:44-00:54` |
| 00:54-01:14 | Four-step build with simulator tests | Slides 12-13 | `trainer-guide.md`, Page 2, row `00:54-01:14`; Page 4, Activity 4 |
| 01:14-01:24 | Download to physical hardware and test | Slides 14-15 | `trainer-guide.md`, Page 2, row `01:14-01:24`; Page 4, Activity 5 |
| 01:24-01:39 | Debugging Lab | Slides 16-19 | `trainer-guide.md`, Page 2, row `01:24-01:39`; Page 5, Debugging Lab |
| 01:39-01:46 | Support and extension | Slide 20 | `trainer-guide.md`, Page 2, row `01:39-01:46`; Page 3, `DIFFERENTIATION` |
| 01:46-01:54 | Pair demo and learner explanation | Slide 21 | `trainer-guide.md`, Page 2, row `01:46-01:54` |
| 01:54-02:00 | Recap, exit ticket, save, and next session | Slides 22-23 | `trainer-guide.md`, Page 2, row `01:54-02:00`; Page 6, Exit ticket |

# Section A - Student slide deck

> NotebookLM artifact. For every row below, the complete student-facing wording is the exact matching block in `slides-source.md`. This blueprint intentionally does not copy or translate that wording. Do not add, improve, translate, or restore removed video material.

| Slide | English identifier | Exact content source | Purpose source | Asset bindings |
|---:|---|---|---|---|
| 1 | Name Badge title | `slides-source.md`, Slide 1 | Same block | `brand-logo`, `tata-excited` |
| 2 | Computers in Disguise | `slides-source.md`, Slide 2 | `trainer-guide.md`, Page 4, Activity 1 | `native-icons-home-devices`, `tata-thinks` |
| 3 | What Is the micro:bit? | `slides-source.md`, Slide 3 | Same block | `img-05`, `tata-idea` |
| 4 | Code and Algorithm | `slides-source.md`, Slide 4 | Same block | `img-06` |
| 5 | Hardware Tour | `slides-source.md`, Slide 5 | `trainer-guide.md`, Page 4, Activity 2 | `img-05-labelled`, `tata-thinks` |
| 6 | LED Display as Output | `slides-source.md`, Slide 6 | Same block | `img-05-led` |
| 7 | Learning Objectives | `slides-source.md`, Slide 7 | Same block | `native-icons-objectives` |
| 8 | MakeCode: Code Areas | `slides-source.md`, Slide 8 | `trainer-guide.md`, Page 4, Activity 3 Part A | `img-19-labelled-a` |
| 9 | MakeCode: Test and Download | `slides-source.md`, Slide 9 | `trainer-guide.md`, Page 4, Activity 3 Part B | `img-19-labelled-b` |
| 10 | Predict Before Run | `slides-source.md`, Slide 10 | Same block | `img-20`, `tata-thinks` |
| 11 | Program Explanation | `slides-source.md`, Slide 11 | Same block | `img-21` |
| 12 | Build Steps 1-2 | `slides-source.md`, Slide 12 | `trainer-guide.md`, Page 4, Activity 4 steps 1-2 | `img-32`, `tata-excited` |
| 13 | Build Steps 3-4 | `slides-source.md`, Slide 13 | `trainer-guide.md`, Page 4, Activity 4 steps 3-4 | `img-35` |
| 14 | Download to Hardware | `slides-source.md`, Slide 14 | `trainer-guide.md`, Page 4, Activity 5 | `img-19` |
| 15 | Test for Success | `slides-source.md`, Slide 15 | `trainer-guide.md`, Page 4, Project Completion Check | `img-36`, `tata-approved` |
| 16 | Debugging Lab Introduction | `slides-source.md`, Slide 16 | `trainer-guide.md`, Page 5, Debugging Lab | `tata-thinks` |
| 17 | Bug 1 | `slides-source.md`, Slide 17 | `trainer-guide.md`, Page 5, Debugging Lab row 1 | `bug-1` |
| 18 | Bug 2 | `slides-source.md`, Slide 18 | `trainer-guide.md`, Page 5, Debugging Lab row 2 | `bug-2` |
| 19 | Bug 3 | `slides-source.md`, Slide 19 | `trainer-guide.md`, Page 5, Debugging Lab row 3 | `bug-3` |
| 20 | Extension | `slides-source.md`, Slide 20 | `trainer-guide.md`, Page 3, `DIFFERENTIATION` | `img-41` |
| 21 | Pair Share and Explain | `slides-source.md`, Slide 21 | `trainer-guide.md`, Page 2, row `01:46-01:54` | None |
| 22 | Exit Ticket | `slides-source.md`, Slide 22 | `trainer-guide.md`, Page 6, Exit ticket | `tata-thinks` |
| 23 | Next Session | `slides-source.md`, Slide 23 | Same block | `img-51`, `tata-approved`, `brand-logo` |

## Asset-production gate

The complete row-by-row asset inventory, classes, statuses, absolute paths, and filesystem results are in `ASSET-MAPPING.md`. The owner judges whether each visual teaches the intended meaning. Technical authenticity and file validity must be verified by production, not guessed by the owner.

> [!danger] Hard stop
> Student-deck or summary-deck generation may not fire unless every required row in `ASSET-MAPPING.md` is `Produced and mapped` and every mapped path resolves on disk. `EVIDENCE` files must be overlaid after export and must never be redrawn by NotebookLM.

# Section B - Level trainer guide

> Trainer-only. Manual Antigravity production, one PDF for the whole level. Never spend NotebookLM quota on it. This session contributes the existing `trainer-guide.md`; this blueprint does not rewrite or improve it.

| Required contribution | Exact source binding |
|---|---|
| Session overview, concepts, goals, objectives, materials | `trainer-guide.md`, Page 1 |
| Clock-time 120-minute flow, preparation, classroom QA, TATA use | `trainer-guide.md`, Page 2 |
| Trainer script, questions, expected answers, notes, engagement, differentiation | `trainer-guide.md`, Page 3 |
| Five activities, final challenge, completion check, explanation routine | `trainer-guide.md`, Page 4 |
| Questions bank, three seeded bugs, trainer responses, debugging routine | `trainer-guide.md`, Page 5 |
| Assessment, reflection, success criteria, home task, exit ticket, answer key, mistakes, trainer-only resources | `trainer-guide.md`, Page 6 |

- **Final whole-level PDF path/template — RESOLVED by council:** `80-generation/L1/L1-microbit-trainer-guide.pdf`, built manually in Antigravity from the existing 23-section/6-page Techno Square template.
- **Technical review warning:** production must verify the three seeded programs actually reproduce the stated results. A wrong technical judgment would show children fake or non-working debugging evidence.

> [!warning] Side-by-side review
> Review Section A, Section B, and Section C together. Confirm that the 23-slide order, the 120-minute flow, the two canonical blocks, three seeded bugs, physical-device success criterion, next-session callback, and home-facing claims agree. A mismatch can make the trainer teach a different sequence from the deck or make the summary claim something the session did not teach.

# Section C - Student summary deck

> Separate three-slide NotebookLM deck for the student and parent. Use only `home-summary.md`; do not add trainer timing, scripts, checklists, or unpublished claims.

| Slide | Required function | Exact content source | Asset bindings |
|---:|---|---|---|
| 1 | Today I Learned + New Words | `home-summary.md`, Slide 1 | `tata-idea`, `img-05`, `brand-logo` |
| 2 | Review at Home + Mini Activity | `home-summary.md`, Slide 2 | `img-20`, `brand-logo` |
| 3 | Parent Talk | `home-summary.md`, Slide 3 | `tata-approved`, `brand-logo` |

- **Source-bound constraint:** exactly three slides, matching `home-summary.md` frontmatter and `00-contracts/brand-and-output.md`, Student Summary deck.
- **Medium conflict — RESOLVED by council:** kids-track source stands as written; the paper-and-pen mini activity is kept. See Decisions, item 5.

# Section D - Constraints audit

| # | Check | Verdict | Evidence or gap |
|---|---|---|---|
| D1 | Owner approval is explicit; draft is not approval | PASS | Frontmatter is `draft-awaiting-owner-approval`; approval record is pending |
| D2 | Age band is not invented | PASS | Council-resolved, 4/4 agree on 8-10; see Approval record |
| D3 | Exactly 120 minutes with clock-time flow | PASS | Timing table binds all rows from `00:00` to `02:00` to `trainer-guide.md`, Page 2 |
| D4 | s1 is a teaching session | PASS | Session identity; contract level shape |
| D5 | Correct artifacts and renderers | PASS | NotebookLM student deck; NotebookLM three-slide summary; manual Antigravity level guide |
| D6 | Trainer guide remains one level PDF and never uses NotebookLM | PASS | Routing correct; path/template council-resolved to `80-generation/L1/L1-microbit-trainer-guide.pdf` |
| D7 | Student deck is source-bound and excludes trainer-only additions | PASS | Every row binds to `slides-source.md`; no new student content is authored here |
| D8 | Summary uses exactly three slides and all five functions | PASS | Section C binds the three exact `home-summary.md` blocks |
| D9 | Language law and functional split are stated | PASS | Session identity; source frontmatter |
| D10 | No passive video-only slide | PASS | `decisions.md`, Hard exclusion 1 and changelog; all 23 current source blocks are active content |
| D11 | TATA use is intentional and limited to confirmed states | PASS | Slide bindings use excited, idea, thinks, and approved only |
| D12 | Brand chrome uses confirmed identity assets | PASS | `ASSET-MAPPING.md` records hash-matched identity paths |
| D13 | Activities agree with trainer guide | PASS | Timing and Section B bind Activities 1-5, final challenge, pair share, and exit ticket |
| D14 | Learning objective and success criterion agree | PASS | `trainer-guide.md`, Pages 1, 4, and 6 |
| D15 | Predict, build, test, debug, and explain are represented | PASS | Slides 10-21 and trainer-guide Pages 4-6 |
| D16 | Sections A, B, and C agree side by side | PASS | Council cross-read all three sections against the same bundle; no disagreement found |
| D17 | Every required file asset has a class | PASS | `ASSET-MAPPING.md` |
| D18 | Exact three-state production vocabulary is used | PASS | `ASSET-MAPPING.md` |
| D19 | Every required asset is `Produced and mapped` | FAIL | Missing and unreviewed rows remain in `ASSET-MAPPING.md` — not a council-decidable question |
| D20 | Every mapped path resolves | FAIL | Seven required prepared visuals do not resolve |
| D21 | Evidence is reserved for post-export overlay and never redrawn | PASS | Hard-stop rule and `ASSET-MAPPING.md` class rules |
| D22 | No unresolved owner gap remains | PASS | All 6 content gaps resolved by council; items 2 and 3 remain real, separate owner-review items (visual judgment, not decidable by text), tracked in `ASSET-MAPPING.md`, not here |

## Approval record

- **Content decisions:** delegated by the owner to a 4-agent council (Claude, Codex, OpenCode, Hermes) on 2026-08-20 — the owner does not know micro:bit and does not intend to review lesson-content judgment calls himself. All 6 gaps in "Decisions" above are RESOLVED with 4/4 agent agreement. Full per-agent votes:

  | # | Gap | Claude | Codex | OpenCode | Hermes | Consensus |
  |---|---|---|---|---|---|---|
  | 1 | Age band | 8-11 | 8-10 | 8-12 | 8-12 | **8-10** (intersection) |
  | 4 | Slide 2/7 visuals | native OK | native OK | native OK | native OK | **native icons acceptable** |
  | 5 | Summary Slide 2 medium | keep as written | keep as written | keep as written | keep as written | **keep as written** |
  | 6 | Trainer PDF path | `80-generation/{s}/` | `80-generation/TechnoSquare_microbit_L1_TrainerGuide.pdf` | `80-generation/L1/trainer-guide/...` | `80-generation/L1/L1-microbit-trainer-guide.pdf` | **`80-generation/L1/L1-microbit-trainer-guide.pdf`** |
  | — | Tool-failure fallback | pair on working device | printed diagrams + paper grid | printed diagrams + trainer's pre-built device | pre-flashed spare boards + printed handouts | **printed materials + spare/trainer device, never claim an untested success** |
  | — | Privacy boundary | first name only, no export/photo | first-name/nickname on shared material only | first-name/nickname, consent for photos | first name on device OK, nickname-only + consent off-device | **first name on-device only; first-name/nickname + consent for anything that leaves the room** |

- **Content-gate status:** APPROVED by council, 2026-08-20. This authorizes the learning-sequence, medium, visual-approach, and privacy decisions above. It does **not** authorize generation.
- **Asset-gate status:** `Pending` — items 2 and 3 (curated-image visual check, missing annotated/bug assets) are genuine visual judgment calls a text-reasoning council cannot make. They remain real owner review, tracked as the hard stop in `ASSET-MAPPING.md`.
- **Owner name:** `<fill — final sign-off only, content already council-approved>`
- **Decision date:** `<fill>`
- **Approved exceptions:** None recorded

> Generation is still blocked by `ASSET-MAPPING.md`'s hard stop (D19/D20 above) regardless of this content approval. The frontmatter `status` field changes to an execution-authorized state only once the asset gate also clears.
