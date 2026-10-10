# AI Coding Agent — Targeted Normative Blocker Resolution

## Current Repository State

Repository: `naoufelbvb2-arch/ai-coding-agent`

Branch: `docs/canonical-source-checkpoint`

Reviewed baseline commit:

`d50b7f88105b5397aa7d76e0bb8a1c2099a7c85e`

All eight canonical layer documents have been published.

Mechanical source verification passed.

Full normative acceptance remains open due to 40 recorded questions.

## Objective

Resolve the remaining genuine architectural blockers without restarting documentation consolidation.

**Do not regenerate L0–L7 from scratch.**

The existing consolidated layer documents are the working baseline.

The task is now targeted legal-contract reconciliation.

## Phase A — Classify the 40 Questions

Read:

`reviews/canonical/UNRESOLVED_ISSUES.json`

For each question, assign exactly one classification:

**A — NORMATIVE_CONFLICT**

Two effective authoritative requirements cannot coexist without a documented resolution.

**B — LOSSLESS_MAPPING_REQUIRED**

Multiple valid representations exist, but the relationship between their fields or meanings requires proof.

**C — IMPLEMENTATION_DETAIL_DEFERRED**

The authoritative specifications define the required semantics, but leave implementation-level representation or serialization details open.

**D — ALREADY_RESOLVED**

The effective consolidated specification already resolves the question, and this can be proven from authoritative source clauses.

**E — EXPLICIT_ARCHITECTURAL_DECISION_REQUIRED**

The frozen sources are genuinely insufficient or contradictory, and resolving the issue would require a new approved architectural decision.

For every classification, provide exact source evidence and explain why the classification is justified.

Do not classify an issue as implementation-deferred if it affects legal authority, mandatory information preservation, canonical identity, state transitions, durability, or recovery correctness.

## Phase B — Resolve Source-Determinate Questions

Prioritize the following areas:

1. L3 — ActionProposal, ActionRecord and ActionEffectSemantics.
2. L1 — CE-01 canonical-event metadata.
3. L6 — ResumptionCapsule and ResumeAssessment.
4. L4 — TriggerFire, TriggerReaction and TriggerCondition.
5. L2 — HG-01 Hypothesis support assessments.
6. L7 — CapabilityResult and MemoryRetrievalResult transport mappings.

Apply corrections only when their meaning follows from approved FCA/RDMS sources.

Preserve all non-superseded fields and legal requirements.

Do not invent field aliases, thresholds, lifecycle transitions, or authorities.

## Phase C — Update Canonical Documents

For each resolved issue:

* Modify only the owning canonical layer document and genuinely affected references.
* Record the exact source clauses establishing the resolution.
* Preserve historical source bytes.
* Remove obsolete warnings only when the underlying issue is actually resolved.
* Update the unresolved register with the evidence and disposition.
* Add focused regression checks for every resolved normative requirement.

Do not modify unrelated layer contracts.

Do not introduce architectural mechanisms outside the frozen specifications.

## Phase D — Handle Implementation-Deferred Questions

For each genuinely implementation-level question:

Document the binding architectural obligations that any implementation must satisfy.

Specify what remains deliberately unspecified.

Explain why the open detail does not affect architectural correctness or authority.

Mark it as deferred to Implementation Design, not silently resolved.

Do not create an arbitrary schema merely to close the issue.

## Phase E — Architectural Decisions

If a question genuinely requires a new architectural decision:

Do not choose one automatically.

Provide:

* The exact conflicting or missing source clauses.
* The smallest decision required.
* The available source-compatible alternatives.
* The consequences of each alternative.
* The affected layers and interfaces.

Keep the issue open for architecture review.

## Phase F — Verification and Publication

Run the existing consolidation verifier and new focused regression tests.

Verify that all twelve cross-layer interfaces preserve their required legal semantics.

Create focused Git commits for proven corrections.

Push to the existing documentation branch.

Do not merge into main.

Do not implement production code.

Do not declare FROZEN.

## Required Final Report

Provide:

1. Original unresolved questions: 40.
2. Questions resolved with authoritative evidence.
3. Questions safely deferred to Implementation Design.
4. Genuine normative conflicts still open.
5. Architectural decisions requiring approval.
6. Exact modified files and commit SHAs.
7. Verification results.
8. Cross-layer interface impact.
9. Updated freeze-readiness assessment.

The total of all final classifications must equal 40.

## Critical Requirement

The objective is not to make the number of open issues artificially reach zero.

The objective is to establish whether any **genuine unresolved normative requirement** still prevents an architectural freeze.

A complete architectural specification does not require inventing implementation details that the original specification intentionally leaves open.

Proceed with targeted analysis and source-determined corrections. Stop before making any new architectural decision that requires approval.
