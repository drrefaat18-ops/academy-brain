# EthOS generation method: what made one-command operation work

## Bottom line

The documented operating command was not literally `start s1`. No occurrence of that phrase exists in the two inspected vaults. **UNVERIFIED:** the owner may have used those exact words in chat, but the vault does not preserve them.

What the vault does preserve is the equivalent trigger contract: `ethos`, `fire the deck`, `generate the deck`, or `run ethos`, followed by an explicit session or artifact target. The skill gives the literal example: **`ethos, generate Session 1's deck`** (`D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md:3`; target requirement at `:12-15`). The course operating manual confirms the same trigger phrases and says a session/file target is required (`D:\vault\Dr mahmoud AI course\_CLAUDE.md:150-154`).

The later, production-hardened form was a copy-paste pickup prompt such as **`Claude pickup — generate Session 9 through the standard EthOS pipeline, then stop for Dr. Refaat's final artifact judgment.`** (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Claude Pickup Prompt.md:11-16`). That prompt explicitly named the target deliverables (`:39-43`), declared the approval gate already complete (`:45-51`), and told EthOS not to ask again. This is the exact mechanism that made a short operator instruction sufficient: the missing detail was already stored in files.

## A. What the operator actually typed

1. **Documented generic triggers:** `ethos`, `fire the deck`, `generate the deck`, `run ethos`; legacy `moon os` and `run moon os` also worked (`D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md:1-3`).
2. **Documented literal targeted example:** `ethos, generate Session 1's deck` (same file, `:3`).
3. **Documented production pickup form:** `Claude pickup — generate Session 9 through the standard EthOS pipeline, then stop for Dr. Refaat's final artifact judgment.` (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Claude Pickup Prompt.md:14-16`). Equivalent session-specific pickup prompts also existed for S8 (`:149-155`) and S6 (`:252-258`).
4. **`start s1`: UNVERIFIED.** It is not present in the inspected vault text. The closest verifiable operating meaning is: invoke EthOS and supply session 1 as the explicit target.

## B. What ran after the one command

The canonical educational order was fixed:

`Session Analysis -> Educational Architecture -> Educational Decision Mapping -> Required Assets Planning -> Trainer Guide check -> Student Slides -> Worksheet -> Home Summary -> QA Review -> SAVE` (`D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md:16-26`).

For an already prepared session, the operator did not redo the front half. The course architecture and learning outcomes were already the source scripts, so EthOS ran the back half (`:26-28`). The actual operating sequence was:

1. **Automatic: diagnose the target.** EthOS stated the session, source files, and output type before generation (`:28`).
2. **Already completed manual approval:** the owner had reviewed and approved the Session Blueprint. No artifact could be generated before that approval (`:107-114`). The pickup prompt treated `status: approved` as execution authorization and prohibited another approval question (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Claude Pickup Prompt.md:45-51`).
3. **Already completed asset production:** Codex produced and verified every approved session asset, then wrote `Asset Mapping.md`; EthOS had a hard stop until every required row was `Produced and mapped` and every file resolved (`D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md:116-126`).
4. **Automatic preflight:** check output language, reuse an existing notebook or create one, add session text, upload real logo images, upload approved visual-reference pages, and wait until every source was READY (`:205-215`). Source readiness mattered because generation against processing sources silently degraded output (`:295-301`).
5. **Automatic generation:** call NotebookLM in detailed-deck mode with the standing prompt clauses (`:215`; API mechanism at `:192-201`). Sessions over the approximately 20-21-slide limit were split into multiple calls and merged (`:280`).
6. **Automatic completion and retrieval:** wait for generation, download the artifact, and open the real file (`:216-218`). A timeout was followed by a direct download attempt before declaring failure (`:199-200`).
7. **Automatic QA:** inspect the artifact, run deterministic checks, visually review every page, and issue PASS/FAIL/UNVERIFIED per gate (`:71-85`, `:218-220`).
8. **Automatic repair loop:** classify each failure, repair or regenerate in the same work cycle, and preserve already-passed pages by repairing only the smallest affected part (`:43-58`, `:461-470`).
9. **Automatic asset placement after export:** measure the rendered placeholder region and insert mapped evidence images; the owner did not hand-position them (`:118-125`; overlay mechanism at `:382-415`).
10. **Automatic SAVE:** record exact filenames, versions, QA verdicts, repair history, blueprint status, mapping, and manifests (`:473-475`; `D:\vault\Dr mahmoud AI course\08-REFERENCE\Blueprint Asset Production SOP.md:35-49`).
11. **Manual final judgment only:** the owner reviewed the finished artifacts after production; this was explicitly not another pre-production checkpoint (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Claude Pickup Prompt.md:142-144`).

Therefore, “one command” did not mean “no human decisions ever.” It meant all instructional and asset decisions had already been approved and persisted before the command; after it, generation, retrieval, QA, repair, placement, and recording continued without conversational interruption.

## C. NotebookLM inputs and image/brand placement

### Original Dr Mahmoud course

For the student deck, EthOS uploaded one session only: the session script, expanded learning outcomes, that session's case study, and exercise; trainer-only Teaching Guide material was excluded (`D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md:205-225`). It then uploaded real dark-background logo PNGs with `add_file`, specifically the white logo, white landscape logo, and the localized wordmark; describing the logo in prose was explicitly rejected (`:227-231`).

For S2-S9 it also uploaded 1-2 rendered PNG pages of the accepted S1 artifact as visual references for each artifact type (`:348-365`). TATA was an actual asset set under `08-REFERENCE/Brand Assets/TATA/`, used only at defined beat markers (`:30-41`).

Session-specific images had two routes:

- **Reference/framework asset:** upload it to NotebookLM as an image source and instruct NotebookLM to recreate its exact wording, structure, and field order natively (`:371-380`).
- **Evidence asset:** reserve a clean region during generation, then crop, measure, preview-confirm, and insert the exact mapped image after export (`:382-415`). The overlay tool matched files to stable manifest IDs and used contain/letterbox placement, inset margin, and a thin brand-gray frame (`:404-413`).

The asset handoff was explicit: `Asset Mapping.md` held the absolute asset root, one slide-to-file mapping per asset, preservation rules, provenance links, and the approved choice (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Blueprint Asset Production SOP.md:111-127`). A real example maps exact PNG filenames to slides 10, 11, 12, 13, and 15, and orders NotebookLM not to recreate the evidence (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Session Assets\Session 3\Asset Mapping.md:11-34`).

### Current Micro:bit restatement

The Micro:bit contract now requires a seven-source student-deck bundle: lesson material, trainer guide, decision note, branding rules, TATA guide, curated project images, and curated code screenshots (`D:\vault\Microbit\00-contracts\brand-and-output.md:28-48`). Its intended ingestion mechanism is: upload image files as notebook sources, and make each slide's `- **Asset:** img-NN.png` line name the file and placement (`:129-136`). Because the MCP wrapper lacks file upload, the contract says to use the CLI command `notebooklm source add -n <notebook_id> --type file --title "<name>" <path>` for images, then MCP for deck generation (`:138-161`).

L1-s1 already has a precise upload manifest listing the seven source classes plus logo and four TATA poses (`D:\vault\Microbit\75-bundle\L1-s1\SOURCES.md:10-39`), and `slides-source.md` already binds named assets and TATA poses to individual slides (for example `D:\vault\Microbit\75-bundle\L1-s1\slides-source.md:26-32`, `:47-54`, `:67-77`).

## D. State that prevented repeated questions

The pipeline persisted all decisions needed to resume without asking:

1. **Approved Session Blueprint:** actual slide content, narrative spine, timings, placeholders, case study, exercise, trainer-guide content, handout content, and constraint audit (`D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md:107-176`).
2. **Pickup prompt:** exact files to read, explicit deliverables, authorization, source-routing rules, QA requirements, and stop condition (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Claude Pickup Prompt.md:14-51`, `:132-144`).
3. **Asset Mapping:** exact slide-to-file mapping, asset class, provenance, preservation rules, and approved candidate (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Blueprint Asset Production SOP.md:111-127`).
4. **Source provenance and attempt logs:** retained genuine sources, calculations, model/tool attribution, unsuccessful attempts, and retrieval details (`:101-109`).
5. **Placeholder manifest:** stable ID, page, label, measured rectangle, and fit mode (`D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md:404-415`).
6. **Session-local Production Record:** exact artifact filenames, versions, QA verdicts, repair history, blueprint status, mapping, and manifests were retained even when central tracker updates were batched (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Blueprint Asset Production SOP.md:35-49`).
7. **Session Deck Status ledger:** one row per session for deck, trainer guide, handout, placeholder fill, and notes; it defined states from Not started through FINAL (`D:\vault\Dr mahmoud AI course\06-PLANNING-AND-EXECUTION\Session Deck Status.md:7-30`).
8. **Decision Log and operating manual:** the manual required checking the Decision Log and Current State before acting (`D:\vault\Dr mahmoud AI course\_CLAUDE.md:19-20`) and identified EthOS, the asset SOP, and the active production sequence (`:51-68`).

Micro:bit has some of this state already: an L1-s1 upload manifest (`D:\vault\Microbit\75-bundle\L1-s1\SOURCES.md:1-16`), exact two-pass split (`:95-106`), generation prompts (`D:\vault\Microbit\80-generation\nblm-student-deck-prompts.md:9-31`, `:95-123`), and gate receipts. But the slide receipt still reports `overall: UNVERIFIED` because brand palette was not verified (`D:\vault\Microbit\90-receipts\slides-source\L1-s1.gates.yaml:1-18`); the trainer-guide and home-summary receipts are also not final rendered-artifact production records (`D:\vault\Microbit\90-receipts\trainer-guide\L1-s1.gates.yaml:1-14`; `D:\vault\Microbit\90-receipts\home-summary\L1-s1.gates.yaml:1-18`).

## E. Missing from Micro:bit today, most blocking first

### 1. A session runner/conductor file — BLOCKING

**File that needs to exist:** `D:\vault\Microbit\scripts\generation\run_session.py` (or an equivalent single canonical executable named by the operating manual).

Micro:bit documents individual MCP/CLI operations but has no executable that performs them. The current contract describes the split surfaces (`D:\vault\Microbit\00-contracts\brand-and-output.md:129-161`), while the original EthOS had an exact ordered run sequence from language check through SAVE (`D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md:192-221`). Without this file, `start s1` has nothing to dispatch to.

### 2. A root trigger contract mapping `start s1` to that runner — BLOCKING

**File that needs to exist:** `D:\vault\Microbit\AGENTS.md`.

The Micro:bit `CLAUDE.md` contains generic Ruflo coordination rules, not an EthOS session trigger (`D:\vault\Microbit\CLAUDE.md:15-40`, `:198-224`). The original course's root manual explicitly mapped the trigger phrases to the EthOS skill and required a target (`D:\vault\Dr mahmoud AI course\_CLAUDE.md:150-154`). The new root contract must state that `start s1` means: load EthOS v2, resolve `L1-s1`, run the canonical session runner, and stop only at a genuine blocker or final-artifact judgment.

### 3. A per-session approved execution brief / blueprint — BLOCKING

**File that needs to exist:** `D:\vault\Microbit\75-bundle\L1-s1\BLUEPRINT.md` with an explicit approved/ready state.

The original pipeline would not generate without an approved Blueprint (`D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md:107-126`), and pickup prompts used that stored status to forbid repeated approval questions (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Claude Pickup Prompt.md:45-51`). Micro:bit has source and prompt files, but `slides-source.md` is still marked `status: draft` (`D:\vault\Microbit\75-bundle\L1-s1\slides-source.md:1-16`), and `SOURCES.md` still lists human checks and not-yet-created annotated assets (`D:\vault\Microbit\75-bundle\L1-s1\SOURCES.md:44-82`). Therefore the stored authorization needed for unattended execution does not exist.

### 4. A resolved asset map with every referenced file present — BLOCKING

**File that needs to exist:** `D:\vault\Microbit\75-bundle\L1-s1\ASSET-MAPPING.md`.

It must classify every asset, give exact slide-to-file destinations, and prove every path resolves, matching the original handoff contract (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Blueprint Asset Production SOP.md:111-127`, `:142-153`). Current `SOURCES.md` says five annotated assets “must be CREATED before generation” and names three additional bug screenshots (`D:\vault\Microbit\75-bundle\L1-s1\SOURCES.md:55-82`). It also lists `tata_device.png` as an upload (`:27-29`), but that file is absent from the bundle: **UNVERIFIED asset reference until repaired or removed.**

### 5. A per-session pickup prompt — HIGH

**File that needs to exist:** `D:\vault\Microbit\80-generation\L1-s1-pickup.md`.

This should be the complete no-reasking execution envelope: target, sources, approval state, two-pass boundary, generation calls, QA, repair, merge, download paths, and stop condition. The original pickup prompt carried exactly that information (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Claude Pickup Prompt.md:14-51`, `:120-144`). Micro:bit currently has renderer prompts, but they begin at “Upload exactly those sources” (`D:\vault\Microbit\80-generation\nblm-student-deck-prompts.md:9-15`) and end with manual merge/check instructions (`:83-123`); they are not an end-to-end operating brief.

### 6. A real rendered-artifact production record — HIGH

**File that needs to exist:** `D:\vault\Microbit\90-receipts\L1-s1.production.yaml`.

It must hold notebook IDs, source IDs/statuses, task/artifact IDs, output paths and hashes, pass-A/pass-B merge result, visual QA verdicts, repairs, and final operator judgment. The original system required artifact-local filenames, versions, QA verdicts, repair history, mappings, and manifests (`D:\vault\Dr mahmoud AI course\08-REFERENCE\Blueprint Asset Production SOP.md:35-49`). Current receipts are source-gate snapshots and remain `overall: UNVERIFIED` (`D:\vault\Microbit\90-receipts\slides-source\L1-s1.gates.yaml:1-18`). They cannot resume a NotebookLM run or prove a deck was downloaded and inspected.

### 7. A course/session status ledger — MEDIUM

**File that needs to exist:** `D:\vault\Microbit\90-receipts\session-generation-status.md`.

The original `Session Deck Status.md` showed, per session, deck/trainer-guide/handout status and placeholder-fill state, with explicit workflow states (`D:\vault\Dr mahmoud AI course\06-PLANNING-AND-EXECUTION\Session Deck Status.md:7-30`). Micro:bit has separate receipts but no one-glance session ledger telling the runner whether to create, resume, repair, or stop.

### 8. A deterministic rendered-output QA/merge command — MEDIUM

**File that needs to exist:** `D:\vault\Microbit\scripts\generation\finalize_nblm_deck.py`.

The current prompt tells a human to merge pass A then B and perform visual checks (`D:\vault\Microbit\80-generation\nblm-student-deck-prompts.md:83-93`, `:95-123`). The original pipeline automatically downloaded, opened, verified, repaired, merged, and saved evidence (`D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md:205-223`, `:461-475`). Until this is executable and receipt-producing, the single-command promise remains incomplete.

## Decisive conclusion

The old experience worked because the operator supplied only the **target**, while the vault supplied the **procedure and state**. Restoring that experience does not require redesigning the Micro:bit content. L1-s1 already has much of the source bundle, image bindings, renderer prompts, and basic gate receipts. The restoration blocker is operational: add the runner, root trigger, approved per-session blueprint, resolved asset map, pickup brief, and resumable production ledger. Then `start s1` can truthfully mean “execute the already-approved L1-s1 package through generation, QA, repair, placement, and SAVE without asking me again.”
