# GAIA-C05 — Source-anchored legal deltas (RDMS-03/04/05)

**Scope:** 12 additional witness pairs, not a claim that every correction across RDMS-01…10 has been normalized. The classification is a narrow reading of the cited clauses. Original text below is verbatim.

**Precedence:** An approved later correction controls its own explicit domain when incompatible with an earlier draft; earlier fields not expressly removed are not silently deleted.

## C05-W01 — `Observation` (REQUIRED_TRUST_METADATA_ADDED)

- Owner: `L3_ACTIONS.md`; route `X8-07`.
- Controlled reading: Observation raw text must retain a trust context; no wording-based promotion of authority.
- Original: `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 69–98, SHA-256 `09d0a3e293271505e1a861dcf1b35b6bd1972e8859ee8551b77c65fb63e6ae49`.
- Correction: `a1ca0249-b287-4c4b-8254-773c8f6edbda`, lines 11–58, SHA-256 `c826880def32c3b735258daac8ed86a35266357a2b33bcffb13df3ed898570c2`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
3. Observation
Observation {
    observation_id
    project_id

    observation_kind

    source_ref

    subject_ref?

    observed_at
    ingested_commit_seq

    repo_ref?
    world_ref?
    environment_ref?

    normalized_content

    raw_artifact_ref?

    provenance

    capture_integrity

    origin_ref?
}

Observations are immutable after canonical append.
```

### Approved correction (unedited)
```text
C01-01 — Content Trust Must Travel With Content

كل Observation تحمل:

trust_context_ref

ويشير إلى immutable:

ContentTrustContext {
    trust_context_id

    content_role:
        DATA
        CODE
        DOCUMENTATION
        TOOL_OUTPUT
        HUMAN_REQUIREMENT
        SYSTEM_POLICY
        OTHER

    instruction_authority:
        NONE
        USER_TASK
        PROJECT
        SYSTEM

    source_trust_class

    domain_authority_binding_ref?

    created_commit_seq
}

القاعدة:

Content and trust metadata are inseparable at every reasoning boundary.

أي Retrieval يرسل Observation إلى Reasoning Provider يجب أن يرسل معها Trust Context.

غير قانوني:

retrieve normalized_content
↓
drop trust metadata
↓
send text to LLM

هذا يمنع prompt injection من العودة أثناء retrieval.
```

## C05-W02 — `ObservationAmendment` (AMENDMENT_AUTHORITY_NARROWED)

- Owner: `L3_ACTIONS.md`; route `X8-07`.
- Controlled reading: Observation immutability retained; corrections concern capture/provenance, not semantic disagreement.
- Original: `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 385–423, SHA-256 `dcc476fd9ef111d3a966b8a9ad80ee165a703955b4e6a86df4e74d1d75349f78`.
- Correction: `a1ca0249-b287-4c4b-8254-773c8f6edbda`, lines 185–251, SHA-256 `6eda08648abe96f2dd8a8ae0ecbed0697c72e6599a600491af15cf928fe52a0c`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
ObservationAmendment {
    amendment_id

    target_observation_id

    kind:
        CAPTURE_INVALID
        NORMALIZATION_REPLACED
        METADATA_CORRECTED
        DUPLICATE_OF

    replacement_observation_id?
    duplicate_of_observation_id?

    rationale
    authority_ref

    created_commit_seq
}
18. Observation Usability

Derived:

ObservationUsability:
    USABLE
    DEGRADED
    INVALID_CAPTURE
    SUPERSEDED_CAPTURE
    DUPLICATE

This is computed from:

capture_integrity
+
ObservationAmendments

It is not another mutable status copied into Observation.

19. Source Being Wrong Is Not a Capture Correction
```

