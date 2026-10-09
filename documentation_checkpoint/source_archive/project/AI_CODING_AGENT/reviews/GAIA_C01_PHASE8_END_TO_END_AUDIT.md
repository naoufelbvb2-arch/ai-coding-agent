# GAIA-C01 Phase 8 — End-to-End Integration Path Audit

**Scope:** architecture-level causal and authority conservation. Paths are proposed audit witnesses; no code has been executed.

| ID | Layer path | Scenario | Legal path | Threat | Required protection | Related contracts |
|---|---|---|---|---|---|---|
| `X8-01` | `L2 → L7 → L2` | Capability invocations | FCA CapabilityResult → L7 CapabilityTransportResult → Executive Decision | Missing specialist_request or rationale; transport SUCCESS treated as accepted decision | Canonical ref required, semantically reversible, no direct commit | P6-01; GAIA-B01 |
| `X8-02` | `L5 → L7 → L2` | Memory retrieval | RDMS-07 MemoryRetrievalResult → L7 bounded projection → cognition | Partial retrieval presented as exhaustive/no-memory evidence | Preserve omitted scope/ranking/coverage/freshness by legal ref | P6-02 |
| `X8-03` | `L2 → L4 → L1` | Temporary obligations | RDMS-02 Commitment → RDMS-05 temporal condition → ControlCommit | Missing owner/root; statement collapsed to required_followup; due falsely SATISFIED | One legal Commitment, explicit reactivation root, atomic continuation | P6-03 |
| `X8-04` | `L4 → L1 → L3` | Trigger to action | TriggerDefinition → committed Reaction → durable continuation → ActionProposal | EDGE event replay duplicates world effect or loses derived follow-up | Stable trigger generation/reaction identity + ActionGate | P6-04; R2-G04 |
| `X8-05` | `L4 → L6 → L1` | Suspension/resumption | ResumptionCapsule payload verified → atomic SUSPENDED → Recovery → Executive | Compact capsule drops hypotheses, evidence or next cognitive step | Pinned durable payload; corrupt means recovery quarantine | P6-05 |
| `X8-06` | `L2 → L3 → L1` | Code/world change | ActionProposal → ActionGate → ActionRecord → Reality Executor | FILESYSTEM category hides file_delete; latest_attempt_ref hides uncertain prior effect | Sealed exact operation + recoverable attempt history + journal | P7-02; P7-03 |
| `X8-07` | `L3 → L2 → L1` | Observation to belief | Observation → EvidenceLink → Claim/ConfidenceAssessment → CommitGate | Two observations double-counted; forged success becomes verified FACT | Accepted evidence with source cardinality and FactGrounding; no raw report authority | P7-04; P7-09; P7-17 |
| `X8-08` | `L2 → L3 → L2` | Experiment and causality | Hypothesis → predictions → Experiment design → ExperimentRun → OVC | RUNNING conflated with DESIGNED or hypothesis strength treated as causal closure | Persisted preintervention prediction; verification matrix + separate design/run states | P7-10; P7-13; P7-18 |
| `X8-09` | `L3 → L2` | Contradictory reality | Raw observation pair → comparability → ContradictionRecord → InformationNeed | UNRESOLVED silently maps to RESOLVED; causal explanation invented | Nonterminal unresolved remains, explanation separate from comparison | P7-06; P7-14 |
| `X8-10` | `L4 → L2 → L1` | Freshness and finalization | DependencyStamp → current checks → Decision/Slice → finalization | Stale dependencies masked or rejected rationale lost | RDMS-06 single freshness owner; preserve scope and finalization evidence | P7-07; P7-08; P7-21 |
| `X8-11` | `L3 → L5 → L7` | Learning and egress | Observation/Evidence → MemoryProposal → LearningGate → Provider Context | Proposal silently promoted; sensitive derivative disclosed on fallback | No auto learning; sealed outbound context and lineage | P7-16 |
| `X8-12` | `L3 → L6 → L1` | Sandbox and recovery | SandboxActivityRecord → artifact publication → legal recovery | Unproven isolation mistaken for ephemeral; result state lost | Containment proof; world effects default SHARED_WORLD if uncertain | P7-20 |

## Cross-path certification requirements

- Ownership: no path duplicates persistent state authority or grants a worker/transport new authority.
- Atomicity: legal state transitions and durable continuation obligations survive relevant crash windows.
- Effect isolation: attempt, reported result, observation and verified effect remain separate.
- Epistemic integrity: source identity, comparability, provenance, confidence and causal closure retain their legal distinctions.
- Temporal validity: trigger replay/edge detection and stale dependencies do not silently reactivate old plans.
- Policy enforcement: provider egress and shared-worker delegated scope rechecked at final enforceable boundaries.
- End-to-end paths are review specifications, not runtime results; scope beyond 27 repeated type names remains to audit.

