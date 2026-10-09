# GAIA-C01 Phase 7 — Remaining 22 Contract Reconciliations

> **REVIEW CANDIDATE — NO CANONICAL TYPE MIGRATION APPROVED.** This record is a source-anchored, field-preservation analysis of all 22 names left open in Phase 6. Historical FCA/RDMS texts are immutable. No runtime tests have been run.

## Method and status meanings

- `LOW_RISK_MAPPING_CANDIDATE`: apparent syntax/identity refinement; requires round-trip conformance and owner approval. Not auto-approved.
- `CONDITIONAL_PRESERVATION`: valid only with proof that required refs, authority, histories and fields survive.
- `SEMANTIC_GATE_OPEN`: unsafe to declare equivalent until specific meaning/lifecycle/cardinality mismatch is resolved.

## Audit coverage

| Status | Count | Freeze consequence |
|---|---:|---|
| `LOW_RISK_MAPPING_CANDIDATE` | 5 | No automatic promotion |
| `CONDITIONAL_PRESERVATION` | 9 | No automatic promotion |
| `SEMANTIC_GATE_OPEN` | 8 | No automatic promotion |

**22/22 remaining reused names reviewed; 27/27 total cross-source names now have individual analysis when combined with Phase 6.** The lexical list is not an exhaustive guarantee over all prose-defined contracts or interface methods.

## Decisions by original contract owner

| ID | Type | Owner | Triage |
|---|---|---|---|
| P7-01 | `ActionEffectSemantics` | L3 | `CONDITIONAL_PRESERVATION` |
| P7-02 | `ActionProposal` | L3 | `SEMANTIC_GATE_OPEN` |
| P7-03 | `ActionRecord` | L3 | `CONDITIONAL_PRESERVATION` |
| P7-04 | `Claim` | L2 | `SEMANTIC_GATE_OPEN` |
| P7-05 | `ConfidenceAssessment` | L3 | `CONDITIONAL_PRESERVATION` |
| P7-06 | `ContradictionRecord` | L3 | `SEMANTIC_GATE_OPEN` |
| P7-07 | `Decision` | L2 | `CONDITIONAL_PRESERVATION` |
| P7-08 | `DependencyStamp` | L4 | `CONDITIONAL_PRESERVATION` |
| P7-09 | `EvidenceLink` | L3 | `SEMANTIC_GATE_OPEN` |
| P7-10 | `Experiment` | L3 | `SEMANTIC_GATE_OPEN` |
| P7-11 | `Goal` | L2 | `LOW_RISK_MAPPING_CANDIDATE` |
| P7-12 | `GoalStack` | L2 | `LOW_RISK_MAPPING_CANDIDATE` |
| P7-13 | `Hypothesis` | L2 | `SEMANTIC_GATE_OPEN` |
| P7-14 | `InformationNeed` | L2 | `LOW_RISK_MAPPING_CANDIDATE` |
| P7-15 | `Invariant` | L2 | `CONDITIONAL_PRESERVATION` |
| P7-16 | `MemoryProposal` | L5 | `CONDITIONAL_PRESERVATION` |
| P7-17 | `Observation` | L3 | `SEMANTIC_GATE_OPEN` |
| P7-18 | `OperationalCausalClaim` | L2 | `SEMANTIC_GATE_OPEN` |
| P7-19 | `QueryDependencyStamp` | L4 | `LOW_RISK_MAPPING_CANDIDATE` |
| P7-20 | `SandboxActivityRecord` | L3 | `CONDITIONAL_PRESERVATION` |
| P7-21 | `Slice` | L2 | `CONDITIONAL_PRESERVATION` |
| P7-22 | `TemporalValidity` | L4 | `LOW_RISK_MAPPING_CANDIDATE` |

## Detailed field-conservation crosswalk

### P7-01 — `ActionEffectSemantics`

**Owner:** L3; **status:** `CONDITIONAL_PRESERVATION`; **source comparison:** `FIELD_ALIAS_AND_REF_MAPPING`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1756`; declaration SHA-256 `581d7c8417786b26dbad453318909b0f434b6fcf75c355c492f89a05ef46262e`. Fields/values: `effect_identity?; retry_policy:; IDEMPOTENT; PROBE_THEN_RETRY; NO_AUTOMATIC_RETRY; idempotency_key?; outcome_probe?; compensation?; verification_mode:; DIRECT_EFFECT; ACKNOWLEDGEMENT_ONLY; BEST_EFFORT; timeout_policy`
- `RDMS-04` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt:341`; declaration SHA-256 `2b16928c00b5e49fcb5dcef348fff062c7c65c40cb8d96a528590f5c25d9a2e2`. Fields/values: `effect_identity?; retry_policy:; IDEMPOTENT; PROBE_THEN_RETRY; NO_AUTOMATIC_RETRY; idempotency_key?; outcome_probe_spec?; compensation_spec?; verification_mode:; DIRECT_EFFECT; ACKNOWLEDGEMENT_ONLY; BEST_EFFORT; timeout_policy_ref`

**Candidate legal interpretation:** FCA outcome_probe / compensation / timeout_policy are semantic specifications; RDMS-04 *_spec / *_ref representations must resolve to semantically identical objects. Retry enum and verification mode remain unchanged.

**Mandatory conformance evidence:** Proof: dereference and compare probe, compensation and timeout semantics; missing/mismatched references fail closed. No conversion of IDEMPOTENT into exactly-once.

**Unsafe shortcut / blocker:** Inability to reconstruct original outcome-probe/compensation and timeout contracts must block conversion.

**Acceptance vector:** `AT7-01` — scenario defined, **NOT EXECUTED**.

### P7-02 — `ActionProposal`

