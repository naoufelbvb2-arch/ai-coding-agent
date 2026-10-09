# Operative interface schemas and source-bound admission — candidate

**Status: ARCHITECTURE-LEVEL CONSOLIDATION CANDIDATE; NO PRODUCTION CODE AUTHORIZED.**
Source-owned names and source-spelled fields are listed below. The two transport aliases are editorial collision resolutions from GAIA-C03; they do not amend frozen source documents.
A field marked `[]` is a collection, `?` optional; missing primitive types are not inferred. This is a field-surface contract, not a wire-format or implementation signature.

## A. Full interface admission contracts

### X8-01 — Capability invocation / result
**Owner:** L7_RUNTIME_INTEGRATION.md; **route:** L2 → L7 → L2
**Inputs:** CapabilityInvocation; **outputs:** CapabilityResult
**Transport-only aliases:** CapabilityTransportResult
**Supporting legal types:** CapabilityActivationContract, ExecutiveTransitionIntegrationBinding
**Admitting authority:** L2 Cognitive Executive proposes; only authorized Control CommitGate can adopt legal state.
**Preconditions:** invocation/context/dependency identity valid; capability activated and budget/scope accepted; transport provenance resolves to original cognitive result.
**Reject:** unactivated capability; unresolved provenance; identity or epoch mismatch; tool response pretending to be a canonical decision.
**Transactional boundary:** No provider or transport result is itself a canonical commit.
**Recovery/retry:** Repeated or late invocation results must be fenced/deduplicated under canonical authority.
**Canonical/transport rule:** RDMS-10 transport list is not FCA §23 CapabilityResult; only source-bound dereference and executive/CommitGate admission can form canonical cognitive state.
**Frozen governing norms:** FCA §23, §48–52; RDMS-10 capability activation and executive transition bindings.

### X8-02 — Memory retrieval and re-use
**Owner:** L5_MEMORY.md; **route:** L5 → L7 → L2
**Inputs:** MemoryRetrievalRequest; **outputs:** MemoryRetrievalResult
**Transport-only aliases:** MemoryRetrievalTransportResult
**Supporting legal types:** MemoryRetrievalCoverage, MemoryUseAssessment
**Admitting authority:** L5 owns retrieval evidence and use constraints; L2 owns cognitive incorporation; L7 conveys only.
**Preconditions:** scope, coverage, provenance, applicability and freshness available from legal retrieval result; access policy respected.
**Reject:** short list falsely asserted exhaustive; missing coverage/freshness; access/scope mismatch; transport alias not dereferenceable.
**Transactional boundary:** Retrieval or ranking does not mutate belief or authorize learning.
**Recovery/retry:** Replay keeps retrieval/query identity; stale results re-assessed before use.
**Canonical/transport rule:** RDMS-07 result owns query, ranking, omissions, coverage, freshness; RDMS-10 return cannot overwrite this and must resolve to canonical evidence.
**Frozen governing norms:** RDMS-07 retrieval coverage/use assessment; RDMS-10 memory transport.

### X8-03 — Commitment / reactivation
**Owner:** L2_COGNITION.md; **route:** L2 → L4 → L1
**Inputs:** Commitment, TriggerCondition; **outputs:** TriggerDerivedWorkCommitment
**Transport-only aliases:** none
**Supporting legal types:** ExecutiveTransitionIntegrationBinding
**Admitting authority:** L2 owns commitment semantics; L4 determines temporal eligibility; L1 owns legal mutation.
**Preconditions:** single lawful reactivation condition root and valid target identity/lifecycle; derived work durably attributable to commitment.
**Reject:** legacy timestamp or trigger aliases fabricated; activation treated as satisfaction; stale or already retired commitment.
**Transactional boundary:** Activation and accepted derived-work obligation require canonical durable transition before downstream work.
**Recovery/retry:** Idempotent processing keyed to durable source and target; no action authority from trigger.
**Canonical/transport rule:** Use source-owned contract directly; no adapter or implicit schema migration.
**Frozen governing norms:** RDMS-02 C01-32; RDMS-05 trigger-derived work; RDMS-10 C02.

### X8-04 — Trigger firing and actions
**Owner:** L4_TEMPORAL_SPECIALISTS.md; **route:** L4 → L1 → L3
**Inputs:** TriggerDefinition, TriggerFire; **outputs:** TriggerReaction
**Transport-only aliases:** none
**Supporting legal types:** DispatchAdmissionCutover, TriggerActionCausalityBinding
**Admitting authority:** L4 evaluates conditions; L1 validates and commits durable reaction; L3 requires independent ActionGate.
**Preconditions:** definition snapshot/generation/qualified occurrence verified; target version and reaction are current.
**Reject:** duplicate fire; obsolete target; invalid trigger generation; reaction directly dispatching an external mutation.
**Transactional boundary:** Reaction/target transition obey ControlCommit atomicity and durable identity.
**Recovery/retry:** Reaction remains inspectable, replay-safe, and cannot be mistaken for an external effect.
**Canonical/transport rule:** Use source-owned contract directly; no adapter or implicit schema migration.
**Frozen governing norms:** RDMS-05 C01 TriggerFire/TriggerReaction; RDMS-10 TriggerActionCausalityBinding.

### X8-05 — Suspension / resumption
**Owner:** L6_RECOVERY.md; **route:** L4 → L6 → L1
**Inputs:** ResumptionCapsule; **outputs:** RecoverySuspensionCommitment
**Transport-only aliases:** none
**Supporting legal types:** BootstrapHandoffProof, RecoveryAdmissionBinding
**Admitting authority:** L6 validates restoration and containment; L1 owns admission and epoch fencing.
**Preconditions:** full durable capsule payload is integrity-checked and consistent with pinned state, identity, authority, and epoch.
**Reject:** truncated historical conversion; absent payload verification; stale/missing handoff or authority; fabricated field defaults.
**Transactional boundary:** Suspension/resumption creates no implied world rollback.
**Recovery/retry:** IN_DOUBT effects reconcile before further shared-world mutation.
**Canonical/transport rule:** Use source-owned contract directly; no adapter or implicit schema migration.
**Frozen governing norms:** RDMS-09 recovery; RDMS-10 BootstrapHandoffProof/RecoveryAdmissionBinding.

