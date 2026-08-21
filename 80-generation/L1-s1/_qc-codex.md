# L1-s1 generated-output QC — Codex

Inspected all 26 rendered frames individually against `slides-source.md`, `home-summary.md`, `ASSET-MAPPING.md`, and `brand-and-output.md`. The two owner-confirmed defects on a-05 are intentionally omitted.

1. [all 26 slides: a-01–a-14, b-01–b-09, summary-01–summary-03] BLOCKING — Every frame carries the unauthorized “Gemini Notebook” watermark at bottom-right, so none of the three PDFs meets the “ONLY Techno Square branding” rule. — Exact fix: remove/crop the Gemini watermark from every exported page and re-render; verify all 26 bottom-right corners contain no renderer branding.

2. [summary-02] BLOCKING — `img-20` is EVIDENCE, but NotebookLM drew a simplified `forever` + `show string` pseudo-screenshot instead of leaving the required reserved region. This is fabricated technical evidence. — Exact fix: delete the drawn blocks, replace them with a clean box labelled `[Reserved Image Area: img-20]`, then overlay the exact mapped file `75-bundle/L1-s1/assets/img-20.png` after export.

3. [a-06, a-08, a-09, a-10, a-11, a-12, a-13, a-14] BLOCKING — These EVIDENCE destinations are rendered as anonymous grey/black empty panels rather than explicit `[Reserved Image Area: …]` placeholders. On a-10 and a-12, TATA also intrudes into the reserved panel, so an exact overlay would collide with the mascot. — Exact fix: label each clean, unobstructed region with its mapped ID (`img-05-led`, `img-19-labelled-a`, `img-19-labelled-b`, `img-20`, `img-20-reuse`, `img-32-step12`, `img-35-step34`, `img-19` respectively); move TATA fully outside the a-10 and a-12 regions; overlay only the exact mapped evidence files after export.

4. [a-08, a-10, b-09] BLOCKING — Literal source markup leaks into student-visible text: a-08 shows `<h2>`, `</h2>`, `<strong>`, `</strong>`, `<span>`, `</span>`, `<p>`, and `</p>`; a-10 shows `<h2>`, `<div dir="rtl">`, `<strong>`, `<p>` and closing tags; b-09 shows `**forever**` twice. — Exact fix: strip all HTML/Markdown delimiters before generation, apply heading/bold/RTL as actual formatting, and render only the intended wording.

5. [b-01, b-03, b-04, b-05, b-06, b-07, b-08, b-09] BLOCKING — Deck B abandons the required dark/black + gold visual system for a plain white background. The break starts on b-01, briefly returns to dark on b-02, then remains white from b-03 through b-09, creating a visibly discontinuous single lesson. — Exact fix: rebuild these eight slides using the same black/dark background, gold-yellow highlights, white secondary text, circuit-line texture, margins, and title treatment used in deck A and b-02.

6. [a-01] BLOCKING — The bound `tata_excited.png` pose is not used; the slide shows an invented pointing/running TATA rather than the official excited asset (TATA 7, waving). — Exact fix: replace the invented mascot with the exact transparent `Techno Square identity/TATA/7.png` image without redrawing or pose alteration.

7. [b-08] BLOCKING — Slide 22 requires `tata_thinks.png`, but the visible standing hand-on-chin mascot is the Idea pose, not the seated Thinks pose. — Exact fix: replace it with the exact `Techno Square identity/TATA/2.png` asset.

8. [summary-01] BLOCKING — Summary slide 1 requires `tata_idea.png`, but it displays the seated Thinks pose. — Exact fix: replace it with the exact `Techno Square identity/TATA/3.png` asset.

9. [b-02, b-07] BLOCKING — The Techno Square logo is present but corrupted/reinvented. On b-02 the tagline is illegible nonsense; on b-07 the icon, wordmark arrangement, and tagline layout differ from the official landscape logo. — Exact fix: replace both with the exact mapped `Techno Square identity/PNG/landscape logo.png`, preserving its aspect ratio and wording with no redraw.

10. [b-04] BLOCKING — A stray visible `*` precedes `“Hello!”`, leaking Markdown and changing the displayed bug statement. — Exact fix: remove the asterisk and render the exact source sentence: `بيظهر "Hello!" مش اسمي.` with `"Hello!"` formatted as code/emphasis, not markup text.

11. [summary-01] COSMETIC — NotebookLM added the non-source, nontechnical English labels “The Achievement” and “The Vocab Matrix.” They add clutter and work against the 70% Egyptian-Arabic / 30% technical-English rule. — Exact fix: delete both invented labels; retain only the required bilingual headings `Today I Learned — النهاردة اتعلمت` and `New Words — كلمات جديدة`.

12. [b-01, b-07, b-08, b-09] COSMETIC — These white-theme slides also introduce mutually unrelated visual systems (plain success card, quote/checklist layout, graph-paper worksheet), so even after recolouring they would not read as one deck. — Exact fix: normalize typography, logo placement, corner geometry, circuit motif, spacing, and gold-accent components to the deck-A master layout while preserving each slide’s content hierarchy.

13. [a-04] COSMETIC — The arrow between `code` and the micro:bit points left toward the board while the sentence says the learner tells the computer what to do with code; the visual direction implies the reverse flow. — Exact fix: reverse the arrow so it runs from `code` toward the micro:bit, or place `code` on the left and the board on the right with a left-to-right arrow.

14. [summary-01] COSMETIC — The slide is materially overcrowded: achievement copy, a large illustration, a four-row vocabulary table, two invented English sublabels, and TATA compete in one frame; the mascot also sits across the table boundary. This violates the short/visual/not-text-heavy summary requirement. — Exact fix: remove the two invented labels, shrink the decorative illustration, keep TATA outside the table, and give the four vocabulary rows consistent padding and an unobstructed reading area.

