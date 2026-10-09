# GAIA-C01 Phase 8 — Conditional & Low-Risk Mapping Proof Obligations

**This is a specification-level proof plan; it does not certify actual conversion or code execution.**

## Nine conditional-preservation cases

### C8-01 `ActionEffectSemantics`
- Owner: `L3`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:1756,RDMS-04:Original draft:341`.
- Gate: Retry policy and verification_mode not weakened.
- Required witness: Probe/compensation/timeout_spec refs resolve to exact original semantics; unknown non-idempotent effect never blindly retried.
- Failure policy: `MIGRATION_REVIEW_REQUIRED` / no silent data loss.

### C8-02 `ActionRecord`
- Owner: `L3`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:1883,RDMS-04:Original draft:208`.
- Gate: Action Journal legal history complete.
- Required witness: Recover all attempts, reports, observations, compensation, timestamps; latest_attempt_ref alone insufficient.
- Failure policy: `MIGRATION_REVIEW_REQUIRED` / no silent data loss.

### C8-03 `ConfidenceAssessment`
- Owner: `L3`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:698,RDMS-03:Original draft:1412`.
- Gate: Confidence independent of mere ranking.
- Required witness: Evidence/verification refs resolve and wall-clock timestamps not silently mapped to commit sequence.
- Failure policy: `MIGRATION_REVIEW_REQUIRED` / no silent data loss.

### C8-04 `Decision`
- Owner: `L2`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:805,RDMS-02:Original draft:855`.
- Gate: Choice/rejection rationale lossless.
- Required witness: Preserve chosen option, rejected option reasons, evidence, alternatives, constraints, scope, version.
- Failure policy: `MIGRATION_REVIEW_REQUIRED` / no silent data loss.

### C8-05 `DependencyStamp`
- Owner: `L4`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:2486,RDMS-01:Original draft:794,RDMS-06:Original draft:659`.
- Gate: Single RDMS-06 freshness semantics.
- Required witness: Enumerate all nine FCA kinds; RDMS-01 projections cannot bypass currentness checks.
- Failure policy: `MIGRATION_REVIEW_REQUIRED` / no silent data loss.

### C8-06 `Invariant`
- Owner: `L2`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:887,RDMS-02:Original draft:947`.
- Gate: Hard/critical guard cannot be softened.
- Required witness: All enforcement modes, severity, scope and failure semantics survive.
- Failure policy: `MIGRATION_REVIEW_REQUIRED` / no silent data loss.

### C8-07 `MemoryProposal`
- Owner: `L5`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:2237,RDMS-07:Original draft:486`.
- Gate: No automatic learning or disclosure.
- Required witness: Evidence, counterexamples, applicability, consent/provenance and approval path preserved.
- Failure policy: `MIGRATION_REVIEW_REQUIRED` / no silent data loss.

### C8-08 `SandboxActivityRecord`
- Owner: `L3`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:1857,RDMS-04:Original draft:1124`.
- Gate: Containment evidence and outcome preserved.
- Required witness: Recover evidence of isolation, op counts, output/observation refs and result including partial failure.
- Failure policy: `MIGRATION_REVIEW_REQUIRED` / no silent data loss.

### C8-09 `Slice`
- Owner: `L2`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:1246,RDMS-02:Original draft:1217`.
- Gate: Plan transition and proof obligations preserved.
- Required witness: Actual-vs-expected change surface, rollback/proof obligations and all slice statuses remain separate.
- Failure policy: `MIGRATION_REVIEW_REQUIRED` / no silent data loss.

## Five lower-risk mappings (still requiring explicit proof)

### L8-01 `Goal`
- Owner: `L2`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:735,RDMS-02:Original draft:576`.
- Gate: No fabricated priority class.
- Required witness: Preserve hierarchy, status, acceptance criteria, blockers, provenance and priority as typed-or-unresolved.
- Failure policy: non-equivalent data remains explicitly unresolved.

### L8-02 `GoalStack`
- Owner: `L2`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:760,RDMS-02:Original draft:736`.
- Gate: No fabricated optional hierarchy entities.
- Required witness: Empty/populated stack yields same focus, project/version and ordering.
- Failure policy: non-equivalent data remains explicitly unresolved.

### L8-03 `InformationNeed`
- Owner: `L2`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:440,RDMS-02:Original draft:285`.
- Gate: No fabricated answer provenance.
- Required witness: Preserve route, blockers and resolution reference, else require review.
- Failure policy: non-equivalent data remains explicitly unresolved.

### L8-04 `QueryDependencyStamp`
- Owner: `L4`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:2544,RDMS-06:Original draft:897`.
- Gate: No widened absence proof.
- Required witness: Validate exact frontier, proof scope, revision, index generation/hash and freshness.
- Failure policy: non-equivalent data remains explicitly unresolved.

### L8-05 `TemporalValidity`
- Owner: `L4`; legal source declarations: `FCA v1.0.1:FCA v1.0.1 baseline:2088,RDMS-05:Original draft:803`.
- Gate: Enum normalization only.
- Required witness: CURRENT/STALE/UNKNOWN map case-insensitively but CURRENT requires validity reevaluation.
- Failure policy: non-equivalent data remains explicitly unresolved.

## Proof requirements common to all 14 cases

1. Compare **full original declaration**, not only a name and a list of field aliases.
2. Identify adopted correction precedence and the owning schema version.
3. Demonstrate identity, scope, source provenance and authority cannot be forged by serialization.
4. Show required fields, optional fields, nested cardinality and state histories can be recovered, or record an explicit non-reversible exception.
5. Verify at least positive, missing-ref, stale-version and forged-authorization negative witnesses.
6. The acceptance tests below are planned; none are executable runtime tests in this phase.

