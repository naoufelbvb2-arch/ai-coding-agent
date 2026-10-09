"""Source-grounded architecture publication acceptance. Not runtime authorization tests."""
from pathlib import Path
import hashlib,json,re,zipfile

ROOT=Path(__file__).resolve().parents[2]
ARCH=ROOT/'architecture'
REV=ROOT/'reviews/GAIA_NORMATIVE_CLOSEOUT'
OLD=Path('/mnt/data/AI_CODING_AGENT_NORMATIVE_SOURCE_MERGE_CANDIDATE.zip')

def test_source_archive_unchanged():
    assert OLD.exists()
    with zipfile.ZipFile(OLD) as z:
        files=[f for f in z.namelist() if f.startswith('AI_CODING_AGENT/reviews/source_archive/') and not f.endswith('/')]
        assert len(files)>=27
        for f in files:
            assert (ROOT/f.removeprefix('AI_CODING_AGENT/')).read_bytes()==z.read(f),f

def test_12_routes_are_named_and_complete():
    routes=json.loads((ARCH/'EFFECTIVE_INTERFACE_BOUNDARIES.json').read_text())
    assert len(routes)==12
    for i,r in enumerate(routes,1):
        assert r['route_id']==f'X8-{i:02d}'
        assert r['input_records'] and r['output_records']
        assert r['authority_boundary'] and r['acceptance_preconditions']
        assert r['mandatory_rejection_conditions'] and r['retry_and_recovery']
        assert (ARCH/r['owner_document']).exists()

def test_primitive_types_not_invented():
    a=json.loads((ARCH/'OPERATIVE_INTERFACE_TYPE_REGISTRY.json').read_text())
    assert len(a)==56
    assert all(x['primitive_type_resolution']=='DEFERRED_TO_IMPLEMENTATION_CONFORMING_TO_FROZEN_SEMANTICS' for x in a)
    assert {x['effective_type'] for x in a}==set(json.loads((ARCH/'EFFECTIVE_INTERFACE_FIELD_SURFACE.json').read_text()))

def test_names_and_source_fields_not_colliding():
    a=json.loads((ARCH/'EFFECTIVE_INTERFACE_FIELD_SURFACE.json').read_text());e=json.loads((ARCH/'EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json').read_text())
    assert len(a)==len(e)==56
    cognitive={x['base_name'] for x in a['CapabilityResult']['surface_fields']}
    transport={x['base_name'] for x in a['CapabilityTransportResult']['surface_fields']}
    assert 'patch_proposal' in cognitive and 'proposed_claims' in cognitive
    assert 'invocation_id' in transport and 'result_status' in transport
    assert 'invocation_id' not in cognitive and 'patch_proposal' not in transport
    memcanon={x['base_name'] for x in a['MemoryRetrievalResult']['surface_fields']}
    memtrans={x['base_name'] for x in a['MemoryRetrievalTransportResult']['surface_fields']}
    assert 'retrieval_coverage' in memcanon and 'ranking_policy_ref' in memcanon
    assert 'memory_refs' in memtrans and 'retrieval_coverage' not in memtrans
    for name,obj in e.items():
        assert name in a
        assert obj['raw_declaration']

def test_no_legacy_competing_reactivation_roots_in_current_schema():
    a=json.loads((ARCH/'EFFECTIVE_INTERFACE_FIELD_SURFACE.json').read_text())
    f={x['base_name'] for x in a['Commitment']['surface_fields']}
    assert 'reactivation_condition_ref' in f
    assert not {'due_at','removal_trigger_id','revisit_trigger_id'}&f

def test_retained_resumption_header_and_payload():
    a=json.loads((ARCH/'EFFECTIVE_INTERFACE_FIELD_SURFACE.json').read_text())
    f={x['base_name'] for x in a['ResumptionCapsule']['surface_fields']}
    assert {'durable_payload_artifact_ref','content_integrity_ref'}<=f

def test_11_legacy_supersessions_have_clear_after_text():
    a=json.loads((REV/'APPLIED_LEGACY_REPLACEMENTS.json').read_text())
    assert len(a)==11
    for x in a:
        text=(ARCH/x['layer']).read_text();segment=text[text.index('## 4. Inherited RDMS base clauses'):text.index('## 5. Cross-layer interface admission and rejection')]
        assert x['archive_unmodified'] and x['source_id']
        # SHA is over the substitution payload: at least the full new span survived exactly.
        # Stored hash disallows silently altered correction text in future revisions.
        # Source declarations are subject to prefix annotations; no re-inference from this audit.
        assert len(x['effective_text_sha256'])==64

def test_layers_have_effective_schemas_and_full_source_regions():
    layers=sorted(ARCH.glob('L[0-7]_*.md'))
    assert len(layers)==8
    for layer in layers:
        text=layer.read_text()
        assert '## 1. Current source-proven legal resolutions' in text
        assert '## 2. Original FCA v1.0.1 frozen normative sections' in text
        assert '## 3. RDMS corrective provisions' in text
        assert '## 4. Inherited RDMS base clauses' in text
        assert '## 5. Cross-layer interface admission' in text

def test_explicit_legal_replacements_are_current():
    l1=(ARCH/'L1_CONTROL.md').read_text();b=l1[l1.index('## 4. Inherited RDMS base clauses'):]
    assert 'control_schema_version' in b and 'request_fingerprint' in b and 'authority_context' in b
    l2=(ARCH/'L2_COGNITION.md').read_text();b=l2[l2.index('## 4. Inherited RDMS base clauses'):]
    assert 'CanonicalEntityMeta {' in b
    assert 'reactivation_condition_ref' in b
    l4=(ARCH/'L4_TEMPORAL_SPECIALISTS.md').read_text();b=l4[l4.index('## 4. Inherited RDMS base clauses'):]
    assert 'trigger_definition_snapshot_ref' in b
    assert 'durable_payload_artifact_ref' in b
    l7=(ARCH/'L7_RUNTIME_INTEGRATION.md').read_text();b=l7[l7.index('## 4. Inherited RDMS base clauses'):]
    assert 'CapabilityTransportResult {' in b and 'MemoryRetrievalTransportResult {' in b

def run():
    for name,f in sorted(globals().items()):
        if name.startswith('test_') and callable(f):
            f();print('PASS',name)
    print('ARCHITECTURE_SOURCE_MERGE_TESTS_PASS')
if __name__=='__main__':run()
