# GAIA-C08 — Source-backed interface declaration dossiers

**STATUS: SOURCE DECLARATIONS VERIFIED / FULL INTERFACE SIGNATURES NOT RATIFIED.**

Each quoted block below is an exact excerpt of the frozen-source message text (verified SHA-256). Historical base definitions and later amendments may coexist. The newest block is **not automatically** treated as full replacement: partial `...` definitions are overlays only.

This is not a new API surface, schema migration, authorization grant, or assertion of atomic external side effects.

---
## X8-01 — Capability invocation / result
**Boundary:** L2 → L7 → L2 | **Primary dossier owner:** `L7_RUNTIME_INTEGRATION.md`

**Source rule to retain:** Transport envelope ≠ approved cognitive result or canonical commit.

**Original schema names found:** 4 / 4 requested; **literal declaration occurrences:** 4.

### CapabilityInvocation
**RDMS-10 / Original draft**, message `99533762-bba8-407a-b27b-952a236c00a4`, lines 355–371; SHA-256 `8fec5e274ffc9f94b0bbde0178edb4b6fdcfe0241105dd079e62d1f954b26ccd`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

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
**RDMS-10 / Original draft**, message `99533762-bba8-407a-b27b-952a236c00a4`, lines 372–390; SHA-256 `e8ae9d35f870fc3efb84694641074038fd2961677393b2a5f5ee6d6f0cb717b5`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
CapabilityResult {
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

### CapabilityActivationContract
**RDMS-10 / C01**, message `e4828797-8ddb-48ae-a3e4-3e9ec47b70c3`, lines 2052–2068; SHA-256 `026bb25fd353ffcabaa2ba4b1a5e101238efb218e9af666701f6045a6ccd9282`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### ExecutiveTransitionIntegrationBinding
**RDMS-10 / C01**, message `e4828797-8ddb-48ae-a3e4-3e9ec47b70c3`, lines 569–593; SHA-256 `74d692bfc0f33d9890f8b7bc9fbe3e4dae3b7563bd8d637370e7288527aa5c2e`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-02 — Memory retrieval and re-use
**Boundary:** L5 → L7 → L2 | **Primary dossier owner:** `L5_MEMORY.md`

**Source rule to retain:** A short transport return cannot omit scope, coverage, ranking or freshness without an authoritative dereference.

**Original schema names found:** 4 / 4 requested; **literal declaration occurrences:** 5.

### MemoryRetrievalRequest
**RDMS-10 / Original draft**, message `99533762-bba8-407a-b27b-952a236c00a4`, lines 1123–1135; SHA-256 `52a9b95579ab0c8cb214cff7e5cd1fef339e20d509c4a10944811e445f887d36`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

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
**RDMS-07 / Original draft**, message `938c1bc7-97a0-46ad-be19-cd3ba3ca125f`, lines 1068–1084; SHA-256 `e4ae715a27b230289f343447d8b7723501f62538065a5e61fa5dc5009c17c67d`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

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

**RDMS-10 / Original draft**, message `99533762-bba8-407a-b27b-952a236c00a4`, lines 1136–1146; SHA-256 `a70de6ab479231f1c2f991196c6406715513f940d0af266e1e05b22ce533c35a`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
MemoryRetrievalResult {
    memory_refs[]

    relevance_assessments[]

    provenance_refs[]

    applicability_assessments[]

    trust_metadata_refs[]
}
```

### MemoryRetrievalCoverage
**RDMS-07 / C01 and Adversarial Freeze Review 02 with freeze decision**, message `5ee62ad7-b67d-4382-be9d-cd85f6331a8c`, lines 519–536; SHA-256 `141502db00751fe46e006bdf466aa1a1bfda4d18bec292c7a78aada5c4ac500f`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

```text
MemoryRetrievalCoverage {
    query_ref

    searchable_universe_ref

    index_snapshot_ref

    searched_scope

    retrieval_budget

    completeness:
        COMPLETE_WITHIN_SCOPE
        PARTIAL
        UNKNOWN

    excluded_scope_refs[]
}
```

### MemoryUseAssessment
**RDMS-07 / C01 and Adversarial Freeze Review 02 with freeze decision**, message `5ee62ad7-b67d-4382-be9d-cd85f6331a8c`, lines 450–473; SHA-256 `8f8244a812cfab524dd5c263128acd9995026dfc1c8f9db78537d2e6698e0fb6`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

    permitted_use:
        HISTORICAL_CONTEXT
        HYPOTHESIS_SOURCE
        PROCEDURAL_CANDIDATE
        CURRENTLY_SUPPORTED_REFERENCE

    limitations[]
}
```

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-03 — Commitment / reactivation
**Boundary:** L2 → L4 → L1 | **Primary dossier owner:** `L2_COGNITION.md`

**Source rule to retain:** Time/trigger activation cannot fabricate satisfaction of the underlying obligation.

**Original schema names found:** 4 / 4 requested; **literal declaration occurrences:** 6.

### Commitment
**RDMS-02 / Original draft**, message `a62cc59d-b288-4be8-97c4-ac84d835a933`, lines 1368–1396; SHA-256 `da8ac753225c695d17105d549b2d3eca57f648d2343a84a0a8daefc58e46fce9`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
Commitment {
    commitment_id

    statement

    why_temporary

    scope: ScopeSpec

    owner_ref?

    linked_entity_refs[]

    created_at

    due_at?

    removal_trigger_id?
    revisit_trigger_id?

    status:
        ACTIVE
        DUE
        SATISFIED
        CANCELLED
        SUPERSEDED

    resolution_ref?
}
```

**RDMS-02 / C01, second review corrections and final freeze decision**, message `266bb347-d2a5-41ea-872a-32e140c803eb`, lines 918–931; SHA-256 `bbf875e7b0cbf30ca4d9017a16388b676e74ef8ce1bc2e0840b520c777a78836`; classification `APPROVED_LATER_SOURCE_TEXT`; PARTIAL OVERLAY (ellipsis present)

```text
Commitment {
    ...

    reactivation_condition_ref

    status:
        ACTIVE
        DUE
        SATISFIED
        CANCELLED
        SUPERSEDED

    resolution_ref?
}
```

**RDMS-05 / Original draft**, message `6276f296-457b-462d-b674-933a15194429`, lines 514–535; SHA-256 `b9f1955870bd84b03c06400dc25992a54d5c6e25ae2af05d74764502e180ae3e`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
Commitment {
    commitment_id

    owner_ref

    subject_ref

    reason
    required_followup

    reactivation_condition_ref

    lifecycle:
        ACTIVE
        DUE
        SATISFIED
        CANCELLED
        SUPERSEDED

    created_commit_seq
    updated_commit_seq
}
```

### TriggerCondition
**RDMS-05 / Original draft**, message `6276f296-457b-462d-b674-933a15194429`, lines 179–197; SHA-256 `c3092a02ce0b441049cfe58978e5eaa1bbee23f7b4fd879240b58e666822bdbd`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
TriggerCondition {
    condition_id

    kind:
        STATE_EVENT
        REPO_CHANGE
        METRIC_THRESHOLD
        TEMPORAL
        EXTERNAL_EVENT
        HUMAN_EVENT
        SEMANTIC_REVIEW
        COMPOSITE

    predicate_spec

    dependency_set_ref?

    required_evidence_policy_ref?
}
```

### TriggerDerivedWorkCommitment
**RDMS-10 / C02**, message `5f33fe0d-af3e-4f37-aeac-8979e64d941f`, lines 273–297; SHA-256 `d9b47cadcb4d7322b954a69c91d8acb6c3e871b54bd31510b1e216f209714373`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### ExecutiveTransitionIntegrationBinding
**RDMS-10 / C01**, message `e4828797-8ddb-48ae-a3e4-3e9ec47b70c3`, lines 569–593; SHA-256 `74d692bfc0f33d9890f8b7bc9fbe3e4dae3b7563bd8d637370e7288527aa5c2e`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-04 — Trigger firing and actions
**Boundary:** L4 → L1 → L3 | **Primary dossier owner:** `L4_TEMPORAL_SPECIALISTS.md`

**Source rule to retain:** Trigger acceptance is not direct ActionGate authority; durable reaction identity is mandatory.

**Original schema names found:** 5 / 5 requested; **literal declaration occurrences:** 7.

### TriggerDefinition
**RDMS-05 / Original draft**, message `6276f296-457b-462d-b674-933a15194429`, lines 149–174; SHA-256 `349aaa77a493ffa1b2250985d02f46558844cb2d58143502b52fe5b43e532723`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
TriggerDefinition {
    trigger_id
    project_id

    generation

    condition_ref

    fire_policy:
        ONE_SHOT
        REARMABLE

    detection_policy:
        LEVEL_TRIGGERED
        EDGE_TRIGGERED

    source_refs[]

    reaction_spec_ref

    owner_ref
    linked_object_ref

    created_commit_seq
    entity_version
}
```

### TriggerReaction
**RDMS-05 / Original draft**, message `6276f296-457b-462d-b674-933a15194429`, lines 471–491; SHA-256 `23f43aee7f11e84ef54c3c9e4f2d9d3909f51068ee0230bb59b2ea4d51ae8b4b`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
TriggerReaction {
    reaction_id

    fire_ref
    target_ref

    reaction_kind:
        MARK_COMMITMENT_DUE
        REQUEST_GOAL_REACTIVATION
        REQUEST_SLICE_REVALIDATION
        REQUEST_EXECUTIVE_ATTENTION
        RECORD_CONDITION_SATISFIED

    reaction_key

    lifecycle:
        PENDING
        APPLIED
        BLOCKED
        CANCELLED
}
```

**RDMS-05 / C01**, message `77caba5f-8e8e-4b8e-a9fe-027c4801efad`, lines 622–642; SHA-256 `89679654e9b97a64373c679bb1c0a96e71021f9d8d3df7dd19cfa3fa682f0fd3`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

```text
TriggerReaction {
    reaction_id

    fire_ref

    target_entity_ref
    expected_target_version
    expected_lifecycle

    target_goal_lineage_ref?

    frozen_reaction_spec_ref

    status:
        PENDING
        CLAIMED
        APPLIED
        BLOCKED
        OBSOLETE
        CANCELLED
}
```

### TriggerFire
**RDMS-05 / Original draft**, message `6276f296-457b-462d-b674-933a15194429`, lines 439–454; SHA-256 `559e11a3e82f870ebb618aa1f4932f5a0c389404f52a5a7d17abf6f1e8a6c9ce`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
TriggerFire {
    fire_id

    trigger_id
    generation

    condition_version_ref

    triggering_basis_refs[]

    source_frontier_ref

    fire_identity_key

    fired_at_commit_seq
}
```

**RDMS-05 / C01**, message `77caba5f-8e8e-4b8e-a9fe-027c4801efad`, lines 345–357; SHA-256 `5bdd4a1ad86972d86c9fd8cb77adaec3e60236a88d76f37540b48f091096f69c`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### TriggerActionCausalityBinding
**RDMS-10 / C01**, message `e4828797-8ddb-48ae-a3e4-3e9ec47b70c3`, lines 1690–1712; SHA-256 `ca5026690cd7b722270eced9f7105032da6a7e6f95e0173c7d2dcad84052bd4c`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### DispatchAdmissionCutover
**RDMS-10 / C02**, message `5f33fe0d-af3e-4f37-aeac-8979e64d941f`, lines 536–562; SHA-256 `6c98bbb843273f8f952861c7c49cd7c8967d3780a4448fd801c529765879ca95`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-05 — Suspension / resumption
**Boundary:** L4 → L6 → L1 | **Primary dossier owner:** `L6_RECOVERY.md`

**Source rule to retain:** No lossy restoration from abbreviated fields; integrity and pinned state must be checked.

**Original schema names found:** 4 / 4 requested; **literal declaration occurrences:** 5.

### ResumptionCapsule
**RDMS-05 / Original draft**, message `6276f296-457b-462d-b674-933a15194429`, lines 642–678; SHA-256 `c1d22ca4a7ddbf38aa27abd8caa3fbbf1587f636463b3d7827b840bc809528b1`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
ResumptionCapsule {
    capsule_id

    project_id
    task_or_goal_ref

    suspended_from_state

    base_canonical_commit_seq

    repo_ref?
    world_ref?
    environment_ref?

    dependency_set_ref?

    current_focus_ref?

    relevant_claim_refs[]
    relevant_hypothesis_refs[]
    relevant_evidence_refs[]

    decision_refs[]
    rejected_path_refs[]

    active_slice_refs[]
    unresolved_action_refs[]

    open_information_need_refs[]
    commitment_refs[]

    temporary_change_refs[]

    next_action_proposal_ref?

    created_commit_seq
}
```

**RDMS-05 / C01**, message `77caba5f-8e8e-4b8e-a9fe-027c4801efad`, lines 720–741; SHA-256 `1c38a08ce60f890ed64f69cfd6cb8d2928d75d5b6637be31299a5b209e420409`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### RecoverySuspensionCommitment
**RDMS-09 / C02**, message `d59160dd-fa7a-4058-8892-69794f57e9b8`, lines 1203–1225; SHA-256 `3b26f4b204905173a8e5b908d644ebc07499fcaba2a2a9b9c7761cfea8b030e8`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### BootstrapHandoffProof
**RDMS-09 / C03**, message `89e41ed5-ac4e-4b95-9680-b9bec79f278a`, lines 120–147; SHA-256 `01cc1a26ba1a3cc33acd111480bd8dba1b4eecc380f0e4ef4f4f07ac40d31b8c`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### RecoveryAdmissionBinding
**RDMS-09 / C02**, message `d59160dd-fa7a-4058-8892-69794f57e9b8`, lines 1085–1113; SHA-256 `6999b109f9532e1ccce580354e9c6bb30c52921f487e04769ee4229fec5f0f6b`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-06 — External execution and journal
**Boundary:** L2 → L3 → L1 | **Primary dossier owner:** `L3_ACTIONS.md`

**Source rule to retain:** Ledger atomicity cannot imply atomic external-world effects; IN_DOUBT and repairable delivery are required.

**Original schema names found:** 7 / 7 requested; **literal declaration occurrences:** 7.

### ActionProposal
**RDMS-04 / Original draft**, message `32ad532a-40cd-4b2a-8a0a-3372937cf6db`, lines 85–137; SHA-256 `1d1d2dfa1eaacd278ba44f59a1e7c5a2807b8f4e22cd867864b3688ac7587273`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
ActionProposal {
    action_proposal_id
    project_id

    requested_by_ref
    goal_id
    slice_id

    action_kind:
        TERMINAL
        FILESYSTEM
        GIT
        TEST
        BUILD
        DEBUGGER
        DATABASE
        NETWORK
        DEPLOYMENT
        OTHER

    requested_action_class:
        EPHEMERAL_SANDBOX
        SHARED_WORLD

    intent

    target_scope[]
    expected_effects[]
    preconditions[]

    base_repo_ref?
    base_world_ref?

    dependency_set_ref?

    risk_profile_ref?

    reversibility:
        REVERSIBLE
        COMPENSATABLE
        PARTIALLY_REVERSIBLE
        IRREVERSIBLE

    compensation_plan_ref?

    effect_semantics_ref

    execution_spec_ref

    mode:
        DIAGNOSTIC
        PRODUCTION
}
```

### ActionRecord
**RDMS-04 / Original draft**, message `32ad532a-40cd-4b2a-8a0a-3372937cf6db`, lines 196–221; SHA-256 `b04404a6eafcf8aec73c83958aa5553aca3762a62a892c1cc8e857d5f0e3f386`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

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

### SealedExecutionIntent
**RDMS-10 / C01**, message `e4828797-8ddb-48ae-a3e4-3e9ec47b70c3`, lines 748–774; SHA-256 `8bf749d80ed5502c3a670b64853ea11cd4fb0635541eb7efd087468202bde01a`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### EffectiveExecutionBinding
**RDMS-10 / C02**, message `5f33fe0d-af3e-4f37-aeac-8979e64d941f`, lines 423–449; SHA-256 `d5c98f9d9e69edf753fbdda12922a0df68c67cc556e02990bb963f0a93601da1`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### ActionDeliveryContract
**RDMS-10 / C01**, message `e4828797-8ddb-48ae-a3e4-3e9ec47b70c3`, lines 867–891; SHA-256 `d9771caf5be03c5c6995858af38e0539561a2f4975711c59d1e28db84713003f`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### DispatchAdmissionCutover
**RDMS-10 / C02**, message `5f33fe0d-af3e-4f37-aeac-8979e64d941f`, lines 536–562; SHA-256 `6c98bbb843273f8f952861c7c49cd7c8967d3780a4448fd801c529765879ca95`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### RecoverableActionDeliveryObligation
**RDMS-10 / C02**, message `5f33fe0d-af3e-4f37-aeac-8979e64d941f`, lines 130–152; SHA-256 `52b78f2353eea358151165a9b085d7c6354098967e027ef30510af0365ac7e76`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-07 — Observation and evidence
**Boundary:** L3 → L2 → L1 | **Primary dossier owner:** `L3_ACTIONS.md`

**Source rule to retain:** Source acceptance differs from epistemic certainty and causal attribution.

**Original schema names found:** 6 / 6 requested; **literal declaration occurrences:** 7.

### Observation
**RDMS-03 / Original draft**, message `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 70–96; SHA-256 `2e8195bef03066422a8996e4d6329cdf17d9415a4d0584a12d65b788d09aebc1`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

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

### EvidenceLink
**RDMS-03 / Original draft**, message `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 449–480; SHA-256 `b56d24206ab7628d92c266e4a6d8c3e3a63aa29a627ede82c373819a56071e26`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
EvidenceLink {
    evidence_link_id

    observation_refs[]

    target_ref

    relation:
        SUPPORTS
        WEAKENS
        CONTRADICTS
        RELEVANT

    derivation:
        DETERMINISTIC
        SEMANTIC
        AUTHORITATIVE

    rationale

    derivation_ref?

    dependency_set_ref?

    lifecycle:
        PROPOSED
        ACCEPTED
        REJECTED
        SUPERSEDED

    accepted_commit_seq?
}
```

**RDMS-03 / Original draft**, message `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 502–505; SHA-256 `c3afbd4eb962992437673decec2fc0f1672639db8a9a935f704eb0c450995eaa`; classification `HISTORICAL_DRAFT`; PARTIAL OVERLAY (ellipsis present)

```text
EvidenceLink {
    observation_refs = []
    rationale = "I strongly believe..."
}
```

### FactGrounding
**RDMS-02 / Original draft**, message `a62cc59d-b288-4be8-97c4-ac84d835a933`, lines 161–170; SHA-256 `7d1365a80728c8d4e2a9340e7262e71274d698c0cdeb9dfb01d9c61d8a54ccca`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
FactGrounding {
    kind:
        OBSERVED
        DETERMINISTIC
        AUTHORITATIVE

    source_refs[]

    authority_domain?
}
```

### ContentTrustContext
**RDMS-03 / C01 and Freeze Review 02 Final**, message `a1ca0249-b287-4c4b-8254-773c8f6edbda`, lines 19–42; SHA-256 `e23cfcddd8eb07ae9047a8525c20108715194aba476cb801827b2462f1e6432e`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

```text
ContentTrustContext {
    trust_context_id

    content_role:
        DATA
        CODE
        DOCUMENTATION
        TOOL_OUTPUT
        HUMAN_REQUIREMENT
        SYSTEM_POLICY
        OTHER

    instruction_authority:
        NONE
        USER_TASK
        PROJECT
        SYSTEM

    source_trust_class

    domain_authority_binding_ref?

    created_commit_seq
}
```

### ObservationSourceBinding
**RDMS-10 / C01**, message `e4828797-8ddb-48ae-a3e4-3e9ec47b70c3`, lines 1122–1148; SHA-256 `486ffdc2cc70a4eaff365090f9321a578a1cd667846176b85b0974c84e077994`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### ObservationCausalAttachmentContract
**RDMS-10 / C02**, message `5f33fe0d-af3e-4f37-aeac-8979e64d941f`, lines 754–776; SHA-256 `6dbabd3c921605671ac0cd84d1d22319559f537e42ec6eb9c930984bf3121851`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-08 — Experiment and causal verification
**Boundary:** L2 → L3 → L2 | **Primary dossier owner:** `L3_ACTIONS.md`

**Source rule to retain:** A prediction is frozen before intervention; Experiment ≠ ExperimentRun.

**Original schema names found:** 5 / 5 requested; **literal declaration occurrences:** 6.

### Experiment
**RDMS-03 / Original draft**, message `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 859–891; SHA-256 `77b9d1f12e730ad6d94c444aef8d1dd545a8852df355849803557a8712ed4ea8`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
Experiment {
    experiment_id

    question

    purpose:
        REPRODUCTION
        DISCRIMINATING
        CAUSAL_INTERVENTION
        REGRESSION
        PERFORMANCE
        EXPLORATORY
        OTHER

    target_hypothesis_ids[]

    method_spec

    prediction_ids[]

    required_action_specs[]

    risk_refs[]

    lifecycle:
        DRAFT
        DESIGNED
        AUTHORIZED
        RETIRED
        CANCELLED

    prediction_set_frozen_at_commit_seq?
}
```

### ExperimentRun
**RDMS-03 / Original draft**, message `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 918–943; SHA-256 `809f19f3dd7a910bff6e6e48f04a1d684257914c8a7706fb57b035fde58fc948`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
ExperimentRun {
    experiment_run_id

    experiment_id
    run_number

    repo_ref?
    world_ref?
    environment_ref?

    dependency_set_ref?

    run_state:
        PREPARED
        RUNNING
        BLOCKED
        COMPLETED
        PARTIAL
        FAILED_TO_EXECUTE
        CANCELLED

    started_at?
    ended_at?

    execution_issue_ref?
}
```

### ExperimentDesignSnapshot
**RDMS-03 / C01 and Freeze Review 02 Final**, message `a1ca0249-b287-4c4b-8254-773c8f6edbda`, lines 535–559; SHA-256 `fbdf6d6301d7fa360c4f13c7ffbc2cf8ad4c191e341558d219c605548b73966b`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

```text
ExperimentDesignSnapshot {
    design_snapshot_id

    experiment_id
    design_version

    question

    purpose

    method_spec

    prediction_refs[]:
        VersionedEntityRef<Prediction>

    required_action_specs[]

    risk_refs[]

    design_scope

    authorized_commit_seq

    design_fingerprint
}
```

### Prediction
**RDMS-03 / Original draft**, message `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 753–771; SHA-256 `557093dfde485e4408fdd764faa37e88d42fc59c27fbadc5f293a1f2de41ee3f`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

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

### VerificationRecord
**RDMS-03 / Original draft**, message `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 1100–1131; SHA-256 `732b01c781d88c2661eea6b8463d7a66965593279c0ee897e63d1a005f2892b8`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

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

    outcome:
        SATISFIED
        NOT_SATISFIED
        INCONCLUSIVE
        ERROR

    derivation:
        DETERMINISTIC
        BEHAVIORAL
        SEMANTIC
        COMPOSITE

    executed_at

    artifact_refs[]
}
```

**RDMS-03 / C01 and Freeze Review 02 Final**, message `a1ca0249-b287-4c4b-8254-773c8f6edbda`, lines 759–774; SHA-256 `4c6bf58fb82d972bb101d884919cb328c00f46fe9641b16685375716196b5d14`; classification `APPROVED_LATER_SOURCE_TEXT`; PARTIAL OVERLAY (ellipsis present)

```text
VerificationRecord {
    verification_record_id

    verification_spec_ref:
        VersionedEntityRef<VerificationSpec>

    subject_ref

    repo_ref?
    world_ref?
    environment_ref?

    dependency_set_ref?

    ...
}
```

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-09 — Contradiction and reality mismatch
**Boundary:** L3 → L2 | **Primary dossier owner:** `L3_ACTIONS.md`

**Source rule to retain:** An unresolved discrepancy is not silently resolved, nor an independent source of causal truth.

**Original schema names found:** 3 / 3 requested; **literal declaration occurrences:** 5.

### ContradictionRecord
**RDMS-03 / Original draft**, message `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 620–645; SHA-256 `e8e2641455efb82f3da738cfff8f716fcead8179e6b63ddbd46618cbc58948ed`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
ContradictionRecord {
    contradiction_id

    observation_refs[]

    subject_ref?
    subject_key?

    comparison_scope

    comparability

    dimension_analysis[]

    lifecycle:
        CANDIDATE
        CONFIRMED
        EXPLAINED
        RESOLVED
        DISMISSED

    information_need_id?

    explanation_ref?
    resolution_ref?
}
```

**RDMS-03 / C01 and Freeze Review 02 Final**, message `a1ca0249-b287-4c4b-8254-773c8f6edbda`, lines 468–473; SHA-256 `02fb0ca2cc801ad9abf3659661af8e9d5ba4e2cd3cae7b81c41e31be927f788f`; classification `APPROVED_LATER_SOURCE_TEXT`; PARTIAL OVERLAY (ellipsis present)

```text
ContradictionRecord {
    ...

    dimension_analysis[]
    explanation_ref?
}
```

### Claim
**RDMS-02 / Original draft**, message `a62cc59d-b288-4be8-97c4-ac84d835a933`, lines 120–152; SHA-256 `0cc9ca22709f89fa2ed2187d5495b91a57d92b5beb04229b530afce7b69d7a45`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
Claim {
    claim_id

    kind:
        FACT
        BELIEF
        ASSUMPTION

    statement

    scope: ScopeSpec

    support:
        UNASSESSED
        WEAK
        MODERATE
        STRONG
        VERIFIED

    support_assessed_at_commit?

    grounding?
    dependency_set_ref?

    temporal_validity?

    status:
        ACTIVE
        REFUTED
        SUPERSEDED

    superseded_by?
}
```

**RDMS-02 / Original draft**, message `a62cc59d-b288-4be8-97c4-ac84d835a933`, lines 199–202; SHA-256 `28c429da95506d97a29d01a07cf4519a2f805ab04ce63aac809e9827a1698367`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
Claim {
    kind = FACT
    grounding = null
}
```

### OperationalCausalClaim
**RDMS-02 / Original draft**, message `a62cc59d-b288-4be8-97c4-ac84d835a933`, lines 449–477; SHA-256 `25acaae38d4e0e7933822b74e801146eedd80d82784a97f384e9f359af8ab0d5`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

```text
OperationalCausalClaim {
    causal_claim_id

    source_hypothesis_id

    cause
    effect
    mechanism

    scope: CausalScope

    verification_ref

    dependency_set_ref

    validity_conditions[]

    contradictory_observation_refs[]

    status:
        OPERATIONALLY_VERIFIED
        STALE
        CONTRADICTED
        SUPERSEDED

    promoted_commit_seq

    superseded_by?
}
```

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-10 — Freshness and completion
**Boundary:** L4 → L2 → L1 | **Primary dossier owner:** `L4_TEMPORAL_SPECIALISTS.md`

**Source rule to retain:** Freshness is dependency-scoped; completion requires an appropriate proof of acceptance.

**Original schema names found:** 5 / 5 requested; **literal declaration occurrences:** 5.

### DependencySet
**RDMS-06 / Original draft**, message `4bcbb2bf-86d9-4b93-9b1c-9f9529916667`, lines 676–688; SHA-256 `f596f8c673ea27846249b5dcfa447baa4e251351ee006131cc0ae5688825d270`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

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

### DependencyCaptureReceipt
**RDMS-06 / C01 and Adversarial Freeze Review 02 with freeze decision**, message `1ed5a815-4917-47b8-9e00-0b450a0581e2`, lines 609–634; SHA-256 `d7ff97834f08dcd7e2556a12314b38b719619e9cec054f56018795a05827beba`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

    capture_coverage:
        COMPLETE_WITHIN_DEFINED_SCOPE
        PARTIAL
        UNKNOWN

    enforcement_basis_refs[]

    capture_fingerprint
}
```

### DependencyAttestation
**RDMS-06 / C01 and Adversarial Freeze Review 02 with freeze decision**, message `1ed5a815-4917-47b8-9e00-0b450a0581e2`, lines 655–668; SHA-256 `2558385e10da2a9ead0dafaab139ad30b0fe45edb12ae06acd9ec6c36f013373`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### CompletionStateBinding
**RDMS-10 / C02**, message `5f33fe0d-af3e-4f37-aeac-8979e64d941f`, lines 972–994; SHA-256 `fa6057f2f9c27814e892375aa6f9af148e8edcf0abcb5239dce4d4210d87b515`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### IntegratedCompletionEvidence
**RDMS-10 / C01**, message `e4828797-8ddb-48ae-a3e4-3e9ec47b70c3`, lines 1212–1240; SHA-256 `61a9b48635b374ccf5a78e9ed18ca8b50097e9d29a11b2dfcef1994e06afd3df`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-11 — Learning and context egress
**Boundary:** L3 → L5 → L7 | **Primary dossier owner:** `L7_RUNTIME_INTEGRATION.md`

**Source rule to retain:** No unreviewed auto-learning; egress must bind exact destination, payload and permitted context.

**Original schema names found:** 5 / 5 requested; **literal declaration occurrences:** 5.

### MemoryProposal
**RDMS-07 / Original draft**, message `938c1bc7-97a0-46ad-be19-cd3ba3ca125f`, lines 474–500; SHA-256 `954762e236b07d60a1c7480f60f9383a0f914a88043e9f541e6567ed0a6557af`; classification `HISTORICAL_DRAFT`; LITERAL STRUCTURE

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

### LearningAuthorizationBinding
**RDMS-07 / C01 and Adversarial Freeze Review 02 with freeze decision**, message `5ee62ad7-b67d-4382-be9d-cd85f6331a8c`, lines 392–404; SHA-256 `b874b8422dc956055f19393b3ef64da2d1e7499648ef92e4920324f6b4bd87b4`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### SealedOutboundContext
**RDMS-10 / C02**, message `5f33fe0d-af3e-4f37-aeac-8979e64d941f`, lines 858–882; SHA-256 `9a32bf619d57ada734a71008191da386626d6d7fbd7d4c8da3bd4383e79674f6`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### ContextDisclosureAdmission
**RDMS-10 / C01**, message `e4828797-8ddb-48ae-a3e4-3e9ec47b70c3`, lines 1460–1482; SHA-256 `cf8ab1e0abe27665db71d9e9661c8a78dc07d830b2123480121809753ff8df72`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### MemoryRetrievalCoverage
**RDMS-07 / C01 and Adversarial Freeze Review 02 with freeze decision**, message `5ee62ad7-b67d-4382-be9d-cd85f6331a8c`, lines 519–536; SHA-256 `141502db00751fe46e006bdf466aa1a1bfda4d18bec292c7a78aada5c4ac500f`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

```text
MemoryRetrievalCoverage {
    query_ref

    searchable_universe_ref

    index_snapshot_ref

    searched_scope

    retrieval_budget

    completeness:
        COMPLETE_WITHIN_SCOPE
        PARTIAL
        UNKNOWN

    excluded_scope_refs[]
}
```

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.


---
## X8-12 — Containment and recovery
**Boundary:** L3 → L6 → L1 | **Primary dossier owner:** `L6_RECOVERY.md`

**Source rule to retain:** A sandbox isolation claim requires evidence; ambiguous effects are not blindly retried.

**Original schema names found:** 5 / 5 requested; **literal declaration occurrences:** 5.

### RestoreContainmentProof
**RDMS-09 / C03**, message `89e41ed5-ac4e-4b95-9680-b9bec79f278a`, lines 739–766; SHA-256 `0b16b3bfce95f242d0305488af1d2ec2d2b2e4d4d6586cce16d0a378f4287b03`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

    proof_result:
        CONTAINED_WITHIN_SCOPE
        NOT_CONTAINED
        UNKNOWN
}
```

