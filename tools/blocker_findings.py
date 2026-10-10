"""Reviewed source-based dispositions; documentation data, not runtime policy."""

# A classification describes the original question. A B entry stays open until
# its preservation proof exists; C defers only the stated representation detail.
FINDINGS = {}


def finding(ident, category, reason, obligations, unspecified, units, **extra):
    FINDINGS[ident] = dict(classification=category, justification=reason,
        binding_obligations=obligations, remaining_detail=unspecified,
        additional_source_units=units.split(), **extra)


finding('PARENT-ActionEffectSemantics', 'B',
    'The retry and verification enums agree. The sources do not explicitly bind the inline outcome_probe, compensation and timeout_policy to the later spec/reference fields. Those contents govern safe retry; equal names or comparable labels are not a preservation proof.',
    'Retain effect identity, idempotency identity, all three retry policies, all three verification modes, timeout semantics, probe adequacy and authorized compensation. A referenced spec must preserve the original operational content.',
    'Proof for outcome_probe versus outcome_probe_spec, compensation versus compensation_spec, and timeout_policy versus timeout_policy_ref, including reference integrity and historical reconstruction. No alias is approved here.',
    'FCA-43 RDMS-04-M06-U012 RDMS-04-M07-U041 RDMS-04-M07-U042 RDMS-04-M07-U043')
finding('PARENT-ActionProposal', 'B',
    'RDMS-04 expressly makes the requested class advisory and provides a separate authorization. That resolves the authority division, but does not prove preservation of every FCA proposal field. FCA base_world_ref/risk_profile are mandatory where the RDMS specimen makes their references optional; authority_required and proposal status have no explicit complete crosswalk.',
    'Requested class never authorizes execution. Preserve identity, requester, Goal/Slice lineage, intent, detailed operation, target/effect/precondition information, risk, reversibility, compensation, diagnostic/production meaning, relevant world basis, required authority and proposal history. ActionGate and authorization fingerprint govern actual execution.',
    'Prove the detailed operation-kind information, mandatory risk/world information, authority_required and proposal status survive in the owner records. An ActionAuthorization is not itself a proved storage location for proposal authority requirements.',
    'FCA-42 RDMS-04-M06-U004 RDMS-04-M06-U005 RDMS-04-M06-U006 RDMS-04-M07-U002')
finding('PARENT-ActionRecord', 'B',
    'RDMS-04 separates action, attempt, report, observation and reconciled effect explicitly. This proves the decomposition, but not a complete per-action reconstruction of every original timestamp, observation membership and before-world requirement.',
    'Retain the original action identity, proposal, lifecycle, before/after world context, execution reports, observations, compensation association and start/finish information. Keep ActionId, AttemptId and DispatchId distinct; latest_attempt_ref cannot erase older attempts or establish the effect.',
    'Proof for mandatory world_ref_before, execution_result, observation_ids, compensation_action_id, started_at and finished_at across ActionRecord/ActionAttempt/Observation/ProcessRun/ReconciliationRecord. Do not choose first/last-attempt timestamp aggregation.',
    'FCA-46 RDMS-04-M06-U008 RDMS-04-M06-U010 RDMS-04-M06-U064 RDMS-04-M06-U071 RDMS-04-M07-U002')
finding('SHAPE-CanonicalStateView', 'C',
    'The sole declaration is explicitly abbreviated with an ellipsis and is a read view, not a new canonical entity. RDMS-02 defines the entity owners and later explicitly replaces GoalStack. There is no competing current legal state schema to decide between.',
    'Read the authoritative canonical entities; use GoalPath and the current canonical focus; preserve epistemic types, derived OVC usability and scope. A view cannot create state, permission, a lifecycle or an independent freshness engine.',
    'Read-view class, table joins, nesting, pagination and serialized member names. These choices cannot omit information required by a particular consuming contract; that conformance obligation remains binding.',
    'FCA-6 RDMS-02-M02-U000 RDMS-02-M03-U009 RDMS-02-M03-U025 RDMS-10-M24-U010')
