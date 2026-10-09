#!/usr/bin/env python3
"""Source-checked editorial publication of verified clauses; not a production runtime."""
from pathlib import Path
from collections import defaultdict,Counter
import hashlib,json,re,zipfile,shutil,datetime

ROOT=Path('/mnt/data/AI_CODING_AGENT')
REV=ROOT/'reviews'
SRC=REV/'source_archive/RDMS_ORIGINAL_SOURCES'
ARCH=ROOT/'architecture'
START='<!-- GAIA-C07-EFFECTIVE-CLAUSES START -->'
END='<!-- GAIA-C07-EFFECTIVE-CLAUSES END -->'
SHA=lambda s:hashlib.sha256(s.encode('utf-8')).hexdigest()
messages={}
for f in SRC.glob('RDMS-*_APPROVED_SOURCE_SET.txt'):
    text=f.read_text(encoding='utf-8')
    for match in re.finditer(r'(?m)^MESSAGE ID: ([a-f0-9-]+)\nBEGIN ORIGINAL MESSAGE\n={72}\n\n',text):
        msg=text[match.end():].split('\nEND ORIGINAL MESSAGE')[0].rstrip('\n')
        assert match.group(1) not in messages
        messages[match.group(1)]={'text':msg,'file':f.name}
manifest=json.loads((SRC/'SOURCE_MANIFEST.json').read_text())
for rec in manifest:
    msg=messages[rec['message_id']]['text']
    assert SHA(msg)==rec['text_sha256'], f"original changed {rec['message_id']}"
assert len(messages)==len(manifest)==27

reg=json.loads((REV/'GAIA_C01_PHASE9_EFFECTIVE_CONTRACT_REGISTRY.json').read_text())['entries']
c04=json.loads((REV/'GAIA_C04/GAIA_C04_EXPLICIT_SUPERSESSION_WITNESSES.json').read_text())
c05=json.loads((REV/'GAIA_C05/GAIA_C05_VERIFIED_DELTA_REGISTER.json').read_text())
c06=json.loads((REV/'GAIA_C06/GAIA_C06_VERIFIED_CROSS_DOMAIN_GUARDS.json').read_text())
routes=json.loads((REV/'GAIA_C06/GAIA_C06_12_INTERFACE_EVIDENCE_MATRIX.json').read_text())
assert len(reg)==27 and len(c04)==6 and len(c05)==12 and len(c06)==15 and len(routes)==12
source_ids=set()
entries=[]
def proof(source, kind):
    mid=source['message_id']; assert mid in messages
    a,b=source.get('lines') or (source.get('line_start',source.get('start_line')),source.get('line_end',source.get('end_line')))
    lines=messages[mid]['text'].splitlines()
    assert 1<=a<=b<=len(lines),(mid,a,b,len(lines))
    s='\n'.join(lines[a-1:b])
    expected=source.get('sha256',source.get('text_sha256'))
    assert SHA(s)==expected,(mid,SHA(s),expected)
    return s,a,b

for item in c04:
    new,a,b=proof(item['effective_source'],'C04'); old,oa,ob=proof(item['superseded_source'],'C04') if item.get('superseded_source') else ('',0,0)
    entries.append(dict(id=item['id'],spec=item['specification'],owner={'RDMS-01':'L1_CONTROL.md','RDMS-02':'L2_COGNITION.md'}[item['specification']],kind=item['status'],rule=item['meaning'],new=new,new_source=item['effective_source'],old_source=item['superseded_source'],old_sha256=SHA(old),verified=True))
for item in c05:
    new,a,b=proof(item['effective_correction'],'C05')
    old,oa,ob=proof(item['old'],'C05')
    assert new==item['effective_correction']['verbatim'] and old==item['old']['verbatim']
    entries.append(dict(id=item['id'],spec=item['specification'],owner=item['owner_layer'],kind=item['relationship'],rule=item['binding_rule'],new=new,new_source=item['effective_correction'],old_source=item['old'],old_sha256=SHA(old),verified=True,route=item['route']))
for item in c06:
    new,a,b=proof(item['new'],'C06');old,oa,ob=proof(item['old'],'C06')
    assert new==item['new']['verbatim'] and old==item['old']['verbatim']
    entries.append(dict(id=item['id'],spec=item['specification'],owner=item['owner_layer'],kind='ADDITIONAL_APPROVED_GUARD',rule=item['safe_coexistence_rule'],new=new,new_source=item['new'],old_source=item['old'],old_sha256=SHA(old),verified=True,route=item['related_route']))
assert len(entries)==33 and len({e['id'] for e in entries})==33
by_layer=defaultdict(list)
for e in entries:by_layer[e['owner']].append(e)
by_type=defaultdict(list)
for d in reg:
    by_type[f"L{d['owning_layer_candidate'][1:]}"].append(d)

