# L7 RUNTIME INTEGRATION

**Document status: REVIEW CANDIDATE; BASELINE/FIELD AUDIT LIMITS RECORDED; NOT FROZEN.** Source baselines retain their recorded specification freeze; this consolidation has no new freeze authority. Production implementation is not authorized.

L7 owns integration and transport contracts. It connects canonical owners and enforces their admission contracts at receiving boundaries. It has no independent cognitive, canonical-commit, action, temporal, freshness, learning or recovery authority.

Each source-backed article is current only within its stated scope. Imported contracts retain the named owner; storage, delivery and scheduling do not create additional authorization. Source text remains unchanged in the archive. Source spelling and optionality are preserved; unspecified serialization types are not invented.


## Imported and exported boundaries

| Contract / responsibility | Canonical owner | This layer's obligation |
|---|---|---|
| Foundation and content/authority conservation | [L0](../architecture/L0_FOUNDATION.md) | Carry trusted metadata without granting authority to content. |
| ControlTransaction, CommitGate and durability | [L1](../architecture/L1_CONTROL.md) | Route owner-authorized mutation; delivery acknowledgement is not canonical commit. |
| Executive, canonical CapabilityResult and finalization | [L2](../architecture/L2_COGNITION.md) | Keep transport result distinct; submit proposals for adoption. |
| ActionGate, Action Journal, observations and evidence | [L3](../architecture/L3_ACTIONS.md) | Separate admission, external dispatch, observation and reconciliation. |
| TriggerCondition, specialists and one dependency engine | [L4](../architecture/L4_TEMPORAL_SPECIALISTS.md) | Deliver requests without authorizing execution or duplicating scheduling. |
| Canonical MemoryRetrievalResult and LearningGate | [L5](../architecture/L5_MEMORY.md) | Preserve semantic payload, provenance, trust and applicability. |
| Recovery admission, capsule integrity and restore policy | [L6](../architecture/L6_RECOVERY.md) | Activation requires current scoped admission; transport cannot expand it. |


## Effective amended responsibilities

Articles below contain the operative source clauses in their authorized scope, with historical findings, review narratives and replaced record specimens omitted. Record fields are maintained once in the owning contract section. Later hardening supplements earlier duties; it does not repeal an earlier duty without an explicit replacement.


### L7-A24-U001 — 1. Objective

تعالج هذه الوثيقة الثغرات التي تظهر عند دمج الأنظمة المختلفة داخل Runtime واحدة.

لدينا بالفعل:

Cognitive Executive.

Canonical Cognitive Workspace.

Capability Runtime.

Reasoning Gateway.

CommitGate.

ActionGate.

Control Ledger.

Action Journal.

Reality Executor.

Observation Ingress.

Dependency Evaluation.

Specialist Runtime.

Memory Runtime.

Temporal Scheduler.

Recovery Runtime.

لكن مجرد وجود هذه المكونات لا يضمن سلامة تكاملها.

المطلوب هو أن تكون جميع العمليات الحاملة للسلطة أو المؤثرة في الحالة قابلة للتتبع والتحقق، من لحظة اقتراحها حتى تسجيل نتيجتها.

Source: [RDMS-10-M24-U001](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2909>); source-unit SHA-256 `8ed9070957557bc0afc3ec1aba764260b0c977ce6dd7cda9675aa5b84f6565eb`.

### L7-A24-U002 — 2. Fundamental Integration Principle

نعتمد:

Authority, identity, state version and effect scope must survive every component boundary.

أي:

يجب أن تظل السلطة والهوية ونسخة الحالة ونطاق التأثير محفوظة عبر جميع حدود المكونات.

مثال:

Executive authorizes Action X
             ↓
ActionGate validates X
             ↓
Action Journal persists X
             ↓
Queue delivers X
             ↓
Executor executes X
             ↓
Observation records effect of X

يجب أن تبقى هوية X ومعنى التفويض ثابتين خلال هذا المسار.

لا يجوز أن يصبح X عملية أخرى بسبب تحويل بيانات أو إعادة إرسال رسالة أو اختلاف Provider.

Source: [RDMS-10-M24-U002](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2949>); source-unit SHA-256 `55686b165a28074587109526b7e72cc33c0b3ed135de5d87b464d8be360c6f67`.

### L7-A24-U003 — 3. Legal Ownership Conservation

تبقى ملكية السلطة كما يلي:

Responsibility	Canonical authority
Semantic authorization	Current Cognitive Executive
Canonical state mutation	CommitGate
World-action authorization	ActionGate
Control durability	Control Ledger
Action lifecycle	RDMS-04
Raw observation append	Observation Ingress
Dependency freshness	RDMS-06
Memory promotion	LearningGate + Executive
Temporal commitments	RDMS-05
Recovery orchestration	RDMS-09

لا تنشئ RDMS-10 أي سلطة إضافية فوق هذه السلطات.

Source: [RDMS-10-M24-U003](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2977>); source-unit SHA-256 `1bb914f8f865abe5832b7a9d9211d70b83d29060210caf7c3861b3ae405700a5`.

### L7-A24-U004 — 4. Integration-Level Rule

كل عقد جديد في C01 يجب أن يكون واحدًا من الأنواع التالية:

Transport Contract

Authority Binding

Canonical Projection

Integration Transaction

Validation Assessment

Recovery Binding

هذه عقود تكامل.

ليست كيانات معرفية قانونية جديدة إلا إذا كان تعريفها مطلوبًا صراحة من المواصفة المالكة.

Source: [RDMS-10-M24-U004](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2995>); source-unit SHA-256 `d267eaa9c22d7c2eeff3d9b64cf262c886acdcf09098f13c9754c7d5152842ae`.

### L7-A24-U007 — 6. Architectural Decision

نعتمد مبدأ:

Canonical types have one semantic owner. Integration contracts may reference or project them, but cannot redefine them.

أي أن لكل نوع قانوني مصدر تعريف واحدًا.

يمكن للواجهات استعماله أو اشتقاق تمثيل نقل منه.

لكن لا يجوز إعادة تعريف معناه.

Source: [RDMS-10-M24-U007](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3036>); source-unit SHA-256 `e93e57d799294ebcaf9646767a5957ebdba2e625681c00654f56cd99390d8778`.

### L7-A24-U008 — 7. CanonicalContractRegistry

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U008](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3048>); source-unit SHA-256 `756a49a85a51c12d5169370471ee89376d97b067c74cfa015da0cf36449c1b09`.

### L7-A24-U009 — 8. Registry Authority

هذا السجل لا يملك سلطة قانونية مستقلة.

هو مرجع تكامل يربط العقود بتعريفاتها المجمدة.

إذا وجد تعارض بين:

RDMS-04 ActionLifecycle

و:

RDMS-10 Action transport projection

فإن RDMS-04 هي المصدر المعياري للمعنى.

لا يجوز لـRDMS-10 تعديل معنى ActionLifecycle بهدف جعل التكامل أسهل.

Source: [RDMS-10-M24-U009](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3072>); source-unit SHA-256 `4700b81ba9cab025272a39c9c916c62284f9ef2c494e867302ac417248c6328a`.

### L7-A24-U010 — 9. Contract Categories

نميز بين:

Canonical Entity

كيان قانوني معتمد.

Command

طلب لتنفيذ انتقال أو عملية.

Event

تسجيل لحدث وقع ضمن نطاق معين.

Read Projection

تمثيل مخصص للقراءة مشتق من الحالة المعتمدة.

Assessment

نتيجة تقييم يمكن أن تكون صالحة أو قديمة أو غير مكتملة.

Transport Envelope

غلاف يحمل البيانات عبر حدود المكونات.

هذه الأنواع ليست قابلة للاستبدال تلقائيًا.

Source: [RDMS-10-M24-U010](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3090>); source-unit SHA-256 `a5b9f2f444d81bf5b0f816ce4dbefeba222e68000fd20bfd38063a095b3c16cb`.

### L7-A24-U011 — 10. Contract Compatibility Rule

لا تقبل واجهة Contract غير متوافقة مع النسخة القانونية التي تعتمد عليها.

إذا كانت العلاقة بين نسختين غير معروفة:

Compatibility = UNKNOWN
        ↓
Authority-bearing transition = REJECTED

لا يجوز استخدام Parser متساهل لتغيير معنى حقل قانوني.

C01-A1 Result

FR10-G02 — ADDRESSED

Source: [RDMS-10-M24-U011](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3120>); source-unit SHA-256 `a3f376fa06a3ea426413ffb3ca0aae773e8c9659ce6af7a4dbe4fa9f96168095`.

### L7-A24-U014 — 12. Architectural Decision

Transported authority claims are not trusted authority proofs.

وجود ادعاء بالسلطة داخل رسالة لا يثبت صحة الادعاء.

يجب إصدار بيانات السلطة الموثوقة أو التحقق منها عبر Control Boundary مناسبة.

Source: [RDMS-10-M24-U014](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3153>); source-unit SHA-256 `5503d4f04f1bce176b9cba6387a5f4eb77d93dd0be4e7e27b1a50f15f360163a`.

### L7-A24-U015 — 13. TrustedEnvelopeAdmission

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U015](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3161>); source-unit SHA-256 `631d25a04619ab4452db804688fed0e22ca85bb3aff7cebcac1566620bafa65a`.

### L7-A24-U016 — 14. Trusted Field Ownership

لا يجوز لـProvider أو Specialist غير مخولة إصدار:

Executive Authorization

Commit Authorization

ActionGate Approval

System Instruction Authority

Leadership Grant

Canonical State Version

بوصفها بيانات موثوقة.

قد يحتوي Payload على نص يقترح هذه القيم أو يشير إليها، لكنه لا يتحول إلى إثبات لها.

Source: [RDMS-10-M24-U016](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3189>); source-unit SHA-256 `8a8168983eff94ed1b80ffaf2480f85d51b3fd497de6b266742d6f0103b97698`.

### L7-A24-U017 — 15. Receiving Boundary Enforcement

عند استقبال رسالة تحمل أثرًا قانونيًا، يجب التحقق من:

Authenticated source

Allowed message type

Effective authority scope

Current epoch where required

Project binding

Schema compatibility

Payload integrity

ويجب رفض الانتقال القانوني عندما لا تتوفر الأدلة المطلوبة.

Source: [RDMS-10-M24-U017](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3209>); source-unit SHA-256 `e1e16604ce49f86bf7bf404cfa3a9f38f44c748ecbca3d6b5f615382bb67d759`.

### L7-A24-U018 — 16. Replay Protection

إعادة إرسال رسالة قديمة لا تعيد صلاحية تفويض انتهى.

يجب الحفاظ على:

Message Identity

Operation Identity

Attempt Identity

Epoch Binding

Idempotency Scope

وفق طبيعة العملية.

Source: [RDMS-10-M24-U018](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3229>); source-unit SHA-256 `8978972391fb3dc7fa9a7c30c3f9c344a5e3b4362d32a0e189fc8a4a11bd6d4e`.

### L7-A24-U019 — 17. Trusted Transport Is Not Trusted Content

قد تكون الرسالة قد وصلت عبر قناة موثوقة، لكن Payload تحتوي على Tool Output غير موثوقة.

يجب الحفاظ على ContentEnvelope الأصلية.

لا يجوز ترقية سلطة المحتوى بسبب نقله عبر خدمة داخلية موثوقة.

C01-A2 Result

FR10-G01 — ADDRESSED

Source: [RDMS-10-M24-U019](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3247>); source-unit SHA-256 `5e786dd8c725bc215ed24d48f98053ed5353e56e05b9b5a8dc202d9cb55984b7`.

### L7-A24-U022 — 19. HumanIngressAuthorityBinding

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U022](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3270>); source-unit SHA-256 `325b96475ddccd0a86cec005b22a10c6a961aed6d8b29e23d6b6c1bc35c32f2a`.

### L7-A24-U023 — 20. Domain-Specific Authority

لا توجد سلطة بشرية مطلقة لمجرد أن الرسالة صادرة عن شخص.

قد يكون شخص ما مخولًا بتغيير متطلبات واجهة المستخدم، لكنه غير مخول بتعديل سياسات الأمان أو تنفيذ Deployment.

يجب أن يتوافق التفويض مع نطاق القرار.

Source: [RDMS-10-M24-U023](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3294>); source-unit SHA-256 `f67c2750a3131e3108010cfdebb72a87375a0e937aad95a3fc915d720d14b296`.

### L7-A24-U024 — 21. User Content vs Authoritative Request

إذا احتوى طلب المستخدم على نص مقتبس من Issue أو ملف خارجي، فلا تكتسب تعليمات ذلك النص سلطة المستخدم تلقائيًا.

يجب الحفاظ على الفرق بين:

User's actual instruction

و:

External content supplied for analysis

Source: [RDMS-10-M24-U024](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3302>); source-unit SHA-256 `ebc3220e6097286abe4ed7fa9636d1320c304bca98dcabd7b7cf3451d8967050`.

### L7-A24-U025 — 22. Human Response Adoption

عندما تسأل Executive مستخدمًا عن قرار، يجب ربط الإجابة بالسؤال ونطاق السلطة والنسخة القانونية التي كانت نافذة.

لا يجوز استعمال إجابة قديمة لتفويض عملية مختلفة.

C01-A3 Result

FR10-G21 — ADDRESSED

Source: [RDMS-10-M24-U025](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3313>); source-unit SHA-256 `9848ea28e8a3ffc244684d444c7628334e4a4864b7673d247a71383462fa7091`.

### L7-A24-U028 — 24. Architectural Decision

نعتمد الفصل التالي:

COGNITIVE COMMIT
    Changes accepted cognitive state.

REPOSITORY ACTION
    Changes the actual repository.

OBSERVATION
    Records what happened.

INTEGRATION DECISION
    Determines whether the result
    satisfies the intended engineering goal.

Source: [RDMS-10-M24-U028](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3336>); source-unit SHA-256 `c53d8132447dd7c1a5e87f165a6e141099f8ccf33d986ac402a3facc3f43c653`.

### L7-A24-U029 — 25. RepositoryMutationIntegrationContract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U029](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3352>); source-unit SHA-256 `036081c2accd131b50640c61e0a2e428b5d4c354fb35ba6889df5c798aeda04d`.

### L7-A24-U030 — 26. Legal Mutation Path

Candidate Patch
      ↓
Executive Engineering Decision
      ↓
ActionProposal
      ↓
ActionGate
      ↓
Durable Action Intent
      ↓
Repository Mutation
      ↓
Observation
      ↓
Verification
      ↓
Canonical Reconciliation

Source: [RDMS-10-M24-U030](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3382>); source-unit SHA-256 `20d371751b30592e265bb28f31cf8bd0b7122caca9537462ea27c3defea3c3a7`.

### L7-A24-U031 — 27. Candidate Is Not Canonical

ملف ينتج داخل Specialist Workspace لا يصبح تعديلًا معتمدًا في Repository المشتركة لمجرد نجاح توليده.

يحتاج إلى مسار تكامل مناسب.

Source: [RDMS-10-M24-U031](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3400>); source-unit SHA-256 `1dff60a5b9b32ef315b755f87a2b0f0ad279b04d6646852be9996ad68a687406`.

### L7-A24-U032 — 28. Repository Base Validation

إذا كان التعديل مبنيًا على Revision قديمة، يجب تقييم توافقه مع Repository الحالية.

ولا يجوز استعمال Last Writer Wins تلقائيًا عندما يمكن أن يؤدي إلى فقدان تغييرات أو كسر متطلبات.

Source: [RDMS-10-M24-U032](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3406>); source-unit SHA-256 `37ae0181ce5f4de44edbd4ded49469f5f1f756f15cd1535ac7bb2b1c55d66332`.

### L7-A24-U033 — 29. Mutation and Acceptance Separation

يجب أن يستطيع النظام تمثيل:

Repository mutation:
    APPLIED

Engineering acceptance:
    NOT YET VERIFIED

دون تناقض.

نجاح الكتابة أثر واقعي.

أما نجاح الهدف الهندسي فهو حكم يحتاج أدلة أخرى.

C01-A4 Result

FR10-G03 — ADDRESSED

Source: [RDMS-10-M24-U033](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3412>); source-unit SHA-256 `9126e3d78fa97dfb0a82c4ab995309ce1b30ede64e469829cd846237672706c1`.

### L7-A24-U036 — 31. ExecutiveTransitionIntegrationBinding

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U036](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3441>); source-unit SHA-256 `b50ccc44a7710431b044d04c1d3fccb15f4df6857f8ee8c64bd8cfbb58e553c6`.

### L7-A24-U037 — 32. Decision Adoption Rule

لا يجوز لـCapability Runtime تنفيذ عملية جديدة اعتمادًا على Executive Decision فقدت شروط صلاحيتها.

Source: [RDMS-10-M24-U037](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3467>); source-unit SHA-256 `ffa2fb4b6fc8c0af4dd2b6d6156c34dc2e1c6234b14c8fcd6828d2c430340ebe`.

### L7-A24-U038 — 33. Transition Commit

يجب أن يستخدم Runtime مسار RDMS-08 وRDMS-01 لربط:

Current Goal

Current Focus

Current State

Executive Decision

Selected Operation

Required Preconditions

بالانتقال القانوني.

Source: [RDMS-10-M24-U038](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3471>); source-unit SHA-256 `9a3d9630e5392c8e3a9a7e6eea15a133c766875ebdd64cf275c78952bfe4a2de`.

### L7-A24-U039 — 34. Concurrent State Changes

إذا تغير أحد الشروط الإلزامية أثناء محاولة اعتماد الانتقال:

Expected State != Current State

يجب رفض الانتقال أو إعادة تقييمه حسب القوانين المجمدة.

لا يجوز تنفيذ العملية القديمة على حالة جديدة بصورة صامتة.

C01-A5 Result

FR10-G04 — ADDRESSED

Source: [RDMS-10-M24-U039](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3489>); source-unit SHA-256 `5a2e701b0660bb3c8142c751a83d1a515dbee9cc29cf3efd55e63c6a0d74f25b`.

### L7-A24-U042 — 36. Architectural Decision

There must be one authoritative legal lifecycle, even when its physical records are distributed.

أي:

يجب أن تكون دورة حياة Action قانونية واحدة.

ويمكن توزيع تخزينها فعليًا بشرط الحفاظ على ضمانات السلطة والمتانة والتعافي.

Source: [RDMS-10-M24-U042](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3514>); source-unit SHA-256 `1b07f71de3f1233e66b92db820f338fed906d242730cabfee1d5111c49f69312`.

### L7-A24-U043 — 37. ControlActionDurabilityContract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U043](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3524>); source-unit SHA-256 `616e63b0c68842350db9b3f8b6ff6b646eec1dff1024b573da613929e352278f`.

### L7-A24-U044 — 38. No Dual Lifecycle Authority

لا يجوز أن تقرر Control Ledger أن Action أصبحت EFFECT_VERIFIED بينما تعتبر Action Journal ذلك غير صحيح وفق تاريخين قانونيين مستقلين.

يجب أن توجد قاعدة واضحة للمصدر القانوني وإعادة بناء العرض المشتق.

Source: [RDMS-10-M24-U044](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3548>); source-unit SHA-256 `b9e6e6f8f61d50c287166f8d5efc108401143c305ba032eecd069accb2c9486d`.

### L7-A24-U045 — 39. Required Dispatch Ordering

نحافظ على تسلسل FCA المجمد:

ActionProposal
      ↓
Executive Authorization
      ↓
ActionGate
      ↓
Persist AUTHORIZED
      ↓
Persist DISPATCH_INTENT
      ↓
Durable Acknowledgement
      ↓
Dispatch SHARED_WORLD mutation

Source: [RDMS-10-M24-U045](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3554>); source-unit SHA-256 `3b2b60a45b37f733b0023dc82c59dfca9837b0c1b1f0b9eebdcbf9b58fbe5125`.

### L7-A24-U046 — 40. Physical Storage Alternatives

يمكن تحقيق العقد باستخدام:

A. Shared Transactional Boundary

تخزين بيانات التحكم ومراجع Action ضمن حد معاملات يضمن الذرية المطلوبة.

B. Explicit Durable Protocol

استخدام بروتوكول متعدد المراحل يحدد حالات الانقطاع والاستعادة بصورة قانونية.

لا نفرض أحدهما في RDMS-10.

لكن الخيار المستخدم يجب أن يحقق جميع الالتزامات المجمدة.

Source: [RDMS-10-M24-U046](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3571>); source-unit SHA-256 `2c307244df5bbe5bf5ad31978a6dfccf6c4e5b87eb786a731840a6b690fdae8c`.

### L7-A24-U047 — 41. Crash Between Stores

إذا انقطع النظام بين كتابة متينتين، يجب أن تحدد عملية الاستعادة:

What was legally committed?

What was only prepared?

What may have been dispatched?

Which records remain authoritative?

ولا يجوز التخمين.

Source: [RDMS-10-M24-U047](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3587>); source-unit SHA-256 `d2028cf648f9ddbceafc3ffd87bdf66cadf10d044bb07a015003b746c649c9fe`.

### L7-A24-U048 — 42. Recovery Consistency

إذا تعذر إثبات أن حالة Action متماسكة، يجب منع Dispatch جديدة قد تكرر أثرًا مجهولًا.

لا يجوز استعمال غياب Action من إحدى Projection باعتباره إثباتًا لعدم حدوثها.

C01-B1 Result

FR10-G05 — ADDRESSED

Source: [RDMS-10-M24-U048](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3601>); source-unit SHA-256 `6d8b3cff7257e8fbb985dd8d436a7bcec304da23c4307b8519ccfbaa34b5c12e`.

### L7-A24-U051 — 44. SealedExecutionIntent

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U051](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3620>); source-unit SHA-256 `82bccbec81a83e5cf065d1bbd2d6a618c8b178489b28bfde0da4a354a9e3137c`.

### L7-A24-U052 — 45. Sealing Rule

يجب أن يرتبط التفويض القانوني بما سيُنفذ فعليًا.

لا يكفي الاعتماد على النص الذي عرضه النموذج.

يجب أن يشمل الربط:

Tool identity

Operation kind

Effective arguments

Target identity

Resource scope

Effect semantics

Execution context

بحسب طبيعة العملية.

Source: [RDMS-10-M24-U052](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3648>); source-unit SHA-256 `792a2221aef2f38bc0bfa862e0940f7d25020e26250521538efb38981f2a8ca9`.

### L7-A24-U053 — 46. Effective Arguments

يجب أن تُحسب هوية Arguments بعد التحويلات المؤثرة التي تطبقها Runtime.

مثال:

Original path:
    ./tmp/output

Resolved target:
    /workspace/tmp/output

لا يجوز تغيير المسار النهائي إلى مورد آخر بعد التفويض دون تحقق مناسب.

Source: [RDMS-10-M24-U053](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3672>); source-unit SHA-256 `c76bf4f12d9143709e2dff38afbf9b93f0459c5c9f21ca022eb2d127207cbcc1`.

### L7-A24-U054 — 47. TOCTOU Protection

قد يتغير المورد نفسه بين التحقق والتنفيذ.

مثل:

Symlink target changes.

Repository revision changes.

Database schema changes.

لذلك يجب أن ترتبط شروط التنفيذ بهوية المورد ونسخته أو بآلية تحقق مناسبة عند الاستخدام.

إذا تعذر ضمان ثبات الهدف المطلوب، يجب رفض العملية أو إعادة تقييمها.

Source: [RDMS-10-M24-U054](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3686>); source-unit SHA-256 `dcc79f7432530cfc52d79c32ad717619cbbea2b856dd8122db9e4e16278fa6c3`.

### L7-A24-U055 — 48. Executor Rule

قبل التنفيذ:

Received Operation
      ↓
Verify Sealed Intent
      ↓
Verify Current Execution Eligibility
      ↓
Verify Applicable Dispatch Boundary
      ↓
Execute

لا يجوز للـExecutor تنفيذ Payload مختلفة ماديًا عن المصرح بها.

Source: [RDMS-10-M24-U055](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3702>); source-unit SHA-256 `b2168b88bf7b686aaf34a8515a0a41c16c24df3f1051c8c9bff4c239c981f373`.

### L7-A24-U056 — 49. Intent Integrity vs Outcome

سلامة SealedExecutionIntent لا تثبت نجاح التنفيذ.

هي تثبت فقط أن العملية المرسلة مطابقة للتفويض ضمن الضمانات المعتمدة.

أما النتيجة الخارجية فتحتاج إلى Observation وReconciliation.

C01-B2 Result

FR10-G06 — ADDRESSED

Source: [RDMS-10-M24-U056](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3718>); source-unit SHA-256 `e2144cade897a83a46ff0f456efb5977a36d99375bab2195417e10762a14a44d`.

### L7-A24-U059 — 51. ActionDeliveryContract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U059](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3739>); source-unit SHA-256 `a27a9936b1084c09dbd590cd882b7eb10a9d0b01312f24f37817334c93eab54f`.

### L7-A24-U060 — 52. Critical Distinction

نميز بين:

MESSAGE DELIVERY

EXECUTION ATTEMPT

EXTERNAL EFFECT

هذه أحداث مختلفة.

قد تصل الرسالة مرتين دون أن يعني ذلك السماح بتنفيذ العملية مرتين.

Source: [RDMS-10-M24-U060](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3765>); source-unit SHA-256 `487be0685d558ea350f8496ca73949501cd9c16c0179151d9819ad6e4cfa1837`.

### L7-A24-U061 — 53. Redelivery Rule

Message redelivery is not a new authorization.

إذا وصلت رسالة مرة ثانية، يجب فحص حالة Action القانونية قبل أي محاولة تنفيذ أخرى.

Source: [RDMS-10-M24-U061](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3779>); source-unit SHA-256 `f3df4f8c1fff66aaa03e4255e4e435784606ae211ac755f7037cd83524adc904`.

### L7-A24-U062 — 54. IN_DOUBT Behavior

إذا كانت هناك إمكانية لحدوث الأثر الخارجي، لكن النتيجة مجهولة:

Action outcome = IN_DOUBT

وفق RDMS-04.

ولا يجوز اعتبار عدم وصول Acknowledgement دليلًا على فشل العملية.

Source: [RDMS-10-M24-U062](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3785>); source-unit SHA-256 `1b875b965ca3bbdceee19503c5b0d53757edffb7f4fb895dcf35f415c8d03720`.

### L7-A24-U063 — 55. Retry Eligibility

تعتمد إعادة المحاولة على:

Action Effect Semantics

Retry Policy

External Idempotency Guarantee

Outcome Probe

Current Authority

Current Preconditions

ولا تعتمد على عدد مرات تسليم الرسالة وحده.

Source: [RDMS-10-M24-U063](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3795>); source-unit SHA-256 `cd33af79ab08ff69f07b647bb453f876afc9cc9f82fcf23e80b427e3d4ced9b8`.

### L7-A24-U064 — 56. Worker Generation

