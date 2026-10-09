# GAIA-C05 — Structural Field Preservation Gate

**Important:** A field absent from a later top-level schema is a mapping obligation, NOT proof that the field was legally deleted or stored nowhere. This audit does not certify a lossless adapter.

## `ResumptionCapsule`

- Old top-level fields: **22**
- Corrected top-level fields: **11**
- Original fields without same-name top-level peer: **16**

| Missing same-name field | Action before legal conversion |
|---|---|
| `active_slice_refs[]` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `base_canonical_commit_seq` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `commitment_refs[]` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `current_focus_ref?` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `decision_refs[]` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `dependency_set_ref?` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `environment_ref?` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `open_information_need_refs[]` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `project_id` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `rejected_path_refs[]` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `relevant_claim_refs[]` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `relevant_evidence_refs[]` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `relevant_hypothesis_refs[]` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `repo_ref?` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `temporary_change_refs[]` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `world_ref?` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |

**Status:** `BLOCK_DIRECT_FIELD_DROPPING_UNTIL_PAYLOAD_REFERENCE_PROOF`

## `TriggerFire`

- Old top-level fields: **8**
- Corrected top-level fields: **7**
- Original fields without same-name top-level peer: **5**

| Missing same-name field | Action before legal conversion |
|---|---|
| `condition_version_ref` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `fired_at_commit_seq` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `generation` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `trigger_id` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |
| `triggering_basis_refs[]` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |

**Status:** `SCHEMA_DELTA_MUST_BE_MAPPED_NOT_NAME_ONLY`

## `ObservationAmendment`

- Old top-level fields: **7**
- Corrected top-level fields: **8**
- Original fields without same-name top-level peer: **1**

| Missing same-name field | Action before legal conversion |
|---|---|
| `authority_ref` | Preserve via explicitly verified payload/ref mapping; otherwise reject migration |

**Status:** `SCHEMA_DELTA_MUST_BE_MAPPED_NOT_NAME_ONLY`
