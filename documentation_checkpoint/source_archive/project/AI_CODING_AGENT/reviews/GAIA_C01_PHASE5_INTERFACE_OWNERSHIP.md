# GAIA-C01 Phase 5 — Proposed Cross-Layer Interface Ownership

> **DISCOVERY AND MIGRATION PROPOSALS ONLY — NOT FROZEN.** Canonical layer documents remain the target; this review index is not a ninth architecture specification.

| Contract / Entity | Canonical owner | Consuming layers / transport mapping | Current status |
|---|---|---|---|
| `CapabilityResult` | L2, FCA §23 | L7 `CapabilityTransportResult` (proposed) | GAIA-B01 OPEN |
| `MemoryRetrievalResult` | L5, RDMS-07 | L7 `MemoryRetrievalTransportResult` (proposed) | GAIA-B03 OPEN |
| `Commitment` | L4 lifecycle with L2 decisions | L2/RDMS-02 C01 and L4/RDMS-05 fields must converge | GAIA-B04 OPEN |
| `TriggerCondition` | L4 | Full trigger vs predicate component split must be explicit | GAIA-B05 OPEN |
| `ResumptionCapsule` | L4 | Compact record + durable payload must preserve FCA recovery context | GAIA-RCAP REVIEW |
| `ActionProposal` / `ActionRecord` | L3, FCA and RDMS-04 | L1 control persistence; L7 delivery projection | Field/enum mapping pending |
| `Observation` / `EvidenceLink` | L3 | L2 interpretations, L7 observation transport | Epistemic mapping pending |
| `DependencyStamp` / `QueryDependencyStamp` | L4, RDMS-06 | L1 persistence, L2/L7 freshness checks | Three-way mapping pending |

Invariants: source authority is not derived from list order; a transport projection is never a canonical entity merely because it has a similar name; C01/C02 repair sets require explicit precedence and verified field preservation.

Evidence: see `GAIA_C01_PHASE5_CONTRACT_RECONCILIATION.md`, `GAIA_C01_PHASE5_CROSS_SOURCE_COMPARISONS.json` and original read-only source sets.
