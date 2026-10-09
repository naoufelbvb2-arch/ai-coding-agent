# AI Coding Agent — Canonical Architecture Consolidation

You are acting as a senior software architect, specification engineer, and technical documentation integrator.

## Objective

Transform the supplied AI Coding Agent ZIP archive into a clean, source-traceable, canonical architecture documentation repository.

The goal is **not to redesign the architecture**. It is to consolidate existing approved and frozen specifications into eight coherent, implementation-ready layer documents.

## Authoritative sources

Identify and inspect:

- FCA v1.0.1 FROZEN.
- RDMS-01 through RDMS-09, including all approved corrections and freeze decisions.
- RDMS-10, including C01, C02, and final freeze reviews.
- Subsequent GAIA reconciliation artifacts as supporting evidence, not as automatic replacements for original frozen sources.

Do not assume that the latest generated GAIA document is necessarily legally authoritative. Verify every effective definition against the original approved source and its explicit corrections.

## Non-negotiable rules

1. Do not invent new cognitive mechanisms, authority structures, fields, state transitions, or architectural laws.
2. Do not silently alter frozen specifications.
3. Preserve all original sources in an immutable archival directory and record their SHA-256 hashes.
4. Apply approved corrections only within their authorized scope.
5. A later approved correction supersedes an earlier clause only where it explicitly modifies that clause.
6. A historical draft must not appear as current normative law when superseded.
7. Each canonical contract must have exactly one owning layer.
8. Cross-layer references must not create duplicate legal ownership.
9. If a contradiction cannot be resolved from authoritative sources, record the precise conflicting clauses and stop short of inventing a resolution.
10. Do not write production implementation code.

## Target architecture documents

Create or consolidate:

- `architecture/L0_FOUNDATION.md`
- `architecture/L1_CONTROL.md`
- `architecture/L2_COGNITION.md`
- `architecture/L3_ACTIONS.md`
- `architecture/L4_TEMPORAL_SPECIALISTS.md`
- `architecture/L5_MEMORY.md`
- `architecture/L6_RECOVERY.md`
- `architecture/L7_RUNTIME_INTEGRATION.md`
- `architecture/ARCHITECTURE_MANIFEST.md`

Each layer document must be self-contained regarding its own normative responsibilities and imported interfaces.

## Required workflow

### Stage A — Source discovery

Inspect the complete archive recursively.

Classify documents as:

- Frozen authoritative source
- Approved amendment or correction
- Freeze decision
- Historical draft
- Previous integration attempt
- Supporting verification evidence

Create a source manifest containing origin, version, authority status, and checksum.

Do not modify canonical architecture documents before completing this inventory.

### Stage B — Effective law consolidation

For each layer, construct the current effective specification by combining the original authoritative rules with all applicable approved amendments.

Remove superseded statements from the normative body, but preserve them in the historical archive.

Ensure that every normative rule has traceability to its authoritative source.

Do not simply concatenate original drafts and correction documents.

### Stage C — Cross-layer contract validation

Validate all twelve previously identified interface paths.

For each interface establish, from the authoritative sources:

- Owning layer and participating layers
- Input and output types
- Required fields and legal constraints
- Authorization and state-transition authority
- Atomicity and durability boundaries
- Failure, retry, and recovery behavior
- Explicit rejection conditions
- Source references and amendment precedence

Do not fabricate unspecified interface signatures.

Preserve the distinction between canonical types and transport envelopes, including `CapabilityResult`, `CapabilityTransportResult`, `MemoryRetrievalResult`, and `MemoryRetrievalTransportResult`.

Pay particular attention to `Commitment`, `TriggerCondition`, `ResumptionCapsule`, action dispatch, evidence admission, recovery, and Control Ledger authority.

### Stage D — Verification

Run documentation-level verification for:

- Completeness of FCA and RDMS coverage
- Application of all approved normative corrections
- Duplicate or conflicting canonical definitions
- Missing required fields
- Invalid cross-layer ownership
- Broken source references
- Contradictory state-transition or authority rules
- Preservation of original source hashes

Provide an exact list of unresolved blockers. Do not report full completion if any mandatory normative clause remains unresolved.

### Stage E — GitHub workflow

Work in a dedicated documentation branch.

Commit each validated layer separately with a clear commit message.

Push the branch to the configured GitHub repository only after local verification.

Do not merge into `main` or declare the architecture FROZEN without explicit approval.

## Deliverables

- Eight current canonical layer specifications.
- Updated architecture manifest.
- Immutable original-source archive.
- Normative source-to-clause traceability.
- Cross-layer contract validation report.
- Focused unresolved-issues register.
- Verification commands and results.
- Git commit references and a final change summary.

## First checkpoint

Start by inspecting the archive and presenting:

1. The authoritative source inventory.
2. The proposed ownership map for L0–L7.
3. Any missing or ambiguous authoritative sources.
4. A concrete implementation sequence.

**Stop after this checkpoint. Do not begin rewriting the eight documents until the source inventory and ownership map have been reviewed and approved.**
