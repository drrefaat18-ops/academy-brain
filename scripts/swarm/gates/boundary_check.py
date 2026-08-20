"""Detect trainer-only content leaking into student-facing output.

Brain OS, Academy_Language_and_Output_Rules.md: student-facing outputs must
NOT include trainer scripts, trainer timing, internal notes, assessment
checklists, or classroom management notes.
"""

from __future__ import annotations

from swarm.gates import FAIL, PASS, UNVERIFIED, GateResult, register

TRAINER_MARKERS: tuple[str, ...] = (
    "trainer note",
    "trainer script",
    "trainer question",
    "expected answer",
    "common mistakes",
    "classroom management",
    "assessment checklist",
    "minutes for this",
    "ملاحظة للمدرب",
    "إجابة متوقعة",
    "دليل المدرب",
)


@register("trainer-boundary")
def check(text: str) -> GateResult:
    """Fail if any trainer-only marker appears in student-facing text."""
    if not text.strip():
        return GateResult("trainer-boundary", UNVERIFIED, "no content to scan", {})

    lowered = text.lower()
    matches = [m for m in TRAINER_MARKERS if m.lower() in lowered]

    if matches:
        return GateResult(
            "trainer-boundary",
            FAIL,
            f"{len(matches)} trainer-only marker(s) in student output",
            {"matches": matches},
        )
    return GateResult("trainer-boundary", PASS, "no trainer content detected", {})
