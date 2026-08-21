"""NotebookLM session executor — the eleven steps, as one command.

Restores the original EthOS operating shape: the operator supplies a target,
the vault supplies the procedure and the state. Recovered from
`Dr mahmoud AI course/.claude/skills/ethos/SKILL.md:192-232` and recorded in
`30-research/_lanes/ethos-generation-method/`.

Two things this deliberately does NOT do:

* It does not go through the notebooklm MCP wrapper. The MCP exposes no file
  upload, which is what stopped the first L1-s1 run. The library underneath it
  has `sources.add_file`, and image sources work. The MCP was the wrong surface,
  never a missing capability.
* It does not upload EVIDENCE-class assets. NotebookLM redraws image sources,
  and a redrawn screenshot of MakeCode code is plausible, wrong, and hard to
  spot. Evidence is reserved as a blank region and overlaid after export.

Run under the notebooklm venv for a real run:

    C:/Users/ET/mcp-servers/notebooklm-mcp/.venv/Scripts/python.exe
        scripts/swarm/generate_session.py L1-s1 --live

Dry run is the default and needs no venv, no network, and no quota.
"""

from __future__ import annotations

import argparse
import asyncio
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from swarm import paths  # noqa: E402

VAULT = paths.VAULT_ROOT
BRAND = VAULT / "Techno Square identity"

# ponytail: the brand rule files live outside the vault, in Abdeen's originals.
# Copying them in would fork the doctrine; upload them from where they are.
BRAIN_OS = Path(
    r"D:\vault\GPT_Behavior_Deconstruction_Vault\00_RAW_SOURCES"
    r"\Abdeen_Moon_OS_Docs\Academy_Brain_OS"
)
BRANDING_RULE = BRAIN_OS / "Techno_Square_Branding_Rule.md"
TATA_GUIDE = BRAIN_OS / "Tata_Mascot_Usage Guide.md"

READY = 2  # SourceStatus.READY — generating against a processing source degrades silently


class HardStop(RuntimeError):
    """A gate refused. Never retried, never worked around."""


# --------------------------------------------------------------------------
# plan
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Upload:
    path: Path
    title: str

    def resolves(self) -> bool:
        return self.path.is_file()


@dataclass
class Asset:
    aid: str
    slide: str
    path: Path
    klass: str  # REFERENCE | EVIDENCE
    status: str

    @property
    def produced(self) -> bool:
        return self.status.strip().lower() == "produced and mapped"


@dataclass
class Pass:
    key: str  # deck-a | deck-b | summary
    notebook: str  # notebook title
    instructions: str
    uploads: list[Upload] = field(default_factory=list)
    evidence: list[Asset] = field(default_factory=list)


# --------------------------------------------------------------------------
# ASSET-MAPPING.md — the hard-stop gate, owned by codex
# --------------------------------------------------------------------------

_COLS = {
    "aid": ("id", "asset"),
    # "lands on" is what ASSET-MAPPING.md actually calls this column.
    "slide": ("slide", "lands", "destination"),
    "path": ("path", "file"),
    "klass": ("class",),
    "status": ("status", "production"),
}


def _header_index(cells: list[str]) -> dict[str, int] | None:
    """Map our field names onto whatever the table actually called its columns."""
    lowered = [c.strip().lower() for c in cells]
    idx: dict[str, int] = {}
    for field_name, needles in _COLS.items():
        for i, cell in enumerate(lowered):
            if any(n in cell for n in needles) and i not in idx.values():
                idx[field_name] = i
                break
    return idx if len(idx) == len(_COLS) else None


