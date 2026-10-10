"""Build the current documentation manifest from evidence; never freeze architecture."""
from collections import Counter
import json
from render_layer import ROOT, NAMES, DATA

SOURCES={
'L0':'FCA v1.0.1 foundation, authority/trust, Appendices C/F/G',
'L1':'FCA 48–51; RDMS-01 original + R1 and final freeze',
'L2':'FCA cognition; RDMS-02 original + C01/final; RDMS-08 original + C01/final',
'L3':'FCA action/evidence; RDMS-03 original + C01/final; RDMS-04 original + C01 + Review 02',
'L4':'FCA temporal/specialists; RDMS-05 original + C01 + FC05-01/02; RDMS-06 original + C01/final',
'L5':'FCA memory; RDMS-07 original + C01/final',
'L6':'FCA 52/53/82; RDMS-05 capsule/resume scopes; RDMS-09 original + C01 + C02 + C03 + FC09-04-01…04',
'L7':'FCA 85; RDMS-10 original + C01 + C02 + FC10-03-01…08'}

def make():
    out=ROOT/'reviews/canonical'
    summary=json.loads((out/'COVERAGE_SUMMARY.json').read_text(encoding='utf-8'))
    issues=json.loads((out/'UNRESOLVED_ISSUES.json').read_text(encoding='utf-8'))
    count=Counter(i['owner'] for i in issues)
    lines=['# Architecture manifest','',
     '**Current status: source-backed documentation consolidation for independent review; NOT FROZEN. Full normative acceptance is HOLD.**','',
     'The approved checkpoint is preserved at 397c9a5b8878ba5d5a8d8ab93a3e175146022f8d. The user subsequently approved source admission and L0–L7 ownership with the clarifications recorded in [AUTHORIZATION.md](../reviews/canonical/AUTHORIZATION.md). This approval authorizes documentation consolidation/publication only.','',
     '| Layer | Authoritative coverage and applied amendments | Completion status | Open contract questions |',
     '|---|---|---|---|']
    for layer,name in NAMES.items():
        status='Foundation responsibilities verified; owner imports remain governed by their own acceptance' if layer=='L0' else 'Current source scopes consolidated; full field/semantic acceptance remains OPEN'
        lines.append(f'| [{layer}]({name}.md) | {SOURCES[layer]} | {status} | {count[layer]} |')
    lines.extend(['','## Effective authority and ownership','',
     'L0 owns architectural foundation. Its cross-cutting law applies across all layers, while each layer owns its specific canonical responsibilities and record contracts. L1 owns control persistence and legal replay; L2 owns cognition and Executive semantic authorization; L3 owns actions, observations and evidence; L4 owns temporal evaluation, triggers, specialists, reactivation scheduling and the one dependency engine; L5 owns memory and learning; L6 owns recovery authority/state and suspension/resumption integrity; L7 owns integration/transport.','',
     'ResumptionCapsule and ResumeAssessment have exactly one owner, L6. L4 imports them for scheduling and temporal coordination. Commitment belongs to L2; L4 owns its referenced condition semantics. RDMS-05’s earlier competing Commitment declaration is withdrawn under C01-01, rather than promoted into another canonical entity. L7 can neither mint cognitive authority, commit authority nor external-action permission.','',
     'Canonical CapabilityResult is L2-owned; canonical MemoryRetrievalResult is L5-owned. CapabilityTransportResult and MemoryRetrievalTransportResult identify L7 transport envelopes whose archived RDMS-10 spelling is retained in provenance. These editorial distinctions do not ratify field conversion or authorize lost payload.','',
     'The [contract registry](../reviews/canonical/CANONICAL_CONTRACT_REGISTRY.json) records '+str(summary['registered_record_labels'])+' source record labels, including superseded declarations, partial specimens and transport aliases. That count is not a claim of '+str(summary['registered_record_labels'])+' complete canonical APIs. Every current label has one assigned owner; unresolved complete shapes are withheld from the accepted contract surface.','',
     '## Source integrity and precedence','',
     'All 195 archive files retain their checkpoint SHA-256, including the outer ZIP, nested packaging, originals, message export and historical GAIA artifacts. Read-only attributes and integrity verification provide custody evidence; they are not WORM storage. [Original-source manifest](../documentation_checkpoint/SOURCE_MANIFEST.json) and [message admission manifest](../documentation_checkpoint/SOURCE_UNITS.json) preserve exact file/message hashes.','',
     'FCA v1.0.1 supersedes FCA v1.0 and its admitted draft correction history. For each RDMS, the final source freeze admits the original plus approved corrections. A correction replaces only its stated scope. Later hardening supplements unaffected earlier duties. Final FC05, FC09 and FC10 interpretations are binding within those sources. GAIA reconciliations remain supporting evidence and introduce no law.','',
     'File SHA-256 uses exact archived bytes. Catalogue/unit hashes use UTF-8 clause text with LF line boundaries, excluding an appended synthetic final newline; they are not substituted for raw-file hashes.','',
     '## Verification evidence and acceptance limits','',
     f"Coverage indexes {summary['source_messages']} complete source messages, all {summary['fca_numbered_sections']} FCA numbered sections, {summary['fca_invariants']} invariants and {summary['fca_appendices']} appendices. The disposition ledger accounts for {summary['source_scope_units']} source scope units; {summary['residual_scope_units']} are unclassified residual scopes. A classified/cited scope is traceability evidence, not automatic sentence-level semantic proof.",'',
     'All twelve interface paths have owner/type, authority/transition, durability, failure/retry/recovery and rejection evidence. [Interface review](../reviews/canonical/INTERFACE_VALIDATION.md) and its JSON retain source fields and exact locators. None is declared fully accepted while owner-field/projection questions remain. Unspecified callable signatures are left unspecified.','',
     f"The [issues register](../reviews/canonical/UNRESOLVED_ISSUES.md) contains {summary['contract_issue_entries']} questions: {summary['record_shape_issues']} incomplete/differing record shapes, parent/projection conformance obligations, canonical-event envelope interpretation, changed hypothesis support-floor correspondence and two transport payload mappings. Exact conflicting/candidate clauses, field sets, line ranges, source hashes and consequences are preserved. Questions are bounded; independently verified laws remain effective.",'',
     'The [verification record](../reviews/canonical/VERIFICATION.md) separates mechanical PASS from semantic/field acceptance OPEN. [Clause trace](../reviews/canonical/CLAUSE_TRACEABILITY.json) and [source dispositions](../reviews/canonical/SOURCE_COVERAGE.json) provide bidirectional review evidence. No production code, new law, redesign, merge into main or new freeze is authorized.','',
     '## Reproduction','',
     'Run python tools/build_documents.py to regenerate documentation and evidence from the preserved originals. Run python tools/verify_consolidation.py for current checks. The older checkpoint verifier intentionally verifies Stage A only and must not be used as a current full-consolidation gate.','',
     'Git publication is restricted to docs/canonical-source-checkpoint. [Completion report](../reviews/canonical/COMPLETION_REPORT.md) records layer commits and publication evidence.',''])
    (ROOT/'architecture/ARCHITECTURE_MANIFEST.md').write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')

if __name__=='__main__':make()
