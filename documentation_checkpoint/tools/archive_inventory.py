"""Read-only source preservation and recursive ZIP inventory; no implementation code."""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import stat
import zipfile

WORKSPACE = Path(__file__).resolve().parents[2]
CHECKPOINT = WORKSPACE / "documentation_checkpoint"
ARCHIVE = CHECKPOINT / "source_archive"
INPUT = WORKSPACE / "AI_CODING_AGENT_CODEX_HANDOFF.zip"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def preserve(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data:
            raise RuntimeError(f"Refusing to replace preserved bytes: {path}")
    else:
        path.write_bytes(data)
    path.chmod(stat.S_IREAD)


def classify(name):
    if "RDMS-" in name and name.endswith("_APPROVED_SOURCE_SET.txt"):
        return "Mixed authoritative source bundle", "Embedded originals, amendments and decisions require section-level classification"
    if "Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md" in name:
        return "Frozen authoritative source", "FCA v1.0.1; verify embedded frozen status and paired checksum"
    if "Formal_Cognitive_Architecture_v1.0_FROZEN_SPEC.md" in name:
        return "Frozen authoritative source", "Historical frozen baseline explicitly superseded as current normative reference by FCA v1.0.1"
    if "Formal Cognitive Architecture v1.0.md" in name:
        return "Historical draft", "Earlier FCA draft retained for history; v1.0.1 governs current baseline"
    if "/architecture/" in name or "LAYER_SNAPSHOTS/" in name or "pre_normative_merge_L0_L7/" in name:
        return "Previous integration attempt", "Derived integration, not an independent primary authority"
    return "Supporting verification evidence", "Archive metadata, reviews, tooling or packaging; not admitted as new normative authority"


def inventory():
    records = []
    archive_checks = []

    def add(origin, path, data, is_zip=False):
        classification, basis = classify(origin)
        records.append({
            "source_id": f"S{len(records):04d}", "origin": origin,
            "archived_path": path.relative_to(CHECKPOINT).as_posix(),
            "bytes": len(data), "sha256": digest(data),
            "classification": classification, "authority_basis": basis,
            "version": "Not asserted; see section inventory" if "RDMS-" in origin else "Unspecified",
            "container": is_zip,
        })
        preserve(path, data)

    def visit(data, origin, destination, depth=0):
        if depth > 12:
            raise RuntimeError("Excessive archive nesting")
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            names = set()
            for item in z.infolist():
                if item.is_dir():
                    continue
                relative = PurePosixPath(item.filename.replace("\\", "/"))
                if relative.is_absolute() or ".." in relative.parts or any(":" in p for p in relative.parts):
                    raise RuntimeError(f"Unsafe ZIP path: {item.filename}")
                normalized = str(relative).casefold()
                if normalized in names:
                    raise RuntimeError(f"Duplicate ZIP path: {item.filename}")
                names.add(normalized)
                content = z.read(item)  # ZIP CRC checked by zipfile on read
                path = destination.joinpath(*relative.parts)
                child_origin = origin + "!/" + item.filename
                nested = item.filename.lower().endswith(".zip")
                add(child_origin, path, content, nested)
                if nested:
                    nested_dir = ARCHIVE / "project" if depth == 0 else path.with_suffix(".contents")
                    visit(content, child_origin, nested_dir, depth + 1)
            archive_checks.append({"origin": origin, "files": len(names), "crc": "PASS"})

    input_data = INPUT.read_bytes()
    add(INPUT.name, ARCHIVE / INPUT.name, input_data, True)
    visit(input_data, INPUT.name, ARCHIVE / "handoff")
    sums = (ARCHIVE / "handoff" / "SHA256SUMS.txt").read_text(encoding="utf-8")
    checks = []
    for line in sums.splitlines():
        expected, name = line.split(maxsplit=1)
        path = ARCHIVE / "handoff" / name.strip().lstrip("*")
        actual = digest(path.read_bytes())
        checks.append({"file": name.strip(), "expected": expected, "actual": actual,
                       "result": "PASS" if actual == expected else "FAIL"})
    manifest = {"scope": "Stage A checkpoint only; classification is evidence based and conservative",
                "input_sha256": digest(input_data), "records": records,
                "archive_crc_checks": archive_checks, "handoff_checksum_checks": checks}
    CHECKPOINT.mkdir(exist_ok=True)
    (CHECKPOINT / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    with (CHECKPOINT / "SOURCE_MANIFEST.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    print(json.dumps({"preserved_files": len(records), "zip_checks": archive_checks,
                      "handoff_checks": checks, "input_sha256": digest(input_data)}, indent=2))


def verify():
    manifest = json.loads((CHECKPOINT / "SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    failures = []
    for row in manifest["records"]:
        path = CHECKPOINT / row["archived_path"]
        if not path.is_file() or digest(path.read_bytes()) != row["sha256"]:
            failures.append(row["source_id"])
    originals_unchanged = digest(INPUT.read_bytes()) == manifest["input_sha256"]
    result = {"checked_files": len(manifest["records"]), "hash_failures": failures,
              "original_handoff_unchanged": originals_unchanged,
              "status": "PASS" if not failures and originals_unchanged else "FAIL",
              "immutability": "Read-only attributes and hashes; not WORM or administrator-proof storage"}
    print(json.dumps(result, indent=2))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    import sys
    verify() if "--verify" in sys.argv else inventory()
