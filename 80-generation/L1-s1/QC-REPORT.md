---
type: qc-report
session: L1-s1
date: 2026-08-21
reviewers: claude (full visual sweep, all 26 frames), codex (full visual sweep, all 26 frames, independent), opencode (blocked — see note), hermes (blocked — see note)
verdict: NOT SATISFACTORY — do not ship, regenerate/repair required
---

# L1-s1 Generated Output — QC Report

Both Claude and Codex independently opened and inspected all 26 rendered
frames (`qc-frames/a-01..14.png`, `b-01..09.png`, `summary-01..03.png`)
against `slides-source.md`, `home-summary.md`, `ASSET-MAPPING.md`, and
`00-contracts/brand-and-output.md`. Every finding below was seen by at least
one reviewer directly on the rendered image; the most severe were
cross-verified by both. OpenCode's lane was blocked by its own sandbox
(cannot access files outside its own directory even inside this vault) and by
the PDFs being 100% image — zero extractable text, so nothing for a
text-only lane to check. Hermes hung twice, then on a third attempt ran but
never located the frames and produced no report — excluded from this round
(see `00-contracts/agent-memory.md` for the standing note on this).

**Owner-facing summary: none of this needs the owner's judgment.** Every
defect below is agent-resolvable — a regeneration, re-prompt, or direct PDF
patch. Per the new rule in `00-contracts/agent-memory.md`, agents fix these,
not the owner.

## BLOCKING

1. **[all 26 slides] "Gemini Notebook" watermark on every single frame.**
   Violates the "ONLY Techno Square branding" rule outright.
   **Fix:** crop/remove the watermark from all 26 pages in the exported PDFs
   (mechanical, scriptable — bottom-right corner, consistent position).

2. **[summary-02] Fabricated EVIDENCE.** `img-20` is EVIDENCE-class — must be
   a blank reserved region, never redrawn. NotebookLM instead drew its own
   simplified `forever`/`show string` blocks. Confirmed visually. **Fix:**
   regenerate this slide with an explicit `[Reserved Image Area: img-20]`
   placeholder instruction, or patch the exported PDF directly to blank the
   region and overlay the real `img-20.png` after.

3. **[a-06, a-08, a-09, a-10, a-11, a-12, a-13, a-14] Unlabeled evidence
   boxes.** These correctly stayed blank (not fabricated), but render as bare
   grey/black panels with no `[Reserved Image Area: <id>]` label — looks like
   a rendering error, not an intentional placeholder. On a-10 and a-12, TATA
   overlaps the reserved region, which will collide with the post-export
   overlay. **Fix:** re-prompt with explicit per-slide label text inside each
   box; move TATA outside the reserved rectangle on a-10/a-12.

4. **[a-08, a-10, b-09] Literal markup leaking into visible text.** `<h2>`,
   `</h2>`, `<strong>`, `</strong>`, `<span>`, `</span>`, `<p>`, `</p>`,
   `<div dir="rtl">`, and `**forever**` all render as literal on-slide text
   instead of being applied as formatting. Confirmed by both reviewers
   independently on a-08; Codex additionally found it on a-10 and b-09.
   **Fix:** the source prompt/content must not contain raw HTML/Markdown
   delimiters NotebookLM can't parse — strip them before generation, or
   re-express formatting as plain instructions ("bold this", "heading here").

5. **[b-01, b-03 through b-09 — i.e. all of deck-b except b-02] Total brand
   break.** Deck-b abandons the dark/black + gold-yellow palette entirely for
   a white background, with b-01/b-07/b-08/b-09 each inventing a visually
   unrelated layout system (success card, quote/checklist, graph-paper
   worksheet). deck-a and b-02 correctly use the dark/gold theme. This reads
   as two different lessons stitched together. **Fix:** regenerate deck-b
   with the branding rule re-emphasized in the prompt (it's supplied as a
   source but was evidently not applied) — this is pass B's most severe
   defect and likely needs a full re-prompt/regeneration of the whole pass,
   not a patch.

