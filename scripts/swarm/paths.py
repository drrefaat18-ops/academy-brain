"""Config-bound path derivation for the swarm vault."""

from __future__ import annotations

import re
from pathlib import Path

from .config import CourseConfig, load_course


class CoursePaths:
    """Path API bound to one vault root and its course manifest."""

    def __init__(self, root: Path, course: CourseConfig) -> None:
        self.VAULT_ROOT = Path(root)
        self.COURSE = course
        self.LEVELS = course.levels
        self.SESSION_NUMBERS = tuple(range(1, course.sessions_per_level + 1))
        self.SESSION_IDS = tuple(
            f"L{level}-s{session}"
            for level in self.LEVELS
            for session in self.SESSION_NUMBERS
        )
        self.PROVIDERS = course.providers
        self._session_re = re.compile(
            rf"^(?:{'|'.join(re.escape(sid) for sid in self.SESSION_IDS)})$"
        )

    def validate_session_id(self, sid: str) -> str:
        """Return sid unchanged, or raise ValueError if it is not configured."""
        if not isinstance(sid, str) or not self._session_re.fullmatch(sid):
            raise ValueError(f"invalid session id {sid!r}; expected one of {self.SESSION_IDS}")
        return sid

    def produces_artifacts(self, sid: str) -> bool:
        return self.COURSE.produces_artifacts(self.validate_session_id(sid))

    def _artifact_session_id(self, sid: str) -> str:
        sid = self.validate_session_id(sid)
        if not self.COURSE.produces_artifacts(sid):
            raise ValueError(f"session {sid!r} does not produce artifacts")
        return sid

    def digest_path(self, sid: str) -> Path:
        return self.VAULT_ROOT / self.COURSE.stages.digest / f"{self._artifact_session_id(sid)}.md"

    def assets_dir(self, sid: str) -> Path:
        return (
            self.VAULT_ROOT
            / self.COURSE.stages.digest
            / self.COURSE.stages.digest_assets
            / self._artifact_session_id(sid)
        )

    def provenance_path(self, sid: str) -> Path:
        return self.VAULT_ROOT / self.COURSE.stages.provenance / f"{self._artifact_session_id(sid)}.md"

    def lane_path(self, stage: str, sid: str, provider: str) -> Path:
        """Per-provider lane file; stage names are deliberately pipeline-owned."""
        if provider not in self.PROVIDERS:
            raise ValueError(f"unknown provider {provider!r}; expected one of {sorted(self.PROVIDERS)}")
        return self.VAULT_ROOT / stage / self._artifact_session_id(sid) / f"{provider}.json"

    def merged_path(self, stage: str, sid: str) -> Path:
        """Single-owner output; stage names are deliberately pipeline-owned."""
        return self.VAULT_ROOT / stage / f"{self._artifact_session_id(sid)}.md"

    def receipt_path(self, sid: str, gate: str) -> Path:
        return self.VAULT_ROOT / self.COURSE.stages.receipts / f"{self.validate_session_id(sid)}.{gate}.yaml"


def for_root(root: Path) -> CoursePaths:
    """Load ``root/course.yaml`` and return a path API bound to that root."""
    root = Path(root)
    return CoursePaths(root, load_course(root))


VAULT_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT = for_root(VAULT_ROOT)
COURSE = _DEFAULT.COURSE
LEVELS = _DEFAULT.LEVELS
SESSION_NUMBERS = _DEFAULT.SESSION_NUMBERS
SESSION_IDS = _DEFAULT.SESSION_IDS
PROVIDERS = _DEFAULT.PROVIDERS
_SESSION_RE = _DEFAULT._session_re


def validate_session_id(sid: str) -> str:
    return _DEFAULT.validate_session_id(sid)


def produces_artifacts(sid: str) -> bool:
    return _DEFAULT.produces_artifacts(sid)


def digest_path(sid: str) -> Path:
    return _DEFAULT.digest_path(sid)


def assets_dir(sid: str) -> Path:
    return _DEFAULT.assets_dir(sid)


def provenance_path(sid: str) -> Path:
    return _DEFAULT.provenance_path(sid)


def lane_path(stage: str, sid: str, provider: str) -> Path:
    return _DEFAULT.lane_path(stage, sid, provider)


def merged_path(stage: str, sid: str) -> Path:
    return _DEFAULT.merged_path(stage, sid)


def receipt_path(sid: str, gate: str) -> Path:
    return _DEFAULT.receipt_path(sid, gate)
