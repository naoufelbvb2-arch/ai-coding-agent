# Formal Cognitive Architecture v1.0

من التصور إلى المكونات المنطقية: ما الذي يصبح Service أو Class أو قاعدة بيانات أو دالة، وما الذي يحتاج LLM فعلاً.

## 1. قاعدة التصنيف

كل عنصر في الوثيقة المفاهيمية يمر بهذا الاختبار بالترتيب، ويقف عند أول جواب «نعم»:

- **دالة حتمية (Function):** هل يمكن حسابه بقواعد ثابتة؟ (ترتيب التبعيات، التحقق من schema، فحص قواعد المعمارية، diff، الميزانية)
- **أداة واقع (Tool):** هل الجواب عند الواقع لا عند النموذج؟ (تشغيل اختبار، قراءة ملف، debugger)
- **LLM call:** هل يحتاج حكماً دلالياً مفتوحاً؟ (فهم نية، توليد فرضيات، مقارنة تصاميم، كتابة كود، نقد)
- **Specialist:** هل يحتاج استقلالاً أو توازياً أو عزل سياق؟ (القسم 6)

القاعدة الحاكمة: **LLM يقترح، الحتمي يتحقق، الواقع يحكم، Executive وحده يعتمد.**

## 2. المكونات المنطقية

| المكون | يملك | لا يفعل أبداً | الشكل التنفيذي |
| --- | --- | --- | --- |
| Cognitive Executive | سياسة القرار، آلة الحالات، اعتماد التغييرات، الميزانية | لا يكتب كوداً ولا يثق بمخرج LLM دون تحقق | Service واحد حتمي، يستدعي LLM لأحكام محددة فقط |
| Canonical Workspace | الحالة المعرفية الكاملة + سجل الأحداث | لا يقبل كتابة إلا عبر Patch معتمد | Event store + snapshots (قاعدة بيانات) |
| Capability Runtime | تشغيل القدرات بعقودها (القسم 5) | لا يعدّل الحالة مباشرة، يرجع Patch مقترحاً | مكتبة داخل نفس العملية |
| Verification Engine | اختبارات، قواعد معمارية، semantic diff، فحص schema | لا يستخدم LLM في الحكم النهائي | Service حتمي |
| Reality Interface | مهايئات الأدوات: repo، git، shell، debugger، DB | لا يفسر النتائج، يسجلها كأدلة خام | Adapters خلف واجهة موحدة، تعمل في sandbox |
| Memory System | ذاكرة المشروع والتجارب والإجرائية والقرارات | لا يعمّم تلقائياً ولا يقدم الذاكرة كسلطة | Store + فهرس بحث + Learning Gate |
| Reasoning Gateway | توجيه الطلبات للمزوّد، تنسيق schema، إعادة المحاولة، التكلفة | لا يعرف شيئاً عن المشروع | Adapter لكل مزوّد خلف واجهة واحدة |
| Specialist Manager | إنشاء، عزل، دمج، إنهاء العمال المؤقتين | لا يمنحهم سلطة على الحالة المشتركة | Service حتمي فوق Gateway وRuntime |

## 3. Canonical State: المخطط

الوحدة الأساسية هي `Claim`. هذا ما يفصل الحقيقة عن الاعتقاد عن الافتراض عن المجهول، ويمنع «الطلاقة» من أن تصير دليلاً.

```
Claim {
  id, kind: fact | belief | assumption | unknown | hypothesis,
  statement, scope, confidence: 0..1,
  evidence_for: [EvidenceId], evidence_against: [EvidenceId],
  status: open | supported | refuted | superseded, version
}
Evidence {
  id, source: tool | human | repo | llm_output,
  ref, observed_at, strength: direct | indirect | weak
}
Goal   { id, parent, intent, acceptance: [Check], status }
Decision {
  id, gravity: low|med|high, question, alternatives: [Option],
  chosen, rationale, revisit_trigger, evidence: [EvidenceId]
}
Slice {
  id, goal_id, preconditions, expected_effects,
  verification: [Check], rollback, status, actual_effects
}
Commitment { id, why_temporary, until, removal_trigger, owner }
Specialist { id, goal, scope, base_version, authority, status }
State {
  version, repo_ref, goals, model: {domain, structure, runtime,
  causal, risk}, claims, evidence, decisions, graph: [Slice],
  commitments, specialists, meta: {confidence, stagnation,
  contradictions}, current_strategy, depth
}
```

