<!-- GAIA-C01-PHASE13-CURRENT-STATUS START -->
# CURRENT READING GUIDE — GAIA-C01 Phase 13

**STATUS: CONSOLIDATION DRAFT; NOT FROZEN.**  
**Owned responsibility:** Memory retrieval and governed learning.  
**Source rule:** Full original normative texts remain unmodified in the archived source set and the source annex of this document. A historical draft is NOT automatically the effective current law: approved C01/C02/C03 corrections and final freeze decisions must be incorporated before the consolidated layer supersedes those sources. Phase 11 reference tests are not production/runtime verification.  
**Forbidden:** silent defaulting, missing-authority inference, lossy migration, or treating transport wrappers as canonical entities.

**FCA source sections/appendices assigned:** 7.  
**RDMS source sets assigned:** 1; **approved original message parts:** 2.  
**27-name ownership subset present here:** 2.

| Attached RDMS source | Original message parts | Source interpretation |
|---|---:|---|
| RDMS-07 | 2 | Original draft + approved corrections / freeze decision, read with precedence |

| Canonical-type ownership candidate | Source | Current migration decision |
|---|---|---|
| `MemoryProposal` | RDMS-07 | `DIRECT_CANONICAL_USE_SELECTED__PROJECTION_NOT_APPROVED` |
| `MemoryRetrievalResult` | RDMS-07 | `EDITORIAL_TRANSPORT_ALIAS_SELECTED_FOR_CONSOLIDATION_DRAFT` |

**Freeze blocker:** An independently usable, contradiction-free, *effective* contract and law text has not yet been consolidated from draft plus correction overlays. See `../reviews/GAIA_C01_PHASE13_FREEZE_REVIEW_AR.md`, `GAIA_C01_PHASE13_LAYER_COVERAGE.json`, and the Phase-12 contract decision register. Runtime validation belongs to a separate implementation stage; existing architectural ambiguities cannot be waived by deferring tests.
<!-- GAIA-C01-PHASE13-CURRENT-STATUS END -->

---

<!-- GAIA-C01-PHASE12-DECISION-INDEX START -->
## GAIA-C01 Phase 12 — Effective owner & change-control index (DRAFT)

**Not a new frozen law.** Original source sections and approved overlays below retain authority. Do not infer legal equivalence of transport projections or historical migrations. Global layer freeze remains unauthorized.

**Source-owned reused contracts in this layer:** 2.

| Canonical contract | Governing original source | Phase-12 interpretation |
|---|---|---|
| `MemoryProposal` | `RDMS-07` | Direct original type; no conversion by default. |
| `MemoryRetrievalResult` | `RDMS-07` | Full canonical type kept; L7 transport name is only a draft editorial alias. |

Refer to `../reviews/GAIA_C01_PHASE12_CONTROLLED_CONTRACT_DECISIONS.md` and the JSON decision ledger for exact source anchors and remaining proof gates.
<!-- GAIA-C01-PHASE12-DECISION-INDEX END -->

---

<!-- GAIA-C01-PHASE10-RECONCILIATION START -->
## GAIA-C01 Phase 10 — Effective contract approval boundary (CANDIDATE)

Cross-layer contract focus: **`MemoryRetrievalResult`**. The complete preservation crosswalk and rejection cases are in `../reviews/GAIA_C01_PHASE10_EFFECTIVE_CROSSWALK.md` and `../reviews/GAIA_C01_PHASE10_FIVE_PRIORITY_CROSSWALKS.json`. **Original frozen source annexes and verbatim declarations remain authoritative; no candidate alias or projection is approved for canonical migration.**
<!-- GAIA-C01-PHASE10-RECONCILIATION END -->

---

<!-- GAIA-C01-PHASE9 CONTRACT PUBLICATION START -->
## GAIA-C01 Phase 9 — Curated source-backed contract publication (NOT RE-FROZEN)

**Status: VERBATIM SOURCE BASELINES ONLY — effective cross-layer projections remain unapproved.**

This section is a navigation and source-publication aid. It does not overwrite historical FCA or RDMS source sections. Corrections/overlays must be applied according to the approved original source history, not inferred from an earlier draft.

**Owning layer:** `L5`. **Published reused names:** `2`.

### MemoryProposal — `C8-07`

**Owner candidate:** `RDMS-07` · **Review risk:** `CONDITIONAL` · **Gate:** `MAPPING_PROOF_PENDING`.
**Exact source:** `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt` line 486; extracted block SHA-256 `954762e236b07d60a1c7480f60f9383a0f914a88043e9f541e6567ed0a6557af`.

```text
MemoryProposal {
    proposal_id

    claim

    proposed_scope

    source_episode_refs[]

    causal_basis_ref?

    applicability_conditions[]
    counter_conditions[]
    counterexamples[]

    evidence_refs[]

    confidence_assessment_ref

    proposed_maturity

    dependency_set_ref

    provenance_ref

    proposed_memory_category
}
```

**Non-loss requirement:** No automatic learning or disclosure

**Required verification:** Evidence, counterexamples, applicability, consent/provenance and approval path preserved

- Compare `FCA v1.0.1` (FCA v1.0.1 baseline) at `reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md:2237`

### MemoryRetrievalResult — `P6-02`

**Owner candidate:** `RDMS-07` · **Review risk:** `HIGH_PRIORITY` · **Gate:** `MAPPING_PROOF_PENDING`.
**Exact source:** `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt` line 1080; extracted block SHA-256 `e4ae715a27b230289f343447d8b7723501f62538065a5e61fa5dc5009c17c67d`.

```text
MemoryRetrievalResult {
    retrieval_id

    query_ref

    candidate_refs[]

    omitted_or_filtered_scope[]

    ranking_policy_ref

    retrieval_coverage

    freshness_summary

    created_at
}
```

**Non-loss requirement:** RDMS-07 retrieval coverage/ranking/filtering remains canonical. L7 MemoryRetrievalTransportResult is a bounded view with required canonical reference.

**Required verification:** Crosswalk proof pending

- Compare `RDMS-10` (Original draft) at `reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-10_APPROVED_SOURCE_SET.txt:1148`

**Publication guard:** No inferred fields, default values, status promotions, action permissions, or silent renames are authorized by this section.
<!-- GAIA-C01-PHASE9 CONTRACT PUBLICATION END -->


---

# L5 — Memory, Learning & Data Governance

> **CONSOLIDATION DRAFT — NOT FROZEN.** This file is a working per-layer consolidation, **not** an independently approved replacement for the frozen FCA/RDMS source specifications. Normative FCA source: `../reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md` (SHA-256 `74d0923cbd343b71740da0fc2368a84aad2ea97f8e4e15f156122f48ebe53539`). RDMS-01…10 original source sets arrived in GAIA-C01 Phase 4. Effective cross-source schemas and ownership remain **PENDING RECONCILIATION**; the archived original text below is untouched.

> **Phase 5:** source-name audit and non-normative proposals: `../reviews/GAIA_C01_PHASE5_CONTRACT_RECONCILIATION.md`. Original FCA and RDMS annexes below retain their historical authority/status; proposed aliases are not approved laws.

**Layer owner:** RDMS-07; Executive LearningGate and FCA memory semantics  
**Authoritative FCA trace:** FCA §§57–62, 77; content trust §72  
**Migration status:** CONSOLIDATED DRAFT / REVIEW REQUIRED  
**Source status:** FCA v1.0.1 hash-verified; RDMS source sets imported; effective contract reconciliation pending.

## 1. Scope and charter

L5 owns historical experience and governed promotion to reusable memory. Memory is not canonical world fact merely because it was retrieved.

## 2. Memory categories (FCA §57)

Working, Project Semantic, General Semantic, Episodic, Procedural, Decision, Failure/Anti-pattern, Project Lexicon and Temporal Commitments are conceptual categories; they need not map 1:1 to databases. Temporal control commitments remain legally owned by L4/RDMS-05, not duplicated as an independent scheduler in memory.

## 3. Capture and learning

Episodes may be stored as historical records. Semantic promotion follows `Episode → Reflection → MemoryProposal → Learning Gate → Executive authorization → Memory Store` (FCA §58 and §77). A single success is not an automatically universalizable rule.

## 4. MemoryProposal and maturity

FCA §60 proposes claim, scope, source episodes, applicability/counter conditions, counterexamples, evidence, confidence and maturity target; maturity runs `EPISODE → TASK_LESSON → PROJECT_LESSON → CANDIDATE_GENERALIZATION → CORROBORATED_SCHEMA` (FCA §59).

## 5. Retrieval

Memory retrieval supplies precedent/context, not current-world authorization or direct canonical claim promotion. Outputs carry provenance, applicability, dependency and restricted-use terms, particularly across projects.

## 6. Privacy / source lineage

Source documents, episodes, summaries, indexes, provider context and specialist outputs must carry applicable processing/disclosure restrictions. Restore from an old backup cannot reinstate permissions revoked later. Suppression must be applied before unauthorized processing or outbound disclosure.

## 7. Derived indexes

Caches and indexes are rebuildable views, not authority. Index absence is not proof of source absence when the index may be stale or incomplete. Recovery rebuild may not send restricted content to outside providers.

## 8. Promotion failure and recovery

Any promotion carrying jointly recovery-critical canonical metadata uses L1 control atomicity. If current policy/suppression frontier unavailable, do not assume a more permissive historical one.

## 9. Forbidden behaviors

No unapproved promotion; no treating retrieved memories as fact; no automatic global rules from one episode; no inter-project content leakage, and no post-restore unguarded provider export.


## 10. Dependency and interface register

- Reads trusted observations/experiences from L3, interpretations from L2.
- Uses L1 for promotion authority and durable canonical references.
- Provides bounded retrieval views to L2 and L7.
- Supplies suppression/lineage inputs to L6 recovery.

## 11. Pending effective-contract verification

- **PENDING EFFECTIVE CONTRACT AUDIT:** RDMS-07 exact memory kinds, promotion metadata, lineage, erasure and suppression contracts.
- **GAIA-R03:** verify current suppression and derivative lineage representation before certification.

## 12. Layer conformance requirements

A layer cannot be marked `FROZEN_CONSOLIDATED` until: (a) the owning legal contracts are imported from their frozen source version without loss; (b) all cross-layer projections are typed and referenced; (c) invariants, authority, failure and recovery paths are covered by normative acceptance scenarios; (d) source hashes and changes are recorded in `ARCHITECTURE_MANIFEST.md`; (e) the layer's review explicitly approves the consolidated text.

---

## GAIA-C01 Phase 5 — Memory Retrieval Identity (PROPOSED ONLY)

Canonical `MemoryRetrievalResult` belongs to RDMS-07 / L5, including query, retrieval ID, candidates, omitted/filtered scope, ranking policy, retrieval coverage and freshness. RDMS-10's differently shaped lightweight result should be designated `MemoryRetrievalTransportResult` in L7 after controlled review. It must not silently discard coverage/freshness or promote historical memories to current fact.


# SOURCE-PRESERVED FCA v1.0.1 BASELINE ANNEX

**Source authority:** the immutable `Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md` file in `reviews/source_archive/`. These copied sections are exact FCA source excerpts, not newly approved RDMS definitions. Layer prose above remains a consolidation draft pending full RDMS source validation.
**Source SHA-256:** `74d0923cbd343b71740da0fc2368a84aad2ea97f8e4e15f156122f48ebe53539`

**Ownership note:** This document embeds its assigned FCA source sections once. Do not redefine these names in a second layer; refer to the original owner or validated public projection.

<!-- GAIA-SOURCE FCA-SECTION 57 SHA256=3a826f90c55d75e1d35a8433d46e52b41f30f3d06c769b5102512706cbbf5213 -->
## 57. Memory categories

FCA conceptually distinguishes:

```text
Working Memory
Project Semantic Memory
General Semantic Memory
Episodic Memory
Procedural Memory
Decision Memory
Failure / Anti-pattern Experience
Project Lexicon
Temporal Commitments
```

These categories need not map one-to-one to physical databases.

---

<!-- GAIA-SOURCE FCA-SECTION 58 SHA256=d49d5f4c259bd911fc724782d0425036b5ff26f55accebf4f3c5976d2ad3ac35 -->
## 58. Episode vs learned knowledge

An episode is historical experience and MAY be captured automatically.

Learned knowledge is semantic promotion and requires governance.

```text
Episode
  ↓
Reflection
  ↓
MemoryProposal
  ↓
Learning Gate
  ↓
Executive authorization
  ↓
Memory Store
```

---

<!-- GAIA-SOURCE FCA-SECTION 59 SHA256=ef36d236edbe73fbaf0c2d53cdcd9c308b98804b3c642a1f0c0adda0f3241202 -->
## 59. Memory maturity

```text
EPISODE
↓
TASK_LESSON
↓
PROJECT_LESSON
↓
CANDIDATE_GENERALIZATION
↓
CORROBORATED_SCHEMA
```

A single successful event MUST NOT automatically become a general engineering rule.

---

<!-- GAIA-SOURCE FCA-SECTION 60 SHA256=3cf5efff268c8cbd604d294e913eaabddc3405a4a3d6828d92c6e1832021b245 -->
## 60. MemoryProposal

```text
MemoryProposal {
    claim

    proposed_scope

    source_episodes[]

    causal_basis?

    applicability_conditions[]
    counter_conditions[]
    counterexamples[]

    evidence_refs[]

    confidence_assessment

    maturity_target
}
```

---

<!-- GAIA-SOURCE FCA-SECTION 61 SHA256=38db207b7c2c1e7d7a4c2a9b167c78577be06a3a258c9835dedf82a68baf8935 -->
## 61. Memory metadata

```text
MemoryMetadata {
    scope:
        task
        project
        organization
        domain
        ecosystem
        general

    provenance[]

    applicability_conditions[]
    counter_conditions[]

    confidence_assessment

    stability:
        transient
        version_sensitive
        project_stable
        general_stable

    derived_from[]
    supersedes[]
}
```

