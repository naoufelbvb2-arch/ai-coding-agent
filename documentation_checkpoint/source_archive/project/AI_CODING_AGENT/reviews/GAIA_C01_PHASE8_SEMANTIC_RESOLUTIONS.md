# GAIA-C01 Phase 8 — Semantic Contract & Cross-Layer Consistency Review

**Status: mapping policies specified, not approved as frozen canonical schemas.** Primary FCA/RDMS sources remain untouched; a policy specification is not proof that a migration or adapter is executable.

## Review principles

1. Superseding correction precedence is explicit; do not merge original draft with an adopted C01 as simultaneous authorities.
2. One canonical entity owner; all other representations are typed projections with integrity/version-scoped references.
3. Information never disappears merely because a newer declaration uses fewer fields; references must be durable and reversible for required information.
4. A transport status, inference confidence, temporal freshness or tool result never alone supplies Executive authority, Evidence, world effect or causal closure.
5. Non-equivalent historical values are NOT mapped to fabricated values; mark migration review required.

## Eight semantic-gate determinations

### S8-01 — `ActionProposal`
**Owner:** L3 / RDMS-04 (FCA action semantics conserved)
**Anchored declarations:** FCA v1.0.1:FCA v1.0.1 baseline:1663,RDMS-04:Original draft:97

**Resolution rule (proposed):** Keep detailed operation kind as a mandatory, typed effective-operation discriminator separate from broad action_kind transport categories (FILESYSTEM, TERMINAL, etc.) and separate from action_class. A category alone never authorizes an effect.

**Legacy-to-current crosswalk:** Legacy kind=file_write -> action_kind=FILESYSTEM AND operation=file_write; kind=file_delete -> FILESYSTEM AND operation=file_delete; kind=shell -> TERMINAL AND operation=shell, subject to authorized tool scope.

**Fail-closed condition:** If the exact effect operation, target, reversibility, preconditions, or authorization scope is missing, no SHARED_WORLD dispatch and no automated canonical migration.

**Adversarial witness:** Two proposals with identical action_kind=FILESYSTEM but different delete/write semantics must remain distinguishable at ActionGate and sealed executor; include symlink-target switch.

**Evidence required before approval:** Signed/effective operation specs with explicit discriminator; version/integrity-resolvable context; downstream use and reverse-projection proof.

**Disposition:** `RESOLUTION_RULE_SPECIFIED / PROOF_PENDING / CANONICAL_PROMOTION_DENIED`.

### S8-02 — `Claim`
**Owner:** L2 / RDMS-02 (RDMS-03 owns evidence link)
**Anchored declarations:** FCA v1.0.1:FCA v1.0.1 baseline:387,RDMS-02:Original draft:132,RDMS-02:Original draft:211

**Resolution rule (proposed):** RDMS-02 C01 support assessment governs current support; FCA evidence_for/evidence_against and provenance must remain recoverable via accepted RDMS-03 EvidenceLink relations and historical provenance. FactGrounding remains mandatory for FACT.

**Legacy-to-current crosswalk:** Claim identity/kind/statement/scope/status/version -> RDMS-02 canonical record; support -> separately governed SupportAssessment; evidence arrays -> link relation queries constrained to claim and accepted status; provenance -> lineage refs.

**Fail-closed condition:** Missing source provenance or grounding cannot be promoted into FACT/VERIFIED; a claim with untraceable contradictory evidence enters review, not verified status.

**Adversarial witness:** FACT, BELIEF, ASSUMPTION with positive and negative evidence; challenge a previously strong claim using late contradictory observation; no silent drop.

**Evidence required before approval:** Source version lineage, evidence links, grounding, support-assessment provenance and temporal validity reconstruct FCA-level meaning.

**Disposition:** `RESOLUTION_RULE_SPECIFIED / PROOF_PENDING / CANONICAL_PROMOTION_DENIED`.

### S8-03 — `ContradictionRecord`
**Owner:** L3 / RDMS-03
**Anchored declarations:** FCA v1.0.1:FCA v1.0.1 baseline:662,RDMS-03:Original draft:632,RDMS-03:C01 and Freeze Review 02 Final:2381

**Resolution rule (proposed):** Use RDMS-03 lifecycle as current owner. FCA UNRESOLVED is an active unresolved epistemic condition, never map to RDMS-03 RESOLVED. For legacy migration preserve historical UNRESOLVED claim and derive unresolved as nonterminal/non-dismissed with no accepted resolution, only when demonstrably equivalent.

**Legacy-to-current crosswalk:** candidate -> CANDIDATE; confirmed -> CONFIRMED; explained -> EXPLAINED only with admissible explanation; unresolved -> unresolved condition/history, not RDMS lifecycle RESOLVED. RDMS RESOLVED needs its own closing proof.

**Fail-closed condition:** Without a valid lifecycle history, comparable observation sources and explanation/resolution evidence, do not auto-convert legacy unresolved to any terminal value.

