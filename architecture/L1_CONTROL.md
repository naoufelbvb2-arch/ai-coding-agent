# L1 CONTROL

**Document status: CONTROL LAWS SOURCE-VERIFIED; EVENT/AGGREGATE SERIALIZATION QUESTIONS ISOLATED; NOT FROZEN.** Source baselines retain their recorded specification freeze; this consolidation has no new freeze authority. Production implementation is not authorized.

L1 owns the authoritative control persistence boundary and its deterministic replay representation. Semantic ownership of stored cognitive, action, temporal, memory and recovery entities remains with their defining layer.

Each source-backed article is current only within its stated scope. Imported contracts retain the named owner; storage, delivery and scheduling do not create additional authorization. Source text remains unchanged in the archive. Source spelling and optionality are preserved; unspecified serialization types are not invented.


## Imported and exported boundaries

| Contract / responsibility | Canonical owner | This layer's obligation |
|---|---|---|
| Constitutional authority and content trust | [L0](../architecture/L0_FOUNDATION.md) | Enforce domain-scoped authority and non-bypassable frozen law. |
| Executive authorization and canonical cognitive entity mutations | [L2](../architecture/L2_COGNITION.md) | Commit owner-authorized changes, without independently deciding cognition. |
| Observation ingress, ActionRecord and Action Journal | [L3](../architecture/L3_ACTIONS.md) | Serialize raw observation append under its legal authority; retain world-effect reconciliation boundary. |
| Trigger reactions, specialists and dependency freshness | [L4](../architecture/L4_TEMPORAL_SPECIALISTS.md) | Atomically persist jointly required metadata and consult the sole freshness engine. |
| Memory promotion and revision | [L5](../architecture/L5_MEMORY.md) | Require Executive/LearningGate governance and durable artifact identity. |
| Recovery admission, suspension integrity and replay safety | [L6](../architecture/L6_RECOVERY.md) | Use scoped lawful recovery transitions and the recovery barrier. |
| Transport delivery of control requests | [L7](../architecture/L7_RUNTIME_INTEGRATION.md) | Receiving admission verifies source-owned authority; delivery is not a commit. |


## Effective control requirements

R1 expressly replaces the full-event-sourcing/sole-ledger projection model, gapless numbering, prematurely fixed ID algorithm, actor/authority conflation, prior snapshot/status shape and entity concurrency assumptions. Unchanged project isolation, immutable artifacts, timestamp meaning and external-effect separation remain in force.


### L1-C01

One committed ControlTransaction is authoritative. Current canonical entity state and append-only replay/control history become authoritative atomically. Neither representation creates a competing legal truth source; full event sourcing is not required.

Source: [RDMS-01-M01-U000](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1305>); [RDMS-01-M01-U001](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1336>); [FCA-48](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1921>); [FCA-49](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1949>).

### L1-C02

Every successful ControlCommit validates, allocates commit_seq, applies entity mutations, appends replay mutations and semantic events, advances ProjectHead and commits in one transaction. All these recoverability-critical writes become durable together or none do.

Source: [RDMS-01-M01-U001](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1336>); [FCA-48](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1921>); [FCA-49](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1949>).

### L1-C03

ProjectHead records the legal project head: current committed sequence, Executive epoch, state schema and durable project status. It coordinates serialization, fencing, recovery and schema checks; it is not a cognitive memory.

Source: [RDMS-01-M01-U002](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1377>).

### L1-C04

commit_seq is strictly increasing and unique per project. Physical contiguity is not required. Replay selects commits later than the snapshot's through_commit_seq in ascending legal order; it does not require every integer N+1 to exist. Event ordinal orders representation within an atomic commit, not external-world chronology.

Source: [RDMS-01-M01-U003](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1403>); [RDMS-01-M01-U010](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1634>).

### L1-C05

Use the current ControlCommit and AuthorityContext source declarations below. EXECUTIVE applies to cognitive changes, promotion, action authorization and specialist integration; OBSERVATION_INGRESS admits raw observations; RUNTIME_SYSTEM and RECOVERY authorize only architecturally permitted deterministic/reconciliation transitions. Authority kind alone grants no power: CommitGate validates transition eligibility and the applicable authority reference/epoch.

