# GAIA-C01 — Phase 5: Cross-Specification Contract Reconciliation

**Status: REVIEW CANDIDATE / NOT FROZEN.** This compares the 27 names reused across different original FCA/RDMS source documents. Different bodies are not automatically illegal; corrections override the draft only where explicitly adopted. Original sources and layer historical annexes remain unchanged.

## Evidence baseline

- FCA frozen baseline + 10 original RDMS source sets, containing 27 message parts.
- 467 lexical brace declarations found (not necessarily unique normative entities; illustrative examples are included).
- 413 distinct lexical names; 27 reused across sources.
- All comparisons below point to read-only original source files and part/line references. No source-level law change authorized.

## Triage summary

| Category | Count | Meaning |
|---|---:|---|
| `C01_COMPACT_ARTIFACT_MIGRATION` | 1 | Review classification, not adopted law |
| `CARDINALITY_AND_LIFECYCLE_REVIEW` | 1 | Review classification, not adopted law |
| `CORRECTION_SUPERSESSION` | 2 | Review classification, not adopted law |
| `CROSS_SPEC_EFFECTIVE_SCHEMA_UNRESOLVED` | 1 | Review classification, not adopted law |
| `ENUM_AND_IDENTITY_RECONCILIATION` | 1 | Review classification, not adopted law |
| `ENUM_AND_REFERENCE_MAPPING` | 1 | Review classification, not adopted law |
| `ENUM_CASE_NORMALIZATION` | 1 | Review classification, not adopted law |
| `FIELD_ALIAS_AND_REF_MAPPING` | 1 | Review classification, not adopted law |
| `LIFECYCLE_AND_PREDICTION_MAPPING` | 1 | Review classification, not adopted law |
| `LIFECYCLE_PROJECTION_RECONCILIATION` | 1 | Review classification, not adopted law |
| `PARENT_REFINEMENT` | 10 | Review classification, not adopted law |
| `PROVEN_ROLE_NAME_COLLISION` | 2 | Review classification, not adopted law |
| `RAW_NORMALIZATION_MAPPING` | 1 | Review classification, not adopted law |
| `ROLE_SPLIT_REQUIRES_DECISION` | 1 | Review classification, not adopted law |
| `STATUS_SEMANTICS_REVIEW` | 1 | Review classification, not adopted law |
| `THREE_WAY_PROJECTION` | 1 | Review classification, not adopted law |

## Cross-source 27-name decision matrix

| Type | Proposed owner | Review classification | Decision |
|---|---|---|---|
| `ActionEffectSemantics` | L3 | `FIELD_ALIAS_AND_REF_MAPPING` | PROPOSED; needs validation |
| `ActionProposal` | L3 | `ENUM_AND_IDENTITY_RECONCILIATION` | PROPOSED; needs validation |
| `ActionRecord` | L3 | `LIFECYCLE_PROJECTION_RECONCILIATION` | PROPOSED; needs validation |
| `CapabilityResult` | L2 canonical; L7 transport | `PROVEN_ROLE_NAME_COLLISION` | PROPOSED; needs validation |
| `Claim` | L2 | `CORRECTION_SUPERSESSION` | PROPOSED; needs validation |
| `Commitment` | L4 lifecycle; L2 cognitive references | `CROSS_SPEC_EFFECTIVE_SCHEMA_UNRESOLVED` | PROPOSED; needs validation |
| `ConfidenceAssessment` | L3 epistemic evidence; L2 consumers | `PARENT_REFINEMENT` | PROPOSED; needs validation |
| `ContradictionRecord` | L3 observations; L2 interpretation | `STATUS_SEMANTICS_REVIEW` | PROPOSED; needs validation |
| `Decision` | L2 | `PARENT_REFINEMENT` | PROPOSED; needs validation |
| `DependencyStamp` | L4 dependency semantics; L1 generic reference | `THREE_WAY_PROJECTION` | PROPOSED; needs validation |
| `EvidenceLink` | L3 | `CARDINALITY_AND_LIFECYCLE_REVIEW` | PROPOSED; needs validation |
| `Experiment` | L3 evidence/experiments | `LIFECYCLE_AND_PREDICTION_MAPPING` | PROPOSED; needs validation |
| `Goal` | L2 | `PARENT_REFINEMENT` | PROPOSED; needs validation |
| `GoalStack` | L2 | `PARENT_REFINEMENT` | PROPOSED; needs validation |
| `Hypothesis` | L2 | `CORRECTION_SUPERSESSION` | PROPOSED; needs validation |
| `InformationNeed` | L2 | `PARENT_REFINEMENT` | PROPOSED; needs validation |
| `Invariant` | L2 semantic model; L1 gate | `PARENT_REFINEMENT` | PROPOSED; needs validation |
| `MemoryProposal` | L5 | `PARENT_REFINEMENT` | PROPOSED; needs validation |
| `MemoryRetrievalResult` | L5 canonical; L7 transport | `PROVEN_ROLE_NAME_COLLISION` | PROPOSED; needs validation |
| `Observation` | L3 | `RAW_NORMALIZATION_MAPPING` | PROPOSED; needs validation |
| `OperationalCausalClaim` | L2 | `PARENT_REFINEMENT` | PROPOSED; needs validation |
| `QueryDependencyStamp` | L4 | `ENUM_AND_REFERENCE_MAPPING` | PROPOSED; needs validation |
| `ResumptionCapsule` | L4 | `C01_COMPACT_ARTIFACT_MIGRATION` | PROPOSED; needs validation |
| `SandboxActivityRecord` | L3 | `PARENT_REFINEMENT` | PROPOSED; needs validation |
| `Slice` | L2 | `PARENT_REFINEMENT` | PROPOSED; needs validation |
| `TemporalValidity` | L4 | `ENUM_CASE_NORMALIZATION` | PROPOSED; needs validation |
| `TriggerCondition` | L4 | `ROLE_SPLIT_REQUIRES_DECISION` | PROPOSED; needs validation |

