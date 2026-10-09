# GAIA-C06 — 15 Source-Verified Cross-Domain Guard Witnesses

**Status:** Confirmed presence of each named source shape and the later approved additional guard. This document DOES NOT prove that the later text deletes or replaces the earlier structure; both excerpts are verbatim. No inferred field migration or RPC signature is authorized.

## C06-W01 — RDMS-06: `DependencyStamp` + `DependencyCaptureReceipt`

- Current safe reading: Captured runtime reads must stay attributable to a scoped receipt; specialist cannot erase runtime-observed dependencies.
- Layer: `L4_TEMPORAL_SPECIALISTS.md`; route: `X8-10`.
- Earlier: `4bcbb2bf-86d9-4b93-9b1c-9f9529916667` lines 647–671 SHA-256 `eebe0f2d3f0cbd14f6cc9881d28b165d4410f5c08e645141c582ad48cb4d9588`.
- Later: `1ed5a815-4917-47b8-9e00-0b450a0581e2` lines 609–634 SHA-256 `d7ff97834f08dcd7e2556a12314b38b719619e9cec054f56018795a05827beba`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
DependencyStamp {
    stamp_id

    kind:
        STATE_ENTITY
        REPO_CONTENT
        QUERY_SCOPE
        OBSERVATION
        MEMORY
        TOOL
        ENVIRONMENT
        EXTERNAL_CONTRACT
        HUMAN_REQUIREMENT

    dependency_ref

    version_or_hash?

    validity_condition_ref?

    freshness_requirement:
        EXACT
        COMPATIBLE
        ADVISORY
}
```

### Later approved added guard (verbatim)
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

## C06-W02 — RDMS-06: `QueryDependencyStamp` + `QueryUniverseContract`

- Current safe reading: Negative query evidence is bounded by an explicitly identified universe, including new-entrant detection and coverage.
- Layer: `L4_TEMPORAL_SPECIALISTS.md`; route: `X8-10`.
- Earlier: `4bcbb2bf-86d9-4b93-9b1c-9f9529916667` lines 885–910 SHA-256 `1b3ae40841edc5f5853a4b5867cfaa3c76e2ed21564b77df463f92fe64b69e1f`.
- Later: `1ed5a815-4917-47b8-9e00-0b450a0581e2` lines 721–739 SHA-256 `89ddfd8c6cf1f6a7e79ca3df339c7e5f7faab36cb4c2ace818ce19e36e3f9653`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
QueryDependencyStamp {
    query_id

    query

    query_kind:
        SYMBOL_CALL
        IMPORT
        CONFIG_REFERENCE
        TEXTUAL_PROTOCOL
        RUNTIME_REGISTRY
        GLOBAL_SEARCH
        CUSTOM

    proof_scope

    dependency_frontier[]

    index_kind?
    index_generation?
    frontier_hash?

    invalidation_rule_ref

    repo_ref
}
```

### Later approved added guard (verbatim)
```text
QueryUniverseContract {
    universe_id

    query_kind

    membership_rule

    existing_member_frontier

    new_member_detection_frontier

    index_coverage_ref

    enumeration_completeness_ref

    dynamic_behavior_limitations[]

    universe_fingerprint
}
```

## C06-W03 — RDMS-07: `MemoryRetrievalResult` + `MemoryRetrievalCoverage`

- Current safe reading: Retrieval results do not prove absence beyond the searched scope; coverage and exclusions remain explicit.
- Layer: `L5_MEMORY.md`; route: `X8-02`.
- Earlier: `938c1bc7-97a0-46ad-be19-cd3ba3ca125f` lines 1068–1084 SHA-256 `e4ae715a27b230289f343447d8b7723501f62538065a5e61fa5dc5009c17c67d`.
- Later: `5ee62ad7-b67d-4382-be9d-cd85f6331a8c` lines 519–536 SHA-256 `141502db00751fe46e006bdf466aa1a1bfda4d18bec292c7a78aada5c4ac500f`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
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

### Later approved added guard (verbatim)
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

## C06-W04 — RDMS-07: `MemoryRecord` + `MemoryAccessPolicy`