يجب أن تلتزم Workers بحدود التنفيذ والأجيال القانونية.

لكن انتهاء جيل Worker لا يثبت توقف آثار خارجية أرسلتها سابقًا.

هذه الآثار تحتاج تسوية مستقلة.

C01-B3 Result

FR10-G07 — ADDRESSED

Source: [RDMS-10-M24-U064](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3813>); source-unit SHA-256 `68179a671f9258f25e5cd2f25c34c9384fe1d3c40651cae079e826f9853e02c5`.

### L7-A24-U067 — 58. ArtifactPublicationContract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U067](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3834>); source-unit SHA-256 `87b4ed2bc40dbb1f9d8bb51fe29fc71117cddb69c265467da1cd375ba1c84ac3`.

### L7-A24-U068 — 59. Publication Ordering

عندما تكون Artifact ضرورية لتعافٍ قانوني صحيح:

Produce Artifact
      ↓
Validate Integrity
      ↓
Publish Durably
      ↓
Receive Required Durability Proof
      ↓
Commit Canonical Reference

لا يجوز عكس الترتيب بصورة تسمح بوجود مرجع قانوني لا يمكن استعادة محتواه الضروري.

Source: [RDMS-10-M24-U068](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3858>); source-unit SHA-256 `cafbdcd600bf1cfb8f66a0cc801dd7eebfadb7586832fdb8c84ea2439d808108`.

### L7-A24-U069 — 60. Artifact Classes

نميز بين:

Recovery-critical artifact

Canonical supporting artifact

Rebuildable derived artifact

Disposable diagnostic artifact

يجب أن تحدد المواصفة المالكة الحاجة الفعلية لكل Artifact.

Source: [RDMS-10-M24-U069](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3874>); source-unit SHA-256 `7c60c0e1d772e46a7d1a3f06acda3c6b1c9dacbd5e8ad495af6fbb5b06b617e1`.

### L7-A24-U070 — 61. Garbage Collection Safety

لا يجوز حذف Artifact ما زالت مطلوبة عبر مراجع قانونية أو التزامات تعافٍ أو سياسات احتفاظ نافذة.

كما لا يجوز أن تعتمد عملية Cleanup على افتراض أن المهمة انتهت لمجرد توقف Worker.

Source: [RDMS-10-M24-U070](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3888>); source-unit SHA-256 `740cf3c52b2e021504743c9d604812f5f2e11fe46c5d3774eb2459d843a6f322`.

### L7-A24-U071 — 62. Integrity After Recovery

عند استعادة Artifact يجب التحقق من سلامتها ومراجعها وفق RDMS-09.

وجود الملف وحده لا يثبت أنه المحتوى الصحيح.

C01-B4 Result

FR10-G08 — ADDRESSED

Source: [RDMS-10-M24-U071](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3894>); source-unit SHA-256 `1026ba83a12dafba8a95e24819bc53a0eda679a4b23f085508e22c044ddc7479`.

### L7-A24-U074 — 64. CrossComponentEventContract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U074](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3913>); source-unit SHA-256 `86f69937951edff4449b1ff83ac3780a779fb304ac6bee24d344d72aa71dc442`.

### L7-A24-U075 — 65. Causal Ordering vs Arrival Ordering

لا يجوز استخدام وقت وصول الرسالة باعتباره مصدر الحقيقة القانوني.

مثال:

Action Authorized
      ↓
Action Dispatched
      ↓
Effect Reported

قد تصل Effect Report إلى مكون قبل وصول إشعار Authorization.

لكن لا يجوز تفسير ذلك على أنه تغيير قانوني لترتيب الأحداث.

Source: [RDMS-10-M24-U075](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3941>); source-unit SHA-256 `68ff37a4e42cb201b48d6638cd5d9f0a54d940f925eb41441636c046909c6c1b`.

### L7-A24-U076 — 66. No Universal Total Order Requirement

لا نفرض ترتيبًا عالميًا لجميع أحداث النظام.

قد تكون أحداث مشاريع مستقلة قابلة للمعالجة بالتوازي.

لكن يجب الحفاظ على الترتيب السببي الذي تعتمد عليه صحة الانتقالات القانونية.

Source: [RDMS-10-M24-U076](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3957>); source-unit SHA-256 `69049e223315fa9e7d2143ffe165a5434e21f8c0660933969ec242ff13ab1845`.

### L7-A24-U077 — 67. Duplicate Events

يجب استخدام هوية الحدث ومجال Idempotency لمنع تكرار الأثر القانوني عند إعادة التسليم.

ولا تعني إزالة تكرار Event إزالة تكرار External Effect تلقائيًا.

Source: [RDMS-10-M24-U077](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3965>); source-unit SHA-256 `9d9fbee4586590a02c4ff0d1b4059536b3937b96152f4dfa592165718c7de435`.

### L7-A24-U078 — 68. Unknown Parent Event

إذا وصلت رسالة تتطلب Parent Event قانونية لا يمكن التحقق منها، فلا يجوز اعتماد انتقالها القانوني اعتمادًا على افتراض وجود ذلك الحدث.

يمكن الاحتفاظ بالرسالة للتحقيق، لكن قبولها يخضع إلى شروط السببية اللازمة.

C01-B5 Result

FR10-G09 — ADDRESSED

Source: [RDMS-10-M24-U078](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3971>); source-unit SHA-256 `f482b59b20a469f9c96f42c0eb1e8cadcb0368fc09dca406b506676622f745c7`.

### L7-A24-U081 — 70. ObservationSourceBinding

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U081](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3994>); source-unit SHA-256 `0628273bbb4f4c16df7eb1e8d5e409f955a690cbc97d0cc13114ce20c55545a5`.

### L7-A24-U082 — 71. Report vs Observation

يمكن تسجيل:

Observation:
    Tool returned exit code 0.

لكن لا يجوز القفز إلى:

Fact:
    Deployment is fully healthy.

دون أدلة مناسبة.

Source: [RDMS-10-M24-U082](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4022>); source-unit SHA-256 `721626bb9ccf9dfb4632cc4fc31cf771a328cda4520e1ab9bcc232b436fe1f0e`.

### L7-A24-U083 — 72. Source Authority

يجب أن تكون سلطة المصدر متناسبة مع نوع الادعاء.

مثلًا:

Compiler:
    May establish compilation outcome
    within the observed build scope.

Test runner:
    May establish reported test results.

Deployment API:
    May report deployment status.

Runtime probe:
    May provide evidence about actual service behavior.

لكن لا يصبح أي مصدر مخولًا لإثبات جميع خصائص النظام.

Source: [RDMS-10-M24-U083](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4036>); source-unit SHA-256 `f96b4dac78a71f8a212e5ca37d50cd45ba6e1b3d35c2df4bf1cfda8387fe2728`.

### L7-A24-U084 — 73. Observation Ingress Rule

يجب أن يحتفظ Observation Ingress بالمحتوى الخام ومصدره وسلامته.

ولا يجوز أن ينتج Fact أوسع من حدود التسجيل المسموح بها.

Source: [RDMS-10-M24-U084](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4057>); source-unit SHA-256 `c635049c1e1eb6052e933eb6e4556fd9ce6bb14cc6df568ceb5ed6ea14d719ea`.

### L7-A24-U085 — 74. Evidence Promotion

أي استنتاج معرفي من Observation يخضع إلى قواعد RDMS-03.

كما أن الادعاءات السببية تحتاج المسار القانوني المناسب، ولا تصبح حقائق عامة لمجرد قبول تفسير سببي محدود.

C01-C1 Result

FR10-G10 — ADDRESSED

Source: [RDMS-10-M24-U085](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4063>); source-unit SHA-256 `530a0900fcc1b35ba29110f136a119175379852015b2da9e73aae5695b763b52`.

### L7-A24-U088 — 76. IntegratedCompletionEvidence

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U088](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4084>); source-unit SHA-256 `e3f73ce4253300549f2fef531751de5a4259964050cfdb0077831e492fe031ec`.

### L7-A24-U089 — 77. Completion Semantics

يجب التمييز بين:

Implementation attempted.

Implementation applied.

Verification executed.

Acceptance satisfied.

Goal finalized.

هذه مراحل ذات معانٍ مختلفة.

Source: [RDMS-10-M24-U089](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4114>); source-unit SHA-256 `c9187d3a60d7fc3d8498d97e68291f5a5ebf0da8c1cf6db735b6815f4285c7e7`.

### L7-A24-U090 — 78. Finalization Gate

قبل اعتماد Finalization يجب تحديد:

أي شروط قبول ثبت تحققها.

أي شروط ما زالت مجهولة.

هل الأدلة صالحة للحالة الحالية؟

هل توجد آثار خارجية غير محسومة تؤثر في النتيجة؟

هل توجد تغييرات غير مدمجة تؤثر في الادعاء؟

Source: [RDMS-10-M24-U090](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4130>); source-unit SHA-256 `1b143a7abab6990d7b9ccd9f91c9f6f9520ace01276eb825307670cbd5ae351f`.

### L7-A24-U091 — 79. Partial Completion

إذا أنجز النظام جزءًا من المهمة، فلا يجوز تقديمه باعتباره إنجازًا كاملًا.

يمكن إصدار تقرير دقيق يبين ما تحقق وما لم يتحقق.

Source: [RDMS-10-M24-U091](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4144>); source-unit SHA-256 `b6361a3d8e9078f67395bad19c126043929838e7e46451ceade2e0fa22a1ee75`.

### L7-A24-U092 — 80. No Completion From Fluency

قد ينتج LLM شرحًا ممتازًا للتعديل.

لكن جودة الشرح لا تثبت صحة التنفيذ.

يجب أن تتبع الثقة الأدلة الفعلية.

C01-C2 Result

FR10-G11 — ADDRESSED

Source: [RDMS-10-M24-U092](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4150>); source-unit SHA-256 `19a8c180409daac5fc1fd2253dd25e700b2f4ff15c943499850fbf94e795a1eb`.

### L7-A24-U095 — 82. ActiveWorkInvalidationContract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U095](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4171>); source-unit SHA-256 `793bfce195ec548cf563dc55ecb4d6612feea4a6545a449912537cc53165430d`.

### L7-A24-U096 — 83. Invalidation Propagation

Relevant Dependency Changes
            ↓
Canonical Dependency Evaluation
            ↓
Affected Results Identified
            ↓
Affected Active Work Identified
            ↓
Queued Operations Revalidated
            ↓
In-flight Effects Reconciled
            ↓
Executive Reassessment

Source: [RDMS-10-M24-U096](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4199>); source-unit SHA-256 `205e45a49a7eaa0c2f45b0ec0313034c13eb8d0c27d23d610bbb2b481480c0e6`.

### L7-A24-U097 — 84. Pending vs Dispatched

نميز بين:

Pending operation

لم تتجاوز بعد نقطة التنفيذ القانوني.

يمكن منعها أو إعادة تقييمها.

Already dispatched operation

قد تكون أحدثت أثرًا خارجيًا.

لا يجوز اعتبار إبطال Decision أو Plan إلغاءً تلقائيًا لذلك الأثر.

Source: [RDMS-10-M24-U097](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4213>); source-unit SHA-256 `98ab9ecaecec681f218ec57457436b5c3be114fae44910a685beb4c5bf0debd9`.

### L7-A24-U098 — 85. Scoped Invalidation

لا تعني تغييرات Repository أن جميع النتائج أصبحت stale.

يجب استخدام DependencySet الفعلية.

عندما لا يمكن إثبات نطاق ضيق، يستخدم المحرك تقييمًا محافظًا.

Source: [RDMS-10-M24-U098](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4229>); source-unit SHA-256 `612b9e416484b38587fee31a028b74f894d872b9338a51c6b3a04835421da7b7`.

### L7-A24-U099 — 86. Race With Dispatch

إذا تغيرت اعتمادية مؤثرة بالتزامن مع Dispatch، يجب أن تحدد حدود التنفيذ القانونية ما إذا كانت العملية ما زالت مؤهلة.

لا يكفي الاعتماد على نتيجة تقييم قديمة لا تغطي النسخة الحالية.

C01-C3 Result

FR10-G14 — ADDRESSED

Source: [RDMS-10-M24-U099](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4237>); source-unit SHA-256 `c80e4ce2363013897e5daed769ea535249d809b0cc2b44a8e6426d8d6ea83003`.

### L7-A24-U102 — 88. ReasoningProviderCapabilityContract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U102](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4256>); source-unit SHA-256 `7fb1a639e9219590c5ebbb065bc5044f28f8e26e05c6440822d8d830c718ea46`.

### L7-A24-U103 — 89. Capability Negotiation

قبل استدعاء Provider يجب التحقق من أن المهمة تتوافق مع الإمكانات المطلوبة.

لا نفترض أن كل النماذج تستطيع إنتاج Structured Output موثوقة بالطريقة نفسها.

Source: [RDMS-10-M24-U103](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4282>); source-unit SHA-256 `6a13ba2fbaedf556c03fb7625c127513f4721f3825db72145643e10ceb7bdd26`.

### L7-A24-U104 — 90. Output Validation

إذا كانت Capability تحتاج إلى:

Structured ActionProposal

وأعادت Provider نصًا حرًا غير متوافق، فلا يجوز تحويله مباشرة إلى Action قانونية.

يمكن إعادة طلب النتيجة أو استخدام طريقة تحويل لا تمنح سلطة، لكن المقترح النهائي يجب أن يجتاز جميع شروطه.

Source: [RDMS-10-M24-U104](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4288>); source-unit SHA-256 `c20d3c36bd43eba2124f6ee8657f18f697a48b832bd6f978c67a3c4f813aa2b2`.

### L7-A24-U105 — 91. Provider Fallback

يمكن تغيير Provider وفق سياسة RDMS-08.

لكن يجب الحفاظ على:

Original Invocation Identity

Attempt Generation

Context Provenance

Dependency Set

Current Executive Authority

Source: [RDMS-10-M24-U105](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4298>); source-unit SHA-256 `9086523c26fab8fb2efbb3002426f705911033ae50189acd2e6e3aec775cd32f`.

### L7-A24-U106 — 92. Provider Failure

عدم توفر Provider لا يغير صلاحيات النظام.

كما لا يجوز أن يؤدي Fallback إلى تجاوز سياسات البيانات أو تخفيض متطلبات التفويض.

C01-D1 Result

FR10-G12 — ADDRESSED

Source: [RDMS-10-M24-U106](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4313>); source-unit SHA-256 `4eb6c5198cfb6eec5d50a63e0fa95f9b6ee22a461e9b2bb73a1b955d22c64b4a`.

### L7-A24-U109 — 94. ContextDisclosureAdmission

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U109](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4332>); source-unit SHA-256 `a77555c4316ef4025ef7adf0f016e288db52e383b350c30e6d630b01084622b6`.

### L7-A24-U110 — 95. Disclosure Boundary

يجب التحقق من شروط الإفصاح قبل إرسال البيانات.

ليس بعد وصول الاستجابة.

Source: [RDMS-10-M24-U110](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4356>); source-unit SHA-256 `fd732d5f94f4c16819ea470d5eba21fd0d0b4ba15bb705f01e992ab9a0a2d157`.

### L7-A24-U111 — 96. Multi-Project Memory

قد تحتوي Memory Service على معرفة من مشاريع متعددة.

لكن صلاحية استرجاع المعرفة لا تعني تلقائيًا صلاحية مشاركة محتواها مع كل Provider أو Project.

Source: [RDMS-10-M24-U111](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4362>); source-unit SHA-256 `214e036d4dfc0fd6f24a9e00fc9fb3610960d50b6101ce9c55e73c42142bf5c1`.

### L7-A24-U112 — 97. Context Minimization

يجب أن تتضمن Context ما يلزم للمهمة ضمن الحدود المناسبة.

لكن تقليل حجم السياق لا يجوز أن يؤدي إلى حذف Hard Invariants أو شروط إلزامية لازمة لاتخاذ قرار آمن.

Source: [RDMS-10-M24-U112](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4368>); source-unit SHA-256 `411a2bbd6866d9b3f982b15c56e22be82f71a1ef9bec8ac5e06aef9ebdf7ab0f`.

### L7-A24-U113 — 98. Provider Switching

عند تغيير Provider يجب إعادة تقييم شروط الإفصاح المرتبطة بالوجهة الجديدة.

لا يجوز وراثة إذن الإفصاح الخاص بـProvider A تلقائيًا إلى Provider B.

C01-D2 Result

FR10-G13 — ADDRESSED

Source: [RDMS-10-M24-U113](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4374>); source-unit SHA-256 `9c008fde0016d15a7315d8149e05bc3d1ff850744f035061138f7a228af29d55`.

### L7-A24-U116 — 100. SpecialistExecutionAuthorityBinding

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U116](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4393>); source-unit SHA-256 `ee9fd29375e86a4104d72201669e43a40152d7d29eba224e9fd134b26e350b7f`.

### L7-A24-U117 — 101. End-to-End Specialist Authority

يجب أن تُفرض قيود Specialist عند:

Specialist Contract
        ↓
Tool Request
        ↓
Tool Gateway
        ↓
Execution Boundary
        ↓
Actual Resource Access

لا يكفي أن تذكر القيود داخل Prompt.

Source: [RDMS-10-M24-U117](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4417>); source-unit SHA-256 `100a49fa0d7f04dd78ca597f2a2cfa4158cc53f5207e47fb7555fb80da6c7418`.

### L7-A24-U118 — 102. Tool Authority Intersection

صلاحية التنفيذ الفعلية لا يجوز أن تتجاوز تقاطع:

Specialist Contract

Project Policy

Tool Policy

Execution Boundary

Current Authorization

إذا كان أحد القيود يمنع العملية، فلا يجوز منحها بواسطة قيد آخر أوسع.

Source: [RDMS-10-M24-U118](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4433>); source-unit SHA-256 `8a7b0d7707847aa42076177ab2da6d940377bac98ebaf39a266ac576cd273828`.

### L7-A24-U119 — 103. Specialist Scope Changes

إذا تغير عقد Specialist، يجب أن يخضع التغيير إلى المسار القانوني المناسب.

ولا يمكن لـSpecialist تعديل صلاحياتها بنفسها.

Source: [RDMS-10-M24-U119](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4449>); source-unit SHA-256 `0fef1f5036f8adb9a65a9ab2a525d9b69cdb06ee18f30a7ead7b12f33183d65c`.

### L7-A24-U120 — 104. Nested Specialists

تحافظ المواصفة على FCA v1.0.1:

Specialist لا تستطيع إنشاء Specialist فرعية بسلطتها الخاصة.

يمكنها اقتراح الحاجة إلى متخصص إضافي، لكن قرار Recruitment يعود إلى Executive الحالية.

C01-D3 Result

FR10-G15 — ADDRESSED

Source: [RDMS-10-M24-U120](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4455>); source-unit SHA-256 `0f503b09e116d895aafdb0c53620748a9bc5d6370632a5ef9cf27e8492c51af2`.

### L7-A24-U123 — 106. SpecialistIntegrationTransaction

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U123](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4476>); source-unit SHA-256 `80041339b3c2e665ee5e6472152bf7a5f9623f19164ac7e5790fc852e3b17dd0`.

### L7-A24-U124 — 107. Integration Preconditions

قبل الدمج يجب التحقق من:

Specialist result provenance

Current contract validity

Dependency freshness

Repository compatibility

Structural conflicts

Semantic conflicts

Required verification

Source: [RDMS-10-M24-U124](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4504>); source-unit SHA-256 `cdc1c435058fc89850f300de26610139245a96a45e6ef92a5894162ed3ad7ed2`.

### L7-A24-U125 — 108. Parallel Result Handling

قد تكون نتيجة Specialist صالحة عند تسليمها، لكنها تفقد صلاحية جزء منها بعد دمج نتيجة أخرى.

يجب إعادة تقييم الأجزاء المتأثرة.

Source: [RDMS-10-M24-U125](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4521>); source-unit SHA-256 `d6bbe127311a7b72a0f77b14f5ec767deb4739d881f5ff941dd49df4ca761a65`.

### L7-A24-U126 — 109. Physical Merge vs Cognitive Acceptance

نميز بين:

Git merge operation

و:

Executive integration decision

الأولى عملية في Repository.

الثانية قرار معرفي.

يجب أن تحافظ كل منهما على مسارها القانوني.

Source: [RDMS-10-M24-U126](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4527>); source-unit SHA-256 `6b18e012104bf9e6ea429c5dc7bbc3ea151b5a98c9a48a32aa539247a77e6e14`.

### L7-A24-U127 — 110. Verification After Combination

إذا أدى دمج نتيجتين إلى حالة جديدة لم يختبرها أي متخصص منفردًا، فقد يحتاج النظام إلى Verification إضافية على الحالة المجمعة.

لا يجوز اعتبار نجاح اختبارات كل فرع منفصل دليلًا تلقائيًا على سلامة الدمج.

C01-D4 Result

FR10-G16 — ADDRESSED

Source: [RDMS-10-M24-U127](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4543>); source-unit SHA-256 `8e2f3f8e237ec40d5c37b8f57f030e651930d98e229d7a3a6d33a2b52df2182f`.

### L7-A24-U130 — 112. TriggerActionCausalityBinding

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U130](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4562>); source-unit SHA-256 `dfd879b43d2d41c56d9b1ade78ec2857bacc533b0fef6b8db33d7a6d1242e355`.

### L7-A24-U131 — 113. Trigger Reaction vs Action

يجب الفصل بين:

Trigger detected

و:

Canonical reaction committed

و:

External Action dispatched

هذه مراحل مختلفة.

Source: [RDMS-10-M24-U131](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4586>); source-unit SHA-256 `99d0bd1a92bd09961cff3d481e2476c989b3a5677982874e39ee65ac3733d405`.

### L7-A24-U132 — 114. Stable Causality

إذا أعاد النظام معالجة Reaction نفسها، يجب أن يستطيع تحديد ما إذا كانت قد أنتجت ActionProposal قانونية من قبل.

ولا يجوز أن يؤدي Replay إلى إنشاء أثر خارجي جديد مستقل بصورة صامتة.

Source: [RDMS-10-M24-U132](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4602>); source-unit SHA-256 `afdbfd88cc4710d0fa467ab7d7e2d5a9a6b7f79cc87ff854dd6d7966b1760f2b`.

### L7-A24-U133 — 115. External Effect Limitation

حتى إذا كانت Canonical Reaction idempotent، فإن العالم الخارجي قد لا يضمن Exactly-Once.

تظل RDMS-04 مسؤولة عن هوية Action وأهلية Retry والتسوية.

Source: [RDMS-10-M24-U133](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4608>); source-unit SHA-256 `036ce2c04c976573295d4d9b2bf1dbcc822a463ba1739f1b1416f671ba38730f`.

### L7-A24-U134 — 116. Crash Recovery

إذا وقع Crash بين اعتماد Reaction وتسجيل Action، يجب استخدام التاريخ القانوني لتحديد ما الذي تم اعتماده فعلًا.

لا يجوز استنتاج وجود أو عدم وجود أثر خارجي من نتيجة Trigger وحدها.

C01-E1 Result

FR10-G17 — ADDRESSED

Source: [RDMS-10-M24-U134](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4614>); source-unit SHA-256 `d612d6da21a1a1a9946380fa564c3dc7ad4a11d39bb49143ce1cffa7c9c5eea3`.

### L7-A24-U137 — 118. RuntimeActivationContract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U137](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4633>); source-unit SHA-256 `bde828d77fee4959c5963353192b243ebb0f37d2ab012d420d939aa6eab519dd`.

### L7-A24-U138 — 119. Component Running vs Operationally Admitted

نميز بين:

Process running.

و:

Component admitted for legal operation.

وجود Process لا يثبت أن مكونها يستطيع تنفيذ عمليات حقيقية بصورة آمنة.

Source: [RDMS-10-M24-U138](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4657>); source-unit SHA-256 `a6f258e1cd0fc8712c7e1d4835669625b917d3510446b2ae6d7ff943f061ddf3`.

### L7-A24-U139 — 120. Activation Scope

يمكن تشغيل:

Read-only inspection

بينما تبقى:

Shared-world mutation

محجوبة.

إذا كانت شروط الاستعادة تسمح بذلك.

Source: [RDMS-10-M24-U139](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4669>); source-unit SHA-256 `431aa97d71ed1ee54ffe81280b81604aec7e7daf5d422bfb023a7147b6551399`.

### L7-A24-U140 — 121. Recovery Ordering

يجب الحفاظ على تسلسل التعافي القانوني في FCA وRDMS-09.

ولا يجوز أن تبدأ Capability Runtime تنفيذ آثار مشتركة قبل استيفاء Recovery Admission المناسبة.

Source: [RDMS-10-M24-U140](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4683>); source-unit SHA-256 `6790f96bfcf85f0897c1cd1b9666fc22dc49046869f46759221d414311b6b10f`.

### L7-A24-U141 — 122. Admission Invalidation

قد تصبح Activation قديمة إذا:

Executive epoch changes

Policy changes

Security incident occurs

New unresolved action is discovered

Required dependency becomes stale

يجب أن تظل البوابات القانونية مسؤولة عن التحقق من الشروط الحالية.

C01-E2 Result

FR10-G18 — ADDRESSED

Source: [RDMS-10-M24-U141](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4689>); source-unit SHA-256 `9c47226055c368e20836551b76066116970cc54374be3d4e2d2c5e3657379562`.

### L7-A24-U144 — 124. ProjectExecutionBoundary

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U144](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4720>); source-unit SHA-256 `210a2bcae0e691e751be9b719ed759e39ff9064ba7fddf3209d13598f3513d9a`.

### L7-A24-U145 — 125. Project Identity Binding

كل عملية حاملة للسلطة يجب أن ترتبط بمشروعها القانوني.

لا يكفي أن تحتوي الرسالة على project_id كنص.

يجب التحقق من علاقة الهوية بالمورد والسلطة الفعلية.

Source: [RDMS-10-M24-U145](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4744>); source-unit SHA-256 `9cd8d95fb3d5013680c02bcd1b39b5c5027c125a950f8b276a7b262faaa54353`.

### L7-A24-U146 — 126. Cross-Project Access

إذا كانت العملية تحتاج موارد مشروع آخر، فيجب أن يوجد تفويض صريح يغطي هذا الانتقال وفق سياسات المشاريع المعنية.

لا يجوز استخدام قدرة خدمة مشتركة للوصول إلى موارد غير مصرح بها.

Source: [RDMS-10-M24-U146](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4752>); source-unit SHA-256 `7b7f96ab5e06c4a218e6332f3f73ca333a1016be4a54904e0a9266a0c61c984b`.

### L7-A24-U147 — 127. Shared Provider

يمكن استخدام Provider واحدة لعدة مشاريع.

لكن هذا لا يبرر خلط:

Canonical contexts

Private memory

Credentials

Authorization metadata

