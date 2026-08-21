"""Path derivation for the swarm vault.

Every path is computed from a session ID. Agents never search for their
inputs, which is what keeps read scope declared rather than discovered.
"""

from __future__ import annotations

import re
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]

SESSION_IDS: tuple[str, ...] = tuple(
    f"L{level}-s{n}" for level in (1, 2) for n in range(1, 8)
)

PROVIDERS: frozenset[str] = frozenset({"claude", "codex", "opencode", "hermes"})

_SESSION_RE = re.compile(r"^L[12]-s[1-7]$")


def validate_session_id(sid: str) -> str:
    """Return sid unchanged, or raise ValueError if it is not one of the 14."""
    if not _SESSION_RE.match(sid):
        raise ValueError(
            f"invalid session id {sid!r}; expected one of {SESSION_IDS}"
        )
    return sid


def digest_path(sid: str) -> Path:
    return VAULT_ROOT / "10-digest" / f"{validate_session_id(sid)}.md"


def assets_dir(sid: str) -> Path:
    return VAULT_ROOT / "10-digest" / "_assets" / validate_session_id(sid)


def provenance_path(sid: str) -> Path:
    return VAULT_ROOT / "20-provenance" / f"{validate_session_id(sid)}.md"


def lane_path(stage: str, sid: str, provider: str) -> Path:
    """Per-provider lane file. Distinct providers never share a path."""
    if provider not in PROVIDERS:
        raise ValueError(f"unknown provider {provider!r}; expected one of {sorted(PROVIDERS)}")
    return VAULT_ROOT / stage / validate_session_id(sid) / f"{provider}.json"


def merged_path(stage: str, sid: str) -> Path:
    """Single-owner output for a stage that merges lanes."""
    return VAULT_ROOT / stage / f"{validate_session_id(sid)}.md"


def receipt_path(sid: str, gate: str) -> Path:
    return VAULT_ROOT / "90-receipts" / f"{validate_session_id(sid)}.{gate}.yaml"
