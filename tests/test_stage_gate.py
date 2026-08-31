import datetime as dt

import pytest
import yaml

from swarm import stage_gate

TODAY = dt.date(2026, 9, 1)


@pytest.fixture
def vault(tmp_path):
    for stage in stage_gate.STAGE_CHAIN:
        (tmp_path / stage.directory).mkdir(parents=True, exist_ok=True)
    return tmp_path


def _evidence(vault, sid, *stages):
    """Write the minimum artifact that satisfies each named stage."""
    for name in stages:
        stage = next(s for s in stage_gate.STAGE_CHAIN if s.name == name)
        rel = stage.pattern.format(sid=sid, level=sid.split("-")[0].lstrip("L"))
        rel = rel.replace("*", "x")
        path = vault / stage.directory / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("evidence", encoding="utf-8")


def _waiver(vault, sid, stage_name, **fields):
    stage = next(s for s in stage_gate.STAGE_CHAIN if s.name == stage_name)
    path = stage_gate.waiver_path(vault, stage, sid)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(fields, sort_keys=False), encoding="utf-8")
    return path


# --- the failure this gate exists to prevent -------------------------------


def test_bundle_is_refused_when_research_and_critique_were_skipped(vault):
    """The exact EV3 shape: receipts -> digest -> provenance -> straight to bundle."""
    _evidence(vault, "L1-s1", "receipts", "digest", "provenance")
    results = stage_gate.check(vault, "L1-s1", "bundle", TODAY)
    failed = {r["stage"] for r in results if r["verdict"] == stage_gate.FAIL}
    assert {"research", "critique", "patch", "refuted", "approved", "localized"} <= failed
    assert stage_gate.receipt("L1-s1", "bundle", results)["overall"] == stage_gate.FAIL


def test_complete_chain_passes(vault):
    names = [s.name for s in stage_gate.STAGE_CHAIN]
    _evidence(vault, "L1-s1", *names[: names.index("bundle")])
    results = stage_gate.check(vault, "L1-s1", "bundle", TODAY)
    assert stage_gate.receipt("L1-s1", "bundle", results)["overall"] == stage_gate.PASS


def test_only_predecessors_are_checked(vault):
    _evidence(vault, "L1-s1", "receipts")
    assert [r["stage"] for r in stage_gate.check(vault, "L1-s1", "research", TODAY)] == [
        "receipts"
    ]


# --- waivers must be structured, authorized, and expiring -------------------


def test_valid_not_applicable_waiver_satisfies_a_stage(vault):
    _waiver(
        vault, "L1-s1", "critique",
        reason="not-applicable", authority="owner", scope="session",
        granted=dt.date(2026, 8, 31),
    )
    ok, detail = stage_gate.check_stage(vault, stage_gate._BY_NAME["critique"], "L1-s1", TODAY)
    assert ok and "not-applicable" in detail


def test_blocked_waiver_without_expiry_is_refused(vault):
    """A permanent exemption wearing a temporary label."""
    _waiver(
        vault, "L1-s1", "critique",
        reason="blocked", authority="owner", scope="session", granted=dt.date(2026, 8, 31),
    )
    ok, detail = stage_gate.check_stage(vault, stage_gate._BY_NAME["critique"], "L1-s1", TODAY)
    assert not ok and "requires an `expires`" in detail


def test_expired_waiver_is_refused(vault):
    _waiver(
        vault, "L1-s1", "critique",
        reason="blocked", authority="owner", scope="session",
        granted=dt.date(2026, 8, 1), expires=dt.date(2026, 8, 30),
    )
    ok, detail = stage_gate.check_stage(vault, stage_gate._BY_NAME["critique"], "L1-s1", TODAY)
    assert not ok and "expired" in detail


def test_free_text_reason_is_refused(vault):
    """'not applicable' as prose is what EV3's contract already asked for, and got."""
    _waiver(
        vault, "L1-s1", "critique",
        reason="we didn't have time", authority="owner", scope="session",
        granted=dt.date(2026, 8, 31),
    )
    ok, _ = stage_gate.check_stage(vault, stage_gate._BY_NAME["critique"], "L1-s1", TODAY)
    assert not ok