Memory is fallible, scoped, versioned, and provenance-bearing.

---

<!-- GAIA-SOURCE FCA-SECTION 62 SHA256=a82fbd46f0b53f4ab8004d4d9e3710667fd559f7f0b2a0660026173ecaa3775e -->
## 62. Retrieval law

Retrieved memory enters current cognition as:

```text
precedent
analogy candidate
procedural suggestion
```

not as current Fact.

> **Experience → hypothesis / precedent, not authority.**

Transfer is based preferentially on structural and causal similarity, not surface textual similarity.

---

# Part XVII — Specialists and team cognition

<!-- GAIA-SOURCE FCA-SECTION 77 SHA256=88f0d216af63bc319baeca4d4ecc782c63031b84eb65aa105a702d0361400ce9 -->
## 77. Memory promotion

```text
Episode / Reflection
   ↓
MemoryProposal
   ↓
Learning Gate
   ↓
Executive authorization
   ↓
Memory commit
```

---


---

## RDMS Verbatim Source Annexes — Phase 4 (historical draft + corrections + freeze decision)

> **SOURCE PRESERVATION, NOT NORMALIZED LAW.** The following original user-supplied text is included **verbatim** as a migration input. Drafts and later corrections coexist historically. Later approved corrective parts and freeze decisions must govern disagreements. This annex does not itself certify exact schema compatibility or replace the original archive. Do not implement directly until semantic reconciliation is completed.

#
## GAIA-C01 Phase 6 — Memory retrieval return contract (NON-NORMATIVE)

- `MemoryRetrievalResult` belongs to RDMS-07 and preserves query identity, ranked candidates, filtered/omitted scope, retrieval coverage, freshness and creation time. RDMS-10's shorter same-name result is a presentation/transport projection, not replacement canonical truth.
- Proposed L7 alias: `MemoryRetrievalTransportResult` with required `canonical_memory_retrieval_result_ref`. Without resolvable canonical coverage/freshness, do not claim exhaustive search.
- See `../reviews/GAIA_C01_PHASE6_EFFECTIVE_CONTRACT_RESOLUTION.md`.

## Original source set: RDMS-07

Archive: `../reviews/source_archive/RDMS_ORIGINAL_SOURCES/RDMS-07_APPROVED_SOURCE_SET.txt`  
SHA-256 of complete source set: `fe065cda37c20625ac4c42c64251f87d4daabb9d5d466d49a8c201784d948700`  
Contained original message parts: 2

````text
RDMS-07 — ORIGINAL APPROVED SOURCE SET
Source: https://chatgpt.com/share/6ac82d7b-ba7c-83ea-a3a9-b41734948bb2

ملاحظة تحريرية: هذا الملف تجميع للنصوص الأصلية المسترجعة من المحادثة، لا إعادة صياغة ولا مواصفة موحدة جديدة. حالة التجميد مثبتة في قرار المراجعة النهائي المرفق؛ عبارة DRAFT داخل النص الأساسي تصف مرحلته التاريخية قبل التصحيحات. تُقرأ المسودة مع التصحيحات وقرار الاعتماد، ولا يجوز استعمال نص سابق يخالف تصحيحًا معتمدًا لاحقًا. لم نغير نصوص القوانين ولم نضف FCA.


========================================================================
SOURCE PART: Original draft
MESSAGE ID: 938c1bc7-97a0-46ad-be19-cd3ba3ca125f
BEGIN ORIGINAL MESSAGE
========================================================================

RDMS-07 — Memory, Learning, Experience & Knowledge Governance

وصلنا الآن إلى المرحلة السابعة من تصميم وكيلنا البرمجي.

بعد RDMS-06 أصبح لدينا تصميم يسمح للوكيل بتوزيع العمل على متخصصين، ومقارنة نتائجهم، والتحقق من صلاحية المعرفة بعد تغير المشروع.

لكن هناك قدرة أخرى ضرورية لمحاكاة المبرمج البشري المحترف:

أن يتعلم الوكيل من تجاربه السابقة، ويستفيد من أخطائه ونجاحاته، دون أن يكرر التحليل والعمل من الصفر في كل مشروع.

تخيل أن وكيلنا أمضى يومين في تشخيص خطأ معقد في نظام متعدد الخيوط، واكتشف أن المشكلة ناتجة عن Race Condition مرتبطة بترتيب تحديث الذاكرة.

بعد شهر، يعمل على مشروع مختلف ويواجه أعراضًا مشابهة.

لا نريده أن يبدأ من الصفر، ولا أن يفترض تلقائيًا أن السبب هو نفسه.

نريده أن يتذكر التجربة، ويستخرج منها فرضية مناسبة، ويختبر ما إذا كانت تنطبق على المشروع الجديد.

هذه هي الفلسفة التي سنبني عليها RDMS-07.

RDMS-07 — Memory, Learning, Experience & Knowledge Governance — Draft v1.0
Runtime & Data Model Specification v1.0
RDMS-07 — Memory, Learning, Experience & Knowledge Governance

Parent: FCA v1.0.1 — FROZEN
Dependencies: RDMS-01 → RDMS-06 — FROZEN
Status: DRAFT v1.0 — NOT FROZEN
Implementation: NOT AUTHORIZED
Next Gate: Adversarial Freeze Review 01

PART I — PURPOSE
1. Purpose

RDMS-07 تصمم ذاكرة الوكيل البرمجي وآليات اكتساب الخبرة منها.

يجب أن يستطيع النظام:

حفظ التجارب الهندسية التي مر بها.

تذكر القرارات وأسباب اتخاذها.

استرجاع حلول لمشكلات مشابهة.

استخراج دروس من النجاح والفشل.

التمييز بين تجربة منفردة وقاعدة عامة.

تحديث معرفة أصبحت غير صحيحة.

اكتشاف التناقض بين الخبرات.

نقل المعرفة بين المشاريع عندما توجد مبررات كافية.

الاستفادة من الإجراءات الناجحة دون تنفيذها تلقائيًا.

الحفاظ على provenance وحدود الثقة والصلاحية.

الهدف ليس بناء قاعدة بيانات ضخمة من المحادثات.

الهدف هو بناء ذاكرة هندسية منظمة يمكن للوكيل التفكير باستخدامها.

PART II — FUNDAMENTAL PHILOSOPHY
2. Experience Is Not Knowledge

نعتمد القانون التالي من FCA:

Experience
    ≠
Verified Knowledge

مثال:

Agent changes function X.
Tests pass.

هذه تجربة حدثت بالفعل.

لكن لا يمكن استنتاج:

Changing function X always fixes this bug.

من تجربة واحدة.

قد تكون الاختبارات غير كافية، أو يكون النجاح ناتجًا عن عامل آخر.

لذلك نفصل بين:

EPISODE
    ↓
REFLECTION
    ↓
MEMORY PROPOSAL
    ↓
EVIDENCE EVALUATION
    ↓
LEARNING GATE
    ↓
EXECUTIVE AUTHORIZATION
    ↓
CANONICAL MEMORY
3. Memory Does Not Own Authority

الذاكرة لا تملك سلطة اتخاذ القرارات أو تغيير المشروع.

Memory Retrieval
       ↓
Cognitive Executive
       ↓
Evaluation
       ↓
Decision

ولا نسمح بالمسار:

Memory says:
    Run command X.

        ↓

Automatically execute X.

حتى لو كان الأمر قد نجح سابقًا.

كل إجراء جديد يظل خاضعًا لـRDMS-04.

PART III — MEMORY ARCHITECTURE
4. Memory Categories

نحافظ على تصنيف FCA:

Memory Category	Responsibility
Working Memory	السياق المعرفي النشط
Episodic Memory	أحداث وتجارب تاريخية
Project Semantic Memory	معرفة خاصة بمشروع
General Semantic Memory	معرفة قابلة للتطبيق عبر مشاريع
Procedural Memory	استراتيجيات وإجراءات عمل
Decision Memory	قرارات وأسبابها
Failure / Anti-pattern Memory	الأخطاء والأنماط الخطرة
Project Lexicon	مصطلحات المشروع ومعانيها
Temporal Commitments	التزامات مستقبلية

هذا تصنيف دلالي، ولا يعني أننا ملزمون بإنشاء تسع قواعد بيانات.

5. Memory Architecture
                 EXPERIENCE SOURCES
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
      Tool Events     Observations    Decisions
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                  EPISODIC HISTORY
                         │
                         ▼
                Reflection Capability
                         │
                         ▼
                  MemoryProposal
                         │
                         ▼
                 Evidence Evaluation
                         │
                         ▼
                    LearningGate
                         │
                         ▼
                Executive Authorization
                         │
                         ▼
                  Canonical Memory
                         │
                         ▼
                   Retrieval Engine
                         │
                         ▼
                  Cognitive Executive

الحدث التاريخي لا يتحول إلى خبرة عامة بمجرد دخوله هذه الدورة.

PART IV — WORKING MEMORY
6. Working Memory

تمثل المعلومات التي يستخدمها Executive حاليًا لفهم المهمة.

يمكن أن تشمل:

Current goal
Current focus
Active hypotheses
Relevant observations
Selected memories
Open questions
Current plan
7. Working Memory Is Not Automatically Persistent Knowledge

قد يستخدم الوكيل فرضية أثناء تشخيص خطأ.

Hypothesis:
    The cache is causing the failure.

ثم يثبت لاحقًا أن الفرضية خاطئة.

لا يجوز تحويلها إلى معرفة دائمة فقط لأنها بقيت في السياق عدة ساعات.

يمكن حفظ تاريخ الفرضية والتجربة، لكن قبول معرفة مستخلصة منها يحتاج مسار التعلم.

8. Working Memory Recovery

استمرارية السياق بعد التوقف تعتمد على:

RDMS-05 ResumptionCapsule
+
Canonical Cognitive State
+
Relevant Memory References

RDMS-07 لا تنشئ آلية استئناف منافسة.

PART V — EPISODIC MEMORY
9. Engineering Episode

Episode تمثل تجربة تاريخية محددة.

EngineeringEpisode {
    episode_id

    project_id

    goal_ref?
    slice_ref?

    temporal_bounds

    source_event_refs[]

    action_refs[]
    observation_refs[]

    decision_refs[]
    verification_refs[]

    result_refs[]

    outcome_status

    provenance_ref

    created_commit_seq
}
10. What an Episode Records

مثال:

Project:
    Web Server A

Problem:
    Requests occasionally fail.

Hypothesis:
    Connection pool exhaustion.

Experiment:
    Increase pool capacity.

Observation:
    Failure rate decreases.

Verification:
    Targeted tests pass.

هذه البيانات تحفظ ما حدث وما رُصد.

لكنها لا تثبت تلقائيًا أن زيادة Connection Pool هي السبب الوحيد للتحسن.

11. Automatic Episode Capture

يجوز حفظ Episode تلقائيًا من أحداث معتمدة، دون موافقة دلالية منفصلة على كل حدث.

لكن هذا لا يمنح محتواها معنى Fact عام.

يجب أن تبقى الروابط واضحة إلى:

Actual ActionRecord
Actual Observation
Actual VerificationRecord
Actual Decision

ولا يُسمح لـLLM بإنشاء أحداث خارجية مزيفة عبر كتابة قصة تبدو كتجربة حقيقية.

12. Episode Immutability

الأحداث الأصلية لا تُعاد كتابتها لتوافق تفسيرًا لاحقًا.

إذا تغير فهمنا لتجربة:

Original Episode
       ↓
New Interpretation
       ↓
New Reflection

تبقى الأحداث التاريخية كما سُجلت، ضمن سياسات الاحتفاظ والخصوصية القانونية.

تصحيح provenance يتم عبر آليات RDMS-03، وليس عبر تغيير النتائج غير المرغوبة.

PART VI — REFLECTION
13. Reflection Capability

Reflection هي العملية التي يحلل بها الوكيل خبرته.

أسئلتها الأساسية:

What happened?

What was expected?

What actually happened?

Which hypothesis was supported?

Which hypothesis was rejected?

What caused the outcome?

What remains uncertain?

What could be reused?
14. ReflectionRecord
ReflectionRecord {
    reflection_id

    source_episode_refs[]

    analysis_context_ref

    successful_patterns[]

    failure_patterns[]

    causal_hypothesis_refs[]

    supported_conclusions[]

    rejected_explanations[]

    counterexamples[]

    unresolved_uncertainty[]

    candidate_lessons[]

    dependency_set_ref
}
15. Reflection Is an Interpretation

لا يجوز أن تصبح Reflection دليلًا مستقلًا عن Episodes التي استندت إليها.

مثال:

Episode A
    ↓
Reflection 1
Reflection 2
Reflection 3

هذه ليست ثلاث تجارب مستقلة.

يجب الحفاظ على Evidence Root Lineage وفق RDMS-03.

16. Reflection Cannot Manufacture Causality

إذا قال الوكيل:

After patch P, tests passed.

لا يستطيع تحويل ذلك تلقائيًا إلى:

Patch P caused the problem to disappear.

إنشاء OperationalCausalClaim يظل خاضعًا إلى Causal Closure Gate المجمدة في FCA.

Reflection تستطيع اقتراح تفسير سببي أو ربطه بادعاء سببي مقبول، لكنها لا تتجاوز تلك البوابة.

PART VII — MEMORY MATURITY
17. Memory Maturity Levels

نحافظ على سلم FCA:

EPISODE
   ↓
TASK_LESSON
   ↓
PROJECT_LESSON
   ↓
CANDIDATE_GENERALIZATION
   ↓
CORROBORATED_SCHEMA

هذا السلم يمثل اتساع النطاق ونضج الدعم المعرفي.

وليس عدادًا لعدد مرات تكرار جملة معينة.

18. EPISODE

تجربة تاريخية محددة.

قد تكون صحيحة الوصف لكنها محدودة في دلالتها.

