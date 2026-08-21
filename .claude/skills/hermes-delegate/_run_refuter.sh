#!/usr/bin/env bash
set -uo pipefail
cd /d/vault/Microbit

SCHEMA='Return ONLY valid JSON (no markdown fence, no prose) matching: {"session":"<ID>","verdicts":[{"loc":"<loc from patch file>","verdict":"survives|refuted","reasoning":"<one sentence>","stronger_cite":"<url or MID, only if verdict=refuted and you have one that outranks the patch cites>"}]}. Only refute a patch if you can cite a source that is EQUALLY OR MORE grounded than its existing cites (an upstream microbit.org/makecode URL, or a stronger pedagogical principle) — do not refute on stylistic preference or "could word it differently." Default to survives when uncertain.'

for sid in L1-s1 L1-s2 L1-s3 L1-s4 L1-s5 L1-s6; do
  echo "=== ${sid} / refuter (codex) ==="
  codex exec --skip-git-repo-check "You are the refuter lane for stage 55-refuted in the Micro:bit course swarm, session ${sid}. Read 50-patch/${sid}.md. For EVERY entry with 'severity: high', attempt to refute it: argue it is wrong, unnecessary, or not actually a problem. ${SCHEMA} Write the JSON to 55-refuted/${sid}.raw.json (create/overwrite). Do not write anywhere else." < /dev/null
done
echo REFUTER_DONE
