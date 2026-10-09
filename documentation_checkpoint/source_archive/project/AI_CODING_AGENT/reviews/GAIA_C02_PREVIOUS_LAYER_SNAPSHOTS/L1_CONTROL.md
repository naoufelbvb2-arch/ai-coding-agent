<!-- GAIA-C01-PHASE13-CURRENT-STATUS START -->
# CURRENT READING GUIDE — GAIA-C01 Phase 13

**STATUS: CONSOLIDATION DRAFT; NOT FROZEN.**  
**Owned responsibility:** Canonical control, Control Ledger and CommitGate.  
**Source rule:** Full original normative texts remain unmodified in the archived source set and the source annex of this document. A historical draft is NOT automatically the effective current law: approved C01/C02/C03 corrections and final freeze decisions must be incorporated before the consolidated layer supersedes those sources. Phase 11 reference tests are not production/runtime verification.  
**Forbidden:** silent defaulting, missing-authority inference, lossy migration, or treating transport wrappers as canonical entities.

**FCA source sections/appendices assigned:** 7.  
**RDMS source sets assigned:** 1; **approved original message parts:** 2.  
**27-name ownership subset present here:** 0.

| Attached RDMS source | Original message parts | Source interpretation |
|---|---:|---|
| RDMS-01 | 2 | Original draft + approved corrections / freeze decision, read with precedence |

| Canonical-type ownership candidate | Source | Current migration decision |
|---|---|---|
| — | — | No audited reused-name contract owned here |

**Freeze blocker:** An independently usable, contradiction-free, *effective* contract and law text has not yet been consolidated from draft plus correction overlays. See `../reviews/GAIA_C01_PHASE13_FREEZE_REVIEW_AR.md`, `GAIA_C01_PHASE13_LAYER_COVERAGE.json`, and the Phase-12 contract decision register. Runtime validation belongs to a separate implementation stage; existing architectural ambiguities cannot be waived by deferring tests.
<!-- GAIA-C01-PHASE13-CURRENT-STATUS END -->

---

<!-- GAIA-C01-PHASE12-DECISION-INDEX START -->
## GAIA-C01 Phase 12 — Effective owner & change-control index (DRAFT)

**Not a new frozen law.** Original source sections and approved overlays below retain authority. Do not infer legal equivalence of transport projections or historical migrations. Global layer freeze remains unauthorized.

**Source-owned reused contracts in this layer:** 0.

No repeated-name contracts from the 27-name audit are owned here; other original legal entities remain in the source annex below.

Refer to `../reviews/GAIA_C01_PHASE12_CONTROLLED_CONTRACT_DECISIONS.md` and the JSON decision ledger for exact source anchors and remaining proof gates.
<!-- GAIA-C01-PHASE12-DECISION-INDEX END -->

---

<!-- GAIA-C01-PHASE9 CONTRACT PUBLICATION START -->
## GAIA-C01 Phase 9 — Curated source-backed contract publication (NOT RE-FROZEN)

**Status: VERBATIM SOURCE BASELINES ONLY — effective cross-layer projections remain unapproved.**

This section is a navigation and source-publication aid. It does not overwrite historical FCA or RDMS source sections. Corrections/overlays must be applied according to the approved original source history, not inferred from an earlier draft.

**Owning layer:** `L1`. **Published reused names:** `0`.

No audited duplicate canonical data type in the 27-name registry is primarily owned by this layer. Consult the original FCA/RDMS source annex below for this layer’s other definitions.

**Publication guard:** No inferred fields, default values, status promotions, action permissions, or silent renames are authorized by this section.
<!-- GAIA-C01-PHASE9 CONTRACT PUBLICATION END -->


---

# L1 — Canonical State & Control

> **CONSOLIDATION DRAFT — NOT FROZEN.** This file is a working per-layer consolidation, **not** an independently approved replacement for the frozen FCA/RDMS source specifications. Normative FCA source: `../reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md` (SHA-256 `74d0923cbd343b71740da0fc2368a84aad2ea97f8e4e15f156122f48ebe53539`). RDMS-01…10 original source sets arrived in GAIA-C01 Phase 4. Effective cross-source schemas and ownership remain **PENDING RECONCILIATION**; the archived original text below is untouched.

> **Phase 5:** source-name audit and non-normative proposals: `../reviews/GAIA_C01_PHASE5_CONTRACT_RECONCILIATION.md`. Original FCA and RDMS annexes below retain their historical authority/status; proposed aliases are not approved laws.

**Layer owner:** RDMS-01 primary; FCA canonical-state semantics  
**Authoritative FCA trace:** FCA §§6, 48–52, 74, Appendix D  
**Migration status:** CONSOLIDATED DRAFT / REVIEW REQUIRED  
**Source status:** FCA v1.0.1 hash-verified; RDMS source sets imported; effective contract reconciliation pending.

## 1. Scope and charter