19. TASK_LESSON

درس قابل للاستفادة داخل المهمة نفسها.

مثال:

For this test harness, reset the mock database
before running the integration test.
20. PROJECT_LESSON

درس يبدو صالحًا ضمن مشروع معين، مع شروط تطبيق واضحة.

مثال:

In Project A, service X requires configuration Y
when running integration tests.
21. CANDIDATE_GENERALIZATION

قاعدة مرشحة للتطبيق خارج سياقها الأصلي.

لم تصل بعد إلى دعم يسمح باعتبارها معرفة عامة مستقرة.

22. CORROBORATED_SCHEMA

نمط هندسي له دعم متنوع مناسب لنطاقه.

لكن:

CORROBORATED_SCHEMA

لا تعني صحة مطلقة أو صلاحية أبدية.

يظل لها:

Applicability conditions
Counterconditions
Counterexamples
Dependency validity
23. Maturity Promotion

الانتقال إلى مستوى أعلى يحتاج قرارًا جديدًا.

Memory M
    ↓
PromotionProposal
    ↓
Evidence & scope review
    ↓
LearningGate
    ↓
Executive authorization
    ↓
New accepted maturity

لا نحدد عدد تكرارات عالميًا يؤدي تلقائيًا إلى الترقية.

قد تكون عشر تجارب متكررة على النظام نفسه أضعف من تجربتين مستقلتين صُممتا لاختبار فرضيتين متعارضتين.

PART VIII — MEMORY PROPOSAL
24. MemoryProposal

نعتمد حقول FCA ونوسعها:

MemoryProposal {
    proposal_id

    claim

    proposed_scope

    source_episode_refs[]

    causal_basis_ref?

    applicability_conditions[]
    counter_conditions[]
    counterexamples[]

    evidence_refs[]

    confidence_assessment_ref

    proposed_maturity

    dependency_set_ref

    provenance_ref

    proposed_memory_category
}
25. Proposal Requirements

يجب أن تحدد MemoryProposal:

ما الادعاء المطلوب حفظه؟

ما نطاق تطبيقه؟

على أي أدلة يعتمد؟

متى قد لا يكون صحيحًا؟

هل توجد أمثلة مضادة؟

ما مستوى النضج المطلوب؟

ما الاعتماديات التي يمكن أن تبطل صلاحيته؟

الذاكرة التي لا تحدد نطاقها معرضة للتحول إلى تعميم مضلل.

PART IX — LEARNING GATE
26. LearningGate

تمنع البوابة تحويل الاستنتاجات غير المؤهلة إلى معرفة معتمدة.

LearningGateEvaluation {
    evaluation_id

    memory_proposal_ref

    provenance_validity

    evidence_usability

    scope_adequacy

    causal_basis_status

    counterexample_review

    dependency_evaluation_ref

    maturity_eligibility

    trust_boundary_validation

    hard_invariant_compliance

    result:
        ELIGIBLE
        REVISE
        BLOCKED
        INSUFFICIENT_EVIDENCE
}
27. Gate Authority

البوابة تتحقق من الشروط البنيوية والقانونية ومن توفر متطلبات الدليل.

لكن:

LearningGate = ELIGIBLE

لا تعني:

Memory accepted.

يظل القبول الدلالي بيد Executive.

كما لا تستطيع Executive جعل Memory مخالفة لقانون مجمد قانونية.

28. Canonical Memory Commit
MemoryProposal
      ↓
LearningGate
      ↓
Executive semantic authorization
      ↓
CommitGate
      ↓
ControlCommit
      ↓
Canonical Memory State

جميع معلومات الإصدار والـprovenance اللازمة للتعافي تدخل السلطة المعتمدة لـRDMS-01.

PART X — CANONICAL MEMORY
29. MemoryRecord
MemoryRecord {
    memory_id

    memory_category

    claim_or_procedure_ref

    scope

    maturity

    applicability_conditions[]
    counter_conditions[]

    evidence_basis_refs[]

    provenance_refs[]

    dependency_set_ref

    confidence_assessment_ref

    stability

    version

    lifecycle

    derived_from[]
    supersedes[]

    created_commit_seq
    updated_commit_seq
}
30. Memory Lifecycle

نقترح:

CANDIDATE
    ↓
ACTIVE
    ↓
SUPERSEDED

مع مسارات أخرى:

ACTIVE → DISPUTED
ACTIVE → STALE
ACTIVE → RETIRED

هذه حالات مقترحة لسياسة الذاكرة، وليست بديلًا عن حالة صلاحية الاعتماديات.

يجب الفصل بين:

حالة قبول Memory.

صلاحية اعتمادياتها الحالية.

وجود أدلة متناقضة.

قابلية استرجاعها للاستعمال.

31. Memory Versioning

لا نغير مضمون Memory معتمدة بصمت.

إذا تغيرت القاعدة:

Memory v1
    ↓
Revision proposal
    ↓
Memory v2

مع:

supersedes = v1

هذا يسمح للوكيل بفهم كيف تطورت خبرته.

32. Historical Memory vs Current Guidance

يمكن إبقاء Memory قديمة متاحة للتفسير التاريخي.

لكن لا يجوز تقديمها بوصفها توصية حالية إذا فقدت صلاحيتها.

نفرق بين:

HISTORICAL_RETRIEVAL

و:

CURRENT_APPLICABILITY_CANDIDATE

ويسمح الأول بفهم القرارات السابقة دون اعتبارها مناسبة تلقائيًا اليوم.

PART XI — PROJECT SEMANTIC MEMORY
33. Project Memory

تحفظ المعرفة المتعلقة بمشروع معين.

أمثلة:

Repository architecture
Module ownership
Internal conventions
Verified interfaces
Known architectural constraints
Accepted technical decisions
34. Project Scope
ProjectMemoryScope {
    project_id

    repository_ref?

    relevant_component_refs[]

    environment_ref?

    applicable_version_range?

    authority_context_ref?
}

لا يجوز نقل معرفة Project A إلى Project B وكأنهما نظام واحد.

35. Repository Is Not Replaced by Memory

إذا حفظت الذاكرة:

Module X implements interface Y.

ثم تغيرت repository، لا نستعمل العبارة القديمة كدليل على الحالة الحالية.

يجب التحقق من الاعتماديات باستخدام RDMS-06.

PART XII — GENERAL SEMANTIC MEMORY
36. General Memory

تمثل قواعد أو أنماطًا هندسية تتجاوز مشروعًا واحدًا.

لكنها لا تنشأ تلقائيًا من نجاح محلي.

مثال مرشح:

Concurrent writes to shared mutable state may
require synchronization or other correctness controls.

هذا مثال على معرفة عامة يمكن أن تكون لها تطبيقات واسعة.

أما تفاصيل أسلوب إصلاح المشكلة في مشروع معين فقد لا تصلح للتعميم.

37. GeneralizationProposal
GeneralizationProposal {
    proposal_id

    candidate_memory_refs[]

    source_project_scopes[]

    common_structure

    proposed_general_rule

    applicability_conditions[]

    known_counterexamples[]

    independent_support_analysis_ref

    proposed_target_scope

    residual_uncertainty
}
38. Generalization Limits

عندما تستخدم عدة مشاريع المكتبة نفسها والإعدادات نفسها، لا نفترض أنها توفر دعمًا مستقلاً بالكامل.

نحتاج تحديد الجذور المشتركة والاختلافات ذات الصلة.

PART XIII — PROCEDURAL MEMORY
39. Procedural Knowledge

تمثل معرفة الوكيل بكيفية أداء عمل هندسي.

مثال:

When diagnosing an intermittent concurrency bug:

1. Identify shared mutable state.
2. Reproduce the failure under controlled conditions.
3. Examine interleavings.
4. Form competing causal hypotheses.
5. Test targeted interventions.

هذا إجراء استدلالي يمكن أن يكون مفيدًا في مهام متعددة.

40. ProcedureMemory
ProcedureMemory {
    procedure_id

    objective

    applicability_conditions[]

    prerequisites[]

    ordered_steps[]

    branching_conditions[]

    required_tools[]

    expected_intermediate_observations[]

    termination_conditions[]

    failure_handling[]

    safety_constraints[]

    verification_requirements[]

    evidence_refs[]

    dependency_set_ref
}
41. Procedures Are Suggestions

لا يجوز أن تتحول ProcedureMemory إلى سلطة تنفيذ.

Retrieve procedure
       ↓
Evaluate applicability
       ↓
Build current plan
       ↓
Executive authorization
       ↓
Legal Action Runtime

إذا كانت الخطوة المخزنة تتطلب حذف قاعدة بيانات، فإن استرجاعها لا يجعل الحذف مسموحًا.

42. Procedure Adaptation

قد تحتاج Procedure ناجحة سابقًا إلى تعديل بسبب:

Operating system differences
Different toolchain
New library versions
Different repository structure
Different security requirements

أي تعديل مادي على الإجراء يجب أن يكون واضحًا داخل خطة المهمة الحالية.

لا نسمح بالتنفيذ الأعمى لتسلسل أوامر محفوظ.

PART XIV — DECISION MEMORY
43. Decision Memory

تختلف عن حفظ النتيجة فقط.

المهم أن يعرف الوكيل:

What was decided?
Why?
What alternatives were considered?
What evidence supported the decision?
What assumptions were made?
What would cause reconsideration?
44. DecisionMemory
DecisionMemory {
    memory_id

    canonical_decision_ref

    decision_context_ref

    accepted_option_ref

    rejected_alternatives[]

    rationale_refs[]

    supporting_evidence_refs[]

    assumptions[]

    reconsideration_conditions[]

    applicability_scope

    dependency_set_ref
}
45. Decision History

إذا قرر فريق هندسي استخدام PostgreSQL ثم استبدلها لاحقًا بنظام آخر، يجب أن يستطيع الوكيل معرفة سبب القرار القديم وسبب العدول عنه.

لكن DecisionMemory التاريخية لا تستبدل Decision الحالية المخزنة في Canonical Workspace.

PART XV — FAILURE & ANTI-PATTERN MEMORY
46. Failure Memory

الفشل مصدر مهم للتعلم.

ليس كل فشل دليلًا على أن الفكرة نفسها خاطئة؛ فقد يكون السبب:

Incorrect implementation
Insufficient resources
Invalid assumptions
Wrong environment
Broken test harness
47. FailurePattern
FailurePattern {
    failure_pattern_id

    observed_symptoms[]

    affected_contexts[]

    supported_causes[]

    unresolved_causes[]

    known_bad_approaches[]

    verified_counterexamples[]

    mitigation_options[]

    applicability_conditions[]

    evidence_basis_refs[]

    maturity
}
48. Avoid Overgeneralizing Failure

إذا فشلت مكتبة في مشروع معين، لا يجوز استنتاج:

Never use this library.

دون تحديد الظروف والإصدارات والأسباب.

قد يكون الدرس الصحيح:

Version X failed under configuration Y
because of condition Z.
PART XVI — PROJECT LEXICON
49. Project Lexicon

تحتاج المشاريع الكبيرة إلى ذاكرة خاصة بالمصطلحات والاختصارات.

مثال:

"ActionRecord"
"CommitGate"
"Slice"
"DependencyStamp"
50. LexiconEntry
LexiconEntry {
    term

    project_scope

    definition_ref

    authoritative_spec_ref?

    aliases[]

    related_concept_refs[]

    version
}
51. Lexicon Does Not Redefine Architecture

إذا تغير معنى مصطلح في مواصفة مجمدة، لا يجوز تحديث Lexicon فقط لإخفاء هذا التغيير.

المواصفة القانونية تظل المرجع.

وتخضع التعديلات الدلالية إلى آلية revision المناسبة.

PART XVII — TEMPORAL COMMITMENTS
52. Commitment Memory Boundary

Temporal Commitments موجودة ضمن تصنيف ذاكرة FCA.

لكن lifecycle والتفعيل الزمني يقعان تحت RDMS-05.

RDMS-07 يمكنها استرجاع:

Why was this commitment created?

Which decision created it?

What historical experience motivated it?

لكنها لا تنشئ Scheduler ثانية.

ولا تعيد تسليح Trigger بسبب استرجاع ذاكرة قديمة.

PART XVIII — MEMORY RETRIEVAL
53. Retrieval Philosophy

الاسترجاع ليس عملية إحضار نص مشابه فقط.

نريد استرجاع الخبرة المناسبة للمشكلة الحالية.

يجب مراعاة:

Structural similarity
Causal relevance
Problem characteristics
Environment compatibility
Applicability conditions
Evidence quality
Dependency freshness
Known counterexamples
54. MemoryQuery
MemoryQuery {
    query_id

    requesting_goal_ref

    problem_context_ref

    requested_memory_categories[]

    allowed_memory_scopes[]

    structural_features[]

    causal_features[]

    environment_constraints[]

    retrieval_budget

    sensitivity_policy_ref
}
55. RetrievalCandidate
RetrievalCandidate {
    candidate_id

    memory_ref

    query_ref

    relevance_assessment

    applicability_assessment

    dependency_evaluation_ref

    evidence_basis_refs[]

    known_limitations[]

    retrieval_role:
        PRECEDENT
        ANALOGY_CANDIDATE
        PROCEDURAL_SUGGESTION
        HISTORICAL_CONTEXT
}
56. Retrieval Is Not Truth Promotion

نتيجة الاسترجاع:

This memory resembles the current problem.

لا تساوي:

This memory proves the current diagnosis.

يمكن أن تقترح الذاكرة فرضية يجب اختبارها.

ولا يسمح أن تتحول معرفة محفوظة عن مشروع قديم إلى Fact عن مشروع جديد بلا Observation مناسبة.

57. RetrievalResult
MemoryRetrievalResult {
    retrieval_id

    query_ref

    candidate_refs[]

    omitted_or_filtered_scope[]

    ranking_policy_ref

    retrieval_coverage

    freshness_summary

    created_at
}

