from pathlib import Path
import json,hashlib,re
BASE=Path(__file__).resolve().parents[2]
path=BASE/'reviews/GAIA_C08/GAIA_C08_PRIMARY_SOURCE_INTERFACE_LEDGER.json'
ledger=json.loads(path.read_text())
source=BASE/'reviews/source_archive/RDMS_ORIGINAL_SOURCES/original_message_dom.json'
messages={m['id']:m['text'] for m in json.loads(source.read_text())}
hashtext=lambda t:hashlib.sha256(t.encode()).hexdigest()
assert len(messages)==ledger['verified_original_messages']==27
assert hashlib.sha256(source.read_bytes()).hexdigest()==ledger['source_corpus_sha256']
for rel, expected in ledger['all_original_archive_sha256'].items():
    assert hashlib.sha256((BASE/rel).read_bytes()).hexdigest()==expected,(rel,'source drift')
assert len(ledger['routes'])==12
for r in ledger['routes']:
    assert r['source_schema_count']>=3
    assert r['legal_status'].endswith('NOT_RATIFIED')
    for g in r['source_schemas']:
        assert g['occurrences']
        for d in g['occurrences']:
            assert d['source_message_id'] in messages
            text=messages[d['source_message_id']]
            lines=text.splitlines(keepends=True)
            # source blocks were stripped of exterior newlines only
            matched=''.join(lines[d['start_line']-1:d['end_line']]).strip('\n')
            assert d['text']==matched,(r['route_id'],g['symbol'],d['start_line'])
            assert hashtext(d['text'])==d['sha256']
assert all((BASE/'architecture'/x).exists() for x in ('L0_FOUNDATION.md','L1_CONTROL.md','L2_COGNITION.md','L3_ACTIONS.md','L4_TEMPORAL_SPECIALISTS.md','L5_MEMORY.md','L6_RECOVERY.md','L7_RUNTIME_INTEGRATION.md'))
assert not ledger['global_freeze_approved']
print('PASS: 27/27 original messages, all archived source digests unchanged')
print('PASS: 12/12 interface dossiers, source block lines/text/digests replayed')
print('PASS: 8/8 layer documents present, no false freeze assertion')
print('AUDIT:',sum(r['source_occurrences'] for r in ledger['routes']),'source declaration occurrences')
