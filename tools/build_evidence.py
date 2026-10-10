"""Produce auditable source disposition and unresolved contract evidence."""
from collections import Counter
import hashlib
import json
import re
from render_layer import DATA, ROOT, NAMES, fca, message
from schema_selection import REGISTRY
from complete_fca_links import INVARIANT_OWNERS

OUT=ROOT/'reviews/canonical'
BASE_LAST={0:47,2:74,4:89,6:60,9:56,12:72,14:88,16:127,18:103,23:104}
AMEND_LAST={1:28,13:47,15:51,17:86,19:125,20:95,21:75,24:157,25:82}
SCOPES={
 0:{3:(1,[1,2]),4:(1,[5]),5:(1,[4]),6:(1,[10,11]),7:(1,[12]),8:(1,[12]),10:(1,[13]),12:(1,[1,2]),13:(1,[1,2]),14:(1,[18,19]),15:(1,[19,25]),16:(1,[19,20]),17:(1,[21]),18:(1,[21]),19:(1,[21]),20:(1,[22]),21:(1,[2]),22:(1,[16]),23:(1,[16]),24:(1,[7]),27:(1,[23]),29:(13,[22,23]),38:(1,[14,15]),39:(1,[14,15]),40:(1,[15]),41:(1,[3,25]),43:(1,[24,25]),44:(1,[24]),46:(1,[28])},
 2:{2:(3,[1]),5:(3,[2,4,5,6]),8:(3,[2]),9:(3,[19]),14:(3,[2,7,20]),15:(3,[2,7]),17:(3,[8]),21:(3,[8]),22:(3,[11,14]),23:(3,[12]),24:(3,[9]),28:(3,[10]),29:(3,[10]),31:(3,[26]),32:(3,[26]),35:(3,[15,16]),39:(3,[28,29]),40:(3,[28,29]),45:(3,[17]),46:(3,[30,31]),47:(3,[30,31]),48:(3,[21,25]),51:(3,[21]),55:(3,[23]),56:(3,[32]),57:(3,[32]),60:(3,[27]),63:(3,[1,15,21,27,30]),74:(3,[35])},
 4:{3:(5,[1,6,15,21]),8:(5,[1,2]),9:(5,[3,4,5]),10:(5,[2]),11:(5,[6]),17:(5,[7,8]),18:(5,[9]),20:(5,[10,11,12,13]),23:(5,[10,11,12]),26:(5,[4,5]),30:(5,[20]),42:(5,[23,24,25,26]),44:(5,[25,27,29,30,31,32]),52:(5,[35,36,37]),54:(5,[38,39,40]),56:(5,[43,44]),57:(5,[43,44]),89:(5,[48])},
 6:{9:(7,[4]),13:(7,[11]),20:(7,[17,39]),21:(7,[16,17]),39:(7,[36])},
 9:{5:(10,[24,25,26,27,28]),18:(10,[5]),19:(10,[5,6]),21:(10,[13,14]),22:(10,[13,14]),23:(10,[15,29,30,31,32]),24:(10,[15,32]),25:(10,[1])},
 16:{101:(17,[72,73,74,75])},
 23:{54:(24,[3,6,7,8,10])}
}
NUM_C01={3,5,7,10}

def units(order,numbers):
    result=[]
    for n in numbers:
        prefix=f'C01-{n:02d} ' if order in NUM_C01 else str(n)+'. '
        result.append(next(s['unit_id'] for s in message(order)['segments'] if s['heading'].startswith(prefix)))
    return result

def fields(raw):
    if not raw:return []
    return [m.group(1) for line in raw.splitlines() if (m:=re.match(r'^    ([a-zA-Z_]\w*)(?:\??(?:\[\])?\??)(?::|\s*$)',line))]