finding('PARENT-Claim', 'B',
    'C01 explicitly externalizes support and independent relations. That resolves their authority, but the parent evidence/provenance and temporal information require a documented reconstruction through the exact accepted links and metadata; the record specimen alone does not prove it.',
    'Preserve statement identity, kind, scope, evidence for/against, provenance, lifecycle, temporal validity and entity version. SupportAssessment and EvidenceLink own their respective conclusions/relations; no second authoritative embedded evidence list.',
    'Prove evidence_for/evidence_against, provenance, version and parent temporal_validity preservation through the associated records and exact reference policy, including the optional temporal_validity specimen.',
    'FCA-8 RDMS-02-M03-U000 RDMS-02-M03-U001 RDMS-02-M03-U032 RDMS-03-M04-U021')
finding('PARENT-ConfidenceAssessment', 'B',
    'The level values and residual uncertainty agree, but assessed_at and assessed_at_commit_seq are different information. A commit ordering number is not a wall-clock timestamp or a complete evidence-basis conversion.',
    'Preserve target, confidence level, evidence basis, residual uncertainty and assessment time/context. Claim/Hypothesis support must not gain a competing ConfidenceAssessment authority.',
    'Proof for basis versus evidence_link_refs plus verification_record_refs, and assessed_at versus assessed_at_commit_seq. Do not silently equate time with sequence.',
    'FCA-14 RDMS-03-M05-U040 RDMS-01-M01-U004')
finding('SHAPE-ContainmentProof', 'D',
    'C01-27 is the approved complete scoped restatement of ContainmentProof for effective configuration and trusted enforcement. C01-28 supplements it with continuous enforcement. The old record is not a second current native schema. FCA reachable-effect isolation duties remain unchanged.',
    'Use the C01-27 native fields and trusted enforcement evidence. Prove filesystem isolation, absence of shared writable mounts and dangerous credentials, blocking of mutating network/privileged paths and disposability of reachable effects. Enforce the policy during execution; drift invalidates new launches under an old proof.',
    'No historical-record converter or Boolean-to-policy alias is asserted. Backend-specific proof encoding remains subject to the retained containment duties.',
    'FCA-42 RDMS-04-M06-U052 RDMS-04-M07-U033 RDMS-04-M07-U034', correction='Publish the approved C01-27 record once and explicitly retain the original isolation duties.')
finding('PARENT-ContradictionRecord', 'B',
    'The comparison and causal-explanation boundary are explicit, but FCA UNRESOLVED is absent from the RDMS lifecycle, and possible_dimensions is replaced by dimension_analysis. No exact lifecycle/field projection is authorized by the excerpts.',
    'Preserve both observations, subject, scope, comparability, time/input/environment/world/nondeterminism/measurement dimensions and unresolved information. Causal explanations must refer to a typed proposition/result; they are not hidden in dimension_analysis.',
    'Document how FCA unresolved status and dimension information are represented without inventing a new lifecycle value or declaring UNRESOLVED equal to CONFIRMED.',
    'FCA-13 RDMS-03-M04-U029 RDMS-03-M04-U032 RDMS-03-M05-U019')
finding('PARENT-Decision', 'B',
    'C01 resolves accepted-content immutability, freshness and lineage. It does not give a complete crosswalk for FCA evidence_refs, rejected option reasons and chosen content into the later option/reference surface.',
    'Preserve question/context, gravity, quality drivers, constraints, alternatives, chosen option, every rejection reason, assumptions, accepted tradeoffs, evidence, consequences, risks, revisitation, lifecycle and version. Accepted semantic content is immutable.',
    'Prove evidence_refs and every rejected {option, reason}, chosen content and version are recoverable through the exact owner records; do not infer that dependency_set_ref substitutes for evidence.',
    'FCA-17 RDMS-02-M02-U034 RDMS-02-M02-U035 RDMS-02-M03-U014 RDMS-02-M03-U015')
finding('PARENT-DependencyStamp', 'B',
    'RDMS-06 explicitly retains FCA dependency kinds and freshness meanings. The inline validity_condition and the later validity_condition_ref still require preservation of the condition and its version/identity; this affects correctness, not only encoding.',
    'Retain dependency kind/subject, version or hash, validity condition and EXACT/COMPATIBLE/ADVISORY meaning. Use the one dependency engine; an incomplete dependency universe cannot certify complete validity.',
    'Prove the subject and validity-condition reference binding, including source version, available content and replay/retention. No ref/dep-ref or inline-condition alias is invented.',
    'FCA-69 RDMS-06-M12-U038 RDMS-06-M12-U040 RDMS-06-M13-U031')
