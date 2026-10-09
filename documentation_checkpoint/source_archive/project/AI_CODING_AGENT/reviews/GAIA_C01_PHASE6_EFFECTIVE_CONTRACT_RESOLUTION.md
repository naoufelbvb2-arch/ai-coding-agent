# GAIA-C01 — Phase 6: Effective Contract Resolution and Non-Lossy Migration Rules

**Status: REVIEW CANDIDATE / NOT FROZEN.**  The approved original sources and their annexes remain immutable. These rulings describe the **proposed effective per-layer vocabulary**, not retroactive amendments to frozen FCA or RDMS sources. Every proposed alias or projection must be approved in global integration review before it becomes normative.

## Findings and disposition

| ID | Contract | Current authoritative semantics | Proposed resolution | Status |
|---|---|---|---|---|
| P6-01 / GAIA-B01 | `CapabilityResult` | FCA §23 semantic output (L2) | L7 transport name `CapabilityTransportResult`, with required `canonical_capability_result_ref` | PROJECTION SPECIFIED; APPROVAL PENDING |
| P6-02 / GAIA-B03 | `MemoryRetrievalResult` | RDMS-07 retrieval record (L5) | L7 transport name `MemoryRetrievalTransportResult`, with required `canonical_memory_retrieval_result_ref` | PROJECTION SPECIFIED; APPROVAL PENDING |
| P6-03 / GAIA-B04 | `Commitment` | RDMS-02 C01 governs canonical semantic entity; RDMS-05 governs temporal runtime | Single canonical RDMS-02 `Commitment`, RDMS-05 lifecycle projection only after explicit full mapping | BLOCKED: NON-EQUIVALENT FIELDS |
| P6-04 / GAIA-B05 | `TriggerCondition` | FCA full-trigger vocabulary; RDMS-05 distinguishes full `TriggerDefinition` from condition/predicate | Scope FCA legacy name; use RDMS-05 `TriggerDefinition` for full runtime trigger; propose `TriggerPredicateCondition` as L4 effective predicate name | BLOCKED: COMPLETE CROSSWALK REQUIRED |
| P6-05 / GAIA-RCAP | `ResumptionCapsule` | FCA §53 recovery-critical contents; RDMS-05 C01 compact durable capsule | Retain C01 compact capsule plus integrity-pinned payload with explicit field preservation | CONDITIONAL: PAYLOAD SCHEMA PROOF NEEDED |

## P6-01 — `CapabilityResult`: canonical semantic result vs transport

**Sources:** `Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md` near line 1012; `RDMS-10_APPROVED_SOURCE_SET.txt` near line 384; RDMS-10 C01 `CanonicalContractRegistry` near line 3048.

The FCA semantic contract MUST NOT be replaced by the RDMS-10 transport-shaped declaration. The FCA fields are `patch_proposal?`, `proposed_claims[]`, `proposed_hypotheses[]`, `proposed_information_needs[]`, `evidence_refs[]`, `tool_requests[]`, `experiment_requests[]`, `confidence_assessment?`, `specialist_request?`, `needs[]`, and `rationale_summary?`.

**Proposed L7 transport projection (not an amendment to RDMS-10 original):**