Source: [RDMS-01-M01-U004](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1430>); [RDMS-01-M01-U005](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1455>).

### L1-C06

The proposer/initiator, semantic authorizer and runtime writer are separate roles. Do not infer authorization from initiator identity. The runtime records initiator_ref and authority_context and writes only the authorized transition.

Source: [RDMS-01-M01-U006](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1504>).

### L1-C07

Every canonical mutation has a deterministic replay representation. CREATE, REPLACE and TOMBSTONE use expected ABSENT or an expected entity version, a new entity version, payload schema and the committed after-image or payload reference. After-image semantics are the Runtime v1 preference; recovery replays committed results without invoking the LLM, capability or original engineering reasoning.

Source: [RDMS-01-M01-U007](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1526>); [RDMS-01-M01-U008](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1566>).

### L1-C08

Semantic ControlEvents carry meaning, audit and lifecycle history; CanonicalMutations carry replay state. They are distinct and immutable after commitment. Preserve FCA's mandatory canonical-event metadata requirement: event_id, schema_version and idempotency_key. The relationship to the R1 ControlEvent fields is the explicitly isolated CE-01 question below; no metadata deletion or guessed serializer is authorized.

Source: [RDMS-01-M01-U009](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1600>); [FCA-48](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1921>).

### L1-C09

IDs are opaque, stable, typed, non-reusable and globally unique within the required domain. Type identities must not be mixed. UUIDv7 is only an implementation candidate, not a frozen ID algorithm.

Source: [RDMS-01-M01-U011](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1646>).

### L1-C10

Mutable canonical entities carry entity_version, created_commit_seq and updated_commit_seq. Creation requires expected ABSENT and new_version 1; update requires the current version and increments it by one. Blind overwrite is illegal. Runtime v1 conflicts are whole-entity conflicts; automatic field-level merging is forbidden. Re-read/reconcile outside the transaction and issue a new proposal.

Source: [RDMS-01-M01-U012](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1679>); [RDMS-01-M01-U013](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1700>).

### L1-C11

WRITE_CONFLICT means the intended write target changed; DEPENDENCY_STALE means a reasoning dependency changed, even if that dependency is not being written. A successful write compare-and-set does not prove dependency freshness. Freshness decisions use the L4 owner contract.

Source: [RDMS-01-M01-U014](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1732>).

### L1-C12

A redeliverable canonical command carries idempotency_key and request_fingerprint. The recorded identity scope is (project_id, operation_scope, idempotency_key), associated with commit_id and fingerprint. Same key/fingerprint returns the original result; different fingerprint yields IDEMPOTENCY_CONFLICT. Canonical mutation keys have no automatic TTL.

Source: [RDMS-01-M01-U015](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1750>).

### L1-C13

Keep control_schema_version, event_type_version, payload_schema_version and snapshot_codec_version distinct. Immutable historical events may be deterministically decoded/upcast but never rewritten; migration preserves their historical meaning and deterministic replay.

Source: [RDMS-01-M01-U016](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1768>).

### L1-C14

Normal restart may read intact current state directly when its applied marker matches ProjectHead. A snapshot accelerates rebuilding; it is not a truth prerequisite. Rebuild loads a valid snapshot and replays later CanonicalMutations. Snapshot hashes validate actual encoded payload bytes; a semantic hash requires a separately defined canonical serialization.

Source: [RDMS-01-M01-U017](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1795>); [RDMS-01-M01-U018](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1822>).

### L1-C15

CanonicalStore.applied_through_commit_seq equals ProjectHead.latest_commit_seq in the intact state. A lower applied marker requires missing-commit replay. A greater marker claims history absent from the authoritative head and is CORRUPTION/FAILED_SAFE; do not normalize it into an accepted head.

Source: [RDMS-01-M01-U019](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1848>).

### L1-C16

Large artifacts are outside the ledger, but a reference cannot be committed before bytes are durable and their hash verified. Preserve PREPARED, REFERENCED, ORPHAN and RETIRED artifact lifecycle semantics. RECOVERY_CRITICAL content is not garbage-collected while canonical state or replay history depends on it. Changed bytes require a new artifact identity/hash.