# A human-facing, source-backed operative section immediately at the start of each existing layer.
role={
'L0_FOUNDATION.md':'الأساس الدستوري وحدود الثقة والصلاحية (FCA v1.0.1)',
'L1_CONTROL.md':'الحالة القانونية وControlCommit والتسلسل والتاريخ المتين',
'L2_COGNITION.md':'الالتزامات والقرارات والاستدلال والادعاءات المعرفية',
'L3_ACTIONS.md':'تنفيذ الأفعال والملاحظات والأدلة والتحقق من الآثار',
'L4_TEMPORAL_SPECIALISTS.md':'Triggers والمتخصصون والاعتماديات وصلاحية النتائج',
'L5_MEMORY.md':'الذاكرة والاسترجاع وتغطية النتائج وحفظ الأثر',
'L6_RECOVERY.md':'الاستعادة والـepochs ومنع التكرار والأثر غير المعلوم',
'L7_RUNTIME_INTEGRATION.md':'المعابر والعقود والربط بين الصلاحيات والتبادل',
}
fcamap=(REV/'GAIA_C01_FCA_TRACEABILITY.md').read_text()
source_layer=defaultdict(list)
for m in re.finditer(r'^\| FCA §([^|]+) \| `([^`]+)` \| `([a-f0-9]{64})` \|$',fcamap,re.M):
    source_layer[m.group(2)].append(m.group(1))
assert len(source_layer)==8

for layer, description in role.items():
    p=ARCH/layer
    original=p.read_text()
    # Existing historical meta may have similar headings; new section is single current editorial gate only.
    if START in original:
        original=original.split(START,1)[0]+original.split(END,1)[1].lstrip('\n')
    out=[START,
        f'# GAIA-C07 — متن البنود النافذة المثبتة: {layer.removesuffix(".md")}',
        '',
        '**حالة النشر: VERIFIED-CLAUSE EDITORIAL VIEW / NON-FROZEN.** هذه الفقرة تضع الأحكام التي ثبتت نصوصها في الواجهة. ليست دمجًا مكتملًا لكل مصادر RDMS، ولا تنقل ملكية العقود أو تمنح سلطة تنفيذ. عند عدم اكتمال التسوية، يظل النص المجمد الأصلي مع التصحيح المقبول اللاحق هو المرجع.',
        '', f'**الاختصاص:** {description}.',
        '',f'**نطاق FCA الأصلي في هذه الطبقة:** {", ".join("§"+i for i in source_layer.get(layer, []))}. تم الحفاظ على نصها الأصلي في بقية الوثيقة وفي `reviews/source_archive/`.',
        '', '## أحكام التعديل والتقييد المثبتة حرفيًا',
        '',f'**عدد شواهد هذه الطبقة: {len(by_layer[layer])}.** كل بند أدناه مصدّق بنص المصدر وبصمته، لكن هذه العيّنات لا تثبت مراجعة جميع بنود المصادر.',
        '']
    for e in by_layer[layer]:
        src=e['new_source']
        ln=src.get('lines') or [src.get('line_start',src.get('start_line')),src.get('line_end',src.get('end_line'))]
        out += [f'### {e["id"]} — {e["spec"]}',
            f'**العلاقة القانونية:** `{e["kind"]}`. **الحكم المثبت:** {e["rule"]}',
            f'**المصدر المصحح:** message `{src["message_id"]}`، الأسطر {ln[0]}–{ln[1]}، SHA-256 `{SHA(e["new"])}`.',
            '**نص المصدر المصحح حرفيًا (قد يتضمن وصفًا للنص القديم؛ الوصف ليس قاعدة نافذة):**',
            '```text', e['new'], '```','']
    out += ['## أنواع البيانات المالكة لها الطبقة — مرجع نشر لا إثبات مواءمة نهائية','']
    types=[x for x in reg if x['owning_layer_candidate']==layer.split('_')[0]]
    if types:
        out += ['| العقد | المصدر المختار لنصه الأساسي | اختبار الإثبات المتبقي |', '|---|---|---|']
        for t in types:
            proof_text=t.get('proof_gate') or 'Proof gate not supplied'
            proof_text=proof_text.replace('|','\\|').replace('\n',' ')
            out += [f'| `{t["name"]}` | {t["owning_specification_source"]} | {proof_text} |']
    else: out += ['لا توجد عقود من قائمة التكرار الـ27 مملوكة لهذه الطبقة؛ تظل قواعد FCA الأصلية نافذة.']
    out += ['', '## شرط قراءة بقية الوثيقة','',
       'بقية المحتوى أدناه تضم نصوص FCA الأصلية وتاريخ FCA/RDMS والتصحيحات ومراجعات سابقة. **أي عنوان قديم يحمل CURRENT أو FROZEN يخص مصدره/مرحلته ولا يمثل تلقائيًا اعتماد دمج L0–L7.** يُقدّم التصحيح المقبول على المسودة فقط في موضوعه المثبت؛ لا تُلغى حقول أخرى بالصمت.',
       '', '**ما لا تثبته هذه المرحلة:** (أ) مطابقة كل فقرة من جميع التصحيحات، (ب) توقيع واجهة متكامل لكل مسار، (ج) ذرية تنفيذ خارجي، (د) اختبار Runtime إنتاجي، (هـ) تجميد الطبقات الثماني.',END,'','---','']
    p.write_text('\n'.join(out)+original)

