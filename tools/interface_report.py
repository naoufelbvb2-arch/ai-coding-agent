"""Documentation-level interface constraint evidence; no fabricated signatures."""
import json
from render_layer import ROOT, DATA, NAMES, fca, message, source_link
from schema_selection import REGISTRY

PATHS=[
('X8-01','L2 → L7 → L2','L2 canonical capability meaning / L7 transport',
 ['CapabilityInvocation'],['CapabilityResult','CapabilityTransportResult'],
 'Executive consumes proposals; L7 cannot issue cognitive or action permission.',
 'No canonical state transition follows delivery alone. Owner-authorized adoption enters L1 ControlTransaction.',
 'Provider timeout, malformed output or old epoch yields rejection/revalidation; retries are invocation delivery and never automatic tool redispatch.',
 'Reject omitted canonical payload, forged authority, stale dependencies or any unproved lossy transport conversion.',
 [(23,'9. '),(24,'7. '),(26,'FC10-03-08')],[23]),
('X8-02','L5 → L7 → L2','L5 canonical retrieval / L7 transport',
 ['MemoryQuery','MemoryRetrievalRequest'],['MemoryRetrievalResult','MemoryRetrievalTransportResult'],
 'Retrieval supplies precedent; only Executive can adopt current guidance, and LearningGate governs promotion.',
 'Memory revisions use L1 durability; transport cannot replace retrieval coverage, query identity or canonical version.',
 'Provider/index failure reports partial/unknown coverage; absent search results do not prove absence.',
 'Reject missing trust/provenance/coverage, unauthorized cross-project disclosure or lossy result mapping.',
 [(14,'57. '),(15,'17. '),(15,'20. '),(23,'37. '),(26,'FC10-03-08')],[62]),
('X8-03','L2 → L4 → L1','L2 Commitment / L4 condition and processing',
 ['Commitment','TriggerCondition'],['TriggerEvaluation','TriggerFire','TriggerReaction'],
 'Executive owns Commitment transitions. L4 may evaluate frozen temporal predicates and apply only the declared reaction authority.',
 'Preserve one condition root, inbox/processing separation and atomic fire/reaction target mutation. Detection may repeat; canonical application deduplicates.',
 'Replayable sources and qualified occurrence identity govern replay; UNKNOWN coverage cannot assert a missed edge or absence.',
 'Reject unbound temporal commitment, incoherent composite input, changed frozen definition, duplicate effect or invalid target version.',
 [(3,'C01-32 '),(10,'C01-01 '),(10,'C01-06 '),(10,'C01-14 '),(10,'C01-30 ')],[55,56]),
('X8-04','L4 → L1 → L3','L4 temporal reaction / L3 action authority',
 ['TriggerReaction','TriggerDerivedWorkCommitment'],['ActionProposal','ActionAuthorization','ActionRecord'],
 'Trigger reaction may commit continuation work; it never authorizes ActionProposal or dispatch independently.',
 'Reaction/continuation is atomic where required. Dispatch needs ActionGate, durable intent, legal ownership and trusted executor fencing.',
 'Reaction replay deduplicates. Action delivery recovery enumerates obligations; external retry follows L3 effect semantics.',
 'Reject obsolete generation, cancelled target, orphaned obligation, missing durable dispatch intent or reused unsafe authorization.',
 [(10,'C01-29 '),(11,'2. Final '),(25,'16. '),(25,'17. '),(26,'FC10-03-04')],[45]),
('X8-05','L4 → L6 → L1','L6 capsule, suspension and resume integrity / L4 scheduling',
 ['ResumptionCapsule','WorkReactivationBinding'],['ResumeAssessment','RecoveryAdmissionBinding'],
 'L6 owns admission/integrity; L4 schedules detection and reactivation. Executive must reassess resumed cognition.',
 'Durable capsule bytes/hash precede atomic suspension metadata and legal recovery continuation. Cursor advancement cannot outrun required durable reaction.',
 'Missing/corrupt capsule or unresolved action blocks resume. Persistence failure cannot be reported as guaranteed automatic recovery.',
 'Reject corrupt/missing payload, stale check at commit, unproved action outcome or expanded recovery scope.',
 [(10,'C01-34 '),(10,'C01-35 '),(10,'C01-37 '),(10,'C01-40 '),(21,'62. '),(22,'FC09-04-04')],[52,53,82]),
('X8-06','L2 → L3 → L1','L3 world action / L2 Executive / L1 durability',
 ['Slice','ActionProposal'],['ActionAuthorization','ActionRecord','ControlCommit'],
 'Current Executive supplies semantic authorization; ActionGate validates legal scope and effect; control persistence grants no independent permission.',
 'Compare expected state/resources, commit dispatch ownership, persist acknowledged recoverable intent, validate effective execution at last enforceable boundary, then dispatch.',
 'Before possible dispatch, revoke/revalidate. At intent or later, preserve unknown effects and reconcile; compensation is a new authorized action.',
 'Reject stale epoch, failed expected-version check, altered effective operation, unknown containment or missing recoverable durability.',
 [(7,'C01-04 '),(7,'C01-05 '),(24,'44. '),(25,'25. '),(25,'34. ')],[41,42,45,49]),
('X8-07','L3 → L2 → L1','L3 observation/evidence / L2 epistemic adoption',
 ['Observation','EvidenceLink','SupportAssessment'],['Claim','Hypothesis','CanonicalMutation'],
 'Trusted Observation Ingress captures reality without Executive semantic inference. Executive authorizes interpretation/adoption under grounding law.',
 'Observation append has legal commit ordering; historical capture and accepted evidence are immutable. Source causality is not inferred from arrival.',
 'Duplicate capture retains origin lineage. Missing causal parent may allow raw capture while causal attachment remains pending.',
 'Reject model-fabricated observation, semantic capture deletion, unsupported evidence root, wrapper inflation or forged source/authority metadata.',
 [(5,'C01-01 '),(5,'C01-07 '),(5,'C01-10 '),(5,'C01-19 '),(25,'51. '),(26,'FC10-03-05')],[7,11,12,76]),
('X8-08','L2 → L3 → L2','L2 hypothesis/causal entities / L3 experimental evidence',
 ['Hypothesis','Experiment','ExperimentDesignSnapshot'],['ExperimentRun','PredictionEvaluation','CausalVerificationRecord','OperationalCausalClaim'],
 'Executive approves experiments and causal adoption; mutating experiment steps separately obey ActionGate.',
 'Prediction freeze, authorized design snapshot and experiment authorization are atomic. Every run pins exact design and relevant execution context.',
 'Execution failure differs from falsified prediction. Nonconforming or unresolved required effects cannot close the intended experiment.',
 'Reject post-result prediction rewriting, current-experiment-only run binding, causal truth from simulation or COMPLETED alone.',
 [(3,'C01-07 '),(5,'C01-23 '),(5,'C01-24 '),(5,'C01-31 '),(5,'C01-33 '),(5,'C01-42 ')],[40,74]),
('X8-09','L3 → L2','L3 comparison record / L2 causal proposition',
 ['ContradictionRecord','Observation'],['InformationNeed','Hypothesis','Claim'],
 'A contradiction record compares scoped observations; causal explanation belongs to a typed proposition or deterministic result adopted under Executive authority.',
 'Preserve conflicting observations and comparison provenance; lifecycle changes cannot erase historical capture.',
 'Resolve dimensions such as time/input/environment before interpretation; unknown comparability requires acquisition rather than invented cause.',
 'Reject hidden root-cause truth in dimension_analysis or inconvenient observation invalidation.',
 [(5,'C01-08 '),(5,'C01-20 '),(5,'C01-21 ')],[13]),
('X8-10','L4 → L2 → L1','L4 freshness / L2 adoption and finalization',
 ['DependencySet','DependencyEvaluation','ReadinessSnapshot'],['CognitiveControlDecision','CompletionStateBinding','CanonicalMutation'],
 'One dependency engine reports freshness. Executive owns adoption/completion; estimates and compatibility claims cannot self-authorize transitions.',
 'Use coherent dependency universe, transitive lineage and commit-time recheck of affected state. Completion is atomically bound to evidence-covered state.',
 'Unrelated repository changes need not invalidate valid scoped knowledge. Incomplete indexes and unproved negative-query coverage remain UNKNOWN.',
 'Reject downgraded EXACT requirements, COMPATIBLE without proof, stale supporting dependencies or future-state completion claims.',
 [(13,'22. '),(13,'28. '),(13,'31. '),(13,'33. '),(17,'12. '),(25,'70. '),(26,'FC10-03-07')],[69,70,71]),
('X8-11','L3 → L5 → L7','L5 learning/use / L7 actual egress binding',
 ['Observation','MemoryProposal','MemoryProposalSnapshot'],['MemoryRecord','MemoryRetrievalResult','SealedOutboundContext'],
 'LearningGate plus Executive authorization governs canonical promotion. Retrieval and transport cannot promote truth or grant disclosure.',
 'Freeze proposal/evidence binding, revalidate LearningGate at commit and use governed revision transaction. Actual outbound bytes/destination/purpose must match sealed admission.',
 'Replay learning promotion idempotently. Revision conflicts require new evaluation; provider switching or altered outbound context requires renewed disclosure checks.',
 'Reject unsupported causal memory, repeated evidence counted as diversity, stale promotion, stored prompt authority or unapproved actual egress.',
 [(15,'13. '),(15,'15. '),(15,'23. '),(15,'42. '),(25,'60. '),(26,'FC10-03-06')],[60,62,77]),
('X8-12','L3 → L6 → L1','L6 recovery admission / L3 containment and effects',
 ['ContainmentProof','ActionRecord','RecoveryCase'],['ScopedRecoveryAdmission','RecoveryAdmissionBinding','CrossFrontierAdmissionProof'],
 'Recovery has bounded source-owned authority. Destructive restore, compensation and world mutation retain ActionGate requirements.',
 'Prove acknowledged-history continuity, anti-rollback/admission frontiers, containment and disclosure barriers before enabling affected execution.',
 'Restore cannot undo possible post-backup effects. Unknown scope uses conservative bounds; independent proved scopes may proceed.',
 'Reject guessed successful effect, blind retry, unfenced stale writer, missing authority frontier or uncontained restored executable data.',
 [(19,'23. '),(19,'65. '),(20,'37. '),(21,'13. '),(21,'21. '),(21,'46. '),(22,'FC09-04-01')],[48,52,73]),
]

