"""Tests for check_assets.py asset discovery, incl. non-micro:bit courses.

The cross-course coverage runs through main(argv) — the real CLI entry point —
because a generalisation the entry point cannot reach is not a generalisation.
"""

import re

from swarm import check_assets

EV3_REF = re.compile(r"`((?:shot|render)[A-Za-z0-9_.\-]*\.(?:png|svg))`")

# A differently-named course manifest: different asset prefixes, different
# source filenames. Written raw so the regex backslashes survive verbatim.
EV3_MANIFEST = r"""
asset_discovery:
  asset_ref_pattern: '`((?:shot|render)[A-Za-z0-9_.\-]*\.(?:png|svg))`'
  asset_source_files: [deck.md]
"""


def _microbit_bundle(tmp_path):
    b = tmp_path / "mb"
    (b / "assets").mkdir(parents=True)
    for name in ("img-01.png", "tata-01.gif", "img-99.png"):
        (b / "assets" / name).write_bytes(b"x")
    (b / "slides-source.md").write_text(
        "- **Asset:** `img-01.png`\n"
        "- **Asset:** `img-02.png`\n"
        "- **Asset:** `technosquare-logo.jpg`\n",
        encoding="utf-8",
    )
    (b / "home-summary.md").write_text("- **Asset:** `tata-01.gif`\n", encoding="utf-8")
    (b / "SOURCES.md").write_text("| `img-02.png` | to be created |", encoding="utf-8")
    return b


def _bare_bundle(tmp_path):
    """Assets dir + one source file the test fills in itself."""
    b = tmp_path / "bare"
    (b / "assets").mkdir(parents=True)
    (b / "slides-source.md").touch()
    return b


def _ev3_course(tmp_path):
    """A differently-named course: its own manifest declares its discovery."""
    root = tmp_path / "ev3-course"
    b = root / "bundles" / "e1-s1"
    (b / "assets").mkdir(parents=True)
    (b / "assets" / "shot-arm.png").write_bytes(b"x")
    (b / "assets" / "render-arm.svg").write_bytes(b"x")
    (b / "assets" / "img-orphan.png").write_bytes(b"x")  # matches no pattern: UNUSED
    (b / "deck.md").write_text(
        "`shot-arm.png` and `render-arm.svg`, plus missing `shot-gyro.png`\n",
        encoding="utf-8",
    )
    # micro:bit-style reference in a file that is NOT an EV3 source: ignored.
    (b / "slides-source.md").write_text("- **Asset:** `img-01.png`\n", encoding="utf-8")
    (root / "course.yaml").write_text(EV3_MANIFEST.lstrip(), encoding="utf-8")
    return b


def test_microbit_shape_default_params(tmp_path):
    """One-arg audit on a micro:bit-shaped bundle behaves exactly as today."""
    b = _microbit_bundle(tmp_path)
    ok, to_create, dangling = check_assets.audit(b)
    assert ok == ["img-01.png", "tata-01.gif"]
    assert to_create == ["img-02.png"]
    assert dangling == ["technosquare-logo.jpg"]
    assert check_assets.unused(b) == ["img-99.png"]