### X8-06 — External execution and journal
**Owner:** L3_ACTIONS.md; **route:** L2 → L3 → L1
**Inputs:** ActionProposal, SealedExecutionIntent; **outputs:** ActionRecord, ActionDeliveryContract
**Transport-only aliases:** none
**Supporting legal types:** DispatchAdmissionCutover, EffectiveExecutionBinding, RecoverableActionDeliveryObligation
**Admitting authority:** L3 ActionGate approves exact shared-world mutation; executor cannot change effective command or scope; L1 records legal transitions.
**Preconditions:** authorization matches exact effective operation/arguments/target, resource versions and current policy/dependency/epoch frontier.
**Reject:** unsealed or modified command; stale authority; missing durable dispatch intent; blind retry of unknown non-idempotent effect.
**Transactional boundary:** Persist DISPATCH_INTENT before effect. Ledger atomicity != atomic external side effect; durable Action Journal/reconciliation required.
**Recovery/retry:** Mark IN_DOUBT and probe/reconcile; do not assert exactly-once without external guarantee.
**Canonical/transport rule:** Use source-owned contract directly; no adapter or implicit schema migration.
**Frozen governing norms:** FCA §42–47, §48–52; RDMS-04 C01; RDMS-10 C01/C02.

### X8-07 — Observation and evidence
**Owner:** L3_ACTIONS.md; **route:** L3 → L2 → L1
**Inputs:** Observation, ContentTrustContext; **outputs:** EvidenceLink, ObservationCausalAttachmentContract
**Transport-only aliases:** none
**Supporting legal types:** FactGrounding, ObservationSourceBinding
**Admitting authority:** L3 ingests provenance and trust; L2 decides epistemic use; L1 gates legal writes.
**Preconditions:** source/trust context travels with observation; observed content preserved as immutable; causal attachment separately justified.
**Reject:** tool self-report promoted to certainty; untrusted content granting authority; disagreement mislabeled capture corruption.
**Transactional boundary:** Append accepted observation and source binding; separate append from causal inference.
**Recovery/retry:** Amend only capture/provenance defects with traceable amendment; keep original observation.
**Canonical/transport rule:** Use source-owned contract directly; no adapter or implicit schema migration.
**Frozen governing norms:** FCA §75–76; RDMS-03 C01 observation trust/amendment; RDMS-10 C01/C02.

### X8-08 — Experiment and causal verification
**Owner:** L3_ACTIONS.md; **route:** L2 → L3 → L2
**Inputs:** Experiment, Prediction; **outputs:** ExperimentRun, VerificationRecord
**Transport-only aliases:** none
**Supporting legal types:** ExperimentDesignSnapshot
**Admitting authority:** L2 owns hypothesis/causal decision; L3 performs authorized experiment and independent observation.
**Preconditions:** frozen design and prediction predate intervention; run/evidence attached to exact design and target.
**Reject:** post-hoc prediction substituted; experiment-design state conflated with run outcome; simulated result treated as verified reality.
**Transactional boundary:** External experiments remain subject to ActionGate and Action Journal.
**Recovery/retry:** Unknown partial intervention remains unresolved until observation/probe.
**Canonical/transport rule:** Use source-owned contract directly; no adapter or implicit schema migration.
**Frozen governing norms:** RDMS-03 experiment vs run; FCA causal hypothesis and evidence gates.

### X8-09 — Contradiction and reality mismatch
**Owner:** L3_ACTIONS.md; **route:** L3 → L2
**Inputs:** Claim; **outputs:** ContradictionRecord
**Transport-only aliases:** none
**Supporting legal types:** OperationalCausalClaim
**Admitting authority:** L2 controls epistemic assessment; L3 sources observations, not causal truth.
**Preconditions:** observations comparable in explicit scope/dimensions with traceable evidence and unresolved/resolved proof.
**Reject:** UNRESOLVED silently mapped to RESOLVED; hypothesis dismissed solely due conflicting observation; causal explanation invented.
**Transactional boundary:** Contradiction transition needs legal state/sequence and supporting references.
**Recovery/retry:** Keep prior inconsistent evidence and lifecycle history; correction must be attributable.
**Canonical/transport rule:** Use source-owned contract directly; no adapter or implicit schema migration.
**Frozen governing norms:** RDMS-03 C01 contradiction and observation rules; FCA epistemic distinctions.

### X8-10 — Freshness and completion
**Owner:** L4_TEMPORAL_SPECIALISTS.md; **route:** L4 → L2 → L1
**Inputs:** DependencySet, DependencyCaptureReceipt; **outputs:** DependencyAttestation, IntegratedCompletionEvidence
**Transport-only aliases:** none
**Supporting legal types:** CompletionStateBinding
**Admitting authority:** L4 specialist/dependency layer attests freshness; L2 judges completion; L1 adopts legal goal state.
**Preconditions:** dependency coverage and policy/versions attested for exact operation; completion proof matches goal acceptance contract.
**Reject:** PARTIALLY_STALE treated as VALID; generic success text treated as task completion; missing dependency frontier.
**Transactional boundary:** Completion or focus change requires epoch/version-fenced canonical commit.
**Recovery/retry:** Invalidate derived work on changed dependencies; re-evaluate at admission.
**Canonical/transport rule:** Use source-owned contract directly; no adapter or implicit schema migration.
**Frozen governing norms:** FCA §71; RDMS-06 freshness; RDMS-08 completion proof.

### X8-11 — Learning and context egress
**Owner:** L7_RUNTIME_INTEGRATION.md; **route:** L3 → L5 → L7
**Inputs:** MemoryProposal, SealedOutboundContext; **outputs:** LearningAuthorizationBinding, ContextDisclosureAdmission
**Transport-only aliases:** none
**Supporting legal types:** MemoryRetrievalCoverage
**Admitting authority:** L5 learning policy and L1/CommitGate own durable memory acceptance; L7 only transports sealed outbound content.
**Preconditions:** memory promotion separately authorized; outbound effective bytes/destination/context scope sealed and policy-approved.
**Reject:** automatic learning from agent suggestion; sending unapproved private context; destination/payload changed after authorization.
**Transactional boundary:** No memory state change without canonical commit; no egress without policy admission.
**Recovery/retry:** After restart, replay only scoped authorization; reject stale outbound binding.
**Canonical/transport rule:** Use source-owned contract directly; no adapter or implicit schema migration.
**Frozen governing norms:** RDMS-07 learning; RDMS-10 C01/C02 context disclosure.