Specialist outputs

بين المشاريع.

Source: [RDMS-10-M24-U147](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4758>); source-unit SHA-256 `e159a5aa8bf6ab1701ecdb77b6a202ab5267c0877e8b554df84fded24e73e6bf`.

### L7-A24-U148 — 128. Shared Storage

يمكن تخزين مشاريع عديدة داخل Database واحدة.

لكن يجب أن تحافظ آليات الوصول والنسخ والتدقيق على حدود كل مشروع.

C01-F1 Result

FR10-G19 — ADDRESSED

Source: [RDMS-10-M24-U148](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4776>); source-unit SHA-256 `b07b1aad3f4575e4025bdf09252f0b3df901d3f10581afc54638dc02e1390179`.

### L7-A24-U151 — 130. ExecutionContainmentContract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U151](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4795>); source-unit SHA-256 `9d4f5ecb975307362b0919e5e4571c9be3116ba0acd9fe2d15c609adc97918c4`.

### L7-A24-U152 — 131. Classification by Reachable Effects

لا يجوز تصنيف عملية باعتبارها EPHEMERAL_SANDBOX بناءً على:

Command name

Tool name

LLM description

Intended purpose

فقط.

يجب النظر إلى الآثار الممكنة.

Source: [RDMS-10-M24-U152](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4819>); source-unit SHA-256 `d476dd64001bcb6a0d950c576df117cc8c7c9091b0ef59d0f28605c0d0dcf2e8`.

### L7-A24-U153 — 132. Sandbox Requirements

عندما تستخدم العملية المسار السريع، يجب إثبات العزل المطلوب عن:

Canonical repository mutations

Shared databases

Production credentials

Remote repositories

Deployment services

Non-disposable external effects

Source: [RDMS-10-M24-U153](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4835>); source-unit SHA-256 `589b401ac8c4421d891c4e246ef6b658f7763cbdd293eb53ba954905c80e31e3`.

### L7-A24-U154 — 133. Unknown Containment

إذا لم يمكن إثبات أن جميع الآثار القابلة للوصول قابلة للتخلص منها ومعزولة:

EPHEMERAL_SANDBOX eligibility:
    NOT ESTABLISHED

يجب رفض العملية أو معاملتها ضمن SHARED_WORLD وفق FCA.

Source: [RDMS-10-M24-U154](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4850>); source-unit SHA-256 `0adf7972a2eabaed19c2a002d2ebaea9f5fa01165ceef1cb59bac2b391402d51`.

### L7-A24-U155 — 134. Containment Across Workers

إذا انتقلت العملية من Worker إلى أخرى، يجب ألا تضيع قيود الاحتواء.

ولا يجوز أن تحصل Worker البديلة على صلاحيات أوسع دون تفويض مناسب.

C01-F2 Result

FR10-G20 — ADDRESSED

Source: [RDMS-10-M24-U155](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4859>); source-unit SHA-256 `28d4befe8ee9d54173c77a38b532e5ae41c92a4c90ae3df0e69c76fd56f45edd`.

### L7-A24-U158 — 136. ImplementationDependencyGraph

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U158](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4882>); source-unit SHA-256 `e7fdd28a310e66b08018709a3188f986c6c24fa7d060c1a9aced397908c94a01`.

### L7-A24-U159 — 137. Implementation vs Activation

نميز بين:

Component Implemented

الكود موجود.

Component Tested

اجتاز اختبارات محددة.

Component Integrated

مرتبط بالمكونات الأخرى وفق العقود.

Capability Activated

مسموح باستخدامه ضمن نطاق تشغيلي محدد.

هذه ليست حالات قانونية جديدة لكيانات FCA، بل أوصاف لتقدم تنفيذ المنتج.

Source: [RDMS-10-M24-U159](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4902>); source-unit SHA-256 `c165947c185fa2ae638989c60de8fb4d4be7597f6a71c24b69a72fa004eb3af4`.

### L7-A24-U160 — 138. Capability Activation Contract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M24-U160](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4924>); source-unit SHA-256 `c415b20878b0dfa43d46c7c36ca7806d4c20ba5213445ef596180f5c4506536b`.

### L7-A24-U161 — 139. No Safety Stub Bypass

يمكن استخدام Stubs أثناء تطوير المكونات.

لكن:

Stub CommitGate:
    Always approve.

لا يمكن استعمالها كبديل قانوني عن CommitGate الحقيقية في مسار Canonical Mutations إنتاجي.

وينطبق الشيء نفسه على:

Stub ActionGate

Stub Dependency Engine

Stub Recovery Journal

Stub Security Policy

Source: [RDMS-10-M24-U161](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4942>); source-unit SHA-256 `a4a73384155bf446c385da20ffa4a8daa5bdd4a3f7e8adb5eb30412aaf5a085d`.

### L7-A24-U162 — 140. Initial Walking Skeleton

يمكن بناء نموذج تكاملي أولي يحتوي على:

One project

One simple Goal

One Executive epoch

Canonical state store

CommitGate

ActionGate

Durable action protocol

Observation Ingress

Minimal reasoning adapter

لكن لا يسمح بتنفيذ عمليات خارجية حقيقية إلا إذا توفرت ضماناتها الإلزامية.

يمكن استخدام بيئات محاكاة أو Sandboxes مثبتة العزل أثناء تطوير بقية المكونات.

Source: [RDMS-10-M24-U162](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4962>); source-unit SHA-256 `2550b9e7a5e4eeceb37680de97431388633fa97dda7ec85b9de3ab42624c9c17`.

### L7-A24-U163 — 141. Safe Growth

تُفعّل القدرات تدريجيًا.

مثال:

Read-only cognitive analysis
        ↓
Isolated experiments
        ↓
Controlled repository changes
        ↓
Specialist execution
        ↓
Long-running tasks
        ↓
Recovery-tested broader operation

كل انتقال يحتاج إلى شروط تفعيل مناسبة.

C01-F3 Result

FR10-G22 — ADDRESSED

Source: [RDMS-10-M24-U163](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4988>); source-unit SHA-256 `5d0edbddc71557f0b8e66265527713d27d6bc3756a43b974f24f2fb20509ef55`.

### L7-A24-U165 — 142. H01 — Interface Duplication Control

يجب تقليل تكرار تعريفات الكيانات.

نقترح أن يحتوي Contract Registry على مراجع واضحة إلى التعريفات القانونية، وأن تستخدم المكونات Transport Projections بدل نسخ Schemas كاملة عندما يكون ذلك ممكنًا.

لا نريد خمس نسخ مختلفة من تعريف ActionRecord.

Source: [RDMS-10-M24-U165](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5013>); source-unit SHA-256 `85b9a9fb1b2f2ac24c44cab492922d9f06ec44fbf83d684dd5f35eb0d1a1a081`.

### L7-A24-U166 — 143. H02 — Runtime Performance

يجب أن تميز Runtime بين:

Mandatory legal checks

Conditional verification

Advisory analysis

Optional deep reasoning

يمكن تحسين الأداء عبر Caching أو Incremental Evaluation عندما تحافظ على شروط الصلاحية.

لكن لا يجوز إزالة فحص قانوني إلزامي بهدف تقليل Latency.

Source: [RDMS-10-M24-U166](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5021>); source-unit SHA-256 `d41ba717e2995dd66be9aab14baa92075a560603d9416b56e3ea6a91606f0f71`.

### L7-A24-U167 — 144. H03 — Diagnostic Data Governance

يجب فصل البيانات القانونية الضرورية للتعافي عن Logs التشخيصية.

كما يجب أن تخضع Logs إلى سياسات الاحتفاظ والإفصاح المناسبة.

ولا يجوز أن تتحول إلى نسخة غير محكومة من Memory أو Tool Outputs.

Source: [RDMS-10-M24-U167](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5037>); source-unit SHA-256 `be4c4902f407fbedfe5a8d9b95e55ea615d8b1db2917b2f2e52e36076e9e861c`.

### L7-A24-U168 — 145. H04 — Provider Quality Evaluation

يجب تقييم جودة Providers المختلفة في:

Structured proposal validity

Code correctness

Causal reasoning

Planning quality

Tool-use reliability

Context adherence

صلاحية Provider قانونيًا لا تعني أنها تقدم نفس الجودة المعرفية.

Source: [RDMS-10-M24-U168](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5045>); source-unit SHA-256 `a3695df9c95df6e01c63af55e88fa1a2134ac331be565abeb5c5c0d87f8bd865`.

### L7-A24-U169 — 146. H05 — Resource Backpressure

يمكن تقييد عدد:

Concurrent reasoning calls

Running specialists

Pending tool executions

Queued observations

Recovery probes

لكن لا يجوز إسقاط أحداث قانونية أو التزامات سلامة لمجرد ضغط الموارد.

يجب استخدام RDMS-05 وRDMS-08 وفق ملكية الجدولة والتحكم المعتمدة.

Source: [RDMS-10-M24-U169](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5063>); source-unit SHA-256 `aeb69b20dca0931396dcb826b6ed43429e4016c179900b5760bd101f80213d19`.

### L7-A24-U170 — 147. H06 — Package Dependency Direction

ينبغي أن تعتمد الحزم على واجهات قانونية واضحة بدل الوصول المباشر إلى تفاصيل تخزين بعضها.

يمكن استخدام:

Ports

Adapters

Dependency Injection

Typed domain interfaces

حسب الحاجة.

لكن لا نفرض Framework معينًا في هذه المرحلة.

Source: [RDMS-10-M24-U170](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5081>); source-unit SHA-256 `b11aed9189ef4285a9a7395af5e426f91ef6343e8c1d1b3f2e744051088a2c5e`.

### L7-A24-U171 — 148. H07 — Engineering Quality Benchmarking

اختبارات Conformance تثبت امتثال النظام للقوانين، لكنها لا تثبت أنه مبرمج محترف.

نحتاج لاحقًا إلى تقييم مستقل لـ:

Requirement understanding

Mental model accuracy

Bug diagnosis

Code quality

Architectural judgment

Verification quality

Long-horizon task completion

Cost efficiency

يجب أن نفصل بين سلامة Runtime وجودة الاستدلال الهندسي.

Source: [RDMS-10-M24-U171](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5099>); source-unit SHA-256 `e1e8b684254d39ac107bb279ec5e45557b943ff85b69e7caba0341caf44b539a`.

### L7-A24-U173 — 149. No Second Executive

لا تستطيع أي من عقود C01 إنشاء سلطة معرفية جديدة.

Source: [RDMS-10-M24-U173](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5124>); source-unit SHA-256 `8bb9d9e09c301d359f206adb20c86f2ecc814301e05889b871c500791643d6a8`.

### L7-A24-U174 — 150. No Second CommitGate

كل تعديل قانوني للحالة المعرفية يبقى تحت RDMS-01.

Source: [RDMS-10-M24-U174](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5128>); source-unit SHA-256 `ae54d780c0a070e82d3b9ecd84afb75e7aa6ee5b7c16586606491937ff06f04d`.

### L7-A24-U175 — 151. No Second ActionGate

أي تنفيذ خارجي جديد من الوكيل يخضع إلى RDMS-04.

Source: [RDMS-10-M24-U175](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5132>); source-unit SHA-256 `b1bcf4be8556ef42d756927fcc6ebe2f554ea8709fe2d2b16c3a9a9ea8d90976`.

### L7-A24-U176 — 152. No Second Dependency Engine

كل تقييم Freshness قانوني يستخدم محرك RDMS-06.

Source: [RDMS-10-M24-U176](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5136>); source-unit SHA-256 `346e109ddda42d43ad7aec263bb98832327d2322e643f6e5f5b40268c7b330e5`.

### L7-A24-U177 — 153. No Second Scheduler

كل Trigger أو التزام زمني يخضع إلى RDMS-05.

Source: [RDMS-10-M24-U177](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5140>); source-unit SHA-256 `1227cd25cf40b5355f583829f3727a3d9f673e8ca72786f3b85582ab5b0e2bbc`.

### L7-A24-U178 — 154. No Direct Provider Authority

لا يمكن لمخرجات LLM أن تتحول إلى تفويض قانوني دون المسار المعتمد.

Source: [RDMS-10-M24-U178](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5144>); source-unit SHA-256 `d0610908b456f43ec437c7331a288c97cd1ba58130ca60739d9d60fc69eab8b8`.

### L7-A24-U179 — 155. No Implicit Specialist Authority

لا يستطيع Specialist أن يمنح نفسه صلاحيات أو يدمج نتائجه مباشرة.

Source: [RDMS-10-M24-U179](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5148>); source-unit SHA-256 `00fa3164b8c43395aea43a0c78a9d822302af0159f375cb087c4f4eb7896615a`.

### L7-A24-U180 — 156. No Reinterpretation of External Effects

لا يجوز أن يؤدي نجاح انتقال معرفي إلى إثبات أثر خارجي لم تتم ملاحظته أو التحقق منه.

Source: [RDMS-10-M24-U180](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5152>); source-unit SHA-256 `768ffdeebda4c386f1986ecf0e2e59202430e72e5718ac5665a1d114baa6176b`.

### L7-A24-U181 — 157. No Recovery-Based Authority Escalation

توقف مكون أو فقدان الاتصال به لا يمنح مكونًا آخر سلطة لم تكن لديه.

Source: [RDMS-10-M24-U181](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5156>); source-unit SHA-256 `0d1f28d426371b53adda8e6c3cf0d7419ca48d7b284ea64ec3704ba423d0665d`.

### L7-A24-U182 — PART XXVI — ADDITIONAL FORMAL INVARIANTS

تُقترح إضافة الثوابت التالية بعد RDMS10-I01…I40.

RDMS10-I41 — Every canonical contract has one authoritative semantic owner.

RDMS10-I42 — Transport projections cannot silently redefine frozen canonical entities.

RDMS10-I43 — Trusted authority fields must originate from, or be verified by, an authorized control boundary.

RDMS10-I44 — Untrusted payload content cannot authenticate its own sender or legal authority.

RDMS10-I45 — Human instruction authority is scoped to the authenticated principal and relevant decision domain.

RDMS10-I46 — Canonical cognitive commits and repository mutations remain distinct legal effects.

RDMS10-I47 — Executive operation selection must remain bound to the current legal goal, state and authority conditions.

RDMS10-I48 — Action lifecycle durability must preserve a single legal history across control and action storage domains.

RDMS10-I49 — Shared-world dispatch requires durable evidence of the applicable authorized dispatch intent.

RDMS10-I50 — Executed operation identity, effective arguments and resource scope must conform to the authorized execution intent.

RDMS10-I51 — Message redelivery does not authorize a new external effect.

RDMS10-I52 — Execution attempts and external effects are distinct from transport deliveries.

RDMS10-I53 — Recovery-critical artifact references require appropriate durable publication before canonical adoption.

RDMS10-I54 — Cross-component event processing preserves required causal ordering and idempotency.

RDMS10-I55 — Tool reports cannot be promoted into stronger verified-world claims without appropriate evidence.

RDMS10-I56 — Goal finalization requires evidence scoped to its applicable acceptance criteria and unresolved obligations.

RDMS10-I57 — Dependency invalidation must reach affected active, queued and pending work.

RDMS10-I58 — Already dispatched effects remain subject to reconciliation after their originating plans become invalid.

RDMS10-I59 — Reasoning-provider compatibility must be checked for each required invocation capability.

RDMS10-I60 — Invalid or malformed provider output cannot become a legal proposal or authorization through permissive parsing.

RDMS10-I61 — Context disclosure must be authorized for the destination and current applicable policy.

RDMS10-I62 — Provider fallback cannot inherit unrelated disclosure permissions.

RDMS10-I63 — Specialist tool authority must be enforced at actual execution boundaries.

RDMS10-I64 — Specialist integration requires current dependency and repository compatibility assessment.

RDMS10-I65 — Independent specialist verification does not automatically establish correctness of the merged result.

RDMS10-I66 — Trigger reaction identity and derived action identity must preserve their legal causal relationship.

RDMS10-I67 — Runtime component availability does not itself authorize operational activation.

RDMS10-I68 — Recovery admission constrains the operation classes permitted during startup and recovery.

RDMS10-I69 — Project identity and authority scope must be enforced across shared services.

RDMS10-I70 — Cross-project access requires explicit applicable authority.

RDMS10-I71 — Execution containment claims must match actual reachable resources and effects.

RDMS10-I72 — Missing containment proof prevents use of the ephemeral sandbox fast path.

RDMS10-I73 — Component implementation does not imply capability activation eligibility.

RDMS10-I74 — Safety-critical capabilities cannot activate while mandatory enforcement dependencies are absent or simulated by non-conformant stubs.

RDMS10-I75 — Integration optimizations cannot bypass mandatory legal authority, durability or trust requirements.

Source: [RDMS-10-M24-U182](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5160>); source-unit SHA-256 `8cad7a215584e0b94c7dd453119846ef56ab5fbb4246ecd24cfac40d56b772ab`.

### L7-A25-U001 — 1. Purpose

تعالج RDMS-10 C02 ثماني ثغرات تكاملية، موزعة على أربعة مجالات:

Domain	Findings	Objective
Durable Handoff	R2-G01, G04	عدم فقدان الالتزامات أثناء انتقال العمل بين المكونات
Effective Execution Authority	R2-G02, G03, G07	ضمان أن التنفيذ الفعلي يطابق التفويض الحالي
Observation & Disclosure Integrity	R2-G05, G06	الحفاظ على معنى الأدلة وحدود الإفصاح
Completion Consistency	R2-G08	ربط إعلان الإنجاز بالحالة التي تثبتها الأدلة

Source: [RDMS-10-M25-U001](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5583>); source-unit SHA-256 `f70f0a8635a42e7f22836c545e55a4c9b87089a06bc69bfde51d284c2c843fc2`.

### L7-A25-U002 — 2. Architectural Conservation

يجب أن تحافظ التصحيحات على السلطات المجمدة:

Executive
    Semantic authorization

RDMS-01
    Canonical control
    CommitGate
    Control Ledger
    Executive epoch

RDMS-03
    Observation Ingress

RDMS-04
    ActionGate
    Action lifecycle
    Action Journal
    Reconciliation

RDMS-05
    Trigger lifecycle
    Durable commitments

RDMS-06
    Dependency validity
    Specialist governance

RDMS-07
    Memory governance

RDMS-08
    Cognitive control

RDMS-09
    Recovery governance

RDMS-10
    Integration contracts
    Cross-boundary enforcement

RDMS-10 لا تصبح مصدر سلطة قانونية جديدًا.

Source: [RDMS-10-M25-U002](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5592>); source-unit SHA-256 `0c8d2d4d84c69fa81552a7dac91c7039baeb3e9d1ee2028b2daec52825391fa0`.

### L7-A25-U003 — 3. Central Integration Principle

نعتمد:

A legal decision must remain traceable to its authorized continuation, while every actual effect must remain separately accountable.

أي أن القرار القانوني يجب أن تكون استمراريته قابلة للتتبع، بينما تحتفظ الآثار الفعلية بمسار مستقل لتسجيلها والتحقق منها.

نميز بين:

Decision authorized
       ≠
Work durably scheduled
       ≠
Action authorized
       ≠
Action dispatched
       ≠
World effect verified

ولا يجوز لأي مكون استنتاج المرحلة التالية بمجرد تحقق المرحلة السابقة.

Source: [RDMS-10-M25-U003](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5637>); source-unit SHA-256 `8d946d734fa9bd236373077782f87dcc899405632d51f2078349930cbe5c4a73`.

### L7-A25-U006 — 5. Architectural Decision

نعتمد:

Durable action continuity belongs to the authoritative action lifecycle, not to transport queues.

بالعربية:

استمرارية Action تأتي من سجلها القانوني، وليس من مجرد وجود رسالة داخل Queue.

Source: [RDMS-10-M25-U006](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5674>); source-unit SHA-256 `c208f57e02a4d529b77fd79f598353276dc4737e9b6b2a51cfd53f67c2aef2bf`.

### L7-A25-U007 — 6. RecoverableActionDeliveryObligation

[Record declaration: consult its sole owner in the contract registry.]

هذا العقد لا ينشئ ActionLifecycle ثانية.

بل يحدد كيفية اكتشاف التزامات التسليم والمتابعة انطلاقًا من الحالة القانونية التي تملكها RDMS-04.

Source: [RDMS-10-M25-U007](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5684>); source-unit SHA-256 `028f3641e48837daafad5d0cfed751cd78c99a8ed3a3fc18e0b0690154fbd9a3`.

### L7-A25-U008 — 7. Durable Enumeration

بعد Crash، يجب أن تستطيع Recovery البحث في المصدر القانوني عن العمليات التي تحتاج إلى متابعة.

تشمل الحالات:

AUTHORIZED

DISPATCH_INTENT

RESULT_REPORTED

PARTIAL

IN_DOUBT

RECONCILING

بحسب شروط الاستمرار والتسوية الخاصة بكل حالة.

لا يعني وجود Action داخل إحدى هذه الحالات أن جميعها قابلة لإعادة الإرسال.

Source: [RDMS-10-M25-U008](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5713>); source-unit SHA-256 `53ba2cf9f8682a9738eae3798fce70a9adf019b4ebc09f22e15dfc5634cf5de9`.

### L7-A25-U009 — 8. Recovery Decision

إذا وجدت Recovery:

Action X:
    DISPATCH_INTENT

Delivery acknowledgement:
    MISSING

فالقرار ليس:

Retry X.

بل:

Determine whether X may have been dispatched.
        ↓
Inspect available delivery/effect evidence.
        ↓
Apply RDMS-04 retry/outcome semantics.
        ↓
Reconcile or continue lawfully.

Source: [RDMS-10-M25-U009](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5735>); source-unit SHA-256 `2047ce24bf87faf0b7647eb7380bb7d3e338a37b9dbac6a51f2387339cb120a2`.

### L7-A25-U010 — 9. Old Executive Epoch

إذا كانت Action تحمل AUTHORIZED من Executive Epoch قديمة، فيلزم اعتمادها من Executive الجديدة وفق FCA قبل إرسال أثر جديد.

أما إذا وصلت إلى DISPATCH_INTENT أو مرحلة لاحقة، فتدخل مسار Reconciliation المناسب.

لا تعيد RDMS-10 تعريف هذه القاعدة.

Source: [RDMS-10-M25-U010](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5758>); source-unit SHA-256 `3d5c8c74a94feb8ca7ec68f4340673bbdec02bc241c57657f6b46ff3f3e46c48`.

### L7-A25-U011 — 10. Queue Authority

Queue تستطيع:

تخزين رسالة نقل.

إعادة تسليم رسالة.

إبلاغ Worker بوجود مهمة.

دعم جدولة التنفيذ.

لكنها لا تستطيع:

إنشاء Authorization جديدة.

إعلان فشل أثر خارجي.

تحويل IN_DOUBT إلى FAILED.

إعطاء إذن جديد بإعادة تنفيذ Action.

Source: [RDMS-10-M25-U011](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5766>); source-unit SHA-256 `f899a6918161735eef9bcfabe77030b84efbfcbfd5fc3b3f971a7dd36fe0bfb9`.

### L7-A25-U012 — 11. Enforcement Point

يجب أن تتحقق Execution Boundary من أن الطلب الذي تسلمته مرتبط بسجل قانوني صالح.

لا يكفي مجرد وجود رسالة تحمل Action ID.

Source: [RDMS-10-M25-U012](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5788>); source-unit SHA-256 `d7356c01b150e6517b43cb92a139d406e24e89e85d05f906c2085f215afe9ea8`.

### L7-A25-U013 — 12. Crash Cases

Crash point	Required behavior
قبل تسجيل AUTHORIZED	لا يوجد تفويض قانوني معتمد
بعد AUTHORIZED وقبل DISPATCH_INTENT	متابعة قانونية؛ وإعادة اعتماد عند تغير Epoch وفق FCA
بعد DISPATCH_INTENT وقبل التسليم المعروف	لا افتراض بعدم الإرسال؛ فحص وتسوية
بعد التسليم وقبل Acknowledgement	عدم إعادة التنفيذ عمياء
بعد حدوث World Effect وقبل التسجيل	الحفاظ على عدم اليقين حتى تتوفر الأدلة
بعد Result Report وقبل Effect Verification	عدم اعتبار التقرير وحده تحققًا نهائيًا

Source: [RDMS-10-M25-U013](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5794>); source-unit SHA-256 `096931f949f25cb430bbcc28f0ebfc77b6bbe5be64819d9add0de2784982ced9`.

### L7-A25-U014 — 13. Closure Requirement

يعتبر R2-G01 مغلقًا على مستوى المواصفة عندما يكون كل التزام متابعة ضروري قابلًا للاكتشاف بعد Crash من مصدر متين معتمد، دون تحويل اكتشافه إلى تفويض تلقائي بإعادة التنفيذ.

FR10-R2-G01: ADDRESSED

Source: [RDMS-10-M25-U014](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5802>); source-unit SHA-256 `279906105e5671769367fd04619ad10c6f0a82b118cdfb8c9f46ba50b472bd14`.

### L7-A25-U017 — 15. Architectural Decision

نعتمد:

A committed reaction must not lose its required downstream continuation.

لكن لا يجوز أن تتحول Reaction إلى تفويض Action تلقائي.

Source: [RDMS-10-M25-U017](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5819>); source-unit SHA-256 `7ce75fb0c6ea019da2c196965248307168dcc3e993e70737d08bd23ed4ec2e78`.

### L7-A25-U018 — 16. TriggerDerivedWorkCommitment

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M25-U018](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5827>); source-unit SHA-256 `8202cf44065ffe577f2ccf2513d5d60b9e29889ecbdca72b2f07b637bc74ce43`.

### L7-A25-U019 — 17. Atomicity Rule

إذا كان قبول Reaction يستلزم تسجيل التزام متابعة، فيجب أن تكون البيانات اللازمة لاستعادة هذا الالتزام مشمولة بالحد الذري القانوني نفسه أو ببروتوكول مكافئ يضمن عدم فقدانها.

مثال قانوني:

Canonical Reaction Accepted
          +
Required Continuation Reference
          +
Control State Version
          ↓
One recoverably consistent transition

هذه ليست مطالبة بإنشاء Action فعلية دون تفويض.

إنما نضمن أن النظام لن ينسى ضرورة معالجة العمل المشتق.

Source: [RDMS-10-M25-U019](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5853>); source-unit SHA-256 `a2f3413cd3f55b17cc29b0f35146bf6bc2c61e16d4bd19e8732cc49b4f80ea6b`.

### L7-A25-U020 — 18. Action Proposal Creation

يمكن أن يكون العمل المشتق:

A. Canonical follow-up task

B. Executive reassessment requirement

C. ActionProposal requiring authorization

D. Observation or dependency revalidation

تحدد المواصفات المالكة المسار القانوني المناسب.

لا نسمح لـRDMS-05 بالحلول محل Executive في اتخاذ قرار دلالي جديد.

