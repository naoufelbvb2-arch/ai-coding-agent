# GAIA-C04 — Verified Source-Backed Supersessions and Clarifications

**Scope:** Explicit cases with source excerpts; not approval of every implicit or unnumbered correction. Source text blocks below are verbatim and kept separate from editorial commentary.

## C04-W01 — Event-sourcing projection-only assertion replaced by one authoritative ControlCommit atomic mutation+ledger model
**Effective:** RDMS-01, message `e3a45231-ddae-4ed4-9bd1-35202ecdfcf7`, source lines 13–41. **Old:** 2aacdc73-38d8-4456-9a73-9900fe14f900

### Effective source (verbatim)
```text

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
```

### Earlier source (historical; superseded insofar as incompatible)
```text

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
```

## C04-W02 — ControlCommit fields and authority-context distinction are replaced in R1
**Effective:** RDMS-01, message `e3a45231-ddae-4ed4-9bd1-35202ecdfcf7`, source lines 137–181. **Old:** 2aacdc73-38d8-4456-9a73-9900fe14f900

### Effective source (verbatim)
```text
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
```

### Earlier source (historical; superseded insofar as incompatible)
```text
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
```

## C04-W03 — commit_seq strictly increasing, not necessarily gapless
**Effective:** RDMS-01, message `e3a45231-ddae-4ed4-9bd1-35202ecdfcf7`, source lines 110–137. **Old:** 2aacdc73-38d8-4456-9a73-9900fe14f900

### Effective source (verbatim)
```text
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
```

### Earlier source (historical; superseded insofar as incompatible)
```text

لا نعتمد على timestamps لترتيب الحقيقة.

لأن:

clock time
≠
causal commit order

الترتيب الرسمي:

(project_id, commit_seq)
6. Event Ordering داخل Commit واحدة

لأن commit قد تحتوي أحداثًا متعددة:
```

## C04-W04 — Physical UUID choice made implementation boundary; typed IDs still required
**Effective:** RDMS-01, message `e3a45231-ddae-4ed4-9bd1-35202ecdfcf7`, source lines 366–384. **Old:** 2aacdc73-38d8-4456-9a73-9900fe14f900

### Effective source (verbatim)
```text
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
```

### Earlier source (historical; superseded insofar as incompatible)
```text
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
```

## C04-W05 — Remove shared CanonicalEntity.lifecycle_status and use CanonicalEntityMeta + own domain lifecycle
**Effective:** RDMS-02, message `266bb347-d2a5-41ea-872a-32e140c803eb`, source lines 11–35. **Old:** a62cc59d-b288-4be8-97c4-ac84d835a933

### Effective source (verbatim)
```text
C01-01 — Common Entity Metadata

نلغي تمامًا:

CanonicalEntity.lifecycle_status

كل Entity تملك lifecycle واحدة فقط داخل schema الخاصة بها.

الـcommon metadata:

CanonicalEntityMeta {
    entity_id
    project_id

    entity_version

    created_commit_seq
    updated_commit_seq

    payload_schema_version

    creation_provenance_ref?
}

لا توجد حالة domain عامة هنا.
```

### Earlier source (historical; superseded insofar as incompatible)
```text
database engine
physical indexes
2. Common Canonical Entity Envelope

كل entity canonical mutable تستخدم envelope مشتركة:

CanonicalEntity {
    entity_id
    project_id

    entity_version

    created_commit_seq
    updated_commit_seq

    payload_schema_version

    lifecycle_status

    created_from?
}

created_from هي typed provenance reference وليست free-form string.

مثال:

USER_REQUEST
CAPABILITY_RESULT
OBSERVATION
EXPERIMENT
DECISION
SPECIALIST_RESULT
RECOVERY
Rule

created_from لا تمنح authority.

هي provenance فقط.

3. Reference Model

```

## C04-W06 — Commitment use one reactivation-condition root instead of three competing mechanisms
**Effective:** RDMS-02, message `266bb347-d2a5-41ea-872a-32e140c803eb`, source lines 907–943. **Old:** a62cc59d-b288-4be8-97c4-ac84d835a933

### Effective source (verbatim)
```text
C01-32 — Commitment Reactivation

نستبدل:

due_at
removal_trigger_id
revisit_trigger_id

كآليات متوازية غير واضحة بـ:

reactivation_condition_ref
Commitment {
    ...

    reactivation_condition_ref

    status:
        ACTIVE
        DUE
        SATISFIED
        CANCELLED
        SUPERSEDED

    resolution_ref?
}

معنى:

ANY_OF
ALL_OF
time + triggers

سيُجمد داخل RDMS-05.

لكن RDMS-02 تفرض فقط:

Every ACTIVE Commitment must have one valid reactivation-condition root.
```
