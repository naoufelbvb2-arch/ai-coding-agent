# L1_CONTROL — Effective normative composition candidate


**STATUS: CONSOLIDATION CANDIDATE — NOT FROZEN.** This is a direct source-based, self-contained layer view. FCA v1.0.1 and frozen RDMS decisions control. This document is not authority for new code or world effects.


**Responsibility:** Durable canonical state, ControlCommit, sequencing and replay.


**Reading rule (essential):** Later approved RDMS corrections override incompatible earlier RDMS draft clauses. Undisturbed draft provisions remain inherited. A review narrative, rejected alternative, test illustration or future proposal is not a normative instruction. Approved source quotations appear in their original form. If an exact clause relationship remains unproved, it is a FREEZE HOLD rather than a guessed merge.


**Source boundary:** legacy accumulated GAIA notes are archived in `../reviews/source_archive/pre_normative_merge_L0_L7/`; no older "CURRENT" heading in that archive is authoritative.


---
## 1. Current source-proven legal resolutions


### C04-W01 — Event-sourcing projection-only assertion replaced by one authoritative ControlCommit atomic mutation+ledger model

**Relation:** `SOURCE_BACKED_EXPLICIT_SUPERSESSION`; **RDMS:** `RDMS-01`; **source message:** `e3a45231-ddae-4ed4-9bd1-35202ecdfcf7`; **source lines:** `13–41`; **SHA-256:** `d29448b2272dfda4a3b27e753fc2cd52c2bf8616d4d2ed78d7c6d2993aad4bff`.

**Application rule:** approved later source governs over incompatible historical baseline. No automatic deletion of unrelated baseline fields is implied.

**Verbatim effective source:**

````text

النموذج السابق:

Control Ledger
= sole source of truth

Canonical State
= projection only

صحيح نظريًا، لكنه يدفعنا نحو Event Sourcing كامل حتى في الأماكن التي لا نحتاجه فيها.

يُستبدل بالنموذج التالي:

             ControlCommit
        AUTHORITATIVE UNIT
                 │
        ┌────────┴────────┐
        ▼                 ▼
Current Canonical     Append-only
Entity State          Control Ledger
        │                 │
fast current reads    history / audit /
                     deterministic replay

ليس لدينا مصدران مستقلان للحقيقة.

لدينا عملية commit authoritative واحدة تكتب الاثنين ذريًا.

The authority is the committed ControlTransaction, not one physical representation of it.
````


### C04-W02 — ControlCommit fields and authority-context distinction are replaced in R1

**Relation:** `SOURCE_BACKED_EXPLICIT_SUPERSESSION`; **RDMS:** `RDMS-01`; **source message:** `e3a45231-ddae-4ed4-9bd1-35202ecdfcf7`; **source lines:** `137–181`; **SHA-256:** `c83de9a9553b65c3a139916affdce723eea7d38ed47e55069ab4d5cfbac61080`.

**Application rule:** approved later source governs over incompatible historical baseline. No automatic deletion of unrelated baseline fields is implied.

**Verbatim effective source:**

````text
5. ControlCommit النهائية
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
6. Authority Context

وجود:

executive_epoch?

وحده غامض لأن بعض العمليات لا تحتاج Executive أصلًا.

نستبدله بـ:

AuthorityContext {
    kind:
        EXECUTIVE
        OBSERVATION_INGRESS
        RUNTIME_SYSTEM
        RECOVERY

    executive_epoch?
    authority_ref?
}
````


### C04-W03 — commit_seq strictly increasing, not necessarily gapless

**Relation:** `SOURCE_BACKED_CLARIFICATION`; **RDMS:** `RDMS-01`; **source message:** `e3a45231-ddae-4ed4-9bd1-35202ecdfcf7`; **source lines:** `110–137`; **SHA-256:** `53c8d06b7bf541df061035e7d171577463fb4f467507494577f8f17a747c9e7e`.

**Application rule:** approved later source governs over incompatible historical baseline. No automatic deletion of unrelated baseline fields is implied.

**Verbatim effective source:**

````text
4. commit_seq

القاعدة تصبح:

strictly increasing
unique per project

ولا نشترط:

gapless

لأن gap في رقم داخلي لا يغير semantics.

الصحيح هو:

commit A < commit B
iff
A.commit_seq < B.commit_seq

Recovery تستخدم:

WHERE commit_seq > snapshot.through_commit_seq
ORDER BY commit_seq

ولا تعتمد على:

N + 1 must physically exist
5. ControlCommit النهائية
````


### C04-W04 — Physical UUID choice made implementation boundary; typed IDs still required

**Relation:** `SOURCE_BACKED_CLARIFICATION`; **RDMS:** `RDMS-01`; **source message:** `e3a45231-ddae-4ed4-9bd1-35202ecdfcf7`; **source lines:** `366–384`; **SHA-256:** `5f84daf6df802c2f997f8818b725e3e745af4b831d0c53bdad2a391f89fa95c5`.

**Application rule:** approved later source governs over incompatible historical baseline. No automatic deletion of unrelated baseline fields is implied.

**Verbatim effective source:**

````text
مثال:

ProjectId
GoalId
ClaimId
ActionId
ObservationId

ولا يجوز خلطها.

أما:

UUIDv7
ULID
other suitable implementation

فقرار Implementation Boundary لاحق.

UUIDv7 يبقى المرشح الافتراضي، وليس قانون RDMS.
````


---
## 2. Original FCA v1.0.1 frozen normative sections (verbatim)


**Authority:** `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md`. These are direct excerpts from the single frozen FCA document, allocated exactly once across L0–L7.


<!-- FCA-SECTION 6 PART 1; exact-source -->
## 6. Canonical Cognitive Workspace

The Workspace is the structured, persistent representation of the current accepted cognitive state of the project.

It replaces the idea that chat history is the agent’s mind.

A canonical state contains at least:

```text
State {
    identity

    goals
    focus

    model

    epistemic

    engineering

    execution

    temporal

    specialists

    memory_refs

    meta
}
```

### 6.1 Identity

```text
Identity {
    project_id
    global_state_version
    repo_ref
    schema_version
    current_executive_epoch
}
```

`global_state_version` establishes historical order. It MUST NOT be treated as sufficient proof that a specialist result is stale.

