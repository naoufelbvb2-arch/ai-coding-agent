# Cross-layer interface validation

**All twelve paths processed. Full field/conversion and baseline-law acceptance remains OPEN.**
This is a source-backed constraint review. No callable signature or unspecified serializer is fabricated. Source-defined record fields and optionality are attached in the JSON evidence. Transport projections preserve owner semantics; naming an alias does not prove a lossless mapping.

## X8-01: L2 → L7 → L2

Owner contracts: L2 canonical capability meaning / L7 transport.

Inputs: CapabilityInvocation. Outputs: CapabilityResult, CapabilityTransportResult.

**Authority and transitions:** Executive consumes proposals; L7 cannot issue cognitive or action permission.

**Atomicity and durability:** No canonical state transition follows delivery alone. Owner-authorized adoption enters L1 ControlTransaction.

**Failure, retry and recovery:** Provider timeout, malformed output or old epoch yields rejection/revalidation; retries are invocation delivery and never automatic tool redispatch.

**Rejection:** Reject omitted canonical payload, forged authority, stale dependencies or any unproved lossy transport conversion.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: baseline-law and owner-projection conformance audit.

Source/amendment evidence: [RDMS-10-M23-U012](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L342>); [RDMS-10-M24-U008](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3048>); [RDMS-10-M26-U023](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7658>); [FCA-23](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L999>).

## X8-02: L5 → L7 → L2

Owner contracts: L5 canonical retrieval / L7 transport.

Inputs: MemoryQuery, MemoryRetrievalRequest. Outputs: MemoryRetrievalResult, MemoryRetrievalTransportResult.

**Authority and transitions:** Retrieval supplies precedent; only Executive can adopt current guidance, and LearningGate governs promotion.

**Atomicity and durability:** Memory revisions use L1 durability; transport cannot replace retrieval coverage, query identity or canonical version.

**Failure, retry and recovery:** Provider/index failure reports partial/unknown coverage; absent search results do not prove absence.

**Rejection:** Reject missing trust/provenance/coverage, unauthorized cross-project disclosure or lossy result mapping.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: baseline-law and owner-projection conformance audit.

Source/amendment evidence: [RDMS-07-M14-U074](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L1079>); [RDMS-07-M15-U024](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L2308>); [RDMS-07-M15-U027](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L2377>); [RDMS-10-M23-U046](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1134>); [RDMS-10-M26-U023](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7658>); [FCA-62](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2294>).

## X8-03: L2 → L4 → L1

Owner contracts: L2 Commitment / L4 condition and processing.

Inputs: Commitment, TriggerCondition. Outputs: TriggerEvaluation, TriggerFire, TriggerReaction.

**Authority and transitions:** Executive owns Commitment transitions. L4 may evaluate frozen temporal predicates and apply only the declared reaction authority.

**Atomicity and durability:** Preserve one condition root, inbox/processing separation and atomic fire/reaction target mutation. Detection may repeat; canonical application deduplicates.

**Failure, retry and recovery:** Replayable sources and qualified occurrence identity govern replay; UNKNOWN coverage cannot assert a missed edge or absence.

**Rejection:** Reject unbound temporal commitment, incoherent composite input, changed frozen definition, duplicate effect or invalid target version.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: TriggerCondition, TriggerFire, TriggerReaction.

Source/amendment evidence: [RDMS-02-M03-U031](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2831>); [RDMS-05-M10-U001](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1357>); [RDMS-05-M10-U007](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1509>); [RDMS-05-M10-U017](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1691>); [RDMS-05-M10-U037](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1993>); [FCA-55](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2106>); [FCA-56](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2123>).

## X8-04: L4 → L1 → L3

Owner contracts: L4 temporal reaction / L3 action authority.

Inputs: TriggerReaction, TriggerDerivedWorkCommitment. Outputs: ActionProposal, ActionAuthorization, ActionRecord.

**Authority and transitions:** Trigger reaction may commit continuation work; it never authorizes ActionProposal or dispatch independently.

**Atomicity and durability:** Reaction/continuation is atomic where required. Dispatch needs ActionGate, durable intent, legal ownership and trusted executor fencing.

**Failure, retry and recovery:** Reaction replay deduplicates. Action delivery recovery enumerates obligations; external retry follows L3 effect semantics.

**Rejection:** Reject obsolete generation, cancelled target, orphaned obligation, missing durable dispatch intent or reused unsafe authorization.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: TriggerReaction, ActionProposal, ActionRecord.

Source/amendment evidence: [RDMS-05-M10-U036](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L1968>); [RDMS-05-M11-U001](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2453>); [RDMS-10-M25-U018](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5827>); [RDMS-10-M25-U019](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5853>); [RDMS-10-M26-U019](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7640>); [FCA-45](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1808>).

## X8-05: L4 → L6 → L1

Owner contracts: L6 capsule, suspension and resume integrity / L4 scheduling.

Inputs: ResumptionCapsule, WorkReactivationBinding. Outputs: ResumeAssessment, RecoveryAdmissionBinding.