finding('SHAPE-EvidenceLink', 'C',
    'This question specifically concerns the embedding field for already specified EvidenceBasis and pinned AuthorityBinding. C01-04 and C01-10 through 13 fully bind their information and usability. Choosing a member name or inline versus reference encoding supplies no additional legal meaning. Parent field preservation is separately kept open as PARENT-EvidenceLink.',
    'Carry EvidenceBasis items with observation identity and REQUIRED/CORROBORATING/CONTEXT role, ALL_REQUIRED or STRUCTURED semantics and the required derivation. Pin the AuthorityBinding version for AUTHORITATIVE evidence. Retain accepted-link immutability and derived usability.',
    'Embedding member name and serializer layout only. Missing basis, lost role, unpinned authority, unavailable referent or changed derivation is a normative violation, never an implementation discretion.',
    'RDMS-03-M05-U003 RDMS-03-M05-U009 RDMS-03-M05-U010 RDMS-03-M05-U011 RDMS-03-M05-U012')
finding('PARENT-EvidenceLink', 'B',
    'Multi-observation support and structured roles are explicitly approved. The full parent target identity/type, single-observation information and accepted semantic-link projection still need an exact reference/preservation proof; an unspecified embedding does not discharge this distinct question.',
    'Preserve link identity, canonical observations, typed target identity, relation, rationale, derivation and lifecycle. Every accepted link has a real Observation root. Preserve C01 basis roles, pinned authority and historical meaning.',
    'Field-by-field parent/current reconstruction including observation_id, target_type/target_id and the new structured basis. No lossy flattening of REQUIRED/CORROBORATING/CONTEXT or automatic alias.',
    'FCA-12 RDMS-03-M04-U021 RDMS-03-M04-U022 RDMS-03-M05-U009 RDMS-03-M05-U012')
finding('PARENT-Experiment', 'B',
    'RDMS-03 expressly separates design from run, observations and conclusion proposals. That is a resolved legal distinction. The complete FCA design/run lifecycle and designed_at/executed_at reconstruction is not established by the abbreviated cross-layer record inventory.',
    'Retain question, hypotheses, method, discriminating predictions, authorized actions, risk, design/execution history, observations, conclusion proposal and time. Freeze predictions before runs; failed execution does not refute a hypothesis.',
    'Prove all original fields through Experiment/Prediction/ExperimentRun/Observation/ExperimentConclusionProposal, especially original timestamps and lifecycle participation. No run-state-to-design-state alias.',
    'FCA-40 RDMS-03-M04-U040 RDMS-03-M04-U043 RDMS-03-M04-U046 RDMS-03-M04-U048 RDMS-03-M05-U023')
finding('PARENT-Goal', 'D',
    'All FCA Goal information is retained by RDMS-02 Goal plus AcceptanceCriterion. C01-14 explicitly renames priority to declared_priority; C01-11 adds cancellation without dropping the original states. This is an approved owner elaboration, not an unproved competing projection.',
    'Preserve typed Goal identity and parent, intent, acceptance criteria, declared priority, all original statuses and created_from. CANCELLED requires cancellation_reason and cancellation_authority_ref. Priority alone cannot drive scheduling.',
    'No importer conversion API is approved. Entity identity is governed by CanonicalEntityMeta, and criterion requirements/waivers by the owner law.',
    'FCA-15 RDMS-02-M02-U021 RDMS-02-M02-U022 RDMS-02-M03-U000 RDMS-02-M03-U010 RDMS-02-M03-U013')
finding('PARENT-Hypothesis', 'B',
    'Support, closure, relation and lineage ownership are explicitly amended, but a complete parent evidence/assumption/prediction/experiment reconstruction still needs proof. HG-01 separately handles the missing support-admission correspondence.',
    'Retain immutable explanatory identity, scope, explained subjects, assumptions, predictions, for/against evidence, experiments and competing relations. One lifecycle and one SupportAssessment authority; closure points to the causal result when applicable.',
    'Prove complete original information across references and independent relation owners. This entry does not resolve HG-01 or permit replacing old support values with guessed new thresholds.',
    'FCA-10 RDMS-02-M03-U001 RDMS-02-M03-U006 RDMS-02-M03-U019 RDMS-02-M03-U032')