## Evidence detail and field-level preservation prompts

### 01. `ActionEffectSemantics`

**Proposed owner:** L3  
**Classification:** `FIELD_ALIAS_AND_REF_MAPPING`  
**Rationale:** RDMS-04 changes outcome_probe/compensation to *_spec and timeout_policy to timeout_policy_ref; ensure effect semantics conserved.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1756`, SHA `581d7c8417786b26`. Fields: effect_identity?; retry_policy:; IDEMPOTENT; PROBE_THEN_RETRY; NO_AUTOMATIC_RETRY; idempotency_key?; outcome_probe?; compensation?; verification_mode:; DIRECT_EFFECT; ACKNOWLEDGEMENT_ONLY; BEST_EFFORT; timeout_policy
- `RDMS-04` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt:341`, SHA `2b16928c00b5e49f`. Fields: effect_identity?; retry_policy:; IDEMPOTENT; PROBE_THEN_RETRY; NO_AUTOMATIC_RETRY; idempotency_key?; outcome_probe_spec?; compensation_spec?; verification_mode:; DIRECT_EFFECT; ACKNOWLEDGEMENT_ONLY; BEST_EFFORT; timeout_policy_ref

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 02. `ActionProposal`

**Proposed owner:** L3  
**Classification:** `ENUM_AND_IDENTITY_RECONCILIATION`  
**Rationale:** FCA kind=file_write/shell/git/... vs RDMS-04 action_kind=FILESYSTEM/TERMINAL/GIT/TEST/BUILD/...; classification and preconditions must not be lost.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1663`, SHA `cc2711c38b5f5a5f`. Fields: id; requested_by; slice_id; goal_id; action_class:; EPHEMERAL_SANDBOX; SHARED_WORLD; kind:; file_write; file_delete; shell; git; database; network; deployment; debugger_control; other; target_scope[]; intent; expected_effects[]; preconditions[]; risk_profile; reversibility:; reversible; compensatable; partially_reversible; irreversible; rollback_or_compensation?; mode:; diagnostic; production; base_world_ref; authority_required; effect_semantics; status
- `RDMS-04` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt:97`, SHA `80c517ed3ccef74e`. Fields: action_proposal_id; project_id; requested_by_ref; goal_id; slice_id; action_kind:; TERMINAL; FILESYSTEM; GIT; TEST; BUILD; DEBUGGER; DATABASE; NETWORK; DEPLOYMENT; OTHER; requested_action_class:; EPHEMERAL_SANDBOX; SHARED_WORLD; intent; target_scope[]; expected_effects[]; preconditions[]; base_repo_ref?; base_world_ref?; dependency_set_ref?; risk_profile_ref?; reversibility:; REVERSIBLE; COMPENSATABLE; PARTIALLY_REVERSIBLE; IRREVERSIBLE; compensation_plan_ref?; effect_semantics_ref; execution_spec_ref; mode:; DIAGNOSTIC; PRODUCTION

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 03. `ActionRecord`

**Proposed owner:** L3  
**Classification:** `LIFECYCLE_PROJECTION_RECONCILIATION`  
**Rationale:** RDMS-04 adds authorization, before/after repo references and attempts; FCA execution_result and observation_ids need explicit equivalent persistence paths.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1883`, SHA `ff2cdd32ddddba43`. Fields: action_id; proposal_ref; lifecycle; world_ref_before; world_ref_after?; execution_result?; observation_ids[]; compensation_action_id?; started_at?; finished_at?
- `RDMS-04` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt:208`, SHA `faea5165f58fc365`. Fields: action_id; proposal_ref; authorization_ref; action_class; lifecycle; world_ref_before?; repo_ref_before?; effect_semantics_ref; latest_attempt_ref?; world_ref_after?; repo_ref_after?; effect_verification_refs[]; compensation_action_ref?; created_commit_seq; updated_commit_seq

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 04. `CapabilityResult`