- Current safe reading: Memory applicability does not confer unrestricted use or disclosure to a different security domain.
- Layer: `L5_MEMORY.md`; route: `X8-11`.
- Earlier: `938c1bc7-97a0-46ad-be19-cd3ba3ca125f` lines 588–621 SHA-256 `4d4f24539c6c089eb406401aea694a4db5f2db2be5b2c817c88d7a455c75aa68`.
- Later: `5ee62ad7-b67d-4382-be9d-cd85f6331a8c` lines 835–851 SHA-256 `f78b9f5b8f72738628c59f4a4d37094c9aa21266f40cec3f7ba8762ab518548d`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
MemoryRecord {
    memory_id

    memory_category

    claim_or_procedure_ref

    scope

    maturity

    applicability_conditions[]
    counter_conditions[]

    evidence_basis_refs[]

    provenance_refs[]

    dependency_set_ref

    confidence_assessment_ref

    stability

    version

    lifecycle

    derived_from[]
    supersedes[]

    created_commit_seq
    updated_commit_seq
}
```

### Later approved added guard (verbatim)
```text
MemoryAccessPolicy {
    memory_ref

    source_security_domain

    permitted_use_scopes[]

    permitted_recipient_domains[]

    sensitivity_classification

    disclosure_constraints[]

    derived_data_restrictions[]

    declassification_authority_ref?
}
```

## C06-W05 — RDMS-07: `MemoryProposal` + `LearningAuthorizationBinding`

- Current safe reading: Learning/promotion requires independent authorization binding; a proposal is not an authorized memory commit.
- Layer: `L5_MEMORY.md`; route: `X8-11`.
- Earlier: `938c1bc7-97a0-46ad-be19-cd3ba3ca125f` lines 474–500 SHA-256 `954762e236b07d60a1c7480f60f9383a0f914a88043e9f541e6567ed0a6557af`.
- Later: `5ee62ad7-b67d-4382-be9d-cd85f6331a8c` lines 392–404 SHA-256 `b874b8422dc956055f19393b3ef64da2d1e7499648ef92e4920324f6b4bd87b4`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
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

### Later approved added guard (verbatim)
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

## C06-W06 — RDMS-08: `CognitiveControlDecision` + `ControlDecisionTransaction`

- Current safe reading: Where decision and resulting legal transition form one recoverable unit, use a bound ControlCommit with version checks.
- Layer: `L2_COGNITION.md`; route: `INTERNAL_CONTROL_CONTRACT`.
- Earlier: `c955b372-e904-441b-8a0f-c8d9ae56c2f7` lines 549–563 SHA-256 `009388b00442f363ea9b80b43c1258033337b1d0dd498b440a0cd257b8ee767e`.
- Later: `a0f04ffe-181e-409d-9f94-d7d5c426502b` lines 251–270 SHA-256 `249663f07547d0aa77ad6b89e7d76b1dd2bfe9fba1f62d59d96615b6900764b9`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
CognitiveControlDecision {
    decision_id

    cycle_ref

    executive_epoch

    candidate_operations[]

    admissible_operations[]

    rejected_operations[] {
        operation_ref
        rejection_reason
    }
```

### Later approved added guard (verbatim)
```text
ControlDecisionTransaction {
    transaction_id

    executive_epoch

    current_goal_ref
    current_slice_ref?

    selected_operation_ref

    expected_canonical_state_version

    expected_focus_version

    governing_policy_version

    proposed_transition_ref

    idempotency_key
}
```

## C06-W07 — RDMS-08: `CompletionAssessment` + `FinalizationEvidenceContract`

- Current safe reading: A completion claim needs scoped evidence of acceptance satisfaction and cannot hide unresolved obligations.
- Layer: `L2_COGNITION.md`; route: `X8-10`.
- Earlier: `c955b372-e904-441b-8a0f-c8d9ae56c2f7` lines 1802–1818 SHA-256 `424c2007da92a94d41d327bde94a3477de178dddafa3bfdc879f974702f79104`.
- Later: `a0f04ffe-181e-409d-9f94-d7d5c426502b` lines 1233–1253 SHA-256 `250ab1ffc86da7bc5d9765c07c468e38982b3579849df390314035a7246bbb30`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
CompletionAssessment {
    goal_ref

    acceptance_criteria_refs[]

    verification_coverage_ref

    unresolved_critical_obligations[]

    unresolved_action_refs[]

    dependency_status

    known_limitations[]

    completion_claim
}
```

### Later approved added guard (verbatim)
```text
FinalizationEvidenceContract {
    goal_ref

    target_acceptance_refs[]

    satisfied_acceptance_refs[]

    unsatisfied_acceptance_refs[]

    verification_coverage_ref

    unresolved_required_actions[]

    unresolved_critical_obligations[]

    dependency_evaluation_ref

    authorized_completion_scope

    finalization_disposition
}
```

## C06-W08 — RDMS-09: `StartupRecoveryAssessment` + `RecoveryBootstrapContract`

- Current safe reading: Bootstrap infrastructure authority is separate from restored canonical Executive authority.
- Layer: `L6_RECOVERY.md`; route: `X8-12`.
- Earlier: `6ee1a6d1-3dfe-4de8-8c44-54ac4b07f8d4` lines 399–421 SHA-256 `d838b4864d766e28750c5f7c18430a14cf2e5460239b74d19c4479453dfa53e8`.
- Later: `d59160dd-fa7a-4058-8892-69794f57e9b8` lines 147–175 SHA-256 `3627f5109f1283c25e945cc14599a1d04c351156bf06ccf4b2be3c8b91339d72`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
StartupRecoveryAssessment {
    startup_id

    canonical_snapshot_ref

    ledger_replay_ref

    executive_epoch_ref

    action_reconciliation_ref

    trigger_recovery_ref

    specialist_recovery_ref

    dependency_validation_ref

    goal_restoration_ref

    unresolved_blockers[]

    readiness_for_normal_control
}
```