### 6.2 Goals

The agent maintains a hierarchy:

```text
Mission
  ↓
Milestone
  ↓
Task
  ↓
Subgoal
  ↓
Current cognitive operation
```

Every executable Slice MUST trace to a Goal.

### 6.3 Focus

Working cognition is intentionally bounded. The Workspace represents what is actively relevant without loading the whole project.

### 6.4 System Mental Model

The mental model contains at least:

```text
SystemMentalModel {
    domain
    structure
    runtime
    causal
    risk
}
```

It is a revisable belief state, not immutable documentation.

---

# Part IV — Epistemic model
<!-- /FCA-SECTION -->


<!-- FCA-SECTION 48 PART 1; exact-source -->
## 48. Control Ledger

The Control Ledger is the authoritative durability boundary for control-plane state.

It stores or atomically references at least:

```text
Executive Epoch
Canonical cognitive commits
Action lifecycle
Trigger lifecycle
Specialist lifecycle
Memory promotions
Goal/task lifecycle
```

Large artifacts may live elsewhere, but recoverability-critical references and lifecycle metadata belong to the authoritative control boundary.

Each canonical event includes at least:

```text
event_id
schema_version
idempotency_key
```

---
<!-- /FCA-SECTION -->


<!-- FCA-SECTION 49 PART 1; exact-source -->
## 49. Atomic control transitions

Transitions whose control metadata is jointly required for recovery MUST commit atomically.

Example:

```text
DecisionAccepted
+
TriggerArmed
+
StateVersionAdvanced
```

must appear together or not at all.

---
<!-- /FCA-SECTION -->


<!-- FCA-SECTION 50 PART 1; exact-source -->
## 50. Executive epoch and fencing

```text
LeadershipGrant {
    project_id
    executive_id
    epoch
    status
    acquired_at
}
```

Only the current epoch may authorize new canonical effects.

Every authority-bearing operation includes `executive_epoch`.

If a new Executive acquires epoch N+1, requests from older epochs are fenced.

Loss of leadership does not erase world effects already durably dispatched.

---
<!-- /FCA-SECTION -->


<!-- FCA-SECTION 51 PART 1; exact-source -->
## 51. Leadership handoff

A new Executive performs:

```text
1. acquire new epoch
2. fence old authority
3. inspect unfinished actions
4. inspect specialists
5. inspect pending triggers
6. inspect blocked/waiting work
7. reconcile before new conflicting effects
```

An action that was only `AUTHORIZED` under an old epoch requires explicit adoption by the new Executive.

An action at `DISPATCH_INTENT` or later enters reconciliation.

---
<!-- /FCA-SECTION -->


<!-- FCA-SECTION 74 PART 1; exact-source -->
## 74. Canonical cognitive mutation

```text
Capability
   ↓
PatchProposal
   ↓
Executive semantic authorization
   ↓
CommitGate
   ↓
Canonical Workspace commit
   ↓
Control Ledger
```

The Executive can authorize a legal change. It cannot make an illegal change legal.

---
<!-- /FCA-SECTION -->


---
## 3. RDMS corrective provisions and final normative freeze interpretations (approved source order)


### RDMS-01: corrective source (latest approved amendments control)


#### R1 corrections and final freeze decision — `e3a45231-ddae-4ed4-9bd1-35202ecdfcf7`

**Original message SHA-256:** `4398e8f667678ad2efcaf328720ff94857d9aac764a32411b78bd7d590c2860f`. **Source status:** approved corrective/final-freeze source message; contains some explanatory review material which is not separately normative. Where later approved sections in the same group replace earlier sections, the later one controls.

<!-- RDMS-MESSAGE e3a45231-ddae-4ed4-9bd1-35202ecdfcf7 SHA256 4398e8f667678ad2efcaf328720ff94857d9aac764a32411b78bd7d590c2860f -->

````text
راجعت RDMS-01 عدائيًا، وظهر فعلًا أن فرض event sourcing كامل سيكون ثقلًا غير ضروري. الـFCA لا تفرض ذلك؛ ما تفرضه هو Control Ledger كحد ديمومة authoritative، ذرية metadata الحرجة، وإمكانية recovery، مع كون الـphysical schema مفتوحًا. كما أن recovery المجمدة تعتمد على durable state وLedger، وليس على إعادة تشغيل reasoning أو LLM.

لذلك أصلحت RDMS-01 قبل أن نبني فوقه.

RDMS-01R1 — Runtime Foundations Correction & Freeze Review
Runtime & Data Model Specification v1.0
RDMS-01R1 — Runtime Foundations Correction

Parent: FCA v1.0.1 — FROZEN
Status after review: CANDIDATE FROZEN

1. النتيجة الرئيسية للمراجعة

النموذج السابق:

Control Ledger
= sole source of truth

Canonical State
= projection only

صحيح نظريًا، لكنه يدفعنا نحو Event Sourcing كامل حتى في الأماكن التي لا نحتاجه فيها.

يُستبدل بالنموذج التالي:

             ControlCommit
        AUTHORITATIVE UNIT
                 │
        ┌────────┴────────┐
        ▼                 ▼
Current Canonical     Append-only
Entity State          Control Ledger
        │                 │
fast current reads    history / audit /
                     deterministic replay

ليس لدينا مصدران مستقلان للحقيقة.

لدينا عملية commit authoritative واحدة تكتب الاثنين ذريًا.

The authority is the committed ControlTransaction, not one physical representation of it.

2. Hybrid Transactional Persistence Model

كل ControlCommit ناجحة تقوم داخل transaction واحدة بـ:

validate
↓
allocate commit_seq
↓
apply canonical entity mutations
↓
append replay mutations
↓
append semantic control events
↓
advance ProjectHead
↓
COMMIT

إما كل ذلك يصبح durable:

YES

أو:

NONE

وبالتالي القراءة اليومية لا تحتاج:

replay entire history

بل تقرأ مباشرة:

canonical current-state tables

بينما الـLedger يبقى:

immutable history
audit trail
recovery source
forensic source
replay source
3. ProjectHead

لكل مشروع سجل صغير يمثل الرأس القانوني للحالة:

ProjectHead {
    project_id

    latest_commit_seq

    current_executive_epoch

    state_schema_version

    project_status

    updated_at
}