Source: [RDMS-10-M25-U020](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5871>); source-unit SHA-256 `1b81519154c07630e100de27d24a315dd1fc334a0f597c106de9f0af7e0c824c`.

### L7-A25-U021 — 19. Replay Rule

إذا وصلت Trigger نفسها مرة أخرى:

تُحدد هوية Reaction القانونية.

يُفحص هل سبق اعتمادها.

لا تُعتمد Reaction مرة ثانية بصورة غير قانونية.

يُفحص التزام العمل المشتق القابل للاستعادة.

تُستأنف المعالجة غير المكتملة فقط وفق مسارها القانوني.

Source: [RDMS-10-M25-U021](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5887>); source-unit SHA-256 `248cf04a49cc1d17ccc65bf19671e38d5053aa59257130ef96e5ffb744993790`.

### L7-A25-U022 — 20. Example

Event E1:
    Build pipeline completed.

Reaction R1:
    Accepted and committed.

Continuation:
    Evaluate deployment eligibility.

Crash.

بعد إعادة التشغيل:

R1 already committed.
        ↓
Find durable continuation.
        ↓
Executive evaluates deployment.
        ↓
ActionProposal if appropriate.
        ↓
ActionGate.

لا يعني قبول R1 أن Deployment أصبحت مصرحًا بها.

Source: [RDMS-10-M25-U022](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5901>); source-unit SHA-256 `cc9a33685849eb0ef2deec08556df76b6a5ae388b0630521c34540ef33e7155a`.

### L7-A25-U023 — 21. Ownership Boundary

RDMS-05 تملك Trigger وReaction.

RDMS-01 تملك ذرية التسجيل القانوني.

RDMS-08 تملك الاختيار المعرفي.

RDMS-04 تملك Action إن جرى إنشاؤها.

RDMS-10 تربط هذه المسؤوليات.

Source: [RDMS-10-M25-U023](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5927>); source-unit SHA-256 `39d07d3382f4f614b53ff8e9dce821161937906cd7938a05a6fd261601da796b`.

### L7-A25-U024 — 22. Required Compatibility

يجب أن يثبت التنفيذ أن RDMS-05 وRDMS-01 تستطيعان تمثيل التزام الاستمرار دون تعديل خفي لقانون مجمد.

إذا ظهر تعارض حقيقي في شكل الانتقال القانوني، يجب إعلانه في مراجعة التكامل بدل إضافة سجل قانوني منافس.

FR10-R2-G04: ADDRESSED

Source: [RDMS-10-M25-U024](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5939>); source-unit SHA-256 `03f8ddcc86850f79bda6956f9a42cae47fdddd74be55d24a7ecff2cc9c4da67e`.

### L7-A25-U027 — 24. Architectural Decision

Authorization must bind the effective operation, not only its original textual representation.

لا يكفي ختم النص الذي أنتجته LLM.

يجب أن يغطي التفويض دلالة العملية الفعلية ونطاق آثارها.

Source: [RDMS-10-M25-U027](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5969>); source-unit SHA-256 `f5783e702b58d3f09873318801c0e9f635a2b3b1acb6fe5f3e9fae70d3c2d562`.

### L7-A25-U028 — 25. EffectiveExecutionBinding

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M25-U028](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5977>); source-unit SHA-256 `cf1460ef3d1aa5e0dd740105e627f583b8a5c9da90cd82f96a3db83ee52f131a`.

### L7-A25-U029 — 26. Three Execution Representations

نميز بين:

Requested Operation

ما اقترحته Capability أو Provider.

Authorized Effective Intent

ما وافقت عليه Executive وActionGate ضمن نطاق معروف.

Actual Dispatch Operation

ما ستحاول Executor إرساله أو تنفيذه بالفعل.

المطلوب:

Actual Dispatch Operation
    must conform to
Authorized Effective Intent

Source: [RDMS-10-M25-U029](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6005>); source-unit SHA-256 `22a277b1bc92ebba358dccb15f15f04ce17e53d4fbe704c29485aa39c12bf582`.

### L7-A25-U030 — 27. Last Enforceable Boundary

يجب أن يحدث التحقق النهائي عند حد تستطيع البنية عنده منع العملية غير المطابقة.

لا يكفي إجراء فحص داخل Planning ثم ترك Tool Adapter تغير الوسائط دون رقابة.

Source: [RDMS-10-M25-U030](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6026>); source-unit SHA-256 `c3802f6e5466b0b7883098e0d2f1abf0347b15253e08484442a4b3ad2cfe876f`.

### L7-A25-U031 — 28. Resource Identity

قد تكون:

./output

اسمًا نسبيًا.

لا يجوز افتراض أنها تشير دائمًا إلى المورد نفسه.

ينبغي تحديد هوية المورد الفعلية وفق إمكانات البيئة ونوع العملية.

قد يتطلب ذلك تثبيت مرجع المورد أو إعادة التحقق منه عند الاستخدام.

Source: [RDMS-10-M25-U031](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6032>); source-unit SHA-256 `377283851d9d18e32c167f0fb6236f378d1873706f4a075f64551edafef73c2b`.

### L7-A25-U032 — 29. Tool Version

إذا تغيرت نسخة Tool Adapter بصورة تغير معنى Arguments أو آثار الأمر، يجب ألا ترث Authorization سابقة دون تقييم التوافق.

Source: [RDMS-10-M25-U032](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6046>); source-unit SHA-256 `b677db2337c9bdf498489e18d6105cbd793c485533358f012140b68aa164bfec`.

### L7-A25-U033 — 30. Failure Behavior

إذا تعذر إثبات المطابقة:

Dispatch eligibility:
    REJECTED

مع الحفاظ على Action القانونية والتفويضات المسجلة حسب حالتها الفعلية.

لا يجوز اعتبار رفض الإرسال دليلًا على عدم وجود إرسال سابق من محاولة أخرى.

Source: [RDMS-10-M25-U033](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6050>); source-unit SHA-256 `57fa3751343731af5f015f5574e74105e0df082d31739b15191f1381f6a72bc1`.

### L7-A25-U034 — 31. No Hidden Tool Effects

إذا كانت أداة تستطيع إحداث آثار أوسع من النطاق المصرح، يجب تصنيف العملية وفق الآثار القابلة للوصول.

وإذا تعذر إثبات العزل، تُطبق قواعد SHARED_WORLD وفق FCA.

FR10-R2-G02: ADDRESSED

Source: [RDMS-10-M25-U034](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6061>); source-unit SHA-256 `b8f75319a486074171033d07db0c8f4b16a0f147ff0b66def596cada06b136de`.

### L7-A25-U037 — 33. Architectural Decision

نحتاج نقطة ترتيب قانونية واضحة بين:

Relevant invalidation

و:

Dispatch admission

لكن لا نفترض معاملة ذرية مع كل خدمة خارجية.

Source: [RDMS-10-M25-U037](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6078>); source-unit SHA-256 `48ce0c3bbfbbea5b599bf9b79d5415446c379d7f40fbae5e8140ccb990a3c00e`.

### L7-A25-U038 — 34. DispatchAdmissionCutover

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M25-U038](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6090>); source-unit SHA-256 `0079f235a4c2cfec539347308d7c97285ace60a603fdf96f544a1ccf7380b6ba`.

### L7-A25-U039 — 35. Legal Ordering

إذا حدث:

Invalidation committed
        ↓
Dispatch eligibility evaluated

فيجب تقييم الأثر الحالي للإبطال قبل السماح بالإرسال.

أما إذا وقع الحدثان بالتزامن، فيجب أن تفرض Control Boundary ترتيبًا قانونيًا محددًا في النطاق الذي تملكه.

Source: [RDMS-10-M25-U039](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6118>); source-unit SHA-256 `460b47d2fc55a2d468bb579764c9d47004ed2e2b9c011d773fe87383b0d067c2`.

### L7-A25-U040 — 36. Pre-Dispatch Protection

قبل إرسال عملية جديدة، يجب إثبات:

Current epoch eligible

Relevant authority valid

Relevant dependencies valid

Applicable policy conditions satisfied

Sealed operation matches actual operation

Dispatch intent durable

Execution generation permitted

هذه شروط تقييم تكاملي، وليست ActionGate ثانية.

Source: [RDMS-10-M25-U040](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6130>); source-unit SHA-256 `89d566c597a5de16feafe9ec501ee6c22eb4bc4294f6fb07ac197d518b76e2e5`.

### L7-A25-U041 — 37. Race After Admission

قد يحدث تغير خارجي بعد آخر فحص وقبل وصول الطلب إلى الخدمة.

لا تستطيع المعمارية أن تضمن اختفاء هذا الاحتمال في كل نظام خارجي.

يجب أن تحدد العقود:

ما الذي تستطيع منعه عند حدودها الموثوقة.

ما الذي قد يصبح in-flight.

ما الذي يحتاج إلى Reconciliation.

ما الذي لا يمكن الادعاء بإلغائه.

Source: [RDMS-10-M25-U041](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6150>); source-unit SHA-256 `0974465a41fdd946a5cba627f2cd6fd64a6ab23c04cb454f669c71c2aece31de`.

### L7-A25-U042 — 38. Revocation Rule

إبطال Authorization لا يعني:

Already dispatched effect = cancelled.

إذا كانت Action قد تصل إلى العالم الخارجي أو وصلت إليه، تظل تحت RDMS-04.

Source: [RDMS-10-M25-U042](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6166>); source-unit SHA-256 `44af64d4b8b2dbdebc9fabafae797a299fe8ce01690b7d461b34b34c27f8279b`.

### L7-A25-U043 — 39. No Unbounded Global Lock

لا نطلب قفلًا عالميًا يمنع جميع أنشطة النظام أثناء كل Action.

يجب أن تكون ترتيبات التزامن محددة النطاق وفق الاعتماديات والموارد المتأثرة.

إذا تعذر إثبات نطاق ضيق، يمكن استخدام قيود أكثر تحفظًا.

Source: [RDMS-10-M25-U043](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6174>); source-unit SHA-256 `17c6e949793384ccd36644ef7ec3fd73f7b488f92b7e3fc19d619f866e215415`.

### L7-A25-U044 — 40. Required Enforcement

لا يجوز لـWorker استخدام نتيجة قديمة من Dependency Engine كتصريح دائم.

يجب أن تكون صلاحية العملية مرتبطة بنقطة الإرسال القانونية الحالية.

FR10-R2-G03: ADDRESSED

Source: [RDMS-10-M25-U044](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6182>); source-unit SHA-256 `46f5d8543c9408ed65e2a83f8e4413ac7e32bb2eac8480caca3a90c94482de36`.

### L7-A25-U047 — 42. Architectural Decision

A service's technical reach is not the authority of the request it executes.

قد تكون الخدمة قادرة تقنيًا على تعديل مورد.

لكن هذا لا يعني أن الطلب الحالي مصرح له بتعديله.

Source: [RDMS-10-M25-U047](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6201>); source-unit SHA-256 `da901dfec6f212de3f6c9570c535171dc8b09ad39e079bad28232fd81bd75143`.

### L7-A25-U048 — 43. EffectiveExecutionAuthorityScope

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M25-U048](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6209>); source-unit SHA-256 `cd3e88675509b589c5e273adf070b594221d5f6c1d4dea44bc2c76b8743a527a`.

### L7-A25-U049 — 44. Authority Intersection

يجب أن تكون الصلاحية الفعلية للعملية داخل تقاطع القيود التالية:

Originating project authority

Executive authorization

ActionGate restrictions

Tool policy

Resource policy

Credential scope

Execution boundary

لا يمكن لقيد أوسع أن يلغي قيدًا أضيق ملزمًا.

Source: [RDMS-10-M25-U049](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6235>); source-unit SHA-256 `103597e7e39264b151f1b6a472262a7ba7b8f9881e4770eb36188e2b3b3baa9e`.

### L7-A25-U050 — 45. Shared Worker Rule

إذا وصل:

Request:
    Project A

Target:
    Resource belonging to Project B

يجب إثبات تفويض Cross-Project المناسب.

لا يكفي أن تكون Worker قادرة على الوصول إلى المورد B.

Source: [RDMS-10-M25-U050](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6255>); source-unit SHA-256 `c0341354a75c3b43c5cd17436f8802ab21b65030116074c8e1424b1d7038d8a2`.

### L7-A25-U051 — 46. Credential Binding

يجب ألا تختار Worker Credential واسعة الصلاحيات ثم تفترض أن الطلب أصبح مخولًا بالوصول إلى جميع الموارد التي تستطيع Credential تعديلها.

يجب فرض العلاقة بين التفويض والمورد المستهدف.

قد تستخدم البنية Credentials مقيدة أو Credential Broker أو وسيلة مكافئة.

Source: [RDMS-10-M25-U051](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6269>); source-unit SHA-256 `cd62dd20df83852093d8ae50d58ceb291e93bdac07d08d4074069966f6803268`.

### L7-A25-U052 — 47. Resource Resolution

يجب التحقق من هوية الهدف النهائي بعد تحويل المسارات أو أسماء الموارد أو معرفات الخدمات المؤثرة.

فالتحقق من project_id قبل حل Resource Target لا يثبت صلاحية المورد النهائي.

Source: [RDMS-10-M25-U052](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6277>); source-unit SHA-256 `3e71ba896c6b60a35474b90c4725459ba53fe6ce88e51325a2457667aa522c01`.

### L7-A25-U053 — 48. Enforcement Limits

إذا كانت Execution Boundary لا تستطيع تقييد أو التحقق من آثار الخدمة الخارجية بدرجة كافية، فلا يجوز الادعاء بتحقيق العزل المطلوب.

يجب رفض العملية أو استعمال مجال تنفيذ أضيق يحقق الضمان.

FR10-R2-G07: ADDRESSED

Source: [RDMS-10-M25-U053](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6283>); source-unit SHA-256 `9d01d3b7d3b0261883e5093e2598a74cd26efc285b78636d2fa39dda6a6cf12b`.

### L7-A25-U056 — 50. Architectural Decision

Observation admission and causal interpretation are distinct legal operations.

تسجيل ما قاله المصدر أو رصده يختلف عن إثبات السبب أو ربط الحدث بعملية محددة.

Source: [RDMS-10-M25-U056](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6302>); source-unit SHA-256 `ff7a3b2820eda3fda4fd224593d024e5c3d04a356e0635fd1ed09f003f50f3db`.

### L7-A25-U057 — 51. ObservationCausalAttachmentContract

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M25-U057](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6308>); source-unit SHA-256 `5a2068a7ab445108d88f367973bd4d30aa82f1e73982c9187b3ee0a7464519fc`.

### L7-A25-U058 — 52. Raw Observation Admission

يمكن قبول Observation خام إذا استوفت قواعد RDMS-03 الخاصة بالنوع والمصدر والهوية والسلامة.

لا يلزم أن تكون جميع علاقاتها السببية قد ثبتت مسبقًا.

Source: [RDMS-10-M25-U058](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6332>); source-unit SHA-256 `489afffb6fa347887170b91fde1f47995e744fd45f453c874a765bad9de8de5c`.

### L7-A25-U059 — 53. Example

تصل رسالة:

Deployment service reports:
    Release R42 is active.

يمكن تسجيل:

Observation:
    Service reported R42 active.

لكن لا يجوز استنتاج:

Action X caused release R42.

دون دليل يربط العملية بذلك الإصدار.

Source: [RDMS-10-M25-U059](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6338>); source-unit SHA-256 `14fa90b63df9750eb6a31025562fffad24602465231f5ed914a6136a4adf0c48`.

### L7-A25-U060 — 54. Deferred Causal Attachment

إذا كانت ActionRecord مفقودة مؤقتًا:

Raw Observation accepted
        ↓
Causal relationship unresolved
        ↓
Related record recovered
        ↓
Causal evaluation performed
        ↓
EvidenceLink proposed/committed legally

لا يجوز تعديل Observation الخام بصورة صامتة لجعل التاريخ يبدو متناسقًا.

Source: [RDMS-10-M25-U060](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6356>); source-unit SHA-256 `c14cc466207123de5700f763bd35f764fcdcf42462ae1bbfdf4250517b8f99e5`.

### L7-A25-U061 — 55. Duplicate Delivery

إذا وصلت Observation نفسها أكثر من مرة، يجب الحفاظ على قواعد هوية الحدث وإزالة التكرار المناسبة.

ولا يجوز دمج حدثين مختلفين لمجرد تشابه النص.

Source: [RDMS-10-M25-U061](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6372>); source-unit SHA-256 `7d9b237ab82195172aa56ec2beb828f295f23e9b6f4a87db292c47c0782b738d`.

### L7-A25-U062 — 56. Unsupported Causality

إذا لم تتوفر أدلة كافية لإثبات الارتباط:

Causal claim:
    NOT ESTABLISHED

يمكن أن تبقى Observation مفيدة في نطاقها الأصلي.

Source: [RDMS-10-M25-U062](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6378>); source-unit SHA-256 `19a3e91ea2e3448e28255a2d463cdf67eb33e4b6529abc499cc4a8f3283de79d`.

### L7-A25-U063 — 57. Owner

RDMS-03 تملك Observation وEvidence semantics.

RDMS-04 تملك Action outcome.

RDMS-10 تحدد الربط بينهما عبر حدود النقل.

FR10-R2-G05: ADDRESSED

Source: [RDMS-10-M25-U063](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6387>); source-unit SHA-256 `426b5a216b5b978909a31d5148d10f1271463b1ae47a01cc57d0a4519fa19154`.

### L7-A25-U066 — 59. Architectural Decision

Disclosure approval must bind the actual outbound content, destination and processing purpose.

Source: [RDMS-10-M25-U066](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6408>); source-unit SHA-256 `493d039e1c0ff5a441070cd5b2919401114daf3d769b6ce131140db09d413b8d`.

### L7-A25-U067 — 60. SealedOutboundContext

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M25-U067](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6412>); source-unit SHA-256 `029f8848c7f121f837fae1d32c65a260e70b10bece525dd8db695869353456f5`.

### L7-A25-U068 — 61. Outbound Sequence

Assemble candidate context
        ↓
Resolve included sources
        ↓
Determine final destination
        ↓
Apply current disclosure policy
        ↓
Seal effective outbound context
        ↓
Verify seal at trusted egress boundary
        ↓
Transmit

Source: [RDMS-10-M25-U068](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6438>); source-unit SHA-256 `6e530922cf96a0c2985c68f915411d316ad1a9a7bf8c37993f374e8059cb6781`.

### L7-A25-U069 — 62. Content Modification

إذا تغير محتوى مؤثر بعد الموافقة:

Previous disclosure approval:
    NOT REUSABLE

ويجب إعادة التقييم حسب طبيعة التغيير.

Source: [RDMS-10-M25-U069](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6452>); source-unit SHA-256 `e26875bf9287e1e6f5ef3c9d77760de3a9eb7bc1230186c120f30fdd910eb443`.

### L7-A25-U070 — 63. Provider Switching

إذا تغيرت Provider:

Provider A
    ↓
Provider B

فلا يجوز نقل تصريح الإفصاح من A إلى B دون تقييم جديد.

Source: [RDMS-10-M25-U070](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6461>); source-unit SHA-256 `da67d481a1ecaf8e56636523baf50ccb0f6929b78a707a0d86717e760700e7dd`.

### L7-A25-U071 — 64. Streaming

إذا استُخدم Streaming أو إرسال على دفعات، يجب أن يغطي التفويض جميع الأجزاء التي يسمح النظام بإرسالها.

لا يجوز إلحاق أجزاء جديدة غير مشمولة بالسياسة بعد إرسال أول دفعة.

Source: [RDMS-10-M25-U071](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6471>); source-unit SHA-256 `a50a8dd40c2c2438b39eb8aac50205409254fffe416eb01128117c83cbe2aaea`.

### L7-A25-U072 — 65. Post-Seal Transformations

أي تحويل بعد الختم قد يؤثر في المحتوى أو الوجهة، مثل:

Middleware injection

Additional logging context

Tool-result expansion

Memory expansion

Provider request rewriting

يجب أن يكون:

مثبتًا أنه لا يغير نطاق الإفصاح المعتمد، أو

مشمولًا بعقد التحقق، أو

سببًا لإعادة تقييم الإذن.

Source: [RDMS-10-M25-U072](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6477>); source-unit SHA-256 `e3982be92c7de12445dd5ef67bdf46a898a69f251a3305363d124c4cf1e12c63`.

### L7-A25-U073 — 66. Trusted Egress Enforcement

التحقق يجب أن يحدث عند حد موثوق يستطيع منع الإرسال.

لا يكفي أن تعلن Context Builder أن البيانات آمنة ثم يرسل مكون آخر محتوى مختلفًا.

Source: [RDMS-10-M25-U073](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6499>); source-unit SHA-256 `a95b3e21b1c0c277fd8125dd82e5432c231931ff025baa099c3e6e67598b5c04`.

### L7-A25-U074 — 67. No Independent Disclosure Authority

لا تنشئ SealedOutboundContext سياسة خصوصية جديدة.

هي تفرض السياسات التي تملكها الأنظمة المعنية، خصوصًا RDMS-07 وRDMS-09.

FR10-R2-G06: ADDRESSED

Source: [RDMS-10-M25-U074](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6505>); source-unit SHA-256 `9e21291ac11d443b64e01146e03b3825aa5c6b86ad86edc3846702cde9ea43ae`.

### L7-A25-U077 — 69. Architectural Decision

Completion claims must be bound to the actual verified state and their applicable dependency frontier.

Source: [RDMS-10-M25-U077](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6522>); source-unit SHA-256 `0db72e6bcff81005db2451f74cc2ddf4308df2298ac2de8c600226ea76b98375`.

### L7-A25-U078 — 70. CompletionStateBinding

[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M25-U078](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6526>); source-unit SHA-256 `e51e1812b9345d6dadac8f22137c6d72072733fbba4d4562c9aca5bca9ac91f6`.

### L7-A25-U079 — 71. Evidence Scope

إذا نجحت الاختبارات على:

Repository R10

فلا يجوز أن تصبح دليلًا تلقائيًا على:

Repository R11

إذا كان التغيير بينهما قد يؤثر في السلوك الذي جرى التحقق منه.

Source: [RDMS-10-M25-U079](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6550>); source-unit SHA-256 `88b6cf77fc2a3f3b5ff9a77a355b7693c94101d1e463bbb93d42200727602cc2`.

### L7-A25-U080 — 72. Scoped Freshness

لا يلزم إعادة كل الاختبارات عند تغير ملف غير مرتبط، إذا أثبت RDMS-06 أن الأدلة ما زالت صالحة.

لكن لا يجوز افتراض الاستقلال دون تقييم.

Source: [RDMS-10-M25-U080](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6562>); source-unit SHA-256 `154ebd6ed3d4272b90eb7efb7ab32b944051e878be5dc699cf2fe3dbfdcd2fa0`.

### L7-A25-U081 — 73. Finalization Commit

قبل اعتماد Finalization يجب أن تكون:

Goal version compatible

Acceptance criteria current

Verification evidence applicable

Relevant dependency frontier valid

Mandatory unresolved obligations accounted for

Source: [RDMS-10-M25-U081](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6568>); source-unit SHA-256 `8b73e565855dabc29e04c2706a3f5113199778bcb58222717053f1926410383a`.

### L7-A25-U082 — 74. External State Limitation

قد تكون Repository تحت سيطرة خدمة خارجية يمكن أن تتغير بعد Verification.

لا نفترض وجود Global Atomic Commit بين Control Ledger وGitHub.

يمكن للنظام إثبات الإنجاز بالنسبة إلى Revision أو World Scope محددة.

ولا يجوز أن يدعي دوام هذه الحالة إلى الأبد.

Source: [RDMS-10-M25-U082](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6581>); source-unit SHA-256 `4a4b13f1180bcd397c1b2c039b96ffb420663f2dacbb38293d11f8f090e063d9`.

### L7-A25-U083 — 75. Example

Verification:
    Passed on Revision R10.

Another process:
    Creates Revision R11.

Completion decision:
    Must assess whether evidence
    still covers the claimed state.

إذا لم تكن R11 مشمولة بالأدلة أو باختبار صلاحية مناسب، يجب تقييد الادعاء أو إعادة التحقق.

Source: [RDMS-10-M25-U083](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6591>); source-unit SHA-256 `1c7c6bdd4d5a4d66155d414c5c88e72b2971cf0341a5ab6a515b0eb8dab43035`.

### L7-A25-U084 — 76. Historical Completion

إذا أُنجزت Goal فعلًا عند R10 ثم تغير المشروع لاحقًا، لا يعني ذلك أن Finalization السابقة أصبحت كاذبة بالضرورة.

الصحيح هو أن يكون تقرير الإنجاز مرتبطًا بالحالة التي يغطيها.

FR10-R2-G08: ADDRESSED

Source: [RDMS-10-M25-U084](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6604>); source-unit SHA-256 `af942fb2d55398fe95d0eac4687733a674e0f4b5ee4b45b28b09617f5be17baa`.

### L7-A25-U086 — 77. Required Failure Behavior

Failure scenario	Legal response
Crash after DISPATCH_INTENT, before known delivery	Recover Action and reconcile; no blind retry
Queue message redelivered	Check authoritative lifecycle and retry eligibility
Reaction committed, derived work not completed	Recover durable continuation; no duplicate Reaction
Tool adapter changes target	Reject nonconforming effective execution
Dependency invalidated before dispatch admission	Reevaluate or deny affected operation
Potential prior dispatch during invalidation	Preserve possible effect and reconcile
Shared Worker receives cross-project target	Require applicable cross-project authorization
Observation arrives before ActionRecord	Preserve admissible raw observation; defer causal link
Context changes after disclosure approval	Reevaluate before outbound transfer
Provider changes	Reevaluate destination-specific disclosure
Repository changes after verification	Reevaluate affected completion evidence
Control history incomplete	Do not assume missing obligations never existed

Source: [RDMS-10-M25-U086](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6613>); source-unit SHA-256 `546bd76592bfe1107dc5b077890ba282b96d8d5b295666c783fac58789456799`.

### L7-A25-U087 — 78. Important Conservation

لا تؤدي هذه القواعد إلى إدخال:

New Executive

New CommitGate

New ActionGate

New Scheduler

New Dependency Engine

New Action Lifecycle

بل تجعل مسارات التكامل تستخدم المصادر القانونية الموجودة.

Source: [RDMS-10-M25-U087](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6627>); source-unit SHA-256 `925cbbc45a17aa219d819bbf7d35b6a9d55f8c98aa0221b18c000d5daaca4b56`.

### L7-A25-U089 — 79. H01 — Projection Conformance

يجب أن يحدد Contract Registry كيفية التحقق من تحويل:

Canonical Entity
    ↓
Transport Projection
    ↓
Serialization
    ↓
Deserialization
    ↓
Receiving Component

