---
type: session-blueprint
level: "<L1>"
session: "<s1>"
status: draft-awaiting-owner-approval
last_updated: YYYY-MM-DD
track: kids-microbit
age_band: "UNCONFIRMED - owner must fill"
duration_minutes: 120
---

# <Level>-<Session> Blueprint - <English session title>

> [!important] Owner-approval gate
> This document is the pre-generation record for the student slide deck, student summary deck, and level trainer guide. The owner must review all three sections side by side. Nothing may be generated until the owner changes the status to an explicitly approved state.
>
> The owner is a pharmacist. He is being asked to judge whether the lesson is suitable for the children, whether the sequence makes sense, and whether each visual teaches the intended idea. He is not being asked to validate code syntax, wiring, file formats, or rendering mechanics. Those technical checks belong to the production team. A wrong content decision can teach the wrong idea; a wrong technical decision can produce code or hardware instructions that fail, so technical uncertainties must be recorded as gaps instead of being guessed.

## Session identity

| Field | Value |
|---|---|
| Track | Techno Square micro:bit kids track |
| Age band | `UNCONFIRMED - owner must fill` |
| Duration | 120 minutes |
| Session role | `<teaching / revision / graduation project>` |
| Level shape | s1-s6 teaching; s7 revision; s8 graduation project |
| Language law | 30% English / 70% Egyptian-colloquial Arabic; English carries technical terms and Arabic carries explanation |

> [!danger] Artifact routing law
> Teaching sessions s1-s6 produce a NotebookLM student slide deck and a three-slide NotebookLM student summary deck. Session s7 produces a NotebookLM student slide deck and a two-slide NotebookLM student summary deck. Session s8 produces no artifacts. The trainer guide is one manually produced Antigravity PDF for the whole level. Never use NotebookLM quota for the trainer guide.

## Decisions that need the owner's call before generation

> Each item must explain what the owner is judging in plain language and what a wrong choice would cause. If there are no open decisions, state that explicitly.

1. `<Decision, plain-language judgment, and consequence of a wrong choice>`

## Story and learning contract

- **One-line session story:** `<fill from approved bundle source>`
- **Learning objective:** `<observable learner outcome>`
- **Emotional arc:** `<starting state -> challenge -> successful finish>`
- **Prior-session callback:** `<exact callback or N/A>`
- **Next-session handoff:** `<what learners carry forward or N/A>`
- **Trainer warnings:** `<source-bound warnings only>`
- **Tool-failure fallback:** `<how the learning outcome survives a service or hardware failure>`
- **Privacy boundary:** `<what learner information may appear>`

## Timing

Use a clock-time timeline from `00:00` to `02:00`. Every row must bind to the trainer-guide source. Total: 120 minutes.

| Clock time | Session beat | Student-deck slides | Trainer-guide source |
|---|---|---|---|
| `<00:00-00:00>` | `<beat>` | `<slides or activity>` | `<exact source section>` |

# Section A - Student slide deck

> NotebookLM artifact. List every slide in order. Student-facing content must come only from the approved slide source. Trainer timings, scripts, assessment checklists, classroom-management notes, and passive video payloads may not enter this section.

## Every slide, in order

### Slide <N> - <English identifier>

- **Content source:** `<absolute or bundle-relative file and exact slide block>`
- **Content rule:** use the exact source block; do not add, improve, translate, or restore removed material.
- **Purpose:** `<restatement from an approved source>`
- **Activity or static slide:** `<Activity / static>`
- **Asset bindings:** `<asset IDs from ASSET-MAPPING.md or None>`

## Asset requirements - owner reviews; production team produces

> The owner judges whether each visual belongs and whether it demonstrates the intended idea. The owner does not judge pixel dimensions, image encoding, code validity, or overlay geometry. Approving the wrong meaning can teach the wrong lesson; guessing at technical validity can create fake or non-working evidence.

| ID | Slide | What it must teach or prove | Class (`REFERENCE` / `EVIDENCE`) | What the owner must judge | Production status | Mapped file |
|---|---:|---|---|---|---|---|
| `<asset-id>` | `<N>` | `<purpose>` | `<class>` | `<plain-language decision and consequence>` | `Needs owner review` | `GAP - owner must decide` |

Allowed production statuses, in order: `Needs owner review` -> `Approved for production` -> `Produced and mapped`.

