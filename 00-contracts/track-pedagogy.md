---
stage: contracts
owner: claude
status: living
purpose: >-
  Defines `track` — the optional pedagogical category a course may declare in
  its manifest — and states which format decisions are track-conditional
  versus academy-wide. Cross-referenced from pedagogy.md §4.
---

# Track pedagogy

## 1. What `track` is, and is not

`track` is a course-manifest field (`course.yaml`, optional, `""` if
undeclared) naming which of the academy's five pedagogical tracks a course
belongs to. The vocabulary is not invented here — it is Abdeen's own academy
roadmap, `Abdeen_Moon_OS_Docs/Academy_Brain_OS/Techno_Square_Roadmap_Knowledge.md`
(kept in this vault only, never scaffolded — it names specific example
courses, some by other vendors' product names, which is exactly the kind of
course-specific naming a shared contract must not carry into every new
course). This file registers the vocabulary; that file is where to read the
full picture, including which example courses the owner associated with each
track and their typical ages.

| Track | Style |
|---|---|
| `early-childhood-tech` | playful, visual, mascot-supported, very low text |
| `kids-hardware` | hands-on, project-based, guided step-by-step |
| `kids-software` | visual, playful, story-driven |
| `stem-engineering` | project/challenge-based, debugging and reflection |
| `professional-technology` | structured, technical, career-oriented, assessment-driven |

Value is one of the five slugs above, or `""` for undeclared. This is NOT
machine-enforced yet — `config.py` accepts any single-line string. Treat the
five values above as the correct vocabulary regardless.

**`track` is not `audience`.** The roadmap's example courses each carry a
typical age, but that number is guidance for picking a track, not a value to
copy into `audience`. A real course's `audience` is its own declared fact
(pedagogy.md §4), independent of what the roadmap's example course for that
track looked like. Two courses can share a track and declare different
audiences, or share an audience and sit in different tracks — do not collapse
the two into one field, and never infer one from the other.

This file exists because an earlier document
(`.claude/skills/ethos-v2/references/kids-track-rules.md`) framed several
format decisions as "adult EthOS vs. kids EthOS v2" reversals, scoped to two
specific courses by name. That framing does not travel: a third course is
neither of those two, and most of what it reversed has since been settled
one way, academy-wide, below.

## 2. Already academy-wide — NOT track-conditional

The following are binding for every course regardless of track. Do not write
a track-specific override for any of these; if a course seems to need one,
that is a conflict with `00-contracts/brand-and-output.md` to raise, not a
track rule to add here.

- **One idea per slide.** No crowded slides, large titles, simple shapes.
  (`brand-and-output.md` §3)
- **TATA mascot, all four states**, used with intent, never on every slide
  and never absent. (`brand-and-output.md` §4)
- **30% English / 70% Arabic**, and the Arabic must be simple, short,
  age-appropriate, beginner-friendly, and RTL-correct.
  (`brand-and-output.md` §5)
- **Home Summary's five sections and Parent Talk** are required, not an
  optional restoration for one track. (`brand-and-output.md` §1c)
- **No video-only slides.** (`brand-and-output.md` §7)
- **Logo on first/last slide only.** (`brand-and-output.md` §3)

## 3. Genuinely track-conditional — a course may vary these

- **Examples and visuals.** Calibrated to the declared audience (age,
  experience), not to a track label — this already follows from `audience`
  and needs no separate track rule.
- **Explanation depth within the academy language law.** The mandatory 30/70
  ratio and simple, short Arabic remain academy-wide; the source contract's
  ban on adult-level explanation is explicitly scoped to a kids track
  (`brand-and-output.md` §5). Calibrate depth to the declared `audience`; do
  not infer it from `track` alone.

None of the format dimensions the retired reversal table covered survive as
track-conditional once §2 is accounted for. If a future course needs a real
track-conditional format rule, add it here with the same evidence discipline
as everything else in `00-contracts/` — a stated rationale, not an inherited
assumption from one course's decisions.

## 4. Open conflict — Trainer Guide cadence (unresolved, do not silently pick a side)

The contracts leave the relationship between Trainer Guide drafts and the
final guide unresolved:

- `topology.md` (generated per-course by `new_course.py` from the stage
  shape) describes `75-bundle` as **per-session**: one
  `trainer-guide.md` per session folder.
- `brand-and-output.md` §1 requires that per-session draft in each student
  deck's source bundle, while §1b also requires **one level-wide final PDF**
  that must not be split per session.
- `pipeline-lessons.md` §7 names "an independent **level-wide** Trainer Guide
  track" as a distinct thing from per-session lock state.

The contracts do not say whether or how the per-session drafts aggregate into
the level-wide final PDF, or which stage owns that final artifact. A course
specialist or producer that hits this should record the ambiguity in its
receipt's `holes` list (per the specialist's own stop-condition discipline)
rather than resolve it by assumption. This is an owner decision, not a
specialist judgment call.