Source: [RDMS-01-M01-U020](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1870>).

### L1-C17

Indexes and caches are disposable, non-authoritative derived state. IndexMetadata records generation, the source fingerprint and available repo/commit frontier, with BUILDING/CURRENT/STALE/FAILED status. An index cannot independently establish canonical truth or negative-query freshness.

Source: [RDMS-01-M01-U021](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1900>).

### L1-C18

A dependency RepoRef denotes an identifiable COMMIT, IMMUTABLE_WORKING_SNAPSHOT or SANDBOX_SNAPSHOT, with revision and content fingerprint. A mutable filesystem path is not an immutable repository reference. WorldRef represents only the operation-relevant world/environment dimensions, not an omniscient world snapshot.

Source: [RDMS-01-M01-U022](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1926>); [RDMS-01-M00-U027](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L764>).

### L1-C19

Durable ProjectStatus is ACTIVE/SUSPENDED/ARCHIVED/FAILED_SAFE. ProcessRuntimeMode is INITIALIZING/RECOVERING/READY/DEGRADED/STOPPING and is process-local. Startup initializes/recoveries anew and becomes READY only after the recovery barrier; READY cannot be treated as a lasting project fact after a process dies.

Source: [RDMS-01-M01-U023](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1952>).

### L1-C20

Fast recovery opens the authoritative store, reads ProjectHead, checks the applied sequence, acquires/fences the Executive epoch, inspects unresolved actions, replays triggers, validates specialists/dependencies and crosses the RecoveryBarrier before READY. Rebuild reconstructs current state from a valid snapshot plus replay and verifies it against ProjectHead before normal reconciliation. Neither route relies on chat history or re-running reasoning.

Source: [RDMS-01-M01-U024](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1984>).

### L1-C21

Raw observation append need not receive Executive semantic authorization, but it still enters ControlTransaction and receives legal per-project commit ordering. Concurrent ingress and Executive transitions do not race an independently writable ledger head.

Source: [RDMS-01-M01-U025](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L2019>).

### L1-C22

The storage engine prevents dirty canonical reads, lost updates, double allocation of authority and partial ControlCommit. No named SQL isolation level or particular database engine is frozen. Required storage semantics include ACID control transactions, uniqueness, monotonic per-project ordering, optimistic entity versions, durable acknowledgement, append-only history and crash recovery.

Source: [RDMS-01-M01-U026](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L2044>); [RDMS-01-M00-U044](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1132>).

### L1-C23

Each ProjectRuntime has independent canonical state, Executive epoch, commit ordering, Action Journal and trigger lifecycle even when projects share a physical process or database. Immutable observations, raw episodes and committed events are corrected by new records/relations, not by overwriting captured history. commit_seq defines legal ordering; wall-clock timestamps serve temporal reasoning, latency, timeout and forensic purposes.

Source: [RDMS-01-M00-U000](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L25>); [RDMS-01-M00-U010](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L325>); [RDMS-01-M00-U025](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L703>).

### L1-C24

Do not implicitly enlist a filesystem, GitHub, production database or external API in ControlTransaction. Durable local intent precedes external effect; observation and reconciliation establish what happened. A control commit or leadership handoff does not erase dispatched world effects. ActionGate/Action Journal ownership remains L3; recovery admission remains L6.

Source: [RDMS-01-M00-U036](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L950>); [FCA-50](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1967>); [FCA-51](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1989>).

### L1-C25

global_state_version equals the latest legally committed per-project commit_seq, including observation append. It is historical ordering, not semantic freshness; entity_version changes only for that entity. The original uint64 declaration for these counters remains a source constraint; R1 relaxes contiguity, not typed counter meaning.

Source: [RDMS-01-M00-U004](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L144>); [RDMS-01-M00-U008](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L261>); [RDMS-01-M00-U009](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L287>); [RDMS-01-M01-U003](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1403>); [RDMS-01-M01-U012](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1679>).

### L1-C26