### X8-12 — Containment and recovery
**Owner:** L6_RECOVERY.md; **route:** L3 → L6 → L1
**Inputs:** PossibleExternalEffectAssessment, RestoreContainmentProof; **outputs:** CrossFrontierAdmissionProof
**Transport-only aliases:** none
**Supporting legal types:** RecoveryBootstrapContract, RecoveryOwnershipLease
**Admitting authority:** L6 validates containment/uncertain effects; L1 authorizes safe resumption under epoch.
**Preconditions:** isolation claim evidenced, uncertain effects reconciled or explicitly guarded, ownership lease valid.
**Reject:** snapshot restore asserted to reverse external world; unverified isolation; old worker keeps authorization.
**Transactional boundary:** Canonical recovery commit fences old authority; no global rollback of external effects.
**Recovery/retry:** Reconcile IN_DOUBT before new mutation; persist recovery basis and admission evidence.
**Canonical/transport rule:** Use source-owned contract directly; no adapter or implicit schema migration.
**Frozen governing norms:** RDMS-09 C01/C02/C03, RDMS-10 recovery bindings.

## B. Source-derived field surfaces

Nothing here authorizes a conversion from the historical truncated record forms. The exact full frozen clauses remain controlling.

### ActionDeliveryContract
**Source:** RDMS-10 / C01; **declared name:** `ActionDeliveryContract`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `d9771caf5be03c5c6995858af38e0539561a2f4975711c59d1e28db84713003f`
```text
ActionDeliveryContract {
    action_ref
    delivery_identity
    execution_attempt_identity
    dispatch_intent_ref
    sealed_execution_intent_ref
    receiving_worker_identity
    receiving_worker_generation
    retry_policy_ref
    delivery_deduplication_scope
    acknowledgement_semantics
    possible_external_effect_status
    required_reconciliation_ref?
}
```

### ActionProposal
**Source:** RDMS-04 / Original draft; **declared name:** `ActionProposal`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `1d1d2dfa1eaacd278ba44f59a1e7c5a2807b8f4e22cd867864b3688ac7587273`
```text
ActionProposal {
    action_proposal_id
    project_id
    requested_by_ref
    goal_id
    slice_id
    action_kind
    requested_action_class
    intent
    target_scope[]
    expected_effects[]
    preconditions[]
    base_repo_ref?
    base_world_ref?
    dependency_set_ref?
    risk_profile_ref?
    reversibility
    compensation_plan_ref?
    effect_semantics_ref
    execution_spec_ref
    mode
}
```

### ActionRecord
**Source:** RDMS-04 / Original draft; **declared name:** `ActionRecord`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `b04404a6eafcf8aec73c83958aa5553aca3762a62a892c1cc8e857d5f0e3f386`
```text
ActionRecord {
    action_id
    proposal_ref
    authorization_ref
    action_class
    lifecycle
    world_ref_before?
    repo_ref_before?
    effect_semantics_ref
    latest_attempt_ref?
    world_ref_after?
    repo_ref_after?
    effect_verification_refs[]
    compensation_action_ref?
    created_commit_seq
    updated_commit_seq
}
```

### BootstrapHandoffProof
**Source:** RDMS-09 / C03; **declared name:** `BootstrapHandoffProof`; **owner:** `L6_RECOVERY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `01cc1a26ba1a3cc33acd111480bd8dba1b4eecc380f0e4ef4f4f07ac40d31b8c`
```text
BootstrapHandoffProof {
    bootstrap_case_ref
    recovery_principal_ref
    verified_authority_ref
    authorized_bootstrap_scope
    initial_resource_frontier
    performed_operations[]
    modified_resource_refs[]
    created_resource_refs[]
    replaced_resource_refs[]
    unknown_change_scope[]
    restoration_evidence_refs[]
    final_resource_frontier
    audit_completeness
    canonical_handoff_status
}
```

### CapabilityActivationContract
**Source:** RDMS-10 / C01; **declared name:** `CapabilityActivationContract`; **owner:** `L7_RUNTIME_INTEGRATION.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `026bb25fd353ffcabaa2ba4b1a5e101238efb218e9af666701f6045a6ccd9282`
```text
CapabilityActivationContract {
    capability_ref
    intended_operational_scope
    required_component_refs[]
    required_invariant_proofs[]
    required_conformance_tests[]
    prohibited_effects_until_activation[]
    activation_policy_ref
    activation_decision
}
```