def source(order,prefix):
    item=next(s for s in message(order)['segments'] if s['heading'].startswith(prefix))
    return {**item,'source_path':message(order)['source_path']}

def make():
    records={r['type']:r for r in REGISTRY}
    report=[]
    lines=['# Cross-layer interface validation','',
     '**All twelve paths processed. Full field/conversion and baseline-law acceptance remains OPEN.**',
     'This is a source-backed constraint review. No callable signature or unspecified serializer is fabricated. Source-defined record fields and optionality are attached in the JSON evidence. Transport projections preserve owner semantics; naming an alias does not prove a lossless mapping.','']
    for ident,path,owner,inputs,outputs,authority,atomicity,failure,rejection,refs,fc in PATHS:
        types=inputs+outputs
        absent=[n for n in types if n not in records]
        assert not absent,(ident,absent)
        issues=[n for n in types if records[n]['status'].startswith(('PARTIAL','MULTIPLE','UNSPECIFIED')) or records[n]['parent_or_projection_variance'] and not records[n].get('parent_conformance_disposition')]
        evidence=[source(o,p) for o,p in refs]+[fca(n) for n in fc]
        report.append({'id':ident,'path':path,'ownership':owner,'input_records':inputs,'output_records':outputs,
         'signature':'UNSPECIFIED; record participation only','authority':authority,'atomicity_durability':atomicity,
         'failure_retry_recovery':failure,'rejection_conditions':rejection,'status':'CONSTRAINTS_RECORDED; FULL_ACCEPTANCE_OPEN',
         'field_or_projection_review':issues,'source_units':[{'unit_id':s['unit_id'],'source_path':s['source_path'],'line':s.get('bundle_start_line',s.get('start_line')),'sha256':s['sha256']} for s in evidence],
         'record_evidence':[{k:records[n].get(k) for k in ['type','owner','status','effective_raw','explicit_overlays','associated_contracts','selected']} for n in types]})
        links=[]
        for s in evidence:
            line=s.get('bundle_start_line',s.get('start_line',1))
            links.append(f"[{s['unit_id']}](<../../{s['source_path']}#L{line}>)")
        lines.extend([f'## {ident}: {path}','',f'Owner contracts: {owner}.','',
         'Inputs: '+', '.join(inputs)+'. Outputs: '+', '.join(outputs)+'.','',
         '**Authority and transitions:** '+authority,'','**Atomicity and durability:** '+atomicity,'',
         '**Failure, retry and recovery:** '+failure,'','**Rejection:** '+rejection,'',
         '**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: '+(', '.join(issues) or 'baseline-law and owner-projection conformance audit')+'.','',
         'Source/amendment evidence: '+'; '.join(links)+'.',''])
    out=ROOT/'reviews/canonical'
    (out/'INTERFACE_VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (out/'INTERFACE_VALIDATION.md').write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
    print(json.dumps({'paths':len(report),'constraints_recorded':len(report),'fully_accepted':0}))

if __name__=='__main__': make()
