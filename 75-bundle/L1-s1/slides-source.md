---
id: L1-s1
stage: bundle
type: student-slides-source
owner: claude
status: draft
role: >-
  NBLM source #1 (lesson material). Derived from 70-localized/L1-s1.md with
  §7 interaction law applied — video-only slides replaced by hands-on beats —
  and §4 TATA / §1 asset bindings added per slide. 70-localized is NOT modified.
renders_via: notebooklm (MCP, claude-run)
audience: STUDENT-FACING — no trainer notes, no timings, no scripts
language: ar-EG (Egyptian colloquial) + en, 30/70
contract: 00-contracts/brand-and-output.md
derived_from: 70-localized/L1-s1.md
---

# L1-s1 — بطاقة الاسم (Name Badge)

> **Rendering rules for every slide:** Techno Square logo present. Dark/black
> with yellow-gold highlights. Large title. One idea per slide. Not text-heavy.
> English term + Arabic explanation. TATA only where named below.

---

## Slide 1 — Title / بطاقة الاسم

**Name Badge — بطاقة الاسم**
Techno Square Academy · micro:bit · Level 1 · Session 1

- **TATA:** `tata_excited.png`
- **Asset:** `technosquare_logo.png`

---

## Slide 2 — كمبيوترات مخبّية!

**قبل ما نفتح أي شاشة:**

قولي حاجة في البيت فيها كمبيوتر جواها… وشكلها مش كمبيوتر!

- **TATA:** `tata_thinks.png`
- **Visual:** icons — microwave, washing machine, TV, car

---

## Slide 3 — إيه هو الـ micro:bit؟

**micro:bit = كمبيوتر صغير جداً**

أصغر من كف إيدك… وبرضه كمبيوتر!

- **Asset:** `img-05.png` (micro:bit board, whole-device view)
- **TATA:** `tata_idea.png`

---

## Slide 4 — الكمبيوتر بيسمع كلامك

بتقوله يعمل إيه بالـ **code**
التعليمات مرتبة = **algorithm**

- **Asset:** `img-06.gif`

---

## Slide 5 — نتعرّف على الجهاز 🔍

**LED display** — الشاشة، 25 لمبة
**Buttons A / B** — الأزرار
**USB** — منها بيدخل الكود
**Battery** — عشان يشتغل من غير كمبيوتر

هات جهازك ودوّر على كل جزء!

- **Asset:** `img-05-labelled.png` (board with LED / buttons / USB / battery labelled)
- **TATA:** `tata_thinks.png`

---

## Slide 6 — الـ LED display = Output

الشاشة الصغيرة قدام الـ micro:bit فيها **LEDs**

أي حاجة بتطلع من الكمبيوتر اسمها **output**

- **Asset:** `img-05-led.png` (close crop of the 5x5 LED grid, lit)

---

## Slide 7 — أهداف الدرس

1. أقدر أشرح إن الـ micro:bit كمبيوتر صغير
2. أقدر أشرح إن الكمبيوتر محتاج **algorithm**
3. أقدر أعمل **Name Badge** على شاشة الـ LED

- **Visual:** three numbered icons — micro:bit board, ordered list, scrolling name


---

## Slide 8 — محرر MakeCode: فين الكود؟

**Toolbox** — هنا قطع الكود
**Workspace** — هنا نركّب الكود بتاعنا

- **Asset:** `img-19-labelled-a.png` (editor screenshot, arrows on Toolbox + Workspace only)

---

## Slide 9 — محرر MakeCode: نجرّب ونحمّل

**Simulator** — نجرّب الكود على الشاشة
**Download** — نحمّله على الجهاز الحقيقي

- **Asset:** `img-19-labelled-b.png` (editor screenshot, arrows on Simulator + Download only)

---

## Slide 10 — اتوقع الأول! 🤔

**قبل ما نشغّل الكود — إيه اللي هيحصل؟**

- **Asset:** `img-20.png` (the completed forever + show string code)
- **TATA:** `tata_thinks.png`

---