Preserve correlation_id for task/intent lineage and causation_id for the immediate triggering event/command. Semantic transition classes are COGNITIVE_COMMIT, OBSERVATION_APPEND, CONTROL_LIFECYCLE, MEMORY_PROMOTION and WORLD_ACTION_LIFECYCLE; these are not five databases. Raw observation append validates schema/provenance/integrity and cannot smuggle in interpretation. Learning promotion requires proposal, LearningGate, Executive authorization and traceable lifecycle. Disposable isolated sandbox micro-actions may aggregate under SandboxActivityRecord.

Source: [RDMS-01-M00-U024](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L664>); [RDMS-01-M00-U029](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L825>); [RDMS-01-M00-U030](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L843>); [RDMS-01-M00-U031](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L861>); [RDMS-01-M00-U032](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L885>); [RDMS-01-M00-U033](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L899>); [RDMS-01-M00-U034](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L915>).

### L1-C27

After failure, distinguish definitely committed, definitely uncommitted, possibly world-effecting, unresolved and required reconciliation work. If losing one half of control metadata while preserving its required partner would make recovery ambiguous, both share the authoritative transaction. Search/index/cache state cannot override current canonical state or legal committed history.

Source: [RDMS-01-M00-U035](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L928>); [RDMS-01-M00-U041](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1072>); [RDMS-01-M00-U012](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L370>); [RDMS-01-M01-U000](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1305>).

### L1-B02 — 2. طبقات البيانات الدائمة

الـruntime يميز خمسة أنواع من البيانات:

1. Control Ledger
2. Canonical Entity State
3. Snapshots
4. Immutable Artifacts
5. Derived Indexes / Read Models

ولا تحمل كلها الدرجة نفسها من السلطة.

Source: [RDMS-01-M00-U001](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L62>); source-unit SHA-256 `f45c19613dac38ec26735a7b265c4a2c87519d76bf2ca9453bd6229ba103715c`.

## Owned source-defined record surfaces

These are the exact current R1 declarations and unchanged artifact/world reference declarations. They state source spelling, collections, enums and optionality; they do not imply a production serialization API. Source-independent fields are not added.


### ProjectHead

```text
ProjectHead {
    project_id

    latest_commit_seq

    current_executive_epoch

    state_schema_version

    project_status

    updated_at
}
```

Source: [ProjectHead](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1381>); declaration SHA-256 `3bc7d2b7acaed1be1112f6c50a54b258506dc586f87fe6adf1af2e4deac17962`.

### ControlCommit

```text
ControlCommit {
    commit_id

    project_id
    commit_seq

    control_schema_version

    authority_context

    idempotency_key
    request_fingerprint

    correlation_id?
    causation_ref?

    initiator_ref

    mutations[]

    events[]

    committed_at
}
```

Source: [ControlCommit](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1431>); declaration SHA-256 `41502380fc6597de922a89d6827a323f77c3f445e3f4c795a7bb04930990a837`.

### AuthorityContext

```text
AuthorityContext {
    kind:
        EXECUTIVE
        OBSERVATION_INGRESS
        RUNTIME_SYSTEM
        RECOVERY

    executive_epoch?
    authority_ref?
}
```

Source: [AuthorityContext](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1465>); declaration SHA-256 `5a758ca3a3800606fa25f5fbde90eb542cc48be9605f1ce31833e8f1058759f0`.

### CanonicalMutation

```text
CanonicalMutation {
    mutation_id

    entity_kind
    entity_id

    operation:
        CREATE
        REPLACE
        TOMBSTONE

    expected:
        ABSENT
        or entity_version

    new_entity_version

    payload_schema_version

    after_image
        or payload_ref
}
```

Source: [CanonicalMutation](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1530>); declaration SHA-256 `8735b403de80146409ebf3cb7f07f3e532f0a4489b87d36ab48448ade9101aea`.

### ControlEvent

```text
ControlEvent {
    event_id

    event_type
    event_type_version

    ordinal

    payload
}
```

Source: [ControlEvent](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1604>); declaration SHA-256 `b345887249f8d33f7076b03b8bc74d2e5f1ccf4aabbfc0d972edbaa11b571289`.

