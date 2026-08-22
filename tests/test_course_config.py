from pathlib import Path

import pytest

from swarm.config import CourseConfigError, StageDirectories, load_course


VALID_CONFIG = """\
levels: [1, 2]
sessions_per_level: 8
providers: [claude, codex, opencode, hermes]
artifact_schedule:
  s1: true
  s2: true
  s3: true
  s4: true
  s5: true
  s6: true
  s7: true
  s8: false
stages:
  digest: 10-digest
  digest_assets: _assets
  provenance: 20-provenance
  receipts: 90-receipts
asset_discovery:
  asset_ref_pattern: '`(img-[^`]+[.]png)`'
  asset_source_files: [slides-source.md]
  expect_references: true
"""


def write_config(root: Path, text: str = VALID_CONFIG) -> None:
    (root / "course.yaml").write_text(text, encoding="utf-8")


def test_load_course_returns_typed_validated_config(tmp_path):
    write_config(tmp_path)

    config = load_course(tmp_path)

    assert config.levels == (1, 2)
    assert config.sessions_per_level == 8
    assert config.providers == frozenset({"claude", "codex", "opencode", "hermes"})
    assert config.artifact_schedule == (True, True, True, True, True, True, True, False)
    assert config.produces_artifacts("L1-s7") is True
    assert config.produces_artifacts("L2-s8") is False
    assert config.stages == StageDirectories(
        digest="10-digest",
        digest_assets="_assets",
        provenance="20-provenance",
        receipts="90-receipts",
    )


def test_load_course_missing_file_is_actionable(tmp_path):
    with pytest.raises(CourseConfigError, match=r"course\.yaml.*does not exist"):
        load_course(tmp_path)


@pytest.mark.parametrize(
    ("text", "message"),
    [
        ("levels: [1\n", "invalid YAML"),
        (VALID_CONFIG.replace("sessions_per_level: 8", "sessions_per_level: 0"), "sessions_per_level"),
        (VALID_CONFIG.replace("providers: [claude, codex, opencode, hermes]", "providers: []"), "providers"),
        (VALID_CONFIG.replace("  s8: false\n", ""), "artifact_schedule.s8"),
        (VALID_CONFIG.replace("  s8: false", "  s8: sometimes"), "artifact_schedule.s8"),
        (VALID_CONFIG.replace("  receipts: 90-receipts\n", ""), "stages.receipts"),
        (VALID_CONFIG + "unexpected: true\n", "unknown field"),
    ],
)
def test_load_course_rejects_malformed_config(tmp_path, text, message):
    write_config(tmp_path, text)

    with pytest.raises(CourseConfigError, match=message):
        load_course(tmp_path)


def test_non_string_source_file_is_a_config_error_not_a_typeerror(tmp_path):
    """C5-03. set() on a list holding a YAML mapping raised an unhashable-type
    TypeError from inside the validator, making its own error branch unreachable."""
    write_config(
        tmp_path,
        VALID_CONFIG.replace(
            "asset_source_files: [slides-source.md]",
            "asset_source_files:\n    - {a: 1}",
        ),
    )

    with pytest.raises(CourseConfigError, match="must be non-empty strings"):
        load_course(tmp_path)
