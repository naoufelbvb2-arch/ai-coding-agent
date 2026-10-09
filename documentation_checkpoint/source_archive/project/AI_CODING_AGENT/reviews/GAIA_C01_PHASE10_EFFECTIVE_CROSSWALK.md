# GAIA-C01 Phase 10 — Effective Contract Crosswalk and Approval Gate

**Status: structural-source checks PASS; legal projections remain proposals and runtime evidence is NOT supplied.**

## Rules of interpretation

- Frozen FCA/RDMS texts stay unchanged. A transport alias never amends a canonical type.
- Exactly one canonical owner; other layers hold bounded references/projections.
- Source-hash preservation is not proof that converters, persistence, retries, or external effects work.
- An unresolved legacy value is never guessed; it requires review and cannot receive extra authority.

## Five high-priority contracts

### CapabilityResult

**Canonical authority:** FCA v1.0.1 §23 CapabilityResult (L2)  
**Integration alias:** CapabilityTransportResult (L7 candidate)  
**Evidence gate:** `EDITORIAL_ALIAS_AFTER_CHANGE_CONTROL_ONLY`

**Required recovery:** Required integrity-checked canonical_capability_result_ref; resolve original FCA fields by the reference, never assume proposal_refs lists are complete.

**No-unsafe-promotion checks:**

- Reject / quarantine: unresolvable original reference
- Reject / quarantine: mismatched source version/hash or project
- Reject / quarantine: transport SUCCESS treated as Executive acceptance
- Reject / quarantine: lost specialist_request or rationale_summary

**Source fields → proposed preservation route**

| Source field | Preservation / boundary |
|---|---|
| `patch_proposal` | canonical_capability_result_ref -> verified immutable FCA record |
| `proposed_claims` | canonical_capability_result_ref -> verified immutable FCA record |
| `proposed_hypotheses` | canonical_capability_result_ref -> verified immutable FCA record |
| `proposed_information_needs` | canonical_capability_result_ref -> verified immutable FCA record |
| `evidence_refs` | canonical_capability_result_ref -> verified immutable FCA record |
| `tool_requests` | canonical_capability_result_ref -> verified immutable FCA record |
| `experiment_requests` | canonical_capability_result_ref -> verified immutable FCA record |
| `confidence_assessment` | canonical_capability_result_ref -> verified immutable FCA record |
| `specialist_request` | canonical_capability_result_ref -> verified immutable FCA record |
| `needs` | canonical_capability_result_ref -> verified immutable FCA record |
| `rationale_summary` | canonical_capability_result_ref -> verified immutable FCA record |

**Authoritative excerpt:** `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:1012`; SHA-256 `b60b418b16f38240fec6c0be2929b5701ef1cbb2d8c59cf0014fb6bf2fb26e4a`

### MemoryRetrievalResult

**Canonical authority:** RDMS-07 MemoryRetrievalResult (L5)  
**Integration alias:** MemoryRetrievalTransportResult (L7 candidate)  
**Evidence gate:** `EDITORIAL_ALIAS_AFTER_CHANGE_CONTROL_ONLY`

**Required recovery:** Required canonical_memory_retrieval_result_ref; retrieve omission/filtered scope, coverage and ranking metadata; transport shortlist is not exhaustive.

**No-unsafe-promotion checks:**

- Reject / quarantine: missing result identity
- Reject / quarantine: missing omitted/filtered scope for partial retrieval
- Reject / quarantine: empty shortlist interpreted as no stored knowledge
- Reject / quarantine: unapproved cross-project disclosure

**Source fields → proposed preservation route**

| Source field | Preservation / boundary |
|---|---|
| `retrieval_id` | canonical_memory_retrieval_result_ref -> verified immutable RDMS-07 record |
| `query_ref` | canonical_memory_retrieval_result_ref -> verified immutable RDMS-07 record |
| `candidate_refs` | canonical_memory_retrieval_result_ref -> verified immutable RDMS-07 record |
| `omitted_or_filtered_scope` | canonical_memory_retrieval_result_ref -> verified immutable RDMS-07 record |
| `ranking_policy_ref` | canonical_memory_retrieval_result_ref -> verified immutable RDMS-07 record |
| `retrieval_coverage` | canonical_memory_retrieval_result_ref -> verified immutable RDMS-07 record |
| `freshness_summary` | canonical_memory_retrieval_result_ref -> verified immutable RDMS-07 record |
| `created_at` | canonical_memory_retrieval_result_ref -> verified immutable RDMS-07 record |

**Authoritative excerpt:** `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt:1080`; SHA-256 `e4ae715a27b230289f343447d8b7723501f62538065a5e61fa5dc5009c17c67d`

### Commitment

**Canonical authority:** RDMS-02 post-C01 semantic Commitment (L2); L4 owns evaluation only  
**Integration alias:** TemporalCommitmentView (L4 suggested; not another persistent Commitment)  
**Evidence gate:** `BLOCKED_UNTIL_NONLOSS_PROOF`

**Required recovery:** Identity ref to RDMS-02 semantic record + separate RDMS-05 temporal metadata. Preserve original statement, why_temporary, structured scope, all linked entities, timestamp, resolution, and reactivation root.