إذا كان الاسترجاع غير شامل، يجب ألا يستنتج النظام عدم وجود معرفة أخرى لمجرد أن البحث لم يجدها ضمن الميزانية.

PART XIX — CROSS-PROJECT TRANSFER
58. Knowledge Transfer

قد يتعلم الوكيل من مشروع A ما يساعده في مشروع B.

لكن النقل يحتاج تقييمًا مستقلًا.

Project A Experience
        ↓
Transfer Candidate
        ↓
Structural/Causal Comparison
        ↓
Applicability Review
        ↓
Executive Acceptance for Current Task
59. TransferAssessment
TransferAssessment {
    assessment_id

    source_memory_ref

    target_project_ref

    structural_correspondence

    causal_correspondence

    environment_compatibility

    required_assumptions[]

    conflicting_conditions[]

    transfer_risks[]

    result:
        APPLICABLE_CANDIDATE
        INAPPLICABLE
        UNCERTAIN
}
60. Scope and Confidentiality

نقل الخبرة لا يعني نقل كل بيانات المشروع الأصلي.

قد تحتوي Memory على:

Private source code
Secrets
Credentials
Internal architecture
Customer information
Confidential decisions

يمكن أن يكون الدرس العام صالحًا للنقل دون السماح بكشف تفاصيل المصدر.

لذلك نحتاج فصل:

Knowledge applicability

عن:

Information disclosure permission

وكل انتقال عبر حدود المشاريع أو المؤسسات يخضع لسياسة مشاركة البيانات.

PART XX — CONTRADICTIONS & BELIEF REVISION
61. Memory Contradiction

قد تتعارض ذاكرة قديمة مع Observation جديدة.

مثال:

Memory:
    Library X version 2 does not support feature F.

New Observation:
    Feature F works in version 2.4.

لا نمحو الذاكرة القديمة فورًا.

نحتاج فحص:

Exact version
Configuration
Environment
Claim scope
Evidence provenance

قد يكون التناقض ظاهريًا بسبب اختلاف النطاق.

62. MemoryConflictRecord
MemoryConflictRecord {
    conflict_id

    memory_refs[]

    contradicting_evidence_refs[]

    overlap_scope

    conflict_kind:
        DIRECT_CONTRADICTION
        SCOPE_MISMATCH
        TEMPORAL_MISMATCH
        INSUFFICIENT_EVIDENCE
        UNRESOLVED

    resolution_status
}
63. Contradiction Does Not Mean Automatic Deletion

إذا كانت لدينا أدلة متعارضة، تبقى معروفة ومحفوظة.

لا تُستبدل الأدلة السابقة بناءً على ترتيب وصولها فقط.

يحتاج حل التناقض إلى مراجعة scope والدليل والاعتماديات والسلطة.

64. Memory Revision
Existing Memory
       ↓
New Evidence / Contradiction
       ↓
RevisionProposal
       ↓
Evidence and Dependency Review
       ↓
LearningGate
       ↓
Executive Authorization
       ↓
New Memory Version / Retirement
PART XXI — STALENESS & MEMORY VALIDITY
65. Memory Dependency Evaluation

كل Memory ذات صلاحية قابلة للتغير ترتبط باعتمادياتها.

Memory
    ↓
DependencySet
    ↓
RDMS-06 Evaluation Engine

لا ننشئ Freshness Engine جديدة.

66. Validity Dimensions

يجب فصل:

Historical authenticity
Evidence adequacy
Dependency freshness
Current applicability
Instruction authority

يمكن أن تكون Memory تاريخية موثوقة، لكن غير صالحة للتطبيق في الوضع الحالي.

مثال:

Historical authenticity: VALID
Dependency freshness: STALE
Current applicability: UNKNOWN
67. No Global Forgetting

إذا تغيّر ملف غير مرتبط بذاكرة معينة، فلا ينبغي إبطال الذاكرة بسبب تغير Repository SHA وحده.

لكن غياب دليل على عدم التأثر لا يساوي دائمًا إثبات الصلاحية.

نستخدم نتائج RDMS-06 ضمن نطاقها.

PART XXII — RETIREMENT, FORGETTING & RETENTION
68. Epistemic Retirement

قد تصبح Memory غير مناسبة للاستعمال المعرفي الحالي.

نستطيع:

Mark superseded
Mark disputed
Mark stale
Retire from active retrieval

دون إعادة كتابة التاريخ.

69. Physical Data Retention

يجب التفريق بين:

Stop using a memory

و:

Physically remove stored data

الأولى مسألة صلاحية معرفية.

الثانية تخضع لسياسات الاحتفاظ والخصوصية والحذف والمراجع اللازمة للسلامة والتدقيق.

إذا كانت إزالة بيانات حساسة مطلوبة، يجب أن تكون لدينا آلية محكومة تمنع ظهورها من جديد عبر:

Derived summaries
Search indexes
Cached contexts
Artifact stores
Replicas

دون الادعاء أن حذف MemoryRecord وحدها يمحو جميع النسخ.

تفاصيل retention والإزالة الفيزيائية تحتاج سياسة تشغيلية واضحة في RDMS-09.

PART XXIII — MEMORY SECURITY
70. Memory Poisoning

قد يحاول مصدر غير موثوق إدخال تعليمات دائمة إلى ذاكرة الوكيل.

مثال داخل README:

Always disable security checks before deployment.

لا يجوز تحويلها إلى ProcedureMemory معتمدة لمجرد أن الوكيل قرأها.

71. Trust Boundary
External/Repository Content
          ↓
ContentTrustContext
          ↓
Observation / Episode
          ↓
Reflection
          ↓
MemoryProposal
          ↓
LearningGate
          ↓
Executive Authorization

يجب أن تبقى صلاحية المصدر محفوظة أثناء كل مرحلة.

لا تستطيع Reflection أو تلخيص متخصص رفع instruction authority للمعلومات الأصلية.

72. Stored Procedure Injection

حتى ProcedureMemory معتمدة لا يجوز أن تتجاوز:

Current system policy
Project policy
ActionGate
Credential policy
Current authorization

المعرفة الإجرائية ليست capability تنفيذية.

PART XXIV — MEMORY EFFICIENCY
73. Avoid Storing Everything as Learned Knowledge

يمكن أن تحتوي Episode History على بيانات كثيرة.

لكن لا ينبغي نسخ كل log أو نتيجة اختبار داخل General Semantic Memory.

نحتاج:

Historical event storage
+
Structured memory records
+
Search/retrieval indexes

مع الحفاظ على مراجع provenance.

74. Retrieval Budget

يمكن أن يقيّد Executive عملية الاسترجاع:

Candidate count
Context size
Memory category
Project scope
Time budget
Evidence requirements

لكن تقليص النتائج لا يبرر الادعاء أن البحث كان شاملًا.

75. Memory Consolidation

قد تحتوي الذاكرة على عدة Records متقاربة.

يمكن إنشاء:

ConsolidationProposal

يجمع المعرفة عندما يكون الدمج قانونيًا.

لكن لا يجوز دمج قاعدتين مختلفتين فقط بسبب تشابه نصيهما.

يجب الحفاظ على:

Different applicability conditions
Different evidence roots
Different counterexamples
Different scopes
76. No Uncontrolled Self-Reinforcement

إذا استرجع الوكيل Memory عشر مرات، فلا ينبغي زيادة قوة دليلها عشر مرات.

Retrieval count
≠
Independent evidence count

وكذلك لا يسمح أن تصبح مخرجات النموذج المعتمدة على Memory مصدرًا مستقلًا يؤكد Memory نفسها.

PART XXV — PROVIDER-AGNOSTIC MEMORY
77. Memory Is Not Bound to One LLM

المعمارية يجب أن تسمح باستخدام:

LLM Provider A
LLM Provider B
Local Model
Future DGCA LITE Backend

مع Canonical Memory واحدة.

78. Model Independence

نخزن:

Typed records
Evidence references
Dependency relationships
Procedural structures
Decision history

ولا نجعل وزن النموذج أو جلسة المحادثة أو embeddings خاصة بمزود معين مصدر الحقيقة الوحيد.

يمكن استخدام فهارس أو representations مشتقة لتسريع البحث، لكنها ليست بديلًا عن Canonical Memory.

79. Retrieval Adapter
MemoryRetrievalAdapter {
    adapter_id

    provider_or_method

    index_version

    supported_query_types[]

    ranking_policy_ref

    result_provenance_policy

    completeness_limitations[]
}

يمكن تغيير RetrievalAdapter دون إعادة تعريف معنى MemoryRecord.

PART XXVI — FAILURE & RECOVERY
80. Crash During Memory Promotion

إذا وقع crash أثناء:

MemoryProposal
    ↓
LearningGate
    ↓
Executive Authorization
    ↓
CommitGate

لا يجوز إنشاء Memory مرتين أو اعتبارها معتمدة قبل اكتمال ControlCommit.

81. Promotion Idempotency
MemoryPromotionIdentity {
    proposal_ref

    target_memory_identity

    target_revision

    promotion_decision_ref
}

تُستخدم هوية مستقرة لمنع التكرار العرضي.

ولا تمنع هذه الهوية إنشاء revision جديدة مقصودة بعد وصول أدلة جديدة.

82. Recovery
Restore Canonical Control State
        ↓
Inspect unfinished Memory Promotions
        ↓
Validate stored artifacts
        ↓
Restore Memory lifecycle
        ↓
Rebuild derived retrieval indexes if required
        ↓
Reconcile dependency freshness
        ↓
Resume authorized learning work

لا تعتبر فهارس الاسترجاع مصدر حقيقة مستقلًا إذا اختلفت مع Canonical Memory.

PART XXVII — CROSS-RDMS INTEGRATION
83. RDMS-01

Memory commits والانتقالات القانونية تستعمل Canonical ControlCommit.

84. RDMS-02

Memory ترتبط بهويات Goals وDecisions وClaims وProjects، ولا تعيد تعريفها.

85. RDMS-03

Observation وEvidence وOperationalCausalClaim تخضع لقواعد provenance والتفسير والسببية المجمدة.

86. RDMS-04

ProcedureMemory لا تنفذ العالم مباشرة.

كل Action جديدة تخضع لبوابات التنفيذ القانونية.

87. RDMS-05

Temporal Commitments وآليات الاستئناف تحتفظ بسلطتها الزمنية.

88. RDMS-06

Dependency Evaluation Engine تحدد freshness، وSpecialist Results لا تُرقّى إلى ذاكرة تلقائيًا.

PART XXVIII — PROPOSED INVARIANTS
RDMS07-I01
Historical experience and accepted semantic knowledge are
distinct.

RDMS07-I02
Episode capture cannot automatically create general knowledge.

RDMS07-I03
Memory promotion requires LearningGate and Executive authority.

RDMS07-I04
LearningGate eligibility does not itself constitute acceptance.

RDMS07-I05
Memory records preserve scope, provenance and evidence basis.

RDMS07-I06
Memory maturity cannot increase solely through repetition count.

RDMS07-I07
Repeated interpretations of one evidence root cannot manufacture
independent corroboration.

RDMS07-I08
Reflection cannot manufacture causal closure.

RDMS07-I09
Historical events are not silently rewritten to match later
interpretations.

RDMS07-I10
Canonical memory revisions preserve explicit lineage.

RDMS07-I11
Retrieved memory enters cognition as precedent, analogy candidate
or procedural suggestion, not current Fact.

RDMS07-I12
Procedural memory cannot bypass ActionGate.

RDMS07-I13
Project-specific memory cannot silently become general knowledge.

RDMS07-I14
Cross-project transfer requires applicability and disclosure
governance.

RDMS07-I15
Memory contradiction does not automatically delete either
supporting observation.

RDMS07-I16
Memory dependency freshness uses RDMS-06.

RDMS07-I17
Historical authenticity, evidence adequacy, freshness and current
applicability remain distinct.

RDMS07-I18
A stale memory cannot be presented as currently applicable
without qualified revalidation.

RDMS07-I19
Negative retrieval results cannot imply universal memory absence
without sufficient coverage.

RDMS07-I20
Memory content cannot self-assign instruction authority.

RDMS07-I21
Untrusted content cannot acquire higher authority through
summarization, reflection or consolidation.

RDMS07-I22
Memory retrieval cannot strengthen its own evidence basis merely
through repeated use.

RDMS07-I23
Memory indexes are derived structures, not independent canonical
sources of truth.

RDMS07-I24
Memory correctness cannot rely exclusively on one LLM provider's
hidden state.

RDMS07-I25
Memory promotion and revision must be recoverably idempotent.

RDMS07-I26
A historical decision memory cannot replace the currently
authoritative Decision.

RDMS07-I27
Physical data deletion and epistemic retirement require distinct
governance.

RDMS07-I28
Confidence assessments cannot substitute for evidence or
authorized semantic acceptance.

RDMS07-I29
Partial memory reuse must retain the applicability conditions
and counterexamples relevant to the reused content.

RDMS07-I30
A memory derived from multiple agents or reflections must preserve
its underlying independent evidence roots.
PART XXIX — EXAMPLE SCENARIOS
Scenario A — Learning From a Debugging Failure
Agent investigates intermittent failure.
        ↓
Tests several hypotheses.
        ↓
First hypothesis rejected.
        ↓
Second hypothesis supported.
        ↓
Targeted intervention succeeds.
        ↓
Verification completed.
        ↓
Episode recorded.
        ↓
Reflection proposes task lesson.
        ↓
LearningGate review.
        ↓
Executive authorizes memory.

النتيجة معرفة محددة النطاق، لا قاعدة عامة عن كل أنظمة البرمجة.

Scenario B — Reusing an Old Solution
Project B encounters concurrency bug.
        ↓
Memory Retrieval finds similar Project A episode.
        ↓
TransferAssessment compares structures.
        ↓