> [!danger] Asset-production hard stop
> Generation may not fire unless every required asset row is `Produced and mapped` and every mapped absolute path resolves on disk. `REFERENCE` assets are uploaded as image sources and may be redrawn natively by NotebookLM. `EVIDENCE` assets are never redrawn: NotebookLM reserves a blank region and the real file is overlaid after export.

# Section B - Level trainer guide

> Trainer-only. Antigravity, manual owner-run, one PDF for the whole level. Never send this artifact to NotebookLM. For a session blueprint, bind the session-specific contribution to the existing trainer-guide source without rewriting it.

- **Source file:** `<trainer-guide.md>`
- **Level-PDF destination:** `<owner-approved destination or GAP>`
- **Session overview source:** `<exact section>`
- **120-minute flow source:** `<exact section>`
- **Trainer script and interaction source:** `<exact section>`
- **Activity guide source:** `<exact section>`
- **Questions and debugging source:** `<exact section>`
- **Assessment and reflection source:** `<exact section>`
- **Trainer-only resource boundary:** `<exact section>`

> [!warning] Side-by-side review
> Compare Section A, Section B, and Section C in the same review. Confirm that slide order, trainer actions, timing, terminology, assets, success criteria, and home-facing claims agree. A mismatch can make the trainer teach a sequence different from the students' deck or send families a claim the session did not teach.

# Section C - Student summary deck

> NotebookLM artifact. This replaces the adult-course handout. It is a separate student-and-parent slide deck: three slides for s1-s6, two slides for s7, and none for s8. It is not the trainer guide and must contain no trainer-only material.

## Slide budget and required coverage

| Session role | Slide budget | Required coverage |
|---|---:|---|
| Teaching, s1-s6 | 3 | Slide 1: Today I Learned + New Words; Slide 2: Review at Home + Mini Activity; Slide 3: Parent Talk |
| Revision, s7 | 2 | All required summary functions compressed across two source-approved slides |
| Graduation project, s8 | 0 | No artifact; this absence is not a gap |

### Summary slide <N> - <English identifier>

- **Content source:** `<home-summary.md exact slide block>`
- **Content rule:** use the exact source block; do not add, improve, or translate.
- **Asset bindings:** `<asset IDs from ASSET-MAPPING.md or None>`

# Section D - Constraints audit

> Complete this audit from the three sections above and their bound source files. A `FAIL` is fixed in the canonical source before generation. Do not patch the generated artifact to hide a source defect.

| # | Check | Verdict | Evidence or gap |
|---|---|---|---|
| D1 | Owner approval is explicit; draft is not treated as approval | | |
| D2 | Age band is owner-filled and not invented | | |
| D3 | Session duration is exactly 120 minutes with a clock-time flow | | |
| D4 | Session role matches s1-s6 teaching, s7 revision, or s8 graduation project | | |
| D5 | Artifact count and renderer routing match the session role | | |
| D6 | Trainer guide is one level PDF, manual Antigravity, never NotebookLM | | |
| D7 | Student deck contains only student-facing source content | | |
| D8 | Student summary uses the fixed slide budget and all required sections | | |
| D9 | Language law is 30% English / 70% Egyptian-colloquial Arabic with the correct functional split | | |
| D10 | One coherent idea per student slide; no passive video-only slide | | |
| D11 | TATA is intentional and uses only confirmed states | | |
| D12 | Brand chrome uses confirmed Techno Square identity assets | | |
| D13 | All activities are identifiable and run as the trainer guide specifies | | |
| D14 | Learning objective and observable success criterion agree | | |
| D15 | Predict, build, test, debug, and explain are represented where the source requires them | | |
| D16 | Section A, Section B, and Section C agree when reviewed side by side | | |
| D17 | Every required asset is classified as `REFERENCE` or `EVIDENCE` | | |
| D18 | Every asset status uses the exact three-state vocabulary | | |
| D19 | Every required asset is `Produced and mapped` | | |
| D20 | Every mapped absolute path resolves on disk | | |
| D21 | Evidence regions are reserved for post-export overlay and never redrawn | | |
| D22 | No unresolved `GAP - owner must decide` remains | | |

## Approval record

- **Owner decision:** `Pending`
- **Owner name:** `<fill>`
- **Decision date:** `<fill>`
- **Approved exceptions:** `<None or explicit list>`

> Changing the frontmatter status is an execution authorization. Do not change it to an approved state until the owner has reviewed Sections A, B, C, the asset table, and Section D side by side.
