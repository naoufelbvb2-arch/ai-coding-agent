# Targeted normative blocker classification

Reviewed baseline: `d50b7f88105b5397aa7d76e0bb8a1c2099a7c85e`. Original questions: **40**. Every entry has exactly one classification.

| Class | Meaning | Count |
|---|---|---|
| A | NORMATIVE_CONFLICT | 0 |
| B | LOSSLESS_MAPPING_REQUIRED | 25 |
| C | IMPLEMENTATION_DETAIL_DEFERRED | 6 |
| D | ALREADY_RESOLVED | 8 |
| E | EXPLICIT_ARCHITECTURAL_DECISION_REQUIRED | 1 |

D closes the source-determined question; C defers only representation to Implementation Design. B requires a preservation proof and stays open. E requires an approved architectural decision. No direct mutually impossible pair was proven for class A; zero A does not mean the B/E legal-information gaps are harmless.

Source custody, current-law completeness and implementation conformance are distinct. All original candidates and exact clauses/hashes remain in [BLOCKER_CLASSIFICATION.json](BLOCKER_CLASSIFICATION.json).

### L3-NR-PARENT-ActionEffectSemantics

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

The retry and verification enums agree. The sources do not explicitly bind the inline outcome_probe, compensation and timeout_policy to the later spec/reference fields. Those contents govern safe retry; equal names or comparable labels are not a preservation proof.

**Binding obligations:** Retain effect identity, idempotency identity, all three retry policies, all three verification modes, timeout semantics, probe adequacy and authorized compensation. A referenced spec must preserve the original operational content.

**Remaining detail / acceptance limit:** Proof for outcome_probe versus outcome_probe_spec, compensation versus compensation_spec, and timeout_policy versus timeout_policy_ref, including reference integrity and historical reconstruction. No alias is approved here.

Exact authoritative evidence: [FCA-43](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1751>); [RDMS-04-M06-U012](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L340>); [RDMS-04-M07-U041](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L2260>); [RDMS-04-M07-U042](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L2280>); [RDMS-04-M07-U043](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L2298>).

### L3-NR-PARENT-ActionProposal

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

RDMS-04 expressly makes the requested class advisory and provides a separate authorization. That resolves the authority division, but does not prove preservation of every FCA proposal field. FCA base_world_ref/risk_profile are mandatory where the RDMS specimen makes their references optional; authority_required and proposal status have no explicit complete crosswalk.

**Binding obligations:** Requested class never authorizes execution. Preserve identity, requester, Goal/Slice lineage, intent, detailed operation, target/effect/precondition information, risk, reversibility, compensation, diagnostic/production meaning, relevant world basis, required authority and proposal history. ActionGate and authorization fingerprint govern actual execution.

**Remaining detail / acceptance limit:** Prove the detailed operation-kind information, mandatory risk/world information, authority_required and proposal status survive in the owner records. An ActionAuthorization is not itself a proved storage location for proposal authority requirements.

Exact authoritative evidence: [FCA-42](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1660>); [RDMS-04-M06-U004](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L96>); [RDMS-04-M06-U005](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L155>); [RDMS-04-M06-U006](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L181>); [RDMS-04-M07-U002](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1643>).

### L3-NR-PARENT-ActionRecord

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

RDMS-04 separates action, attempt, report, observation and reconciled effect explicitly. This proves the decomposition, but not a complete per-action reconstruction of every original timestamp, observation membership and before-world requirement.

**Binding obligations:** Retain the original action identity, proposal, lifecycle, before/after world context, execution reports, observations, compensation association and start/finish information. Keep ActionId, AttemptId and DispatchId distinct; latest_attempt_ref cannot erase older attempts or establish the effect.

**Remaining detail / acceptance limit:** Proof for mandatory world_ref_before, execution_result, observation_ids, compensation_action_id, started_at and finished_at across ActionRecord/ActionAttempt/Observation/ProcessRun/ReconciliationRecord. Do not choose first/last-attempt timestamp aggregation.

Exact authoritative evidence: [FCA-46](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1880>); [RDMS-04-M06-U008](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L207>); [RDMS-04-M06-U010](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L266>); [RDMS-04-M06-U064](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1281>); [RDMS-04-M06-U071](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1365>); [RDMS-04-M07-U002](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1643>).

### L2-NR-SHAPE-CanonicalStateView

**C — IMPLEMENTATION_DETAIL_DEFERRED; DEFERRED_TO_IMPLEMENTATION_DESIGN.**

The sole declaration is explicitly abbreviated with an ellipsis and is a read view, not a new canonical entity. RDMS-02 defines the entity owners and later explicitly replaces GoalStack. There is no competing current legal state schema to decide between.

**Binding obligations:** Read the authoritative canonical entities; use GoalPath and the current canonical focus; preserve epistemic types, derived OVC usability and scope. A view cannot create state, permission, a lifecycle or an independent freshness engine.

**Remaining detail / acceptance limit:** Read-view class, table joins, nesting, pagination and serialized member names. These choices cannot omit information required by a particular consuming contract; that conformance obligation remains binding.

Exact authoritative evidence: [FCA-6](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L278>); [RDMS-02-M02-U000](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L23>); [RDMS-02-M03-U009](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2209>); [RDMS-02-M03-U025](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2631>); [RDMS-10-M24-U010](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3090>); [RDMS-02-M02-U072](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1733>).