Executive forms candidate hypothesis.
        ↓
Targeted experiment.
        ↓
Current verification.
        ↓
Current decision.

لا ينفذ الوكيل الحل القديم دون اختبار قابليته للتطبيق.

Scenario C — Old Memory Becomes Stale
Memory:
    Library X version 3 requires workaround W.

New dependency:
    Library X version 4.

Dependency Evaluation:
    Memory applicability UNKNOWN / STALE.

Executive:
    Reinvestigate before reusing W.

تبقى التجربة التاريخية محفوظة، لكن لا تُستخدم باعتبارها تعليمات حالية.

Scenario D — Multiple Agents Repeat One Error
Specialist A:
    Claim X.

Specialist B:
    Claim X.

Specialist C:
    Claim X.

All three rely on the same incorrect source.

لا تؤدي كثرة التقارير إلى تحويل X إلى حقيقة.

يجب فحص Evidence Origins والتناقضات.

Scenario E — Project-Specific Knowledge Leakage
Project A:
    Contains confidential internal architecture.

Project B:
    Similar engineering problem.

يمكن اقتراح درس مجرد إذا سمحت سياسة المعلومات بذلك، دون كشف كود أو بيانات Project A.

PART XXX — ADVERSARIAL REVIEW TARGETS

قبل تجميد RDMS-07 يجب مهاجمة 36 سيناريو:

Experience & Evidence

Episode تتضمن Observation مزيفة.

Reflection تنشئ دليلًا مستقلًا من حدث واحد.

نجاح اختبار واحد يتحول إلى General Schema.

MemoryProposal تستعمل Evidence لا تدعم Claim.

MemoryPromotion تتجاوز Causal Closure Gate.

تكرار استرجاع Memory يرفع confidence دون دليل جديد.

Learning Authority

Specialist تحاول ترقية Memory مباشرة.

LLM تعلن LearningGate PASS دون سلطة.

Executive تحاول اعتماد Memory تخالف Hard Invariant.

Crash بين موافقة Executive وMemory Commit.

إعادة تشغيل تؤدي إلى MemoryPromotion مكررة.

تغيير MemoryProposal بعد اجتياز LearningGate.

Scope & Transfer

Project Memory تنتقل إلى General Memory تلقائيًا.

نقل قاعدة لا تنطبق على البيئة الجديدة.

كشف معلومات سرية عبر Cross-project transfer.

تشابه نصي يخفي اختلافًا سببيًا.

Procedure قديمة تنفذ أمرًا خطيرًا.

Memory عن إصدار سابق تستخدم مع إصدار جديد.

Contradiction & Revision

Observation جديدة تناقض Memory معتمدة.

تعارض ظاهري سببه اختلاف Scope.

Memory v2 تحذف Counterexample موجودة في v1.

Retired Memory تظهر كتوصية حالية.

Derived Memory تستمر رغم بطلان مصدرها.

قرار قديم يُستخدم بدل Decision الحالية.

Retrieval & Performance

Search index ناقصة تنتج استنتاجًا بعدم وجود معرفة.

Ranking يفضل Memory عالية التشابه لكنها stale.

ذاكرة منخفضة الثقة تطغى على Evidence حديثة.

Consolidation تدمج قاعدتين غير متوافقتين.

Memory retrieval تستهلك السياق وتخفي قيودًا مهمة.

Derived index تختلف عن Canonical Memory.

Security & Privacy

Prompt injection داخل Episode.

ProcedureMemory تحتوي تعليمات تتجاوز ActionGate.

تلخيص Specialist يرفع سلطة محتوى غير موثوق.

حذف Memory حساسة يترك نسخًا داخل indexes/artifacts.

نقل خبرة بين مشاريع يخرق AccessPolicy.

تغير LLM Provider يؤدي إلى إعادة تفسير Memory canonical بصورة مختلفة.

FINAL DRAFT VERDICT
Episodic memory                 DEFINED
Reflection                      DEFINED
Memory maturity                 DEFINED
Memory proposals                DEFINED
LearningGate                    DEFINED
Canonical memory                DEFINED
Project/general memory          DEFINED
Procedural memory               DEFINED
Decision memory                 DEFINED
Failure patterns                DEFINED
Project lexicon                 DEFINED
Memory retrieval                DEFINED
Cross-project transfer          DEFINED
Contradiction and revision      DEFINED
Dependency freshness            DEFINED
Provider independence           DEFINED
Recovery                        DEFINED

Adversarial Freeze Review       PENDING
Implementation                  NOT AUTHORIZED

RDMS-07 DRAFT v1.0 — COMPLETE FOR ADVERSARIAL REVIEW.

Next authorized step: RDMS-07 — Adversarial Freeze Review 01.

أهم قرار هندسي في RDMS-07

أريد التأكيد على نقطة ستحدد طبيعة وكيلنا على المدى الطويل.

هناك فرق بين نظام يتذكر الحلول ونظام يتعلم من الخبرة.

الأول يستطيع البحث عن إصلاح سابق وإعادة اقتراحه.

أما الثاني فيستطيع أن يتذكر لماذا نجح الإصلاح، ومتى فشل، وما الشروط التي جعلته مناسبًا، وأي أجزاء من التجربة يمكن نقلها إلى مشكلات أخرى.

هذا هو المستوى الذي نستهدفه، لكن الوصول إليه سيعتمد على قوة الأدلة والتجارب والاستدلال السببي، وليس مجرد زيادة حجم قاعدة الذاكرة.

كذلك سنحافظ على استقلال الذاكرة عن نموذج اللغة المستخدم، حتى نستطيع تغيير الـLLM لاحقًا أو استخدام DGCA LITE دون فقدان التاريخ المعرفي المنظم للمشروع.

حالة المشروع
Specification	Status
FCA v1.0.1	✅ FROZEN
RDMS-01 → RDMS-06	✅ FROZEN
RDMS-07	🟡 DRAFT v1.0
RDMS-08 → RDMS-10	⏳ PENDING

الخطوة التالية: الهجوم العدائي الأول على RDMS-07، وخاصة Memory Poisoning، والتعميم غير الصحيح، وتحويل التجارب إلى ادعاءات سببية، والتناقض بين المعرفة القديمة والأدلة الجديدة.

END ORIGINAL MESSAGE

========================================================================
SOURCE PART: C01 and Adversarial Freeze Review 02 with freeze decision
MESSAGE ID: 5ee62ad7-b67d-4382-be9d-cd85f6331a8c
BEGIN ORIGINAL MESSAGE
========================================================================

ممتاز. سنحافظ على منهجيتنا دون تغيير:

التصميم → الهجوم العدائي → التصحيح → إعادة الهجوم → التجميد.

وصلنا إلى RDMS-07، وقد كشفت المراجعة الأولى عن 21 ثغرة معمارية و7 نقاط تحسين.

سننجز الآن مرحلتين بالترتيب:

RDMS-07 C01: إغلاق الثغرات وتثبيت العقود الرياضية والمنطقية والتشغيلية.

Adversarial Freeze Review 02: محاولة كسر التصميم المصحح، ثم اتخاذ قرار التجميد.

سأركز خصوصًا على ضمان ألا يستطيع الوكيل صناعة أدلة من ذاكرته، أو تحويل تجربة محدودة إلى قاعدة عامة، أو استخدام معرفة قديمة لإصدار قرارات خطيرة.

RDMS-07 C01 — Memory Integrity, Learning Authority & Knowledge Evolution Closure
RDMS-07 C01
Memory Integrity, Learning Authority & Knowledge Evolution Closure

Parent: RDMS-07 Draft v1.0
Review Source: FR07-G01…G21 / FR07-H01…H07
Dependencies: FCA v1.0.1 and RDMS-01…06 — FROZEN
Status: CORRECTED SPECIFICATION — READY FOR FREEZE REVIEW 02
Implementation: NOT AUTHORIZED

PART I — ARCHITECTURAL CONSERVATION
1. Canonical Learning Architecture

نحافظ على سلسلة التعلم الأساسية:

Engineering Experience
         │
         ▼
   Episode Capture
         │
         ▼
    Reflection
         │
         ▼
   MemoryProposal
         │
         ▼
 Evidence Evaluation
         │
         ▼
    LearningGate
         │
         ▼
Cognitive Executive
         │
         ▼
     CommitGate
         │
         ▼
  Canonical Memory

لا نسمح بإنشاء مسارات مختصرة تمنح LLM أو Specialist أو Retrieval Engine صلاحية إنشاء معرفة معتمدة مباشرة.

القواعد الأساسية:

Episode تمثل تاريخًا محددًا، لا قاعدة عامة.

Reflection تمثل تفسيرًا، لا دليلًا مستقلًا.

MemoryProposal تمثل ادعاءً مرشحًا، لا حقيقة مقبولة.

LearningGate تتحقق من أهلية المقترح، لكنها لا تقبله دلاليًا وحدها.

Executive تقرر القبول ضمن حدود القوانين.

CommitGate تمنع اعتماد انتقال غير قانوني.

Retrieval تعيد المعرفة المرشحة للاستعمال، لا تمنحها صلاحية حالية تلقائيًا.

PART II — HISTORICAL EXPERIENCE INTEGRITY
2. Verified Episode Source Binding

Corrects G01 — Fabricated Episodes

نعرف:

EpisodeSourceBinding {
    episode_id

    source_event_refs[]
    action_record_refs[]
    observation_refs[]
    verification_refs[]
    decision_refs[]

    source_frontier_ref

    capture_component_ref
    integrity_receipt_ref

    source_coverage_status
}

يجب أن يشير كل ادعاء تاريخي معتمد إلى مصدر قانوني مناسب.

مثلًا:

Claim:
    Tests passed.

لا يقبل كحدث مثبت لمجرد ظهوره في تقرير LLM.

يحتاج مرجعًا إلى Observation أو VerificationRecord حقيقية تدعم الادعاء ضمن نطاقها.

الـLLM يمكنها إنشاء ملخص للتجربة، لكن يجب تسجيله كتفسير مشتق، وليس مصدرًا جديدًا لما حدث في العالم.

3. Episode Completeness

Corrects G02 — Partial Episode Misrepresented as Complete

EpisodeCompletenessReceipt {
    episode_ref

    expected_event_scope

    captured_event_frontier

    missing_event_scope[]

    unresolved_action_refs[]

    completeness:
        COMPLETE
        PARTIAL
        UNKNOWN

    basis_refs[]
}

إذا بدأ الوكيل خمسة اختبارات ولم تُرصد نتيجة اختبارين، فلا يجوز إعلان نجاح مجموعة الاختبارات كلها.

نثبت:

PARTIAL Episode
    ≠
COMPLETE successful task

يمكن استخراج درس محدود من الأجزاء المثبتة، لكن لا يُسمح بتعميم النجاح على نطاق لم تُغطه الأدلة.

4. Historical Event vs Interpretation

نفصل:

HistoricalObservation
DerivedInterpretation
UnverifiedNarrative

فإذا قالت Reflection:

يبدو أن التعديل P أصلح المشكلة.

تبقى العبارة تفسيرًا يحتاج الدعم.

ولا يجوز أن تتحول إلى Observation بأن P سببت الإصلاح.

PART III — EVIDENCE LINEAGE AND SELF-REINFORCEMENT
5. MemoryEvidenceLineage

Corrects G03 — Evidence Feedback Loops

MemoryEvidenceLineage {
    memory_or_proposal_ref

    original_evidence_roots[]

    source_episode_refs[]

    derived_reflection_refs[]
    derived_memory_refs[]

    support_relationships[]

    circular_support_status

    evidence_basis_fingerprint
}

يجب الحفاظ على جذور الأدلة الأصلية حتى لو مرت المعلومات عبر عشرات عمليات التلخيص أو الاسترجاع.

6. No Evidence Multiplication

نفترض:

Observation O1
      │
      ▼
Episode E1
      │
      ├── Reflection R1
      ├── Reflection R2
      └── Reflection R3
              │
              ▼
         MemoryProposal

هذه ليست ثلاثة أدلة مستقلة.

يجب ألا يزداد مستوى نضج المعرفة أو تقييم قوة دليلها بسبب كثرة المشتقات من الجذر نفسه.

نثبت:

Derived interpretations do not create independent evidence roots.

7. Circular Support Detection

ممنوع اعتبار السلسلة التالية دعمًا مستقلًا:

Memory M1
    ↓
Retrieval
    ↓
Reflection R2
    ↓
Memory M2
    ↓
Used to corroborate M1

يستخدم النظام Evidence Lineage لاكتشاف الاعتماد الدائري.

إذا كان الدعم دائريًا دون جذور خارجية كافية:

CorroborationStatus = INSUFFICIENT

ولا يسمح بإنتاج maturity أعلى بناءً على هذه الحلقة.

PART IV — CAUSAL CLOSURE
8. Memory Claim Semantics

Corrects G04 — Causal Closure Bypass

MemoryClaimSemantics {
    claim_ref

    epistemic_kind:
        DESCRIPTIVE
        ASSOCIATIVE
        PROCEDURAL
        CAUSAL
        NORMATIVE

    accepted_basis_ref?

    required_governance_ref
}

يجب معرفة نوع الادعاء الذي نحاول حفظه.

مثال
Observed:
    Patch P was applied.
    Tests passed afterward.

هذا لا يساوي:

Causal:
    Patch P caused the tests to pass.

يمكن للوكيل حفظ النتيجة الوصفية كتجربة.

أما الادعاء السببي المعتمد فيجب أن يحترم Causal Closure Gate الموجودة في FCA.

9. Causal Memory Promotion

إذا كان MemoryProposal يحتوي على علاقة سببية، يجب تحديد:

causal_claim_ref?
causal_closure_status
supporting_intervention_refs[]
alternative_explanation_status

عندما تكون العلاقة السببية غير مثبتة، يمكن الاحتفاظ بها بصفتها:

CAUSAL_HYPOTHESIS

