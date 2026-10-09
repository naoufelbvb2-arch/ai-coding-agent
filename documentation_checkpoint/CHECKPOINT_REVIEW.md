# Stage A checkpoint — source inventory and proposed layer ownership

Review date: 2026-10-09, America/New_York. Status: **READY FOR SOURCE/OWNERSHIP REVIEW ONLY. Consolidation not started; architecture freeze remains HOLD.**

This checkpoint follows the user's pasted request, including: “Stop after this checkpoint. Do not begin rewriting the eight documents until the source inventory and ownership map have been reviewed and approved.” The similarly worded prompt inside the ZIP is preserved as packaging evidence, not treated as an independent instruction.

## 1. Inventory scope and custody

The complete handoff was recursively inspected: the outer ZIP has four members, and its project ZIP has 190 files with no further nested ZIPs. The source archive preserves **195 files**: the original outer ZIP, its four members, and all 190 project members. **179 text documents/artifacts** were read and indexed; every JSON document parsed successfully. Archived executables, verification scripts, pytest caches, and implementation placeholders were inventoried without execution.

The original ZIP remains unchanged. Preserved copies carry read-only filesystem attributes; `.gitattributes` disables text normalization for every archived file. SHA-256 verification detects changes. This is repository custody with read-only attributes, not WORM storage or protection against an administrator intentionally rewriting files.

The entire file inventory, full SHA-256 values, origin archive chains, version information, authority status, classification, and classification basis are in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) and [SOURCE_MANIFEST.csv](SOURCE_MANIFEST.csv). [DOCUMENT_INDEX.json](DOCUMENT_INDEX.json) contains document headings and line locators. [SOURCE_UNITS.json](SOURCE_UNITS.json) classifies all 27 RDMS original messages and records their message IDs, complete-text checksums, exact bundle line ranges, and freeze evidence.

Integrity results:

- Both ZIP containers passed CRC reads for every member.
- All three supplied handoff checksums matched.
- Both FCA frozen-spec sidecar checksums matched. The v1.0 sidecar's historical `/mnt/data/` locator was resolved to the same preserved filename, without editing the sidecar.
- All **27/27** RDMS DOM message texts matched their supplied SHA-256 and character count, and each appeared exactly in its corresponding TXT bundle.
- All **195/195** preserved file hashes matched after inspection.

## 2. Authoritative source inventory

Paths below are relative to `source_archive/project/AI_CODING_AGENT/reviews/source_archive/`. Full hashes are in the file manifest. Hash prefixes here identify the exact inventoried bytes, not approval authority.

| Source | Original file | Source chain and authority | Primary destination |
|---|---|---|---|
| FCA v1.0.1 | `Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md` | Current frozen source; header declares Freeze Review 05 PASS. Explicitly supersedes FCA v1.0 as the current normative reference. SHA-256 `74d0923cbd343b71…`. | L0 constitutional ownership; specialist rules assigned to their responsible layer |
| RDMS-01 | `RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt` | Baseline → R1 corrections and final freeze; 2 messages. Freeze declaration at bundle line 2169. | L1 |
| RDMS-02 | `RDMS_ORIGINAL_SOURCES/RDMS-02_APPROVED_SOURCE_SET.txt` | Baseline → C01 plus second-review corrections and final freeze; 2 messages. Freeze at line 3456. | L2 |
| RDMS-03 | `RDMS_ORIGINAL_SOURCES/RDMS-03_APPROVED_SOURCE_SET.txt` | Baseline → C01 plus Freeze Review 02 Final; 2 messages. Freeze at line 3507. | L3 |
| RDMS-04 | `RDMS_ORIGINAL_SOURCES/RDMS-04_APPROVED_SOURCE_SET.txt` | Baseline → C01 → Adversarial Freeze Review 02; 3 messages. Specification-level freeze at line 2747. | L3 |
| RDMS-05 | `RDMS_ORIGINAL_SOURCES/RDMS-05_APPROVED_SOURCE_SET.txt` | Baseline → C01 → Adversarial Freeze Review 02; 3 messages. Specification-level freeze at line 2852. | L4 |
| RDMS-06 | `RDMS_ORIGINAL_SOURCES/RDMS-06_APPROVED_SOURCE_SET.txt` | Baseline → C01 plus Adversarial Freeze Review 02; 2 messages. Specification-level freeze at line 3305. | L4 |
| RDMS-07 | `RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt` | Baseline → C01 plus Adversarial Freeze Review 02; 2 messages. Specification-level freeze at line 3538. | L5 |
| RDMS-08 | `RDMS_ORIGINAL_SOURCES/RDMS-08_APPROVED_SOURCE_SET.txt` | Baseline → C01 plus Adversarial Freeze Review 02; 2 messages. Specification-level freeze at line 4594. | L2 |
| RDMS-09 | `RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt` | Baseline → C01 → C02 → C03 → Adversarial Freeze Review 04 and final interpretations; 5 messages. Specification-level freeze at line 8408. | L6 |
| RDMS-10 | `RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt` | Baseline → C01 → C02 → Final Freeze Review 03 and final interpretations; 4 messages. Architectural specification-level freeze at line 7818. | L7 |