### Approved correction (unedited)
```text
C01-07 — Observation Amendment Governance

ObservationAmendment تصبح:

ObservationAmendment {
    amendment_id

    target_observation_id

    kind:
        CAPTURE_INVALID
        NORMALIZATION_REPLACED
        METADATA_CORRECTED
        DUPLICATE_OF

    basis_refs[]

    replacement_observation_id?
    duplicate_of_observation_id?

    capture_governance_authority_ref

    rationale

    created_commit_seq
}
C01-08 — Semantic Disagreement Cannot Amend Observation

قانون صارم:

ObservationAmendment may correct capture/provenance defects; it may never erase inconvenient meaning.

غير قانوني:

Observation contradicts my hypothesis
↓
CAPTURE_INVALID

قانوني:

parser truncated half the HTTP body
↓
CAPTURE_INVALID / replacement

أو:

same source event accidentally ingested twice
↓
DUPLICATE_OF
C01-09 — Observation Usability

تظل Observation immutable.

ويُشتق:

ObservationUsability:
    USABLE
    DEGRADED
    INVALID_CAPTURE
    SUPERSEDED_CAPTURE
    DUPLICATE

من:

capture_integrity
+
ObservationAmendments
```

## C05-W03 — `EvidenceLink` (EVIDENCE_BASIS_REFINED)

- Owner: `L2_COGNITION.md`; route `X8-07`.
- Controlled reading: Multiple observations have roles and combination rules; historical acceptance is not current usability.
- Original: `11d811dc-87b8-4c44-8322-bdae96f7b95d`, lines 449–480, SHA-256 `b56d24206ab7628d92c266e4a6d8c3e3a63aa29a627ede82c373819a56071e26`.
- Correction: `a1ca0249-b287-4c4b-8254-773c8f6edbda`, lines 252–329, SHA-256 `301cd6b3a855a356ebae172f062c56fe284f5f18a25f6aee8d2894fd47b747c2`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
EvidenceLink {
    evidence_link_id

    observation_refs[]

    target_ref

    relation:
        SUPPORTS
        WEAKENS
        CONTRADICTS
        RELEVANT

    derivation:
        DETERMINISTIC
        SEMANTIC
        AUTHORITATIVE

    rationale

    derivation_ref?

    dependency_set_ref?

    lifecycle:
        PROPOSED
        ACCEPTED
        REJECTED
        SUPERSEDED

    accepted_commit_seq?
}
```

### Approved correction (unedited)
```text
C01-10 — Evidence Basis Semantics

EvidenceLink لم تعد تحمل observation_refs[] غامضة فقط.

نضيف:

EvidenceBasis {
    items[] {
        observation_id

        role:
            REQUIRED
            CORROBORATING
            CONTEXT
    }

    combination:
        ALL_REQUIRED
        STRUCTURED
}
C01-11 — ALL_REQUIRED

إذا:

combination = ALL_REQUIRED

فكل REQUIRED Observation يجب أن تكون usable.

إذا واحدة تصبح:

INVALID_CAPTURE

فـEvidenceLink لا تبقى usable كأن شيئًا لم يحدث.

C01-12 — STRUCTURED

يستخدم عندما العلاقة ليست مجرد conjunction.

مثال causal sequence:

O1 = failure before intervention
O2 = intervention actually occurred
O3 = failure absent afterward

ويجب أن يحدد:

derivation_ref

المنطق الذي يربط الأدوار.

لا يسمح بـfree-form ambiguity.

C01-13 — EvidenceLink Usability

EvidenceLink accepted لا يعاد كتابتها.

نحسب:

EvidenceLinkUsability:
    CURRENT
    STALE
    INVALID_BASIS
    UNKNOWN

من:

Observation usability
AuthorityBinding validity
DependencySet freshness
derivation validity

وبذلك نحافظ على التاريخ:

"This interpretation was accepted at commit N"

مع القدرة على القول:

"Do not rely on it now."
```

## C05-W04 — `ActionAttempt` (EXECUTION_IDENTITY_REFINED)

- Owner: `L3_ACTIONS.md`; route `X8-06`.
- Controlled reading: ActionProposalId / ActionId / AttemptId / DispatchId are separate identifiers.
- Original: `32ad532a-40cd-4b2a-8a0a-3372937cf6db`, lines 254–285, SHA-256 `d6672e9ce719da28c832b6f8214d24452b72d723fa449f36fa14315c8cfba81e`.
- Correction: `4f585132-49b6-448d-8506-4b502aee6311`, lines 39–56, SHA-256 `68ae8c4e36f7f61a79771b5875b5396dc72ec24d6fe38208a53b67ab20b9fef5`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
8. ActionAttempt

نفصل Action عن كل محاولة إرسال.

ActionAttempt {
    attempt_id
    action_id

    attempt_number

    authorization_ref

    dispatch_intent_commit_seq

    executor_ref
    execution_context_ref

    dispatch_ack_ref?

    execution_started_at?
    execution_ended_at?

    reported_result_ref?

    outcome_probe_refs[]

    attempt_outcome:
        UNKNOWN
        REPORTED_SUCCESS
        REPORTED_FAILURE
        OBSERVED_PARTIAL_EFFECT
        EFFECT_CONFIRMED
```