### Snapshot

```text
Snapshot {
    snapshot_id
    project_id

    through_commit_seq

    state_schema_version
    snapshot_codec_version

    payload_ref
    payload_hash

    created_at
}
```

Source: [Snapshot](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1823>); declaration SHA-256 `05c04f8bf27077be5fa63949d40e58ccace4ab71aff3d26c78555ca0eb98233d`.

### IndexMetadata

```text
IndexMetadata {
    index_id
    index_kind

    generation

    built_from_repo_ref?
    built_through_commit_seq?

    source_fingerprint

    status:
        BUILDING
        CURRENT
        STALE
        FAILED
}
```

Source: [IndexMetadata](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1906>); declaration SHA-256 `fecc7438d05e1aa44ed6b0baf0f4981efef8a5a1c667df9b7f49d4b2686af85f`.

### RepoRef

```text
RepoRef {
    repository_id

    revision_kind:
        COMMIT
        IMMUTABLE_WORKING_SNAPSHOT
        SANDBOX_SNAPSHOT

    revision_id
    content_fingerprint

    parent_revision?
}
```

Source: [RepoRef](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1936>); declaration SHA-256 `75d279714763039a77d15948df4853c3e0c2519da0065a02ca4f2b9e8f7ccc90`.

### ProjectStatus

```text
ProjectStatus {
    ACTIVE
    SUSPENDED
    ARCHIVED
    FAILED_SAFE
}
```

Source: [ProjectStatus](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1957>); declaration SHA-256 `37c1db84494587d1d9e13d5ac525db94f7475b44360d83d78d2b4aada1cb4dac`.

### ProcessRuntimeMode

```text
ProcessRuntimeMode {
    INITIALIZING
    RECOVERING
    READY
    DEGRADED
    STOPPING
}
```

Source: [ProcessRuntimeMode](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1964>); declaration SHA-256 `5517694d77348cb192c92afbaccc64d219757f6e5d5d079b76dbef161ea7add7`.

### ArtifactRef

```text
ArtifactRef {
    artifact_id

    content_hash

    media_type

    byte_size

    storage_locator

    created_at

    provenance

    retention_class
}
```

Source: [ArtifactRef](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L480>); declaration SHA-256 `cbf386420baffcd2ac8ed3ac296d737db7108a3dc78b0eb24f6f8702d0e7d415`.

### WorldRef

```text
WorldRef {
    environment_id

    dimensions[]
}
```

Source: [WorldRef](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L770>); declaration SHA-256 `7e734d3f93fa839bf286a319251d91b18e724cb4d4cbfd512686dad2c3fb8cb4`.

## Remaining bounded serialization questions

**CE-01:** FCA §48 requires every canonical event to include `event_id`, `schema_version`, `idempotency_key`; RDMS-01 R1 §10's ControlEvent lists `event_id`, `event_type`, `event_type_version`, `ordinal`, `payload`. The sources do not explicitly equate a ControlEvent with the whole canonical event envelope, bind the inherited key to an enclosing commit, or rename schema_version to event_type_version. Both logical requirements remain mandatory. Their exact record/envelope mapping is not declared complete, and no lossy event serializer is approved.

**PR-01:** RDMS-01 baseline §1's ProjectRuntime aggregate references `control_head` and `runtime_status`; R1 introduces ProjectHead and separates durable project status from process-local mode. Project-scoped authority and all required semantics above are current. A revised literal ProjectRuntime transport/aggregate field shape is unspecified; a schema that preserves the old mixed RuntimeStatus as current law is rejected. This does not block implementation-independent control laws or unrelated owner contracts.


## Amendment and baseline coverage

All R1 §§1–28 are represented in the effective rules and record surfaces; §28's RDMS-I01…22 invariants constrain those rules. R1 §29 is a documentary adversarial retest, §30 admits the corrected specification, and §31 is historical phase progression rather than new law. Baseline §§1–47 are reconciled by the scoped replacement ledger; §48 is historical next-phase material. The original baseline ArtifactRef/WorldRef, project isolation, immutability, logical/wall-clock separation and external-transaction prohibition remain effective. Actor identity remains distinct from authority; LedgerHead and mixed RuntimeStatus are not exported as competing current canonical definitions. The L4-owned DependencyStamp is imported, not redefined by its older L1 foundation sketch.