def _row_cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_asset_mapping(text: str) -> list[Asset]:
    """Pull every asset row out of the mapping's markdown tables.

    Column order is not assumed — headers are matched by name, because the file
    is authored by another agent and its exact shape is not ours to dictate.
    """
    assets: list[Asset] = []
    idx: dict[str, int] | None = None
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            idx = None
            continue
        cells = _row_cells(line)
        if set("".join(cells)) <= set("-: "):  # separator row
            continue
        if idx is None:
            idx = _header_index(cells)
            continue
        if len(cells) <= max(idx.values()):
            continue
        raw = cells[idx["path"]].strip("`").strip()
        raw = re.sub(r"^\[|\]\(.*\)$", "", raw)  # unwrap a markdown link
        if not raw or raw in {"-", "\u2014"}:
            continue
        p = Path(raw)
        assets.append(
            Asset(
                aid=cells[idx["aid"]].strip("`"),
                slide=cells[idx["slide"]],
                path=p if p.is_absolute() else VAULT / p,
                klass=cells[idx["klass"]].strip("*` ").upper(),
                status=cells[idx["status"]],
            )
        )
    return assets


def enforce_blueprint_gate(path: Path) -> None:
    """DEC-027: the owner approves the content before any quota is spent.

    This is the gate that made 'start s1' feel effortless in the original EthOS —
    not the shortness of the command, but that every content decision was already
    settled before it was typed.
    """
    if not path.is_file():
        raise HardStop(f"no blueprint at {path} — the owner has approved nothing yet")
    text = path.read_text(encoding="utf-8")
    status = re.search(r"^status:\s*(.+)$", text, re.M)
    state = status.group(1).strip().strip("\"'") if status else "(no status field)"
    if "approved" not in state.lower() or "awaiting" in state.lower():
        raise HardStop(f"blueprint status is {state!r} — the owner has not approved it")
    open_gaps = text.count("GAP - owner must decide")
    if open_gaps:
        raise HardStop(f"blueprint still has {open_gaps} unresolved 'GAP - owner must decide'")


def enforce_asset_gate(assets: list[Asset]) -> None:
    """DEC-030's hard stop: every row produced, every path on disk."""
    if not assets:
        raise HardStop("ASSET-MAPPING.md parsed to zero asset rows — refusing to guess")
    unproduced = [a for a in assets if not a.produced]
    dangling = [a for a in assets if a.produced and not a.path.is_file()]
    unclassed = [a for a in assets if a.klass not in {"REFERENCE", "EVIDENCE"}]
    problems = []
    if unproduced:
        problems.append(
            "not yet produced: " + ", ".join(f"{a.aid} [{a.status}]" for a in unproduced)
        )
    if dangling:
        problems.append("mapped but missing on disk: " + ", ".join(a.aid for a in dangling))
    if unclassed:
        problems.append(
            "unclassified (must be REFERENCE or EVIDENCE): "
            + ", ".join(f"{a.aid}={a.klass!r}" for a in unclassed)
        )
    if problems:
        raise HardStop("asset gate failed — " + "; ".join(problems))


# --------------------------------------------------------------------------
# instructions — lifted from the prompt file, never re-derived per run
# --------------------------------------------------------------------------

_SECTION = re.compile(r"^## (?P<head>.+?)\n(?P<body>.*?)(?=^## |\Z)", re.S | re.M)
_FIRST_FENCE = re.compile(r"```\n(?P<body>.*?)\n```", re.S)


def parse_prompts(text: str) -> dict[str, str]:
    """Return {deck-a, deck-b, summary} from 80-generation's prompt file.

    A heading's own body ends at the next '## ' heading, never mid-fence —
    otherwise a fence-less section (like "After generation") lets a naive
    fence search skip past it and steal the next heading's block.
    """
    out: dict[str, str] = {}
    for sec in _SECTION.finditer(text):
        head = sec.group("head").lower()
        fence = _FIRST_FENCE.search(sec.group("body"))
        if not fence:
            continue
        if "pass b" in head:
            key = "deck-b"
        elif "notebook b" in head:
            key = "summary"
        elif "notebook a" in head:
            key = "deck-a"
        else:
            continue
        out.setdefault(key, fence.group("body").strip())
    return out


