---
type: template
scope: academy-wide
domain: neutral
status: extracted
extracted_from: 75-bundle/L1-s1 (slides 16-19, trainer-guide.md Page 5)
extracted_on: 2026-08-22
enforced_by:
  - 00-contracts/brand-and-output.md:115   # debugging segment is academy law
  - 75-bundle/_TEMPLATE-blueprint.md:140   # gate D15, per session
---

# Debugging Lab — design template

The **requirement** ("break the code on purpose, students fix it") is already
academy law and survives any archive. The **know-how** does not. This file is
that know-how, stated without reference to any one platform.

Every session needs a debugging lab. This is how to build one.

---

## 1. Design rules — non-negotiable

### Rule 1 — state the symptom, never the fault

A bug slide says what the student **observes**. It never names the broken
construct.

- ✅ "the name shows once then stops"
- ✅ "it shows `Hello!` not my name"
- ✅ "nothing shows at all"
- ❌ "the loop block is missing"
- ❌ "the handler is wrong"

Naming the fault destroys the exercise. The student is being taught to
reason from symptom to cause; handing over the cause skips the entire skill.

### Rule 2 — predict before fix, every time

Each bug slide ends with the same prompt, worded identically across all bugs:

> `اتوقّع الأول: إيه اللي غلط؟` — *predict first: what's wrong?*

(Bug 3 in L1-s1 varies it to `إيه الناقص؟` — *what's missing?* — because the
symptom is absence, not wrongness. Vary only when the symptom class demands it.)

This matches the predict-before-run rule at `brand-and-output.md:113`. The
prediction is the assessed act. Fixing is secondary.

### Rule 3 — one failure mode per bug, escalating

Bugs form a ladder, not a set. Each isolates exactly one failure mode, and the
severity climbs:

| Rung | Failure class | Student sees |
|---|---|---|
| 1 | **Lifecycle** — runs, but not for the right duration | partial success |
| 2 | **Content** — right structure, wrong data | runs, wrong output |
| 3 | **Scope** — code exists but is never reached | total failure |

Never two faults in one program. Never two programs testing the same class.

### Rule 4 — fixed slide shape

```
1 intro slide  ("today we are bug-fixers — I'll show you N broken programs")
N bug slides   (symptom → predict prompt → screenshot of the broken program)
```

The mascot pose is bound to debugging throughout (`brand-and-output.md:201`).
Use the thinking pose on the intro and every bug slide. Do not vary it — the
pose is the visual cue that this is a reasoning segment.

### Rule 5 — trainer side is part of the deliverable

A debugging lab is not done when the slides are done. It also ships:

- a **questions bank** — one open question per concept in the session, including
  one debugging question phrased as a symptom
- a **seeded-bug table** — `# | seeded program | what they see | fix`
- a **problem → trainer response** table, covering both the seeded bugs *and*
  the environmental failures that look like bugs (wrong cable, file not flashed,
  weak power, device not mounting)
- a **debugging routine** — an ordered checklist the student runs top-down,
  cheapest check first

The environmental rows matter as much as the seeded ones. Most classroom
"bugs" are not in the code.

### Rule 6 — hard verification (`blueprint.md:126`)

**Production must confirm each seeded program actually reproduces its stated
symptom.** Run it. Observe it. Record the observation.

An unverified seeded bug makes children fake debugging evidence — they "fix"
something that was never broken the way the slide claims, and the trainer
confirms it. This is the single most damaging failure mode in the segment and
it is invisible without an explicit check.

Non-negotiable. Carries to every domain unchanged.

---

## 2. Choosing the three bugs — the trap

Picking a fault is easy. Picking a fault whose **symptom matches the slide** is
where this goes wrong.

Worked example from L1-s1, and the reason it was rewritten once:

> A block left loose on the workspace, attached to no handler, **never runs at
> all**. It does not produce "shows once then stops." The block that genuinely
> runs exactly once is the run-once handler.
>
> So: rung 1 (lifecycle) must use the run-once handler. Rung 3 (scope) is the
> true unattached-block case, and its correct symptom is nothing happening.

Generalised: **derive the symptom from the fault by executing it, not by
reasoning about it.** Intuition about what a fault "looks like" is wrong often
enough to matter, and the error is only visible in the classroom.

---

## 3. Worked example — L1-s1 (micro:bit), for shape only

Domain-specific. Reproduce the *structure*, not the content.

| # | Seeded program | What they see | Fix | Class |
|---|---|---|---|---|
| 1 | `on start` + `show string "<name>"` | name appears once, then stops | swap `on start` → `forever` | lifecycle |
| 2 | `forever` + `show string "Hello!"` | wrong name scrolls | type own name over `"Hello!"` | content |
| 3 | empty `forever`, `show string` loose outside | nothing appears at all | drag `show string` inside `forever` | scope |

Debugging routine used:

1. correct project open →
2. **handler** correct →
3. block **inside** the handler →
4. text content correct →
5. build actually deployed →
6. test one thing at a time

Ask after each: **what was wrong? how did you know?** The reasoning matters more
than the fix.

---

## 4. Porting to a new domain

Fill the same three rungs with domain-native faults, then verify each by running it.

| Rung | Ask | Example shape in a motor/robot domain |
|---|---|---|
| 1 lifecycle | what runs once when it should repeat? | action in the run-once block instead of the loop |
| 2 content | what runs correctly with wrong values? | correct drive command, wrong duration/port/power |
| 3 scope | what never runs at all? | code below an unterminated wait, or on an unreached branch |

Then:

1. Build all three programs in the real environment.
2. Run each. Write down what actually happened.
3. If the observation differs from the intended symptom, **change the bug, not
   the slide text.** The slide states observed reality.
4. Record the verification in the session receipt. Rule 6 is a gate, not advice.

---

## 5. Gate checklist

A debugging lab passes when all of these hold:

- [ ] N ≥ 3 bugs, one per failure class, escalating
- [ ] every slide states a symptom, no slide names a fault
- [ ] identical predict-first prompt on every bug slide
- [ ] thinking mascot pose on intro + all bug slides
- [ ] each seeded program executed and its symptom observed and recorded
- [ ] trainer guide carries: questions bank, seeded-bug table, problem→response
      table including environmental failures, ordered debugging routine
- [ ] the segment has its own contiguous block in the session timeline

---

## 6. Note for the archive

In L1-s1 this segment is load-bearing twice. `b-03` — the bug-1 slide — is the
one slide that rendered correctly in the entire failed production run, and is
the designated evidence-region regression fixture. Keep it reachable.
