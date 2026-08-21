# L1-s1 visual review — Codex

Review date: 2026-08-20

Scope: the ten curated raw images and the seven missing derived assets listed in `ASSET-MAPPING.md`. I read `ASSET-MAPPING.md`, `slides-source.md`, `SOURCES.md`, and `blueprint.md` Section A before reviewing the files. I opened every still image and sampled the beginning, middle, and end of every GIF. I did not edit any governing source file.

## Job 1 — curated raw-image QA

| File | Verdict | What the file actually shows | Mismatch / quality flags |
|---|---|---|---|
| `assets/img-05.png` | **REJECT for the claimed evidence derivatives** | A wide cartoon illustration of a child using a laptop connected to a simplified, front-facing micro:bit drawing. The 5×5 LEDs show a static smile. | It is not a real board photo. A battery connector is not visible, so it cannot truthfully support the required four-part labelled board. It does not show a scrolling name. Partial cut-off black text (`ON`) at lower left and other decorative marks reveal that it is a crop from a larger upstream graphic. The whole-device claim is only loosely true for a stylized front view. |
| `assets/img-06.gif` | **ACCEPT with scope caveat** | A 25-frame MakeCode micro:bit simulator animation in which LEDs scroll a short text sequence and return blank. | It supports changing output / a computer following code in a general sense, but it does not show code blocks or an ordered algorithm. No placeholder or stray logo. |
| `assets/img-19.png` | **ACCEPT** | A full genuine MakeCode editor screenshot: simulator at left, Toolbox center-left, Workspace at right, `forever` containing `show string "Amari"`, and the purple Download button at bottom left. | Microsoft and micro:bit marks are authentic MakeCode UI chrome, not stray pasted branding. The Download button is visible in its normal styling rather than separately annotated. |
| `assets/img-20.png` | **ACCEPT** | A clean close-up of a MakeCode `forever` block containing `show string "Amari"`. | Matches the completed-code claim. No logo or placeholder. |
| `assets/img-21.png` | **REJECT — severe mismatch / placeholder** | A 1002×2500 mostly transparent canvas containing only a tall red outline/loop arrow. | No MakeCode block is visible. It is not the claimed block close-up. |
| `assets/img-32.gif` | **REJECT for the claimed slide role** | A 116-frame genuine MakeCode animation that begins with `on start` and `forever`, opens Basic, drags `show string` into `forever`, changes `Hello!` to `Amari`, and runs it in the simulator. | This covers and reveals the full build, including steps 3–4 and the final answer. It is not limited to steps 1–2 as claimed. Microsoft/micro:bit branding is authentic UI chrome. |
| `assets/img-35.png` | **REJECT — wrong tutorial step** | A genuine MakeCode tutorial screenshot titled `Name badge - Step 2 of 7`. Its instruction says to return `on start` to the toolbox; the Workspace shows empty `on start` and empty `forever`. | It does not show placing `show string`, typing a name, or simulator testing, so it does not support claimed steps 3–4. |
| `assets/img-36.jpg` | **ACCEPT with quality caveat** | A real photo of a child's hands holding a physical micro:bit with red LEDs lit. | It supports real-device testing generally, but a still cannot establish that a name scrolls and no code block is visible to point to. Resolution is only 203×152, which is weak for a slide. |
| `assets/img-41.png` | **ACCEPT** | A clean MakeCode close-up: `forever` containing `show string "My name is Amari"`, `show icon`, and `show string "I am 10 years old"`. | Direct match for the extension instruction. No logo or placeholder. |
| `assets/img-51.gif` | **ACCEPT** | A two-frame micro:bit simulator animation alternating between two LED patterns. | Supports the next-session animation teaser. No logo or placeholder. |

No exact duplicate exists among the ten files (all hashes are unique), and there is no visual duplicate. There is intentional subject overlap among `img-19`, `img-20`, and `img-32` (the Amari name-badge program), and between `img-06` and `img-51` (different simulator animations).

Primary raw-asset blockers: `img-05.png`, `img-21.png`, `img-32.gif`, and `img-35.png`.

## Job 2 — derived assets

### Produced

| Output | Authenticity / method |
|---|---|
| `assets/img-05-led.png` | Direct PIL crop from the visibly lit 5×5 grid in `img-05.png`; no pixels or labels were invented. Important limitation: the source is a stylized illustration, not the real board photo described by the task/source premise. |
| `assets/img-19-labelled-a.png` | PIL crop of the real `img-19.png` MakeCode screenshot with labels/arrows for Toolbox and Workspace only. |
| `assets/img-19-labelled-b.png` | PIL crop of the real `img-19.png` MakeCode screenshot with labels/arrows for Simulator and Download only. |
| `assets/img-20-bug1.png` | Genuine live MakeCode Blocks editor screenshot made headlessly in Chrome/Playwright. The actual editor state is `on start` containing `show string "Amari"`. |
| `assets/img-20-bug2.png` | Genuine live MakeCode Blocks editor screenshot made headlessly in Chrome/Playwright. The actual editor state is `forever` containing `show string "Hello!"`. |
| `assets/img-20-bug3.png` | Genuine live MakeCode Blocks editor screenshot made headlessly in Chrome/Playwright. In the actual Blockly workspace, `forever` is empty and `show string "Amari"` is detached; MakeCode displays the loose block with its authentic disabled/cross-hatched treatment. |

The bug images are not drawings, composites, or plausible mockups. They were created by loading `https://makecode.microbit.org/#editor`, constructing the programs in the live editor, converting to Blocks, manipulating the third program with real Blockly pointer/context-menu actions, and screenshotting the visible Blockly workspace.

### Not produced

`assets/img-05-labelled.png` was intentionally left absent. The required labels are LED display, Buttons A/B, USB, and battery connector. The source `img-05.png` is a simplified illustration and contains no visible battery connector. Pointing an arrow at a guessed location or relabelling the visible USB cable/port as a battery connector would fabricate EVIDENCE. A replacement real front/back micro:bit image that visibly includes both the USB socket and battery connector is required before this asset can be produced honestly.

## Gate conclusion

The three MakeCode bug screenshots can be produced genuinely headlessly, and they have been produced. The asset gate is still blocked because `img-05-labelled.png` cannot be derived truthfully from its mapped source, and four curated raw files fail their claimed teaching roles (`img-05`, `img-21`, `img-32`, `img-35`).