يجب ألا تُفقد الحقول التي تؤثر في:

السلطة.

هوية العملية.

النسخة القانونية.

الاعتماديات.

الصلاحيات.

شروط الاستعادة.

يمكن اختبار ذلك عبر Contract Conformance Tests.

Source: [RDMS-10-M25-U089](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6646>); source-unit SHA-256 `c19ce5619fdbe667c4721113e4e04fdba280a123ee4b2344cd532cf01bd199e3`.

### L7-A25-U090 — 80. H02 — Cancellation Semantics

يجب أن تفصل الواجهات بين:

Local request cancelled

Worker terminated

External request potentially active

External effect reconciled

ولا يجوز أن تعرض واجهة المستخدم رسالة تفيد بأن الأثر الخارجي أُلغي إذا كان المعروف فقط هو توقف Worker المحلية.

Source: [RDMS-10-M25-U090](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6676>); source-unit SHA-256 `572ccab40071d1721db7839289c2b426f4d62e2a5fee0aa26a66043013dab878`.

### L7-A25-U091 — 81. H03 — Backpressure

يجب عدم إسقاط:

Legal control events

Unresolved action obligations

Required trigger commitments

Recovery-critical references

بسبب ضغط Queue.

أما Logs التشخيصية منخفضة القيمة، فيمكن تطبيق سياسات الاحتفاظ والإسقاط المسموح بها عليها.

Source: [RDMS-10-M25-U091](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6690>); source-unit SHA-256 `5463b74836fd12e121eff158a211f58271fa2fc257a6dd83cbb71ab157b9ddb4`.

### L7-A25-U092 — 82. H04 — Interface Complexity

يجب إعادة استخدام الهويات القانونية الموجودة.

لا ننشئ:

ActionRecord v2

Alternative Trigger Lifecycle

Independent Recovery Journal

Second Authorization Token Registry

إذا كانت العقود المجمدة تستطيع تمثيل المتطلبات بصورة متماسكة.

نفضل أقل عدد من العقود التي تحقق الضمانات المطلوبة فعلًا.

Source: [RDMS-10-M25-U092](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6706>); source-unit SHA-256 `47a3a5117fd16746c5e00df1d24a89370d4e7299f5bec4a89a96ca9ce7e560c5`.

### L7-A26-U016 — FC10-03-01 — Recoverable Does Not Mean Repeatable

وجود التزام قابل للاستعادة لا يعني أن أثره الخارجي قابل لإعادة التنفيذ.

يجب استخدام RDMS-04 لتحديد أهلية إعادة المحاولة.

Source: [RDMS-10-M26-U016](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7622>); source-unit SHA-256 `bb00f422c85bd192391ee8a837e11b6e512a41d21447942e838a79d470fad202`.

### L7-A26-U017 — FC10-03-02 — Dispatch Admission Is Not External Completion

قبول dispatch قانونيًا لا يثبت وصول الأمر إلى العالم الخارجي أو حدوث أثره.

ولا يمكن إلغاء آثار محتملة عبر إبطال التفويض محليًا بعد إمكانية إرسالها.

Source: [RDMS-10-M26-U017](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7628>); source-unit SHA-256 `88ef41db554ce3683de1b124351bf2f3a76e30e63291d461ac53521e80209144`.

### L7-A26-U018 — FC10-03-03 — The Effective Operation Is the Authorized Operation

لا يجوز أن يغير Tool Adapter معنى العملية أو نطاق مواردها بعد التفويض دون تحقق قانوني ملائم.

إذا تعذر التحقق من المطابقة، يجب منع إرسال العملية الجديدة.

Source: [RDMS-10-M26-U018](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7634>); source-unit SHA-256 `6d0db6eef8028b5331cf07f1c92ee1b1da73ee2b755e019b984652368db71273`.

### L7-A26-U019 — FC10-03-04 — Trigger Continuation Is Not Action Authorization

يمكن اعتماد التزام لاستمرار العمل دون أن يعني ذلك اعتماد ActionProposal أو السماح بإرسال أثر خارجي.

Source: [RDMS-10-M26-U019](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7640>); source-unit SHA-256 `0ee3455ef0120e6a329701a105c1026f918c822b8babc6cdd74573c3b6b27004`.

### L7-A26-U020 — FC10-03-05 — Raw Observation Is Not Verified Causality

وجود Observation صحيحة لا يثبت تلقائيًا أنها نتيجة Action معينة.

يجب إثبات العلاقة وفق RDMS-03 وRDMS-04.

Source: [RDMS-10-M26-U020](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7644>); source-unit SHA-256 `216199c35e9182022d844f051bf34cdee42a41036c0a9f33ccf2246f5c6ecef3`.

### L7-A26-U021 — FC10-03-06 — Disclosure Applies to Actual Egress

إذن الإفصاح يتعلق بالبيانات الفعلية التي تغادر الحدود الموثوقة، وبالوجهة والغرض المعتمدين.

Source: [RDMS-10-M26-U021](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7650>); source-unit SHA-256 `ac8cfb93c9d8d2ee63796bfbcb5d3970880415eb0bb7e980d3740c5acfc0e130`.

### L7-A26-U022 — FC10-03-07 — Completion Is State-Scoped

يجب أن تعكس نتيجة Finalization الحالة التي تغطيها الأدلة، لا حالة مستقبلية مجهولة.

Source: [RDMS-10-M26-U022](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7654>); source-unit SHA-256 `c89cd365824d5f84d467ac036e2525a6430a01a0beffaa18b46102acf5fa3290`.

### L7-A26-U023 — FC10-03-08 — Contract Projections Cannot Redefine Their Owners

تظل المواصفة المالكة لكل نوع قانوني المصدر النهائي لمعناه.

أي اختلاف في تسمية أو تمثيل حقل لا يجوز أن يغير سلطته أو معناه.

Source: [RDMS-10-M26-U023](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L7658>); source-unit SHA-256 `0320f8065d47d9c92113923a91057bce2dc864f49639fafb2886fb2ebc93b447`.

## Retained independent baseline responsibilities

The following individually selected original clauses preserve independent duties. They are not admission of an entire historical draft. Where an amendment adds a requirement, the amended article and its sole-owner record contract govern that added requirement.


### L7-B23-001 — 1. Purpose

RDMS-10 تحدد كيفية دمج مكونات FCA وRDMS-01…09 في Runtime واحدة متماسكة.

تشمل هذه المواصفة:

المكونات المنطقية للنظام.

مسؤولية كل مكون.

ملكية البيانات والحالة القانونية.

واجهات التواصل بين المكونات.

حدود العمليات والخدمات.

حدود الصلاحيات والثقة.

العقود الموحدة للرسائل والطلبات.

كيفية تطبيق التغييرات على الحالة المعتمدة.

كيفية تنفيذ العمليات الخارجية.

كيفية إدارة المتخصصين بالتوازي.

كيفية دمج نتائجهم دون تضارب.

كيفية تنظيم الاستدعاءات إلى LLM Providers.

كيفية تشغيل المهام الزمنية والتعافي منها.

كيفية استعادة النظام بعد توقفه.

كيفية اختبار التكامل بين جميع المكونات.

الترتيب المقترح لتنفيذ المكونات برمجيًا.

Source: [RDMS-10-M23-U001](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L46>); source-unit SHA-256 `fb62b2eaf94a89a9178857611914995a4c1c28384b5d221de668cc38dc42e5f6`.

### L7-B23-002 — 2. Fundamental Architecture Rule

نعتمد:

One Canonical Cognitive Authority. Multiple Capabilities. Controlled Side Effects.

بالعربية:

سلطة معرفية معتمدة واحدة، وقدرات متعددة، وآثار خارجية محكومة.

لا يعني ذلك أن جميع المكونات يجب أن تعمل في Process واحدة.

بل يعني أن توزيع العمليات لا يؤدي إلى توزيع السلطة المعرفية القانونية.

Source: [RDMS-10-M23-U002](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L84>); source-unit SHA-256 `551f41d5a4086f595fbd5d7c44e03352ac47fb49a84dfc3978ddf6064763eec1`.

### L7-B23-003 — 3. What RDMS-10 Must Not Do

لا يجوز أن تعيد هذه المواصفة تصميم القوانين التي جُمّدت سابقًا.

لا تنشئ:

Cognitive Executive ثانية.

Canonical Workspace ثانية.

CommitGate ثانية.

ActionGate ثانية.

Dependency Evaluation Engine ثانية.

Durable Scheduler ثانية.

سلطة تعلم مستقلة.

سلطة تنفيذ خاصة بالـLLM.

نظامًا منافسًا لحالات Executive الموجودة في FCA.

أي قرار هندسي لا يستطيع الحفاظ على هذه الشروط يجب رفضه أو عرضه كتعارض يتطلب مراجعة رسمية للمواصفة المالكة.

Source: [RDMS-10-M23-U003](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L98>); source-unit SHA-256 `f82bbe48a82d3fd74e0e5a9b5ca0ff5983741e68341762348d96521ecf81c086`.

### L7-B23-004 — 4. Integrated Runtime Architecture

البنية المنطقية المقترحة:

                         USER / CLIENT
                               │
                               ▼
                     ┌─────────────────┐
                     │ Agent Interface │
                     │    Gateway      │
                     └────────┬────────┘
                              │
                              ▼
┌────────────────────────────────────────────────────┐
│                                                    │
│                 COGNITIVE RUNTIME                  │
│                                                    │
│  ┌──────────────────────────────────────────────┐  │
│  │           COGNITIVE EXECUTIVE                │  │
│  │                                              │  │
│  │        Adaptive Cognitive Control            │  │
│  │                                              │  │
│  │   Decision / Attention / Strategy            │  │
│  └──────────────────────┬───────────────────────┘  │
│                         │                          │
│             ┌───────────┴───────────┐              │
│             ▼                       ▼              │
│     Cognitive Workspace       Capability Runtime  │
│             │                       │              │
│             │             ┌─────────┴─────────┐    │
│             │             ▼                   ▼    │
│             │       Reasoning Gateway    Memory   │
│             │             │                   │    │
│             └─────────────┼───────────────────┘    │
│                           │                        │
└───────────────────────────┼────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────┐
│                                                    │
│                    CONTROL PLANE                   │
│                                                    │
│   Executive Epoch / Fencing                        │
│                                                    │
│   CommitGate                                       │
│   ActionGate                                       │
│   Control Ledger                                   │
│                                                    │
│   Specialist Lifecycle                             │
│   Dependency Evaluation                            │
│   Durable Trigger Lifecycle                        │
│                                                    │
└───────────────────────────┬────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────┐
│                                                    │
│                    ACTION PLANE                    │
│                                                    │
│   Action Journal                                   │
│   Reality Executor                                 │
│   Tool Adapters                                    │
│   Isolated Workspaces                              │
│   Specialist Execution Workers                     │
│                                                    │
└───────────────────────────┬────────────────────────┘
                            │
                            ▼
                      REAL WORLD
                            │
                            ▼
┌────────────────────────────────────────────────────┐
│                                                    │
│                 OBSERVATION PLANE                  │
│                                                    │
│   Observation Ingress                              │
│   Provenance Validation                            │
│   Evidence Interpretation                          │
│   Contradiction Detection                          │
│                                                    │
└───────────────────────────┬────────────────────────┘
                            │
                            ▼
                    COGNITIVE RUNTIME

Source: [RDMS-10-M23-U005](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L125>); source-unit SHA-256 `80852a35ce681071dd58c197f81680ea451d151dc0de73df2892acfda68f89e2`.

### L7-B23-005 — 5. Architectural Interpretation

هذا المخطط يصف المسؤوليات المنطقية.

لا يعني أن كل صندوق يمثل خدمة مستقلة أو قاعدة بيانات مستقلة.

قد تشترك عدة مكونات في العملية نفسها.

وقد يجري تشغيل بعض المكونات في Workers منفصلة.

القاعدة الأساسية هي الحفاظ على حدود السلطة والثقة والكتابة، بغض النظر عن كيفية توزيع العمليات فعليًا.

Source: [RDMS-10-M23-U006](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L209>); source-unit SHA-256 `fbbcf566ae6f0a1a61cd68a171fda0fa36cbd71787b5c9b19f5ff9dfb5e1dc4a`.

### L7-B23-006 — 6. Component Categories

نقسم المكونات إلى ست مجموعات تشغيلية:

Group	Responsibility
Cognitive Kernel	الهوية المعرفية والتفكير والاختيار
Control Services	السلطة والانتقالات القانونية
Execution Services	تنفيذ الأفعال واستخدام الأدوات
Observation Services	تسجيل الواقع والأدلة
Memory & Temporal Services	الذاكرة والالتزامات الزمنية
Infrastructure Services	التخزين والتعافي والأمان والتشغيل

كل مجموعة تحتوي على مكونات ذات مسؤوليات محددة.

Source: [RDMS-10-M23-U008](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L222>); source-unit SHA-256 `1ad646c49d6277cc20f3fbb1f8fd3e7c8048d39abca0917735f8b6fa5f80ef8a`.

### L7-B23-007 — 7. Cognitive Executive

Source: RDMS-08

Responsibility

هي صاحبة السلطة الدلالية الحالية.

تحدد:

Current Goal
Current Focus
Next Cognitive Operation
Required Cognitive Depth
Information Acquisition
Delegation
Implementation Readiness
Verification Strategy
Recovery Reassessment
Completion Decision
May

تقييم المقترحات.

اختيار العمليات المعرفية.

اعتماد التغييرات الدلالية المسموحة.

إصدار تفويضات تمر بالبوابات القانونية.

طلب معلومات إضافية.

إدارة استراتيجية التفكير والتفويض.

Must Not

الكتابة مباشرة إلى Canonical Workspace.

تجاوز CommitGate.

تجاوز ActionGate.

تغيير Observations.

ترقية Memory دون LearningGate.

منح Provider سلطة تنفيذ.

Ownership

تمتلك Executive القرار الدلالي.

لكنها لا تمتلك حق تجاوز شروط الكتابة القانونية.

Source: [RDMS-10-M23-U010](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L237>); source-unit SHA-256 `34fb76ac5fe42cc74f38412be964cb674633543e8b9419328c0159ff036c488e`.

### L7-B23-008 — 8. Canonical Cognitive Workspace

Source: FCA / RDMS-01 / RDMS-02

Responsibility

تمثل الحالة المعرفية المقبولة حاليًا.

تشمل منطقيًا:

Identity
Goals
Focus
System Mental Model
Epistemic State
Engineering State
Execution State
Temporal State
Specialist References
Memory References
Metacognitive State
Control References
Write Rule
Capability
    ↓
PatchProposal
    ↓
Executive Authorization
    ↓
CommitGate
    ↓
Canonical Workspace

لا يستطيع أي مكون تجاوز هذا المسار لإجراء تحديث معرفي معتمد.

Physical Storage

يمكن توزيع البيانات على جداول أو ملفات أو مخازن مختلفة.

لكن يجب أن تحافظ البنية على:

النسخ القانونية.

العلاقات المرجعية.

الذرية المطلوبة.

التاريخ الضروري للتعافي.

سلطة الكتابة المعتمدة.

Source: [RDMS-10-M23-U011](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L291>); source-unit SHA-256 `7b2d20bf74234f6ebc771580b448f748b7fa2002a40522a2842b27976888b38f`.

### L7-B23-009 — 9. Capability Runtime

Source: FCA / RDMS-08

Responsibility

تشغيل القدرات المعرفية.

تشمل:

Intent Modeling
Mental Modeling
Information Foraging
Causal Reasoning
Experiment Design
Engineering Judgment
Adaptive Planning
Code Construction
Verification
Metacognition
Learning Proposals
Capability Contract

كل Capability يجب أن تستقبل مدخلات محددة النطاق وتعيد مقترحات أو نتائج واضحة النوع.

[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]

هذه أغلفة تكامل مقترحة، وليست بديلًا عن الكيانات المجمدة.

Important Rule

CapabilityResult ليست بالضرورة حقيقة معتمدة.

قد تحتوي على:

Hypothesis
PatchProposal
ActionProposal
DecisionProposal
MemoryProposal

تحتاج هذه المقترحات إلى المرور بمسار قبولها القانوني.

Source: [RDMS-10-M23-U012](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L342>); source-unit SHA-256 `31f9c1d70d2c898cf2ec50af580bacbf9f69166956aacc52ad44d0c40d1d8d09`.

### L7-B23-010 — 10. Reasoning Gateway

Source: FCA / RDMS-08

Responsibility

توفير واجهة موحدة لاستدعاء نماذج الاستدلال.

يمكن أن يدعم:

OpenAI models

Anthropic models

Google models

Local models

Future reasoning systems

DGCA LITE

التكامل مع DGCA LITE خيار مستقبلي، وليس اعتمادًا معماريًا إلزاميًا.

Source: [RDMS-10-M23-U014](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L421>); source-unit SHA-256 `c292556fcaf50258fc608ca1975ce07dde9b812acdb64e489d24e2f40334fe09`.

### L7-B23-011 — 11. Provider-Neutral Contract

[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M23-U015](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L445>); source-unit SHA-256 `d8dd3584c914412a54994c0c488cf1e0df6999627d5688247118af6457425ee7`.

### L7-B23-012 — 12. Provider Authority

الـProvider تستطيع:

إنتاج تحليل.

اقتراح تعديل.

اقتراح تجربة.

اقتراح Action.

اقتراح خطة.

اقتراح قرار.

لكن لا تستطيع:

Commit canonical state.

Execute shell commands directly.

Write production files directly.

Recruit Specialists directly.

Promote Memory directly.

Issue legal authorization.

أي استدعاء أداة تطلبه Provider يمر عبر المسار القانوني الملائم.

Source: [RDMS-10-M23-U016](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L488>); source-unit SHA-256 `efdac0a412b93ace6c9953dda36409a280bc3989527bb336d26c399fa09a12bf`.

### L7-B23-013 — 13. Provider Switching

تغيير Provider لا يغير:

Project Identity
Canonical Workspace
Executive Epoch
Action History
Memory
Control Ledger

إذا وصلت نتيجة قديمة بعد تغيير Provider، تُربط بمحاولة الاستدلال الأصلية، وتخضع لفحص الصلاحية قبل اعتمادها.

Source: [RDMS-10-M23-U017](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L520>); source-unit SHA-256 `c4cda273b0d2d41c8220832291661b24388c52a50dab22814cfb2c59945c7fb4`.

### L7-B23-014 — 14. Context Assembly

يجب أن تتكون حزمة السياق من مصادر موثقة.

[Record declaration: consult its sole owner in the contract registry.]
Critical Rule

لا يمكن لمحتوى داخل Repository أو Tool Output أن يرفع درجة سلطته بتضمين تعليمات تبدو رسمية.

مصدر سلطة التعليمات يأتي من الـTrusted Envelope، وليس من النص نفسه.

Source: [RDMS-10-M23-U018](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L533>); source-unit SHA-256 `805627114788dad79e6faf81c47d5b640ada0dfb4871c740cea0382455343f8c`.

### L7-B23-015 — 15. CommitGate

Source: RDMS-01

Responsibility

التحقق من قانونية كل تغيير معرفي معتمد.

Proposed Interface
[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]
Requirements

يجب أن تتحقق البوابة من:

Current Executive Epoch

Legal authorization

Hard invariants

Expected versions

Dependency validity

Required atomicity

Idempotency

لا يستطيع النموذج اللغوي ملء الحقول الموثوقة بطريقة تمنح نفسه سلطة.

يجب إصدار أو التحقق من بيانات السلطة داخل Control Plane الموثوقة.

Source: [RDMS-10-M23-U020](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L569>); source-unit SHA-256 `ba50188e418d8113a78cd869c84faea7c80f0669c5262aebf56745d5ca60998d`.

### L7-B23-016 — 16. Control Ledger

Source: RDMS-01

Responsibility

حفظ التاريخ القانوني الضروري لاستعادة النظام.

يشمل:

Executive Epoch

Canonical commits

Action lifecycle

Trigger lifecycle

Specialist lifecycle

Goal lifecycle

Memory promotion references
Durability Contract

أي انتقال يعتمد التعافي الصحيح على حفظ عدة بيانات معًا يجب أن يحافظ على الذرية المطلوبة.

كما يجب أن تكون إقرارات المتانة متوافقة مع نموذج الأعطال المعلن.

Important Distinction

ControlLedger ليست مجرد نظام Logs.

إنها حد قانوني معتمد.

أما Logging التشخيصي فهو بنية مختلفة لا يجوز استخدامها بديلًا عن الأحداث القانونية.

Source: [RDMS-10-M23-U021](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L630>); source-unit SHA-256 `6b83f9fa60a2fd1445f7710fc3e891eb259e688b52e89e4f371beb24c9b1f878`.

### L7-B23-017 — 17. ActionGate

Source: RDMS-04

Responsibility

التحقق من قانونية العمليات التي قد تؤثر في العالم الخارجي.

Proposed Interface
[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]
Core Rule

الـExecutive تقرر دلاليًا.

لكن ActionGate تتحقق من الالتزامات القانونية.

ولا يسمح للـExecutive بتحويل عملية غير قانونية إلى عملية قانونية بمجرد الموافقة عليها.

Source: [RDMS-10-M23-U022](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L667>); source-unit SHA-256 `b5e2956b175f6eb3342953b4a2897e7e7536b3d6273423e6b56d425c3fad1c4e`.

### L7-B23-018 — 18. Dependency Evaluation Engine

Source: RDMS-06

Responsibility

تقييم صلاحية النتائج وفق الاعتماديات الفعلية.

يستخدمه:

CommitGate

Cognitive Executive

Specialist Integration

Recovery

Memory Applicability

Implementation Readiness

Finalization
Interface
[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]
Important Rule

لا يجوز إنشاء Dependency Engine جديدة داخل RDMS-09 أو RDMS-10.

ولا يكفي تغير Global State Version لإثبات أن نتيجة Specialist أصبحت قديمة.

يجب تقييم ما اعتمدت عليه النتيجة فعلًا.

Source: [RDMS-10-M23-U023](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L714>); source-unit SHA-256 `03d43c28d4f35e4aa3d941cf6a2eb33f28732b97acae10de53e9fb5790d4918f`.

### L7-B23-019 — 19. Action Journal

Source: RDMS-04

Responsibility

حفظ دورة حياة العمليات الخارجية.

يجب المحافظة على:

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

وفق المعاني المجمدة.

Source: [RDMS-10-M23-U025](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L771>); source-unit SHA-256 `e95c666fcc246ddb28e98bb43f34527bfeccc02b5cf03fe11c50d30fd2733469`.

### L7-B23-020 — 20. Durable Dispatch Protocol

ActionProposal
      ↓
Executive Authorization
      ↓
ActionGate
      ↓
Persist AUTHORIZED
      ↓
Persist DISPATCH_INTENT
      ↓
Durable acknowledgement
      ↓
Reality Executor
      ↓
Record reported result
      ↓
Observation Ingress
      ↓
Reconciliation
Fundamental Rule

لا يجوز تنفيذ SHARED_WORLD mutation قبل وجود DISPATCH_INTENT متينة.

Source: [RDMS-10-M23-U026](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L796>); source-unit SHA-256 `1d834cf51d578b74c98954b0ba23498987bacf4386fc850af5e2996fb509b29c`.

### L7-B23-021 — 21. Execution Adapter Interface

[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]

هذه الواجهة لا تسمح للـExecutor بتقرير النجاح النهائي للأثر بناءً على Exit Code وحده.

Source: [RDMS-10-M23-U027](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L820>); source-unit SHA-256 `5f2d013f521d51effc3ebbdddb211a1da513a567112686512475474127a55b9a`.

### L7-B23-022 — 22. Tool Adapter Categories

يمكن توفير Adapters لأنواع أدوات مختلفة:

Filesystem

Git

Shell

Build tools

Test runners

Debugger

Database

Network

Deployment

External APIs

جميعها تخضع لتصنيف الآثار.

Source: [RDMS-10-M23-U028](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L860>); source-unit SHA-256 `5dd29a657de73f54dfe8ba41a042c38960aa7fd560f2367a6cb620c5f324bebc`.

### L7-B23-023 — 23. Actual Effect Classification

يجب الفصل بين:

Cognitive operation intent

و:

Actual tool effects

فعملية اسمها INSPECT قد تستخدم Shell ذات آثار جانبية.

لا يجوز أن يسمح اسم العملية المعرفية بتجاوز ActionGate.

Source: [RDMS-10-M23-U029](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L886>); source-unit SHA-256 `7615cbaa322d4b81a1ce4f53db30b4c967d93b0196d6028a9020b091314b9ee1`.

### L7-B23-024 — 24. Ephemeral Sandbox Path

يمكن استخدام المسار السريع عندما يثبت أن جميع الآثار القابلة للوصول:

معزولة.

مؤقتة.

قابلة للتخلص منها.

لا تصل إلى حالة المشروع المشتركة.

لا تستطيع استخدام صلاحيات إنتاجية مشتركة.

عندما لا يمكن إثبات ذلك، يكون التصنيف الافتراضي SHARED_WORLD.

Source: [RDMS-10-M23-U030](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L900>); source-unit SHA-256 `3f10ee8991f37adebc1a0f520a198b769358fc16cf9235137a024035f2ce8eec`.

### L7-B23-025 — 25. Recovery and Retry

يجب أن تظل:

Action authorized

مختلفة عن:

Action dispatched

ومختلفة عن:

Effect observed

ومختلفة عن:

Effect verified

لا يُسمح بإعادة تنفيذ Action غير محسومة بصورة عمياء.

Source: [RDMS-10-M23-U031](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L916>); source-unit SHA-256 `cac522d84a3b13f213d81330df0e070d90f91e2657ee9bce367b978346582bc6`.

### L7-B23-026 — 26. Observation Ingress

Source: RDMS-03

Responsibility

استقبال الملاحظات الواقعية وتسجيلها وفق provenance والهوية والسلامة.

Proposed Interface
[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M23-U033](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L937>); source-unit SHA-256 `cd319307423b4eb48c53deb6f194c24046b7df6ba007211b659d514741ae4820`.

### L7-B23-027 — 27. Observation Authority

لا تحتاج Observation الخام إلى موافقة دلالية من Executive لمجرد تسجيلها.

لكن يجب التحقق من المصدر والشكل والهوية والسلامة وفق RDMS-03.

Source: [RDMS-10-M23-U034](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L972>); source-unit SHA-256 `0ee69e3653187084a1b6dd18e723572720fb1e02161a37336ac8635161be81de`.

### L7-B23-028 — 28. Observation vs Interpretation

نميز بين:

Observation:
    Test returned exit code 1.

و:

Hypothesis:
    A database race condition caused the failure.

الثانية لا تصبح Fact لمجرد أن النموذج استنتجها.

Source: [RDMS-10-M23-U035](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L978>); source-unit SHA-256 `77c62d2bca7dd3bd5a13072d6984d9bc1fbb6a357defaf9422c793904ff661e1`.

