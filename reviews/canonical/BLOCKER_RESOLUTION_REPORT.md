# Targeted normative blocker resolution report

Repository: naoufelbvb2-arch/ai-coding-agent. Branch: `docs/canonical-source-checkpoint`. Reviewed baseline: `d50b7f88105b5397aa7d76e0bb8a1c2099a7c85e`.

**Freeze readiness: HOLD. NOT FROZEN.** The existing consolidated layer documents remain the working baseline; only targeted owner contracts, dispositions and related review evidence changed. No new architectural decision was adopted.

Original unresolved questions: **40**. Exactly one final classification is assigned to each question.

| Class | Meaning | Count | Final disposition |
|---|---|---|---|
| A | NORMATIVE_CONFLICT | 0 | No mutually impossible effective pair established |
| B | LOSSLESS_MAPPING_REQUIRED | 25 | Preservation proof still OPEN |
| C | IMPLEMENTATION_DETAIL_DEFERRED | 6 | Deferred to Implementation Design with binding obligations |
| D | ALREADY_RESOLVED | 8 | Source-determined resolution / existing owner elaboration proven |
| E | EXPLICIT_ARCHITECTURAL_DECISION_REQUIRED | 1 | Architecture review approval required; no decision selected |

**Total: 40.** Eight questions are resolved/proven (three current-record corrections and five already effective elaborations); six representation details are safely deferred; 26 questions remain open (25 mapping proofs and one required decision). Zero A is not a claim that the B/E requirements are optional.

## Proven corrections and closures

- Current record corrections: SHAPE-Risk, SHAPE-ContainmentProof, SHAPE-TriggerFire.
- Existing source determinations proven: PARENT-Goal, PARENT-InformationNeed, PARENT-Invariant, PARENT-MemoryProposal, PARENT-TemporalValidity.
- Implementation Design deferrals: SHAPE-CanonicalStateView, SHAPE-State, SHAPE-ProjectRuntime, SHAPE-EvidenceLink, SHAPE-ToolResult, SHAPE-TriggerSourceCursor.

Every question retains its original candidates, exact authoritative clauses, hashes, classification reason, mandatory obligations and remaining detail in [the classification register](BLOCKER_CLASSIFICATION.md) and [JSON](BLOCKER_CLASSIFICATION.json). The [eight preservation proofs](SOURCE_DETERMINATE_PROOFS.md) explain why class D closes the normative question. Deferral concerns only the stated layout/encoding/view detail; required information, identity, authority, lifecycle, durability and recovery remain binding.

## Remaining legal-information gaps and required decision

The 25 class B questions are source-compatible representation/preservation questions, not automatically contradictory laws or approval requests for new laws. Specific missing proofs include action risk/world/authority/history information, inline-spec/reference content and versions, parent evidence/decision fields, complete capsule context and resume action coverage, schedule instants/bounds, reaction keys/kinds, canonical-event metadata scope and both transport payloads. They remain acceptance gaps; no serializer alias or lossy projection is invented.

**HG-01 requires an approved architectural decision.** RDMS-02 original §15 uses the old support combinations for CONFIRMED/REJECTED. C01-02 replaces scalar support with a different immutable SupportAssessment vocabulary; C01-07 and RDMS-03 C01-42 settle the separate OVC closure path. The missing ordinary hypothesis admission correspondence cannot be chosen by a serialization library.

Smallest decision: ratify the post-C01 SupportAssessment predicates for ordinary CONFIRMED/REJECTED, including assessment validity and whether VERIFIED satisfies the earlier STRONG minimum. Available resolution approaches are a minimal shared-level admission rule or a complete legacy-to-assessment correspondence. Both must retain the original support-floor obligations and the independent causal gate; neither is adopted. The register includes exact missing/conflicting scopes and consequences. Affected layers: L2, L3, L1; interfaces X8-07/X8-08.

## Layer and interface impact

| Layer | Open proof / decision questions |
|---|---|
| L0 | 0 |
| L1 | 1 |
| L2 | 6 |
| L3 | 9 |
| L4 | 5 |
| L5 | 0 |
| L6 | 3 |
| L7 | 2 |

L0 is unchanged. L1–L7 contain only their own targeted reconciliation articles and affected contract-section edits. No unrelated current normative article or owner contract changed; the focused checker compares them with the reviewed Git baseline.

All twelve interface paths were rechecked against their existing source-backed authority/transition, durability/atomicity, failure/retry/recovery and rejection constraints. Those constraints remain unchanged. Resolved source contracts and deferred layout details are distinguished from the specific B/E blockers in [the interface review](INTERFACE_VALIDATION.md). **All twelve still have full field/preservation acceptance OPEN.** No runtime conformance claim is made.

## Verification

