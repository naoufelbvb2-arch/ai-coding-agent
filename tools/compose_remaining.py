"""Build coherent layer bodies from operative amendment clauses and retained scopes."""
import re
from render_layer import DATA, fca, header, imports, message, retained_prose, rule, source_link, write
from schema_selection import schemas

CONFIG = {
'L3': {
 'mandate':'L3 owns action admission/execution, reality observations, evidence governance, experimental and verification records. It does not own the Executive, canonical Claim identity, the control persistence boundary or recovery admission.',
 'amendments':[(5,'C01-',None),(7,'C01-',None)],
 'baseline':{4:[1,2,4,5,6,7,12,13,14,15,16,19,21,22,24,25,27,28,29,31,32,33,34,35,36,38,39,40,41,43,46,47,48,49,50,51,53,55,58,59,60,61,62,63,64,66,69,71,73,74,75,76,77,80,81,82,86,87,88],
             6:[1,2,3,4,5,6,7,8,10,11,12,17,18,19,24,25,27,28,30,31,32,34,35,36,37,38,40,41,42,44,45,49,50,51,52,53,57,58,59,60]},
 'fca':[11,12,13,14,35,40,41,42,43,44,45,46,47,75,76,79],
 'boundaries':[('ControlCommit, canonical authority and epoch','L1','Persist legal control changes and dispatch prerequisites; no external-store atomicity assumption.'),
 ('Claim/Hypothesis/OVC identities and Executive decision','L2','Propose evidence or actions; consume lawful authorization.'),
 ('Dependency evaluation and specialist grants','L4','Use one freshness engine and enforce actual grant/effect intersection.'),
 ('Learning and canonical memory','L5','Supply attributed evidence without implicit promotion.'),
 ('Recovery admission and suspension integrity','L6','Reconcile unresolved effects before conflicting continuation.'),
 ('Execution/observation transport','L7','Receiving admission verifies effective authority; delivery is not dispatch.')]},
'L4': {
 'mandate':'L4 owns temporal evaluation, durable trigger processing, specialist orchestration, reactivation scheduling and the single dependency evaluation engine. Commitment belongs to L2; ResumptionCapsule, ResumeAssessment and recovery-transition integrity belong to L6.',
 'amendments':[(10,'C01-',set(range(34,42))),(13,'NUMBERED',set(range(48,200)))],
 'baseline':{9:[1,2,3,4,7,9,10,11,12,13,14,15,17,26,28,29,30,32,38,39,41,43,44,48,49,51,52,53,54,55,56],
             12:[1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,22,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,45,46,47,48,49,53,54,55,56,57,58,59,60,63,65,66,67,68,69,70,71,72]},
 'fca':[54,56,63,64,65,66,67,68,69,70,71,78,80],
 'boundaries':[('Commitment, Goal/Slice state and Executive adoption','L2','Evaluate owned condition roots; request reactivation without authorizing work.'),
 ('ResumptionCapsule, ResumeAssessment and recovery admission','L6','Schedule recovery/resumption work; import sole-owner integrity and barrier contracts.'),
 ('ControlTransaction and idempotent canonical application','L1','Atomic cursor/fire/reaction metadata and prescribed target mutation.'),
 ('ActionGate and evidence ingress','L3','Monitoring, specialist tools and trigger effects obey legal action/evidence boundaries.'),
 ('Memory use and learning','L5','Specialist experience is a proposal, not memory promotion.'),
 ('Event and specialist delivery','L7','Keep at-least-once delivery separate from canonical effect and dispatch.')]},
'L5': {
 'mandate':'L5 owns canonical memory, retrieval semantics, maturity, revision, learning proposals and LearningGate. It retains source trust and evidence lineage; memory similarity, historical knowledge and procedures confer no action or cognitive authority.',
 'amendments':[(15,'NUMBERED',set(range(52,200)))],
 'baseline':{14:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,65,66,67,68,73,74,77,78,79,80,81,82,83,84,85,86,87,88]},
 'fca':[57,58,59,60,61,62,77],
 'boundaries':[('Executive authorization and current cognitive state','L2','Gate learning proposals and assess retrieved guidance in current context.'),
 ('Observation/evidence roots and causal closure','L3','Bind learning to genuine evidence; do not multiply wrappers into corroboration.'),
 ('Dependency engine and temporal conditions','L4','Use sole engine for applicability/freshness and import Commitment.'),
 ('ControlTransaction, artifact publication and version concurrency','L1','Commit governed revisions atomically with pinned durable references.'),
 ('Erasure, retention, restore suppression and recovery admission','L6','Physical lifecycle is distinct from epistemic retirement.'),
 ('MemoryRetrievalTransportResult and outbound context','L7','Transport canonical results without changing their owner or disclosure conditions.')]},