### L7-B23-029 — 29. Evidence Integration

Observation
      ↓
Evidence Interpretation Proposal
      ↓
Executive Review
      ↓
CommitGate
      ↓
Canonical Epistemic State

يجب أن تستخدم الادعاءات السببية بوابة Causal Closure المجمدة عندما تكون شروطها منطبقة.

Source: [RDMS-10-M23-U036](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L992>); source-unit SHA-256 `32a7b20b7129e4cb4de9f39dcddcc27994582484b376b00e3aa4aa5c2fbba3ca`.

### L7-B23-030 — 30. Specialist Manager

Source: RDMS-06

Responsibility

إدارة دورة حياة المتخصصين المؤقتين.

يشمل:

Recruitment

Contract assignment

Workspace isolation

Budget allocation

Execution tracking

Result delivery

Freshness evaluation

Integration

Source: [RDMS-10-M23-U038](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1006>); source-unit SHA-256 `467ecf20107268f97cd471438bad9033c7b413b08de3241d4d96cb400899f5b6`.

### L7-B23-031 — 31. Specialist Recruitment Interface

[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M23-U039](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1031>); source-unit SHA-256 `85d329ddb704ec2748217209f11f0c9ea3fe5f6f6db5c3a4cb8392c5727c05f6`.

### L7-B23-032 — 32. Specialist Authority

لا تمتلك Specialist سلطة تعديل Canonical Workspace.

يمكنها:

إجراء تحليل.

توليد كود مرشح.

تنفيذ تجارب مصرح بها.

إعداد مراجعة.

إنتاج Findings.

اقتراح تعديلات.

لكن التكامل النهائي يخضع لسلطة Executive والبوابات القانونية.

Source: [RDMS-10-M23-U040](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1060>); source-unit SHA-256 `28fd9f6c2e894c0969bb5a6ed7394e59636962c0faf42bfacda856a89c2e0e47`.

### L7-B23-033 — 33. Specialist Workspace

يجب أن تحتوي كل Specialist على نطاق عمل معزول وفق عقدها.

يمكن أن يعمل عدة متخصصين بالتوازي:

Specialist A:
    API analysis

Specialist B:
    Security review

Specialist C:
    Test design

لكن ذلك لا يمنحهم سلطة دمج نتائجهم مباشرة.

Source: [RDMS-10-M23-U041](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1080>); source-unit SHA-256 `eb3985d5d774d5a09ae090a073bc3e9deb1e25d153a88987fea6dc27f932fa25`.

### L7-B23-034 — 34. Specialist Integration

Specialist Result
       ↓
Provenance Validation
       ↓
Dependency Evaluation
       ↓
Conflict Detection
       ↓
Verification
       ↓
Executive Integration Decision
       ↓
CommitGate / ActionGate as applicable
Critical Requirement

يجب تقييم النتائج وفق اعتمادياتها الفعلية.

وقد تظل بعض Findings صالحة حتى عندما تتغير أجزاء أخرى من المشروع.

Source: [RDMS-10-M23-U042](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1097>); source-unit SHA-256 `d40e55c92eea35b2ed2e83138cb56f83ad41aa3f1519197438eff63a43ae08e2`.

### L7-B23-035 — 35. No Implicit Majority Authority

إذا اتفقت ثلاث Specialists على تفسير واحد، فهذا لا يحوله تلقائيًا إلى حقيقة.

قد تكون جميعها اعتمدت على الفرضية الخاطئة نفسها.

يجب الحفاظ على متطلبات الأدلة والتحقق المناسبة.

Source: [RDMS-10-M23-U043](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1117>); source-unit SHA-256 `9a341e89705de7786abb82f61ab36e8f55d3987ac96ee691e4ee94b73be9f6a5`.

### L7-B23-036 — 36. Memory Services

Source: RDMS-07

Responsibility

تخزين واسترجاع المعرفة والخبرة المعتمدة، مع الحفاظ على provenance وقيود الاستعمال.

Source: [RDMS-10-M23-U045](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1126>); source-unit SHA-256 `c298e7abacffe08f8c69fab71c1f4215800a377b0f7a3a4351be557033cb6af8`.

### L7-B23-037 — 37. Memory Retrieval

[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M23-U046](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1134>); source-unit SHA-256 `1a657d69c455d9f9d7261ae137196bfdf88d6121d71c85fede97fddc480924df`.

### L7-B23-038 — 38. Retrieved Memory Is Not Current Truth

يجب التمييز بين:

Historical precedent

و:

Current project evidence

قد تكون تجربة سابقة صحيحة في مشروع آخر، لكنها غير صالحة للمشروع الحالي.

Source: [RDMS-10-M23-U047](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1159>); source-unit SHA-256 `477a80bdf109f816b9d906eb9960a749286c3682ee30271a92389e498a5bdc92`.

### L7-B23-039 — 39. Memory Promotion

Episode
      ↓
Reflection
      ↓
MemoryProposal
      ↓
LearningGate
      ↓
Executive Authorization
      ↓
Memory Promotion Commit

لا تُرقّى المعرفة تلقائيًا لمجرد أن تجربة نجحت مرة واحدة.

Source: [RDMS-10-M23-U048](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1171>); source-unit SHA-256 `45b8ec34125d1ae06e2c173fa5fecb305cf62eb425d9f58dbe13279b32c2e10f`.

### L7-B23-040 — 40. Derived Memory Indexes

يمكن أن تستخدم الذاكرة فهارس أو Cache أو وسائل استرجاع متعددة.

لكن هذه الهياكل المشتقة لا تصبح مصدر الحقيقة المعتمد.

ويمكن إعادة بنائها من البيانات القانونية المتاحة وفق صلاحياتها.

Source: [RDMS-10-M23-U049](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1186>); source-unit SHA-256 `8ab05783e8a3dfc4ded764d024f66bf0cf05b79d87fbb7500de14d97f2162645`.

### L7-B23-041 — 41. Durable Temporal Scheduler

Source: RDMS-05

Responsibility

إدارة الالتزامات الزمنية والتفعيل عند توفر شروط مستقبلية.

يشمل:

Waiting

Suspension

Resumption

Time-based triggers

External event triggers

Dependency reactivation

Source: [RDMS-10-M23-U051](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1195>); source-unit SHA-256 `13e3ea855ebc4a82f6e2187b97d2779b461575c3176d6862ef9ef2b5c328fd31`.

### L7-B23-042 — 42. Trigger Interface

[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M23-U052](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1216>); source-unit SHA-256 `5fb94d6ec9077ff10ba549a031e4bb41835306a3287042ed51654b6045cf2574`.

### L7-B23-043 — 43. Trigger Authority

يمكن اكتشاف الحدث عدة مرات.

لكن يجب أن تكون Reaction القانونية قابلة لإزالة التكرار وفق RDMS-05.

كما يجب ألا تؤدي إعادة تشغيل Trigger إلى إعادة تنفيذ Mutation خارجية بصورة غير قانونية.

Source: [RDMS-10-M23-U053](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1239>); source-unit SHA-256 `0ee6efcd255a7791bbb3d955a3a146ac9c24a5826cd684f54caf53ef6b154763`.

### L7-B23-044 — 44. Suspended Tasks

كل مهمة معلقة تحتاج إلى حالة قابلة للاستعادة.

يجب أن يعرف النظام:

Why suspended?

What was active?

What remains unresolved?

What changed?

What event may reactivate it?

What must be revalidated?

لا يجوز الاعتماد على ذاكرة محادثة LLM لاستئناف المهمة.

Source: [RDMS-10-M23-U054](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1247>); source-unit SHA-256 `0df2b1c1a75caec7c0e5f83d309eb7b2787e7aff32d4a41b0d5159bfd78804f5`.

### L7-B23-045 — 45. Recovery Coordinator

Source: RDMS-09

Responsibility

تنسيق استعادة النظام عبر المكونات.

لا تملك سلطة معرفية مستقلة.

Source: [RDMS-10-M23-U056](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1268>); source-unit SHA-256 `8e2be1a286df198817d08c959a8a49c1f74d71b678568157a708fe294a36f77f`.

### L7-B23-046 — 46. Recovery Assessment Interface

[Record declaration: consult its sole owner in the contract registry.]
[Record declaration: consult its sole owner in the contract registry.]

Source: [RDMS-10-M23-U057](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1278>); source-unit SHA-256 `4c3749934d0eeeca7a6b76521ffc64537629dad5b48aeb40a70d6e5e04d4d81c`.

### L7-B23-047 — 47. Canonical Startup Order

يحافظ التكامل على تسلسل FCA:

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

Source: [RDMS-10-M23-U058](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1309>); source-unit SHA-256 `dd4de704f9e33786040d6963eb38e88a92e3dd99675a1dfd3ba49822e36d69d0`.

### L7-B23-048 — 48. Operational Dependency

قد تحتاج بعض خطوات التعافي إلى إجراءات تحضيرية لا تمتلك السلطة المعرفية أصلًا.

في هذه الحالة تطبق RDMS-09 بروتوكول Recovery Bootstrap الذي يميز بين استعادة البنية التحتية واستئناف الوكيل.

ولا يجوز أن يصبح Bootstrap مسارًا بديلًا لتنفيذ قرارات المشروع.

Source: [RDMS-10-M23-U059](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1332>); source-unit SHA-256 `a2bdbf1288ad03830e00dea752eb1d1b41a5bbe5b5dea50e6cd7d8140a95d358`.

### L7-B23-049 — 49. Recovery Admission

يمكن استئناف العمليات ضمن نطاق ثبتت سلامته.

مثال:

Read-only analysis:
    ALLOWED

Shared-world mutation:
    BLOCKED

Unresolved deployment:
    IN_DOUBT

Independent documentation task:
    MAY CONTINUE

لا نفرض توقفًا عالميًا عندما يمكن إثبات استقلال بعض العمليات.

Source: [RDMS-10-M23-U060](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1340>); source-unit SHA-256 `c6674159869d52b85a8a8ad92ce4468ef638de0418fc4229de66dc5b93371bb9`.

### L7-B23-050 — 50. Trust Classification

يجب أن تحتفظ الرسائل والمحتويات بمعلومات السلطة والمصدر.

نميز بين:

Trusted control metadata

User-authorized requirements

Repository content

Tool output

Provider-generated content

Specialist output

External content

Memory retrieval

Source: [RDMS-10-M23-U062](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1361>); source-unit SHA-256 `087f587c30819bdd385770968ca0a7491607ef3dfeaa47ad46131b0d66a2da24`.

### L7-B23-051 — 51. Trusted Envelope

[Record declaration: consult its sole owner in the contract registry.]
Mandatory Rule

لا يجوز أن يحدد payload غير موثوق صلاحيات envelope الخاصة به.

يجب التمييز بين ما يرسله Provider وبين البيانات التي تصدرها أو تتحقق منها Control Plane.

Source: [RDMS-10-M23-U063](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1382>); source-unit SHA-256 `cfd1fcf1c4dd783851593c7b85f52f0172cd5a372dc839c9307fed1dc2913f2d`.

### L7-B23-052 — 52. Trust Boundary Matrix

Source	Direct canonical write	Direct external mutation
Cognitive Executive	No — CommitGate required	No — ActionGate required
LLM Provider	No	No
Cognitive Capability	No	No
Specialist	No	Only through authorized action path
Tool Adapter	No	Only within authorized execution scope
Recovery Coordinator	No	No independent agent-world authority
Observation Ingress	Append accepted observations only	No
CommitGate	Legal canonical writes	No
ActionGate/authorized executor path	No direct cognitive mutation	Governed dispatch

Source: [RDMS-10-M23-U064](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1414>); source-unit SHA-256 `8a8491287a7a9a64cdff3f48745a70ac01226a9ba96f3313e9409cd9fab01b28`.

### L7-B23-053 — 53. Credentials

لا يجوز إعطاء Provider أو Specialist صلاحيات أوسع من نطاق المهمة.

كما لا يجوز أن يكتسب كود المشروع غير الموثوق صلاحية الوصول إلى Credentials مشتركة لمجرد تشغيله داخل Test Runner.

Source: [RDMS-10-M23-U065](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1425>); source-unit SHA-256 `a1a7838f98498e31308382eed2822000279b2c15f175e9517f459c1c2377160d`.

### L7-B23-055 — 55. One Owner, Multiple Readers

يمكن لمكونات عديدة قراءة الحالة نفسها.

لكن لا يجوز أن يؤدي ذلك إلى إنشاء سلطات كتابة متعددة.

مثال:

Executive reads Decision.

Planner reads Decision.

Verifier reads Decision.

Specialist reads Decision.

Only legal canonical path changes Decision.

Source: [RDMS-10-M23-U068](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1455>); source-unit SHA-256 `c1492cc951cebecbc46e29a341711a3a002ddad27e7b1980686f24231e2f965a`.

### L7-B23-056 — 56. Derived Data

تعتبر الفهارس وSnapshots العرضية وCaches بنى مشتقة عندما لا تكون مصدر الحقيقة القانوني.

يجب أن تحتوي على معلومات تسمح بمعرفة:

Source version

Dependency frontier

Schema version

Validity status

ولا يجوز استخدامها لإثبات حقيقة أوسع من نطاق مصادرها.

Source: [RDMS-10-M23-U069](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1472>); source-unit SHA-256 `dd496ac6f611b543cf51326a38bb6e427eff8a430edce1254d8c1d97cae13178`.

### L7-B23-057 — 57. Interface Design Rule

كل واجهة بين مكونين يجب أن تحدد:

Input contract

Output contract

Authority requirement

Side-effect classification

Idempotency requirement

Version requirement

Failure semantics

Recovery semantics

لا يكفي تعريف Function Signature دون تحديد آثارها القانونية.

Source: [RDMS-10-M23-U071](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1489>); source-unit SHA-256 `f8332c8617d9ae9d9f2e5461cde77d7f605cc9938f127bebaf8a1d3aa886ccb4`.

### L7-B23-058 — 58. Request Identity

كل عملية مؤثرة تحتاج إلى هوية مستقرة وفق مجالها.

نميز بين:

Request ID

Invocation ID

Control Event ID

Action ID

Action Attempt ID

Trigger Reaction Key

Specialist Run ID

Recovery Case ID

لا يجوز دمج هذه المعرفات في حقل واحد لمجرد أنها جميعًا UUIDs.

لكل منها معنى مختلف.

Source: [RDMS-10-M23-U072](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1511>); source-unit SHA-256 `b96c837dc0cf4da0c168be61b6097d5874ad44fb956f9ab41ee2eae3eb5393b8`.

### L7-B23-059 — 59. Idempotency Scope

يجب تحديد المجال الذي يمنع التكرار.

مثال:

Canonical control commit:
    Idempotent under commit key.

External payment:
    Only idempotent if external
    domain guarantees it.

عدم تكرار ControlCommit لا يثبت عدم تكرار الأثر الخارجي.

Source: [RDMS-10-M23-U073](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1537>); source-unit SHA-256 `ec58126b374eb31e4536873ceebdf831ba693993f468fdb358c955d9a80d7ad5`.

### L7-B23-060 — 60. Versioning

ينبغي أن تحتوي الرسائل المعتمدة على Schema Version واضحة.

ويجب أن تعرف المكونات كيفية التعامل مع:

Compatible version

Incompatible version

Unknown version

لا يسمح بتفسير Payload غير متوافقة بصورة صامتة.

Source: [RDMS-10-M23-U074](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1552>); source-unit SHA-256 `3c962f4ece0565c6037d79dd7597fe7b5529081b9965be5d2d91660c547c114a`.

### L7-B23-061 — 61. Error Semantics

نقترح تصنيفًا موحدًا لأخطاء الواجهات:

VALIDATION_REJECTED

AUTHORITY_REJECTED

STALE_DEPENDENCY

CONFLICT

TEMPORARILY_UNAVAILABLE

UNSUPPORTED_OPERATION

UNKNOWN_OUTCOME

هذه نتائج واجهات تكامل، وليست حالات جديدة للكيانات القانونية.

لا يجوز أن يحول Adapter خطأ UNKNOWN_OUTCOME إلى FAILED من تلقاء نفسه.

Source: [RDMS-10-M23-U075](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1566>); source-unit SHA-256 `f91abe62406976a0d6bb5b2e09edca568d89b834b77d76e971debdb370bf0d78`.

### L7-B23-062 — 62. Timeouts

ينبغي الفصل بين:

Request timeout

Process termination

Execution failure

World-effect failure

انتهاء مهلة الاستدعاء لا يثبت أن العملية الخارجية لم تحدث.

Source: [RDMS-10-M23-U076](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1588>); source-unit SHA-256 `8d6dee824b807ad98e2eec9de8dede3d16bcb34bb5a8893e1e19e13750964f6e`.

### L7-B23-063 — 63. Physical Deployment Philosophy

أقترح في النسخة الأولى:

Modular Monolith for the trusted cognitive/control core, with isolated execution domains.

أي:

نواة معيارية واحدة تضم المكونات التي تحتاج إلى تفاعل قانوني متقارب، مع عزل العمليات الخطرة والمتخصصين.

هذا اقتراح هندسي أولي، وليس شرطًا مفروضًا من FCA.

Source: [RDMS-10-M23-U078](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1603>); source-unit SHA-256 `6117aa6e0d61cbe4e6edd3fbf4e7ae0294cefe18dd5907e423158171054b7bbf`.

### L7-B23-064 — 64. Proposed Runtime Processes

┌───────────────────────────────────────────┐
│            AGENT HOST RUNTIME             │
│                                           │
│  Cognitive Executive                      │
│  Canonical Workspace Access               │
│  Capability Orchestrator                   │
│  CommitGate                                │
│  ActionGate                                │
│  Dependency Evaluation                    │
│  Specialist Manager                       │
│                                           │
└─────────────────────┬─────────────────────┘
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
   Provider       Action       Specialist
   Workers        Workers       Workers
         │            │            │
         └────────────┼────────────┘
                      ▼
                Controlled IO

يمكن تشغيل المكونات الموثوقة في عملية واحدة مبدئيًا إذا كانت متطلبات العزل والذرية والأمان تسمح بذلك.

أما تنفيذ أدوات المشروع غير الموثوقة فيجب أن يحترم حدود العزل المطلوبة.

Source: [RDMS-10-M23-U079](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1615>); source-unit SHA-256 `6b24a5c3f92feeb1fd4e1cb185dad7920d624328bcc9ae8e7d0687d579f5e7d1`.

### L7-B23-065 — 65. Why Not Microservices Everywhere?

لا يوجد سبب معماري يجبرنا على فصل كل قدرة معرفية في خدمة مستقلة.

مثلًا، تحويل:

Intent Modeling
Planning
Verification
Metacognition

إلى خدمات شبكة منفصلة قد يزيد التعقيد والتكلفة دون توفير فائدة متناسبة.

يجب أن يعتمد الفصل على:

Isolation requirement

Failure domain

Scaling requirement

Security boundary

Resource usage

Concurrency requirement

وليس على عدد المفاهيم الموجودة في الوثائق.

Source: [RDMS-10-M23-U080](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1642>); source-unit SHA-256 `27edda94d32cad808566130460bc75c7c24c3d8b33efc287eab47d65294259c0`.

### L7-B23-066 — 66. Process Isolation

المكونات التي تشغل كودًا غير موثوق تحتاج إلى حدود مناسبة.

يمكن أن تشمل:

Restricted filesystem

Restricted network

Controlled credentials

Execution budgets

Resource limits

Explicit mounts

Process termination controls

لكن اختيار التقنية الفعلية للعزل يتم أثناء Implementation Boundary Design.

Source: [RDMS-10-M23-U081](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1671>); source-unit SHA-256 `83062fb3c87b1ba77da2b4ad9a3b648672a5acb1d5ed0aefbfdadce59aab38e5`.

### L7-B23-068 — 68. Low-Gravity Task

مثال:

تعديل صياغة بسيطة داخل ملف توثيق.

قد تستخدم Executive مسارًا مختصرًا:

Understand
    ↓
Inspect relevant scope
    ↓
Determine small change
    ↓
Authorize edit
    ↓
Apply change
    ↓
Verify
    ↓
Finalize

لا يلزم إنشاء عدة Specialists أو إجراء محاكاة ذهنية عميقة لمهمة بسيطة.

لكن يجب أن تحافظ العمليات المنفذة على جميع القوانين الإلزامية.

Source: [RDMS-10-M23-U085](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1755>); source-unit SHA-256 `895155534c70feff263aa45e28ac44634f70c35577bb6407522c06f56c262c6c`.

### L7-B23-069 — 69. Fast Path Is Not a Safety Bypass

يمكن اختصار التفكير الاختياري.

لكن لا يمكن اختصار:

Authority checks

Required write gates

Mandatory invariants

Required action journaling

Applicable verification obligations

Source: [RDMS-10-M23-U086](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1781>); source-unit SHA-256 `afaabb2b32ac8d29dd642bca9104e951f6d71def14cf888d80d948defe55c1eb`.

### L7-B23-070 — 70. Architectural Change

مثال:

تغيير نظام Authentication في مشروع كبير.

قد تتطلب العملية:

Goal Modeling
        ↓
System Mental Model
        ↓
Risk Analysis
        ↓
Information Acquisition
        ↓
Competing Alternatives
        ↓
Causal and Future Simulation
        ↓
Independent Security Review
        ↓
Decision
        ↓
Risk-First Planning
        ↓
Incremental Implementation
        ↓
Verification
        ↓
Integration Review
        ↓
Finalization

Source: [RDMS-10-M23-U088](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1797>); source-unit SHA-256 `2e098ee3f1b8e726cdb85a82d4a13b2cbdd7f4c21d69ea8942bd7fa6f6265bf3`.

### L7-B23-071 — 71. Adaptive Depth

لا تحدد درجة الخطورة عدد استدعاءات LLM بصورة آلية فقط.

بل تحدد نوع الالتزامات المعرفية والتحقق المطلوبة.

يمكن لنظام قوي أن يصل إلى قرار جيد بعد عدد قليل من العمليات إذا كانت الأدلة كافية.

ولا يجوز أن تستمر Executive في التفكير بلا تقدم لمجرد أن المهمة HIGH.

Source: [RDMS-10-M23-U089](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1830>); source-unit SHA-256 `b38c6259e71c7dca13556c07b6e16bdc34a7b29d50b7217cdac6c18948396af7`.

### L7-B23-072 — 72. Parallel Cognitive Work

يمكن تنفيذ أعمال مستقلة بالتوازي عندما تكون الفائدة واضحة.

مثلًا:

Goal: Improve authentication module

Specialist A:
    Study existing architecture.

Specialist B:
    Security analysis.

Specialist C:
    Test coverage analysis.

Source: [RDMS-10-M23-U091](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1841>); source-unit SHA-256 `44f220369863f70591ad4a749e209a6f72eb3276115ef40ac71023d4610e2a64`.

### L7-B23-073 — 73. Parallel Results Are Proposals

كل Specialist تعيد نتيجة مستقلة.

لا تُدمج النتائج في Canonical Workspace بصورة تلقائية.

Source: [RDMS-10-M23-U092](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1857>); source-unit SHA-256 `1327be15aa4676fdf3fce2c52ad87ddc571962b0a4b564cba0942200fc1c53e2`.

### L7-B23-074 — 74. Integration Concurrency

قد تحاول نتيجتان تعديل الكيان نفسه.

يجب أن يمر قبول كل تعديل عبر شروط النسخ والاعتماديات والسلطة.

إذا أصبح مقترح قديمًا، يجب إعادة تقييمه.

لا يجوز فرض آخر نتيجة وصلت باعتبارها الصحيحة.

Source: [RDMS-10-M23-U093](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1863>); source-unit SHA-256 `52da9afa449ace64ea37de395c41403b0015f8b003c412c0309ff1ea29984dbc`.

### L7-B23-075 — 75. World Actions

يمكن تنفيذ Actions مستقلة بالتوازي إذا كان نطاقها والتفويضات والاعتماديات تسمح بذلك.

لكن يجب ألا يؤدي التوازي إلى:

Conflicting filesystem mutations

Conflicting Git operations

Uncontrolled database migrations

Duplicate external transactions

Unsafe shared workspace writes

عندما تكون العلاقات غير محسومة، يجب استخدام تحليل محافظ أو عزل مناسب.

Source: [RDMS-10-M23-U094](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1873>); source-unit SHA-256 `e7d227e8df6a93a15adcd3b4f28947c2ccef3f6cc7ac3f0240ade9eea85d6b82`.

### L7-B23-076 — 76. Logical Storage Domains

نقترح تقسيمًا منطقيًا:

CONTROL DATA

CANONICAL COGNITIVE STATE

ACTION JOURNAL

OBSERVATIONS

ARTIFACTS

MEMORY

DERIVED INDEXES

DIAGNOSTIC LOGS

لا يعني ذلك ثماني قواعد بيانات.

Source: [RDMS-10-M23-U096](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1892>); source-unit SHA-256 `247fc3a595088dc2bce9c0ab8e792fc5a2e78e572bdc0fe489b71c08a7fb06a3`.

### L7-B23-077 — 77. Storage Ownership

يجب أن يحدد كل نطاق:

Authoritative owner

Write path

Versioning rules

Durability requirements

Backup requirements

Recovery rules

Retention policy

Source: [RDMS-10-M23-U097](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1914>); source-unit SHA-256 `3747498fc3fa7db90f6830b6e17b2cbe6de213d1960baf71b0ce664d5852fc9b`.

### L7-B23-078 — 78. Atomicity Boundaries

قد يحتاج النظام إلى اعتماد:

Decision Accepted
+
Trigger Armed
+
State Version Advanced

بصورة ذرية.

لكن لا يجوز افتراض معاملة ذرية واحدة تشمل:

Control Ledger
+
GitHub
+
External Database
+
Deployment Service

تظل الآثار الخارجية خاضعة إلى Action Journal وReconciliation.

Source: [RDMS-10-M23-U098](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1931>); source-unit SHA-256 `3f2ebf316c6c76bb31a0379d66dea50d30838cecb83ad5a92782b295f8480347`.

### L7-B23-079 — 79. Large Artifacts

يمكن تخزين ملفات كبيرة مثل:

Repository snapshots

Test outputs

Build artifacts

Logs

Specialist workspaces

خارج مخزن التحكم الأساسي.

لكن يجب أن تبقى المراجع الضرورية للتعافي متينة وقابلة للتحقق ضمن العقد المعتمد.

Source: [RDMS-10-M23-U099](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1955>); source-unit SHA-256 `012c4e5a7409fe04c0a7caa84acbb0e7b5c8998a27d20d908117567006bae92f`.

### L7-B23-080 — 80. Index Rebuild

يمكن إعادة بناء الفهارس المشتقة.

لكن لا يجوز اعتبار فهرس غير مكتمل مصدرًا صالحًا لإثبات غياب اعتماديات أو نتائج.

