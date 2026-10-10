"""Documentation-only source section and declaration indexing from preserved originals."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive"
OUT = ROOT / "reviews/canonical"
PRIMARY_OWNER = {"FCA": "L0", "RDMS-01": "L1", "RDMS-02": "L2", "RDMS-03": "L3", "RDMS-04": "L3",
                 "RDMS-05": "L4", "RDMS-06": "L4", "RDMS-07": "L5", "RDMS-08": "L2", "RDMS-09": "L6", "RDMS-10": "L7"}


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class Headings(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag = None
        self.parts = []
        self.headings = []

    def handle_starttag(self, tag, attrs):
        if re.fullmatch(r"h[1-6]", tag):
            self.tag = tag
            self.parts = []

    def handle_data(self, data):
        if self.tag:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == self.tag:
            self.headings.append({"level": int(tag[1]), "heading": "".join(self.parts).strip()})
            self.tag = None


def declarations(text):
    lines = text.splitlines()
    items = []
    for i, line in enumerate(lines):
        match = re.match(r"^([A-Z][A-Za-z0-9_]*)\s*\{\s*$", line.strip())
        if not match or line.startswith((" ", "\t")):
            continue
        balance = 0
        for j in range(i, len(lines)):
            balance += lines[j].count("{") - lines[j].count("}")
            if balance == 0:
                raw = "\n".join(lines[i:j + 1])
                items.append({"name": match.group(1), "start_line": i + 1, "end_line": j + 1,
                              "raw": raw, "raw_sha256": sha(raw),
                              "partial_or_example": bool(re.search(r"\.\.\.|^\s+\w+\s*=|\b(?:C12|C1|D10)\b", raw, re.M))})
                break
    return items


def build():
    manifest = json.loads((ARCHIVE / "RDMS_ORIGINAL_SOURCES/SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    dom = json.loads((ARCHIVE / "RDMS_ORIGINAL_SOURCES/original_message_dom.json").read_text(encoding="utf-8"))
    units = json.loads((ROOT / "documentation_checkpoint/SOURCE_UNITS.json").read_text(encoding="utf-8"))
    by_id = {item["message_id"]: item for item in units}
    messages = []
    for order, (meta, message) in enumerate(zip(manifest, dom)):
        assert meta["message_id"] == message["id"] and sha(message["text"]) == meta["text_sha256"]
        parser = Headings()
        parser.feed(message["html"])
        lines = message["text"].splitlines()
        positioned = []
        cursor = 0
        for heading in parser.headings:
            hits = [i for i in range(cursor, len(lines)) if lines[i].strip() == heading["heading"]]
            if not hits:
                continue
            start = hits[0]
            cursor = start + 1
            positioned.append({**heading, "start_line": start + 1})
        # Keep true HTML headings, not numbered list items mistaken for clauses.
        major = [h for h in positioned if re.match(r"^(?:\d+\. |C\d+-\d+|FC\d+-\d+-\d+|(?:PART|Part) [IVX]+|Test \d+|T\d+|R\d-|FR\d-|Additional Attack|One Remaining)", h["heading"])]
        segments = []
        for index, item in enumerate(major):
            end = major[index + 1]["start_line"] - 1 if index + 1 < len(major) else len(lines)
            raw = "\n".join(lines[item["start_line"] - 1:end])
            segments.append({**item, "end_line": end, "raw": raw, "sha256": sha(raw),
                             "bundle_start_line": by_id[meta["message_id"]]["start_line"] + item["start_line"] - 1,
                             "bundle_end_line": by_id[meta["message_id"]]["start_line"] + end - 1,
                             "unit_id": f"{meta['specification']}-M{order:02d}-U{index:03d}"})
        decls = declarations(message["text"])
        for decl in decls:
            decl.update({"specification": meta["specification"], "source_part": meta["part"], "message_id": meta["message_id"],
                         "source_path": "documentation_checkpoint/" + by_id[meta["message_id"]]["archived_path"],
                         "bundle_start_line": by_id[meta["message_id"]]["start_line"] + decl["start_line"] - 1,
                         "bundle_end_line": by_id[meta["message_id"]]["start_line"] + decl["end_line"] - 1,
                         "message_order": order})
        messages.append({**meta, "order": order, "source_path": "documentation_checkpoint/" + by_id[meta["message_id"]]["archived_path"],
                         "owner": PRIMARY_OWNER[meta["specification"]], "segments": segments, "declarations": decls})
    fca_path = ARCHIVE / "Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md"
    fca_text = fca_path.read_text(encoding="utf-8")
    fca_lines = fca_text.splitlines()
    starts = [(i, match.group(1), match.group(2)) for i, line in enumerate(fca_lines)
              if (match := re.match(r"^## (\d+(?:\.\d+)*)\. (.+)$", line))]
    sections = []
    for index, (start, number, title) in enumerate(starts):
        end = starts[index + 1][0] if index + 1 < len(starts) else 3264
        # Numbered units end before unrelated next Part headings or the unnumbered invariant corpus.
        for n in range(start + 1, end):
            if fca_lines[n].startswith("# Part "):
                end = n
                break
        raw = "\n".join(fca_lines[start:end])
        sections.append({"unit_id": "FCA-" + number, "section": number, "title": title, "start_line": start + 1,
                         "end_line": end, "raw": raw, "sha256": sha(raw), "source_path": fca_path.relative_to(ROOT).as_posix()})
    invariants = [{"unit_id": m.group(1), "raw": line, "start_line": i + 1,
                   "sha256": sha(line), "source_path": fca_path.relative_to(ROOT).as_posix()}
                  for i, line in enumerate(fca_lines) if (m := re.match(r"\*\*(FCA-I\d+)\*\*", line))]
    fca_decls = declarations(fca_text)
    for decl in fca_decls:
        decl.update({"specification": "FCA", "source_part": "v1.0.1 FROZEN", "message_id": "FCA-1.0.1-FROZEN-SPEC",
                     "source_path": fca_path.relative_to(ROOT).as_posix(), "bundle_start_line": decl["start_line"],
                     "bundle_end_line": decl["end_line"], "message_order": -1})
    OUT.mkdir(parents=True, exist_ok=True)
    data = {"messages": messages, "fca_sections": sections, "fca_invariants": invariants, "fca_declarations": fca_decls}
    appendix_starts = [(i, re.match(r"^# Appendix ([A-G]) ",line).group(1)) for i,line in enumerate(fca_lines) if re.match(r"^# Appendix ([A-G]) ",line)]
    data["fca_appendices"] = []
    for index,(start,letter) in enumerate(appendix_starts):
        end=appendix_starts[index+1][0] if index+1<len(appendix_starts) else len(fca_lines)
        raw="\n".join(fca_lines[start:end])
        data["fca_appendices"].append({"unit_id":"FCA-APP-"+letter,"section":letter,"title":fca_lines[start].lstrip("# "),"start_line":start+1,"end_line":end,"raw":raw,"sha256":sha(raw),"source_path":fca_path.relative_to(ROOT).as_posix()})
    (OUT / "SOURCE_CATALOGUE.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"messages": len(messages), "rdms_sections": sum(len(m["segments"]) for m in messages),
                      "rdms_declarations": sum(len(m["declarations"]) for m in messages),
                      "fca_sections": len(sections), "fca_invariants": len(invariants), "fca_declarations": len(fca_decls)}, indent=2))


if __name__ == "__main__":
    build()