L1 owns the authoritative control boundary and canonical state commit contract. It must not become another Executive deciding semantics.

## 2. Canonical control state

From FCA §6: `Identity {project_id, global_state_version, repo_ref, schema_version, current_executive_epoch}`. Canonical state additionally groups goals, focus, system mental model, epistemic, engineering, execution, temporal, specialists, memory refs, meta and control refs (see FCA Appendix D). A physical storage layout may normalize these structures without changing who can authorize mutations.

## 3. Persisted control responsibilities

The Control Ledger stores or atomically references Executive epochs, canonical cognitive commits, Action lifecycle, Trigger lifecycle, Specialist lifecycle, memory promotions and goal/task lifecycle. Every canonical event has `event_id`, `schema_version`, `idempotency_key` (FCA §48). Recovery-critical control metadata jointly needed for continuity commits atomically (FCA §49).

## 4. CommitGate contract

```text
CognitivePatch (not a world action)
   → current-epoch semantic authorization
   → hard invariants + schema/version/freshness checks
   → authoritative commit and required control events
```

A tentative integration envelope may include request ID, project ID, executive epoch, patch ref, authority proof, expected entity versions, typed dependency set and idempotency key. **PENDING EFFECTIVE CONTRACT AUDIT:** exact frozen RDMS-01 request/response schema, rejection modes and CAS rules.

## 5. Executive epochs and adoption

`LeadershipGrant {project_id, executive_id, epoch, status, acquired_at}` is the FCA §50 reference. Only the current epoch authorizes new canonical effects. An `AUTHORIZED` action from an old epoch requires explicit adoption; `DISPATCH_INTENT` and beyond require reconciliation, not new blind dispatch.

## 6. Transaction matrix

| Transition | Atomicity concern | Owner |
|---|---|---|
| Decision accepted + required Trigger armed + StateVersion advanced | All-or-none if jointly recovery-critical | Control Ledger |
| Action state with dispatch intent | Durable before shared-world send | RDMS-01 / RDMS-04 jointly |
| Trigger reaction plus required follow-up commitment | Recoverably consistent handoff | RDMS-01 / RDMS-05 |
| Memory promotion with governance references | No bypass of Learning Gate | RDMS-01 / RDMS-07 |
| Reference to recovery-critical artifact | Artifact publish durability before legal reference | L1 with L7 interface |

## 7. Conflict and concurrency behavior

Canonical mutation is fenced by current epoch, expected entity versions and applicable hard constraints. An incompatible or stale proposal is rejected or re-evaluated through its owner; last-writer-wins cannot silently resolve semantic conflicts. A global version alone is insufficient to prove staleness of unrelated results.

## 8. Failure and recovery

Restore canonical snapshot, replay ledger, acquire current epoch, inspect unresolved actions and triggers; only then permit scoped execution through RDMS-09. Control-state absence cannot be replaced with unverifiable chat history.

## 9. Forbidden behaviors

No direct provider writes, no independently authoritative shadow ledger, no splitting atomic recovery-critical transitions, no treating diagnostic logs as a replacement for Control Ledger, no acknowledging storage durability outside its proven failure model.


## 10. Dependency and interface register

- Inputs: executive semantic authorizations from L2, action lifecycle references from L3, trigger/specialist continuations from L4, memory promotion references from L5.
- Reads: authority/policy/trust terms from L0.
- Outputs: durable legal events, state/version and epoch proofs consumed by L2–L7.

## 11. Pending effective-contract verification

- **PENDING EFFECTIVE CONTRACT AUDIT:** RDMS-01 and RDMS-02 final type definitions, exact events, transaction boundaries, rejection codes, provenance.
- **GAIA-R01:** verify Action Journal–Control Ledger ownership and atomic linkage against RDMS-04.

## 12. Layer conformance requirements

A layer cannot be marked `FROZEN_CONSOLIDATED` until: (a) the owning legal contracts are imported from their frozen source version without loss; (b) all cross-layer projections are typed and referenced; (c) invariants, authority, failure and recovery paths are covered by normative acceptance scenarios; (d) source hashes and changes are recorded in `ARCHITECTURE_MANIFEST.md`; (e) the layer's review explicitly approves the consolidated text.

---

# SOURCE-PRESERVED FCA v1.0.1 BASELINE ANNEX

**Source authority:** the immutable `Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md` file in `reviews/source_archive/`. These copied sections are exact FCA source excerpts, not newly approved RDMS definitions. Layer prose above remains a consolidation draft pending full RDMS source validation.
**Source SHA-256:** `74d0923cbd343b71740da0fc2368a84aad2ea97f8e4e15f156122f48ebe53539`

**Ownership note:** This document embeds its assigned FCA source sections once. Do not redefine these names in a second layer; refer to the original owner or validated public projection.

<!-- GAIA-SOURCE FCA-SECTION 06 SHA256=74df7481c463583772ddaef91581b8223661bd5896267bff7e44a8cc3ef83b1f -->
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

