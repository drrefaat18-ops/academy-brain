---
id: L1-s1
stage: bundle
type: trainer-guide-draft
owner: claude
status: draft
role: >-
  DRAFT INPUT ONLY. This markdown is uploaded to Antigravity, which renders the
  single Techno Square-themed Trainer Guide PDF. It is not itself a deliverable
  and is never handed to a trainer in this form.
renders_via: antigravity (manual, owner-run)
audience: TRAINER ONLY — internal use, never student-facing
course: Techno Square Academy — MICROBIT-HW-L1
session: 1 of 8
duration: 120 minutes
source: 70-localized/L1-s1.md
contract: 00-contracts/brand-and-output.md
template: >-
  Exact 23-section, 6-page session template extracted from
  PICTOBLOX-2D-ADV-L1-Trainer-Guide-v1.0. Section names and order are copied
  deliberately so trainers recognise the document.
---

# Session 1 — Name Badge / بطاقة الاسم

> **INTERNAL USE ONLY.** Nothing on this page goes on a student slide.

---

# Page 1 — Session Overview

| | | | |
| --- | --- | --- | --- |
| **Course** | micro:bit Hardware Studio | **Duration** | 120 Minutes |
| **Level** | Level 1 — Session 1 | **Session Type** | Hardware Foundations / Hands-on Lab |
| **Age Group** | *see note* | **Difficulty** | Beginner |

> **Age band unconfirmed.** PictoBlox L1 is 11–13; the micro:bit upstream material
> targets younger. Confirm with the academy before this guide is finalised.

## MAIN CONCEPT

الطالب يفهم إن الـ **micro:bit** كمبيوتر حقيقي صغير، بيسمع كلامنا لما نديله
تعليمات مرتبة (**algorithm**)، وإن شاشة الـ **LED** بتاعته **output** — حاجة
بتطلع من الكمبيوتر ونقدر نشوفها.

## PROGRAMMING FOCUS

MakeCode interface · Toolbox · Workspace · Simulator · Download · `forever` ·
`show string` · `on start` (debug lab) · `show icon` (extension only)

## SESSION GOAL

الطالب يبني أول برنامج ليه — **Name Badge** بيعرض اسمه بيتحرك على شاشة الـ LED —
يحمّله على جهاز حقيقي، يصلّح تلات أخطاء مقصودة، ويشرح الكود بتاعه بنفسه.

## LEARNING OBJECTIVES

- أقدر أشرح إن الـ micro:bit كمبيوتر صغير
- أقدر أشرح إن الكمبيوتر محتاج تعليمات مرتبة (**algorithm**)
- أقدر أسمّي أجزاء محرر **MakeCode** وأستخدمها
- أقدر أبني **Name Badge** بـ `forever` و `show string`
- أقدر أحمّل الكود على جهاز حقيقي وأتأكد إنه شغال
- أقدر أدوّر على **bug** بسيط وأصلّحه
- أقدر أشرح الكود بتاعي لزميلي

## REQUIRED MATERIALS

- micro:bit + **data** USB cable (not charge-only), one per student
- Battery pack per micro:bit
- Laptop with browser — `https://makecode.microbit.org/`
- Projector
- Three pre-broken projects for the Debugging Lab (see Page 5)
- Exit ticket slips
- Project naming sheet
- Logo + TATA assets

---

# Page 2 — Session Flow

## TIME · SESSION STEP

| TIME | SESSION STEP |
| --- | --- |
| 00:00-00:08 | Welcome, course promise, what we build in 8 sessions |
| 00:08-00:18 | Screen-free hook — computers in disguise (no devices) |
| 00:18-00:28 | What is a micro:bit? Hardware tour, pass the device around |
| 00:28-00:32 | Learning objectives |
| 00:32-00:44 | MakeCode editor tour + 60 seconds free exploration |
| 00:44-00:54 | Examine the code — predict before reveal |
| 00:54-01:14 | Build: 4 steps, simulator test after every step |
| 01:14-01:24 | Download to the physical micro:bit and test |
| 01:24-01:39 | **Debugging Lab** — three broken programs, students fix them |
| 01:39-01:46 | Extend / support tier |
| 01:46-01:54 | Share — pair demo, each student explains their own code |
| 01:54-02:00 | Recap, exit ticket, save and name project |