**No-unsafe-promotion checks:**

- Reject / quarantine: statement automatically equated to required_followup
- Reject / quarantine: why_temporary replaced by reason
- Reject / quarantine: linked_entity_refs[] reduced to subject_ref
- Reject / quarantine: created_at substituted by created_commit_seq
- Reject / quarantine: missing owner on ACTIVE
- Reject / quarantine: ACTIVE without valid reactivation root
- Reject / quarantine: DUE auto promotes SATISFIED

**Source fields → proposed preservation route**

| Source field | Preservation / boundary |
|---|---|
| `commitment_id` | same identity and project/version scope |
| `statement` | semantic canonical ref; no automatic mapping to required_followup |
| `why_temporary` | semantic canonical ref; no automatic mapping to reason |
| `scope` | canonical ScopeSpec; subject_ref only subview |
| `owner_ref` | retain; ACTIVE requires authorized owner |
| `linked_entity_refs` | canonical relation set; no collapse to subject_ref |
| `created_at` | preserve separately from legal created_commit_seq |
| `reactivation_condition_ref` | active legal root after adopted C01; RDMS-05 evaluator resolves |
| `status` | one canonical lifecycle, no DUE=>SATISFIED |
| `resolution_ref` | preserve canonical resolution history |

**Authoritative excerpt:** `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt:1380`; SHA-256 `da8ac753225c695d17105d549b2d3eca57f648d2343a84a0a8daefc58e46fce9`

### TriggerCondition

**Canonical authority:** FCA §56 full-trigger conceptual contract; RDMS-05 TriggerDefinition is full current runtime record; RDMS-05 TriggerCondition is a predicate subrecord  
**Integration alias:** TriggerPredicateCondition (L4 for the local predicate only; candidate)  
**Evidence gate:** `BLOCKED_UNTIL_AGGREGATE_PROOF`

**Required recovery:** Resolve trigger_id + generation to complete TriggerDefinition, separate fire_policy and detection_policy, predicate tree, source cursors, reaction identity and lifecycle history.

**No-unsafe-promotion checks:**

- Reject / quarantine: predicate alone promoted to full trigger
- Reject / quarantine: ONE_SHOT merged with EDGE_TRIGGERED as one axis
- Reject / quarantine: missing detection/fire axis invented
- Reject / quarantine: unreplayable EDGE becomes FALSE
- Reject / quarantine: replay creates second reaction/effect

**Source fields → proposed preservation route**

| Source field | Preservation / boundary |
|---|---|
| `id` | TriggerDefinition.trigger_id |
| `generation` | TriggerDefinition.generation |
| `semantics` | fire_policy AND detection_policy, distinct axes |
| `kind` | TriggerPredicateCondition.kind and definition source refs |
| `watches` | source refs, cursor generation and condition graph |
| `predicate` | condition_ref -> predicate definition |
| `source_cursor` | TriggerSourceCursor + replay frontier |
| `reaction_key` | generation-scoped reaction identity, not mere string |
| `linked_object` | linked_object_ref |
| `on_fire` | reaction_spec_ref with legal action path |
| `status` | trigger lifecycle distinct from action delivery |
| `last_evaluated_at` | evaluation history with original clock |
| `last_fire_id` | TriggerFire identity |

**Authoritative excerpt:** `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt:191`; SHA-256 `c3092a02ce0b441049cfe58978e5eaa1bbee23f7b4fd879240b58e666822bdbd`

### ResumptionCapsule

**Canonical authority:** RDMS-05 adopted C01 compact capsule header (L4); FCA §53 contextual semantics recoverable in immutable durable payload; RDMS-09 governs recovery  
**Integration alias:** None; original name retained  
**Evidence gate:** `BLOCKED_UNTIL_DURABLE_PAYLOAD_AND_RECOVERY_PROOF`

**Required recovery:** Durable payload artifact and digest verified BEFORE atomic SUSPENDED transition; dereference all FCA fields, and maintain RDMS-05 expanded references, world/dependency history and unresolved effects.

**No-unsafe-promotion checks:**

- Reject / quarantine: durable_payload_artifact_ref missing
- Reject / quarantine: content_integrity_ref mismatch
- Reject / quarantine: relevant_entity_refs alone assumed sufficient
- Reject / quarantine: next_action_proposal_ref auto-dispatched
- Reject / quarantine: work marked SUSPENDED before durable payload acknowledged

**Source fields → proposed preservation route**

| Source field | Preservation / boundary |
|---|---|
| `task_id` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `suspended_from_state` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `base_state_version` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `repo_ref` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `goal` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `subgoal` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `current_focus` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `current_hypotheses` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `relevant_evidence` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `rejected_paths` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `temporary_changes` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `open_information_needs` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `next_concrete_action` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |
| `created_at` | verified durable payload artifact (or fully defined immutable ref and lineage), NOT guaranteed by compact header alone |

**Authoritative excerpt:** `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt:2067`; SHA-256 `1c38a08ce60f890ed64f69cfd6cb8d2928d75d5b6637be31299a5b209e420409`

## Field-level gate for the other 22 reusable names