**Adversarial witness:** Same observations but different times are NOT_COMPARABLE; later contradictory observation reopens question; UNRESOLVED must never disappear through RESOLVED alias.

**Evidence required before approval:** State history with comparability assessment, observation references, interpretation/proof separation and unresolved-state query.

**Disposition:** `RESOLUTION_RULE_SPECIFIED / PROOF_PENDING / CANONICAL_PROMOTION_DENIED`.

### S8-04 — `EvidenceLink`
**Owner:** L3 / RDMS-03
**Anchored declarations:** FCA v1.0.1:FCA v1.0.1 baseline:616,RDMS-03:Original draft:461,RDMS-03:Original draft:514

**Resolution rule (proposed):** RDMS-03 may bind multiple canonical observation_refs to one EvidenceLink with individual provenance; a FCA single observation_id view can be emitted only when cardinality equals one or via explicit composite link reference preserving whole set, not by silently spawning several independent accepted links.

**Legacy-to-current crosswalk:** FCA observation_id -> singleton observation_refs; RDMS multiple observation_refs -> collection-level evidence with full lineage. Target relation, derivation and acceptance remain distinct.

**Fail-closed condition:** Zero observations cannot form accepted EvidenceLink; untrusted generated text, duplicated observation or missing source cannot gain accepted evidential authority through projection.

**Adversarial witness:** Two observations and one interpretation accepted as one link, vs two independent links; assert different evidence cardinality and identical canonical provenance on reconstruction.

**Evidence required before approval:** Observation ID multiplicity, link IDs, acceptance history, signed source trace and exact target/relation preservation.

**Disposition:** `RESOLUTION_RULE_SPECIFIED / PROOF_PENDING / CANONICAL_PROMOTION_DENIED`.

### S8-05 — `Experiment`
**Owner:** L3 / RDMS-03
**Anchored declarations:** FCA v1.0.1:FCA v1.0.1 baseline:1595,RDMS-03:Original draft:871

**Resolution rule (proposed):** RDMS-03 Experiment is the authorized immutable design; ExperimentRun owns execution and outcome. FCA aggregate Experiment is a compatibility view over the design plus zero/multiple runs; design lifecycle does not inherit RUNNING or FAILED.

**Legacy-to-current crosswalk:** FCA designed/authorized -> design-state translation; running/completed/failed/cancelled -> explicit run(s) and observation/conclusion provenance, never design-state substitution.

**Fail-closed condition:** Legacy aggregate with RUNNING but no identifiable run, pre-committed prediction set or action authorization must be reviewed; do not infer design or retroactively freeze predictions.

**Adversarial witness:** One design -> two runs: first failed, second completed; same predictions predate both, and conclusion links back to correct runs.

**Evidence required before approval:** ExperimentID/RunID mapping, immutable prediction hashes, risk/authorization, run timestamps, observations and status history.

**Disposition:** `RESOLUTION_RULE_SPECIFIED / PROOF_PENDING / CANONICAL_PROMOTION_DENIED`.

### S8-06 — `Hypothesis`
**Owner:** L2 / RDMS-02 (RDMS-03 evidence, RDMS-02 causal closure)
**Anchored declarations:** FCA v1.0.1:FCA v1.0.1 baseline:472,RDMS-02:Original draft:382,RDMS-02:C01, second review corrections and final freeze decision:2117

**Resolution rule (proposed):** RDMS-02 C01 separates support assessment from lifecycle. Strongly supported or CONFIRMED hypotheses are not CAUSALLY_VERIFIED merely by ranking; only correctly evidenced causal-closure path to OVC can justify verified causal status.

**Legacy-to-current crosswalk:** FCA predictions, positive/negative evidence, competitors and experiments -> typed references and RDMS-03 accepted links; support and hypothesis lifecycle kept separate; historical support source retained.

**Fail-closed condition:** Cannot upgrade to CAUSALLY_VERIFIED if persisted prediction, intervention, regression or scope proof missing; no independent synthetic causal owner.

**Adversarial witness:** High support but no intervention; refuted competitor; confirmed but not operationally verified; intervention-based causal closure.

**Evidence required before approval:** Typed reference resolution for each FCA cognitive relation and explicit authorized OVC verification record.

**Disposition:** `RESOLUTION_RULE_SPECIFIED / PROOF_PENDING / CANONICAL_PROMOTION_DENIED`.

### S8-07 — `Observation`
**Owner:** L3 / RDMS-03
**Anchored declarations:** FCA v1.0.1:FCA v1.0.1 baseline:581,RDMS-03:Original draft:82

**Resolution rule (proposed):** RDMS-03 stores normalized observation with immutable raw artifact provenance and source/capture/ingest time separation. The original reported content remains retrievable; a trusted envelope or checksum proves integrity/provenance, not truth of source claim.

