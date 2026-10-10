"""Cognitive law consolidation; explicitly scoped amendments, never a draft bundle."""
from render_layer import DATA, fca, header, imports, message, retained_prose, rule, segment, write
from schema_selection import schemas

ENTITY = [
("Use CanonicalEntityMeta for common identity/version metadata. There is no generic canonical lifecycle: each entity owns exactly its declared lifecycle.", [1]),
("SupportAssessment is an immutable assessment for Claim or Hypothesis, with evidence basis, dependencies and assessed commit. Replace embedded support with current_support_assessment_ref; CURRENT/STALE/UNKNOWN assessment validity is derived.", [2,3]),
("Promote a Claim with the same proposition from ASSUMPTION to BELIEF or grounded FACT. Material proposition changes require a new identity and lineage. A FACT remains historically a FACT when stale; current usability is derived, not a fabricated demotion or refutation.", [4,5,6]),
("Hypothesis lifecycle is ACTIVE/REJECTED/CONFIRMED/SUPERSEDED, with closure_ref where applicable. A confirmed hypothesis is a precursor to causal closure, not an additional independent confirmation. OVC lifecycle is OPERATIONALLY_VERIFIED/CONTRADICTED/SUPERSEDED; OVCUsability is VALID/STALE/UNKNOWN.", [7,8]),
("The goal hierarchy is acyclic, within one project, rooted in MISSION and without a fixed four-level depth. GoalPath replaces GoalStack: it begins at MISSION and follows each parent edge. Terminal ancestors are forbidden except the expressly allowed cleanup/finalization context.", [9,10]),
("Goal CANCELLED requires cancellation_reason and cancellation_authority_ref. It differs from CLOSED and OBSOLETE. WAIVED acceptance requires WaiverRecord and lawful waiver authority, not omission of the criterion. declared_priority is LOW/NORMAL/HIGH/CRITICAL and is a scheduling signal.", [11,12,14]),
("Before CLOSED, requirement changes reset affected criteria to PENDING and reopen VERIFIED goals to READY/ACTIVE through lawful authority. A CLOSED goal's history is not rewritten; subsequent work uses a successor.", [13]),
("Accepted Decision content is immutable history. New reasoning requires a new decision identity; lawful supersession/invalidation changes lifecycle. dependency_set_ref and validity_conditions govern derived DecisionUsability CURRENT/REVIEW_REQUIRED/INVALID/UNKNOWN. REVIEW_REQUIRED is not a new decision lifecycle.", [15,16]),
("Versions preserve one concept's identity; split, merge or materially new ownership concepts require new identities. Correctness-sensitive references in slices and decisions pin versions.", [17,18]),
("EntityLineageEdge replaces authoritative scalar superseded_by and supports REPLACES/SPLITS_INTO/MERGES_INTO/REFINES. HypothesisRelation is independently governed; symmetric COMPETES_WITH/ALTERNATIVE_TO and directed REFINES are not an authoritative embedded competing array. Reject self-edges, illegal project boundaries and prohibited cycles.", [19,20]),
("SliceState has independent stage PLANNED/READY/EXECUTING/VERIFYING/VERIFIED/INTEGRATING/INTEGRATED, condition NORMAL/BLOCKED/SUSPENDED and terminal NONE/CLOSED/FAILED/CANCELLED/OBSOLETE. Blocking preserves stage; failed execution attempt is not automatically terminal FAILED.", [21,22,23]),
("CLOSED requires INTEGRATED, satisfied or lawfully waived mandatory proof obligations and no violated hard invariant. Cognitive integration of a diagnostic slice counts where appropriate. planned_from_commit_seq is provenance; dependency_set_ref and base_repo_ref replace the old global base_state_version freshness gate.", [24,25]),
("Canonical focus is the compact GoalPath, current slice/operation, active hypotheses, needs, landmarks and focus reason. File/symbol/search attention remains ephemeral unless explicit durable suspension material requires it. MentalModelElement stores source-governed assertions and references, not a second canonical entity database; freshness is derived and lifecycle is ACTIVE/SUPERSEDED.", [26,27]),
("EnforcementSpec separates enforcement mode, verifier, coverage and failure response BLOCK/ESCALATE/WARN from severity. HARD requires an enforceable plan, possibly semantic review, and cannot silently downgrade on unavailable enforcement.", [28,29]),
("Risk lifecycle OPEN/MITIGATED/REALIZED/OBSOLETE differs from treatment UNASSESSED/MONITOR/MITIGATE/ACCEPT/AVOID. RiskAssessment is immutable likelihood/impact/basis/dependency history with derived freshness. Accepting risk needs the prescribed decision reference, not a lifecycle named ACCEPTED.", [30,31]),
("Commitment is owned here. Replace due_at/removal_trigger_id/revisit_trigger_id with reactivation_condition_ref while retaining unaffected fields and lifecycle. L4 owns condition composition, evaluation and scheduling; it cannot redefine Commitment.", [32]),
("Independent relation entities own relations; cached embedded arrays do not gain authority. EntityRef names logical identity, VersionedEntityRef pins correctness-sensitive content and DependencyStamp supplies freshness evidence.", [33,34]),
("The amended RDMS-02 invariants 23–45 are source-namespaced obligations; their numbering does not alias FCA or another RDMS invariant corpus.", [35]),
]