These are **10 baseline messages and 17 later amendment/review/freeze messages**, not 17 standalone correction specifications. Several messages contain multiple document stages. The complete bundles are mixed source containers, not already consolidated final specifications. Their historical `DRAFT` headings must not become current normative status merely through copying.

The frozen RDMS composite is the unchanged baseline rules plus explicitly approved amendments and binding final interpretations. Superseded baseline statements remain historical. A partial correction struct is an overlay within its stated scope, not permission to delete omitted fields.

FCA has **88 base numbered sections, §0–§87**, associated decimal subsections, unnumbered invariant/traceability sections, and **seven appendices, A–G**. [FCA_SECTION_OWNERSHIP_PROPOSAL.json](FCA_SECTION_OWNERSHIP_PROPOSAL.json) assigns every base section once. Decimal subsections inherit their enclosing section's owner. Appendix B explicitly remains non-normative; the appendix index does not turn examples or historical review narratives into law.

## 3. Classification and precedence

| Classification | Admitted examples | Effective handling |
|---|---|---|
| Frozen authoritative source | FCA v1.0.1; historically frozen FCA v1.0 | v1.0.1 is current. v1.0 stays frozen historical evidence, not a second current authority. RDMS effective frozen composites are established by their embedded final decisions. |
| Approved amendment or correction | RDMS-01 R1; RDMS-02–08 C01 and explicitly binding review refinements; RDMS-09 C01/C02/C03; RDMS-10 C01/C02 | Apply only to clauses and responsibilities expressly changed. No automatic cross-specification supersession. |
| Freeze decision | Embedded final RDMS reviews, including FC09-04-01…04 and FC10-03-01…08 | Admit the described source composition and binding interpretations; preserve the distinction between specification review and implementation proof. |
| Historical draft | Original FCA draft; RDMS original messages in their historical form | Retain only unchanged rules admitted by the final composite. Exclude superseded statements from future normative bodies. |
| Previous integration attempt | Existing eight `architecture/L*.md` files, architecture manifest and interfaces, prior layer snapshots, pre-normative-merge snapshots | Migration/reconciliation input only; independently re-check against original sources. None is promoted because it is latest. |
| Supporting verification evidence | GAIA C01–C08 review ledgers, closeout gates, inventories, tests/logs, original-message DOM and manifests, packaging/tooling/cache artifacts | Useful evidence and locators. Neither generated claims nor passing historical tests authorize new law. |

FCA's own §0 and §0.1.1 govern the v1.0/v1.0.1 relationship. RDMS amendments are read in their recorded order, with later corrections superseding only explicit earlier clauses. RDMS-10 C01 §6–§10 states that canonical owners govern semantic meaning, the contract registry has no independent authority, and unknown compatibility rejects authority-bearing transitions. Final FC10-03-08 repeats that owner/projection rule.

## 4. Proposed ownership map

This is an editorial allocation of existing responsibility, not a new authority structure. Ownership of an entity's semantics is distinct from physical persistence, executive authorization, transport, and recovery participation. A consuming layer imports the owner contract by source-backed reference and specifies its own boundary responsibilities.