### Approved correction (unedited)
```text
C01-02 — Action Execution Identity

نفصل أربع هويات:

ActionProposalId
  └── ActionId
        └── AttemptId
              └── DispatchId

ActionProposalId: طلب ذو معنى هندسي محدد.

ActionId: العملية المعتمدة داخل المشروع.

AttemptId: محاولة واحدة لتنفيذ العملية.

DispatchId: هوية عملية الإرسال الواحدة إلى Executor أو العالم الخارجي.

لا تعتبر إعادة إرسال رسالة إلى Executor محاولة جديدة تلقائيًا؛ يجب التحقق من DispatchId الحالية أولًا.
```

## C05-W05 — `DispatchOwnership` (DURABLE_DISPATCH_PRECONDITION)

- Owner: `L3_ACTIONS.md`; route `X8-06`.
- Controlled reading: Ownership and durable intent precede external dispatch; DISPATCH_INTENT is not evidence that effects occurred.
- Original: `32ad532a-40cd-4b2a-8a0a-3372937cf6db`, lines 225–252, SHA-256 `356212119249e0d9539f397a04cb38cb2253a2b2908bac8802844f17de7a8cfb`.
- Correction: `4f585132-49b6-448d-8506-4b502aee6311`, lines 58–106, SHA-256 `023cecb0d53bb8405f7d592048b9dc929515941d04e6a5dada921141154770d8`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
7. Action Lifecycle

نحافظ على حالات FCA:

PROPOSED
    ↓
AUTHORIZED
    ↓
DISPATCH_INTENT
    ↓
RESULT_REPORTED
    ↓
EFFECT_VERIFIED
    ↓
RECONCILED

لكن التنفيذ ليس دائمًا نجاحًا خطيًا.

المسارات البديلة تشمل:

PARTIAL
FAILED
IN_DOUBT
RECONCILING

هذه الحالات لها معانٍ مختلفة.

FAILED لا تستخدم لمجرد أن الأمر انتهى برمز خروج غير صفري؛ يجب أن نحدد هل الفشل متعلق بمحاولة العملية، أو بالمهمة المطلوبة، أو بالتأثير الخارجي.
```

### Approved correction (unedited)
```text
C01-03 — Durable Dispatch Ownership
DispatchOwnership {
    action_id
    attempt_id
    dispatch_id

    executor_id
    executor_generation

    executive_epoch
    fencing_token

    ownership_state:
        CLAIMED
        DISPATCH_POSSIBLE
        RELEASED
        UNCERTAIN

    claimed_at_commit_seq
}

إنشاء CLAIMED يتم بمعاملة atomic compare-and-set مقابل النسخة المتوقعة من ActionRecord.

لا يُسمح لمحاولتين متنافستين بحيازة حق dispatch جديد لنفس الأثر عندما لا تسمح retry policy بذلك.

C01-04 — Dispatch Protocol
AUTHORIZED
    ↓
Validate current authority and preconditions
    ↓
Atomic DispatchOwnership CLAIMED
    ↓
Persist DISPATCH_INTENT
    ↓
Durability acknowledged
    ↓
Executor validates claim and fencing
    ↓
External dispatch boundary
    ↓
Result / Unknown
    ↓
Observation / Reconciliation

القاعدة المهمة:

لا يجوز إرسال shared-world mutation قبل إقرار durable dispatch intent.

