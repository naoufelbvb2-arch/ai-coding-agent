# GAIA-C01 — Phase 4 Source Admission & Baseline Reconciliation

**State:** SOURCE GAP CLOSED (original user-provided message sets admitted); CANONICAL LAYER CONSOLIDATION NOT FROZEN.

## Provenance result

- User-supplied ZIP: `RDMS-01_to_RDMS-10_Original_Approved_Sources.zip`.
- ZIP SHA-256: `6b68364b4d804e92346ac50335c4a9d57765040039eef48fc09bb6f4460226d9`.
- Archive contains exactly 10 RDMS original source-set TXT files, a README, a SOURCE_MANIFEST, and `original_message_dom.json`.
- All **27 of 27** original message texts were individually extracted and validated against the provided SHA-256 manifest (using the source-extraction whitespace boundary convention). The associated part names and message IDs were preserved.
- Ten source sets include their correction and final freeze-decision records. Historical DRAFT messages do not override their later corrective/final records.
- This is **internal source-package integrity** and provenance supplied by the user; it does not independently revalidate the public share URL.

## Source custody and primary layer annexes

| Set | Message parts | Source-set SHA-256 (prefix) | Verbatim annex |
|---|---:|---|---|
| RDMS-01 | 2 | `b5b023dff0003f456d…` | L1_CONTROL.md |
| RDMS-02 | 2 | `54772a75a54baea03c…` | L2_COGNITION.md |
| RDMS-03 | 2 | `97f836c691a373b9a2…` | L3_ACTIONS.md |
| RDMS-04 | 3 | `c06407aad889cad4d0…` | L3_ACTIONS.md |
| RDMS-05 | 3 | `9152f6eb671ce1c952…` | L4_TEMPORAL_SPECIALISTS.md |
| RDMS-06 | 2 | `a55748e558446497a4…` | L4_TEMPORAL_SPECIALISTS.md |
| RDMS-07 | 2 | `fe065cda37c20625ac…` | L5_MEMORY.md |
| RDMS-08 | 2 | `fff70116d3f26bd42c…` | L2_COGNITION.md |
| RDMS-09 | 5 | `84ed1246a86b6f5923…` | L6_RECOVERY.md |
| RDMS-10 | 4 | `5464a1a1db1a64d909…` | L7_RUNTIME_INTEGRATION.md |

The raw source files and original HTML/DOM export remain unchanged in `reviews/source_archive/RDMS_ORIGINAL_SOURCES/`. The complete TXT source sets are additionally copied as plainly labeled **historical verbatim annexes** into their primary owner layer file, avoiding duplicate definitions in multiple layer files. An annex is not a clean canonical merged specification until corrections, supersessions, and type ownership are normalized and reviewed.

## Schema-name discovery

The initial lexical scan found **454** brace-block declaration occurrences and **27** type names repeated across distinct FCA/RDMS source documents. A repeated name is **not automatically a defect**: RDMS documents frequently refine frozen parent entity definitions. Each candidate requires semantic comparison with the final corrections.

`CapabilityResult` in FCA §23 versus RDMS-10 remains **GAIA-B01**, a verified distinct-shape collision that must be resolved through documented owner/projection naming; see existing collision report. Other candidate names must not be labeled actual contradictions without proof.

| Candidate | Sources | Distinct declaration-body forms |
|---|---|---:|
| `ActionEffectSemantics` | FCA v1.0.1, RDMS-04 | 2 |
| `ActionProposal` | FCA v1.0.1, RDMS-04 | 2 |
| `ActionRecord` | FCA v1.0.1, RDMS-04 | 2 |
| `CapabilityResult` | FCA v1.0.1, RDMS-10 | 2 |
| `Claim` | FCA v1.0.1, RDMS-02 | 3 |
| `Commitment` | RDMS-02, RDMS-05 | 3 |
| `ConfidenceAssessment` | FCA v1.0.1, RDMS-03 | 2 |
| `ContradictionRecord` | FCA v1.0.1, RDMS-03 | 3 |
| `Decision` | FCA v1.0.1, RDMS-02 | 2 |
| `DependencyStamp` | FCA v1.0.1, RDMS-01, RDMS-06 | 3 |
| `EvidenceLink` | FCA v1.0.1, RDMS-03 | 3 |
| `Experiment` | FCA v1.0.1, RDMS-03 | 2 |
| `Goal` | FCA v1.0.1, RDMS-02 | 2 |
| `GoalStack` | FCA v1.0.1, RDMS-02 | 2 |
| `Hypothesis` | FCA v1.0.1, RDMS-02 | 3 |
| `InformationNeed` | FCA v1.0.1, RDMS-02 | 2 |
| `Invariant` | FCA v1.0.1, RDMS-02 | 2 |
| `MemoryProposal` | FCA v1.0.1, RDMS-07 | 2 |
| `MemoryRetrievalResult` | RDMS-07, RDMS-10 | 2 |
| `Observation` | FCA v1.0.1, RDMS-03 | 2 |
| `OperationalCausalClaim` | FCA v1.0.1, RDMS-02 | 2 |
| `QueryDependencyStamp` | FCA v1.0.1, RDMS-06 | 2 |
| `ResumptionCapsule` | FCA v1.0.1, RDMS-05 | 3 |
| `SandboxActivityRecord` | FCA v1.0.1, RDMS-04 | 2 |
| `Slice` | FCA v1.0.1, RDMS-02 | 2 |
| `TemporalValidity` | FCA v1.0.1, RDMS-05 | 2 |
| `TriggerCondition` | FCA v1.0.1, RDMS-05 | 2 |

## GAIA status after arrival

- **GAIA-B02 source availability:** CLOSED. All 10 original source sets are in the archive, with 27/27 per-message manifest integrity checks.
- **GAIA-B01 type collision:** OPEN. Correction still requires formal consolidation/compatibility review.
- **New schema-name review queue:** 27 cross-source repeated names (including GAIA-B01), none automatically a blocker except independently substantiated conflicts.
- **Field-by-field canonical effective contract reconciliation:** PENDING. This requires applying corrective/freeze precedence within every source set.
- **FCA original:** unchanged, previously verified; its 88 numbered sections and seven appendices remain in existing layer annexes.
- **All L0…L7 layer docs:** still CONSOLIDATION DRAFT, not independently FROZEN.
- **Implementation:** NOT AUTHORIZED.

## Next bounded step

**GAIA-C01 Phase 5 — Canonical Effective Contract Reconciliation.** For each owned type, compare FCA schema, original RDMS draft, later corrections, and RDMS-10 transport projections. Produce an effective field list, ownership decision, and exact source pointers. Only after the review passes should historical annexes be restructured into a clean, singular normative specification per layer.
