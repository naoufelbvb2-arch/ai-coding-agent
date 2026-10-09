<!-- GAIA-C01-PHASE13-CURRENT-STATUS START -->
# CURRENT READING GUIDE — GAIA-C01 Phase 13

**STATUS: CONSOLIDATION DRAFT; NOT FROZEN.**  
**Owned responsibility:** Recovery lifecycle, fencing and resilience.  
**Source rule:** Full original normative texts remain unmodified in the archived source set and the source annex of this document. A historical draft is NOT automatically the effective current law: approved C01/C02/C03 corrections and final freeze decisions must be incorporated before the consolidated layer supersedes those sources. Phase 11 reference tests are not production/runtime verification.  
**Forbidden:** silent defaulting, missing-authority inference, lossy migration, or treating transport wrappers as canonical entities.

**FCA source sections/appendices assigned:** 3.  
**RDMS source sets assigned:** 1; **approved original message parts:** 5.  
**27-name ownership subset present here:** 0.

| Attached RDMS source | Original message parts | Source interpretation |
|---|---:|---|
| RDMS-09 | 5 | Original draft + approved corrections / freeze decision, read with precedence |

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

**Owning layer:** `L6`. **Published reused names:** `0`.

No audited duplicate canonical data type in the 27-name registry is primarily owned by this layer. Consult the original FCA/RDMS source annex below for this layer’s other definitions.

**Publication guard:** No inferred fields, default values, status promotions, action permissions, or silent renames are authorized by this section.
<!-- GAIA-C01-PHASE9 CONTRACT PUBLICATION END -->


---

# L6 — Recovery, Resilience & Continuity

> **CONSOLIDATION DRAFT — NOT FROZEN.** This file is a working per-layer consolidation, **not** an independently approved replacement for the frozen FCA/RDMS source specifications. Normative FCA source: `../reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md` (SHA-256 `74d0923cbd343b71740da0fc2368a84aad2ea97f8e4e15f156122f48ebe53539`). RDMS-01…10 original source sets arrived in GAIA-C01 Phase 4. Effective cross-source schemas and ownership remain **PENDING RECONCILIATION**; the archived original text below is untouched.

> **Phase 5:** source-name audit and non-normative proposals: `../reviews/GAIA_C01_PHASE5_CONTRACT_RECONCILIATION.md`. Original FCA and RDMS annexes below retain their historical authority/status; proposed aliases are not approved laws.

**Layer owner:** RDMS-09; FCA recovery laws  
**Authoritative FCA trace:** FCA §§43–52, 72–75, 80–82  
**Migration status:** CONSOLIDATED DRAFT / REVIEW REQUIRED  
**Source status:** FCA v1.0.1 hash-verified; RDMS source sets imported; effective contract reconciliation pending.

## 1. Scope and charter

L6 coordinates authoritative restart, crash recovery, data-quarantine and external effect reconciliation. It is **not** a shadow Cognitive Executive and cannot bypass L1/L3.

## 2. Startup sequence (FCA §52)

```text
1 Restore canonical snapshot
2 Replay Control Ledger
3 Obtain valid Executive epoch
4 Inspect unresolved ActionRecords
5 Reconcile possible external effects
6 Replay/evaluate durable triggers
7 Inspect Specialist workspaces
8 Validate dependency freshness
9 Restore active/suspended/blocked work
10 Resume normal Executive control
```

Operational bootstrap can repair control infrastructure under separate trusted scope before this sequence, but it must not create new cognitive authority.

## 3. Unknown effects

An action possibly dispatched cannot be assumed failed because of timeout, lost ack or worker death. Reconstruct journal and classify via RDMS-04. Protect safety while allowing proven-independent operations to resume.

## 4. Recovery authority and anti-rollback

Recovering an old snapshot cannot reinstate old Executive epochs, old policies or erased data permissions. Bootstrap handoff records changed resources and unknown scopes; historical completeness is positively established within declared failure model. If trusted history cannot be reconstructed, block conflicting effects.

## 5. Runtime admission

Process running ≠ component admitted for all operations. Recovery can allow read-only or isolated operations before shared-world mutation when legal proofs cover those scopes. Recovery admission is not a permanent authorization; CommitGate/ActionGate revalidate current requirements.

## 6. Schema and restored data

Older writers must be physically fenced after incompatible schema cutover; restore into restricted staging and assess hooks, credentials, watched directories and possible auto-execution. Old sensitive data must be restricted before LLM, indexing or export processing.

## 7. Durable continuation

Persist required suspension/Trigger/Action obligations before claiming resumability. If reliable persistence is unavailable, do not claim automated recovery. Repeated crashes must not silently discard unresolved obligations.

## 8. Recovery failure model

Guarantees are bounded by declared storage durability, trusted witness availability, external provider observability and enforceable resource reachability. No universal exactly-once, no guarantee of reconstructing permanently lost evidence.

## 9. Acceptance targets

Disaster rollback; cross-frontier revocation race; in-flight external effects; restore-time hooks; pre-materialization erasure leaks; schema stale writer; trigger cursor gaps; multi-crash suspension continuity. These are **specification scenarios**, not recorded execution tests.


## 10. Dependency and interface register

- Restores L1 authoritative control, coordinates L3 action reconciliation, L4 trigger/specialist continuation, L5 suppression, and L2 Executive readmission.
- Sends scoped activation conditions to L7; cannot authorize otherwise-illegal mutations.

## 11. Pending effective-contract verification

- **PENDING EFFECTIVE CONTRACT AUDIT:** RDMS-09 Draft+C01+C02+C03 final consolidated copy and exact invariants RDMS09-I01…113.
- Frozen source text is only represented by reviewed conversation records here; do not claim exact field-level conformance.

## 12. Layer conformance requirements

A layer cannot be marked `FROZEN_CONSOLIDATED` until: (a) the owning legal contracts are imported from their frozen source version without loss; (b) all cross-layer projections are typed and referenced; (c) invariants, authority, failure and recovery paths are covered by normative acceptance scenarios; (d) source hashes and changes are recorded in `ARCHITECTURE_MANIFEST.md`; (e) the layer's review explicitly approves the consolidated text.

---

# SOURCE-PRESERVED FCA v1.0.1 BASELINE ANNEX

**Source authority:** the immutable `Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md` file in `reviews/source_archive/`. These copied sections are exact FCA source excerpts, not newly approved RDMS definitions. Layer prose above remains a consolidation draft pending full RDMS source validation.
**Source SHA-256:** `74d0923cbd343b71740da0fc2368a84aad2ea97f8e4e15f156122f48ebe53539`

**Ownership note:** This document embeds its assigned FCA source sections once. Do not redefine these names in a second layer; refer to the original owner or validated public projection.

<!-- GAIA-SOURCE FCA-SECTION 52 SHA256=01de44b2a6d0e07eca98ba9a93552ad5ebe8815927e36964681243e3363d4ba1 -->
## 52. Startup recovery

A complete process restart restores cognition from durable state, not chat history.

Recovery sequence:

```text
1. Restore canonical snapshot.
2. Replay Control Ledger.
3. Obtain a valid Executive epoch.
4. Inspect unresolved ActionRecords.
5. Reconcile possibly dispatched effects.
6. Replay/evaluate durable triggers.
7. Inspect Specialist workspaces.
8. Validate dependency freshness.
9. Restore active/suspended/blocked work.
10. Resume normal Executive control.
```

---

# Part XV — Temporal cognition

<!-- GAIA-SOURCE FCA-SECTION 80 SHA256=5fe808a7385e72c1ef7ccdbde5ddb08868115be5e52a71c0b796456c4e507ddd -->
## 80. Cognitive continuity

The unit of continuity is not the conversation.

> **The unit of continuity is persistent cognitive state.**

The system maintains a current “Cognitive HEAD” and retrieves history on demand.

Chat history is not authoritative state.

---

<!-- GAIA-SOURCE FCA-SECTION 82 SHA256=92b9097710856ff2fb540eac313422afc0852e6f5588e47d62d498b15d0eacf2 -->
## 82. Safe suspension

Where possible, the system SHOULD suspend at a coherent boundary where:

- repository/world state is understood;
- temporary state is recorded;
- current reasoning is summarized;
- next action is explicit;
- no unresolved effect is silently abandoned.

---


---

## RDMS Verbatim Source Annexes — Phase 4 (historical draft + corrections + freeze decision)

> **SOURCE PRESERVATION, NOT NORMALIZED LAW.** The following original user-supplied text is included **verbatim** as a migration input. Drafts and later corrections coexist historically. Later approved corrective parts and freeze decisions must govern disagreements. This annex does not itself certify exact schema compatibility or replace the original archive. Do not implement directly until semantic reconciliation is completed.

### Original source set: RDMS-09

Archive: `../reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-09_APPROVED_SOURCE_SET.txt`  
SHA-256 of complete source set: `84ed1246a86b6f5923b6bf3320c2830e10c8e3fddac14e778c8c503272062a4b`  
Contained original message parts: 5

````text
RDMS-09 — ORIGINAL APPROVED SOURCE SET
Source: https://chatgpt.com/share/6ac82d7b-ba7c-83ea-a3a9-b41734948bb2

ملاحظة تحريرية: هذا الملف تجميع للنصوص الأصلية المسترجعة من المحادثة، لا إعادة صياغة ولا مواصفة موحدة جديدة. حالة التجميد مثبتة في قرار المراجعة النهائي المرفق؛ عبارة DRAFT داخل النص الأساسي تصف مرحلته التاريخية قبل التصحيحات. تُقرأ المسودة مع التصحيحات وقرار الاعتماد، ولا يجوز استعمال نص سابق يخالف تصحيحًا معتمدًا لاحقًا. لم نغير نصوص القوانين ولم نضف FCA.


========================================================================
SOURCE PART: Original draft
MESSAGE ID: 6ee1a6d1-3dfe-4de8-8c44-54ac4b07f8d4
BEGIN ORIGINAL MESSAGE
========================================================================

نبدأ الآن RDMS-09 — System Recovery, Resilience, Operational Safety & Lifecycle Governance.

وصلنا إلى مرحلة تختلف عن المراحل السابقة في طبيعتها. لقد صممنا عقلًا تنفيذيًا يستطيع التفكير والتخطيط واتخاذ القرارات، لكننا نحتاج الآن إلى ضمان ألا يفقد النظام تماسكه عندما يتعرض لعطل أو انقطاع أو انهيار أثناء تنفيذ مهمة حقيقية.

هناك سؤال أريد أن يكون محور RDMS-09:

كيف نضمن أن الوكيل يستطيع استعادة حالة موثوقة بعد أي عطل مدعوم، دون اختراع تاريخ لم يحدث، أو فقدان أثر خارجي، أو تكرار عملية خطيرة، أو استئناف قرار فقد صلاحيته؟

راجعت قواعد التعافي المجمدة في FCA، خصوصًا Control Ledger وExecutive Epoch وAction Journal وIN_DOUBT وResumption Capsules.

وسنحافظ على نقطة أساسية: RDMS-09 لن تنشئ محرك تعافٍ ثانيًا ينافس المكونات السابقة، بل ستحدد كيفية تنسيق تعافي النظام بأكمله والتحقق من سلامة عودته إلى العمل.

RDMS-09 — System Recovery, Resilience, Operational Safety & Lifecycle Governance — Draft v1.0
RDMS-09
System Recovery, Resilience, Operational Safety & Lifecycle Governance

Runtime & Data Model Specification — Draft v1.0

Parent: FCA v1.0.1 — FROZEN
Dependencies: RDMS-01 → RDMS-08 — FROZEN
Status: DRAFT v1.0 — NOT FROZEN
Implementation: NOT AUTHORIZED
Next Gate: Adversarial Freeze Review 01

PART I — PURPOSE
1. Objective

RDMS-09 تحدد سياسة تعافي النظام واستمرارية تشغيله عندما تتعرض مكوناته لأعطال أو فقدان اتصال أو توقف غير متوقع.

يجب أن يستطيع النظام التعامل مع:

انهيار عملية Cognitive Executive.

فقدان الاتصال بنموذج اللغة.

انهيار الجهاز أو نظام التشغيل.

توقف تنفيذ أداة أثناء عملية خارجية.

فقدان الاتصال بمستودع Git.

تعطل Specialist أثناء عملها.

تلف Snapshot أو عدم اكتمالها.

إعادة تشغيل تؤدي إلى تكرار أحداث.

تغير المشروع أثناء توقف الوكيل.

فقدان أو انتهاء صلاحيات التنفيذ.

تعطل التخزين أو فقدان بعض البيانات.

تعارض الذاكرة مع الأدلة المستعادة.

فشل التحديثات والمهاجرات البرمجية.

عمليات الإلغاء والتوقف الآمن.

طلبات الاحتفاظ بالبيانات وإزالتها.

استعادة النظام بعد حادث أمني.

لا يعني ذلك أن النظام يستطيع إصلاح جميع الأعطال تلقائيًا.

بعض الحالات يجب أن تنتهي بحالة محجوبة واضحة، تتطلب إصلاحًا بشريًا أو استعادة نسخة احتياطية أو إعادة اعتماد قانونية.

2. Fundamental Principle

نعتمد المبدأ التالي:

Recovery must restore justified authority and known state, not manufacture continuity.

أي:

يجب أن يستعيد النظام السلطة القانونية والحالة المثبتة، لا أن يخترع استمرارية اعتمادًا على التخمين.

مثال:

Action:
    Deploy new version.

Process:
    Crashed after dispatch.

Recovery:
    External deployment status UNKNOWN.

لا يجوز تفسير ذلك باعتباره نجاحًا.

ولا يجوز تفسيره باعتباره فشلًا يسمح بإعادة النشر مباشرة.

يجب أن يظل احتمال الأثر الخارجي قائمًا حتى تجري التسوية المناسبة.

PART II — ARCHITECTURAL POSITION
3. Recovery Architecture
                 SYSTEM FAILURE
                       │
                       ▼
               Failure Detection
                       │
                       ▼
             Operational Containment
                       │
                       ▼
               Recovery Assessment
                       │
                       ▼
             Canonical State Restore
                       │
                       ▼
              Executive Epoch/Fencing
                       │
                       ▼
              Cross-RDMS Reconciliation
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Actions        Triggers       Specialists
        │              │              │
        └──────────────┼──────────────┘
                       ▼
             Dependency Revalidation
                       │
                       ▼
             Executive Reassessment
                       │
                       ▼
                Recovery Decision
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       RESUME        BLOCK       SUSPEND

هذا مخطط تنسيق منطقي.

لا يستبدل Recovery Sequence المجمدة في FCA.

ترتيب العمليات الفعلي يجب أن يحافظ على القيود المجمدة، مع السماح بإعادة المحاولات والتقييمات الموثوقة اللازمة للتعافي.

4. Recovery Ownership
Component	Recovery responsibility
RDMS-01	Control Ledger، snapshots، CAS، epochs
RDMS-02	Goals، Slices، Decisions
RDMS-03	Observations وEvidence integrity
RDMS-04	Action reconciliation وworld effects
RDMS-05	Triggers وResumption
RDMS-06	Specialists وDependency Evaluation
RDMS-07	Memory وLearning integrity
RDMS-08	Executive reassessment
RDMS-09	System-wide recovery orchestration and operational governance
5. No Second Executive

نظام التعافي لا يملك سلطة معرفية مستقلة.

يمكنه تنفيذ عمليات سلامة محددة مسبقًا، مثل منع dispatch جديدة أو عزل مورد وفق سياسة موثوقة.

لكن قبول خطة جديدة أو تعديل قرار معرفي معتمد يبقى من صلاحيات Executive الحالية والبوابات القانونية.

PART III — FAILURE CLASSIFICATION
6. Failure Domains

نقترح التصنيف التالي:

FailureDomain {
    CONTROL_PLANE
    COGNITIVE_RUNTIME
    REASONING_PROVIDER
    ACTION_RUNTIME
    OBSERVATION_PIPELINE
    TEMPORAL_RUNTIME
    SPECIALIST_RUNTIME
    MEMORY_RUNTIME
    DEPENDENCY_ENGINE
    STORAGE
    NETWORK
    SECURITY_BOUNDARY
    ENVIRONMENT
}

هذا التصنيف يحدد أين حدث العطل.

ولا يعني أن العطل محصور بالضرورة في ذلك المكون.

7. FailureRecord
FailureRecord {
    failure_id

    project_id

    detected_at
    detecting_component_ref

    failure_domain

    affected_resource_refs[]

    affected_goal_refs[]

    affected_operation_refs[]

    last_known_control_ref

    relevant_action_refs[]

    observed_symptoms[]

    supporting_observation_refs[]

    confidence_limitations[]

    containment_status

    recovery_case_ref?
}

يجب فصل:

العطل المرصود.

سببه المفترض.

الأثر المحتمل.

الإجراءات التي نُفذت استجابة له.

لا يُسمح بتسجيل فرضية السبب الجذري باعتبارها Observation مثبتة.

8. Failure Severity

نستخدم تقييمًا يعتمد على:

Safety risk
Authority compromise
Potential external effects
Data integrity risk
Recovery uncertainty
Affected scope
Availability impact

الأولوية لا تعتمد فقط على توقف المكون.

فمثلًا، انهيار LLM أثناء كتابة تفسير نصي قد يكون أقل خطورة من انقطاع اتصال أثناء إجراء دفع مالي.

PART IV — SYSTEM OPERATIONAL MODES
9. OperationalRecoveryMode

نقترح أوضاع تشغيلية على مستوى إدارة النظام:

NORMAL
DEGRADED
RECOVERY_REQUIRED
RECOVERING
QUARANTINED
SAFE_SUSPENDED

هذه ليست حالات جديدة ضمن Cognitive Executive State Machine الموجودة في FCA.

إنها أوضاع تشغيلية تحدد الأنشطة التي تستطيع البيئة السماح بها.

10. Mode Semantics

NORMAL

الشروط التشغيلية المطلوبة مستوفاة.

DEGRADED

تعطل مكون غير حرج، لكن توجد عمليات يمكن الاستمرار فيها ضمن حدود موثوقة.

RECOVERY_REQUIRED

يوجد خلل يمنع الاستمرار الطبيعي.

RECOVERING

تجري إجراءات استعادة وتحقيق.

QUARANTINED

يوجد خطر على سلامة البيانات أو السلطة أو حدود الثقة يستوجب العزل.

SAFE_SUSPENDED

أوقف النظام الأعمال الجديدة بصورة محكومة، مع الحفاظ على الحالة والالتزامات غير المحسومة.

11. Mode Transition
OperationalModeTransition {
    transition_id

    from_mode
    to_mode

    trigger_ref

    required_conditions[]

    safety_obligations[]

    controlling_policy_ref

    durable_control_ref
}

لا يجوز لرسالة ناتجة عن LLM أن تحول النظام مباشرة إلى NORMAL.

يجب إثبات شروط الخروج من الوضع المقيد.

PART V — RECOVERY CASE
12. RecoveryCase

كل حادث يتطلب تعافيًا منسقًا يمكن تمثيله بـ:

RecoveryCase {
    recovery_case_id

    project_id

    initiating_failure_refs[]

    affected_domains[]

    recovery_scope

    originating_control_frontier

    current_executive_epoch?

    unresolved_action_refs[]

    unresolved_trigger_refs[]

    unresolved_specialist_refs[]

    data_integrity_assessment_ref?

    required_reconciliation_refs[]

    recovery_policy_version

    current_disposition

    audit_refs[]
}
13. Recovery Identity

يجب أن تمتلك محاولة التعافي هوية مستقرة عبر إعادة التشغيل.

لا نريد:

Crash
  ↓
Recovery Case A created
  ↓
Crash
  ↓
Recovery Case B created
  ↓
Both attempt the same reconciliation

يجب استخدام هويات وأرقام أجيال مرتبطة بالحادث ومجال التعافي وControl Ledger.

قد توجد محاولات متعددة داخل RecoveryCase واحدة.

لكنها لا تصبح عمليات مستقلة ذات سلطة متناقضة.

14. Recovery Authority

لا تمنح RecoveryCase وحدها صلاحية تعديل Canonical Workspace أو العالم الخارجي.

يجب أن تستخدم العمليات المناسبة:

CommitGate
ActionGate
Observation Ingress
Executive Epoch

وفق المسؤولية الفعلية لكل انتقال.

PART VI — STARTUP RECOVERY
15. Canonical Recovery Sequence

نحافظ على التسلسل المجمد في FCA:

1. Restore canonical snapshot.
2. Replay Control Ledger.
3. Obtain valid Executive epoch.
4. Inspect unresolved ActionRecords.
5. Reconcile possibly dispatched effects.
6. Replay/evaluate durable triggers.
7. Inspect Specialist workspaces.
8. Validate dependency freshness.
9. Restore active/suspended/blocked work.
10. Resume normal Executive control.

RDMS-09 تحدد كيف نتحقق من سلامة هذه المراحل، ولا تستبدلها بمسار جديد.

16. StartupRecoveryAssessment
StartupRecoveryAssessment {
    startup_id

    canonical_snapshot_ref

    ledger_replay_ref

    executive_epoch_ref

    action_reconciliation_ref

    trigger_recovery_ref

    specialist_recovery_ref

    dependency_validation_ref

    goal_restoration_ref

    unresolved_blockers[]

    readiness_for_normal_control
}
17. Startup Admission

لا يُسمح بالعودة إلى التشغيل الطبيعي إذا كان النظام غير قادر على إثبات حالة التحكم الأساسية التي يعتمد عليها.

مثال:

Ledger unavailable
+
No verified replacement authority
=
NO NORMAL OPERATION

يمكن السماح بعمليات تحقيق أو حماية محدودة وفق سياسة موثوقة، لكنها لا تمنح السلطة لتنفيذ أعمال إنتاجية جديدة.

PART VII — DURABLE CONTROL STATE
18. Control State Integrity

المصدر القانوني لحالة التحكم هو RDMS-01.

يشمل:

Canonical state versions
Executive epochs
Control commits
Action lifecycle references
Trigger lifecycle references
Specialist lifecycle references
Goal transitions
Memory promotions

لا تعتمد استعادة هذه المعلومات على تاريخ المحادثة مع LLM.

19. Snapshot Validation
SnapshotValidation {
    snapshot_ref

    schema_version

    source_control_frontier

    content_integrity

    completeness_status

    referenced_artifact_validity

    compatibility_status

    result
}

لا يجوز استعادة Snapshot متضررة باعتبارها حالة سليمة لمجرد أن الملف قابل للقراءة.

20. Ledger Replay Integrity

قبل قبول Replay يجب التحقق من:

Event identity
Event ordering
Schema compatibility
Required event continuity
Control transition validity
Referenced artifact availability

يجب أن تنتج replay نتيجة حتمية ضمن العقد المجمد.

21. Incomplete Control History

إذا كانت هناك فجوة لا يمكن تبريرها في التاريخ القانوني:

Snapshot S100
+
Missing required events
+
Later events S120

فلا يجوز بناء حالة حالية اعتمادًا على التخمين.

تدخل الحالة مسار استعادة موثوقة أو عزل أو تدخل بشري حسب السياسة.

PART VIII — BACKUP AND DISASTER RECOVERY
22. Backup Architecture

النسخ الاحتياطي ليس مجرد نسخ ملفات Repository.

قد يحتاج النظام إلى:

Canonical state snapshots
Control Ledger
Recovery-critical metadata
Action Journal references
Artifact manifests
Memory metadata
Schema versions
Security-policy references

تحدد سياسة النسخ الاحتياطي أي مكونات يجب أن تستعاد معًا بطريقة متسقة.

23. BackupManifest
BackupManifest {
    backup_id

    source_project_id

    source_control_frontier

    snapshot_refs[]

    ledger_segment_refs[]

    artifact_manifest_refs[]

    schema_version_refs[]

    encryption_policy_ref?

    integrity_proofs[]

    consistency_scope

    creation_time

    retention_class
}
24. Backup Consistency

إذا كان:

Canonical State = S500
Action Journal = S480

فلا يجوز اعتبار النسختين صورة موحدة سليمة دون التحقق من العلاقة بينهما وإمكان إعادة بناء التاريخ المفقود.

النسخة الاحتياطية يجب أن تحمل Consistency Frontier واضحة.

25. Disaster Restore

قد تعيد النسخة الاحتياطية حالة قديمة نسبيًا.

لكن العالم الخارجي ربما استمر في التغير بعد نقطة النسخ.

لذلك:

Restored Control State
        ≠
Current World State

لا يسمح بإعادة تنفيذ عمليات قديمة تلقائيًا بسبب استعادة Snapshot سابقة.

يجب إجراء reconciliation باستخدام الأدلة المتاحة.

26. Recovery Objectives

يمكن تعريف:

RPO — Recovery Point Objective
RTO — Recovery Time Objective

بوصفهما أهدافًا تشغيلية قابلة للقياس.

لكن لا نعد بتحقيق زمن تعافٍ معين أو عدم فقدان أي بيانات دون إثبات أن البنية التحتية تستطيع الوفاء بذلك.

PART IX — ACTION RECONCILIATION
27. Action Recovery Boundary

تظل RDMS-04 صاحبة السلطة على حالات ActionRecord:

PROPOSED
AUTHORIZED
DISPATCH_INTENT
RESULT_REPORTED
EFFECT_VERIFIED
PARTIAL
FAILED
IN_DOUBT
RECONCILING
RECONCILED

لا تضيف RDMS-09 حالات جديدة إلى هذه القائمة.

28. Reconciliation Priority

عند التعافي يجب إعطاء الأولوية إلى:

Potentially dispatched shared-world mutations
Unresolved irreversible effects
Potential security effects
Required compensations
Dependent blocked operations

لكن الأولوية لا تعني افتراض حدوث الأثر أو عدم حدوثه.

29. ActionRecoveryAssessment
ActionRecoveryAssessment {
    action_ref

    pre_failure_lifecycle

    effect_identity_ref?

    retry_policy

    outcome_probe_ref?

    observed_world_status

    reconciliation_evidence_refs[]

    dependent_operation_refs[]

    permitted_recovery_options[]

    unresolved_uncertainty[]
}
30. No Blind Retry

إذا كانت Action غير قابلة لضمان التكرار الآمن:

Dispatch may have occurred.
Outcome unknown.

لا يجوز إعادة إرسالها لمجرد أن النظام أعاد التشغيل.

IN_DOUBT لا تعني FAILED.

31. Partial World Effects

قد يكون تنفيذ عملية خارجية جزئيًا.

مثال:

Database migration:
    Table A updated.
    Table B update failed.

لا يمكن اعتبار النظام في الحالة السابقة أو الجديدة تلقائيًا.

يجب تحديد الأثر الفعلي والاعتماديات المتأثرة.

أي تعويض أو استكمال يخضع إلى التفويض القانوني المناسب.

32. Reconciliation Failure

إذا تعذر التحقق من الأثر الخارجي:

IN_DOUBT
    ↓
Reconciliation attempted
    ↓
Evidence insufficient

يجب الحفاظ على عدم اليقين.

يمكن تعليق العمل التابع للعملية، مع استمرار آلية إعادة التفعيل أو التصعيد المناسبة.

PART X — EXECUTIVE EPOCH AND FAILOVER
33. Leadership Recovery

يستخدم النظام Executive Epoch من RDMS-01.

Executive N
    ↓
Failure
    ↓
Epoch N+1 acquired
    ↓
Old authority fenced
    ↓
New Executive reconciles state
34. Split-Brain Protection

قد تعمل عمليتا Executive في الوقت نفسه بسبب انقطاع شبكة أو فشل تنسيق القيادة.

يجب ألا تمتلك الاثنتان السلطة القانونية نفسها.

Executive A:
    epoch 15

Executive B:
    epoch 16

فقط epoch الحالية المعتمدة تستطيع إصدار انتقالات جديدة.

ولا يكفي الاعتماد على معرفة العملية بأنها القائدة؛ يجب فرض fencing عند حدود العمليات الحاملة للسلطة.

35. Leadership Uncertainty

إذا لم يمكن إثبات السلطة الحالية، لا يجوز للنظام متابعة أعمال معرفية تتطلب اعتمادًا قانونيًا جديدًا.

يمكن الاحتفاظ بتحليلات مؤقتة لا تحمل تأثيرًا قانونيًا عندما تسمح السياسة بذلك.

لكن لا يجوز تحويلها إلى Canonical Commit أو Action جديدة دون تفويض صالح.

36. Late Results

قد تصل نتائج:

LLM calls
Tool calls
Specialist results
Human responses

بعد انتقال القيادة.

هذه النتائج لا تحمل سلطة اعتماد جديدة.

يجب فحص provenance والاعتماديات ثم إقرار استعمالها من Executive الحالية عند الحاجة.

PART XI — PROVIDER FAILURE AND RESILIENCE
37. Reasoning Provider Failure

قد يتعطل نموذج اللغة بسبب:

Timeout
Connection failure
Rate limiting
Provider outage
Invalid response
Context incompatibility

يجب فصل فشل الاتصال عن فشل الاستدلال أو عدم اكتمال المهمة.

38. ProviderRecoveryPolicy
ProviderRecoveryPolicy {
    provider_ref

    failure_class

    retry_eligibility

    bounded_retry_policy

    fallback_provider_candidates[]

    context_compatibility_requirements

    budget_limit

    resumption_constraints
}
39. Provider Substitution

يمكن استخدام Provider أخرى إذا كانت متاحة ومصرحًا بها.

لكن:

Provider replacement
    ≠
Executive authority replacement

يجب الحفاظ على:

Canonical memory
Project identity
Decision history
Action state
Executive epoch
40. Late Provider Responses

إذا انتهى Timeout ثم وصلت استجابة قديمة، لا يجوز التعامل معها باعتبارها نتيجة أحدث محاولة بصورة تلقائية.

يجب ربط كل استجابة بـInvocation Identity وسياقها.

41. Provider Recovery Limit

إذا تعذرت جميع البدائل، يمكن تعليق العمل المعرفي.

لكن لا يجوز استخدام تعطل LLM ذريعة للتخلي عن التزامات السلامة التي تستطيع المكونات الموثوقة تنفيذها أو توثيقها دون استدلال جديد.

PART XII — TOOL AND PROCESS RECOVERY
42. Tool Execution Failures

تختلف الأخطاء بين:

Process failed before invocation
Process terminated during execution
Process returned error
Process timed out
Process lost connection
Process completed but result persistence failed

هذه الحالات ليست متكافئة.

43. ProcessRecoveryRecord
ProcessRecoveryRecord {
    process_ref

    originating_action_ref?

    execution_boundary_ref

    last_known_process_state

    ownership_ref

    possible_external_effects[]

    containment_status

    termination_evidence_ref?

    recovery_constraints[]
}
44. Process Termination