- Existing consolidation verifier: PASS. Original archive files: 195; source units: 2628; source-backed articles: 1655; single-owner current definitions: 388.
- Focused blocker regression verifier: PASS; 935 checks, 0 failures.
- Checks include all 40 original questions/candidates preserved, exact evidence clause/hash equality, only permitted owner edits, exact amended fields, unaffected Risk field bodies/optionality, retained Goal/Need/Invariant values, source-native MemoryProposal, capitalization-only TemporalValidity, unresolved HG/metadata gates and all 12 unchanged legal interface constraints.
- Source catalogue, all 27 authoritative messages, FCA sections/invariants and amendment sources retain their original custody; archive bytes are unchanged. Verification hashes in VERIFICATION.json describe the current documents; LAYER_COMMITS.json retains historical baseline hashes.
- No production code or executable runtime tests. Mechanical/source regression PASS does not certify complete field mapping, backend durability, operational authorization or architecture freeze.

Commands: `python tools/verify_consolidation.py` and `python tools/verify_blocker_resolution.py`. Full regeneration is disabled after targeted reconciliation. [Detailed regression evidence](BLOCKER_REGRESSION_RESULTS.json); [current verification evidence](VERIFICATION.json).

## Focused commits

| Commit SHA | Change |
|---|---|
| `e7a0b81ad0fedcdef683855476f159b02593de42` | docs(L3): bind approved containment and retain action contract obligations |
| `5cc4d34df8f59fe5a8568c2169f939b6e7d6947e` | docs(L1): clarify mandatory event metadata and deferred runtime embedding |
| `33eb2bddc66d5830fd39d78ba72e7022b64f044a` | docs(L6): delimit capsule context and resume preservation proofs |
| `d57918afd5d8453d20f658696cb8b49216c76488` | docs(L4): bind stable fires and classify temporal contract questions |
| `c2c9c1c317b71455c07194be4157152b5ade8011` | docs(L2): apply scoped Risk amendment and delimit admission blockers |
| `45db6bb0df354395bce57b28905331a044858198` | docs(L5): prove source-owned MemoryProposal preservation |
| `c6d0cf74cddc95d121400265ba81e328836f03b2` | docs(L7): retain canonical payload requirements across transport projections |

[TARGETED_COMMITS.json](TARGETED_COMMITS.json) lists exact files for the recorded focused commits. The final evidence/publication commit cannot record its own SHA without changing that SHA; the exact final remote/local SHA is supplied in the accompanying completion response and local Git publication receipt.

## Exact modified files

- `README.md`
- `architecture/ARCHITECTURE_MANIFEST.md`
- `architecture/L1_CONTROL.md`
- `architecture/L2_COGNITION.md`
- `architecture/L3_ACTIONS.md`
- `architecture/L4_TEMPORAL_SPECIALISTS.md`
- `architecture/L5_MEMORY.md`
- `architecture/L6_RECOVERY.md`
- `architecture/L7_RUNTIME_INTEGRATION.md`
- `reviews/canonical/BLOCKER_CLASSIFICATION.json`
- `reviews/canonical/BLOCKER_CLASSIFICATION.md`
- `reviews/canonical/BLOCKER_REGRESSION_RESULTS.json`
- `reviews/canonical/BLOCKER_RESOLUTION_AUTHORIZATION.md`
- `reviews/canonical/BLOCKER_RESOLUTION_REPORT.md`
- `reviews/canonical/BLOCKER_RESOLUTION_SUMMARY.json`
- `reviews/canonical/CANONICAL_CONTRACT_REGISTRY.json`
- `reviews/canonical/CLAUSE_TRACEABILITY.json`
- `reviews/canonical/COMPLETION_REPORT.md`
- `reviews/canonical/COVERAGE_SUMMARY.json`
- `reviews/canonical/INTERFACE_VALIDATION.json`
- `reviews/canonical/INTERFACE_VALIDATION.md`
- `reviews/canonical/SOURCE_COVERAGE.json`
- `reviews/canonical/SOURCE_DETERMINATE_PROOFS.md`
- `reviews/canonical/TARGETED_BASELINE_HASHES.json`
- `reviews/canonical/TARGETED_COMMITS.json`
- `reviews/canonical/UNRESOLVED_ISSUES.json`
- `reviews/canonical/UNRESOLVED_ISSUES.md`
- `reviews/canonical/VERIFICATION.json`
- `reviews/canonical/VERIFICATION.md`
- `tools/blocker_findings.py`
- `tools/blocker_resolution_report.py`
- `tools/build_documents.py`
- `tools/reconcile_blockers.py`
- `tools/schema_selection.py`
- `tools/targeted_interface_review.py`
- `tools/verify_blocker_resolution.py`
- `tools/verify_consolidation.py`

## Publication boundary

Publish only to `refs/heads/docs/canonical-source-checkpoint`, preserving the reviewed baseline and source checkpoint history. Verify remote/local head equality and a clean tree after the push. No merge into main, history rewrite, source edit, production implementation, new law or FROZEN declaration is authorized. Publication equality is confirmed by the final response/receipt rather than inferred from this pre-publication report.