finding('PARENT-InformationNeed', 'D',
    'RDMS-02 section 10 explicitly replaces the single resolution route with resolution_routes[] because multiple routes can answer the same question; section 12 explicitly makes the answer a typed ResolutionRef. Original identity, question, importance, blocks, candidates and all four lifecycle states remain.',
    'Retain all routes and source candidates; preserve typed blocked entities and resolution evidence. OBSOLETE is distinct from RESOLVED. HUMAN in the route list does not itself require immediate escalation.',
    'Physical reference/serialization encoding; no new route, lifecycle or authority is introduced.',
    'FCA-9 RDMS-02-M02-U002 RDMS-02-M02-U009 RDMS-02-M02-U010 RDMS-02-M02-U011 RDMS-02-M02-U012')
finding('PARENT-Invariant', 'D',
    'RDMS-02 section 39 explicitly permits simultaneous enforcement modes; C01-28 replaces these with EnforcementSpec entries while preserving severity and modes. C01-01 supplies version metadata and C01-17/18 pins engineering semantics. No original enforcement duty is waived.',
    'Retain statement, scope, kind, severity, predicate/verification and source authority, version and ACTIVE/SUPERSEDED/RETIRED lifecycle. EnforcementSpec records mode, verifier, coverage and fail behavior. HARD remains unacceptable even when checking is semantic.',
    'No automatic field converter is asserted. Runtime verifier mechanics cannot weaken coverage or fail behavior.',
    'FCA-19 RDMS-02-M02-U038 RDMS-02-M03-U000 RDMS-02-M03-U016 RDMS-02-M03-U017 RDMS-02-M03-U027 RDMS-02-M03-U028')
finding('PARENT-MemoryProposal', 'D',
    'RDMS-07 section 24 expressly adopts and expands FCA fields. Section 25 enumerates the required claim, scope, evidence, counterconditions/examples, requested maturity and invalidating dependencies; section 17 preserves the FCA maturity ladder. There is no omitted parent semantic category.',
    'Retain claim, proposed scope, source episodes, optional causal basis, applicability/counterconditions/counterexamples, evidence, confidence assessment and requested maturity. Added provenance/category/dependencies do not authorize promotion; LearningGate and Executive approval remain required.',
    'Reference encoding only; no maturity_target/proposed_maturity wire alias or lossy converter is declared by this review.',
    'FCA-60 RDMS-07-M14-U023 RDMS-07-M14-U029 RDMS-07-M14-U031 RDMS-07-M14-U032')
finding('PARENT-Observation', 'B',
    'C01 binds content trust, normalization and temporal provenance, but the whole parent field projection is not proven: mandatory parent world_ref versus optional native reference and source_authority versus associated bindings affect evidential interpretation.',
    'Preserve source, authority when applicable, real observation context/time/content/raw material/provenance/integrity and stable event identity. Normalization cannot introduce semantic inference. Trust metadata must travel with content.',
    'Proof of parent world context, source authority and content/raw/integrity projection into the current surface. Do not manufacture a world reference for an observation whose source has no known world context.',
    'FCA-11 RDMS-03-M04-U002 RDMS-03-M04-U010 RDMS-03-M04-U011 RDMS-03-M05-U000 RDMS-03-M05-U020')
finding('PARENT-OperationalCausalClaim', 'B',
    'CausalVerificationRecord is explicitly a compact replacement for inline verification, and C01 makes freshness derived. Complete proof is still needed for every FCA evidence/dependency/verification and promotion-time field, including conditional regression capture.',
    'Preserve all eight FCA causal-closure obligations, causal scope, evidence, dependencies, contradictory observations and promotion history. OVC is scoped operational knowledge, not universal Fact; STALE usability does not become an independent lifecycle.',
    'Prove evidence_refs, promoted_at, exact CausalScope and verification content through the approved records. Optional regression_verification_ref does not waive FCA technically-feasible durable regression duty.',
    'FCA-10 RDMS-02-M02-U017 RDMS-02-M02-U018 RDMS-02-M03-U007 RDMS-03-M05-U041')
finding('SHAPE-ProjectRuntime', 'C',
    'R1 explicitly provides ProjectHead, the atomic current-store/ledger boundary and separate durable ProjectStatus/process-local ProcessRuntimeMode. Only the aggregate embedding names remain unspecified; there is no missing authority or recovery state definition.',
    'One authoritative ControlTransaction atomically advances current state and replay/control records. ProjectHead carries the legal head/epoch/schema/status. Startup resets process mode and requires RecoveryBarrier before READY. Never persist READY as durable project truth.',
    'ProjectRuntime aggregate member names, class layout and lookup arrangement. These cannot merge ProjectStatus with ProcessRuntimeMode or create a second control head.',
    'RDMS-01-M01-U000 RDMS-01-M01-U001 RDMS-01-M01-U002 RDMS-01-M01-U023')