def test_main_cli_finds_differently_named_course(tmp_path, capsys):
    """main() generalises via the course manifest — this test would have caught C0-03.

    Under micro:bit defaults this bundle yields zero references and a green PASS;
    the manifest-declared deck.md/shot-* discovery must flip it to a real FAIL.
    """
    b = _ev3_course(tmp_path)
    rc = check_assets.main(["check_assets.py", str(b)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "  OK         shot-arm.png\n" in out
    assert "  OK         render-arm.svg\n" in out
    assert "  DANGLING   shot-gyro.png\n" in out
    assert "\nFAIL: 1 dangling asset reference(s)" in out
    assert "  TO-CREATE  " not in out
    assert "img-01.png" not in out  # slides-source.md is not an EV3 source file
    assert "UNUSED     img-orphan.png" in out


def test_main_cli_manifest_without_discovery_keeps_defaults(tmp_path, capsys):
    """A course.yaml without an asset_discovery section changes nothing."""
    b = _microbit_bundle(tmp_path)
    (b.parent / "course.yaml").write_text("levels: [1]\n", encoding="utf-8")
    rc = check_assets.main(["check_assets.py", str(b)])
    out = capsys.readouterr().out
    assert rc == 1  # technosquare-logo.jpg is referenced, undeclared, missing
    assert "  TO-CREATE  img-02.png\n" in out
    assert "  OK         img-01.png\n" in out
    assert "\nFAIL: 1 dangling asset reference(s)" in out


def test_call_time_pattern_override_changes_results(tmp_path, monkeypatch):
    """Module-global REF overrides resolve at call time (C0-02 regression guard).

    Definition-time binding froze the default into the signature and made this
    override silently dead; it must keep steering the one-argument API.
    """
    b = tmp_path / "shot-bundle"
    (b / "assets").mkdir(parents=True)
    (b / "assets" / "shot-arm.png").write_bytes(b"x")
    (b / "slides-source.md").write_text("`shot-arm.png`\n", encoding="utf-8")

    assert check_assets.audit(b) == ([], [], [])  # default pattern never sees shot-*

    monkeypatch.setattr(check_assets, "REF", EV3_REF)
    assert check_assets.audit(b) == (["shot-arm.png"], [], [])


def test_call_time_source_files_override_changes_results(tmp_path, monkeypatch):
    """SOURCE_FILES overrides resolve at call time too."""
    b = tmp_path / "deck-bundle"
    (b / "assets").mkdir(parents=True)
    (b / "assets" / "img-x.png").write_bytes(b"x")
    (b / "deck.md").write_text("`img-x.png`\n", encoding="utf-8")

    assert check_assets.audit(b) == ([], [], [])  # default sources never read deck.md

    monkeypatch.setattr(check_assets, "SOURCE_FILES", ("deck.md",))
    assert check_assets.audit(b) == (["img-x.png"], [], [])


def test_partial_discovery_section_mixes_with_defaults(tmp_path, capsys):
    """Only asset_source_files declared -> ref pattern falls back to the default."""
    root = tmp_path / "partial-course"
    b = root / "b1"
    (b / "assets").mkdir(parents=True)
    (b / "assets" / "img-07.png").write_bytes(b"x")
    (b / "deck.md").write_text("`img-07.png` and missing `img-08.png`\n", encoding="utf-8")
    (root / "course.yaml").write_text(
        "asset_discovery:\n  asset_source_files: [deck.md]\n", encoding="utf-8"
    )

    rc = check_assets.main(["check_assets.py", str(b)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "  OK         img-07.png\n" in out
    assert "  DANGLING   img-08.png\n" in out


def test_empty_bundle_reports_clean_pass(tmp_path, capsys):
    b = tmp_path / "empty"
    (b / "assets").mkdir(parents=True)
    assert check_assets.audit(b) == ([], [], [])
    assert check_assets.unused(b) == []
    rc = check_assets.main(["check_assets.py", str(b)])
    out = capsys.readouterr().out
    assert rc == 0
    assert "\nPASS: 0 present, 0 to create" in out


def test_missing_assets_dir_is_dangling_not_crash(tmp_path):
    b = tmp_path / "no-assets"
    b.mkdir(parents=True)
    (b / "slides-source.md").write_text("`img-lost.png`\n", encoding="utf-8")
    ok, to_create, dangling = check_assets.audit(b)
    assert ok == []
    assert to_create == []
    assert dangling == ["img-lost.png"]
    assert check_assets.unused(b) == []


def test_missing_source_files_are_skipped_silently(tmp_path):
    b = tmp_path / "only-home"
    (b / "assets").mkdir(parents=True)
    (b / "assets" / "tata-01.gif").write_bytes(b"x")
    (b / "home-summary.md").write_text("- **Asset:** `tata-01.gif`\n", encoding="utf-8")
    ok, to_create, dangling = check_assets.audit(b)
    assert ok == ["tata-01.gif"]
    assert dangling == []


def test_matching_is_case_sensitive(tmp_path):
    """Documented policy: exact case, at both layers.

    A recognised reference (`img-Camera.png`) matches no on-disk file whose name
    differs in case; and a fully uppercased name (IMG-UPPER.png) is not even
    recognised, because the known prefixes are lowercase.
    """
    b = tmp_path / "case"
    (b / "assets").mkdir(parents=True)
    (b / "assets" / "img-camera.png").write_bytes(b"x")
    (b / "slides-source.md").write_text("`img-Camera.png`\n`IMG-UPPER.png`\n", encoding="utf-8")
    ok, to_create, dangling = check_assets.audit(b)
    assert ok == []
    assert dangling == ["img-Camera.png"]
    assert check_assets.unused(b) == ["img-camera.png"]


def test_only_backticked_asset_shaped_spans_are_references(tmp_path):
    b = _bare_bundle(tmp_path)
    (b / "slides-source.md").write_text(
        "`img-real.png`\n"
        "plain text mention of img-naked.png without backticks\n"
        "`foo-unrelated.png` wrong prefix\n"
        "see docs at https://example.com/img-url.png\n",
        encoding="utf-8",
    )
    ok, to_create, dangling = check_assets.audit(b)
    assert ok == []
    assert to_create == []
    assert dangling == ["img-real.png"]
    for ignored in ("img-naked.png", "foo-unrelated.png", "img-url.png"):
        assert ignored not in dangling


def test_source_file_may_escape_bundle_by_design(tmp_path, monkeypatch):
    """Documented policy: containment is NOT enforced here.

    Source names come from the trusted course manifest and are joined to the
    bundle path as-is; ../outside.md deliberately reads outside the bundle.
    Callers auditing untrusted manifests must validate containment themselves.
    """
    outside = tmp_path / "outside.md"
    outside.write_text("`img-shared.png`\n", encoding="utf-8")
    b = tmp_path / "b"
    (b / "assets").mkdir(parents=True)

    monkeypatch.setattr(check_assets, "SOURCE_FILES", ("../outside.md",))
    ok, to_create, dangling = check_assets.audit(b)
    assert ok == []
    assert dangling == ["img-shared.png"]


def test_manifest_rejects_unknown_discovery_keys(tmp_path, capsys):
    """A typo'd discovery key must fail loudly, not silently audit the wrong course."""
    root = tmp_path / "typo-course"
    b = root / "b1"
    b.mkdir(parents=True)
    (root / "course.yaml").write_text(
        "asset_discovery:\n  asset_ref_patterns: ['oops']\n", encoding="utf-8"
    )
    rc = check_assets.main(["check_assets.py", str(b)])
    err = capsys.readouterr().err
    assert rc == 2
    assert "unknown asset_discovery key(s): asset_ref_patterns" in err


def test_manifest_rejects_uncompilable_ref_pattern(tmp_path, capsys):
    root = tmp_path / "bad-regex-course"
    b = root / "b1"
    b.mkdir(parents=True)
    (root / "course.yaml").write_text(
        "asset_discovery:\n  asset_ref_pattern: '`([unclosed'\n", encoding="utf-8"
    )
    rc = check_assets.main(["check_assets.py", str(b)])
    err = capsys.readouterr().err
    assert rc == 2
    assert "invalid asset_ref_pattern" in err


def test_manifest_rejects_non_mapping_discovery_section(tmp_path, capsys):
    root = tmp_path / "flat-course"
    b = root / "b1"
    b.mkdir(parents=True)
    (root / "course.yaml").write_text("asset_discovery: [not, a, mapping]\n", encoding="utf-8")
    rc = check_assets.main(["check_assets.py", str(b)])
    err = capsys.readouterr().err
    assert rc == 2
    assert "asset_discovery must be a mapping" in err


def test_manifest_rejects_unparseable_yaml(tmp_path, capsys):
    root = tmp_path / "broken-course"
    b = root / "b1"
    b.mkdir(parents=True)
    (root / "course.yaml").write_text("asset_discovery: {unclosed\n", encoding="utf-8")
    rc = check_assets.main(["check_assets.py", str(b)])
    err = capsys.readouterr().err
    assert rc == 2
    assert "unreadable course manifest" in err


def test_dangling_reference(tmp_path):
    b = _bare_bundle(tmp_path)
    (b / "slides-source.md").write_text("`img-nope.png`\n", encoding="utf-8")
    ok, to_create, dangling = check_assets.audit(b)
    assert ok == []
    assert to_create == []
    assert dangling == ["img-nope.png"]


def test_to_create_reference_declared_in_sources_md(tmp_path):
    b = _bare_bundle(tmp_path)
    (b / "slides-source.md").write_text("`img-later.png`\n", encoding="utf-8")
    (b / "SOURCES.md").write_text("| `img-later.png` | planned |", encoding="utf-8")
    ok, to_create, dangling = check_assets.audit(b)
    assert ok == []
    assert to_create == ["img-later.png"]
    assert dangling == []


def test_unused_asset_on_disk(tmp_path):
    b = _microbit_bundle(tmp_path)
    (b / "assets" / "orphan.png").write_bytes(b"x")
    (b / "assets" / "stray.txt").write_bytes(b"x")
    assert check_assets.unused(b) == ["img-99.png", "orphan.png", "stray.txt"]