EXEC = [
("One Cognitive Executive decides; provider text remains a proposal. Trusted issuance creates ExecutiveAuthorization after eligibility validation. A model's authorized=true has no legal force.", range(1,6)),
("Preserve FCA states. OperationTransitionContract maps CLARIFY to ASK_USER, INSPECT to INVESTIGATE, RETRIEVE_MEMORY to ORIENT/INVESTIGATE, MODEL to ORIENT/DELIBERATE, SIMULATE and DELIBERATE to DELIBERATE, DESIGN_EXPERIMENT to INVESTIGATE/PLAN, and RECRUIT_SPECIALIST to SPAWN_SPECIALIST. REASSESS chooses an existing state. Target mapping never makes every source state eligible.", range(6,9)),
("Decision acceptance, canonical transition and required goal/context mutations share one legal ControlCommit. World dispatch is a separate L3 boundary.", range(9,12)),
("Revalidate affected dependencies in ReadinessSnapshot before use. Unrelated commits do not automatically invalidate it; readiness never grants action permission.", range(12,15)),
("Trusted ContextManifest preserves mandatory operation-specific context. Compression cannot remove essential constraints or conceal missing coverage; a model cannot certify its own context completeness.", range(15,18)),
("Distinguish measured resource use from predicted estimates. Unknown cost, risk and uncertainty remain unknown; fabricated scalar estimates cannot justify authority.", range(18,21)),
("AggregateRiskAssessment preserves obligations across decomposed high-gravity work. Small slices cannot launder aggregate gravity; downgrade requires the specified lawful reassessment.", range(21,24)),
("Operation selection excludes hard violations and unresolved critical uncertainty, then compares admissible candidates with rationale, bounds and stop/revisit conditions. No universal utility weights are frozen. Incomparability may require information, a defensible low-cost equivalent, human authority or lawful waiting.", range(24,27)),
("Bound reasoning by objective, budget, expected output and stop condition. Rephrasing, provider churn and tool activity are not progress. A failed hypothesis or experiment can supply epistemic progress.", range(27,31)),
("When no operation is admissible, preserve safety restrictions and use lawful wait/suspension with durable reactivation. Uncertain external effects cannot be evaded by a cognitive fallback.", range(31,34)),
("Classify human input by trusted authority, recommendation, preference or opinion. Late answers require current-context validation before adoption.", range(34,37)),
("Simulation is scoped prediction, never reality evidence. Propagate assumptions and coverage limits into readiness. Exploratory spikes obey L3 actual containment/effect rules and do not automatically promote artifacts to production.", range(37,43)),
("Implementation readiness requires adequate goal, scope, contracts, dependencies, failure conditions, acceptance and verification plans plus legal gates. Scale preparation to gravity without hiding aggregate risk; readiness does not claim proof of unwritten code.", range(43,46)),
("Classify tools by reachable effects. Cognitive names INSPECT, VERIFY and DIAGNOSE cannot bypass ActionGate.", range(46,49)),
("Delegation requires marginal value, portfolio and bounded creation/run/integration cost. Specialists cannot bypass Executive budget constraints.", range(49,52)),
("Replanning follows transitive decision, plan and slice dependencies even when files are unchanged. Already dispatched world effects require L3 reconciliation.", range(52,55)),
("Separate verified engineering progress, epistemic progress and activity counts. Apply required independent verification; producer self-approval is not new reality evidence.", range(55,59)),
("Interrupt authority depends on trusted source, applicable policy, affected scope/risk and dependencies; rhetorical urgency cannot create it. Deduplicate replayed interrupts.", range(59,62)),
("Cancellation before legal dispatch prevents dispatch. At DISPATCH_INTENT or later, possible effects remain subject to reconciliation; stopping long-running activity requires evidence.", range(62,65)),
("Scheduling considers age, urgency, blocking, cost and resources under bounded work in progress. A large backlog does not authorize unlimited active work; critical safety obligations cannot be indefinitely deferred for fairness.", range(65,69)),
("Old-epoch results remain untrusted proposals until fresh Executive adoption. Adoption does not revive old authorizations.", range(69,72)),
("Finalization evaluates current evidence and acceptance, disclosing unresolved/failed work. VERIFIED_COMPLETION/PARTIAL_DELIVERY/BLOCKED_COMPLETION/SUSPENDED/UNRESOLVED_OUTCOME are source-defined dispositions, not new FCA cognitive states.", range(72,76)),
("Bind effective policy versions for pending transitions, authorization, in-flight actions and suspension. A provider cannot change policy; version changes cannot erase external effects or silently mix rules.", range(76,80)),
("Persist recovery-relevant decision evidence, not every reasoning token. Clarification, provider fallback and resource use remain bounded by legal context, eligibility and cost; fallback never redispatches external actions. Reconstruct legal conditions rather than model prose. Apply disclosure governance and evaluate held-out behavior with matched models/tools/budgets and full costs.", range(80,87)),
]