*Verified contiguous, 00:00 → 02:00, 120 minutes exactly.*

## BEFORE THE SESSION

- Open MakeCode on the trainer laptop
- Prepare a sample finished project
- **Prepare the three broken projects for the Debugging Lab**
- Test the download path on the school machines — USB write permission is the
  usual failure point
- Confirm students can save files
- Check projector visibility for block screenshots
- Prepare logo/TATA as branding only
- Have two known-good spare USB **data** cables

## CLASSROOM / QA FOCUS

- Devices stay closed during the screen-free hook — announce it before handing out
- Battery packs held back until the hardware tour, or they become the lesson
- Test after every build step, not once at the end
- Team roles when pairing: **Builder / Checker**
- Pair a struggling student with the tutorial, not with a stronger student who
  will simply build it for them
- Project naming and save checklist before anyone leaves

## TATA TIP

خلي أول Session سهلة ومبهجة. المهم إن الطالب يحس إن الكود بتاعه حرّك حاجة
حقيقية في إيده — مش إنه يحفظ أسماء البلوكات.

---

# Page 3 — Trainer Script & Interaction

## TRAINER SAYS

النهارده هنشوف كمبيوتر صغير قد كف الإيد، وهنخليه يعرض اسمنا. مش هنكتب كود كتير —
هنفهم إزاي الكمبيوتر بينفّذ التعليمات اللي إحنا بنكتبها، بالترتيب اللي إحنا
عايزينه.

## ASK STUDENTS

- إيه الحاجة اللي في البيت فيها كمبيوتر وشكلها مش كمبيوتر؟
- الـ micro:bit ده كمبيوتر ازاي وهو صغير كده؟
- إيه اللي يخلي الكود يفضل شغال ومايقفش؟
- لو عايز اسمي يظهر، أستخدم أنهي بلوك؟
- إيه الفرق بين الـ **Simulator** والجهاز الحقيقي؟

## EXPECTED ANSWERS

- الميكروويف، الغسالة، التلفزيون، العربية، الساعة الذكية
- مش الحجم اللي بيحدد؛ اللي بيحدد إنه بينفّذ تعليمات
- بلوك **`forever`** — حلقة بتكرر الكود طول الوقت
- **`show string`** — بيعرض كلام بيتحرك على شاشة الـ LED
- الـ Simulator بيجرّب على الشاشة؛ الجهاز الحقيقي محتاج **Download**

## TRAINER NOTES

استخدم تشبيه: الـ `forever` زي حاجة بتلفّ وترجع من الأول على طول. تجنّب شرح كل
واجهة MakeCode بالتفصيل — ركّز على الأربع مناطق اللي هيستخدمها الطالب النهاردة
بس. الـ **algorithm** كلمة كبيرة على ودن صغيرة، فاربطها بحاجة ملموسة: تعليمات
مرتبة، لو غيّرت الترتيب النتيجة تتغيّر.

**Verified:** the official MakeCode Name Tag project genuinely places
`show string` inside `forever`. Canonical — do not "correct" it to `on start`.

## ENGAGEMENT MOVES

- اطلب **Hands Up** قبل كشف الإجابة في الـ hook
- خلي الطالب **يتوقع النتيجة قبل الـ Run** — كل خطوة في البناء
- استخدم **One-Minute Pair Explain** بعد ما الكود يشتغل
- اختار **Demo Student** لخطوة واحدة بس، مش للدرس كله
- مرّر الجهاز في إيدين الطلاب وهم بيسمعوا، مش بعدين

## DIFFERENTIATION

- **Support:** step card أو التدريب خطوة بخطوة (`https://mbit.io/tutorial-name-badge`)، أو starter project جاهز
- **Core:** Name Badge شغّال بالاسم بتاع الطالب على جهاز حقيقي
- **Extension:** كلمات أو أرقام إضافية، أو `show icon` تعبّر عن المزاج
- **Challenge:** اكتشاف الـ bug من غير تلميح مباشر في الـ Debugging Lab

---

# Page 4 — Activity Guide

## Activity 1 — Computers in Disguise *(screen-free)*

الطلاب يقولوا أجهزة في البيت جواها كمبيوتر وشكلها مش كمبيوتر. 6–8 إجابات قبل أي
كشف. الأجهزة لسه مقفولة.

