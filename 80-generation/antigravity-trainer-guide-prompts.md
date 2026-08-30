---
stage: generation
owner: claude
status: draft
usage: manual — owner runs these in the Antigravity IDE (no headless CLI)
renders: Trainer Guide ONLY (one PDF, whole level)
not_this_file: >-
  Student Slide Deck and Student Summary deck are NotebookLM artifacts, not
  Antigravity. See 75-bundle/L1-sN/SOURCES.md.
contract: 00-contracts/brand-and-output.md §1b
---

# Antigravity Trainer Guide — Manual Prompts

Antigravity has no headless CLI. The owner runs these two prompts by hand in the
Antigravity IDE.

**Scope:** ONE Techno Square-themed PDF covering all 6 Level 1 sessions. Do not
split per session. Do not spend NotebookLM quota on this — NBLM is reserved for
the two student-facing decks per session.

**Prerequisite:** `75-bundle/L1-sN/trainer-guide.md` must exist for every session
being included. Currently only L1-s1 exists — S2–S6 drafts are still to be written.

## 1. Landing prompt (session/context setup)

Paste this first, in a fresh Antigravity session.

```
You are producing the Trainer Guide PDF for the Techno Square Academy micro:bit
course, Level 1. This is an INTERNAL, TRAINER-ONLY document.

Read these trainer guide drafts — they are the content source of truth:
D:\vault\Microbit\75-bundle\L1-s1\trainer-guide.md
(through L1-s6\trainer-guide.md as they become available)

Each draft is already QA-approved: session goal, materials checklist, timed
segment flow, facilitation script, answer key, common mistakes, assessment
checklist, and classroom management notes. Do not alter its pedagogy, timings,
sequencing, or claims. Your job is presentation, not authorship.

Read the brand doctrine and apply it as the visual system:
D:\vault\Microbit\00-contracts\brand-and-output.md
D:\vault\Microbit\Abdeen_Moon_OS_Docs\Academy_Brain_OS\Techno_Square_Branding_Rule.md
D:\vault\Microbit\Abdeen_Moon_OS_Docs\Academy_Brain_OS\Tata_Mascot_Usage Guide.md

Brand assets:
D:\vault\Microbit\Techno Square identity\PNG\landscape logo.png
D:\vault\Microbit\Techno Square identity\TATA\   (mascot poses)

Visual system: Techno Square logo as official identity. Dark/black accents with
yellow/gold highlights. Large titles. Icons, arrows, simple shapes. Clean, not
crowded. Child-friendly where student-facing content is quoted, professional
where trainer-facing.

Language: the drafts are bilingual, 30% English / 70% Egyptian-colloquial Arabic.
Preserve that balance exactly and keep all Arabic right-to-left correct. Do not
re-translate, re-balance, or re-sequence anything.

TATA mascot: intentional use only, per the four documented states
(Excited / Idea / Thinks / Approved). Not on every page. Optional in a trainer
document — use sparingly, mainly on session dividers.

Confirm you have read every trainer guide draft and the brand doctrine before I
send the generation prompt.
```

## 2. Generation prompt (fires the PDF build)

Send only after Antigravity confirms it has read the sources above.

```
Generate the Level 1 Trainer Guide as a single Techno Square-themed PDF.

Structure:

1. Cover page — Techno Square Academy branding, "micro:bit Level 1 — Trainer
   Guide", session count, "Internal use only" marking.
2. How to use this guide — one page: the academy teaches interactively; video
   links in this guide are trainer prep only and must never be shown as a
   student slide.
3. Table of contents — 6 sessions.
4. One section per session (S1–S6), each reproducing its draft in full:
   - Session title + goal
   - Target age and prerequisites
   - Materials / setup checklist (as printable checkboxes)
   - Session flow table with per-segment timing
   - Segment-by-segment facilitation script
   - Answer key
   - Common mistakes table
   - Assessment checklist (printable checkboxes)
   - Classroom management notes
   - Trainer resources (clearly marked NOT for student slides)

Formatting requirements:
- Each session starts on a new page with a branded divider.
- Timing tables and common-mistakes tables render as real tables, not prose.
- Checkboxes are printable squares — trainers tick these during class.
- Arabic renders right-to-left, correctly shaped, never reversed or broken.
- Page footer: Techno Square Academy + page number + "Internal use only".

Output: a single PDF named "TechnoSquare_microbit_L1_TrainerGuide.pdf".
Save it to D:\vault\Microbit\80-generation\.
```

## Known issue to check on output

Antigravity's PDF pipeline has broken Arabic shaping in the past. Per
`AI_Tools_Workflow_Guide.md`, Canva is the sanctioned fallback for *"fixing
Arabic text if AI image output breaks it"*. Inspect the Arabic on the first
generated page before accepting the whole PDF.