finding('PARENT-QueryDependencyStamp', 'B',
    'The query kinds and frontier fields agree. The invalidation_rule is inline in FCA and referenced in RDMS-06; an exact identity/content/version binding is not established by equal-sounding names.',
    'Retain query, query kind, proof scope, dependency frontier, index kind/generation/hash where present, invalidation rule and repository basis. Negative knowledge cannot exceed proved coverage.',
    'Prove invalidation_rule_ref preserves the exact invalidation rule with the required scope and historical/reference integrity. This is a freshness correctness proof, not just member naming.',
    'FCA-70 RDMS-06-M12-U054 RDMS-06-M12-U055 RDMS-06-M12-U056')
finding('SHAPE-ResumeAssessment', 'B',
    'C01-38 adds context, reconciliations and Goal/Slice validity while retaining result meanings. It does not explicitly prove preservation of the earlier unresolved_action_refs and created_commit_seq through those aggregates. Scope completeness is recovery-critical.',
    'Assess current repository/world/environment context, every relevant unresolved action and its reconciliation, dependency evaluation and Goal/Slice validity. Retain assessment identity, capsule, basis and canonical history. RESUMABLE permits cognition, not world mutation.',
    'Prove baseline current_repo_ref/current_world_ref, unresolved_action_refs and created_commit_seq remain recoverable. A list of reconciliation refs alone cannot prove that all relevant unresolved actions were considered.',
    'RDMS-05-M09-U046 RDMS-05-M10-U046 RDMS-05-M10-U047 RDMS-05-M10-U049 RDMS-05-M10-U050')
finding('SHAPE-ResumptionCapsule', 'B',
    'C01-34 supplies durable payload and integrity references, not an explicit content crosswalk for every earlier context member. relevant_entity_refs and canonical_snapshot_ref do not by themselves prove retained context coverage. L6 sole ownership is already settled.',
    'Retain all source-required suspension context, canonical/repository/world/environment basis, dependencies, focus, claims/hypotheses/evidence/decisions, rejected paths, slices/actions, unknowns, commitments and temporary changes. Verify durable payload before atomic suspension; a capsule never authorizes replay of an old action.',
    'Field/payload preservation proof for original project/context/basis collections and their versions. No new payload schema, snapshot alias or field embedding is selected.',
    'FCA-53 RDMS-05-M09-U040 RDMS-05-M09-U041 RDMS-05-M10-U042 RDMS-05-M10-U043 RDMS-05-M10-U044')
finding('PARENT-ResumptionCapsule', 'B',
    'The FCA goal/subgoal, current focus, repo basis, created time and contextual arrays are mandatory architectural information. The compact amended capsule does not prove they are present merely by holding a payload/snapshot reference.',
    'Preserve every FCA suspension-context category and timestamp plus all non-superseded RDMS additions. Restore canonical state, evaluate changes and stale dependencies, reconcile relevant actions and then resume through Executive authority.',
    'Prove task/goal/subgoal, base_state_version, repo_ref, focus, hypotheses/evidence/rejected paths/temporary changes/open needs, optional next action and created_at in the frozen referenced content. Do not equate created_at to a sequence number.',
    'FCA-53 RDMS-05-M09-U040 RDMS-05-M09-U043 RDMS-05-M10-U042 RDMS-05-M10-U046')
finding('SHAPE-Risk', 'D',
    'C01-30 is explicitly an abbreviated scoped amendment: status is split into lifecycle and treatment, with current_assessment_ref added. The ellipsis cannot erase unrelated original fields. The source therefore determines a conservative complete overlay without a guessed state migration.',
    'Retain risk_id, statement, scope, category, likelihood, impact, affected_refs, mitigation_refs, evidence_basis_refs, owner_ref and accepted_by_decision_id. Replace the single status with the exact C01 lifecycle/treatment enums and add current_assessment_ref. RiskAssessment freshness remains derived; acceptance is a Decision, not elimination of risk.',
    'No old-status-to-new-pair converter or inline likelihood/impact-to-assessment alias is approved. These historical conversions require source-compatible conformance evidence; they do not prevent publishing the current scoped fields.',
    'RDMS-02-M02-U045 RDMS-02-M02-U046 RDMS-02-M03-U029 RDMS-02-M03-U030', correction='Apply only the explicit lifecycle/treatment overlay and retain every unrelated baseline field.')