<!-- GAIA-SOURCE FCA-SECTION 48 SHA256=ccb6b64224f31f353fd63c697214ef5fe8717c5409cd63053c3006d1068bf821 -->
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

<!-- GAIA-SOURCE FCA-SECTION 49 SHA256=f0799d14dfde373ffb26e9f6205b665497853562cf44f895e02f1e7e6dd4dc5c -->
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

<!-- GAIA-SOURCE FCA-SECTION 50 SHA256=125f59fbb8cdac86621981b67d018d699afd4a3bc4b1205290606bd9964bad6e -->
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

<!-- GAIA-SOURCE FCA-SECTION 51 SHA256=6dd2f8fefc5d93b177235aa9a46fb2f82ce2db0e57ce31de6c67feea0c7e6687 -->
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

<!-- GAIA-SOURCE FCA-SECTION 74 SHA256=e493cb9fb56600bb9699bac3e8f58fd1cef41859a0c70d63069f45869ac515b5 -->
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

<!-- GAIA-SOURCE FCA-APPENDIX D SHA256=ad4ead81c8bf814733ac4b46a6c544f45f3463e0f9a3edd4cc46342252fcda45 -->
# Appendix D — Composite canonical-state view

The exact physical schema is implementation work, but the logical canonical state frozen by FCA can be summarized as:

```text
State {
  identity {
    project_id
    global_state_version
    repo_ref
    schema_version
    current_executive_epoch
  }

  goals {
    stack
    items[]
  }

  focus: FocusState

  model {
    domain
    structure
    runtime
    causal
    risk
  }

  epistemic {
    claims[]
    information_needs[]
    hypotheses[]
    observations[]
    evidence_links[]
    contradictions[]
    experiments[]
  }

  engineering {
    invariants[]
    contracts[]
    vocabulary[]
    decisions[]
    risks[]
  }

  execution {
    graph[]
    active_slice?
    deviations[]
    structural_diffs[]
    semantic_change_proposals[]
    verification_records[]
  }

  temporal {
    active_tasks[]
    suspended_tasks[]
    blocked_tasks[]
    waiting_tasks[]
    commitments[]
    triggers[]
    resumption_capsules[]
  }

  specialists[]

  memory_refs[]

  meta {
    confidence_profile
    contradictions[]
    prediction_errors[]
    stagnation_signals[]
    drift_signals[]
    residual_risks[]
    current_strategy
    cognitive_depth
  }

  control_refs {
    action_records[]
    control_events[]
    leadership_grant
  }
}
```

The physical implementation MAY normalize or separate these stores as long as authority, durability, consistency, and recovery semantics remain conformant.

---


---

## RDMS Verbatim Source Annexes — Phase 4 (historical draft + corrections + freeze decision)

> **SOURCE PRESERVATION, NOT NORMALIZED LAW.** The following original user-supplied text is included **verbatim** as a migration input. Drafts and later corrections coexist historically. Later approved corrective parts and freeze decisions must govern disagreements. This annex does not itself certify exact schema compatibility or replace the original archive. Do not implement directly until semantic reconciliation is completed.

### Original source set: RDMS-01

Archive: `../reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-01_APPROVED_SOURCE_SET.txt`  
SHA-256 of complete source set: `b5b023dff0003f456d13e9d0492d674d36860427dda67874157467c19721038b`  
Contained original message parts: 2

````text
RDMS-01 — ORIGINAL APPROVED SOURCE SET
Source: https://chatgpt.com/share/6ac82d7b-ba7c-83ea-a3a9-b41734948bb2

ملاحظة تحريرية: هذا الملف تجميع للنصوص الأصلية المسترجعة من المحادثة، لا إعادة صياغة ولا مواصفة موحدة جديدة. حالة التجميد مثبتة في قرار المراجعة النهائي المرفق؛ عبارة DRAFT داخل النص الأساسي تصف مرحلته التاريخية قبل التصحيحات. تُقرأ المسودة مع التصحيحات وقرار الاعتماد، ولا يجوز استعمال نص سابق يخالف تصحيحًا معتمدًا لاحقًا. لم نغير نصوص القوانين ولم نضف FCA.


========================================================================
SOURCE PART: Original draft
MESSAGE ID: 2aacdc73-38d8-4456-9a73-9900fe14f900
BEGIN ORIGINAL MESSAGE
========================================================================

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

3. Control Ledger — Source of Truth

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

ControlCommit {
    commit_id

    project_id

    commit_seq

    schema_version

    executive_epoch?

    idempotency_key

    actor

    cause?

    correlation_id?

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

END ORIGINAL MESSAGE

========================================================================
SOURCE PART: R1 corrections and final freeze decision
MESSAGE ID: e3a45231-ddae-4ed4-9bd1-35202ecdfcf7
BEGIN ORIGINAL MESSAGE
========================================================================

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

END ORIGINAL MESSAGE
````

