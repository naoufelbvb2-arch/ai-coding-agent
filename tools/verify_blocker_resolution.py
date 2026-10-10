"""Focused source and preservation checks for the targeted normative delta."""
from collections import Counter
import hashlib
import json
import re
import subprocess
from blocker_findings import CLASS_NAMES
from render_layer import ROOT, NAMES

OUT = ROOT/'reviews/canonical'
BASELINE = 'd50b7f88105b5397aa7d76e0bb8a1c2099a7c85e'


def baseline(path):
    return subprocess.check_output(['git', 'show', BASELINE+':'+path], cwd=ROOT).decode('utf-8')


def record(text, name):
    match = re.search(r'```text\n('+re.escape(name)+r' \{[\s\S]*?^\})\n```', text, re.M)
    return match.group(1) if match else ''


def members(raw):
    """Keep field spelling, optionality and body, not just a string occurrence."""
    matches = list(re.finditer(r'^    ([a-z]\w*)([^\n]*)', raw, re.M))
    return {m.group(1): raw[m.start():matches[i+1].start() if i+1<len(matches) else raw.rfind('}')].strip()
            for i, m in enumerate(matches)}


def values(raw, name):
    body = members(raw).get(name, '')
    return [v.strip().lower() for v in body.splitlines()[1:] if v.strip()]


