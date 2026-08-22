"""Verify every asset a bundle references either exists or is declared to-be-created.

Codex found four dangling references in the L1-s1 deck: slides pointed at
`img-05.png` for four different jobs it cannot do, and at `img-20.png` for the
debugging bugs it does not contain, while the correct filenames sat unreferenced
in SOURCES.md. Nothing caught it, because the gates read text and never looked
at the filesystem.

Usage:  python scripts/swarm/check_assets.py 75-bundle/L1-s1

Asset discovery
---------------
Defaults are the micro:bit course: backticked filenames with an img/tata/
technosquare prefix, referenced from slides-source.md / home-summary.md.

Other courses run the same CLI without editing this file: main() resolves
discovery AT CALL TIME from the nearest course.yaml found walking up from the
bundle directory, reading its optional section

    asset_discovery:
      asset_ref_pattern: "`((?:shot|render)[A-Za-z0-9_.\\-]*\\.(?:png|svg))`"
      asset_source_files: [deck.md]

Either key alone is allowed; the other keeps its default. A found manifest that
has no asset_discovery section owns the config and yields the defaults; so does
"no manifest at all". A malformed section fails loudly rather than silently
auditing the wrong course.

Direct callers of audit()/unused() keep the historical override channel:
the module globals REF and SOURCE_FILES are read at call time, so assigning
``check_assets.REF = re.compile(...)`` changes subsequent results.

Decided policies
----------------
- Matching is case-sensitive: `IMG-01.PNG` on a slide is a dangling reference
  even when img-01.png exists.
- Bundle containment for source file names is NOT enforced here. Names come
  from the trusted course manifest and are joined to the bundle path as-is;
  "../outside.md" deliberately reads outside the bundle. Callers accepting
  untrusted manifests must validate containment themselves.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REF = re.compile(r"`((?:img|tata|technosquare)[A-Za-z0-9_.\-]*\.(?:png|gif|jpg|jpeg))`")
SOURCE_FILES = ("slides-source.md", "home-summary.md")

MANIFEST_NAME = "course.yaml"
_DISCOVERY_SECTION = "asset_discovery"
_REF_PATTERN_KEY = "asset_ref_pattern"
_SOURCE_FILES_KEY = "asset_source_files"


def _refs(
    bundle: Path,
    ref: re.Pattern[str],
    source_files: tuple[str, ...],
) -> set[str]:
    """Filenames referenced by the bundle's source files (containment: see docstring)."""
    refs: set[str] = set()
    for name in source_files:
        f = bundle / name
        if f.exists():
            refs |= set(ref.findall(f.read_text(encoding="utf-8")))
    return refs


def _audit(
    bundle: Path,
    ref: re.Pattern[str],
    source_files: tuple[str, ...],
) -> tuple[list[str], list[str], list[str]]:
    refs = _refs(bundle, ref, source_files)

    assets = bundle / "assets"
    have = {p.name for p in assets.iterdir()} if assets.is_dir() else set()

    manifest = bundle / "SOURCES.md"
    declared = manifest.read_text(encoding="utf-8") if manifest.exists() else ""

    ok, to_create, dangling = [], [], []
    for r in sorted(refs):
        if r in have:
            ok.append(r)
        elif r in declared:
            to_create.append(r)
        else:
            dangling.append(r)
    return ok, to_create, dangling


def _unused(
    bundle: Path,
    ref: re.Pattern[str],
    source_files: tuple[str, ...],
) -> list[str]:
    refs = _refs(bundle, ref, source_files)
    assets = bundle / "assets"
    if not assets.is_dir():
        return []
    return sorted(p.name for p in assets.iterdir() if p.name not in refs)


def audit(bundle: Path) -> tuple[list[str], list[str], list[str]]:
    """Return (ok, to_create, dangling) filenames referenced by the bundle."""
    return _audit(bundle, REF, SOURCE_FILES)


def unused(bundle: Path) -> list[str]:
    """Assets on disk that no source file references — dead weight in the upload."""
    return _unused(bundle, REF, SOURCE_FILES)