def numbered(order, number):
    found = next(s for s in message(order)['segments'] if s['heading'].startswith(str(number)+'. '))
    return {**found, 'source_path': message(order)['source_path']}

parts = [header('L2', 'L2 owns canonical cognitive entities, the single Executive, cognitive policy, readiness and finalization. It consumes evidence, freshness, temporal, memory and recovery contracts from their sole owners.', 'REVIEW CANDIDATE; FIELD RECONCILIATION OPEN')]
parts.append(imports([
('Foundation, content trust and authority conservation','L0','Enforce immutable architectural boundaries.'),
('ControlTransaction, versions and Executive epoch','L1','Submit authorized mutations with legal compare-and-swap.'),
('Observations, evidence, action authorization and causal closure','L3','Never substitute model output for reality or execution authority.'),
('TriggerCondition, specialists and dependency evaluation','L4','Own Commitment; import temporal evaluation and freshness.'),
('Canonical memory and learning/retrieval','L5','Adopt guidance only through present-context assessment.'),
('ResumptionCapsule, ResumeAssessment and recovery admission','L6','Reassess before lawful cognitive resumption.'),
('Reasoning/transport envelopes','L7','Validate delivery as proposals; retain cognitive authority.'),
]))
parts.append('## Effective canonical entity law\n\n')
for i,(text,refs) in enumerate(ENTITY,1):
    parts.append(rule(f'L2-E{i:02d}',text,[segment(3,f'C01-{n:02d} ') for n in refs]))
parts.append(retained_prose(segment(3,'C01-35 '),'L2-E-INVARIANTS'))
parts.append(rule('L2-E19','Causal closure creates the OperationalCausalClaim and records the source Hypothesis as CONFIRMED in the same ControlCommit. The Hypothesis remains a historical precursor, is not automatically SUPERSEDED, and its closure_ref identifies the OVC. Causal evidence and closure requirements remain mandatory; the removed embedded support enum is not reintroduced.',[numbered(2,20),segment(3,'C01-07 ')]))
parts.append(rule('L2-E20','Claim lifecycle and the current proposition-support conclusion must be coherent. A REFUTED Claim cannot use a current assessment as if VERIFIED affirmed that proposition; previous support remains immutable history. The old embedded support values are not current fields. Hypothesis closure-floor correspondence after the support-enum replacement is recorded for source interpretation rather than filled with invented thresholds.',[numbered(2,8),numbered(2,15),segment(3,'C01-02 '),segment(3,'C01-07 ')]))
parts.append('## Effective Executive law\n\n')
for i,(text,refs) in enumerate(EXEC,1):
    parts.append(rule(f'L2-X{i:02d}',text,[numbered(17,n) for n in refs]))
parts.append('## Retained independent entity obligations\n\n')
for n in [3,4,6,7,10,11,12,13,16,18,19,25,26,27,30,33,34,36,37,38,41,42,43,44,49,50,52,53,54,58,59,61,62,64,65,66,67,68,69,70,71,72,73]:
    parts.append(retained_prose(numbered(2,n),f'L2-B{n:02d}'))
parts.append('## Independent Executive baseline duties\n\nOnly unchanged baseline units appear here. The superseded finalization disposition list is omitted; effective dispositions are in L2-X22. C01 admission, context, readiness and authority conditions apply to each activity.\n\n')
for n in range(1,128):
    if n!=101:
        parts.append(retained_prose(numbered(16,n),f'L2-XB{n:03d}'))
parts.append('## FCA cognitive obligations\n\n')
for n in [5,6,7,9,10,16,18,19,22,23,24,25,26,27,28,30,31,32,33,34,36,37,38,39,55,74,81,83]:
    parts.append(retained_prose(fca(n),f'L2-F{n:02d}'))
parts.append(schemas('L2'))
parts.append('## Verification limits\n\nEvery RDMS-02 C01 numbered correction and RDMS-08 C01 operative section is cited above. Record-shape questions are individually identified in the contract registry. A cited correction group is not a proof that every baseline sentence and parent field has been preserved: the source-coverage ledger separately records that obligation. No unresolved record surface is accepted as a complete implementation signature.\n')
write('L2','\n'.join(parts))