ProjectHead نفسها لا تستخدم كذاكرة معرفية.

وظيفتها:

commit serialization
epoch fencing
recovery head
schema coordination
4. commit_seq

القاعدة تصبح:

strictly increasing
unique per project

ولا نشترط:

gapless

لأن gap في رقم داخلي لا يغير semantics.

الصحيح هو:

commit A < commit B
iff
A.commit_seq < B.commit_seq

Recovery تستخدم:

WHERE commit_seq > snapshot.through_commit_seq
ORDER BY commit_seq

ولا تعتمد على:

N + 1 must physically exist
5. ControlCommit النهائية
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
6. Authority Context

وجود:

executive_epoch?

وحده غامض لأن بعض العمليات لا تحتاج Executive أصلًا.

نستبدله بـ:

AuthorityContext {
    kind:
        EXECUTIVE
        OBSERVATION_INGRESS
        RUNTIME_SYSTEM
        RECOVERY

    executive_epoch?
    authority_ref?
}
EXECUTIVE

للـ:

Claims
Goals
Plans
Decisions
Memory promotion
Action authorization
Specialist integration
OBSERVATION_INGRESS

لإضافة Observation خام.

RUNTIME_SYSTEM

لانتقالات runtime الحتمية المسموح بها معماريًا.

RECOVERY

لانتقالات reconciliation التي يجيزها recovery protocol.

وجود kind لا يمنح authority تلقائيًا.

CommitGate يتحقق أن:

requested transition
is legal for authority kind
7. Initiator ≠ Authorizer

نلغي غموض actor.

مثال:

Specialist proposes something
Executive authorizes it
Runtime commits it

هذه ثلاثة أدوار مختلفة.

لذلك:

initiator_ref
authority_context
commit_writer = runtime

ولا نستنتج authority من initiator.

Who proposed a transition and who had authority to authorize it are separate facts.

8. CanonicalMutation

حتى نستطيع recovery دون إعادة تشغيل LLM أو domain code، كل ControlCommit تحتوي mutation representation قابلة لإعادة التشغيل حتميًا.

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

في Runtime v1 نفضل:

after-image semantics

بدل سلسلة patches معقدة.

أي أن replay لا يحتاج أن يعرف:

why transition happened

بل فقط:

what canonical entity became
9. لماذا After-Image؟

إذا لدينا:

Claim C12 v4

ثم commit تحولها إلى v5:

CanonicalMutation {
    expected = 4
    new_entity_version = 5
    after_image = complete C12 v5
}

Replay:

verify current version = 4
↓
replace with after_image
↓
version = 5

لا نستدعي:

LLM
Capability
Engineering logic

أثناء recovery.

وهذا invariant مهم جدًا:

Recovery replays committed results, not the cognition that originally produced them.

10. Semantic Events منفصلة عن Replay Mutations

ControlCommit قد تحتوي كذلك:

ControlEvent {
    event_id

    event_type
    event_type_version

    ordinal

    payload
}

مثل:

DecisionAccepted
TriggerArmed
GoalBlocked
SpecialistIntegrated

لكن هذه الأحداث ليست مضطرة وحدها لإعادة بناء الـentity.

لدينا فصل:

CanonicalMutation
→ deterministic state replay

ControlEvent
→ meaning / audit / lifecycle / forensics

وهذا يبسط schema evolution كثيرًا.

11. Event Ordinal

داخل Commit واحدة:

ordinal

يعطي ترتيب representation حتمي.

لكنه لا يعني أن العالم الخارجي شهد الأحداث زمنيًا بهذا الترتيب.

فالـControlCommit ذرية من ناحية canonical state.

12. IDs

قرار UUIDv7 في المسودة السابقة كان سابقًا لأوانه.

المواصفة الآن تجمد فقط:

IDs are:
opaque
globally unique within their required domain
stable
typed
non-reusable

مثال:

ProjectId
GoalId
ClaimId
ActionId
ObservationId

ولا يجوز خلطها.

أما:

UUIDv7
ULID
other suitable implementation

فقرار Implementation Boundary لاحق.

UUIDv7 يبقى المرشح الافتراضي، وليس قانون RDMS.

13. Entity Versioning

كل mutable canonical entity تحمل:

entity_version
created_commit_seq
updated_commit_seq

Create:

expected = ABSENT
new_version = 1

Update:

expected = current_version
new_version = current_version + 1

لا يوجد:

blind overwrite
14. Conflict Granularity في v1

في Runtime v1 يكون conflict على مستوى entity كاملة.

إذا عاملان يريدان تعديل:

Decision D17

من نفس version:

الأول الذي ينجح يرفع version.

الثاني يحصل على:

WRITE_CONFLICT

لا نحاول تلقائيًا:

field-level merge

حتى لو عدّل كل منهما field مختلفة.

الـsemantic merge يحدث خارج transaction:

read new entity
↓
reconcile
↓
new proposal

هذا أكثر أمانًا وأبسط في v1.

15. Staleness ≠ Write Conflict

نثبت الفرق:

WRITE_CONFLICT
→ entity the proposal wants to mutate changed

DEPENDENCY_STALE
→ something reasoning depended upon changed

يمكن Proposal ألا تكتب A لكنها قرأتها.

إذا:

A v4 → A v5

فتصبح reasoning stale رغم أن write target مختلف.

16. Idempotency

كل canonical command القابل لإعادة الإرسال يحمل:

idempotency_key
request_fingerprint

الـruntime يخزن association:

(project_id, operation_scope, idempotency_key)
→ commit_id + request_fingerprint
نفس key + نفس fingerprint
return original result
نفس key + fingerprint مختلف
IDEMPOTENCY_CONFLICT

ولا توجد TTL تلقائية لمفاتيح canonical mutation.

17. Schema Evolution

ظهرت فجوة حقيقية في RDMS-01 الأصلية: event التاريخية immutable، لكن schemas ستتطور.

لذلك نفصل:

control_schema_version
event_type_version
payload_schema_version
snapshot_codec_version

ولا نعتمد على version واحدة لكل النظام.

Event التاريخية

لا يعاد كتابتها.

عند القراءة يمكن استخدام:

deterministic upcaster / decoder

من version أقدم إلى representation الحالي.

لكن:

Schema migration may reinterpret representation, never rewrite historical meaning.