```text
CapabilityTransportResult {
    invocation_id
    canonical_capability_result_ref     // REQUIRED for full semantic recovery
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

**Projection rule:** receiving consumers MUST resolve the durable canonical result reference to obtain *every* FCA field, including `specialist_request?`, `needs[]`, and `rationale_summary?`, which are not present in the original RDMS-10 abbreviated shape. `result_status` is transport execution status, not Executive acceptance. If the reference is missing/unresolvable/unverified, the projection is **not lossless** and MUST NOT be treated as a canonical `CapabilityResult`. All proposal/evidence references retain their original authorities and version guards.

**Acceptance vectors:** V01 (all FCA fields survive), V02 (missing canonical ref fails), V03 (successful transport result does not commit cognition).

## P6-02 — `MemoryRetrievalResult`: canonical retrieval vs presentation

**Sources:** `RDMS-07_APPROVED_SOURCE_SET.txt` near line 1080; `RDMS-10_APPROVED_SOURCE_SET.txt` near line 1148.

RDMS-07 `MemoryRetrievalResult` owns `retrieval_id`, `query_ref`, `candidate_refs[]`, `omitted_or_filtered_scope[]`, `ranking_policy_ref`, `retrieval_coverage`, `freshness_summary`, `created_at`. A consumer must not infer exhaustive search or present-day truth from a subset of memory snippets.

**Proposed L7 transport projection:**

```text
MemoryRetrievalTransportResult {
    canonical_memory_retrieval_result_ref  // REQUIRED
    memory_refs[]
    relevance_assessments[]
    provenance_refs[]
    applicability_assessments[]
    trust_metadata_refs[]
}
```

**Projection rule:** `memory_refs[]` is a bounded consumer view derived from the canonical result; it is *not* asserted equivalent to all `candidate_refs[]`. Coverage, omissions, ranking policy and freshness must remain retrievable by canonical reference. Missing/mismatched canonical identity, project scope, or version must fail closed. The projected view does not independently authorize memory promotion or cross-project transfer.

**Acceptance vectors:** V04 (coverage preserved by reference), V05 (projection of partial retrieval cannot assert total absence), V06 (missing result proof rejected).

## P6-03 — `Commitment`: one entity, two distinct specification roles

**Sources:** RDMS-02 original line 1380 and adopted C01 `C01-32` at 2831–2867; RDMS-05 original line 526 and validity at 551–573.

RDMS-02 C01 explicitly replaces the three parallel reactivation fields (`due_at?`, `removal_trigger_id?`, `revisit_trigger_id?`) with a single `reactivation_condition_ref`, and stipulates an **ACTIVE Commitment must have a valid root**. RDMS-05 states it adopts the RDMS-02 model but shows a different runtime-oriented shape and additionally requires owner, purpose and reactivation condition.

**Canonical owner decision proposed:** L2 (`RDMS-02` semantic entity) owns definition/identity and semantic fields; L4 (`RDMS-05`) owns condition semantics and lifecycle evaluation. The RDMS-05 shape cannot become a second independently authoritative `Commitment` entity. L4 may use a transport/lifecycle projection after full mapping review.

| RDMS-02 post-C01 | RDMS-05 | Proposed equivalence and risk |
|---|---|---|
| `commitment_id` | `commitment_id` | identity match, provided project and version scope agree |
| `statement` | `required_followup` | **NOT automatically equivalent:** statement may contain condition/rationale, follow-up may be an instruction |
| `why_temporary` | `reason` | **NOT automatically equivalent:** needs semantics check |
| `scope: ScopeSpec` | `subject_ref` | **NOT equivalent**: structured scope vs one referenced subject |
| `owner_ref?` | `owner_ref` | owner mandatory in RDMS-05 validity; legacy missing owner needs review, not fabrication |
| `linked_entity_refs[]` | `subject_ref` | many-to-one information loss unless independent links retained |
| `created_at` | `created_commit_seq` | wall-time vs legal sequence; distinct facts, preserve both if available |
| `reactivation_condition_ref` | `reactivation_condition_ref` | semantic root reference must point to valid RDMS-05 composite/condition |
| `status` | `lifecycle` | five known values align; canonical state transition ownership must be unique |
| `resolution_ref?` | no direct counterpart | MUST remain recoverable; do not silently discard |
| no direct counterpart | `updated_commit_seq` | lifecycle metadata, not substitute for `resolution_ref` |

**Minimal lawful position:** No canonical union/overwrite is authorized in Phase 6. Consumers may read a RDMS-05 lifecycle projection only if a documented `commitment_id` points to the RDMS-02 semantic record and none of its required properties are lost; no projection may create a second legal owner. Migration of missing `owner_ref`, semantic statement and scopes requires a recorded migration decision and applicable Executive/CommitGate authorization, not inferred field renaming. On ambiguous migration: `MIGRATION_REVIEW_REQUIRED`, no false `SATISFIED`.

**Acceptance vectors:** V07 (all semantic fields preserved), V08 (multi-linked entities not collapsed), V09 (old parallel trigger migration explicit), V10 (missing owner fails closed).

## P6-04 — `TriggerCondition`: full-trigger vs predicate distinction

**Sources:** FCA §56 at about line 2126; RDMS-05 `TriggerDefinition` at 161–186, local `TriggerCondition` at 191–209, state semantics at 307–325, composition at 328–350, replay and C01 versioned snapshots.

FCA uses `TriggerCondition` to represent full trigger generation, firing/detection semantics, source cursors, reaction identity, linked object and lifecycle. RDMS-05 explicitly separates **full trigger** (`TriggerDefinition`) from **condition predicate** (`TriggerCondition`). The two names must not be bound to the same type across module boundaries.

**Proposed effective L4 vocabulary:** `TriggerDefinition` = full current runtime trigger; `TriggerPredicateCondition` = subcondition record (formerly RDMS-05-local `TriggerCondition`); FCA `TriggerCondition` remains historical constitutional vocabulary for the aggregate full-trigger concept, not a competing persistent structure. Renaming the local predicate is a proposed consolidation-only interface alias, not a rewrite of RDMS-05 frozen text.

| FCA full-trigger field | RDMS-05 legal destination | Caveat |
|---|---|---|
| `id`, `generation` | `TriggerDefinition.trigger_id`, `.generation` | stable composite identity |
| `semantics` | `fire_policy` + `detection_policy` | original enum is two orthogonal axes; do not invent a missing axis during migration |
| `kind`, `predicate?`, `watches[]` | `condition_ref` + `TriggerPredicateCondition` + `source_refs[]` | preserve complete predicate and source coverage |
| `reaction_key`, `on_fire` | `reaction_spec_ref` and stable reaction identity records | **not a simple string rename**; dedup/action intent must survive |
| `source_cursor?` | `TriggerSourceCursor` | source generation/coverage required for replay |
| `status` | trigger lifecycle state (`ARMED/FIRED/SATISFIED/CANCELLED`) | keep independent of reaction delivery state |
| `last_evaluated_at`, `last_fire_id?` | evaluation history, `TriggerFire` refs | explicit relation required, not silent erasure |
| `linked_object` | `linked_object_ref` | preserve linked entity identity |

**Acceptance:** Demonstrate full aggregate reconstitution from RDMS-05 records at frozen event positions, especially `reaction_key` and generation-specific deduplication. A migration with only a predicate but no full `TriggerDefinition` is invalid. Unreplayable EDGE triggers remain `UNKNOWN`, not `FALSE`.

**Acceptance vectors:** V11 (full trigger reconstructible), V12 (predicate cannot self-authorize fire), V13 (missing detection axis requires review), V14 (replay cannot duplicate fire).

## P6-05 — `ResumptionCapsule`: compact header plus pinned durable payload

**Sources:** FCA §53 at line 2037; RDMS-05 expanded schema at line 654; adopted C01 `C01-34–36` at 2066–2117.

RDMS-05 C01 replaces expanded inline capsule content by durable referenced payload, integrity reference and canonical snapshot. It mandates publish-and-verify before atomic suspension, and corrupted/missing capsules enter Recovery rather than executing stale next actions.

**Proposed logical composite:**

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

ResumptionCapsulePayload {
    // REQUIRED RECOVERABLE SEMANTIC CONTENT FROM FCA §53
    task_id
    base_state_version
    repo_ref
    goal
    subgoal
    current_focus
    current_hypotheses[]
    relevant_evidence[]
    rejected_paths[]
    temporary_changes[]
    open_information_needs[]
    next_concrete_action?
    created_at
    // RDMS-05 original expanded fields must also survive by reference or content
    project_id?
    world_ref?
    environment_ref?
    relevant_claim_refs[]
    decision_refs[]
    active_slice_refs[]
    commitment_refs[]
}
```