## Activity 2 — Hardware Tour

كل طالب يمسك جهازه ويدوّر بنفسه على:

| Part | Arabic | Job |
| --- | --- | --- |
| **LED display** | الشاشة | output — 25 لمبة بنتحكم فيهم |
| **Buttons A / B** | الأزرار | input — هنستخدمهم من Session 3 |
| **USB port** | مدخل الـ USB | منه بيدخل الكود |
| **Battery connector** | مكان البطارية | يشتغل من غير كمبيوتر |

## Activity 3 — Editor Tour *(split, two halves)*

**Part A — فين الكود:** Toolbox (صندوق الأدوات) · Workspace (مساحة العمل)
**Part B — نجرّب ونبعت:** Simulator (المحاكي) · Download (تحميل)

بعدها **60 ثانية ضغط حر** قبل ما تكمّل. هيعملوها في كل الأحوال؛ لما تجدولها
بتكسب الانتباه بدل ما تحارب عليه.

## Activity 4 — Build the Name Badge *(test after every step)*

1. مشروع MakeCode جديد. **اتوقّع:** مشروع فاضي هيعمل إيه؟
2. هات `forever` من الـ Toolbox → simulator: لسه مفيش حاجة. ليه؟
3. حط `show string` جواه، اكتب **اسمك** → simulator: الاسم بيتحرك
4. غيّر الاسم لحاجة تانية → simulator: اتغيّر

## Activity 5 — Download to Hardware

وصّل الـ USB → دوس **Download** → شوف اسمك على الجهاز الحقيقي.

## Final Challenge — Fix It Yourself

في الـ Debugging Lab، الطالب يكتشف الـ bug بنفسه من غير تلميح مباشر، ويشرح
إزاي عرف.

## PROJECT COMPLETION CHECK

قبل اعتبار المشروع مكتمل: الاسم بتاع الطالب بيتحرك على **الجهاز الحقيقي** مش
الـ simulator بس، الطالب اختبر وغيّر الاسم مرة على الأقل، ويشرح دور البلوكين
من غير ما يقرأ من الشاشة.

## CODE EXPLANATION ROUTINE

لكل script اسأل: **What starts it?** إيه اللي بيشغّله؟ · إيه اللي بيتغيّر؟ ·
إيه النتيجة المتوقعة؟ · إزاي نختبرها؟ · إيه أشهر bug ممكن يحصل هنا؟

---

# Page 5 — Questions Bank & Debugging

## Questions Bank

**Concept**
ليه الكمبيوتر محتاج التعليمات تكون مرتبة؟

**Output**
إيه يعني كلمة **output**؟ هات مثال من الجهاز اللي في إيدك.

**Loops**
لو شيلنا الـ `forever`، إيه اللي هيحصل للاسم؟

**Debugging**
لو الاسم ظهر مرة واحدة وبعدين وقف — تفحص إيه الأول؟

**Design**
لو عايز الاسم يظهر أبطأ، تغيّر إيه؟

## Debugging Lab — the three seeded bugs

Students **predict** what is wrong before touching anything, then fix it on
their own machine.

| # | Seeded program | What they see | Fix |
| --- | --- | --- | --- |
| 1 | `on start` + `show string "اسمي"` | الاسم بيظهر مرة واحدة وبعدين يقف | استبدل `on start` بـ `forever` |
| 2 | `forever` + `show string "Hello!"` | اسم غلط بيتحرك | اكتب اسمك مكان `"Hello!"` |
| 3 | `forever` فاضي، و `show string` سايب بره | مفيش أي حاجة بتظهر خالص | اسحب `show string` جوه الـ `forever` |

> **Why bug 1 uses `on start`:** a `show string` block left loose on the
> workspace, attached to no handler, never runs at all — it does not produce
> "shows once then stops." `on start` is the block that genuinely runs exactly
> once. Bug 3 is the true unattached-block case, and its correct symptom is
> nothing happening at all.

اسأل بعد كل واحد: **إيه اللي كان غلط؟ عرفت منين؟** التفكير أهم من الإصلاح.

## PROBLEM · TRAINER RESPONSE / DEBUGGING