18. Snapshot Model المصحح

مع Hybrid Model، Snapshot ليست مطلوبة لكل restart.

لدينا مساران.

Normal restart

إذا current canonical state متسقة مع:

ProjectHead.latest_commit_seq

يمكن تحميلها مباشرة.

Rebuild / integrity recovery
latest valid snapshot
↓
replay later CanonicalMutations
↓
reconstruct current tables

إذن Snapshot تصبح:

rebuild accelerator

لا runtime prerequisite.

19. Snapshot Schema
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

نستخدم:

payload_hash

لا state_hash.

لأننا نتحقق من bytes المشفرة فعلًا.

إذا أردنا semantic canonical hash لاحقًا، يجب أولًا تجميد canonical serialization.

20. Current-State Integrity Marker

Current canonical store تحمل:

applied_through_commit_seq

ويجب في الحالة السليمة:

CanonicalStore.applied_through_commit_seq
==
ProjectHead.latest_commit_seq

إذا أقل:

replay missing commits

إذا أكبر:

CORRUPTION / FAILED_SAFE

لأن current state تدعي transition غير موجودة في التاريخ authoritative.

21. Artifact Store

Artifact كبيرة لا توضع في Control Ledger.

لكن lifecycle تصبح:

PREPARED
REFERENCED
ORPHAN
RETIRED

ولا يمكن commit لـArtifactRef قبل إثبات:

bytes durable
hash verified
Recovery-critical artifacts

تحمل:

retention_class = RECOVERY_CRITICAL

ولا يجوز Garbage Collection لها طالما canonical state أو replay history تعتمد عليها.

أما:

temporary prompt trace
derived cache

فيمكن أن تكون retention أقل.

22. Derived Indexes

تبقى non-authoritative.

لكن metadata تحتاج:

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

وهذا مهم لاحقًا لـNegative Knowledge.

23. Repository References

working_snapshot لا يجوز أن يعني:

C:\project

لأن المسار mutable.

بل:

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

كل RepoRef تستخدم كdependency يجب أن تصف حالة قابلة للتعرف لاحقًا.

24. Runtime Status Split

المسودة السابقة خلطت حالتين مختلفتين.

Durable ProjectStatus
ProjectStatus {
    ACTIVE
    SUSPENDED
    ARCHIVED
    FAILED_SAFE
}
ProcessRuntimeMode
ProcessRuntimeMode {
    INITIALIZING
    RECOVERING
    READY
    DEGRADED
    STOPPING
}

READY ليست حقيقة دائمة عن المشروع.

إذا مات process وهي READY فلا معنى لتخزينها كأنها ما زالت تعمل.

عند كل startup:

ProcessRuntimeMode = INITIALIZING
→ RECOVERING

ثم فقط بعد RecoveryBarrier:

READY
25. Recovery Model النهائي لـRDMS-01
Fast Recovery
open authoritative store
↓
read ProjectHead
↓
verify current-state applied seq
↓
acquire/fence Executive epoch
↓
inspect unresolved actions
↓
replay triggers
↓
validate specialists/dependencies
↓
RecoveryBarrier
↓
READY
Rebuild Recovery

إذا current-state store غير متسقة:

load valid Snapshot
↓
replay CanonicalMutations
↓
reconstruct current state
↓
verify against ProjectHead
↓
normal reconciliation

لا يحتاج أي منهما chat history.

26. Observation Concurrency

Observation append لا تحتاج Executive.

لذلك قد تأتي بالتوازي مع Executive transition.

لكن كلاهما يدخل:

ControlTransaction

ويحصل على commit ordering قانوني.

مثلًا:

commit 400
Executive: HypothesisCreated

commit 401
ObservationIngress: TestFailed

commit 402
Executive: HypothesisUpdated

ولا توجد write race على Ledger head لأن commit boundary نفسها serialized.

27. Canonical Commit Isolation

أي storage engine نختاره يجب أن يمنع:

dirty canonical reads
lost update
double allocation of authority
partial ControlCommit

لكن RDMS لا تجمد اسم SQL isolation level الآن.

نحدد semantics لا implementation flag.

28. Revised Runtime Invariants
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
29. Adversarial Re-test
Attack	Result
Current entity committed but history missing	Impossible if same ControlTransaction → PASS
Ledger event committed but current state update missing	Same transaction → PASS
Process crashes after both commit	Both durable → PASS
Process crashes before commit	Neither authoritative → PASS
Replay requires LLM output again	CanonicalMutation after-image prevents it → PASS
Old event schema	versioned decoder/upcaster path → PASS
Two writers update same entity version	compare-and-set → one wins, one conflicts → PASS
Global state changes for unrelated entity	does not invalidate entity automatically → PASS
Retried command creates duplicate transition	idempotency key + fingerprint → PASS
Same idempotency key reused for different request	fail closed → PASS
Snapshot corrupt	discard/rebuild → PASS
Current state lags Ledger	deterministic replay → PASS
Current state ahead of Ledger	corruption / FAILED_SAFE → PASS
Artifact reference committed before bytes durable	forbidden → PASS
README changes and derived index stale	index metadata exposes generation/fingerprint → PASS
Runtime dies while marked READY	process mode reconstructed, not durable truth → PASS
Mutable working directory used as immutable dependency	forbidden; snapshot/fingerprint required → PASS
30. Freeze Verdict for RDMS-01

لم يبقَ blocker في Runtime Foundations يؤثر على:

authority
atomicity
replay
current-state consistency
idempotency
schema evolution
artifact integrity
basic concurrency
startup recovery

لذلك:

RDMS-01 — Runtime Foundations: FROZEN

مع قرار مركزي نهائي:

We are not building a pure event-sourced system.

نحن نبني:

Transactional Canonical State + Append-Only Replay/Audit Ledger

ويُحدَّث الاثنان في ControlCommit واحدة ذرية.

هذا يحتفظ بمزايا event sourcing التي نحتاجها، من دون فرض تكلفته على كل قراءة وكل جزء من النظام.

31. Next Authorized Specification

الخطوة التالية أصبحت:

RDMS-02 — Canonical Entity Schemas

وسنحدد فيها تحديدًا دقيقًا:

Claim
InformationNeed
Hypothesis
OperationalCausalClaim
Goal
GoalStack
FocusState
Decision
Invariant
Contract
Risk
Slice
Commitment

