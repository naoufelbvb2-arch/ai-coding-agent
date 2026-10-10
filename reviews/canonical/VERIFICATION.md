# Current consolidation verification

**Mechanical result: PASS. Full normative acceptance: OPEN.**

Command: python tools/verify_consolidation.py. This check verifies custody, locators, ownership and selected high-risk amendment effects. It does not infer semantic completeness from a passing search or hash.

| Check | Result |
|---|---|
| archive_files | 195 |
| catalogued_source_units | 2628 |
| source_backed_articles | 1615 |
| local_links_checked | 2384 |
| single_owner_exported_record_definitions | 385 |
| interface_paths_processed | 12 |

## Required acceptance checks

- complete_authoritative_source_inventory: PASS.
- source_scope_dispositions_and_amendment_locators: PASS.
- original_source_sha256_integrity: PASS.
- unique_assigned_contract_ownership: PASS.
- known_explicit_field_replacements: PASS.
- complete_non_superseded_field_preservation: OPEN; exact shape and parent/projection questions recorded.
- amendment_precedence_and_no_contradictory_effective_laws: SCOPED REPLACEMENTS VERIFIED; full semantic acceptance remains OPEN.
- no_unauthorized_authority_expansion: SOURCE-BOUND AUTHORITY CONTRACTS RECORDED; independent semantic review required.
- cross_layer_interfaces: 12 constraints reviewed; complete field/projection acceptance OPEN.
- durability_and_recovery: SOURCE REQUIREMENTS PRESERVED; serialization/admission conformance and runtime proof not claimed.

Unresolved exact clauses and consequences: [issues register](UNRESOLVED_ISSUES.md). Document hashes and detailed failures: [VERIFICATION.json](VERIFICATION.json). Archive byte custody is independently reproducible with python documentation_checkpoint/tools/archive_inventory.py --verify.

No executable runtime or platform conformance tests were run because production implementation is not authorized. Source freeze reviews are documentary specification evidence, not runtime tests or a new consolidated freeze.
