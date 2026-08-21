---
cluster: ethos-generation-method
provider: hermes
status: complete
question: What made "start s1" work in the Dr Mahmoud course, and what is missing in the Microbit vault?
evidence:
  - D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md (482 lines)
  - D:\vault\Microbit\.claude\skills\ethos-v2\SKILL.md
  - D:\vault\Microbit\00-contracts\brand-and-output.md (restated contract)
  - D:\vault\Microbit\75-bundle\L1-s1\SOURCES.md, slides-source.md
  - D:\vault\Microbit\scripts\swarm\check_assets.py, gate_runner.py, prepare.py
  - D:\vault\Microbit\.mcp.json
---

A. WHAT THE OPERATOR ACTUALLY TYPED

There is NO literal "start s1" command anywhere in either vault. A whole-vault
grep for "start s1..s9" returns only this research lane's own prior notes
(Microbit/30-research/_lanes/ethos-generation-method/claude.md). The real trigger
phrases are recorded in the original EthOS skill description:

  Dr mahmoud AI course/.claude/skills/ethos/SKILL.md:3
  "Trigger phrase 'ethos' / 'fire the deck' / 'generate the deck' / 'run ethos'
   (legacy 'moon os' / 'run moon os' still work)."

The single-word form the owner remembers was the TARGET, not the command.
EthOS itself states (SKILL.md:12-14): "This skill loading does NOT mean 'start
generating slides.' Only produce output when given an explicit target: a session
number, a file, or 'the deck.'"

So the verbatim interaction was one of:
    "ethos, generate Session 1's deck"
    "fire the deck"  (for s1)
    "run ethos"  +  the session number s1
The "s1" was the explicit target; "ethos"/"fire the deck" was the activator.
"start s1" is the owner's paraphrase, not a logged literal. MARKED: the exact
string "start s1" is UNVERIFIED as a verbatim command; the trigger family and the
target convention above are verified from SKILL.md:3 and SKILL.md:14.

B. WHAT RAN AUTOMATICALLY AFTER THAT ONE COMMAND

Order is fixed in the original EthOS "Firing NotebookLM" section:

  SKILL.md:192  header "Firing NotebookLM (the actual generation step)"
  SKILL.md:194  note: calls the notebooklm Python LIBRARY directly, not the MCP
  SKILL.md:207-221  the exact 11-step sequence (verbatim code block):

  0. get_output_language()            -> must be "ar"
  1. notebooks.list()                 -> reuse, don't spawn duplicates
  2. notebooks.create(title)          -> only if none exists
  3. sources.add_text(..., wait=True) -> ONE session's material only
  3a. sources.add_file(..., wait=True)-> REAL logo PNG images
  3b. sources.add_file(..., wait=True)-> S2-S9: 1-2 PNG pages of S1 FINAL as style lock
  4. sources.list(nb_id)              -> EVERY source must read status=READY
  5. generate_slide_deck(... DETAILED_DECK, language='ar')
  6. artifacts.wait_for_completion(nb, task)
  7. download_slide_deck(nb, path, artifact_id=task_id)
  8. open the file and QA it
  9. VERDICT LOOP  -> PASS/FAIL per gate, classify FAIL, OFFER REGEN same turn
 10. SAVE production record -> never self-mark Confirmed

AUTOMATED vs MANUAL:
  - Steps 0-7 (create notebook, add text/file sources, wait-for-index,
    generate, download): AUTOMATED by the library call inside the skill.
  - Step 8 (open the file and QA): the model inspects the rendered file itself.
  - Step 9 (verdict loop): AUTOMATED gates, but a detected FAIL produces a
    REGENERATION OFFER to the owner in the same turn — the owner decides, the
    machine does not silently retry or silently shudown (SKILL.md:43-58, the
    "patched after a real failure" rule).
  - Step 3a/3b image upload: AUTOMATED (add_file), NOT manual drag-drop.
  - The owner's only manual inputs were: (a) approve the Session Blueprint
    BEFORE generation (DEC-027 gate), (b) approve/reject each generated artifact
    after the verdict loop, (c) run "notebooklm login" when Google auth expired
    (~3h lifetime, SKILL.md:308).

C. WHAT SOURCES WERE FED PER SESSION, AND HOW IMAGES/CHROME WERE PLACED

PER-SESSION SOURCE BUNDLE (original, SKILL.md:225):
  - Level 1 - AI Smart User (session script)
  - Learning Outcomes (expanded slide content, not outline)
  - that session's case study and exercise
  - NEVER the Teaching Guide (trainer-only)

