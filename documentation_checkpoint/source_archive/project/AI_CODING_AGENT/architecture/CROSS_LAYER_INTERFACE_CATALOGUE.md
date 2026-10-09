# GAIA-C02 — Cross-Layer Interface Ownership Catalogue (specification candidate)

**Status: CANDIDATE, NOT FROZEN.** Twelve tracked interfaces. This defines legal boundary, not unverified Python function signatures or storage transactions.

| Route | Producer / consumer | Legal witness and rule | Control boundary |
|---|---|---|---|
| X8-01 | L2 → L7 → L2 | Capability invocations: Canonical ref required, semantically reversible, no direct commit | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-02 | L5 → L7 → L2 | Memory retrieval: Preserve omitted scope/ranking/coverage/freshness by legal ref | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-03 | L2 → L4 → L1 | Temporary obligations: One legal Commitment, explicit reactivation root, atomic continuation | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-04 | L4 → L1 → L3 | Trigger to action: Stable trigger generation/reaction identity + ActionGate | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-05 | L4 → L6 → L1 | Suspension/resumption: Pinned durable payload; corrupt means recovery quarantine | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-06 | L2 → L3 → L1 | Code/world change: Sealed exact operation + recoverable attempt history + journal | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-07 | L3 → L2 → L1 | Observation to belief: Accepted evidence with source cardinality and FactGrounding; no raw report authority | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-08 | L2 → L3 → L2 | Experiment and causality: Persisted preintervention prediction; verification matrix + separate design/run states | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-09 | L3 → L2 | Contradictory reality: Nonterminal unresolved remains, explanation separate from comparison | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-10 | L4 → L2 → L1 | Freshness and finalization: RDMS-06 single freshness owner; preserve scope and finalization evidence | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-11 | L3 → L5 → L7 | Learning and egress: No auto learning; sealed outbound context and lineage | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |
| X8-12 | L3 → L6 → L1 | Sandbox and recovery: Containment proof; world effects default SHARED_WORLD if uncertain | Legal mutation must use existing canonical owner, CommitGate or ActionGate as applicable |

## Cross-cutting prohibitions

- Transport workers cannot create canonical writes: use owning service and existing CommitGate/ActionGate.
- Where durable control and Action Journal are physically separate, specify commit boundary and repairable recovery handoff; do not assert an atomic world transaction.
- A trigger occurrence acceptance may durably create follow-up obligations but never silently authorizes an external action.
- Independent Observation ingress is not proof of causal attribution; causal evidence requires matching provenance and state.
- A provider disclosure decision is bound to exact egress destination and bytes; no worker inherits a previous broad approval.
- Stale epochs or ambiguous external effects require fencing, IN_DOUBT and reconciliation rather than speculative retry.

## Publication gate

Before a final freeze, each interface needs a single owner for command signature, required/optional fields, pre/post-conditions, idempotency and error states; this catalogue presently identifies the 12 witnessed paths but does not yet reproduce all formal source schemas.