لكن لا تُعرض كقاعدة سببية مؤكدة.

لا ننشئ محرك سببية ثانيًا داخل الذاكرة.

PART V — MEMORY MATURITY GOVERNANCE
10. MaturityPromotionAssessment

Corrects G05 — Unsupported Generalization

MaturityPromotionAssessment {
    proposal_ref

    source_maturity
    requested_maturity

    source_scope
    requested_scope

    independent_evidence_analysis_ref

    evidence_diversity_assessment_ref

    applicability_coverage_ref

    counterexample_review_ref

    generalization_risk_refs[]

    assessment:
        ELIGIBLE
        INSUFFICIENT_SUPPORT
        SCOPE_TOO_BROAD
        UNKNOWN
}

لا نعتمد قاعدة:

Repeated success 3 times
    ↓
Automatically general knowledge

بل نطلب إثباتًا مناسبًا لاتساع النطاق المقترح.

11. Scope Expansion Rule

كل توسع في مجال صلاحية Memory يحتاج مراجعة مستقلة.

TASK_LESSON
    ↓
PROJECT_LESSON
    ↓
CANDIDATE_GENERALIZATION
    ↓
CORROBORATED_SCHEMA

هذا السلم ليس عدادًا آليًا.

قد تبقى معرفة في مستوى PROJECT_LESSON سنوات دون أن تصبح قاعدة عامة، وهذا ليس فشلًا.

12. Evidence Diversity

يجب فحص:

استقلال جذور الأدلة.

تنوع البيئات.

اختلاف implementations.

وجود اختبارات سلبية.

الأمثلة المضادة.

الافتراضات المشتركة بين التجارب.

لا نحدد رقمًا ثابتًا صالحًا لكل أنواع المعرفة.

لكن يجب أن تكون مبررات الترقية قابلة للتتبع والتحقق.

PART VI — FROZEN MEMORY PROPOSALS
13. MemoryProposalSnapshot

Corrects G06 — Proposal Mutation After LearningGate

MemoryProposalSnapshot {
    proposal_id
    proposal_version

    claim_ref
    scope_ref

    applicability_ref
    counterconditions_ref

    evidence_basis_ref
    dependency_set_ref

    maturity_target

    canonical_content_fingerprint

    created_commit_seq
}

تمر النسخة المثبتة نفسها عبر:

LearningGate
Executive Authorization
CommitGate

ولا يجوز تبديل محتوى الادعاء بعد اجتياز LearningGate.

14. Authorization Binding
LearningAuthorizationBinding {
    proposal_snapshot_ref

    learning_gate_evaluation_ref

    executive_authorization_ref

    expected_memory_head_ref?

    dependency_evaluation_ref

    authorized_commit_scope
}

إذا تغير مضمون المقترح أو نطاقه أو أدلته، تصبح الموافقة السابقة غير كافية.

PART VII — LEARNINGGATE FRESHNESS
15. Commit-Time Revalidation

Corrects G07 — Stale LearningGate Approval

نحدد المسار:

Frozen Proposal
       ↓
LearningGate Evaluation
       ↓
Executive Authorization
       ↓
Revalidate dependency frontier
       ↓
Check current contradiction state
       ↓
Check expected memory version
       ↓
CommitGate
       ↓
Canonical ControlCommit

لا يسمح باعتماد Memory اعتمادًا على نتيجة LearningGate قديمة إذا تغيرت الاعتماديات المؤثرة.

تُستخدم RDMS-06 لتقييم الصلاحية.

16. Observation Frontier

كل اعتماد معرفي يحدد نطاق الأدلة التي كانت معروفة عند القبول.

إذا ظهرت أدلة جديدة بعد ControlCommit، لا نمحو القرار التاريخي.

بل يعاد تقييم صلاحية الاعتماد على Memory وفق آليات RDMS-06 والتناقض.

هذا يمنع الادعاء غير الواقعي بأن النظام يستطيع ضمان عدم وصول أدلة جديدة في المستقبل.

PART VIII — RETRIEVAL AND APPLICABILITY
17. MemoryUseAssessment

Corrects G10 — Memory Becomes Current Fact

MemoryUseAssessment {
    memory_ref

    current_goal_ref

    source_scope_ref
    target_scope_ref

    applicability_assessment

    dependency_evaluation_ref

    current_evidence_refs[]

    required_revalidation_refs[]

    permitted_use:
        HISTORICAL_CONTEXT
        HYPOTHESIS_SOURCE
        PROCEDURAL_CANDIDATE
        CURRENTLY_SUPPORTED_REFERENCE

    limitations[]
}

لا يكفي أن تكون Memory صحيحة تاريخيًا.

يجب أن تكون مناسبة للنطاق الحالي.

18. Historical Knowledge Is Not Current Fact

مثال:

Memory:
    Project A uses Redis.

لا تسمح بالاستنتاج:

Current Project B uses Redis.

إلا بوجود أدلة حالية ملائمة.

نثبت:

Retrieved Memory
    → precedent or hypothesis

Current Fact
    → RDMS-03 evidence and legal acceptance
19. Retrieval Eligibility

Corrects G15 — Stale Memory Dominates Ranking

نقسم النتائج إلى:

CURRENTLY_APPLICABLE_CANDIDATES

HISTORICAL_OR_DIAGNOSTIC_CANDIDATES

BLOCKED_OR_INELIGIBLE_CANDIDATES

لا يجوز لترتيب التشابه أن ينقل Memory stale إلى مجموعة التوصيات الحالية دون إعادة تحقق.

يمكن استرجاعها للتحقيق في خطأ قديم، لكن مع إظهار حدود استخدامها.

20. Retrieval Coverage

Corrects G16 — Incomplete Search Interpreted as Absence

MemoryRetrievalCoverage {
    query_ref

    searchable_universe_ref

    index_snapshot_ref

    searched_scope

    retrieval_budget

    completeness:
        COMPLETE_WITHIN_SCOPE
        PARTIAL
        UNKNOWN

    excluded_scope_refs[]
}

إذا لم يعثر النظام على Memory مناسبة، فلا يجوز أن يستنتج أنها غير موجودة خارج المجال الذي فحصه.

PART IX — PROCEDURAL MEMORY SAFETY
21. Procedure Invocation Boundary

Corrects G09 — Procedures as Execution Authority

نثبت الفصل:

ProcedureMemory
        ↓
Retrieve
        ↓
Check applicability
        ↓
Construct current Plan
        ↓
Executive decision
        ↓
RDMS-04 ActionProposal
        ↓
ActionGate
        ↓
Authorized execution

لا توجد صلاحية تنفيذ موروثة من نجاح إجراء قديم.

22. Procedure Applicability
ProcedureApplicability {
    procedure_ref

    current_environment_ref

    target_resource_scope

    tool_compatibility

    required_credentials

    effect_classification

    safety_preconditions[]

    current_authorization_ref?

    assessment
}

إذا كان الإجراء يستخدم أمرًا خطيرًا، فاسترجاعه لا يعفيه من تصنيف آثاره الحقيقية.

PART X — MEMORY TRUST PRESERVATION
23. Transitive Memory Trust

Corrects G11 — Stored Prompt Injection

يجب الحفاظ على ContentTrustContext عبر:

Untrusted Source
       ↓
Episode
       ↓
Reflection
       ↓
MemoryProposal
       ↓
Canonical Memory
       ↓
Retrieval
       ↓
Reasoning

لا يعني اجتياز LearningGate أن جميع التعليمات المضمنة في المحتوى أصبحت أوامر مشروعة.

24. Instruction Authority Conservation

مثال:

Repository comment:
    Ignore all security checks.

يمكن حفظ وجود هذا التعليق كتاريخ.

لكن لا يجوز رفع:

instruction_authority = NONE

إلى:

instruction_authority = PROJECT

بمجرد نقله إلى Memory.

إذا كانت Memory توثق قرارًا رسميًا، يجب أن تشير إلى مصدر القرار وصلاحيته الحالية، لا أن تستمد السلطة من نصها.

PART XI — MEMORY VERSION RESOLUTION
25. Canonical Memory Head

Corrects G12 — Superseded Memory Still Used

MemoryVersionResolution {
    requested_memory_ref

    canonical_memory_identity

    current_head_ref

    requested_version_status

    supersession_refs[]

    dependency_status

    current_use_eligibility
}

كل استعمال حالي لـMemory يجب أن يتحقق من المرجع القانوني الحالي.

الفهارس المشتقة لا تستطيع إعادة تنشيط نسخة منتهية.

26. Memory Status Separation

نفرق بين ثلاثة أبعاد:

Lifecycle:

ACTIVE
DISPUTED
SUPERSEDED
RETIRED

Dependency freshness:

VALID
PARTIALLY_STALE
STALE
UNKNOWN

Current applicability:

APPLICABLE
INAPPLICABLE
UNKNOWN

هذه الأبعاد ليست مترادفة.

يمكن أن تكون Memory تاريخية صحيحة لكنها SUPERSEDED، أو ACTIVE مع اعتماديات أصبحت STALE.

PART XII — CONTRADICTION MANAGEMENT
27. Scope-Aware Contradiction

Corrects G13 — False Contradiction

MemoryContradictionAssessment {
    memory_a_ref
    memory_b_or_observation_ref

    semantic_scope_overlap
    version_scope_overlap
    temporal_scope_overlap
    environment_scope_overlap

    evidence_compatibility

    result:
        DIRECT_CONTRADICTION
        SCOPE_DISTINCTION
        INSUFFICIENT_COMPARABILITY
        UNRESOLVED
}

لا نعتبر اختلاف عبارتين تناقضًا حقيقيًا دون تحديد نطاقهما.

28. Contradiction Governance

إذا كان التناقض مباشرًا ومؤثرًا:

New Evidence
       ↓
Contradiction Assessment
       ↓
Memory reliance restricted
       ↓
RevisionProposal
       ↓
LearningGate
       ↓
Executive decision

لا تُحذف Observation القديمة ولا تُستبدل تلقائيًا.

PART XIII — DERIVED MEMORY VALIDITY
29. MemoryDerivationGraph

Corrects G14 — Derived Knowledge Outlives Source

MemoryDerivationGraph {
    memory_nodes[]

    evidence_root_nodes[]

    derivation_edges[]

    required_support_edges[]

    alternative_support_groups[]

    dependency_set_refs[]

    graph_version
}

يجب أن يعرف النظام كيف وصلت القاعدة المعتمدة إلى شكلها الحالي.

30. Transitive Invalidation

مثال:

Observation O1
      ↓
Task Lesson T1
      ↓
Project Lesson P1
      ↓
General Schema G1

إذا فُقدت صلاحية O1، فلا يجوز إبقاء G1 صالحة لمجرد أن نصها لم يتغير.

لكن إذا امتلكت G1 أدلة مستقلة أخرى كافية، فقد تظل بعض جوانبها مدعومة.

لذلك:

Source invalidation
    → dependency reevaluation
    → scoped invalidation

وليس:

Source invalidation
    → delete everything
31. Support Graph Cycles

إذا كانت Memory A تدعم B وB تدعم A دون أدلة خارجية مناسبة، فلا يجوز أن تكتسبا دعمًا حقيقيًا من الحلقة نفسها.

يستخدم المحرك cycle detection وEvidence Root Analysis.

عند عدم إمكان تقييم الاعتماديات الدائرية بصورة مؤهلة:

Memory support status = UNKNOWN
PART XIV — SAFE MEMORY CONSOLIDATION
32. MemoryConsolidationAssessment

Corrects G17 — Unsafe Merging

MemoryConsolidationAssessment {
    source_memory_refs[]

    semantic_equivalence_assessment

    scope_compatibility_assessment

    applicability_preservation_assessment

    counterexample_preservation_assessment

    evidence_lineage_preservation

    proposed_consolidated_memory_ref

    information_loss_risk

    result
}
33. Consolidation Rules

إذا كانت لدينا:

Memory A:
    Technique T works under condition X.

Memory B:
    Technique T fails under condition Y.

لا يجوز اختصارهما إلى:

Technique T works.

Consolidation يجب أن تحافظ على الشروط والأمثلة المضادة.

إذا غيرت المعنى الدلالي، فهي MemoryProposal جديدة تحتاج LearningGate.

أما إزالة التكرار المادي في الفهارس دون تغيير الحقيقة المعتمدة، فهي عملية تخزين مختلفة.

PART XV — INFORMATION GOVERNANCE
34. Memory Access Policy

Corrects G18 — Cross-Project Leakage

MemoryAccessPolicy {
    memory_ref

    source_security_domain

    permitted_use_scopes[]

    permitted_recipient_domains[]

    sensitivity_classification

    disclosure_constraints[]

    derived_data_restrictions[]

    declassification_authority_ref?
}

صلاحية استعمال معرفة لا تعني صلاحية الإفصاح عن تفاصيلها.

35. Derived Information Restrictions

إذا استُخرجت معرفة عامة من ملفات سرية، فإن إعادة صياغتها لا تزيل تلقائيًا قيود الإفصاح.

يجب تحديد:

source information restrictions
derived content restrictions
target recipient
target project
provider disclosure context

أي مشاركة تتجاوز القيود تحتاج declassification معتمدة أو نسخة مشتقة ثبتت صلاحية الإفصاح عنها.

لا تملك LLM سلطة رفع السرية.

PART XVI — RETENTION AND ERASURE
36. Epistemic Retirement vs Physical Erasure

Corrects G19 — Immutable History and Data Deletion

نفصل صراحة:

RETIRE_FROM_ACTIVE_USE

عن:

ERASE_STORED_INFORMATION

الأولى عملية معرفية.

الثانية عملية تخزين وخصوصية تحتاج ضمانات مختلفة.

