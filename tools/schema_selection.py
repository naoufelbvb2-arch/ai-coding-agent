"""Source-declaration selection and explicitly scoped field overlays for documentation."""
import re
from render_layer import DATA, message, source_link

OWNERS = {"FCA": "L0", "RDMS-01": "L1", "RDMS-02": "L2", "RDMS-03": "L3", "RDMS-04": "L3",
          "RDMS-05": "L4", "RDMS-06": "L4", "RDMS-07": "L5", "RDMS-08": "L2", "RDMS-09": "L6", "RDMS-10": "L7"}
SPECIAL = {"CapabilityResult": ("FCA", "L2"), "MemoryRetrievalResult": ("RDMS-07", "L5"),
           "Commitment": ("RDMS-02", "L2"), "ResumptionCapsule": ("RDMS-05", "L6"),
           "ResumeAssessment": ("RDMS-05", "L6"), "DependencyStamp": ("RDMS-06", "L4")}
FCA_OWNERS = {"ContentEnvelope": "L0", "LeadershipGrant": "L1", "Identity": "L2", "FocusState": "L2",
              "SystemMentalModel": "L2", "State": "L2", "SemanticChangeProposal": "L2", "ConfidenceProfile": "L3",
              "ActionLifecycle": "L3", "Specialist": "L4", "MemoryMetadata": "L5"}
RETIRED = {"CanonicalEntity": "RDMS-02 C01-01 removes generic lifecycle and replaces common metadata with CanonicalEntityMeta",
           "GoalStack": "RDMS-02 C01-10 explicitly replaces fixed GoalStack with GoalPath",
           "LedgerHead": "RDMS-01 R1 ProjectHead/current-store model replaces the original ledger-only head",
           "RuntimeStatus": "RDMS-01 R1 §24 splits durable project and process mode"}


def field_replace(raw, name, new=""):
    lines = raw.splitlines()
    start = next(i for i, line in enumerate(lines) if re.match(r"^    " + re.escape(name) + r"(?:\??(?:\[\])?\??)(?::|\s*$)", line))
    end = start + 1
    while end < len(lines) - 1:
        if lines[end].strip() and (not lines[end].startswith("        ") or lines[end].strip() == "}"):
            break
        end += 1
    replacement = new.rstrip().splitlines() + [""] if new else []
    return "\n".join(lines[:start] + replacement + lines[end:])


def add_fields(raw, text):
    return raw.rstrip()[:-1].rstrip() + "\n\n" + text.rstrip() + "\n}"