def verify():
    errors, checks = [], []
    def check(name, ok, detail=None):
        checks.append(name)
        if not ok:
            errors.append({'check': name, 'detail': detail})
    rows = json.loads((OUT/'BLOCKER_CLASSIFICATION.json').read_text(encoding='utf-8'))
    indexed = {r['id']:r for r in rows}
    old = json.loads(baseline('reviews/canonical/UNRESOLVED_ISSUES.json'))
    check('all-40-questions-once', len(rows)==40 and len(indexed)==40 and set(indexed)=={r['id'] for r in old})
    for original in old:
        actual = indexed[original['id']]
        for k, v in original.items():
            if k != 'status':
                check('original-question-and-exact-candidates-preserved', actual[k]==v, (original['id'], k))
        check('original-status-preserved', actual['original_status']==original['status'], original['id'])
        review = actual['normative_review']
        check('one-permitted-classification', review['classification'] in CLASS_NAMES, original['id'])
        check('classification-reason-and-binding-obligations', all(review.get(k) for k in
            ['justification', 'binding_obligations', 'remaining_detail', 'source_evidence']), original['id'])
        if review['classification'] in 'ABE':
            check('normative-or-information-question-not-deferred', actual['status'].startswith('OPEN'), original['id'])
        if review['classification'] == 'C':
            check('implementation-design-deferral-explicit', actual['status']=='DEFERRED_TO_IMPLEMENTATION_DESIGN', original['id'])
        for e in review['source_evidence']:
            lines = (ROOT/e['source_path']).read_text(encoding='utf-8').splitlines()
            raw = '\n'.join(lines[e['start_line']-1:e['end_line']])
            check('exact-classification-source-clause-and-sha', raw==e['exact_clause'] and
                  hashlib.sha256(raw.encode('utf-8')).hexdigest()==e['sha256'], (original['id'], e['unit_id']))
        owner = (ROOT/'architecture'/(NAMES[actual['owner']]+'.md')).read_text(encoding='utf-8')
        check('owner-obligations-visible', review['binding_obligations'] in owner and
              review['remaining_detail'] in owner, original['id'])
    totals = Counter(r['normative_review']['classification'] for r in rows)
    check('classification-total-equals-40', sum(totals.values())==40)
    summary = json.loads((OUT/'BLOCKER_RESOLUTION_SUMMARY.json').read_text(encoding='utf-8'))
    check('summary-matches-register', summary['classification_totals']=={c:totals[c] for c in CLASS_NAMES})
    check('freeze-and-new-decision-not-claimed', summary['freeze_readiness']=='HOLD' and
          not summary['architecture_frozen'] and not summary['new_architectural_decision_adopted'])
    texts = {l:(ROOT/'architecture'/(n+'.md')).read_text(encoding='utf-8') for l,n in NAMES.items()}
    check('L0-byte-content-unchanged', texts['L0']==baseline('architecture/L0_FOUNDATION.md'))
    allowed = {r.get('type') for r in rows if r['normative_review']['classification'] in 'CD'}
    def unaffected(text):
        text = text.split('\n## Targeted normative reconciliation\n')[0].rstrip()
        for name in allowed:
            text = re.sub(r'^### '+re.escape(name)+r'\n[\s\S]*?(?=^### |^## |\Z)', '', text, flags=re.M)
        return text.rstrip()
    for l,n in NAMES.items():
        check('unrelated-owner-contracts-and-articles-unchanged', unaffected(texts[l])==unaffected(baseline('architecture/'+n+'.md')), l)
    declarations = {r['type']:r for r in json.loads((OUT/'CANONICAL_CONTRACT_REGISTRY.json').read_text(encoding='utf-8'))}
    # Three current contract corrections are checked against the immutable
    # clauses, not against the documentation writer's output.
    risk_question = indexed['SHAPE-Risk']
    native = next(d['raw'] for d in risk_question['exact_source_declarations'] if d['source_part']=='Original draft')
    amendment = next(d['raw'] for d in risk_question['exact_source_declarations'] if d['source_part']!='Original draft')
    risk = record(texts['L2'], 'Risk')
    rm, nm = members(risk), members(native)
    check('risk-all-unaffected-native-fields-exact', all(rm.get(k)==v for k,v in nm.items() if k!='status'))
    check('risk-exact-scoped-new-field-set', set(rm)==(set(nm)-{'status'})|{'lifecycle','treatment','current_assessment_ref'})
    check('risk-corrected-lifecycle-treatment-enums', values(risk,'lifecycle')==values(amendment,'lifecycle') and
          values(risk,'treatment')==values(amendment,'treatment') and 'status' not in rm)
    for name, l, issue in [('ContainmentProof','L3','SHAPE-ContainmentProof'), ('TriggerFire','L4','SHAPE-TriggerFire')]:
        approved = next(d for d in indexed[issue]['exact_source_declarations'] if d['source_part']=='C01')
        check('approved-native-record-exact', record(texts[l],name)==approved['raw'], name)
        check('registry-and-owner-record-agree', declarations[name]['effective_raw']==approved['raw'], name)
    check('risk-registry-matches-owner', declarations['Risk']['effective_raw']==risk)
    # Five existing owner elaborations are independently checked against the
    # parent/source requirements and their explicit scoped amendments.
    goal = record(texts['L2'], 'Goal')
    goal_parent = indexed['PARENT-Goal']['exact_source_declarations'][0]['raw']
    check('goal-preserves-original-lifecycle-and-adds-only-cancelled', set(values(goal,'status'))==set(values(goal_parent,'status'))|{'cancelled'})
    check('goal-priority-explicit-rename-and-cancellation-authority', 'declared_priority' in members(goal) and
          'priority' not in members(goal) and all(k in texts['L2'] for k in ['cancellation_reason','cancellation_authority_ref']))
    need = record(texts['L2'], 'InformationNeed')
    need_parent = indexed['PARENT-InformationNeed']['exact_source_declarations'][0]['raw']
    check('need-lifecycle-preserved', values(need,'status')==values(need_parent,'status'))
    check('need-retains-sources-blocks-and-typed-resolution', all(n in members(need) for n in
          ['question','importance','blocks','source_candidates','resolution_routes','resolution_ref']) and bool(record(texts['L2'],'ResolutionRef')))
    invariant = record(texts['L2'], 'Invariant')
    ip = indexed['PARENT-Invariant']['exact_source_declarations'][0]['raw']
    check('invariant-kind-severity-lifecycle-preserved', all(values(invariant,k)==values(ip,k) for k in ['kind','severity','status']))
    spec = record(texts['L2'],'EnforcementSpec')
    check('all-invariant-enforcement-modes-preserved', values(spec,'mode')==values(ip,'enforcement') and
          'enforcement_specs' in members(invariant) and 'enforcement_modes' not in members(invariant))
    check('invariant-version-and-enforcement-plan-retained', 'entity_version' in members(record(texts['L2'],'CanonicalEntityMeta')) and
          all(n in members(spec) for n in ['coverage_scope','fail_behavior','verifier_ref']))
    memory = record(texts['L5'],'MemoryProposal')
    check('memory-proposal-source-native-surface-unchanged', memory==declarations['MemoryProposal']['selected']['raw'])
    check('memory-preserves-all-source-expansion-categories', all(n in members(memory) for n in
          ['claim','proposed_scope','source_episode_refs','causal_basis_ref','applicability_conditions',
           'counter_conditions','counterexamples','evidence_refs','confidence_assessment_ref','proposed_maturity']))
    tv = indexed['PARENT-TemporalValidity']['exact_source_declarations']
    check('temporal-validity-source-difference-only-capitalization', tv[0]['raw'].lower()==tv[1]['raw'].lower())
    check('temporal-validity-current-source-record-preserved', record(texts['L4'],'TemporalValidity')==tv[1]['raw'])
    # Binding architectural duties for the corrected and deferred questions.
    containment = indexed['SHAPE-ContainmentProof']['normative_review']['binding_obligations']
    check('original-containment-properties-still-required', all(s in containment for s in
          ['filesystem isolation','shared writable mounts','dangerous credentials','mutating network','privileged paths','disposability']))
    check('fire-identity-frozen-and-replay-deduplicated', all(s in indexed['SHAPE-TriggerFire']['normative_review']['binding_obligations'] for s in
          ['trigger_id/generation/occurrence_key','same Fire','immutable condition/reaction identity']))
    check('CE-required-metadata-not-aliased-away', all(s in indexed['CE-01']['normative_review']['binding_obligations'] for s in
          ['event_id','schema_version','idempotency_key','event type/version','ordinal','payload']))
    check('HG-still-open-and-alternatives-not-adopted', indexed['HG-01']['status']=='OPEN_ARCHITECTURAL_DECISION' and
          len(indexed['HG-01']['normative_review']['decision_alternatives'])>=2 and 'neither alternative is adopted' in texts['L2'])
    interfaces = json.loads((OUT/'INTERFACE_VALIDATION.json').read_text(encoding='utf-8'))
    previous = json.loads(baseline('reviews/canonical/INTERFACE_VALIDATION.json'))
    check('all-12-interfaces-retained', [p['id'] for p in interfaces]==[p['id'] for p in previous] and len(interfaces)==12)
    for p, oldp in zip(interfaces, previous):
        for k in ['path','ownership','authority','atomicity_durability','failure_retry_recovery','rejection_conditions','source_units']:
            check('interface-legal-semantics-preserved', p[k]==oldp[k], (p['id'],k))
        delta = p.get('targeted_review', {})
        check('interface-acceptance-gap-not-hidden', bool(delta.get('open_issue_ids')) and
              delta.get('full_acceptance') is False, p['id'])
        check('interface-issue-identities-exist', all(ident in indexed for ident in delta.get('issue_ids',[])), p['id'])
    trace = json.loads((OUT/'CLAUSE_TRACEABILITY.json').read_text(encoding='utf-8'))
    for r in rows:
        ident = r['owner']+'-NR-'+r['id']
        matches = [c for c in trace if c['clause_id']==ident]
        check('one-source-trace-per-targeted-article', len(matches)==1, ident)
        if matches:
            c = matches[0]
            check('targeted-trace-line-correct', texts[r['owner']].splitlines()[c['line']-1]=='### '+ident, ident)
    result = {'status':'FAIL' if errors else 'PASS', 'checks_run':len(checks), 'failures':errors,
              'classification_totals':{c:totals[c] for c in CLASS_NAMES}, 'baseline':BASELINE,
              'limits':'Source/document regressions only; no runtime proof, complete mapping acceptance or new architectural decision.',
              'full_normative_acceptance':False, 'architecture_frozen':False}
    (OUT/'BLOCKER_REGRESSION_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(verify())
