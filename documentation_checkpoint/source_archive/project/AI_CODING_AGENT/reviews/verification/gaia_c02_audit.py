"""Source preservation and limited GAIA-C02 release-candidate publication audit.
Not an equivalence proof of every effective law, nor a production/runtime test.
"""
from pathlib import Path
import hashlib, json, re, zipfile, sys
ROOT=Path(__file__).resolve().parents[2]
REV=ROOT/'reviews'; ARCH=ROOT/'architecture'
FILES={'L0':'L0_FOUNDATION.md','L1':'L1_CONTROL.md','L2':'L2_COGNITION.md','L3':'L3_ACTIONS.md','L4':'L4_TEMPORAL_SPECIALISTS.md','L5':'L5_MEMORY.md','L6':'L6_RECOVERY.md','L7':'L7_RUNTIME_INTEGRATION.md'}
source_hashes=json.loads((REV/'GAIA_C01_PHASE12_SOURCE_HASHES.json').read_text())
contracts=json.loads((REV/'GAIA_C01_PHASE12_27_CONTRACT_DECISIONS.json').read_text())['decisions']
gates=json.loads((REV/'GAIA_C01_PHASE9_CROSS_INTERFACE_GATES.json').read_text())['gates']
passes=[];errors=[]
for path,h in source_hashes.items():
 p=ROOT/path
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=h:errors.append('SOURCE_HASH_MISMATCH '+path)
passes.append(f'SOURCE_HASHES_{len(source_hashes)}' if not errors else 'SOURCE_HASH_FAILURE')
for ly,name in FILES.items():
 p=ARCH/name;txt=p.read_text();marker='<!-- GAIA-C02-NORMATIVE-CANDIDATE END -->';snap=(REV/'GAIA_C02_PREVIOUS_LAYER_SNAPSHOTS'/name).read_text()
 if txt.count(marker)!=1 or not txt.split(marker,1)[1].lstrip('\n')==snap:errors.append('APPENDIX_CHANGED '+name)
 front=txt.split(marker,1)[0]
 for c in [c for c in contracts if c['owner_layer']==ly]:
  if front.count('### `'+c['contract']+'`')!=1:errors.append('TYPE_MISSING_OR_DUPLICATED '+c['contract'])
passes.append('EIGHT_LAYER_FRONTS_AND_SNAPSHOTS' if not any(e.startswith('APPENDIX_CHANGED') or e.startswith('TYPE_') for e in errors) else 'FRONT_FAILURE')
if len(contracts)!=27:errors.append('INVALID_CONTRACT_COUNT')
if len(gates)!=12:errors.append('INVALID_INTERFACE_COUNT')
interface=(ARCH/'CROSS_LAYER_INTERFACE_CATALOGUE.md').read_text()
for g in gates:
 if interface.count('| '+g['id']+' |')!=1:errors.append('MISSING_INTERFACE '+g['id'])
passes.append('27_OWNED_CONTRACTS_12_WITNESSES' if not any('INVALID' in e or 'INTERFACE' in e for e in errors) else 'CATALOGUE_FAILURE')
parts={}
for i in range(1,11):
 txt=(REV/'source_archive'/'RDMS_ORIGINAL_SOURCES'/f'RDMS-{i:02d}_APPROVED_SOURCE_SET.txt').read_text()
 parts[f'RDMS-{i:02d}']=len(re.findall(r'^MESSAGE ID:',txt,flags=re.M))
if sum(parts.values())!=27:errors.append('RDMS_SOURCE_MESSAGE_COUNT')
passes.append('27_RDMS_SOURCE_MESSAGES')
summary={'phase':'GAIA-C02','audit':'source/baseline/publication structure only','passed':not errors,'checks':passes,'errors':errors,'counts':{'source_files':len(source_hashes),'layer_docs':len(FILES),'contracts':len(contracts),'interface_paths':len(gates),'rdms_source_messages':sum(parts.values())},'effective_full_law_frozen':False,'production_conformance_tested':False}
(REV/'GAIA_C02_VALIDATION_RESULTS.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)