لكل entity سنحسم:

identity
mutable vs immutable
versioning
required fields
references
status machine
legal creator
legal updater
terminal states
staleness semantics
tombstone/supersession behavior
ControlEvents

ثم نهاجمها قبل الانتقال إلى Observation/Experiment/Action.

هذه المراجعة وفّرت علينا مشكلة كبيرة مستقبلًا: لو دخلنا البرمجة بالنموذج السابق، كان من السهل أن ينتهي Antigravity ببناء event-sourcing framework ضخم بدل بناء الـagent نفسه. الآن لدينا نموذج أبسط بكثير: SQL-like current state للقراءة والعمل اليومي + سجل immutable للـaudit/recovery في نفس transaction. وهذا أقرب لما أريد أن نعطيه لـAntigravity لاحقًا: semantics واضحة من دون infrastructure غير ضرورية.

نستطيع الآن الانتقال مباشرة إلى RDMS-02: Canonical Entity Schemas.
````
<!-- /RDMS-MESSAGE -->


---
## 4. Inherited RDMS base clauses — subordinate to amendments


**Important:** each baseline excerpt is retained to make the layer self-contained, **not** to revive overridden language. Any conflict with §3 or frozen FCA is superseded. Historical `DRAFT` labels inside these verbatim quoted sources describe their origin, not the state of this composite.


### RDMS-01 original baseline — subject to later approved amendments

**Message:** `2aacdc73-38d8-4456-9a73-9900fe14f900`; **SHA-256:** `278dee38200e828c246e4488ceebeada0d19b03d4c6267083083527a28e460ba`; **legal status:** base only where not modified by §3.

<!-- RDMS-MESSAGE 2aacdc73-38d8-4456-9a73-9900fe14f900 SHA256 278dee38200e828c246e4488ceebeada0d19b03d4c6267083083527a28e460ba -->

````text
نعم. نبدأ الآن رسميًا Runtime & Data Model Specification v1.0، لكن بنفس الانضباط السابق: لن نقفز إلى class Claim وclass Executive مباشرة. أولًا نثبت «فيزياء» الـruntime: ما الذي يمثل الحقيقة الدائمة، كيف يُرتب التاريخ، ما معنى version، وكيف تكون المعاملة ذرية وقابلة للاسترجاع.

المسودة الأولى التالية هي RDMS-01 — Runtime Foundations، وليست مجمدة بعد.

Runtime & Data Model Specification v1.0 — RDMS-01 Runtime Foundations
Runtime & Data Model Specification v1.0
RDMS-01 — Runtime Foundations

Parent Architecture: Formal Cognitive Architecture v1.0.1 — FROZEN
Status: DRAFT / NOT FROZEN
Purpose: تحويل الضمانات المعمارية المجمدة إلى نموذج persistence/runtime دقيق قبل تصميم classes أو اختيار لغة التنفيذ.

1. Runtime Unit

الوحدة العليا في الـruntime هي:

ProjectRuntime

كل مشروع له عقل canonical مستقل:

ProjectRuntime {
    project_id

    control_head
    canonical_state

    current_executive_epoch

    repo_binding

    schema_version

    runtime_status
}

ولا تشترك المشاريع في:

Executive epoch
global ordering
canonical state
action journal
trigger lifecycle

حتى لو استخدمت نفس عملية التشغيل أو نفس قاعدة البيانات الفيزيائية.

المبدأ:

Canonical authority is scoped to one ProjectRuntime.

2. طبقات البيانات الدائمة

الـruntime يميز خمسة أنواع من البيانات:

1. Control Ledger
2. Canonical Entity State
3. Snapshots
4. Immutable Artifacts
5. Derived Indexes / Read Models

ولا تحمل كلها الدرجة نفسها من السلطة.

3. Control Ledger — historical heading superseded by RDMS-01 R1 ControlCommit atomic authority (append-only audit remains obligatory)

Control Ledger هو التاريخ القانوني authoritative للـruntime.

هو:

append-only
ordered
durable
replayable
immutable after commit

ولا يجوز تعديل event سابقة.

إذا كان الاعتقاد أو القرار القديم خاطئًا:

old event remains
+
new correction/supersession event

وليس:

UPDATE old history
أهم قاعدة

The Control Ledger records what the system legally committed, not merely what it intended to do.

4. Control Commit

الوحدة الذرية للـLedger ليست event واحدة بالضرورة.

إنها:

ControlCommit

لأن transition واحدة قد تتطلب عدة Events يجب أن تظهر معًا.

مثال:

DecisionAccepted
TriggerArmed
StateAdvanced

يجب أن تكون transaction واحدة.

البنية:

[RDMS-01 original ControlCommit fields superseded by R1-approved exact interface; the historical version remains in the source archive.]

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
5. commit_seq

لكل ProjectRuntime عداد monotonic:

commit_seq: uint64

مثال:

1
2
3
4
...

ويزداد مرة واحدة لكل ControlCommit ناجحة.

لا نعتمد على timestamps لترتيب الحقيقة.

لأن:

clock time
≠
causal commit order

الترتيب الرسمي:

(project_id, commit_seq)
6. Event Ordering داخل Commit واحدة

لأن commit قد تحتوي أحداثًا متعددة:

ControlEvent {
    event_id
    ordinal
    event_type
    payload
}

وترتيب الأحداث الكلي:

(commit_seq, ordinal)

مثال:

commit_seq = 104

ordinal 0 → DecisionAccepted
ordinal 1 → TriggerArmed
ordinal 2 → GoalActivated

لكن الثلاثة تصبح durable كوحدة واحدة.

7. Event Identity

كل Event تحصل على ID عالمي مستقل:

EventId = UUIDv7

وكذلك:

ProjectId
EntityId
CommitId
ActionId
TriggerId
SpecialistId
ExperimentId
ObservationId

تستخدم UUIDv7 منطقيًا لأنها:

globally unique
time-sortable
provider-independent
distributed-runtime friendly

لكن ترتيب authority لا يعتمد على ترتيب UUID.

يبقى:

commit_seq

هو canonical ordering داخل المشروع.

التمثيل الفيزيائي للـUUID:

16-byte binary
or canonical textual form

يبقى قرار implementation.