def evidence_clause(evidence: list[Asset]) -> str:
    """The clause that stops NotebookLM inventing a screenshot.

    Not in the prompt file — it comes from the two-asset-class rule
    (`ethos/SKILL.md:371-415`), which the first run predated.
    """
    if not evidence:
        return ""
    rows = "\n".join(f"- slide {a.slide}: {a.aid}" for a in evidence)
    return (
        "\n\nReserved image regions. These slides carry a real screenshot that is "
        "inserted after export:\n"
        f"{rows}\n"
        "On each of those slides, leave a single clean empty image area and put "
        "nothing in it. Do NOT draw, recreate, paraphrase, illustrate or imagine "
        "the code or the device. An invented screenshot is worse than an empty "
        "box, because it looks right and teaches something false."
    )


# --------------------------------------------------------------------------
# building the plan
# --------------------------------------------------------------------------


def _is_brand(p: Path) -> bool:
    name = p.name.lower()
    return "logo" in name or "tata" in name or BRAND in p.parents


def build_plan(sid: str, assets: list[Asset], prompts: dict[str, str]) -> list[Pass]:
    bundle = VAULT / "75-bundle" / sid
    missing = [k for k in ("deck-a", "deck-b", "summary") if k not in prompts]
    if missing:
        raise HardStop(f"prompt file has no block for: {', '.join(missing)}")

    reference = [a for a in assets if a.klass == "REFERENCE"]
    evidence = [a for a in assets if a.klass == "EVIDENCE"]

    deck_title = f"TechnoSquare microbit {sid} — student deck"
    common = [
        Upload(bundle / "slides-source.md", "slides-source.md"),
        Upload(bundle / "trainer-guide.md", "trainer-guide.md"),
        Upload(bundle / "decisions.md", "decisions.md"),
        Upload(BRANDING_RULE, "Techno_Square_Branding_Rule.md"),
        Upload(TATA_GUIDE, "Tata_Mascot_Usage_Guide.md"),
    ] + [Upload(a.path, a.path.name) for a in reference]

    # Bound by what the mapping says lands on a summary slide — not by whether the
    # filename looks like branding. img-05 is a summary reference and is not brand.
    summary_refs = [
        a for a in reference if "summary" in a.slide.lower() or _is_brand(a.path)
    ]
    summary = [
        Upload(bundle / "home-summary.md", "home-summary.md"),
        Upload(BRANDING_RULE, "Techno_Square_Branding_Rule.md"),
        Upload(TATA_GUIDE, "Tata_Mascot_Usage_Guide.md"),
    ] + [Upload(a.path, a.path.name) for a in summary_refs]

    return [
        Pass("deck-a", deck_title, prompts["deck-a"] + evidence_clause(evidence), common, evidence),
        Pass("deck-b", deck_title, prompts["deck-b"] + evidence_clause(evidence), common, evidence),
        Pass(
            "summary",
            f"TechnoSquare microbit {sid} — student summary",
            prompts["summary"],
            summary,
            [],
        ),
    ]


def preflight(plan: list[Pass]) -> list[str]:
    """Everything checkable without spending a single quota slot."""
    problems = []
    for ps in plan:
        for up in ps.uploads:
            if not up.resolves():
                problems.append(f"{ps.key}: upload does not resolve — {up.path}")
        if not ps.instructions.strip():
            problems.append(f"{ps.key}: empty instructions")
    return problems


# --------------------------------------------------------------------------
# the live run
# --------------------------------------------------------------------------


