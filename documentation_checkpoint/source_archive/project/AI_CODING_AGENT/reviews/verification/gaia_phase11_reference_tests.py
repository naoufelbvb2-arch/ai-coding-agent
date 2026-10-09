"""GAIA-C01 Phase 11: *reference-only* crosswalk conformance examples.

NOT implementation tests. No production packages, no external tools/services/DB/queues.
The fixtures are constrained by field inventory from supplied FCA/RDMS source texts.
"""
from __future__ import annotations

import hashlib
import json
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = json.loads((ROOT / "reviews/GAIA_C01_PHASE10_FIVE_PRIORITY_CROSSWALKS.json").read_text(encoding="utf-8"))["cases"]
VECTORS = json.loads((ROOT / "reviews/GAIA_C01_PHASE10_18_VECTOR_ACCEPTANCE_LEDGER.json").read_text(encoding="utf-8"))["vectors"]

class ContractRejection(Exception):
    """Reference-only fail-closed state."""


def encoded(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def source_fields(name, source_start):
    for key, fields in REGISTRY[name]["source_field_inventory"].items():
        if key.startswith(source_start):
            return fields
    raise ContractRejection("No original field inventory " + name + ":" + source_start)


class ImmutableRefStore:
    """In-memory integrity/scope model; NOT a durable implementation."""
    def __init__(self):
        self.records = {}

    def put(self, payload, project="P1", schema="v1"):
        snapshot = deepcopy(payload)
        digest = hashlib.sha256(encoded(snapshot)).hexdigest()
        ref = f"sha256:{digest}"
        self.records[ref] = {"payload": snapshot, "project": project, "schema": schema}
        return {"ref": ref, "project": project, "schema": schema, "digest": digest}

    def resolve(self, handle, project="P1", schema="v1"):
        if not handle or handle.get("project") != project or handle.get("schema") != schema:
            raise ContractRejection("Invalid reference scope/schema")
        ref = handle.get("ref")
        entry = self.records.get(ref)
        if not entry or entry["project"] != project or entry["schema"] != schema:
            raise ContractRejection("Missing or wrong-scope canonical record")
        if hashlib.sha256(encoded(entry["payload"])).hexdigest() != handle.get("digest"):
            raise ContractRejection("Content integrity mismatch")
        if ref != f"sha256:{handle['digest']}":
            raise ContractRejection("Reference/digest mismatch")
        return deepcopy(entry["payload"])


def fixture(fields, **overrides):
    rec = {f: f"example:{f}" for f in fields}
    rec.update(overrides)
    return rec


def projection(store, record, expected_fields, project="P1", schema="v1"):
    if not set(expected_fields).issubset(record):
        raise ContractRejection("Unrecoverable source fields")
    return {"canonical_ref": store.put(record, project, schema), "delivery_status": "SUCCESS"}


def unproject(store, transport, fields, project="P1", schema="v1"):
    record = store.resolve(transport.get("canonical_ref"), project, schema)
    if not set(fields).issubset(record):
        raise ContractRejection("Source schema incomplete")
    return record


def temporal_view(store, commit, allowed_owner=True):
    if commit["status"] == "ACTIVE":
        if not commit.get("owner_ref") or not allowed_owner:
            raise ContractRejection("ACTIVE requires authorized owner")
        if not commit.get("reactivation_condition_ref"):
            raise ContractRejection("ACTIVE requires a legal root")
    if not isinstance(commit.get("linked_entity_refs"), list):
        raise ContractRejection("Missing legal relation set")
    return {"commitment_ref": store.put(commit), "reactivation_root": commit.get("reactivation_condition_ref")}


def legacy_condition_transform(record):
    if record.get("due_at") or record.get("removal_trigger_id") or record.get("revisit_trigger_id"):
        raise ContractRejection("Explicit migration for ANY_OF/ALL_OF requires authoritative composite-root rule")
    return record


def trigger_view(definition):
    mandatory = ("trigger_id", "generation", "fire_policy", "detection_policy", "source_cursors", "reaction_key", "status", "condition_ref")
    if any(not definition.get(f) for f in mandatory):
        raise ContractRejection("Not a full trigger; no invented fire/detection policy")
    return deepcopy(definition)


class TriggerDedup:
    """Reference identity simulation, not durable RDMS-05 dedup implementation."""
    def __init__(self):
        self.events = set()
    def accept(self, project, trigger_id, generation, occurrence):
        k = (project, trigger_id, generation, occurrence)
        if k in self.events:
            return False
        self.events.add(k)
        return True


class ReferenceCapsule:
    """Reference-only publish->ack->suspend state-machine; no actual fsync/DB."""
    def __init__(self):
        self.store = ImmutableRefStore()
        self.suspended = False
        self.published = None
    def publish(self, payload):
        self.published = self.store.put(payload)
        return self.published
    def suspend(self, handle):
        self.store.resolve(handle)
        self.suspended = True
    def restore(self, handle, expected_fields):
        if not self.suspended:
            raise ContractRejection("No legal suspended state")
        payload = self.store.resolve(handle)
        if not set(expected_fields).issubset(payload):
            raise ContractRejection("Cannot reconstruct FCA §53")
        return payload


class Phase11ReferenceVectors(unittest.TestCase):
    """Exactly V01..V18 from phase10 vector ledger, plus independent negatives."""
    def setUp(self):
        self.store = ImmutableRefStore()

    def test_V01_capability_roundtrip(self):
        f = source_fields("CapabilityResult", "FCA v1.0.1:")
        original = fixture(f, specialist_request={"capability": "review"}, rationale_summary="because")
        wire = projection(self.store, original, f)
        self.assertEqual(unproject(self.store, wire, f), original)

    def test_V02_missing_capability_reference_rejects(self):
        f = source_fields("CapabilityResult", "FCA v1.0.1:")
        with self.assertRaises(ContractRejection):
            unproject(self.store, {"delivery_status":"SUCCESS"}, f)

    def test_V03_transport_success_not_cognitive_commit(self):
        f = source_fields("CapabilityResult", "FCA v1.0.1:")
        transport = projection(self.store, fixture(f), f)
        self.assertEqual(transport["delivery_status"], "SUCCESS")
        self.assertNotIn("executive_decision", transport)
        self.assertNotIn("canonical_commit", transport)

    def test_V04_memory_partial_coverage_roundtrip(self):
        f = source_fields("MemoryRetrievalResult", "RDMS-07:")
        original = fixture(f, retrieval_coverage="PARTIAL", omitted_or_filtered_scope=["sensitive"], candidate_refs=["M1","M2"])
        wire = projection(self.store, original, f)
        wire["memory_refs"] = ["M1"]
        self.assertEqual(unproject(self.store, wire, f), original)

    def test_V05_empty_shortlist_not_no_knowledge(self):
        f = source_fields("MemoryRetrievalResult", "RDMS-07:")
        original = fixture(f, retrieval_coverage="PARTIAL", candidate_refs=["M2"], omitted_or_filtered_scope=["policy-filtered"])
        wire = projection(self.store, original, f)
        wire["memory_refs"] = []
        canonical = unproject(self.store, wire, f)
        self.assertEqual(canonical["candidate_refs"], ["M2"])
        self.assertNotEqual(canonical["retrieval_coverage"], "EXHAUSTIVE")

    def test_V06_missing_memory_reference_rejects(self):
        with self.assertRaises(ContractRejection):
            unproject(self.store, {"memory_refs": []}, source_fields("MemoryRetrievalResult", "RDMS-07:"))

    def valid_commitment(self):
        f = source_fields("Commitment", "RDMS-02:Original draft:")
        original = fixture(f, linked_entity_refs=["E1","E2"], status="ACTIVE", owner_ref="Exec", reactivation_condition_ref="root:11", scope={"project":"P1"}, resolution_ref="R1")
        return original

    def test_V07_commitment_semantics_by_ref(self):
        c = self.valid_commitment()
        view = temporal_view(self.store, c)
        self.assertEqual(self.store.resolve(view["commitment_ref"]), c)
        self.assertEqual(c["scope"], {"project":"P1"})

    def test_V08_commitment_relation_cardinality(self):
        c = self.valid_commitment()
        view = temporal_view(self.store, c)
        simplified = {"subject_ref":"E1"}
        self.assertNotEqual(simplified.get("linked_entity_refs"), c["linked_entity_refs"])
        self.assertEqual(self.store.resolve(view["commitment_ref"])["linked_entity_refs"], ["E1","E2"])

    def test_V09_legacy_due_migration_rejects_unsupported(self):
        with self.assertRaises(ContractRejection):
            legacy_condition_transform({"due_at":"2026-11-01","removal_trigger_id":"T1","revisit_trigger_id":"T2"})

    def test_V10_active_requires_owner(self):
        c = self.valid_commitment()
        c["owner_ref"] = None
        with self.assertRaises(ContractRejection):
            temporal_view(self.store, c)

    def valid_trigger(self):
        return {"trigger_id":"T1", "generation":3, "fire_policy":"ONE_SHOT", "detection_policy":"EDGE_TRIGGERED", "source_cursors":{"stream":"c14"}, "reaction_key":"rk1", "status":"armed", "condition_ref":"condition:P7"}

    def test_V11_trigger_full_definition_roundtrip(self):
        source = self.valid_trigger()
        self.assertEqual(trigger_view(source), source)
        self.assertNotEqual(source["fire_policy"], source["detection_policy"])

    def test_V12_predicate_true_not_action_authorization(self):
        pred = {"condition_id":"P7","result":True}
        self.assertNotIn("action_authorization",pred)
        with self.assertRaises(ContractRejection):
            trigger_view(pred)

    def test_V13_missing_axis_rejects(self):
        source = self.valid_trigger()
        del source["detection_policy"]
        with self.assertRaises(ContractRejection):
            trigger_view(source)

    def test_V14_trigger_replay_dedup(self):
        dedup = TriggerDedup()
        self.assertTrue(dedup.accept("P1","T1",3,"occ01"))
        self.assertFalse(dedup.accept("P1","T1",3,"occ01"))
        self.assertTrue(dedup.accept("P1","T1",3,"occ02"))

    def test_V15_capsule_full_FCA_payload_roundtrip(self):
        fields = source_fields("ResumptionCapsule", "FCA v1.0.1:")
        payload = fixture(fields, current_hypotheses=["H1"], rejected_paths=["bad-route"], relevant_evidence=["E1"], next_concrete_action="reassess")
        state = ReferenceCapsule()
        handle = state.publish(payload)
        state.suspend(handle)
        self.assertEqual(state.restore(handle, fields), payload)

    def test_V16_entity_refs_not_equivalent_to_payload(self):
        state=ReferenceCapsule()
        payload={"relevant_entity_refs":["E1","H1"]}
        h=state.publish(payload)
        state.suspend(h)
        with self.assertRaises(ContractRejection):
            state.restore(h, source_fields("ResumptionCapsule", "FCA v1.0.1:"))

    def test_V17_capsule_corruption_quarantine(self):
        state=ReferenceCapsule()
        fields=source_fields("ResumptionCapsule", "FCA v1.0.1:")
        payload=fixture(fields)
        h=state.publish(payload)
        state.suspend(h)
        state.store.records[h["ref"]]["payload"]["goal"]="altered"
        with self.assertRaises(ContractRejection):
            state.restore(h, fields)

    def test_V18_next_proposal_not_dispatched(self):
        state=ReferenceCapsule()
        fields=source_fields("ResumptionCapsule", "FCA v1.0.1:")
        payload=fixture(fields)
        payload["next_action_proposal_ref"]="Proposal-17"
        h=state.publish(payload)
        state.suspend(h)
        self.assertEqual(state.restore(h,fields)["next_action_proposal_ref"],"Proposal-17")
        self.assertNotIn("dispatch_intent",state.store.resolve(h))

    # Extra negative checks, scoped to this reference-only model.
    def test_N01_wrong_project_rejected(self):
        fields=source_fields("CapabilityResult", "FCA v1.0.1:")
        h=projection(self.store,fixture(fields),fields)
        with self.assertRaises(ContractRejection):
            unproject(self.store,h,fields,"P2")

    def test_N02_wrong_schema_rejected(self):
        fields=source_fields("MemoryRetrievalResult", "RDMS-07:")
        h=projection(self.store,fixture(fields),fields)
        with self.assertRaises(ContractRejection):
            unproject(self.store,h,fields,schema="v2")

    def test_N03_capsule_not_suspended_before_ack(self):
        state=ReferenceCapsule()
        self.assertFalse(state.suspended)
        with self.assertRaises(ContractRejection):
            state.suspend({"ref":"missing","project":"P1","schema":"v1","digest":"0"*64})
        self.assertFalse(state.suspended)

    def test_N04_ref_mutation_does_not_mutate_canonical(self):
        fields=source_fields("CapabilityResult", "FCA v1.0.1:")
        h=projection(self.store,fixture(fields),fields)
        record=unproject(self.store,h,fields)
        record["specialist_request"]="tampered"
        self.assertNotEqual(unproject(self.store,h,fields)["specialist_request"],"tampered")

    def test_N05_trigger_other_generation_distinct(self):
        dedup=TriggerDedup()
        self.assertTrue(dedup.accept("P1","T1",1,"occ01"))
        self.assertTrue(dedup.accept("P1","T1",2,"occ01"))

    def test_N06_commitment_cannot_be_active_without_root(self):
        c=self.valid_commitment()
        c["reactivation_condition_ref"]=None
        with self.assertRaises(ContractRejection):
            temporal_view(self.store,c)

    def test_N07_unrepresentable_canonical_field_rejects(self):
        f=source_fields("CapabilityResult", "FCA v1.0.1:")
        rec=fixture(f)
        rec.pop("rationale_summary")
        with self.assertRaises(ContractRejection):
            projection(self.store,rec,f)

    def test_N08_missing_capsule_payload_rejects(self):
        state=ReferenceCapsule()
        fields=source_fields("ResumptionCapsule", "FCA v1.0.1:")
        h=state.publish(fixture(fields))
        state.suspend(h)
        del state.store.records[h["ref"]]
        with self.assertRaises(ContractRejection):
            state.restore(h,fields)


if __name__ == "__main__":
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Phase11ReferenceVectors)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    print("RESULT_JSON="+json.dumps({"tests_run":result.testsRun,"failures":len(result.failures),"errors":len(result.errors),"success":result.wasSuccessful(),"scope":"REFERENCE_ONLY_NO_PRODUCTION_ADAPTERS_OR_DURABLE_STORAGE"}))
    raise SystemExit(0 if result.wasSuccessful() else 1)