انتهاء مهلة انتظار عملية لا يثبت توقفها.

وقد يستمر subprocess في الخلفية بعد انتهاء الجلسة الأصلية.

يجب أن يعرف النظام حدود قدرته على:

Observe
Contain
Terminate
Reconcile

إذا كان التوقف غير مؤكد، فلا يجوز تنفيذ عمليات تتطلب افتراض توقف العملية السابقة.

45. Orphan Processes

يجب تحديد مسؤولية العمليات التي بقيت بعد انهيار Worker.

يمكن محاولة اكتشافها عبر Process Identity ومعلومات البيئة.

لكن لا نعتمد على PID وحده عندما تكون إعادة استخدام المعرفات ممكنة.

PART XIII — SPECIALIST RECOVERY
46. Specialist Continuity

تخضع Specialists إلى RDMS-06.

قد يحدث:

Specialist working
    ↓
Worker crashes
    ↓
Workspace survives
    ↓
Executive restarts

لا يعني هذا أن Specialist انتهت أو أن نتيجتها صالحة تلقائيًا.

47. SpecialistRecoveryAssessment
SpecialistRecoveryAssessment {
    specialist_run_ref

    contract_ref

    originating_executive_epoch

    workspace_ref

    last_durable_progress_ref

    pending_tool_actions[]

    contract_validity

    resource_budget_status

    dependency_evaluation_ref

    recovery_recommendation
}
48. Resume or Replace

يمكن لـExecutive الحالية:

Resume authorized work
Recruit replacement
Integrate verified partial result
Reject result
Suspend task

وفق شروط RDMS-06.

لا يجوز أن يؤدي Crash إلى إنشاء Specialist جديدة تلقائيًا دون RecruitmentIdentity قانونية.

49. Specialist Result Integrity

يجب ألا تتحول ملفات مؤقتة أو Logs غير موثوقة إلى Results معتمدة بمجرد العثور عليها بعد التعافي.

تظل provenance والأدلة والاعتماديات ضرورية.

PART XIV — TEMPORAL RECOVERY
50. Trigger Recovery

RDMS-05 مسؤولة عن:

Durable triggers
Source cursors
Trigger generations
Reaction identities
Temporal commitments

تعالج RDMS-09 اعتماد هذه الحالة عند استعادة النظام.

51. Trigger Replay

قد يحدث Trigger أثناء توقف النظام ثم يُكتشف بعد إعادة التشغيل.

وقد يُسلَّم الحدث نفسه أكثر من مرة.

يجب أن تكون Reaction المعتمدة idempotent وفق RDMS-05.

52. Edge Trigger Limitation

إذا كان Trigger يعتمد على حدث لحظي وقع أثناء توقف النظام، ولم يكن المصدر يحتفظ بتاريخ قابل لإعادة التشغيل، فلا يجوز اختراع دليل أن الحدث حدث.

يظل عدم إمكان الإثبات واضحًا.

53. Temporal Recovery and Clock Changes

قد يتغير الوقت بسبب:

DST
Timezone changes
Clock corrections
Machine restart

يجب استخدام semantics الزمنية المجمدة في RDMS-05.

ولا تُستخدم ساعة النظام المحلية وحدها لإثبات ترتيب الأحداث المعتمدة عندما لا يكون ذلك مضمونًا.

PART XV — DEPENDENCY RECOVERY
54. Dependency Evaluation After Restart

عند عودة النظام، قد تكون:

Repository changed
Environment changed
Tool version changed
Memory revised
External contract changed

لذلك لا يجوز استئناف أي نتيجة معرفية متأثرة دون تقييم مناسب لصلاحية اعتمادياتها.

55. DependencyRecoveryAssessment
DependencyRecoveryAssessment {
    recovery_case_ref

    affected_result_refs[]

    current_repository_ref

    current_environment_ref

    changed_dependency_frontiers[]

    dependency_evaluation_refs[]

    invalidated_result_refs[]

    unknown_validity_refs[]
}
56. No Global Invalidation By Default

لا ينبغي أن يؤدي Restart وحده إلى إبطال جميع نتائج المشروع.

يجب استخدام RDMS-06 لتحديد التأثير الفعلي.

إذا لم يمكن إثبات نطاق ضيق آمن، تستخدم آلية التقييم fallback محافظة.

57. Derived State Recovery

يجب إعادة تقييم:

Plans
Slices
Specialist results
Negative knowledge
Memory applicability
Readiness assessments
Finalization candidates

إذا تغيرت اعتمادياتها المؤثرة.

PART XVI — MEMORY RECOVERY
58. Memory Integrity

تظل RDMS-07 مسؤولة عن الحوكمة المعرفية للذاكرة.

أما RDMS-09 فتحدد ضمانات استعادتها من التخزين والمراجع المعتمدة.

59. MemoryRecoveryAssessment
MemoryRecoveryAssessment {
    canonical_memory_frontier

    recovered_memory_refs[]

    missing_memory_artifact_refs[]

    schema_compatibility

    index_consistency

    unresolved_derivation_refs[]

    access_policy_status

    recovery_limitations[]
}
60. Derived Index Rebuild

يمكن إعادة بناء:

Search indexes
Semantic retrieval indexes
Cached retrieval structures

من مصادر معتمدة متاحة.

لكن الفهرس المشتق لا يصبح مصدر الحقيقة عندما تختلف نتائجه عن Canonical Memory.

61. Memory Promotion Recovery

إذا وقع Crash أثناء MemoryPromotion:

Proposal approved
    ↓
Commit pending
    ↓
Crash

يجب استخدام هوية الترقية وControl Ledger لتحديد هل تم الاعتماد بالفعل.

ولا يجوز تكرار الترقية بلا تحقق.

PART XVII — SECURITY INCIDENT RECOVERY
62. Security Incident

قد يحدث:

Credential compromise
Unauthorized filesystem mutation
Malicious tool output
Prompt injection escalation
Unexpected network access
Tampered artifact
Compromised specialist workspace

هذه أحداث مختلفة عن الفشل التشغيلي العادي.

63. SecurityRecoveryAssessment
SecurityRecoveryAssessment {
    incident_ref

    affected_security_domains[]

    suspected_compromise_scope

    verified_compromise_evidence_refs[]

    affected_credentials[]

    affected_artifacts[]

    containment_actions[]

    required_integrity_checks[]

    recovery_constraints
}
64. Quarantine

إذا لم يعد مصدر معين موثوقًا:

Potentially compromised source
        ↓
QUARANTINED
        ↓
Restricted use
        ↓
Integrity investigation

لا يجوز استخدام محتوى المصدر نفسه كدليل وحيد على أنه لم يتعرض للتلاعب.

65. Credential Rotation

قد يؤدي تعافي حادث أمني إلى تغيير Credentials.

لكن تغيير Credential لا يثبت أن العمليات التي بدأت باستخدامها قد توقفت.

يجب فحص الجلسات والآثار الخارجية الممكنة وفق قدرة الأنظمة المعنية.

66. Recovery From Compromise

لا يجوز إعادة النظام إلى NORMAL اعتمادًا على:

Service restarted successfully.

إذا بقيت مخاطر تتعلق بسلامة التحكم أو البيانات أو التفويض دون معالجة.

PART XVIII — LIFECYCLE GOVERNANCE
67. System Lifecycle

نميز بين:

Initialization
Normal operation
Degraded operation
Recovery
Maintenance
Upgrade
Suspension
Shutdown
Retirement

هذه مراحل تشغيلية، وليست حالات معرفية جديدة.

68. Graceful Shutdown

عند طلب توقف منظم:

Stop new discretionary dispatch
        ↓
Preserve durable control state
        ↓
Inspect active operations
        ↓
Handle cancellable work
        ↓
Reconcile possible world effects
        ↓
Persist unresolved obligations
        ↓
Shutdown safely
69. Forced Shutdown

قد لا تتوفر فرصة للتوقف المنظم.

لذلك يجب ألا يعتمد النظام على تنفيذ Cleanup اختياري عند نهاية العملية كي يصبح التاريخ القانوني صحيحًا.

كل عملية ذات أثر مشترك تخضع لضمانات Write-Ahead المناسبة قبل حدوث الأثر.

70. Maintenance Mode

أثناء تحديث النظام أو إصلاحه، قد نحتاج منع عمليات جديدة.

لكن بعض عمليات التحقيق والتسوية يجب أن تبقى متاحة وفق سياسة محكومة.

لا يصبح Maintenance Mode استثناءً يسمح بتجاوز Hard Invariants.

PART XIX — UPGRADE AND SCHEMA MIGRATION
71. Runtime Upgrade

قد نحدث:

Cognitive Controller
Tool Adapters
Memory Schema
Control Projections
Dependency Indexes
Provider Integration

يجب ألا يؤدي تحديث مكون إلى إعادة تفسير حالة قديمة بصورة غير قانونية.

72. UpgradePlan
UpgradePlan {
    upgrade_id

    source_version

    target_version

    affected_components[]

    migration_steps[]

    compatibility_requirements[]

    rollback_or_recovery_strategy

    expected_downtime

    required_verification[]

    authority_refs[]
}
73. Schema Migration

يجب التمييز بين:

Canonical schema migration

و:

Derived index rebuild

الأولى تؤثر في تفسير الحالة المعتمدة.

الثانية تعيد بناء بنية مشتقة.

لا نسمح بتحويل دلالي صامت داخل Canonical State بحجة إعادة بناء Index.

74. Upgrade Failure

إذا فشلت Migration بعد تنفيذ جزء منها، يجب تحديد الحالة الفعلية.

لا يمكن افتراض نجاح Rollback دائمًا.

وقد تحتاج RecoveryCase إلى reconciliation لحالة التخزين والواجهات والعمليات التي بدأت أثناء التحديث.

PART XX — RETENTION, PRIVACY AND ERASURE

هذا القسم يكمل التزامات RDMS-07 المتعلقة بحذف البيانات والاحتفاظ بها.

75. Three Distinct Operations

نميز بين:

Epistemic Retirement

منع استخدام معرفة قديمة باعتبارها معرفة حالية.

Access Suppression

منع استرجاع أو إفصاح بيانات مشمولة بقيد قانوني أو تشغيلي.

Physical Erasure

إزالة المحتوى من وسائط التخزين الواقعة ضمن نطاق السيطرة المحدد.

لا يجوز الخلط بينها.

76. DataLifecyclePolicy
DataLifecyclePolicy {
    policy_id

    data_class

    retention_scope

    permitted_storage_domains[]

    permitted_processing_domains[]

    expiry_or_erasure_conditions[]

    legal_hold_conditions[]

    derived_data_rules[]

    audit_requirements[]

    authorized_policy_version
}
77. ArtifactLineageManifest
ArtifactLineageManifest {
    source_artifact_ref

    derived_artifact_refs[]

    index_entry_refs[]

    cache_refs[]

    backup_presence_refs[]

    external_copy_refs[]

    known_replication_scope

    coverage_status
}

هذه البنية مهمة عندما تحتاج عملية حذف إلى تحديد النسخ والمشتقات.

78. ErasureOperation
ErasureOperation {
    erasure_operation_id

    authorized_request_ref

    affected_data_scope

    immediate_access_suppression_ref

    storage_target_refs[]

    index_invalidation_refs[]

    derived_artifact_refs[]

    backup_policy_actions[]

    verification_refs[]

    residual_copy_disclosures[]

    completion_scope
}
79. Erasure Ordering

عندما يكون طلب الإزالة صالحًا ويستلزم منع استعمال المحتوى:

Authorized Erasure Request
        ↓
Durable Access Suppression
        ↓
Identify Controlled Copies
        ↓
Execute Authorized Erasure
        ↓
Verify Within Declared Scope
        ↓
Record Residual Limitations

لا نعتمد على تحديث Search Index فقط لفرض المنع.

يجب تطبيق الحظر عند حدود الاسترجاع والإفصاح المناسبة.

80. Append-Only Ledger Compatibility

إذا كانت هناك بيانات حساسة داخل سجل غير قابل للتعديل، فإن تغيير حالة Memory إلى RETIRED لا يزيلها فعليًا.

ينبغي أن تفصل البنية بين:

Immutable control metadata

و:

Governed removable content

مع الحفاظ على مراجع تدقيق مناسبة لا تكشف المحتوى المحذوف عندما تسمح السياسة بذلك.

لا نفترض إمكانية حذف بيانات دخلت بالفعل إلى نسخ خارج نطاق السيطرة.

81. Backup Erasure

قد تحتوي النسخ الاحتياطية على بيانات خاضعة لطلب حذف.

تحتاج السياسة إلى تحديد كيفية التعامل معها، بما في ذلك:

Retention expiration
Backup replacement
Cryptographic erasure where appropriate
Restore-time suppression

ولا يجوز أن تؤدي استعادة Backup قديمة إلى إعادة تنشيط بيانات كانت مشمولة بقيد حذف نافذ.

82. Erasure Verification

النتيجة القانونية يجب أن تكون محددة النطاق:

VERIFIED_WITHIN_DECLARED_SCOPE
INCOMPLETE
UNKNOWN

ولا يجوز الإعلان عن إزالة عالمية كاملة إذا بقيت نسخ غير قابلة للفحص أو خارج السيطرة.

83. Evidence Impact

قد تعتمد Memory معتمدة على Episode أزيل محتواها.

إذا لم يعد الدليل متاحًا للتحقق، يجب أن يعاد تقييم الدعم المعرفي المناسب وفق RDMS-06 وRDMS-07.

الحذف لا يثبت خطأ الادعاء، لكنه قد يقلل الأدلة المتاحة لإسناده.

PART XXI — OPERATIONAL SAFETY RESERVE
84. Safety Reserve

نحافظ على مبدأ FCA وRDMS-04:

Budget exhaustion must not abandon unresolved world mutation.

يمكن أن تنفد الميزانية الاختيارية للمهمة.

لكن ذلك لا يسمح بإهمال عمليات Reconciliation الضرورية.

85. RecoveryBudgetPolicy
RecoveryBudgetPolicy {
    recovery_case_ref

    normal_budget_ref

    safety_reserve_ref

    authorized_safety_operations[]

    spending_limits

    escalation_conditions[]

    exhaustion_disposition
}
86. Reserve Exhaustion

لا ندعي أن Safety Reserve غير محدودة.

إذا لم تعد الموارد كافية لإكمال التسوية، يجب:

Persist unresolved state
Block dependent operations
Preserve recovery obligations
Escalate when appropriate

لا يمكن تحويل IN_DOUBT إلى FAILED لمجرد نفاد الموارد.

PART XXII — OPERATIONAL HEALTH
87. Health Monitoring

يمكن مراقبة:

Control Ledger availability
Snapshot integrity
Action reconciliation backlog
Pending triggers
Specialist failures
Provider failures
Storage health
Dependency evaluation failures
Memory index consistency
88. HealthStatus
OperationalHealthAssessment {
    evaluated_scope

    component_statuses[]

    critical_dependency_statuses[]

    unresolved_incidents[]

    recovery_backlog

    assessment_coverage

    overall_operational_risk
}
89. Health Is Not Authority

يمكن لمؤشرات Health أن تقترح:

DEGRADED
RECOVERY_REQUIRED
QUARANTINED

لكنها لا تستطيع تجاوز قوانين السلطة والبوابات.

كما أن نجاح Health Check لا يثبت وحده سلامة جميع العمليات الخارجية.

PART XXIII — RECOVERY READINESS
90. RecoveryReadinessAssessment

قبل العودة إلى العمل الطبيعي:

RecoveryReadinessAssessment {
    recovery_case_ref

    canonical_state_integrity

    executive_authority_validity

    unresolved_action_assessment

    trigger_recovery_status

    specialist_recovery_status

    dependency_freshness_status

    security_integrity_status

    required_policy_compliance

    remaining_blockers[]

    permitted_operational_scope
}
91. Scoped Recovery

ليس ضروريًا أن يؤدي خلل محدود إلى إيقاف كل المشاريع إذا ثبت استقلالها التشغيلي والسلطوي والبياني.

يمكن السماح بعودة:

Project A → NORMAL
Project B → SAFE_SUSPENDED

إذا كان الفصل بين المشروعين مثبتًا.

أما الاعتماديات المشتركة غير المحسومة فقد تستدعي نطاقًا أوسع من التقييد.

92. Recovery Completion

لا تعني نهاية RecoveryCase أن جميع آثار الحادث قد زالت تلقائيًا.

يجب تحديد ما الذي اكتمل:

Control state restored
World effects reconciled
Dependencies validated
Security constraints satisfied
Normal operation permitted

قد تنتهي معالجة جزء من الحادث بينما تبقى التزامات أخرى مفتوحة.

PART XXIV — NON-FUNCTIONAL REQUIREMENTS
93. Recovery Performance

يجب تقييم:

Recovery latency
Ledger replay cost
Snapshot restoration cost
Artifact verification cost
Reconciliation workload
Memory index rebuild cost

لكن الأداء لا يجوز أن يتحقق بتجاوز فحص سلامة لازم.

94. Scalability

عندما يتوسع الوكيل ليعمل على مشاريع عديدة ومتخصصين متعددين، يجب أن تتجنب Recovery إعادة تقييم جميع المعلومات غير المرتبطة بكل حادث.

نستخدم:

Affected scope
Dependency frontiers
Component ownership
Recovery priority
95. Observability

يجب أن نستطيع معرفة:

ما الذي تعطل؟

ما الحالة القانونية قبل العطل؟

ما الذي يمكن إثبات حدوثه؟

ما الذي ما زال مجهولًا؟

ما العمليات التي مُنعت؟

ما الذي تم إصلاحه؟

لماذا سُمح باستئناف العمل؟

دون الاعتماد على رواية جديدة ينتجها نموذج لغوي بعد وقوع الحادث.

PART XXV — CROSS-RDMS CONSERVATION
96. RDMS-01

لا تعيد RDMS-09 تعريف:

ControlCommit
CAS
Executive Epoch
Canonical Ledger
97. RDMS-02

لا تعيد RDMS-09 تعريف حالات Goals وSlices وDecisions.

98. RDMS-03

لا يستطيع Recovery System إنشاء Observations مزيفة أو إعادة تفسير التاريخ لتبرير الاستئناف.

99. RDMS-04

لا تستطيع RDMS-09 تغيير معنى IN_DOUBT أو تجاوز Write-Ahead Action Protocol.

100. RDMS-05

لا تنشئ Scheduler ثانية أو Trigger lifecycle منافسة.

101. RDMS-06

لا تمنح Specialists صلاحيات جديدة بسبب وقوع Crash أو Recovery.

102. RDMS-07

لا تتحول استعادة Memory إلى ترقية معرفية جديدة دون LearningGate.

103. RDMS-08

يحدد Cognitive Executive الحالية الاستراتيجية المعرفية بعد التعافي.

لكن إعادة تشغيل النظام لا تمنحها حق تجاوز شروط السلامة أو التحقق.

PART XXVI — FORMAL INVARIANTS

تقترح RDMS-09 الثوابت التالية:

RDMS09-I01 — Recovery cannot manufacture historical events or external outcomes.

RDMS09-I02 — Canonical control recovery derives from RDMS-01, not conversational model state.

RDMS09-I03 — Recovery orchestration cannot become a second semantic authority.

RDMS09-I04 — Operational recovery modes do not redefine FCA cognitive states.

RDMS09-I05 — Recoverability-critical metadata must remain durable and versioned.

RDMS09-I06 — An incomplete or untrusted control history cannot be silently accepted as current canonical state.

RDMS09-I07 — Restoring an older snapshot does not imply restoration of the external world to that time.

RDMS09-I08 — Potentially dispatched effects remain subject to RDMS-04 reconciliation.

RDMS09-I09 — IN_DOUBT cannot be converted to success or failure by timeout, retry or budget exhaustion alone.

RDMS09-I10 — Non-idempotent unknown actions cannot be blindly retried.

RDMS09-I11 — Leadership failover must fence obsolete authority.

RDMS09-I12 — Late results cannot recover expired authority.

RDMS09-I13 — Provider replacement cannot alter canonical project identity or authority.

RDMS09-I14 — Tool termination and world-effect termination are distinct claims.

RDMS09-I15 — Crash recovery cannot silently duplicate Specialist recruitment.

RDMS09-I16 — Trigger replay follows RDMS-05 identity and deduplication semantics.

RDMS09-I17 — Missing event history cannot be replaced by speculative edge-trigger reconstruction.

RDMS09-I18 — Resumed cognition must evaluate relevant dependency changes.

RDMS09-I19 — Restart alone does not invalidate unrelated knowledge.

RDMS09-I20 — Derived indexes cannot override canonical state.

RDMS09-I21 — Recovery from security incidents requires assessment of trust and integrity boundaries.

RDMS09-I22 — Revoked credentials do not imply already-started external effects have ceased.

RDMS09-I23 — Maintenance and shutdown cannot bypass mandatory reconciliation obligations.

RDMS09-I24 — Runtime upgrades must preserve canonical authority, state meanings and provenance.

RDMS09-I25 — Schema migration cannot silently rewrite accepted cognitive meaning.

RDMS09-I26 — Epistemic retirement and physical erasure are distinct.

RDMS09-I27 — Access suppression must not depend solely on derived retrieval-index freshness.

RDMS09-I28 — Physical deletion claims must remain bounded by verified storage scope.

RDMS09-I29 — Backup restoration cannot silently reactivate currently prohibited information.

RDMS09-I30 — Erasure-related evidence loss must be reflected in relevant knowledge validity.

RDMS09-I31 — Safety reconciliation takes precedence over ordinary discretionary budget limits.

RDMS09-I32 — Safety-reserve exhaustion cannot justify fabricating a resolved action state.

RDMS09-I33 — Recovery readiness must be assessed against actual outstanding obligations.

RDMS09-I34 — A healthy component status does not prove all external effects succeeded.

RDMS09-I35 — Recovery scope may be partial only when isolation and dependencies justify it.

RDMS09-I36 — Operational metrics cannot independently authorize cognitive or world mutations.

RDMS09-I37 — Recovery attempts must be recoverably identifiable and idempotent where their effects require it.

RDMS09-I38 — Recovery must preserve sufficient auditability to distinguish known, unknown, and inferred conditions.

RDMS09-I39 — Recovery cannot silently downgrade hard security or authority constraints.

RDMS09-I40 — Return to normal operation requires explicit satisfaction of applicable recovery-admission conditions.

PART XXVII — ADVERSARIAL FREEZE REVIEW TARGETS

قبل تجميد RDMS-09 يجب مهاجمة السيناريوهات التالية.

Control and Authority

A01 — Executive قديمة تستمر بعد انتقال epoch.

A02 — عمليتا Recovery تحاولان استعادة الحالة نفسها بالتزامن.

A03 — Ledger تحتوي فجوة في أحداث مطلوبة.

A04 — Snapshot قابلة للقراءة لكنها غير متماسكة.

A05 — Restore تستخدم Control State من إصدار غير متوافق.

A06 — Recovery Coordinator تحاول اعتماد Decision معرفية مباشرة.

World Effects

A07 — Crash بعد DISPATCH_INTENT وقبل التأكد من إرسال الأمر.

A08 — Crash بعد إرسال أمر خارجي وقبل حفظ النتيجة.

A09 — إعادة تشغيل تؤدي إلى تكرار عملية دفع.

A10 — Database migration جزئية.

A11 — Timeout بينما العملية الخارجية ما زالت تعمل.

A12 — RecoveryBudget تنفد أثناء Reconciliation.

A13 — OutcomeProbe تعطي نتيجة قديمة لا تثبت الحالة الحالية.

A14 — محاولة Compensation تفشل جزئيًا.

Storage and Disaster Recovery

A15 — فقدان Snapshot حديثة.

A16 — Backup تستعيد حالة أقدم من آثار العالم الخارجي.

A17 — Backup تحتوي Ledger غير مكتملة.

A18 — انقطاع تخزين أثناء ControlCommit.

A19 — تلف Artifact مطلوب لإثبات قرار.

A20 — انقطاع شبكة يؤدي إلى Split-Brain.

Providers and Tools

A21 — LLM Provider تتوقف أثناء التفكير.

A22 — استجابة قديمة تصل بعد تبديل Provider.

A23 — Tool process تستمر بعد Crash.

A24 — PID يعاد استخدامه ويخطئ Recovery في تحديد العملية.

A25 — نتائج Tool غير محفوظة رغم حدوث الأثر.

A26 — Provider fallback تستهلك ميزانية المهمة بالكامل.

Specialists and Temporal State

A27 — Specialist تتوقف أثناء تنفيذ Tool.

A28 — Restart ينشئ Specialist مكررة.

A29 — Specialist تعيد نتيجة بعد انتهاء عقدها.

A30 — Trigger يحدث أثناء Downtime.

A31 — Trigger نفسها تُسلَّم عدة مرات.

A32 — Edge Trigger لا تمتلك Replayable Source.

A33 — تغير التوقيت الصيفي أثناء انتظار Trigger.

Dependencies and Memory

A34 — Repository تتغير أثناء توقف النظام.

A35 — Negative Query تصبح stale بسبب ملف جديد.

A36 — Memory Index تختلف عن Canonical Memory.

A37 — Crash أثناء MemoryPromotion.

A38 — Derived Memory تفقد Evidence بعد Erasure.

Security and Data Lifecycle

A39 — Backup قديمة تعيد بيانات تم حذفها.

A40 — Derived summaries تحتفظ بمعلومات حساسة.

A41 — Credential compromise قبل Recovery.

A42 — Source Artifact تتعرض للتلاعب.

A43 — Recovery تستخدم Logs غير موثوقة لإصدار تعليمات.

A44 — ErasureOperation تدعي النجاح رغم بقاء Backups.

Upgrades and Shutdown

A45 — Migration تغير معنى كيان معرفي.

A46 — Upgrade تفشل بعد تعديل نصف الحالة.

A47 — Graceful Shutdown تبدأ أثناء World mutation.

A48 — Forced Shutdown يمنع Cleanup.

A49 — Normal Mode تُستعاد رغم وجود Action غير محسومة تؤثر في العمل.

A50 — Recovery تتجاوز سياسة جديدة نافذة باستخدام تفويض قديم.

PART XXVIII — IMPLEMENTATION ACCEPTANCE GATES
IG09-01 — Canonical Recovery

اختبارات سلامة Snapshots وControl Ledger وReplay.

IG09-02 — Authority and Failover

اختبارات epoch fencing وSplit-Brain ومحاولات الاعتماد القديمة.

IG09-03 — External Action Reconciliation

اختبارات DISPATCH_INTENT وIN_DOUBT وPARTIAL وعمليات التعويض.

IG09-04 — Process and Tool Recovery

اختبارات timeouts والعمليات اليتيمة وفقدان نتائج التنفيذ.

IG09-05 — Temporal Recovery

اختبارات replay وdeduplication وأحداث Downtime.

IG09-06 — Specialist Recovery

اختبارات الحفاظ على العقود والهوية والصلاحيات بعد Crash.

IG09-07 — Dependency Recovery

اختبارات تحديث Repository والحالات stale وPARTIALLY_STALE.

IG09-08 — Memory and Index Recovery

اختبارات ترقية الذاكرة وإعادة بناء الفهارس المشتقة.

IG09-09 — Security Recovery

اختبارات العزل وCredential Rotation والتحقق من سلامة المصادر.

IG09-10 — Backup and Disaster Recovery

اختبارات استعادة نسخ متماسكة مع التحقق من حدود RPO/RTO الفعلية.

IG09-11 — Erasure and Retention

اختبارات Access Suppression والنسخ والمشتقات والنسخ الاحتياطية.

IG09-12 — Upgrade and Shutdown

اختبارات migrations الجزئية والتوقف أثناء العمليات الخارجية.

IG09-13 — Recovery Admission

اختبارات منع الانتقال إلى NORMAL عندما تبقى التزامات حرجة غير محسومة.

PART XXIX — DRAFT VERDICT
Architecture:
    SYSTEM-WIDE GOVERNED RECOVERY

Canonical Control:
    RDMS-01

World-Effect Reconciliation:
    RDMS-04

Temporal Recovery:
    RDMS-05

Specialist Recovery:
    RDMS-06

Memory Governance:
    RDMS-07

Executive Reassessment:
    RDMS-08

RDMS-09 Responsibility:
    Cross-component recovery orchestration
    Operational safety
    Disaster recovery
    Lifecycle governance
    Data retention and erasure

Proposed Invariants:
    40

Adversarial Targets:
    50

Implementation Acceptance Gates:
    13

Adversarial Review:
    PENDING

Implementation:
    NOT AUTHORIZED
Final Draft Decision

RDMS-09 — System Recovery, Resilience, Operational Safety & Lifecycle Governance

DRAFT v1.0 COMPLETE.

NOT FROZEN.

هذه المسودة تحتاج إلى الهجوم العدائي الأول، خصوصًا على حدود التعافي بين Control Ledger والعالم الخارجي، وسلامة استعادة النسخ الاحتياطية، وتزامن عمليات القيادة والتعافي، وإزالة البيانات الحساسة.

Next Authorized Step: RDMS-09 — Adversarial Freeze Review 01.

ثلاثة قرارات أعتبرها الأهم في RDMS-09
1. التعافي ليس مجرد إعادة تشغيل البرنامج

تخيل أن وكيلنا يعمل على مشروع ضخم لمدة أسبوعين. خلال هذه المدة قام بقراءة المستودع، وبناء نموذج ذهني، وتنفيذ تعديلات، وإنشاء اختبارات، واتخاذ قرارات معمارية.

ثم ينطفئ الجهاز فجأة.

لا نريد عند إعادة التشغيل أن يبدأ من الصفر، ولا أن يستعيد آخر محادثة مع LLM ويحاول تخمين ما حدث.

نريد أن يستعيد الحالة المعرفية والقانونية المعتمدة، ويحدد ما الذي حدث فعلًا وما الذي ما زال مجهولًا.

2. لا يمكن التضحية بسلامة النظام من أجل الاستمرارية

قد يكون إبقاء الوكيل يعمل مفيدًا، لكن ليس في جميع الحالات.

إذا فقد النظام القدرة على إثبات صلاحياته، أو أصبحت حالة عملية خارجية حساسة مجهولة، فالتصرف الصحيح قد يكون إيقاف العمليات التابعة لها حتى تتوفر أدلة كافية.

التوقف الآمن أحيانًا أفضل من الاستمرار الخاطئ.

3. نحتاج إلى اختبار التعافي عن طريق إحداث الأعطال عمدًا

بعد تنفيذ المعمارية مستقبلًا، لا ينبغي أن نكتفي باختبارات Unit Tests العادية.

سنحتاج إلى ما يمكن تسميته Failure Injection Testing.