def _manifest_section(manifest: Path) -> dict:
    try:
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise ValueError(f"{manifest}: unreadable course manifest: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{manifest}: course manifest must be a mapping")
    section = data.get(_DISCOVERY_SECTION)
    if section is None:
        return {}
    if not isinstance(section, dict):
        raise ValueError(f"{manifest}: {_DISCOVERY_SECTION} must be a mapping")
    unknown = set(section) - {_REF_PATTERN_KEY, _SOURCE_FILES_KEY}
    if unknown:
        raise ValueError(
            f"{manifest}: unknown {_DISCOVERY_SECTION} key(s): {', '.join(sorted(unknown))}"
        )
    return section


def discovery_for(bundle: Path) -> tuple[re.Pattern[str], tuple[str, ...]]:
    """Resolve discovery settings at call time for ``bundle``.

    Walks up from the bundle directory to the nearest ``course.yaml``. The
    nearest manifest owns the config: a manifest without an asset_discovery
    section stops the search and yields today's micro:bit defaults.
    """
    current = Path(bundle).resolve()
    for candidate in (current, *current.parents):
        manifest = candidate / MANIFEST_NAME
        if not manifest.is_file():
            continue
        section = _manifest_section(manifest)

        ref = REF
        pattern = section.get(_REF_PATTERN_KEY)
        if pattern is not None:
            if not isinstance(pattern, str) or not pattern.strip():
                raise ValueError(
                    f"{manifest}: {_DISCOVERY_SECTION}.{_REF_PATTERN_KEY} "
                    "must be a non-empty regex string"
                )
            try:
                ref = re.compile(pattern)
            except re.error as exc:
                raise ValueError(f"{manifest}: invalid {_REF_PATTERN_KEY}: {exc}") from exc

        files = SOURCE_FILES
        sources = section.get(_SOURCE_FILES_KEY)
        if sources is not None:
            if (
                not isinstance(sources, list)
                or not sources
                or any(not isinstance(name, str) or not name.strip() for name in sources)
            ):
                raise ValueError(
                    f"{manifest}: {_DISCOVERY_SECTION}.{_SOURCE_FILES_KEY} "
                    "must be a non-empty list of source file names"
                )
            files = tuple(sources)
        return ref, files
    return REF, SOURCE_FILES


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    bundle = Path(argv[1])
    try:
        ref, source_files = discovery_for(bundle)
    except ValueError as exc:
        print(f"check_assets: {exc}", file=sys.stderr)
        return 2
    ok, to_create, dangling = _audit(bundle, ref, source_files)
    for r in ok:
        print(f"  OK         {r}")
    for r in to_create:
        print(f"  TO-CREATE  {r}")
    for r in dangling:
        print(f"  DANGLING   {r}")
    for r in _unused(bundle, ref, source_files):
        print(f"  UNUSED     {r}  (on disk, referenced by nothing)")

    if dangling:
        print(f"\nFAIL: {len(dangling)} dangling asset reference(s)")
        return 1
    print(f"\nPASS: {len(ok)} present, {len(to_create)} to create")
    return 0


def _demo() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as d:
        b = Path(d)
        (b / "assets").mkdir()
        (b / "assets" / "img-01.png").write_bytes(b"x")
        (b / "assets" / "img-99.png").write_bytes(b"x")  # never referenced
        (b / "slides-source.md").write_text(
            "- **Asset:** `img-01.png`\n"
            "- **Asset:** `img-02.png`\n"
            "- **Asset:** `img-03.png`\n",
            encoding="utf-8",
        )
        (b / "SOURCES.md").write_text("| `img-02.png` | to be created |", encoding="utf-8")
        ok, to_create, dangling = audit(b)
        assert ok == ["img-01.png"], ok
        assert to_create == ["img-02.png"], to_create
        assert dangling == ["img-03.png"], dangling
        assert unused(b) == ["img-99.png"], unused(b)
    print("check_assets.py self-check OK")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--self-check":
        _demo()
    else:
        sys.exit(main(sys.argv))
