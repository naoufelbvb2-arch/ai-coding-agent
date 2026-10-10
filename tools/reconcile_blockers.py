"""Apply the reviewed targeted documentation delta once, never regenerate layers."""
from collections import Counter
import hashlib
import json
import re
from pathlib import Path
from blocker_findings import FINDINGS, CLASS_NAMES
from render_layer import ROOT, DATA, NAMES
from schema_selection import REGISTRY

OUT = ROOT/'reviews/canonical'
BASELINE = 'd50b7f88105b5397aa7d76e0bb8a1c2099a7c85e'


def write_json(name, value):
    (OUT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def units():
    result = {}
    for msg in DATA['messages']:
        for item in msg['segments']:
            result[item['unit_id']] = {**item, 'source_path': msg['source_path']}
    for item in DATA['fca_sections']+DATA['fca_appendices']+DATA['fca_invariants']:
        result[item['unit_id']] = item
    return result


UNITS = units()


def evidence(ident):
    s = UNITS[ident]
    return {'unit_id': ident, 'source_path': s['source_path'],
            'start_line': s.get('bundle_start_line', s.get('start_line')),
            'end_line': s.get('bundle_end_line', s.get('end_line', s.get('start_line'))),
            'sha256': s['sha256'], 'exact_clause': s['raw']}


def link(s, owner=False):
    prefix = '../' if owner else '../../'
    return f"[{s['unit_id']}](<{prefix}{s['source_path']}#L{s['start_line']}>)"


def fields(raw):
    return re.findall(r'^    ([a-z][\w]*)(\??(?:\[\])?\??)(?::|\s*$)', raw or '', re.M)


def review(original):
    f = FINDINGS[original['id']]
    result = dict(original)
    result['original_status'] = original['status']
    result['status'] = {'B': 'OPEN_MAPPING_PROOF', 'C': 'DEFERRED_TO_IMPLEMENTATION_DESIGN',
                        'D': 'RESOLVED_WITH_SOURCE_EVIDENCE', 'E': 'OPEN_ARCHITECTURAL_DECISION',
                        'A': 'OPEN_NORMATIVE_CONFLICT'}[f['classification']]
    declarations = original.get('exact_source_declarations', [])
    if 'canonical_source' in original:
        declarations = [original['canonical_source'], original['transport_source']]
    scopes = list(f['additional_source_units'])
    # Include the exact smallest containing source unit for every candidate;
    # declaration bytes themselves remain present in the original question.
    for d in declarations:
        begin, end = d['bundle_start_line'], d['bundle_end_line']
        candidates = [s for s in UNITS.values() if s['source_path'] == d['source_path']
                      and s.get('bundle_start_line', s.get('start_line', 0)) <= begin
                      and s.get('bundle_end_line', s.get('end_line', s.get('start_line', 0))) >= end]
        if candidates:
            scopes.append(min(candidates, key=lambda s: len(s['raw']))['unit_id'])
    for s in original.get('exact_conflicting_scopes', []):
        scopes.append(s['unit_id'])
    source_evidence = [evidence(n) for n in dict.fromkeys(scopes)]
    result['normative_review'] = {**f, 'classification_name': CLASS_NAMES[f['classification']],
        'reviewed_baseline': BASELINE, 'source_evidence': source_evidence,
        'is_freeze_blocker': f['classification'] in 'ABE',
        'does_not_approve_serializer_alias': True,
        'candidate_field_surfaces': [dict(specification=d['specification'], source_part=d['source_part'],
                                        declaration_sha256=d['raw_sha256'], fields=fields(d['raw']))
                                     for d in declarations]}
    return result


def section(record, owner=False):
    r = record['normative_review']
    lines = [f"### {record['owner']}-NR-{record['id']}", '',
             f"**{r['classification']} — {r['classification_name']}; {record['status']}.**", '',
             r['justification'], '', '**Binding obligations:** '+r['binding_obligations'], '',
             '**Remaining detail / acceptance limit:** '+r['remaining_detail'], '']
    if r.get('correction'):
        lines += ['Source-determined correction: '+r['correction'], '']
    if r.get('decision_alternatives'):
        lines += ['Architecture review must decide the stated minimum; neither alternative is adopted.', '']
        lines += ['- '+a['option']+': '+a['consequence'] for a in r['decision_alternatives']]
        lines += ['']
    lines += ['Exact authoritative evidence: '+'; '.join(link(s, owner) for s in r['source_evidence'])+'.', '']
    return '\n'.join(lines)


def apply():
    if (OUT/'BLOCKER_CLASSIFICATION.json').exists():
        raise SystemExit('Already applied. Edit the owner documents and reviewed findings directly; no full regeneration.')
    originals = json.loads((OUT/'UNRESOLVED_ISSUES.json').read_text(encoding='utf-8'))
    assert len(originals) == 40 and set(FINDINGS) == {r['id'] for r in originals}
    records = [review(r) for r in originals]
    write_json('BLOCKER_CLASSIFICATION.json', records)
    write_json('UNRESOLVED_ISSUES.json', records)
    counts = Counter(FINDINGS[r['id']]['classification'] for r in records)
    summary = {'baseline': BASELINE, 'original_questions': 40,
               'classification_totals': {c: counts[c] for c in CLASS_NAMES},
               'resolved': counts['D'], 'implementation_deferred': counts['C'],
               'open_lossless_mapping_proofs': counts['B'], 'open_normative_conflicts': counts['A'],
               'architectural_decisions': counts['E'], 'freeze_readiness': 'HOLD',
               'architecture_frozen': False, 'new_architectural_decision_adopted': False}
    write_json('BLOCKER_RESOLUTION_SUMMARY.json', summary)
    current = {r['type']: r for r in REGISTRY}
    hashes = {}
    for owner in [f'L{i}' for i in range(1, 8)]:
        path = ROOT/'architecture'/(NAMES[owner]+'.md')
        content = path.read_text(encoding='utf-8')
        before = content
        hashes[owner] = hashlib.sha256(path.read_bytes()).hexdigest()
        for r in records:
            if r['owner'] != owner:
                continue
            typ = r.get('type')
            heading = '\n### '+str(typ)+'\n'
            if heading not in content:
                continue
            start = content.index(heading)
            match = re.search(r'\n(?:### |## )', content[start+len(heading):])
            end = start+len(heading)+match.start() if match else len(content)
            part = content[start:end]
            category = r['normative_review']['classification']
            if typ in {'Risk', 'ContainmentProof', 'TriggerFire'} and category == 'D':
                item = current[typ]
                selected = item['selected']
                replacement = heading+'\nCanonical owner: '+owner+'. Approved current scoped contract.\n\n'
                replacement += '```text\n'+item['effective_raw']+'\n```\n\n'
                replacement += r['normative_review']['binding_obligations']+'\n\n'
                replacement += 'The historical declarations remain in the immutable archive; their current disposition and exact amendment evidence are in the targeted review below. No historical converter is approved.\n'
                content = content[:start]+replacement+content[end:]
            elif category == 'C':
                part = part.replace('**Record-shape reconciliation remains OPEN.**',
                    '**Representation detail DEFERRED TO IMPLEMENTATION DESIGN.**')
                part = part.replace('this prevents a historical or partial declaration from being published as current complete law.',
                    'the binding obligations and intentionally unspecified representation detail are recorded in the targeted review below. Parent-field questions remain separately classified.')
                content = content[:start]+part+content[end:]
            elif category == 'D':
                part = part.replace('Parent/other-source declarations have different record surfaces. The registry retains their exact clauses; preserving the parent semantic obligations is mandatory, and field-renaming/conversion is not automatically approved.',
                    'Parent semantic preservation is proven by the authoritative elaborations cited in the targeted review below. This does not approve an automatic historical-record converter.')
                content = content[:start]+part+content[end:]
        owner_records = [r for r in records if r['owner'] == owner]
        content += '\n## Targeted normative reconciliation\n\n'
        content += 'This targeted review uses the published consolidation as its baseline. Classes B/E remain open; C defers only the stated representation detail; D is source-determined. These dispositions supply no new architectural decision, serializer alias, threshold or authority.\n\n'
        content += '\n'.join(section(r, owner=True) for r in owner_records)
        path.write_text(content.rstrip()+'\n', encoding='utf-8', newline='\n')
        assert content != before
    write_json('TARGETED_BASELINE_HASHES.json', hashes)
    registry = json.loads((OUT/'CANONICAL_CONTRACT_REGISTRY.json').read_text(encoding='utf-8'))
    for item in registry:
        relevant = [r for r in records if r.get('type') == item['type']]
        if relevant:
            item['targeted_review'] = [{'issue_id': r['id'], 'classification': r['normative_review']['classification'],
                                       'status': r['status']} for r in relevant]
        if item['type'] in {'Risk', 'ContainmentProof', 'TriggerFire'}:
            item.update({k: current[item['type']][k] for k in ['selected', 'effective_raw', 'status', 'explicit_overlays']})
    write_json('CANONICAL_CONTRACT_REGISTRY.json', registry)
    trace = json.loads((OUT/'CLAUSE_TRACEABILITY.json').read_text(encoding='utf-8'))
    # Update line locators after the small contract-section edits.
    for clause in trace:
        text = (ROOT/clause['document']).read_text(encoding='utf-8')
        match = re.search(r'^### '+re.escape(clause['clause_id'])+r'(?: |\s*$)', text, re.M)
        assert match, clause['clause_id']
        clause['line'] = text[:match.start()].count('\n')+1
    for r in records:
        doc = ROOT/'architecture'/(NAMES[r['owner']]+'.md')
        text = doc.read_text(encoding='utf-8')
        ident = r['owner']+'-NR-'+r['id']
        body = section(r, owner=True)
        line = text[:text.index('### '+ident)].count('\n')+1
        trace.append(dict(clause_id=ident, owner=r['owner'], document=doc.relative_to(ROOT).as_posix(),
            line=line, source_unit_ids=[s['unit_id'] for s in r['normative_review']['source_evidence']],
            article_sha256=hashlib.sha256(body.encode('utf-8')).hexdigest()))
    write_json('CLAUSE_TRACEABILITY.json', trace)
    lines = ['# Targeted normative blocker classification', '',
             'Reviewed baseline: `'+BASELINE+'`. Original questions: **40**. Every entry has exactly one classification.', '',
             '| Class | Meaning | Count |', '|---|---|---|']
    lines += [f'| {c} | {name} | {counts[c]} |' for c, name in CLASS_NAMES.items()]
    lines += ['', 'D closes the source-determined question; C defers only representation to Implementation Design. B requires a preservation proof and stays open. E requires an approved architectural decision. No direct mutually impossible pair was proven for class A; zero A does not mean the B/E legal-information gaps are harmless.', '',
              'Source custody, current-law completeness and implementation conformance are distinct. All original candidates and exact clauses/hashes remain in [BLOCKER_CLASSIFICATION.json](BLOCKER_CLASSIFICATION.json).', '']
    for r in records:
        lines.append(section(r))
    (OUT/'BLOCKER_CLASSIFICATION.md').write_text('\n'.join(lines).rstrip()+'\n', encoding='utf-8')
    (OUT/'UNRESOLVED_ISSUES.md').write_text('# Current issue dispositions\n\n'
        'The original 40 questions are preserved with their targeted dispositions. **8 resolved; 6 deferred to Implementation Design; 25 lossless-mapping proofs and 1 architectural decision remain open.** Full normative acceptance remains HOLD; NOT FROZEN.\n\n'
        'Exact question, classification, justification, binding obligations, remaining proof/decision and source clauses: [targeted classification](BLOCKER_CLASSIFICATION.md) and [full JSON register](UNRESOLVED_ISSUES.json).\n\n'
        'No question was removed. Deferred representation details cannot relax authority, identity, required information, lifecycle, durability or recovery.\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    apply()
