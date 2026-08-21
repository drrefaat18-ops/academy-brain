import pytest

from swarm import paths


def test_exactly_fourteen_session_ids():
    assert len(paths.SESSION_IDS) == 14
    assert paths.SESSION_IDS[0] == "L1-s1"
    assert paths.SESSION_IDS[-1] == "L2-s7"


@pytest.mark.parametrize("sid", ["L1-s1", "L1-s7", "L2-s1", "L2-s7"])
def test_validate_accepts_real_ids(sid):
    assert paths.validate_session_id(sid) == sid


@pytest.mark.parametrize("bad", ["L3-s1", "L1-s8", "L1-s0", "l1-s1", "L1 s1", "L1-s01", ""])
def test_validate_rejects_malformed_ids(bad):
    with pytest.raises(ValueError):
        paths.validate_session_id(bad)


def test_digest_path_is_derived_not_searched():
    p = paths.digest_path("L1-s3")
    assert p.name == "L1-s3.md"
    assert p.parent.name == "10-digest"


def test_assets_dir_is_per_session():
    assert paths.assets_dir("L2-s4").as_posix().endswith("10-digest/_assets/L2-s4")


def test_lane_paths_never_collide_across_providers():
    lanes = {
        paths.lane_path("40-critique", "L1-s3", provider)
        for provider in ("codex", "opencode", "hermes")
    }
    assert len(lanes) == 3


def test_lane_path_rejects_unknown_provider():
    with pytest.raises(ValueError):
        paths.lane_path("40-critique", "L1-s3", "gpt5")


def test_merged_path_has_single_owner_per_session():
    assert paths.merged_path("50-patch", "L1-s3").name == "L1-s3.md"


def test_receipt_path_includes_gate_name():
    p = paths.receipt_path("L1-s3", "arabic-ratio")
    assert p.name == "L1-s3.arabic-ratio.yaml"
    assert p.parent.name == "90-receipts"
