"""Verify every asset a bundle references either exists or is declared to-be-created.

Codex found four dangling references in the L1-s1 deck: slides pointed at
`img-05.png` for four different jobs it cannot do, and at `img-20.png` for the
debugging bugs it does not contain, while the correct filenames sat unreferenced
in SOURCES.md. Nothing caught it, because the gates read text and never looked
at the filesystem.

Usage:  python scripts/swarm/check_assets.py 75-bundle/L1-s1
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REF = re.compile(r"`((?:img|tata|technosquare)[A-Za-z0-9_.\-]*\.(?:png|gif|jpg|jpeg))`")
SOURCE_FILES = ("slides-source.md", "home-summary.md")


def audit(bundle: Path) -> tuple[list[str], list[str], list[str]]:
    """Return (ok, to_create, dangling) filenames referenced by the bundle."""
    refs: set[str] = set()
    for name in SOURCE_FILES:
        f = bundle / name
        if f.exists():
            refs |= set(REF.findall(f.read_text(encoding="utf-8")))

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


def unused(bundle: Path) -> list[str]:
    """Assets on disk that no source file references — dead weight in the upload."""
    refs: set[str] = set()
    for name in SOURCE_FILES:
        f = bundle / name
        if f.exists():
            refs |= set(REF.findall(f.read_text(encoding="utf-8")))
    assets = bundle / "assets"
    if not assets.is_dir():
        return []
    return sorted(p.name for p in assets.iterdir() if p.name not in refs)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    bundle = Path(argv[1])
    ok, to_create, dangling = audit(bundle)
    for r in ok:
        print(f"  OK         {r}")
    for r in to_create:
        print(f"  TO-CREATE  {r}")
    for r in dangling:
        print(f"  DANGLING   {r}")
    for r in unused(bundle):
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
