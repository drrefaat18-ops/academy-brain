"""Refuse to advance a session past a stage whose predecessors have no evidence.

Every other gate in this vault judges the TEXT of one artifact. This one judges
the VAULT: it answers "may this session enter stage X at all", which is the
question nothing was asking when an entire course ran 90-receipts -> 75-bundle
and skipped research, critique, patch, refutation, approval and localization
without a single complaint.

A stage is satisfied by evidence or by a valid waiver. Nothing else. A waiver is
a structured document with a named authority and an expiry date, because the one
course that DID carry a written "record why the stage is not applicable" rule in
its contract recorded nothing at all and shipped fifteen sessions anyway. Prose
that asks for a justification is not a gate; this file is the gate.

Scope note: this checks that evidence EXISTS and that waivers are VALID. It does
not check that evidence is fresh relative to its predecessor.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

from .paths import validate_session_id

# Bumped when the stage chain or the waiver contract changes in a way that would
# alter a verdict. Stamped into every receipt so a later doctrine change can
# never silently reinterpret an artifact that passed under earlier rules.
DOCTRINE_VERSION = 1

PASS = "PASS"
FAIL = "FAIL"

# Reasons a stage may legitimately be skipped. Free text is not one of them:
# "not applicable" with no vocabulary behind it is how a permanent exemption
# gets laundered out of a temporary blockage.
WAIVER_REASONS = frozenset(
    {
        "not-applicable",  # the stage cannot apply to this session, ever
        "blocked",  # the stage is owed and not yet done — MUST carry an expiry
        "superseded",  # another session's artifact covers this one, named in `covered_by`
    }
)
_TERMINAL_REASONS = frozenset({"not-applicable", "superseded"})


@dataclass(frozen=True)
class Stage:
    """One stage of the pipeline and what counts as evidence for it."""

    name: str
    directory: str
    pattern: str  # glob, with {sid} and {level} substituted
    scope: str  # "session" or "level"


# The chain, in order. A stage's prerequisites are every stage before it.
STAGE_CHAIN: tuple[Stage, ...] = (
    Stage("receipts", "90-receipts", "{sid}.*.yaml", "session"),
    Stage("research", "30-research", "*.md", "level"),
    Stage("digest", "10-digest", "{sid}.md", "session"),
    Stage("provenance", "20-provenance", "{sid}.md", "session"),
    Stage("critique", "40-critique", "{sid}/*.json", "session"),
    Stage("patch", "50-patch", "{sid}.md", "session"),
    Stage("refuted", "55-refuted", "{sid}.md", "session"),
    Stage("approved", "60-approved", "{sid}.md", "session"),
    Stage("localized", "70-localized", "{sid}.md", "session"),
    Stage("bundle", "75-bundle", "{sid}/*.md", "session"),
    Stage("generation", "80-generation", "{sid}/*", "session"),
)
_BY_NAME = {s.name: s for s in STAGE_CHAIN}


class StageGateError(RuntimeError):
    """The gate could not reach a verdict. Never reported as a pass."""


def _level_of(sid: str) -> str:
    """`L2-s5` -> `2`. Session ids are already validated before this runs."""
    return sid.split("-", 1)[0].lstrip("L")


def waiver_path(vault: Path, stage: Stage, sid: str) -> Path:
    return vault / stage.directory / f"{sid}.waiver.yaml"


def read_waiver(path: Path, today: _dt.date) -> tuple[bool, str]:
    """Return (valid, detail). A malformed waiver is invalid, never ignored."""
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return False, f"waiver {path.name} does not parse ({exc})"
    if not isinstance(doc, dict):
        return False, f"waiver {path.name} is not a YAML mapping"

    missing = [k for k in ("reason", "authority", "scope", "granted") if not doc.get(k)]
    if missing:
        return False, f"waiver {path.name} is missing required field(s): {', '.join(missing)}"

    reason = str(doc["reason"])
    if reason not in WAIVER_REASONS:
        return False, (
            f"waiver {path.name} reason {reason!r} is not one of "
            f"{', '.join(sorted(WAIVER_REASONS))}"
        )
    if reason == "superseded" and not doc.get("covered_by"):
        return False, f"waiver {path.name} claims 'superseded' but names no covered_by"

    expiry = doc.get("expires")
    if reason not in _TERMINAL_REASONS:
        # A 'blocked' waiver with no expiry is a permanent exemption wearing a
        # temporary label — the exact laundering this vocabulary exists to stop.
        if expiry is None:
            return False, f"waiver {path.name} reason 'blocked' requires an `expires` date"
    if expiry is not None:
        if isinstance(expiry, _dt.datetime):
            expiry = expiry.date()
        if not isinstance(expiry, _dt.date):
            return False, f"waiver {path.name} `expires` must be a YYYY-MM-DD date"
        if expiry < today:
            return False, f"waiver {path.name} expired on {expiry.isoformat()}"
    return True, f"waived: {reason} by {doc['authority']}"


def check_stage(vault: Path, stage: Stage, sid: str, today: _dt.date) -> tuple[bool, str]:
    """Is this one stage satisfied for this session — by evidence or by waiver?"""
    pattern = stage.pattern.format(sid=sid, level=_level_of(sid))
    directory = vault / stage.directory
    hits = [p for p in directory.glob(pattern) if p.is_file() and ".waiver." not in p.name]
    if hits:
        return True, f"{len(hits)} artifact(s) at {stage.directory}/{pattern}"

    wp = waiver_path(vault, stage, sid)
    if wp.is_file():
        return read_waiver(wp, today)
    return False, (
        f"no artifact matching {stage.directory}/{pattern} and no waiver at "
        f"{wp.relative_to(vault).as_posix()}"
    )


def check(vault: Path, sid: str, entering: str, today: _dt.date | None = None) -> list[dict]:
    """Check every stage that must be complete before `entering` begins."""
    validate_session_id(sid)
    if entering not in _BY_NAME:
        raise StageGateError(
            f"unknown stage {entering!r} — expected one of "
            f"{', '.join(s.name for s in STAGE_CHAIN)}"
        )
    vault = Path(vault)  # callers hand this in from argv and from other vaults
    today = today or _dt.date.today()
    index = [s.name for s in STAGE_CHAIN].index(entering)
    results = []
    for stage in STAGE_CHAIN[:index]:
        ok, detail = check_stage(vault, stage, sid, today)
        results.append({"stage": stage.name, "verdict": PASS if ok else FAIL, "detail": detail})
    return results


def receipt(sid: str, entering: str, results: list[dict]) -> dict:
    return {
        "id": sid,
        "entering": entering,
        "doctrine_version": DOCTRINE_VERSION,
        "overall": FAIL if any(r["verdict"] == FAIL for r in results) else PASS,
        "prerequisites": results,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("session_id")
    ap.add_argument("--entering", required=True, choices=[s.name for s in STAGE_CHAIN])
    ap.add_argument("--vault", type=Path, default=Path(__file__).resolve().parents[2])
    ap.add_argument("--out", type=Path, default=None, help="write a YAML receipt here")
    ns = ap.parse_args(argv)

    try:
        results = check(ns.vault, ns.session_id, ns.entering)
    except StageGateError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2

    doc = receipt(ns.session_id, ns.entering, results)
    if ns.out:
        ns.out.parent.mkdir(parents=True, exist_ok=True)
        ns.out.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), "utf-8")
    for r in results:
        print(f"  {r['verdict']:4} {r['stage']:12} {r['detail']}")
    print(f"{doc['overall']} — {ns.session_id} entering {ns.entering}")
    return 0 if doc["overall"] == PASS else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main(sys.argv[1:]))
