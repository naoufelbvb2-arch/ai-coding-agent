"""Verify the Stage A evidence and Git byte preservation; no archived tooling is run."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent


def main():
    manifest = json.loads((ROOT / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    units = json.loads((ROOT / "SOURCE_UNITS.json").read_text(encoding="utf-8"))
    allocation = json.loads((ROOT / "FCA_SECTION_OWNERSHIP_PROPOSAL.json").read_text(encoding="utf-8"))
    errors = []
    git_stage = "--git-index" in sys.argv
    git_commit = "--git-head" in sys.argv
    head_available = subprocess.run(["git", "rev-parse", "--verify", "HEAD"], cwd=WORKSPACE,
                                    capture_output=True).returncode == 0
    if git_commit and not head_available:
        errors.append("HEAD unavailable: checkpoint commit has not been created")
    for record in manifest["records"]:
        path = ROOT / record["archived_path"]
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != record["sha256"]:
            errors.append(f"Archived bytes changed: {record['source_id']}")
        if git_stage or (git_commit and head_available):
            rel = path.relative_to(WORKSPACE).as_posix()
            obj = ("HEAD:" if git_commit else ":") + rel
            result = subprocess.run(["git", "show", obj], cwd=WORKSPACE, capture_output=True)
            if result.returncode != 0 or hashlib.sha256(result.stdout).hexdigest() != record["sha256"]:
                errors.append(f"Git blob missing or changed: {rel}")
    for unit in units:
        path = ROOT / unit["archived_path"]
        lines = path.read_text(encoding="utf-8").splitlines()
        if not 1 <= unit["start_line"] <= unit["end_line"] <= len(lines):
            errors.append(f"Invalid line range: {unit['message_id']}")
        if not all(unit[key] for key in ("hash_matches", "characters_match", "exact_text_in_bundle")):
            errors.append(f"Unverified original message: {unit['message_id']}")
    if sorted(int(row["section"]) for row in allocation["sections"]) != list(range(88)):
        errors.append("FCA section allocation missing or duplicated")
    if {row["appendix"] for row in allocation["appendices"]} != set("ABCDEFG"):
        errors.append("FCA appendix allocation incomplete")
    plan = (ROOT / "INTERFACE_REVIEW_PLAN.md").read_text(encoding="utf-8")
    if sorted(re.findall(r"^\| (X8-\d{2}) \|", plan, re.M)) != [f"X8-{i:02d}" for i in range(1, 13)]:
        errors.append("Twelve interface paths missing or duplicated")
    local_links = 0
    for document in ROOT.glob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:", "#")):
                continue
            local_links += 1
            if not (document.parent / target.split("#")[0]).exists():
                errors.append(f"Broken document link: {document.name}: {target}")
    if (WORKSPACE / "architecture").exists():
        errors.append("Live canonical architecture directory exists before checkpoint approval")
    branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=WORKSPACE, text=True).strip()
    origin = subprocess.check_output(["git", "remote", "get-url", "origin"], cwd=WORKSPACE, text=True).strip()
    if not branch.startswith("docs/"):
        errors.append("Not on a documentation branch")
    result = {"stage": "A_ONLY", "source_files_verified": len(manifest["records"]),
              "source_unit_locators_verified": len(units), "fca_sections_owned_once": 88,
              "fca_appendices_indexed": 7, "interface_paths_indexed": 12,
              "local_report_links_checked": local_links,
              "git_blob_hash_checks": len(manifest["records"]) if git_stage or (git_commit and head_available) else 0,
              "git_check_target": "HEAD" if git_commit else "index" if git_stage else "not requested",
              "branch": branch, "origin": origin, "errors": errors,
              "status": "PASS" if not errors else "FAIL",
              "limitation": "Inventory and custody checks, not full semantic reconciliation or interface proof"}
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