6. **[a-01] Wrong TATA pose.** Slide 1 is bound to `tata_excited.png`
   (waving, TATA 7); the rendered mascot is an invented pointing/running
   pose, not the real asset. **Fix:** re-prompt with stronger emphasis that
   TATA must be the exact uploaded image, not a redraw; or patch in the real
   `Techno Square identity/TATA/7.png` directly.

7. **[b-08] Wrong TATA pose.** Slide 22 needs `tata_thinks.png`; rendered
   mascot is the Idea pose. **Fix:** same as #6, target `TATA/2.png`.

8. **[summary-01] Wrong TATA pose.** Needs `tata_idea.png`; rendered mascot
   is the Thinks pose. **Fix:** same as #6, target `TATA/3.png`.

9. **[b-02, b-07, and separately confirmed by Claude on a-13] Corrupted
   logo.** The Techno Square logo is being redrawn instead of preserved
   exactly — tagline reads as illegible/wrong text ("FDB INNOVATE" instead of
   "YOU INNOVATE" on a-13; "illegible nonsense" on b-02), and b-07's whole
   logo layout differs from the real asset. This is REFERENCE-class brand
   chrome that should never be redrawn with altered text. **Fix:** re-prompt
   with explicit "use this exact logo image, do not redraw, do not alter
   text" instruction, or patch the real `landscape logo.png` over every
   corrupted instance directly in the exported PDF (safest fix — logo
   position is consistent top-right on every slide).

10. **[b-04] Stray literal asterisk.** `*"Hello!"` — a Markdown emphasis
    marker leaked as visible text, changing the displayed sentence. **Fix:**
    same root cause as #4 — strip markdown delimiters before generation.

## COSMETIC

11. **[summary-01]** Two invented English labels ("The Achievement", "The
    Vocab Matrix") not in `home-summary.md` — clutter, works against the
    30/70 language rule. **Fix:** remove both, keep only the bilingual
    headings that are actually in the source.

12. **[a-04]** Arrow between "code" and the micro:bit points the wrong
    direction relative to the sentence's meaning. **Fix:** reverse the arrow
    or swap element positions.

13. **[summary-01]** Slide is overcrowded — copy, illustration, 4-row table,
    two invented labels, and TATA all compete in one frame; TATA crosses the
    table boundary. **Fix:** remove the invented labels (also fixes #11),
    shrink the illustration, keep TATA clear of the table.

## What worked correctly (don't touch)

- b-03's bug-1 evidence region: correctly blank with an explicit
  `[Reserved Image Area: bug-1]` label — this is the template every other
  evidence slide (#3 above) should match.
- a-02, a-07, a-13 (aside from the logo defect), b-06: clean, on-brand,
  correct TATA/asset bindings, no markup leaks.
- Slide count and order are correct: deck-a is exactly slides 1-14, deck-b
  exactly 15-23, summary exactly 3 — nothing merged, dropped, or reordered.
- No EVIDENCE asset besides #2 (summary-02) was fabricated — every other
  reserved region either correctly stayed blank or is only missing its label
  (#3), not its content.

## Recommended path

Given the scope (10 blocking defects, several affecting whole passes), the
fastest real fix is not manual per-slide patching for everything:

- **Deck-b (defect #5):** full regeneration of pass B with the branding rule
  more forcefully stated in the prompt — patching 8 slides individually to a
  different visual system is not realistically achievable by prompt/PDF
  editing.
- **Watermark (#1), logo corruption (#9), TATA pose errors (#6-8):** these
  are all "wrong image in a known fixed position" — direct PDF patching
  (crop + overlay the real asset) is likely faster and more reliable than a
  further NotebookLM regeneration, which has already shown it won't reliably
  preserve exact uploaded images.
- **Markup leaks (#4, #10) and unlabeled evidence boxes (#3):** need a
  re-prompt fix since they're content/formatting issues, not asset-swap
  issues.
- **Fabricated evidence (#2):** re-prompt this one slide specifically, or
  patch directly since the fix (blank + label) is mechanical.
