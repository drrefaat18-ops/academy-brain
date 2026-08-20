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
"C:/Users/ET/AppData/Local/hermes/hermes-agent/venv/Scripts/hermes" \
  -z "<prompt>" \
  --skills master-instructional-design \
  -t web \
  --safe-mode
```

- `-z` — one-shot prompt, no interactive session
- `--skills` — load the shared pedagogy skill so Hermes judges by the same rules as every other lane
- `-t` — toolsets; Hermes owns the web-research lanes
- `--safe-mode` — Hermes is a research worker, not an editor

## Adapter contract

Every provider adapter in this swarm obeys the same three rules. Hermes is no exception.

1. **Read only what is declared.** The task's `reads_allowed` frontmatter is the complete read scope. Do not explore the vault.
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