def dump(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

def build():
    texts={layer:(ROOT/'architecture'/(name+'.md')).read_text(encoding='utf-8') for layer,name in NAMES.items()}
    clauses=[]
    for layer,text in texts.items():
        starts=list(re.finditer(r'^### (L[0-7]-[A-Za-z0-9_-]+)(?:[^\n]*)\n',text,re.M))
        for i,m in enumerate(starts):
            end=starts[i+1].start() if i+1<len(starts) else len(text)
            body=text[m.start():end]
            # Schema section starts after the last article; do not attach it to the article.
            boundary=re.search(r'^## ',body[m.end()-m.start():],re.M)
            if boundary:end=m.end()+boundary.start()
            body=text[m.start():end]
            sources=re.findall(r'\[(FCA-(?:\d+(?:\.\d+)?|APP-[A-G])|RDMS-\d+-M\d+-U\d+)\]',body)
            clauses.append({'clause_id':m.group(1),'owner':layer,'document':'architecture/'+NAMES[layer]+'.md',
                            'line':text[:m.start()].count('\n')+1,'source_unit_ids':sorted(set(sources)),
                            'article_sha256':hashlib.sha256(body.encode('utf-8')).hexdigest()})
    by_unit={}
    for c in clauses:
        for ident in c['source_unit_ids']:by_unit.setdefault(ident,[]).append(c['clause_id'])
    coverage=[]
    for m in DATA['messages']:
        seen=set()
        for s in m['segments']:
            record={k:s[k] for k in ['unit_id','heading','sha256','bundle_start_line','bundle_end_line']}
            record.update({'specification':m['specification'],'source_part':m['part'],'source_path':m['source_path'],'owner':m['owner'],'canonical_clauses':by_unit.get(s['unit_id'],[])})
            match=re.match(r'^(\d+)\. ',s['heading'])
            number=int(match.group(1)) if match else None
            if m['order'] in {9,10}:
                capnum=re.match(r'C01-(\d+)',s['heading'])
                n=int(capnum.group(1)) if capnum else number
                if (m['order']==9 and n in range(31,38)) or (m['order']==10 and n in range(34,42)):
                    record['owner']='L6'
            if record['canonical_clauses']:
                record['disposition']='CURRENT_SCOPE_INCORPORATED'
            elif m['order'] in SCOPES and number in SCOPES[m['order']]:
                dest,nums=SCOPES[m['order']][number]
                record['disposition']='EXPLICIT_AMENDED_SCOPE_CROSSWALK'
                record['effective_source_units']=units(dest,nums)
                record['canonical_clauses']=sorted({c for u in record['effective_source_units'] for c in by_unit.get(u,[])})
                record['scope_warning']='Only the cited replacement scope is admitted; residual field obligations remain subject to contract issues.'
            elif 'Finding' in s['heading'] or number in seen or number and number>BASE_LAST.get(m['order'],AMEND_LAST.get(m['order'],0)):
                record['disposition']='HISTORICAL_REVIEW_OR_NON_NORMATIVE_CONTEXT'
            elif re.match(r'^(?:T\d+|Test \d+|PART|Part|Additional Attack|One Remaining)',s['heading']):
                record['disposition']='REVIEW_OR_SECTION_STRUCTURE_RETAINED_IN_ARCHIVE'
            elif 'Example' in s['heading'] or s['heading'].startswith(('1. Purpose','1. Objective','47. What RDMS-01 Has Frozen Conceptually')):
                record['disposition']='EXPLANATORY_CONTEXT_RETAINED_IN_ARCHIVE'
            else:
                record['disposition']='RESIDUAL_SCOPE_REQUIRES_RECONCILIATION'
                record['exact_clause']=s['raw']
            if number is not None:seen.add(number)
            coverage.append(record)
    proposal=json.loads((ROOT/'documentation_checkpoint/FCA_SECTION_OWNERSHIP_PROPOSAL.json').read_text(encoding='utf-8'))
    owners={s['section']:s['proposed_owner'] for s in proposal['sections']}
    owners.update({'53':'L6','82':'L6'})
    for s in DATA['fca_sections']+DATA['fca_appendices']:
        disposition='CURRENT_SCOPE_INCORPORATED' if by_unit.get(s['unit_id']) else 'HISTORICAL_OR_NON_NORMATIVE_APPENDIX'
        owner=owners.get(s['section'],'L2' if s['section']=='D' else 'L0')
        if s['section']=='86':disposition='SOURCE_FREEZE_EVIDENCE_ONLY'
        if s['section']=='D':disposition='COMPOSITE_VIEW; EFFECTIVE_OWNER_RECORDS_AND_OPEN_FIELD_RECONCILIATION'
        targets={'8':['L2-E03','L2-E20'],'15':['L2-E05','L2-E06'],'17':['L2-E07','L2-E08'],'29':['L2-E11','L2-E12']}
        if s['section'] in targets:
            disposition='PARENT_ENTITY_SCOPE_CROSSWALK; FIELD_CONFORMANCE_OPEN'
        coverage.append({k:s[k] for k in ['unit_id','sha256','start_line','end_line','source_path']}|
                        {'owner':owner,'disposition':disposition,'canonical_clauses':targets.get(s['section'],by_unit.get(s['unit_id'],[]))})
    for inv in DATA['fca_invariants']:
        n=int(inv['unit_id'].split('I')[1])
        owner=next(l for l,ns in INVARIANT_OWNERS.items() if n in ns)
        coverage.append({k:inv[k] for k in ['unit_id','sha256','start_line','source_path']}|
                        {'owner':owner,'disposition':'CURRENT_INVARIANT_INCORPORATED','canonical_document':'architecture/'+NAMES[owner]+'.md'})
    registry=[]
    issues=[]
    for r in REGISTRY:
        r={**r,'current_top_level_fields':fields(r['effective_raw'])}
        registry.append(r)
        if r['status'].startswith(('PARTIAL','MULTIPLE','UNSPECIFIED')):
            issue={'id':'SHAPE-'+r['type'],'owner':r['owner'],'type':r['type'],'status':'OPEN',
                   'question':r['status'],'exact_source_declarations':r['candidates'],
                   'scoped_amendments':r['explicit_overlays'],'associated_contracts':r.get('associated_contracts',[]),
                   'consequence':'No complete serializer or conversion is accepted. Independently specified semantic laws remain effective.'}
            issue['field_variance']=[{'source':c['specification']+' / '+c['source_part'],'line':c['bundle_start_line'],'fields':fields(c['raw'])} for c in r['candidates']]
            issues.append(issue)
        if r['parent_or_projection_variance'] and len({c['specification'] for c in r['candidates']})>1 and r['status']!='SUPERSEDED_HISTORICAL_DECLARATION' and not r.get('parent_conformance_disposition'):
            issues.append({'id':'PARENT-'+r['type'],'owner':r['owner'],'type':r['type'],'status':'OPEN_CONFORMANCE_PROOF',
              'question':'Preserve all non-superseded parent semantic fields; a rename, aggregate reference or projection is not by itself a proved mapping.',
              'exact_source_declarations':r['candidates'],'scoped_amendments':r['explicit_overlays'],
              'consequence':'Current source-owned records retain their defining semantics; callers cannot assume a lossless inter-specification mapping.'})
    for ident,a,b,question in [
     ('CE-01',fca(48),next(s for s in message(1)['segments'] if s['heading'].startswith('10. ')),'Canonical event schema_version/idempotency_key versus R1 ControlEvent/event_type_version and enclosing ControlCommit.'),
     ('HG-01',next(s for s in message(2)['segments'] if s['heading'].startswith('15. ')),next(s for s in message(3)['segments'] if s['heading'].startswith('C01-02 ')),'Baseline confirmed/rejected support-floor combinations use removed Hypothesis support values; C01 introduces different SupportAssessment levels without an explicit complete threshold crosswalk.')]:
        aa={**a,'source_path':a.get('source_path',message(2)['source_path'])}
        bb={**b,'source_path':message(1 if ident=='CE-01' else 3)['source_path']}
        issues.append({'id':ident,'owner':'L1' if ident=='CE-01' else 'L2','status':'OPEN','question':question,'exact_conflicting_scopes':[aa,bb],
                       'consequence':'Preserve both non-superseded semantic requirements; do not invent a field alias or assessment threshold.'})
    for alias,canonical in [('CapabilityTransportResult','CapabilityResult'),('MemoryRetrievalTransportResult','MemoryRetrievalResult')]:
        a=next(r for r in registry if r['type']==canonical)
        b=next(r for r in registry if r['type']==alias)
        issues.append({'id':'TRANSPORT-'+canonical,'owner':'L7','status':'OPEN','question':'Exact canonical payload/reference preservation and field conversion are not frozen by an editorial alias.',
          'canonical_source':a['selected'],'transport_source':b['selected'],
          'canonical_fields':a['current_top_level_fields'],'transport_fields':b['current_top_level_fields'],
          'consequence':'Reject lossy conversion; carry source-owned meaning and provenance. Do not assert a fabricated callable signature.'})
    residual=[r for r in coverage if r['disposition']=='RESIDUAL_SCOPE_REQUIRES_RECONCILIATION']
    dump('CLAUSE_TRACEABILITY.json',clauses)
    dump('CANONICAL_CONTRACT_REGISTRY.json',registry)
    dump('SOURCE_COVERAGE.json',coverage)
    dump('UNRESOLVED_ISSUES.json',issues)
    summary={'archive_files':195,'source_messages':27,'fca_numbered_sections':88,'fca_appendices':7,'fca_invariants':50,
             'source_scope_units':len(coverage),'canonical_articles':len(clauses),'registered_record_labels':len(registry),
             'scope_dispositions':dict(Counter(c['disposition'] for c in coverage)),
             'residual_scope_units':len(residual),'contract_issue_entries':len(issues),
             'record_shape_issues':sum(i['id'].startswith('SHAPE-') for i in issues),'interface_paths_processed':12,
             'fully_accepted_interface_paths':0,'full_normative_completion':False}
    dump('COVERAGE_SUMMARY.json',summary)
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    print('Residual scope headings: '+str([(r['specification'],r['source_part'],r['heading']) for r in residual]))
    lines=['# Unresolved source and contract questions','',
      'Checkpoint publication and ownership approval are resolved. These are consolidation questions, not permission to create new fields, transitions or authority. Full normative acceptance remains HOLD.','',
      '| ID | Owner | Exact question / consequence |','|---|---|---|']
    for i in issues:
        lines.append('| '+i['id']+' | '+i['owner']+' | '+i['question']+' '+i['consequence']+' |')
    lines.extend(['','Exact candidate text, source paths, line ranges and hashes are in [UNRESOLVED_ISSUES.json](UNRESOLVED_ISSUES.json). Distinct candidates are evidence of a reconciliation obligation, not proof that every difference is a legal contradiction.','',
     'Residual source scopes not yet admitted as completely reconciled are recorded individually, with exact original text, in [SOURCE_COVERAGE.json](SOURCE_COVERAGE.json). Source presence is not semantic proof.',''])
    for r in residual:
        lines.append('- '+r['unit_id']+': '+r['heading']+'; owner '+r['owner']+'.')
    (OUT/'UNRESOLVED_ISSUES.md').write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
    return summary

if __name__=='__main__':build()