لكن وصول العملية إلى DISPATCH_INTENT لا يثبت أنها أُرسلت فعلًا.
```

## C05-W06 — `ExternalEffect` (EXACTLY_ONCE_CLAIM_CONSTRAINED)

- Owner: `L3_ACTIONS.md`; route `X8-06`.
- Controlled reading: Epoch cutover cannot retroactively undo external effects; never claim exactly-once without external guarantees.
- Original: `32ad532a-40cd-4b2a-8a0a-3372937cf6db`, lines 343–353, SHA-256 `27faab5303c5e0824ee7f58bfd66b3abe818d73eb54dea11fc17d45659cc0dae`.
- Correction: `4f585132-49b6-448d-8506-4b502aee6311`, lines 108–142, SHA-256 `c390974a765aa0e57a93c3da2259a4b67aa76d518a91b99447158e1c37490f52`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
    verification_mode:
        DIRECT_EFFECT
        ACKNOWLEDGEMENT_ONLY
        BEST_EFFORT

    timeout_policy_ref
}

Idempotent لا تعني exactly-once.

يجب أن تدعم الخدمة أو الأداة المعنية semantics اللازمة، وإلا لا يجوز الادعاء أن إعادة الإرسال آمنة.
```

### Approved correction (unedited)
```text
C01-05 — Executive Epoch Change

نحدد ثلاثة سيناريوهات.

A — Authorization قديمة لم تصل إلى dispatch:

تحتاج adoption أو إعادة تفويض وفق سلطة Executive الجديدة.

B — DispatchIntent معتمدة لكن لا يوجد دليل كافٍ على الإرسال أو عدمه:

لا نعيد التنفيذ تلقائيًا. ندخل recovery/reconciliation أو IN_DOUBT.

C — External dispatch بدأت بالفعل:

الـepoch الجديدة لا تستطيع إلغاء التاريخ. تتولى reconciliation وتمنع العمليات المتعارضة.

الـfencing يجب أن يُفرض عند trusted executor boundary، وعند النظام الخارجي إن كان يدعمه.

إذا لم يستطع النظام الخارجي احترام fencing، فلا نزعم منع كل أثر صادر بالفعل عن محاولة قديمة.

C01-06 — The External Exactly-Once Limit

يمكن للـRuntime أن تضمن، ضمن شروط تنفيذها:

عدم اعتماد DispatchOwnership متنافسة لنفس الأثر.

عدم إنشاء retry غير قانونية.

حفظ كل dispatch محتملة.

وقف العمليات المتعارضة عند عدم اليقين.

لكنها لا تضمن exactly-once external effect دون دعم كافٍ من النظام الخارجي.

هذا حد معماري صريح.
```

## C05-W07 — `TriggerDefinition` (GENERATION_SNAPSHOT_REQUIRED)

- Owner: `L4_TEMPORAL_SPECIALISTS.md`; route `X8-04`.
- Controlled reading: Trigger change produces new generation with frozen snapshot, not retroactive reinterpretation.
- Original: `6276f296-457b-462d-b674-933a15194429`, lines 143–176, SHA-256 `0118b5c8a747a119455ef333f57c47c713c736c363073a2d56a5ab917602837b`.
- Correction: `77caba5f-8e8e-4b8e-a9fe-027c4801efad`, lines 291–322, SHA-256 `5eafdafd656f0767464fa5975e24f65e38631068ff1c64c907510f71286bdcff`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
6. TriggerDefinition

نصحح نقطة غموض في التصور الأولي: ONE_SHOT / REARMABLE ليست بدائل منطقية لـLEVEL_TRIGGERED / EDGE_TRIGGERED.

الأولى تصف التكرار، والثانية تصف كيفية اكتشاف الشرط.

TriggerDefinition {
    trigger_id
    project_id

    generation

    condition_ref

    fire_policy:
        ONE_SHOT
        REARMABLE

    detection_policy:
        LEVEL_TRIGGERED
        EDGE_TRIGGERED

    source_refs[]

    reaction_spec_ref

    owner_ref
    linked_object_ref

    created_commit_seq
    entity_version
}

وهذا يحافظ على معاني FCA الأصلية مع تحويلها إلى بعدين مستقلين.
```

### Approved correction (unedited)
```text
C01-12 — TriggerDefinitionSnapshot
TriggerDefinitionSnapshot {
    trigger_id
    generation

    condition_snapshot_ref
    reaction_spec_snapshot_ref

    source_contract_refs[]
    evaluation_policy_ref

    fire_policy
    detection_policy
    rearm_policy_ref?

    definition_fingerprint

    activated_commit_seq
}