8. Typed IDs

لا نسمح runtime بخلط IDs دلاليًا حتى لو كلها UUID.

مفاهيميًا:

ProjectId
ClaimId
GoalId
ActionId
ObservationId
HypothesisId
DecisionId
SpecialistId
TriggerId

أنواع مختلفة.

مثال غير قانوني:

ActionId passed where ClaimId expected

حتى لو القيمة فيزيائيًا UUID صحيحة.

هذه قاعدة type-system/runtime validation.

9. Global State Version

global_state_version في FCA يصبح:

global_state_version == latest committed commit_seq

لكل ProjectRuntime.

أي:

ControlCommit 101
→ global_state_version = 101

ثم:

ControlCommit 102
→ global_state_version = 102

يشمل ذلك كل canonical control transition المهمة، بما فيها Observation append.

لكن:

Global state version is historical ordering, not semantic dependency validity.

لذلك لا نستعمله وحده لقبول أو رفض Specialist result.

10. Entity Version

كل entity قابلة للتطور لها version مستقلة:

entity_version: uint64

مثال:

Decision D17 v1
↓
Decision D17 v2

ويزيد version فقط عندما تتغير تلك الـentity نفسها.

EntityEnvelope {
    entity_id
    entity_kind

    entity_version

    created_commit_seq
    updated_commit_seq

    status

    payload
}

وبالتالي لدينا:

global_state_version
→ What changed anywhere?

entity_version
→ Did this specific thing change?

وهما لا يؤديان الوظيفة نفسها.

11. Immutable Entities

بعض entities لا يتم تعديلها أصلًا.

مثل:

Observation
raw Episode
committed ControlEvent

إذا احتاجت correction:

Observation O17
+
ObservationCorrection / supersession relation

بدل تعديل O17.

هذا يحافظ على provenance.

12. Canonical Entity State

الحالة الحالية للمشروع يمكن أن تحتوي materialized current records مثل:

Goals
Claims
Hypotheses
Decisions
Invariants
Triggers
Specialists
Actions
...

لكن هذه ليست تاريخًا موازيًا مستقلًا.

إنها:

projection(Control Ledger)

ويجب من حيث المبدأ أن تكون قابلة لإعادة البناء من:

Snapshot
+
subsequent Control Commits
13. Source of Truth Hierarchy

الترتيب الرسمي:

1. Control Ledger
      ↓
2. Rebuilt Canonical State
      ↓
3. Snapshots / materialized projections
      ↓
4. Search indexes / caches

لا يجوز لـ:

search index
cache
vector index

أن يصبح authority.

إذا اختلف index مع Ledger:

Ledger wins.
14. Snapshot

Snapshot موجود لتسريع recovery.

Snapshot {
    snapshot_id

    project_id

    through_commit_seq

    schema_version

    state_hash

    payload_ref

    created_at
}

through_commit_seq تعني:

snapshot includes every committed transition
up to and including N

Recovery:

load latest valid snapshot S
↓
verify integrity
↓
replay commits S.through_commit_seq + 1 ... HEAD
15. Snapshot ليست Authority مستقلة

إذا snapshot تالفة:

discard
↓
use older snapshot
↓
replay more Ledger

إذا لا توجد Snapshot:

replay Ledger from origin

إذن:

Snapshot loss may hurt performance; it must not destroy project cognition.

16. Snapshot Integrity

كل Snapshot تحمل:

state_hash

ويحسب على canonical serialized state بطريقة deterministic.

نستخدم مبدئيًا:

SHA-256

لـintegrity.

لكن hashing ليست authority.

هي فقط:

corruption / mismatch detector
17. Immutable Artifact Store

ليست كل البيانات مناسبة داخل Control Ledger.

مثال:

large logs
LLM responses
runtime traces
patches
source snapshots
test reports
debug dumps
images
large code context

توضع في Artifact Store.

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
18. Artifact Commit Rule

لا يجوز لـControl Event أن تشير إلى artifact لم تصبح durable بعد.

المسار:

write artifact
↓
verify content hash
↓
artifact becomes PREPARED
↓
ControlTransaction commits ArtifactRef
↓
artifact becomes referenced

إذا crash بعد PREPARED وقبل ControlCommit:

orphan artifact

يمكن Garbage Collector حذفه لاحقًا.

هذا أفضل من:

Ledger references missing artifact
19. Artifact Immutability

أي ArtifactRef committed يجب أن تشير إلى محتوى immutable.

إذا تغير المحتوى:

new artifact
new hash
new ArtifactId

لا:

same ArtifactId
different bytes
20. Derived Indexes

يمكن للruntime لاحقًا بناء:

symbol index
AST index
full-text index
memory search index
dependency graph
vector index

لكنها derived state.

كل Index يجب أن تعرف على الأقل:

IndexMetadata {
    index_id
    index_kind

    built_from_repo_ref?
    built_through_commit_seq?

    generation

    status
}

حتى نستطيع الحكم على freshness.

21. Control Transaction

كل canonical mutation تحدث داخل:

ControlTransaction

شكلها المفاهيمي:

BEGIN

validate:
    project
    executive_epoch if required
    schema
    authority
    hard invariants
    expected entity versions
    idempotency

allocate:
    commit_seq

apply:
    entity mutations
    lifecycle updates
    control events

COMMIT

إما:

all succeed

أو:

none become authoritative
22. Idempotency

كل عملية قابلة لإعادة الإرسال إلى Control Plane تحمل:

idempotency_key

والـscope:

(project_id, operation_kind, idempotency_key)

يجب أن يكون unique.

إذا runtime تلقى الطلب نفسه مجددًا:

same key
same semantic operation

لا ينشئ commit ثانية.

بل يعيد نتيجة commit الأصلية.

23. Idempotency Conflict

إذا استعمل نفس key مع payload مختلف:

same idempotency_key
different semantic request

فهذا ليس retry.

إنه خطأ:

IDEMPOTENCY_CONFLICT

ولا يتم التنفيذ.

24. Actor Identity

كل ControlCommit تعرف من تسبب فيها.

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

هذا ليس authority بحد ذاته.

مثلًا:

actor_type = specialist

لا يمنح Specialist حق commit.

الـauthority تتحقق مستقلاً.

25. Correlation and Causation

نضيف:

correlation_id
causation_id

لمتابعة السلاسل.

مثال:

UserRequest
↓
GoalCreated
↓
SliceCreated
↓
ActionAuthorized
↓
ObservationRecorded
↓
HypothesisUpdated

كلها يمكن ربطها تحت:

correlation_id = Task/Intent execution lineage

أما:

causation_id

فتشير مباشرة إلى event/command الذي سبب transition الحالية.

هذا مهم جدًا لـ:

debugging runtime
audit
recovery
postmortem
26. Logical Clock vs Wall Clock

كل record قد تحمل:

created_at
observed_at
started_at
finished_at

لكن الزمن الجداري لا يحدد canonical ordering.

الترتيب القانوني يأتي من:

commit_seq

بينما timestamps تستخدم لـ:

temporal reasoning
latency
timeouts
trigger timing
forensics
27. Repository Reference

لا يكفي string عامة اسمها repo_ref.

نعرف:

RepoRef {
    repository_id

    revision_kind:
        commit
        working_snapshot
        sandbox_snapshot

    revision_id

    content_fingerprint?

    dirty:
        true | false
}

مثال:

commit
→ git SHA

working_snapshot
→ stable runtime snapshot ID

sandbox_snapshot
→ isolated workspace snapshot

حتى لا نقارن:

Git commit abc

مع working tree معدلة وكأنهما الشيء نفسه.

28. World Reference

بعض Actions لا تعتمد على repository فقط.

لذلك:

WorldRef {
    environment_id

    dimensions[]
}

والـdimensions قد تكون:

database_schema_version
deployment_revision
external_api_contract_version
service_instance_generation
dataset_version

لا نطلب أن يستطيع النظام تمثيل العالم كله.

بل فقط:

the world dimensions relevant to the operation being reasoned about.

29. Dependency Stamp Foundation

كل اعتماد معرفي طويل العمر يستخدم:

DependencyStamp {
    dependency_kind

    ref

    version_or_hash?

    validity_condition?

    freshness_requirement:
        exact
        compatible
        advisory
}

ولا نقيد dependency_kind بالـstate فقط.

يمكن أن يكون:

canonical_entity
repo_content
query_scope
observation
memory_item
tool_version
environment
external_contract
human_requirement

وسنفصل schema الدقيقة لها في قسم لاحق.

30. Canonical Transition Classes

من ناحية الـruntime يوجد خمسة أنواع أساسية من transitions الدائمة:

COGNITIVE_COMMIT

OBSERVATION_APPEND

CONTROL_LIFECYCLE

MEMORY_PROMOTION

WORLD_ACTION_LIFECYCLE

ولا تعني أنها خمس databases.

هي semantic classes للـevents.

31. Cognitive Commit

تغير:

Goal
Claim
Hypothesis
Model
Decision
Plan
Invariant
...

وتتطلب عادة:

Executive authorization
+
CommitGate
32. Observation Append

تضيف Observation خام.

لا تحتاج semantic authorization.

لكن تحتاج:

schema validation
provenance validation
integrity validation

ولا يجوز أن تضيف معها interpretation في العملية نفسها.

أي:

Observation append

ثم لاحقًا:

EvidenceLink / Claim update

Transition مستقلة.

33. Control Lifecycle

مثل:

Executive epoch acquired
Specialist spawned
Trigger armed
Task blocked
Task resumed

بعضها حتمي ولا يحتاج LLM.

لكنها كلها durable عندما تكون مطلوبة للتعافي.

34. Memory Promotion

يجب أن يكون:

MemoryProposal
+
Learning Gate result
+
Executive authorization
+
Memory lifecycle event

داخل control semantics قابلة للتتبع.

ولا يكفي أن يكتب Memory Store record خارج الـLedger.

35. World Action Lifecycle

الـshared-world action لها lifecycle في Control Ledger:

PROPOSED
AUTHORIZED
DISPATCH_INTENT
RESULT_REPORTED
EFFECT_VERIFIED
...

أما micro-actions داخل EPHEMERAL_SANDBOX فيمكن تجميعها داخل SandboxActivityRecord بدل حدث دائم لكل عملية صغيرة.

36. Transaction Boundary Rule

القاعدة العامة:

If losing one half while retaining the other half would make recovery ambiguous, both belong in the same authoritative transaction.

مثال:

DecisionAccepted
+
required TriggerArmed

ذرية.

ومثال:

Specialist status = INTEGRATED
+
accepted canonical changes

يجب ألا يصبح أحدهما durable دون الآخر.

37. What MUST NOT be transactionally coupled

لا نحاول عمل distributed transaction بين:

Control DB
+
GitHub
+
filesystem
+
external API
+
production DB

هذا غير واقعي.

بل:

durable local intent
↓
external effect
↓
observation
↓
reconciliation

وهو سبب وجود Action Journal أصلًا.

38. Concurrency Model

الـControl Ledger يوفر:

one canonical commit order per project

لكن workers يستطيعون القراءة والعمل بالتوازي.

عند commit:

expected entity versions
DependencySet
Executive epoch

تحدد صلاحية النتيجة.

لا نستعمل:

global_state_version changed
→ reject everything
39. Optimistic Canonical Concurrency

الافتراضي:

optimistic concurrency

Proposal تقول:

I read:
A v4
B v9

I intend to change:
C

عند commit:

إذا:

A still v4
B still v9

يمكن الاستمرار.

أما إذا:

A now v5

يحدث:

DEPENDENCY_STALE

لا last-write-wins.

40. Hard Conflict vs Staleness

نفرق:

WRITE_CONFLICT

عن:

DEPENDENCY_STALE

WRITE_CONFLICT:

عاملان يحاولان كتابة نفس canonical entity incompatible.

DEPENDENCY_STALE:

ما اعتمد عليه reasoning تغير.

وقد توجد:

PARTIALLY_STALE

إذا جزء فقط من النتيجة تأثر.

41. Recovery Head

عند startup:

LedgerHead {
    project_id
    latest_commit_seq
    current_executive_epoch
}

يتم التحقق منه أولًا.

ثم أحدث snapshot سليمة.

ثم replay.

42. Recovery Principle

الـruntime يجب أن يستطيع الإجابة بعد أي crash:

What was definitely committed?

What was definitely not committed?

What may have affected the world?