### CapabilityInvocation
**Source:** RDMS-10 / Original draft; **declared name:** `CapabilityInvocation`; **owner:** `L7_RUNTIME_INTEGRATION.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `8fec5e274ffc9f94b0bbde0178edb4b6fdcfe0241105dd079e62d1f954b26ccd`
```text
CapabilityInvocation {
    invocation_id
    capability_kind
    goal_ref
    cognitive_context_ref
    dependency_set_ref
    provider_policy_ref?
    resource_budget_ref
    requested_outputs[]
}
```

### CapabilityResult
**Source:** FCA v1.0.1 / FROZEN §23; **declared name:** `CapabilityResult`; **owner:** `L2_COGNITION.md`
**Status:** CANONICAL_COGNITIVE_RESULT; **SHA-256 of declaration:** `b60b418b16f38240fec6c0be2929b5701ef1cbb2d8c59cf0014fb6bf2fb26e4a`
```text
CapabilityResult {
    patch_proposal?
    proposed_claims[]
    proposed_hypotheses[]
    proposed_information_needs[]
    evidence_refs[]
    tool_requests[]
    experiment_requests[]
    confidence_assessment?
    specialist_request?
    needs[]
    rationale_summary?
}
```

### CapabilityTransportResult
**Source:** RDMS-10 / Original draft; **declared name:** `CapabilityResult`; **owner:** `L7_RUNTIME_INTEGRATION.md`
**Status:** NONCANONICAL_TRANSPORT_ALIAS__SOURCE_NAMING_COLLISION_CLOSED; **SHA-256 of declaration:** `e8ae9d35f870fc3efb84694641074038fd2961677393b2a5f5ee6d6f0cb717b5`
```text
CapabilityTransportResult {
    invocation_id
    proposal_refs[]
    information_need_refs[]
    tool_request_refs[]
    experiment_request_refs[]
    assessment_refs[]
    dependency_set_ref
    provenance_refs[]
    result_status
}
```

### Claim
**Source:** RDMS-02 / Original draft; **declared name:** `Claim`; **owner:** `L3_ACTIONS.md`
**Status:** CURATED_SOURCE_DECISION; **SHA-256 of declaration:** `0cc9ca22709f89fa2ed2187d5495b91a57d92b5beb04229b530afce7b69d7a45`
```text
Claim {
    claim_id
    kind
    statement
    scope
    support
    support_assessed_at_commit?
    grounding?
    dependency_set_ref?
    temporal_validity?
    status
    superseded_by?
}
```

### Commitment
**Source:** RDMS-02 / Original draft; **declared name:** `Commitment`; **owner:** `L2_COGNITION.md`
**Status:** CURATED_RDMS02_C01_SUPERSESSION_APPLIED; **SHA-256 of declaration:** `da8ac753225c695d17105d549b2d3eca57f648d2343a84a0a8daefc58e46fce9`
```text
Commitment {
    commitment_id
    statement
    why_temporary
    scope
    owner_ref?
    linked_entity_refs[]
    created_at
    reactivation_condition_ref
    status
    resolution_ref?
}
```

### CompletionStateBinding
**Source:** RDMS-10 / C02; **declared name:** `CompletionStateBinding`; **owner:** `L4_TEMPORAL_SPECIALISTS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `fa6057f2f9c27814e892375aa6f9af148e8edcf0abcb5239dce4d4210d87b515`
```text
CompletionStateBinding {
    goal_ref
    goal_version
    acceptance_criteria_frontier
    verified_repository_ref
    verified_world_state_scope
    verification_evidence_refs[]
    dependency_validation_ref
    relevant_policy_frontier
    unresolved_obligation_refs[]
    finalization_commit_preconditions[]
    finalization_commit_ref?
}
```

### ContentTrustContext
**Source:** RDMS-03 / C01 and Freeze Review 02 Final; **declared name:** `ContentTrustContext`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `e23cfcddd8eb07ae9047a8525c20108715194aba476cb801827b2462f1e6432e`
```text
ContentTrustContext {
    trust_context_id
    content_role
    instruction_authority
    source_trust_class
    domain_authority_binding_ref?
    created_commit_seq
}
```

### ContextDisclosureAdmission
**Source:** RDMS-10 / C01; **declared name:** `ContextDisclosureAdmission`; **owner:** `L7_RUNTIME_INTEGRATION.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `cf8ab1e0abe27665db71d9e9661c8a78dc07d830b2123480121809753ff8df72`
```text
ContextDisclosureAdmission {
    context_package_ref
    originating_project_ref
    destination_provider_ref
    requested_processing_purpose
    included_data_class_refs[]
    applicable_policy_frontier
    authorized_disclosure_scope
    prohibited_content_refs[]
    source_trust_refs[]
    effective_transfer_scope
    admission_status
}
```

### ContradictionRecord
**Source:** RDMS-03 / Original draft; **declared name:** `ContradictionRecord`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_COMPLETE_DECLARATION_WITH_OPTIONAL_OVERLAYS; **SHA-256 of declaration:** `e8e2641455efb82f3da738cfff8f716fcead8179e6b63ddbd46618cbc58948ed`
```text
ContradictionRecord {
    contradiction_id
    observation_refs[]
    subject_ref?
    subject_key?
    comparison_scope
    comparability
    dimension_analysis[]
    lifecycle
    information_need_id?
    explanation_ref?
    resolution_ref?
}
```

### CrossFrontierAdmissionProof
**Source:** RDMS-09 / C03; **declared name:** `CrossFrontierAdmissionProof`; **owner:** `L6_RECOVERY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `a3c71d0e55272f3b8ee54a710026eb0875282e7c0811e1dcdb4341a975dc9203`
```text
CrossFrontierAdmissionProof {
    admission_ref
    project_scope
    permitted_operation_classes[]
    executive_epoch
    canonical_state_ref
    policy_frontier_refs[]
    security_frontier_refs[]
    suppression_frontier_refs[]
    dependency_frontier_refs[]
    outstanding_effect_constraints[]
    compatibility_results[]
    required_revalidation_conditions[]
    applicable_gate_refs[]
    admission_status
}
```

### DependencyAttestation
**Source:** RDMS-06 / C01 and Adversarial Freeze Review 02 with freeze decision; **declared name:** `DependencyAttestation`; **owner:** `L4_TEMPORAL_SPECIALISTS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `2558385e10da2a9ead0dafaab139ad30b0fe45edb12ae06acd9ec6c36f013373`
```text
DependencyAttestation {
    dependency_ref
    observed_identity
    observed_version_or_hash
    source_read_context_ref
    trusted_capture_component_ref
    capture_time_or_commit_ref
    integrity_ref
}
```

### DependencyCaptureReceipt
**Source:** RDMS-06 / C01 and Adversarial Freeze Review 02 with freeze decision; **declared name:** `DependencyCaptureReceipt`; **owner:** `L4_TEMPORAL_SPECIALISTS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `d7ff97834f08dcd7e2556a12314b38b719619e9cec054f56018795a05827beba`
```text
DependencyCaptureReceipt {
    receipt_id
    subject_execution_or_reasoning_ref
    trusted_observed_reads[]
    trusted_index_queries[]
    trusted_tool_context_refs[]
    trusted_environment_refs[]
    declared_additional_dependencies[]
    capture_scope
    capture_coverage
    enforcement_basis_refs[]
    capture_fingerprint
}
```

