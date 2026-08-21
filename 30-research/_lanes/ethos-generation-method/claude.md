---
cluster: ethos-generation-method
provider: claude
status: complete
question: What made "start s1" work in the Dr Mahmoud course, and what is missing in the Microbit vault?
evidence:
  - D:\vault\Dr mahmoud AI course\.claude\skills\ethos\SKILL.md (482 lines)
  - D:\vault\Dr mahmoud AI course\06-PLANNING-AND-EXECUTION\Session Blueprints\_TEMPLATE.md
  - D:\vault\Dr mahmoud AI course\06-PLANNING-AND-EXECUTION\Session Deck Status.md
---

# How generation actually worked, and the one thing that blocks us

## A. The trigger really was one word — because the judgment happened earlier

`ethos/SKILL.md:12` "Do Not Generate on Invocation Alone": the skill accepts a bare
target ("session number, a file, or 'the deck'"). Everything else was already
settled, so "start s1" was sufficient. It was not magic; it was that nothing was
left to ask.

What absorbed the questions: **the Session Blueprint** (DEC-027, `SKILL.md:107`).
One document per session, copied from `_TEMPLATE.md`, containing every slide's
actual content, the trainer guide content, the handout content, timing, and an
asset table. The owner reads and signs it off. **No artifact may be generated
until he approves it.** Quote from the decision: *"i have no saying regarding what
goes into NBLM content wise ... this process happens silently."* The blueprint
exists to end that.

## B. THE BLOCKER IS FALSE — EthOS never used the MCP

`SKILL.md:192`, verbatim:

> **No MCP tool wrapper is used in practice — this vault calls the `notebooklm`
> Python library directly** via the venv at
> `C:\Users\ET\mcp-servers\notebooklm-mcp\.venv\Scripts\python.exe`
> (run with `PYTHONIOENCODING=utf-8`).

Sources API:

```python
client.sources.add_text(nb_id, title, text, wait=True)
client.sources.add_file(nb_id, path, wait=True)   # PDF/text/markdown/Word AND image
                                                  # SourceType.IMAGE works despite the docstring
```

So image upload was never a missing capability. The MCP wrapper is simply the
wrong surface. **The escalation that stopped the last run ("no add_source_file
tool, proceed text-only or stop") was answering the wrong question.**

## C. The exact firing sequence (SKILL.md:195-232) — 11 steps, ordered

```
 0. get_output_language()          -> must be "ar"
 1. notebooks.list()               -> reuse, never spawn duplicates
 2. notebooks.create(title)        -> only if none exists
 3. sources.add_text(wait=True)    -> ONE session's material only
 3a. sources.add_file(wait=True)   -> REAL logo PNGs. "Never described in text only again."
 3b. sources.add_file(wait=True)   -> s2+: rendered PNG pages of s1 FINAL as visual-style lock
 4. sources.list()                 -> EVERY source must read status=READY (2)
 5. generate_slide_deck(slide_format=SlideDeckFormat.DETAILED_DECK, language='ar')
 6. artifacts.wait_for_completion(nb, task, initial_interval=15)
 7. download_slide_deck(nb, path, artifact_id=task_id)
 8. open the file and QA it        -> never infer success from a tool result
 9. VERDICT LOOP                   -> PASS/FAIL per gate, offer regeneration same turn
10. SAVE production record         -> never self-mark Confirmed
```

Step 3a is the direct fix for our defect #1. It was added `2026-07-25` after the
identical failure: *"the academy logo itself was not used which is a red flag."*
The fix recorded there is one line: **description is not the asset — upload it.**

Notes bound to real defects:
- Pass enum members, not strings. `orientation='portrait'` throws AttributeError.
- `from notebooklm import ...`, NOT `from notebooklm.models import ...`.
- No `poll_artifact_status`; no generic `download_artifact`.
- A `wait_for_completion` TimeoutError does NOT mean failure — try `download_*`
  first. Re-firing burns a quota slot on work already finished.
- Trainer guide via `generate_slide_deck`, never `generate_report` — report output
  is markdown with a .pdf name and will not open.
- Slide cap ~20-21 per call is a platform limit, prompt-independent. Segment-based
  multi-call + merge, one call per timing block. Matches our split-and-merge ruling.
- Empty `task_id` on a hollow success = daily quota exhausted, not rate limiting.
  Stop, do not retry.

## D. State the pipeline kept

- `Session N Blueprint.md` — approved content, the sole input
- `Asset Mapping.md` + `08-REFERENCE/Session Assets/Session N/` — Codex-produced
  assets with provenance; generation hard-stops unless every row is
  `Produced and mapped` and each file resolves (DEC-030)
- `Session Deck Status.md` — per-session tracker with a defined status vocabulary
- Per-session Production Record — the SAVE

## E. Gap list, most-blocking first

| # | Missing in Microbit vault | File that must exist |
|---|---|---|
| 1 | Direct-library generation runner (the 11 steps as a script) | `scripts/swarm/generate_session.py` |
| 2 | Owner-approved Session Blueprint gate | `75-bundle/L1-s1/blueprint.md` + `_TEMPLATE.md` |
| 3 | Brand asset PNGs to upload at step 3a | `00-contracts/brand-assets/*.png` — **not present** |
| 4 | Visual-style reference lock (an accepted s1 render) | none yet — s1 is the one being made |
| 5 | Asset production gate w/ hard stop | we have `check_assets.py`; needs the 3-status vocabulary |
| 6 | Session status tracker | `75-bundle/STATUS.md` |

## F. Correction to the premise

"start s1 and it simply worked" is not what the record shows. `Session Deck Status.md`
lists `Deck (v4 FINAL)`, `Handout (v7, Codex rebuilt)` after v1-v6 were *"rejected
outright"*, a hand-patched S6 handout, and a five-regeneration S2 handout. The
single command worked; the *first output* usually did not. What made it feel
effortless is that the owner's judgment was spent at blueprint sign-off, and the
QA verdict loop caught defects without asking him to diagnose them.

That is the thing to rebuild — not a shorter command.
