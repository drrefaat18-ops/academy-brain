---
stage: contracts
owner: claude
status: living
purpose: >-
  Recovered Techno Square Academy production doctrine (moonOS / Abdeen), restated
  as binding contract for EthOS v2. This is the continuity guarantee: output must
  feel like what Abdeen shipped, improved — not replaced.
sources:
  - Abdeen_Moon_OS_Docs/Academy_Brain_OS/AI_Tools_Workflow_Guide.md
  - Abdeen_Moon_OS_Docs/Academy_Brain_OS/Production_Workflow_and_SAVE_Mode.md
  - Abdeen_Moon_OS_Docs/Academy_Brain_OS/Techno_Square_Branding_Rule.md
  - Abdeen_Moon_OS_Docs/Academy_Brain_OS/Tata_Mascot_Usage Guide.md
  - Abdeen_Moon_OS_Docs/Academy_Brain_OS/Academy_Language_and_Output_Rules.md
  - Abdeen_Moon_OS_Docs/Academy_Brain_OS/Techno_Square_QA_Checklist.md
---

# Brand and Output Contract

## 0. Root cause this contract exists to close

The L1-s1 generation attempt fed NotebookLM **one** source: a text-only
`70-localized/L1-s1.md`. Abdeen's own doctrine requires **seven**. Every defect
in that deck (no logo, no TATA, no original course assets, passive video links)
follows from that single omission. NotebookLM is the correct renderer. The
source bundle was wrong.

## 1. NBLM source bundle — MANDATORY

Verbatim from `AI_Tools_Workflow_Guide.md`, "For Student Slides, use":

| # | Source | Vault origin for this project |
| --- | --- | --- |
| 1 | lesson material | `70-localized/L1-sN.md` |
| 2 | trainer guide | `75-bundle/L1-sN/trainer-guide.md` (see §2) |
| 3 | educational decision note | `75-bundle/L1-sN/decisions.md` |
| 4 | branding rules | `Techno_Square_Branding_Rule.md` |
| 5 | Tata guide | `Tata_Mascot_Usage Guide.md` |
| 6 | key robot/project images | `10-digest/_assets/L1-sN/` (curated subset) |
| 7 | key code screenshots | `10-digest/_assets/L1-sN/` (curated subset) |

Also mandated: **"NotebookLM works best when sources are focused. Do not overload
NotebookLM with too many files."** Curate the 56 digest assets down to the key
ones. Do not dump the folder. Avoid: unrelated previous sessions, too many raw
screenshots, trainer-only overload.

Generating student slides from fewer than these sources is a contract violation,
not a quality issue.

## 1b. Renderer routing — NBLM quota is scarce

NotebookLM generation is rate-limited. It is spent on the artifact only it can
produce well, and nothing else.

| Artifact | Renderer | Run mode | Input |
| --- | --- | --- | --- |
| **Student Slides** | **NotebookLM** | MCP, claude-run | the 7-source bundle, §1 |
| **Trainer Guide** | **Antigravity** | manual, owner-run | `trainer-guide.md` draft + template + logo + optional TATA |
| **Student Summary deck** | **NotebookLM** | MCP, claude-run | `home-summary.md` + logo + TATA + key project images |

Trainer Guide is **one single PDF**, Techno Square themed, covering the level.
Do not split it per session, and do not spend NBLM on it.

**Student Summary is a slide deck, not a document.** Per session, generated in
NotebookLM alongside the main deck. Fixed length:

- **3 slides** for s1–s6 (teaching sessions)
- **2 slides** for s7 (revision)
- **none** for s8 (graduation project)

So NBLM is spent twice per session: one full student deck, one 3-slide summary
deck. Everything else is Antigravity. This matches `AI_Tools_Workflow_Guide.md`,
which lists both Student Slides and Home Summary under NotebookLM.

## 1c. Student Summary deck — required sections

From `Techno_Square_QA_Checklist.md`, Home Summary QA. All five sections are
mandatory, compressed across the fixed 3-slide budget:

1. **Today I Learned** — النهاردة اتعلمت
2. **New Words** — كلمات جديدة (English term + short Arabic gloss)
3. **Review at Home** — نراجع في البيت
4. **Parent Talk** — كلام لولي الأمر
5. **Mini Activity** — نشاط صغير

Slide budget:

| Slide | Carries |
| --- | --- |
| 1 | Today I Learned + New Words |
| 2 | Review at Home + Mini Activity |
| 3 | Parent Talk |

Must be parent-friendly, student-friendly, short, visual. Must contain no
trainer-only content (no timings, no scripts, no assessment checklists).

## 1d. Level shape — owner ruling

Binding, stated by the academy owner:

| Sessions | Role | Artifacts |
| --- | --- | --- |
| **s1–s6** | teaching | full student deck + 3-slide summary each |
| **s7** | revision | full student deck + **2**-slide summary |
| **s8** | graduation project | **none** — no artifacts generated |

**Every Techno Square session is 120 minutes.** Owner ruling, all courses, all
levels. Upstream vendor decks are typically built for
60-minute lessons — roughly half a session. Content must be expanded to fill 120 minutes with substance, not
padding. Per the academy's own trainer framework
(`Think → Build → Test → Debug → Explain`), the added time goes to:

- predict-before-run on every build step
- test after every mechanic, not once at the end
- a deliberate debugging segment — break the code on purpose, students fix it
- students explaining their own code (the academy's primary evidence of learning)
- extension challenges for fast finishers
- an exit ticket in the closing minutes

Session flow is stated as a **clock-time timeline** (`00:00-00:10`), matching the
shipped PictoBlox trainer guide, not as bare durations.

So a level produces **7** student decks and **7** summary decks, not 8. The
Trainer Guide (one PDF) covers the level.

Do not treat the absence of s8 artifacts as a gap. Do not generate anything for
s8.

## 1e. Ingestion mechanism — how images actually reach a slide

Settled by the owner, who previously built a package-prep tool for exactly this.

**The mechanism:** upload the image files as notebook *sources*, and have the text
package name each image and say where it goes. NotebookLM places them during
generation. The `- **Asset:** img-NN.png` line on each slide in
`slides-source.md` IS that instruction — it is load-bearing, not a comment.

**Tooling.** The `notebooklm` MCP server exposes only `add_source_text` and
`add_source_url`. It has **no file-upload tool**. This is a gap in the MCP
wrapper, *not* in the underlying tool: the CLI supports it directly.

```
notebooklm source add -n <notebook_id> --type file --title "<name>" <path>
```

`--type` accepts `url|text|file|youtube`; `--mime-type` overrides extension
inference. Same auth and profile as the MCP (`~/.notebooklm/profiles/<profile>/`).

So ingestion splits across two surfaces, deliberately:

| Step | Surface |
| --- | --- |
| create notebook | MCP `create_notebook` |
| add image sources | **CLI** `notebooklm source add --type file` |
| add text sources | CLI `--type file` (markdown) or MCP `add_source_text` |
| generate deck | MCP `generate_slide_deck` |

Do **not** conclude from the missing MCP tool that images cannot be uploaded and
degrade to a text-only generation. That reproduces the exact §0 failure — no
logo, no TATA, no course assets. If the MCP lacks a capability, check the CLI
before escalating.

**Run the CLI with `--active`, or clear `VIRTUAL_ENV` first.** Invoked from the
vault root it inherits that vault's own `VIRTUAL_ENV=<vault>/.venv`, which shadows the
server's own environment. Same shadowing broke the MCP registration once already.

## 2. Trainer Guide is mandatory and comes FIRST

From `Academy_Language_and_Output_Rules.md`: *"The only fixed output across all
Techno Square Academy courses is: Trainer Guide. Every session must have a
Trainer Guide."*

From `Production_Workflow_and_SAVE_Mode.md`, official order:

```
Session Analysis -> Educational Architecture -> Required Assets
-> Trainer Guide Draft PDF -> Gemini Prompt -> Student Slides
-> Worksheet -> Home Summary -> QA Review -> SAVE / Progress Update
```

Student Slides are **downstream** of the Trainer Guide, and consume it as a
source. The current pipeline produced slides with no trainer guide in existence.
That ordering is now binding.

## 3. Brand chrome

- Techno Square logo is the official identity, present on student slides.
- Dark/black accents with yellow or gold highlights.
- Large titles. Icons, arrows, simple shapes, clear images. No crowded slides.
- **One idea per slide.**
- Child-friendly, colourful, clean and playful.

## 4. TATA mascot — intentional use only

Four states, each with a defined trigger. TATA is a guide, not decoration.

| State | Use on |
| --- | --- |
| `Tata_Excited` | welcome, mission intro, build time, fun challenges |
| `Tata_Idea` | new concept, new vocabulary, key learning point |
| `Tata_Thinks` | thinking questions, prediction, debugging, problem-solving |
| `Tata_Approved` | success, completed challenge, recap, goodbye |

**Do not use Tata on every slide.** Absence of TATA is a defect; TATA on every
slide is also a defect.

## 5. Language law (confirmed origin of the 30/70 rule)

30% English / 70% Arabic. English carries: course/session titles, STEM terms,
programming terms, block names, robotics vocabulary, activity names, tool names.
Arabic carries: explanations, trainer guidance, student instructions, parent
communication, concept clarification, engagement questions.

Arabic must be simple, short, age-appropriate, beginner-friendly, RTL-correct.
No heavy academic Arabic, no long paragraphs, no adult-level explanation on a
kids track.

## 6. Student-facing / trainer-facing separation

Student slides MUST NOT contain: trainer scripts, trainer timing, internal notes,
assessment checklists, classroom management notes, private methodology, long
pedagogical explanations. Trainer Guide is **internal use only**.

This is a hard boundary — the existing `trainer_boundary` gate enforces it.

## 7. Interaction law (EthOS v2 addition)

Not in Abdeen's docs; added because upstream vendor decks tend to be video-first
and the academy is not. It first bit on the source decks this vault started
from; it is a standing law for every course, not a patch for one of them.

A slide whose only content is a video link is a **defect**. Every such slide is
replaced by a hands-on beat: predict -> try -> check, a build step, or a
trainer-led demo. Video URLs may survive only in the Trainer Guide as an
optional trainer resource, never as a student slide's payload.

Rationale: academy trainers teach interactively. A passive link transfers the
teaching job to YouTube.

## 8. QA checklist — Student Slides (binding gate criteria)

- visual
- age-appropriate
- not text-heavy
- one idea per slide
- English terms + Arabic explanation
- no trainer-only content
- Tata used intentionally
- branding consistent

## 9. What EthOS v2 changes vs moonOS

Kept: every rule above. Changed: the manual custom-GPT operator loop becomes a
multi-provider agentic swarm with deterministic gates and provenance receipts.
The doctrine is identical; the enforcement is now mechanical instead of relying
on one person remembering it. That person left.