| Layer / target | Sole normative responsibility and representative contracts | Governing sources and imported responsibilities |
|---|---|---|
| L0 / `architecture/L0_FOUNDATION.md` | Architectural identity, authority/trust constitution, frozen invariants and change-control rules; source and principle indices | FCA §0–§4, §20–§21, §72–§73, §84, §86–§87; operational rules allocated to their responsible layers, with references from L0 |
| L1 / `architecture/L1_CONTROL.md` | `ControlCommit`, current-state/ledger atomic persistence, `ProjectHead`, sequencing, idempotency, epoch fencing, lawful control commits | FCA §48–§51; RDMS-01 + R1. Imports semantic authorization and owner mutations; does not take semantic ownership of every stored entity |
| L2 / `architecture/L2_COGNITION.md` | Canonical cognitive workspace/entities, Goal/Slice/Decision/Claim/Hypothesis, **Commitment**, capability result, executive selection and cognitive transition policy | FCA cognition/capabilities/executive sections and §55; RDMS-02 + C01/final refinements; RDMS-08 + C01/final review. Imports L1 persistence, L3 evidence/actions, L4 reactivation/freshness, L5 memory, L6 recovery |
| L3 / `architecture/L3_ACTIONS.md` | Observation/EvidenceLink/FactGrounding, experiments/predictions/verification/contradictions; ActionProposal/ActionRecord/Action Journal, ActionGate, exact dispatch, tools, sandbox and external outcomes | FCA §11–§14, §35, §40–§47, §75–§76, §79; RDMS-03/04 plus their corrections/final reviews. Imports L1 commits, L2 cognition, L4 freshness, L6 recovery |
| L4 / `architecture/L4_TEMPORAL_SPECIALISTS.md` | TriggerCondition and durable trigger/fire/reaction contracts; temporal reactivation; **ResumptionCapsule**; specialist isolation/contracts/integration freshness; single dependency evaluation authority | FCA §53–§54, §56, §63–§71, §78, §80, §82; RDMS-05/06 plus corrections/final reviews. Imports L2 Commitment lifecycle, L1 persistence, L3 evidence/actions, L6 recovery admission |
| L5 / `architecture/L5_MEMORY.md` | MemoryProposal, canonical **MemoryRetrievalResult**, retrieval scope/ranking/coverage/freshness, governed learning/promotion and data lineage | FCA §57–§62, §77; RDMS-07 + C01/final review. Imports L4 dependency assessment, L2 decisions, L1 persistence and L7 outbound disclosure |
| L6 / `architecture/L6_RECOVERY.md` | Recovery incidents/admissions/continuations, restore integrity, anti-rollback, quarantine, migration/cutover and scoped recovery | FCA §52; RDMS-09 baseline + C01/C02/C03 + final review interpretations. Imports L1 authority/history, L3 unresolved world effects, L4 capsules/reactivation/freshness, L5 data restrictions |
| L7 / `architecture/L7_RUNTIME_INTEGRATION.md` | Provider/integration envelopes, owner registry references, trusted ingress/egress, exact outbound context and cross-component binding | FCA §85; RDMS-10 baseline + C01/C02 + final FC10-03 interpretations. Imports canonical owner contracts. **CapabilityTransportResult** and **MemoryRetrievalTransportResult** remain distinguishable editorial labels for RDMS-10 homonyms, with no independent canonical authority |

Commitment ownership is explicitly settled by **RDMS-05 C01-01**, bundle lines 1357–1398: RDMS-02 owns Goals/Slices/Commitments; RDMS-05 owns temporal triggers/reactivation and must not define alternative lifecycles. The older GAIA Phase 5 proposal assigning Commitment lifecycle to L4 is historical and must not drive the consolidation.

RDMS-08's ownership matrix, bundle lines 166–181, corroborates the source responsibilities. RDMS-10's original draft table at lines 1433–1451 attributes Claim/Hypothesis to “RDMS-03 semantics,” while RDMS-02 defines their entities. This is an integration ambiguity, not permission to move their entity ownership to L3: RDMS-10 C01's canonical-owner rule and final FC10-03-08 preserve the owning specification. L3 owns evidence/grounding semantics, while L2 owns Claim/Hypothesis entities.

The proposed owners for the twelve tracked interface paths, participants, source anchors, and outstanding validation obligations are in [INTERFACE_REVIEW_PLAN.md](INTERFACE_REVIEW_PLAN.md). Route ownership does not override ownership of the types traversing it.

## 5. Missing or ambiguous sources

