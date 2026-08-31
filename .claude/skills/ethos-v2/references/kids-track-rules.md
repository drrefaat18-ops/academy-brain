# Kids-Track Rules

> Historical record for the micro:bit course (now at `D:\vault\microbit-academy`).
> For any NEW course, `00-contracts/track-pedagogy.md` is the current authority:
> most of what this file reversed against the old adult EthOS has since become
> an academy-wide default, and the rest is superseded there.

EthOS was adapted for an adult audience on the AI course. Techno Square's Micro:bit course is a kids STEM track, which reverses several of those decisions. Where this file and the adult EthOS disagree, this file wins.

## Reversals

| Dimension | EthOS (adult) | EthOS v2 (kids) |
| --- | --- | --- |
| Slide density | one concept plus 2–4 supporting points | **one idea per slide**, strict |
| Tata mascot | beat-markers only | **full 4-state usage**: Excited, Idea, Thinks, Approved — still never on every slide |
| Examples | calibrated to profession and tool familiarity | calibrated to age; concrete and physical |
| Visuals | real interface screenshots | colourful, child-friendly; icons, arrows, simple shapes |
| Arabic register | adult explanatory | simple, short, beginner-friendly, RTL-correct |
| Trainer guide | per session | **per level**, one PDF, produced by Gemini |
| Take-home | Parent Talk dropped | **Home Summary with Parent Talk restored** |

## Unchanged from EthOS

- **Language ratio:** literal 30% English / 70% Arabic. Put the ratio in every generation prompt, not just "include some Arabic."
- **Brand palette:** `#231F20` near-black, `#FFED10` yellow, `#585858` grey, white.
- **Retired and wrong:** `#F5B301` gold and `#1A1A1A` placeholder black. Anything generated with these is off-brand and fails `brand-palette`.
- **Tata is used to support learning, not as decoration**, and never on every slide.

## Home Summary format

Specified in Brain OS `Techno_Square_QA_Checklist.md`. Do not reinvent it. Required sections:

- Today I Learned
- New Words
- Review at Home
- Parent Talk
- Mini Activity

Three slides per session; session 7 is two slides. Twenty slides per level.