| Contract | Owner | Risk | Exact-source proof | Legal projection proof |
|---|---|---|---|---|
| `ActionEffectSemantics` | L3 | CONDITIONAL | PASS (source & publication) | **PENDING** — Probe/compensation/timeout_spec refs resolve to exact original semantics; unknown non-idempotent effect never blindly retried |
| `ActionProposal` | L3 | SEMANTIC | PASS (source & publication) | **PENDING** — Signed/effective operation specs with explicit discriminator; version/integrity-resolvable context; downstream use and reverse-projection proof. |
| `ActionRecord` | L3 | CONDITIONAL | PASS (source & publication) | **PENDING** — Recover all attempts, reports, observations, compensation, timestamps; latest_attempt_ref alone insufficient |
| `Claim` | L2 | SEMANTIC | PASS (source & publication) | **PENDING** — Source version lineage, evidence links, grounding, support-assessment provenance and temporal validity reconstruct FCA-level meaning. |
| `ConfidenceAssessment` | L3 | CONDITIONAL | PASS (source & publication) | **PENDING** — Evidence/verification refs resolve and wall-clock timestamps not silently mapped to commit sequence |
| `ContradictionRecord` | L3 | SEMANTIC | PASS (source & publication) | **PENDING** — State history with comparability assessment, observation references, interpretation/proof separation and unresolved-state query. |
| `Decision` | L2 | CONDITIONAL | PASS (source & publication) | **PENDING** — Preserve chosen option, rejected option reasons, evidence, alternatives, constraints, scope, version |
| `DependencyStamp` | L4 | CONDITIONAL | PASS (source & publication) | **PENDING** — Enumerate all nine FCA kinds; RDMS-01 projections cannot bypass currentness checks |
| `EvidenceLink` | L3 | SEMANTIC | PASS (source & publication) | **PENDING** — Observation ID multiplicity, link IDs, acceptance history, signed source trace and exact target/relation preservation. |
| `Experiment` | L3 | SEMANTIC | PASS (source & publication) | **PENDING** — ExperimentID/RunID mapping, immutable prediction hashes, risk/authorization, run timestamps, observations and status history. |
| `Goal` | L2 | LOW_RISK | PASS (source & publication) | **PENDING** — Preserve hierarchy, status, acceptance criteria, blockers, provenance and priority as typed-or-unresolved |
| `GoalStack` | L2 | LOW_RISK | PASS (source & publication) | **PENDING** — Empty/populated stack yields same focus, project/version and ordering |
| `Hypothesis` | L2 | SEMANTIC | PASS (source & publication) | **PENDING** — Typed reference resolution for each FCA cognitive relation and explicit authorized OVC verification record. |
| `InformationNeed` | L2 | LOW_RISK | PASS (source & publication) | **PENDING** — Preserve route, blockers and resolution reference, else require review |
| `Invariant` | L2 | CONDITIONAL | PASS (source & publication) | **PENDING** — All enforcement modes, severity, scope and failure semantics survive |
| `MemoryProposal` | L5 | CONDITIONAL | PASS (source & publication) | **PENDING** — Evidence, counterexamples, applicability, consent/provenance and approval path preserved |
| `Observation` | L3 | SEMANTIC | PASS (source & publication) | **PENDING** — Raw byte hash, explicit source identity, clock trust, event order, capture integrity and interpretation provenance. |
| `OperationalCausalClaim` | L2 | SEMANTIC | PASS (source & publication) | **PENDING** — Ref dereference yields full source checklist with chronological commits, authority, specific environment and dependency frontier. |
| `QueryDependencyStamp` | L4 | LOW_RISK | PASS (source & publication) | **PENDING** — Validate exact frontier, proof scope, revision, index generation/hash and freshness |
| `SandboxActivityRecord` | L3 | CONDITIONAL | PASS (source & publication) | **PENDING** — Recover evidence of isolation, op counts, output/observation refs and result including partial failure |
| `Slice` | L2 | CONDITIONAL | PASS (source & publication) | **PENDING** — Actual-vs-expected change surface, rollback/proof obligations and all slice statuses remain separate |
| `TemporalValidity` | L4 | LOW_RISK | PASS (source & publication) | **PENDING** — CURRENT/STALE/UNKNOWN map case-insensitively but CURRENT requires validity reevaluation |

## Approval recommendation

1. **Two L7 aliases:** source collision and required canonical-reference strategy are documented; approve the *names as consolidation candidates*, not schema equivalence or automatic promotion.
2. **Commitment:** requires a single canonical semantic entity and separately referenced temporal metadata with no destructive field union.
3. **TriggerCondition:** predicate must be distinct from full trigger; reconstruction needs both fire/detection dimensions and immutable reaction history.
4. **ResumptionCapsule:** compact header and verified durable payload require atomic suspension and restore evidence.
5. **Remaining 22:** published source baseline is useful but every required crosswalk needs actual round-trip/nonloss evidence or recorded no-migration-needed rationale.

**Global disposition:** `CANONICAL_EFFECTIVE_CONTRACT_FREEZE=DENIED`; `IMPLEMENTATION_NOT_AUTHORIZED`.