# Exact duplicate audit: each normative-new excerpt occurs once in newly published front segment.
for layer in role:
    x=(ARCH/layer).read_text()
    assert x.count(START)==1 and x.count(END)==1 and x.index(START)<x.index(END)
    front=x.split(END,1)[0]
    for e in by_layer[layer]:
        assert e['new'] in front, e['id']
# Validate original source files unchanged against byte hashes recorded before mutation.
source_files={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (REV/'source_archive').rglob('*') if p.is_file()}
# FCA freeze source integrity
assert source_files['reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md']=='74d0923cbd343b71740da0fc2368a84aad2ea97f8e4e15f156122f48ebe53539'

outdir=REV/'GAIA_C07';outdir.mkdir(exist_ok=True)
(outdir/'GAIA_C07_OPERATIVE_CLAUSES.json').write_text(json.dumps([{k:v for k,v in e.items() if k not in ('new',)} for e in entries],ensure_ascii=False,indent=2))
iface_md=['# GAIA-C07 — بوابة الواجهات الاثني عشر','', '**نتيجة جميع المسارات: HOLD.** يوجد توثيق لشروط جزئية مثبتة، لكن لا توجد واجهة واحدة تستوفي معًا توقيع المنتج والمستهلك، شروط الأخطاء والمعاملة، ودليل الذرية الفعلي.','', '| المسار | الأدلة المعتمدة | توقيع كامل؟ |', '|---|---|---|']
for r in routes:
    ids=r.get('C06_additional_verified_guard_ids',[])
    ids+= [e['id'] for e in c05 if e['route']==r['route']]
    iface_md.append(f"| {r['route']} | {', '.join(ids) if ids else 'لا يوجد إثبات حارس إضافي'} | HOLD |")
iface_md += ['','**معايير الإغلاق قبل أي تجميد:** حقول الطلب والاستجابة والإلزامية، جهة الإنشاء والاستهلاك، سياق المشروع والإصدار والحقبة، السلطة المصدّقة، لحظة الاستيثاق، حدود الذرية والتسليم الموثوق، أثر الفشل/الإعادة والتسوية، نموذج إثبات الاسترداد، منع اختلاق حالة غير موجودة، وقبول نسخ المستندات التي تراجع حقليًا.','', 'التعامل الذري مع Control Ledger لا يعني معاملة ذرية مع أدوات العالم الخارجي. حالات IN_DOUBT تتطلب reconciler مستقلًا.']
(outdir/'GAIA_C07_INTERFACE_CLOSEOUT.md').write_text('\n'.join(iface_md))

report=['# GAIA-C07 — تقرير نشر الأحكام المثبتة إلى المتون الحالية','',
 '**القرار: VERIFIED CLAUSE FRONT-PUBLICATION PASS / FULL FREEZE HOLD.**','',
 'قمنا بنشر نصوص التصحيحات والقيود المتحقق منها حرفيًا في بداية وثائق L0–L7 الحالية، دون اختراع صيغة جديدة للقوانين أو إزالة النصوص الأصلية. هذا إجراء نشر مادي في ملفات الطبقات، لا مجرد فهرسة.','',
 f'- 27/27 رسالة مصدر RDMS تطابق بصمتها المحفوظة.',
 f'- 6/6 أحكام C04 (4 استبدالات و2 توضيح)، و12/12 قيدًا C05، و15/15 حارسًا/عقدًا إضافيًا C06: **33** شهادة أُعيد حساب بصماتها من نص الرسائل الأصلية.',
 f'- 27/27 عقدًا متكررًا مذكورة في الوثيقة المالكة مع بوابة إثبات التوافق، ولا يعني ذلك منح محول قانوني تلقائي.',
 f'- 12/12 واجهة أعيد فحص حالات إثباتها: لا توقيع كامل معتمد.',
 f'- 8/8 وثائق محدثة؛ جميع الأصول المجمدة محفوظة بلا تعديل.',
 '', '## توزيع الشواهد على الطبقات', '', '| الطبقة | الشواهد المثبتة حرفيًا |', '|---|---:|']