**ثوابت لا تُخرق (يفرضها Workspace حتمياً):**

- لا يُقبل `Evidence.source = llm_output` كدليل من فئة `direct`. مخرج النموذج فرضية، لا ملاحظة.
- كل `Claim` من نوع fact يحتاج دليلاً واحداً على الأقل من الواقع.
- كل `Slice` مرتبطة بـ `Goal`، وإلا تُعلَّم انحرافاً (drift).
- الكتابة فقط عبر `Patch {base_version, ops}`، ويُرفض إن كان `base_version` قديماً.
- كل تغيير يُسجَّل كحدث غير قابل للتعديل (event sourcing)، فيمكن إعادة بناء أي حالة سابقة.

## 4. آلة حالات Executive

| الحالة | ماذا يحدث | الانتقال التالي (الشرط) |
| --- | --- | --- |
| INTAKE | فهم النية، بناء Goal، تحديد المجهول | ORIENT، أو ASK_USER إن كان الغموض يغيّر الهدف |
| ORIENT | بناء أو تحديث النموذج الذهني، حساب Decision Gravity | INVESTIGATE إن وُجدت مجاهيل مؤثرة، وإلا PLAN |
| INVESTIGATE | تركيز الانتباه، جمع الأدلة، فرضيات وتجارب | DELIBERATE إن لزم قرار، وإلا PLAN (عند انخفاض عدم اليقين تحت العتبة) |
| DELIBERATE | بدائل، محاكاة مستقبلية، مقارنة، تسجيل Decision | PLAN، أو INVESTIGATE إن ظهر مجهول جديد |
| PLAN | بناء Execution Graph، المخاطر أولاً | EXECUTE_SLICE |
| EXECUTE_SLICE | توليد مقيَّد لـ Slice واحدة، تطبيقها | VERIFY |
| VERIFY | اختبارات، قواعد معمارية، semantic diff، محاكاة القارئ | المتوقع = الفعلي: REVIEW. وإلا DIAGNOSE |
| DIAGNOSE | أي نموذج كان خاطئاً؟ فرضيات سببية، تصحيح النموذج | EXECUTE_SLICE (إصلاح محلي) أو REPLAN (خطأ في الخطة) أو ORIENT (خطأ في الفهم) |
| REVIEW | بوابة ما وراء المعرفة، مراجعة مستقلة عند الجاذبية العالية | EXECUTE_SLICE التالية، أو FINALIZE، أو REPLAN |
| SUSPEND / RESUME | إنشاء كبسولة استئناف، ثم مطابقتها مع تغيّر العالم | الحالة التي علّقنا منها بعد المطابقة |
| FINALIZE | فحص معايير القبول، تحديث الحالة، Learning Gate | انتهاء |

**مقاطعات عامة** تُفحص بعد كل انتقال بدوال حتمية، وتقفز بالتنفيذ إلى ORIENT أو REPLAN:

- **Patch cascade:** فشلان متتاليان بعد إصلاحين.
- **Blast radius:** الملفات المتغيرة الفعلية أكثر من ضعف المتوقعة.
- **Drift:** Slice بلا Goal أب.
- **الميزانية:** تجاوز حد الخطوات أو التكلفة، فيتوقف ويسأل المستخدم.

## 5. عقود القدرات

كل قدرة دالة بهذا العقد: `run(StateSlice, Objective, Budget) → { Patch, Evidence[], Confidence, Needs[] }`. تقرأ شريحة من الحالة فقط، ولا تكتب شيئاً، وتعيد اقتراحاً.

