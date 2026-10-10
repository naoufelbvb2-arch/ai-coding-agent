"""Record targeted review evidence and focused commits; no layer regeneration."""
from collections import Counter
import hashlib
import json
import subprocess
from render_layer import ROOT, NAMES

OUT=ROOT/'reviews/canonical'
BASELINE='d50b7f88105b5397aa7d76e0bb8a1c2099a7c85e'
BRANCH='docs/canonical-source-checkpoint'


def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8').strip()


def report():
    summary=json.loads((OUT/'BLOCKER_RESOLUTION_SUMMARY.json').read_text(encoding='utf-8'))
    rows=json.loads((OUT/'BLOCKER_CLASSIFICATION.json').read_text(encoding='utf-8'))
    verification=json.loads((OUT/'VERIFICATION.json').read_text(encoding='utf-8'))
    regression=json.loads((OUT/'BLOCKER_REGRESSION_RESULTS.json').read_text(encoding='utf-8'))
    commits=[]
    for line in git('log','--reverse','--format=%H%x09%s',BASELINE+'..HEAD').splitlines():
        sha,subject=line.split('\t',1)
        files=git('diff-tree','--no-commit-id','--name-only','-r',sha).splitlines()
        commits.append(dict(sha=sha,subject=subject,files=files))
    (OUT/'TARGETED_COMMITS.json').write_text(json.dumps(commits,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    modified=sorted(set(git('diff','--name-only',BASELINE).splitlines())|
                    set(git('ls-files','--others','--exclude-standard').splitlines())|
                    {'reviews/canonical/BLOCKER_RESOLUTION_REPORT.md','reviews/canonical/TARGETED_COMMITS.json'})
    counts=summary['classification_totals']
    opened=Counter(r['owner'] for r in rows if r['normative_review']['is_freeze_blocker'])
    lines=['# Targeted normative blocker resolution report','',
           'Repository: naoufelbvb2-arch/ai-coding-agent. Branch: `'+BRANCH+'`. Reviewed baseline: `'+BASELINE+'`.', '',
           '**Freeze readiness: HOLD. NOT FROZEN.** The existing consolidated layer documents remain the working baseline; only targeted owner contracts, dispositions and related review evidence changed. No new architectural decision was adopted.', '',
           'Original unresolved questions: **40**. Exactly one final classification is assigned to each question.', '',
           '| Class | Meaning | Count | Final disposition |','|---|---|---|---|']
    names={'A':'NORMATIVE_CONFLICT','B':'LOSSLESS_MAPPING_REQUIRED','C':'IMPLEMENTATION_DETAIL_DEFERRED','D':'ALREADY_RESOLVED','E':'EXPLICIT_ARCHITECTURAL_DECISION_REQUIRED'}
    dispositions={'A':'No mutually impossible effective pair established','B':'Preservation proof still OPEN','C':'Deferred to Implementation Design with binding obligations','D':'Source-determined resolution / existing owner elaboration proven','E':'Architecture review approval required; no decision selected'}
    lines += ['| '+c+' | '+names[c]+' | '+str(counts[c])+' | '+dispositions[c]+' |' for c in names]
    lines += ['', '**Total: 40.** Eight questions are resolved/proven (three current-record corrections and five already effective elaborations); six representation details are safely deferred; 26 questions remain open (25 mapping proofs and one required decision). Zero A is not a claim that the B/E requirements are optional.', '',
              '## Proven corrections and closures','',
              '- Current record corrections: SHAPE-Risk, SHAPE-ContainmentProof, SHAPE-TriggerFire.',
              '- Existing source determinations proven: PARENT-Goal, PARENT-InformationNeed, PARENT-Invariant, PARENT-MemoryProposal, PARENT-TemporalValidity.',
              '- Implementation Design deferrals: SHAPE-CanonicalStateView, SHAPE-State, SHAPE-ProjectRuntime, SHAPE-EvidenceLink, SHAPE-ToolResult, SHAPE-TriggerSourceCursor.', '',
              'Every question retains its original candidates, exact authoritative clauses, hashes, classification reason, mandatory obligations and remaining detail in [the classification register](BLOCKER_CLASSIFICATION.md) and [JSON](BLOCKER_CLASSIFICATION.json). The [eight preservation proofs](SOURCE_DETERMINATE_PROOFS.md) explain why class D closes the normative question. Deferral concerns only the stated layout/encoding/view detail; required information, identity, authority, lifecycle, durability and recovery remain binding.', '',
              '## Remaining legal-information gaps and required decision','',
              'The 25 class B questions are source-compatible representation/preservation questions, not automatically contradictory laws or approval requests for new laws. Specific missing proofs include action risk/world/authority/history information, inline-spec/reference content and versions, parent evidence/decision fields, complete capsule context and resume action coverage, schedule instants/bounds, reaction keys/kinds, canonical-event metadata scope and both transport payloads. They remain acceptance gaps; no serializer alias or lossy projection is invented.', '',
              '**HG-01 requires an approved architectural decision.** RDMS-02 original §15 uses the old support combinations for CONFIRMED/REJECTED. C01-02 replaces scalar support with a different immutable SupportAssessment vocabulary; C01-07 and RDMS-03 C01-42 settle the separate OVC closure path. The missing ordinary hypothesis admission correspondence cannot be chosen by a serialization library.', '',
              'Smallest decision: ratify the post-C01 SupportAssessment predicates for ordinary CONFIRMED/REJECTED, including assessment validity and whether VERIFIED satisfies the earlier STRONG minimum. Available resolution approaches are a minimal shared-level admission rule or a complete legacy-to-assessment correspondence. Both must retain the original support-floor obligations and the independent causal gate; neither is adopted. The register includes exact missing/conflicting scopes and consequences. Affected layers: L2, L3, L1; interfaces X8-07/X8-08.', '',
              '## Layer and interface impact','',
              '| Layer | Open proof / decision questions |','|---|---|']
    lines += ['| '+l+' | '+str(opened[l])+' |' for l in NAMES]
    lines += ['', 'L0 is unchanged. L1–L7 contain only their own targeted reconciliation articles and affected contract-section edits. No unrelated current normative article or owner contract changed; the focused checker compares them with the reviewed Git baseline.', '',
              'All twelve interface paths were rechecked against their existing source-backed authority/transition, durability/atomicity, failure/retry/recovery and rejection constraints. Those constraints remain unchanged. Resolved source contracts and deferred layout details are distinguished from the specific B/E blockers in [the interface review](INTERFACE_VALIDATION.md). **All twelve still have full field/preservation acceptance OPEN.** No runtime conformance claim is made.', '',
              '## Verification','',
              '- Existing consolidation verifier: '+verification['mechanical_status']+'. Original archive files: '+str(verification['counts']['archive_files'])+'; source units: '+str(verification['counts']['catalogued_source_units'])+'; source-backed articles: '+str(verification['counts']['source_backed_articles'])+'; single-owner current definitions: '+str(verification['counts']['single_owner_exported_record_definitions'])+'.',
              '- Focused blocker regression verifier: '+regression['status']+'; '+str(regression['checks_run'])+' checks, '+str(len(regression['failures']))+' failures.',
              '- Checks include all 40 original questions/candidates preserved, exact evidence clause/hash equality, only permitted owner edits, exact amended fields, unaffected Risk field bodies/optionality, retained Goal/Need/Invariant values, source-native MemoryProposal, capitalization-only TemporalValidity, unresolved HG/metadata gates and all 12 unchanged legal interface constraints.',
              '- Source catalogue, all 27 authoritative messages, FCA sections/invariants and amendment sources retain their original custody; archive bytes are unchanged. Verification hashes in VERIFICATION.json describe the current documents; LAYER_COMMITS.json retains historical baseline hashes.',
              '- No production code or executable runtime tests. Mechanical/source regression PASS does not certify complete field mapping, backend durability, operational authorization or architecture freeze.', '',
              'Commands: `python tools/verify_consolidation.py` and `python tools/verify_blocker_resolution.py`. Full regeneration is disabled after targeted reconciliation. [Detailed regression evidence](BLOCKER_REGRESSION_RESULTS.json); [current verification evidence](VERIFICATION.json).', '',
              '## Focused commits','', '| Commit SHA | Change |','|---|---|']
    lines += ['| `'+c['sha']+'` | '+c['subject']+' |' for c in commits]
    if not commits:
        lines += ['| Pending local commit | Reviewed edits prepared; no publication claimed by this draft |']
    lines += ['', '[TARGETED_COMMITS.json](TARGETED_COMMITS.json) lists exact files for the recorded focused commits. The final evidence/publication commit cannot record its own SHA without changing that SHA; the exact final remote/local SHA is supplied in the accompanying completion response and local Git publication receipt.', '',
              '## Exact modified files','']
    lines += ['- `'+p+'`' for p in modified]
    lines += ['', '## Publication boundary','',
              'Publish only to `refs/heads/'+BRANCH+'`, preserving the reviewed baseline and source checkpoint history. Verify remote/local head equality and a clean tree after the push. No merge into main, history rewrite, source edit, production implementation, new law or FROZEN declaration is authorized. Publication equality is confirmed by the final response/receipt rather than inferred from this pre-publication report.', '']
    (OUT/'BLOCKER_RESOLUTION_REPORT.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({'recorded_commits':len(commits),'modified_files':len(modified),'classification_total':sum(counts.values())}))


if __name__=='__main__':
    report()
