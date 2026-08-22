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
class CourseConfig:
    levels: tuple[int, ...]
    sessions_per_level: int
    providers: frozenset[str]
    artifact_schedule: tuple[bool, ...]
    stages: StageDirectories

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
    {"levels", "sessions_per_level", "providers", "artifact_schedule", "stages"}
)
_STAGE_FIELDS = frozenset({"digest", "digest_assets", "provenance", "receipts"})


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
        stages=StageDirectories(
            digest=_directory(stages_raw["digest"], "stages.digest", source),
            digest_assets=_directory(stages_raw["digest_assets"], "stages.digest_assets", source),
            provenance=_directory(stages_raw["provenance"], "stages.provenance", source),
            receipts=_directory(stages_raw["receipts"], "stages.receipts", source),
        ),
    )
