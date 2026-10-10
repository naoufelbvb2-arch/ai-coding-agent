# Architecture manifest

**Current status: source-backed documentation consolidation for independent review; NOT FROZEN. Full normative acceptance is HOLD.**

The approved checkpoint is preserved at 397c9a5b8878ba5d5a8d8ab93a3e175146022f8d. The user subsequently approved source admission and L0–L7 ownership with the clarifications recorded in [AUTHORIZATION.md](../reviews/canonical/AUTHORIZATION.md). This approval authorizes documentation consolidation/publication only.

| Layer | Authoritative coverage and applied amendments | Completion status | Open contract questions |
|---|---|---|---|
| [L0](L0_FOUNDATION.md) | FCA v1.0.1 foundation, authority/trust, Appendices C/F/G | Foundation responsibilities verified; owner imports remain governed by their own acceptance | 0 |
| [L1](L1_CONTROL.md) | FCA 48–51; RDMS-01 original + R1 and final freeze | Current source scopes consolidated; full field/semantic acceptance remains OPEN | 2 |
| [L2](L2_COGNITION.md) | FCA cognition; RDMS-02 original + C01/final; RDMS-08 original + C01/final | Current source scopes consolidated; full field/semantic acceptance remains OPEN | 12 |
| [L3](L3_ACTIONS.md) | FCA action/evidence; RDMS-03 original + C01/final; RDMS-04 original + C01 + Review 02 | Current source scopes consolidated; full field/semantic acceptance remains OPEN | 12 |
| [L4](L4_TEMPORAL_SPECIALISTS.md) | FCA temporal/specialists; RDMS-05 original + C01 + FC05-01/02; RDMS-06 original + C01/final | Current source scopes consolidated; full field/semantic acceptance remains OPEN | 8 |
| [L5](L5_MEMORY.md) | FCA memory; RDMS-07 original + C01/final | Current source scopes consolidated; full field/semantic acceptance remains OPEN | 1 |
| [L6](L6_RECOVERY.md) | FCA 52/53/82; RDMS-05 capsule/resume scopes; RDMS-09 original + C01 + C02 + C03 + FC09-04-01…04 | Current source scopes consolidated; full field/semantic acceptance remains OPEN | 3 |
| [L7](L7_RUNTIME_INTEGRATION.md) | FCA 85; RDMS-10 original + C01 + C02 + FC10-03-01…08 | Current source scopes consolidated; full field/semantic acceptance remains OPEN | 2 |

## Effective authority and ownership

L0 owns architectural foundation. Its cross-cutting law applies across all layers, while each layer owns its specific canonical responsibilities and record contracts. L1 owns control persistence and legal replay; L2 owns cognition and Executive semantic authorization; L3 owns actions, observations and evidence; L4 owns temporal evaluation, triggers, specialists, reactivation scheduling and the one dependency engine; L5 owns memory and learning; L6 owns recovery authority/state and suspension/resumption integrity; L7 owns integration/transport.

ResumptionCapsule and ResumeAssessment have exactly one owner, L6. L4 imports them for scheduling and temporal coordination. Commitment belongs to L2; L4 owns its referenced condition semantics. RDMS-05’s earlier competing Commitment declaration is withdrawn under C01-01, rather than promoted into another canonical entity. L7 can neither mint cognitive authority, commit authority nor external-action permission.

Canonical CapabilityResult is L2-owned; canonical MemoryRetrievalResult is L5-owned. CapabilityTransportResult and MemoryRetrievalTransportResult identify L7 transport envelopes whose archived RDMS-10 spelling is retained in provenance. These editorial distinctions do not ratify field conversion or authorize lost payload.

The [contract registry](../reviews/canonical/CANONICAL_CONTRACT_REGISTRY.json) records 402 source record labels, including superseded declarations, partial specimens and transport aliases. That count is not a claim of 402 complete canonical APIs. Every current label has one assigned owner; unresolved complete shapes are withheld from the accepted contract surface.

## Source integrity and precedence

All 195 archive files retain their checkpoint SHA-256, including the outer ZIP, nested packaging, originals, message export and historical GAIA artifacts. Read-only attributes and integrity verification provide custody evidence; they are not WORM storage. [Original-source manifest](../documentation_checkpoint/SOURCE_MANIFEST.json) and [message admission manifest](../documentation_checkpoint/SOURCE_UNITS.json) preserve exact file/message hashes.

FCA v1.0.1 supersedes FCA v1.0 and its admitted draft correction history. For each RDMS, the final source freeze admits the original plus approved corrections. A correction replaces only its stated scope. Later hardening supplements unaffected earlier duties. Final FC05, FC09 and FC10 interpretations are binding within those sources. GAIA reconciliations remain supporting evidence and introduce no law.

File SHA-256 uses exact archived bytes. Catalogue/unit hashes use UTF-8 clause text with LF line boundaries, excluding an appended synthetic final newline; they are not substituted for raw-file hashes.

## Verification evidence and acceptance limits

Coverage indexes 27 complete source messages, all 88 FCA numbered sections, 50 invariants and 7 appendices. The disposition ledger accounts for 2628 source scope units; 0 are unclassified residual scopes. A classified/cited scope is traceability evidence, not automatic sentence-level semantic proof.

All twelve interface paths have owner/type, authority/transition, durability, failure/retry/recovery and rejection evidence. [Interface review](../reviews/canonical/INTERFACE_VALIDATION.md) and its JSON retain source fields and exact locators. None is declared fully accepted while owner-field/projection questions remain. Unspecified callable signatures are left unspecified.

The [issues register](../reviews/canonical/UNRESOLVED_ISSUES.md) contains 40 questions: 13 incomplete/differing record shapes, parent/projection conformance obligations, canonical-event envelope interpretation, changed hypothesis support-floor correspondence and two transport payload mappings. Exact conflicting/candidate clauses, field sets, line ranges, source hashes and consequences are preserved. Questions are bounded; independently verified laws remain effective.

The [verification record](../reviews/canonical/VERIFICATION.md) separates mechanical PASS from semantic/field acceptance OPEN. [Clause trace](../reviews/canonical/CLAUSE_TRACEABILITY.json) and [source dispositions](../reviews/canonical/SOURCE_COVERAGE.json) provide bidirectional review evidence. No production code, new law, redesign, merge into main or new freeze is authorized.

## Reproduction

Run python tools/build_documents.py to regenerate documentation and evidence from the preserved originals. Run python tools/verify_consolidation.py for current checks. The older checkpoint verifier intentionally verifies Stage A only and must not be used as a current full-consolidation gate.

Git publication is restricted to docs/canonical-source-checkpoint. [Completion report](../reviews/canonical/COMPLETION_REPORT.md) records layer commits and publication evidence.
