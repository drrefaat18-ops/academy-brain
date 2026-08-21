#!/usr/bin/env bash
set -uo pipefail
cd /d/vault/Microbit

MODEL="opencode/x-preview-f-free"

declare -A TOPIC
TOPIC[T01]="Differentiation strategies for a micro:bit kids-track intro unit (ages read from Brain OS context-pack if available, else assume 8-11): how do published micro:bit / CS-education sources recommend supporting struggling learners and stretching advanced learners within a single short lesson (forever loop, show string/icon, pause, if/then, shake, random blocks)? Applies to L1-s1 through L1-s6."
TOPIC[T02]="Assessment design for a micro:bit intro-unit lesson aimed at kids: what lightweight, non-written formative assessment patterns (exit-ticket questions, demo-based checks, peer-share prompts) fit a single ~45-60 min session teaching MakeCode blocks? Applies to L1-s1, L1-s3, L1-s4, L1-s6."
TOPIC[T03]="Answer-key / worked-solution conventions for short MakeCode block programs (name badge, beating heart, emotion badge, step counter, nightlight, rock-paper-scissors): what block sequence and structure count as the canonical correct solution, and what common kid mistakes should an answer key flag? Applies to L1-s1, L1-s2, L1-s4, L1-s5, L1-s6."
TOPIC[T04]="MakeCode block/API technical reference: exact behavior and parameters of forever, show string, show icon, pause, if/then/else, on shake, pick random, input.acceleration/on-shake gesture — cite makecode.microbit.org/reference pages. Applies to L1-s1 through L1-s6, grounds technical-accuracy critique."
TOPIC[T05]="microbit.org 'Introduction to the micro:bit' unit pedagogy (Think/Create/Evaluate/Extend/Share model) and how it should adapt for a young kids track per general instructional-design best practice (age-appropriate pacing, one-idea-per-slide, concrete physical examples). Applies to L1-s1 through L1-s6."

for id in T01 T02 T03 T04 T05; do
  topic="${TOPIC[$id]}"
  echo "=== $id / opencode ==="
  mkdir -p "30-research/_lanes/${id}"
  raw=$(timeout 90 opencode run -m "$MODEL" "You are the opencode lane for research cluster ${id} in the Micro:bit course swarm. Answer directly from your own knowledge — do NOT read or search any files. (If you need context, 00-contracts/agent-memory.md has provider quirks and pipeline decisions, but for this task your own knowledge is enough.) Research topic: ${topic} Return ONLY valid JSON (no markdown fence, no prose) matching: {\"cluster\":\"${id}\",\"provider\":\"opencode\",\"claims\":[{\"claim\":\"<finding>\",\"source\":\"<URL or MID:principle-name>\",\"applies_to\":[\"L1-sN\"]}]}. 3-8 claims, every claim needs a source and applies_to. Do not write Arabic." 2>&1)
  echo "$raw" > "30-research/_lanes/${id}/opencode.raw.txt"
  echo "$raw" | awk 'BEGIN{s=0} /{/{s=1} s{print} /^}/{if(s)exit}' > "30-research/_lanes/${id}/opencode.json"
  if [ -s "30-research/_lanes/${id}/opencode.json" ]; then
    echo "wrote 30-research/_lanes/${id}/opencode.json"
    rm -f "30-research/_lanes/${id}/opencode.raw.txt"
  else
    echo "WARN: ${id} opencode extraction empty, raw kept for inspection"
  fi
done
echo OPENCODE_FANOUT_DONE