MICROBIT RESTATED BUNDLE (00-contracts/brand-and-output.md:32-40), the 7 sources:
  1 lesson material        75-bundle/L1-s1/slides-source.md
  2 trainer guide          75-bundle/L1-s1/trainer-guide.md
  3 educational decision  75-bundle/L1-s1/decisions.md
  4 branding rules         Abdeen_Moon_OS_Docs/.../Techno_Square_Branding_Rule.md
  5 Tata guide             Abdeen_Moon_OS_Docs/.../Tata_Mascot_Usage Guide.md
  6 key project images    75-bundle/L1-s1/assets/img-*.png/.gif/.jpg
  7 key code screenshots  75-bundle/L1-s1/assets/img-*.png/.gif
  (Plus logo + TATA mascot chrome — see below.)
  The authoritative upload list is 75-bundle/L1-s1/SOURCES.md (status: ready).

HOW IMAGES/CHROME REACH THE SLIDE:
  ORIGINAL (SKILL.md:228-231): upload REAL logo PNGs via add_file — never
  described in text. Dr. Refaat's own red flag (SKILL.md:227): "the academy logo
  itself was not used which is a red flag." Fix: add_file with dark-bg variants
  (white logo.png, landscape logo white.png, لوجو عربي.png).
  MICROBIT (00-contracts/brand-and-output.md:129-161, §1e):
  - The text package NAMES each image and says where it goes. slides-source.md
    carries load-bearing "**Asset:** img-NN.png" and "**TATA:** tata_*.png"
    directives (see slides-source.md:20-23, and prepare.py strips these as
    renderer-only, not learner text).
  - Renderer placement: NotebookLM reads those directives and places the images
    during generation (brand-and-output.md:133-136).
  - EXECUTION SURFACE SPLIT (brand-and-output.md:149-156):
      create notebook  -> MCP create_notebook
      add image sources -> CLI (NOT MCP): notebooklm source add --type file
      add text sources  -> CLI --type file (markdown) or MCP add_source_text
      generate deck     -> MCP generate_slide_deck
    Reason: the notebooklm MCP exposes only add_source_text and add_source_url;
    it has NO file-upload tool (brand-and-output.md:138-140). So images MUST go
    through the CLI or the library, never the MCP text tool.
  - TATA STATES (brand-and-output.md:193-205): four mascot states mapped to
    triggers (Excited/Idea/Thinks/Approved). Microbit assets/ holds
    tata_excited/idea/thinks/approved.png — 4 of the 4 states present.

D. STATE THE PIPELINE KEPT BETWEEN STEPS (so it never re-asked the operator)

  1. SESSION BLUEPRINT (DEC-027, SKILL.md:107-114): one doc per session copied
     from _TEMPLATE.md, holding every slide's content, trainer guide content,
     handout content, timing, asset table. Owner signs it off. NO artifact may
     generate until approved. This is what absorbed every "what goes in?" question
     before the single command.
  2. ASSET MAPPING + ASSET PACKAGE (DEC-030, SKILL.md:116-126): per session,
     Asset Mapping.md under 08-REFERENCE/Session Assets/Session N/, with
     provenance. Generation HARD-STOPS unless every SLOT/SCREENSHOT row is
     "Produced and mapped" and each file resolves.
  3. SESSION DECK STATUS (SKILL.md:68): one-glance per-session tracker
     (deck/trainer-guide/handout/placeholder-fill status), derived from Active
     Tasks + Decision Log.
  4. PER-SESSION PRODUCTION RECORD (SAVE) (SKILL.md:220, 473-475): artifact
     filenames, versions, QA verdicts, repair history, Blueprint status, Asset
     Mapping.md kept locally; central trackers batched-updated after Session 9.
  5. VISUAL-STYLE REFERENCE LOCK (SKILL.md:348-356): an accepted render (S1 FINAL)
     uploaded as image source to every later session so styling cannot drift.
  6. CONFIRMED-STATUS WALL (SKILL.md:469): generated output stays "pending" until
     the owner reviews; it can never self-mark "Confirmed".

E. GAP LIST — WHAT IS MISSING IN Microbit TODAY (most-blocking first)

Each item: the missing piece and the file that must exist. Verified against the
live Microbit tree on 2026-08-20.

1. [BLOCKER] NO NOTEBOOKLM EXECUTOR IS WIRED INTO THIS VAULT.
   The original ran the 11 steps by calling the notebooklm PYTHON LIBRARY
   (SKILL.md:194). Microbit instead declares "renders_via: notebooklm (MCP,
   claude-run)" (slides-source.md:11) and "MCP, claude-run" (brand-and-output.md:57),
   but .mcp.json declares ONLY the "claude-flow" server — there is NO notebooklm
   MCP server and NO script that calls the library or CLI. 80-generation/ holds
   only prompt TEXT (nblm-student-deck-prompts.md), not an executor.
   => File needed: scripts/swarm/generate_session.py (or equivalent) that performs
      the 11-step sequence via library or `notebooklm source add --type file` CLI,
      and a declared execution surface (notebooklm MCP or documented CLI path) in
      .mcp.json / agent config. Without this, "start s1" has nothing to call.

