# GAIA-C04 — Twelve Interface Source-Schema Witnesses

**Not formal RPC signatures.** Only literal brace-delimited structs from archived messages are indexed. `NO_EXACT_BRACE_SCHEMA_FOUND` means the exact spelling did not appear as an extracted braced definition; the contract may be expressed in prose, FCA, or another name. It is NOT proof that a source lacks the information.


## X8-01

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `CapabilityResult` | EXACT_STRUCT_FOUND | RDMS-10 Original draft, `99533762`:372–390 |
| `CapabilityTransportResult` | NO_EXACT_BRACE_SCHEMA_FOUND | — |
| `CapabilityInvocation` | EXACT_STRUCT_FOUND | RDMS-10 Original draft, `99533762`:355–371 |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-02

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `MemoryRetrievalResult` | EXACT_STRUCT_FOUND | RDMS-07 Original draft, `938c1bc7`:1068–1084; RDMS-10 Original draft, `99533762`:1136–1146 |
| `MemoryRetrievalTransportResult` | NO_EXACT_BRACE_SCHEMA_FOUND | — |
| `MemoryRetrievalRequest` | EXACT_STRUCT_FOUND | RDMS-10 Original draft, `99533762`:1123–1135 |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-03

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `Commitment` | EXACT_STRUCT_FOUND | RDMS-02 Original draft, `a62cc59d`:1368–1396; RDMS-02 C01, second review corrections and final freeze decision, `266bb347`:918–931; RDMS-05 Original draft, `6276f296`:514–535 |
| `CanonicalEntityMeta` | EXACT_STRUCT_FOUND | RDMS-02 C01, second review corrections and final freeze decision, `266bb347`:21–33 |
| `ReactivationCondition` | NO_EXACT_BRACE_SCHEMA_FOUND | — |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-04

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `TriggerDefinition` | EXACT_STRUCT_FOUND | RDMS-05 Original draft, `6276f296`:149–174 |
| `TriggerCondition` | EXACT_STRUCT_FOUND | RDMS-05 Original draft, `6276f296`:179–197 |
| `TriggerFire` | EXACT_STRUCT_FOUND | RDMS-05 Original draft, `6276f296`:439–454; RDMS-05 C01, `77caba5f`:345–357 |
| `TriggerEvaluation` | EXACT_STRUCT_FOUND | RDMS-05 Original draft, `6276f296`:204–222 |
| `ReactionExecutionRecord` | NO_EXACT_BRACE_SCHEMA_FOUND | — |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-05

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `ResumptionCapsule` | EXACT_STRUCT_FOUND | RDMS-05 Original draft, `6276f296`:642–678; RDMS-05 C01, `77caba5f`:720–741 |
| `SuspensionRecord` | NO_EXACT_BRACE_SCHEMA_FOUND | — |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-06

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `ActionProposal` | EXACT_STRUCT_FOUND | RDMS-04 Original draft, `32ad532a`:85–137 |
| `ActionRecord` | EXACT_STRUCT_FOUND | RDMS-04 Original draft, `32ad532a`:196–221 |
| `ActionAttempt` | EXACT_STRUCT_FOUND | RDMS-04 Original draft, `32ad532a`:258–288 |
| `ControlCommit` | EXACT_STRUCT_FOUND | RDMS-01 Original draft, `2aacdc73`:109–131; RDMS-01 R1 corrections and final freeze decision, `e3a45231`:138–161 |
| `SealedExecutionIntent` | EXACT_STRUCT_FOUND | RDMS-10 C01, `e4828797`:748–774 |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-07

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `Observation` | EXACT_STRUCT_FOUND | RDMS-03 Original draft, `11d811dc`:70–96 |
| `EvidenceLink` | EXACT_STRUCT_FOUND | RDMS-03 Original draft, `11d811dc`:449–480; RDMS-03 Original draft, `11d811dc`:502–505 |
| `SupportAssessment` | EXACT_STRUCT_FOUND | RDMS-02 C01, second review corrections and final freeze decision, `266bb347`:43–63 |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-08

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `Experiment` | EXACT_STRUCT_FOUND | RDMS-03 Original draft, `11d811dc`:859–891 |
| `ExperimentRun` | EXACT_STRUCT_FOUND | RDMS-03 Original draft, `11d811dc`:918–943 |
| `Hypothesis` | EXACT_STRUCT_FOUND | RDMS-02 Original draft, `a62cc59d`:370–404; RDMS-02 C01, second review corrections and final freeze decision, `266bb347`:193–205 |
| `CausalVerificationRecord` | EXACT_STRUCT_FOUND | RDMS-02 Original draft, `a62cc59d`:503–517 |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-09

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `ContradictionRecord` | EXACT_STRUCT_FOUND | RDMS-03 Original draft, `11d811dc`:620–645; RDMS-03 C01 and Freeze Review 02 Final, `a1ca0249`:468–473 |
| `ObservationComparison` | NO_EXACT_BRACE_SCHEMA_FOUND | — |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-10

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `DependencyStamp` | EXACT_STRUCT_FOUND | RDMS-01 Original draft, `2aacdc73`:782–795; RDMS-06 Original draft, `4bcbb2bf`:647–671 |
| `TemporalValidity` | EXACT_STRUCT_FOUND | RDMS-05 Original draft, `6276f296`:791–804 |
| `QueryDependencyStamp` | EXACT_STRUCT_FOUND | RDMS-06 Original draft, `4bcbb2bf`:885–910 |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-11

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `MemoryProposal` | EXACT_STRUCT_FOUND | RDMS-07 Original draft, `938c1bc7`:474–500 |
| `OutboundContextDisclosure` | NO_EXACT_BRACE_SCHEMA_FOUND | — |
| `ContentEnvelope` | NO_EXACT_BRACE_SCHEMA_FOUND | — |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.

## X8-12

| Expected witness | Extraction status | Located sources |
|---|---|---|
| `SandboxActivityRecord` | EXACT_STRUCT_FOUND | RDMS-04 Original draft, `32ad532a`:1112–1133 |
| `ActionAttempt` | EXACT_STRUCT_FOUND | RDMS-04 Original draft, `32ad532a`:258–288 |
| `RecoverySession` | NO_EXACT_BRACE_SCHEMA_FOUND | — |

**Gate:** producer/consumer required fields, durable transaction, idempotency, epoch fencing, error and reconciliation semantics need source-level proof before contract-freeze.