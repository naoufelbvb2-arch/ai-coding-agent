# AI Coding Agent — canonical architecture documentation

All eight layer documents are consolidated for independent review on docs/canonical-source-checkpoint. **Full normative acceptance remains OPEN; the architecture is NOT FROZEN.**

The targeted review of the original 40 questions records **8 source-determined resolutions, 6 representation details deferred to Implementation Design, 25 open preservation proofs and 1 architectural decision requiring review**. No direct irreconcilable pair was established; the remaining information/admission gaps still prevent full acceptance.

Start with the [architecture manifest](architecture/ARCHITECTURE_MANIFEST.md) and [targeted resolution report](reviews/canonical/BLOCKER_RESOLUTION_REPORT.md). The [consolidation completion report](reviews/canonical/COMPLETION_REPORT.md) records the preceding baseline.

- [Layer specifications](architecture/ARCHITECTURE_MANIFEST.md): current responsibilities, owned contracts and imported interfaces.
- [Source-to-clause trace](reviews/canonical/CLAUSE_TRACEABILITY.json) and [source dispositions](reviews/canonical/SOURCE_COVERAGE.json).
- [Twelve interface paths](reviews/canonical/INTERFACE_VALIDATION.md), including authority, durability, failure and rejection constraints.
- [Exact unresolved questions](reviews/canonical/UNRESOLVED_ISSUES.md).
- [All 40 classifications and exact evidence](reviews/canonical/BLOCKER_CLASSIFICATION.md), including binding obligations for deferred details.
- [Eight source-determined preservation proofs](reviews/canonical/SOURCE_DETERMINATE_PROOFS.md) and [focused regression results](reviews/canonical/BLOCKER_REGRESSION_RESULTS.json).
- [Verification commands and results](reviews/canonical/VERIFICATION.md).
- [Approved source checkpoint](documentation_checkpoint/CHECKPOINT_REVIEW.md) and [195-file SHA-256 manifest](documentation_checkpoint/SOURCE_MANIFEST.json).

The original archives and historical integrations remain byte-preserved under documentation_checkpoint/source_archive/. Their read-only attributes and hashes provide custody evidence; do not edit them. Historical checkpoint files retain their checkpoint-time statuses. Subsequent approval and ownership clarifications are recorded in [AUTHORIZATION.md](reviews/canonical/AUTHORIZATION.md).

Python tools here generate and verify documentation only. No production agent runtime was implemented, no new architecture law was introduced, and no merge into main or consolidated freeze is authorized.

Use `python tools/verify_consolidation.py` and `python tools/verify_blocker_resolution.py` for the current baseline. Full regeneration is disabled after targeted reconciliation to protect reviewed document edits.