**Status of this payload shape: PROPOSED.** It describes required *recoverable meaning*, not mandatory duplicate persistent fields or a new cognitive owner. `relevant_entity_refs[]` are not sufficient proof of preserving historical context by themselves. `next_action_proposal_ref?` does not cover arbitrary `next_concrete_action?` (which might be a cognitive step). Missing payload or integrity mismatch MUST block automatic resume. Suspension requires payload durability + verification followed by atomic reference+state+reactivation commit.

**Acceptance vectors:** V15 (all FCA semantic content resolvable), V16 (reference-only incomplete proof rejected), V17 (corrupt payload quarantined), V18 (no auto-replay of next action).

## 27-name reconciliation progress

Phase 5 identified 27 reused lexical names; this phase supplies focused crosswalks for five priority names. **The remaining 22 are not silently declared resolved.** Source annexes preserve their original text, but future effective schema reconciliation must close each parent refinement, field alias and correction supersession. See `GAIA_C01_PHASE5_27_TYPE_DECISIONS.csv` and `GAIA_C01_PHASE6_REMAINING_TYPES.csv`.

## Change-control and review gates

1. Approve proposed transport-only effective aliases at L7, with required canonical references and no semantic loss.
2. Resolve commitment field mismatches and select the single authoritative entity representation consistent with RDMS-02 C01 and RDMS-05.
3. Prove full-trigger aggregate reconstruction including reaction identity and separate fire/detection axes.
4. Prove capsule durable-payload content and integrity mapping end to end.
5. Close the remaining 22 name mappings individually, using source citations and verified precedence; never assume lexical similarity equals semantic equivalence.
6. Conformance tests of source text integrity, declarations, projections and forbidden authority paths remain mandatory. No runtime code or renewed specification freeze is authorized by this report.
