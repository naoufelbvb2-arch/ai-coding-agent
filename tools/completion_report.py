"""Record verified layer commits and precise acceptance limits."""
from collections import Counter
import json
import subprocess
from render_layer import ROOT, NAMES
from architecture_manifest import SOURCES

def make():
    git=lambda *args:subprocess.check_output(['git',*args],cwd=ROOT,text=True,encoding='utf-8').strip()
    receipt=ROOT/'.git/documentation-layer-commits.json'
    if not receipt.exists():receipt=ROOT/'reviews/canonical/LAYER_COMMITS.json'
    commits=json.loads(receipt.read_text(encoding='utf-8'))
    issues=json.loads((ROOT/'reviews/canonical/UNRESOLVED_ISSUES.json').read_text(encoding='utf-8'))
    summary=json.loads((ROOT/'reviews/canonical/COVERAGE_SUMMARY.json').read_text(encoding='utf-8'))
    counts=Counter(i['owner'] for i in issues)
    lines=['# Canonical documentation consolidation report','',
     '**All eight layer documents processed and committed separately. Mechanical verification PASS. Full normative completion remains OPEN; the consolidated architecture is NOT FROZEN.**','',
     'The approved source checkpoint commits remain ancestors of every consolidation commit. Initial checkpoint publication was verified at local and remote SHA 397c9a5b8878ba5d5a8d8ab93a3e175146022f8d. No production implementation, new architectural law, redesign or merge into main was performed.','',
     '## Layer completion and commits','',
     '| Layer | Verified consolidation scope | Remaining acceptance | Commit SHA |',
     '|---|---|---|---|']
    for c in commits:
        layer=c['layer']
        status='Foundation responsibilities verified against current FCA' if layer=='L0' else 'Source-backed duties, scoped amendments, owner contracts and imports consolidated'
        remaining='No local foundation record issue; imported owners retain their own gates' if layer=='L0' else str(counts[layer])+' exact shape/parent/interpretation questions; full acceptance OPEN'
        lines.append(f"| [{layer}](../../{c['document']}) | {status} | {remaining} | [{c['sha']}](https://github.com/naoufelbvb2-arch/ai-coding-agent/commit/{c['sha']}) |")
    lines.extend(['','## Authoritative coverage and amendment precedence','',
     'Coverage includes the exact FCA v1.0.1 file, all 88 numbered sections, all 50 invariant obligations, seven appendices, ten original RDMS messages and seventeen later correction/review messages. All 27 original message hashes and locators come from the preserved admission manifest. Historical GAIA outputs are supporting evidence only.','',
     '| Layer | Authoritative originals and applied amendment/final interpretation coverage |','|---|---|'])
    for l in NAMES:lines.append('| '+l+' | '+SOURCES[l]+' |')
    lines.extend(['',
     f"The source disposition ledger accounts for {summary['source_scope_units']} source units. It records {summary['scope_dispositions']['CURRENT_SCOPE_INCORPORATED']} directly incorporated scopes and {summary['scope_dispositions']['EXPLICIT_AMENDED_SCOPE_CROSSWALK']} explicitly amended baseline crosswalks, plus invariant, parent-field, historical and non-normative dispositions. There are zero unclassified residual scopes. Accounting is not a claim that every record conversion or full sentence-level semantic proof has passed.",'',
     'Explicit field replacements include the control-store/replay R1 model, entity concurrency/authority separation, single Commitment condition root with unaffected fields preserved, normalized lineage, independent SliceState dimensions, support assessments, observed-content trust metadata, pinned verification, advisory BLOCK_RECOMMENDED, EnforcementSpec and independent process launch dimensions. Superseded current record declarations are withheld; complete originals remain in the archive.','',
     'Final FC05-01/02 constrain generation supersession and late events after cancellation. FC09-04-01…04 constrain recovery scope, transient admission, external-effect uncertainty and honest continuation durability. FC10-03-01…08 constrain recoverability versus repetition, effective dispatch, trigger continuation, observation causality, actual disclosure, state-scoped completion and projection ownership.','',
     '## Verification results','',
     'python tools/verify_consolidation.py: PASS for archive integrity, exact source clause ranges, article provenance, unique record exports, selected amendment regressions, source/layer links and twelve-path obligation presence. The indexed evidence contains 195 preserved file hashes, 2,628 source-unit hashes/ranges, 1,615 article identities and 385 record definitions exported once under their assigned owners. All committed layer document bytes match their verified SHA-256 values.','',
     'The mandatory semantic gate remains OPEN for complete parent-field preservation, record-shape reconciliation, canonical event interpretation, hypothesis support-floor correspondence and lossless transport mapping. Mechanical PASS does not certify those questions. Source durability/recovery requirements are preserved as duties; no runtime, filesystem, sandbox, disaster recovery or deployment implementation was tested.','',
     'Commands and detailed results: [VERIFICATION.md](VERIFICATION.md), [VERIFICATION.json](VERIFICATION.json). Original-byte custody: python documentation_checkpoint/tools/archive_inventory.py --verify.','',
     '## Remaining source and architectural questions','',
     'There are 40 recorded questions: 13 record shapes, 23 parent/projection conformance questions, CE-01 canonical-event metadata interpretation, HG-01 changed hypothesis support-floor correspondence and two transport mappings. Candidate differences are not all declared legal contradictions. Each question retains exact source clauses/declarations, file paths, line ranges, hashes and the consequence of leaving it unresolved.','',
     'The 13 shapes are CanonicalStateView, ContainmentProof, EvidenceLink, ProjectRuntime, ResumeAssessment, ResumptionCapsule, Risk, State, TemporalSchedule, ToolResult, TriggerFire, TriggerReaction and TriggerSourceCursor. The archive retains all baseline fields; no abbreviated correction is treated as permission to delete unaffected data. Complete unresolved shapes are not exported as accepted implementations.','',
     'CE-01 preserves FCA canonical-event event_id/schema_version/idempotency_key and R1’s ControlEvent/event_type_version without inventing an enclosing-envelope alias. HG-01 preserves the duty to validate lifecycle/support coherence without inventing replacement thresholds for removed Hypothesis support values. L7 transport mappings cannot omit canonical capability payload or memory query/coverage/freshness metadata.','',
     'Exact questions and consequences: [UNRESOLVED_ISSUES.md](UNRESOLVED_ISSUES.md) and [UNRESOLVED_ISSUES.json](UNRESOLVED_ISSUES.json). Source classifications and clause-level disposition: [SOURCE_COVERAGE.json](SOURCE_COVERAGE.json). These questions bound acceptance of their own scopes; independently verified foundation, memory, temporal, control and action duties remain available for review.','',
     '## Cross-layer interface validation','',
     'All twelve paths were processed. Each has source-owned inputs/outputs, required field evidence, authority/transition constraints, atomicity/durability, failure/retry/recovery and explicit rejection conditions. Callable signatures and unprovided serialization bindings remain unspecified. None is represented as fully accepted while its field/projection proof remains open.','',
     '| Path | Status |','|---|---|'])
    for p in json.loads((ROOT/'reviews/canonical/INTERFACE_VALIDATION.json').read_text(encoding='utf-8')):
        lines.append('| '+p['id']+': '+p['path']+' | Constraints recorded; field/semantic acceptance OPEN |')
    lines.extend(['','See [INTERFACE_VALIDATION.md](INTERFACE_VALIDATION.md) and its [typed source evidence](INTERFACE_VALIDATION.json). Commitment is owned by L2, its temporal condition by L4, and capsule/resume integrity by L6. L7 retains integration-only authority.','',
     '## Publication and next review','',
     'Exact remote branch: refs/heads/docs/canonical-source-checkpoint in [naoufelbvb2-arch/ai-coding-agent](https://github.com/naoufelbvb2-arch/ai-coding-agent/tree/docs/canonical-source-checkpoint). The eight layer SHAs above identify the document changes. A subsequent evidence-report commit completes this report; its final remote SHA and local/remote equality are provided in the publication receipt and accompanying completion response.','',
     'Next step: independent review of the GitHub diffs, particularly the exact bounded source questions. Consolidated freeze and production implementation remain unauthorized.'])
    out=ROOT/'reviews/canonical'
    (out/'LAYER_COMMITS.json').write_text(json.dumps(commits,indent=2)+'\n',encoding='utf-8',newline='\n')
    (out/'COMPLETION_REPORT.md').write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'layers':len(commits),'layer_head':git('rev-parse','HEAD'),'questions':len(issues)}))

if __name__=='__main__':make()