def test_waiver_missing_authority_is_refused(vault):
    _waiver(vault, "L1-s1", "critique", reason="not-applicable", scope="session",
            granted=dt.date(2026, 8, 31))
    ok, detail = stage_gate.check_stage(vault, stage_gate._BY_NAME["critique"], "L1-s1", TODAY)
    assert not ok and "authority" in detail


def test_superseded_waiver_must_name_what_covers_it(vault):
    _waiver(vault, "L1-s1", "critique", reason="superseded", authority="owner",
            scope="session", granted=dt.date(2026, 8, 31))
    ok, detail = stage_gate.check_stage(vault, stage_gate._BY_NAME["critique"], "L1-s1", TODAY)
    assert not ok and "covered_by" in detail


def test_malformed_waiver_is_refused_not_ignored(vault):
    stage = stage_gate._BY_NAME["critique"]
    stage_gate.waiver_path(vault, stage, "L1-s1").write_text("[: not yaml", encoding="utf-8")
    ok, _ = stage_gate.check_stage(vault, stage, "L1-s1", TODAY)
    assert not ok


def test_a_waiver_file_is_not_itself_evidence(vault):
    """A waiver lives in the stage directory; it must never glob as an artifact."""
    _waiver(vault, "L1-s1", "patch", reason="not-applicable", authority="owner",
            scope="session", granted=dt.date(2026, 8, 31))
    stage = stage_gate._BY_NAME["patch"]
    hits = [p for p in (vault / stage.directory).glob("L1-s1.*")]
    assert hits, "fixture wrote nothing"
    ok, detail = stage_gate.check_stage(vault, stage, "L1-s1", TODAY)
    assert ok and "waived" in detail  # satisfied as a waiver, not counted as an artifact


# --- doctrine does not run backwards ---------------------------------------


def _golden(vault, sid, name="deck-a.LOCKED-GOLDEN.pdf", sub=None):
    d = vault / "80-generation" / sid / (sub or "")
    d.mkdir(parents=True, exist_ok=True)
    (d / name).write_bytes(b"%PDF-1.4 locked")


def test_a_locked_session_is_not_re_judged(vault):
    """A shipped session predates this gate; failing it now improves nothing."""
    _golden(vault, "L1-s1")
    results = stage_gate.check(vault, "L1-s1", "bundle", TODAY)
    assert all(r["verdict"] == stage_gate.PASS for r in results)
    assert "not re-judged" in results[0]["detail"]


def test_a_rejected_golden_is_not_a_lock(vault):
    """_rejected/ holds incident evidence, including goldens locked in error."""
    _golden(vault, "L2-s1", name="deck-a-LOCKED-GOLDEN-IN-ERROR.pdf", sub="_rejected")
    results = stage_gate.check(vault, "L2-s1", "bundle", TODAY)
    assert any(r["verdict"] == stage_gate.FAIL for r in results)


def test_an_unlocked_session_is_still_gated(vault):
    """The grandfather clause covers shipped work only, never everything."""
    _golden(vault, "L1-s1")  # a DIFFERENT session is locked
    assert not stage_gate.is_locked(vault, "L2-s8")
    results = stage_gate.check(vault, "L2-s8", "bundle", TODAY)
    assert all(r["verdict"] == stage_gate.FAIL for r in results)


# --- guards ----------------------------------------------------------------


def test_unknown_stage_raises_rather_than_passing(vault):
    with pytest.raises(stage_gate.StageGateError):
        stage_gate.check(vault, "L1-s1", "no-such-stage", TODAY)


def test_bad_session_id_is_refused(vault):
    with pytest.raises(Exception):
        stage_gate.check(vault, "../../etc", "bundle", TODAY)


def test_receipt_stamps_the_doctrine_version(vault):
    doc = stage_gate.receipt("L1-s1", "bundle", [])
    assert doc["doctrine_version"] == stage_gate.DOCTRINE_VERSION