**Authority and transitions:** L6 owns admission/integrity; L4 schedules detection and reactivation. Executive must reassess resumed cognition.

**Atomicity and durability:** Durable capsule bytes/hash precede atomic suspension metadata and legal recovery continuation. Cursor advancement cannot outrun required durable reaction.

**Failure, retry and recovery:** Missing/corrupt capsule or unresolved action blocks resume. Persistence failure cannot be reported as guaranteed automatic recovery.

**Rejection:** Reject corrupt/missing payload, stale check at commit, unproved action outcome or expanded recovery scope.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: ResumptionCapsule, ResumeAssessment.

Source/amendment evidence: [RDMS-05-M10-U042](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2066>); [RDMS-05-M10-U043](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2092>); [RDMS-05-M10-U046](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2120>); [RDMS-05-M10-U049](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt#L2188>); [RDMS-09-M21-U070](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt#L6851>); [RDMS-09-M22-U016](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt#L8258>); [FCA-52](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2009>); [FCA-53](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2032>); [FCA-82](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2842>).

## X8-06: L2 → L3 → L1

Owner contracts: L3 world action / L2 Executive / L1 durability.

Inputs: Slice, ActionProposal. Outputs: ActionAuthorization, ActionRecord, ControlCommit.

**Authority and transitions:** Current Executive supplies semantic authorization; ActionGate validates legal scope and effect; control persistence grants no independent permission.

**Atomicity and durability:** Compare expected state/resources, commit dispatch ownership, persist acknowledged recoverable intent, validate effective execution at last enforceable boundary, then dispatch.

**Failure, retry and recovery:** Before possible dispatch, revoke/revalidate. At intent or later, preserve unknown effects and reconcile; compensation is a new authorized action.

**Rejection:** Reject stale epoch, failed expected-version check, altered effective operation, unknown containment or missing recoverable durability.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: Slice, ActionProposal, ActionRecord, ControlCommit.

Source/amendment evidence: [RDMS-04-M07-U004](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1687>); [RDMS-04-M07-U005](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt#L1712>); [RDMS-10-M24-U051](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3620>); [RDMS-10-M25-U028](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5977>); [RDMS-10-M25-U038](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6090>); [FCA-41](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1641>); [FCA-42](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1660>); [FCA-45](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1808>); [FCA-49](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1949>).

## X8-07: L3 → L2 → L1

Owner contracts: L3 observation/evidence / L2 epistemic adoption.

Inputs: Observation, EvidenceLink, SupportAssessment. Outputs: Claim, Hypothesis, CanonicalMutation.

**Authority and transitions:** Trusted Observation Ingress captures reality without Executive semantic inference. Executive authorizes interpretation/adoption under grounding law.

**Atomicity and durability:** Observation append has legal commit ordering; historical capture and accepted evidence are immutable. Source causality is not inferred from arrival.

**Failure, retry and recovery:** Duplicate capture retains origin lineage. Missing causal parent may allow raw capture while causal attachment remains pending.

**Rejection:** Reject model-fabricated observation, semantic capture deletion, unsupported evidence root, wrapper inflation or forged source/authority metadata.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: Observation, EvidenceLink, Claim, Hypothesis, CanonicalMutation.

Source/amendment evidence: [RDMS-03-M05-U000](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L1924>); [RDMS-03-M05-U006](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2098>); [RDMS-03-M05-U009](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2165>); [RDMS-03-M05-U018](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2357>); [RDMS-10-M25-U057](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6308>); [RDMS-10-M26-U020](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7644>); [FCA-7](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L367>); [FCA-11](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L576>); [FCA-12](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L611>); [FCA-76](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2716>).

## X8-08: L2 → L3 → L2

Owner contracts: L2 hypothesis/causal entities / L3 experimental evidence.

Inputs: Hypothesis, Experiment, ExperimentDesignSnapshot. Outputs: ExperimentRun, PredictionEvaluation, CausalVerificationRecord, OperationalCausalClaim.

**Authority and transitions:** Executive approves experiments and causal adoption; mutating experiment steps separately obey ActionGate.

**Atomicity and durability:** Prediction freeze, authorized design snapshot and experiment authorization are atomic. Every run pins exact design and relevant execution context.

**Failure, retry and recovery:** Execution failure differs from falsified prediction. Nonconforming or unresolved required effects cannot close the intended experiment.

**Rejection:** Reject post-result prediction rewriting, current-experiment-only run binding, causal truth from simulation or COMPLETED alone.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: Hypothesis, Experiment, OperationalCausalClaim.

Source/amendment evidence: [RDMS-02-M03-U006](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt#L2113>); [RDMS-03-M05-U022](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2444>); [RDMS-03-M05-U023](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2473>); [RDMS-03-M05-U030](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2601>); [RDMS-03-M05-U032](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2639>); [RDMS-03-M05-U041](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2823>); [FCA-40](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1592>); [FCA-74](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2674>).

## X8-09: L3 → L2

Owner contracts: L3 comparison record / L2 causal proposition.

Inputs: ContradictionRecord, Observation. Outputs: InformationNeed, Hypothesis, Claim.

**Authority and transitions:** A contradiction record compares scoped observations; causal explanation belongs to a typed proposition or deterministic result adopted under Executive authority.

**Atomicity and durability:** Preserve conflicting observations and comparison provenance; lifecycle changes cannot erase historical capture.

**Failure, retry and recovery:** Resolve dimensions such as time/input/environment before interpretation; unknown comparability requires acquisition rather than invented cause.

**Rejection:** Reject hidden root-cause truth in dimension_analysis or inconvenient observation invalidation.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: ContradictionRecord, Observation, InformationNeed, Hypothesis, Claim.

Source/amendment evidence: [RDMS-03-M05-U007](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2124>); [RDMS-03-M05-U019](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2377>); [RDMS-03-M05-U020](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt#L2410>); [FCA-13](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L657>).

## X8-10: L4 → L2 → L1

Owner contracts: L4 freshness / L2 adoption and finalization.

Inputs: DependencySet, DependencyEvaluation, ReadinessSnapshot. Outputs: CognitiveControlDecision, CompletionStateBinding, CanonicalMutation.

**Authority and transitions:** One dependency engine reports freshness. Executive owns adoption/completion; estimates and compatibility claims cannot self-authorize transitions.

**Atomicity and durability:** Use coherent dependency universe, transitive lineage and commit-time recheck of affected state. Completion is atomically bound to evidence-covered state.

**Failure, retry and recovery:** Unrelated repository changes need not invalidate valid scoped knowledge. Incomplete indexes and unproved negative-query coverage remain UNKNOWN.

**Rejection:** Reject downgraded EXACT requirements, COMPATIBLE without proof, stale supporting dependencies or future-state completion claims.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: CanonicalMutation.

Source/amendment evidence: [RDMS-06-M13-U031](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt#L2268>); [RDMS-06-M13-U038](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt#L2390>); [RDMS-06-M13-U042](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt#L2468>); [RDMS-06-M13-U045](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt#L2518>); [RDMS-08-M17-U016](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-08_APPROVED_SOURCE_SET.txt#L2766>); [RDMS-10-M25-U078](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6526>); [RDMS-10-M26-U022](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7654>); [FCA-69](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2481>); [FCA-70](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2524>); [FCA-71](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2601>).

## X8-11: L3 → L5 → L7

Owner contracts: L5 learning/use / L7 actual egress binding.

Inputs: Observation, MemoryProposal, MemoryProposalSnapshot. Outputs: MemoryRecord, MemoryRetrievalResult, SealedOutboundContext.

**Authority and transitions:** LearningGate plus Executive authorization governs canonical promotion. Retrieval and transport cannot promote truth or grant disclosure.

**Atomicity and durability:** Freeze proposal/evidence binding, revalidate LearningGate at commit and use governed revision transaction. Actual outbound bytes/destination/purpose must match sealed admission.

**Failure, retry and recovery:** Replay learning promotion idempotently. Revision conflicts require new evaluation; provider switching or altered outbound context requires renewed disclosure checks.

**Rejection:** Reject unsupported causal memory, repeated evidence counted as diversity, stale promotion, stored prompt authority or unapproved actual egress.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: Observation, MemoryProposal.

Source/amendment evidence: [RDMS-07-M15-U018](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L2221>); [RDMS-07-M15-U021](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L2271>); [RDMS-07-M15-U032](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L2451>); [RDMS-07-M15-U059](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt#L2860>); [RDMS-10-M25-U067](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6412>); [RDMS-10-M26-U021](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7650>); [FCA-60](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2234>); [FCA-62](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2294>); [FCA-77](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2732>).

## X8-12: L3 → L6 → L1

Owner contracts: L6 recovery admission / L3 containment and effects.

Inputs: ContainmentProof, ActionRecord, RecoveryCase. Outputs: ScopedRecoveryAdmission, RecoveryAdmissionBinding, CrossFrontierAdmissionProof.

**Authority and transitions:** Recovery has bounded source-owned authority. Destructive restore, compensation and world mutation retain ActionGate requirements.

**Atomicity and durability:** Prove acknowledged-history continuity, anti-rollback/admission frontiers, containment and disclosure barriers before enabling affected execution.

**Failure, retry and recovery:** Restore cannot undo possible post-backup effects. Unknown scope uses conservative bounds; independent proved scopes may proceed.

**Rejection:** Reject guessed successful effect, blind retry, unfenced stale writer, missing authority frontier or uncontained restored executable data.

**Field acceptance:** OPEN. Candidate source fields remain subject to the registry issues: ContainmentProof, ActionRecord.

Source/amendment evidence: [RDMS-09-M19-U029](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt#L2426>); [RDMS-09-M19-U082](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt#L3006>); [RDMS-09-M20-U042](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt#L4681>); [RDMS-09-M21-U015](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt#L6119>); [RDMS-09-M21-U024](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt#L6251>); [RDMS-09-M21-U052](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt#L6612>); [RDMS-09-M22-U013](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt#L8240>); [FCA-48](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1921>); [FCA-52](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2009>); [FCA-73](<../../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2656>).