### L1-R1-INVARIANTS — 28. Revised Runtime Invariants

RDMS-I01
The authoritative persistence unit is ControlCommit.

RDMS-I02
Current canonical entity state and its corresponding replay/control
records become authoritative atomically.

RDMS-I03
No implementation may create independent dual authorities between
the current-state store and Control Ledger.

RDMS-I04
Per-project commit_seq defines canonical commit ordering and is
strictly increasing; physical contiguity is not required.

RDMS-I05
Committed ControlEvents and replay mutations are immutable.

RDMS-I06
Every committed canonical entity mutation must have a deterministic
replay representation that does not invoke reasoning providers.

RDMS-I07
Canonical current-state records are read directly during normal
operation; replay is a recovery/audit mechanism, not the normal read path.

RDMS-I08
Current state must declare the ControlCommit through which it is applied.

RDMS-I09
Global commit ordering and per-entity versioning remain distinct.

RDMS-I10
Canonical create/update operations use compare-and-set semantics
against ABSENT or an expected entity version.

RDMS-I11
Automatic field-level conflict merging is forbidden in Runtime v1.

RDMS-I12
Idempotency key and request fingerprint together identify retry
of one semantic control operation.

RDMS-I13
Historical events are never rewritten to perform schema migration.

RDMS-I14
Schema evolution must preserve historical meaning and deterministic replay.

RDMS-I15
Snapshots accelerate rebuild but are not required to preserve truth.

RDMS-I16
A committed artifact reference must point to durable,
integrity-verified immutable content.

RDMS-I17
Indexes and caches remain disposable derived state.

RDMS-I18
Mutable filesystem locations are not valid immutable RepoRefs.

RDMS-I19
Durable project lifecycle and process-local runtime mode are distinct.

RDMS-I20
Recovery must never re-run LLM reasoning merely to rediscover an
already committed canonical transition.

RDMS-I21
Observation append may bypass Executive semantic authorization,
but not the authoritative ControlTransaction boundary.

RDMS-I22
External world systems never participate implicitly in the
ControlTransaction; they remain governed by Action reconciliation.

Source: [RDMS-01-M01-U027](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L2057>); source-unit SHA-256 `a14552dde0d648307514312e53513cf34e15f8d3574e5ae5508b3a406724061d`.

## Single-owner record contracts

The owner registry distinguishes source record declarations from callable or transport signatures. Source fields marked `?` retain optionality and `[]` retain collection shape; primitive types not declared by the source remain unspecified. An abbreviated `...` correction is not permission to discard other fields. Multi-surface or parent-field preservation questions are explicitly bounded below; their declarations must not be treated as a proved conversion API.

### ActorRef

Canonical owner: L1; defining specification: RDMS-01.

Source: [ActorRef](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L641>); declaration SHA-256 `7017beaf9910b320a76077762f8f0ac5eb641708c6bd383dfbe89ac041ef7eee`.

```text
ActorRef {
    actor_type:
        runtime
        executive
        capability
        specialist
        human
        tool
        trigger

    actor_id?
}
```

### EntityEnvelope

Canonical owner: L1; defining specification: RDMS-01.

Source: [EntityEnvelope](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L301>); declaration SHA-256 `4ffaa637e7a28c4de98efd92af4d2b7d700747ce59ddbcb62c9fa455559f493c`.

```text
EntityEnvelope {
    entity_id
    entity_kind

    entity_version

    created_commit_seq
    updated_commit_seq

    status

    payload
}
```

### LeadershipGrant

Canonical owner: L1; defining specification: FCA.

Source: [LeadershipGrant](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1970>); declaration SHA-256 `4a80286f2836d43a7b85b643eddb100fd4f0063ada1fc4e47cd308bfad19e82f`.

```text
LeadershipGrant {
    project_id
    executive_id
    epoch
    status
    acquired_at
}
```

