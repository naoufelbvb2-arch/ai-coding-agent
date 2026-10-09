#!/usr/bin/env python3
"""Offline audit of the GAIA effective interface closeout, no production runtime."""
import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ARCH=ROOT/'architecture'
REV=ROOT/'reviews'
class EffectiveCloseout(unittest.TestCase):
 def test_source_archive_original_hashes(self):
  expected=json.loads((REV/'GAIA_C01_PHASE12_SOURCE_HASHES.json').read_text())
  self.assertEqual(len(expected),18)
  for rel,sha in expected.items():
   self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),sha,rel)
 def test_all_twelve_have_legal_gates(self):
  gates=json.loads((ARCH/'EFFECTIVE_INTERFACE_BOUNDARIES.json').read_text())
  self.assertEqual(set(x['route_id'] for x in gates),{f'X8-{i:02}' for i in range(1,13)})
  for x in gates:
   for attr in ('input_records','output_records','acceptance_preconditions','mandatory_rejection_conditions','authority_boundary','commit_and_effect_boundary','retry_and_recovery'):
    self.assertTrue(x[attr],(x['route_id'],attr))
   self.assertTrue((ARCH/x['owner_document']).exists())
   self.assertIn(f"## {x['route_id']}",(ARCH/x['owner_document']).read_text())
 def test_literal_67_witness_hashes(self):
  ledger=json.loads((REV/'GAIA_C08/GAIA_C08_PRIMARY_SOURCE_INTERFACE_LEDGER.json').read_text())
  witnesses=[o for route in ledger['routes'] for symbol in route['source_schemas'] for o in symbol['occurrences']]
  self.assertEqual(len(witnesses),67)
  for x in witnesses:self.assertEqual(hashlib.sha256(x['text'].encode()).hexdigest(),x['sha256'])
 def test_record_inventory_and_field_surfaces(self):
  types=json.loads((ARCH/'EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json').read_text())
  fields=json.loads((ARCH/'EFFECTIVE_INTERFACE_FIELD_SURFACE.json').read_text())
  self.assertEqual(len(types),54)
  self.assertEqual(set(types),set(fields))
  self.assertGreater(sum(len(x['surface_fields']) for x in fields.values()),500)
  for x in types.values():self.assertTrue(x['source_message_id'] and x['base_source_sha256'])
 def test_canonical_commitment_patch_applied(self):
  alltypes=json.loads((ARCH/'EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json').read_text())
  c=alltypes['Commitment'];txt=c['effective_declaration_candidate']
  self.assertIn('reactivation_condition_ref',txt)
  for old in ('due_at?', 'removal_trigger_id?', 'revisit_trigger_id?'):self.assertNotIn(old,txt)
  self.assertTrue(c['supersession']['RDMS05_temporal_view_is_not_canonical_replacement'])
  self.assertFalse(c['supersession']['historical_data_automatic_migration_authorized'])
  self.assertIn('reactivation_condition_ref',(ARCH/'L2_COGNITION.md').read_text()[:2200])
 def test_two_contract_name_collisions_not_conflated(self):
  types=json.loads((ARCH/'EFFECTIVE_INTERFACE_SCHEMA_EVIDENCE.json').read_text())
  self.assertEqual(types['CapabilityResult']['logical_transport_alias'],'CapabilityTransportResult')
  self.assertEqual(types['CapabilityResult']['canonical_cognitive_result_owner'],'FCA v1.0.1 §23')
  self.assertEqual(types['MemoryRetrievalResult']['transport_shortlist_alias'],'MemoryRetrievalTransportResult')
  self.assertEqual(types['MemoryRetrievalResult']['canonical_result_owner'],'RDMS-07')
 def test_freeze_gate_is_truthful(self):
  g=json.loads((REV/'GAIA_EFFECTIVE_CLOSEOUT/CLOSEOUT_GATE.json').read_text())
  self.assertEqual(g['final_freeze'],'HOLD')
  self.assertEqual(g['interface_contracts_with_explicit_admission_rejection_and_recovery'],12)
  self.assertEqual(g['interface_architectural_signatures_ratified'],0)
  self.assertFalse(g['full_legal_layer_consolidation_proven'])
if __name__=='__main__':unittest.main(verbosity=2)