نوقف العمليات عمدًا عند نقاط حساسة، ونقطع الاتصالات، ونعيد تشغيل المكونات، ونختبر ما إذا كانت الحالة القانونية محفوظة وما إذا كان النظام يمنع تكرار الآثار الخارجية.

هذا النوع من الاختبارات سيكون ضروريًا لإثبات أن تصميمنا يعمل خارج الظروف المثالية.

حالة المشروع الحالية
Specification	Status
FCA v1.0.1	✅ FROZEN
RDMS-01 → RDMS-08	✅ FROZEN
RDMS-09	🟡 DRAFT v1.0
RDMS-10	⏳ PENDING

أصبح لدينا الآن تصميم أولي للمراحل التسع.

الخطوة التالية هي RDMS-09 — Adversarial Freeze Review 01، حيث سنحاول مهاجمة نظام التعافي من جميع الجهات قبل السماح بتجميده.

بعد إغلاق RDMS-09، سننتقل إلى RDMS-10 ثم المراجعة المعمارية الشاملة وتنظيم المشروع إلى مكونات وطبقات مستقلة، كما اتفقنا.

END ORIGINAL MESSAGE

========================================================================
SOURCE PART: C01
MESSAGE ID: 74cf7fd3-01ca-4f35-abed-fbbc8716eb5c
BEGIN ORIGINAL MESSAGE
========================================================================

سننتقل الآن إلى RDMS-09 C01 — Recovery Integrity & Lifecycle Safety Closure.

هذه المرحلة تحتاج دقة خاصة؛ لأن بعض أخطاء التعافي لا تؤدي فقط إلى توقف الوكيل، بل قد تسبب فقدان بيانات أو تكرار عمليات خارجية أو استعادة صلاحيات انتهت.

سنعالج الثغرات الـ28 والتحسينات الثمانية، مع الحفاظ على FCA وRDMS-01…08 دون تعديل. وسنحدد لكل ثغرة عقدًا تشغيليًا، وشروط السماح والمنع، والسلوك المطلوب عند فقدان اليقين.

لن نجمد RDMS-09 خلال هذه الخطوة. بعد اكتمال C01 سنخضع التصميم المصحح للهجوم العدائي الثاني.

RDMS-09 C01 — Recovery Integrity & Lifecycle Safety Closure
RDMS-09 C01
Recovery Integrity, Durable Authority, World Reconciliation & Lifecycle Safety Closure

Parent: RDMS-09 Draft v1.0
Review Source: FR09-G01…G28 / FR09-H01…H08
Architecture: Governed System Recovery
Dependencies: FCA v1.0.1 and RDMS-01…08 — FROZEN

Status: CORRECTIVE SPECIFICATION — READY FOR FREEZE REVIEW 02
Implementation: NOT AUTHORIZED
Production Changes: NONE

PART I — ARCHITECTURAL CONSERVATION
1. Recovery Is Not a Second Authority

يجب الحفاظ على مبدأ:

Recovery coordinates restoration; it does not create authority.

أي أن نظام التعافي مسؤول عن تنسيق استعادة الحالة والتأكد من سلامتها، لكنه لا يمتلك سلطة معرفية مستقلة.

المعمارية:

                    SYSTEM FAILURE
                          │
                          ▼
                 Recovery Detection
                          │
                          ▼
                Trusted Containment
                          │
                          ▼
                Recovery Coordinator
                          │
                 ┌────────┴────────┐
                 ▼                 ▼
          State Recovery      World Inspection
                 │                 │
                 └────────┬────────┘
                          ▼
                 Consistency Checks
                          │
                          ▼
                 Current Executive
                          │
                   Legal Decisions
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
          CommitGate              ActionGate
              │                       │
              ▼                       ▼
       Canonical State           World Actions

لا يجوز أن ينشئ Recovery Coordinator مسار كتابة مستقلًا.

2. Conserved Authorities

تبقى المسؤوليات التالية دون تغيير:

Authority	Canonical owner
Cognitive decisions	Current Cognitive Executive
Canonical commits	RDMS-01 / CommitGate
External actions	RDMS-04 / ActionGate
Observations	RDMS-03 / Observation Ingress
Temporal triggers	RDMS-05
Specialists	RDMS-06
Dependency evaluation	RDMS-06
Memory learning	RDMS-07
Cognitive control	RDMS-08
Recovery coordination	RDMS-09
3. Fundamental Recovery Separation

يجب الفصل بين:

RECOVERED CONTROL STATE

CURRENT LEGAL AUTHORITY

CURRENT WORLD STATE

TRUSTED RECOVERY EVIDENCE

هذه ليست شيئًا واحدًا.

يمكن أن تكون الحالة المستعادة صحيحة تاريخيًا، لكنها قديمة.

ويمكن أن تكون Executive الحالية مفوضة قانونيًا، لكن حالة العالم الخارجي غير محسومة.

ويمكن أن تبدو Snapshot متماسكة دون أن يكون مصدرها موثوقًا.

لا يسمح بالعودة إلى العمل الطبيعي إلا ضمن نطاق تتحقق فيه الالتزامات المطلوبة لكل محور.

PART II — RECOVERY MODE AUTHORITY
4. RecoveryModeAuthorityContract

Corrects FR09-G01

نحدد:

RecoveryModeAuthorityContract {
    operational_mode

    permitted_operation_classes[]

    prohibited_operation_classes[]

    required_authority_paths[]

    preauthorized_containment_controls[]

    mandatory_safety_guards[]

    required_control_integrity

    mode_exit_conditions[]
}
5. Operational Modes

نحافظ على الأوضاع الموجودة في المسودة:

NORMAL
DEGRADED
RECOVERY_REQUIRED
RECOVERING
QUARANTINED
SAFE_SUSPENDED

هذه أوضاع تشغيلية وليست حالات معرفية جديدة داخل FCA.

NORMAL

يسمح بالعمليات المعتمدة وفق القوانين المعتادة.

DEGRADED

يسمح فقط بالعمليات التي ثبت استقلالها عن المكونات المعطلة.

RECOVERY_REQUIRED

تمنع العمليات الجديدة المتأثرة إلى أن تبدأ إجراءات التعافي المعتمدة.

RECOVERING

تسمح بعمليات القراءة والتحقق والتسوية والإصلاح المصرح بها، مع بقاء حدود ActionGate وCommitGate نافذة.

QUARANTINED

تمنع استعمال المصادر أو الصلاحيات المشكوك في سلامتها.

SAFE_SUSPENDED

توقف الأعمال الاختيارية وتحافظ على الالتزامات القانونية غير المحسومة.

6. Emergency Containment

يجب التمييز بين:

Preventing an operation

و:

Performing a world mutation.

يمكن لمكون سلامة موثوق، وفق سياسة مثبتة مسبقًا، أن يمنع dispatch جديدة عندما تفشل شروط السلطة.

لكن تنفيذ عملية خارجية مثل:

Delete repository
Reset database
Revoke external credential
Terminate remote process

يبقى خاضعًا لمسار التفويض القانوني المناسب.

لا تصبح العملية قانونية بمجرد وصفها بأنها طارئة.

إذا كانت البيئة لا تستطيع تنفيذ إجراء الاحتواء الضروري ضمن السلطة المتاحة، يجب إظهار هذا القيد بدل اختراع صلاحية جديدة.

PART III — RECOVERY OWNERSHIP AND FENCING
7. RecoveryOwnershipLease

Corrects FR09-G02

RecoveryOwnershipLease {
    recovery_case_ref

    recovery_owner_id

    recovery_generation

    governing_executive_epoch

    ownership_scope[]

    lease_or_fencing_ref

    expected_control_version

    acquisition_commit_ref

    status
}
8. Single Recovery Owner Per Conflicting Scope

يمكن تنفيذ أعمال تحقيق مستقلة ومتوازية.

لكن لا يجوز وجود سلطتين متنافستين لتنفيذ عمليات تعافٍ متعارضة على المورد نفسه.

نحدد:

Recovery A:
    owns Action X reconciliation

Recovery B:
    attempts Action X compensation

النتيجة المطلوبة:

B cannot authorize conflicting effects
without lawful ownership transition.
9. Recovery Generation

إذا تعطل Recovery Worker ثم أعيد تشغيله، لا يفترض أنه ما زال يملك التفويض القديم.

يجب أن يتحقق من:

Current recovery generation
Current Executive epoch
Current recovery scope ownership
Expected control version

إذا انتقلت الملكية إلى Generation أحدث، تُحجب العمليات القانونية الجديدة الصادرة عن القديمة.

10. Lease Expiry Is Not World-Effect Cancellation

انتهاء صلاحية Recovery Lease لا يعني أن عملية خارجية سبق إرسالها قد توقفت.

تظل آثارها تحت مسؤولية RDMS-04.

وهذا يمنع الخلط بين إنهاء صلاحية المنسق وإنهاء الأثر الذي نسقه.

PART IV — SNAPSHOT, LEDGER AND ARTIFACT CONSISTENCY
11. RecoveryConsistencyManifest

Corrects FR09-G03

RecoveryConsistencyManifest {
    recovery_source_id

    snapshot_ref

    canonical_control_frontier

    required_ledger_segments[]

    required_artifact_refs[]

    required_schema_versions[]

    required_external_reference_manifests[]

    byte_integrity_assessment

    referential_integrity_assessment

    replay_consistency_assessment

    semantic_compatibility_assessment

    completeness_status
}
12. Three Levels of Integrity
Level 1 — Byte Integrity

هل البيانات المستعادة مطابقة للبصمة أو الإثبات المرجعي المتوقع؟

Level 2 — Referential Integrity

هل جميع المراجع الضرورية موجودة وقابلة للحل؟

Level 3 — Recovery Semantic Consistency

هل تسمح البيانات مجتمعة بإعادة بناء الحالة القانونية الصحيحة؟

مثال:

Snapshot:
    Decision D42 references Artifact A17.

Recovered storage:
    Artifact A17 missing.

حتى لو كانت Snapshot سليمة، لا يجوز اعتبار الحالة المستعادة مكتملة.

13. Missing Recovery-Critical Artifact

إذا كان Artifact مفقودًا لكنه ضروري لإثبات قرار أو أثر قانوني، يجب منع الاستعمال الذي يعتمد عليه.

أما Artifact مشتق يمكن إعادة بنائه من مصادر قانونية سليمة، فيمكن إعادة بنائه ضمن شروطه.

نميز بين:

CANONICAL_REQUIRED
RECOVERY_CRITICAL_REFERENCE
DERIVED_REBUILDABLE
OPTIONAL_DIAGNOSTIC

هذا تصنيف لاحتياجات الاستعادة، وليس إعادة تعريف لسلطة التخزين الأصلية.

14. Incomplete Ledger

لا يجوز ملء فجوة في Control Ledger عبر استدلال LLM.

Missing required control event
        ↓
Control history incomplete
        ↓
Block affected canonical continuation

إذا توفرت نسخة معتمدة مستقلة تسد الفجوة، يمكن استخدامها وفق بروتوكول الاستعادة القانوني.

أما إذا لم تتوفر أدلة كافية، فيجب الحفاظ على حالة عدم اليقين.

PART V — DURABLE ACKNOWLEDGEMENT GUARANTEES
15. DurabilityCapabilityAssessment

Corrects FR09-G04

DurabilityCapabilityAssessment {
    storage_backend_ref

    durable_ack_semantics

    required_persistence_boundary

    crash_consistency_model

    replication_ack_policy?

    acknowledged_control_frontier

    failover_consistency_guarantee

    verification_basis_ref

    compliance_result
}
16. Durable Means Recoverably Durable

لا يكفي أن تعيد واجهة التخزين:

write_success = true

إذا كان نجاحها يعني فقط إدراج البيانات في ذاكرة مؤقتة قابلة للفقدان.

بالنسبة إلى SHARED_WORLD، تشترط FCA تسجيل DISPATCH_INTENT تسجيلًا متينًا قبل إرسال العملية.

لذلك يجب أن تحقق طبقة التخزين معنى الإقرار بالمتانة الذي تعتمد عليه هذه القاعدة.

قد تستخدم البنية تنفيذًا محليًا أو موزعًا، لكن يجب إثبات ملاءمة ضماناتها.

17. Replication and Failover

إذا استُخدم تخزين موزع، ينبغي تحديد:

Which acknowledgements are durable?

Which replicas may become authoritative?

Can acknowledged writes disappear after failover?

Can two writers accept conflicting epochs?

إذا لم تستطع البنية ضمان الاحتفاظ بكتابة تم الإقرار بمتانتها ضمن نموذج الفشل المعلن، فلا يجوز استخدامها كحد قانوني مطابق لـWrite-Ahead Protocol دون معالجة هذه الفجوة.

18. Fail-Closed Dispatch
Durable dispatch intent not proven
        ↓
Shared-world dispatch forbidden

ولا يجوز تعويض نقص الإثبات بوعد النموذج اللغوي أن الكتابة حدثت.

PART VI — EXECUTIVE EPOCH ANTI-ROLLBACK
19. AuthorityAntiRollbackAssessment

Corrects FR09-G05

AuthorityAntiRollbackAssessment {
    restored_executive_epoch

    trusted_current_epoch_frontier

    trusted_leadership_source_ref

    known_active_grants[]

    conflicting_authority_refs[]

    post_backup_authority_events[]

    anti_rollback_proof_ref

    authority_recovery_status
}
20. Backup Is Not Authority

إذا استعدنا:

Backup epoch = 87

لكن التاريخ القانوني الحقيقي وصل سابقًا إلى:

Epoch = 105

فلا يجوز اعتبار 87 أحدث سلطة لمجرد أنها موجودة داخل النسخة المستعادة.

يجب إثبات الوضع الحالي عبر مصدر قيادة موثوق ومتوافق مع RDMS-01.

21. Monotonic Authority Recovery

يجب أن تمنع آلية استعادة القيادة إعادة إصدار جيل يتعارض مع جيل أحدث سبق اعتماده.

هذه مسؤولية ضمانات RDMS-01 والبنية التي تحققها.

لا تستحدث RDMS-09 مصدر قيادة ثانويًا يمكن أن ينافس المصدر القانوني.

22. Lost Authority Frontier

إذا فقد النظام القدرة على معرفة ما إذا كانت سلطة أحدث موجودة، فلا يجوز إعلان أن Executive المستعادة هي القائدة الوحيدة.

السلوك المطلوب:

Authority status = UNKNOWN
        ↓
No new authority-bearing effects
        ↓
Recover trusted leadership evidence
        ↓
Or require authorized recovery intervention
PART VII — POST-BACKUP EXTERNAL EFFECT COVERAGE
23. ExternalEffectRecoveryCoverage

Corrects FR09-G06

ExternalEffectRecoveryCoverage {
    restored_control_frontier

    independent_dispatch_history_refs[]

    external_effect_domains[]

    external_operation_identity_sources[]

    post_frontier_action_candidates[]

    recovered_action_refs[]

    unresolved_history_gaps[]

    reconciliation_coverage

    permitted_resumption_scope
}
24. Recovery Point vs External Reality

مثال:

10:00 Backup created
10:15 Payment dispatched
10:20 Payment completed
10:30 Storage lost
11:00 Backup restored

لا يجوز افتراض أن العالم الخارجي عاد إلى 10:00.

25. Required Recovery Search

يجب فحص المصادر المستقلة المتاحة، مثل:

External operation identifiers
Service transaction history
Remote repository state
Deployment history
Independent action-journal replicas

حسب نوع العملية وإمكانات المصدر.

لا نفترض أن كل خدمة خارجية توفر هذه البيانات أو أن تاريخها كامل.

26. Irrecoverable History Gap

إذا تعذر إثبات اكتمال السجل بعد Recovery Point:

Recovery coverage = INCOMPLETE

ويجب منع العمليات التي قد تتعارض مع آثار غير مرصودة ضمن نطاق الفجوة.

لا يلزم حجب جميع المشاريع إذا ثبت استقلالها عن المجال المتأثر.

PART VIII — TRUSTWORTHY OUTCOME PROBES
27. RecoveryProbeEvidence

Corrects FR09-G07

RecoveryProbeEvidence {
    action_ref

    probe_ref

    probed_effect_identity

    observed_resource_identity

    observation_timestamp_or_version

    source_consistency_guarantees

    source_provenance_ref

    freshness_assessment

    ambiguity_assessment

    supported_outcome
}
28. Probe Result Semantics

يجب أن يميز Probe بين:

EFFECT_CONFIRMED
EFFECT_ABSENCE_CONFIRMED_WITHIN_SCOPE
PARTIAL_EFFECT_CONFIRMED
INCONCLUSIVE

هذه نتائج تقييم وليست بدائل لحالات ActionLifecycle القانونية.

يستخدم RDMS-04 نتائجها لتحديد انتقال الحالة.

29. Stale Probe Protection

إذا كانت القراءة تأتي من Cache قديمة، فلا يجوز اعتبار عدم العثور على أثر إثباتًا لعدم حدوثه.

مثلًا:

Replica says:
    No deployment found.

قد تكون Replica متأخرة عن Primary.

ينبغي أن يحمل Probe معلومات تسمح بتحديد حدود هذه النتيجة.

30. Probe Cannot Resolve Ambiguity

إذا لم تستطع الأداة التمييز بين احتمالين مؤثرين:

Action executed but not visible yet.

Action never executed.

تبقى حالة الأثر غير محسومة.

لا يجوز تحويل IN_DOUBT إلى FAILED لمجرد أن Probe لم تجد سجلًا.

PART IX — RECONCILIATION OWNERSHIP
31. ActionRecoveryOwnership

Corrects FR09-G08

ActionRecoveryOwnership {
    action_ref

    recovery_case_ref

    owner_generation

    expected_action_lifecycle

    permitted_reconciliation_scope

    reconciliation_attempt_id

    current_fencing_ref

    ownership_commit_ref
}
32. Single Conflicting-Effect Authority

يمكن أن تعمل عدة عمليات قراءة على Action نفسها.

لكن يجب ألا تنفذ عمليتان متعارضتان إعادة إرسال أو تعويضًا أو تغييرًا لحالتها القانونية دون ترتيب صالح.

33. Reconciliation Is Not Compensation Authorization

امتلاك حق التحقيق في Action لا يمنح حق تنفيذ Compensation.

إذا كانت Compensation تؤثر في العالم الخارجي، فإنها تحتاج ActionProposal ومسار التفويض المناسب.

34. Ownership Transfer

إذا تعطل Recovery Owner:

Owner generation N
        ↓
Failure
        ↓
Generation N+1 takes ownership

يجب حجب الاعتمادات الجديدة من Generation القديمة.

أما الآثار التي سبق إرسالها فتظل جزءًا من التاريخ الواجب تسويته.

PART X — COMPENSATION FAILURE GOVERNANCE
35. CompensationEffectLineage

Corrects FR09-G09

CompensationEffectLineage {
    original_action_ref

    compensation_proposal_ref

    compensation_action_ref

    compensation_execution_refs[]

    observed_compensation_effects[]

    affected_resource_refs[]

    residual_uncertainty_refs[]

    verification_status
}
36. Compensation Is Another World Action

إذا نفذ النظام:

Original Action:
    PARTIAL

Compensation:
    PARTIAL

فلا يجوز اعتبار العالم قد عاد إلى الحالة الأصلية.

37. No Automatic Compensation Chain

يجب ألا تتحول:

Action fails
    ↓
Compensation fails
    ↓
Second compensation fails
    ↓
Third compensation...

إلى حلقة غير محدودة.

كل عملية جديدة تحتاج إلى مبرر وأهلية وتفويض وموازنة مخاطر وفق RDMS-04 وRDMS-08.

38. Residual World State

النتيجة الصحيحة قد تكون:

Original effect partly applied.

Compensation partly applied.

Current world state incompletely known.

يجب حفظ هذه الحالة بوضوح، وحجب الأعمال التابعة حسب اعتمادياتها الفعلية.

PART XI — RECOVERABLE PROCESS IDENTITY
39. RecoverableProcessIdentity

Corrects FR09-G10

RecoverableProcessIdentity {
    action_ref

    execution_host_ref

    process_instance_id

    process_start_identity

    containment_domain_ref

    originating_executive_epoch

    launch_receipt_ref

    available_lifecycle_evidence_refs[]
}
40. PID Is Not Sufficient

لا يجوز تحديد عملية بناءً على PID وحده عندما تسمح البيئة بإعادة استخدامه.

يجب استخدام معلومات إضافية موثوقة حسب إمكانات النظام.

قد تشمل:

Process start identity
Execution container identity
Host instance identity
Supervisor ownership
Action identity
41. Safe Termination

قبل محاولة إنهاء Process يجب التأكد من:

Target identity
Authority to terminate
Expected side effects
Current process ownership

إذا تعذر تحديد العملية بصورة آمنة، فلا يجوز إرسال Kill اعتباطي.

42. Termination Does Not Prove Effect Reversal

حتى لو ثبت توقف Process، فقد تكون قد أرسلت طلبًا خارجيًا قبل توقفها.

لذلك:

Process terminated
    ≠
World effect cancelled
PART XII — DOWNSTREAM FENCING
43. DownstreamFencingAssessment

Corrects FR09-G11

DownstreamFencingAssessment {
    project_ref

    current_executive_epoch

    action_runtime_refs[]

    tool_session_refs[]

    specialist_session_refs[]

    enforceable_fencing_boundaries[]

    non_fenceable_effect_paths[]

    affected_inflight_action_refs[]

    required_reconciliation_refs[]
}
44. Fencing Boundaries

يجب فرض Fencing عند جميع نقاط السلطة التي نستطيع التحكم فيها.

مثلًا:

ControlCommit admission
Action authorization
Dispatch gateway
Specialist integration
Tool-session authorization

لكن ليس من الصحيح الادعاء بأن جميع الخدمات الخارجية تدعم Executive Epoch.

45. Unfenceable External Sessions

إذا كانت جلسة خارجية بدأت سابقًا ولا تستطيع البيئة إيقافها أو إبطال تفويضها فورًا، يجب تسجيل هذا الحد.

قد تكون النتيجة:

Old Executive fenced locally.

External session may still be active.

ويجب التعامل مع آثارها الممكنة في Reconciliation.

PART XIII — LATE INVOCATION ADOPTION
46. RecoveredInvocationBinding

Corrects FR09-G12

RecoveredInvocationBinding {
    invocation_id

    attempt_generation

    originating_executive_epoch

    originating_canonical_context_ref

    originating_dependency_set_ref

    provider_or_tool_ref

    returned_result_ref

    current_freshness_evaluation_ref

    adoption_authorization_ref?
}
47. Delayed Response Rule

إذا وصلت استجابة من محاولة قديمة بعد بدء محاولة جديدة، فلا يجوز خلط النتيجتين.

حتى لو كان نص الإجابة متشابهًا.

48. Result Adoption

يمكن استعمال نتيجة قديمة بوصفها تحليلًا مرشحًا عندما:

يكون مصدرها معروفًا.

تكون صلاحية اعتمادياتها مقبولة.

تسمح سياسة Executive الحالية باستخدامها.

لا تحمل صلاحية تنفيذ منتهية.

ولا يجوز أن تتحول مباشرة إلى Action جديدة اعتمادًا على سلطة سابقة.

PART XIV — TRIGGER RECOVERY FRONTIER
49. TriggerRecoveryFrontier

Corrects FR09-G13

TriggerRecoveryFrontier {
    trigger_ref

    trigger_generation

    source_stream_identity

    recovered_source_cursor

    canonical_reaction_frontier

    replay_coverage

    unresolved_event_gaps[]

    deduplication_basis_ref
}
50. Source Cursor and Reaction Cursor

يجب التمييز بين:

Event observed from source

و:

Canonical reaction committed

قد يكون الحدث قد شوهد لكن لم تُعتمد استجابته بعد.

وقد يكون رد الفعل قد اعتُمد بينما لم تصل acknowledgement إلى المصدر.

51. Replay Safety

تستخدم RDMS-05 هوية الحدث ورد الفعل لتجنب تكرار Control Effects.

أما إذا احتاج رد الفعل إلى Mutation خارجية، فيجب أن تدخل RDMS-04 ولا يجوز افتراض exactly-once خارجي دون ضمان مناسب.

52. Edge Trigger Limitation

إذا لم يكن المصدر قادرًا على إثبات حدوث Edge أثناء الانقطاع:

Replay coverage = UNKNOWN

ولا يجوز اختلاق Event مفقودة.

PART XV — SPECIALIST RECOVERY OWNERSHIP
53. SpecialistRecoveryOwnership

Corrects FR09-G14

SpecialistRecoveryOwnership {
    original_specialist_run_ref

    original_contract_ref

    original_generation

    workspace_ref

    pending_action_refs[]

    fencing_status

    replacement_run_ref?

    replacement_authorization_ref?

    supersession_relation_ref?
}
54. No Duplicate Recruitment

إذا ظن النظام أن Specialist تعطلت، فلا يجوز تلقائيًا إنشاء نسخة أخرى قبل تحديد حالة العقد السابق.

قد تكون Specialist الأصلية:

Alive but disconnected
Paused
Crashed
Completed but unreported
Running external action

هذه حالات مختلفة.

55. Replacement Semantics

يمكن إنشاء Replacement وفق RDMS-06.

لكن يجب أن تكون علاقتها بالنسخة السابقة واضحة.

لا يجوز دمج نتيجتيهما بصورة تلقائية، خصوصًا إذا كانتا تعملان على Snapshots مختلفة.

56. Workspace Ownership

يجب حماية مساحة العمل من كتابة متزامنة غير مصرح بها عندما تتطلب العقود العزل.

ولا يستطيع Recovery تجاوز Isolation لمجرد محاولة تسريع الاستعادة.

PART XVI — DEPENDENCY RECOVERY COVERAGE
57. RecoveryDependencyCoverage

Corrects FR09-G15

RecoveryDependencyCoverage {
    evaluated_scope

    required_index_refs[]

    available_index_refs[]

    source_frontier_refs[]

    completeness_assessment

    dependency_evaluation_refs[]

    unresolved_dependency_scope[]
}
58. Incomplete Index Rule

إذا كانت Dependency Index غير مكتملة:

No dependency found

لا يثبت:

No dependency exists

يجب استعمال RDMS-06 لتقييم الصلاحية ضمن حدود مصادر الأدلة المتاحة.

59. Conservative Fallback

عندما لا يمكن إثبات نطاق اعتمادية ضيق، تستخدم سياسة أكثر تحفظًا.

لكن لا نعتبر كل Repository Change سببًا لإبطال جميع النتائج دون تحليل.

60. Derived Index Rebuild

يمكن إعادة بناء Index مشتقة من مصادرها القانونية.

لكن لا يسمح باستعمالها في قرارات تتطلب اكتمالًا حتى تثبت تغطيتها المطلوبة.

PART XVII — OBSERVATION RECOVERY COVERAGE
61. ObservationRecoveryCoverage

Corrects FR09-G16

ObservationRecoveryCoverage {
    related_action_ref?

    expected_observation_scope

    observation_source_refs[]

    source_ingress_frontiers[]

    received_observation_refs[]

    missing_observation_scope[]

    observation_completeness

    supported_outcome_claims[]
}
62. Missing Observation Is Not Success

إذا لم توجد Observation تثبت فشل اختبار:

No failure observed.

فهذا لا يثبت:

Test succeeded.

خصوصًا إذا تعطل Observation Pipeline.

63. Delayed Observation Ingress

إذا وصلت Observation بعد Recovery، يجب الحفاظ على:

Original observation identity
Source provenance
Source event or time context
Related action identity

ولا يجوز اعتبار وصولها المتأخر حدثًا جديدًا مستقلًا إذا كانت إعادة تسليم للحدث نفسه.

64. Incomplete Observation History

عندما تكون تغطية الرصد ناقصة، لا يجوز إصدار استنتاجات تتطلب اكتمالها.

ويجب الحفاظ على التناقضات بدل إعادة كتابة التاريخ لتوافق النتائج المتوقعة.

PART XVIII — SCOPED RECOVERY ADMISSION
65. ScopedRecoveryAdmission

Corrects FR09-G17

ScopedRecoveryAdmission {
    requested_project_scope

    requested_operation_classes[]

    required_control_integrity

    shared_resource_refs[]

    required_dependency_frontier

    unresolved_action_impact

    security_restrictions[]

    applicable_policy_versions[]

    admission_result

    authorized_operational_scope
}
66. Partial Recovery

ليس مطلوبًا إيقاف جميع المشاريع بسبب عطل محدود.

يمكن أن تكون:

Project A:
    NORMAL

Project B:
    SAFE_SUSPENDED

إذا ثبت استقلال A عن العطل الذي أصاب B.

67. Shared Dependency Rule

إذا تشارك المشروعان في Credential أو Service تعرضت للاختراق، فلا يكفي القول إن ملفات Project A سليمة.

يجب تقييم الاعتماديات المشتركة.

68. Unknown Isolation

إذا لم يمكن إثبات العزل المطلوب، فلا يسمح بعودة العمليات التي تعتمد عليه.

ولا يجوز استخدام رغبة النظام في الاستمرار بدل دليل استقلال فعلي.

PART XIX — TRUSTED RECOVERY SOURCES
69. RecoveryTrustAnchorAssessment

Corrects FR09-G18

RecoveryTrustAnchorAssessment {
    recovery_source_ref

    integrity_proof_ref

    verification_authority_ref

    trusted_reference_location

    source_provenance

    key_or_anchor_status

    compromise_assessment

    admissibility
}
70. Checksum vs Trusted Integrity

وجود Checksum بجوار Backup لا يثبت أن النسخة أصلية إذا تمكن مهاجم من تعديل الملف والـChecksum معًا.

يجب تحديد:

Who produced the integrity proof?

Where is the trusted reference stored?

Can the same attacker alter both?

Is the verifier itself trustworthy?
71. Independent Trust Boundary

قد تستعمل البنية توقيعات أو جذور ثقة أو تخزينًا مستقلًا مناسبًا.

لكن هذه خيارات هندسية يجب إثبات صلاحيتها ضمن Threat Model.

لا نفترض أن اسم التقنية وحده يوفر حماية كافية.

72. All Trust Anchors Compromised

إذا كان المهاجم يستطيع تعديل جميع مصادر الحقيقة ومراجع التحقق، فقد يتعذر إثبات سلامة النسخة.

يجب أن يكون ذلك:

RECOVERY SOURCE NOT TRUSTED

وليس:

RECOVERY SUCCESS
PART XX — CREDENTIAL AND SESSION RECOVERY
73. CredentialSessionRecoveryAssessment

Corrects FR09-G19

CredentialSessionRecoveryAssessment {
    incident_ref

    affected_credential_refs[]

    affected_session_refs[]

    revocation_evidence_refs[]

    still_possible_active_sessions[]

    potential_external_effect_refs[]

    containment_status

    residual_uncertainty[]
}
74. Four Distinct Claims