**Owner:** L3; **status:** `SEMANTIC_GATE_OPEN`; **source comparison:** `ENUM_AND_IDENTITY_RECONCILIATION`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1663`; declaration SHA-256 `cc2711c38b5f5a5f53b9082f86c6f03bae9155b2190413d61e3a304a317b1df5`. Fields/values: `id; requested_by; slice_id; goal_id; action_class:; EPHEMERAL_SANDBOX; SHARED_WORLD; kind:; file_write; file_delete; shell; git; database; network; deployment; debugger_control; other; target_scope[]; intent; expected_effects[]; preconditions[]; risk_profile; reversibility:; reversible; compensatable; partially_reversible; irreversible; rollback_or_compensation?; mode:; diagnostic; production; base_world_ref; authority_required; effect_semantics; status`
- `RDMS-04` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt:97`; declaration SHA-256 `80c517ed3ccef74ed5b3b11292af8825782a16aeaf8fca3fed36b1c9b00eac34`. Fields/values: `action_proposal_id; project_id; requested_by_ref; goal_id; slice_id; action_kind:; TERMINAL; FILESYSTEM; GIT; TEST; BUILD; DEBUGGER; DATABASE; NETWORK; DEPLOYMENT; OTHER; requested_action_class:; EPHEMERAL_SANDBOX; SHARED_WORLD; intent; target_scope[]; expected_effects[]; preconditions[]; base_repo_ref?; base_world_ref?; dependency_set_ref?; risk_profile_ref?; reversibility:; REVERSIBLE; COMPENSATABLE; PARTIALLY_REVERSIBLE; IRREVERSIBLE; compensation_plan_ref?; effect_semantics_ref; execution_spec_ref; mode:; DIAGNOSTIC; PRODUCTION`

**Candidate legal interpretation:** RDMS-04 action_kind is a broader tool category, whereas FCA kind includes file_write vs file_delete and shell. Keep requested_action_class distinct from ActionGate actual classification; preserve precise operation in execution_spec_ref.

**Mandatory conformance evidence:** Proof: inject file_write and file_delete under FILESYSTEM, shell under TERMINAL; round-trip must preserve legal effect kind, authority, preconditions and reversibility.

**Unsafe shortcut / blocker:** Many-to-one kind mapping could conceal destructive operation; no automatic mapping until exact operation discriminator proven.

**Acceptance vector:** `AT7-02` — scenario defined, **NOT EXECUTED**.

### P7-03 — `ActionRecord`

**Owner:** L3; **status:** `CONDITIONAL_PRESERVATION`; **source comparison:** `LIFECYCLE_PROJECTION_RECONCILIATION`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1883`; declaration SHA-256 `ff2cdd32ddddba43e8251e3d78fa815d22361f25de6cea54d59f546556580fa9`. Fields/values: `action_id; proposal_ref; lifecycle; world_ref_before; world_ref_after?; execution_result?; observation_ids[]; compensation_action_id?; started_at?; finished_at?`
- `RDMS-04` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt:208`; declaration SHA-256 `faea5165f58fc365a0d3d4d88ffd1670a1fb5fd07165c559ca15526e0559ea4c`. Fields/values: `action_id; proposal_ref; authorization_ref; action_class; lifecycle; world_ref_before?; repo_ref_before?; effect_semantics_ref; latest_attempt_ref?; world_ref_after?; repo_ref_after?; effect_verification_refs[]; compensation_action_ref?; created_commit_seq; updated_commit_seq`

**Candidate legal interpretation:** FCA execution_result, observation_ids[], timestamps and compensation_action_id are not present as identical RDMS-04 fields; recover them through attempt/result/verification/observation references and legal sequence metadata.

**Mandatory conformance evidence:** Proof: replay ACTION with multiple attempts, partial effect, observations and compensation, then reconstruct every FCA recovery-critical fact.

**Unsafe shortcut / blocker:** Single latest_attempt_ref is insufficient if attempt history is not separately durable and enumerable.

**Acceptance vector:** `AT7-03` — scenario defined, **NOT EXECUTED**.

### P7-04 — `Claim`