2. [BLOCKER] NO SESSION BLUEPRINT / OWNER SIGN-OFF GATE (DEC-027).
   75-bundle/L1-s1/ already holds the pre-generation content
   (slides-source.md, trainer-guide.md, home-summary.md, decisions.md),
   but there is NO _TEMPLATE.md and NO approved Blueprint document with an owner
   approval state. This is the exact mechanism that made the single command
   sufficient — the owner's judgment was already spent.
   => File needed: 75-bundle/_TEMPLATE.md + 75-bundle/L1-s1/blueprint.md with an
      owner-approved frontmatter gate (mirror SKILL.md:107-114).

3. [BLOCKER] IMAGE/CHROME UPLOAD STEP IS NOT IMPLEMENTED.
   brand-and-output.md:143-156 mandates CLI `notebooklm source add --type file`
   for images because the MCP lacks file upload — but no script performs it, and
   it is absent from the (missing) executor in gap #1. The logo PNGs needed DO
   exist (75-bundle/L1-s1/assets/technosquare_logo.png, technosquare_logo_black.png)
   and the Abdeen branding/tata source docs exist. So the assets are present; the
   UPLOAD ACTION is not.
   => File needed: upload step inside generate_session.py (CLI --type file for
      every asset/*.png + logo + tata + S1-style-lock image).

4. [DEFECT] DANGLING ASSET THE CONTRACT ITSELF WILL TRIP ON.
   SOURCES.md (notebook B and the manifest) references `tata_device.png`, but that
   file does NOT exist on disk (only tata_excited/idea/thinks/approved.png do).
   scripts/swarm/check_assets.py would report it DANGLING. The 4 TATA states are
   covered by the 4 files present, so tata_device is an extra, uncreated asset.
   => File needed: either create 75-bundle/L1-s1/assets/tata_device.png or remove
      the tata_device reference from SOURCES.md and slides-source.md.

5. [MISSING] NO STATUS TRACKER / PRODUCTION RECORD (SAVE) FOR THE MICROBIT VAULT.
   Original Session Deck Status.md + per-session production record (SKILL.md:68,
   220) let the pipeline know what was done without re-asking. Microbit has no
   STATUS.md or production-record convention.
   => File needed: 75-bundle/STATUS.md (per-session deck/trainer-guide/summary
      status) + a SAVE record convention.

6. [CHICKEN-AND-EGG] NO VISUAL-STYLE REFERENCE LOCK EXISTS YET.
   Original step 3b uploaded 1-2 PNG pages of an ACCEPTED prior render (SKILL.md:213,
   348-356). For Microbit, s1 is the first being built, so there is no accepted
   render to anchor against. This is expected for the first session; it unblocks
   automatically once s1 is approved and its render is saved as the reference.
   => File needed (later): 80-generation/ or 90-receipts/ render of the approved
      L1-s1 deck, uploaded as the style lock for s2+.

7. [SOFT] ASSET GATE HAS NO HARD-STOP VOCABULARY.
   check_assets.py exists and classifies OK / TO-CREATE / DANGLING and exits 1 on
   dangling — good. But it is NOT the DEC-030 "Produced and mapped" 3-state gate
   with a hard stop before generation (SKILL.md:126). It is a post-hoc auditor, not
   a pre-flight wall.
   => File needed: wire check_assets.py as a hard pre-flight gate inside
      generate_session.py (abort if non-zero), matching DEC-030 semantics.

WHAT IS ALREADY PRESENT (so we do not rebuild it):
  - The 7-source doctrine + renderer routing + ingestion mechanism:
    00-contracts/brand-and-output.md (complete, verified).
  - The per-session bundle content for s1: 75-bundle/L1-s1/* (slides-source,
    trainer-guide, home-summary, decisions, SOURCES.md, 16 asset files).
  - Brand/tata source docs: Abdeen_Moon_OS_Docs/Academy_Brain_OS/*.md (exist).
  - Mechanical gates: scripts/swarm/gate_runner.py + prepare.py + check_assets.py.
  - EthOS v2 doctrine: .claude/skills/ethos-v2/SKILL.md (gates, verdict loop,
    kids-track rules).

BOTTOM LINE: The original "start s1 simply worked" because (a) the owner had
already approved a Blueprint so nothing was left to ask, and (b) a single script
called NotebookLM end-to-end (11 steps) and only then offered a regeneration.
Microbit has the DOCTRINE, the SOURCE BUNDLE, and the GATES — but NOT the
executor (gap #1), NOT the blueprint sign-off gate (#2), and NOT the image-upload
step (#3). Those three are the blockers. Fix those and "start s1" becomes a real
command again.