### PossibleExternalEffectAssessment
**RDMS-09 / C03**, message `89e41ed5-ac4e-4b95-9680-b9bec79f278a`, lines 509–537; SHA-256 `cc9b1b7dbb8cdcf3c67ee0a2c9d5c15eb170d44f8ce70cf6a9f923b008eeb7e9`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

    conclusion:
        CONFLICT_IMPOSSIBLE
        EFFECTS_RECONCILED
        FOLLOWUP_SAFE_UNDER_UNCERTAINTY
        NOT_PROVEN
}
```

### CrossFrontierAdmissionProof
**RDMS-09 / C03**, message `89e41ed5-ac4e-4b95-9680-b9bec79f278a`, lines 378–406; SHA-256 `a3c71d0e55272f3b8ee54a710026eb0875282e7c0811e1dcdb4341a975dc9203`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

### RecoveryBootstrapContract
**RDMS-09 / C02**, message `d59160dd-fa7a-4058-8892-69794f57e9b8`, lines 147–175; SHA-256 `3627f5109f1283c25e945cc14599a1d04c351156bf06ccf4b2be3c8b91339d72`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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
**RDMS-09 / C01**, message `74cf7fd3-01ca-4f35-abed-fbbc8716eb5c`, lines 194–212; SHA-256 `cc18adf30b86d39abb8b5a38533743fe9c335e5247cd5cea669f6e60a52862a5`; classification `APPROVED_LATER_SOURCE_TEXT`; LITERAL STRUCTURE

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

**Freeze-gate outcome:** HOLD — field presence and source excerpts do not independently establish a current effective producer/consumer contract.