### L2-NR-PARENT-Claim

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

C01 explicitly externalizes support and independent relations. That resolves their authority, but the parent evidence/provenance and temporal information require a documented reconstruction through the exact accepted links and metadata; the record specimen alone does not prove it.

**Binding obligations:** Preserve statement identity, kind, scope, evidence for/against, provenance, lifecycle, temporal validity and entity version. SupportAssessment and EvidenceLink own their respective conclusions/relations; no second authoritative embedded evidence list.

**Remaining detail / acceptance limit:** Prove evidence_for/evidence_against, provenance, version and parent temporal_validity preservation through the associated records and exact reference policy, including the optional temporal_validity specimen.

Exact authoritative evidence: [FCA-8](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L384>); [RDMS-02-M03-U000](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1935>); [RDMS-02-M03-U001](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1961>); [RDMS-02-M03-U032](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2869>); [RDMS-03-M04-U021](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L508>); [RDMS-02-M02-U004](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L131>); [RDMS-02-M02-U006](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L207>).

### L3-NR-PARENT-ConfidenceAssessment

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

The level values and residual uncertainty agree, but assessed_at and assessed_at_commit_seq are different information. A commit ordering number is not a wall-clock timestamp or a complete evidence-basis conversion.

**Binding obligations:** Preserve target, confidence level, evidence basis, residual uncertainty and assessment time/context. Claim/Hypothesis support must not gain a competing ConfidenceAssessment authority.

**Remaining detail / acceptance limit:** Proof for basis versus evidence_link_refs plus verification_record_refs, and assessed_at versus assessed_at_commit_seq. Do not silently equate time with sequence.

Exact authoritative evidence: [FCA-14](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L693>); [RDMS-03-M05-U040](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2791>); [RDMS-01-M01-U004](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1430>); [RDMS-03-M04-U066](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L1408>).

### L3-NR-SHAPE-ContainmentProof

**D — ALREADY_RESOLVED; RESOLVED_WITH_SOURCE_EVIDENCE.**

C01-27 is the approved complete scoped restatement of ContainmentProof for effective configuration and trusted enforcement. C01-28 supplements it with continuous enforcement. The old record is not a second current native schema. FCA reachable-effect isolation duties remain unchanged.

**Binding obligations:** Use the C01-27 native fields and trusted enforcement evidence. Prove filesystem isolation, absence of shared writable mounts and dangerous credentials, blocking of mutating network/privileged paths and disposability of reachable effects. Enforce the policy during execution; drift invalidates new launches under an old proof.

**Remaining detail / acceptance limit:** No historical-record converter or Boolean-to-policy alias is asserted. Backend-specific proof encoding remains subject to the retained containment duties.

Source-determined correction: Publish the approved C01-27 record once and explicitly retain the original isolation duties.

Exact authoritative evidence: [FCA-42](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1660>); [RDMS-04-M06-U052](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1083>); [RDMS-04-M07-U033](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L2161>); [RDMS-04-M07-U034](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L2185>).

### L3-NR-PARENT-ContradictionRecord

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

The comparison and causal-explanation boundary are explicit, but FCA UNRESOLVED is absent from the RDMS lifecycle, and possible_dimensions is replaced by dimension_analysis. No exact lifecycle/field projection is authorized by the excerpts.

**Binding obligations:** Preserve both observations, subject, scope, comparability, time/input/environment/world/nondeterminism/measurement dimensions and unresolved information. Causal explanations must refer to a typed proposition/result; they are not hidden in dimension_analysis.

**Remaining detail / acceptance limit:** Document how FCA unresolved status and dimension information are represented without inventing a new lifecycle value or declaring UNRESOLVED equal to CONFIRMED.

Exact authoritative evidence: [FCA-13](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L657>); [RDMS-03-M04-U029](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L631>); [RDMS-03-M04-U032](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L697>); [RDMS-03-M05-U019](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2377>).

### L2-NR-PARENT-Decision

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

C01 resolves accepted-content immutability, freshness and lineage. It does not give a complete crosswalk for FCA evidence_refs, rejected option reasons and chosen content into the later option/reference surface.

**Binding obligations:** Preserve question/context, gravity, quality drivers, constraints, alternatives, chosen option, every rejection reason, assumptions, accepted tradeoffs, evidence, consequences, risks, revisitation, lifecycle and version. Accepted semantic content is immutable.

**Remaining detail / acceptance limit:** Prove evidence_refs and every rejected {option, reason}, chosen content and version are recoverable through the exact owner records; do not infer that dependency_set_ref substitutes for evidence.

Exact authoritative evidence: [FCA-17](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L802>); [RDMS-02-M02-U034](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L854>); [RDMS-02-M02-U035](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L895>); [RDMS-02-M03-U014](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2340>); [RDMS-02-M03-U015](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2384>).

### L4-NR-PARENT-DependencyStamp

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

RDMS-06 explicitly retains FCA dependency kinds and freshness meanings. The inline validity_condition and the later validity_condition_ref still require preservation of the condition and its version/identity; this affects correctness, not only encoding.

**Binding obligations:** Retain dependency kind/subject, version or hash, validity condition and EXACT/COMPATIBLE/ADVISORY meaning. Use the one dependency engine; an incomplete dependency universe cannot certify complete validity.

**Remaining detail / acceptance limit:** Prove the subject and validity-condition reference binding, including source version, available content and replay/retention. No ref/dep-ref or inline-condition alias is invented.