37. Erasure Architecture Contract
MemoryErasureControl {
    erasure_request_ref

    affected_memory_refs[]

    affected_artifact_refs[]

    affected_index_refs[]

    affected_derivation_refs[]

    access_suppression_status

    erasure_execution_ref?

    verification_status:
        NOT_STARTED
        IN_PROGRESS
        VERIFIED_WITHIN_DECLARED_SCOPE
        INCOMPLETE
        UNKNOWN
}

عند قبول طلب إزالة قانوني، يجب منع الاستعمال المستقبلي للبيانات المشمولة وفق نطاق الطلب وسياساته، حتى لو لم ينته التنفيذ الفيزيائي بعد.

38. Append-Only Compatibility

يجب ألا نخزن محتوى حساسًا غير قابل للإزالة داخل Audit Ledger غير قابل للتعديل، ثم ندعي إمكان حذفه لاحقًا.

التصميم المطلوب:

Canonical audit metadata
    +
Opaque references
    +
Governed content storage
    +
Erasure-aware indexes

يمكن استخدام تشفير مناسب وفصل المفاتيح حيث تدعمه سياسة التخزين، لكن التشفير وحده لا يضمن إزالة جميع النسخ.

إذا كان مصدرًا سابقًا يحتوي بيانات حساسة داخل سجل غير قابل للمحو فعلًا، فلا يجوز إعلان إزالة فيزيائية كاملة دون معالجة التعارض.

39. RDMS-09 Boundary

RDMS-07 تحدد:

متى يمنع استخدام Memory.

ما المراجع والمشتقات التي يجب تتبعها.

ما حدود ادعاء اكتمال الإزالة.

كيف تؤثر الإزالة على أدلة المعرفة.

أما تنفيذ سياسات retention وعمليات الإزالة المادية والتحقق عبر التخزين والنسخ الاحتياطية فسيُفصل في RDMS-09.

قاعدة إلزامية: لا يجوز للتنفيذ ادعاء اكتمال إزالة تتجاوز نطاق النسخ التي يثبت التحكم فيها.

PART XVII — PROVIDER-INDEPENDENT SEMANTICS
40. Canonical Memory Schema

Corrects G20 — Provider Interpretation Drift

CanonicalMemorySchema {
    schema_version

    typed_entity_definitions

    canonical_serialization_rules

    semantic_validation_rules

    migration_contract_ref

    derived_index_contract_refs[]
}

الذاكرة المعتمدة ليست مجرد نص حر يفسره كل نموذج كما يشاء.

يجب أن تبقى العناصر المهمة:

claim
scope
conditions
counterexamples
evidence
authority
version

محددة بصورة مستقرة.

41. Provider Migration

عند تغيير LLM:

Provider A
    ↓
Canonical Memory
    ↓
Provider B

لا يجوز تغيير المعنى القانوني للذاكرة نتيجة اختلاف تفسير Provider B.

يمكن إعادة بناء Index أو إنشاء RetrievalAdapter جديدة.

أما تعديل Memory نفسها فيحتاج Migration أو Revision قانونية.

PART XVIII — CONCURRENT MEMORY REVISIONS
42. MemoryRevisionTransaction

Corrects G21 — Concurrent Revision and Duplicate Promotion

MemoryRevisionTransaction {
    revision_intent_id

    target_memory_id

    expected_current_version

    proposed_successor_ref

    frozen_proposal_snapshot_ref

    learning_gate_evaluation_ref

    executive_authorization_ref

    expected_dependency_frontier

    idempotency_key
}

يجب استخدام ControlCommit وCAS من RDMS-01.

43. Concurrent Revision Conflict

إذا حاولت عمليتان تعديل النسخة نفسها:

Memory M1
   ├── Revision A → M2
   └── Revision B → M3

لا يسمح باعتماد M2 وM3 باعتبارهما نسختين حاليّتين متنافستين بصورة صامتة.

يمكن حفظ المقترحين وتاريخ النزاع، لكن اختيار successor معتمدة يحتاج قرارًا قانونيًا.

44. Promotion Replay

إذا وقع crash بعد اعتماد Memory وقبل وصول acknowledgement:

Replay same revision_intent_id

يجب أن يعيد النظام نتيجة المعاملة المعتمدة، لا أن ينشئ Memory جديدة.

أما Revision مقصودة لاحقة فلها هوية منفصلة وتحتاج قرارًا جديدًا.

PART XIX — HARDENING CORRECTIONS
45. H01 — Confidence Calibration

لا نفترض أن confidence الصادرة عن نماذج مختلفة معايرة على مقياس احتمالي واحد.

تُحفظ طريقة تقدير الثقة وسياقها وحدودها.

46. H02 — Memory Growth Governance

نحدد:

storage quotas
episode retention classes
artifact archival
index budgets
compaction eligibility

مع الحفاظ على الأدلة والالتزامات المطلوبة وفق سياسة الاحتفاظ.

47. H03 — Retrieval Diversity

يمكن للـRetrieval طلب:

supporting precedents
counterexamples
failure patterns
competing procedures

لمنع انحياز السياق نحو مجموعة من النتائج المتشابهة فقط.

48. H04 — Knowledge Identity

نميز بين:

textual similarity
semantic equivalence
claim identity
scope identity

لا تندمج Memory تلقائيًا لمجرد التشابه النصي.

49. H05 — Derived Index Recovery

كل فهرس مشتق يجب أن يمتلك:

canonical source frontier
index generation
completeness status
schema version

الفهرس غير المتزامن لا يستطيع إثبات صلاحية Memory حالية دون الرجوع إلى الحالة المعتمدة.

50. H06 — Learning Budget

يملك Executive سياسة لتحديد متى تستحق التجربة:

reflection
independent review
generalization
consolidation

دون استهلاك ميزانيات مرتفعة لكل Episode صغيرة.

51. H07 — Memory Quality Monitoring

نسمح بقياس:

stale retrieval rate
incorrect applicability rate
unsupported promotion rate
contradiction detection rate
reuse value
revision outcomes

لكن القياسات لا تملك سلطة تلقائية لتغيير قوانين LearningGate أو حذف الذاكرة.

PART XX — ADDITIONAL INVARIANTS

تُضاف إلى RDMS07-I01…I30:

RDMS07-I31 — Historical claims within Episodes require verified source bindings or explicit unverified status.

RDMS07-I32 — Episode completeness and unresolved effects must be preserved through reflection and learning.

RDMS07-I33 — Derived interpretations, retrievals and summaries cannot create independent evidence roots.

RDMS07-I34 — Causal memories cannot bypass the existing Causal Closure Gate.

RDMS07-I35 — Maturity promotion requires scope-appropriate evidence and independent support analysis.

RDMS07-I36 — LearningGate and Executive authorization bind an immutable MemoryProposal snapshot.

RDMS07-I37 — Memory promotion must revalidate relevant dependencies and contradictions at CommitGate.

RDMS07-I38 — Memory retrieval cannot convert historical precedent into current Fact without qualified current evidence.

RDMS07-I39 — Procedural memories never carry reusable world-mutation authority.

RDMS07-I40 — Instruction authority cannot increase through Episode, Reflection, Memory or Retrieval transformations.

RDMS07-I41 — Current memory use must resolve canonical version, lifecycle, dependency validity and applicability.

RDMS07-I42 — Contradiction analysis must reconcile scope, version, time and environment.

RDMS07-I43 — Invalidated support propagates through required memory derivation dependencies.

RDMS07-I44 — Memory consolidation must preserve relevant conditions, counterexamples and evidence lineage.

RDMS07-I45 — Knowledge-transfer permission and information-disclosure permission are separate.

RDMS07-I46 — Privacy erasure must distinguish active-use suppression from verified physical removal.

RDMS07-I47 — Memory semantics remain canonical and provider-independent.

RDMS07-I48 — Concurrent memory revisions require version-guarded canonical commits.

RDMS07-I49 — Promotion replay cannot create duplicate canonical memory.

RDMS07-I50 — Retrieval completeness and index freshness must be explicit.

PART XXI — CORRECTION MATRIX
Finding	Correction	Status
G01 Fabricated Episodes	§§2–4	ADDRESSED
G02 Incomplete Episodes	§3	ADDRESSED
G03 Evidence Loops	§§5–7	ADDRESSED
G04 Causal Closure	§§8–9	ADDRESSED
G05 Unsupported Maturity	§§10–12	ADDRESSED
G06 Proposal Mutation	§§13–14	ADDRESSED
G07 Stale Gate	§§15–16	ADDRESSED
G08 Scope Expansion	§§10–12	ADDRESSED
G09 Procedure Authority	§§21–22	ADDRESSED
G10 Retrieved Memory as Fact	§§17–18	ADDRESSED
G11 Stored Injection	§§23–24	ADDRESSED
G12 Superseded Memory	§§25–26	ADDRESSED
G13 False Contradiction	§§27–28	ADDRESSED
G14 Derived Knowledge	§§29–31	ADDRESSED
G15 Invalid Ranking	§§19–20	ADDRESSED
G16 Incomplete Retrieval	§20	ADDRESSED
G17 Unsafe Consolidation	§§32–33	ADDRESSED
G18 Cross-Project Leakage	§§34–35	ADDRESSED
G19 Physical Deletion	§§36–39	ADDRESSED AT CONTRACT LEVEL
G20 Provider Drift	§§40–41	ADDRESSED
G21 Concurrent Revision	§§42–44	ADDRESSED
H01–H07	§§45–51	HARDENED
C01 VERDICT
Original blocking findings:      21
Corrective contracts supplied:   21

Hardening findings:               7
Hardening corrections supplied:   7

Changes to frozen FCA:            0
Changes to RDMS-01…06:            0

Implementation authorized:        NO

Freeze Review 02:                 REQUIRED

RDMS-07 C01 — COMPLETE FOR SECOND REVIEW.

هذا يعني أن كل ثغرة أصبحت لها قاعدة معالجة مقترحة، وليس أن صحتها التشغيلية قد ثبتت.

المرحلة الثانية — Adversarial Freeze Review 02

بعد إغلاق C01 على مستوى المواصفة، نعيد مهاجمة المعمارية.

الهدف ليس فقط التحقق من الثغرات السابقة، بل أيضًا البحث عن تناقضات قد تكون التصحيحات نفسها أدخلتها.

RDMS-07 — Adversarial Freeze Review 02
RDMS-07 — Adversarial Freeze Review 02

Target: RDMS-07 Draft v1.0 + C01
Review: Targeted Architectural Re-Audit
Status: FINAL SPECIFICATION REVIEW

1. Freeze Acceptance Criteria

يجب أن تضمن العقود المصححة:

عدم اختلاق تجربة أو دليل تاريخي.

عدم تضخيم الأدلة بواسطة التلخيص والاسترجاع.

عدم تجاوز Causal Closure Gate.

عدم تحويل نجاح محلي إلى تعميم غير مبرر.

عدم تعديل MemoryProposal بعد اجتياز البوابات.

عدم تنفيذ Procedure قديمة خارج التفويض الحالي.

عدم تحويل Memory مسترجعة إلى Fact حالي تلقائيًا.

عدم بقاء معرفة مشتقة صالحة بعد سقوط دعمها الضروري.

عدم تسرب معلومات سرية عبر الذاكرة.

عدم تكرار أو فقدان MemoryRevision بسبب التعافي.

2. EXPERIENCE AND EVIDENCE ATTACKS
T01 — Fabricated Episode

Attack: تنشئ LLM تقريرًا يقول إن جميع الاختبارات نجحت، دون Observation حقيقية.

Guard: EpisodeSourceBinding.

Expected: رفض الادعاء التاريخي المعتمد أو حفظه بوصفه سردًا غير مثبت.

Result: PASS BY CONTRACT.

T02 — Partial Episode

Attack: سجلت Episode ثلاثة اختبارات ناجحة من أصل خمسة.

Guard: EpisodeCompletenessReceipt.

Expected: لا يُسمح باستنتاج النجاح الشامل.

Result: PASS.

T03 — Evidence Self-Reinforcement

Attack: تجربة واحدة تولد خمس Reflections متفقة.

Guard: MemoryEvidenceLineage + independent roots.

Expected: لا تُحسب كمصادر أدلة مستقلة.

Result: PASS.

T04 — Recursive Memory Corroboration

Attack: Memory A تُسترجع لإنتاج B، ثم تُستخدم B لتأكيد A.

Guard: Circular support detection.

Expected: منع تضخيم الدعم دون دليل خارجي مستقل.

Result: PASS.

T05 — Causal Claim Without Closure

Attack: تحوّل Reflection نجاح اختبار إلى ادعاء سببي مؤكد.

Guard: typed claim semantics + Causal Closure Gate.

Expected: يبقى Hypothesis أو يُرفض القبول السببي.

Result: PASS.

3. MATURITY AND LEARNING AUTHORITY
T06 — Single Success Promoted to General Rule

Attack: نجاح واحد يؤدي إلى CORROBORATED_SCHEMA.

Guard: MaturityPromotionAssessment.

Result: PASS.

T07 — Many Repetitions With Same Evidence Root

Attack: عدة مشاريع متشابهة تشترك في مصدر دليل واحد.

Guard: evidence diversity and independence analysis.

Result: PASS.

T08 — Proposal Modified After LearningGate

Attack: توسيع claim من version 2.1 إلى جميع الإصدارات بعد اجتياز البوابة.

Guard: immutable proposal snapshot fingerprint.

Result: PASS.

T09 — Evidence Becomes Stale Before Commit

Attack: تظهر Observation جديدة مؤثرة بعد تقييم LearningGate.

Guard: dependency and contradiction revalidation at CommitGate.

Result: PASS BY CONTRACT.

T10 — Specialist Attempts Direct Memory Promotion

Attack: Specialist تطلب كتابة Canonical Memory مباشرة.

Guard: existing Executive/CommitGate authority.

Result: PASS.

T11 — Executive Attempts Illegal Promotion

Attack: Executive توافق على Memory تخالف Hard Invariant.

Guard: CommitGate.

Result: PASS.