| Problem | Trainer response |
| --- | --- |
| الاسم بيظهر مرة واحدة | راجع الـ handler — `on start` ولا `forever`؟ |
| مفيش أي حاجة بتظهر | البلوك جوه الـ handler ولا سايب بره؟ |
| اسم غلط بيتحرك | النص لسه `"Hello!"` — الطالب مكتبش اسمه |
| الجهاز مش ظاهر كـ drive | كابل شحن مش data — غيّر الكابل |
| نزّل بس مفيش تغيير | الـ `.hex` في Downloads — لازم يتسحب على drive الـ MICROBIT |
| الشاشة بتلمع بسرعة غريبة | بطارية ضعيفة أو توصيل USB مش ثابت |

## DEBUGGING ROUTINE

1) Correct project open → 2) **Handler** (`forever` / `on start`) →
3) Block **inside** the handler → 4) Text content correct →
5) Download actually flashed → 6) Test one thing at a time

---

# Page 6 — Assessment & Reflection

## TRAINER CHECKLIST

استخدم القائمة أثناء التطبيق:

- ☐ يسمّي جهاز في البيت جواه كمبيوتر
- ☐ يقول إن الـ micro:bit كمبيوتر صغير
- ☐ يستخدم كلمة **algorithm** لتعليمات مرتبة
- ☐ يحدّد Toolbox / Workspace / Simulator / Download
- ☐ يبني Name Badge شغّال باسمه هو
- ☐ يحمّله على **جهاز حقيقي** ويشتغل
- ☐ يصلّح واحد على الأقل من التلات bugs
- ☐ يشرح الكود بتاعه من غير مساعدة
- ☐ يحفظ المشروع بالاسم الصح

## TRAINER REFLECTION

- هل الطلاب فهموا إن الـ `forever` هو سبب التكرار، ولا حفظوا اسم البلوك بس؟
- هل حصل خلط بين الـ Simulator والجهاز الحقيقي؟
- كام طالب احتاج الـ support tier؟ ده مؤشر لسرعة Session 2.
- هل الـ Debugging Lab كان صعب زيادة ولا سهل زيادة للمجموعة دي؟
- هل كل طالب حفظ المشروع باسم صحيح؟

## SUCCESS CRITERIA

الطالب ينجح إذا شغّل **Name Badge** باسمه على جهاز حقيقي، صلّح واحد على الأقل من
الـ bugs المقصودة، ويشرح دور `forever` و `show string` بكلامه هو.

## STUDENT NOTEBOOK / HOME TASK

اكتب اسم البلوكين اللي استخدمتهم النهاردة وجنب كل واحد بيعمل إيه. وارسم شكل
الشاشة وهي بتعرض أول حرف من اسمك.

*(Home Task is carried to the family by the separate 3-slide Student Summary
deck — see `home-summary.md`.)*

## Exit ticket

Three questions, on a slip, individually:

1. الـ micro:bit ده إيه؟ (جملة واحدة)
2. اكتب اسم البلوكين اللي استخدمتهم
3. لو الاسم ظهر مرة واحدة وبعدين وقف — إيه اللي غلط؟

Q3 is the discriminator. A student who answers it has understood the loop; a
student who only parrots Q2 has not.

## Answer key

- **Handler:** `forever`
- **Block:** `show string` with the learner's own name
- **Expected behaviour:** the name scrolls continuously across the LED display
- **Success criterion:** learner's own name visibly scrolling on the **physical
  device**, and the learner can name and explain the two blocks used

## Common mistakes

| Mistake | What you will see | Fix |
| --- | --- | --- |
| Placeholder text unchanged | `"Hello!"` scrolling | type their own name |
| `on start` instead of `forever` | name shows once, then stops | swap the handler |
| Block outside any handler | nothing happens at all | drag inside `forever` |
| Charge-only USB cable | device never appears as a drive | swap the cable |
| Downloaded but not flashed | `.hex` sits in Downloads | drag onto the MICROBIT drive |

## Trainer resources — NOT for student slides

Trainer preview only:
- micro:bit introduction — `https://youtu.be/u2u7UJSRuko`
- Name badge introduction — `https://youtu.be/teC0wzWF4tI`
- Coding walkthrough — `https://mbit.io/lessons-name-code-video`

Per `00-contracts/brand-and-output.md` §7 these are trainer references only. They
must never appear as student slide content — the academy teaches interactively.
