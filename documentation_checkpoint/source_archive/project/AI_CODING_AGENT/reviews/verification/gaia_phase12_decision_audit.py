"""Phase 12 audit-only consistency checks; not a runtime adapter test."""
import hashlib
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
R=ROOT/'reviews'
D=json.loads((R/'GAIA_C01_PHASE12_27_CONTRACT_DECISIONS.json').read_text())
class DecisionAudit(unittest.TestCase):
    def test_complete_unique_decisions(self):
        assert len(D['decisions'])==27
        assert len({e['contract'] for e in D['decisions']})==27
    def test_explicit_dispositions(self):
        assert sum('DIRECT_CANONICAL' in e['decision'] for e in D['decisions'])==22
        assert sum('EDITORIAL_TRANSPORT_ALIAS' in e['decision'] for e in D['decisions'])==2
        assert sum('LEGACY_EFFECTIVE_MAPPING_BLOCKED' in e['decision'] for e in D['decisions'])==3
    def test_primary_paths_resolve(self):
        for e in D['decisions']:
            p=ROOT/e['source_path']
            assert p.is_file(),p
            assert e['source_line']>0
            assert len(p.read_text().splitlines())>=e['source_line']
    def test_original_sha256_manifest(self):
        original=json.loads((R/'GAIA_C01_PHASE12_SOURCE_HASHES.json').read_text())
        for rel,expected in original.items():
            assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==expected,rel
    def test_eight_layers_and_one_index_each(self):
        for i in range(8):
            p=next((ROOT/'architecture').glob(f'L{i}_*.md'))
            content=p.read_text()
            assert content.count('<!-- GAIA-C01-PHASE12-DECISION-INDEX START -->')==1,p
            assert content.count('<!-- GAIA-C01-PHASE12-DECISION-INDEX END -->')==1,p
    def test_no_product_code(self):
        src=ROOT/'src'
        assert not [p for p in src.rglob('*.py') if p.is_file()]
    def test_high_risk_remain_blocked(self):
        for n in ('Commitment','TriggerCondition','ResumptionCapsule'):
            e=next(x for x in D['decisions'] if x['contract']==n)
            assert 'BLOCKED' in e['decision']
    def test_distinct_aliases(self):
        aliases=('CapabilityTransportResult','MemoryRetrievalTransportResult')
        assert not set(aliases)&{e['contract'] for e in D['decisions']}
        l7=(ROOT/'architecture'/'L7_RUNTIME_INTEGRATION.md').read_text()
        assert all(x in l7 for x in aliases)
    def test_archive_no_frozen_overwrite(self):
        assert D['architecture_freeze_authorized'] is False
        assert D['production_code_written'] is False
if __name__=='__main__':unittest.main(verbosity=2)