**Owner:** L2; **status:** `SEMANTIC_GATE_OPEN`; **source comparison:** `CORRECTION_SUPERSESSION`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:387`; declaration SHA-256 `43c470f915cfa3b4ed377cf421cd1760c1467d175eabd53d520c55f6a73f6089`. Fields/values: `id; kind:; fact; belief; assumption; statement; scope; support:; unassessed; weak; moderate; strong; verified; evidence_for[]; evidence_against[]; provenance[]; status:; active; refuted; superseded; temporal_validity; version`
- `RDMS-02` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:132`; declaration SHA-256 `b832ee2baff17a73b0fb062850206f5b917b0acde2337e4a76984a28cf56cb6b`. Fields/values: `claim_id; kind:; FACT; BELIEF; ASSUMPTION; statement; scope: ScopeSpec; support:; UNASSESSED; WEAK; MODERATE; STRONG; VERIFIED; support_assessed_at_commit?; grounding?; dependency_set_ref?; temporal_validity?; status:; ACTIVE; REFUTED; SUPERSEDED; superseded_by?`
- `RDMS-02` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:211`; declaration SHA-256 `cecfe0c8f6ffec132a826f6bc6f82c0d11639a5196f9255b601e8d420b6ef173`. Fields/values: `kind = FACT; grounding = null`

**Candidate legal interpretation:** RDMS-02 C01 replaces inline support certainty with separate SupportAssessment semantics; FCA evidence_for[], evidence_against[] and provenance[] cannot be dropped or converted into a VERIFIED scalar. Keep provenance and accepted EvidenceLinks independently accessible.

**Mandatory conformance evidence:** Proof: old claim with supporting and contradictory evidence projects into effective form and reconstructs history/assessment; no self-certified FACT or fabricated VERIFIED.

**Unsafe shortcut / blocker:** Support is not a standalone truth claim; accepted correction precedence and evidence cardinality require proof.

**Acceptance vector:** `AT7-04` — scenario defined, **NOT EXECUTED**.

### P7-05 — `ConfidenceAssessment`

**Owner:** L3; **status:** `CONDITIONAL_PRESERVATION`; **source comparison:** `PARENT_REFINEMENT`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:698`; declaration SHA-256 `2036f86aeced830e0d8151d608f235ff95bd2d4874de38193bdbd2b6ab3a8ac9`. Fields/values: `level:; unknown; low; medium; high; verified; basis: EvidenceLinkId[]; residual_uncertainty[]; assessed_at`
- `RDMS-03` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:1412`; declaration SHA-256 `02a4d160af55e2669ff1ca0d3f0ae80c0e6dca6046c3398d3e8f08538f28635e`. Fields/values: `confidence_assessment_id; target_ref; level:; UNKNOWN; LOW; MEDIUM; HIGH; VERIFIED; evidence_link_refs[]; verification_record_refs[]; residual_uncertainty[]; dependency_set_ref?; assessed_at_commit_seq; supersedes_assessment_id?`

**Candidate legal interpretation:** FCA level/basis/residual_uncertainty/assessed_at correspond to RDMS-03 scoped, versioned assessment and evidence_link_refs, with additional verification_record_refs. VERIFIED requires actual verification records and applicable scope.

**Mandatory conformance evidence:** Proof: resolve basis to accepted evidence links and proof records; distinguish historical assessment time from commit sequence and reject stale VERIFIED promotion.

**Unsafe shortcut / blocker:** Commit sequence does not equal source wall-clock timestamp.

**Acceptance vector:** `AT7-05` — scenario defined, **NOT EXECUTED**.

### P7-06 — `ContradictionRecord`

**Owner:** L3; **status:** `SEMANTIC_GATE_OPEN`; **source comparison:** `STATUS_SEMANTICS_REVIEW`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:662`; declaration SHA-256 `9fcf8fdcad0b497f8ad71c7aab70d192662d63cd26fbd818160add44c0cff747`. Fields/values: `id; observations[]; subject; compared_scope; status:; candidate; confirmed; explained; unresolved; possible_dimensions:; time; input; environment; world_version; nondeterminism; measurement_error; information_need_id?`
- `RDMS-03` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:632`; declaration SHA-256 `815450b81d4960169dd120ee07c4e38c279797c70c343bf23c958d4532a841bd`. Fields/values: `contradiction_id; observation_refs[]; subject_ref?; subject_key?; comparison_scope; comparability; dimension_analysis[]; lifecycle:; CANDIDATE; CONFIRMED; EXPLAINED; RESOLVED; DISMISSED; information_need_id?; explanation_ref?; resolution_ref?`
- `RDMS-03` — C01 and Freeze Review 02 Final, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:2381`; declaration SHA-256 `a0b5226eaa78052ac6de366d6a51852e7a763b8ce1e0878a566e66ca8db4ad08`. Fields/values: `...; dimension_analysis[]; explanation_ref?`

**Candidate legal interpretation:** FCA UNRESOLVED is a live epistemic condition, not RDMS-03 RESOLVED. C01 limits dimension_analysis to comparability and explanation_ref to separate causal entities. Keep unresolved/dismissed/resolved distinctions.

**Mandatory conformance evidence:** Proof: map candidate/confirmed/explained/unresolved scenarios without treating unresolved as resolved; late contradictory observations must preserve status and explanation provenance.

**Unsafe shortcut / blocker:** No blind enum conversion for UNRESOLVED. Lifecycle meaning and derived unresolved predicate need legal ownership.

**Acceptance vector:** `AT7-06` — scenario defined, **NOT EXECUTED**.

### P7-07 — `Decision`

**Owner:** L2; **status:** `CONDITIONAL_PRESERVATION`; **source comparison:** `PARENT_REFINEMENT`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:805`; declaration SHA-256 `f02abde171d1b49fba2d05dfdb9d6208a680c1d4c8d911fa089584d422862ae5`. Fields/values: `id; question; context; gravity:; low; medium; high; quality_drivers[]; constraints[]; alternatives[]; chosen; rejected[] {; option; reason; }; assumptions[]; accepted_tradeoffs[]; evidence_refs[]; expected_consequences[]; risks[]; revisit_triggers[]; status:; proposed; accepted; superseded; invalidated; version`
- `RDMS-02` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:855`; declaration SHA-256 `76c22b352bb2b5a45a7f263c47a9b5b630110cc6c2b24170bddbff63aabf02ab`. Fields/values: `decision_id; question; context; scope: ScopeSpec; gravity:; LOW; MEDIUM; HIGH; quality_drivers[]; constraints[]; alternatives[]; chosen_option_id?; rejected_options[]; assumption_refs[]; accepted_tradeoffs[]; expected_consequences[]; risk_refs[]; revisit_trigger_ids[]; status:; PROPOSED; ACCEPTED; SUPERSEDED; INVALIDATED; superseded_by?`

**Candidate legal interpretation:** RDMS-02 stores chosen_option_id, rejected_options and risk refs; FCA rejected[{option,reason}], evidence_refs[] and version must remain recoverable in canonical decision relations.

**Mandatory conformance evidence:** Proof: rejected option rationales, evidence, constraints, tradeoffs, accepted status and supersession all round-trip via defined refs.