4. RETRIEVAL AND PROCEDURAL SAFETY
T12 — Historical Memory Presented as Current Fact

Attack: معرفة تخص Project A تُستخدم لإثبات حالة Project B.

Guard: MemoryUseAssessment and current evidence requirements.

Result: PASS.

T13 — Unsafe Procedure Reused in Production

Attack: إجراء حذف قاعدة بيانات كان ناجحًا في Sandbox، ثم يُسترجع للإنتاج.

Guard: ProcedureApplicability + RDMS-04 ActionGate.

Result: PASS.

T14 — Prompt Injection Stored in Procedure

Attack: نص خبيث يتحول عبر Reflection إلى إجراء محفوظ.

Guard: transitive instruction-authority conservation.

Result: PASS BY CONTRACT.

T15 — Stale Memory Dominates Similarity Ranking

Attack: Memory ذات similarity مرتفعة لكنها stale تتفوق على Memory صالحة.

Guard: retrieval eligibility before current-use recommendation.

Result: PASS.

T16 — Partial Retrieval Declares No Memory Exists

Attack: بحث محدود لا يجد نتيجة ثم يستنتج غياب المعرفة.

Guard: MemoryRetrievalCoverage.

Result: PASS.

5. MEMORY EVOLUTION
T17 — Superseded Memory Remains in Search Index

Attack: Index قديمة تعيد Memory منتهية بوصفها حالية.

Guard: canonical memory head resolution.

Result: PASS.

T18 — False Contradiction Caused by Versions

Attack: Memory عن version 2.0 تتعارض ظاهريًا مع Observation عن version 2.4.

Guard: scope-aware contradiction assessment.

Result: PASS.

T19 — Invalidated Episode Supports General Schema

Attack: يُكتشف أن Observation الأصلية غير صالحة، لكن الذاكرة العامة المشتقة ما زالت موجودة.

Guard: MemoryDerivationGraph + RDMS-06 transitive evaluation.

Expected: يمنع الاستعمال الحالي غير المؤهل حتى إعادة تقييم الدعم.

Result: PASS.

T20 — Independent Alternative Evidence Remains Valid

Attack: يسقط دليل واحد لكن توجد أدلة مستقلة أخرى.

Guard: alternative support groups.

Expected: لا يحدث حذف أو إبطال شامل بلا تحليل.

Result: PASS.

T21 — Consolidation Removes Counterexample

Attack: دمج قاعدتين مع حذف شرط فشل مهم.

Guard: MemoryConsolidationAssessment.

Result: PASS.

T22 — Old Decision Memory Overrides Canonical Decision

Attack: استرجاع Decision تاريخية بعد supersession.

Guard: canonical decision and memory resolution.

Result: PASS.

6. PRIVACY AND PORTABILITY
T23 — Confidential Memory Transferred to Another Project

Attack: استرجاع معلومات خاصة بمشروع شركة A أثناء العمل على مشروع شركة B.

Guard: MemoryAccessPolicy + derived-data restrictions.

Expected: منع الإفصاح غير المصرح به، حتى لو كانت المعرفة مفيدة تقنيًا.

Result: PASS BY CONTRACT.

T24 — Confidential Detail Hidden in Generalization

Attack: يحاول النظام نقل معلومة سرية في صياغة مجردة تكشف بنية داخلية.

Guard: derived information restrictions + disclosure review.

Result: PASS BY CONTRACT.

T25 — Retired Memory Still Available in Derived Index

Attack: أُوقفت Memory عن الاستعمال الحالي لكن الفهرس القديم يعيدها.

Guard: active-use suppression + canonical eligibility resolution.

Result: PASS.

T26 — Physical Deletion Requested

Attack: تُحذف MemoryRecord، لكن المحتوى يبقى في artifacts وbackups.

Guard: erasure lineage, suppression and scoped verification.

Expected: لا يجوز إعلان حذف فيزيائي كامل دون إثباته.

Result: PASS AT CONTRACT LEVEL.

Residual: التنفيذ الفعلي لإزالة النسخ والتحقق منها يقع ضمن RDMS-09.

T27 — LLM Provider Changes Memory Meaning

Attack: Provider جديدة تعيد تفسير scope أو شروط Procedure.

Guard: typed canonical schema + validated adapters.

Result: PASS.

7. CONCURRENCY AND RECOVERY
T28 — Two Concurrent Memory Revisions

Attack: عمليتان تحاولان اعتماد successor مختلفة لـMemory واحدة.

Guard: expected current version + CAS.

Result: PASS.

T29 — Promotion Committed, Worker Crashes

Attack: تضيع acknowledgement بعد اعتماد Memory.

Guard: revision identity and idempotent ControlCommit.

Result: PASS.

T30 — Derived Index Rebuilt With Missing Records

Attack: Index ناقصة تُستخدم لاسترجاع المعرفة بوصفها كاملة.

Guard: index completeness/frontier validation.

Result: PASS.

T31 — Memory Confidence Increases Through Retrieval Count

Attack: استرجاع متكرر يرفع confidence دون أدلة.

Guard: evidence lineage and separate confidence governance.

Result: PASS.

T32 — LearningGate PASS Forged in LLM Output

Attack: ينتج النموذج نصًا يدّعي صدور موافقة.

Guard: trusted canonical gate identity.

Result: PASS.

8. SECOND-ROUND EDGE CASES

أثناء المراجعة حددنا ثلاث حالات تحتاج توضيحًا نهائيًا ملزمًا.

FC07-01 — Erasure Suppression Must Precede Retrieval Eligibility

قد يكون طلب الإزالة معتمدًا، بينما لم تُحدّث Retrieval Index بعد.

Final clarification:

RetrievalCandidate
        ↓
Canonical Access/Suppression Check
        ↓
Eligible for Disclosure?

يجب ألا تعتمد سلامة الإفصاح على وصول تحديث الفهرس المشتق فقط.

إذا كانت Memory محظورة أو مشمولة بإزالة تمنع الاستعمال، يرفض Retrieval Gateway إظهارها وفق السياسة الحالية.

Disposition: CLOSED BY CONTRACT.

FC07-02 — LearningGate Cannot Treat Missing Counterexamples as Proof of Absence

قد لا يجد النظام أمثلة مضادة بسبب نقص البحث.

هذا لا يثبت عدم وجودها.

Final clarification:

CounterexampleSearch {
    search_scope
    coverage_status
    known_counterexamples[]
    unresolved_search_limitations[]
}

إذا كان مستوى التعميم المطلوب يحتاج مراجعة شاملة ضمن نطاق معين، فلا تكفي نتيجة بحث ناقصة لإثبات استيفاء هذا الشرط.

يمكن اعتماد درس أضيق إذا كان الدليل يكفي لنطاقه.

Disposition: CLOSED BY CONTRACT.

FC07-03 — Privacy Erasure Can Weaken Memory Evidence

قد تعتمد Memory M2 على Episode E1.

ثم تُزال بيانات E1 بموجب سياسة الاحتفاظ أو الخصوصية.

إذا لم تعد الأدلة اللازمة قابلة للتحقق، فلا يجوز الاستمرار في الادعاء بأن M2 تمتلك السند نفسه.

Final clarification:

Evidence removed or inaccessible
        ↓
Reevaluate remaining support
        ↓
VALID / PARTIALLY_STALE / STALE / UNKNOWN

بحسب عقد RDMS-06 ووجود دعم مستقل بديل.

ولا يعني ذلك أن إزالة البيانات تجعل كل الاستنتاجات المشتقة خاطئة؛ لكنها قد تقلل الأدلة المتاحة للتحقق منها.

Disposition: CLOSED BY CONTRACT.

9. FREEZE REVIEW MATRIX
Area	Verdict
Episode source integrity	PASS
Episode completeness	PASS
Reflection evidence conservation	PASS
Circular evidence prevention	PASS
Causal Closure compatibility	PASS
Maturity governance	PASS
Proposal immutability	PASS
Commit-time freshness	PASS
Scope expansion	PASS
Procedure authority	PASS
Memory-to-Fact boundary	PASS
Stored prompt-injection boundary	PASS
Supersession resolution	PASS
Contradiction scope analysis	PASS
Transitive memory validity	PASS
Safe consolidation	PASS
Retrieval eligibility	PASS
Retrieval completeness	PASS
Cross-project information policy	PASS
Erasure contract	PASS — implementation deferred
Provider-independent schema	PASS
Concurrent revisions	PASS
Promotion idempotency	PASS
10. RESIDUAL IMPLEMENTATION GATES

التجميد المعماري لا يلغي التحقق البرمجي اللاحق.

يجب أن يجتاز التنفيذ:

IG07-01 — Evidence integrity

اختبارات تزوير Observation وEpisode وEvidenceBasis.

IG07-02 — LearningGate consistency

اختبارات تعديل MemoryProposal بعد الموافقة، وتغير dependencies قبل CommitGate.

IG07-03 — Circular evidence

اختبارات Reflections وMemories التي تعتمد بعضها على بعض دون جذور مستقلة.

IG07-04 — Retrieval safety

اختبارات Memory stale وsuperseded وretired والحالات غير المؤهلة للإفصاح.

IG07-05 — Dependency propagation

اختبارات سقوط أدلة أصلية ووجود دعم بديل مستقل.

IG07-06 — Privacy and retention

اختبارات access suppression، وتحديد النسخ والمشتقات، والتحقق من حدود الإزالة الفعلية.

IG07-07 — Provider migration

اختبارات بقاء المعنى القانوني للحقول والعقود عند تغيير النموذج أو الفهرس.

IG07-08 — Concurrency and recovery

اختبارات Revision CAS، وpromotion idempotency، وانهيار العمليات عند حدود ControlCommit.

11. FINAL FREEZE DECISION
Original blocking findings:      21
Addressed in C01:                21

Original hardening findings:      7
Addressed in C01:                 7

Additional review clarifications: 3
Closed at contract level:         3

Remaining identified
specification blockers:           0

Changes required to FCA:          0
Changes required to RDMS-01…06:   0

Executable tests performed:       0
Verdict

RDMS-07 — PASS: SPECIFICATION-LEVEL FREEZE REVIEW 02.

RDMS-07 — MEMORY, LEARNING, EXPERIENCE & KNOWLEDGE GOVERNANCE: FROZEN AT SPECIFICATION LEVEL.

هذا التجميد يثبت العقود المصححة وقيود السلطة والإجراءات المحافظة عند عدم اليقين.

ولا يُعد شهادة بسلامة تنفيذ فعلي، أو باكتمال سياسة إزالة البيانات التي يجب تفصيلها في RDMS-09.

12. NEXT AUTHORIZED PHASE

RDMS-08 — Cognitive Executive, Decision Runtime & Governance Enforcement

المجالات الأساسية:

Executive state machine.

Cognitive attention and focus management.

Capability selection.

Decision authority.

Goal and Slice orchestration.

CommitGate and ActionGate integration.

Planning and replanning.

Decision gravity.

Model and provider orchestration.

Metacognitive control.

Budget and work-in-progress governance.

Recovery and Executive epoch enforcement.

RDMS-07: CLOSED / FROZEN.

النتيجة

بهذا نكون قد أغلقنا RDMS-07 على مستوى المواصفات المعمارية.

أهم ما ثبتناه هو الفصل بين أربع عمليات غالبًا ما تختلط في أنظمة الوكلاء:

التذكر: استرجاع ما حدث سابقًا.

التفسير: محاولة فهم لماذا حدث.

التعلم: قبول درس هندسي مدعوم بالأدلة.

التطبيق: تحديد هل يصلح ذلك الدرس للمهمة الحالية، ثم اتخاذ إجراء قانوني.

لن نسمح للذاكرة بتجاوز هذه الحدود.

الحالة الحالية
المواصفة	الحالة
FCA v1.0.1	✅ FROZEN
RDMS-01	✅ FROZEN
RDMS-02	✅ FROZEN
RDMS-03	✅ FROZEN
RDMS-04	✅ FROZEN
RDMS-05	✅ FROZEN
RDMS-06	✅ FROZEN
RDMS-07	✅ FROZEN
RDMS-08	⏳ NEXT
RDMS-09	⏳ PENDING
RDMS-10	⏳ PENDING

بقيت لنا ثلاث مواصفات رئيسية قبل الوصول إلى RDMS-10، حيث سنعود إلى فكرتك الخاصة بتنظيم المشروع في طبقات مستقلة، ثم إجراء المراجعة المعمارية الشاملة قبل البرمجة.

المرحلة التالية: RDMS-08 — Cognitive Executive, Decision Runtime & Governance Enforcement.

وهنا سنقترب من أهم عنصر في النظام كله: كيف يدير العقل التنفيذي عملية التفكير والتخطيط واتخاذ القرار، ومتى يطلب معلومات إضافية، ومتى يكلّف متخصصًا، ومتى يسمح بكتابة الكود، ومتى يوقف العمل ويعيد التخطيط.

END ORIGINAL MESSAGE
````



## GAIA-C01 Phase 7 — Proposed Effective Contract Crosswalk (non-normative)


> Review-only annotations. They **do not** replace any FCA/RDMS original source annex or modify frozen legal definitions. Canonical promotion requires explicit approval and proof.

| Original type | Current crosswalk status | Review anchor |
|---|---|---|
| `MemoryProposal` | `CONDITIONAL_PRESERVATION` | `../reviews/GAIA_C01_PHASE7_REMAINING_CONTRACT_RECONCILIATION.md` §P7-16 |

**No production code or new canonical schema authorized at this stage.**


## GAIA-C01 Phase 11 — Verification boundary

`MemoryRetrievalResult` source fields are preserved through a verified canonical reference in the in-memory example; real transport adapter and approved alias remain pending.

See `../reviews/GAIA_C01_PHASE11_LOSSLESS_PROOF_REPORT.md` and `../reviews/verification/gaia_phase11_reference_tests.py`. **NOT FROZEN.**
