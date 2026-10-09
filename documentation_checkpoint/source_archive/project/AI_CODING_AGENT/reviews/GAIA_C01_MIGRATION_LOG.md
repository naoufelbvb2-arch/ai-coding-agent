# GAIA-C01 — Canonical Architecture Consolidation Migration Log

## Baseline
- User-approved reorganization: L0…L7, one canonical **future** layer document each, preserve historical design as archives.
- Existing source: frozen FCA v1.0.1, **byte-for-byte copied**, SHA-256 verified `74d0923cbd343b71740da0fc2368a84aad2ea97f8e4e15f156122f48ebe53539`.
- Existing partial design: RDMS-10 Draft, C01, C02 and review decisions in conversation; RDMS-09 summarized with design details.
- Missing primary artifacts: frozen RDMS-01…09 originals; RDMS-10 final exact primary exported text. They were not invented and must be imported later.

## Actions carried out
1. Created the exact `architecture/` layer filenames agreed with the user.
2. Added type ownership registry, authority gates, dependency and source trace in architecture manifest.
3. Wrote self-contained **working consolidation drafts** grounded in FCA and reviewed conversation architecture.
4. Kept source FCA unchanged under `reviews/source_archive/`.
5. Created empty `src/agent/` and `tests/` scaffolding without source code, tests or runnable system.
6. Recorded GAIA-B01 collision and a proposed nonbreaking transport rename.

## Open issues
- GAIA-B01 verified: `CapabilityResult` name collision. RDMS-10 frozen source still needs an authorized corrective amendment and exact converter checks.
- GAIA-B02: missing RDMS source texts prevent full field-level verification.
- Exact Action Journal/Control Ledger legal owner and atomic transaction projection must be audited against RDMS-01/04 originals.
- Original Trigger lifecycle vs durable derived continuation to be compared with RDMS-05.
- Memory suppression/lineage schema vs recovery to be compared with RDMS-07/09.
- Layer type migrations must not create a second authority or change a frozen schema by implication.

## Status
GAIA-C01 STRUCTURAL CONSOLIDATION INITIAL PASS / NOT COMPLETE.
No repository code modified. No executable tests. No consolidated layer frozen. No implementation authorization.

---

## Phase 2 — Primary FCA source preservation and exact layer allocation

- Enumerated **88/88** FCA main sections and **7/7** appendices; each assigned once to an L0–L7 source annex.
- Copied original sections without paraphrasing; each block has a SHA-256 evidence marker.
- See `GAIA_C01_FCA_TRACEABILITY.md` for per-section ownership and integrity.
- Added `GAIA_C01_CONTRACT_COLLISION.md` detailing lossless field mapping for the FCA/RDMS-10 `CapabilityResult` collision.
- Added `GAIA_C01_SOURCE_INVENTORY.md` explicitly listing missing normative RDMS sources.
- **No RDMS-01…09 exact source text was invented.** Existing frozen FCA file remains unchanged.
- No production code or runnable tests implemented.
- GAIA-B01 remains PROPOSED, GAIA-B02 remains SOURCE MISSING.


## Phase 3 — exact source recovery
- Searched attached Project files, Library and connected GitHub repo inventory for RDMS source documents. No authoritative final RDMS-01…09 primary source found.
- Created source recovery protocol, normative source registry, and canonical contract candidate mapping; none are frozen legal schemas.
- All eight layer docs remain provisional; source archive and any `src/agent/` production source remain unchanged.