## Slide 11 — الكود بتاعنا

**`forever`** — حلقة (loop)، الكود يفضل شغال
**`show string`** — بيعرض الاسم وبيخليه يتحرك

الكود يرجع لأول الحلقة ويشتغل تاني

- **Asset:** `img-21.png` (block close-up)

---

## Slide 12 — نبني الكود: خطوة 1 و 2

**1.** افتح مشروع MakeCode جديد
**2.** هات بلوك **`forever`** من الـ Toolbox

- **Asset:** `img-32.gif` (build animation, steps 1–2)
- **TATA:** `tata_excited.png`

---

## Slide 13 — نبني الكود: خطوة 3 و 4

**3.** حط بلوك **`show string`** جواه، واكتب **اسمك**
**4.** جرّب في الـ **Simulator** — اسمك بيتحرك؟

- **Asset:** `img-35.png`

---

## Slide 14 — حمّل على الجهاز! 🔌

**5.** وصّل الـ micro:bit بالـ USB
**6.** دوس **`Download`** — واتفرج على اسمك على الجهاز الحقيقي!

- **Asset:** `img-19.png` (Download button highlighted)

---

## Slide 15 — جرّب واتأكد ✅

**Success:** اسمي بيتحرك صح على الشاشة
**و** أقدر أأشر على البلوك اللي بيحرّكه

الاسم اللي على الشاشة ده هو الـ **output** بتاعك!

- **Asset:** `img-36.jpg`
- **TATA:** `tata_approved.png`

---

## Slide 16 — Debugging Lab 🐛

النهاردة هنبقى **مصلّحين أخطاء**!

هوريكم تلات برامج فيهم غلط — **اتوقّع الأول** إيه الغلط، وبعدين صلّحه.

- **TATA:** `tata_thinks.png`

---

## Slide 17 — Bug 1 🐛

الاسم بيظهر **مرة واحدة** وبعدين يقف.

اتوقّع الأول: إيه اللي غلط؟

- **Asset:** `img-20-bug1.png` (`on start` + `show string`)

---

## Slide 18 — Bug 2 🐛

بيظهر **`"Hello!"`** مش اسمي.

اتوقّع الأول: إيه اللي غلط؟

- **Asset:** `img-20-bug2.png` (`forever` + `show string "Hello!"`)

---

## Slide 19 — Bug 3 🐛

**مفيش أي حاجة بتظهر خالص.**

اتوقّع الأول: إيه الناقص؟

- **Asset:** `img-20-bug3.png` (empty `forever`, `show string` loose outside it)

---

## Slide 20 — خلصت بدري؟ ⭐

ضيف كلمة أو رقم يعبر عنك
ضيف أيقونة بـ **`show icon`** تعبر عن مزاجك

- **Asset:** `img-41.png`

---

## Slide 21 — نوري بعض! 👀

كل اتنين يورّوا بطاقتهم لبعض ويكملوا:

**"بطاقتي بتعرض ___ لما ___."**

واسأل نفسك: عرفت تشرح إن الـ micro:bit كمبيوتر صغير؟ ومحتاج **algorithm**؟
وعملت الـ Name Badge بنفسك؟


---

## Slide 22 — Exit Ticket 📝

جاوب لوحدك:

1. الـ micro:bit ده إيه؟ (جملة واحدة)
2. اكتب اسم **البلوكين** اللي استخدمتهم
3. لو الاسم ظهر مرة واحدة وبعدين وقف — إيه اللي غلط؟

- **TATA:** `tata_thinks.png`

---

## Slide 23 — المرة الجاية

النهاردة: **`forever`** عشان نعمل **Name Badge**
المرة الجاية: **`forever`** عشان نعمل **Animation**!

- **Asset:** `img-51.gif`
- **TATA:** `tata_approved.png`
- **Asset:** `technosquare_logo.png`

---

Production changelog for this file lives in `decisions.md`, not here.

---

Production changelog and the NBLM two-pass split live in `SOURCES.md` and
`decisions.md`, not here.