### DependencySet
**Source:** RDMS-06 / Original draft; **declared name:** `DependencySet`; **owner:** `L4_TEMPORAL_SPECIALISTS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `f596f8c673ea27846249b5dcfa447baa4e251351ee006131cc0ae5688825d270`
```text
DependencySet {
    dependency_set_id
    owner_result_ref
    stamps[]
    derivation_context_ref?
    capture_frontier_ref?
    dependency_set_fingerprint
}
```

### DispatchAdmissionCutover
**Source:** RDMS-10 / C02; **declared name:** `DispatchAdmissionCutover`; **owner:** `L4_TEMPORAL_SPECIALISTS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `6c98bbb843273f8f952861c7c49cd7c8967d3780a4448fd801c529765879ca95`
```text
DispatchAdmissionCutover {
    action_ref
    executive_epoch
    originating_authorization_ref
    dispatch_intent_commit_ref
    dependency_frontier_ref
    current_dependency_assessment_ref
    current_policy_frontier_ref
    current_execution_generation
    admission_ordering_ref
    applicable_invalidation_refs[]
    effective_execution_binding_ref
    cutover_disposition
    possible_dispatch_assessment
}
```

### EffectiveExecutionBinding
**Source:** RDMS-10 / C02; **declared name:** `EffectiveExecutionBinding`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `d5c98f9d9e69edf753fbdda12922a0df68c67cc556e02990bb963f0a93601da1`
```text
EffectiveExecutionBinding {
    action_ref
    sealed_execution_intent_ref
    authorized_operation_kind
    adapter_identity
    adapter_integrity_ref
    effective_operation_ref
    effective_argument_integrity_ref
    resolved_target_resource_refs[]
    execution_environment_ref
    effective_execution_principal_ref
    authorized_effect_scope
    final_validation_ref
    dispatch_eligibility
}
```

### EvidenceLink
**Source:** RDMS-03 / Original draft; **declared name:** `EvidenceLink`; **owner:** `L3_ACTIONS.md`
**Status:** CURATED_SOURCE_DECISION; **SHA-256 of declaration:** `b56d24206ab7628d92c266e4a6d8c3e3a63aa29a627ede82c373819a56071e26`
```text
EvidenceLink {
    evidence_link_id
    observation_refs[]
    target_ref
    relation
    derivation
    rationale
    derivation_ref?
    dependency_set_ref?
    lifecycle
    accepted_commit_seq?
}
```

### ExecutiveTransitionIntegrationBinding
**Source:** RDMS-10 / C01; **declared name:** `ExecutiveTransitionIntegrationBinding`; **owner:** `L7_RUNTIME_INTEGRATION.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `74d692bfc0f33d9890f8b7bc9fbe3e4dae3b7563bd8d637370e7288527aa5c2e`
```text
ExecutiveTransitionIntegrationBinding {
    executive_decision_ref
    executive_epoch
    project_ref
    goal_ref
    slice_ref?
    source_cognitive_state
    selected_operation_ref
    expected_canonical_versions[]
    policy_frontier_ref
    dependency_frontier_ref
    target_transition_contract_ref
    control_commit_ref?
}
```

### Experiment
**Source:** RDMS-03 / Original draft; **declared name:** `Experiment`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `77b9d1f12e730ad6d94c444aef8d1dd545a8852df355849803557a8712ed4ea8`
```text
Experiment {
    experiment_id
    question
    purpose
    target_hypothesis_ids[]
    method_spec
    prediction_ids[]
    required_action_specs[]
    risk_refs[]
    lifecycle
    prediction_set_frozen_at_commit_seq?
}
```

### ExperimentDesignSnapshot
**Source:** RDMS-03 / C01 and Freeze Review 02 Final; **declared name:** `ExperimentDesignSnapshot`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `fbdf6d6301d7fa360c4f13c7ffbc2cf8ad4c191e341558d219c605548b73966b`
```text
ExperimentDesignSnapshot {
    design_snapshot_id
    experiment_id
    design_version
    question
    purpose
    method_spec
    prediction_refs[]
    required_action_specs[]
    risk_refs[]
    design_scope
    authorized_commit_seq
    design_fingerprint
}
```

### ExperimentRun
**Source:** RDMS-03 / Original draft; **declared name:** `ExperimentRun`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `809f19f3dd7a910bff6e6e48f04a1d684257914c8a7706fb57b035fde58fc948`
```text
ExperimentRun {
    experiment_run_id
    experiment_id
    run_number
    repo_ref?
    world_ref?
    environment_ref?
    dependency_set_ref?
    run_state
    started_at?
    ended_at?
    execution_issue_ref?
}
```

### FactGrounding
**Source:** RDMS-02 / Original draft; **declared name:** `FactGrounding`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `7d1365a80728c8d4e2a9340e7262e71274d698c0cdeb9dfb01d9c61d8a54ccca`
```text
FactGrounding {
    kind
    source_refs[]
    authority_domain?
}
```

### IntegratedCompletionEvidence
**Source:** RDMS-10 / C01; **declared name:** `IntegratedCompletionEvidence`; **owner:** `L4_TEMPORAL_SPECIALISTS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `61a9b48635b374ccf5a78e9ed18ca8b50097e9d29a11b2dfcef1994e06afd3df`
```text
IntegratedCompletionEvidence {
    goal_ref
    current_goal_version
    acceptance_criteria_refs[]
    verified_criteria_refs[]
    unverified_criteria_refs[]
    failed_criteria_refs[]
    verification_record_refs[]
    dependency_evaluation_ref
    current_repository_ref
    unresolved_action_constraints[]
    unresolved_specialist_constraints[]
    applicable_policy_ref
    finalization_assessment_ref
    authorized_completion_scope
}
```