أي تغيير مادي في:

condition
reaction
source assumptions
detection semantics
rearm rules

يتطلب generation جديدة.

لا يُعاد تفسير Fire سابقة بناءً على تعريف لاحق.

```

## C05-W08 — `TriggerFire` (FIRE_IDENTITY_SCHEMA_REFINED)

- Owner: `L4_TEMPORAL_SPECIALISTS.md`; route `X8-04`.
- Controlled reading: Stable occurrence identity and definition-snapshot binding disambiguate fire replay.
- Original: `6276f296-457b-462d-b674-933a15194429`, lines 439–468, SHA-256 `ddcc501dd024d5ad717513d8b847bf01d34968c034b8ab8067f9c497a078b300`.
- Correction: `77caba5f-8e8e-4b8e-a9fe-027c4801efad`, lines 323–367, SHA-256 `ea7e8c2e7a77ea891ad80f0aad70ac38d6d61aeac31ed6a20e9706cd1c8026dd`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
TriggerFire {
    fire_id

    trigger_id
    generation

    condition_version_ref

    triggering_basis_refs[]

    source_frontier_ref

    fire_identity_key

    fired_at_commit_seq
}
22. Idempotent Fire Identity

لا تُنشأ fire_id جديدة لمجرد إعادة تقييم نفس الحدث بعد restart.

يُشتق مفتاح هوية fire بصورة مستقرة من:

trigger identity
generation
qualified occurrence identity
reaction identity

بحسب trigger semantics.

أما periodic/recurring triggers فيجب أن تكون لها occurrence identity مميزة لكل موعد قانوني.
```

### Approved correction (unedited)
```text
C01-13 — QualifiedOccurrenceIdentity

نضيف:

QualifiedOccurrenceIdentity {
    trigger_id
    generation

    occurrence_kind:
        SOURCE_EVENT
        EDGE_TRANSITION
        LEVEL_CYCLE
        SCHEDULE_OCCURRENCE

    occurrence_key

    identity_derivation_version
}

الهوية تُبنى من الحدث أو الدورة المؤهلة نفسها، لا من وقت معالجة worker.

C01-14 — Stable TriggerFire
TriggerFire {
    fire_id

    trigger_definition_snapshot_ref
    qualified_occurrence_ref

    evidence_basis_refs[]
    source_frontier_ref

    fire_identity_key

    created_commit_seq
}

مع uniqueness constraint على:

trigger_id
generation
occurrence_key

حيث تحدد سياسة trigger أي occurrences قانونية.

أي إعادة معالجة لنفس occurrence تعيد Fire نفسها، لا كيانًا جديدًا.
```

## C05-W09 — `TriggerProcessing` (ATOMIC_TRIGGER_COMMIT_REQUIRED)

- Owner: `L4_TEMPORAL_SPECIALISTS.md`; route `X8-04`.
- Controlled reading: Event persistence and trigger processing cursors differ; durable trigger outcome precedes processing cursor advance.
- Original: `6276f296-457b-462d-b674-933a15194429`, lines 437–469, SHA-256 `1af303e417ce83c3284c2bbb17fac62c5138cfc1f4f119ff913ca3cd921abf1f`.
- Correction: `77caba5f-8e8e-4b8e-a9fe-027c4801efad`, lines 124–180, SHA-256 `6edfd718d7336ecbfd8114a2eec6a632e4b181e4789bec85c1f62040dc8c7055`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
PART VII — TRIGGER FIRE & REACTION
21. TriggerFire
TriggerFire {
    fire_id

    trigger_id
    generation

    condition_version_ref

    triggering_basis_refs[]

    source_frontier_ref

    fire_identity_key

    fired_at_commit_seq
}
22. Idempotent Fire Identity

لا تُنشأ fire_id جديدة لمجرد إعادة تقييم نفس الحدث بعد restart.

يُشتق مفتاح هوية fire بصورة مستقرة من:

trigger identity
generation
qualified occurrence identity
reaction identity

بحسب trigger semantics.