**No FCA v1.0.1 or RDMS-01–10 source bundle is missing from this handoff.** RDMS-09 C03, RDMS-10 C01/C02, and both final freeze reviews are present. Old GAIA reports saying RDMS sources were absent predate their recovery and must remain historical.

There are no separate, uniformly rewritten final frozen RDMS files. This is not by itself a missing-clause blocker: the complete approved-message composites are available. It means effective-law reconstruction must explicitly combine baseline, amendments, and final interpretation rather than treat a TXT bundle as a ready-to-use clean final document.

Approval provenance has a precise limit: `original_message_dom.json` contains 27 records, all with role `assistant`. It preserves recorded specification decisions, but no separate user ratification messages, signed approval records, or independently authenticated source-session export. We can prove supplied-package identity and internal consistency; hashes do not prove who approved the law. The review should confirm that the supplied frozen composites are the intended authoritative basis. No public share URL was fetched or claimed authenticated.

The editorial transport aliases are present in GAIA material and explicitly requested by the user for distinction; their names are not exact frozen RDMS declaration spellings. Their canonical-versus-transport identity may be made clear editorially, but lossless field semantics and any signature authorization still require source-grounded proof.

No irreconcilable normative contradiction is asserted as established at this checkpoint. Concrete competing shapes and the remaining proof obligations are recorded in [UNRESOLVED_ISSUES.md](UNRESOLVED_ISSUES.md). A future clause conflict that has no explicit authoritative resolution must remain blocked, with exact source clauses retained.

## 6. Concrete implementation sequence after approval

1. Confirm the source admission and L0–L7 ownership proposal at this checkpoint. Until approval, make no changes to the eight canonical documents.
2. Keep working on `docs/canonical-source-checkpoint`, or a continuation documentation branch. Use configured `origin` at `https://github.com/naoufelbvb2-arch/ai-coding-agent.git`. The remote returned no refs when inspected; no existing branch history was imported or replaced.
3. Build a clause-level effective-law ledger: source ID, message ID, exact section/line range and hash, rule identity, original clause, approved delta, explicit supersession scope, current effective rule, owner, and unresolved disposition. Include all baseline material, all 17 later messages, final interpretations, FCA decimal subsections/invariants/appendices, and distinguish non-normative examples.
4. Resolve field-preservation and homonym obligations before publishing clean owner contracts, especially Commitment, TriggerCondition/TriggerFire/TriggerReaction, ResumptionCapsule, CapabilityResult and MemoryRetrievalResult. Preserve spelling and optionality; never fill an unspecified primitive type, transition, or API signature by inference.
5. Consolidate and validate L0, then L1, L2, L3, L4, L5, L6 and L7. Each document has one normative owner body and explicit imported interfaces, with no mixed historical annex promoted into current law. Validate each layer against its complete source allocation and commit that validated layer separately with a clear message. Retain the immutable archive and trace ledger.
6. For every X8-01…X8-12 path, verify source-defined inputs/outputs, fields/constraints, canonical and transition owners, authorizations, atomicity/durability, failure/retry/recovery and explicit rejections. Cross-check producer and consumer obligations and amendment precedence. Mark unspecified signatures as unresolved rather than inventing them.
7. Publish `architecture/ARCHITECTURE_MANIFEST.md`, the source-to-clause traceability ledger, contract validation report and focused unresolved register. Check for missing source clauses/fields, duplicate definitions, broken source locators, unauthorized ownership, conflicting transitions and preservation of all original hashes. Historical reference tests are supporting evidence, not proof of the new documents.
8. Push the documentation branch only after local documentation verification. Do not merge into `main`. Do not declare the consolidated architecture FROZEN without explicit approval. If a mandatory clause remains unresolved, report incomplete consolidation and its exact blocker.

## 7. Current checkpoint result and approval boundary

The source inventory, archival integrity verification and proposed ownership map are ready for review. The existing eight layer documents and architecture manifest are preserved **only as original archived inputs**; no live canonical replacement has been created. No production code was written or executed. None of the future layer validation, full twelve-interface proof, layer commits or remote publication is claimed complete.

Review requested: approve the authoritative composite source basis and the proposed ownership map, or specify corrections. This approval boundary comes directly from the user's pasted request quoted above; it is not an additional skill or repository restriction.