**Legacy-to-current crosswalk:** FCA observation content/observed_at/source -> RDMS-03 raw_artifact_ref, normalized report and TemporalProvenance (event/capture/ingest clocks) with original source identity.

**Fail-closed condition:** Missing raw bytes, degraded source trust or unknown event timestamp cannot be silently repaired by ingestion timestamp or promoted to verified fact.

**Adversarial witness:** Late-arriving log with event_time < ingestion_time; duplicated message; spoofed tool success that must remain report, not verified world effect.

**Evidence required before approval:** Raw byte hash, explicit source identity, clock trust, event order, capture integrity and interpretation provenance.

**Disposition:** `RESOLUTION_RULE_SPECIFIED / PROOF_PENDING / CANONICAL_PROMOTION_DENIED`.

### S8-08 — `OperationalCausalClaim`
**Owner:** L2 / RDMS-02
**Anchored declarations:** FCA v1.0.1:FCA v1.0.1 baseline:514,RDMS-02:Original draft:461

**Resolution rule (proposed):** RDMS-02 C01 verification_ref resolves complete FCA causal-closure checklist and its temporal order; canonical causal history and derived dependency freshness are distinct. Staleness is not evidence of causal refutation and later validity does not rewrite historical causal closure.

**Legacy-to-current crosswalk:** FCA verification {reproduction, prior prediction, targeted intervention, expected effect, regression, weakened alternatives, optional ablation} -> versioned verification_ref and evidence/observation references; FCA operational status with RDMS canonical lifecycle + derived freshness view.

**Fail-closed condition:** Any missing mandatory proof element, broken pre-intervention time ordering, unresolved contradiction or invalid scope blocks OPERATIONALLY_VERIFIED.

**Adversarial witness:** Proof missing prediction persistence; ablation present; dependency becomes stale and returns VALID; distinguish lifecycle history from current applicability.

**Evidence required before approval:** Ref dereference yields full source checklist with chronological commits, authority, specific environment and dependency frontier.

**Disposition:** `RESOLUTION_RULE_SPECIFIED / PROOF_PENDING / CANONICAL_PROMOTION_DENIED`.

## Phase-6 five priority contracts (unchanged legal status)

| Type | Intended owner(s) | Review status | Non-regression condition |
|---|---|---|---|
| `CapabilityResult` | L2 canonical / L7 transport | `ALIAS_PROPOSED` | FCA full semantic result remains canonical. L7 CapabilityTransportResult must resolve immutable original and preserve all fields, including needs, rationale and specialist_request. |
| `MemoryRetrievalResult` | L5 canonical / L7 transport | `ALIAS_PROPOSED` | RDMS-07 retrieval coverage/ranking/filtering remains canonical. L7 MemoryRetrievalTransportResult is a bounded view with required canonical reference. |
| `Commitment` | L2 semantic / L4 temporal | `MAPPING_REVIEW_REQUIRED` | No direct field union; purpose, owner, scope, links, statement, follow-up, timestamp and sequence remain distinct; RDMS-02 C01 reactivation root mandatory. |
| `TriggerCondition` | L4 temporal | `MAPPING_REVIEW_REQUIRED` | FCA full trigger vs RDMS-05 predicate; use distinct effective names and reconstruct full trigger with both detection and fire axes and exact reaction identity. |
| `ResumptionCapsule` | L4 lifecycle / L6 recovery | `PAYLOAD_PROOF_REQUIRED` | FCA complete recovery-context fields must remain in verified durable RDMS-05 C01 payload with integrity-pinned header, and resume never auto-dispatches next action. |

## Cross-layer invariant conservation

- RDMS-01 keeps canonical control commit and leadership authority; no transport type creates writes.
- RDMS-03 keeps observational and evidential semantics; false tool claims cannot become accepted evidence.
- RDMS-04 keeps world-action authorization, journal, effect semantics and uncertain-effect reconciliation.
- RDMS-05 keeps temporal evaluation, reaction identity and reactivation conditions; no direct autonomous tool actions.
- RDMS-06 keeps dependency freshness, including partially stale and UNKNOWN.
- RDMS-07 retains memory lineage and promotion governance.
- RDMS-09 recovery does not create a second Executive and cannot infer that an external worker stopped.
- RDMS-10 projections must link to existing legal entities; adapters cannot rename away their obligations.

## Open certification gates

1. Approve proposed L7 transport aliases (`CapabilityResult`, `MemoryRetrievalResult`) with complete mapping.
2. Produce proof of composite semantic preservation for `Commitment`, `TriggerCondition` and `ResumptionCapsule`.
3. Demonstrate eight semantic policies against archival data and current source schemas; no implicit coercions.
4. Verify nine conditional maps and five low-risk mappings with field-level evidence (below).
5. Conduct interface/method/transaction and causality audit, not only repeated type names.
6. Explicitly authorize canonical layer promotion; all L0–L7 documents remain DRAFT until then.