Exact authoritative evidence: [FCA-69](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2481>); [RDMS-06-M12-U038](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt#L655>); [RDMS-06-M12-U040](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt#L706>); [RDMS-06-M13-U031](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt#L2268>); [RDMS-01-M00-U028](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L790>).

### L3-NR-SHAPE-EvidenceLink

**C — IMPLEMENTATION_DETAIL_DEFERRED; DEFERRED_TO_IMPLEMENTATION_DESIGN.**

This question specifically concerns the embedding field for already specified EvidenceBasis and pinned AuthorityBinding. C01-04 and C01-10 through 13 fully bind their information and usability. Choosing a member name or inline versus reference encoding supplies no additional legal meaning. Parent field preservation is separately kept open as PARENT-EvidenceLink.

**Binding obligations:** Carry EvidenceBasis items with observation identity and REQUIRED/CORROBORATING/CONTEXT role, ALL_REQUIRED or STRUCTURED semantics and the required derivation. Pin the AuthorityBinding version for AUTHORITATIVE evidence. Retain accepted-link immutability and derived usability.

**Remaining detail / acceptance limit:** Embedding member name and serializer layout only. Missing basis, lost role, unpinned authority, unavailable referent or changed derivation is a normative violation, never an implementation discretion.

Exact authoritative evidence: [RDMS-03-M05-U003](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2019>); [RDMS-03-M05-U009](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2165>); [RDMS-03-M05-U010](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2185>); [RDMS-03-M05-U011](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2199>); [RDMS-03-M05-U012](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2217>); [FCA-12](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L611>); [RDMS-03-M04-U019](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L457>); [RDMS-03-M04-U021](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L508>).

### L3-NR-PARENT-EvidenceLink

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

Multi-observation support and structured roles are explicitly approved. The full parent target identity/type, single-observation information and accepted semantic-link projection still need an exact reference/preservation proof; an unspecified embedding does not discharge this distinct question.

**Binding obligations:** Preserve link identity, canonical observations, typed target identity, relation, rationale, derivation and lifecycle. Every accepted link has a real Observation root. Preserve C01 basis roles, pinned authority and historical meaning.

**Remaining detail / acceptance limit:** Field-by-field parent/current reconstruction including observation_id, target_type/target_id and the new structured basis. No lossy flattening of REQUIRED/CORROBORATING/CONTEXT or automatic alias.

Exact authoritative evidence: [FCA-12](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L611>); [RDMS-03-M04-U021](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L508>); [RDMS-03-M04-U022](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L529>); [RDMS-03-M05-U009](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2165>); [RDMS-03-M05-U012](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2217>); [RDMS-03-M04-U019](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L457>).

### L3-NR-PARENT-Experiment

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

RDMS-03 expressly separates design from run, observations and conclusion proposals. That is a resolved legal distinction. The complete FCA design/run lifecycle and designed_at/executed_at reconstruction is not established by the abbreviated cross-layer record inventory.

**Binding obligations:** Retain question, hypotheses, method, discriminating predictions, authorized actions, risk, design/execution history, observations, conclusion proposal and time. Freeze predictions before runs; failed execution does not refute a hypothesis.

**Remaining detail / acceptance limit:** Prove all original fields through Experiment/Prediction/ExperimentRun/Observation/ExperimentConclusionProposal, especially original timestamps and lifecycle participation. No run-state-to-design-state alias.

Exact authoritative evidence: [FCA-40](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1592>); [RDMS-03-M04-U040](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L848>); [RDMS-03-M04-U043](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L929>); [RDMS-03-M04-U046](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L994>); [RDMS-03-M04-U048](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L1033>); [RDMS-03-M05-U023](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2473>); [RDMS-03-M04-U041](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L870>).

### L2-NR-PARENT-Goal

**D — ALREADY_RESOLVED; RESOLVED_WITH_SOURCE_EVIDENCE.**

All FCA Goal information is retained by RDMS-02 Goal plus AcceptanceCriterion. C01-14 explicitly renames priority to declared_priority; C01-11 adds cancellation without dropping the original states. This is an approved owner elaboration, not an unproved competing projection.

**Binding obligations:** Preserve typed Goal identity and parent, intent, acceptance criteria, declared priority, all original statuses and created_from. CANCELLED requires cancellation_reason and cancellation_authority_ref. Priority alone cannot drive scheduling.

**Remaining detail / acceptance limit:** No importer conversion API is approved. Entity identity is governed by CanonicalEntityMeta, and criterion requirements/waivers by the owner law.

Exact authoritative evidence: [FCA-15](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L732>); [RDMS-02-M02-U021](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L575>); [RDMS-02-M02-U022](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L616>); [RDMS-02-M03-U000](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1935>); [RDMS-02-M03-U010](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2242>); [RDMS-02-M03-U013](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2321>).

### L2-NR-PARENT-Hypothesis

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

Support, closure, relation and lineage ownership are explicitly amended, but a complete parent evidence/assumption/prediction/experiment reconstruction still needs proof. HG-01 separately handles the missing support-admission correspondence.

**Binding obligations:** Retain immutable explanatory identity, scope, explained subjects, assumptions, predictions, for/against evidence, experiments and competing relations. One lifecycle and one SupportAssessment authority; closure points to the causal result when applicable.

**Remaining detail / acceptance limit:** Prove complete original information across references and independent relation owners. This entry does not resolve HG-01 or permit replacing old support values with guessed new thresholds.

Exact authoritative evidence: [FCA-10](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L469>); [RDMS-02-M03-U001](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1961>); [RDMS-02-M03-U006](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2113>); [RDMS-02-M03-U019](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2497>); [RDMS-02-M03-U032](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2869>); [RDMS-02-M02-U013](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L381>).

### L2-NR-PARENT-InformationNeed

**D — ALREADY_RESOLVED; RESOLVED_WITH_SOURCE_EVIDENCE.**

RDMS-02 section 10 explicitly replaces the single resolution route with resolution_routes[] because multiple routes can answer the same question; section 12 explicitly makes the answer a typed ResolutionRef. Original identity, question, importance, blocks, candidates and all four lifecycle states remain.

**Binding obligations:** Retain all routes and source candidates; preserve typed blocked entities and resolution evidence. OBSOLETE is distinct from RESOLVED. HUMAN in the route list does not itself require immediate escalation.

**Remaining detail / acceptance limit:** Physical reference/serialization encoding; no new route, lifecycle or authority is introduced.

Exact authoritative evidence: [FCA-9](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L435>); [RDMS-02-M02-U002](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L86>); [RDMS-02-M02-U009](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L284>); [RDMS-02-M02-U010](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L322>); [RDMS-02-M02-U011](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L347>); [RDMS-02-M02-U012](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L369>).

### L2-NR-PARENT-Invariant

**D — ALREADY_RESOLVED; RESOLVED_WITH_SOURCE_EVIDENCE.**

RDMS-02 section 39 explicitly permits simultaneous enforcement modes; C01-28 replaces these with EnforcementSpec entries while preserving severity and modes. C01-01 supplies version metadata and C01-17/18 pins engineering semantics. No original enforcement duty is waived.

**Binding obligations:** Retain statement, scope, kind, severity, predicate/verification and source authority, version and ACTIVE/SUPERSEDED/RETIRED lifecycle. EnforcementSpec records mode, verifier, coverage and fail behavior. HARD remains unacceptable even when checking is semantic.

**Remaining detail / acceptance limit:** No automatic field converter is asserted. Runtime verifier mechanics cannot weaken coverage or fail behavior.

Exact authoritative evidence: [FCA-19](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L884>); [RDMS-02-M02-U038](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L946>); [RDMS-02-M03-U000](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1935>); [RDMS-02-M03-U016](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2414>); [RDMS-02-M03-U017](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2435>); [RDMS-02-M03-U027](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2717>); [RDMS-02-M03-U028](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2750>).

### L5-NR-PARENT-MemoryProposal

**D — ALREADY_RESOLVED; RESOLVED_WITH_SOURCE_EVIDENCE.**

RDMS-07 section 24 expressly adopts and expands FCA fields. Section 25 enumerates the required claim, scope, evidence, counterconditions/examples, requested maturity and invalidating dependencies; section 17 preserves the FCA maturity ladder. There is no omitted parent semantic category.

**Binding obligations:** Retain claim, proposed scope, source episodes, optional causal basis, applicability/counterconditions/counterexamples, evidence, confidence assessment and requested maturity. Added provenance/category/dependencies do not authorize promotion; LearningGate and Executive approval remain required.

**Remaining detail / acceptance limit:** Reference encoding only; no maturity_target/proposed_maturity wire alias or lossy converter is declared by this review.

Exact authoritative evidence: [FCA-60](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2234>); [RDMS-07-M14-U023](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L399>); [RDMS-07-M14-U029](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L461>); [RDMS-07-M14-U031](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L482>); [RDMS-07-M14-U032](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L513>).

### L3-NR-PARENT-Observation

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

C01 binds content trust, normalization and temporal provenance, but the whole parent field projection is not proven: mandatory parent world_ref versus optional native reference and source_authority versus associated bindings affect evidential interpretation.

**Binding obligations:** Preserve source, authority when applicable, real observation context/time/content/raw material/provenance/integrity and stable event identity. Normalization cannot introduce semantic inference. Trust metadata must travel with content.

**Remaining detail / acceptance limit:** Proof of parent world context, source authority and content/raw/integrity projection into the current surface. Do not manufacture a world reference for an observation whose source has no known world context.

Exact authoritative evidence: [FCA-11](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L576>); [RDMS-03-M04-U002](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L81>); [RDMS-03-M04-U010](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L264>); [RDMS-03-M04-U011](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L286>); [RDMS-03-M05-U000](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L1924>); [RDMS-03-M05-U020](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2410>).

### L2-NR-PARENT-OperationalCausalClaim

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

CausalVerificationRecord is explicitly a compact replacement for inline verification, and C01 makes freshness derived. Complete proof is still needed for every FCA evidence/dependency/verification and promotion-time field, including conditional regression capture.

**Binding obligations:** Preserve all eight FCA causal-closure obligations, causal scope, evidence, dependencies, contradictory observations and promotion history. OVC is scoped operational knowledge, not universal Fact; STALE usability does not become an independent lifecycle.

**Remaining detail / acceptance limit:** Prove evidence_refs, promoted_at, exact CausalScope and verification content through the approved records. Optional regression_verification_ref does not waive FCA technically-feasible durable regression duty.

Exact authoritative evidence: [FCA-10](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L469>); [RDMS-02-M02-U017](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L490>); [RDMS-02-M02-U018](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L511>); [RDMS-02-M03-U007](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2146>); [RDMS-03-M05-U041](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2823>); [RDMS-02-M02-U016](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L460>).

### L1-NR-SHAPE-ProjectRuntime

**C — IMPLEMENTATION_DETAIL_DEFERRED; DEFERRED_TO_IMPLEMENTATION_DESIGN.**

R1 explicitly provides ProjectHead, the atomic current-store/ledger boundary and separate durable ProjectStatus/process-local ProcessRuntimeMode. Only the aggregate embedding names remain unspecified; there is no missing authority or recovery state definition.

**Binding obligations:** One authoritative ControlTransaction atomically advances current state and replay/control records. ProjectHead carries the legal head/epoch/schema/status. Startup resets process mode and requires RecoveryBarrier before READY. Never persist READY as durable project truth.

**Remaining detail / acceptance limit:** ProjectRuntime aggregate member names, class layout and lookup arrangement. These cannot merge ProjectStatus with ProcessRuntimeMode or create a second control head.

Exact authoritative evidence: [RDMS-01-M01-U000](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1305>); [RDMS-01-M01-U001](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1336>); [RDMS-01-M01-U002](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1377>); [RDMS-01-M01-U023](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1952>); [RDMS-01-M00-U000](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L25>).

### L4-NR-PARENT-QueryDependencyStamp

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

The query kinds and frontier fields agree. The invalidation_rule is inline in FCA and referenced in RDMS-06; an exact identity/content/version binding is not established by equal-sounding names.

**Binding obligations:** Retain query, query kind, proof scope, dependency frontier, index kind/generation/hash where present, invalidation rule and repository basis. Negative knowledge cannot exceed proved coverage.

**Remaining detail / acceptance limit:** Prove invalidation_rule_ref preserves the exact invalidation rule with the required scope and historical/reference integrity. This is a freshness correctness proof, not just member naming.

Exact authoritative evidence: [FCA-70](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2524>); [RDMS-06-M12-U054](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt#L896>); [RDMS-06-M12-U055](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt#L923>); [RDMS-06-M12-U056](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt#L949>).

### L6-NR-SHAPE-ResumeAssessment

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

C01-38 adds context, reconciliations and Goal/Slice validity while retaining result meanings. It does not explicitly prove preservation of the earlier unresolved_action_refs and created_commit_seq through those aggregates. Scope completeness is recovery-critical.

**Binding obligations:** Assess current repository/world/environment context, every relevant unresolved action and its reconciliation, dependency evaluation and Goal/Slice validity. Retain assessment identity, capsule, basis and canonical history. RESUMABLE permits cognition, not world mutation.

**Remaining detail / acceptance limit:** Prove baseline current_repo_ref/current_world_ref, unresolved_action_refs and created_commit_seq remain recoverable. A list of reconciliation refs alone cannot prove that all relevant unresolved actions were considered.

Exact authoritative evidence: [RDMS-05-M09-U046](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L758>); [RDMS-05-M10-U046](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2120>); [RDMS-05-M10-U047](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2147>); [RDMS-05-M10-U049](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2188>); [RDMS-05-M10-U050](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2200>).

### L6-NR-SHAPE-ResumptionCapsule

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

C01-34 supplies durable payload and integrity references, not an explicit content crosswalk for every earlier context member. relevant_entity_refs and canonical_snapshot_ref do not by themselves prove retained context coverage. L6 sole ownership is already settled.

**Binding obligations:** Retain all source-required suspension context, canonical/repository/world/environment basis, dependencies, focus, claims/hypotheses/evidence/decisions, rejected paths, slices/actions, unknowns, commitments and temporary changes. Verify durable payload before atomic suspension; a capsule never authorizes replay of an old action.

**Remaining detail / acceptance limit:** Field/payload preservation proof for original project/context/basis collections and their versions. No new payload schema, snapshot alias or field embedding is selected.

Exact authoritative evidence: [FCA-53](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2032>); [RDMS-05-M09-U040](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L653>); [RDMS-05-M09-U041](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L694>); [RDMS-05-M10-U042](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2066>); [RDMS-05-M10-U043](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2092>); [RDMS-05-M10-U044](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2107>).

### L6-NR-PARENT-ResumptionCapsule

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

The FCA goal/subgoal, current focus, repo basis, created time and contextual arrays are mandatory architectural information. The compact amended capsule does not prove they are present merely by holding a payload/snapshot reference.

**Binding obligations:** Preserve every FCA suspension-context category and timestamp plus all non-superseded RDMS additions. Restore canonical state, evaluate changes and stale dependencies, reconcile relevant actions and then resume through Executive authority.

**Remaining detail / acceptance limit:** Prove task/goal/subgoal, base_state_version, repo_ref, focus, hypotheses/evidence/rejected paths/temporary changes/open needs, optional next action and created_at in the frozen referenced content. Do not equate created_at to a sequence number.

Exact authoritative evidence: [FCA-53](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2032>); [RDMS-05-M09-U040](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L653>); [RDMS-05-M09-U043](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L722>); [RDMS-05-M10-U042](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2066>); [RDMS-05-M10-U046](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2120>).

### L2-NR-SHAPE-Risk

**D — ALREADY_RESOLVED; RESOLVED_WITH_SOURCE_EVIDENCE.**

C01-30 is explicitly an abbreviated scoped amendment: status is split into lifecycle and treatment, with current_assessment_ref added. The ellipsis cannot erase unrelated original fields. The source therefore determines a conservative complete overlay without a guessed state migration.

**Binding obligations:** Retain risk_id, statement, scope, category, likelihood, impact, affected_refs, mitigation_refs, evidence_basis_refs, owner_ref and accepted_by_decision_id. Replace the single status with the exact C01 lifecycle/treatment enums and add current_assessment_ref. RiskAssessment freshness remains derived; acceptance is a Decision, not elimination of risk.

**Remaining detail / acceptance limit:** No old-status-to-new-pair converter or inline likelihood/impact-to-assessment alias is approved. These historical conversions require source-compatible conformance evidence; they do not prevent publishing the current scoped fields.

Source-determined correction: Apply only the explicit lifecycle/treatment overlay and retain every unrelated baseline field.

Exact authoritative evidence: [RDMS-02-M02-U045](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1139>); [RDMS-02-M02-U046](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1192>); [RDMS-02-M03-U029](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2770>); [RDMS-02-M03-U030](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2802>).

### L3-NR-PARENT-SandboxActivityRecord

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

The sandbox proof and snapshot references are explicit, but the parent result has no approved equivalence to activity_summary or completed_at. A completed activity is not necessarily a successful or effect-verified activity.

**Binding obligations:** Retain activity/Slice identity, base snapshot, proven containment, operation count, output and observation references and actual result. Sandbox completion cannot authorize artifact promotion.

**Remaining detail / acceptance limit:** Prove containment_profile/base_snapshot/output_refs and especially result survive in the current record/proof/artifacts. Do not replace result with a prose summary or completion time.

Exact authoritative evidence: [FCA-45](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1808>); [RDMS-04-M06-U052](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1083>); [RDMS-04-M06-U054](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1123>); [RDMS-04-M06-U055](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1146>).

### L2-NR-PARENT-Slice

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

C01 explicitly resolves SliceState decomposition and scoped freshness. It does not expressly waive parent rollback information or prove all inline engineering/change-surface information through the later reference specimen.

**Binding obligations:** Retain engineering scope, preconditions, pinned invariants/contracts, expected/actual effects and change surface, risk, proof, verification and rollback obligations. Keep stage/condition/terminal independent and use dependency freshness rather than global version alone.

**Remaining detail / acceptance limit:** Prove mandatory rollback versus rollback_spec?, risk_profile versus risk_refs, dependencies and inline expected-change-surface information. No automatic status-to-SliceState migration is chosen.

Exact authoritative evidence: [FCA-29](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1243>); [RDMS-02-M02-U048](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1268>); [RDMS-02-M03-U020](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2527>); [RDMS-02-M03-U024](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2615>); [RDMS-02-M03-U017](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2435>); [RDMS-02-M02-U047](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1216>).

### L2-NR-SHAPE-State

**C — IMPLEMENTATION_DETAIL_DEFERRED; DEFERRED_TO_IMPLEMENTATION_DESIGN.**

FCA section 6 gives logical groups; Appendix D expands a composite state view. RDMS defines the actual entity ownership and current replacements. A grouped view need not itself be a second canonical aggregate with a competing schema.

**Binding obligations:** Preserve access to all FCA logical categories and control references through their actual owners. Use GoalPath, derived validity and source-owned records. A State view cannot commit, redefine lifecycle or claim a separate recovery authority.

**Remaining detail / acceptance limit:** Composite view nesting, physical tables, joins and serializer layout. This does not defer any underlying entity field question; those remain individually classified.

Exact authoritative evidence: [FCA-6](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L278>); [RDMS-02-M03-U009](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2209>); [RDMS-02-M03-U032](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2869>); [RDMS-10-M24-U010](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3090>); [FCA-APP-D](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L3536>).

### L4-NR-SHAPE-TemporalSchedule

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

C01 hardens timezone/DST/discontinuity policies but its complete specimen omits original instant/local rule and validity bounds. Those specify which occurrence is legal and cannot be deferred as mere serialization.

**Binding obligations:** Preserve schedule kind, intended instant/local/recurring rule and not-before/valid-until bounds, timezone and rules version, DST/missed-occurrence/discontinuity policy. Legal occurrence identity must not depend on worker processing time.

**Remaining detail / acceptance limit:** Prove absolute_instant, local_time_rule, not_before and valid_until are retained by the effective schedule/occurrence contracts; no field alias or new scheduling law is selected.

Exact authoritative evidence: [RDMS-05-M09-U006](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L124>); [RDMS-05-M10-U030](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1879>); [RDMS-05-M10-U031](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1901>); [RDMS-05-M10-U032](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1922>); [RDMS-05-M10-U033](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1942>).

### L4-NR-PARENT-TemporalValidity

**D — ALREADY_RESOLVED; RESOLVED_WITH_SOURCE_EVIDENCE.**

The six field names and optionalities are identical. The three freshness symbols differ only in capitalization, and RDMS-05 section 38 explicitly preserves the FCA concept while stating that freshness is derived. There is no missing field or lifecycle mapping.

**Binding obligations:** Retain observed_at?, verified_at?, repo_ref?, state_version?, valid_until_condition? and CURRENT/STALE/UNKNOWN freshness. Use the canonical dependency engine; the Scheduler cannot assert authoritative freshness.

**Remaining detail / acceptance limit:** Serializer capitalization only; no independent freshness field authority.

Exact authoritative evidence: [FCA-54](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2083>); [RDMS-05-M09-U049](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L799>); [RDMS-05-M09-U050](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L820>).

### L3-NR-SHAPE-ToolResult

**C — IMPLEMENTATION_DETAIL_DEFERRED; DEFERRED_TO_IMPLEMENTATION_DESIGN.**

The only declaration is explicitly an example exit_code = 0, used to demonstrate that a report does not establish reality. RDMS-04 ToolAdapter has output_schema_ref; ProcessRun, ActionAttempt and Observation already define binding semantics. The example is not an incomplete mandatory canonical ToolResult schema.

**Binding obligations:** Keep reported output attributed to its actual attempt/process/source; preserve output completeness/integrity and capture it through Observation Ingress. Exit code zero does not prove the requested effect; OutcomeProbe/reconciliation still apply.

**Remaining detail / acceptance limit:** Adapter-specific result representation and output serializer under output_schema_ref. No new canonical ToolResult entity, success lifecycle or dispatch authority is created.

Exact authoritative evidence: [RDMS-04-M06-U015](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L386>); [RDMS-04-M06-U020](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L498>); [RDMS-04-M06-U062](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1241>); [RDMS-04-M06-U071](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1365>); [RDMS-04-M07-U039](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L2247>).

### L4-NR-PARENT-TriggerCondition

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

RDMS-05 section 6 expressly splits repetition and detection dimensions; section 13 preserves conceptual trigger states and separates evaluation/fire/reaction. The remaining FCA last_evaluated_at/last_fire_id/source/watch and reaction associations still need a complete information-preservation crosswalk.

**Binding obligations:** Retain trigger identity/generation, both semantics dimensions, watched sources/predicate, cursor, reaction identity, linked object, on-fire semantics, conceptual state and evaluation/fire history. L4 evaluates; it never authorizes a world action.

**Remaining detail / acceptance limit:** Prove each original field through TriggerDefinition, condition, state/evaluation, fire and reaction records, especially timestamps and last-fire relation. No condition-state or time-to-commit alias is invented.

Exact authoritative evidence: [FCA-56](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2123>); [RDMS-05-M09-U008](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L155>); [RDMS-05-M09-U016](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L307>); [RDMS-05-M10-U015](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1638>); [RDMS-05-M10-U018](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1716>); [RDMS-05-M09-U009](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L190>).

### L4-NR-SHAPE-TriggerFire

**D — ALREADY_RESOLVED; RESOLVED_WITH_SOURCE_EVIDENCE.**

C01-12/13/14 explicitly replace unstable fire construction with immutable definition and qualified occurrence references plus a uniqueness tuple. C01-06 binds canonical processing atomically. This is the approved current native fire surface; old direct trigger/generation/condition fields are retained by the frozen definition/occurrence semantics rather than competing mutable copies.

**Binding obligations:** Use the exact C01-14 fields. The definition and occurrence bind the trigger and generation; preserve immutable condition/reaction identity, evidence basis and source frontier. Enforce uniqueness of trigger_id/generation/occurrence_key; replay returns the same Fire. The canonical creation sequence is not the source event time.

**Remaining detail / acceptance limit:** No old-record importer or fired_at_commit_seq/created_commit_seq wire alias is invented. Source occurrence time and canonical processing order remain distinct.

Source-determined correction: Publish the approved stable TriggerFire record and its source-defined identity/atomicity requirements.

Exact authoritative evidence: [RDMS-05-M09-U027](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L450>); [RDMS-05-M10-U007](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1509>); [RDMS-05-M10-U015](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1638>); [RDMS-05-M10-U016](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1670>); [RDMS-05-M10-U017](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1691>).

### L4-NR-SHAPE-TriggerReaction

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

C01-29 supplies target-version/lifecycle admission and C01-15 the stable reaction identity. The relationship of old reaction_kind/reaction_key to frozen_reaction_spec_ref/reaction identity is not a complete declared field mapping. Deduplication is legally mandatory.

**Binding obligations:** Preserve the frozen reaction kind, target, stable reaction identity/key and exact trigger definition generation. Apply legal target transition, APPLIED and key consumption in one ControlCommit. Worker reclaiming is not a second effect or action authority.

**Remaining detail / acceptance limit:** Prove all original reaction_kind/key semantics through the frozen spec and C01 identity without guessing a key alias or hash serialization. C01 target-bound statuses govern current admission; source history remains intact.

Exact authoritative evidence: [RDMS-05-M09-U029](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L482>); [RDMS-05-M09-U030](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L511>); [RDMS-05-M10-U018](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1716>); [RDMS-05-M10-U036](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1968>); [RDMS-05-M10-U037](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1993>); [RDMS-05-M10-U039](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2031>).

### L4-NR-SHAPE-TriggerSourceCursor

**C — IMPLEMENTATION_DETAIL_DEFERRED; DEFERRED_TO_IMPLEMENTATION_DESIGN.**

C01-05 explicitly replaces the conflated cursor concept with two different frontiers and defines exactly when each may advance. The remaining question is how to embed these already distinct contracts. Position meaning is explicitly delegated to the source adapter, not guessed globally.

**Binding obligations:** IngressCursor tracks durable source capture; TriggerProcessingCursor tracks durable evaluation and required Fire/Reaction or deferred evaluation obligations. Neither can outrun its own durable frontier. Retain source generation, adapter-defined position and coverage semantics.

**Remaining detail / acceptance limit:** Member names, physical cursor tables, position serialization and aggregate embedding. Never defer the capture/processing distinction, acknowledgement fence, coverage or atomicity.

Exact authoritative evidence: [RDMS-05-M09-U023](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L386>); [RDMS-05-M10-U005](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1471>); [RDMS-05-M10-U006](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1493>); [RDMS-05-M10-U007](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1509>).

### L1-NR-CE-01

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

FCA says each canonical event includes at least event_id/schema_version/idempotency_key; R1 adds event_type_version and separates schema dimensions. These requirements can coexist, so this is not a proved contradiction. R1 does not explicitly waive the two FCA members or equate them with enclosing commit metadata.

**Binding obligations:** Preserve event_id, schema_version and idempotency_key for every canonical event, alongside R1 event type/version, ordinal and payload. Preserve ControlCommit control_schema_version, command idempotency_key/fingerprint and immutable events. Do not conflate event, payload, control and snapshot codec versions.

**Remaining detail / acceptance limit:** Prove event metadata inclusion/resolution and its exact scope. No schema_version = event_type_version/control_schema_version or event key = enclosing commit key is approved. The original warning is narrowed to this precise binding proof.

Exact authoritative evidence: [FCA-48](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1921>); [RDMS-01-M01-U004](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1430>); [RDMS-01-M01-U009](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1600>); [RDMS-01-M01-U015](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1750>); [RDMS-01-M01-U016](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1768>).

### L2-NR-HG-01

**E — EXPLICIT_ARCHITECTURAL_DECISION_REQUIRED; OPEN_ARCHITECTURAL_DECISION.**

C01 removes scalar Hypothesis.support and uses a shared SupportAssessment level vocabulary. C01-07 and RDMS-03 C01-42 resolve OVC closure authority, but no clause supplies the complete ordinary CONFIRMED/REJECTED admission correspondence from the earlier support combinations. This affects a legal transition; it cannot be deferred to a serializer.

**Binding obligations:** Keep immutable assessments and derived validity, one Hypothesis lifecycle, historical closure precursor and the full Causal Closure Gate. STRONG and REFUTED are present in both vocabularies, but that fact is not a complete new admission table; generic VERIFIED is not automatically causal verification.

**Remaining detail / acceptance limit:** Smallest decision: ratify the effective support-assessment predicates for ordinary CONFIRMED/REJECTED admission after C01, including validity and whether VERIFIED satisfies the old minimum. Do not reopen OVC gate or invent weaker support thresholds.

Architecture review must decide the stated minimum; neither alternative is adopted.

- Ratify a minimal shared-level admission rule: Explicitly retain the known STRONG/REFUTED obligations and specify treatment of the remaining new assessment levels/validity. This supplies a new approved legal guard; an implementation cannot choose it.
- Ratify a complete legacy-to-assessment correspondence: Specify each relevant old support meaning and the predicates supporting ordinary closure under C01; preserves interpretable historical transitions but requires a broader approved crosswalk.

Exact authoritative evidence: [RDMS-02-M02-U014](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L422>); [RDMS-02-M02-U015](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L448>); [RDMS-02-M03-U001](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L1961>); [RDMS-02-M03-U002](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2003>); [RDMS-02-M03-U006](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2113>); [RDMS-03-M05-U041](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2823>).

### L7-NR-TRANSPORT-CapabilityResult

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

The canonical payload has patch, typed propositions, needs, evidence, assessments, specialist request and rationale categories missing as literal members of the RDMS-10 envelope. FC10-03-08 forbids redefinition, and the final registry limitation expressly leaves field audit necessary. proposal_refs is not evidence that all payload survives.

**Binding obligations:** Retain all eleven FCA result categories with optionality, types, provenance, dependencies and immutable identity/version when required. Only the Executive adopts cognition; delivery cannot authorize commits/actions.

**Remaining detail / acceptance limit:** Produce a lossless payload/reference projection proof for each canonical field, particularly specialist_request, needs, rationale_summary and evidence_refs. No new attachment field or field alias is selected.

Exact authoritative evidence: [FCA-23](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L999>); [RDMS-10-M23-U012](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L342>); [RDMS-10-M24-U007](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3036>); [RDMS-10-M24-U008](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3048>); [RDMS-10-M26-U023](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7658>); [RDMS-10-M26-U028](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7720>).

### L7-NR-TRANSPORT-MemoryRetrievalResult

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

The transport envelope does not literally include canonical retrieval/query identity, omitted scope, ranking policy, coverage, freshness or creation time. Memory and transport meanings may coexist, but trust annotations do not prove those retrieval facts are carried.

**Binding obligations:** Retain retrieval_id, query_ref, candidate_refs, omitted_or_filtered_scope, ranking_policy_ref, retrieval_coverage, freshness_summary and created_at plus transport trust/provenance/applicability. Retrieval never promotes truth or grants disclosure.

**Remaining detail / acceptance limit:** Produce a lossless reference/payload projection for every canonical retrieval field. Do not equate memory_refs with candidate_refs or provenance with coverage without source-compatible proof.

Exact authoritative evidence: [RDMS-07-M14-U074](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L1079>); [RDMS-10-M23-U046](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1134>); [RDMS-10-M24-U007](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3036>); [RDMS-10-M26-U023](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7658>); [RDMS-10-M26-U028](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7720>).
