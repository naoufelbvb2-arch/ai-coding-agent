"""Build source evidence indices for the Stage A checkpoint, without editing sources."""
import csv
import hashlib
import json
from pathlib import Path
import re
import sys
from archive_inventory import classify

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "source_archive/project/AI_CODING_AGENT"
SOURCES = PROJECT / "reviews/source_archive/RDMS_ORIGINAL_SOURCES"
OWNER = {"RDMS-01": "L1", "RDMS-02": "L2", "RDMS-03": "L3", "RDMS-04": "L3",
         "RDMS-05": "L4", "RDMS-06": "L4", "RDMS-07": "L5", "RDMS-08": "L2",
         "RDMS-09": "L6", "RDMS-10": "L7"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(name, obj):
    (ROOT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    manifest = json.loads((ROOT / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    # Read every text document and every JSON file, not just the normative candidates.
    text_index = []
    json_errors = []
    for record in manifest["records"]:
        path = ROOT / record["archived_path"]
        name = path.name
        record["classification"], record["authority_basis"] = classify(record["origin"])
        version = re.search(r"(v\d+(?:\.\d+)+|GAIA[_-]C\d+|RDMS-\d+)", record["origin"])
        record["version"] = version.group(0) if version else "Not specified in filename; see document index"
        record["authority_status"] = {
            "Frozen authoritative source": "Current frozen FCA" if "v1.0.1" in name else "Historical frozen FCA; superseded for current use",
            "Mixed authoritative source bundle": "Supplied frozen composite; baseline and explicit corrections admitted by recorded final decision; external approval not authenticated",
            "Historical draft": "Historical, not independently current normative law",
            "Previous integration attempt": "Candidate/editorial derivative; not independently authoritative",
            "Supporting verification evidence": "Evidence/artifact only; no independent normative authority",
        }[record["classification"]]
        if "_APPROVED_SOURCE_SET.txt" in name:
            record["version"] += " / v1.0 baseline plus recorded amendment and final freeze chain; see SOURCE_UNITS.json"
        if path.suffix.lower() not in {".md", ".txt", ".json", ".csv", ".py", ".log", ".sha256"}:
            continue
        text = path.read_text(encoding="utf-8-sig")
        headings = [{"line": i + 1, "text": line} for i, line in enumerate(text.splitlines())
                    if re.match(r"^(#{1,6} |SOURCE PART:|MESSAGE ID:|(?:PART|Part) [IVX]+|C\d+-\d+|FC\d+-\d+-\d+|\d+\. )", line)]
        entry = {"source_id": record["source_id"], "path": record["archived_path"],
                 "lines": len(text.splitlines()), "headings": headings,
                 "classification": record["classification"]}
        if path.suffix == ".json":
            try:
                obj = json.loads(text)
                entry["json_shape"] = {"kind": type(obj).__name__, "keys": list(obj) if isinstance(obj, dict) else [],
                                       "items": len(obj) if hasattr(obj, "__len__") else None}
            except ValueError as error:
                json_errors.append({"path": record["archived_path"], "error": str(error)})
        text_index.append(entry)
    write("DOCUMENT_INDEX.json", text_index)
    write("SOURCE_MANIFEST.json", manifest)
    with (ROOT / "SOURCE_MANIFEST.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(manifest["records"][0]))
        writer.writeheader()
        writer.writerows(manifest["records"])

    original_manifest = json.loads((SOURCES / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    dom = json.loads((SOURCES / "original_message_dom.json").read_text(encoding="utf-8"))
    by_id = {message["id"]: message for message in dom}
    messages = []
    for record in original_manifest:
        message = by_id[record["message_id"]]
        text = message["text"]
        path = SOURCES / (record["specification"] + "_APPROVED_SOURCE_SET.txt")
        bundle = path.read_text(encoding="utf-8")
        offset = bundle.find(text)
        start = bundle[:offset].count("\n") + 1 if offset >= 0 else None
        original = record["part"] == "Original draft"
        freezes = [{"line": start + i, "text": line} for i, line in enumerate(text.splitlines())
                   if not original and re.search(r"FROZEN", line)
                   and "NOT FROZEN" not in line and "CANDIDATE" not in line
                   and (record["specification"] in line or line.startswith("STATUS: FROZEN"))]
        messages.append({**record, "owner_layer": OWNER[record["specification"]],
                         "archived_path": path.relative_to(ROOT).as_posix(),
                         "start_line": start, "end_line": start + text.count("\n") if start else None,
                         "role_in_export": message["role"], "hash_matches": sha(text.encode("utf-8")) == record["text_sha256"],
                         "characters_match": len(text) == record["text_characters"],
                         "exact_text_in_bundle": offset >= 0,
                         "classification": "Historical draft" if original else "Approved amendment or correction",
                         "additional_classifications": ["Freeze decision"] if freezes else [],
                         "authority_scope": "Unchanged baseline clauses only, as admitted by final freeze; superseded clauses remain historical" if original else "Explicit corrections only; review prose creates no additional powers",
                         "freeze_evidence": freezes})
    write("SOURCE_UNITS.json", messages)

    fca = PROJECT / "reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md"
    lines = fca.read_text(encoding="utf-8").splitlines()
    base_sections = []
    # This is a proposed editorial allocation. Shared invariant text is referenced, not re-owned.
    assignments = {
        "L0": [*range(0, 5), 20, 21, 72, 73, 84, 86, 87],
        "L1": [48, 49, 50, 51],
        "L2": [*range(5, 11), *range(15, 20), *range(22, 35), *range(36, 40), 55, 74, 81, 83],
        "L3": [11, 12, 13, 14, 35, *range(40, 48), 75, 76, 79],
        "L4": [53, 54, 56, *range(63, 72), 78, 80, 82],
        "L5": [*range(57, 63), 77], "L6": [52], "L7": [85],
    }
    section_owner = {number: owner for owner, numbers in assignments.items() for number in numbers}
    assert sorted(section_owner) == list(range(88))
    assert sum(map(len, assignments.values())) == 88
    for i, line in enumerate(lines):
        match = re.match(r"^## (\d+)\. (.+)$", line)
        if match:
            number = int(match.group(1))
            base_sections.append({"section": str(number), "heading": match.group(2), "line": i + 1,
                                  "proposed_owner": section_owner[number], "source": fca.relative_to(ROOT).as_posix()})
    assert sorted(int(row["section"]) for row in base_sections) == list(range(88))
    appendices = [{"appendix": match.group(1), "heading": match.group(2), "line": i + 1,
                   "proposed_owner": "L2" if match.group(1) == "D" else "L0",
                   "handling": "Preserve normative status of source content; cross-cutting matrix/scenarios reference single operative owner contracts; Appendix B stays explicitly non-normative"}
                  for i, line in enumerate(lines)
                  if (match := re.match(r"^# Appendix ([A-G]) — (.*)$", line))]
    write("FCA_SECTION_OWNERSHIP_PROPOSAL.json", {"status": "PROPOSED_NOT_APPROVED", "sections": base_sections,
                                                "appendices": appendices,
                                                "unnumbered_invariants": "FCA-I01 onward: index in L0; each operative rule owned in its responsible layer with explicit source locator"})

    pair_checks = []
    for sidecar in (PROJECT / "reviews/source_archive").glob("*.sha256"):
        expected, name = sidecar.read_text(encoding="utf-8").strip().split(maxsplit=1)
        local_name = name.replace("\\", "/").split("/")[-1]
        actual = sha((sidecar.parent / local_name).read_bytes())
        pair_checks.append({"file": local_name, "original_locator": name,
                            "locator_resolution": "Same archived directory, filename preserved; historical absolute path is not a live path",
                            "expected": expected, "actual": actual, "result": "PASS" if expected == actual else "FAIL"})
    summary = {"stage": "A_SOURCE_CHECKPOINT_ONLY", "inventory_records": len(manifest["records"]),
               "project_files": 190, "text_documents_inspected": len(text_index), "json_parse_errors": json_errors,
               "fca_checksum_checks": pair_checks, "fca_base_numbered_sections": len(base_sections), "fca_appendices": len(appendices),
               "rdms_source_bundles": len(OWNER), "rdms_original_messages": len(messages),
               "rdms_baselines": sum(row["classification"] == "Historical draft" for row in messages),
               "rdms_correction_and_freeze_messages": sum(row["classification"] != "Historical draft" for row in messages),
               "rdms_message_hashes_pass": all(row["hash_matches"] and row["characters_match"] and row["exact_text_in_bundle"] for row in messages),
               "rdms_final_freeze_evidence_present": {spec: bool([e for row in messages if row["specification"] == spec for e in row["freeze_evidence"]]) for spec in OWNER},
               "external_approval_authenticated": False, "source_roles": sorted(set(row["role_in_export"] for row in messages)),
               "canonical_architecture_rewritten": False, "full_effective_law_verified": False, "freeze_status": "HOLD"}
    write("VERIFICATION_RESULTS.json", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    assert not json_errors
    assert summary["rdms_message_hashes_pass"]
    assert all(summary["rdms_final_freeze_evidence_present"].values())
    assert all(check["result"] == "PASS" for check in pair_checks)


if __name__ == "__main__":
    main()