### LearningAuthorizationBinding
**Source:** RDMS-07 / C01 and Adversarial Freeze Review 02 with freeze decision; **declared name:** `LearningAuthorizationBinding`; **owner:** `L7_RUNTIME_INTEGRATION.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `b874b8422dc956055f19393b3ef64da2d1e7499648ef92e4920324f6b4bd87b4`
```text
LearningAuthorizationBinding {
    proposal_snapshot_ref
    learning_gate_evaluation_ref
    executive_authorization_ref
    expected_memory_head_ref?
    dependency_evaluation_ref
    authorized_commit_scope
}
```

### MemoryProposal
**Source:** RDMS-07 / Original draft; **declared name:** `MemoryProposal`; **owner:** `L7_RUNTIME_INTEGRATION.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `954762e236b07d60a1c7480f60f9383a0f914a88043e9f541e6567ed0a6557af`
```text
MemoryProposal {
    proposal_id
    claim
    proposed_scope
    source_episode_refs[]
    causal_basis_ref?
    applicability_conditions[]
    counter_conditions[]
    counterexamples[]
    evidence_refs[]
    confidence_assessment_ref
    proposed_maturity
    dependency_set_ref
    provenance_ref
    proposed_memory_category
}
```

### MemoryRetrievalCoverage
**Source:** RDMS-07 / C01 and Adversarial Freeze Review 02 with freeze decision; **declared name:** `MemoryRetrievalCoverage`; **owner:** `L5_MEMORY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `141502db00751fe46e006bdf466aa1a1bfda4d18bec292c7a78aada5c4ac500f`
```text
MemoryRetrievalCoverage {
    query_ref
    searchable_universe_ref
    index_snapshot_ref
    searched_scope
    retrieval_budget
    completeness
    excluded_scope_refs[]
}
```

### MemoryRetrievalRequest
**Source:** RDMS-10 / Original draft; **declared name:** `MemoryRetrievalRequest`; **owner:** `L5_MEMORY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `52a9b95579ab0c8cb214cff7e5cd1fef339e20d509c4a10944811e445f887d36`
```text
MemoryRetrievalRequest {
    project_ref
    query_context_ref
    requested_memory_scopes[]
    applicability_context_ref
    access_policy_ref
    result_budget
}
```

### MemoryRetrievalResult
**Source:** RDMS-07 / Original draft; **declared name:** `MemoryRetrievalResult`; **owner:** `L5_MEMORY.md`
**Status:** CURATED_SOURCE_DECISION; **SHA-256 of declaration:** `e4ae715a27b230289f343447d8b7723501f62538065a5e61fa5dc5009c17c67d`
```text
MemoryRetrievalResult {
    retrieval_id
    query_ref
    candidate_refs[]
    omitted_or_filtered_scope[]
    ranking_policy_ref
    retrieval_coverage
    freshness_summary
    created_at
}
```

### MemoryRetrievalTransportResult
**Source:** RDMS-10 / Original draft; **declared name:** `MemoryRetrievalResult`; **owner:** `L7_RUNTIME_INTEGRATION.md`
**Status:** NONCANONICAL_TRANSPORT_ALIAS__SOURCE_NAMING_COLLISION_CLOSED; **SHA-256 of declaration:** `a70de6ab479231f1c2f991196c6406715513f940d0af266e1e05b22ce533c35a`
```text
MemoryRetrievalTransportResult {
    memory_refs[]
    relevance_assessments[]
    provenance_refs[]
    applicability_assessments[]
    trust_metadata_refs[]
}
```

### MemoryUseAssessment
**Source:** RDMS-07 / C01 and Adversarial Freeze Review 02 with freeze decision; **declared name:** `MemoryUseAssessment`; **owner:** `L5_MEMORY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `8f8244a812cfab524dd5c263128acd9995026dfc1c8f9db78537d2e6698e0fb6`
```text
MemoryUseAssessment {
    memory_ref
    current_goal_ref
    source_scope_ref
    target_scope_ref
    applicability_assessment
    dependency_evaluation_ref
    current_evidence_refs[]
    required_revalidation_refs[]
    permitted_use
    limitations[]
}
```

### Observation
**Source:** RDMS-03 / Original draft; **declared name:** `Observation`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `2e8195bef03066422a8996e4d6329cdf17d9415a4d0584a12d65b788d09aebc1`
```text
Observation {
    observation_id
    project_id
    observation_kind
    source_ref
    subject_ref?
    observed_at
    ingested_commit_seq
    repo_ref?
    world_ref?
    environment_ref?
    normalized_content
    raw_artifact_ref?
    provenance
    capture_integrity
    origin_ref?
}
```

### ObservationCausalAttachmentContract
**Source:** RDMS-10 / C02; **declared name:** `ObservationCausalAttachmentContract`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `6dbabd3c921605671ac0cd84d1d22319559f537e42ec6eb9c930984bf3121851`
```text
ObservationCausalAttachmentContract {
    observation_ref
    source_identity
    source_event_identity?
    raw_observation_scope
    claimed_action_ref?
    verified_action_ref?
    source_provenance_ref
    causal_attachment_evidence_refs[]
    missing_parent_refs[]
    admissible_interpretation_scope
    reattachment_requirements[]
}
```

### ObservationSourceBinding
**Source:** RDMS-10 / C01; **declared name:** `ObservationSourceBinding`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `486ffdc2cc70a4eaff365090f9321a578a1cd667846176b85b0974c84e077994`
```text
ObservationSourceBinding {
    observation_ref
    source_identity
    source_kind
    source_trust_classification
    related_action_ref?
    observed_resource_scope
    observed_event_scope
    raw_report_ref?
    directly_observed_effect_refs[]
    observation_provenance_ref
    observation_integrity_ref
    supported_claim_scope
    known_limitations[]
}
```

### OperationalCausalClaim
**Source:** RDMS-02 / Original draft; **declared name:** `OperationalCausalClaim`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `25acaae38d4e0e7933822b74e801146eedd80d82784a97f384e9f359af8ab0d5`
```text
OperationalCausalClaim {
    causal_claim_id
    source_hypothesis_id
    cause
    effect
    mechanism
    scope
    verification_ref
    dependency_set_ref
    validity_conditions[]
    contradictory_observation_refs[]
    status
    promoted_commit_seq
    superseded_by?
}
```

### PossibleExternalEffectAssessment
**Source:** RDMS-09 / C03; **declared name:** `PossibleExternalEffectAssessment`; **owner:** `L6_RECOVERY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `cc9b1b7dbb8cdcf3c67ee0a2c9d5c15eb170d44f8ce70cf6a9f923b008eeb7e9`
```text
PossibleExternalEffectAssessment {
    assessment_id
    related_action_refs[]
    confirmed_effect_refs[]
    possible_unconfirmed_effects[]
    unknown_effect_scope[]
    external_execution_guarantees[]
    outstanding_dispatch_paths[]
    effect_identity_refs[]
    proposed_followup_action_ref?
    conflict_analysis
    safety_evidence_refs[]
    conclusion
}
```