finding('PARENT-SandboxActivityRecord', 'B',
    'The sandbox proof and snapshot references are explicit, but the parent result has no approved equivalence to activity_summary or completed_at. A completed activity is not necessarily a successful or effect-verified activity.',
    'Retain activity/Slice identity, base snapshot, proven containment, operation count, output and observation references and actual result. Sandbox completion cannot authorize artifact promotion.',
    'Prove containment_profile/base_snapshot/output_refs and especially result survive in the current record/proof/artifacts. Do not replace result with a prose summary or completion time.',
    'FCA-45 RDMS-04-M06-U052 RDMS-04-M06-U054 RDMS-04-M06-U055')
finding('PARENT-Slice', 'B',
    'C01 explicitly resolves SliceState decomposition and scoped freshness. It does not expressly waive parent rollback information or prove all inline engineering/change-surface information through the later reference specimen.',
    'Retain engineering scope, preconditions, pinned invariants/contracts, expected/actual effects and change surface, risk, proof, verification and rollback obligations. Keep stage/condition/terminal independent and use dependency freshness rather than global version alone.',
    'Prove mandatory rollback versus rollback_spec?, risk_profile versus risk_refs, dependencies and inline expected-change-surface information. No automatic status-to-SliceState migration is chosen.',
    'FCA-29 RDMS-02-M02-U048 RDMS-02-M03-U020 RDMS-02-M03-U024 RDMS-02-M03-U017')
finding('SHAPE-State', 'C',
    'FCA section 6 gives logical groups; Appendix D expands a composite state view. RDMS defines the actual entity ownership and current replacements. A grouped view need not itself be a second canonical aggregate with a competing schema.',
    'Preserve access to all FCA logical categories and control references through their actual owners. Use GoalPath, derived validity and source-owned records. A State view cannot commit, redefine lifecycle or claim a separate recovery authority.',
    'Composite view nesting, physical tables, joins and serializer layout. This does not defer any underlying entity field question; those remain individually classified.',
    'FCA-6 RDMS-02-M03-U009 RDMS-02-M03-U032 RDMS-10-M24-U010')
finding('SHAPE-TemporalSchedule', 'B',
    'C01 hardens timezone/DST/discontinuity policies but its complete specimen omits original instant/local rule and validity bounds. Those specify which occurrence is legal and cannot be deferred as mere serialization.',
    'Preserve schedule kind, intended instant/local/recurring rule and not-before/valid-until bounds, timezone and rules version, DST/missed-occurrence/discontinuity policy. Legal occurrence identity must not depend on worker processing time.',
    'Prove absolute_instant, local_time_rule, not_before and valid_until are retained by the effective schedule/occurrence contracts; no field alias or new scheduling law is selected.',
    'RDMS-05-M09-U006 RDMS-05-M10-U030 RDMS-05-M10-U031 RDMS-05-M10-U032 RDMS-05-M10-U033')
finding('PARENT-TemporalValidity', 'D',
    'The six field names and optionalities are identical. The three freshness symbols differ only in capitalization, and RDMS-05 section 38 explicitly preserves the FCA concept while stating that freshness is derived. There is no missing field or lifecycle mapping.',
    'Retain observed_at?, verified_at?, repo_ref?, state_version?, valid_until_condition? and CURRENT/STALE/UNKNOWN freshness. Use the canonical dependency engine; the Scheduler cannot assert authoritative freshness.',
    'Serializer capitalization only; no independent freshness field authority.',
    'FCA-54 RDMS-05-M09-U049 RDMS-05-M09-U050')
finding('SHAPE-ToolResult', 'C',
    'The only declaration is explicitly an example exit_code = 0, used to demonstrate that a report does not establish reality. RDMS-04 ToolAdapter has output_schema_ref; ProcessRun, ActionAttempt and Observation already define binding semantics. The example is not an incomplete mandatory canonical ToolResult schema.',
    'Keep reported output attributed to its actual attempt/process/source; preserve output completeness/integrity and capture it through Observation Ingress. Exit code zero does not prove the requested effect; OutcomeProbe/reconciliation still apply.',
    'Adapter-specific result representation and output serializer under output_schema_ref. No new canonical ToolResult entity, success lifecycle or dispatch authority is created.',
    'RDMS-04-M06-U015 RDMS-04-M06-U020 RDMS-04-M06-U062 RDMS-04-M06-U071 RDMS-04-M07-U039')