def select():
    declarations = DATA["fca_declarations"] + [d for m in DATA["messages"] for d in m["declarations"]]
    groups = {}
    for item in declarations:
        name = item["name"]
        if item["specification"] == "RDMS-10" and name in {"CapabilityResult", "MemoryRetrievalResult"}:
            name = name.replace("Result", "TransportResult")
        groups.setdefault(name, []).append(item)
    registry = []
    for name, items in sorted(groups.items()):
        sources = {item["specification"] for item in items}
        if name in SPECIAL:
            source, owner = SPECIAL[name]
        elif name.endswith("TransportResult"):
            source, owner = "RDMS-10", "L7"
        else:
            source = max(sources, key=lambda s: int(s.split("-")[1]) if s.startswith("RDMS-") else -1)
            owner = OWNERS[source] if source != "FCA" else FCA_OWNERS.get(name, "L2")
        candidates = [item for item in items if item["specification"] == source and not item["partial_or_example"]]
        unique = {item["raw_sha256"]: item for item in candidates}
        selected = candidates[-1] if candidates else None
        registry.append({"type": name, "source_declared_name": selected["name"] if selected else items[-1]["name"],
                         "owner": owner, "owning_specification": source, "candidates": items,
                         "selected": selected, "effective_raw": selected["raw"] if selected else None,
                         "explicit_overlays": [], "status": "SOURCE_RECORD_SURFACE" if selected else "PARTIAL_SOURCE_DECLARATION_ONLY",
                         "distinct_native_surfaces": len(unique), "parent_or_projection_variance": len({i["raw_sha256"] for i in items}) > 1,
                         "interface_signature_ratified": False})
        record = registry[-1]
        if name in RETIRED:
            record["status"] = "SUPERSEDED_HISTORICAL_DECLARATION"
            record["retired_by"] = RETIRED[name]
        if name == "Commitment":
            baseline = next(x for x in items if x["specification"] == "RDMS-02" and x["source_part"] == "Original draft" and not x["partial_or_example"])
            raw = baseline["raw"]
            for old in ["due_at", "removal_trigger_id", "revisit_trigger_id"]:
                raw = field_replace(raw, old)
            raw = add_fields(raw, "    reactivation_condition_ref")
            record.update({"selected": baseline, "effective_raw": raw, "status": "EXPLICIT_SCOPED_OVERLAY_APPLIED",
                           "explicit_overlays": ["RDMS-02 C01-32 removes due_at/removal_trigger_id/revisit_trigger_id and adds reactivation_condition_ref; all other baseline fields retained", "RDMS-05 C01-01 preserves RDMS-02 ownership and prohibits alternative lifecycle"]})
            record["parent_conformance_disposition"] = "RESOLVED_WITHDRAWN_RDMS05_RIVAL_DECLARATION; import exact RDMS-02 owner contract under RDMS-05 C01-01"
        if source == "RDMS-02" and selected and name not in RETIRED:
            raw = record["effective_raw"]
            changes = []
            if re.search(r"^    superseded_by\?", raw, re.M):
                raw = field_replace(raw, "superseded_by")
                changes.append("RDMS-02 C01-19 removes authoritative scalar superseded_by; use independently owned EntityLineageEdge")
            if name in {"Claim", "Hypothesis"}:
                raw = field_replace(raw, "support", "    current_support_assessment_ref?")
                if name == "Claim":
                    raw = field_replace(raw, "support_assessed_at_commit")
                else:
                    raw = field_replace(raw, "competing_hypothesis_ids")
                    raw = field_replace(raw, "status", "    lifecycle:\n        ACTIVE\n        REJECTED\n        CONFIRMED\n        SUPERSEDED")
                    raw = add_fields(raw, "    closure_ref?")
                    changes.append("RDMS-02 C01-07/20 replaces hypothesis lifecycle, adds closure_ref and externalizes authoritative hypothesis relations")
                changes.append("RDMS-02 C01-02 moves support conclusion and its commit/dependencies into SupportAssessment")
            if name == "OperationalCausalClaim":
                raw = field_replace(raw, "status", "    status:\n        OPERATIONALLY_VERIFIED\n        CONTRADICTED\n        SUPERSEDED")
                changes.append("RDMS-02 C01-08 explicitly removes STALE from canonical lifecycle; OVCUsability is derived")
            if name == "Goal":
                raw = raw.replace("    priority:", "    declared_priority:")
                raw = raw.replace("        OBSOLETE\n", "        OBSOLETE\n        CANCELLED\n")
                changes += ["RDMS-02 C01-11 adds CANCELLED with cancellation_reason/authority conditions", "RDMS-02 C01-14 renames priority to declared_priority"]
                record["conditional_fields"] = {"CANCELLED": ["cancellation_reason", "cancellation_authority_ref"]}
            if name == "Decision":
                raw = add_fields(raw, "    dependency_set_ref?\n    validity_conditions[]")
                changes.append("RDMS-02 C01-16 explicitly adds dependency_set_ref? and validity_conditions[]; no REVIEW_REQUIRED lifecycle")
            if name == "AcceptanceCriterion":
                raw = add_fields(raw, "    waiver_ref?")
                changes.append("RDMS-02 C01-12 partial overlay adds waiver_ref?; baseline non-superseded fields retained")
            if name == "Slice":
                raw = field_replace(raw, "status")
                raw = field_replace(raw, "base_state_version", "    planned_from_commit_seq\n    dependency_set_ref")
                changes += ["RDMS-02 C01-21 explicitly abolishes single giant status enum; separately owned SliceState carries stage/condition/terminal", "RDMS-02 C01-25 removes base_state_version and replaces freshness basis with planned_from_commit_seq/dependency_set_ref/base_repo_ref"]
                record["state_contract"] = "SliceState"
                record["state_embedding_field"] = "UNSPECIFIED_BY_SOURCE; no new field spelling invented"
            if changes:
                record["effective_raw"] = raw
                record["explicit_overlays"] += changes
                record["status"] = "EXPLICIT_SCOPED_OVERLAY_APPLIED"
        if len(unique) > 1 and not record["explicit_overlays"] and name not in RETIRED:
            record["status"] = "MULTIPLE_NATIVE_SURFACES_REQUIRE_SCOPED_RECONCILIATION"
        if name == "Risk":
            baseline = next(x for x in items if x['source_part'] == 'Original draft' and not x['partial_or_example'])
            raw = field_replace(baseline['raw'], 'status',
                '    lifecycle:\n        OPEN\n        MITIGATED\n        REALIZED\n        OBSOLETE\n\n'
                '    treatment:\n        UNASSESSED\n        MONITOR\n        MITIGATE\n        ACCEPT\n        AVOID')
            raw = add_fields(raw, '    current_assessment_ref?')
            record.update(selected=baseline, effective_raw=raw, status='EXPLICIT_SCOPED_OVERLAY_APPLIED')
            record['explicit_overlays'].append('RDMS-02 C01-30 splits status into lifecycle/treatment and adds current_assessment_ref; the ellipsis retains all unrelated baseline fields. No historical state migration or likelihood/impact alias is ratified.')
        if name in {'ContainmentProof', 'TriggerFire'}:
            # C01 scoped native restatements; remaining parent projection
            # questions are not closed by selecting a newer record.
            approved = next(x for x in candidates if x['source_part'].startswith('C01'))
            record.update(selected=approved, effective_raw=approved['raw'],
                          status='SOURCE_RECORD_SURFACE_WITH_EXPLICIT_REPLACEMENT')
            record['explicit_overlays'].append(
                'RDMS-04 C01-27/28 binds effective containment; original reachable-effect isolation duties remain required.'
                if name == 'ContainmentProof' else
                'RDMS-05 C01-12/13/14 replaces unstable fire construction with frozen definition and qualified occurrence identity; C01-06 governs atomic durable processing.')
        if source == "RDMS-01" and name in {"ControlCommit", "ControlEvent", "Snapshot", "IndexMetadata", "RepoRef"}:
            record["status"] = "SOURCE_RECORD_SURFACE_WITH_EXPLICIT_REPLACEMENT"
            record["explicit_overlays"].append("RDMS-01 R1 replaces this native declaration; FCA event metadata still applies and CE-01 remains open")
        if source == "RDMS-02" and name in {"CanonicalFocusState", "MentalModelElement"}:
            record["status"] = "SOURCE_RECORD_SURFACE_WITH_EXPLICIT_REPLACEMENT"
            record["explicit_overlays"].append("RDMS-02 C01-26/27 expressly replaces this native record; parent obligations are not automatically waived")
        if source == "RDMS-02" and name == "Invariant":
            record["effective_raw"] = field_replace(record["effective_raw"], "enforcement_modes", "    enforcement_specs[]")
            record["status"] = "EXPLICIT_SCOPED_OVERLAY_APPLIED"
            record["explicit_overlays"].append("RDMS-02 C01-28 replaces enforcement mode collection with EnforcementSpec collection")
        if source == "RDMS-03" and name == "ObservationAmendment":
            record["status"] = "SOURCE_RECORD_SURFACE_WITH_EXPLICIT_REPLACEMENT"
            record["explicit_overlays"].append("RDMS-03 C01-07 expressly replaces ObservationAmendment")
        if source == "RDMS-03" and name == "Observation":
            record["effective_raw"] = add_fields(record["effective_raw"], "    trust_context_ref\n    normalization_profile_ref?\n    evidence_origin_group_ref")
            record["status"] = "EXPLICIT_SCOPED_OVERLAY_APPLIED"
            record["explicit_overlays"].append("RDMS-03 C01-01/06/15 explicitly adds these fields; C01-21 also requires associated TemporalProvenance, without freezing an embedding field spelling")
            record["associated_contracts"] = ["TemporalProvenance"]
        if source == "RDMS-03" and name == "SemanticAssessment":
            record["effective_raw"] = record["effective_raw"].replace("BLOCK_CANDIDATE", "BLOCK_RECOMMENDED")
            record["status"] = "EXPLICIT_SCOPED_OVERLAY_APPLIED"
            record["explicit_overlays"].append("RDMS-03 C01-43 expressly renames advisory BLOCK_CANDIDATE to BLOCK_RECOMMENDED")
        if source == "RDMS-03" and name == "EvidenceLink":
            record["status"] = "UNSPECIFIED_ASSOCIATED_CONTRACT_EMBEDDING"
            record["associated_contracts"] = ["EvidenceBasis", "VersionedEntityRef<AuthorityBinding> when AUTHORITATIVE"]
            record["explicit_overlays"].append("RDMS-03 C01-04/10–13 requires pinned authority and structured basis; exact replacement embedding for observation_refs is not declared")
        if source == "RDMS-03" and name == "VerificationRecord":
            record["effective_raw"] = record["effective_raw"].replace("    verification_spec_ref\n", "    verification_spec_ref:\n        VersionedEntityRef<VerificationSpec>\n", 1)
            record["status"] = "EXPLICIT_SCOPED_OVERLAY_APPLIED"
            record["explicit_overlays"].append("RDMS-03 C01-35 pins VerificationSpec without dropping other baseline fields; C01-36 requires associated VerificationExecutionContext without specifying an embedding field")
            record["associated_contracts"] = ["VerificationExecutionContext"]
        if name == "ProjectRuntime":
            record["status"] = "UNSPECIFIED_ASSOCIATED_CONTRACT_EMBEDDING"
            record["associated_contracts"] = ["ProjectHead", "ProjectStatus", "ProcessRuntimeMode"]
            record["explicit_overlays"].append("RDMS-01 R1 replaces the head/status model; PR-01 records the unspecified aggregate field representation")
        if name == "ProcessExecutionRequest":
            record["effective_raw"] = field_replace(record["effective_raw"], "mode")
            record["status"] = "EXPLICIT_SCOPED_OVERLAY_APPLIED"
            record["associated_contracts"] = ["ProcessLaunch"]
            record["explicit_overlays"].append("RDMS-04 C01-11 replaces exclusive EXEC/PTY/SERVICE mode with orthogonal ProcessLaunch dimensions; other baseline fields are retained and no new embedding field is invented")
        if name == "TriggerSourceCursor":
            record["status"] = "UNSPECIFIED_ASSOCIATED_CONTRACT_EMBEDDING"
            record["associated_contracts"] = ["IngressCursor", "TriggerProcessingCursor"]
            record["explicit_overlays"].append("RDMS-05 C01-05 separates durable ingress and legal trigger-processing frontiers; original TriggerSourceCursor must not conflate them")
        if record["status"].startswith(("PARTIAL","MULTIPLE","UNSPECIFIED")) or record["status"]=="SUPERSEDED_HISTORICAL_DECLARATION":
            record["effective_raw"] = None
    return registry