Source: [RDMS-10-M23-U100](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1973>); source-unit SHA-256 `8f665fed19e09022c0a9bff299e5c3cc803149ad349cd7fb29b52a0b33334aed`.

### L7-B23-081 — 81. Legal Effect Matrix

Operation	Required authority	Legal boundary
Change Goal	Executive	CommitGate
Accept Decision	Executive	CommitGate
Update Mental Model	Executive	CommitGate
Record Observation	Valid source / ingress	Observation Ingress
Add EvidenceLink	Executive	CommitGate
Create external mutation	Executive	ActionGate + Journal
Execute sandbox activity	Authorized sandbox scope	Sandbox/Action policy
Recruit Specialist	Executive	Specialist lifecycle
Integrate Specialist result	Executive	Dependency/verification + CommitGate
Create Trigger commitment	Applicable control authority	RDMS-05 + Control Ledger
Promote Memory	Executive + LearningGate	Governed memory commit
Enter recovery restriction	Trusted operational policy	RDMS-09 controls; no shadow authority
Resume affected work	Current Executive	Recovery/dependency checks + legal gates
Finalize Goal	Executive	Completion assessment + canonical transition

Source: [RDMS-10-M23-U102](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1980>); source-unit SHA-256 `a95d6549b845cd776a3aed7d85a638977330de11c56928e3fc3754e4c8d1eaf0`.

### L7-B23-082 — 82. Cross-Store Consistency

إذا أشار Control Ledger إلى Artifact ضرورية، يجب أن توجد قواعد تحدد:

When the artifact becomes durable.

When the reference may be committed.

How missing artifacts are detected.

How recovery handles inconsistent references.

لا يجوز اعتماد مرجع حرج إلى Artifact مؤقتة قد تختفي قبل أن تصبح قابلة للاستعادة.

Source: [RDMS-10-M23-U103](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1996>); source-unit SHA-256 `657aa37b80dce869313add7ca43c1af3450a4a9e7bedcbdc1eb0d7aed9a36ebb`.

### L7-B23-083 — 83. Dispatch Atomicity

لا يسمح لـReality Executor بإرسال mutation مشتركة قبل إثبات الحد المتين المطلوب.

ولا يجوز تحويل مجرد وضع رسالة داخل Queue إلى إثبات حدوث الأثر الخارجي.

Source: [RDMS-10-M23-U104](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2010>); source-unit SHA-256 `0bdd4d659332695fe9975fb5d7bd4348e8f8f9d558fb16eb67ec995d3252ef97`.

### L7-B23-084 — 84. Failure Domains

يجب أن تدعم المعمارية التعامل مع:

Executive crash

Worker crash

Provider outage

Tool timeout

Storage outage

Network partition

Specialist failure

Partial world mutation

Schema migration failure

Recovery failure

Source: [RDMS-10-M23-U106](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2017>); source-unit SHA-256 `be8d194ea6df0a170a1d6c9b8050e08ddf6275783c32a89b9732e9b6ffd6b619`.

### L7-B23-085 — 85. Recovery Source of Truth

الاستعادة تعتمد على:

Canonical snapshots

Control Ledger

Action Journal

Trusted artifact manifests

Applicable authority frontiers

Observation provenance

Durable temporal commitments

لا تعتمد على المحادثة السابقة مع LLM بوصفها سجلًا قانونيًا.

Source: [RDMS-10-M23-U107](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2040>); source-unit SHA-256 `18e6d91ef534f9c7f28d7d448e8a6cd889a9d97ec255cb14938b5874548f3b32`.

### L7-B23-086 — 86. Unknown External Effects

إذا كانت نتيجة Action الخارجية مجهولة:

Action → IN_DOUBT

وفق RDMS-04.

لا يجوز أن تختفي هذه الحالة بسبب Restart أو Provider Switch.

Source: [RDMS-10-M23-U108](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2060>); source-unit SHA-256 `43ff9e0179e5cb85ab30bd26de596d5579b942df968f6d3e8d55787740780c95`.

### L7-B23-087 — 87. Repeated Failures

إذا تعطل Recovery Coordinator نفسها، يجب ألا يؤدي ذلك إلى إنشاء سلطة تنفيذ جديدة أو فقدان الالتزامات المعتمدة.

تستخدم RDMS-09 بروتوكولات الملكية والأجيال والاستعادة المناسبة.

Source: [RDMS-10-M23-U109](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2070>); source-unit SHA-256 `8474325eda75709b66dcc11bddde5966322b3b1600aa6a0ea1953e7a80183378`.

### L7-B23-088 — 88. Runtime Telemetry

نحتاج أن نستطيع رؤية:

Current Goal

Current Executive State

Selected Cognitive Operation

Current Executive Epoch

Active Specialists

Pending Actions

IN_DOUBT Actions

Pending Triggers

Verification Status

Recovery Status

لكن هذه المؤشرات ليست مصدر الحقيقة القانوني.

Source: [RDMS-10-M23-U111](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2077>); source-unit SHA-256 `590ace9393b833956f5e1a7c2a9edcf7d99178d086de463be0387c8122706417`.

### L7-B23-089 — 89. Audit vs Diagnostics

يجب التمييز بين:

Audit Records

البيانات التي نحتاجها لإثبات قرارات أو انتقالات قانونية.

Diagnostic Logs

البيانات التي تساعد المطور على فهم الأداء والأخطاء.

يمكن حذف أو تدوير بعض Logs التشخيصية وفق السياسة.

أما البيانات القانونية الضرورية للتعافي فتخضع لضماناتها الخاصة.

Source: [RDMS-10-M23-U112](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2103>); source-unit SHA-256 `1a4f48426ec5c94d8626beb5cbe3d607d135877e627597864b6035b5bb1b295c`.

### L7-B23-090 — 90. Progress Metrics

لا يجوز اعتبار:

Number of files modified

Number of tool calls

Number of LLM responses

دليلًا مستقلًا على نجاح المهمة.

يجب قياس التقدم المعرفي والهندسي باستخدام أدلة مناسبة.

Source: [RDMS-10-M23-U113](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2119>); source-unit SHA-256 `9c0368c9613159b8cd53cd3be84f54db98e29276eb543d32bd42968462f39b4c`.

### L7-B23-091 — 91. Package Philosophy

نقترح أن تتبع البنية البرمجية ملكية المسؤوليات بدل تقسيمها حسب أسماء RFCs.

يمكن استخدام توزيع مبدئي على النحو التالي:

agent/
    interface/
    runtime/
    cognitive/
    control/
    workspace/
    epistemics/
    planning/
    capabilities/
    reasoning/
    actions/
    observations/
    specialists/
    dependencies/
    memory/
    temporal/
    recovery/
    security/
    storage/
    diagnostics/

هذا تصور تنظيمي أولي، وليس شجرة ملفات مجمدة أو كودًا جاهزًا.

Source: [RDMS-10-M23-U115](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2134>); source-unit SHA-256 `d9304b1db93e8fe7842180baca4d86dd28237194c0100f1994a8832792d5e9c2`.

### L7-B23-092 — 92. Avoid Circular Dependencies

لا ينبغي أن يؤدي التنظيم إلى:

Executive imports Action Runtime

Action Runtime imports Executive internals

Memory imports Planner

Planner imports Memory internals

بصورة تجعل كل المكونات تعتمد بعضها على بعض.

يجب استخدام واجهات واضحة عند حدود المسؤوليات.

Source: [RDMS-10-M23-U116](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2163>); source-unit SHA-256 `aa6e2150e309be739f3af31e884cf266fd7e9ac30a62f7f59627ba56fc8b6bf8`.

### L7-B23-093 — 93. Dependency Direction

المبدأ المقترح:

Domain Contracts
       ↑
Domain Components
       ↑
Application Integration
       ↑
Runtime Composition

أي أن الاعتماد البرمجي على العقود المشتركة يجب ألا يفرض اعتمادًا دائريًا بين الخدمات المالكة للحالة.

يمكن للمكونات الأعلى تنسيق استعمال واجهات المكونات الأدنى، لكن لا يجوز تحويل Coordinator إلى مالك جديد للحالة.

Source: [RDMS-10-M23-U117](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2179>); source-unit SHA-256 `2c4cac3acf3a219ce124f7988e7e3237193e446dee8db4011dcf174503355594`.

### L7-B23-094 — 94. No Framework-Driven Architecture

لا ينبغي أن يحدد اختيار Framework أو لغة برمجة نموذج السلطة.

يمكن أن نبدأ بـPython أو غيرها.

لكن يجب أن تظل العقود صحيحة حتى لو تغيرت لغة التنفيذ أو طريقة نشر المكونات.

Source: [RDMS-10-M23-U118](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2195>); source-unit SHA-256 `8dafb56a73b65d5119211d32e17e1b1bf5ef83ad970fb34afb675136c1d3a059`.

### L7-B23-095 — 95. Implementation Strategy

أقترح تقسيم التنفيذ إلى سبع مراحل تكاملية، تبدأ بالحد الأدنى الذي نستطيع اختبار قوانينه.

Phase I — Trusted Control Foundation

تشمل:

Identity
Control Ledger
Executive Epoch
CommitGate
Canonical Workspace
Typed legal contracts

الهدف:

إثبات أن الحالة القانونية لا يمكن تغييرها عبر مسار غير مصرح.

Phase II — Observation and Action Foundation

تشمل:

ActionGate
Action Journal
Reality Executor
Observation Ingress
Effect Classification
Reconciliation

الهدف:

إثبات أن الأفعال الخارجية تظل قابلة للتدقيق والتسوية، حتى بعد الأعطال.

Phase III — Cognitive Kernel

تشمل:

Cognitive Executive
Capability Runtime
Reasoning Gateway
Context Assembly
Adaptive Cognitive Control

الهدف:

بناء دورة معرفية تعمل فوق حدود التحكم الموجودة، لا أن تتجاوزها.

Phase IV — Engineering Cognition

تشمل:

System Mental Modeling
Information Acquisition
Causal Reasoning
Planning
Code Construction
Verification
Metacognition

الهدف:

تمكين الوكيل من معالجة مهمة برمجية كاملة ضمن نطاق محدود.

Phase V — Specialists and Memory

تشمل:

Specialist Runtime
Workspace Isolation
Dependency Evaluation
Specialist Integration
Memory Retrieval
Memory Promotion Governance

الهدف:

إضافة التوازي والخبرة طويلة المدى دون تغيير الهوية المعرفية المعتمدة.

Phase VI — Temporal and Recovery Integration

تشمل:

Durable Triggers
Suspension
Resumption
Recovery Coordinator
Backup Recovery
Failure Injection
Security Recovery

الهدف:

إثبات الاستمرارية عبر التوقف والانقطاع والأعطال.

Phase VII — System Validation

تشمل:

End-to-end evaluation

Multi-project operation

Provider switching

Long-running tasks

Adversarial verification

Performance profiling

Failure injection

Integration regression

الهدف:

التحقق من أن المكونات تعمل معًا وتحقق المعمارية المقصودة.

Source: [RDMS-10-M23-U120](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2204>); source-unit SHA-256 `af34f9eb22a02dbaca69f0395fa4803f428c3a27f7e5479ecca6bd48e0f3d9e0`.

### L7-B23-096 — 96. Implementation Ordering Constraint

هذا الترتيب خطة أولية للتنفيذ، وليس إذنًا بالبدء.

قد تتطلب بعض المراحل تنفيذ أجزاء صغيرة من المراحل اللاحقة بصورة مبكرة لتوفير بيئة اختبار متكاملة.

لكن لا يجوز تشغيل المسارات الإنتاجية الحساسة دون ضمانات السلطة والمتانة اللازمة.

Source: [RDMS-10-M23-U121](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2323>); source-unit SHA-256 `0c8e10f7a68c53d46d909adc01cde2d4f40d3bca10310a0c4898dcc367892ee3`.

### L7-B23-097 — 97. Control Plane Physical Boundary

هل يجب تشغيل CommitGate وActionGate وControl Ledger في Process واحدة؟

الجواب الأولي: ليس بالضرورة.

لكن يجب إثبات أن توزيعها يحافظ على الذرية والسلطة والـFencing والتعافي.

Source: [RDMS-10-M23-U126](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2630>); source-unit SHA-256 `ea540ab860b4a22b626209aa659ad32344f8fe39b407b8911a0aa7f659f4f779`.

### L7-B23-098 — 98. Storage Technology

هل نستخدم قاعدة بيانات علائقية واحدة أم عدة مخازن متخصصة؟

لا يجب حسم التقنية قبل تحديد متطلبات المتانة والذرية والنسخ القانونية.

Source: [RDMS-10-M23-U127](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2638>); source-unit SHA-256 `e9b5fd3ad472ee0d76820f5d1a49858ec09800051836840963f12d8794edeeb4`.

### L7-B23-099 — 99. Tool Worker Isolation

هل نستخدم Processes محلية أم Containers أم Sandboxes أقوى؟

يتوقف القرار على Threat Model والآثار القابلة للوصول.

لا يجوز اختيار التقنية بناءً على سهولة تشغيلها فقط إذا لم تحقق متطلبات العزل.

Source: [RDMS-10-M23-U128](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2644>); source-unit SHA-256 `db82f619d625e3bffc82bd5e7fe5140a0ea3a635500699699cb4f405cbe9aa4f`.

### L7-B23-100 — 100. Provider Interface Capability Differences

قد تدعم بعض Providers:

Tool calling

Structured output

Streaming

Long context

Reasoning modes

بينما لا تدعمها أخرى.

يجب تحديد القدرات المطلوبة لكل نوع Invocation، وعدم افتراض تجانس Providers.

Source: [RDMS-10-M23-U129](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2652>); source-unit SHA-256 `a415fe15b69984c62bcfdde739de39acb46b4822d8e61011829a04bed14a104d`.

### L7-B23-101 — 101. Cross-Component Backpressure

كيف نمنع تراكم:

Pending actions

Observations

Specialist results

Trigger reactions

بصورة تؤدي إلى استهلاك الموارد أو تأخير الالتزامات الحرجة؟

يجب أن تحافظ السياسة على الأولوية القانونية والذرية المطلوبة، دون إنشاء سلطة جدولة جديدة.

Source: [RDMS-10-M23-U130](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2670>); source-unit SHA-256 `2a672e77172cfe1820ba572b8798487d25f841670edfbccb9c4b7006b26a3560`.

### L7-B23-102 — 102. Contract Compatibility Audit

قبل التجميد، يجب إجراء مقارنة مباشرة بين التعاريف الدقيقة في RDMS-01…09 وبين عقود RDMS-10.

خصوصًا:

Entity names

Authority fields

Allowed lifecycle states

Commit boundaries

Idempotency identities

Dependency results

Recovery semantics

بعض الأغلفة الواردة في المسودة مقترحات تكامل، وليست إثباتًا بأنها مطابقة حرفيًا لجميع Schemas السابقة.

أي تعارض يجب تصحيحه وفق المواصفة المالكة، أو إعلانه كتغيير معماري يتطلب إعادة فتحها.

Source: [RDMS-10-M23-U131](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2686>); source-unit SHA-256 `04d412e3b373d1d4f6de78c3f5f20affb03ed37a442f2f0f9482406092a8998e`.

### L7-B23-103 — 103. Required Freeze Conditions

لا يجوز تجميد RDMS-10 إلا بعد إثبات الآتي على مستوى المواصفات:

لكل كيان دائم مالك قانوني واضح.

لا توجد مسارات كتابة متعددة متنافسة إلى Canonical State.

لا توجد قناة تنفيذ خارجي تتجاوز ActionGate.

جميع الواجهات الحاملة للسلطة قابلة للتحقق.

جميع العمليات غير المتزامنة لها هوية ونتيجة قابلة للتتبع.

حالات الأعطال لا تخلق سلطات جديدة.

العلاقات بين Control Ledger وAction Journal قابلة للتعافي.

يمكن تشغيل المتخصصين بالتوازي دون تعدد الهوية المعرفية المعتمدة.

لا يؤدي تغيير Provider إلى فقدان الحالة القانونية.

يمكن استعادة المهام المعلقة دون الاعتماد على تاريخ المحادثة.

لا تتعارض عقود التكامل مع FCA أو RDMS-01…09.

يوجد مسار تنفيذ تدريجي قابل للاختبار دون التضحية بقوانين السلامة.

Source: [RDMS-10-M23-U133](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2711>); source-unit SHA-256 `0f4d46d299e329a3699ff5d5599f7fef5d45a232ed415ebc4a54ad6de85eb90c`.

### L7-B23-104 — 104. Specification Freeze vs Code Verification

تجميد RDMS-10 سيعني أن عقود التكامل أصبحت مرجعًا هندسيًا معتمدًا.

لكنه لن يعني أن البرنامج قد نُفذ أو أنه اجتاز Failure Injection Tests.

يجب الحفاظ على هذا الفصل.

Source: [RDMS-10-M23-U134](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2739>); source-unit SHA-256 `cd56f2781d6dda101af721fe69e5abf50ca1c7302fe936b21fed83c47ffd0392`.

## FCA responsibilities retained in this layer


### L7-F85 — Normal cognitive loop

```text
USER GOAL
   ↓
INTAKE
   ↓
ORIENT
   ↓
facts / assumptions / unknowns
   ↓
Executive selects cognitive depth
   ↓
focus attention
   ↓
gather highest-value information
   ↓
need causal understanding?
   ├─ yes → hypotheses → experiments → observations
   ↓
need engineering decision?
   ├─ yes → alternatives → future simulation → trade-offs
   ↓
record legal Decision
   ↓
build adaptive execution graph
   ↓
choose coherent Slice
   ↓
constrained candidate-code synthesis
   ↓
ActionProposal(s)
   ↓
legal Action path
   ↓
structural + behavioral + semantic verification
   ↓
Expected == Observed?
   ├─ no → DIAGNOSE / ORIENT / REPLAN
   └─ yes
       ↓
REVIEW / metacognitive gate
       ↓
continue / integrate / finalize
       ↓
checkpoint canonical state
       ↓
Learning Gate when valuable
```

The loop may jump backward whenever reality invalidates the current model.

Source: [FCA-85](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L3155>); source-unit SHA-256 `1c7ebf846b5e60a41437e37221ed2400d360d88f19d4bd617832352134a02168`.

## Single-owner record contracts

The owner registry distinguishes source record declarations from callable or transport signatures. Source fields marked `?` retain optionality and `[]` retain collection shape; primitive types not declared by the source remain unspecified. An abbreviated `...` correction is not permission to discard other fields. Multi-surface or parent-field preservation questions are explicitly bounded below; their declarations must not be treated as a proved conversion API.

### ActionAuthorizationRequest

Canonical owner: L7; defining specification: RDMS-10.

Source: [ActionAuthorizationRequest](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L676>); declaration SHA-256 `a8de8c2a43c680c6f871fd77700a760992bd87f411acf22a7b121e4a5b7dbb79`.

```text
ActionAuthorizationRequest {
    action_proposal_ref

    executive_authorization_ref

    executive_epoch

    target_resource_scope

    expected_world_ref

    effect_semantics_ref

    required_preconditions[]

    dependency_set_ref
}
```

### ActionAuthorizationResult

Canonical owner: L7; defining specification: RDMS-10.

Source: [ActionAuthorizationResult](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L693>); declaration SHA-256 `5640da54e625289949a8f9aeeed5c6e7f05dab315d509a325458b72f4a3b8d48`.

```text
ActionAuthorizationResult {
    action_ref

    authorization_disposition

    action_class

    applicable_execution_boundary

    rejection_reasons[]

    authorization_receipt_ref?
}
```

### ActionDeliveryContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [ActionDeliveryContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3740>); declaration SHA-256 `d9771caf5be03c5c6995858af38e0539561a2f4975711c59d1e28db84713003f`.

```text
ActionDeliveryContract {
    action_ref

    delivery_identity

    execution_attempt_identity

    dispatch_intent_ref

    sealed_execution_intent_ref

    receiving_worker_identity

    receiving_worker_generation

    retry_policy_ref

    delivery_deduplication_scope

    acknowledgement_semantics

    possible_external_effect_status

    required_reconciliation_ref?
}
```

### ActiveWorkInvalidationContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [ActiveWorkInvalidationContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4172>); declaration SHA-256 `781538040cb5f16a1eae3afc9055cee672fcd4e766b14f0fbb6e4b3ce1a1fa17`.

```text
ActiveWorkInvalidationContract {
    invalidation_event_ref

    changed_dependency_refs[]

    affected_decision_refs[]

    affected_plan_refs[]

    affected_slice_refs[]

    affected_capability_invocations[]

    affected_specialist_refs[]

    affected_authorization_refs[]

    affected_queued_action_refs[]

    affected_inflight_action_refs[]

    dependency_evaluation_refs[]

    required_revalidation_refs[]

    unresolved_effect_constraints[]
}
```

### ArtifactPublicationContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [ArtifactPublicationContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3835>); declaration SHA-256 `ecd4efdc4fb857e0f5b37ea9ad5216faaadf587d614793452a1c6c4b4e784a07`.

```text
ArtifactPublicationContract {
    artifact_ref

    artifact_kind

    content_integrity_ref

    source_provenance_ref

    owning_storage_domain

    durability_requirement

    publication_generation

    publication_status

    canonical_reference_eligibility

    retention_obligations[]

    recovery_requirements[]
}
```

### CanonicalContractRegistry

Canonical owner: L7; defining specification: RDMS-10.

Source: [CanonicalContractRegistry](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3049>); declaration SHA-256 `98be26a8ddf6c1883dbe9158e4dbbf0d78fff54a0ac5c52033137d9c08ab493d`.

```text
CanonicalContractRegistry {
    registry_version

    contract_entries[] {
        contract_id

        owning_specification

        canonical_type_ref

        canonical_schema_version

        canonical_field_refs[]

        legal_semantics_ref

        permitted_projection_refs[]

        compatibility_requirements[]

        forbidden_semantic_substitutions[]
    }
}
```

### CapabilityActivationContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [CapabilityActivationContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4925>); declaration SHA-256 `026bb25fd353ffcabaa2ba4b1a5e101238efb218e9af666701f6045a6ccd9282`.

```text
CapabilityActivationContract {
    capability_ref

    intended_operational_scope

    required_component_refs[]

    required_invariant_proofs[]

    required_conformance_tests[]

    prohibited_effects_until_activation[]

    activation_policy_ref

    activation_decision
}
```

### CapabilityInvocation

Canonical owner: L7; defining specification: RDMS-10.

Source: [CapabilityInvocation](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L367>); declaration SHA-256 `8fec5e274ffc9f94b0bbde0178edb4b6fdcfe0241105dd079e62d1f954b26ccd`.

```text
CapabilityInvocation {
    invocation_id

    capability_kind

    goal_ref

    cognitive_context_ref

    dependency_set_ref

    provider_policy_ref?

    resource_budget_ref

    requested_outputs[]
}
```

### CapabilityTransportResult

Canonical owner: L7; defining specification: RDMS-10.

Source: [CapabilityResult](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L384>); declaration SHA-256 `e8ae9d35f870fc3efb84694641074038fd2961677393b2a5f5ee6d6f0cb717b5`.

Editorial transport label only; the archived RDMS-10 spelling remains unchanged. Canonical owner semantics and lossless reference/payload obligations are mandatory; alias naming is not field mapping approval.

