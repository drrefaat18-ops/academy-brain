---
stage: research
owner: claude
status: complete
derived_from:
- 20-provenance/L1-s1.md
- 20-provenance/L1-s2.md
- 20-provenance/L1-s3.md
- 20-provenance/L1-s4.md
- 20-provenance/L1-s5.md
- 20-provenance/L1-s6.md
---

# L1 Research Clusters (T01–T05)

Derived from R0 `missing[]` and `delta[]` fields across all 6 L1 sessions, per
spec §9 R1/R2 ("Clusters are derived from R0 output, not guessed"). All 6 L1
sessions trace to the same microbit.org "Introduction to the micro:bit" unit,
so research is topic-clustered rather than per-session.

| Cluster | Topic | Sessions it feeds | Gap evidence |
| --- | --- | --- | --- |
| T01 | Differentiation strategies for micro:bit kids track | L1-s1..s6 (all) | `missing: differentiation` in all 6 R0 files |
| T02 | Assessment design for micro:bit intro-unit lessons | L1-s1, s3, s4, s6 | `missing: assessment` in 4/6 |
| T03 | Answer-key / worked-solution conventions for MakeCode block programs | L1-s1, s2, s4, s5, s6 | `missing: answer_key` in 5/6 |
| T04 | MakeCode block/API technical reference (forever, show string, show icon, pause, if/then, shake, random, accelerometer) | L1-s1..s6 (all) | grounds REFINE's technical critique; every session's code depends on this block set |
| T05 | microbit.org unit pedagogy + Brain OS kids-track rubric alignment (Think/Create/Evaluate/Extend/Share vs age-band rules) | L1-s1..s6 (all) | structural pattern common to every session per R0 `delta.altered` |

N = 5, within spec's 5–7 target (capped 8).

Each cluster fans out to hermes, codex, opencode → `_lanes/<cluster>/<provider>.json`,
merged by claude (union + dedup by claim, no adjudication) → `<cluster>.md`.
