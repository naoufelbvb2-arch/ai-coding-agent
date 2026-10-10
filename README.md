# AI Coding Agent — canonical architecture documentation

All eight layer documents are consolidated for independent review on docs/canonical-source-checkpoint. **Full normative acceptance remains OPEN; the architecture is NOT FROZEN.**

Start with the [architecture manifest](architecture/ARCHITECTURE_MANIFEST.md) and [completion report](reviews/canonical/COMPLETION_REPORT.md).

- [Layer specifications](architecture/ARCHITECTURE_MANIFEST.md): current responsibilities, owned contracts and imported interfaces.
- [Source-to-clause trace](reviews/canonical/CLAUSE_TRACEABILITY.json) and [source dispositions](reviews/canonical/SOURCE_COVERAGE.json).
- [Twelve interface paths](reviews/canonical/INTERFACE_VALIDATION.md), including authority, durability, failure and rejection constraints.
- [Exact unresolved questions](reviews/canonical/UNRESOLVED_ISSUES.md).
- [Verification commands and results](reviews/canonical/VERIFICATION.md).
- [Approved source checkpoint](documentation_checkpoint/CHECKPOINT_REVIEW.md) and [195-file SHA-256 manifest](documentation_checkpoint/SOURCE_MANIFEST.json).

The original archives and historical integrations remain byte-preserved under documentation_checkpoint/source_archive/. Their read-only attributes and hashes provide custody evidence; do not edit them. Historical checkpoint files retain their checkpoint-time statuses. Subsequent approval and ownership clarifications are recorded in [AUTHORIZATION.md](reviews/canonical/AUTHORIZATION.md).

Python tools here generate and verify documentation only. No production agent runtime was implemented, no new architecture law was introduced, and no merge into main or consolidated freeze is authorized.