```text
CapabilityTransportResult {
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

### CommitRequest

Canonical owner: L7; defining specification: RDMS-10.

Source: [CommitRequest](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L578>); declaration SHA-256 `5d106c2ff415f7230bae0af0e52640cd8a3c93d46e153f65cacdb63015362328`.

```text
CommitRequest {
    request_id

    project_id

    executive_epoch

    patch_proposal_ref

    authorization_ref

    expected_state_versions[]

    dependency_set_ref

    idempotency_key
}
```

### CommitResult

Canonical owner: L7; defining specification: RDMS-10.

Source: [CommitResult](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L595>); declaration SHA-256 `e00f40e684520d081b79fe8f60d55273d2ea9d1f6ec927ebe2b0ad96041a8a17`.

```text
CommitResult {
    request_id

    disposition

    committed_state_ref?

    control_commit_ref?

    rejection_reasons[]

    current_version_refs[]
}
```

### CompletionStateBinding

Canonical owner: L7; defining specification: RDMS-10.

Source: [CompletionStateBinding](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6527>); declaration SHA-256 `fa6057f2f9c27814e892375aa6f9af148e8edcf0abcb5239dce4d4210d87b515`.

```text
CompletionStateBinding {
    goal_ref

    goal_version

    acceptance_criteria_frontier

    verified_repository_ref

    verified_world_state_scope

    verification_evidence_refs[]

    dependency_validation_ref

    relevant_policy_frontier

    unresolved_obligation_refs[]

    finalization_commit_preconditions[]

    finalization_commit_ref?
}
```

### ContextDisclosureAdmission

Canonical owner: L7; defining specification: RDMS-10.

Source: [ContextDisclosureAdmission](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4333>); declaration SHA-256 `cf8ab1e0abe27665db71d9e9661c8a78dc07d830b2123480121809753ff8df72`.

```text
ContextDisclosureAdmission {
    context_package_ref

    originating_project_ref

    destination_provider_ref

    requested_processing_purpose

    included_data_class_refs[]

    applicable_policy_frontier

    authorized_disclosure_scope

    prohibited_content_refs[]

    source_trust_refs[]

    effective_transfer_scope

    admission_status
}
```

### ContextPackage

Canonical owner: L7; defining specification: RDMS-10.

Source: [ContextPackage](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L537>); declaration SHA-256 `42af8074562cf987c00a5635c73aea5a3be37923f905cda77195a277d2830e0a`.

```text
ContextPackage {
    context_package_id

    project_ref

    goal_ref

    focus_ref

    relevant_state_refs[]

    relevant_evidence_refs[]

    applicable_contract_refs[]

    mandatory_context_manifest_ref

    memory_retrieval_refs[]

    dependency_set_ref

    source_trust_metadata_refs[]

    disclosure_policy_ref
}
```

### ControlActionDurabilityContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [ControlActionDurabilityContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3525>); declaration SHA-256 `32c569ea815910da71659bd6c36d2ddb8ddbebe5436444e9c4c1ab879c036ddd`.

```text
ControlActionDurabilityContract {
    action_ref

    canonical_lifecycle_owner_ref

    control_lifecycle_ref

    action_journal_ref

    authoritative_control_frontier

    required_atomic_reference_set[]

    durable_ordering_contract

    dispatch_eligibility_condition

    crash_reconciliation_rules[]

    supported_failure_model_ref

    integrity_verification_refs[]
}
```

### CrossComponentEventContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [CrossComponentEventContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3914>); declaration SHA-256 `e388f1e0327f7181ccf0709ed846e808c0bc3dc6bac9690929edf312a96296bc`.

```text
CrossComponentEventContract {
    event_id

    event_type

    producing_component_ref

    project_ref

    causal_parent_refs[]

    authoritative_sequence_ref?

    related_action_ref?

    schema_version

    idempotency_key

    delivery_semantics

    required_ordering_scope

    replay_requirements

    event_integrity_ref
}
```

### DependencyEvaluationRequest

Canonical owner: L7; defining specification: RDMS-10.

Source: [DependencyEvaluationRequest](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L738>); declaration SHA-256 `a86399344ce0d34cb607529fc4a6b401f584e69ac1d5c2a5a22e7a3f7b2dcd2f`.

```text
DependencyEvaluationRequest {
    target_result_refs[]

    dependency_set_refs[]

    current_context_ref

    requested_validity_scope
}
```

### DependencyEvaluationResult

Canonical owner: L7; defining specification: RDMS-10.

Source: [DependencyEvaluationResult](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L747>); declaration SHA-256 `18e37fd39ccd27d0c2177917254608f627ddda5e4e1909bc1206bb728c666285`.

```text
DependencyEvaluationResult {
    target_result_ref

    validity:
        VALID
        STALE
        PARTIALLY_STALE
        UNKNOWN

    affected_dependency_refs[]

    unaffected_dependency_refs[]

    required_revalidation_refs[]
}
```

### DispatchAdmissionCutover

Canonical owner: L7; defining specification: RDMS-10.

Source: [DispatchAdmissionCutover](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6091>); declaration SHA-256 `6c98bbb843273f8f952861c7c49cd7c8967d3780a4448fd801c529765879ca95`.

```text
DispatchAdmissionCutover {
    action_ref

    executive_epoch

    originating_authorization_ref

    dispatch_intent_commit_ref

    dependency_frontier_ref

    current_dependency_assessment_ref

    current_policy_frontier_ref

    current_execution_generation

    admission_ordering_ref

    applicable_invalidation_refs[]

    effective_execution_binding_ref

    cutover_disposition

    possible_dispatch_assessment
}
```

### EffectiveExecutionAuthorityScope

Canonical owner: L7; defining specification: RDMS-10.

Source: [EffectiveExecutionAuthorityScope](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6210>); declaration SHA-256 `ab5167f3ffcd28130b58e1e38ceadbbf92566c961ed2e58d2d1297f189db6450`.

```text
EffectiveExecutionAuthorityScope {
    action_ref

    originating_project_ref

    authenticated_request_principal_ref

    delegated_authority_ref

    actual_target_resource_ref

    target_project_ref?

    effective_execution_principal_ref

    applicable_credential_scope_ref

    authorized_project_scope

    authorized_resource_scope

    authorization_proof_ref

    enforcement_result
}
```

### EffectiveExecutionBinding

Canonical owner: L7; defining specification: RDMS-10.

Source: [EffectiveExecutionBinding](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5978>); declaration SHA-256 `d5c98f9d9e69edf753fbdda12922a0df68c67cc556e02990bb963f0a93601da1`.

```text
EffectiveExecutionBinding {
    action_ref

    sealed_execution_intent_ref

    authorized_operation_kind

    adapter_identity

    adapter_integrity_ref

    effective_operation_ref

    effective_argument_integrity_ref

    resolved_target_resource_refs[]

    execution_environment_ref

    effective_execution_principal_ref

    authorized_effect_scope

    final_validation_ref

    dispatch_eligibility
}
```

### ExecutionContainmentContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [ExecutionContainmentContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4796>); declaration SHA-256 `b45c7fabafd6d3201c5cf1f9d551fee3cc3eedebb175bc0ff8422b777ae2afdf`.

```text
ExecutionContainmentContract {
    execution_boundary_ref

    project_scope

    filesystem_read_scope

    filesystem_write_scope

    network_access_scope

    credential_access_scope

    process_privileges

    shared_resource_reachability[]

    disposal_guarantees[]

    containment_verification_refs[]

    effective_action_classification
}
```

### ExecutiveTransitionIntegrationBinding

Canonical owner: L7; defining specification: RDMS-10.

Source: [ExecutiveTransitionIntegrationBinding](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3442>); declaration SHA-256 `74d692bfc0f33d9890f8b7bc9fbe3e4dae3b7563bd8d637370e7288527aa5c2e`.

```text
ExecutiveTransitionIntegrationBinding {
    executive_decision_ref

    executive_epoch

    project_ref

    goal_ref

    slice_ref?

    source_cognitive_state

    selected_operation_ref

    expected_canonical_versions[]

    policy_frontier_ref

    dependency_frontier_ref

    target_transition_contract_ref

    control_commit_ref?
}
```

### HumanIngressAuthorityBinding

Canonical owner: L7; defining specification: RDMS-10.

Source: [HumanIngressAuthorityBinding](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3271>); declaration SHA-256 `04bcb4e41fa3f59d9d38bb4a2be054c153bec72689caa13fbbcd6cd0355c36af`.

```text
HumanIngressAuthorityBinding {
    request_ref

    authenticated_principal_ref

    project_ref

    verified_role_refs[]

    authority_domain_refs[]

    requested_operation_scope

    allowed_requirement_scope

    instruction_authority

    applicable_policy_ref

    request_provenance_ref

    authorization_status
}
```

### ImplementationDependencyGraph

Canonical owner: L7; defining specification: RDMS-10.

Source: [ImplementationDependencyGraph](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4883>); declaration SHA-256 `83cfe35a8ba076718cc817b73dee3179911641780a20a666d55467a060bcf21a`.

```text
ImplementationDependencyGraph {
    component_ref

    required_contract_refs[]

    mandatory_runtime_dependencies[]

    optional_runtime_dependencies[]

    minimum_safe_dependency_set[]

    permitted_stub_behavior

    forbidden_activation_conditions[]

    conformance_gate_refs[]

    activation_eligibility
}
```

### IntegratedCompletionEvidence

Canonical owner: L7; defining specification: RDMS-10.

Source: [IntegratedCompletionEvidence](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4085>); declaration SHA-256 `61a9b48635b374ccf5a78e9ed18ca8b50097e9d29a11b2dfcef1994e06afd3df`.

```text
IntegratedCompletionEvidence {
    goal_ref

    current_goal_version

    acceptance_criteria_refs[]

    verified_criteria_refs[]

    unverified_criteria_refs[]

    failed_criteria_refs[]

    verification_record_refs[]

    dependency_evaluation_ref

    current_repository_ref

    unresolved_action_constraints[]

    unresolved_specialist_constraints[]

    applicable_policy_ref

    finalization_assessment_ref

    authorized_completion_scope
}
```

### MemoryRetrievalRequest

Canonical owner: L7; defining specification: RDMS-10.

Source: [MemoryRetrievalRequest](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1135>); declaration SHA-256 `52a9b95579ab0c8cb214cff7e5cd1fef339e20d509c4a10944811e445f887d36`.

```text
MemoryRetrievalRequest {
    project_ref

    query_context_ref

    requested_memory_scopes[]

    applicability_context_ref

    access_policy_ref

    result_budget
}
```

### MemoryRetrievalTransportResult

Canonical owner: L7; defining specification: RDMS-10.

Source: [MemoryRetrievalResult](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1148>); declaration SHA-256 `a70de6ab479231f1c2f991196c6406715513f940d0af266e1e05b22ce533c35a`.

Editorial transport label only; the archived RDMS-10 spelling remains unchanged. Canonical owner semantics and lossless reference/payload obligations are mandatory; alias naming is not field mapping approval.

```text
MemoryRetrievalTransportResult {
    memory_refs[]

    relevance_assessments[]

    provenance_refs[]

    applicability_assessments[]

    trust_metadata_refs[]
}
```

### ObservationCausalAttachmentContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [ObservationCausalAttachmentContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6309>); declaration SHA-256 `6dbabd3c921605671ac0cd84d1d22319559f537e42ec6eb9c930984bf3121851`.

```text
ObservationCausalAttachmentContract {
    observation_ref

    source_identity

    source_event_identity?

    raw_observation_scope

    claimed_action_ref?

    verified_action_ref?

    source_provenance_ref

    causal_attachment_evidence_refs[]

    missing_parent_refs[]

    admissible_interpretation_scope

    reattachment_requirements[]
}
```

### ObservationIngressRequest

Canonical owner: L7; defining specification: RDMS-10.

Source: [ObservationIngressRequest](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L946>); declaration SHA-256 `9a04917555e9f063bdf029e5e24f9c1f189158aecf0506648d1c3371fbf36d98`.

```text
ObservationIngressRequest {
    source_identity

    source_event_identity?

    related_action_ref?

    observation_kind

    payload_ref

    observed_scope

    source_provenance_ref

    source_integrity_metadata
}
```

### ObservationIngressResult

Canonical owner: L7; defining specification: RDMS-10.

Source: [ObservationIngressResult](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L963>); declaration SHA-256 `c5f60baed7e577dadf9aef7a0d67d82589de02dce722ffbf012b6bfa6d16ad67`.

```text
ObservationIngressResult {
    observation_ref

    append_disposition

    deduplication_result

    source_validation_result
}
```

### ObservationSourceBinding

Canonical owner: L7; defining specification: RDMS-10.

Source: [ObservationSourceBinding](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3995>); declaration SHA-256 `486ffdc2cc70a4eaff365090f9321a578a1cd667846176b85b0974c84e077994`.

```text
ObservationSourceBinding {
    observation_ref

    source_identity

    source_kind

    source_trust_classification

    related_action_ref?

    observed_resource_scope

    observed_event_scope

    raw_report_ref?

    directly_observed_effect_refs[]

    observation_provenance_ref

    observation_integrity_ref

    supported_claim_scope

    known_limitations[]
}
```

### ProjectExecutionBoundary

Canonical owner: L7; defining specification: RDMS-10.

Source: [ProjectExecutionBoundary](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4721>); declaration SHA-256 `9b9d072827a7ae2a3a34f9917f8786355a0e493b37f57e1c6b1aa56745e2e974`.

```text
ProjectExecutionBoundary {
    project_id

    canonical_workspace_ref

    executive_authority_domain_ref

    control_namespace_ref

    action_namespace_ref

    artifact_namespace_ref

    specialist_namespace_ref

    memory_access_scope

    credential_scope_ref

    tool_resource_scope

    cross_project_access_policy_ref
}
```

### ReasoningInvocation

Canonical owner: L7; defining specification: RDMS-10.

Source: [ReasoningInvocation](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L446>); declaration SHA-256 `2361951b9792a158ae485ffba195c12056bf6200e6b267aa75e604a93facfb48`.

```text
ReasoningInvocation {
    invocation_id

    originating_executive_epoch

    task_ref

    requested_capability

    context_package_ref

    trusted_instruction_envelope_ref

    allowed_output_schema

    resource_budget_ref

    provider_selection_ref

    attempt_generation
}
```

### ReasoningProviderCapabilityContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [ReasoningProviderCapabilityContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4257>); declaration SHA-256 `9dd5b7f369c733a64f1bb6fcc0a17da3ae9f2ad414a788c95903ecba21a02db2`.

```text
ReasoningProviderCapabilityContract {
    provider_ref

    supported_input_modes[]

    supported_output_modes[]

    supported_schema_modes[]

    tool_call_semantics

    streaming_semantics

    context_limit_profile

    invocation_timeout_profile

    supported_reasoning_operations[]

    provider_data_handling_ref

    capability_validation_refs[]

    compatibility_status
}
```

### ReasoningResult

Canonical owner: L7; defining specification: RDMS-10.

Source: [ReasoningResult](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L467>); declaration SHA-256 `d53200e90a84bfbba5b50933711b23bd58ff8a58713937063f3aa2fb169d660e`.

```text
ReasoningResult {
    invocation_id

    provider_identity

    attempt_generation

    generated_content_ref

    structured_proposals[]

    provider_usage?

    provider_status

    provenance_ref

    trust_classification

    validation_result
}
```

### RecoverableActionDeliveryObligation

Canonical owner: L7; defining specification: RDMS-10.

Source: [RecoverableActionDeliveryObligation](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5685>); declaration SHA-256 `52b78f2353eea358151165a9b085d7c6354098967e027ef30510af0365ac7e76`.

```text
RecoverableActionDeliveryObligation {
    action_ref

    authoritative_lifecycle_ref

    dispatch_intent_commit_ref

    sealed_execution_intent_ref

    delivery_correlation_ref

    execution_attempt_refs[]

    known_external_effect_refs[]

    recovery_enumeration_scope

    unresolved_effect_scope

    legal_continuation_requirement

    recovery_assessment_ref?
}
```

### RecoveryAssessmentRequest

Canonical owner: L7; defining specification: RDMS-10.

Source: [RecoveryAssessmentRequest](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1279>); declaration SHA-256 `ecb8955672273309e633d4a370811442a173a37ec25e624b73e56654a7f3b0e6`.

```text
RecoveryAssessmentRequest {
    recovery_case_ref

    affected_component_refs[]

    restored_control_frontier

    suspected_failure_domains[]

    unresolved_action_refs[]

    relevant_policy_refs[]
}
```

### RecoveryAssessmentResult

Canonical owner: L7; defining specification: RDMS-10.

Source: [RecoveryAssessmentResult](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1292>); declaration SHA-256 `e529143b107029d647f2e4da11d805296d566c43818de829f81c252efa7f63ff`.

```text
RecoveryAssessmentResult {
    recovery_case_ref

    authority_status

    canonical_integrity_status

    external_effect_constraints[]

    dependency_validation_refs[]

    security_restrictions[]

    permitted_operational_scope

    outstanding_recovery_obligations[]
}
```

### RepositoryMutationIntegrationContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [RepositoryMutationIntegrationContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3353>); declaration SHA-256 `d784f1b3d816862c724f1b99b574f15110762662fba65dc63c9e0d245afee075`.

```text
RepositoryMutationIntegrationContract {
    originating_goal_ref

    originating_slice_ref

    candidate_artifact_ref

    base_repository_ref

    expected_repository_ref?

    intended_change_surface

    allowed_repository_scope

    forbidden_repository_scope

    action_proposal_ref

    action_authorization_ref

    execution_result_ref?

    resulting_repository_observation_ref?

    verification_requirement_refs[]

    canonical_reconciliation_refs[]
}
```

### RuntimeActivationContract

Canonical owner: L7; defining specification: RDMS-10.

Source: [RuntimeActivationContract](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4634>); declaration SHA-256 `f01fd303e2e51787f4802da55a040f5c6c87370ff7c027a126cfc0be1097b268`.

```text
RuntimeActivationContract {
    component_ref

    project_scope

    permitted_operation_classes[]

    required_recovery_frontier

    required_authority_status

    required_dependency_status

    required_security_status

    unresolved_effect_restrictions[]

    applicable_policy_frontier

    activation_generation

    activation_authorization_ref
}
```

### SealedExecutionIntent

Canonical owner: L7; defining specification: RDMS-10.

Source: [SealedExecutionIntent](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3621>); declaration SHA-256 `8bf749d80ed5502c3a670b64853ea11cd4fb0635541eb7efd087468202bde01a`.

```text
SealedExecutionIntent {
    action_ref

    authorized_tool_identity

    authorized_operation_kind

    effective_argument_ref

    effective_argument_integrity_ref

    authorized_target_identity

    authorized_resource_scope

    authorized_effect_semantics_ref

    execution_boundary_ref

    executive_epoch

    authorization_generation

    required_pre_dispatch_conditions[]

    authorization_receipt_ref
}
```

### SealedOutboundContext

Canonical owner: L7; defining specification: RDMS-10.

Source: [SealedOutboundContext](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L6413>); declaration SHA-256 `9a32bf619d57ada734a71008191da386626d6d7fbd7d4c8da3bd4383e79674f6`.

```text
SealedOutboundContext {
    invocation_ref

    originating_project_ref

    final_destination_provider_ref

    final_destination_boundary_ref

    final_context_manifest_ref

    included_content_integrity_refs[]

    included_data_classification_refs[]

    applicable_disclosure_policy_frontier

    authorized_processing_purpose

    disclosure_admission_ref

    outbound_integrity_binding

    release_eligibility
}
```

### SpecialistExecutionAuthorityBinding

Canonical owner: L7; defining specification: RDMS-10.

Source: [SpecialistExecutionAuthorityBinding](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4394>); declaration SHA-256 `dcc50090ab383c0335da8556942b07e60b142bf72cc4d1aff6e8bbdf2259133b`.

```text
SpecialistExecutionAuthorityBinding {
    specialist_run_ref

    specialist_contract_ref

    specialist_generation

    project_scope

    permitted_tool_classes[]

    permitted_resource_refs[]

    permitted_effect_classes[]

    forbidden_effect_classes[]

    isolation_boundary_ref

    current_contract_validity

    required_action_authorization_ref?
}
```

### SpecialistIntegrationTransaction

Canonical owner: L7; defining specification: RDMS-10.

Source: [SpecialistIntegrationTransaction](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4477>); declaration SHA-256 `95928a0e471c9e012a12eb39f2efb4b510d8a6b76488768df930e29c50768027`.

```text
SpecialistIntegrationTransaction {
    integration_id

    specialist_result_ref

    originating_contract_ref

    originating_repository_ref

    current_target_repository_ref

    dependency_evaluation_ref

    structural_conflict_assessment_ref

    semantic_conflict_assessment_ref

    verification_obligations[]

    proposed_integration_effect_refs[]

    executive_integration_authorization_ref

    applicable_action_ref?

    final_integration_evidence_ref?
}
```

### SpecialistRecruitmentRequest

Canonical owner: L7; defining specification: RDMS-10.

Source: [SpecialistRecruitmentRequest](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1032>); declaration SHA-256 `0732f107bafea111d91c1027e6b5c6de03958f93a52427e777603177fee9343c`.

```text
SpecialistRecruitmentRequest {
    parent_goal_ref

    recruitment_intent_ref

    specialist_role

    task_contract_ref

    allowed_resource_scope

    isolation_profile_ref

    budget_ref

    originating_executive_epoch
}
```

### SpecialistRecruitmentResult

Canonical owner: L7; defining specification: RDMS-10.

Source: [SpecialistRecruitmentResult](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1049>); declaration SHA-256 `e854d2b3d470048a62d3314f5380688ed1a2bbc23fcb8e49c83dfd1bd6ecf665`.

```text
SpecialistRecruitmentResult {
    specialist_run_ref

    accepted_contract_ref

    workspace_ref

    lifecycle_ref

    execution_generation
}
```

### ToolExecutionReport

Canonical owner: L7; defining specification: RDMS-10.

Source: [ToolExecutionReport](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L840>); declaration SHA-256 `586b59b030ee2eeb8556afa0d4e66daa02c52dc26981a5652ce2b7e63054fe8f`.

```text
ToolExecutionReport {
    action_ref

    execution_attempt_ref

    tool_identity

    reported_status

    output_artifact_refs[]

    execution_metadata_refs[]

    observed_effect_refs[]

    unresolved_effects[]
}
```

### ToolExecutionRequest

Canonical owner: L7; defining specification: RDMS-10.

Source: [ToolExecutionRequest](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L821>); declaration SHA-256 `2ddc26f5f4222dd18c790a6cfc6ae9f11cac691aebdfecd16020479346c18419`.

```text
ToolExecutionRequest {
    action_ref

    dispatch_receipt_ref

    tool_identity

    execution_boundary_ref

    authorized_resource_scope

    arguments_ref

    effect_semantics_ref

    execution_generation

    timeout_policy
}
```

### TriggerActionCausalityBinding

Canonical owner: L7; defining specification: RDMS-10.

Source: [TriggerActionCausalityBinding](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L4563>); declaration SHA-256 `ca5026690cd7b722270eced9f7105032da6a7e6f95e0173c7d2dcad84052bd4c`.

```text
TriggerActionCausalityBinding {
    trigger_ref

    trigger_generation

    source_event_identity

    canonical_reaction_identity

    reaction_commit_ref

    derived_action_proposal_refs[]

    derived_action_identity_refs[]

    action_lifecycle_refs[]

    causal_binding_integrity

    replay_semantics

    deduplication_scope
}
```

### TriggerDerivedWorkCommitment

Canonical owner: L7; defining specification: RDMS-10.

Source: [TriggerDerivedWorkCommitment](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L5828>); declaration SHA-256 `d9b47cadcb4d7322b954a69c91d8acb6c3e871b54bd31510b1e216f209714373`.

```text
TriggerDerivedWorkCommitment {
    trigger_ref

    trigger_generation

    source_event_identity

    canonical_reaction_identity

    reaction_commit_ref

    derived_work_identity

    required_continuation_scope

    durable_continuation_ref

    existing_action_refs[]

    required_authorization_path

    recovery_deduplication_basis

    current_continuation_assessment
}
```

### TriggerEvaluationRequest

Canonical owner: L7; defining specification: RDMS-10.

Source: [TriggerEvaluationRequest](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1217>); declaration SHA-256 `b6c4816dfebd221be3ce916aa5480801c014a2bac401c98990fe5731268b2515`.

```text
TriggerEvaluationRequest {
    trigger_ref

    trigger_generation

    source_event_ref?

    source_cursor_ref?

    evaluation_context_ref
}
```

### TriggerEvaluationResult

Canonical owner: L7; defining specification: RDMS-10.

Source: [TriggerEvaluationResult](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1228>); declaration SHA-256 `5d1bd536aba8106a068c38e5452dca175d8f4843393878118022e8e0057a0ade`.

```text
TriggerEvaluationResult {
    trigger_ref

    firing_candidate_ref?

    canonical_reaction_key

    required_control_transition_ref?

    evaluation_status
}
```

### TrustedEnvelopeAdmission

Canonical owner: L7; defining specification: RDMS-10.

Source: [TrustedEnvelopeAdmission](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L3162>); declaration SHA-256 `6e1618ac872738b218dc2cf66f3754a6baa4a4f6fd32e431281a19564cb55716`.

```text
TrustedEnvelopeAdmission {
    envelope_ref

    authenticated_sender_ref

    receiving_component_ref

    trusted_transport_context_ref

    permitted_message_types[]

    trusted_field_issuer_refs[]

    claimed_authority_metadata

    verified_authority_scope

    executive_epoch_binding?

    project_scope

    replay_protection_ref

    payload_integrity_ref

    admission_result
}
```

### TrustedMessageEnvelope

Canonical owner: L7; defining specification: RDMS-10.

Source: [TrustedMessageEnvelope](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L1383>); declaration SHA-256 `b8acc80fe77b02cf47ecff6614ac9b8db712b9351fb2550b6fe5faf8568870fb`.

```text
TrustedMessageEnvelope {
    message_id

    schema_version

    project_id

    originating_component

    trusted_execution_identity?

    executive_epoch?

    causal_parent_refs[]

    payload_ref

    payload_schema

    provenance_ref

    instruction_authority

    integrity_metadata
}
```


## Acceptance boundary

Source integrity and article locators are mechanically verified. The source coverage ledger distinguishes directly incorporated clauses from baseline reconciliation still requiring proof. The registry distinguishes governing semantic duties from unresolved record-shape or parent-field conversion. This document is a review candidate, not a declaration that mandatory normative completeness or implementation readiness has passed. Open scopes do not suspend unrelated rules whose sources and amendment effects are verified.

## Retained RDMS invariant corpus

Baseline admission follows its final source freeze; the archived draft-status label is historical. Explicit replacements govern affected wording and all added invariant obligations remain in the amended articles.

### L7-BI23

RDMS10-I01 — The integrated runtime preserves one canonical cognitive authority.

RDMS10-I02 — Physical process separation cannot create independent canonical mutation authority.

RDMS10-I03 — Reasoning providers produce proposals and cannot directly authorize effects.

RDMS10-I04 — Canonical cognitive mutation passes through the legal CommitGate path.

RDMS10-I05 — Shared-world mutation passes through ActionGate and durable Action Journal semantics.

RDMS10-I06 — Observation ingress remains distinct from semantic evidence interpretation.

RDMS10-I07 — Semantic reasoning cannot manufacture authoritative reality observations.

RDMS10-I08 — Every executable Slice traces to a canonical Goal.

RDMS10-I09 — Every authority-bearing operation is bound to a valid Executive epoch.

RDMS10-I10 — Trusted authorization metadata cannot be minted by untrusted payload content.

RDMS10-I11 — Provider substitution cannot alter canonical project identity or authority.

RDMS10-I12 — Specialist results cannot directly mutate canonical cognition.

RDMS10-I13 — Specialist integration requires applicable freshness, verification and authority checks.

RDMS10-I14 — Dependency validity is evaluated by the canonical Dependency Evaluation Engine.

RDMS10-I15 — Global state version alone cannot determine semantic staleness.

RDMS10-I16 — Retrieved memory is precedent, not automatically current truth.

RDMS10-I17 — Memory promotion requires the governed learning path.

RDMS10-I18 — Durable triggers use the canonical temporal lifecycle.

RDMS10-I19 — Trigger replay cannot silently duplicate canonical reactions.

RDMS10-I20 — Action timeout is not proof of world-effect failure.

RDMS10-I21 — Unknown external outcomes retain their applicable IN_DOUBT semantics.

RDMS10-I22 — External actions cannot be blindly retried when their outcomes are unresolved and non-idempotent.

RDMS10-I23 — Restore and recovery cannot bypass canonical authority boundaries.

RDMS10-I24 — Canonical recovery derives from trusted durable state, not conversational history.

RDMS10-I25 — Derived indexes and caches cannot override canonical sources.

RDMS10-I26 — Interfaces must preserve typed identity, versions, authority and failure semantics.

RDMS10-I27 — Recoverability-critical cross-component references require enforceable integrity guarantees.

RDMS10-I28 — A legal control commit does not prove that its associated external effect occurred.

RDMS10-I29 — Process isolation claims must correspond to actual reachable effects.

RDMS10-I30 — Tool classification cannot be bypassed through cognitive operation naming.

RDMS10-I31 — Operational monitoring cannot independently authorize cognitive or world mutations.

RDMS10-I32 — Context assembly must preserve applicable mandatory safety and trust constraints.

RDMS10-I33 — Provider and specialist outputs cannot elevate their own instruction authority.

RDMS10-I34 — Finalization claims cannot exceed currently supported verification scope.

RDMS10-I35 — Physical modularization must preserve frozen recovery and atomicity guarantees.

RDMS10-I36 — A component cannot acquire new authority solely because another component is unavailable.

RDMS10-I37 — Implementation choices cannot silently redefine frozen entity states or legal write paths.

RDMS10-I38 — Cross-component concurrency must not permit conflicting canonical ownership.

RDMS10-I39 — Unknown mandatory safety conditions block dependent operations without unnecessarily blocking proven-independent work.

RDMS10-I40 — Runtime integration must preserve the semantics of all frozen parent specifications.

Source: [RDMS-10-M23-U122](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt#L2331>).