**Proposed owner:** L2 canonical; L7 transport  
**Classification:** `PROVEN_ROLE_NAME_COLLISION`  
**Rationale:** FCA semantic result (11 fields) vs RDMS-10 invocation/refs/status envelope (9 fields): alias/rename transport only; no implicit dropped semantics.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1012`, SHA `769fbaaab0d513fb`. Fields: patch_proposal?; proposed_claims[]; proposed_hypotheses[]; proposed_information_needs[]; evidence_refs[]; tool_requests[]; experiment_requests[]; confidence_assessment?; specialist_request?; needs[]; rationale_summary?
- `RDMS-10` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt:384`, SHA `bcc80764033cdad3`. Fields: invocation_id; proposal_refs[]; information_need_refs[]; tool_request_refs[]; experiment_request_refs[]; assessment_refs[]; dependency_set_ref; provenance_refs[]; result_status

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 05. `Claim`

**Proposed owner:** L2  
**Classification:** `CORRECTION_SUPERSESSION`  
**Rationale:** RDMS-02 C01 replaces inline support with immutable SupportAssessment; preserve FCA evidence/provenance/state semantics.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:387`, SHA `43c470f915cfa3b4`. Fields: id; kind:; fact; belief; assumption; statement; scope; support:; unassessed; weak; moderate; strong; verified; evidence_for[]; evidence_against[]; provenance[]; status:; active; refuted; superseded; temporal_validity; version
- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:132`, SHA `b832ee2baff17a73`. Fields: claim_id; kind:; FACT; BELIEF; ASSUMPTION; statement; scope: ScopeSpec; support:; UNASSESSED; WEAK; MODERATE; STRONG; VERIFIED; support_assessed_at_commit?; grounding?; dependency_set_ref?; temporal_validity?; status:; ACTIVE; REFUTED; SUPERSEDED; superseded_by?
- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:211`, SHA `cecfe0c8f6ffec13`. Fields: kind = FACT; grounding = null

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 06. `Commitment`

**Proposed owner:** L4 lifecycle; L2 cognitive references  
**Classification:** `CROSS_SPEC_EFFECTIVE_SCHEMA_UNRESOLVED`  
**Rationale:** RDMS-02 C01 replaces multiple timers/triggers with reactivation_condition_ref; RDMS-05 says adopts RDMS-02 yet declares different fields. Need exact merged legal schema.

**Source declarations:**

- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:1380`, SHA `cd91e685721f769a`. Fields: commitment_id; statement; why_temporary; scope: ScopeSpec; owner_ref?; linked_entity_refs[]; created_at; due_at?; removal_trigger_id?; revisit_trigger_id?; status:; ACTIVE; DUE; SATISFIED; CANCELLED; SUPERSEDED; resolution_ref?
- `RDMS-02` — **C01, second review corrections and final freeze decision**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:2842`, SHA `5d44768b434df4c7`. Fields: ...; reactivation_condition_ref; status:; ACTIVE; DUE; SATISFIED; CANCELLED; SUPERSEDED; resolution_ref?
- `RDMS-05` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt:526`, SHA `8832f7cb81f74eab`. Fields: commitment_id; owner_ref; subject_ref; reason; required_followup; reactivation_condition_ref; lifecycle:; ACTIVE; DUE; SATISFIED; CANCELLED; SUPERSEDED; created_commit_seq; updated_commit_seq

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 07. `ConfidenceAssessment`

**Proposed owner:** L3 epistemic evidence; L2 consumers  
**Classification:** `PARENT_REFINEMENT`  
**Rationale:** RDMS-03 adds target/version/source references; preserve FCA basis, residual uncertainty and VERIFIED meaning.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:698`, SHA `2036f86aeced830e`. Fields: level:; unknown; low; medium; high; verified; basis: EvidenceLinkId[]; residual_uncertainty[]; assessed_at
- `RDMS-03` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:1412`, SHA `02a4d160af55e266`. Fields: confidence_assessment_id; target_ref; level:; UNKNOWN; LOW; MEDIUM; HIGH; VERIFIED; evidence_link_refs[]; verification_record_refs[]; residual_uncertainty[]; dependency_set_ref?; assessed_at_commit_seq; supersedes_assessment_id?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 08. `ContradictionRecord`