**Unsafe shortcut / blocker:** Flattening rejected[] to option IDs drops why rejected, violating cognitive decision memory.

**Acceptance vector:** `AT7-07` — scenario defined, **NOT EXECUTED**.

### P7-08 — `DependencyStamp`

**Owner:** L4; **status:** `CONDITIONAL_PRESERVATION`; **source comparison:** `THREE_WAY_PROJECTION`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2486`; declaration SHA-256 `869869e57b75103ca8e45c2f73d873a390b24565b52267bc57a3c0aa4becb812`. Fields/values: `kind:; state_entity; repo_content; query_scope; observation; memory; tool; environment; external_contract; human_requirement; ref; version_or_hash?; validity_condition?; freshness_requirement:; exact; compatible; advisory`
- `RDMS-01` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt:794`; declaration SHA-256 `c48a75cf52e29b1c4bcecd8946c6d844b73040ec34908725c29835205d622c3a`. Fields/values: `dependency_kind; ref; version_or_hash?; validity_condition?; freshness_requirement:; exact; compatible; advisory`
- `RDMS-06` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt:659`; declaration SHA-256 `81190d88a77fd712d0891421fdc8bb4da89a61da03277a3f302cd6bc6c5bf795`. Fields/values: `stamp_id; kind:; STATE_ENTITY; REPO_CONTENT; QUERY_SCOPE; OBSERVATION; MEMORY; TOOL; ENVIRONMENT; EXTERNAL_CONTRACT; HUMAN_REQUIREMENT; dependency_ref; version_or_hash?; validity_condition_ref?; freshness_requirement:; EXACT; COMPATIBLE; ADVISORY`

**Candidate legal interpretation:** RDMS-01 has a generic control dependency stamp; RDMS-06 supplies typed stamps, and FCA lists the admissible domains. Use RDMS-06 as semantic owner of freshness stamps; RDMS-01 references/projections must not become a second validator.

**Mandatory conformance evidence:** Proof: convert all nine FCA kinds, preserve exact/compatible/advisory requirements, version hashes and condition refs; fail closed on unknown kind.

**Unsafe shortcut / blocker:** Shared name across three sources does not imply three legal owners.

**Acceptance vector:** `AT7-08` — scenario defined, **NOT EXECUTED**.

### P7-09 — `EvidenceLink`

**Owner:** L3; **status:** `SEMANTIC_GATE_OPEN`; **source comparison:** `CARDINALITY_AND_LIFECYCLE_REVIEW`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:616`; declaration SHA-256 `f41267fdbfa15a7d1394bbae60759426db0dc70e7f7ca13ccc504810a09570a4`. Fields/values: `id; observation_id; target_type:; claim; hypothesis; decision; risk; model_element; target_id; relation:; supports; weakens; contradicts; relevant; rationale; derivation:; deterministic; semantic; authoritative; status:; proposed; accepted; rejected; superseded`
- `RDMS-03` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:461`; declaration SHA-256 `a1745a5a5047555c8904911219d93643ca860bab5413f282ac9aa49ca91ab3e4`. Fields/values: `evidence_link_id; observation_refs[]; target_ref; relation:; SUPPORTS; WEAKENS; CONTRADICTS; RELEVANT; derivation:; DETERMINISTIC; SEMANTIC; AUTHORITATIVE; rationale; derivation_ref?; dependency_set_ref?; lifecycle:; PROPOSED; ACCEPTED; REJECTED; SUPERSEDED; accepted_commit_seq?`
- `RDMS-03` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:514`; declaration SHA-256 `54527644170012d590c3a1175609c59091b97675ad478084ed24cd738b2c3677`. Fields/values: `observation_refs = []; rationale = "I strongly believe..."`

**Candidate legal interpretation:** FCA observation_id singular versus RDMS-03 observation_refs[] plural. Multiple inputs must preserve individual provenance and cannot be naively duplicated into accepted independent EvidenceLinks. Empty refs are never accepted evidence merely because proposal schema permits it.

**Mandatory conformance evidence:** Proof: one-to-many evidence sources, cardinality, derivation kind, acceptance, target relation and atomic accepted commit; reject unsupported accepted link.

**Unsafe shortcut / blocker:** A rejected or ungrounded proposal cannot become accepted supporting evidence through projection.

**Acceptance vector:** `AT7-09` — scenario defined, **NOT EXECUTED**.

### P7-10 — `Experiment`

**Owner:** L3; **status:** `SEMANTIC_GATE_OPEN`; **source comparison:** `LIFECYCLE_AND_PREDICTION_MAPPING`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1595`; declaration SHA-256 `13673b48c403b6f2ddf297eedb0e14d682a59f20fd5553b150d985eb00916a0b`. Fields/values: `id; question; target_hypotheses[]; method; predictions[] {; hypothesis_id; expected_observation; discriminates_from[]; }; required_actions[]; risk_profile; status:; designed; authorized; running; completed; failed; cancelled; observation_ids[]; conclusion_proposal?; designed_at; executed_at?`
- `RDMS-03` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:871`; declaration SHA-256 `3b4cf6a7a1ad3fa7492c5d02b9df25ded5fe878e0bc0aeeb4b7c9d1e4a9ed86f`. Fields/values: `experiment_id; question; purpose:; REPRODUCTION; DISCRIMINATING; CAUSAL_INTERVENTION; REGRESSION; PERFORMANCE; EXPLORATORY; OTHER; target_hypothesis_ids[]; method_spec; prediction_ids[]; required_action_specs[]; risk_refs[]; lifecycle:; DRAFT; DESIGNED; AUTHORIZED; RETIRED; CANCELLED; prediction_set_frozen_at_commit_seq?`