async def _run_pass(client, ps: Pass, out_dir: Path, notebooks: dict[str, str]) -> dict:
    from notebooklm import SlideDeckFormat

    nb_id = notebooks.get(ps.notebook)
    if nb_id is None:  # step 1-2: reuse before create, never spawn duplicates
        existing = {nb.title: nb.id for nb in await client.notebooks.list()}
        nb_id = existing.get(ps.notebook)
        if nb_id is None:
            nb_id = (await client.notebooks.create(ps.notebook)).id
            print(f"  created notebook {ps.notebook!r} -> {nb_id}")
        else:
            print(f"  reusing notebook {ps.notebook!r} -> {nb_id}")
        notebooks[ps.notebook] = nb_id
        # step 3: sources go up once per notebook, not once per pass
        have = {s.title for s in await client.sources.list(nb_id)}
        for up in ps.uploads:
            if up.title in have:
                continue
            await client.sources.add_file(nb_id, up.path, wait=True, title=up.title)
            print(f"    + {up.title}")

    # step 4: nothing generates until every source is READY
    srcs = await client.sources.list(nb_id)
    not_ready = [s.title for s in srcs if int(getattr(s.status, "value", s.status)) != READY]
    if not_ready:
        raise HardStop(f"sources not READY: {', '.join(not_ready)}")

    # A finished pass is never regenerated. Quota is daily and small; a rerun
    # after one pass of three failed must not spend a slot on work already done.
    done = out_dir / f"{ps.key}.pdf"
    if done.is_file():
        print(f"  {ps.key} already downloaded at {done} — skipping generation")
        return {"pass": ps.key, "notebook_id": nb_id, "task_id": None, "output": str(done)}

    # step 5-6
    status = await client.artifacts.generate_slide_deck(
        nb_id,
        instructions=ps.instructions,
        slide_format=SlideDeckFormat.DETAILED_DECK,
        language="ar",
    )
    task_id = getattr(status, "task_id", None)
    if not task_id:
        # an empty success, not an empty error — the daily-quota signature
        raise HardStop(
            "generate_slide_deck returned an empty task_id. This is NotebookLM's "
            "daily quota exhaustion signature, not short-term rate limiting. Stop "
            "and wait for the reset; retrying only burns time."
        )
    out = out_dir / f"{ps.key}.pdf"
    try:
        await client.artifacts.wait_for_completion(nb_id, task_id, initial_interval=15)
    except TimeoutError:
        # A client-side give-up is not a server-side failure; the deck is often
        # already finished. Only a timeout means this — every other exception is
        # a real defect and must not be disguised as a download attempt.
        print("  wait timed out; the deck may already be done — trying download")
    await client.artifacts.download_slide_deck(nb_id, out, artifact_id=task_id)
    print(f"  downloaded {out}")
    return {"pass": ps.key, "notebook_id": nb_id, "task_id": task_id, "output": str(out)}


async def run_live(sid: str, plan: list[Pass]) -> dict:
    from notebooklm import NotebookLMClient

    out_dir = VAULT / "80-generation" / sid
    out_dir.mkdir(parents=True, exist_ok=True)
    # `from_storage()` returns a context manager, not a client. Awaiting it
    # directly yields an object whose every call dies with "Client not
    # initialized" — confirmed live, 2026-08-20.
    async with NotebookLMClient.from_storage() as client:
        lang = await client.settings.get_output_language()
        if lang != "ar":  # step 0
            raise HardStop(f"account output language is {lang!r}, must be 'ar'")
        notebooks: dict[str, str] = {}
        results = []
        for ps in plan:
            print(f"[{ps.key}]")
            results.append(await _run_pass(client, ps, out_dir, notebooks))
        return {"session": sid, "passes": results}


# --------------------------------------------------------------------------
# receipt
# --------------------------------------------------------------------------