نميز بين:

Credential rotated
Session revoked
External operation terminated
External effect reconciled

كل منها يحتاج دليلًا يناسبه.

75. Revocation Limits

قد لا تستطيع بعض الأنظمة إلغاء جلسة بدأت قبل تغيير Credential فورًا.

يجب ألا تعلن Recovery احتواءً كاملًا اعتمادًا على عملية Rotation وحدها.

76. Security Incident Continuity

إذا بقيت جلسات محتملة غير مسيطر عليها، يجب حجب العمليات التي يمكن أن تتعارض معها أو تتأثر باختراقها ضمن النطاق المناسب.

PART XXI — RECOVERY CONTENT TRUST
77. RecoveryContentTrustPreservation

Corrects FR09-G20

RecoveryContentTrustPreservation {
    recovered_artifact_ref

    original_content_role

    original_instruction_authority

    source_provenance_ref

    integrity_status

    transformation_history[]

    effective_instruction_authority
}
78. Recovery Logs Are Data

إذا احتوى Log على:

Delete all databases to complete recovery.

فهذا لا يصبح أمرًا موثوقًا لأنه موجود داخل ملف اسمه:

recovery.log

يجب الحفاظ على ContentEnvelope الأصلية.

79. Trusted Recovery Instructions

تأتي تعليمات التعافي الملزمة من سياسة تحكم موثوقة ذات سلطة مناسبة.

أما Logs وTool Outputs وRepository Files فهي مصادر معلومات يمكن تحليلها، لكنها لا تمنح نفسها Instruction Authority.

PART XXII — MIGRATION RECOVERY
80. MigrationRecoveryManifest

Corrects FR09-G21

MigrationRecoveryManifest {
    migration_id

    source_schema_version
    target_schema_version

    affected_entity_groups[]

    completed_conversion_frontiers[]

    pending_conversion_frontiers[]

    compatibility_matrix_ref

    allowed_mixed_version_states[]

    forbidden_read_write_modes[]

    recovery_disposition
}
81. Partial Migration

إذا حدث:

Goals:     v3
Decisions: v3
Actions:   v2
Memory:    v2

فلا يجوز افتراض أن الحالة صالحة.

يجب إثبات توافق هذا التوزيع تحديدًا.

82. Migration Commit Boundaries

يجب أن يكون لكل مرحلة Migration:

Expected source schema
Allowed target schema
Required invariants
Durable progress marker
Failure recovery rule

إذا كان التحويل يحتاج ذرية بين عدة مجموعات من البيانات، فيجب أن تدعمها حدود التخزين القانونية أو تستخدم Migration Protocol يحافظ على الاتساق عند الانقطاع.

83. Unknown Migration State

إذا تعذر تحديد ما الذي تحول وما الذي لم يتحول:

Migration status = UNKNOWN

وتمنع العمليات التي قد تفسر الحالة بصورة خاطئة.

لا يجوز لـLLM تخمين نسخة Schema اعتمادًا على شكل البيانات فقط.

PART XXIII — UPGRADE ROLLBACK SAFETY
84. UpgradeRollbackAssessment

Corrects FR09-G22

UpgradeRollbackAssessment {
    upgrade_ref

    current_schema_frontier

    pre_upgrade_snapshot_ref?

    post_upgrade_action_refs[]

    externally_visible_effect_refs[]

    backward_compatibility_assessment

    rollback_loss_risk

    forward_recovery_requirements[]

    rollback_admissibility
}
85. Rollback Is Not Time Travel

إذا غيّر Runtime الجديد قاعدة بيانات أو أرسل أحداثًا خارجية، فإن استعادة البرنامج القديم لا تعيد تلك الآثار تلقائيًا.

86. Rollback Eligibility

يجب أن يكون الرجوع إلى الإصدار السابق مسموحًا فقط إذا كان النظام يستطيع التعامل بصورة صحيحة مع الحالة الحالية أو إذا وجدت آلية قانونية لاستعادة الاتساق.

وإلا:

Rollback forbidden
        ↓
Forward recovery
or
Safe suspension

بحسب الوضع الفعلي.

PART XXIV — DURABLE DATA PLACEMENT
87. DurableDataPlacementPolicy

Corrects FR09-G23

DurableDataPlacementPolicy {
    data_class

    permitted_control_metadata_fields[]

    forbidden_content_classes[]

    removable_content_storage_ref

    reference_token_policy

    redaction_requirements[]

    audit_preservation_requirements[]

    recovery_reference_requirements[]
}
88. Immutable Metadata Boundary

لا يجوز تصميم Control Ledger بحيث يحتوي تلقائيًا على:

Passwords
Private source files
Customer records
Unredacted tool outputs
Sensitive prompt contexts

ثم الادعاء بإمكان حذف هذه البيانات لاحقًا دون قيود.

89. Opaque References

يفضل أن تحتوي السجلات القانونية على مراجع إلى محتوى محكوم التخزين عندما تسمح متطلبات التدقيق والتعافي بذلك.

لكن يجب الانتباه إلى أن:

Hash
Identifier
Filename
Path

قد يكشف معلومات حساسة بحسب نوعه وسياقه.

لا نعتبر جميع المراجع آمنة تلقائيًا.

90. Already Contaminated Ledger

إذا دخل محتوى حساس بالفعل إلى سجل غير قابل للإزالة، فلا يجوز إعلان محوه الكامل دون دليل.

يجب تسجيل القيد ومعالجة الإفصاح والاحتفاظ وفق السلطة والسياسة المعتمدة.

PART XXV — ERASURE COVERAGE
91. ErasureCoverageAssessment

Corrects FR09-G24

ErasureCoverageAssessment {
    authorized_erasure_request_ref

    source_data_refs[]

    controlled_derivative_refs[]

    controlled_backup_refs[]

    known_external_copy_refs[]

    provider_retention_boundaries[]

    unverifiable_copy_domains[]

    effective_suppression_scope

    verified_physical_erasure_scope

    residual_limitations[]
}
92. Transitive Data Lineage

قد تظهر البيانات في:

Original file
    ↓
Episode
    ↓
Reflection
    ↓
Memory
    ↓
Retrieval context
    ↓
Specialist result
    ↓
Derived summary

يجب تحديد ما أمكن من المشتقات المشمولة بالطلب.

لا يجوز افتراض أن حذف المصدر يزيل جميع المشتقات.

93. External Copies

قد توجد نسخ لدى مزود خدمة خارجي أو داخل سجلات لا يتحكم بها النظام.

يجب تحديد:

Known controlled copies
Known external copies
Unknown or unverifiable copies

لا نعد بإزالة ما لا نستطيع التحكم فيه أو التحقق من إزالته.

94. Physical Erasure Verification

النتائج المقبولة يجب أن تكون محددة النطاق:

VERIFIED_WITHIN_DECLARED_SCOPE
INCOMPLETE
UNKNOWN

ويجب أن يكون نطاق الإثبات جزءًا من تقرير النتيجة.

PART XXVI — ERASURE ANTI-ROLLBACK
95. ErasureAntiRollbackFrontier

Corrects FR09-G25

ErasureAntiRollbackFrontier {
    applicable_data_scope

    durable_suppression_generation

    authoritative_suppression_source_ref

    authorized_erasure_record_refs[]

    recovery_source_frontier

    pending_reapplication_scope[]

    retrieval_release_authorization_ref?
}
96. Restore-Time Suppression

إذا استعدنا Backup تسبق عملية حذف:

Old Backup
      ↓
Recovered Data
      ↓
Current Suppression Policy Check
      ↓
Blocked From Retrieval

لا يجوز تمكين البحث أو الإفصاح قبل تطبيق السياسة النافذة.

97. Anti-Rollback Authority

يجب أن يستند سجل قيود الحذف إلى مصدر موثوق لا يمكن استبداله بصمت بمحتويات Backup القديمة نفسها.

إذا فقد النظام هذا المصدر ولم يستطع إثبات أن السياسة المستعادة أحدث سياسة نافذة:

Disclosure authorization = UNKNOWN

ويجب منع الإفصاح الذي يحتاج إلى هذا الإثبات.

98. Restoration Does Not Reverse Erasure Legality

وجود البيانات مجددًا على القرص بسبب استعادة Backup لا يجعل استخدامها قانونيًا.

كما أن منع استخدامها لا يعني أنها حذفت ماديًا.

يبقى الفصل بين:

Access suppression
Physical erasure

إلزاميًا.

PART XXVII — LEGAL HOLD AND ERASURE CONFLICT
99. DataLifecycleConflictAssessment

Corrects FR09-G26

DataLifecycleConflictAssessment {
    conflicting_request_refs[]

    applicable_policy_refs[]

    verified_authority_domains[]

    affected_data_scope

    conflicting_obligations[]

    required_adjudication_ref?

    permitted_interim_controls[]

    resolution_status
}
100. Conflict Semantics

قد تتعارض:

Delete data

مع:

Preserve data under legal hold

لا يملك النظام سلطة تفسير القانون بصورة نهائية لمجرد توفر LLM.

101. Interim Protection

عند تعذر الحسم، يجب تطبيق القيود المؤقتة المصرح بها لحماية البيانات ومنع الإفصاح غير المبرر، دون حذف لا رجعة فيه أو إفشاء غير مسموح.

يجب الرجوع إلى السلطة المختصة بالمجال عندما يتطلب القرار ذلك.

102. Resolution Binding

أي قرار حاسم يجب أن يحدد:

Decision authority
Affected data scope
Applicable policy version
Authorized action
Evidence of resolution

ولا يجوز تطبيقه على مجالات بيانات لم يشملها القرار.

PART XXVIII — DESTRUCTIVE RECOVERY AUTHORIZATION
103. RecoveryActionAuthorizationAssessment

Corrects FR09-G27

RecoveryActionAuthorizationAssessment {
    recovery_operation_ref

    target_resource_scope

    expected_destructive_effects[]

    preserved_data_scope[]

    potentially_lost_data_scope[]

    reversibility_assessment

    required_domain_authority

    action_gate_requirements[]

    authorization_status
}
104. Destructive Recovery Is a World Action

مثال:

Restore repository from backup.

قد يؤدي إلى فقدان تعديلات لم تُنسخ.

لذلك لا يجوز اعتبار Restore عملية قراءة آمنة دائمًا.

105. Preconditions

قبل عملية Recovery مدمرة يجب فحص:

Current target identity
Current world-state knowledge
Backup integrity
Potentially lost data
Impact on pending actions
Required authorizations
Rollback or compensation feasibility
106. Unknown Destructive Impact

إذا كان أثر الاستعادة غير معروف بصورة مؤثرة، فلا يجوز افتراض أنه مقبول.

قد يحتاج النظام إلى:

Additional inspection
Isolated restoration
Authorized human decision
Safe suspension

وفق المخاطر والسلطة المتاحة.

PART XXIX — RECOVERY LOOP STABILITY
107. RecoveryProgressControl

Corrects FR09-G28

RecoveryProgressControl {
    recovery_case_ref

    attempt_generation

    repeated_failure_signatures[]

    newly_acquired_recovery_evidence[]

    resolved_obligation_refs[]

    unresolved_obligation_refs[]

    remaining_resource_ref

    retry_eligibility

    escalation_conditions[]

    safe_terminal_disposition
}
108. Recovery Must Not Loop Indefinitely

إذا فشلت محاولة الاتصال بالخدمة نفسها دون أي تغيير:

Attempt 1 → no progress
Attempt 2 → no progress
Attempt 3 → no progress

فلا يجوز استمرار إعادة المحاولة دون سياسة حدود وتصعيد.

109. Failed Recovery Can Still Gain Evidence

كما في Cognitive Executive، لا يعني فشل محاولة Recovery غياب الفائدة.

قد تثبت المحاولة أن:

A backup is corrupted.
A remote service is unavailable.
A process identity is invalid.

وهذه معلومات مؤثرة في خطة التعافي.

110. Safe Recovery Stopping

عندما لا تتوفر وسيلة آمنة للاستمرار:

Persist unresolved state
        ↓
Block dependent operations
        ↓
Preserve reactivation conditions
        ↓
Escalate when authorized
        ↓
SAFE_SUSPENDED / BLOCKED

لا يجوز إعلان نجاح التعافي بسبب انتهاء الموارد.

111. RecoveryCase Continuity

إعادة تشغيل Recovery Worker لا تنشئ تلقائيًا حادثًا مستقلًا جديدًا يتجاوز حدود المحاولات السابقة.

تستخدم RecoveryCase وهوية Generation لضمان استمرار الحوكمة.

PART XXX — HARDENING CORRECTIONS
112. H01 — Measurable Recovery Objectives

يجب تحديد RPO وRTO بحسب المجال.

قد تختلف احتياجات:

Canonical Ledger
Action Journal
Memory Index
Temporary workspace

ولا يجوز الادعاء بتحقيق RPO/RTO قبل قياسها في البيئة المقصودة.

113. H02 — Recovery Observability

نحتاج عرضًا واضحًا لـ:

Active recovery cases
Unresolved actions
Missing control artifacts
Current authority
Recovery blockers
Safety obligations

لكن Health Monitoring لا تتحول إلى سلطة تنفيذية.

114. H03 — Backup Failure-Domain Independence

يجب تقييم ما إذا كانت جميع النسخ الاحتياطية تتشارك مخاطر الفشل نفسها.

مثل:

Same disk
Same account
Same credentials
Same administrative domain

وتُحدد الحاجة إلى استقلال إضافي بحسب Threat Model ومتطلبات الاستعادة.

115. H04 — Recovery Drills

يجب اختبار:

Process crash
Power loss
Network partition
Backup restore
Delayed tool results
Concurrent recovery

بتجارب قابلة للتكرار حيث تسمح البيئة بذلك.

116. H05 — Recovery Backpressure

عند استعادة نظام كبير يجب منع إغراق المكونات:

Control Ledger
External services
Provider APIs
Dependency Engine
Memory indexes

مع إعطاء أولوية للالتزامات الحرجة وعدم تحويل Backpressure إلى إسقاط للأحداث.

117. H06 — Recovery Artifact Retention

يجب تطبيق سياسات الاحتفاظ والخصوصية على:

Recovery logs
Diagnostic artifacts
Probe outputs
Audit receipts
Provider responses

ولا تُعفى هذه البيانات من الحوكمة لأنها أُنشئت أثناء حادث.

118. H07 — Human Escalation

عندما يحتاج النظام إلى تدخل بشري، يجب أن يوضح:

Known state
Unknown effects
Affected resources
Blocked operations
Available safe choices
Required authority

دون تقديم تخمينات عن نتائج خارجية باعتبارها حقائق.

119. H08 — Recovery Scalability

تُقاس تكلفة:

Ledger replay
Snapshot validation
World reconciliation
Index reconstruction
Dependency evaluation
Specialist recovery

ويجب دعم الاستعادة المحددة النطاق عندما يمكن إثبات استقلالها.

PART XXXI — CROSS-CUTTING CORRECTIONS
120. Recovery Evidence Conservation

جميع إجراءات التعافي تعتمد على أدلة ذات provenance واضحة.

لا يجوز لـRecovery System أن ينشئ Observation تاريخية من تفسير نصي.

كما لا يجوز له تجاهل Observation متناقضة فقط لأنها تعيق الاستئناف.

121. Trust Before Execution

يجب التفريق بين:

Artifact can be read.

و:

Artifact is trusted for execution.

فيمكن أن تكون ملفات مستعادة قابلة للقراءة لكنها غير موثوقة.

لا يجوز تنفيذ Scripts أو Configurations مستعادة ذات آثار خارجية قبل استيفاء شروط الثقة والتفويض المناسبة.

122. Cross-Domain Recovery Barrier

إذا تأثرت عدة مكونات بالعطل نفسه:

Control Ledger
Memory
Actions
Specialists
Triggers

فيجب تحديد الاعتماديات التي تمنع تشغيل كل جزء.

لا يجوز استئناف جزء يعتمد على آخر غير مستعاد بصورة كافية.

123. Recovery Admission Must Be Scope-Aware

لا نطلب أن تكون كل أجزاء المشروع سليمة قبل السماح بأي عمل.

لكن يجب إثبات سلامة الاعتماديات اللازمة للعمل المسموح به.

Recovered safe scope
        ≠
Globally recovered system
124. Recovery Cannot Upgrade Evidence

إذا استعادت المنظومة Memory أو Observation، فلا يعني ذلك إعادة إثبات حقيقتها الحالية.

يجب احترام temporal validity وDependency Evaluation.

125. Reconciliation Before Conflicting Continuation

عندما يوجد أثر خارجي غير محسوم، يجب تحديد العمليات التابعة أو المتعارضة معه.

هذه العمليات لا تستأنف اعتمادًا على تخمين أن الأثر لم يحدث.

وتظل IN_DOUBT حالة قانونية ذات معنى محدد في RDMS-04.

PART XXXII — ADDITIONAL FORMAL INVARIANTS

تُضاف إلى RDMS09-I01…I40 الثوابت التالية:

RDMS09-I41 — Operational recovery modes constrain permitted actions but never create independent semantic or world-mutation authority.

RDMS09-I42 — Conflicting recovery work requires versioned ownership and fencing.

RDMS09-I43 — Snapshot integrity must include recoverability-critical reference and semantic consistency.

RDMS09-I44 — Shared-world dispatch requires a storage acknowledgement that satisfies the declared durability contract.

RDMS09-I45 — Restored snapshots cannot roll back the authoritative Executive epoch.

RDMS09-I46 — Post-backup external effects must be reconciled within a declared coverage scope before conflicting continuation.

RDMS09-I47 — An inconclusive or stale OutcomeProbe cannot resolve IN_DOUBT.

RDMS09-I48 — Reconciliation ownership cannot implicitly authorize compensation or repeated world effects.

RDMS09-I49 — Compensation effects require their own provenance, legal action records and outcome reconciliation.

RDMS09-I50 — Process termination requires trustworthy target identity and does not itself prove external-effect termination.

RDMS09-I51 — Executive fencing guarantees must explicitly account for downstream execution boundaries and non-fenceable effects.

RDMS09-I52 — Late invocation results cannot regain expired authority.

RDMS09-I53 — Trigger recovery must preserve source and canonical reaction frontiers.

RDMS09-I54 — Specialist recovery cannot silently create duplicate authorized workers or merge incompatible results.

RDMS09-I55 — Incomplete dependency indexes cannot prove absence of affected dependencies.

RDMS09-I56 — Missing observations cannot be interpreted as successful execution.

RDMS09-I57 — Partial operational recovery is legal only within a scope whose relevant shared dependencies are sufficiently validated.

RDMS09-I58 — Recovery source integrity requires a trustworthy verification anchor, not merely a locally editable checksum.

RDMS09-I59 — Credential rotation and session/effect containment are separate claims.

RDMS09-I60 — Recovered content cannot elevate its original instruction authority.

RDMS09-I61 — Partial schema migrations cannot be treated as compatible without explicit compatibility proof.

RDMS09-I62 — Upgrade rollback cannot assume reversal of externally visible effects.

RDMS09-I63 — Sensitive data placement must account for immutable storage and future erasure obligations.

RDMS09-I64 — Erasure completeness claims must include relevant derivatives and known copy domains within declared coverage.

RDMS09-I65 — Backup restoration cannot roll back effective access-suppression obligations.

RDMS09-I66 — Conflicting data-lifecycle obligations require authorized resolution rather than model-generated legal judgment.

RDMS09-I67 — Destructive recovery operations require explicit scope, effect and authority assessment.

RDMS09-I68 — Recovery attempts must follow bounded progress and escalation semantics without fabricating success.

PART XXXIII — CORRECTION MATRIX
Finding	Correction	Status
G01 Recovery modes become shadow authority	§§4–6	ADDRESSED
G02 Concurrent Recovery ownership	§§7–10	ADDRESSED
G03 Snapshot/Ledger inconsistency	§§11–14	ADDRESSED
G04 Durable acknowledgement ambiguity	§§15–18	ADDRESSED
G05 Executive anti-rollback	§§19–22	ADDRESSED
G06 Post-backup actions lost	§§23–26	ADDRESSED
G07 Misleading OutcomeProbe	§§27–30	ADDRESSED
G08 Concurrent reconciliation	§§31–34	ADDRESSED
G09 Compensation failure	§§35–38	ADDRESSED
G10 Orphan process identity	§§39–42	ADDRESSED
G11 Downstream fencing	§§43–45	ADDRESSED
G12 Late results	§§46–48	ADDRESSED
G13 Trigger recovery frontier	§§49–52	ADDRESSED
G14 Specialist recovery duplication	§§53–56	ADDRESSED
G15 Incomplete dependency indexes	§§57–60	ADDRESSED
G16 Missing observations	§§61–64	ADDRESSED
G17 Shared recovery dependencies	§§65–68	ADDRESSED
G18 Compromised backup	§§69–72	ADDRESSED
G19 Credential/session mismatch	§§73–76	ADDRESSED
G20 Recovery prompt injection	§§77–79	ADDRESSED
G21 Mixed schema migration	§§80–83	ADDRESSED
G22 Unsafe upgrade rollback	§§84–86	ADDRESSED
G23 Sensitive immutable metadata	§§87–90	ADDRESSED
G24 Derived/external erasure copies	§§91–94	ADDRESSED
G25 Backup erasure rollback	§§95–98	ADDRESSED
G26 Legal hold conflict	§§99–102	ADDRESSED
G27 Destructive recovery authorization	§§103–106	ADDRESSED
G28 Infinite recovery loop	§§107–111	ADDRESSED
H01–H08	§§112–119	HARDENED
PART XXXIV — C01 VALIDATION REQUIREMENTS

يجب أن تتحقق مراجعة التجميد الثانية من أن كل عقد جديد يحدد:

من يملك السلطة القانونية.

ما الحالة القانونية المتوقعة قبل العملية.

ما الأدلة اللازمة لقبول الانتقال.

ما السلوك عندما تكون الأدلة ناقصة.

كيف تمنع العمليات المتزامنة من التعارض.

كيف يُستعاد القرار بعد Crash.

كيف تمنع التكرار غير القانوني.

كيف تُحفظ حالات العالم الخارجي غير المحسومة.

ما حدود الضمانات التي تستطيع البنية تقديمها.

هل يحافظ العقد على FCA وRDMS-01…08 دون تعديل؟

Critical Review Targets

ينبغي إعطاء أولوية خاصة لمحاولة كسر:

CR09-01 — Authority Anti-Rollback

هل يمكن لنظام استعادة قديم أن يعيد قائدًا فقد سلطته؟

CR09-02 — Lost Dispatch History

هل يمكن تكرار World Action لأن Backup المستعادة لا تعرفها؟

CR09-03 — False Durability

هل يمكن إرسال عملية خارجية بعد acknowledgement لا تصمد أمام Crash؟

CR09-04 — Concurrent Reconciliation

هل يمكن تنفيذ Compensation وإعادة المحاولة في الوقت نفسه؟

CR09-05 — Untrusted Recovery Source

هل يمكن لمهاجم تغيير Backup ومصدر إثبات سلامتها معًا؟

CR09-06 — Erasure Resurrection

هل يمكن استعادة بيانات محظورة من Backup قديمة ثم إفشاؤها؟

CR09-07 — Recovery Shadow Authority

هل يمكن لـRecovery Coordinator تنفيذ أثر خارجي دون ActionGate؟

CR09-08 — Infinite Recovery

هل يمكن أن تستهلك محاولات التعافي جميع الموارد دون وصول إلى حالة قانونية مستقرة؟

PART XXXV — C01 VERDICT
RDMS-09 C01

Original blocking findings:
    28

Corrective contract groups:
    28

Original hardening findings:
    8

Hardening corrections:
    8

Additional proposed invariants:
    RDMS09-I41 ... RDMS09-I68

Changes to FCA:
    NONE PROPOSED

Changes to RDMS-01...08:
    NONE PROPOSED

Code implementation:
    NOT AUTHORIZED

Executable verification:
    NOT PERFORMED

Adversarial Freeze Review 02:
    REQUIRED
Final C01 Decision

RDMS-09 C01 — COMPLETE FOR SECOND ADVERSARIAL REVIEW.

جميع النتائج السابقة أصبحت لها معالجة معمارية مقترحة.

لكن هذا لا يعني إثبات سلامة العقود الجديدة، ولا استيفاءها تلقائيًا لجميع حالات الفشل الممكنة.

RDMS-09 remains NOT FROZEN.

Next Authorized Step: RDMS-09 — Adversarial Freeze Review 02.

ماذا حققنا في C01؟

أرى أن أهم تقدم هنا هو أننا لم نعد نتعامل مع Recovery على أنها عملية تقنية بسيطة لإعادة تشغيل المكونات.

أصبح لدينا فصل واضح بين أربعة أسئلة:

1. هل استعدنا البيانات الصحيحة؟
قد تكون Snapshot قابلة للقراءة، لكن بعض مراجعها مفقودة أو تاريخها غير مكتمل.

2. هل استعدنا السلطة الصحيحة؟
قد تحمل النسخة الاحتياطية Executive Epoch قديمة. استعادة البيانات لا تمنح تلقائيًا صلاحية اتخاذ قرارات جديدة.

3. هل نعرف ما حدث في العالم الخارجي؟
قد تكون عملية Git أو Deployment أو Database Mutation قد نُفذت بينما فقد النظام سجلها. لذلك لا نسمح بإعادة تنفيذها اعتمادًا على غيابها من النسخة المستعادة.

4. هل من القانوني والآمن استئناف العمل؟
حتى بعد إصلاح التخزين واستعادة الذاكرة، يجب التحقق من الاعتماديات والصلاحيات والأحداث غير المحسومة وقيود البيانات الحالية.

القرار المعماري المهم

استعادة حالة البرنامج ≠ استعادة حالة العالم ≠ استعادة السلطة القانونية.

وهذا الفصل سيكون أحد أهم ضمانات سلامة الوكيل عندما يبدأ العمل على مشاريع برمجية حقيقية.

حالة المشروع
Specification	Status
FCA v1.0.1	✅ FROZEN
RDMS-01 → RDMS-08	✅ FROZEN
RDMS-09 Draft v1.0	✅ COMPLETE
RDMS-09 C01	✅ CORRECTIONS COMPLETE
RDMS-09 Freeze Review 02	⏳ NEXT
RDMS-10	⏳ PENDING

الخطوة التالية هي Adversarial Freeze Review 02. سنهاجم العقود الجديدة نفسها، خصوصًا ضمانات استعادة السلطة، وحدود متانة التخزين، وتزامن التعافي، واستعادة البيانات المحذوفة، قبل تقرير ما إذا كانت RDMS-09 جاهزة للتجميد.

END ORIGINAL MESSAGE

========================================================================
SOURCE PART: C02
MESSAGE ID: d59160dd-fa7a-4058-8892-69794f57e9b8
BEGIN ORIGINAL MESSAGE
========================================================================

نواصل الآن إلى RDMS-09 C02 — Recovery Bootstrap, Anti-Rollback & Cross-Domain Safety Closure.

هذه المرحلة تعالج آخر عشر ثغرات كشفها الهجوم العدائي الثاني، وهي من أخطر المسائل في معمارية الوكيل؛ لأنها تتعلق بما يحدث عندما تصبح مصادر السلطة أو التاريخ القانوني أو الأدلة نفسها غير متاحة.

سنعتمد قاعدة حاسمة:

عندما لا يستطيع النظام إثبات سلامة الاستعادة، يجب أن يحافظ على عدم اليقين ويمنع العمليات المتأثرة، بدل اختراع ضمانات لا يستطيع توفيرها.

سأحدد عقود التصحيح وآليات فرضها وحدود ضماناتها، ثم ننتقل إلى مراجعة عدائية ثالثة مستقلة. لن نعلن تجميد RDMS-09 في هذه الخطوة.

RDMS-09 C02 — Recovery Bootstrap, Anti-Rollback & Cross-Domain Safety Closure
RDMS-09 C02
Recovery Bootstrap, Anti-Rollback & Cross-Domain Safety Closure

Specification: RDMS-09
Parent: RDMS-09 Draft v1.0 + C01
Review source: Adversarial Freeze Review 02
Findings: FR09-R2-G01…G10 / FR09-R2-H01…H05

Parent Architecture: FCA v1.0.1 — FROZEN
Dependencies: RDMS-01…08 — FROZEN

Status: C02 — CORRECTIVE SPECIFICATION
Implementation Authorization: NO
Next Gate: Adversarial Freeze Review 03

PART I — ARCHITECTURAL OBJECTIVE
1. Purpose

تهدف C02 إلى إغلاق الثغرات المتعلقة بالاستعادة عندما تصبح المعلومات اللازمة لاتخاذ قرار آمن غير متاحة، أو عندما تكون هناك عدة مصادر للسلطة أو التاريخ أو البيانات يجب التحقق من توافقها.

تركز التصحيحات على عشرة مجالات:

بدء التعافي عندما تكون Control Plane غير متاحة.

منع استعادة أجيال قديمة من السلطة والسياسات.

التعامل مع فقدان تاريخ عمليات العالم الخارجي.

منع تعارض العمليات القديمة مع عمليات التعافي الجديدة.

عزل الملفات المستعادة قبل تنفيذها.

منع إفشاء البيانات المحذوفة أثناء التعافي.

الحفاظ على تفسير موحد للحالة أثناء Schema Migration.

منع استعمال تصريحات Recovery فقدت صلاحيتها.

ضمان استمرار متابعة الالتزامات المعلقة.

تحديد حدود ضمانات متانة التخزين.

2. Fundamental Recovery Principle

نثبت المبدأ التالي:

Recovery must establish sufficient authority, integrity and effect knowledge before permitting dependent continuation.

بالعربية:

يجب أن تثبت الاستعادة قدرًا كافيًا من سلامة السلطة والبيانات والأدلة المتعلقة بالآثار الخارجية، قبل السماح باستمرار العمليات التي تعتمد عليها.

لكن كلمة كافٍ هنا مرتبطة بالنطاق.

فقد يستطيع النظام استئناف مهمة قراءة مستقلة، بينما يمنع عملية نشر أو دفع غير محسومة.

لا نطلب استعادة العالم كله قبل السماح بأي نشاط آمن.

3. Three Independent Recovery Questions

كل قرار باستئناف العمل يجب أن يجيب عن ثلاثة أسئلة منفصلة:

A. AUTHORITY

Who is legally authorized to act now?

B. CANONICAL STATE

Which cognitive/control state is valid?

C. EXTERNAL REALITY

What effects are known, unknown,
or potentially still in flight?

ولا يجوز استنتاج الإجابة عن أحدها من الإجابة عن الآخر.

4. Recovery Cannot Create Truth

يجب أن يظل النظام قادرًا على تمثيل:

KNOWN
UNKNOWN
CONTRADICTED
INCOMPLETE
UNVERIFIABLE

بوصفها نتائج تقييم، دون استخدامها كبدائل غير قانونية لحالات RDMS-01…08.

إذا فقدت جميع المصادر القادرة على إثبات حدث ما، فلا يمكن للتعافي إعادة اختراع ذلك الحدث.

قد تظل النتيجة النهائية:

RECOVERY INCOMPLETE

Affected operations:
    BLOCKED

External effects:
    IN_DOUBT where applicable

وهذه نتيجة قانونية مقبولة.

PART II — C02-A: RECOVERY BOOTSTRAP AUTHORITY
5. Finding

FR09-R2-G01 — Recovery Bootstrap Authority Paradox

المشكلة

إذا أصبحت Control Ledger غير متاحة، فقد تتعذر استعادة Executive الحالية.

لكن بعض عمليات إصلاح Control Ledger قد تتطلب إجراءات تشغيلية على البنية التحتية.

لا يجوز حل المشكلة بمنح Recovery Coordinator سلطة تنفيذية مستقلة.

6. Architectural Decision

نعتمد فصلًا بين:

Infrastructure Restoration

إعادة إتاحة البنية التي تحفظ وتفرض السلطة القانونية.

و:

Canonical Agent Continuation

استئناف الوكيل لاتخاذ قرارات معرفية وتنفيذ عمليات ضمن المشروع.

يمكن أن تحدث الأولى قبل استعادة Executive، ولكن ضمن حدود تشغيلية خارجية موثوقة ومحددة مسبقًا.

أما الثانية فلا يمكن أن تبدأ قبل استعادة السلطة القانونية.

7. RecoveryBootstrapContract
RecoveryBootstrapContract {
    bootstrap_case_id

    affected_project_scope

    unavailable_control_components[]

    trusted_bootstrap_source_refs[]

    recovery_principal_ref

    principal_authority_proof_ref

    permitted_infrastructure_operations[]

    prohibited_project_operations[]

    source_integrity_requirements[]

    destination_integrity_requirements[]

    bootstrap_generation

    bootstrap_audit_receipts[]

    canonical_handoff_requirements[]

    bootstrap_disposition
}
8. Bootstrap Principal

Recovery Principal ليست Cognitive Executive جديدة.

هي جهة تشغيلية موثوقة ومحددة السلطة، مثل مشغل بنية تحتية مفوض وفق سياسة الاستعادة.

قد تكون الجهة بشرية أو آلية بنية تحتية ذات تفويض مسبق ومستقل عن حالة الوكيل المعطلة.

لكنها لا تملك:

Canonical Decision Acceptance

Goal Mutation Authority

Memory Promotion Authority

Project Action Authorization

Specialist Recruitment Authority

بمجرد كونها مسؤولة عن استعادة البنية التحتية.

9. Bootstrap Scope

يمكن أن يسمح بروتوكول Bootstrap، ضمن التفويض التشغيلي الصحيح، بعمليات مثل:

Restore a trusted Control Ledger replica.

Recover required storage availability.

Restore a verified control snapshot.

Recover control-plane encryption material
through authorized infrastructure procedures.

Restore availability of the leadership service.

لا يسمح تلقائيًا بـ:

Deploy project code.

Reset customer databases.

Modify the canonical repository.

Approve a new engineering decision.

Retry an unresolved external Action.

أي عملية مشروع جديدة تخضع إلى FCA ومساراتها القانونية بعد استعادة السلطة.

10. Important Authority Boundary

إذا كان نظام الوكيل نفسه هو من يريد تنفيذ عملية ذات أثر خارجي، فلا يمكنه تجاوز ActionGate بتسميتها Bootstrap.

أما الصيانة الإدارية خارج الوكيل، التي تنفذها جهة مخولة وفق حوكمة البنية التحتية، فهي افتراض تشغيلي خارجي يجب توثيقه والتحقق من آثاره عند استعادة النظام.

لا تستخدم RDMS-09 هذا الاستثناء لتوسيع سلطة الوكيل.

11. Bootstrap Procedure
CONTROL PLANE UNAVAILABLE
          ↓
Restrict new agent effects
          ↓
Identify trusted recovery principal
          ↓
Validate bootstrap authorization
          ↓
Restore authority infrastructure
          ↓
Validate recovered state
          ↓
Replay required Control Ledger state
          ↓
Recover current Executive authority
          ↓
Reconcile world effects
          ↓
Evaluate scoped operational admission

لا يجوز أن يصبح نجاح استعادة التخزين وحده تصريحًا بالانتقال إلى NORMAL.

12. Bootstrap Failure

إذا لم تتوفر جهة استعادة موثوقة، أو لم يمكن إثبات سلامة مصدر الاستعادة:

bootstrap_disposition =
    AUTHORITY_UNAVAILABLE

تبقى العمليات المعرفية ذات الآثار القانونية والعمليات الخارجية الجديدة محجوبة.

لا نسمح لـLLM بتوليد تفويض بديل.

13. Bootstrap Idempotency

يجب أن تمتلك عملية Bootstrap هوية مستقرة ومراجع تدقيق، وأن تكون خطواتها قابلة للاستئناف أو التمييز بوضوح بين ما نُفذ وما لم يُنفذ.

عندما تتضمن خطوة بنية تحتية أثرًا غير قابل للتكرار الآمن، لا يجوز إعادة تنفيذها تلقائيًا دون تحديد نتيجتها.

لا نفترض أن جميع عمليات صيانة البنية التحتية idempotent.

PART III — C02-A: UNIFIED ANTI-ROLLBACK FRONTIER
14. Finding

FR09-R2-G02 — Anti-Rollback Protection Is Not Unified

المشكلة

قد تستعيد المنظومة Executive Epoch حديثة بينما تستعمل سياسة أمنية أو سياسة حذف بيانات قديمة.

ونتيجة ذلك وجود سلطة تنفيذ صحيحة فوق مجموعة قيود لم تعد صالحة.

15. RecoveryAuthorityFrontier
RecoveryAuthorityFrontier {
    project_or_domain_ref

    executive_epoch_frontier

    canonical_control_frontier

    control_policy_frontier

    security_policy_frontier

    data_suppression_frontier

    schema_visibility_frontier

    trusted_source_refs[]

    frontier_validation_results[]

    cross_frontier_compatibility

    unresolved_frontier_gaps[]
}

هذه البنية تقييم تجميعي لمراجع سلطة موجودة.

ليست مصدرًا جديدًا للحقيقة أو دفترًا موازيًا لـControl Ledger.

16. Authority Frontier Rules

يجب فحص:

Current Executive Epoch
        +
Current Security Policy
        +
Current Data Suppression Obligations
        +
Current Canonical Schema View
        +
Current Control State

قبل استئناف عملية تعتمد على جميع هذه العناصر.

17. Compatibility Requirement

لا يكفي أن تكون كل Frontier صحيحة منفردة.

يجب التأكد من أن مجموعة Frontiers متوافقة.

مثال:

Executive Epoch:
    105

Security Policy:
    v8

Erasure Policy:
    v4

Canonical Schema:
    v3

هذه المجموعة ليست بالضرورة قانونية.

يجب التحقق من أن الإصدارات النافذة صالحة للتعايش وفق تاريخ التحكم ومراجع السياسة المعتمدة.

18. Anti-Rollback Decision
Frontier Assessment
        ↓
Verify trusted source generations
        ↓
Verify required compatibility
        ↓
Identify unresolved gaps
        ↓
Admit operation scope
or
Restrict affected scope
19. Unknown Frontier

إذا كانت سياسة حذف البيانات الأحدث غير قابلة للاسترجاع، فلا يجوز افتراض أن السياسة الموجودة داخل Backup القديمة هي الأحدث.

يجب حجب الاسترجاع أو الإفصاح الذي يتطلب إثبات صلاحية السياسة.

وينطبق المنطق نفسه على القيود الأمنية والسلطات التي يمكن أن تكون قد تغيرت.

20. No Global Atomicity Assumption

قد تكون مصادر Frontiers موزعة على أنظمة مختلفة.

لا نفترض وجود معاملة ذرية واحدة بينها جميعًا.

إذا لم توجد آلية تثبت Snapshot متوافقة، يجب استخدام مراجعة حالة موثوقة عند حدود العمليات القانونية.

لا نضيف Global Consensus Engine ثانية.

PART IV — C02-A: DURABILITY FAILURE MODEL
21. Finding

FR09-R2-G10 — Durable Acknowledgement Requires an Explicit Failure Model

المشكلة

قد تكون الكتابة متينة أمام انهيار Process، لكنها لا تصمد أمام فقدان القرص أو فقدان جميع Replicas.

لذلك فإن كلمة Durable وحدها غير كافية.

22. DurabilityFailureModel
DurabilityFailureModel {
    model_id

    protected_control_scope

    storage_backend_ref

    assumed_failure_domains[]

    tolerated_failure_classes[]

    excluded_failure_classes[]

    acknowledgement_contract

    write_ordering_guarantees

    failover_consistency_requirements

    recovery_evidence_requirements[]

    validation_test_refs[]

    declared_limitations[]
}
23. Durability Classes

لا نفرض تصنيفًا عالميًا واحدًا.

لكن يجب تحديد ضمانات فعلية مثل:

Process crash survival

Operating-system crash survival

Power-loss survival

Storage-device failure survival

Replica failure survival

Network partition behavior

Site disaster survival

كل ضمان يجب أن يستند إلى خصائص backend وإعداداته واختبارات مناسبة.

24. Write-Ahead Enforcement

يظل القانون المجمد:

Persist DISPATCH_INTENT
        ↓
Receive valid durable acknowledgement
        ↓
Only then dispatch SHARED_WORLD action

ولا يجوز أن تتحول:

Write accepted into volatile buffer

إلى:

Durability confirmed

إذا كان نموذج الفشل المعتمد يشترط متانة أقوى.

25. Storage Failover

إذا كان backend موزعًا، يجب تحديد شروط:

Authoritative writer selection

Acknowledged commit preservation

Replica promotion

Split-brain rejection

Ordered event replay

ويجب ألا يؤدي Failover إلى إخفاء كتابة جرى الاعتراف بمتانتها ضمن نموذج الضمان المعلن.

26. Out-of-Model Disaster

إذا وقع عطل خارج نطاق الضمان المثبت:

Durability guarantee no longer sufficient.

لا يعني ذلك افتراض ضياع جميع البيانات.

لكنه يمنع اعتبار سلامة التاريخ مثبتة دون مراجعة أو استعادة مناسبة.

27. Verification Requirement

لا تُقبل ضمانات المتانة اعتمادًا على اسم محرك التخزين أو مواصفاته التسويقية فقط.

يجب أن تتضمن خطة التنفيذ المستقبلية Failure Injection واختبارات إعدادات التخزين الفعلية.

PART V — C02-B: EXTERNAL HISTORY COVERAGE
28. Finding

FR09-R2-G03 — Post-Backup Action History Cannot Always Be Reconstructed

المشكلة

قد تختفي Action من النسخة المستعادة رغم أنها نُفذت في العالم الخارجي.

والأخطر أن النظام ربما فقد معرفها أيضًا.

29. ExternalHistoryCoverageProof
ExternalHistoryCoverageProof {
    coverage_id

    restored_control_frontier

    affected_effect_domains[]

    possible_dispatch_interval

    independent_history_source_refs[]

    independent_operation_identity_sources[]

    authoritative_query_scope[]

    proven_covered_scope[]

    unverifiable_scope[]

    coverage_result:
        COMPLETE_WITHIN_SCOPE
        PARTIAL
        UNKNOWN

    supporting_evidence_refs[]
}
30. Completeness Is a Positive Claim

يجب التمييز بين:

Search returned zero operations.

و:

The authoritative source proves
that no operations occurred
within the declared scope.

الأولى Observation لنتيجة البحث.

الثانية استنتاج يحتاج إثبات اكتمال المصدر ونطاق البحث.

31. Recovery Coverage Dimensions

يجب تقييم التغطية عبر:

Time interval

Resource scope

External service

Operation identity

Effect class

Available history retention

Source consistency

إذا أثبتنا اكتمال سجل خدمة Deployment، فهذا لا يثبت اكتمال سجل العمليات المالية لخدمة أخرى.

32. Lost Identity Problem

إذا فقد النظام معرف عملية خارجية محتملة، يجب فحص ما إذا كان المصدر الخارجي يستطيع تقديم تاريخ كامل لنطاق التأثير.

إذا لم يستطع، فلا يجوز استنتاج أن العملية لم تحدث.

33. Conflicting Continuation Rule

إذا كان:

History coverage = UNKNOWN

وكانت عملية جديدة قد تكرر أثرًا غير قابل للتكرار الآمن، فإن:

Conflicting operation = BLOCKED

إلى أن تتوفر أدلة أو إجراء قانوني قادر على معالجة الخطر.

34. Independent Dispatch Evidence

ينبغي في تصميم التنفيذ اعتماد وسائل مناسبة لتقليل احتمالات فقدان تاريخ العمليات، مثل:

Durable Action Journal

Stable external operation identities

External idempotency keys

Independent effect receipts

Authoritative outcome probes

لكن RDMS-09 لا تفترض أن كل خدمة خارجية تدعم هذه الإمكانات.

35. No Exactly-Once Promise

لا يمكن ضمان Exactly-Once External Effects عمومًا إذا كانت الأنظمة الخارجية لا تدعم بروتوكولًا ملائمًا، أو إذا ضاع التاريخ اللازم للتمييز بين المحاولة الأولى والثانية.

لذلك يبقى الهدف:

منع التكرار غير المبرر والمحافظة على عدم اليقين عندما يستحيل حسمه.

PART VI — C02-B: DISPATCH QUIESCENCE AND CUTOVER
36. Finding

FR09-R2-G04 — Downstream Fencing and Dispatch Cutover Race

المشكلة

قد تفقد Executive القديمة سلطتها، لكن Worker قديمة ما زالت قادرة على إرسال طلب سبق تفويضه.

وفي الوقت نفسه قد تبدأ Recovery جديدة إعادة المحاولة أو التعويض.

37. DispatchQuiescenceAssessment
DispatchQuiescenceAssessment {
    assessment_id

    affected_action_refs[]

    old_execution_generations[]

    current_execution_generation

    enforceable_dispatch_fences[]

    dispatcher_stop_evidence_refs[]

    active_session_refs[]

    potentially_inflight_effect_refs[]

    unresolved_dispatch_intents[]

    conflicting_action_restrictions[]

    quiescence_status:
        PROVEN_FOR_SCOPE
        NOT_PROVEN
        UNKNOWN
}
38. Dispatch Cutover Principle

نميز بين:

Authority fencing

و:

Dispatcher fencing

و:

External-effect completion

هذه ثلاثة أمور مختلفة.

39. Pre-Dispatch Guard

قبل أن ترسل Execution Boundary عملية مشتركة جديدة، يجب التحقق من شروط التفويض الحالية التي تفرضها RDMS-01 وRDMS-04.

ومن ضمنها صلاحية جيل التنفيذ عندما يكون ذلك مطلوبًا.

40. Previously Committed Dispatch

إذا كانت Action تحمل DISPATCH_INTENT قديمة، فلا يجوز استنتاج أنها لم تُرسل.

وقد تكون:

Not yet transmitted

Currently transmitting

Already transmitted

Externally completed

Externally pending

يجب أن يعامل Recovery هذه الاحتمالات وفق RDMS-04.

41. Quiescence Requirement

قبل تنفيذ عملية قد تتعارض مع أثر قديم، يجب إثبات أحد الشروط:

A. Old dispatch path can no longer
   produce conflicting effects.

OR

B. Old effects are sufficiently known
   and reconciled.

OR

C. Proposed new operation is safe
   under every still-possible old effect.

إذا تعذر إثبات أي شرط:

Conflicting continuation prohibited.
42. Late Dispatch Problem

قد ترسل Worker قديمة طلبًا قبل فقدان سلطة التنفيذ مباشرة، ويصل إلى النظام الخارجي بعد ذلك.

حتى لو توقف Worker المحلي، لا يمكن افتراض اختفاء الطلب من الشبكة أو توقف المعالجة الخارجية.

لهذا لا تعني Quiescence المحلية بالضرورة اكتمال أثر العالم الخارجي.

43. Compensation Interaction

لا يجوز تنفيذ Compensation اعتمادًا فقط على إثبات أن Worker القديمة توقفت.

يجب معرفة ما يكفي عن الأثر الخارجي، أو إثبات أن Compensation مناسبة وآمنة تحت جميع الحالات الممكنة ذات الصلة.

44. Irreducible Uncertainty

إذا كان النظام الخارجي لا يدعم Fencing أو إلغاء العمليات المرسلة أو الاستعلام الحاسم عن النتائج، فقد لا يمكن تحقيق Quiescence شاملة.

في هذه الحالة لا نختلق ضمانًا.

تبقى آثار العمليات غير المحسومة تحت RDMS-04، وتُحجب العمليات المتعارضة.

PART VII — C02-C: RESTORE-TIME QUARANTINE
45. Finding

FR09-R2-G05 — Recovered Artifacts May Execute Before Trust Validation

المشكلة

قد تستعيد المنظومة ملفات قابلة للتنفيذ تعرضت للتلاعب.

إذا بدأت الخدمات قبل التحقق من الملفات، فقد تعمل Scripts ضارة داخل Recovery نفسها.

46. RecoveryArtifactQuarantine
RecoveryArtifactQuarantine {
    quarantine_id

    recovery_source_ref

    restored_artifact_refs[]

    executable_artifact_refs[]

    configuration_artifact_refs[]

    known_indirect_execution_paths[]

    trust_verification_status

    permitted_inspection_operations[]

    prohibited_execution_operations[]

    containment_proof_ref

    release_authorization_ref?
}
47. Quarantine Must Precede Activation
Restore into controlled environment
        ↓
Disable automatic execution
        ↓
Validate trusted source
        ↓
Inspect executable content
        ↓
Validate configuration
        ↓
Validate schema compatibility
        ↓
Determine legal release scope
        ↓
Authorize activation
48. Restore-Time Forbidden Operations

قبل اكتمال شروط الثقة اللازمة، لا يجوز تشغيل:

Restored startup scripts

Unverified plugins

Project build hooks

Package-manager lifecycle scripts

Recovered agent tool adapters

Unverified recovery automation

عندما تكون هذه العمليات قادرة على إحداث آثار غير مأذون بها.

49. Data That Becomes Executable

يجب الانتباه إلى أن بعض الملفات ليست Executables تقليدية، لكنها قد تتحكم في تنفيذ لاحق.

مثل:

Build configuration

Plugin manifests

CI workflow files

Dependency installation scripts

Tool configuration

Project-specific commands

لا يجوز اعتبارها آمنة لمجرد امتداد الملف.

50. Trusted Inspection

يجب تنفيذ فحوص السلامة باستخدام أدوات وبيئة يثبت أنها لا تعتمد على تنفيذ المحتوى المشكوك فيه بطريقة تمنحه تأثيرًا غير مصرح.

إذا تطلب الفحص تشغيل محتوى غير موثوق، يجب أن يجري ذلك ضمن احتواء مناسب وتصنيف قانوني للأثر.

51. Failed Quarantine

إذا لم يمكن إثبات السلامة:

Artifact release = DENIED

يمكن الاحتفاظ بالمحتوى للتحقيق حسب السياسة، لكن لا يجوز تفعيله تلقائيًا.

PART VIII — C02-C: RECOVERY DISCLOSURE BARRIER
52. Finding

FR09-R2-G06 — Erasure Suppression Is Not Enforced Across Every Recovery Exposure Path

المشكلة

يمكن أن يؤدي Restore إلى إعادة بيانات محذوفة مؤقتًا.

وقد تصل هذه البيانات إلى Provider أو Specialist أو تقرير تشخيصي قبل تطبيق حظر Retrieval.

53. RecoveryDisclosureBarrier
RecoveryDisclosureBarrier {
    barrier_id

    restored_data_scope

    applicable_suppression_frontier

    authorized_processing_scope

    prohibited_disclosure_scope[]

    protected_processing_paths[]

    protected_indexing_paths[]

    protected_provider_paths[]

    protected_specialist_paths[]

    protected_export_paths[]

    effective_policy_version

    barrier_enforcement_status

    release_authorization_ref?
}
54. Suppression Before Disclosure

يجب أن يكون الترتيب:

Restore data into restricted scope
        ↓
Recover current suppression obligations
        ↓
Apply disclosure barrier
        ↓
Determine permitted processing
        ↓
Reapply required erasure/suppression
        ↓
Authorize permitted release

لا يجوز إرسال البيانات إلى LLM أولًا ثم فحص سياسة حذفها لاحقًا.

55. Covered Exposure Paths

تشمل القيود:

Memory retrieval

Context construction

External LLM requests

Specialist context packages

Search result materialization

Diagnostic reports

Human-facing output

Artifact export

Debug logs

Derived summaries
56. Necessary Internal Processing

قد تحتاج Recovery إلى قراءة بعض البيانات لتحديد ما يجب حذفه.

هذا لا يمنح تصريحًا بالإفصاح عنها خارج النطاق المسموح.

يجب أن تكون المعالجة:

محدودة الغرض.

محكومة الصلاحيات.

قابلة للتدقيق.

لا تسمح بالاستعمال المعرفي أو الخارجي غير المصرح.

57. Missing Suppression Frontier

إذا تعذر إثبات سياسة الحذف النافذة:

Disclosure eligibility = UNKNOWN

ويجب منع الإفصاح الذي يعتمد على هذا الإثبات.

لا يجوز استعمال سياسة Backup القديمة بوصفها السياسة الحالية دون تحقق.

58. Derived Data

قد تكون البيانات المحذوفة موجودة داخل Summary أو Memory مشتقة.

يجب استخدام Lineage وحوكمة RDMS-07 لتحديد المشتقات المتأثرة.

ولا يُسمح بإعادة بناء الفهارس ثم كشف محتوياتها قبل تطبيق القيود المطلوبة.

59. External Provider Boundary

إذا كان المحتوى قد أُرسل بالفعل إلى مزود خارجي قبل اكتشاف الحادث، فلا يجوز إعلان أن تطبيق حظر محلي أزال النسخة الخارجية.

تُوثق حدود التحكم والتحقق من الإزالة وفق Data Lifecycle Governance.

PART IX — C02-D: CANONICAL SCHEMA VISIBILITY
60. Finding

FR09-R2-G07 — Schema Migration Has No Fully Defined Canonical Visibility Boundary

المشكلة

قد تعيد Migration جزئية إنتاج حالة يكون جزء منها قابلًا للتفسير وفق Schema v2 وجزء آخر وفق v3.

وقد يؤدي اختلاف القراء إلى قرارات قانونية متناقضة.

61. CanonicalSchemaVisibilityContract
CanonicalSchemaVisibilityContract {
    migration_ref

    source_schema_version

    target_schema_version

    authoritative_schema_view

    allowed_reader_versions[]

    allowed_writer_versions[]

    compatibility_proof_refs[]

    migration_commit_boundary

    canonical_visibility_generation

    reference_consistency_requirements[]

    rollback_conditions[]

    forward_recovery_conditions[]
}
62. Single Authoritative Meaning

يمكن تخزين البيانات ماديًا بأشكال متعددة خلال Migration.

لكن يجب ألا يكون هناك تفسيران قانونيان متناقضان للحالة Canonical نفسها.

التمثيلات الانتقالية لا تكتسب السلطة لمجرد وجودها على القرص.

63. Migration Visibility Phases

نقترح:

PREPARE

    Build target representation.

VALIDATE

    Prove required compatibility and integrity.

CUTOVER

    Commit authoritative schema visibility.

CLEANUP

    Retire obsolete derived representations
    when legally allowed.

هذه مراحل ضمن Migration Protocol وليست حالات جديدة ضمن Cognitive Executive.

64. Atomic Cutover Requirement

إذا كان تبديل التفسير القانوني يعتمد على عدة مراجع يجب أن تصبح نافذة معًا، فيجب أن يحترم Cutover حدود الذرية القانونية في RDMS-01.

لا يجوز إعلان Schema الجديدة Canonical بينما تبقى بعض المراجع المطلوبة غير معتمدة.

65. Mixed-Version Readers

يُسمح للقراء القدماء والجدد بالتعايش فقط عندما يثبت أن ذلك لا يغير معنى الحالة المعتمدة أو يؤدي إلى تفسير خاطئ.

66. Writer Compatibility

لا يكفي أن يتمكن Reader قديم من قراءة جزء من Schema الجديدة.

يجب تحديد هل يستطيع Writer القديم الكتابة بصورة تحفظ القوانين والمعنى والنسخ.

إذا لم يثبت ذلك:

Old writer = FENCED

بالنسبة إلى النطاق غير المتوافق.

67. Crash Before Cutover

إذا تعطل النظام قبل اعتماد Cutover:

Authoritative schema remains
the previously committed view.

وفق بروتوكول Migration المنطبق.

ولا يجوز اعتبار الملفات التي حُولت جزئيًا تفسيرًا قانونيًا جديدًا.

68. Crash After Cutover

إذا اعتمد Cutover ثم حدث Crash:

Recovery must restore the committed
authoritative view.

ولا يجوز العودة بصمت إلى Schema قديمة إذا أدى ذلك إلى إعادة تفسير أحداث اعتمدت وفق الجديدة.

69. Unknown Visibility State

إذا فقد النظام الأدلة اللازمة لتحديد Schema المعتمدة:

Canonical interpretation = UNKNOWN

يجب حجب العمليات التي تعتمد على تفسير غير مثبت.

PART X — C02-D: VERSION-BOUND RECOVERY ADMISSION
70. Finding

FR09-R2-G08 — Recovery Admission Is Vulnerable to TOCTOU

المشكلة

قد تجتاز عملية Recovery فحص السلامة، ثم تتغير الاعتماديات أو السياسات قبل تنفيذ العملية التالية.

71. RecoveryAdmissionBinding
RecoveryAdmissionBinding {
    admission_id

    recovery_case_ref

    admitted_project_scope

    admitted_operation_classes[]

    current_executive_epoch

    canonical_state_frontier

    policy_frontier

    dependency_frontier

    security_frontier

    suppression_frontier

    unresolved_action_constraints[]

    admission_generation

    invalidation_conditions[]

    admission_integrity_ref
}
72. Admission Is Scoped

لا تعني:

Project status = NORMAL

أن كل عملية يمكن تنفيذها دون فحص جديد.

بل يعني أن المشروع اجتاز شروط العودة إلى النطاق التشغيلي المحدد عند نقطة معينة.

73. Admission Revalidation

عند حدود العملية القانونية، يجب التأكد من صلاحية:

Executive authority

Required policies

Relevant dependencies

Security restrictions

Unresolved action constraints

حسب طبيعة العملية.

لا نعيد كل فحوص Recovery العالمية عند كل عملية صغيرة.

لكننا نعيد التحقق من الشروط المؤثرة التي قد تكون تغيرت.

74. Admission Invalidation

قد تبطل صلاحية Admission عند:

Executive epoch change

Relevant policy change

Security incident

New IN_DOUBT effect

Dependency invalidation

Schema visibility change

Erasure restriction update

تستخدم Dependency Engine وآليات الأحداث المجمدة لتحديد التأثير.

ولا ننشئ محرك صلاحية ثانويًا مستقلًا.

75. Concurrent Admission and Revocation

إذا صدر حدث يغيّر أهلية التشغيل بالتزامن مع Action جديدة، يجب أن تحدد حدود CommitGate/ActionGate الترتيب القانوني المناسب.

إذا كانت Action قد أُرسلت بالفعل، فلا يجوز التعامل مع إبطال Admission بوصفه إلغاءً تلقائيًا للأثر.

تظل RDMS-04 مسؤولة عن Reconciliation.

76. Degraded Admission

يمكن أن تكون النتيجة:

READ_ONLY_OPERATIONS:
    ALLOWED

ISOLATED_DIAGNOSTICS:
    ALLOWED

SHARED_WORLD_MUTATION:
    BLOCKED

إذا كانت الأدلة تسمح بهذا الفصل.

لا يلزم اعتبار النظام كله NORMAL أو كله FAILED دون خيارات وسطية محكومة.

PART XI — C02-E: DURABLE SUSPENDED RECOVERY
77. Finding

FR09-R2-G09 — Trigger Recovery and Suspended Obligation Liveness

المشكلة

قد يبقى أثر خارجي غير محسوم، ثم تُعلق المهمة بسبب تعطل الخدمة الخارجية.

إذا لم توجد آلية استئناف متينة، قد تُنسى مسؤولية التسوية.

78. RecoverySuspensionCommitment
RecoverySuspensionCommitment {
    commitment_id

    recovery_case_ref

    unresolved_obligation_refs[]

    blocked_goal_refs[]

    dependent_action_refs[]

    suspension_reason

    required_reactivation_conditions[]

    durable_trigger_refs[]

    responsible_authority_ref

    escalation_conditions[]

    suspension_commit_ref
}
79. Suspension Is Not Obligation Removal

إذا كانت:

Action X = IN_DOUBT

ثم دخلت المهمة:

SUSPEND

فيجب أن تظل Action X غير محسومة.

ولا يسمح بتفسير تعليق المهمة باعتباره تسوية للأثر.

80. Durable Reactivation

عندما يعتمد الاستئناف على حدث مستقبلي:

External service available

Human decision received

Required artifact restored

New authoritative observation

يجب أن توجد آلية تفعيل قانونية مناسبة وفق RDMS-05.

81. Atomic Suspension Requirements

إذا كان حفظ حالة التعليق وتسجيل التزام إعادة التفعيل مطلوبين معًا للتعافي، يجب اعتمادهما ذريًا وفق Control Ledger.

لا يجوز الوصول إلى حالة:

Goal suspended
+
No durable recovery obligation
+
No authorized reactivation path

عندما تكون إعادة التفعيل إلزامية.

82. Recovery Trigger Ordering

نحدد:

TriggerRecoveryOrdering {
    trigger_ref

    trigger_generation

    source_event_identity

    source_cursor

    canonical_reaction_identity

    reaction_commit_ref?

    deduplication_key

    replay_requirement

    ordering_contract_ref
}
83. Source Cursor vs Reaction Commit

يجب الفصل بين:

Event observed

و:

Canonical reaction committed

إذا قُرئ حدث ثم وقع Crash قبل اعتماد رد الفعل، يجب ألا يؤدي تقدم Cursor إلى فقدان الحدث بصورة نهائية.

84. At-Least-Once Detection

إذا كان المصدر يعيد تسليم الأحداث، يجب أن يستطيع RDMS-05 إزالة التكرار عند اعتماد التفاعل القانوني.

