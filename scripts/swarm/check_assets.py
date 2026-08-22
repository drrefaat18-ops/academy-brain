"""Verify every asset a bundle references either exists or is declared to-be-created.

Codex found four dangling references in the L1-s1 deck: slides pointed at
`img-05.png` for four different jobs it cannot do, and at `img-20.png` for the
debugging bugs it does not contain, while the correct filenames sat unreferenced
in SOURCES.md. Nothing caught it, because the gates read text and never looked
at the filesystem.

Usage:  python scripts/swarm/check_assets.py 75-bundle/L1-s1

Asset discovery
---------------
Discovery is NOT hardcoded and NOT defaulted. main() walks up from the bundle
directory to the nearest course.yaml and reads its required section

    asset_discovery:
      asset_ref_pattern: "`((?:shot|render)[A-Za-z0-9_.\-]*\.(?:png|svg))`"
      asset_source_files: [deck.md]

through the canonical loader in config.py, which owns the schema. There is no
second parser here: one file, one set of rules.

Everything fails closed. No manifest, no asset_discovery section, a malformed
pattern, or a configured source file that is not on disk are all errors with a
nonzero exit — never a fallback to another course's naming. A silent fallback
reports "PASS: 0 present" on a course whose every asset is missing, which is
the exact defect this gate exists to catch and the reason the first two
iterations of it were rejected.

Direct callers of audit()/unused() keep the historical override channel: the
module globals REF and SOURCE_FILES are read at call time, so assigning
``check_assets.REF = re.compile(...)`` changes subsequent results. These remain
the micro:bit defaults and are used by no CLI path.

Decided policies
----------------
- Matching is case-sensitive: `IMG-01.PNG` on a slide is a dangling reference
  even when img-01.png exists.
- Source file names are validated by config.py as single names inside the
  bundle: absolute paths and "../outside.md" are refused at load time, so this
  gate can never be pointed at another course's files.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from swarm import config  # noqa: E402

class DiscoveryError(ValueError):
    """Discovery could not be resolved. Never defaulted around."""



class DiscoveryError(ValueError):
    """Discovery could not be resolved. Never defaulted around."""


REF = re.compile(r"`((?:img|tata|technosquare)[A-Za-z0-9_.\-]*\.(?:png|gif|jpg|jpeg))`")
SOURCE_FILES = ("slides-source.md", "home-summary.md")

MANIFEST_NAME = "course.yaml"


def _refs(
    bundle: Path,
    ref: re.Pattern[str],
    source_files: tuple[str, ...],
) -> set[str]:
    """Filenames referenced by the bundle's source files (containment: see docstring)."""
    refs: set[str] = set()
    missing = []
    for name in source_files:
        f = bundle / name
        if not f.is_file():
            # A typo'd source file used to be skipped, turning the whole audit
            # into an empty pass. Absence is a configuration error, not a hint.
            missing.append(name)
            continue
        refs |= set(ref.findall(f.read_text(encoding="utf-8")))
    if missing:
        raise DiscoveryError(
            f"{bundle}: configured source file(s) not found: {', '.join(sorted(missing))}"
        )
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


def discovery_for(bundle: Path) -> tuple[re.Pattern[str], tuple[str, ...]]:
    """Resolve discovery at call time from the nearest course.yaml above ``bundle``.

    Fails closed. There is no default and no fallback: auditing a course with
    another course's naming finds nothing and reports success.
    """
    current = Path(bundle).resolve()
    for candidate in (current, *current.parents):
        if (candidate / MANIFEST_NAME).is_file():
            course = config.load_course(candidate)
            return course.asset_discovery.ref, course.asset_discovery.source_files
    raise DiscoveryError(
        f"no {MANIFEST_NAME} found at or above {current}. Asset discovery is "
        "course-specific and has no default; create the manifest rather than "
        "auditing this bundle with another course's naming."
    )


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    bundle = Path(argv[1])
    try:
        ref, source_files = discovery_for(bundle)
    except (DiscoveryError, config.CourseConfigError) as exc:
        print(f"check_assets: {exc}", file=sys.stderr)
        return 2
    try:
        ok, to_create, dangling = _audit(bundle, ref, source_files)
        unused_now = _unused(bundle, ref, source_files)
    except DiscoveryError as exc:
        print(f"check_assets: {exc}", file=sys.stderr)
        return 2
    for r in ok:
        print(f"  OK         {r}")
    for r in to_create:
        print(f"  TO-CREATE  {r}")
    for r in dangling:
        print(f"  DANGLING   {r}")
    for r in unused_now:
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
        # every declared source file must exist — absence is a config error,
        # not a reason to audit less
        (b / "home-summary.md").touch()
        (b / "SOURCES.md").write_text("| `img-02.png` | to be created |", encoding="utf-8")
        ok, to_create, dangling = audit(b)
        assert ok == ["img-01.png"], ok
        assert to_create == ["img-02.png"], to_create
        assert dangling == ["img-03.png"], dangling
        assert unused(b) == ["img-99.png"], unused(b)

        # a declared source file that is not on disk must fail closed, not
        # quietly shrink the audit to an empty pass
        (b / "home-summary.md").unlink()
        try:
            audit(b)
        except DiscoveryError as exc:
            assert "home-summary.md" in str(exc), exc
        else:  # pragma: no cover
            raise AssertionError("a missing source file was silently skipped")

    # discovery itself has no default: no manifest is an error, never micro:bit
    with tempfile.TemporaryDirectory() as d:
        try:
            discovery_for(Path(d))
        except DiscoveryError as exc:
            assert "no course.yaml found" in str(exc), exc
        else:  # pragma: no cover
            raise AssertionError("discovery fell back to a default")

    print("check_assets.py self-check OK")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--self-check":
        _demo()
    else:
        sys.exit(main(sys.argv))