'L6': {
 'mandate':'L6 owns recovery authority and admission, durable recovery state, suspension/resumption integrity, anti-rollback, restore, migration and data lifecycle safety. It owns ResumptionCapsule and ResumeAssessment, including the integrity contracts originating in RDMS-05. Recovery never becomes a second Executive, CommitGate or ActionGate.',
 'amendments':[(10,'C01-',set(range(1,34))|set(range(42,99))),(19,'NUMBERED',set(range(126,200))),(20,'NUMBERED',set(range(96,200))),(21,'NUMBERED',set(range(76,200))),(22,'FC09-',None)],
 'baseline':{18:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]},
 'fca':[52,53,82],
 'boundaries':[('Control current-store/replay, ProjectHead and durable ordering','L1','Reconstruct acknowledged legal state; do not fabricate missing commits.'),
 ('Executive authority, decisions and cognitive resumption','L2','Issue bounded recovery admission; Executive reassesses resumed work.'),
 ('Action Journal, effective dispatch, probes and compensation','L3','Preserve uncertain effects and normal action authorization.'),
 ('Trigger replay, reactivation and dependency engine','L4','Import temporal scheduling; own durable recovery suspension integrity.'),
 ('Canonical memory, derived indexes and retirement','L5','Restore legal memory and suppress erased/restricted data before use.'),
 ('Activation, delivery and dispatch admission transport','L7','Require source-owned current admission at the last enforceable boundary.')]},
'L7': {
 'mandate':'L7 owns integration and transport contracts. It connects canonical owners and enforces their admission contracts at receiving boundaries. It has no independent cognitive, canonical-commit, action, temporal, freshness, learning or recovery authority.',
 'amendments':[(24,'NUMBERED',set(range(158,200))),(25,'NUMBERED',set(range(83,200))),(26,'FC10-',None)],
 'baseline':{23:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104]},
 'fca':[85],
 'boundaries':[('Foundation and content/authority conservation','L0','Carry trusted metadata without granting authority to content.'),
 ('ControlTransaction, CommitGate and durability','L1','Route owner-authorized mutation; delivery acknowledgement is not canonical commit.'),
 ('Executive, canonical CapabilityResult and finalization','L2','Keep transport result distinct; submit proposals for adoption.'),
 ('ActionGate, Action Journal, observations and evidence','L3','Separate admission, external dispatch, observation and reconciliation.'),
 ('TriggerCondition, specialists and one dependency engine','L4','Deliver requests without authorizing execution or duplicating scheduling.'),
 ('Canonical MemoryRetrievalResult and LearningGate','L5','Preserve semantic payload, provenance, trust and applicability.'),
 ('Recovery admission, capsule integrity and restore policy','L6','Activation requires current scoped admission; transport cannot expand it.')]},
}

# Superseded baseline sentences are not imported here. Retained candidates have a
# separate ledger and remain visibly pending until a sentence-level amendment audit.
# This keeps a partial audit from publishing an old draft as current normative law.
SAFE_BASE = {
 'L3':{4:[1,2,4,5,6,7,12,13,14,15,16,19,21,22,24,25,27,28,29,31,32,33,34,35,36,38,39,40,41,46,47,48,49,50,51,53,55,58,59,60,61,62,63,64,66,69,71,73,74,75,76,77,80,81,82,86,87],
       6:[1,2,3,4,5,6,7,8,10,11,12,17,18,19,24,25,27,28,30,31,32,34,35,36,37,38,40,41,42,44,45,49,50,51,52,53,57,58,59,60]},
 'L4':{9:[1,2,3,4,7,14,15,17,26,28,29,30,32,38,39,41,44,48,51,52,53,54,55,56],
       12:[1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,22,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,46,47,48,49,53,54,55,56,57,58,59,60,63,65,66,67,68,69,70,71,72]},
 'L5':{14:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,65,66,67,68,73,74,77,78,79,80,81,82,83,84,85,86,87,88]},
 'L6':{18:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,22,26,27,28,29,30,31,32,37,38,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]},
 'L7':{23:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104]},
}