### ProjectRuntime

Canonical owner: L1; defining specification: RDMS-01.

Source: [ProjectRuntime](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L33>); declaration SHA-256 `fe0b217ab857240617ab25d12f48cb2865064d86a4cdd3af7c3c0962bf3751b1`.

**Representation detail DEFERRED TO IMPLEMENTATION DESIGN.** The operative rules in this document apply; no complete replacement declaration is asserted. Every exact candidate and its field spelling remains in the source registry; the binding obligations and intentionally unspecified representation detail are recorded in the targeted review below. Parent-field questions remain separately classified.

- [Original draft](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L33>); SHA-256 `fe0b217ab857240617ab25d12f48cb2865064d86a4cdd3af7c3c0962bf3751b1`.


The document's independent control rules and retained record declarations are source-grounded. CE-01/PR-01 prevent asserting a complete event/aggregate mapping or complete layer-wide field reconciliation. Verification must preserve every archived source hash and check these explicit limitations rather than reporting full completion.

## Owned FCA invariant obligations

These parent duties retain their semantic force. Scoped RDMS amendments determine effective record lifecycle and representation; derived staleness must not be confused with a canonical lifecycle mutation.

**FCA-I32** — Only the current Executive epoch may authorize new canonical effects.

Source: [FCA-I32](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2987>).

**FCA-I33** — Leadership loss fences future authority but does not erase already-dispatched world effects.

Source: [FCA-I33](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2989>).

**FCA-I37** — Recoverability-critical control metadata commits atomically.

Source: [FCA-I37](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2997>).

## Targeted normative reconciliation

This targeted review uses the published consolidation as its baseline. Classes B/E remain open; C defers only the stated representation detail; D is source-determined. These dispositions supply no new architectural decision, serializer alias, threshold or authority.

### L1-NR-SHAPE-ProjectRuntime

**C — IMPLEMENTATION_DETAIL_DEFERRED; DEFERRED_TO_IMPLEMENTATION_DESIGN.**

R1 explicitly provides ProjectHead, the atomic current-store/ledger boundary and separate durable ProjectStatus/process-local ProcessRuntimeMode. Only the aggregate embedding names remain unspecified; there is no missing authority or recovery state definition.

**Binding obligations:** One authoritative ControlTransaction atomically advances current state and replay/control records. ProjectHead carries the legal head/epoch/schema/status. Startup resets process mode and requires RecoveryBarrier before READY. Never persist READY as durable project truth.

**Remaining detail / acceptance limit:** ProjectRuntime aggregate member names, class layout and lookup arrangement. These cannot merge ProjectStatus with ProcessRuntimeMode or create a second control head.

Exact authoritative evidence: [RDMS-01-M01-U000](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1305>); [RDMS-01-M01-U001](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1336>); [RDMS-01-M01-U002](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1377>); [RDMS-01-M01-U023](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1952>); [RDMS-01-M00-U000](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L25>).

### L1-NR-CE-01

**B — LOSSLESS_MAPPING_REQUIRED; OPEN_MAPPING_PROOF.**

FCA says each canonical event includes at least event_id/schema_version/idempotency_key; R1 adds event_type_version and separates schema dimensions. These requirements can coexist, so this is not a proved contradiction. R1 does not explicitly waive the two FCA members or equate them with enclosing commit metadata.

**Binding obligations:** Preserve event_id, schema_version and idempotency_key for every canonical event, alongside R1 event type/version, ordinal and payload. Preserve ControlCommit control_schema_version, command idempotency_key/fingerprint and immutable events. Do not conflate event, payload, control and snapshot codec versions.

**Remaining detail / acceptance limit:** Prove event metadata inclusion/resolution and its exact scope. No schema_version = event_type_version/control_schema_version or event key = enclosing commit key is approved. The original warning is narrowed to this precise binding proof.

Exact authoritative evidence: [FCA-48](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L1921>); [RDMS-01-M01-U004](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1430>); [RDMS-01-M01-U009](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1600>); [RDMS-01-M01-U015](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1750>); [RDMS-01-M01-U016](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt#L1768>).
