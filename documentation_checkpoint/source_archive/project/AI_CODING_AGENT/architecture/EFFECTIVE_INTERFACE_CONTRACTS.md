# Effective interface contracts — architecture-level normative consolidation candidate

**Authority:** FCA v1.0.1 and approved RDMS source texts remain controlling. This publication does not alter frozen sources, create an API method or authorize effects. Each record named below imports its source-owned definition; missing field types are **not** inferred. Original definitions and amendment bodies are in `reviews/source_archive/` and `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.

**Contract rule:** At an interface, mandatory data and gates are cumulative; source text marked draft/historical cannot override an approved later correction. A later abbreviated `{...}` is not a legal deletion of untouched fields. Rejected/unknown effects remain observable and recoverable. A provider or specialist never becomes a canonical commit authority.

The signatures below specify **records exchanged and legal admission predicates**. They do not assert that primitive storage types, network serialization, implementations, or adapter conversions have been proven. Therefore they are candidates for the *architectural* freeze, not executable interfaces.


## X8-01 — Capability invocation / result

**Owner:** `L7_RUNTIME_INTEGRATION.md` · **Boundary:** L2 → L7 → L2

**Input records:** `CapabilityInvocation`

**Output records:** `CapabilityResult` (FCA §23); **noncanonical RDMS-10 transport alias:** `CapabilityTransportResult`

**Supporting records:** `CapabilityActivationContract`, `ExecutiveTransitionIntegrationBinding`

**Legal writer/approver:** L2 Cognitive Executive proposes; only authorized Control CommitGate can adopt legal state.

**Acceptance:** invocation/context/dependency identity valid; capability activated and budget/scope accepted; transport provenance resolves to original cognitive result.

**Mandatory rejection:** unactivated capability; unresolved provenance; identity or epoch mismatch; tool response pretending to be a canonical decision.

**Commit/effect boundary:** No provider or transport result is itself a canonical commit.

**Retry/recovery:** Repeated or late invocation results must be fenced/deduplicated under canonical authority.

**Primary norms:** FCA §23, §48–52; RDMS-10 capability activation and executive transition bindings.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-02 — Memory retrieval and re-use

**Owner:** `L5_MEMORY.md` · **Boundary:** L5 → L7 → L2

**Input records:** `MemoryRetrievalRequest`

**Output records:** `MemoryRetrievalResult` (RDMS-07); **noncanonical RDMS-10 transport alias:** `MemoryRetrievalTransportResult`

**Supporting records:** `MemoryRetrievalCoverage`, `MemoryUseAssessment`

**Legal writer/approver:** L5 owns retrieval evidence and use constraints; L2 owns cognitive incorporation; L7 conveys only.

**Acceptance:** scope, coverage, provenance, applicability and freshness available from legal retrieval result; access policy respected.

**Mandatory rejection:** short list falsely asserted exhaustive; missing coverage/freshness; access/scope mismatch; transport alias not dereferenceable.

**Commit/effect boundary:** Retrieval or ranking does not mutate belief or authorize learning.

**Retry/recovery:** Replay keeps retrieval/query identity; stale results re-assessed before use.

**Primary norms:** RDMS-07 retrieval coverage/use assessment; RDMS-10 memory transport.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-03 — Commitment / reactivation

**Owner:** `L2_COGNITION.md` · **Boundary:** L2 → L4 → L1

**Input records:** `Commitment`, `TriggerCondition`

**Output records:** `TriggerDerivedWorkCommitment`

**Supporting records:** `ExecutiveTransitionIntegrationBinding`

**Legal writer/approver:** L2 owns commitment semantics; L4 determines temporal eligibility; L1 owns legal mutation.

**Acceptance:** single lawful reactivation condition root and valid target identity/lifecycle; derived work durably attributable to commitment.

**Mandatory rejection:** legacy timestamp or trigger aliases fabricated; activation treated as satisfaction; stale or already retired commitment.

**Commit/effect boundary:** Activation and accepted derived-work obligation require canonical durable transition before downstream work.

**Retry/recovery:** Idempotent processing keyed to durable source and target; no action authority from trigger.

**Primary norms:** RDMS-02 C01-32; RDMS-05 trigger-derived work; RDMS-10 C02.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-04 — Trigger firing and actions

**Owner:** `L4_TEMPORAL_SPECIALISTS.md` · **Boundary:** L4 → L1 → L3

**Input records:** `TriggerDefinition`, `TriggerFire`

**Output records:** `TriggerReaction`

**Supporting records:** `DispatchAdmissionCutover`, `TriggerActionCausalityBinding`

**Legal writer/approver:** L4 evaluates conditions; L1 validates and commits durable reaction; L3 requires independent ActionGate.

**Acceptance:** definition snapshot/generation/qualified occurrence verified; target version and reaction are current.

**Mandatory rejection:** duplicate fire; obsolete target; invalid trigger generation; reaction directly dispatching an external mutation.

**Commit/effect boundary:** Reaction/target transition obey ControlCommit atomicity and durable identity.

**Retry/recovery:** Reaction remains inspectable, replay-safe, and cannot be mistaken for an external effect.

**Primary norms:** RDMS-05 C01 TriggerFire/TriggerReaction; RDMS-10 TriggerActionCausalityBinding.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-05 — Suspension / resumption

**Owner:** `L6_RECOVERY.md` · **Boundary:** L4 → L6 → L1

**Input records:** `ResumptionCapsule`

**Output records:** `RecoverySuspensionCommitment`

**Supporting records:** `BootstrapHandoffProof`, `RecoveryAdmissionBinding`

**Legal writer/approver:** L6 validates restoration and containment; L1 owns admission and epoch fencing.

**Acceptance:** full durable capsule payload is integrity-checked and consistent with pinned state, identity, authority, and epoch.

**Mandatory rejection:** truncated historical conversion; absent payload verification; stale/missing handoff or authority; fabricated field defaults.

**Commit/effect boundary:** Suspension/resumption creates no implied world rollback.

**Retry/recovery:** IN_DOUBT effects reconcile before further shared-world mutation.

**Primary norms:** RDMS-09 recovery; RDMS-10 BootstrapHandoffProof/RecoveryAdmissionBinding.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-06 — External execution and journal

**Owner:** `L3_ACTIONS.md` · **Boundary:** L2 → L3 → L1

**Input records:** `ActionProposal`, `SealedExecutionIntent`

**Output records:** `ActionRecord`, `ActionDeliveryContract`

**Supporting records:** `DispatchAdmissionCutover`, `EffectiveExecutionBinding`, `RecoverableActionDeliveryObligation`

**Legal writer/approver:** L3 ActionGate approves exact shared-world mutation; executor cannot change effective command or scope; L1 records legal transitions.

**Acceptance:** authorization matches exact effective operation/arguments/target, resource versions and current policy/dependency/epoch frontier.

**Mandatory rejection:** unsealed or modified command; stale authority; missing durable dispatch intent; blind retry of unknown non-idempotent effect.

**Commit/effect boundary:** Persist DISPATCH_INTENT before effect. Ledger atomicity != atomic external side effect; durable Action Journal/reconciliation required.

**Retry/recovery:** Mark IN_DOUBT and probe/reconcile; do not assert exactly-once without external guarantee.

**Primary norms:** FCA §42–47, §48–52; RDMS-04 C01; RDMS-10 C01/C02.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-07 — Observation and evidence

**Owner:** `L3_ACTIONS.md` · **Boundary:** L3 → L2 → L1

**Input records:** `Observation`, `ContentTrustContext`

**Output records:** `EvidenceLink`, `ObservationCausalAttachmentContract`

**Supporting records:** `FactGrounding`, `ObservationSourceBinding`

**Legal writer/approver:** L3 ingests provenance and trust; L2 decides epistemic use; L1 gates legal writes.

**Acceptance:** source/trust context travels with observation; observed content preserved as immutable; causal attachment separately justified.

**Mandatory rejection:** tool self-report promoted to certainty; untrusted content granting authority; disagreement mislabeled capture corruption.

**Commit/effect boundary:** Append accepted observation and source binding; separate append from causal inference.

**Retry/recovery:** Amend only capture/provenance defects with traceable amendment; keep original observation.

**Primary norms:** FCA §75–76; RDMS-03 C01 observation trust/amendment; RDMS-10 C01/C02.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-08 — Experiment and causal verification

**Owner:** `L3_ACTIONS.md` · **Boundary:** L2 → L3 → L2

**Input records:** `Experiment`, `Prediction`

**Output records:** `ExperimentRun`, `VerificationRecord`

**Supporting records:** `ExperimentDesignSnapshot`

**Legal writer/approver:** L2 owns hypothesis/causal decision; L3 performs authorized experiment and independent observation.

**Acceptance:** frozen design and prediction predate intervention; run/evidence attached to exact design and target.

**Mandatory rejection:** post-hoc prediction substituted; experiment-design state conflated with run outcome; simulated result treated as verified reality.

**Commit/effect boundary:** External experiments remain subject to ActionGate and Action Journal.

**Retry/recovery:** Unknown partial intervention remains unresolved until observation/probe.

**Primary norms:** RDMS-03 experiment vs run; FCA causal hypothesis and evidence gates.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-09 — Contradiction and reality mismatch

**Owner:** `L3_ACTIONS.md` · **Boundary:** L3 → L2

**Input records:** `Claim`

**Output records:** `ContradictionRecord`

**Supporting records:** `OperationalCausalClaim`

**Legal writer/approver:** L2 controls epistemic assessment; L3 sources observations, not causal truth.

**Acceptance:** observations comparable in explicit scope/dimensions with traceable evidence and unresolved/resolved proof.

**Mandatory rejection:** UNRESOLVED silently mapped to RESOLVED; hypothesis dismissed solely due conflicting observation; causal explanation invented.

**Commit/effect boundary:** Contradiction transition needs legal state/sequence and supporting references.

**Retry/recovery:** Keep prior inconsistent evidence and lifecycle history; correction must be attributable.

**Primary norms:** RDMS-03 C01 contradiction and observation rules; FCA epistemic distinctions.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-10 — Freshness and completion

**Owner:** `L4_TEMPORAL_SPECIALISTS.md` · **Boundary:** L4 → L2 → L1

**Input records:** `DependencySet`, `DependencyCaptureReceipt`

**Output records:** `DependencyAttestation`, `IntegratedCompletionEvidence`

**Supporting records:** `CompletionStateBinding`

**Legal writer/approver:** L4 specialist/dependency layer attests freshness; L2 judges completion; L1 adopts legal goal state.

**Acceptance:** dependency coverage and policy/versions attested for exact operation; completion proof matches goal acceptance contract.

**Mandatory rejection:** PARTIALLY_STALE treated as VALID; generic success text treated as task completion; missing dependency frontier.

**Commit/effect boundary:** Completion or focus change requires epoch/version-fenced canonical commit.

**Retry/recovery:** Invalidate derived work on changed dependencies; re-evaluate at admission.

**Primary norms:** FCA §71; RDMS-06 freshness; RDMS-08 completion proof.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-11 — Learning and context egress

**Owner:** `L7_RUNTIME_INTEGRATION.md` · **Boundary:** L3 → L5 → L7

**Input records:** `MemoryProposal`, `SealedOutboundContext`

**Output records:** `LearningAuthorizationBinding`, `ContextDisclosureAdmission`

**Supporting records:** `MemoryRetrievalCoverage`

**Legal writer/approver:** L5 learning policy and L1/CommitGate own durable memory acceptance; L7 only transports sealed outbound content.

**Acceptance:** memory promotion separately authorized; outbound effective bytes/destination/context scope sealed and policy-approved.

**Mandatory rejection:** automatic learning from agent suggestion; sending unapproved private context; destination/payload changed after authorization.

**Commit/effect boundary:** No memory state change without canonical commit; no egress without policy admission.

**Retry/recovery:** After restart, replay only scoped authorization; reject stale outbound binding.

**Primary norms:** RDMS-07 learning; RDMS-10 C01/C02 context disclosure.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.


## X8-12 — Containment and recovery

**Owner:** `L6_RECOVERY.md` · **Boundary:** L3 → L6 → L1

**Input records:** `PossibleExternalEffectAssessment`, `RestoreContainmentProof`

**Output records:** `CrossFrontierAdmissionProof`

**Supporting records:** `RecoveryBootstrapContract`, `RecoveryOwnershipLease`

**Legal writer/approver:** L6 validates containment/uncertain effects; L1 authorizes safe resumption under epoch.

**Acceptance:** isolation claim evidenced, uncertain effects reconciled or explicitly guarded, ownership lease valid.

**Mandatory rejection:** snapshot restore asserted to reverse external world; unverified isolation; old worker keeps authorization.

**Commit/effect boundary:** Canonical recovery commit fences old authority; no global rollback of external effects.

**Retry/recovery:** Reconcile IN_DOUBT before new mutation; persist recovery basis and admission evidence.

**Primary norms:** RDMS-09 C01/C02/C03, RDMS-10 recovery bindings.

**Schema field provenance and unresolved type questions:** `EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json`.
