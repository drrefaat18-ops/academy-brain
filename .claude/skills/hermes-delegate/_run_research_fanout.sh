#!/usr/bin/env bash
set -uo pipefail
cd /d/vault/Microbit

HERMES="C:/Users/ET/AppData/Local/hermes/hermes-agent/venv/Scripts/hermes"

declare -A TOPIC
TOPIC[T01]="Differentiation strategies for a micro:bit kids-track intro unit (ages read from Brain OS context-pack if available, else assume 8-11): how do published micro:bit / CS-education sources recommend supporting struggling learners and stretching advanced learners within a single short lesson (forever loop, show string/icon, pause, if/then, shake, random blocks)? Applies to L1-s1 through L1-s6."
TOPIC[T02]="Assessment design for a micro:bit intro-unit lesson aimed at kids: what lightweight, non-written formative assessment patterns (exit-ticket questions, demo-based checks, peer-share prompts) fit a single ~45-60 min session teaching MakeCode blocks? Applies to L1-s1, L1-s3, L1-s4, L1-s6."
TOPIC[T03]="Answer-key / worked-solution conventions for short MakeCode block programs (name badge, beating heart, emotion badge, step counter, nightlight, rock-paper-scissors): what block sequence and structure count as the canonical correct solution, and what common kid mistakes should an answer key flag? Applies to L1-s1, L1-s2, L1-s4, L1-s5, L1-s6."
TOPIC[T04]="MakeCode block/API technical reference: exact behavior and parameters of forever, show string, show icon, pause, if/then/else, on shake, pick random, input.acceleration/on-shake gesture — cite makecode.microbit.org/reference pages. Applies to L1-s1 through L1-s6, grounds technical-accuracy critique."
TOPIC[T05]="microbit.org 'Introduction to the micro:bit' unit pedagogy (Think/Create/Evaluate/Extend/Share model) and how it should adapt for a young kids track per general instructional-design best practice (age-appropriate pacing, one-idea-per-slide, concrete physical examples). Applies to L1-s1 through L1-s6."

SCHEMA='Return ONLY valid JSON (no markdown fence) matching this shape: {"cluster":"<ID>","provider":"<name>","claims":[{"claim":"<research finding, one sentence>","source":"<URL or MID:principle-name>","applies_to":["L1-sN", ...]}]}. Every claim MUST have a source. 3-8 claims. No prose outside the JSON.'

for id in T01 T02 T03 T04 T05; do
  topic="${TOPIC[$id]}"
  echo "=== $id / codex ==="
  codex exec --skip-git-repo-check "You are the codex lane for research cluster ${id} in the Micro:bit course swarm. Working dir D:\\vault\\Microbit. Read ONLY 00-contracts/** and 20-provenance/L1-s*.md relevant to: ${topic} Research topic: ${topic} ${SCHEMA} Write the JSON to 30-research/_lanes/${id}/codex.json (create the file, overwrite if exists). Do not write anywhere else. Do not write Arabic." < /dev/null

  echo "=== $id / gemini ==="
  gemini -p "You are the gemini lane for research cluster ${id} in the Micro:bit course swarm. Working dir D:\\vault\\Microbit. Read ONLY 00-contracts/** and 20-provenance/L1-s*.md relevant to: ${topic} Research topic: ${topic} ${SCHEMA} Write the JSON to 30-research/_lanes/${id}/gemini.json (create the file, overwrite if exists). Do not write anywhere else. Do not write Arabic."

  echo "=== $id / hermes ==="
  timeout 300 "$HERMES" -z "You are the hermes lane for research cluster ${id} in the Micro:bit course swarm. Working dir D:\\vault\\Microbit. Read ONLY 00-contracts/** and 20-provenance/L1-s*.md relevant to: ${topic} Research topic: ${topic} ${SCHEMA} Write the JSON to 30-research/_lanes/${id}/hermes.json (create the file, overwrite if exists). Do not write anywhere else. Do not write Arabic. Report token usage at the end." \
    -m tencent/hy3:free --provider nous \
    --skills master-instructional-design -t file,web --safe-mode < /dev/null
done
echo ALL_LANES_DONE