**Candidate legal interpretation:** RDMS-03 Experiment denotes immutable design while ExperimentRun owns execution; FCA Experiment includes RUNNING/COMPLETED/FAILED and observation_ids. Map FCA operational states to design plus run records, never simply to RDMS-03 lifecycle.

**Mandatory conformance evidence:** Proof: one experiment design, two runs with distinct results and observations; complete/failed/cancelled execution must remain queryable without changing design lifecycle.

**Unsafe shortcut / blocker:** DESIGNED/AUTHORIZED/RETIRED are design lifecycle values, not equivalent to RUNNING/COMPLETED/FAILED.

**Acceptance vector:** `AT7-10` — scenario defined, **NOT EXECUTED**.

### P7-11 — `Goal`

**Owner:** L2; **status:** `LOW_RISK_MAPPING_CANDIDATE`; **source comparison:** `PARENT_REFINEMENT`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:735`; declaration SHA-256 `ec72ecec3d41cec8f52dc3eb4629de6487e6f6388403e732c7784ef4984254fe`. Fields/values: `id; parent_id?; intent; acceptance[]; priority; status:; backlog; ready; active; suspended; blocked; waiting; deferred; verified; closed; obsolete; created_from`
- `RDMS-02` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:576`; declaration SHA-256 `dc58da634c53e0b6403d8f24d9ea7a7ab12cc083d39460d12278374f15da79be`. Fields/values: `goal_id; parent_goal_id?; goal_kind:; MISSION; MILESTONE; TASK; SUBGOAL; intent; acceptance_criteria[]; priority:; LOW; NORMAL; HIGH; CRITICAL; status:; BACKLOG; READY; ACTIVE; SUSPENDED; BLOCKED; WAITING; DEFERRED; VERIFIED; CLOSED; OBSOLETE; created_from; blocker_refs[]?; waiting_on_refs[]?; terminal_reason?`

**Candidate legal interpretation:** RDMS-02 refines FCA goal identity with explicit goal kind, typed priority, criteria and blockers while retaining status set. Preserve parent/child, acceptance, provenance and terminal reason.

**Mandatory conformance evidence:** Proof: complete goal status round-trip across all FCA states and preserve parent/priority/acceptance.

**Unsafe shortcut / blocker:** Historical priority data without explicit class cannot be guessed; may require review.

**Acceptance vector:** `AT7-11` — scenario defined, **NOT EXECUTED**.

### P7-12 — `GoalStack`

**Owner:** L2; **status:** `LOW_RISK_MAPPING_CANDIDATE`; **source comparison:** `PARENT_REFINEMENT`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:760`; declaration SHA-256 `74f69cb7d23596de67d5e664d093e157c00ddd6053b1de6ed1a2e27b260b0515`. Fields/values: `mission; milestone?; task?; subgoal?; current_operation?`
- `RDMS-02` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:736`; declaration SHA-256 `8a4468eaffdd8825d7de1d1204221bd442235f552f27cd9b5a3191b35e02f1ac`. Fields/values: `project_id; mission_goal_id?; milestone_goal_id?; task_goal_id?; subgoal_goal_id?; current_operation_ref?; entity_version`

**Candidate legal interpretation:** FCA symbolic mission/milestone/task/subgoal/current_operation fields become versioned RDMS-02 IDs/refs. Preserve optional slots, hierarchy intent and current operation reference.

**Mandatory conformance evidence:** Proof: serialize empty and fully populated stack, verify project identity and entity version and reconstruct ordered focus.

**Unsafe shortcut / blocker:** Do not fabricate goal records for absent optional levels.

**Acceptance vector:** `AT7-12` — scenario defined, **NOT EXECUTED**.

### P7-13 — `Hypothesis`