**Proposed owner:** L3 observations; L2 interpretation  
**Classification:** `STATUS_SEMANTICS_REVIEW`  
**Rationale:** FCA candidate/confirmed/explained/unresolved vs RDMS-03 candidate/confirmed/explained/resolved/dismissed; must distinguish unresolved from resolved.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:662`, SHA `9fcf8fdcad0b497f`. Fields: id; observations[]; subject; compared_scope; status:; candidate; confirmed; explained; unresolved; possible_dimensions:; time; input; environment; world_version; nondeterminism; measurement_error; information_need_id?
- `RDMS-03` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:632`, SHA `815450b81d496016`. Fields: contradiction_id; observation_refs[]; subject_ref?; subject_key?; comparison_scope; comparability; dimension_analysis[]; lifecycle:; CANDIDATE; CONFIRMED; EXPLAINED; RESOLVED; DISMISSED; information_need_id?; explanation_ref?; resolution_ref?
- `RDMS-03` — **C01 and Freeze Review 02 Final**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:2381`, SHA `a0b5226eaa78052a`. Fields: ...; dimension_analysis[]; explanation_ref?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 09. `Decision`

**Proposed owner:** L2  
**Classification:** `PARENT_REFINEMENT`  
**Rationale:** RDMS-02 introduces canonical option refs and lifecycle; FCA evidence, rejected rationale and tradeoffs must survive.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:805`, SHA `f02abde171d1b49f`. Fields: id; question; context; gravity:; low; medium; high; quality_drivers[]; constraints[]; alternatives[]; chosen; rejected[] {; option; reason; }; assumptions[]; accepted_tradeoffs[]; evidence_refs[]; expected_consequences[]; risks[]; revisit_triggers[]; status:; proposed; accepted; superseded; invalidated; version
- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:855`, SHA `76c22b352bb2b5a4`. Fields: decision_id; question; context; scope: ScopeSpec; gravity:; LOW; MEDIUM; HIGH; quality_drivers[]; constraints[]; alternatives[]; chosen_option_id?; rejected_options[]; assumption_refs[]; accepted_tradeoffs[]; expected_consequences[]; risk_refs[]; revisit_trigger_ids[]; status:; PROPOSED; ACCEPTED; SUPERSEDED; INVALIDATED; superseded_by?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 10. `DependencyStamp`

**Proposed owner:** L4 dependency semantics; L1 generic reference  
**Classification:** `THREE_WAY_PROJECTION`  
**Rationale:** FCA + RDMS-01 generic stamp + RDMS-06 typed stamp; distinguish plain state-reference metadata from domain freshness semantics.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2486`, SHA `869869e57b75103c`. Fields: kind:; state_entity; repo_content; query_scope; observation; memory; tool; environment; external_contract; human_requirement; ref; version_or_hash?; validity_condition?; freshness_requirement:; exact; compatible; advisory
- `RDMS-01` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt:794`, SHA `c48a75cf52e29b1c`. Fields: dependency_kind; ref; version_or_hash?; validity_condition?; freshness_requirement:; exact; compatible; advisory
- `RDMS-06` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt:659`, SHA `81190d88a77fd712`. Fields: stamp_id; kind:; STATE_ENTITY; REPO_CONTENT; QUERY_SCOPE; OBSERVATION; MEMORY; TOOL; ENVIRONMENT; EXTERNAL_CONTRACT; HUMAN_REQUIREMENT; dependency_ref; version_or_hash?; validity_condition_ref?; freshness_requirement:; EXACT; COMPATIBLE; ADVISORY

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 11. `EvidenceLink`