### Later approved added guard (verbatim)
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

## C06-W09 — RDMS-09: `ActionRecoveryAssessment` + `PossibleExternalEffectAssessment`

- Current safe reading: Possible unconfirmed external effects survive process failure and constrain follow-up safety.
- Layer: `L6_RECOVERY.md`; route: `X8-12`.
- Earlier: `6ee1a6d1-3dfe-4de8-8c44-54ac4b07f8d4` lines 615–635 SHA-256 `b2d4b5c7aaa35e7cdc8efe54a998ee0b39dc58b498976475f277f75a26814a78`.
- Later: `89e41ed5-ac4e-4b95-9680-b9bec79f278a` lines 509–537 SHA-256 `cc9b1b7dbb8cdcf3c67ee0a2c9d5c15eb170d44f8ce70cf6a9f923b008eeb7e9`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
ActionRecoveryAssessment {
    action_ref

    pre_failure_lifecycle

    effect_identity_ref?

    retry_policy

    outcome_probe_ref?

    observed_world_status

    reconciliation_evidence_refs[]

    dependent_operation_refs[]

    permitted_recovery_options[]

    unresolved_uncertainty[]
}
```

### Later approved added guard (verbatim)
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

## C06-W10 — RDMS-09: `UpgradePlan` + `CanonicalSchemaVisibilityContract`

- Current safe reading: Schema cutover must make one authoritative meaning visible and survive crash at the boundary.
- Layer: `L6_RECOVERY.md`; route: `X8-12`.
- Earlier: `6ee1a6d1-3dfe-4de8-8c44-54ac4b07f8d4` lines 1181–1201 SHA-256 `8798f4badd6d670ba8c26626ee59db3c7180223af898e9474f2a67330ea9d0f8`.
- Later: `d59160dd-fa7a-4058-8892-69794f57e9b8` lines 969–993 SHA-256 `677eefb64e756423623b112cdfa794ec4786e3ba322ac4766e023518cac9b31b`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
UpgradePlan {
    upgrade_id

    source_version

    target_version

    affected_components[]

    migration_steps[]

    compatibility_requirements[]

    rollback_or_recovery_strategy

    expected_downtime

    required_verification[]

    authority_refs[]
}
```

### Later approved added guard (verbatim)
```text
CanonicalSchemaVisibilityContract {
    migration_ref

    source_schema_version

    target_schema_version

    authoritative_schema_view

    allowed_reader_versions[]

    allowed_writer_versions[]

    compatibility_proof_refs[]

    migration_commit_boundary

    canonical_visibility_generation

    reference_consistency_requirements[]

    rollback_conditions[]

    forward_recovery_conditions[]
}
```

## C06-W11 — RDMS-09: `DataLifecyclePolicy` + `RecoveryDisclosureBarrier`