**Owner:** L2; **status:** `SEMANTIC_GATE_OPEN`; **source comparison:** `CORRECTION_SUPERSESSION`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:472`; declaration SHA-256 `f9845132f38afeffd07a47b4b2b741e0393cd5712a2c60f42f53cbe8a3e6a973`. Fields/values: `id; explanation; explains[]; assumptions[]; predictions[]; evidence_for[]; evidence_against[]; competing_hypotheses[]; experiments[]; support:; untested; plausible; supported; strong; causally_verified; refuted; status:; active; rejected; confirmed; superseded`
- `RDMS-02` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:382`; declaration SHA-256 `ac8a90bdd1a64f1fa0462e9e4c3f948c44bbd66ffa0b12e841564bd5d19ebc1f`. Fields/values: `hypothesis_id; explanation; scope: ScopeSpec; explains_refs[]; assumption_refs[]; prediction_refs[]; competing_hypothesis_ids[]; experiment_refs[]; support:; UNTESTED; PLAUSIBLE; SUPPORTED; STRONG; CAUSALLY_VERIFIED; REFUTED; status:; ACTIVE; REJECTED; CONFIRMED; SUPERSEDED; dependency_set_ref?; superseded_by?`
- `RDMS-02` — C01, second review corrections and final freeze decision, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:2117`; declaration SHA-256 `eaa16ef2ffa6b5ea13931f4f8c3a7e3d1b2ab615458141eb2baf1b2011fa1bac`. Fields/values: `...; current_support_assessment_ref?; lifecycle:; ACTIVE; REJECTED; CONFIRMED; SUPERSEDED; closure_ref?`

**Candidate legal interpretation:** RDMS-02 C01 separates support assessment from lifecycle and closes confirmed hypotheses with causal verification reference. Preserve evidence-for/against and prediction refs independently; ranking/support alone cannot imply causal verification.

**Mandatory conformance evidence:** Proof: historical hypothesis before/after C01, corroborated support without verification, and independently verified causal closure; preserve competing hypotheses and supersession.

**Unsafe shortcut / blocker:** CAUSALLY_VERIFIED cannot arise from strong support alone; no duplicate OVC/causal claim owner.

**Acceptance vector:** `AT7-13` — scenario defined, **NOT EXECUTED**.

### P7-14 — `InformationNeed`

**Owner:** L2; **status:** `LOW_RISK_MAPPING_CANDIDATE`; **source comparison:** `PARENT_REFINEMENT`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:440`; declaration SHA-256 `9675de0f47bfe288243ae9a61abb294fa2b1275a6dc6d7bcfce43a68a9b7745f`. Fields/values: `id; question; importance; blocks[]; source_candidates[]; resolvable:; internally; reality; human; external_dependency; status:; open; investigating; resolved; obsolete; resolution?`
- `RDMS-02` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:285`; declaration SHA-256 `4790799f601adf0ef493c744ce837a32bcf6c38fd93bf646a13531704019e16d`. Fields/values: `information_need_id; question; scope: ScopeSpec; importance:; LOW; MEDIUM; HIGH; CRITICAL; blocks[]:; EntityRef; source_candidates[]; resolution_routes[]:; INTERNAL_REASONING; REALITY; HUMAN; EXTERNAL_DEPENDENCY; status:; OPEN; INVESTIGATING; RESOLVED; OBSOLETE; resolution_ref?; opened_from?`

**Candidate legal interpretation:** RDMS-02 adds scope, typed importance, resolution routes, resolution_ref and opened_from; FCA kinds map to RDMS-02 route set and open/investigating/resolved/obsolete lifecycle.

**Mandatory conformance evidence:** Proof: all route/importance/status cases, multiple blockers and cited resolution, preserving who/what supplied answer.

**Unsafe shortcut / blocker:** If source resolution text lacks reference, migration must record provenance, not invent one.

**Acceptance vector:** `AT7-14` — scenario defined, **NOT EXECUTED**.

### P7-15 — `Invariant`

**Owner:** L2; **status:** `CONDITIONAL_PRESERVATION`; **source comparison:** `PARENT_REFINEMENT`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:887`; declaration SHA-256 `78f1a63fb971c4123d0e776b4f1a53e3b5f89c01a2e07d0854f26cd78685c8e1`. Fields/values: `id; statement; scope; kind:; state; architectural; behavioral; business; security; semantic; severity:; hard; critical; advisory; enforcement:; commit_gate; pre_action_gate; post_action_verify; runtime_monitor; semantic_review; predicate?; verification_spec?; source_authority; version; status:; active; superseded; retired`
- `RDMS-02` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:947`; declaration SHA-256 `8fa5e15e332d5b4a077eaa60043f6415b739a35987df0c58fb6e82cb80da38bb`. Fields/values: `invariant_id; statement; scope: ScopeSpec; kind:; STATE; ARCHITECTURAL; BEHAVIORAL; BUSINESS; SECURITY; SEMANTIC; severity:; HARD; CRITICAL; ADVISORY; enforcement_modes[]:; COMMIT_GATE; PRE_ACTION_GATE; POST_ACTION_VERIFY; RUNTIME_MONITOR; SEMANTIC_REVIEW; predicate_ref?; verification_spec_ref?; source_authority_ref; status:; ACTIVE; SUPERSEDED; RETIRED; superseded_by?`

**Candidate legal interpretation:** RDMS-02 replaces FCA singular enforcement with enforcement_modes[] and reference-based predicates/verification specs. Hard and critical severity may not be weakened to advisory or skipped.

**Mandatory conformance evidence:** Proof: hard invariant with multiple modes, scope, source authority, version and supersession survives; enforcement gates reject weaker projections.

**Unsafe shortcut / blocker:** Multiple enforcement modes cannot be collapsed to one preferred mode without permission.

**Acceptance vector:** `AT7-15` — scenario defined, **NOT EXECUTED**.

### P7-16 — `MemoryProposal`

**Owner:** L5; **status:** `CONDITIONAL_PRESERVATION`; **source comparison:** `PARENT_REFINEMENT`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2237`; declaration SHA-256 `b32126ccb0b056c9df78c8827d3caa67c7a297a6d72ab9e7e6ac6145354fe9c9`. Fields/values: `claim; proposed_scope; source_episodes[]; causal_basis?; applicability_conditions[]; counter_conditions[]; counterexamples[]; evidence_refs[]; confidence_assessment; maturity_target`
- `RDMS-07` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt:486`; declaration SHA-256 `ec572566ec818bf3f937bf674f1767f4d2c122fc1774d61dc570471f22c6edf2`. Fields/values: `proposal_id; claim; proposed_scope; source_episode_refs[]; causal_basis_ref?; applicability_conditions[]; counter_conditions[]; counterexamples[]; evidence_refs[]; confidence_assessment_ref; proposed_maturity; dependency_set_ref; provenance_ref; proposed_memory_category`

**Candidate legal interpretation:** RDMS-07 preserves FCA claim, source episodes, causal basis, applicability and counterexamples while adding versioned dependency/provenance/category references; promotion still governed by Learning Gate.

**Mandatory conformance evidence:** Proof: nested contraindications, evidence and confidence assessment resolve faithfully and no mere proposal becomes learned memory.

**Unsafe shortcut / blocker:** Evidence and confidence refs must be valid; provenance absence cannot imply consent or promotion.

**Acceptance vector:** `AT7-16` — scenario defined, **NOT EXECUTED**.

### P7-17 — `Observation`

**Owner:** L3; **status:** `SEMANTIC_GATE_OPEN`; **source comparison:** `RAW_NORMALIZATION_MAPPING`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:581`; declaration SHA-256 `c695ae560bee8ff68b4d379fd7a13b2c7810f93601b57cc6db836c99540e0ba1`. Fields/values: `id; source; source_authority?; world_ref; repo_ref?; environment_ref?; observed_at; content; raw_ref?; provenance; integrity:; verified; unverified; degraded`
- `RDMS-03` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt:82`; declaration SHA-256 `bc3b0b141c26d54aa9af803a820ac568b37414057eae05b87226caaf46729720`. Fields/values: `observation_id; project_id; observation_kind; source_ref; subject_ref?; observed_at; ingested_commit_seq; repo_ref?; world_ref?; environment_ref?; normalized_content; raw_artifact_ref?; provenance; capture_integrity; origin_ref?`

**Candidate legal interpretation:** RDMS-03 normalizes content and separates raw_artifact_ref/capture_integrity from source_ref and provenance. Preserve raw statement exactly and distinguish observed_at from ingestion order and time provenance.

**Mandatory conformance evidence:** Proof: late log with mismatched event/ingest times and degraded integrity; raw bytes still auditable and not silently promoted to verified reality.

**Unsafe shortcut / blocker:** Capture integrity is not equivalent to truth of observed claim or source authority.

**Acceptance vector:** `AT7-17` — scenario defined, **NOT EXECUTED**.

### P7-18 — `OperationalCausalClaim`

**Owner:** L2; **status:** `SEMANTIC_GATE_OPEN`; **source comparison:** `PARENT_REFINEMENT`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:514`; declaration SHA-256 `d9da8bfbcb1bcef01302c6dda08e50c98cd13ac68ccf7d0ca093e9e0240f895c`. Fields/values: `id; source_hypothesis_id; cause; effect; mechanism; scope {; repo_or_system_version; environment; inputs_or_preconditions[]; runtime_conditions[]; }; verification {; reproduced_failure; persisted_pre_intervention_prediction; targeted_intervention; predicted_effect_observed; regression_capture; alternatives_weakened[]; counterfactual_or_ablation?; }; evidence_refs[]; dependency_stamps[]; validity_conditions[]; contradictory_observations[]; status:; operationally_verified; stale; contradicted; superseded; promoted_at`
- `RDMS-02` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:461`; declaration SHA-256 `d7959844f655a6e8330f3eac470d08616de28ad0cbcb8fe03aa15af70272075c`. Fields/values: `causal_claim_id; source_hypothesis_id; cause; effect; mechanism; scope: CausalScope; verification_ref; dependency_set_ref; validity_conditions[]; contradictory_observation_refs[]; status:; OPERATIONALLY_VERIFIED; STALE; CONTRADICTED; SUPERSEDED; promoted_commit_seq; superseded_by?`

**Candidate legal interpretation:** RDMS-02 C01 separates causal lifecycle from derived freshness, and replaces FCA embedded causal-verification checklist with verification_ref. Preserve every required reproduction/prediction/intervention/regression/alternative-exclusion criterion.

**Mandatory conformance evidence:** Proof: load causal claim with full FCA verification matrix; stale then valid dependency change must not rewrite canonical causal history.

**Unsafe shortcut / blocker:** If verification_ref cannot reconstruct checklist, causal claim cannot be promoted to OPERATIONALLY_VERIFIED.

**Acceptance vector:** `AT7-18` — scenario defined, **NOT EXECUTED**.

### P7-19 — `QueryDependencyStamp`

**Owner:** L4; **status:** `LOW_RISK_MAPPING_CANDIDATE`; **source comparison:** `ENUM_AND_REFERENCE_MAPPING`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2544`; declaration SHA-256 `8d371b8c1ce9c5bd53f5613a2142af5f2de46c7da621a0cce24b8362ea4dc0b1`. Fields/values: `query; query_kind:; symbol_call; import; config_reference; textual_protocol; runtime_registry; global_search; custom; proof_scope; dependency_frontier[]; index_kind?; index_generation?; frontier_hash?; invalidation_rule; repo_ref`
- `RDMS-06` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt:897`; declaration SHA-256 `72e917291a0d7c2e7c4c0b01ea1638f8175257b1f84f0f1e09ace0c148ce653c`. Fields/values: `query_id; query; query_kind:; SYMBOL_CALL; IMPORT; CONFIG_REFERENCE; TEXTUAL_PROTOCOL; RUNTIME_REGISTRY; GLOBAL_SEARCH; CUSTOM; proof_scope; dependency_frontier[]; index_kind?; index_generation?; frontier_hash?; invalidation_rule_ref; repo_ref`

**Candidate legal interpretation:** RDMS-06 aliases FCA query kind, query identifier and invalidation rule to typed references while preserving proof_scope, frontier, index generation, frontier hash and repository revision.

**Mandatory conformance evidence:** Proof: each query kind and generation/hash invalidation round-trip; missing proof scope fails conservative freshness check.

**Unsafe shortcut / blocker:** Absence proof must not become universal merely because a narrow index returned no match.

**Acceptance vector:** `AT7-19` — scenario defined, **NOT EXECUTED**.

### P7-20 — `SandboxActivityRecord`

**Owner:** L3; **status:** `CONDITIONAL_PRESERVATION`; **source comparison:** `PARENT_REFINEMENT`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1857`; declaration SHA-256 `31d790dff6dc50e974fecc1cd62412b7499f69e3659231f1491e15e6c42f9aea`. Fields/values: `activity_id; slice_id; base_snapshot; containment_profile; operation_count; output_refs[]; observation_refs[]; result`
- `RDMS-04` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt:1124`; declaration SHA-256 `50adb3faa10627ee4e1e93547b4d66b86e4201036d5238c7f432b3c49f6c7d94`. Fields/values: `activity_id; project_id; slice_id; sandbox_ref; containment_proof_ref; base_snapshot_ref; operation_count; activity_summary; output_artifact_refs[]; observation_refs[]; final_sandbox_snapshot_ref?; completed_at`

**Candidate legal interpretation:** RDMS-04 enriches FCA activity summary with proof, sandbox and artifact refs; FCA result must be retained as a retrievable bounded outcome rather than implied from completed_at.

**Mandatory conformance evidence:** Proof: reconstruct number of operations, outputs, observations, containment proof, final snapshot and result including failure/partial.

**Unsafe shortcut / blocker:** If containment proof is missing, sandbox fast-path forbidden regardless of recorded completion.

**Acceptance vector:** `AT7-20` — scenario defined, **NOT EXECUTED**.

### P7-21 — `Slice`

**Owner:** L2; **status:** `CONDITIONAL_PRESERVATION`; **source comparison:** `PARENT_REFINEMENT`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1246`; declaration SHA-256 `169635ad70527bd57f27dc5afa1f53f6156d4c7745e897bb9078114bff453f29`. Fields/values: `id; goal_id; parent_slice?; intent; dependencies[]; allowed_scope[]; forbidden_scope[]; preconditions[]; invariants[]; contracts[]; expected_effects[]; expected_change_surface {; modules[]; contracts[]; state_owners[]; public_apis[]; persistent_data[]; }; risk_profile; proof_obligations[]; verification[]; rollback; base_state_version; base_repo_ref; status; actual_effects[]; actual_change_surface?`
- `RDMS-02` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:1217`; declaration SHA-256 `0b123626f4413cffe176ec789c5da7f4e207758aebaadb1cbc7bf2acef2043ae`. Fields/values: `slice_id; goal_id; parent_slice_id?; intent; dependency_refs[]; allowed_scope[]; forbidden_scope[]; preconditions[]; invariant_refs[]; contract_refs[]; expected_effects[]; expected_change_surface; risk_refs[]; proof_obligations[]; verification_specs[]; rollback_spec?; base_state_version; base_repo_ref; status:; PLANNED; READY; EXECUTING; IMPLEMENTED; VERIFYING; VERIFIED; INTEGRATED; CLOSED; BLOCKED; SUSPENDED; FAILED; CANCELLED; OBSOLETE; actual_effects[]; actual_change_surface?`

**Candidate legal interpretation:** RDMS-02 uses typed lifecycle and risk_refs while FCA has risk_profile, rollback and proof obligations. Preserve expected_change_surface including modules/contracts/state owners/APIs/persistent data.

**Mandatory conformance evidence:** Proof: reconcile actual versus expected change surface, proof obligations, rollback conditions, scope changes and all lifecycle statuses.

**Unsafe shortcut / blocker:** Do not silently equate IMPLEMENTED with VERIFIED/INTEGRATED/CLOSED.

**Acceptance vector:** `AT7-21` — scenario defined, **NOT EXECUTED**.

### P7-22 — `TemporalValidity`

**Owner:** L4; **status:** `LOW_RISK_MAPPING_CANDIDATE`; **source comparison:** `ENUM_CASE_NORMALIZATION`.

**Original exact declarations:**
- `FCA v1.0.1` — FCA v1.0.1 baseline, `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2088`; declaration SHA-256 `e40c6165505ab0ef64e4cc5f6265b11a1cf0842081cab1ce110d832da28238e1`. Fields/values: `observed_at?; verified_at?; repo_ref?; state_version?; valid_until_condition?; freshness:; current; stale; unknown`
- `RDMS-05` — Original draft, `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt:803`; declaration SHA-256 `fb5ebce36de924efc914824fa89d63ec5dcaee5d907524a26cf53c7d0154e270`. Fields/values: `observed_at?; verified_at?; repo_ref?; state_version?; valid_until_condition?; freshness:; CURRENT; STALE; UNKNOWN`

**Candidate legal interpretation:** RDMS-05 structurally mirrors FCA temporal validity and changes freshness enum capitalization; keep observed_at/verified_at/repo_ref/state_version/valid_until_condition.

**Mandatory conformance evidence:** Proof: CURRENT/STALE/UNKNOWN round-trip and nullability with version/predicate references.

**Unsafe shortcut / blocker:** CURRENT must be recomputed when conditions expire; enum text change is not new proof of currentness.

**Acceptance vector:** `AT7-22` — scenario defined, **NOT EXECUTED**.

## Cross-system non-regression rules

1. Exactly one canonical owner per persistent entity; derived transport projections do not own lifecycles.
2. `*_ref` conversion is lawful only if reference is durable, integrity-checked, version/scoped, resolvable and preserves all parent fields.
3. Do not equate Action design, dispatch, report and verified world effect; do not equate observation with evidence.
4. Do not equate semantic support, confidence, status and causal verification.
5. Migration must preserve historical observations, accepted evidence, decision rationale, plan/change-surface constraints and retry semantics.
6. Unknown crosswalk or absent source proof -> `MIGRATION_REVIEW_REQUIRED`; never invent missing facts.
7. An approved consolidation may require a controlled alias or typed projection, never a silent change to a frozen source.

## Still open before consolidated layer freeze

- Phase-6 critical mappings for `Commitment`, `TriggerCondition`, `ResumptionCapsule`.
- Phase-6 two transport name collisions requiring formal approval.
- Eight Phase-7 semantic gates; nine conditional-preservation crosswalks; five lower-risk round-trip proposals.
- End-to-end method/event interface, schema-version, state-transition and atomicity audit beyond the 27 lexical duplicate names.
- Implementation conformance and failure injection tests are separate from design certification.
