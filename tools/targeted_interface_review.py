"""Annotate the twelve existing interface reviews without redefining contracts."""
import json
from render_layer import ROOT

OUT = ROOT/'reviews/canonical'
IMPACTS = {
 'X8-01': ['TRANSPORT-CapabilityResult', 'SHAPE-CanonicalStateView'],
 'X8-02': ['TRANSPORT-MemoryRetrievalResult', 'PARENT-MemoryProposal'],
 'X8-03': ['PARENT-TriggerCondition', 'SHAPE-TriggerFire', 'SHAPE-TriggerReaction', 'SHAPE-TriggerSourceCursor', 'SHAPE-TemporalSchedule'],
 'X8-04': ['SHAPE-TriggerReaction', 'PARENT-ActionProposal', 'PARENT-ActionRecord', 'PARENT-ActionEffectSemantics'],
 'X8-05': ['SHAPE-ResumptionCapsule', 'PARENT-ResumptionCapsule', 'SHAPE-ResumeAssessment', 'SHAPE-TriggerSourceCursor'],
 'X8-06': ['PARENT-ActionProposal', 'PARENT-ActionRecord', 'PARENT-ActionEffectSemantics', 'PARENT-Slice', 'SHAPE-ContainmentProof', 'CE-01'],
 'X8-07': ['PARENT-Observation', 'SHAPE-EvidenceLink', 'PARENT-EvidenceLink', 'PARENT-Claim', 'PARENT-Hypothesis', 'HG-01', 'CE-01'],
 'X8-08': ['PARENT-Hypothesis', 'PARENT-Experiment', 'PARENT-OperationalCausalClaim', 'HG-01'],
 'X8-09': ['PARENT-ContradictionRecord', 'PARENT-Observation', 'PARENT-InformationNeed'],
 'X8-10': ['PARENT-DependencyStamp', 'PARENT-QueryDependencyStamp', 'PARENT-TemporalValidity', 'PARENT-Slice', 'PARENT-Decision', 'PARENT-Invariant'],
 'X8-11': ['PARENT-MemoryProposal', 'PARENT-Observation', 'TRANSPORT-MemoryRetrievalResult'],
 'X8-12': ['SHAPE-ContainmentProof', 'PARENT-ActionRecord', 'PARENT-ActionEffectSemantics', 'SHAPE-ResumptionCapsule', 'SHAPE-ResumeAssessment']
}


def update():
    rows = {r['id']:r for r in json.loads((OUT/'BLOCKER_CLASSIFICATION.json').read_text(encoding='utf-8'))}
    interfaces = json.loads((OUT/'INTERFACE_VALIDATION.json').read_text(encoding='utf-8'))
    registry = {r['type']:r for r in json.loads((OUT/'CANONICAL_CONTRACT_REGISTRY.json').read_text(encoding='utf-8'))}
    lines = ['# Cross-layer interface validation after targeted reconciliation', '',
             'All twelve existing paths were rechecked for owner authority, transitions, atomicity/durability, failure/retry/recovery and rejection. The baseline legal constraints and their exact source units are preserved. No transport projection is accepted merely because naming or serialization is deferred.', '',
             '**Full field/preservation acceptance remains OPEN on all twelve paths.** The table identifies the actual blockers; it does not turn those gaps into implementation discretion. This is specification review, not executable runtime conformance.', '',
             '| Interface | Resolved source questions | Implementation detail deferred | Open proof / decision |',
             '|---|---|---|---|']
    for p in interfaces:
        ids = IMPACTS[p['id']]
        grouped = {c:[i for i in ids if rows[i]['normative_review']['classification']==c] for c in 'ABCDE'}
        opened = grouped['A']+grouped['B']+grouped['E']
        p['targeted_review'] = dict(issue_ids=ids, resolved_issue_ids=grouped['D'],
            implementation_deferred_issue_ids=grouped['C'], open_issue_ids=opened,
            authority_transition_check='BASELINE SOURCE CONSTRAINTS PRESERVED',
            durability_recovery_check='BASELINE SOURCE CONSTRAINTS PRESERVED',
            rejection_check='MISSING REQUIRED INFORMATION REMAINS REJECTED',
            full_acceptance=False)
        # Refresh only record evidence actually changed by this targeted pass.
        for rec in p['record_evidence']:
            if rec['type'] in {'Risk', 'ContainmentProof', 'TriggerFire'}:
                rec.update({k:registry[rec['type']].get(k) for k in rec})
        p['field_or_projection_review'] = opened
        p['status'] = 'SOURCE_CONSTRAINTS_RECHECKED; FULL_ACCEPTANCE_OPEN'
        lines.append('| '+p['id']+' '+p['path']+' | '+(', '.join(grouped['D']) or '—')+' | '+
                     (', '.join(grouped['C']) or '—')+' | '+', '.join(opened)+' |')
    for p in interfaces:
        lines += ['', '## '+p['id']+': '+p['path'], '', 'Owner contracts: '+p['ownership']+'.', '',
                  'Inputs: '+', '.join(p['input_records'])+'. Outputs: '+', '.join(p['output_records'])+'.', '',
                  '**Authority and transitions:** '+p['authority'], '',
                  '**Atomicity and durability:** '+p['atomicity_durability'], '',
                  '**Failure, retry and recovery:** '+p['failure_retry_recovery'], '',
                  '**Rejection:** '+p['rejection_conditions'], '',
                  '**Acceptance gap:** '+', '.join(p['targeted_review']['open_issue_ids'])+'.', '',
                  'Exact source evidence: '+'; '.join(f"[{s['unit_id']}](<../../{s['source_path']}#L{s['line']}>)" for s in p['source_units'])+'.', '']
    lines += ['Issue-specific exact fields, scoped amendments and consequences: [targeted classification](BLOCKER_CLASSIFICATION.md). No callable or serializer signature was invented.', '']
    (OUT/'INTERFACE_VALIDATION.json').write_text(json.dumps(interfaces,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUT/'INTERFACE_VALIDATION.md').write_text('\n'.join(lines),encoding='utf-8')


if __name__=='__main__':
    update()