لا نحتاج إلى Exactly-Once Event Delivery كي نمنع تكرار Canonical Reaction، طالما تحافظ آليات الهوية والذرية وإزالة التكرار على ضماناتها.

85. Non-Replayable Sources

إذا كان المصدر غير قادر على إثبات حدوث Edge أثناء Downtime، فلا يجوز اختراع الحدث.

يمكن أن تحتاج المهمة إلى:

Manual revalidation

Alternative authoritative probe

Human intervention

حسب متطلباتها.

يجب أن يبقى عدم اليقين واضحًا.

86. Recovery Reactivation Failure

إذا فشلت Trigger أو آلية إعادة التفعيل، يجب أن تبقى Recovery Obligation قابلة للاكتشاف في الحالة المتينة.

ولا يجوز الاعتماد على ذاكرة LLM لإعادة تذكرها.

PART XII — CROSS-DOMAIN ENFORCEMENT
87. Recovery Safety Barrier

تتطلب عملية العودة إلى العمل تقييمًا منسقًا للعناصر ذات الصلة.

Canonical State
      +
Current Authority
      +
Applicable Policies
      +
Dependency Freshness
      +
External Effect Constraints
      +
Data Disclosure Restrictions
      ↓
Scoped Recovery Admission

لا يعني ذلك وجود Global Recovery Gate جديدة تملك السلطة القانونية.

بل هو عقد تقييم تنفذه المكونات المالكة للشروط ضمن حدودها المجمدة.

88. No Shadow Authority

لا تستطيع RDMS-09:

Accept an engineering Decision

Modify a Goal directly

Dispatch an arbitrary world Action

Promote a Memory

Override a hard invariant

من خلال RecoveryCase أو RecoveryAdmissionBinding.

89. Fail-Closed Scope

إذا كان شرط إلزامي غير قابل للإثبات، يجب حجب العمليات التي تعتمد عليه.

لا نستخدم قاعدة:

Any unknown → Stop everything.

بل:

Unknown mandatory condition
        ↓
Identify affected operational scope
        ↓
Block dependent operations
        ↓
Permit independently safe operations

عندما توجد أدلة كافية للفصل.

90. Recovery Uncertainty Is Persistent

لا يجوز أن يختفي عدم اليقين لمجرد:

Process restart

Provider replacement

Snapshot reload

Timeout expiry

Human-readable summary generation

أي تغيير في الحالة المعتمدة يحتاج إلى الأدلة والمسار القانوني المناسبين.

PART XIII — HARDENING CORRECTIONS
91. R2-H01 — Recovery Priority and Backpressure

يجب ترتيب أعمال التعافي وفق:

Safety urgency

Potential irreversible effects

Dependency blocking impact

Evidence availability

Resource constraints

يمكن تقييد عدد عمليات Reconciliation أو الفحص المتزامنة لتجنب إغراق الخدمات.

لكن لا يجوز إسقاط الالتزامات لمجرد تأجيلها.

تظل RDMS-05 مسؤولة عن الجدولة الزمنية القانونية.

92. R2-H02 — Recovery Test Dimensions

يجب أن توثق اختبارات الأعطال:

Failure injection point

Pre-failure canonical frontier

Executive epoch

Action lifecycle

Durability guarantees

Potential world effects

Expected recovery outcome

Actual observations

Invariant verdict

لا يكفي قياس أن العملية أعادت التشغيل.

93. R2-H03 — Configuration Drift

نقترح:

RecoveryConfigurationBinding {
    storage_configuration_ref

    runtime_configuration_ref

    security_configuration_ref

    schema_configuration_ref

    effective_version_refs[]

    compatibility_assessment
}

إذا تغيرت إعدادات التخزين أو Runtime بصورة تؤثر في ضمانات Recovery، يجب إعادة تقييم الادعاءات المرتبطة بها.

94. R2-H04 — Sensitive Recovery Receipts

قد تحتوي Recovery Receipts على:

Resource identifiers

Sensitive paths

External service metadata

Potentially identifying details

Security configuration

تخضع هذه البيانات إلى سياسات التخزين والإفصاح المناسبة.

ولا يجوز افتراض أن جميع Metadata غير حساسة.

95. R2-H05 — Human Escalation

نقترح:

HumanRecoveryEscalation {
    recovery_case_ref

    known_state_summary

    unresolved_world_effects[]

    blocked_operation_scope

    required_authority_domain

    safe_available_options[]

    forbidden_assumptions[]

    supporting_evidence_refs[]
}

عند طلب تدخل بشري، يجب توضيح ما هو معروف وما هو مجهول.

ولا يجوز أن يصبح النص الذي تنتجه LLM تفويضًا بشريًا.

PART XIV — ADDITIONAL FORMAL INVARIANTS

تضاف الثوابت التالية إلى RDMS09-I01…I68.

RDMS09-I69 — Recovery bootstrap may restore authority infrastructure under independently authorized operational procedures, but cannot create an alternative canonical semantic authority.

RDMS09-I70 — Bootstrap authority does not authorize ordinary project/world mutations.

RDMS09-I71 — Recovery cannot resume authority-bearing operations until a valid canonical Executive authority has been re-established.

RDMS09-I72 — Recovery anti-rollback assessment must consider all applicable authority and policy frontiers, not only Executive Epoch.

RDMS09-I73 — Restored policy frontiers must be mutually compatible within the declared operational scope.

RDMS09-I74 — Missing authoritative policy-generation evidence cannot be replaced by values from an older snapshot without validation.

RDMS09-I75 — Durability claims must declare their supported failure model and persistence boundaries.

RDMS09-I76 — Shared-world dispatch cannot rely on acknowledgement semantics weaker than those required by the applicable durable write-ahead contract.

RDMS09-I77 — Post-backup external-history coverage must be established positively within a declared scope.

RDMS09-I78 — Absence of a recovered ActionRecord is not proof that its external effect never occurred.

RDMS09-I79 — Operations that may conflict with unverifiable external effects remain blocked unless their safety is independently established.

RDMS09-I80 — Executive fencing and downstream dispatch quiescence are distinct guarantees.

RDMS09-I81 — Loss of an old dispatcher's authority does not establish termination of previously transmitted effects.

RDMS09-I82 — Conflicting recovery actions require sufficiently proven dispatch quiescence, outcome reconciliation or safety under all relevant possible effects.

RDMS09-I83 — Restored executable artifacts must not activate before satisfying applicable trust and containment requirements.

RDMS09-I84 — Restored content cannot acquire execution or instruction authority merely through restoration.

RDMS09-I85 — Effective data-suppression controls must precede unauthorized retrieval, context assembly, provider disclosure and export of restored content.

RDMS09-I86 — Missing suppression-frontier evidence prevents disclosures that depend on proof of current authorization.

RDMS09-I87 — Canonical schema interpretation must have one authoritative visibility boundary.

RDMS09-I88 — Mixed-version readers and writers are permitted only when compatibility with frozen canonical semantics is established.

RDMS09-I89 — Schema migration cutover must preserve required atomic control consistency.

RDMS09-I90 — Recovery admission is scope-, operation-, authority-, policy- and dependency-bound.

RDMS09-I91 — Recovery admission cannot be reused after invalidation of a mandatory condition without appropriate revalidation.

RDMS09-I92 — Suspended recovery obligations require durable ownership and a lawful reactivation or escalation mechanism.

RDMS09-I93 — Trigger source-cursor advancement cannot silently discard an uncommitted required canonical reaction.

RDMS09-I94 — A non-replayable source cannot be treated as proof that an unobserved edge event occurred.

PART XV — C02 CORRECTION MATRIX
Finding	Correction	Status
R2-G01 — Bootstrap authority paradox	§§5–13	ADDRESSED
R2-G02 — Inconsistent anti-rollback frontiers	§§14–20	ADDRESSED
R2-G03 — Lost external-action history	§§28–35	ADDRESSED
R2-G04 — Dispatch cutover race	§§36–44	ADDRESSED
R2-G05 — Untrusted restored execution	§§45–51	ADDRESSED
R2-G06 — Disclosure before suppression	§§52–59	ADDRESSED
R2-G07 — Schema visibility ambiguity	§§60–69	ADDRESSED
R2-G08 — Recovery admission TOCTOU	§§70–76	ADDRESSED
R2-G09 — Lost suspended obligations	§§77–86	ADDRESSED
R2-G10 — Unbounded durability claim	§§21–27	ADDRESSED
R2-H01 — Recovery backpressure	§91	HARDENED
R2-H02 — Test dimensions	§92	HARDENED
R2-H03 — Configuration drift	§93	HARDENED
R2-H04 — Sensitive receipts	§94	HARDENED
R2-H05 — Human escalation	§95	HARDENED

ADDRESSED تعني أن المواصفة تحتوي الآن على معالجة مقترحة، ولا تعني اجتياز المراجعة التالية.

PART XVI — REQUIRED ADVERSARIAL ACCEPTANCE TESTS

هذه سيناريوهات اختبار ومراجعة مطلوبة مستقبلًا، وليست اختبارات نُفذت.

AT09-C02-01 — Bootstrap Without Control Ledger

Initial condition: Control Ledger unavailable.

Attack: Recovery Coordinator attempts to authorize a project mutation.

Expected: رفض العملية، مع السماح فقط بإجراء استعادة بنية تحتية خارج الوكيل إذا توفرت سلطة تشغيلية موثوقة.

AT09-C02-02 — Old Policy With New Executive Epoch

Initial condition: Executive authority restored.

Attack: Security Policy and Erasure Frontier remain old.

Expected: منع العمليات التي تتطلب سياسات حديثة لم تُثبت.

AT09-C02-03 — Missing External Payment History

Initial condition: Old Backup restored.

Attack: Payment history after backup unavailable.

Expected: عدم إعادة إرسال عملية يحتمل تكرارها دون دليل ملائم.

AT09-C02-04 — Old Dispatcher After Failover

Initial condition: Executive epoch advanced.

Attack: Old Worker retains an external session.

Expected: منع العمليات المتعارضة ما لم تتحقق شروط Quiescence أو Reconciliation أو السلامة المشروطة.

AT09-C02-05 — Restored Malicious Startup Script

Initial condition: Untrusted Backup restored.

Attack: Startup hooks attempt automatic execution.

Expected: عدم السماح بالتنفيذ قبل التحقق المناسب.

AT09-C02-06 — Deleted Data in LLM Context

Initial condition: Old Backup contains erased data.

Attack: Recovery Context Builder attempts sending it to Provider.

Expected: منع الإفصاح قبل تطبيق Suppression Policy النافذة.

AT09-C02-07 — Partial Migration Crash

Initial condition: Half-completed Schema Migration.

Attack: Old and new Writers attempt canonical mutation.

Expected: عدم وجود تفسيرين قانونيين متناقضين للحالة.

AT09-C02-08 — Admission Becomes Stale

Initial condition: Recovery Admission valid.

Attack: Security Policy changes before Action dispatch.

Expected: إعادة فحص القيود المؤثرة ورفض العملية إذا لم تعد مؤهلة.

AT09-C02-09 — Suspended IN_DOUBT Obligation

Initial condition: External service unavailable.

Attack: Recovery suspends task.

Expected: حفظ التزام تسوية قابل للاكتشاف والاستئناف، دون اعتبار الأثر محسومًا.

AT09-C02-10 — Trigger Cursor Crash Window

Initial condition: Event observed.

Attack: Crash before canonical reaction commit.

Expected: لا يضيع التفاعل المطلوب ولا يتكرر اعتماده بصورة غير قانونية.

AT09-C02-11 — False Durable Acknowledgement

Initial condition: Storage uses volatile acknowledgement.

Attack: Shared-world action attempts dispatch.

Expected: منع dispatch إذا لم تتحقق متطلبات المتانة.

AT09-C02-12 — Unrecoverable Disaster

Initial condition: Authority references and external history cannot be verified.

Attack: Executive attempts NORMAL resumption.

Expected: رفض الاستئناف المتأثر مع تسجيل حدود التعافي والتدخل المطلوب.

PART XVII — NON-REGRESSION REQUIREMENTS

يجب ألا يؤدي C02 إلى:

إنشاء Executive ثانية.

إنشاء صلاحيات مشروع خاصة بـRecovery Coordinator.

تغيير معنى Control Ledger.

تجاوز ActionGate عند تنفيذ عمليات الوكيل.

تغيير معنى IN_DOUBT.

ادعاء Exactly-Once External Effects بلا ضمان.

افتراض استعادة العالم الخارجي مع Backup.

إنشاء محرك جديد لإدارة Triggers.

إنشاء Dependency Engine منافسة.

منح الملفات المستعادة سلطة تعليمات جديدة.

السماح بإفشاء بيانات محذوفة بسبب Restore.

اعتبار Schema جزئية Canonical دون Cutover صحيح.

إعلان الاستعادة ناجحة عندما تكون الالتزامات المؤثرة مجهولة.

افتراض قدرة النظام على إثبات أحداث لم تعد توجد عنها أدلة.

PART XVIII — C02 FINAL VERDICT
RDMS-09 C02

Second-review blockers:
    10

Corrective specifications:
    10

Second-review hardening findings:
    5

Hardening corrections:
    5

New proposed invariants:
    RDMS09-I69 ... RDMS09-I94

Proposed adversarial acceptance tests:
    12

Changes to FCA:
    NONE PROPOSED

Changes to RDMS-01...08:
    NONE PROPOSED

Executable tests:
    0

Implementation:
    NOT AUTHORIZED
C02 Decision

RDMS-09 C02 — CORRECTIVE SPECIFICATION COMPLETE.

RDMS-09 — NOT FROZEN.

توجد الآن معالجة معمارية مقترحة لجميع النتائج العشر التي كشفتها مراجعة التجميد الثانية.

لكن لا يجوز اعتبار هذه المعالجة إثباتًا على أن جميع العقود متوافقة أو أن كل مسارات Recovery أصبحت آمنة.

Next Authorized Step

RDMS-09 — Adversarial Freeze Review 03.

يجب أن تركز المراجعة الثالثة على:

عدم إنشاء سلطة خفية أثناء Bootstrap.

استحالة اختراع تاريخ عمليات مفقود.

التزامن بين Fencing وDispatch.

قابلية ضمانات المتانة للتطبيق.

منع الإفصاح أثناء الاستعادة.

الاتساق بين Schema وPolicy وExecutive Epoch.

استمرار الالتزامات المعلقة بعد انهيارات متكررة.

تقييمي بعد C02

أهم تطور في هذه المرحلة هو أننا أصبحنا نميز بين التعافي الممكن والتعافي الذي يستحيل إثباته بالموارد والأدلة المتاحة.

على سبيل المثال، إذا كانت عملية مالية قد نُفذت، ثم فقد النظام جميع السجلات التي يمكنها إثبات حدوثها، فلا توجد خوارزمية معرفية تستطيع استرجاع حقيقة ضاعت أدلتها بالكامل.

يمكن للوكيل إجراء التحقيقات المناسبة، لكن إن بقيت النتيجة مجهولة، يجب أن يعرف متى يتوقف عن محاولة التقدم.

كذلك عالجنا مشكلة أصعب: كيف تستعيد المنظومة السلطة عندما تكون البنية التي تحفظ السلطة نفسها معطلة، دون إنشاء Executive ثانية أو السماح بتجاوز البوابات القانونية.

التمييز بين استعادة البنية التحتية واستئناف سلطة الوكيل هو القرار الهندسي المركزي في C02.

حالة المشروع
المواصفة	الحالة
FCA v1.0.1	✅ FROZEN
RDMS-01 → RDMS-08	✅ FROZEN
RDMS-09 Draft v1.0	✅ COMPLETE
RDMS-09 C01	✅ COMPLETE
RDMS-09 C02	✅ CORRECTIONS COMPLETE
RDMS-09 Freeze Review 03	⏳ NEXT
RDMS-10	⏳ PENDING

الخطوة التالية: Adversarial Freeze Review 03.

وسنكون أكثر صرامة تحديدًا مع Recovery Bootstrap وDownstream Fencing؛ لأنهما قد يكشفان تعارضًا حقيقيًا مع حدود السلطة المجمدة. وإذا وجدنا هذا التعارض فلن نخفيه داخل تصحيح جديد، بل سنحدده صراحة قبل اتخاذ أي قرار بالتجميد.

END ORIGINAL MESSAGE

========================================================================
SOURCE PART: C03
MESSAGE ID: 89e41ed5-ac4e-4b95-9680-b9bec79f278a
BEGIN ORIGINAL MESSAGE
========================================================================

نواصل الآن إلى RDMS-09 C03 — Recovery Enforcement Boundaries & Durable Continuity Closure.

وصلنا إلى مرحلة دقيقة جدًا في تصميم الوكيل البرمجي. الثغرات الثماني المتبقية لا تتعلق بنقص قدرات التعافي، وإنما بكيفية فرض ضمانات التعافي عند الحدود الفعلية التي تحدث فيها التغييرات.

سنعتمد قرارًا هندسيًا مهمًا في C03:

لا نحتاج إلى بناء أنظمة تحكم إضافية. نحتاج إلى التأكد من أن السلطات التي صممناها سابقًا تستطيع فرض القوانين عند نقاط التنفيذ والاستعادة والتزامن.

وسنميز بوضوح بين ثلاثة مستويات: القانون المعماري، والعقد التشغيلي الذي يفرضه، والتفاصيل التقنية التي يمكن اختيارها أثناء التنفيذ.

RDMS-09 C03 — Recovery Enforcement Boundaries & Durable Continuity Closure
RDMS-09 C03
Recovery Enforcement Boundaries & Durable Continuity Closure

Project: AI Coding Agent
Architecture: Formal Cognitive Architecture — FCA v1.0.1
Specification: RDMS-09
Version: C03 — Corrective Specification v1.0

Parent Documents:

RDMS-09 Draft v1.0

RDMS-09 C01

RDMS-09 C02

RDMS-09 Adversarial Freeze Review 03

Dependencies: RDMS-01…08 — FROZEN

Status: CORRECTIVE SPECIFICATION — NOT FROZEN
Implementation Authorization: NO
Next Gate: Adversarial Freeze Review 04

PART I — ARCHITECTURAL OBJECTIVE
1. Scope

تعالج C03 النتائج الثماني المتبقية من المراجعة الثالثة:

Finding	Problem
R3-G01	Bootstrap Handoff Integrity
R3-G02	Acknowledged History Continuity
R3-G03	Cross-Frontier Enforcement
R3-G04	External Effect Quiescence
R3-G05	Restore-Time Containment
R3-G06	Restored Data Processing Safety
R3-G07	Canonical Schema Cutover
R3-G08	Durable Recovery Continuation

هدف هذه الوثيقة هو تحديد الآليات اللازمة لإغلاق هذه النتائج دون تغيير القوانين المجمدة.

2. Central Recovery Rule

نعتمد:

Recovery may authorize continuation only within a scope for which the required authority, state integrity, policy validity and external-effect constraints are sufficiently established.

أي:

لا يسمح التعافي باستئناف العمليات إلا ضمن نطاق ثبتت فيه الشروط القانونية والتشغيلية اللازمة لها.

هذا لا يعني أن النظام يجب أن يعرف كل شيء.

بل يعني ألا يعتمد قرار التنفيذ على حقيقة لا يستطيع إثباتها.

3. Architectural Conservation

تبقى السلطات كما يلي:

Cognitive Executive
    └── Semantic authorization

RDMS-01
    └── Canonical control authority
    └── Executive epoch
    └── CommitGate
    └── Control Ledger

RDMS-04
    └── ActionGate
    └── Action Journal
    └── World-effect reconciliation

RDMS-05
    └── Durable triggers
    └── Commitments
    └── Resumption

RDMS-06
    └── Dependency Evaluation

RDMS-09
    └── Cross-system recovery orchestration

لا تنشئ هذه الوثيقة سلطة تنفيذية جديدة.

PART II — C03-A: BOOTSTRAP HANDOFF INTEGRITY
4. Finding

FR09-R3-G01 — Bootstrap Authority Has No Complete Handoff Proof

المشكلة

قد تتم استعادة Control Ledger بواسطة جهة تشغيلية خارجية مخولة.

لكن خلال الاستعادة ربما تغيرت موارد أو إعدادات تؤثر في المشروع.

إذا استأنفت Executive عملها دون معرفة هذه التغييرات، فقد تستخدم نموذجًا معرفيًا لم يعد مطابقًا للواقع.

5. Design Decision

Infrastructure restoration and canonical agent resumption are two distinct operations.

استعادة البنية التحتية لا تعني استئناف الوكيل.

يجب أن توجد نقطة تسليم واضحة بينهما.

6. BootstrapHandoffProof
BootstrapHandoffProof {
    bootstrap_case_ref

    recovery_principal_ref
    verified_authority_ref

    authorized_bootstrap_scope

    initial_resource_frontier

    performed_operations[]

    modified_resource_refs[]

    created_resource_refs[]

    replaced_resource_refs[]

    unknown_change_scope[]

    restoration_evidence_refs[]

    final_resource_frontier

    audit_completeness

    canonical_handoff_status
}
7. Mandatory Enforcement

يجب تطبيق الخطوات التالية:

Control Plane unavailable
          ↓
Authorized infrastructure recovery
          ↓
Record or reconstruct actual changes
          ↓
Validate recovered control history
          ↓
Restore current Executive authority
          ↓
Reconcile affected world effects
          ↓
Evaluate changed dependencies
          ↓
Scoped resumption decision

لا يسمح بـ:

Storage restored
    → automatically NORMAL
8. Unknown Bootstrap Effects

إذا كانت جهة الاستعادة لا تستطيع إثبات ما حدث لبعض الموارد:

unknown_change_scope != EMPTY

فلا يجوز افتراض ثباتها.

يجب تحديد العمليات التي تعتمد على هذه الموارد وإعادة فحص صلاحيتها.

لكن لا يلزم إبطال نتائج مستقلة عن الموارد المتأثرة إذا أثبت RDMS-06 استقلالها.

9. Bootstrap Authority Boundary

تبقى جهة Bootstrap جهة تشغيل بنية تحتية.

لا تملك صلاحية:

Accept new engineering decisions

Mutate canonical project cognition

Promote memory

Recruit specialists

Authorize ordinary project actions

بمجرد امتلاكها تفويضًا لإصلاح خدمات التحكم.

أما عمليات صيانة البنية نفسها فتخضع إلى حوكمة تشغيلية موثوقة خارج مسار قرارات الوكيل المعطل.

يجب أن تبقى هذه الحدود واضحة في توثيق النظام.

10. Handoff Failure

إذا تعذرت معرفة حالة السلطة أو سلامة التاريخ القانوني بعد الاستعادة:

BOOTSTRAP:
    COMPLETED_OR_PARTIAL

CANONICAL REENTRY:
    NOT AUTHORIZED

لا يجوز اعتبار نجاح الإصلاح التقني إثباتًا لسلامة الاستئناف.

C03-A1 Result

R3-G01 — CONTRACT CORRECTED.

PART III — C03-A: ACKNOWLEDGED HISTORY CONTINUITY
11. Finding

FR09-R3-G02 — Durable Write Can Disappear Through an Older Recovery Frontier

المشكلة

قد تكون هناك عملية جرى تسجيلها بصورة متينة، ثم نفذت في العالم الخارجي.

لكن Disaster Restore تعيد نسخة احتياطية أقدم لا تحتوي عليها.

المشكلة الأساسية ليست وجود Backup قديمة.

بل أن النظام قد يعتقد أن التاريخ المستعاد كامل.

12. Design Decision

نعتمد مبدأ:

Recovered history completeness must be positively established within its declared failure model and coverage scope.

أي أن اكتمال التاريخ يحتاج إثباتًا، ولا يستنتج من غياب أحداث إضافية.

13. AcknowledgedHistoryContinuity
AcknowledgedHistoryContinuity {
    recovery_case_ref

    restored_control_frontier

    trusted_acknowledged_frontier?

    recovered_ledger_frontier

    recovered_action_journal_frontier

    trusted_history_source_refs[]

    independent_effect_history_refs[]

    missing_event_ranges[]

    uncertain_event_ranges[]

    affected_world_effect_domains[]

    durability_failure_model_ref

    continuity_assessment:
        PROVEN_WITHIN_SCOPE
        INCOMPLETE
        UNKNOWN
}
14. Two Distinct Frontiers

نميز بين:

Acknowledged Frontier

آخر موضع توجد أدلة موثوقة على أنه تم الإقرار بمتانته.

Recovered Frontier

آخر موضع تمكن النظام من استعادته والتحقق من اتساقه.

مثال:

Acknowledged Frontier = 1000

Recovered Frontier = 950

النتيجة:

Missing range = 951 ... 1000

إذا كان هذا النطاق يتضمن أو قد يتضمن آثارًا خارجية، يجب التحقيق فيها.

15. Missing Acknowledgement Evidence

قد نفقد أيضًا السجل الذي يثبت وصول التاريخ إلى 1000.

لا يجوز حينها افتراض:

Recovered Frontier = 950
therefore history complete.

يجب تقييم نموذج الفشل ومصادر التاريخ المستقلة.

إذا لم يمكن إثبات اكتمال التاريخ:

continuity_assessment = UNKNOWN
16. Effect-Domain Restriction

عندما يوجد تاريخ مفقود أو غير قابل للتحقق، يجب تحديد المجالات التي قد تحتوي على آثار غير مرصودة.

مثل:

Remote Git operations

Database mutations

Deployment operations

External API transactions

تُمنع العمليات التي قد تتعارض مع هذه الآثار إلى أن تستوفى شروط RDMS-04.

لا يلزم حجب عمليات مستقلة عنها عندما يمكن إثبات الاستقلال.

17. Durability Limits

لا تدعي C03 أن النظام قادر على النجاة من جميع الأعطال.

بل يجب أن تكون الضمانات محددة بـ:

Declared failure model

Trusted durability sources

Available independent history

Recoverable control frontier

إذا تجاوز الحادث نموذج الأعطال المدعوم، لا نواصل تطبيق ضماناته كما لو أنها ما زالت مثبتة.

18. No Historical Fabrication

إذا لم يعد هناك مصدر يستطيع إثبات وقوع Action مفقودة، فلا تستطيع Recovery إعادة بناء الحدث من التخمين.

الحل هو الحفاظ على عدم اليقين ومنع العمليات المتعارضة.

C03-A2 Result

R3-G02 — CONTRACT CORRECTED.

PART IV — C03-A: CROSS-FRONTIER ADMISSION ENFORCEMENT
19. Finding

FR09-R3-G03 — Cross-Frontier Validation Has No Stable Enforcement Boundary

المشكلة

قد تتحقق Recovery من السلطة والسياسات والاعتماديات عند زمن معين.

ثم تتغير إحدى هذه الشروط قبل تنفيذ عملية جديدة.

هذه مشكلة:

Time-of-Check to Time-of-Use — TOCTOU.

20. Design Decision

لا تعتبر RecoveryAdmission تصريحًا دائمًا.

بل تصبح تقييمًا محدد النطاق تُعاد مراجعة شروطه المؤثرة عند الحدود القانونية المناسبة.

21. CrossFrontierAdmissionProof
CrossFrontierAdmissionProof {
    admission_ref

    project_scope

    permitted_operation_classes[]

    executive_epoch

    canonical_state_ref

    policy_frontier_refs[]

    security_frontier_refs[]

    suppression_frontier_refs[]

    dependency_frontier_refs[]

    outstanding_effect_constraints[]

    compatibility_results[]

    required_revalidation_conditions[]

    applicable_gate_refs[]

    admission_status
}
22. Enforcement Sequence
Recovery Assessment
        ↓
Provisional Scoped Admission
        ↓
Operation Proposed
        ↓
Current Authority Check
        ↓
Relevant Policy Check
        ↓
Relevant Dependency Check
        ↓
Outstanding Effect Check
        ↓
CommitGate / ActionGate
        ↓
Authorized Effect
23. Current-State Requirement

لا يجوز اعتماد العملية باستخدام نتيجة تقييم قديمة إذا تغير أحد شروطها الإلزامية.

مثال:

T1:
    Security Policy v8 valid.

T2:
    Security Policy v9 becomes authoritative.

T3:
    Operation authorized using v8.

يجب رفض T3 عندما تكون v9 نافذة وتغير قانونية العملية.

24. No Universal Global Transaction

قد توجد السياسات في خدمات مختلفة.

لا نفترض القدرة على قراءتها كلها ذريًا.

يجب أن تحدد كل عملية:

الشروط التي تحتاج إلى ضمان اتساق قوي.

المراجع التي يمكن تقييمها وفق Dependency Freshness.

المخاطر التي تتطلب إعادة تحقق.

حدود التأخير أو عدم إمكانية كشف التغيير.

إذا لم يستطع النظام إثبات شرط إلزامي عند نقطة استخدامه، فلا يجوز ادعاء أن الشرط مستوفى.

25. Authority Changes During Dispatch

إذا تغيرت السلطة قبل اعتماد dispatch القانوني، يجب تطبيق شروط السلطة الحالية.

أما إذا كانت Action قد تجاوزت بالفعل نقطة dispatch القانونية وأُرسلت، فلا يعتبر تغيير السلطة دليلًا على توقف الأثر.

يظل RDMS-04 مسؤولًا عن التسوية.

26. Scoped Admission

يمكن أن تسمح Recovery بـ:

READ:
    ALLOWED

ISOLATED ANALYSIS:
    ALLOWED

SHARED_WORLD MUTATION:
    BLOCKED

بحسب الأدلة المتاحة.

هذا يمنع توقف النظام كله بلا داعٍ، دون التضحية بالسلامة.

C03-A3 Result

R3-G03 — CONTRACT CORRECTED.

PART V — C03-B: POSSIBLE EXTERNAL EFFECTS
27. Finding

FR09-R3-G04 — Dispatch Quiescence Cannot Be Established From Local Termination Alone

المشكلة

قد تتوقف Worker محليًا، بينما تكون قد أرسلت طلبًا لم ينفذ بعد في الخدمة الخارجية.

إذا سمح Recovery بعملية متعارضة، فقد يحدث تكرار أو تعويض غير صحيح.

28. Design Decision

نعتمد:

Local execution termination does not establish external-effect quiescence.

أي أن توقف عملية التنفيذ المحلية لا يثبت انتهاء آثارها الخارجية.

29. PossibleExternalEffectAssessment
PossibleExternalEffectAssessment {
    assessment_id

    related_action_refs[]

    confirmed_effect_refs[]

    possible_unconfirmed_effects[]

    unknown_effect_scope[]

    external_execution_guarantees[]

    outstanding_dispatch_paths[]

    effect_identity_refs[]

    proposed_followup_action_ref?

    conflict_analysis

    safety_evidence_refs[]

    conclusion:
        CONFLICT_IMPOSSIBLE
        EFFECTS_RECONCILED
        FOLLOWUP_SAFE_UNDER_UNCERTAINTY
        NOT_PROVEN
}
30. Conservative Effect Set

