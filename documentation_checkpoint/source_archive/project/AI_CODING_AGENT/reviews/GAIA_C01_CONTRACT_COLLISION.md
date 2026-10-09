# GAIA-C01 — Contract Collision Repair Proposal

**State:** PROPOSED ONLY / NOT FROZEN. **Finding:** GAIA-B01 verified against FCA §23 and RDMS-10 Draft v1.0.

## Original FCA canonical type (owner L2)

```text
CapabilityResult {
    patch_proposal?
    proposed_claims[]
    proposed_hypotheses[]
    proposed_information_needs[]
    evidence_refs[]
    tool_requests[]
    experiment_requests[]
    confidence_assessment?
    specialist_request?
    needs[]
    rationale_summary?
}
```

## Colliding RDMS-10 Draft integration result

```text
CapabilityResult {
    invocation_id
    proposal_refs[]
    information_need_refs[]
    tool_request_refs[]
    experiment_request_refs[]
    assessment_refs[]
    dependency_set_ref
    provenance_refs[]
    result_status
}
```

The RDMS-10 structure is a **transport receipt/projection**, not the canonical semantic result. Both types must NOT use the same semantic name.

## Minimal nonbreaking proposed migration

```text
CapabilityTransportResult {
    invocation_id
    canonical_capability_result_ref
    transport_status
    transport_provenance_ref?
    dependency_set_ref?
}
```

The transport reference MUST resolve to the complete unmodified FCA `CapabilityResult`. Materialized fields may be added only with validated type mappings; no field can be silently substituted with an unrelated list of reference IDs. This is a possible minimal shape, **not approved final schema**.

## Field preservation obligations

| FCA field | Mandatory preservation mechanism |
|---|---|
| patch_proposal? | Retained in referenced FCA result |
| proposed_claims[] | Retained, including identity and source semantics |
| proposed_hypotheses[] | Retained, no promotion to fact |
| proposed_information_needs[] | Retained, preserves unknowns |
| evidence_refs[] | Retained without manufacturing evidence |
| tool_requests[] | Retained, not automatically substituted by action IDs |
| experiment_requests[] | Retained, not automatically executed |
| confidence_assessment? | Retained as assessment, not proof |
| specialist_request? | Retained as proposal, not recruitment authority |
| needs[] | Retained, no silent omission |
| rationale_summary? | Retained as non-authoritative text |

## Required acceptance cases

- Canonical-to-transport-to-canonical round-trip preserves all 11 FCA fields, nullability and list semantics.
- Partial fields remain optional according to FCA, never silently filled by guessed content.
- Transport status cannot authorize a canonical commit or world mutation.
- Version and provenance are checked at public boundary.
- No code/test consumer treats the transport type as owning semantic meaning.
- Frozen RDMS-10 requires **explicit controlled amendment** before this rename becomes normative.

**GAIA-B01:** proposal prepared; not yet formally closed. **GAIA-B02:** source import remains blocked.
