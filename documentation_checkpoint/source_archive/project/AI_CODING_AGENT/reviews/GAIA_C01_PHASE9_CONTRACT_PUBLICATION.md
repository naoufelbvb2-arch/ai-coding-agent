# GAIA-C01 Phase 9 — Source-Backed Contract Publication

**Result:** 27 original named declarations published verbatim within proposed owning layers; cross-interface gate specified; freeze denied.

| Name | Published source / line | Owning layer | Review class | Publication status |
|---|---|---|---|---|
| `ActionEffectSemantics` | `RDMS-04`:`341` | L3 | CONDITIONAL | verbatim baseline; crosswalk proof pending |
| `ActionProposal` | `RDMS-04`:`97` | L3 | SEMANTIC | verbatim baseline; crosswalk proof pending |
| `ActionRecord` | `RDMS-04`:`208` | L3 | CONDITIONAL | verbatim baseline; crosswalk proof pending |
| `CapabilityResult` | `FCA v1.0.1`:`1012` | L2 | HIGH_PRIORITY | verbatim baseline; crosswalk proof pending |
| `Claim` | `RDMS-02`:`211` | L2 | SEMANTIC | verbatim baseline; crosswalk proof pending |
| `Commitment` | `RDMS-02`:`1380` | L2 | HIGH_PRIORITY | verbatim baseline; crosswalk proof pending |
| `ConfidenceAssessment` | `RDMS-03`:`1412` | L3 | CONDITIONAL | verbatim baseline; crosswalk proof pending |
| `ContradictionRecord` | `RDMS-03`:`632` | L3 | SEMANTIC | verbatim baseline; crosswalk proof pending |
| `Decision` | `RDMS-02`:`855` | L2 | CONDITIONAL | verbatim baseline; crosswalk proof pending |
| `DependencyStamp` | `RDMS-06`:`659` | L4 | CONDITIONAL | verbatim baseline; crosswalk proof pending |
| `EvidenceLink` | `RDMS-03`:`514` | L3 | SEMANTIC | verbatim baseline; crosswalk proof pending |
| `Experiment` | `RDMS-03`:`871` | L3 | SEMANTIC | verbatim baseline; crosswalk proof pending |
| `Goal` | `RDMS-02`:`576` | L2 | LOW_RISK | verbatim baseline; crosswalk proof pending |
| `GoalStack` | `RDMS-02`:`736` | L2 | LOW_RISK | verbatim baseline; crosswalk proof pending |
| `Hypothesis` | `RDMS-02`:`382` | L2 | SEMANTIC | verbatim baseline; crosswalk proof pending |
| `InformationNeed` | `RDMS-02`:`285` | L2 | LOW_RISK | verbatim baseline; crosswalk proof pending |
| `Invariant` | `RDMS-02`:`947` | L2 | CONDITIONAL | verbatim baseline; crosswalk proof pending |
| `MemoryProposal` | `RDMS-07`:`486` | L5 | CONDITIONAL | verbatim baseline; crosswalk proof pending |
| `MemoryRetrievalResult` | `RDMS-07`:`1080` | L5 | HIGH_PRIORITY | verbatim baseline; crosswalk proof pending |
| `Observation` | `RDMS-03`:`82` | L3 | SEMANTIC | verbatim baseline; crosswalk proof pending |
| `OperationalCausalClaim` | `RDMS-02`:`461` | L2 | SEMANTIC | verbatim baseline; crosswalk proof pending |
| `QueryDependencyStamp` | `RDMS-06`:`897` | L4 | LOW_RISK | verbatim baseline; crosswalk proof pending |
| `ResumptionCapsule` | `RDMS-05`:`2067` | L4 | HIGH_PRIORITY | verbatim baseline; crosswalk proof pending |
| `SandboxActivityRecord` | `RDMS-04`:`1124` | L3 | CONDITIONAL | verbatim baseline; crosswalk proof pending |
| `Slice` | `RDMS-02`:`1217` | L2 | CONDITIONAL | verbatim baseline; crosswalk proof pending |
| `TemporalValidity` | `RDMS-05`:`803` | L4 | LOW_RISK | verbatim baseline; crosswalk proof pending |
| `TriggerCondition` | `RDMS-05`:`191` | L4 | HIGH_PRIORITY | verbatim baseline; crosswalk proof pending |

## Four non-negotiable integration constraints

1. **Approved source precedence:** draft schemas are historical; applied corrections and freeze decisions override earlier conflicts. An overlay with `...` is NEVER treated as a complete replacement.
2. **Single owner:** L7 transport envelope may represent, reference or serialize; it may not create a second canonical entity named `CapabilityResult` or `MemoryRetrievalResult`.
3. **No loss:** nested cardinality, state histories, causality, provenance, unresolved work, retry uncertainty and dependency freshness must survive projection.
4. **No premature freeze:** source publication is not an approval of effective schemas, and archive text is not evidence that every conversion is safe.

## Specific blockers still open

- `CapabilityResult`: confirm canonical FCA type vs proposed L7 `CapabilityTransportResult` envelope.
- `MemoryRetrievalResult`: confirm RDMS-07 result vs proposed L7 `MemoryRetrievalTransportResult`.
- `Commitment`: RDMS-02 C01 partial correction is additive; RDMS-05 runtime form has different fields — typed nonloss mapping required.
- `TriggerCondition`: FCA full trigger vs RDMS-05 predicate-level condition must not be silently substituted.
- `ResumptionCapsule`: compact C01 header requires durable immutable payload preserving all FCA required semantics.
- 22 other repeated names: preservation witness and field/identity/authority reverse-projection tests remain outstanding.

## Publication methodology

Each schema excerpt is copied exactly from its frozen-source archive at a verified line anchor. Where the original owner uses a later partial correction, the later overlay remains separately traceable. All source files are preserved as historical records.

