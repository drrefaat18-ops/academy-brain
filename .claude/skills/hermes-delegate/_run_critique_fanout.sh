#!/usr/bin/env bash
set -uo pipefail
cd /d/vault/Microbit

HERMES="C:/Users/ET/AppData/Local/hermes/hermes-agent/venv/Scripts/hermes"
MODEL="opencode/x-preview-f-free"

SCHEMA='Return ONLY valid JSON (no markdown fence, no prose) matching: {"session":"<ID>","provider":"<name>","issues":[{"loc":"<slide-N or block-name>","severity":"high|medium|low","type":"pedagogy|technical|assessment|differentiation|other","problem":"<one sentence>","fix":"<one sentence>","cites":["<URL or MID:principle-name>"]}]}. Every issue MUST have at least one cite. 3-8 issues. Critique, do not rewrite.'

PROMPT_BASE() {
  local sid="$1"
  echo "You are a lane for critique stage (40-critique) in the Micro:bit course swarm, session ${sid}. Read 00-contracts/agent-memory.md, 10-digest/${sid}.md, 20-provenance/${sid}.md, and 30-research/T01.md through T05.md. Critique the session's pedagogy, technical accuracy (MakeCode blocks), assessment, and differentiation against the R0 missing[] gaps and the research clusters. ${SCHEMA} Do not write Arabic."
}

for sid in L1-s1 L1-s2 L1-s3 L1-s4 L1-s5 L1-s6; do
  mkdir -p "40-critique/${sid}"

  echo "=== ${sid} / codex ==="
  codex exec --skip-git-repo-check "$(PROMPT_BASE "$sid") You are the codex lane. Write the JSON to 40-critique/${sid}/codex.json (create/overwrite). Do not write anywhere else." < /dev/null

  echo "=== ${sid} / opencode ==="
  raw=$(timeout 150 opencode run -m "$MODEL" "$(PROMPT_BASE "$sid") You are the opencode lane. Reply with the JSON only on stdout — you do not have file write access.")
  echo "$raw" | awk 'BEGIN{s=0} /{/{s=1} s{print} /^}/{if(s)exit}' > "40-critique/${sid}/opencode.json"
  if [ ! -s "40-critique/${sid}/opencode.json" ]; then
    echo "WARN: ${sid} opencode extraction empty"
    echo "$raw" > "40-critique/${sid}/opencode.raw.txt"
  fi

  echo "=== ${sid} / hermes ==="
  timeout 300 "$HERMES" -z "$(PROMPT_BASE "$sid") You are the hermes lane. Write the JSON to 40-critique/${sid}/hermes.json (create/overwrite). Do not write anywhere else. Report token usage at the end." \
    -m tencent/hy3:free --provider nous \
    --skills master-instructional-design -t file,web --safe-mode < /dev/null
done
echo CRITIQUE_FANOUT_DONE
