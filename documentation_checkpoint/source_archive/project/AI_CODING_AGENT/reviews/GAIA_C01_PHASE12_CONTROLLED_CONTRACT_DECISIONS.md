# GAIA-C01 Phase 12 — Controlled Contract Decisions & Layer Consolidation Review

**Document status:** EDITORIAL CONSOLIDATION DECISIONS FOR REVIEW — **NOT A RE-FREEZE**.  
**No production code and no amendments to archived FCA/RDMS sources.**

## Executive decision

The audit adopts a **no-converter-by-default** strategy for the 22 source-owned contracts not in the five priority exceptions. New interfaces should use source-native canonical fields/references. A conversion, legacy migration or transport projection is a separately justified activity with a distinct gate; none of those 22 is hereby declared fully mapped or runtime-verified.

### Two naming collisions — selected editorial names only

- **L2 `CapabilityResult` (FCA §23):** remains canonical. The RDMS-10 transport shape is referred to in *consolidation drafts* as `CapabilityTransportResult`. It MUST include an integrity-bound, scoped, immutable reference to the full FCA semantic result. Original RDMS-10 text is unmodified.
- **L5 `MemoryRetrievalResult` (RDMS-07):** remains canonical. The RDMS-10 projection is referred to in drafts as `MemoryRetrievalTransportResult`. Its shorter snippets and relevance fields cannot assert complete search coverage or replace the legal retrieval record.

These names are chosen for a consistent proposed vocabulary, **not adopted amendments to the previously frozen source documents**. Actual transport schemas, consumers, and full data fidelity still need implementation conformance.

### Three high-risk mappings — conservative treatment

| Contract | Controlled decision | Remaining blocker |
|---|---|---|
| `Commitment` | RDMS-02 canonical semantic record; RDMS-05 temporal aspects use references, never a destructive union | Legacy due/removal/revisit rules and authorized ACTIVE owner may not be inferred; actual preservation/migration proof pending |
| `TriggerCondition` | Differentiate FCA whole Trigger from RDMS-05 full `TriggerDefinition` and its condition/predicate | Complete trigger generation, cursor, two policy axes and causal history cannot be reconstructed from a predicate alone |
| `ResumptionCapsule` | Retain full FCA resumption meaning; compact RDMS-05 C01 metadata must reference an integrity-bound durable payload | Actual atomic suspension and recovery/quarantine proof pending |

**Fail closed:** do not auto-upgrade, erase or guess data to bypass a missing projection.

## Change control / single source of truth

1. **Immutable normative sources:** retain original FCA v1.0.1 and RDMS-01…10 with version/part anchors, content hashes and precedence of approved corrections.
2. **One legal owner:** the owner layer defines the effective canonical type; other layers import/reference it and can publish strictly bounded projections.
3. **Change classes:** `EDITORIAL_LABEL` (no behavioral impact); `PRESENTATION_PROJECTION` (requires full/reference-backed preservation); `SCHEMA_MIGRATION` (needs dual-version migration proof); `SEMANTIC_LAW_CHANGE` (requires formal parent reopening); `RUNTIME_ADAPTER` (implementation conformance).
4. **Review protocol:** proposal → impact & downstream consumers → source precedence audit → field/lifecycle matrix → adversarial tests → explicit approval → publish next layer version, leaving old version archived.
5. **No silent coercions:** cannot map missing evidence, authority, user permission, state, idempotency, causality, timestamps, or recovery references into fabricated defaults.
6. **Freeze scope:** architectural specification closure **does not require running non-existent production code**; implementation conformance is a separate gate. But a core semantic ambiguity cannot be waived merely because its future adapter is not implemented.

## 22 remaining names — source-native reference policy

Only the source-owned canonical definition is eligible for legal publication. All direct-use candidates in the register have status `DIRECT_CANONICAL_USE_SELECTED__PROJECTION_NOT_APPROVED`; this does not declare that other historical fields can be dropped or that a transformed schema is accepted. For each contract, see exact source location, owner, risk group and outstanding field-level proof in `GAIA_C01_PHASE12_27_CONTRACT_DECISIONS.json` and `GAIA_C01_PHASE10_EFFECTIVE_CROSSWALK.md`.

## Final gate

| Gate | Result |
|---|---|
| Exact source archive preservation | PASS (audit check) |
| Named owner for 27/27 reused types | PASS (editorial consolidation choice) |
| Collision aliases selected without modifying parent sources | PASS (draft) |
| Conservative refusal of three unsound historical migrations | PASS (spec-level safety condition) |
| Losslessness of real/legacy converters | PENDING; no real adapters implemented |
| Actual transaction/epoch/disclosure/recovery tests | PENDING at implementation stage |
| Effective unified L0–L7 specification freeze | **NOT YET AUTHORIZED** |

**Next:** final per-layer consolidation/coverage review, distinguish actual unresolved semantic definitions from future implementation proof; then seek an explicit specification freeze decision.