### Prediction
**Source:** RDMS-03 / Original draft; **declared name:** `Prediction`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `557093dfde485e4408fdd764faa37e88d42fc59c27fbadc5f293a1f2de41ee3f`
```text
Prediction {
    prediction_id
    experiment_id
    hypothesis_id?
    statement
    expected_observation_spec
    discrimination_targets[]
    falsification_condition?
    created_commit_seq
    frozen_at_commit_seq?
}
```

### RecoverableActionDeliveryObligation
**Source:** RDMS-10 / C02; **declared name:** `RecoverableActionDeliveryObligation`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `52b78f2353eea358151165a9b085d7c6354098967e027ef30510af0365ac7e76`
```text
RecoverableActionDeliveryObligation {
    action_ref
    authoritative_lifecycle_ref
    dispatch_intent_commit_ref
    sealed_execution_intent_ref
    delivery_correlation_ref
    execution_attempt_refs[]
    known_external_effect_refs[]
    recovery_enumeration_scope
    unresolved_effect_scope
    legal_continuation_requirement
    recovery_assessment_ref?
}
```

### RecoveryAdmissionBinding
**Source:** RDMS-09 / C02; **declared name:** `RecoveryAdmissionBinding`; **owner:** `L6_RECOVERY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `6999b109f9532e1ccce580354e9c6bb30c52921f487e04769ee4229fec5f0f6b`
```text
RecoveryAdmissionBinding {
    admission_id
    recovery_case_ref
    admitted_project_scope
    admitted_operation_classes[]
    current_executive_epoch
    canonical_state_frontier
    policy_frontier
    dependency_frontier
    security_frontier
    suppression_frontier
    unresolved_action_constraints[]
    admission_generation
    invalidation_conditions[]
    admission_integrity_ref
}
```

### RecoveryBootstrapContract
**Source:** RDMS-09 / C02; **declared name:** `RecoveryBootstrapContract`; **owner:** `L6_RECOVERY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `3627f5109f1283c25e945cc14599a1d04c351156bf06ccf4b2be3c8b91339d72`
```text
RecoveryBootstrapContract {
    bootstrap_case_id
    affected_project_scope
    unavailable_control_components[]
    trusted_bootstrap_source_refs[]
    recovery_principal_ref
    principal_authority_proof_ref
    permitted_infrastructure_operations[]
    prohibited_project_operations[]
    source_integrity_requirements[]
    destination_integrity_requirements[]
    bootstrap_generation
    bootstrap_audit_receipts[]
    canonical_handoff_requirements[]
    bootstrap_disposition
}
```

### RecoveryOwnershipLease
**Source:** RDMS-09 / C01; **declared name:** `RecoveryOwnershipLease`; **owner:** `L6_RECOVERY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `cc18adf30b86d39abb8b5a38533743fe9c335e5247cd5cea669f6e60a52862a5`
```text
RecoveryOwnershipLease {
    recovery_case_ref
    recovery_owner_id
    recovery_generation
    governing_executive_epoch
    ownership_scope[]
    lease_or_fencing_ref
    expected_control_version
    acquisition_commit_ref
    status
}
```

### RecoverySuspensionCommitment
**Source:** RDMS-09 / C02; **declared name:** `RecoverySuspensionCommitment`; **owner:** `L6_RECOVERY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `3b26f4b204905173a8e5b908d644ebc07499fcaba2a2a9b9c7761cfea8b030e8`
```text
RecoverySuspensionCommitment {
    commitment_id
    recovery_case_ref
    unresolved_obligation_refs[]
    blocked_goal_refs[]
    dependent_action_refs[]
    suspension_reason
    required_reactivation_conditions[]
    durable_trigger_refs[]
    responsible_authority_ref
    escalation_conditions[]
    suspension_commit_ref
}
```

### RestoreContainmentProof
**Source:** RDMS-09 / C03; **declared name:** `RestoreContainmentProof`; **owner:** `L6_RECOVERY.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `0b16b3bfce95f242d0305488af1d2ec2d2b2e4d4d6586cce16d0a378f4287b03`
```text
RestoreContainmentProof {
    restore_operation_ref
    restore_source_ref
    destination_scope
    writable_mount_refs[]
    reachable_service_refs[]
    automatic_activation_paths[]
    executable_content_paths[]
    credential_exposure_scope
    containment_guarantees[]
    relevant_environment_versions[]
    unresolved_escape_paths[]
    proof_result
}
```

### ResumptionCapsule
**Source:** RDMS-05 / C01; **declared name:** `ResumptionCapsule`; **owner:** `L6_RECOVERY.md`
**Status:** CURATED_SOURCE_DECISION; **SHA-256 of declaration:** `1c38a08ce60f890ed64f69cfd6cb8d2928d75d5b6637be31299a5b209e420409`
```text
ResumptionCapsule {
    capsule_id
    task_or_goal_ref
    suspended_from_state
    canonical_snapshot_ref
    relevant_entity_refs[]
    dependency_set_ref
    unresolved_action_refs[]
    next_action_proposal_ref?
    durable_payload_artifact_ref
    content_integrity_ref
    created_commit_seq
}
```

### SealedExecutionIntent
**Source:** RDMS-10 / C01; **declared name:** `SealedExecutionIntent`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `8bf749d80ed5502c3a670b64853ea11cd4fb0635541eb7efd087468202bde01a`
```text
SealedExecutionIntent {
    action_ref
    authorized_tool_identity
    authorized_operation_kind
    effective_argument_ref
    effective_argument_integrity_ref
    authorized_target_identity
    authorized_resource_scope
    authorized_effect_semantics_ref
    execution_boundary_ref
    executive_epoch
    authorization_generation
    required_pre_dispatch_conditions[]
    authorization_receipt_ref
}
```

### SealedOutboundContext
**Source:** RDMS-10 / C02; **declared name:** `SealedOutboundContext`; **owner:** `L7_RUNTIME_INTEGRATION.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `9a32bf619d57ada734a71008191da386626d6d7fbd7d4c8da3bd4383e79674f6`
```text
SealedOutboundContext {
    invocation_ref
    originating_project_ref
    final_destination_provider_ref
    final_destination_boundary_ref
    final_context_manifest_ref
    included_content_integrity_refs[]
    included_data_classification_refs[]
    applicable_disclosure_policy_frontier
    authorized_processing_purpose
    disclosure_admission_ref
    outbound_integrity_binding
    release_eligibility
}
```