REGISTRY = select()


def schemas(layer, exclude=()):
    result = "## Single-owner record contracts\n\nThe owner registry distinguishes source record declarations from callable or transport signatures. Source fields marked `?` retain optionality and `[]` retain collection shape; primitive types not declared by the source remain unspecified. An abbreviated `...` correction is not permission to discard other fields. Multi-surface or parent-field preservation questions are explicitly bounded below; their declarations must not be treated as a proved conversion API.\n\n"
    for item in REGISTRY:
        if item["owner"] != layer or item["type"] in exclude or item["status"] == "SUPERSEDED_HISTORICAL_DECLARATION":
            continue
        result += f"### {item['type']}\n\nCanonical owner: {layer}; defining specification: {item['owning_specification']}.\n\n"
        if item["selected"]:
            result += "Source: " + source_link(item["selected"]) + "; declaration SHA-256 `" + item["selected"]["raw_sha256"] + "`.\n\n"
        if item["status"] in {"MULTIPLE_NATIVE_SURFACES_REQUIRE_SCOPED_RECONCILIATION", "PARTIAL_RISK_OVERLAY_WITH_REQUIRED_BASELINE_PRESERVATION", "PARTIAL_SOURCE_DECLARATION_ONLY", "UNSPECIFIED_ASSOCIATED_CONTRACT_EMBEDDING"}:
            result += "**Record-shape reconciliation remains OPEN.** The operative rules in this document apply; no complete replacement declaration is asserted. Every exact candidate and its field spelling remains in the source registry; this prevents a historical or partial declaration from being published as current complete law.\n\n"
            for candidate in item["candidates"]:
                result += "- " + source_link(candidate, candidate["source_part"]) + "; SHA-256 `" + candidate["raw_sha256"] + "`.\n"
            result += "\n"
            continue
        if item["effective_raw"]:
            display = item["effective_raw"]
            if item["type"] != item["source_declared_name"]:
                display = display.replace(item["source_declared_name"] + " {", item["type"] + " {", 1)
                result += "Editorial transport label only; the archived RDMS-10 spelling remains unchanged. Canonical owner semantics and lossless reference/payload obligations are mandatory; alias naming is not field mapping approval.\n\n"
            result += "```text\n" + display + "\n```\n\n"
        if item["explicit_overlays"]:
            result += "Scoped amendment effects:\n\n" + "\n".join("- " + effect for effect in item["explicit_overlays"]) + "\n\n"
        if item.get("conditional_fields"):
            result += "Conditionally mandatory fields: " + repr(item["conditional_fields"]) + ". These are textual source conditions, not invented optional serializer fields.\n\n"
        if item.get("state_contract"):
            result += "State contract: `SliceState`; the source does not freeze a new embedding field name. Its stage/condition/terminal obligations remain mandatory.\n\n"
        if item.get("associated_contracts"):
            result += "Mandatory associated contracts: " + ", ".join(item["associated_contracts"]) + ". Association does not invent a serialization field name.\n\n"
        if item.get("parent_conformance_disposition"):
            result += item["parent_conformance_disposition"] + ".\n\n"
        elif item["parent_or_projection_variance"]:
            result += "Parent/other-source declarations have different record surfaces. The registry retains their exact clauses; preserving the parent semantic obligations is mandatory, and field-renaming/conversion is not automatically approved.\n\n"
    return result