| القدرة | تقرأ | تقترح | الجزء الحتمي | LLM |
| --- | --- | --- | --- | --- |
| Intent & Goal | طلب المستخدم، Goals | Goal، acceptance، أسئلة | فحص اكتمال الحقول | نعم |
| Mental Model | repo، model | تحديث model، claims | مخطط التبعيات وAST والبنية من الكود | للمفاهيم والسببية فقط |
| Attention / Foraging | unknowns، focus | قائمة ما يُقرأ تالياً | بحث رمزي، ترتيب بالتكلفة | اختياري |
| Hypothesis & Causal | الملاحظات، claims | فرضيات، تحديث الثقة | إدارة الأدلة والحالة | نعم |
| Experiment Design | فرضيتان متنافستان | أرخص تجربة تفرّق بينهما | تنفيذ التجربة عبر الأدوات | نعم للتصميم |
| Engineering Judgment | مشكلة، قيود، model | بدائل، Decision | حساب Decision Gravity، قوائم الفحص | نعم |
| Planning | Goals، تبعيات، مخاطر | Execution Graph | الترتيب الطوبولوجي، التحقق من الدورات | للتفكيك الأولي فقط |
| Code Synthesis | Slice، عقود، مفردات | كود مرشح | بناء السياق المقيَّد، فحص القيود | نعم |
| Verification | Slice، الكود | نتائج، semantic diff | كله | لا (إلا محاكاة القارئ) |
| Reader Simulation / MMRT | الكود فقط، دون السياق | نموذج ذهني مُعاد بناؤه | مقارنة الهياكل | نعم، بسياق معزول |
| Metacognition | meta، claims، evidence | الثقة، تعارضات، جمود | كشف الجمود والانحراف والتعارض | للتقييم الدلالي فقط |
| Learning | سجل الحلقة | دروس مرشحة | Learning Gate: النطاق، قوة الدليل، المقارنة | للتأمل فقط |

## 6. قواعد إنشاء Specialists

**شرط الإنشاء** (يفحصه Specialist Manager حتمياً): يوجد على الأقل واحد من: عمل متوازٍ على نطاقات غير متداخلة، حاجة لحكم مستقل (جاذبية عالية)، عزل سياق مفيد، أو تنوع فرضيات مطلوب. وإلا يعمل Executive بنفسه.

- **العقد عند الإنشاء:** الهدف، النطاق، لقطة من الحالة بإصدار `base_version`، السلطة المسموحة، التغييرات الممنوعة، المخرج المتوقع، التزام التحقق، ميزانية.
- **المخرج الراجع:** نتيجة، أدلة، semantic diff، حقائق وافتراضات جديدة، مخاطر، تغييرات مقترحة على الحالة المشتركة، عدم يقين متبقٍ.
- **الحدود:** عمق واحد (لا ينشئ Specialist غيره)، حد أقصى للمتزامنين، مهلة، وميزانية. لا كتابة على الحالة المشتركة.
- **الدمج:** كل مقترح يمر بفحص التعارض مع `base_version`، ثم Verification، ثم اعتماد Executive أو رفضه. الأدلة تزن أكثر من عدد الموافقين.
- **المراجع المستقل:** يبدأ دون استنتاج الكاتب، ومهمته «كيف يمكن أن يكون هذا خاطئاً؟».
- **الإنهاء:** عند تسليم المخرج أو انتهاء الميزانية، ويُحفظ سجله كحلقة (episode).

## 7. تدفق البيانات

```
Executive picks next capability
  → Workspace.read(slice)            // only what is needed
  → Capability builds request
  → Gateway.complete(ctx, schema)    // if LLM needed
  → schema validation (deterministic)
  → Patch proposal + Evidence[]
  → Verification / invariant checks
  → Executive accepts | rejects | asks for more
  → Workspace.commit(Patch) → event log
  → checkpoint → next state transition
```

Reality Interface يكتب الأدلة الخام مباشرة في Workspace كـ `Evidence` (لأنها ملاحظات لا استنتاجات). أما أي تفسير لها فيمر بقدرة ثم Patch.

## 8. ما يصبح ماذا

| النوع | العناصر |
| --- | --- |
| قاعدة بيانات | Event store وsnapshots للحالة، ذاكرة التجارب والقرارات والإجرائية، فهرس البحث |
| Service | Executive، Verification Engine، Specialist Manager، Reality Interface (sandbox) |
| Class / مكتبة | Workspace API، Capability Runtime، Gateway adapters، Learning Gate |
| دوال حتمية | Decision Gravity، ترتيب التبعيات، كشف الجمود والانحراف، فحص الثوابت، semantic diff، الميزانية، تحقق schema |
| LLM call | فهم النية، فرضيات، تصميم تجارب، بدائل ومقارنة، توليد كود، محاكاة القارئ، النقد الدلالي، التأمل |

## 9. قرارات تنتظر الحسم

- لغة التنفيذ وشكل الـ Workspace (SQLite مع سجل أحداث يكفي للبداية؟).
- عتبات الانتقال: ما «انخفاض عدم اليقين الكافي» وكيف يُقاس رقمياً؟
- أول مجموعة مهام تقييم (benchmark) لقياس أثر كل قدرة.
- هل Reader Simulation في الإصدار الأول أم الثاني؟