### TriggerActionCausalityBinding
**Source:** RDMS-10 / C01; **declared name:** `TriggerActionCausalityBinding`; **owner:** `L4_TEMPORAL_SPECIALISTS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `ca5026690cd7b722270eced9f7105032da6a7e6f95e0173c7d2dcad84052bd4c`
```text
TriggerActionCausalityBinding {
    trigger_ref
    trigger_generation
    source_event_identity
    canonical_reaction_identity
    reaction_commit_ref
    derived_action_proposal_refs[]
    derived_action_identity_refs[]
    action_lifecycle_refs[]
    causal_binding_integrity
    replay_semantics
    deduplication_scope
}
```

### TriggerCondition
**Source:** RDMS-05 / Original draft; **declared name:** `TriggerCondition`; **owner:** `L2_COGNITION.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `c3092a02ce0b441049cfe58978e5eaa1bbee23f7b4fd879240b58e666822bdbd`
```text
TriggerCondition {
    condition_id
    kind
    predicate_spec
    dependency_set_ref?
    required_evidence_policy_ref?
}
```

### TriggerDefinition
**Source:** RDMS-05 / Original draft; **declared name:** `TriggerDefinition`; **owner:** `L4_TEMPORAL_SPECIALISTS.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `349aaa77a493ffa1b2250985d02f46558844cb2d58143502b52fe5b43e532723`
```text
TriggerDefinition {
    trigger_id
    project_id
    generation
    condition_ref
    fire_policy
    detection_policy
    source_refs[]
    reaction_spec_ref
    owner_ref
    linked_object_ref
    created_commit_seq
    entity_version
}
```

### TriggerDerivedWorkCommitment
**Source:** RDMS-10 / C02; **declared name:** `TriggerDerivedWorkCommitment`; **owner:** `L2_COGNITION.md`
**Status:** ONE_ATTESTED_DECLARATION; **SHA-256 of declaration:** `d9b47cadcb4d7322b954a69c91d8acb6c3e871b54bd31510b1e216f209714373`
```text
TriggerDerivedWorkCommitment {
    trigger_ref
    trigger_generation
    source_event_identity
    canonical_reaction_identity
    reaction_commit_ref
    derived_work_identity
    required_continuation_scope
    durable_continuation_ref
    existing_action_refs[]
    required_authorization_path
    recovery_deduplication_basis
    current_continuation_assessment
}
```

### TriggerFire
**Source:** RDMS-05 / C01; **declared name:** `TriggerFire`; **owner:** `L4_TEMPORAL_SPECIALISTS.md`
**Status:** CURATED_SOURCE_DECISION; **SHA-256 of declaration:** `5bdd4a1ad86972d86c9fd8cb77adaec3e60236a88d76f37540b48f091096f69c`
```text
TriggerFire {
    fire_id
    trigger_definition_snapshot_ref
    qualified_occurrence_ref
    evidence_basis_refs[]
    source_frontier_ref
    fire_identity_key
    created_commit_seq
}
```

### TriggerReaction
**Source:** RDMS-05 / C01; **declared name:** `TriggerReaction`; **owner:** `L4_TEMPORAL_SPECIALISTS.md`
**Status:** CURATED_SOURCE_DECISION; **SHA-256 of declaration:** `89679654e9b97a64373c679bb1c0a96e71021f9d8d3df7dd19cfa3fa682f0fd3`
```text
TriggerReaction {
    reaction_id
    fire_ref
    target_entity_ref
    expected_target_version
    expected_lifecycle
    target_goal_lineage_ref?
    frozen_reaction_spec_ref
    status
}
```

### VerificationRecord
**Source:** RDMS-03 / Original draft; **declared name:** `VerificationRecord`; **owner:** `L3_ACTIONS.md`
**Status:** ONE_COMPLETE_DECLARATION_WITH_OPTIONAL_OVERLAYS; **SHA-256 of declaration:** `732b01c781d88c2661eea6b8463d7a66965593279c0ee897e63d1a005f2892b8`
```text
VerificationRecord {
    verification_record_id
    verification_spec_ref
    subject_ref
    repo_ref?
    world_ref?
    environment_ref?
    dependency_set_ref?
    deterministic_result_refs[]
    observation_refs[]
    semantic_assessment_refs[]
    outcome
    derivation
    executed_at
    artifact_refs[]
}
```

## C. Reject-before-commit constraints

1. A transport alias is **never** cognitive authority or a substitute for the canonical, source-owned result.
2. A partial or ellipsis-bearing correction is an **overlay**, not deletion of untouched fields; no source-unverified downgrade is allowed.
3. `Commitment` historical aliases cannot be inferred when absent; RDMS-02 C01 `reactivation_condition_ref` governs.
4. `TriggerFire`/`TriggerReaction` use RDMS-05 C01; firing does not grant ActionGate authority.
5. `ResumptionCapsule` must have intact durable payload and integrity verification; never reconstruct omitted fields from guesses.
6. Existing world side effects cannot be rewound by canonical rollback; unknown delivery is IN_DOUBT pending reconciliation.
7. An unresolved unsupported primitive type or runtime adapter cannot be marked verified solely by this architecture ledger.
