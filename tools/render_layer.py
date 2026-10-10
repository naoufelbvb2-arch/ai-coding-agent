"""Render manually selected source-backed architecture articles; documentation only."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "reviews/canonical/SOURCE_CATALOGUE.json").read_text(encoding="utf-8"))
NAMES = {"L0": "L0_FOUNDATION", "L1": "L1_CONTROL", "L2": "L2_COGNITION", "L3": "L3_ACTIONS",
         "L4": "L4_TEMPORAL_SPECIALISTS", "L5": "L5_MEMORY", "L6": "L6_RECOVERY", "L7": "L7_RUNTIME_INTEGRATION"}


def source_link(source, label=None, line=None):
    path = source["source_path"]
    line = line or source.get("bundle_start_line", source.get("start_line", 1))
    return f"[{label or source.get('unit_id', source.get('name', 'source'))}](<../{path}#L{line}>)"


def fca(number):
    return next(section for section in DATA["fca_sections"] if section["section"] == str(number))


def message(order):
    return next(item for item in DATA["messages"] if item["order"] == order)


def segment(order, prefix):
    candidates = [item for item in message(order)["segments"] if item["heading"].startswith(prefix)]
    if len(candidates) != 1:
        raise ValueError((order, prefix, len(candidates)))
    return {**candidates[0], "source_path": message(order)["source_path"]}


def rule(identifier, text, sources):
    return f"### {identifier}\n\n{text}\n\nSource: " + "; ".join(source_link(item) for item in sources) + ".\n"


def retained(source, identifier):
    # Retain one already-current source unit, never an entire mixed draft/correction bundle.
    raw = source["raw"]
    lines = raw.splitlines()[1:]
    body = "\n".join(lines).strip().strip("-").strip()
    # Source headings remain subordinate to the canonical article, with exact source locator.
    body = re.sub(r"^#{1,6} ", "#### ", body, flags=re.M)
    return f"### {identifier} — {source.get('title', source.get('heading'))}\n\n{body}\n\nSource: {source_link(source)}; source-unit SHA-256 `{source['sha256']}`.\n"


def retained_prose(source, identifier):
    from source_catalogue import declarations
    raw = source['raw']
    if source.get('heading','').startswith('C01-35') and source['unit_id'].startswith('RDMS-02'):
        raw = raw.split('\nResolution\n')[0]
    if source.get('heading','').startswith('C01-48') and source['unit_id'].startswith('RDMS-03'):
        raw = raw.split('\nC01 Resolution\n')[0]
    raw = re.split(r"\nRDMS-\d+ — (?:Freeze Review|Adversarial Freeze Review)",raw,maxsplit=1)[0]
    for declaration in declarations(raw):
        raw = raw.replace(declaration['raw'], '[Record declaration: consult its sole owner in the contract registry.]')
    return retained({**source, 'raw': raw}, identifier)


def write(layer, content):
    directory = ROOT / "architecture"
    directory.mkdir(exist_ok=True)
    content="\n".join(line.rstrip() for line in content.rstrip().splitlines())+"\n"
    (directory / (NAMES[layer] + ".md")).write_text(content, encoding="utf-8", newline="\n")


def header(layer, mandate, status):
    return f"# {NAMES[layer].replace('_', ' ')}\n\n**Document status: {status}; NOT FROZEN.** Source baselines retain their recorded specification freeze; this consolidation has no new freeze authority. Production implementation is not authorized.\n\n{mandate}\n\n" + \
        "Each source-backed article is current only within its stated scope. Imported contracts retain the named owner; storage, delivery and scheduling do not create additional authorization. Source text remains unchanged in the archive. Source spelling and optionality are preserved; unspecified serialization types are not invented.\n\n"


def imports(rows):
    return "## Imported and exported boundaries\n\n| Contract / responsibility | Canonical owner | This layer's obligation |\n|---|---|---|\n" + \
        "\n".join(f"| {contract} | [{owner}](../architecture/{NAMES[owner]}.md) | {obligation} |" for contract, owner, obligation in rows) + "\n\n"