What is currently unresolved?

What must be reconciled before new work?

إذا لم يستطع الإجابة عن واحدة منها:

فإن persistence model غير كافٍ.

43. Recovery Barrier

قبل العودة إلى normal execution بعد restart:

RecoveryBarrier

يجب أن يتأكد على الأقل من:

valid Executive epoch
canonical state rebuilt
unresolved shared-world actions classified
due/replayable triggers processed
specialist states inspected
blocked/waiting tasks restored
critical dependency freshness evaluated

بعدها فقط:

runtime_status = READY
44. Runtime Status
RuntimeStatus {
    INITIALIZING
    RECOVERING
    READY
    DEGRADED
    SUSPENDED
    FAILED_SAFE
}

FAILED_SAFE لا تعني crash.

بل:

runtime is alive
but refuses unsafe progress

مثال:

unresolvable IN_DOUBT payment action

يمكن أن يجعل جزءًا من المشروع blocked بينما runtime نفسها تعمل.

45. Physical Storage Is Not Yet Frozen

RDMS-01 لا يختار بعد:

SQLite
PostgreSQL
LMDB
etc.

لكن أي اختيار يجب أن يدعم semantics التالية:

ACID transaction for ControlCommit
unique constraints
monotonic per-project sequence
optimistic entity-version checks
durable acknowledgement
crash recovery
append-only event history

بالنسبة للنسخة الأولى، قاعدة بيانات relational transactional واحدة للـControl Plane تبدو أبسط خيار هندسي، لكننا لن نجمد اسم المحرك حتى نكمل الـschemas وحجم workload المتوقع.

46. Runtime Foundation Invariants
RDMS-I01
Every authoritative ProjectRuntime transition has exactly one committed
ControlCommit identity.

RDMS-I02
Canonical ordering is defined by per-project commit_seq, not wall-clock time.

RDMS-I03
Committed Control Events are immutable.

RDMS-I04
Canonical current state must be reconstructible from a valid Snapshot
plus subsequent Control Ledger commits.

RDMS-I05
Snapshots and indexes are not independent sources of truth.

RDMS-I06
Global state version and entity version have different semantics
and must never be substituted for each other.

RDMS-I07
Idempotent retry of the same control operation must not create
a second canonical transition.

RDMS-I08
An idempotency key reused for a semantically different operation
must fail closed.

RDMS-I09
A committed ArtifactRef must never point to an artifact whose
durability/integrity was not established before the commit.

RDMS-I10
Authority, dependency freshness and hard-invariant validation occur
before a canonical mutation commits.

RDMS-I11
Recoverability-critical metadata that must coexist after crash
must share one authoritative transaction boundary.

RDMS-I12
No distributed external system is assumed to share the Control
Transaction; external effects use intent → action → observation →
reconciliation.

RDMS-I13
Indexes/caches may accelerate cognition but never override
Canonical State or Control Ledger.

RDMS-I14
Recovery must reach a known reconciled or explicitly unresolved state
before normal conflicting execution resumes.
47. What RDMS-01 Has Frozen Conceptually

هذا الجزء حسم:

runtime ownership unit
Control Ledger semantics
ControlCommit semantics
commit sequencing
event ordering
ID strategy
global vs entity version
immutable vs versioned records
snapshot semantics
artifact semantics
index authority
transaction boundary principle
idempotency semantics
actor/causal lineage
repo/world references
dependency foundation
transition classes
optimistic concurrency
recovery barrier
runtime states

لكنه لم يُجمّد بعد حتى ننفذ عليه adversarial review.

48. Next RDMS Sections

بعد مراجعة RDMS-01، الترتيب المنطقي التالي هو:

RDMS-02
Canonical Entity Schemas
→ Claim
→ InformationNeed
→ Hypothesis
→ OperationalCausalClaim
→ Goal
→ Decision
→ Invariant
→ Slice
→ FocusState

RDMS-03
Observation / Evidence / Experiment Schemas

RDMS-04
Action / Sandbox / ActionJournal Schemas

RDMS-05
Trigger / Temporal / Resumption Schemas

RDMS-06
Specialist / Dependency / Integration Schemas

RDMS-07
Memory / Episode / Promotion Schemas

RDMS-08
Executive / CommitGate / Runtime Transition Events

RDMS-09
Recovery & Migration Protocol

RDMS-10
Full Transaction Matrix + Event Catalog

ثم:

Adversarial Runtime Review
↓
Corrections
↓
Runtime & Data Model Specification v1.0 — FROZEN

هذه البداية مهمة لأننا الآن حددنا ما الذي يجب أن يبقى صحيحًا حتى لو مات البرنامج في منتصف التنفيذ، قبل التفكير في أي class أو database table.

هناك قرار واحد في RDMS-01 أريد أن نراقبه جيدًا أثناء المراجعة القادمة: جعل Control Ledger هو الـsource of truth مع current state كـprojection. هذا يعطي recovery وaudit ممتازين، لكنه إذا بالغنا في event sourcing يمكن أن يصنع تعقيدًا غير ضروري. لذلك في المراجعة العدائية لـRDMS-01 سأختبر خصوصًا ما إذا كان بإمكاننا الحفاظ على نفس الضمانات باستخدام transactional current-state tables + append-only control events بدل فرض event-sourcing كامل على كل entity. هذا قد يكون أبسط كثيرًا عند البرمجة مع الحفاظ على جميع ضمانات FCA.
````
<!-- /RDMS-MESSAGE -->


---
## 5. Cross-layer interface admission and rejection (source-controlled candidates)


No primary interface contract is owned here; incoming/outgoing contracts are governed by their owning layers.


---
## 6. Freeze boundary and unresolved proof obligations


- The 27 RDMS source messages and the FCA sections are now **directly present** in assigned layer views, without GAIA review chronology interspersed as active normative material.
- This is **a precedence-bound legal composition**, not proof of a complete sentence-by-sentence merger. A baseline passage and a later corrective passage may both remain verbatim for audit.
- Before FROZEN: verify every changed baseline clause against its exact corrective replacement; close missing field types, mandatory-field conditions, state transitions and transactional failure semantics for all 12 interfaces.
- No executable persistence, provider, tool or external-effect implementation has been verified.
- **FREEZE HOLD** until full semantic delta review is passed.