- Current safe reading: Restored/derived records remain subject to suppression before they can be disclosed.
- Layer: `L6_RECOVERY.md`; route: `X8-11`.
- Earlier: `6ee1a6d1-3dfe-4de8-8c44-54ac4b07f8d4` lines 1249–1269 SHA-256 `d32c3e44ac71e46192d62f1da86276df05296f61c62c3e7e3a0e9e41952346ef`.
- Later: `d59160dd-fa7a-4058-8892-69794f57e9b8` lines 849–875 SHA-256 `06be8ac3ba76b678e8b9b330ceac7ed27de139745310ad8eb202b6f54ebe4d93`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
DataLifecyclePolicy {
    policy_id

    data_class

    retention_scope

    permitted_storage_domains[]

    permitted_processing_domains[]

    expiry_or_erasure_conditions[]

    legal_hold_conditions[]

    derived_data_rules[]

    audit_requirements[]

    authorized_policy_version
}
```

### Later approved added guard (verbatim)
```text
RecoveryDisclosureBarrier {
    barrier_id

    restored_data_scope

    applicable_suppression_frontier

    authorized_processing_scope

    prohibited_disclosure_scope[]

    protected_processing_paths[]

    protected_indexing_paths[]

    protected_provider_paths[]

    protected_specialist_paths[]

    protected_export_paths[]

    effective_policy_version

    barrier_enforcement_status

    release_authorization_ref?
}
```

## C06-W12 — RDMS-10: `ToolExecutionRequest` + `EffectiveExecutionBinding`

- Current safe reading: Dispatch authorization must bind resolved final operation, arguments, adapter and actual execution principal.
- Layer: `L7_RUNTIME_INTEGRATION.md`; route: `X8-06`.
- Earlier: `99533762-bba8-407a-b27b-952a236c00a4` lines 809–827 SHA-256 `2ddc26f5f4222dd18c790a6cfc6ae9f11cac691aebdfecd16020479346c18419`.
- Later: `5f33fe0d-af3e-4f37-aeac-8979e64d941f` lines 423–449 SHA-256 `d5c98f9d9e69edf753fbdda12922a0df68c67cc556e02990bb963f0a93601da1`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
ToolExecutionRequest {
    action_ref

    dispatch_receipt_ref

    tool_identity

    execution_boundary_ref

    authorized_resource_scope

    arguments_ref

    effect_semantics_ref

    execution_generation

    timeout_policy
}
```

### Later approved added guard (verbatim)
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

## C06-W13 — RDMS-10: `ObservationIngressResult` + `ObservationCausalAttachmentContract`

- Current safe reading: Raw observation admissibility is distinct from later verified causal attachment to an action.
- Layer: `L7_RUNTIME_INTEGRATION.md`; route: `X8-07`.
- Earlier: `99533762-bba8-407a-b27b-952a236c00a4` lines 951–959 SHA-256 `c5f60baed7e577dadf9aef7a0d67d82589de02dce722ffbf012b6bfa6d16ad67`.
- Later: `5f33fe0d-af3e-4f37-aeac-8979e64d941f` lines 754–776 SHA-256 `6dbabd3c921605671ac0cd84d1d22319559f537e42ec6eb9c930984bf3121851`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
ObservationIngressResult {
    observation_ref

    append_disposition

    deduplication_result

    source_validation_result
}
```

### Later approved added guard (verbatim)
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

## C06-W14 — RDMS-10: `ContextPackage` + `SealedOutboundContext`

- Current safe reading: Outbound provider disclosure must be sealed to the actual context payload, destination and scope.
- Layer: `L7_RUNTIME_INTEGRATION.md`; route: `X8-11`.
- Earlier: `99533762-bba8-407a-b27b-952a236c00a4` lines 525–549 SHA-256 `42af8074562cf987c00a5635c73aea5a3be37923f905cda77195a277d2830e0a`.
- Later: `5f33fe0d-af3e-4f37-aeac-8979e64d941f` lines 858–882 SHA-256 `9a32bf619d57ada734a71008191da386626d6d7fbd7d4c8da3bd4383e79674f6`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
ContextPackage {
    context_package_id

    project_ref

    goal_ref

    focus_ref

    relevant_state_refs[]

    relevant_evidence_refs[]

    applicable_contract_refs[]

    mandatory_context_manifest_ref

    memory_retrieval_refs[]

    dependency_set_ref

    source_trust_metadata_refs[]

    disclosure_policy_ref
}
```

### Later approved added guard (verbatim)
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

## C06-W15 — RDMS-10: `TriggerEvaluationResult` + `TriggerDerivedWorkCommitment`

- Current safe reading: Accepted trigger results generate durable derived-work obligations, not implicit permission for external mutations.
- Layer: `L7_RUNTIME_INTEGRATION.md`; route: `X8-04`.
- Earlier: `99533762-bba8-407a-b27b-952a236c00a4` lines 1216–1226 SHA-256 `5d1bd536aba8106a068c38e5452dca175d8f4843393878118022e8e0057a0ade`.
- Later: `5f33fe0d-af3e-4f37-aeac-8979e64d941f` lines 273–297 SHA-256 `d9b47cadcb4d7322b954a69c91d8acb6c3e871b54bd31510b1e216f209714373`.
- **Gate:** legal fieldwise composition and actual durability/authority proof remain separate requirements.

### Earlier declaration (verbatim)
```text
TriggerEvaluationResult {
    trigger_ref

    firing_candidate_ref?

    canonical_reaction_key

    required_control_transition_ref?

    evaluation_status
}
```

### Later approved added guard (verbatim)
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
