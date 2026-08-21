---
name: hermes-delegate
description: Delegate a scoped, read-only research or analysis task to the locally installed Hermes agent CLI as a swarm worker, then collect its output from a single lane file. Use when the swarm assigns Hermes a provenance or research lane, or when the user asks to run something through Hermes. Do not use for tasks small enough to do inline, or for anything that writes learner-facing Arabic.
---

# hermes-delegate

Runs Hermes as one worker inside the Micro:bit course swarm.

## Executable

Hermes is not on PATH. Always invoke by absolute path:

```
C:/Users/ET/AppData/Local/hermes/hermes-agent/venv/Scripts/hermes
```

## Invocation

Non-interactive only. Never open the TUI. Use `hermes -z` for a one-shot, non-interactive prompt.

```bash
timeout 300 "C:/Users/ET/AppData/Local/hermes/hermes-agent/venv/Scripts/hermes" \
  -z "<prompt>" \
  -m tencent/hy3:free --provider nous \
  --skills master-instructional-design \
  -t file,web \
  --safe-mode < /dev/null
```

- `-z` — one-shot prompt, no interactive session
- `-m tencent/hy3:free --provider nous` — **pinned model.** This is the only
  model verified against our free-tier Nous Portal account (see "Real latency,
  not a hang" below). Do not drop this flag: without it the call falls back to
  the account's current default, which can drift if the Portal's free-tier
  offering changes.
- `--skills` — load the shared pedagogy skill so Hermes judges by the same rules as every other lane
- `-t` — toolsets; Hermes owns the web-research lanes
- `--safe-mode` — Hermes is a research worker, not an editor
- `< /dev/null` — always redirect stdin; a task launched detached/backgrounded
  with no stdin attached can otherwise stall waiting on input that never comes
- `timeout 300` — a real multi-file research task (glob-read several
  contracts/provenance files, synthesize claims, write JSON) takes 90–220s on
  this free-tier model. 300s gives headroom without hanging forever if a call
  genuinely wedges.

### Real latency, not a hang (verified 2026-08-21)

A prior string of failures looked like hangs (process alive, 0 CPU, 0 bytes
written, killed after 12–15 min). Isolated with a one-variable-at-a-time
matrix of foreground calls:

- Trivial prompts (`"reply PONG"`) with any flag combination (`--safe-mode`,
  `-t web`, `-t file,web`, `--skills`) return in 15–26s.
- Read-only prompts (single file, or a glob like `00-contracts/**`) return in
  30–90s.
- Write-only prompts return in ~40s (and Hermes' own write_file tool refuses
  non-JSON content into a `.json` path with a clear error — no hang).
- The **combination** — glob-read several files, synthesize a schema'd JSON
  answer, write it — legitimately takes 90–220s on `tencent/hy3:free`. Killed
  at a 100s timeout, this looks identical to a hang (nothing written yet) but
  is just the model still working. Given 240–300s, every attempt completed
  with valid, schema-conformant JSON.
- **Root cause of the historical 12–15 min hangs was not reproduced** in 8
  sequential foreground attempts here. The one documented condition that
  reliably breaks Hermes output is parallel invocation (silently drops
  output, see below) — the earlier hangs most likely occurred during a
  fanout batch that ran hermes concurrently with itself or another provider.
  If a true >5min zero-CPU freeze recurs on a strictly sequential, `< /dev/null`,
  timeout-wrapped call, that is a new failure mode, not this one — capture the
  exact command and file it.

## Adapter contract

Every provider adapter in this swarm obeys the same three rules. Hermes is no exception.

0. **Read `00-contracts/agent-memory.md` first.** Shared second-brain for every agent on this job (claude, codex, opencode, hermes) — provider quirks, pipeline decisions, and schema gotchas already learned. Always in scope regardless of the task's `reads_allowed`.
1. **Read only what is declared.** The task's `reads_allowed` frontmatter is the complete read scope beyond agent-memory.md. Do not explore the vault.
2. **Write exactly one lane file.** Path is derived, never chosen:
   - research lane → `30-research/_lanes/<cluster>/hermes.json`
   - provenance → `20-provenance/<session-id>.md`
   One writer per file is what lets three providers run concurrently without locking.
3. **Emit a token receipt.** Report tokens consumed so `90-receipts/` stays accurate.

## Hard rules

- **Do not use `hermes moa`.** Mixture-of-Agents hides divergence inside a single call. Cross-provider divergence is the signal this project exists to produce; collapsing it into one opaque answer defeats the design.
- **Do not treat `hermes memory-graph` as truth.** The vault is the single source of truth. The memory graph is scratch within a run, never authoritative, and is never read by another provider.
- **Do not write Arabic.** All swarm stages operate in structured English. Localisation to 30/70 bilingual is a Claude-only stage (S5b).
- **Cite every claim.** Output feeding REFINE must carry a source URL or Brain OS rule reference. Uncited items are dropped by `cite_filter.py` before a judge ever sees them.

## Failure handling

If Hermes exits non-zero or produces no lane file, report the failure and stop. Do not retry more than twice. One dead lane out of three is tolerated by the swarm; do not silently substitute another provider.