يجب أن يغطي تقييم الآثار الممكنة جميع الاحتمالات المؤثرة التي لا توجد أدلة كافية لاستبعادها.

مثال:

Request may have been:

Not transmitted

Transmitted but queued

Applied successfully

Applied partially

Still executing

لا يلزم دائمًا تعداد جميع التفاصيل الداخلية للخدمة الخارجية.

لكن يجب ألا يستبعد التحليل احتمالًا يمكن أن يغير قانونية العملية الجديدة.

31. Safe Follow-Up Rule

يمكن السماح بعملية جديدة عندما يثبت أحد الشروط:

Case A — Conflicting effect impossible

توجد أدلة كافية على أن الأثر القديم لا يمكن أن يتعارض مع العملية الجديدة.

Case B — Previous effect reconciled

تم التحقق من حالة الأثر السابق بما يكفي.

Case C — Follow-up safe despite uncertainty

العملية الجديدة آمنة تحت جميع الحالات السابقة التي لا يزال احتمالها قائمًا ضمن نطاق التحليل.

مثال ممكن:

خدمة خارجية تدعم مفتاح Idempotency مضمونًا ضمن مجال وزمن محددين.

لكن يجب إثبات أن الضمان ينطبق على العملية الفعلية.

32. Unknown Effect Space

إذا تعذر تحديد نطاق الآثار الممكنة بدرجة تكفي للحكم على السلامة:

conclusion = NOT_PROVEN

وتمنع العمليات التي قد تتعارض معها.

33. Compensation

لا تصبح Compensation آمنة لمجرد توقف Worker الأصلية.

يجب تقييم أثر العملية الأصلية أو إثبات أن التعويض مناسب ضمن حالات عدم اليقين ذات الصلة.

كما يجب أن تمتلك Compensation سجل Action قانونيًا عند تنفيذ تأثير خارجي.

34. No Global Exactly-Once

لا تدعي هذه المواصفة ضمان Exactly-Once خارجي شامل.

تبقى ضمانات تكرار العمليات مرتبطة بإمكانات النظام الخارجي وبروتوكول RDMS-04.

C03-B1 Result

R3-G04 — CONTRACT CORRECTED.

PART VI — C03-B: SCHEMA CUTOVER ENFORCEMENT
35. Finding

FR09-R3-G07 — Canonical Schema Cutover Is Not Bound to Physical Reader/Writer Enforcement

المشكلة

قد تعتمد المنظومة Schema جديدة بصورة قانونية، لكن Writer قديمة تواصل الكتابة وفق Schema سابقة.

النتيجة المحتملة هي تلف الحالة المعتمدة أو تفسيرها بصورة غير متسقة.

36. Design Decision

Canonical schema visibility and canonical write eligibility must be enforced together.

تغيير المرجع القانوني لـSchema لا يكفي.

يجب أن تمنع حدود الكتابة استعمال كاتب غير متوافق.

37. SchemaCutoverEnforcement
SchemaCutoverEnforcement {
    migration_ref

    source_schema_version
    target_schema_version

    authoritative_schema_generation

    current_schema_visibility_ref

    compatible_reader_generations[]

    compatible_writer_generations[]

    fenced_writer_generations[]

    active_writer_session_refs[]

    outstanding_write_refs[]

    migration_commit_ref

    post_cutover_validation_refs[]

    unresolved_compatibility_risks[]
}
38. Cutover Preconditions

قبل اعتماد Schema الجديدة يجب التحقق من:

Target representation integrity

Reference compatibility

Required invariants

Writer compatibility

Outstanding conflicting writes

Authority and version constraints
39. Writer Fencing

أي Writer تستطيع تعديل Canonical State يجب أن تخضع إلى شروط النسخة القانونية الحالية.

إذا كانت Writer تستخدم تفسيرًا قديمًا غير متوافق:

Write authorization = DENIED

وقد تتطلب البنية إيقاف جلسات الكتابة القديمة أو منع صلاحياتها عند حدود التخزين.

لا يكفي تحديث متغير محلي داخل Runtime الجديدة.

40. In-Flight Writes

قد تكون Writer قد أرسلت كتابة قبل Cutover، لكنها لم تُحسم بعد.

لا يجوز افتراض توقف هذه الكتابة لمجرد فقدان Writer صلاحيتها اللاحقة.

يجب تقييم العمليات المعلقة قبل Cutover وفق آثارها المحتملة.

41. Crash Before Cutover

إذا تعطل النظام قبل اعتماد حد الانتقال القانوني:

Authoritative schema =
    previously committed schema

وفق السجل القانوني الصالح.

البيانات المحولة جزئيًا لا تكتسب سلطة تلقائية.

42. Crash After Cutover

إذا اعتمد Cutover بصورة قانونية ثم تعطل النظام:

Authoritative schema =
    committed target schema

ويجب أن تستعيد Recovery هذا المعنى.

لا يجوز الرجوع إلى Schema القديمة إذا كانت ستعيد تفسير عمليات اعتمدت وفق الجديدة.

43. Mixed-Version Compatibility

يمكن السماح بتعايش Readers وWriters من نسخ مختلفة إذا أثبتت عقود التوافق الحفاظ على المعنى القانوني والقيود.

لكن إذا لم يمكن إثبات ذلك، يجب منع عمليات الكتابة غير المتوافقة.

C03-B2 Result

R3-G07 — CONTRACT CORRECTED.

PART VII — C03-C: RESTORE CONTAINMENT
44. Finding

FR09-R3-G05 — Quarantine Does Not Fully Define the Restoration Boundary

المشكلة

قد تكون عملية Restore نفسها ذات آثار جانبية قبل تشغيل أي ملف مستعاد عمدًا.

مثل الكتابة إلى مجلد تستخدمه خدمة حية أو إعادة تفعيل إعدادات أو Hooks.

45. Design Decision

Restoration must be classified by reachable effects, not by its administrative name.

الاستعادة ليست عملية آمنة تلقائيًا.

46. RestoreContainmentProof
RestoreContainmentProof {
    restore_operation_ref

    restore_source_ref

    destination_scope

    writable_mount_refs[]

    reachable_service_refs[]

    automatic_activation_paths[]

    executable_content_paths[]

    credential_exposure_scope

    containment_guarantees[]

    relevant_environment_versions[]

    unresolved_escape_paths[]

    proof_result:
        CONTAINED_WITHIN_SCOPE
        NOT_CONTAINED
        UNKNOWN
}
47. Restore Procedure

المسار المفضل عند الحاجة إلى استعادة محتوى غير موثوق:

Obtain trusted restoration environment
          ↓
Validate destination containment
          ↓
Restore without automatic activation
          ↓
Verify source provenance
          ↓
Inspect executable/configuration artifacts
          ↓
Validate schema and dependencies
          ↓
Authorize controlled activation
48. Active Destination Risk

إذا كان مسار الاستعادة متصلًا ببيئة حية:

Restore writes into active service directory

فقد يحدث أثر قبل اكتمال التحقق.

يجب تصنيف هذه العملية بحسب آثارها الفعلية.

ولا يسمح بتعاملها على أنها EPHEMERAL_SANDBOX ما لم يثبت العزل المطلوب وفق FCA.

49. Indirect Execution

تدخل ضمن التقييم:

Startup hooks

Build scripts

Package installation hooks

Plugin manifests

CI configuration

Recovered tool adapters

Service configuration

فهذه الملفات قد تسبب تنفيذًا غير مباشر.

50. Quarantine Release

لا يخرج المحتوى المستعاد من العزل لمجرد نجاح فحص واحد.

يجب أن تستوفي العملية شروط الثقة والنطاق والاعتماديات والصلاحيات المناسبة لطريقة استعماله.

إذا بقيت مسارات خروج مؤثرة غير محسومة:

Release authorization = DENIED

للاستخدام الذي يعتمد على إثبات العزل.

C03-C1 Result

R3-G05 — CONTRACT CORRECTED.

PART VIII — C03-C: RESTORED DATA PROCESSING ADMISSION
51. Finding

FR09-R3-G06 — Recovery Disclosure Barrier Must Cover Processing Before Materialization

المشكلة

قد تستعيد Backup قديمة بيانات حُذفت سابقًا.

وقد تنتقل تلك البيانات إلى LLM أو Specialist أو فهرس مشتق قبل تطبيق حظر الإفصاح.

52. Design Decision

Restored data is restricted until its applicable processing and disclosure permissions are established.

لا تصبح البيانات قابلة للاستخدام العام لمجرد استعادتها على القرص.

53. RestoredDataProcessingAdmission
RestoredDataProcessingAdmission {
    admission_ref

    restored_data_scope

    current_suppression_frontier

    processing_purpose

    processing_boundary

    authorized_processing_operations[]

    prohibited_disclosure_paths[]

    permitted_external_transfer_scopes[]

    derivative_restrictions[]

    effective_policy_version

    admission_proof_ref

    admission_status
}
54. Processing Gate

قبل استعمال المحتوى المستعاد يجب تحديد:

What data?

For which purpose?

By which component?

Under which current policy?

Will content leave the trusted boundary?

Will derivatives be created?
55. Restricted Restore Procedure
Restore into restricted storage
        ↓
Verify current suppression obligations
        ↓
Evaluate permitted processing
        ↓
Apply access/disclosure barriers
        ↓
Reapply erasure where required
        ↓
Authorize permitted use
56. External Provider Protection

لا يجوز إرسال بيانات مستعادة إلى Provider خارجية إذا كانت سياسة البيانات الحالية لا تسمح بذلك.

يشمل ذلك:

LLM prompts

Embedding requests

Diagnostic summaries

Specialist context transfer

External indexing services

Log exports
57. Necessary Internal Processing

قد تحتاج Recovery إلى معالجة محدودة لتحديد الملفات والمشتقات المطلوب حذفها.

يمكن السماح بذلك ضمن تفويض مناسب وبيئة محكومة.

لكن هذا لا يمنح الحق في استعمال البيانات لأغراض معرفية جديدة أو إفشائها خارجيًا.

58. Derived Artifacts

يجب أن تخضع المشتقات ذات الصلة إلى قيود المصدر المناسبة.

مثال:

Private document
      ↓
Summary
      ↓
Memory entry
      ↓
Retrieval index

قد يستلزم حذف المستند أو حظر استعماله معالجة بعض هذه المشتقات أيضًا.

تستخدم المعمارية حوكمة RDMS-07 ومراجع Lineage المناسبة.

59. Missing Current Policy

إذا تعذر استعادة أحدث سياسة Suppression ذات الصلة:

Processing/disclosure authorization:
    NOT ESTABLISHED

لا يجوز استعمال سياسة قديمة باعتبارها الحديثة دون إثبات.

C03-C2 Result

R3-G06 — CONTRACT CORRECTED.

PART IX — C03-D: RECOVERY CONTINUATION DURABILITY
60. Finding

FR09-R3-G08 — Trigger Commit and Recovery Suspension Have a Durability Gap

المشكلة

قد تُعلق Recovery مهمة بسبب Action غير محسومة.

لكنها قد تتعطل قبل حفظ Trigger أو Commitment التي تضمن إعادة التفعيل.

وقد تتقدم Source Cursor قبل اعتماد رد الفعل القانوني.

61. Design Decision

Suspension is recoverably safe only when its required unresolved obligations and continuation semantics are durable.

أي أن تعليق المهمة لا يكون قابلًا للاستئناف بصورة موثوقة إلا إذا حُفظت الالتزامات المطلوبة وآلية متابعتها.

62. RecoveryContinuationDurability
RecoveryContinuationDurability {
    recovery_case_ref

    unresolved_obligation_refs[]

    affected_goal_refs[]

    action_reconciliation_refs[]

    canonical_suspension_commit_ref?

    required_trigger_refs[]

    source_cursor_frontier

    canonical_reaction_frontier

    replay_capability_ref

    durable_reactivation_status

    escalation_commitment_ref?

    unresolved_persistence_failures[]
}
63. Atomic Suspension

عندما يجب حفظ:

Goal suspended
+
Unresolved obligations
+
Reactivation commitment

معًا لضمان التعافي، يجب أن يتم اعتمادها وفق الحدود الذرية المطلوبة في RDMS-01.

لا يجوز حفظ تعليق المهمة بصورة تجعل الالتزامات تختفي من الحالة القانونية.

64. Trigger Cursor Ordering

نميز بين:

SOURCE EVENT OBSERVED

و:

CANONICAL REACTION COMMITTED

القاعدة:

لا يجوز أن يؤدي تقدم Source Cursor إلى إسقاط حدث مطلوب لم يعتمد تفاعله القانوني بعد.

65. Legal Replay Options

تستطيع بنية Trigger استخدام بروتوكول مناسب، مثل:

Receive event
      ↓
Determine reaction identity
      ↓
Commit canonical reaction
      ↓
Advance acknowledged progress

أو بروتوكول مكافئ يسمح بإعادة التسليم وإزالة التكرار.

المهم هو الحفاظ على ضمانات RDMS-05.

لا نفرض طريقة تخزين واحدة.

66. Crash Before Reaction Commit

إذا وقع Crash بعد قراءة الحدث وقبل اعتماد رد الفعل:

Reaction not committed

يجب أن تسمح آلية المصدر القابل لإعادة التشغيل بإعادة اكتشاف الحدث.

67. Crash After Reaction Commit

إذا وقع Crash بعد اعتماد رد الفعل لكن قبل تأكيد التقدم إلى المصدر:

Reaction committed

قد يصل الحدث مرة أخرى.

يجب أن تمنع هوية Reaction وidempotency تكرار اعتماد الأثر القانوني.

إذا كانت Reaction تطلب Mutation خارجية، تخضع لاحقًا إلى RDMS-04، ولا نخلط بين عدم تكرار ControlCommit وعدم تكرار World Effect.

68. Non-Replayable Sources

إذا لم يكن المصدر يحتفظ بتاريخ يسمح بإثبات حدوث حدث أثناء Downtime، فلا يمكن اختراع هذا الحدث.

يجب أن تبقى حدود التغطية واضحة.

قد يحتاج النظام إلى:

Alternative authoritative observation

Human review

Explicit revalidation

Safe suspension
69. Persistence Failure During Suspension

إذا تعذر حفظ Commitment المطلوبة:

Durable suspension:
    NOT ESTABLISHED

يجب عدم الإعلان بأن النظام علق المهمة بأمان مع ضمان استئنافها تلقائيًا.

إذا بقي Control Ledger غير متاح، يتعين الاحتفاظ بحالة منع مناسبة ضمن حدود التحكم الموثوقة المتاحة، أو الانتقال إلى إجراء استعادة تشغيلية مخول.

ولا يجوز الادعاء بوجود ضمان استمرارية لم يتمكن النظام من تسجيله.

70. Recovery After Repeated Crash

عندما تتكرر الأعطال:

Recovery Case R1
       ↓
Crash
       ↓
Restart
       ↓
Crash
       ↓
Restart

يجب أن تبقى هوية RecoveryCase والالتزامات المعتمدة قابلة للاستعادة.

لا يجوز بدء حالة جديدة تنسى حدود المحاولات السابقة.

C03-D Result

R3-G08 — CONTRACT CORRECTED.

PART X — CROSS-COMPONENT SAFETY RULES
71. Recovery Admission Principle

يمكن تلخيص منطق السماح باستئناف عملية كما يلي:

Operation proposed
        ↓
Current Executive authority valid?
        │
        ├── NO → DENY
        ▼
Canonical state valid for operation?
        │
        ├── NO → DENY
        ▼
Required policies current and applicable?
        │
        ├── NO → DENY
        ▼
Relevant dependencies valid?
        │
        ├── NO → DENY
        ▼
Outstanding world effects compatible?
        │
        ├── NO → DENY
        ▼
Required trust/disclosure conditions met?
        │
        ├── NO → DENY
        ▼
Applicable CommitGate / ActionGate
        ↓
AUTHORIZED OPERATION

هذا مخطط منطقي لتجميع شروط الأهلية.

لا ننشئ بوابة قانونية ثالثة مستقلة.

72. Unknown Does Not Always Mean Global Shutdown

إذا كانت إحدى المعلومات مجهولة، يجب تحديد العمليات التي تحتاج إليها.

مثال:

Database transaction status:
    UNKNOWN

Unrelated documentation analysis:
    May remain allowed

Dependent database mutation:
    BLOCKED

لا نمنع العمليات المستقلة عندما يثبت استقلالها.

73. Safety Under Partial Recovery

يمكن أن تعود بعض القدرات:

Read-only project inspection

Isolated reasoning

Documentation analysis

قبل أن تصبح جميع العمليات الخارجية مؤهلة.

لكن كل قدرة يجب أن تحترم حدود الموارد والسلطة والثقة المناسبة.

74. No Inferred Completion

لا يجوز اعتبار أي من التالي إثباتًا شاملًا للتعافي:

Service started.

Database connection succeeded.

LLM responded.

Health check passed.

Latest tests passed.

كل نتيجة تثبت فقط ما تسمح أدلتها بإثباته.

75. Authority and Reality Remain Separate

حتى بعد اكتمال هذه المواصفة:

Valid Executive authority
        ≠
Known world state

و:

Known world state
        ≠
Authorized new action

و:

Recovered memory
        ≠
Current verified truth

هذه الفروق جزء أساسي من هوية FCA.

PART XI — ADDITIONAL FORMAL INVARIANTS

تضاف إلى RDMS09-I01…I94 الثوابت التالية:

RDMS09-I95 — Successful infrastructure bootstrap does not independently authorize canonical agent resumption.

RDMS09-I96 — Bootstrap handoff must preserve or explicitly identify unknown changes affecting canonical project dependencies.

RDMS09-I97 — Recovered control history completeness must be supported by evidence appropriate to the declared durability failure model.

RDMS09-I98 — A missing trusted acknowledgement frontier cannot be replaced by the restored snapshot's apparent endpoint without validation.

RDMS09-I99 — Potentially missing externally effective events require scoped reconciliation or restrictions before conflicting continuation.

RDMS09-I100 — Recovery admission cannot be treated as permanent authorization independent of current mandatory policy and authority conditions.

RDMS09-I101 — Current legal gates must enforce relevant conditions at the operation's authorization boundary.

RDMS09-I102 — Local process termination does not establish termination of previously transmitted or queued external effects.

RDMS09-I103 — Safety under unresolved external effects requires a conservative assessment of all materially possible effect states.

RDMS09-I104 — Canonical schema cutover cannot permit incompatible writers to continue mutating authoritative state.

RDMS09-I105 — Committed schema visibility must remain recoverably unambiguous across crashes.

RDMS09-I106 — Restoration containment must account for effects caused by the restore operation itself.

RDMS09-I107 — Restored executable or configuration artifacts cannot be activated before applicable trust and containment conditions are satisfied.

RDMS09-I108 — Restored sensitive data cannot enter unauthorized processing or disclosure paths before current applicable restrictions are established.

RDMS09-I109 — Relevant derived artifacts must preserve applicable data-use restrictions.

RDMS09-I110 — Suspended recovery obligations require durable continuation or an explicitly identified inability to guarantee automatic reactivation.

RDMS09-I111 — Trigger source progress cannot silently discard required uncommitted canonical reactions.

RDMS09-I112 — Replay of an already committed reaction must preserve canonical idempotency.

RDMS09-I113 — Recovery after repeated crashes must not silently discard previously recorded unresolved obligations.

PART XII — CORRECTION MATRIX
Finding	C03 Section	Result
R3-G01 — Bootstrap Handoff	4–10	ADDRESSED
R3-G02 — History Continuity	11–18	ADDRESSED
R3-G03 — Cross-Frontier Enforcement	19–26	ADDRESSED
R3-G04 — External Effect Quiescence	27–34	ADDRESSED
R3-G05 — Restore Containment	44–50	ADDRESSED
R3-G06 — Data Processing Admission	51–59	ADDRESSED
R3-G07 — Schema Cutover	35–43	ADDRESSED
R3-G08 — Durable Continuation	60–70	ADDRESSED

Result: ثمانية عقود تصحيحية تغطي النتائج الثماني.

وهي جاهزة للمراجعة، وليست مثبتة بالتنفيذ.

PART XIII — C03 ACCEPTANCE REQUIREMENTS
76. Freeze Review Criteria

عند مراجعة C03 يجب التركيز على:

عدم خلق سلطة جديدة أثناء Bootstrap.

عدم افتراض اكتمال التاريخ المستعاد.

عدم السماح بتفويض اعتمادًا على سياسة فقدت صلاحيتها.

عدم تفسير توقف Worker على أنه توقف الأثر الخارجي.

عدم السماح لـWriter غير متوافقة بتعديل Canonical State.

عدم تفعيل محتوى مستعاد قبل فحص الثقة المناسب.

عدم إفشاء محتوى محذوف أثناء إجراءات الاستعادة.

عدم فقدان التزامات Recovery بسبب Crash أو Trigger Replay.

77. Implementation Boundary

تحدد المواصفة ما يجب إثباته.

لكنها لا تفرض الآن تقنية واحدة لتنفيذ:

Storage durability

Distributed fencing

Backup isolation

Process supervision

Schema migration

Privacy suppression

Trigger persistence

يمكن اختيار هذه التقنيات أثناء التصميم البرمجي لاحقًا، بشرط تحقيق العقود المجمدة.

إذا تعذرت مطابقة أحد العقود في بيئة محددة، لا يجوز ادعاء نجاح التنفيذ.

PART XIV — REQUIRED ADVERSARIAL TEST MATRIX
AT09-C03-01 — Bootstrap Handoff

Failure: استعادة Control Ledger بعد تعديل مورد يؤثر في المشروع.

Required result: اكتشاف التغيير أو التصريح بنطاق عدم اليقين، وعدم الاستئناف اعتمادًا على افتراض ثبات المورد.

AT09-C03-02 — Missing Acknowledged History

Failure: استعادة Snapshot أقدم من آخر Action خارجية.

Required result: منع استنتاج اكتمال التاريخ دون دليل مناسب.

AT09-C03-03 — Policy Change During Admission

Failure: تغير سياسة أمنية بين Recovery Assessment وAction authorization.

Required result: تطبيق الشروط القانونية النافذة عند الحد المناسب.

AT09-C03-04 — In-Flight External Request

Failure: انتهاء Worker بينما بقي طلب خارجي قيد التنفيذ.

Required result: عدم السماح بعملية متعارضة دون دليل أمان كافٍ.

AT09-C03-05 — Old Schema Writer

Failure: Writer قديمة تحاول تعديل Canonical State بعد Cutover.

Required result: رفض الكتابة غير المتوافقة.

AT09-C03-06 — Restore Into Active Directory

Failure: عملية Restore تسبب تفعيل Hook داخل خدمة حية.

Required result: منع العملية أو معاملتها وفق آثارها الفعلية ومسارها القانوني.

AT09-C03-07 — Sensitive Data During Index Rebuild

Failure: بيانات محذوفة داخل Backup تصل إلى مسار Indexing خارجي.

Required result: منع الإفصاح قبل تحقق سياسة البيانات النافذة.

AT09-C03-08 — Trigger Cursor Crash

Failure: Crash بعد ملاحظة حدث وقبل اعتماد Reaction.

Required result: إعادة الاكتشاف عندما يكون المصدر قابلًا للـReplay، وعدم فقدان الالتزام بصمت.

AT09-C03-09 — Crash After Reaction Commit

Failure: حدث يُسلّم مرتين بعد تعطل النظام.

Required result: عدم تكرار Canonical Reaction، مع إبقاء آثار العالم الخارجي تحت RDMS-04.

AT09-C03-10 — Failed Suspension Persistence

Failure: تعذر حفظ Commitment قبل توقف Recovery.

Required result: عدم ادعاء وجود تعليق قابل للاستئناف تلقائيًا إذا لم يثبت حفظه.

AT09-C03-11 — Multi-Crash Recovery

Failure: تتكرر الأعطال أثناء محاولة تسوية Action غير محسومة.

Required result: الحفاظ على الالتزامات القانونية المعتمدة وعدم إعادة تنفيذ Action بصورة عمياء.

AT09-C03-12 — Unrecoverable External History

Failure: اختفاء جميع المصادر القادرة على تحديد نتيجة Action حساسة.

Required result: الحفاظ على عدم اليقين وحجب العمليات المتعارضة، مع السماح بالأعمال المستقلة المثبتة.

PART XV — FREEZE GOVERNANCE
78. Specification vs Implementation

من المهم الفصل بين:

Specification Freeze

يعني أن عقود السلطة والحالة والتزامن والتعافي متماسكة بما يكفي لتصبح مرجعًا للتنفيذ.

Implementation Verification

يعني أن الكود الفعلي حقق العقود واجتاز الاختبارات المناسبة.

يمكن تجميد مواصفة معمارية قبل كتابة الكود.

لكن لا يجوز تقديم التجميد باعتباره إثباتًا للمتانة التشغيلية.

79. No Endless Review Rule

بعد C03، ينبغي أن تقتصر مراجعة التجميد التالية على العيوب التي:

تخلق تعارضًا مع قانون مجمد.

تترك مسار تنفيذ غير مفوض.

تسمح بفقدان التزام تعافٍ قانوني.

تسمح بافتراض حقيقة عالمية غير مثبتة.

تمنع تنفيذ العقد بصورة متماسكة بسبب غموض معياري جوهري.

أما التفاصيل الخاصة باختيار قواعد البيانات، وأدوات العزل، وإعدادات التخزين، ومكتبات التنفيذ، فلا تصبح عائقًا للتجميد ما دامت لا تغير ضمانات المعمارية.

ولا نعني بذلك تجاهل ثغرات حقيقية جديدة إذا ظهرت.

80. Freeze Decision Authority

لا تصبح C03 مجمدة بمجرد وجود معالجة نصية لكل Finding.

تحتاج إلى مراجعة عدائية لاحقة تحدد هل أغلقنا الأسباب الجذرية دون إدخال تعارضات جديدة.

PART XVI — C03 VERDICT
RDMS-09 C03

Review 03 blocking findings:
    8

Corrective contract groups:
    8

Additional proposed invariants:
    RDMS09-I95 ... RDMS09-I113

Targeted adversarial tests:
    12

FCA modification:
    NONE PROPOSED

RDMS-01...08 modification:
    NONE PROPOSED

Code implementation:
    NOT AUTHORIZED

Executable tests:
    NOT PERFORMED

Specification freeze:
    NOT AUTHORIZED

Next:
    RDMS-09 Adversarial Freeze Review 04
Final C03 Decision

RDMS-09 C03 — COMPLETE FOR REVIEW.

RDMS-09 — NOT FROZEN.

تتضمن C03 الآن عقودًا محددة لجميع النتائج الثماني السابقة.

ولا توجد ضمن هذه التصحيحات حاجة مقترحة لتغيير السلطة المركزية أو حالات Action القانونية أو محرك Triggers أو بقية الحدود المجمدة.

لكن هذه النتيجة تظل بحاجة إلى التحقق المعماري في المراجعة الرابعة.

Next Authorized Step: RDMS-09 — Adversarial Freeze Review 04.

أهم ما حققناه في C03

أرى أننا وصلنا الآن إلى مستوى جيد من الوضوح في منطق التعافي. وأهم القرارات هي:

أولًا: التعافي ليس استرجاع ملفات فقط. أصبح لدينا عقد تسليم بين استعادة البنية التحتية واستئناف Executive، مع ضرورة تقييم التغييرات التي حدثت أثناء الاستعادة.

ثانيًا: سلامة التاريخ لا تُستنتج من سلامة آخر Snapshot. قد تحتوي النسخة المستعادة على تاريخ صحيح لكنه ناقص. ولذلك أصبح اكتمال السجلات الخارجية شرطًا مستقلًا عندما يؤثر في قانونية استمرار العمل.

ثالثًا: منع التنفيذ يجب أن يحدث عند مصدر الأثر. فلا يكفي أن تعلن Executive أن Writer قديمة فقدت صلاحيتها إذا كانت تلك Writer ما زالت تستطيع الكتابة في التخزين. ولا يكفي إعلان Worker متوقفة إذا كان طلبها الخارجي ما زال قيد المعالجة.

رابعًا: حماية البيانات يجب أن تبدأ قبل استعمالها. فالبيانات التي استعيدت من Backup قديمة لا يجوز إرسالها إلى LLM أو Specialist أو نظام فهرسة قبل تحديد قيود المعالجة والإفصاح الحالية.

حالة المشروع
Specification	Status
FCA v1.0.1	✅ FROZEN
RDMS-01 → RDMS-08	✅ FROZEN
RDMS-09 Draft v1.0	✅ COMPLETE
RDMS-09 C01	✅ COMPLETE
RDMS-09 C02	✅ COMPLETE
RDMS-09 C03	✅ CORRECTIVE SPEC COMPLETE
RDMS-09 Freeze Review 04	⏳ NEXT
RDMS-10	⏳ PENDING

الخطوة التالية هي Adversarial Freeze Review 04. وسنجعلها مراجعة حاسمة ومحددة النطاق: سنختبر التناقضات بين العقود والسلطات القانونية، وليس التفاصيل التقنية التي يمكن تأجيلها للتنفيذ.

إذا لم نجد عيوبًا معمارية مانعة، فسيكون تجميد RDMS-09 ممكنًا على مستوى المواصفات، وبعدها ننتقل إلى RDMS-10.

END ORIGINAL MESSAGE

========================================================================
SOURCE PART: Adversarial Freeze Review 04 and final freeze decision
MESSAGE ID: 79d37199-2fe2-4973-bbe9-ac99b4bb5b34
BEGIN ORIGINAL MESSAGE
========================================================================

نبدأ الآن RDMS-09 — Adversarial Freeze Review 04، وهي المراجعة النهائية المقترحة قبل اتخاذ قرار تجميد مواصفة التعافي.

في المراجعات الثلاث السابقة اكتشفنا ثغرات تتعلق باستعادة السلطة، وفقدان تاريخ العمليات الخارجية، وتزامن التنفيذ، وسلامة البيانات المستعادة. ثم عالجناها عبر C01 وC02 وC03.

سأطبق هذه المرة معيارًا محددًا: لن نرفض التجميد بسبب تفاصيل تنفيذية يمكن حسمها لاحقًا، لكننا لن نقبل أي غموض يسمح بتجاوز السلطة القانونية، أو اختراع حالة غير مثبتة، أو تنفيذ أثر خارجي غير آمن.

RDMS-09 — Adversarial Freeze Review 04 — Final Architectural Review
RDMS-09
ADVERSARIAL FREEZE REVIEW 04
Final Architectural Integrity & Recovery Safety Review

Project: AI Coding Agent
Architecture: Formal Cognitive Architecture — FCA v1.0.1