def write_receipt(sid: str, payload: dict) -> Path:
    import yaml

    out = VAULT / "90-receipts" / f"{sid}.production.yaml"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = dict(payload)
    payload["visual_review"] = "PENDING — OCR-blind, a human must open the PDF"
    payload["overall"] = "UNVERIFIED"
    out.write_text(yaml.safe_dump(payload, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return out


# --------------------------------------------------------------------------
# self-check
# --------------------------------------------------------------------------

_DEMO_MAP = """
| ID | Slide | Path | Class | Production status |
| --- | --- | --- | --- | --- |
| `logo` | all | `Techno Square identity/PNG/white logo.png` | REFERENCE | Produced and mapped |
| `img-20-bug1` | 17 | `75-bundle/L1-s1/assets/_demo-fixture-never-exists.png` | EVIDENCE | Needs owner review |
"""

_DEMO_PROMPTS = """
## Notebook A — Student Slide Deck
```
pass A body
```
## Notebook B — Summary
```
summary body
```
## Notebook A — PASS B
```
pass B body
```
"""


def _demo() -> None:
    assets = parse_asset_mapping(_DEMO_MAP)
    assert len(assets) == 2, assets
    assert assets[0].klass == "REFERENCE" and assets[0].produced
    assert assets[1].aid == "img-20-bug1" and not assets[1].produced
    assert assets[0].path.is_absolute()

    # the blueprint gate refuses anything short of a clean owner approval
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        bp = Path(td) / "blueprint.md"
        for body, why in (
            ("---\nstatus: draft-awaiting-owner-approval\n---\n", "draft"),
            ("---\nstatus: approved\n---\nGAP - owner must decide\n", "open gap"),
            ("---\ntype: blueprint\n---\n", "no status field"),
        ):
            bp.write_text(body, encoding="utf-8")
            try:
                enforce_blueprint_gate(bp)
            except HardStop:
                pass
            else:  # pragma: no cover
                raise AssertionError(f"blueprint gate let {why} through")
        bp.write_text("---\nstatus: approved\n---\nall settled\n", encoding="utf-8")
        enforce_blueprint_gate(bp)

    # a row that is not yet produced must stop the run, not warn
    try:
        enforce_asset_gate(assets)
    except HardStop as exc:
        assert "not yet produced" in str(exc)
    else:  # pragma: no cover
        raise AssertionError("unproduced asset did not hard-stop")

    assets[1].status = "Produced and mapped"
    try:
        enforce_asset_gate(assets)
    except HardStop as exc:
        assert "missing on disk" in str(exc), exc
    else:  # pragma: no cover
        raise AssertionError("dangling path did not hard-stop")

    p = parse_prompts(_DEMO_PROMPTS)
    assert p == {"deck-a": "pass A body", "summary": "summary body", "deck-b": "pass B body"}, p

    clause = evidence_clause([assets[1]])
    assert "slide 17" in clause and "Do NOT draw" in clause
    assert evidence_clause([]) == ""
    print("self-check OK")


# --------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("session", nargs="?", help="session id, e.g. L1-s1")
    ap.add_argument("--live", action="store_true", help="actually call NotebookLM and spend quota")
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args(argv)

    if args.self_check:
        _demo()
        return 0
    if not args.session:
        ap.error("session id required")

    sid = paths.validate_session_id(args.session)
    bundle = VAULT / "75-bundle" / sid

    mapping = bundle / "ASSET-MAPPING.md"
    prompt_file = VAULT / "80-generation" / "nblm-student-deck-prompts.md"
    for f in (mapping, prompt_file):
        if not f.is_file():
            print(f"HARD STOP: missing {f}", file=sys.stderr)
            return 2

    try:
        assets = parse_asset_mapping(mapping.read_text(encoding="utf-8"))
        enforce_blueprint_gate(bundle / "blueprint.md")
        enforce_asset_gate(assets)
        plan = build_plan(sid, assets, parse_prompts(prompt_file.read_text(encoding="utf-8")))
        problems = preflight(plan)
        if problems:
            raise HardStop("preflight failed — " + "; ".join(problems))
    except HardStop as exc:
        print(f"HARD STOP: {exc}", file=sys.stderr)
        return 2

    evidence_n = sum(1 for a in assets if a.klass == "EVIDENCE")
    print(f"{sid}: {len(assets)} assets, {evidence_n} reserved as evidence")
    for ps in plan:
        print(f"  {ps.key:8} -> {len(ps.uploads)} sources, notebook {ps.notebook!r}")

    if not args.live:
        print("\ndry run — nothing uploaded, no quota spent. Add --live to fire.")
        return 0

    payload = asyncio.run(run_live(sid, plan))
    print(f"\nreceipt: {write_receipt(sid, payload)}")
    print("Deck is NOT done. Merge the two passes, overlay evidence, then review by eye.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