**Proposed owner:** L3  
**Classification:** `CARDINALITY_AND_LIFECYCLE_REVIEW`  
**Rationale:** FCA observation_id singular and target_type/id; RDMS-03 observation_refs[] and target_ref; preserve derivation, provenance and lawful acceptance.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:616`, SHA `f41267fdbfa15a7d`. Fields: id; observation_id; target_type:; claim; hypothesis; decision; risk; model_element; target_id; relation:; supports; weakens; contradicts; relevant; rationale; derivation:; deterministic; semantic; authoritative; status:; proposed; accepted; rejected; superseded
- `RDMS-03` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:461`, SHA `a1745a5a5047555c`. Fields: evidence_link_id; observation_refs[]; target_ref; relation:; SUPPORTS; WEAKENS; CONTRADICTS; RELEVANT; derivation:; DETERMINISTIC; SEMANTIC; AUTHORITATIVE; rationale; derivation_ref?; dependency_set_ref?; lifecycle:; PROPOSED; ACCEPTED; REJECTED; SUPERSEDED; accepted_commit_seq?
- `RDMS-03` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:514`, SHA `54527644170012d5`. Fields: observation_refs = []; rationale = "I strongly believe..."

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 12. `Experiment`

**Proposed owner:** L3 evidence/experiments  
**Classification:** `LIFECYCLE_AND_PREDICTION_MAPPING`  
**Rationale:** FCA experiment status includes running/completed/failed/cancelled; RDMS-03 uses experiment design and other records. Verify lifecycle split.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1595`, SHA `13673b48c403b6f2`. Fields: id; question; target_hypotheses[]; method; predictions[] {; hypothesis_id; expected_observation; discriminates_from[]; }; required_actions[]; risk_profile; status:; designed; authorized; running; completed; failed; cancelled; observation_ids[]; conclusion_proposal?; designed_at; executed_at?
- `RDMS-03` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:871`, SHA `3b4cf6a7a1ad3fa7`. Fields: experiment_id; question; purpose:; REPRODUCTION; DISCRIMINATING; CAUSAL_INTERVENTION; REGRESSION; PERFORMANCE; EXPLORATORY; OTHER; target_hypothesis_ids[]; method_spec; prediction_ids[]; required_action_specs[]; risk_refs[]; lifecycle:; DRAFT; DESIGNED; AUTHORIZED; RETIRED; CANCELLED; prediction_set_frozen_at_commit_seq?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 13. `Goal`

**Proposed owner:** L2  
**Classification:** `PARENT_REFINEMENT`  
**Rationale:** RDMS-02 adds kind/typed priority and lifecycle: map FCA parent/acceptance/status without narrowing meaning.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:735`, SHA `ec72ecec3d41cec8`. Fields: id; parent_id?; intent; acceptance[]; priority; status:; backlog; ready; active; suspended; blocked; waiting; deferred; verified; closed; obsolete; created_from
- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:576`, SHA `dc58da634c53e0b6`. Fields: goal_id; parent_goal_id?; goal_kind:; MISSION; MILESTONE; TASK; SUBGOAL; intent; acceptance_criteria[]; priority:; LOW; NORMAL; HIGH; CRITICAL; status:; BACKLOG; READY; ACTIVE; SUSPENDED; BLOCKED; WAITING; DEFERRED; VERIFIED; CLOSED; OBSOLETE; created_from; blocker_refs[]?; waiting_on_refs[]?; terminal_reason?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 14. `GoalStack`

**Proposed owner:** L2  
**Classification:** `PARENT_REFINEMENT`  
**Rationale:** RDMS-02 adds project identity/versioned references to FCA goal hierarchy; maintain nullability and order.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:760`, SHA `74f69cb7d23596de`. Fields: mission; milestone?; task?; subgoal?; current_operation?
- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:736`, SHA `8a4468eaffdd8825`. Fields: project_id; mission_goal_id?; milestone_goal_id?; task_goal_id?; subgoal_goal_id?; current_operation_ref?; entity_version

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 15. `Hypothesis`

**Proposed owner:** L2  
**Classification:** `CORRECTION_SUPERSESSION`  
**Rationale:** RDMS-02 C01 changes support into assessed references and scoped lifecycle; no automatic causal verification from rank.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:472`, SHA `f9845132f38afeff`. Fields: id; explanation; explains[]; assumptions[]; predictions[]; evidence_for[]; evidence_against[]; competing_hypotheses[]; experiments[]; support:; untested; plausible; supported; strong; causally_verified; refuted; status:; active; rejected; confirmed; superseded
- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:382`, SHA `ac8a90bdd1a64f1f`. Fields: hypothesis_id; explanation; scope: ScopeSpec; explains_refs[]; assumption_refs[]; prediction_refs[]; competing_hypothesis_ids[]; experiment_refs[]; support:; UNTESTED; PLAUSIBLE; SUPPORTED; STRONG; CAUSALLY_VERIFIED; REFUTED; status:; ACTIVE; REJECTED; CONFIRMED; SUPERSEDED; dependency_set_ref?; superseded_by?
- `RDMS-02` — **C01, second review corrections and final freeze decision**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:2117`, SHA `eaa16ef2ffa6b5ea`. Fields: ...; current_support_assessment_ref?; lifecycle:; ACTIVE; REJECTED; CONFIRMED; SUPERSEDED; closure_ref?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 16. `InformationNeed`

**Proposed owner:** L2  
**Classification:** `PARENT_REFINEMENT`  
**Rationale:** RDMS-02 expands resolution routes, scope and typed importance; preserve FCA unknown/resolved meaning.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:440`, SHA `9675de0f47bfe288`. Fields: id; question; importance; blocks[]; source_candidates[]; resolvable:; internally; reality; human; external_dependency; status:; open; investigating; resolved; obsolete; resolution?
- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:285`, SHA `4790799f601adf0e`. Fields: information_need_id; question; scope: ScopeSpec; importance:; LOW; MEDIUM; HIGH; CRITICAL; blocks[]:; EntityRef; source_candidates[]; resolution_routes[]:; INTERNAL_REASONING; REALITY; HUMAN; EXTERNAL_DEPENDENCY; status:; OPEN; INVESTIGATING; RESOLVED; OBSOLETE; resolution_ref?; opened_from?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 17. `Invariant`

