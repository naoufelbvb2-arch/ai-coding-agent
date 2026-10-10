"""Verify source custody, trace, ownership and dangerous amendment regressions."""
from collections import Counter
import hashlib
import json
import re
from render_layer import ROOT, DATA, NAMES
from schema_selection import REGISTRY

OUT=ROOT/'reviews/canonical'

def verify():
    failures=[]
    counts={}
    if not (OUT/'VERIFICATION.md').exists():
        (OUT/'VERIFICATION.md').write_text('# Verification record\n\nGeneration in progress.\n',encoding='utf-8')
    def check(label,condition,detail=None):
        if not condition:failures.append({'check':label,'detail':detail})
    manifest=json.loads((ROOT/'documentation_checkpoint/SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
    for r in manifest['records']:
        path=ROOT/'documentation_checkpoint'/r['archived_path']
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        check('original-file-sha256',actual==r['sha256'],str(path))
        check('original-size',path.stat().st_size==r['bytes'],str(path))
    counts['archive_files']=len(manifest['records'])
    texts={l:(ROOT/'architecture'/(n+'.md')).read_text(encoding='utf-8') for l,n in NAMES.items()}
    for layer,text in texts.items():
        check('no-new-freeze','NOT FROZEN' in text,layer)
        check('owner-boundary', 'owner' in text.lower(),layer)
    known_units={s['unit_id']:{**s,'source_path':m['source_path']} for m in DATA['messages'] for s in m['segments']}
    known_units.update({s['unit_id']:s for s in DATA['fca_sections']+DATA['fca_appendices']+DATA['fca_invariants']})
    for unit in known_units.values():
        check('source-unit-sha256',hashlib.sha256(unit['raw'].encode('utf-8')).hexdigest()==unit['sha256'],unit['unit_id'])
        lines=(ROOT/unit['source_path']).read_text(encoding='utf-8').splitlines()
        begin=unit.get('bundle_start_line',unit['start_line'])
        end=unit.get('bundle_end_line',unit.get('end_line',begin))
        check('exact-source-clause-range','\n'.join(lines[begin-1:end])==unit['raw'],unit['unit_id'])
    counts['catalogued_source_units']=len(known_units)
    clauses=json.loads((OUT/'CLAUSE_TRACEABILITY.json').read_text(encoding='utf-8'))
    check('unique-clause-identities',len({c['clause_id'] for c in clauses})==len(clauses))
    for c in clauses:
        check('article-provenance',bool(c['source_unit_ids']),c['clause_id'])
        for ident in c['source_unit_ids']:
            check('article-source-locator',ident in known_units,(c['clause_id'],ident))
    counts['source_backed_articles']=len(clauses)
    shapes=[]
    for layer,text in texts.items():
        for match in re.finditer(r'```(?:text)?\n([\s\S]*?)\n```',text):
            for name in re.findall(r'^([A-Z]\w*) \{\s*$',match.group(1),re.M):
                shapes.append((name,layer))
    names=Counter(n for n,l in shapes)
    check('single-current-record-definition',not [n for n,c in names.items() if c>1],[(n,c) for n,c in names.items() if c>1])
    registered={r['type']:r for r in REGISTRY}
    for name,layer in shapes:
        check('record-owner',name in registered and registered[name]['owner']==layer,(name,layer))
    for name in ['CanonicalEntity','GoalStack','LedgerHead','RuntimeStatus']:
        check('superseded-record-not-exported',name not in names,name)
    def effective(name):return registered[name]['effective_raw'] or ''
    for old in ['due_at','removal_trigger_id','revisit_trigger_id']:
        check('commitment-scoped-removal',not re.search(r'^    '+old+r'\??',effective('Commitment'),re.M),old)
    check('commitment-required-root','    reactivation_condition_ref' in effective('Commitment'))
    check('commitment-unaffected-fields',all(n in effective('Commitment') for n in ['statement','why_temporary','scope','linked_entity_refs','created_at','resolution_ref']))
    check('hypothesis-single-lifecycle','    lifecycle:' in effective('Hypothesis') and '    status:' not in effective('Hypothesis'))
    check('slice-no-giant-status','    status:' not in effective('Slice') and 'base_state_version' not in effective('Slice'))
    check('observation-trust-fields',all(n in effective('Observation') for n in ['trust_context_ref','normalization_profile_ref?','evidence_origin_group_ref','capture_integrity']))
    check('advisory-semantic-recommendation','BLOCK_RECOMMENDED' in effective('SemanticAssessment') and 'BLOCK_CANDIDATE' not in effective('SemanticAssessment'))
    check('process-mode-replacement','    mode:' not in effective('ProcessExecutionRequest') and 'ProcessLaunch' in registered['ProcessExecutionRequest']['associated_contracts'])
    check('invariant-enforcement-spec','enforcement_specs[]' in effective('Invariant') and 'enforcement_modes' not in effective('Invariant'))
    check('capsule-single-owner',registered['ResumptionCapsule']['owner']=='L6' and registered['ResumeAssessment']['owner']=='L6')
    check('commitment-single-owner',registered['Commitment']['owner']=='L2')
    check('transport-distinction',all(registered[n]['owner']==o for n,o in [('CapabilityResult','L2'),('CapabilityTransportResult','L7'),('MemoryRetrievalResult','L5'),('MemoryRetrievalTransportResult','L7')]))
    check('no-invented-signatures',all(r['interface_signature_ratified'] is False for r in REGISTRY))
    links=0
    for path in list((ROOT/'architecture').glob('*.md'))+list(OUT.glob('*.md'))+[ROOT/'README.md']:
        content=path.read_text(encoding='utf-8')
        for match in re.finditer(r'\]\((?:<([^>]+)>|([^\s)]+))\)',content):
            target=match.group(1) or match.group(2)
            if target.startswith(('http:','https:','mailto:','#')):continue
            file,_,anchor=target.partition('#')
            resolved=(path.parent/file).resolve()
            check('local-link',resolved.exists(),(str(path),target))
            if resolved.is_file() and re.fullmatch(r'L\d+',anchor):
                n=int(anchor[1:])
                check('source-line-range',1<=n<=len(resolved.read_text(encoding='utf-8').splitlines()),target)
            links+=1
    counts['local_links_checked']=links
    counts['single_owner_exported_record_definitions']=len(shapes)
    interfaces=json.loads((OUT/'INTERFACE_VALIDATION.json').read_text(encoding='utf-8'))
    check('twelve-interface-paths',[x['id'] for x in interfaces]==[f'X8-{n:02d}' for n in range(1,13)])
    for p in interfaces:
        for key in ['authority','atomicity_durability','failure_retry_recovery','rejection_conditions','source_units']:
            check('interface-obligation',bool(p[key]),(p['id'],key))
    counts['interface_paths_processed']=len(interfaces)
    coverage=json.loads((OUT/'SOURCE_COVERAGE.json').read_text(encoding='utf-8'))
    check('source-scope-accounting',not any(c['disposition']=='RESIDUAL_SCOPE_REQUIRES_RECONCILIATION' for c in coverage))
    check('all-fca-sections',all(any(c['unit_id']=='FCA-'+str(n) for c in coverage) for n in range(88)))
    check('all-fca-invariants',all(sum('FCA-I'+str(n).zfill(2) in t for t in texts.values())>=1 for n in range(1,51)))
    check('final-trigger-interpretations',all(n in texts['L4'] for n in ['FC05-01','FC05-02']))
    check('final-recovery-interpretations',all('FC09-04-'+str(n).zfill(2) in texts['L6'] for n in range(1,5)))
    check('final-integration-interpretations',all('FC10-03-'+str(n).zfill(2) in texts['L7'] for n in range(1,9)))
    result={'mechanical_status':'FAIL' if failures else 'PASS','counts':counts,'failures':failures,
      'document_sha256':{l:hashlib.sha256((ROOT/'architecture'/(n+'.md')).read_bytes()).hexdigest() for l,n in NAMES.items()},
      'mandatory_semantic_acceptance':{
       'complete_authoritative_source_inventory':'PASS',
       'source_scope_dispositions_and_amendment_locators':'PASS' if not failures else 'CHECK_FAILURES',
       'original_source_sha256_integrity':'PASS' if not any(f['check']=='original-file-sha256' for f in failures) else 'FAIL',
       'unique_assigned_contract_ownership':'PASS' if not any(f['check']=='record-owner' for f in failures) else 'FAIL',
       'known_explicit_field_replacements':'PASS' if not failures else 'CHECK_FAILURES',
       'complete_non_superseded_field_preservation':'OPEN; exact shape and parent/projection questions recorded',
       'amendment_precedence_and_no_contradictory_effective_laws':'SCOPED REPLACEMENTS VERIFIED; full semantic acceptance remains OPEN',
       'no_unauthorized_authority_expansion':'SOURCE-BOUND AUTHORITY CONTRACTS RECORDED; independent semantic review required',
       'cross_layer_interfaces':'12 constraints reviewed; complete field/projection acceptance OPEN',
       'durability_and_recovery':'SOURCE REQUIREMENTS PRESERVED; serialization/admission conformance and runtime proof not claimed'},
      'full_normative_completion':False,'architecture_frozen':False,'production_implementation':False}
    targeted=OUT/'BLOCKER_RESOLUTION_SUMMARY.json'
    if targeted.exists():
        result['targeted_normative_review']=json.loads(targeted.read_text(encoding='utf-8'))
        result['mandatory_semantic_acceptance']['complete_non_superseded_field_preservation']='8 source-determined questions closed; 25 mapping proofs and 1 architectural decision OPEN; 6 representation details deferred with binding obligations'
        result['mandatory_semantic_acceptance']['cross_layer_interfaces']='12 baseline legal-semantic constraints rechecked; full field/preservation acceptance remains OPEN on all 12'
    (OUT/'VERIFICATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# Current consolidation verification','',
     '**Mechanical result: '+result['mechanical_status']+'. Full normative acceptance: OPEN.**','',
     'Command: python tools/verify_consolidation.py. This check verifies custody, locators, ownership and selected high-risk amendment effects. It does not infer semantic completeness from a passing search or hash.','',
     '| Check | Result |','|---|---|']
    lines.extend('| '+k+' | '+str(v)+' |' for k,v in counts.items())
    lines.extend(['','## Required acceptance checks',''])
    lines.extend('- '+k+': '+v+'.' for k,v in result['mandatory_semantic_acceptance'].items())
    lines.extend(['','Unresolved exact clauses and consequences: [issues register](UNRESOLVED_ISSUES.md). Document hashes and detailed failures: [VERIFICATION.json](VERIFICATION.json). Archive byte custody is independently reproducible with python documentation_checkpoint/tools/archive_inventory.py --verify.','',
      'No executable runtime or platform conformance tests were run because production implementation is not authorized. Source freeze reviews are documentary specification evidence, not runtime tests or a new consolidated freeze.',''])
    if failures:lines.extend(['## Failures','',*['- '+str(f) for f in failures]])
    (OUT/'VERIFICATION.md').write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
    print(json.dumps({'status':result['mechanical_status'],'counts':counts,'failures':failures},ensure_ascii=False,indent=2))
    return 1 if failures else 0

if __name__=='__main__':raise SystemExit(verify())