أما periodic/recurring triggers فيجب أن تكون لها occurrence identity مميزة لكل موعد قانوني.

```

### Approved correction (unedited)
```text
C01-04 — Acknowledgement Fence

الترتيب القانوني:

Receive external event
        ↓
Validate ingress envelope
        ↓
Durably store event identity and content
        ↓
Verify durable persistence
        ↓
Acknowledge external delivery
        ↓
Evaluate relevant triggers

لا يُرسل acknowledgement ناجح إلى المصدر قبل ضمان حفظ الحدث إذا كانت دلالات المصدر تسمح بهذا البروتوكول.

إذا فشل الحفظ، لا يجوز الادعاء بأن الحدث تمت معالجته.

وإذا كان المصدر لا يوفر إعادة تسليم موثوقة بعد فشل الإقرار، فيجب تسجيل حد الضمان ووجود احتمال لفجوة.

C01-05 — Two Different Cursor Concepts

نمنع الخلط بين حفظ الحدث ومعالجته:

IngressCursor
    Tracks durable capture from source

TriggerProcessingCursor
    Tracks durable trigger evaluation obligations

قد تتقدم IngressCursor عندما تُحفظ الأحداث في Durable Inbox، حتى لو لم تقيّم جميع Triggers بعد.

أما TriggerProcessingCursor فلا تتقدم متجاوزة حدثًا إلا بعد حفظ نتيجة تقييمه وما يلزم من Fire/Reaction أو التزام إعادة تقييم مؤجل.

بهذا لا نحتاج إلى تعليق استلام كل الأحداث بسبب Trigger بطيئة، ولا نفقد أحداثًا بسبب التقدم المبكر للمؤشر.

C01-06 — Atomic Trigger Processing

بالنسبة إلى حدث مؤهل:

Read durable event E
        ↓
Evaluate trigger T
        ↓
One ControlCommit:
    TriggerEvaluation
    TriggerFire if qualified
    TriggerReactionIntent if fired
    TriggerProcessingCursor advancement

إذا كانت النتيجة UNKNOWN وتحتاج إعادة تقييم مستقبلية، يُحفظ واجب إعادة التقييم قبل تقدم المؤشر.

إذا وقع crash قبل ControlCommit، تعاد المعالجة.

إذا وقع crash بعدها، تستخدم replay نفس الهويات ولا تنشئ reactions جديدة.
```

## C05-W10 — `ResumptionCapsule` (SCHEMA_NOT_CLOSED)

- Owner: `L4_TEMPORAL_SPECIALISTS.md`; route `X8-05`.
- Controlled reading: Correction has smaller top-level capsule schema; must preserve old context in pinned durable payload before declaring a lossless mapping.
- Original: `6276f296-457b-462d-b674-933a15194429`, lines 642–678, SHA-256 `c1d22ca4a7ddbf38aa27abd8caa3fbbf1587f636463b3d7827b840bc809528b1`.
- Correction: `77caba5f-8e8e-4b8e-a9fe-027c4801efad`, lines 719–743, SHA-256 `3bf68824ac7536fef84c30d05f24ad2f2484f4d63ff423915af866a9c4835f51`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
ResumptionCapsule {
    capsule_id

    project_id
    task_or_goal_ref

    suspended_from_state

    base_canonical_commit_seq

    repo_ref?
    world_ref?
    environment_ref?

    dependency_set_ref?

    current_focus_ref?

    relevant_claim_refs[]
    relevant_hypothesis_refs[]
    relevant_evidence_refs[]

    decision_refs[]
    rejected_path_refs[]

    active_slice_refs[]
    unresolved_action_refs[]

    open_information_need_refs[]
    commitment_refs[]

    temporary_change_refs[]

    next_action_proposal_ref?

    created_commit_seq
}
```

### Approved correction (unedited)
```text
C01-34 — Durable Capsule Content
ResumptionCapsule {
    capsule_id

    task_or_goal_ref

    suspended_from_state

    canonical_snapshot_ref

    relevant_entity_refs[]

    dependency_set_ref

    unresolved_action_refs[]

    next_action_proposal_ref?

    durable_payload_artifact_ref
    content_integrity_ref

    created_commit_seq
}

تظل Capsule دليل استرجاع وسياق، وليست مصدرًا ثانيًا للمعرفة.
```