Target Specification: RDMS-09
Review: Adversarial Freeze Review 04
Review Level: Formal Architectural Specification

Review Package

RDMS-09 Draft v1.0

RDMS-09 C01

RDMS-09 C02

RDMS-09 C03

FCA v1.0.1 — FROZEN

RDMS-01…08 — FROZEN

Implementation Status: NOT IMPLEMENTED
Executable Verification: NOT PERFORMED

PART I — REVIEW MISSION
1. Objective

تحدد هذه المراجعة ما إذا كانت RDMS-09 تمتلك عقودًا معمارية كافية للتحكم في التعافي دون تغيير القوانين المجمدة.

نختبر خمسة متطلبات أساسية:

Authority Safety

لا تستطيع عملية التعافي إنشاء سلطة قانونية منافسة أو استعادة سلطة انتهت.

State Integrity

لا يستطيع النظام اعتبار حالة قانونية مستعادة صحيحة إذا كانت الأدلة اللازمة لصحتها مفقودة.

World-Effect Safety

لا يستطيع التعافي افتراض توقف عملية خارجية أو فشلها دون دليل مناسب.

Recovery Continuity

لا تضيع الالتزامات المعتمدة أو آليات إعادة التفعيل بصورة صامتة أثناء الأعطال.

Trust & Data Safety

لا تؤدي الاستعادة إلى تفعيل محتوى غير موثوق أو كشف بيانات محظورة قبل استيفاء شروط استعمالها.

2. Acceptance Standard

يُقبل العقد عندما يحدد:

السلطة المسؤولة.

الحالة اللازمة قبل العملية.

أدلة السماح أو المنع.

نقطة فرض الشرط.

السلوك عند وقوع Crash.

سلوك العمليات المتزامنة.

نتيجة عدم توفر الأدلة.

لا يُشترط في هذه المرحلة اختيار محرك تخزين أو مكتبة أو نظام تشغيل محدد.

لكن يجب أن يكون العقد قابلًا للتنفيذ والتحقق دون تغيير معناه.

PART II — REVIEW OF THE EIGHT C03 FINDINGS
FR09-R3-G01 — Bootstrap Handoff Integrity
Previous Problem

يمكن استعادة Control Ledger بواسطة جهة تشغيلية مخولة، لكن ربما تتغير موارد تؤثر في المشروع أثناء الاستعادة.

C03 Correction

BootstrapHandoffProof

يحدد:

Authorized recovery principal
Performed infrastructure operations
Modified resources
Unknown change scope
Restoration evidence
Canonical reentry conditions
Adversarial Test

نفترض:

1. Control Ledger becomes unavailable.

2. External infrastructure operator restores it.

3. Operator changes a repository mount.

4. Cognitive Executive becomes available.

5. Executive attempts to resume an old plan.
Required Behavior

لا تستطيع Executive افتراض أن Repository لم تتغير.

يجب أن تمر التغييرات المعروفة والمجهولة عبر تقييم الاعتماديات المناسب.

كما لا يمكن لجهة Bootstrap اعتماد قرارات هندسية جديدة لمجرد امتلاكها صلاحية إصلاح البنية التحتية.

Review Assessment

العقد يعالج فصل السلطة بصورة صحيحة.

ولا يوجد تعارض ضروري مع FCA، بشرط أن تظل سلطة Bootstrap تشغيلية خارجية ومحدودة النطاق، لا قناة تنفيذ بديلة يستخدمها الوكيل.

VERDICT: PASS — SPECIFICATION LEVEL

FR09-R3-G02 — Acknowledged History Continuity
Previous Problem

قد تختفي أحداث معتمدة من نسخة احتياطية قديمة، رغم أن آثارها الخارجية حدثت.

C03 Correction

AcknowledgedHistoryContinuity

يفصل بين:

Trusted Acknowledged Frontier

Recovered Control Frontier

Recovered Action Journal Frontier

Missing Event Ranges

Uncertain Event Ranges

External Effect Coverage
Adversarial Test
Event 1000 committed.

Action dispatched externally.

Storage destroyed.

Backup ending at Event 950 restored.
Required Behavior

إذا كان لدينا دليل موثوق بأن التاريخ وصل إلى Event 1000، فالفجوة واضحة.

أما إذا فقدنا أيضًا دليل Event 1000، فلا نستطيع الاستنتاج بأن Event 950 هو نهاية التاريخ الحقيقي.

يجب عدم اعتبار السجل المستعاد كاملًا إلا ضمن نطاق تدعمه الأدلة ونموذج الأعطال المعلن.

Critical Safety Question

ماذا لو لم نستطع تحديد المجالات التي حدثت فيها العمليات المفقودة؟

في هذه الحالة يجب استخدام نطاق محافظ أوسع.

لا يجوز تضييق نطاق الحجب اعتمادًا على غياب السجلات التي نحاول أصلًا إثبات اكتمالها.

Review Assessment

C03 تحدد السلوك الآمن:

History unknown
    ↓
Do not assert completeness
    ↓
Identify possible effect domains
    ↓
Block conflicting continuation

إذا تعذر إثبات نطاق أضيق، تبقى العمليات الخارجية المحتملة التأثر محجوبة ضمن نطاق أوسع.

VERDICT: PASS — SPECIFICATION LEVEL

FR09-R3-G03 — Cross-Frontier Enforcement
Previous Problem

قد تكون السلطة والسياسات صحيحة أثناء التقييم، ثم تتغير قبل تنفيذ العملية.

C03 Correction

CrossFrontierAdmissionProof

مع إعادة فحص الشروط المؤثرة عند الحدود القانونية.

Adversarial Test
T1:
    Recovery validates Security Policy v8.

T2:
    Security Policy v9 becomes authoritative.

T3:
    Action attempts authorization under v8.
Required Behavior

يجب تطبيق السياسة القانونية النافذة عند نقطة اعتماد العملية.

لا تستطيع Recovery Admission قديمة منح استثناء دائم من الشروط الجديدة.

Concurrency Analysis

لا نفترض وجود معاملة ذرية عالمية بين جميع الخدمات الخارجية.

لكن يجب الحفاظ على الضمانات القانونية للانتقالات التي يتحكم فيها النظام.

أما تغير العالم الخارجي بعد dispatch، فلا يمكن محوه بمجرد إعادة فحص السياسة.

تظل هذه الحالة خاضعة إلى RDMS-04.

Review Assessment

لا يوجد تعارض مع نموذج السلطة.

وقد جرى فصل:

Recovery eligibility assessment

عن:

Legal action authorization

بصورة مناسبة.

VERDICT: PASS — SPECIFICATION LEVEL

FR09-R3-G04 — Possible External Effect Safety
Previous Problem

قد تتوقف Worker قديمة بينما تستمر عملية أرسلتها إلى خدمة خارجية.

C03 Correction

PossibleExternalEffectAssessment

يحدد الآثار المؤكدة والمحتملة وغير المعروفة، ثم يقيّم سلامة العمليات اللاحقة.

Adversarial Test
Old Worker:
    Sends payment request.

Worker crashes.

New Executive:
    Reconciles available records.

No payment confirmation found.

New Executive:
    Considers retry.
Required Behavior

عدم العثور على Confirmation لا يثبت فشل العملية.

يمكن أن يكون الطلب:

Still queued

Already executed

Partially executed

Not transmitted

لا يسمح بإعادة المحاولة إلا وفق شروط RDMS-04.

Review Assessment

C03 لا تدعي Exactly-Once External Effects دون ضمان من النظام الخارجي.

ولا تسمح بتحويل توقف Worker إلى إثبات توقف الأثر.

كما أن شرط السلامة تحت جميع الحالات الممكنة ذات الصلة يمنع استبعاد احتمال خطير دون دليل.

VERDICT: PASS — SPECIFICATION LEVEL

FR09-R3-G05 — Restore Containment
Previous Problem

قد تؤدي عملية Restore نفسها إلى تشغيل Hooks أو تغيير خدمات حية قبل فحص المحتوى المستعاد.

C03 Correction

RestoreContainmentProof

يقيّم:

Destination scope

Writable mounts

Reachable services

Automatic activation paths

Executable configurations

Credential exposure

Containment guarantees
Adversarial Test
Recovery restores files
into an active service directory.

A file watcher detects changes.

Service automatically loads new configuration.
Required Behavior

لا يجوز اعتبار العملية آمنة لمجرد أنها تحمل اسم Restore.

يجب تقييم آثارها القابلة للوصول.

إذا تعذر إثبات العزل المطلوب، فلا يسمح باستعمال المسار السريع EPHEMERAL_SANDBOX.

Review Assessment

العقد متوافق مع FCA-I48، التي تربط تصنيف الأفعال بالآثار القابلة للوصول وليس بأسماء العمليات.

VERDICT: PASS — SPECIFICATION LEVEL

FR09-R3-G06 — Restored Data Processing Safety
Previous Problem

قد تصل بيانات محذوفة إلى Provider أو Specialist قبل تطبيق سياسة المنع الحالية.

C03 Correction

RestoredDataProcessingAdmission

Adversarial Test
Old backup restored.

Sensitive document becomes accessible.

Memory index rebuild begins.

Indexing provider receives content.

Erasure restrictions applied afterward.
Required Behavior

يجب أن تكون المعالجة والإفصاح محكومين قبل إرسال المحتوى أو استعماله في مسار غير مصرح.

إذا كانت سياسة الحذف الحالية غير معروفة، فلا يجوز افتراض أن سياسة Backup القديمة كافية.

Review Assessment

العقد يفصل بصورة صحيحة بين:

Internal processing needed for recovery

و:

External disclosure or general cognitive use

كما يحافظ على حوكمة RDMS-07 بدل إنشاء سياسة ذاكرة منافسة.

VERDICT: PASS — SPECIFICATION LEVEL

FR09-R3-G07 — Canonical Schema Cutover
Previous Problem

قد تصبح Schema جديدة معتمدة، بينما تواصل Writer قديمة تعديل البيانات وفق Schema سابقة غير متوافقة.

C03 Correction

SchemaCutoverEnforcement

Adversarial Test
Schema v3 becomes authoritative.

Writer v2 remains connected.

Writer v2 attempts a canonical mutation.
Required Behavior

يجب رفض الكتابة إذا لم تكن Writer متوافقة مع Schema القانونية الحالية.

ولا يكفي مجرد تحديث إعدادات Runtime الجديدة.

يجب فرض التوافق في حدود الكتابة الموثوقة.

Additional Test

ماذا لو بدأت Writer القديمة عملية كتابة قبل Cutover ولم تُحسم نتيجتها بعده؟

يجب تقييم هذه الكتابة ضمن شروط Migration وآثارها الممكنة.

ولا يجوز اعتبار انتهاء صلاحية Writer دليلًا على أن كتابة سبق إرسالها لم تحدث.

Review Assessment

C03 تربط:

Authoritative schema visibility

بـ:

Legal write eligibility

دون إنشاء Canonical State ثانية.

VERDICT: PASS — SPECIFICATION LEVEL

FR09-R3-G08 — Durable Recovery Continuation
Previous Problem

قد تُعلق مهمة تحتوي على Action غير محسومة، ثم تضيع آلية إعادة تفعيلها بسبب Crash.

C03 Correction

RecoveryContinuationDurability

Adversarial Test A
External Action = IN_DOUBT

Recovery suspends task.

Crash occurs before Trigger persistence.
Required Behavior

لا يجوز الادعاء بأن التعليق قابل للاستئناف تلقائيًا إذا لم يثبت حفظ Commitment المطلوبة.

إذا كانت Control Ledger غير متاحة، يجب أن يظل هذا العجز ظاهرًا، ويُستخدم مسار استعادة تشغيلية مخول عند الحاجة.

Adversarial Test B
Trigger event observed.

Crash before canonical reaction commit.

Event redelivered.
Required Behavior

يجب ألا يفقد النظام التفاعل المطلوب بصمت.

وعندما يكون المصدر Replayable، يمكن إعادة اكتشاف الحدث.

أما إذا اعتمد رد الفعل مسبقًا ثم أعيد تسليم الحدث، فيجب منع تكرار اعتماده القانوني.

Review Assessment

العقد يحافظ على:

FCA-I37: ذرية بيانات التحكم اللازمة للتعافي.

FCA-I38: إزالة تكرار ردود Triggers.

FCA-I39: عدم اختلاق أحداث غير قابلة لإعادة التشغيل.

VERDICT: PASS — SPECIFICATION LEVEL

PART III — CROSS-COMPONENT ADVERSARIAL TESTS

الآن نختبر الحالات التي تتداخل فيها عدة عقود.

AC09-R4-01 — Disaster Restore + Lost Payment History
Attack
Old backup restored
        ↓
Recent Action Journal missing
        ↓
External payment may have occurred
        ↓
Executive attempts payment again
Guards

AcknowledgedHistoryContinuity

ExternalHistoryCoverageProof

PossibleExternalEffectAssessment

RDMS-04 ActionGate

Result

إذا لم يمكن إثبات عدم حدوث العملية أو أمان تكرارها، تُمنع إعادة المحاولة المتعارضة.

PASS BY CONTRACT

AC09-R4-02 — Bootstrap + Old Executive Epoch
Attack

تنجح استعادة التخزين، لكن Leadership Service تعرض Epoch قديمة.

Guards

BootstrapHandoffProof

AuthorityAntiRollbackAssessment

RecoveryAuthorityFrontier

RDMS-01 Fencing

Result

لا تُستعاد سلطة Executive اعتمادًا على Snapshot قديمة وحدها.

إذا تعذر إثبات القيادة الحالية، لا يُسمح بآثار قانونية جديدة.

PASS BY CONTRACT

AC09-R4-03 — Malicious Backup + Automatic Execution
Attack

يحتوي الملف المستعاد على Configuration تؤدي إلى تنفيذ Script خبيثة.

Guards

RestoreContainmentProof

RecoveryArtifactQuarantine

ContentTrustContext

RDMS-04 Effect Classification

Result

لا يُفعّل المحتوى قبل التحقق المناسب.

وإذا كانت عملية Restore نفسها قادرة على إحداث تأثيرات مشتركة، تخضع لمسار الأثر الملائم.

PASS BY CONTRACT

AC09-R4-04 — Deleted Data + Provider Fallback
Attack

تُستعاد بيانات محظورة.

يتعطل Provider المحلي.

تحاول Recovery إرسال Context إلى Provider خارجية بديلة.

Guards

ErasureAntiRollbackFrontier

RecoveryDisclosureBarrier

RestoredDataProcessingAdmission

RDMS-07 Data Governance

Result

تغيير Provider لا يزيل قيود الإفصاح.

PASS BY CONTRACT

AC09-R4-05 — Schema Cutover + Old Writer
Attack

تُعتمد Schema جديدة، لكن Writer قديمة ما زالت متصلة بالتخزين.

Guards

CanonicalSchemaVisibilityContract

SchemaCutoverEnforcement

RDMS-01 Version/Fencing Checks

Result

لا تُقبل كتابة غير متوافقة ضمن Canonical State.

PASS BY CONTRACT

AC09-R4-06 — Trigger Replay + Action Dispatch
Attack

يُعاد تسليم Trigger سبق أن اعتمدت Reaction الخاصة بها.

تحاول Reaction الجديدة إنشاء Action خارجية مكررة.

Guards

TriggerRecoveryOrdering

RecoveryContinuationDurability

RDMS-05 Reaction Identity

RDMS-04 Action Identity

Result

إزالة تكرار التفاعل القانوني لا تعني تلقائيًا ضمان Exactly-Once خارجي.

يجب أن تخضع أي Action خارجية لشروط هويتها وتسويتها.

PASS BY CONTRACT

AC09-R4-07 — Old Worker + New Recovery Compensation
Attack
Old Worker may still dispatch X.

New Recovery proposes compensation Y.
Guards

DispatchQuiescenceAssessment

PossibleExternalEffectAssessment

ActionRecoveryOwnership

RDMS-04 Reconciliation

Result

إذا تعذر إثبات أن Y آمنة تحت حالات X الممكنة، تُمنع.

PASS BY CONTRACT

AC09-R4-08 — Recovery Admission + Security Revocation
Attack

تجتاز Recovery فحوص السلامة.

ثم تُلغى صلاحية مهمة قبل إرسال Action جديدة.

Guards

CrossFrontierAdmissionProof

RecoveryAdmissionBinding

Current Executive Epoch

ActionGate

Result

لا يمكن الاعتماد على تصريح Recovery قديم لتجاوز القيد النافذ عند نقطة التفويض القانوني.

PASS BY CONTRACT

AC09-R4-09 — Crash During Suspension
Attack

تحاول Recovery تعليق مهمة مع Action غير محسومة، لكن التخزين يتعطل أثناء الحفظ.

Guards

RecoveryContinuationDurability

Atomic Control Transition

Recovery Bootstrap Rules

Result

لا يُعلن تعليق قابل للاستئناف دون إثبات حفظ الالتزامات اللازمة.

PASS BY CONTRACT

AC09-R4-10 — Compromised Recovery Logs
Attack

تحتوي Logs المستعادة على تعليمات مزيفة تأمر بتجاوز ActionGate.

Guards

RecoveryContentTrustPreservation

FCA ContentEnvelope

Trusted Executive Authorization

Result

لا تكتسب Logs سلطة تعليمات لأنها استُعيدت من ملف تشخيصي.

PASS BY CONTRACT

AC09-R4-11 — Complete Trust-Anchor Loss
Attack

تُفقد Control Ledger ومراجع الثقة والنسخ الاحتياطية الموثوقة.

تحاول Recovery إعلان استعادة ناجحة اعتمادًا على بيانات لا تستطيع التحقق من أصلها.

Guards

RecoveryTrustAnchorAssessment

RecoveryAuthorityFrontier

BootstrapHandoffProof

ScopedRecoveryAdmission

Result

لا يُعلن تعافٍ قانوني كامل.

تبقى العمليات التي تحتاج إلى سلطة أو تاريخ غير قابلين للإثبات محجوبة.

PASS BY CONTRACT — SAFE NON-RECOVERY

AC09-R4-12 — Repeated Crash During Reconciliation
Attack

تحدث ثلاثة أعطال متتالية أثناء محاولة تسوية Action بحالة IN_DOUBT.

Guards

RecoveryCase Identity

RecoveryOwnershipLease

RecoveryProgressControl

Durable Recovery Obligations

RDMS-04 Action Journal

Result

لا يجوز أن تمحو إعادة التشغيل التزام التسوية المعتمد أو تسمح بإعادة إرسال Action بصورة عمياء.

إذا فُقد التخزين الضروري نفسه، تدخل الحالة مسار Bootstrap والاستعادة الموثوقة، ولا يُدّعى ضمان استمرارية لم يثبت.

PASS BY CONTRACT

PART IV — GLOBAL CONSISTENCY REVIEW
1. Authority Model

راجعنا وجود أي سلطة جديدة قادرة على تجاوز Executive أو البوابات القانونية.

Findings

Recovery Coordinator تنسق ولا تعتمد قرارات هندسية.

Bootstrap Principal تملك تفويضًا تشغيليًا خارجيًا محدودًا.

RecoveryAdmissionBinding ليست CommitGate مستقلة.

SchemaCutoverEnforcement يفرض صلاحية الكتابة ولا ينشئ Canonical State ثانية.

RESULT: NO DIRECT AUTHORITY CONFLICT IDENTIFIED

2. Canonical State Model

لا توجد حاجة لإضافة:

New canonical cognitive workspace

Second decision ledger

Alternative executive identity

Parallel legal state machine

أوضاع Recovery تبقى تشغيلية، ولا تستبدل حالات FCA.

RESULT: CONSISTENT AT SPECIFICATION LEVEL

3. World Action Model

تحافظ RDMS-09 على:

AUTHORIZED

DISPATCH_INTENT

RESULT_REPORTED

EFFECT_VERIFIED

PARTIAL

FAILED

IN_DOUBT

RECONCILING

RECONCILED

وفق المعاني المجمدة في FCA/RDMS-04.

لا تؤسس Recovery حالة جديدة تسمح بإعادة تنفيذ عملية غير محسومة دون أدلة.

RESULT: CONSISTENT

4. Temporal Model

تستخدم RDMS-09 آليات RDMS-05، ولا تنشئ Scheduler ثانية.

تظل الأحداث وإعادة تسليمها واستجاباتها القانونية محكومة بهوياتها وحدود الذرية.

RESULT: CONSISTENT

5. Dependency Model

تستخدم RDMS-09 محرك RDMS-06 لتحديد ما أصبح غير صالح بعد الاستعادة.

لا تؤدي أي عملية Restart تلقائيًا إلى إبطال جميع نتائج المشروع.

لكن نقص الأدلة يمنع استنتاج الصلاحية الكاملة.

RESULT: CONSISTENT

6. Memory and Data Governance

تبقى حوكمة الذاكرة داخل RDMS-07.

ولا تؤدي إعادة بناء Index أو استعادة Episode إلى اعتماد معرفة جديدة تلقائيًا.

كما أن استعادة Backup قديمة لا تعيد صلاحية استعمال بيانات محظورة.

RESULT: CONSISTENT

PART V — NORMATIVE FREEZE INTERPRETATIONS

هذه توضيحات تفسيرية ملزمة عند قراءة حزمة RDMS-09 المجمعة.

لا تضيف سلطة أو State جديدة.

FC09-04-01 — Unknown Recovery Scope

إذا كانت هناك فجوة تاريخية أو أثر خارجي مجهول، ولم يمكن إثبات نطاق تأثير ضيق، يجب استخدام نطاق محافظ أوسع.

لا يجوز اعتبار عدم وجود سجل دليلًا على أن المورد مستقل عن الحادث.

FC09-04-02 — Recovery Authorization Is Not Permanent

كل Recovery Admission مقيدة بالنطاق والشروط التي استندت إليها.

لا تمنح إعفاءً دائمًا من فحص السلطة والسياسات والاعتماديات عند حدود التنفيذ.

FC09-04-03 — No External Effect Cancellation Guarantee

إبطال Epoch أو إيقاف Worker أو تغيير Credential لا يثبت بذاته أن العملية الخارجية توقفت أو أن أثرها لم يحدث.

تبقى شروط RDMS-04 واجبة التطبيق.

FC09-04-04 — No Fabricated Recovery Durability

إذا تعذر حفظ التزام التعافي أو إثبات تاريخ التحكم، فلا يجوز تقديم الحالة بوصفها مستعادة بالكامل أو معلقة مع ضمان استئناف آلي.

قد يتطلب التعافي تدخلًا تشغيليًا مخولًا.

PART VI — REMAINING IMPLEMENTATION OBLIGATIONS

لم نجد ضمن النطاق المراجع ثغرة معمارية جديدة توجب إعادة فتح FCA.

لكن توجد التزامات تنفيذية مهمة.

EO09-01 — Storage Durability

يجب إثبات أن backend التخزين تحقق شروط durable acknowledgement وفق نموذج الأعطال المعلن.

EO09-02 — Actual Fencing

يجب إثبات أن الكتابة إلى Canonical State والـAction Dispatch تخضع للـEpoch وGeneration الصحيحتين.

EO09-03 — Restore Containment

يجب اختبار حدود الاستعادة في البيئة الفعلية، بما في ذلك Scripts وHooks والخدمات المتصلة.

EO09-04 — Action Reconciliation

يجب اختبار حالات فقدان نتائج العمليات الخارجية وعدم تكرارها دون مسوغ.

EO09-05 — Trigger Persistence

يجب اختبار Crash قبل وبعد اعتماد Reaction وقبل وبعد تقدم Source Cursor.

EO09-06 — Data Suppression

يجب اختبار جميع مسارات الإفصاح ذات الصلة، وليس واجهة Retrieval فقط.

EO09-07 — Schema Migration

يجب إثبات أن Writers غير المتوافقة لا تستطيع الكتابة بعد Cutover.

EO09-08 — Repeated Recovery Failures

يجب اختبار التعافي من أعطال متكررة دون فقدان الالتزامات أو إنشاء سلطة جديدة.

هذه التزامات مطابقة لاحقة.

فشل تنفيذ أحدها سيعني أن التنفيذ لا يطابق المواصفة، حتى لو كانت المواصفة نفسها مجمدة.

PART VII — REVIEW RESULTS
1. Previous Findings
Finding	Final assessment
R3-G01 — Bootstrap Handoff	CLOSED BY SPECIFICATION
R3-G02 — History Continuity	CLOSED BY SPECIFICATION
R3-G03 — Cross-Frontier Enforcement	CLOSED BY SPECIFICATION
R3-G04 — External Effect Safety	CLOSED BY SPECIFICATION
R3-G05 — Restore Containment	CLOSED BY SPECIFICATION
R3-G06 — Restored Data Processing	CLOSED BY SPECIFICATION
R3-G07 — Schema Cutover	CLOSED BY SPECIFICATION
R3-G08 — Durable Continuation	CLOSED BY SPECIFICATION
2. Review Summary
RDMS-09 — ADVERSARIAL FREEZE REVIEW 04

Previous blocking findings reviewed:
    8

Previous findings closed at specification level:
    8

Cross-component attack scenarios:
    12

Architectural authority conflicts identified:
    0

New specification-level blockers identified:
    0

Normative freeze interpretations:
    4

Required implementation obligation groups:
    8

Executable tests:
    0

Production implementation:
    NOT STARTED / NOT VERIFIED
3. Scope of PASS

يجب أن يكون معنى PASS دقيقًا.

المراجعة تثبت أن التصميم، وفق الافتراضات وحدود الأعطال والسلطات التي يعلنها، يحتوي على عقود متسقة تمنع الاستمرار غير المبرر عند نقص الأدلة.

لكنها لا تثبت:

أن التخزين الفعلي سيحافظ على جميع الأحداث.

أن الخدمة الخارجية تدعم Exactly-Once.

أن جميع أنواع الهجمات أو الأعطال قد اكتُشفت.

أن التنفيذ سيكون خاليًا من Race Conditions.

أن النظام يستطيع التعافي آليًا من أي كارثة.

أن كل البيانات المحذوفة يمكن إزالتها من جهات خارجية.

هذه ادعاءات لا تسمح بها الأدلة الحالية.

PART VIII — FINAL ARCHITECTURAL VERDICT
1. Freeze Decision

بعد مراجعة:

Draft v1.0

C01

C02

C03

جميع الثغرات السابقة

العلاقات بين السلطات

حدود التنفيذ والتعافي

السيناريوهات المركبة

لم تظهر ثغرة معمارية مانعة جديدة ضمن نطاق المراجعة المحدد.

العقود الحالية تحقق الفصل المطلوب بين:

Recovered Data
    ≠
Valid Canonical State
    ≠
Current Authority
    ≠
Known External Reality

كما أنها لا تمنح Recovery سلطة لتجاوز CommitGate أو ActionGate.

2. Final Verdict
RDMS-09 — PASS

ADVERSARIAL FREEZE REVIEW 04: PASS AT SPECIFICATION LEVEL

RDMS-09: FROZEN — SPECIFICATION LEVEL

يشمل خط الأساس المجمد:

RDMS-09 Draft v1.0

RDMS-09 C01

RDMS-09 C02

RDMS-09 C03

RDMS-09 Freeze Interpretations:
    FC09-04-01
    FC09-04-02
    FC09-04-03
    FC09-04-04
3. Frozen Architectural Identity

RDMS-09 defines a governed recovery and lifecycle architecture that restores or constrains system operation according to proven authority, state integrity, dependency validity, data restrictions and external-effect uncertainty, without creating an independent cognitive authority or bypassing canonical action and commit controls.

4. Implementation Status
Architecture:
    FROZEN AT SPECIFICATION LEVEL

Implementation:
    NOT AUTHORIZED BY THIS REVIEW

Runtime Verification:
    PENDING

Failure Injection:
    PENDING

Storage Durability Proof:
    PENDING

Action Reconciliation Tests:
    PENDING
5. Next Authorized Step

RDMS-10 — Final Runtime Integration, Component Boundaries & Implementation Contracts

FINAL STATUS
Specification	Status
FCA v1.0.1	FROZEN
RDMS-01	FROZEN
RDMS-02	FROZEN
RDMS-03	FROZEN
RDMS-04	FROZEN
RDMS-05	FROZEN
RDMS-06	FROZEN
RDMS-07	FROZEN
RDMS-08	FROZEN
RDMS-09	FROZEN
RDMS-10	NEXT

RDMS-09 — CLOSED / FROZEN AT SPECIFICATION LEVEL.

ماذا يعني نجاح RDMS-09؟

أهم نتيجة حققناها هي أننا حددنا سلوك النظام عند فقدان القدرة على التأكد من الحقيقة.

تخيل أن وكيلنا يعمل على مشروع برمجي ضخم، وأجرى تعديلات عديدة، ثم تعطل الجهاز أثناء عملية نشر.

بعد إعادة التشغيل، قد يعرف الوكيل أن النشر كان مخططًا له، وقد يستعيد سجلات تؤكد إرسال الأمر، لكنه لا يعرف هل اكتملت العملية الخارجية.

النظام الذي صممناه لن يعتبر النشر ناجحًا أو فاشلًا من تلقاء نفسه. سيبحث عن أدلة، ويحاول التسوية، وإذا تعذر إثبات النتيجة فسيحافظ على عدم اليقين ويمنع الأعمال التي تتطلب معرفة النتيجة.

وفي المقابل، يمكنه مواصلة أعمال أخرى ثبت أنها لا تتأثر بالعملية غير المحسومة.

هذه القدرة على التعافي الجزئي الآمن مهمة جدًا لوكيل برمجي يعمل على مشاريع كبيرة ولمدد طويلة.

أين وصلنا في المشروع؟
المرحلة	الحالة
Formal Cognitive Architecture	✅ FROZEN
RDMS-01 → RDMS-07	✅ FROZEN
RDMS-08 — Cognitive Executive	✅ FROZEN
RDMS-09 — Recovery & Resilience	✅ FROZEN
RDMS-10 — Final Runtime Integration	⏳ NEXT
المراجعة المعمارية الشاملة	⏳ PENDING
التصميم البرمجي التفصيلي	⏳ PENDING
التنفيذ والاختبارات	⏳ PENDING

الخطوة التالية هي RDMS-10.

وفيها سننتقل من تصميم الأنظمة منفصلة إلى تحديد كيفية اندماجها في منظومة واحدة: المكونات الفعلية، ملكية كل مكون، واجهات التواصل، حدود العمليات، عقود البيانات، وتسلسل التشغيل والتعافي.

وستكون هذه مرحلة مهمة جدًا؛ لأنها ستكشف ما إذا كانت المواصفات التسع المجمدة قادرة على العمل معًا دون ازدواجية في السلطة أو تضارب بين المسؤوليات.

END ORIGINAL MESSAGE
````