**Proposed owner:** L2 semantic model; L1 gate  
**Classification:** `PARENT_REFINEMENT`  
**Rationale:** RDMS-02 permits enforcement_modes[] and scopes; required hard invariants cannot become advisory.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:887`, SHA `78f1a63fb971c412`. Fields: id; statement; scope; kind:; state; architectural; behavioral; business; security; semantic; severity:; hard; critical; advisory; enforcement:; commit_gate; pre_action_gate; post_action_verify; runtime_monitor; semantic_review; predicate?; verification_spec?; source_authority; version; status:; active; superseded; retired
- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:947`, SHA `8fa5e15e332d5b4a`. Fields: invariant_id; statement; scope: ScopeSpec; kind:; STATE; ARCHITECTURAL; BEHAVIORAL; BUSINESS; SECURITY; SEMANTIC; severity:; HARD; CRITICAL; ADVISORY; enforcement_modes[]:; COMMIT_GATE; PRE_ACTION_GATE; POST_ACTION_VERIFY; RUNTIME_MONITOR; SEMANTIC_REVIEW; predicate_ref?; verification_spec_ref?; source_authority_ref; status:; ACTIVE; SUPERSEDED; RETIRED; superseded_by?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 18. `MemoryProposal`

**Proposed owner:** L5  
**Classification:** `PARENT_REFINEMENT`  
**Rationale:** RDMS-07 adds source episode refs, dependency, provenance and category; preserve FCA contraindications and approval gate.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2237`, SHA `b32126ccb0b056c9`. Fields: claim; proposed_scope; source_episodes[]; causal_basis?; applicability_conditions[]; counter_conditions[]; counterexamples[]; evidence_refs[]; confidence_assessment; maturity_target
- `RDMS-07` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt:486`, SHA `ec572566ec818bf3`. Fields: proposal_id; claim; proposed_scope; source_episode_refs[]; causal_basis_ref?; applicability_conditions[]; counter_conditions[]; counterexamples[]; evidence_refs[]; confidence_assessment_ref; proposed_maturity; dependency_set_ref; provenance_ref; proposed_memory_category

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 19. `MemoryRetrievalResult`

**Proposed owner:** L5 canonical; L7 transport  
**Classification:** `PROVEN_ROLE_NAME_COLLISION`  
**Rationale:** RDMS-07 retrieval_id/query/candidates/coverage/freshness vs RDMS-10 memory_refs/relevance/provenance list; cannot substitute shorter transport for canonical result.

**Source declarations:**

- `RDMS-07` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt:1080`, SHA `194e50ab8f48675e`. Fields: retrieval_id; query_ref; candidate_refs[]; omitted_or_filtered_scope[]; ranking_policy_ref; retrieval_coverage; freshness_summary; created_at
- `RDMS-10` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt:1148`, SHA `9600853549876afd`. Fields: memory_refs[]; relevance_assessments[]; provenance_refs[]; applicability_assessments[]; trust_metadata_refs[]

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 20. `Observation`

**Proposed owner:** L3  
**Classification:** `RAW_NORMALIZATION_MAPPING`  
**Rationale:** FCA raw content/integrity vs RDMS-03 normalized_content/capture_integrity/raw_artifact; raw observation source must remain distinct from interpretation.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:581`, SHA `c695ae560bee8ff6`. Fields: id; source; source_authority?; world_ref; repo_ref?; environment_ref?; observed_at; content; raw_ref?; provenance; integrity:; verified; unverified; degraded
- `RDMS-03` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:82`, SHA `bc3b0b141c26d54a`. Fields: observation_id; project_id; observation_kind; source_ref; subject_ref?; observed_at; ingested_commit_seq; repo_ref?; world_ref?; environment_ref?; normalized_content; raw_artifact_ref?; provenance; capture_integrity; origin_ref?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 21. `OperationalCausalClaim`

**Proposed owner:** L2  
**Classification:** `PARENT_REFINEMENT`  
**Rationale:** FCA embeds mechanism/verification criteria; RDMS-02 holds verification_ref and scopes. Must preserve actual causal basis and references.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:514`, SHA `d9da8bfbcb1bcef0`. Fields: id; source_hypothesis_id; cause; effect; mechanism; scope {; repo_or_system_version; environment; inputs_or_preconditions[]; runtime_conditions[]; }; verification {; reproduced_failure; persisted_pre_intervention_prediction; targeted_intervention; predicted_effect_observed; regression_capture; alternatives_weakened[]; counterfactual_or_ablation?; }; evidence_refs[]; dependency_stamps[]; validity_conditions[]; contradictory_observations[]; status:; operationally_verified; stale; contradicted; superseded; promoted_at
- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:461`, SHA `d7959844f655a6e8`. Fields: causal_claim_id; source_hypothesis_id; cause; effect; mechanism; scope: CausalScope; verification_ref; dependency_set_ref; validity_conditions[]; contradictory_observation_refs[]; status:; OPERATIONALLY_VERIFIED; STALE; CONTRADICTED; SUPERSEDED; promoted_commit_seq; superseded_by?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 22. `QueryDependencyStamp`

