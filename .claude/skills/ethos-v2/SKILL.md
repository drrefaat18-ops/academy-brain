---
name: ethos-v2
description: "EthOS v2 — the Micro:bit course vault's content-generation doctrine, successor to the AI course's EthOS. Governs what correct output is at every pipeline stage: quality gates, the QA verdict loop, brand and language law, and the kids-track rules. Invoke when producing, checking, or generating any course artifact in this vault. Does not schedule work — ruflo does that."
---

# EthOS v2

Successor to EthOS, rebuilt for the Techno Square Micro:bit course. Keeps what EthOS learned through real production failures; reverses the adult-audience decisions that are wrong for a kids track.

## Doctrine, not scheduling

EthOS v2 answers **"what is correct?"** — gates, rules, verdicts, brand and language law.
Ruflo answers **"what runs next?"** — spawning, parallelism, memory, handoffs.

**EthOS v2 never decides scheduling.** Ruflo never decides quality. Without this split, a full-pipeline doctrine becomes a second conductor and the two fight.

## Do not generate on invocation alone

Loading this skill does not mean "start generating." Produce output only when given an explicit target — a session ID, a file, or a named artifact. If invoked with no target, ask.

## Diagnose before produce

State what you are about to generate — which session, which source files, which output type — before calling any generator. This is EthOS's single most reusable habit, confirmed against live production evidence.

## The QA verdict loop

Detection is not the deliverable. A QA phase that reports without closing the loop is note-taking.

After running gates you must:

1. **State an explicit verdict per gate** — `PASS` / `FAIL` / `UNVERIFIED`. No prose hedging. A gate you could not run is `UNVERIFIED`, never silently omitted.
2. **Classify every FAIL by cause**, because the cause determines the fix:
   - *prompt/parameter* → regenerate now with the named change (max 3 retries)
   - *source-content* → the artifact cannot be better than its source; fix the upstream stage, then regenerate (max 2)
   - *external limit* → apply the known workaround (e.g. the ~21-slide NotebookLM cap → split and merge)
   - *needs judgment* → escalate
3. **Act in the same turn.** Do not batch defects for a later cleanup pass.

## Deterministic gates

Model opinion is never the final check on something mechanically checkable. Run via `scripts/swarm/gate_runner.py`:

| gate | catches |
| --- | --- |
| `arabic-ratio` | deviation from the literal 30% English / 70% Arabic rule |
| `cite-filter` | change proposals that cite no source |
| `trainer-boundary` | trainer-only content leaking into student-facing output |
| `brand-palette` | retired brand colors, notably `#F5B301` |

## Documented blind spots

Inherited honestly from EthOS. These are real limits, not caveats to wave at:

- **OCR cannot see a missing connector arrow.** N steps require exactly N-1 arrows, all pointing the same direction, right-to-left in Arabic decks. This slipped through a full QA pass once already.
- **OCR cannot see an unlabelled blank placeholder.** A blank box has no text to read.
- **OCR cannot see duplicated diagram nodes.** Visual duplication is outside what a text checker can reach.

Visual review remains mandatory. It is the only control covering this class of defect.

## Kids-track rules

See `references/kids-track-rules.md` for the full adult→kids reversal table.