## C05-W11 — `SuspensionTransition` (DURABLE_SUSPENSION_PRECONDITION)

- Owner: `L4_TEMPORAL_SPECIALISTS.md`; route `X8-05`.
- Controlled reading: Persist and verify capsule payload before one ControlCommit marks SUSPENDED and reactivation obligations.
- Original: `6276f296-457b-462d-b674-933a15194429`, lines 694–708, SHA-256 `0cf2f6bdb3eaec9598d04d3f774148924738fbdf7da3510f6d1648a128b20a04`.
- Correction: `77caba5f-8e8e-4b8e-a9fe-027c4801efad`, lines 745–769, SHA-256 `442fa060d510810ffbf15cd26173d3d6828c41abdd9d93011b0c70b634b757c8`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
33. Capsule Creation

عند تعليق مهمة:

Validate suspension transition
↓
Persist ResumptionCapsule
↓
Persist work status
↓
Arm required triggers
↓
Commit atomically

لا يجوز أن تكون المهمة SUSPENDED بصورة قانونية دون Capsule قابلة للاسترجاع.
```

### Approved correction (unedited)
```text
C01-35 — Atomic Suspension

الترتيب:

Prepare capsule payload
    ↓
Durably store and verify payload
    ↓
One ControlCommit:
    attach capsule reference
    change work lifecycle to SUSPENDED
    establish reactivation obligations

إذا لم يكتمل حفظ Capsule بصورة قابلة للاسترجاع، لا يجوز اعتماد انتقال SUSPENDED.

C01-36 — Missing or Corrupted Capsule

إذا اكتُشف تلف لاحق:

Capsule usability = INVALID / UNKNOWN

لا نعيد تشغيل next_action_proposal_ref تلقائيًا.

يدخل العمل Recovery Path لإعادة البناء من الكيانات canonical الباقية، مع تسجيل نقص الأدلة.

```

## C05-W12 — `SafeResume` (RECOVERY_SEQUENCE_REFINED)

- Owner: `L6_RECOVERY.md`; route `X8-05`.
- Controlled reading: Resume must validate context and unresolved actions and cannot replay shell commands solely because trigger fired.
- Original: `6276f296-457b-462d-b674-933a15194429`, lines 718–749, SHA-256 `37822f842534ad75e8fe0878b050f33f9b896a095a84eaeb4b2bd1b9858fffaf`.
- Correction: `77caba5f-8e8e-4b8e-a9fe-027c4801efad`, lines 773–798, SHA-256 `d2b2875ebc95ed51775ba907e359246882e6e92b907d05df71101e0537243cb0`.
- **Limit:** This is not a ratified transport schema or executable transaction proof.

### Original (historical, unedited)
```text
PART XI — RESUMPTION PROTOCOL
35. Resume Sequence
1. Detect eligible reactivation
           ↓
2. Acquire valid Executive epoch
           ↓
3. Restore canonical project state
           ↓
4. Load ResumptionCapsule
           ↓
5. Inspect unresolved ActionRecords
           ↓
6. Reconcile potentially dispatched effects
           ↓
7. Compare relevant repo/world/environment
           ↓
8. Evaluate dependency freshness
           ↓
9. Revalidate Goal, Slice, Decisions
           ↓
10. Rebuild current focus
           ↓
11. Replan if necessary
           ↓
12. Authorize next work

هذه ليست مجرد إعادة إرسال آخر prompt إلى LLM.

36. ResumeAssessment
ResumeAssessment {
    assessment_id

```

### Approved correction (unedited)
```text
C01-37 — Safe Resume Protocol
Trigger fires
    ↓
ReactivationRequest
    ↓
Acquire valid Executive epoch
    ↓
Restore canonical state
    ↓
Validate capsule integrity
    ↓
Inspect unresolved ActionRecords
    ↓
Reconcile relevant external effects
    ↓
Evaluate repo/world/environment changes
    ↓
Dependency Evaluation Engine
    ↓
Validate Goal/Slice/Decision scope
    ↓
Executive resumes cognition or replans
    ↓
New Action authorization if needed

الـTrigger لا تستأنف Shell command بنفسها.
```
