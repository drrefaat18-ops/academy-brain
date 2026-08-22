"""Validated per-course runtime configuration."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any

import yaml


class CourseConfigError(ValueError):
    """The course manifest is missing or violates its schema."""


@dataclass(frozen=True)
class StageDirectories:
    digest: str
    digest_assets: str
    provenance: str
    receipts: str


@dataclass(frozen=True)
class AssetDiscovery:
    """How this course names its assets and where they are referenced from.

    Lives here rather than in check_assets.py because two parsers for one file
    disagree eventually: the CLI accepted an ``asset_discovery`` section that
    ``load_course`` then rejected as an unknown field.
    """

    ref: re.Pattern[str]
    source_files: tuple[str, ...]


@dataclass(frozen=True)
class CourseConfig:
    levels: tuple[int, ...]
    sessions_per_level: int
    providers: frozenset[str]
    artifact_schedule: tuple[bool, ...]
    stages: StageDirectories
    asset_discovery: AssetDiscovery

    def produces_artifacts(self, sid: str) -> bool:
        """Return the manifest decision for a configured session ID."""
        if not isinstance(sid, str):
            raise ValueError(f"invalid session id {sid!r}")
        match = re.fullmatch(r"L([1-9][0-9]*)-s([1-9][0-9]*)", sid)
        if match is None:
            raise ValueError(f"invalid session id {sid!r}")
        level, session = (int(part) for part in match.groups())
        if level not in self.levels or session > self.sessions_per_level:
            raise ValueError(f"session id {sid!r} is not configured")
        return self.artifact_schedule[session - 1]


_TOP_LEVEL_FIELDS = frozenset(
    {
        "levels",
        "sessions_per_level",
        "providers",
        "artifact_schedule",
        "stages",
        "asset_discovery",
    }
)
_STAGE_FIELDS = frozenset({"digest", "digest_assets", "provenance", "receipts"})
_DISCOVERY_FIELDS = frozenset({"asset_ref_pattern", "asset_source_files"})


def _mapping(value: Any, field: str, source: Path) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CourseConfigError(f"{source}: {field} must be a mapping")
    return value


def _directory(value: Any, field: str, source: Path) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CourseConfigError(f"{source}: {field} must be a non-empty directory name")
    path = Path(value)
    if path.is_absolute() or len(path.parts) != 1 or value in {".", ".."}:
        raise CourseConfigError(f"{source}: {field} must be one relative directory name")
    return value


def _asset_discovery(raw: Any, source: Path) -> AssetDiscovery:
    data = _mapping(raw, "asset_discovery", source)
    unknown = set(data) - _DISCOVERY_FIELDS
    if unknown:
        raise CourseConfigError(
            f"{source}: unknown asset_discovery field(s): {', '.join(sorted(unknown))}"
        )
    missing = _DISCOVERY_FIELDS - set(data)
    if missing:
        names = ", ".join(f"asset_discovery.{name}" for name in sorted(missing))
        raise CourseConfigError(f"{source}: missing field(s): {names}")

    pattern = data["asset_ref_pattern"]
    if not isinstance(pattern, str) or not pattern.strip():
        raise CourseConfigError(
            f"{source}: asset_discovery.asset_ref_pattern must be a non-empty regex string"
        )
    try:
        ref = re.compile(pattern)
    except re.error as exc:
        raise CourseConfigError(
            f"{source}: asset_discovery.asset_ref_pattern is not a valid regex: {exc}"
        ) from exc
    # findall() returns tuples the moment a second group appears, and every
    # downstream comparison is filename-against-string. Refuse it here rather
    # than let it surface as a TypeError mid-audit.
    if ref.groups != 1:
        raise CourseConfigError(
            f"{source}: asset_discovery.asset_ref_pattern must have exactly one capture "
            f"group (the filename); this one has {ref.groups}"
        )

    files_raw = data["asset_source_files"]
    if (
        not isinstance(files_raw, list)
        or not files_raw
        or len(set(files_raw)) != len(files_raw)
    ):
        raise CourseConfigError(
            f"{source}: asset_discovery.asset_source_files must be a non-empty list "
            "of unique file names"
        )
    for name in files_raw:
        # A source file is read from inside the bundle. An absolute path or a
        # ".." escape would audit a different course and report PASS on this one.
        if not isinstance(name, str) or not name.strip():
            raise CourseConfigError(
                f"{source}: asset_discovery.asset_source_files entries must be non-empty names"
            )
        path = Path(name)
        if path.is_absolute() or len(path.parts) != 1 or name in {".", ".."}:
            raise CourseConfigError(
                f"{source}: asset_discovery.asset_source_files entry {name!r} must be one "
                "file name inside the bundle"
            )
    return AssetDiscovery(ref=ref, source_files=tuple(files_raw))


def load_course(root: Path) -> CourseConfig:
    """Load and validate ``root/course.yaml``.

    Only common artifact directories are controlled by ``stages``. Provider-lane
    and merge stages remain caller-named because pipelines own different stage sets.
    """
    source = Path(root) / "course.yaml"
    if not source.is_file():
        raise CourseConfigError(
            f"course config {source} does not exist; create course.yaml at the vault root"
        )
    try:
        raw = yaml.safe_load(source.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise CourseConfigError(f"{source}: invalid YAML: {exc}") from exc

    data = _mapping(raw, "document", source)
    unknown = set(data) - _TOP_LEVEL_FIELDS
    if unknown:
        raise CourseConfigError(f"{source}: unknown field(s): {', '.join(sorted(unknown))}")
    missing = _TOP_LEVEL_FIELDS - set(data)
    if missing:
        raise CourseConfigError(f"{source}: missing field(s): {', '.join(sorted(missing))}")

    levels_raw = data["levels"]
    if (
        not isinstance(levels_raw, list)
        or not levels_raw
        or any(isinstance(level, bool) or not isinstance(level, int) or level < 1 for level in levels_raw)
        or len(set(levels_raw)) != len(levels_raw)
    ):
        raise CourseConfigError(f"{source}: levels must be a non-empty list of unique positive integers")

    sessions = data["sessions_per_level"]
    if isinstance(sessions, bool) or not isinstance(sessions, int) or sessions < 1:
        raise CourseConfigError(f"{source}: sessions_per_level must be a positive integer")

    providers_raw = data["providers"]
    if (
        not isinstance(providers_raw, list)
        or not providers_raw
        or any(not isinstance(provider, str) or not provider.strip() for provider in providers_raw)
        or len(set(providers_raw)) != len(providers_raw)
    ):
        raise CourseConfigError(f"{source}: providers must be a non-empty list of unique names")

    schedule_raw = _mapping(data["artifact_schedule"], "artifact_schedule", source)
    expected_schedule_keys = {f"s{session}" for session in range(1, sessions + 1)}
    unknown_schedule = set(schedule_raw) - expected_schedule_keys
    if unknown_schedule:
        raise CourseConfigError(
            f"{source}: unknown artifact_schedule field(s): "
            f"{', '.join(sorted(unknown_schedule))}"
        )
    missing_schedule = expected_schedule_keys - set(schedule_raw)
    if missing_schedule:
        names = ", ".join(f"artifact_schedule.{name}" for name in sorted(missing_schedule))
        raise CourseConfigError(f"{source}: missing field(s): {names}")
    for key in sorted(expected_schedule_keys):
        if not isinstance(schedule_raw[key], bool):
            raise CourseConfigError(f"{source}: artifact_schedule.{key} must be a boolean")

    stages_raw = _mapping(data["stages"], "stages", source)
    unknown_stages = set(stages_raw) - _STAGE_FIELDS
    if unknown_stages:
        raise CourseConfigError(
            f"{source}: unknown stages field(s): {', '.join(sorted(unknown_stages))}"
        )
    missing_stages = _STAGE_FIELDS - set(stages_raw)
    if missing_stages:
        names = ", ".join(f"stages.{name}" for name in sorted(missing_stages))
        raise CourseConfigError(f"{source}: missing field(s): {names}")

    return CourseConfig(
        levels=tuple(levels_raw),
        sessions_per_level=sessions,
        providers=frozenset(providers_raw),
        artifact_schedule=tuple(
            schedule_raw[f"s{session}"] for session in range(1, sessions + 1)
        ),
        asset_discovery=_asset_discovery(data["asset_discovery"], source),
        stages=StageDirectories(
            digest=_directory(stages_raw["digest"], "stages.digest", source),
            digest_assets=_directory(stages_raw["digest_assets"], "stages.digest_assets", source),
            provenance=_directory(stages_raw["provenance"], "stages.provenance", source),
            receipts=_directory(stages_raw["receipts"], "stages.receipts", source),
        ),
    )
