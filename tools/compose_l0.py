"""Compose the foundational document from its approved single frozen FCA baseline."""
from render_layer import DATA, fca, header, imports, retained, source_link, write

parts = [header("L0", "L0 owns architectural identity, constitutional authority, trust boundaries, normative language and change control. Layer-specific FCA contracts belong to their respective owner layers; L0's cross-cutting principles do not duplicate their record ownership.", "FOUNDATIONAL ARTICLES VERIFIED AGAINST FCA v1.0.1")]
parts.append(imports([
    ("ControlCommit, Control Ledger, ProjectHead and epoch fencing", "L1", "Use the single control durability boundary; the foundation grants no direct provider writes."),
    ("Cognitive workspace, Claim/Goal/Decision/Commitment and Executive", "L2", "Preserve semantic authorization, typed epistemic states and hard-law constraints."),
    ("Observation/EvidenceLink, ActionGate and Action Journal", "L3", "Preserve independent observation ingress, evidence grounding and world-action authority."),
    ("TriggerCondition, specialist contracts and dependency evaluation", "L4", "Preserve one mind, scoped temporary specialists and one freshness authority."),
    ("MemoryProposal and MemoryRetrievalResult", "L5", "Preserve learning governance and retrieval-as-precedent semantics."),
    ("ResumptionCapsule and suspension/resumption/recovery admission", "L6", "Require durable, integrity-checked recovery context and lawful resumption."),
    ("Provider envelopes, trusted integration and transport projections", "L7", "Transport carries source-owned legal meaning and confers no new authorization."),
]))
parts.append("## Current foundational law\n\nThe following articles retain only the current frozen FCA v1.0.1 units allocated to L0. Their source-section wording is preserved; they are not historical RDMS drafts or unreviewed GAIA substitutions.\n\n")
for number in [0, 1, 2, 3, 4, 20, 21, 72, 73, 84, 87]:
    parts.append(retained(fca(number), f"L0-F{number:02d}"))
for appendix in DATA.get("fca_appendices",[]):
    if appendix["section"] in {"C","F","G"}:
        parts.append(retained(appendix,"L0-APP-"+appendix["section"]))
parts.append("## Cross-cutting invariant responsibilities\n\n")
for inv in DATA["fca_invariants"]:
    if inv["unit_id"] in {"FCA-I01", "FCA-I16", "FCA-I24", "FCA-I25", "FCA-I40", "FCA-I41"}:
        parts.append(inv["raw"] + "\n\nSource: " + source_link(inv) + ".\n\n")
parts.append("## Source coverage, exports and verification\n\nL0 exports the constitutional authority and trust obligations above to L1–L7. ContentEnvelope is owned here; owner-specific record refinements remain in the relevant layer. FCA §§0–4, 20–21, 72–73, 84 and 87 are incorporated with exact source units. §86 is a historical source freeze verdict, retained by reference rather than asserted as a new consolidated freeze. Appendix A and the Studies trace explain provenance; Appendix B is explicitly non-normative; Appendices C/F/G constrain authority and conformance without creating duplicate contract owners; Appendix D is the L2 composite view; Appendix E records approved FCA history. Layer-specific FCA sections, decimal subsections and remaining invariants are allocated in the architecture manifest/trace ledger.\n\n")
parts.append("Source freeze evidence: " + source_link(fca(86)) + ". FCA's v1.0.1 header and §0 explicitly establish precedence over the v1.0 historical baseline. No RDMS or GAIA artifact is admitted as a constitutional amendment. Verification checks the incorporated source-unit hashes, preserved source archive, single ContentEnvelope owner, imported-owner references and absence of independent provider authority. Consolidated freeze remains HOLD pending independent review and remaining layer/interface issues.\n")
write("L0", "\n".join(parts))
print("Rendered architecture/L0_FOUNDATION.md")