# Additional independent scopes reviewed against their operative corrections.
for layer,order,numbers in [
 ('L3',4,[37,43,45,65,67,68,70,72,78,79,83,84,85,88]),
 ('L3',6,[14,15,16,22,23,26,29,33,43,46,47,48,54,55,56]),
 ('L4',9,[6,8,9,10,11,12,13,20,40,42,43,45,46,47,49,50]),
 ('L4',12,[14,21,23,30,40,41,42,43,44,45,50,51,52,61,62,64]),
 ('L5',14,[61,62,69,70,71,72,75,76]),
 ('L6',9,[31,33,34,35,36,37]),
 ('L6',18,[18,19,20,21,23,24,25,33,34,35,36,41,42,43,44,45]),
 ('L7',23,[20,68,69,70,71,91]),
]:
    SAFE_BASE[layer][order]=sorted(set(SAFE_BASE[layer].get(order,[])+numbers))

def operative(order, prefix, excluded):
    seen = set()
    for item in message(order)['segments']:
        heading = item['heading']
        if re.search(r"(?:Additional|Added|New Corrected) (?:Formal )?Invariants",heading,re.I):
            yield {**item,'source_path':message(order)['source_path']}
            continue
        match = re.match(r'^(\d+)\. ',heading) if prefix=='NUMBERED' else re.match(re.escape(prefix)+r'(\d+)',heading)
        if not match:
            continue
        number = int(match.group(1))
        if prefix=='NUMBERED' and number in seen:
            break  # following adversarial review restarts numbering; not new laws
        seen.add(number)
        if excluded and number in excluded:
            continue
        if 'Finding' in heading:
            continue  # historical problem statement, not operative replacement
        yield {**item,'source_path':message(order)['source_path']}

def compile_layer(layer,config):
    parts=[header(layer,config['mandate'],'REVIEW CANDIDATE; BASELINE/FIELD AUDIT LIMITS RECORDED')]
    parts.append(imports(config['boundaries']))
    parts.append('## Effective amended responsibilities\n\nArticles below contain the operative source clauses in their authorized scope, with historical findings, review narratives and replaced record specimens omitted. Record fields are maintained once in the owning contract section. Later hardening supplements earlier duties; it does not repeal an earlier duty without an explicit replacement.\n\n')
    for order,prefix,excluded in config['amendments']:
        for item in operative(order,prefix,excluded):
            identifier=layer+'-A'+str(order).zfill(2)+'-'+item['unit_id'].split('-')[-1]
            parts.append(retained_prose(item,identifier))
    if layer=='L4':
        source=next(s for s in message(11)['segments'] if s['heading'].startswith('2. Final Freeze Clarifications'))
        parts.append(retained_prose({**source,'source_path':message(11)['source_path']},'L4-FC05-01-02'))
    parts.append('## Retained independent baseline responsibilities\n\nThe following individually selected original clauses preserve independent duties. They are not admission of an entire historical draft. Where an amendment adds a requirement, the amended article and its sole-owner record contract govern that added requirement.\n\n')
    for order,numbers in SAFE_BASE[layer].items():
        for n in numbers:
            source=next(s for s in message(order)['segments'] if s['heading'].startswith(str(n)+'. '))
            parts.append(retained_prose({**source,'source_path':message(order)['source_path']},f'{layer}-B{order:02d}-{n:03d}'))
    parts.append('## FCA responsibilities retained in this layer\n\n')
    for n in config['fca']:
        parts.append(retained_prose(fca(n),f'{layer}-F{n:02d}'))
    parts.append(schemas(layer))
    parts.append('## Acceptance boundary\n\nSource integrity and article locators are mechanically verified. The source coverage ledger distinguishes directly incorporated clauses from baseline reconciliation still requiring proof. The registry distinguishes governing semantic duties from unresolved record-shape or parent-field conversion. This document is a review candidate, not a declaration that mandatory normative completeness or implementation readiness has passed. Open scopes do not suspend unrelated rules whose sources and amendment effects are verified.\n')
    write(layer,'\n'.join(parts))

if __name__=='__main__':
    for layer,config in CONFIG.items():
        compile_layer(layer,config)