for n in role:report.append(f'| `{n}` | {len(by_layer[n])} |')
report += ['','## لماذا لم ننفذ تجميدًا؟','',
 'هذه الشواهد الـ33 محدودة النطاق. لا توجد حتى الآن مطابقة دلالية ناجزة لجميع بنود الرسائل اللاحقة البالغ عدد عناوينها المفهرسة 1014، ولا يجوز مساواة العنوان بالتعديل. كما لم تثبت التواقيع النهائية للواجهات أو الفشل/الاسترجاع. الأصل السابق غير المنسوخ صراحة يظل ضمن المصدر المعتمد.',
 '', '## المطلوب للبوابة التالية','',
 'إنهاء التدقيق بندًا بندًا لكل تصحيح مؤثر، ثم توثيق تواقيع الواجهات الـ12 مع الحقول والإثبات القانوني والفشل والتعافي. حينها تراجع الثماني طبقات على أساس متن موحد دون ازدواج.',
 '', '**إنتاج الكود:** لم تُنشأ ملفات إنتاجية في `src/agent/`. الأداة البرمجية المرفقة للتحقق الوثائقي فقط.']
(outdir/'GAIA_C07_EXECUTIVE_REPORT_AR.md').write_text('\n'.join(report))
state=dict(phase='GAIA-C07',source_messages_verified=27,document_layers_updated=8,source_clause_verifications=33,verified_C04_explicit_supersessions=4,verified_C04_clarifications=2,verified_constraints=12,verified_additional_guards=15,source_owned_contracts_listed=27,tracked_interfaces=12,fully_ratified_interfaces=0,full_sourcewide_semantic_reconciliation=False,full_L0_L7_freeze=False,production_code_created=False,source_file_sha256=source_files)
(outdir/'GAIA_C07_GATE.json').write_text(json.dumps(state,ensure_ascii=False,indent=2))

# Update manifest and README only once.
manifest_path=ARCH/'ARCHITECTURE_MANIFEST.md';base=manifest_path.read_text()
if base.startswith('# CURRENT STAGE — GAIA-C07'):
    base=base.split('---\n\n',1)[1]
header='# CURRENT STAGE — GAIA-C07 Verified Operative Clause Publication\n\n**Status: partial clause publication PASS; L0–L7 FREEZE HOLD.** Thirty-three correction passages have been verified against the original RDMS message hashes and physically placed at the start of the appropriate L0–L7 layer files. All twelve cross-layer public signatures remain awaiting legal ratification. `reviews/GAIA_C07/` contains the proof ledger and results. Prior stage headings below are historical. **No production code authorized.**\n\n---\n\n'
manifest_path.write_text(header+base)
readme=ROOT/'README.md';readme.write_text('# AI Coding Agent — Current Architecture Status\n\n**GAIA-C07: VERIFIED-CLAUSE PUBLICATION; CONSOLIDATED FREEZE HOLD.**\n\nOpen `architecture/L0_FOUNDATION.md` through `L7_RUNTIME_INTEGRATION.md`: their first section now contains source-verified current corrective passages and the legal-owner contract register. These sections do not supersede FCA/RDMS sources outside the proven scope.\n\nSee `reviews/GAIA_C07/GAIA_C07_EXECUTIVE_REPORT_AR.md` and `reviews/GAIA_C07/GAIA_C07_INTERFACE_CLOSEOUT.md`.  No production implementation was started.\n')

# Zip all project files (exclude pycache and temporary files) and check archive CRC.
output=Path('/mnt/data/AI_CODING_AGENT_GAIA_C07_operative_clause_publication.zip')
with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in ROOT.rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:
            z.write(p,arcname=str(p.relative_to(ROOT.parent)))
with zipfile.ZipFile(output) as z:
    assert z.testzip() is None
    n=len(z.namelist())
print(f'SOURCE_MESSAGE_SHA_PASS {len(messages)}/{len(manifest)}')
print(f'SOURCE_CLAUSE_SHA_PASS {len(entries)}/{len(entries)}')
print(f'OWNER_DOCS_UPDATED {len(role)}/{len(role)}')
print(f'DUPLICATE_TYPE_REGISTER {len(reg)}/{len(reg)}')
print(f'INTERFACES_RATIFIED 0/{len(routes)}')
print(f'ZIP_CRC_PASS {n} files')
print(f'PACKAGE {output}')
print(f'FULL_FREEZE HOLD')