finding('PARENT-TriggerCondition', 'B',
    'RDMS-05 section 6 expressly splits repetition and detection dimensions; section 13 preserves conceptual trigger states and separates evaluation/fire/reaction. The remaining FCA last_evaluated_at/last_fire_id/source/watch and reaction associations still need a complete information-preservation crosswalk.',
    'Retain trigger identity/generation, both semantics dimensions, watched sources/predicate, cursor, reaction identity, linked object, on-fire semantics, conceptual state and evaluation/fire history. L4 evaluates; it never authorizes a world action.',
    'Prove each original field through TriggerDefinition, condition, state/evaluation, fire and reaction records, especially timestamps and last-fire relation. No condition-state or time-to-commit alias is invented.',
    'FCA-56 RDMS-05-M09-U008 RDMS-05-M09-U016 RDMS-05-M10-U015 RDMS-05-M10-U018')
finding('SHAPE-TriggerFire', 'D',
    'C01-12/13/14 explicitly replace unstable fire construction with immutable definition and qualified occurrence references plus a uniqueness tuple. C01-06 binds canonical processing atomically. This is the approved current native fire surface; old direct trigger/generation/condition fields are retained by the frozen definition/occurrence semantics rather than competing mutable copies.',
    'Use the exact C01-14 fields. The definition and occurrence bind the trigger and generation; preserve immutable condition/reaction identity, evidence basis and source frontier. Enforce uniqueness of trigger_id/generation/occurrence_key; replay returns the same Fire. The canonical creation sequence is not the source event time.',
    'No old-record importer or fired_at_commit_seq/created_commit_seq wire alias is invented. Source occurrence time and canonical processing order remain distinct.',
    'RDMS-05-M09-U027 RDMS-05-M10-U007 RDMS-05-M10-U015 RDMS-05-M10-U016 RDMS-05-M10-U017', correction='Publish the approved stable TriggerFire record and its source-defined identity/atomicity requirements.')
finding('SHAPE-TriggerReaction', 'B',
    'C01-29 supplies target-version/lifecycle admission and C01-15 the stable reaction identity. The relationship of old reaction_kind/reaction_key to frozen_reaction_spec_ref/reaction identity is not a complete declared field mapping. Deduplication is legally mandatory.',
    'Preserve the frozen reaction kind, target, stable reaction identity/key and exact trigger definition generation. Apply legal target transition, APPLIED and key consumption in one ControlCommit. Worker reclaiming is not a second effect or action authority.',
    'Prove all original reaction_kind/key semantics through the frozen spec and C01 identity without guessing a key alias or hash serialization. C01 target-bound statuses govern current admission; source history remains intact.',
    'RDMS-05-M09-U029 RDMS-05-M09-U030 RDMS-05-M10-U018 RDMS-05-M10-U036 RDMS-05-M10-U037 RDMS-05-M10-U039')
finding('SHAPE-TriggerSourceCursor', 'C',
    'C01-05 explicitly replaces the conflated cursor concept with two different frontiers and defines exactly when each may advance. The remaining question is how to embed these already distinct contracts. Position meaning is explicitly delegated to the source adapter, not guessed globally.',
    'IngressCursor tracks durable source capture; TriggerProcessingCursor tracks durable evaluation and required Fire/Reaction or deferred evaluation obligations. Neither can outrun its own durable frontier. Retain source generation, adapter-defined position and coverage semantics.',
    'Member names, physical cursor tables, position serialization and aggregate embedding. Never defer the capture/processing distinction, acknowledgement fence, coverage or atomicity.',
    'RDMS-05-M09-U023 RDMS-05-M10-U005 RDMS-05-M10-U006 RDMS-05-M10-U007')