**Proposed owner:** L4  
**Classification:** `ENUM_AND_REFERENCE_MAPPING`  
**Rationale:** Mostly field/enum normalization; verify proof_scope, frontier and invalidation reference encode FCA requirements.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2544`, SHA `8d371b8c1ce9c5bd`. Fields: query; query_kind:; symbol_call; import; config_reference; textual_protocol; runtime_registry; global_search; custom; proof_scope; dependency_frontier[]; index_kind?; index_generation?; frontier_hash?; invalidation_rule; repo_ref
- `RDMS-06` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt:897`, SHA `72e917291a0d7c2e`. Fields: query_id; query; query_kind:; SYMBOL_CALL; IMPORT; CONFIG_REFERENCE; TEXTUAL_PROTOCOL; RUNTIME_REGISTRY; GLOBAL_SEARCH; CUSTOM; proof_scope; dependency_frontier[]; index_kind?; index_generation?; frontier_hash?; invalidation_rule_ref; repo_ref

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 23. `ResumptionCapsule`

**Proposed owner:** L4  
**Classification:** `C01_COMPACT_ARTIFACT_MIGRATION`  
**Rationale:** RDMS-05 C01 replaces expanded inline snapshot with durable_payload_artifact_ref; verify recovery-critical FCA fields preserved by durable payload and integrity check.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2037`, SHA `0d155dbf562cee99`. Fields: task_id; suspended_from_state; base_state_version; repo_ref; goal; subgoal; current_focus; current_hypotheses[]; relevant_evidence[]; rejected_paths[]; temporary_changes[]; open_information_needs[]; next_concrete_action?; created_at
- `RDMS-05` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt:654`, SHA `b1ca0d0993b4cf9a`. Fields: capsule_id; project_id; task_or_goal_ref; suspended_from_state; base_canonical_commit_seq; repo_ref?; world_ref?; environment_ref?; dependency_set_ref?; current_focus_ref?; relevant_claim_refs[]; relevant_hypothesis_refs[]; relevant_evidence_refs[]; decision_refs[]; rejected_path_refs[]; active_slice_refs[]; unresolved_action_refs[]; open_information_need_refs[]; commitment_refs[]; temporary_change_refs[]; next_action_proposal_ref?; created_commit_seq
- `RDMS-05` — **C01**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt:2067`, SHA `9a662614fe12e56b`. Fields: capsule_id; task_or_goal_ref; suspended_from_state; canonical_snapshot_ref; relevant_entity_refs[]; dependency_set_ref; unresolved_action_refs[]; next_action_proposal_ref?; durable_payload_artifact_ref; content_integrity_ref; created_commit_seq

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 24. `SandboxActivityRecord`

**Proposed owner:** L3  
**Classification:** `PARENT_REFINEMENT`  
**Rationale:** RDMS-04 adds sandbox/proof/version and artifact refs; preserve disposable-only classification and operation summary.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1857`, SHA `31d790dff6dc50e9`. Fields: activity_id; slice_id; base_snapshot; containment_profile; operation_count; output_refs[]; observation_refs[]; result
- `RDMS-04` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt:1124`, SHA `50adb3faa10627ee`. Fields: activity_id; project_id; slice_id; sandbox_ref; containment_proof_ref; base_snapshot_ref; operation_count; activity_summary; output_artifact_refs[]; observation_refs[]; final_sandbox_snapshot_ref?; completed_at

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 25. `Slice`

**Proposed owner:** L2  
**Classification:** `PARENT_REFINEMENT`  
**Rationale:** RDMS-02 adds lifecycle/proofs and canonical IDs; preserve FCA expected_change_surface and risk/rollback semantics.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1246`, SHA `169635ad70527bd5`. Fields: id; goal_id; parent_slice?; intent; dependencies[]; allowed_scope[]; forbidden_scope[]; preconditions[]; invariants[]; contracts[]; expected_effects[]; expected_change_surface {; modules[]; contracts[]; state_owners[]; public_apis[]; persistent_data[]; }; risk_profile; proof_obligations[]; verification[]; rollback; base_state_version; base_repo_ref; status; actual_effects[]; actual_change_surface?
- `RDMS-02` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:1217`, SHA `0b123626f4413cff`. Fields: slice_id; goal_id; parent_slice_id?; intent; dependency_refs[]; allowed_scope[]; forbidden_scope[]; preconditions[]; invariant_refs[]; contract_refs[]; expected_effects[]; expected_change_surface; risk_refs[]; proof_obligations[]; verification_specs[]; rollback_spec?; base_state_version; base_repo_ref; status:; PLANNED; READY; EXECUTING; IMPLEMENTED; VERIFYING; VERIFIED; INTEGRATED; CLOSED; BLOCKED; SUSPENDED; FAILED; CANCELLED; OBSOLETE; actual_effects[]; actual_change_surface?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 26. `TemporalValidity`

**Proposed owner:** L4  
**Classification:** `ENUM_CASE_NORMALIZATION`  
**Rationale:** Fields structurally match apart from capitalization; inspect shared type/version and nullability, do not duplicate canonical type.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2088`, SHA `e40c6165505ab0ef`. Fields: observed_at?; verified_at?; repo_ref?; state_version?; valid_until_condition?; freshness:; current; stale; unknown
- `RDMS-05` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt:803`, SHA `fb5ebce36de924ef`. Fields: observed_at?; verified_at?; repo_ref?; state_version?; valid_until_condition?; freshness:; CURRENT; STALE; UNKNOWN

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

### 27. `TriggerCondition`

**Proposed owner:** L4  
**Classification:** `ROLE_SPLIT_REQUIRES_DECISION`  
**Rationale:** FCA TriggerCondition includes generation/reaction_key/lifecycle, RDMS-05 TriggerCondition appears predicate component with condition_id. Explicit full-trigger vs predicate distinction required.

**Source declarations:**

- `FCA v1.0.1` — **FCA v1.0.1 baseline**, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2126`, SHA `dc0d9ce29e01dc57`. Fields: id; generation; semantics:; ONE_SHOT; REARMABLE; LEVEL_TRIGGERED; EDGE_TRIGGERED; kind:; state_event; repo_change; metric_threshold; temporal; external_event; human_event; semantic_review; watches[]; predicate?; source_cursor?; reaction_key; linked_object; on_fire; status:; armed; fired; satisfied; cancelled; last_evaluated_at; last_fire_id?
- `RDMS-05` — **Original draft**, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt:191`, SHA `5a81e303341509ba`. Fields: condition_id; kind:; STATE_EVENT; REPO_CHANGE; METRIC_THRESHOLD; TEMPORAL; EXTERNAL_EVENT; HUMAN_EVENT; SEMANTIC_REVIEW; COMPOSITE; predicate_spec; dependency_set_ref?; required_evidence_policy_ref?

**Required decision:** Preserve higher-authority/accepted fields and legal meanings; use explicit projection or corrected name for transport-only data, without rewriting frozen source.

## High-priority collision rulings (proposed)

**GAIA-B01 / CapabilityResult:** Retain FCA §23 eleven-field semantic `CapabilityResult` (L2). Rename the RDMS-10 invocation/transport shape to `CapabilityTransportResult` in L7 and prove full canonical-result recovery by reference or lossless projection. No silent RDMS-10 amendment.

**GAIA-B03 / MemoryRetrievalResult:** Retain RDMS-07 result including retrieval ID, query, candidate references, omitted/filtered scope, ranking policy, coverage, freshness and creation time in L5. Rename RDMS-10 lightweight return to `MemoryRetrievalTransportResult` in L7, with explicit resolution to canonical RDMS-07 result. Do not silently erase coverage/freshness.

**GAIA-B04 / Commitment:** RDMS-02 C01 replaces parallel due/trigger fields by reactivation-condition root; RDMS-05 claims adoption but has distinct identity/body fields. Choose a single canonical entity representation across L2/L4; leave definition unresolved until line-level C01 precedence and data migration are explicitly reviewed.

**GAIA-B05 / TriggerCondition:** FCA uses the name for a full generation-bearing trigger with reaction identity; RDMS-05 uses it for a condition/predicate. Require an explicit full-trigger vs predicate record distinction or a proven lossless composition; do not conflate.

**GAIA-RCAP / ResumptionCapsule:** RDMS-05 C01 stores a compact canonical capsule with a durable referenced payload; this may satisfy FCA fields but requires a field-preservation manifest, content integrity and failure-recovery semantics. Not a proven conflict by itself.

## Next gate

1. Review and explicitly approve changes to integration-only names (`CapabilityTransportResult`, `MemoryRetrievalTransportResult`).
2. Produce exact effective schemas and migrations for Commitment, TriggerCondition, ResumptionCapsule and any remaining semantically non-equivalent parent refinements.
3. Resolve all proposal-only classifications before marking per-layer specs `FROZEN_CONSOLIDATED`.
4. Run schema ownership and semantic conformance review; no production code authorized.