finding('CE-01', 'B',
    'FCA says each canonical event includes at least event_id/schema_version/idempotency_key; R1 adds event_type_version and separates schema dimensions. These requirements can coexist, so this is not a proved contradiction. R1 does not explicitly waive the two FCA members or equate them with enclosing commit metadata.',
    'Preserve event_id, schema_version and idempotency_key for every canonical event, alongside R1 event type/version, ordinal and payload. Preserve ControlCommit control_schema_version, command idempotency_key/fingerprint and immutable events. Do not conflate event, payload, control and snapshot codec versions.',
    'Prove event metadata inclusion/resolution and its exact scope. No schema_version = event_type_version/control_schema_version or event key = enclosing commit key is approved. The original warning is narrowed to this precise binding proof.',
    'FCA-48 RDMS-01-M01-U004 RDMS-01-M01-U009 RDMS-01-M01-U015 RDMS-01-M01-U016')
finding('HG-01', 'E',
    'C01 removes scalar Hypothesis.support and uses a shared SupportAssessment level vocabulary. C01-07 and RDMS-03 C01-42 resolve OVC closure authority, but no clause supplies the complete ordinary CONFIRMED/REJECTED admission correspondence from the earlier support combinations. This affects a legal transition; it cannot be deferred to a serializer.',
    'Keep immutable assessments and derived validity, one Hypothesis lifecycle, historical closure precursor and the full Causal Closure Gate. STRONG and REFUTED are present in both vocabularies, but that fact is not a complete new admission table; generic VERIFIED is not automatically causal verification.',
    'Smallest decision: ratify the effective support-assessment predicates for ordinary CONFIRMED/REJECTED admission after C01, including validity and whether VERIFIED satisfies the old minimum. Do not reopen OVC gate or invent weaker support thresholds.',
    'RDMS-02-M02-U014 RDMS-02-M02-U015 RDMS-02-M03-U001 RDMS-02-M03-U002 RDMS-02-M03-U006 RDMS-03-M05-U041',
    decision_alternatives=[
        dict(option='Ratify a minimal shared-level admission rule', consequence='Explicitly retain the known STRONG/REFUTED obligations and specify treatment of the remaining new assessment levels/validity. This supplies a new approved legal guard; an implementation cannot choose it.'),
        dict(option='Ratify a complete legacy-to-assessment correspondence', consequence='Specify each relevant old support meaning and the predicates supporting ordinary closure under C01; preserves interpretable historical transitions but requires a broader approved crosswalk.')],
    affected_layers=['L2', 'L3', 'L1'], affected_interfaces=['X8-07', 'X8-08'])
finding('TRANSPORT-CapabilityResult', 'B',
    'The canonical payload has patch, typed propositions, needs, evidence, assessments, specialist request and rationale categories missing as literal members of the RDMS-10 envelope. FC10-03-08 forbids redefinition, and the final registry limitation expressly leaves field audit necessary. proposal_refs is not evidence that all payload survives.',
    'Retain all eleven FCA result categories with optionality, types, provenance, dependencies and immutable identity/version when required. Only the Executive adopts cognition; delivery cannot authorize commits/actions.',
    'Produce a lossless payload/reference projection proof for each canonical field, particularly specialist_request, needs, rationale_summary and evidence_refs. No new attachment field or field alias is selected.',
    'FCA-23 RDMS-10-M23-U012 RDMS-10-M24-U007 RDMS-10-M24-U008 RDMS-10-M26-U023 RDMS-10-M26-U028')
finding('TRANSPORT-MemoryRetrievalResult', 'B',
    'The transport envelope does not literally include canonical retrieval/query identity, omitted scope, ranking policy, coverage, freshness or creation time. Memory and transport meanings may coexist, but trust annotations do not prove those retrieval facts are carried.',
    'Retain retrieval_id, query_ref, candidate_refs, omitted_or_filtered_scope, ranking_policy_ref, retrieval_coverage, freshness_summary and created_at plus transport trust/provenance/applicability. Retrieval never promotes truth or grants disclosure.',
    'Produce a lossless reference/payload projection for every canonical retrieval field. Do not equate memory_refs with candidate_refs or provenance with coverage without source-compatible proof.',
    'RDMS-07-M14-U074 RDMS-10-M23-U046 RDMS-10-M24-U007 RDMS-10-M26-U023 RDMS-10-M26-U028')

CLASS_NAMES = {'A': 'NORMATIVE_CONFLICT', 'B': 'LOSSLESS_MAPPING_REQUIRED',
    'C': 'IMPLEMENTATION_DETAIL_DEFERRED', 'D': 'ALREADY_RESOLVED',
    'E': 'EXPLICIT_ARCHITECTURAL_DECISION_REQUIRED'}
