# GAIA-C05 — Cross-interface control guards

**Twelve routes remain under audit.** Four have explicit source-bound mandatory guard sets; eight preserve previous source-schema witnesses, but do not gain unverified signatures. These are not implementation endpoints or proof of atomic production transactions.

| Route | Source-bound guards | Status |
|---|---|---|
| X8-01 | — | FULL_SIGNATURE_HOLD |
| X8-02 | — | FULL_SIGNATURE_HOLD |
| X8-03 | — | FULL_SIGNATURE_HOLD |
| X8-04 | C05-W07, C05-W08, C05-W09 | GUARDS_PROVEN; FULL_SIGNATURE_HOLD |
| X8-05 | C05-W10, C05-W11, C05-W12 | GUARDS_PROVEN; FULL_SIGNATURE_HOLD |
| X8-06 | C05-W04, C05-W05, C05-W06 | GUARDS_PROVEN; FULL_SIGNATURE_HOLD |
| X8-07 | C05-W01, C05-W02, C05-W03 | GUARDS_PROVEN; FULL_SIGNATURE_HOLD |
| X8-08 | — | FULL_SIGNATURE_HOLD |
| X8-09 | — | FULL_SIGNATURE_HOLD |
| X8-10 | — | FULL_SIGNATURE_HOLD |
| X8-11 | — | FULL_SIGNATURE_HOLD |
| X8-12 | — | FULL_SIGNATURE_HOLD |

## X8-04

- Precondition: QualifiedOccurrenceIdentity bound to TriggerDefinitionSnapshot
- Durability: One ControlCommit: TriggerEvaluation/Fire/ReactionIntent/ProcessingCursor
- Failure: Unknown evaluation saves retry obligation before advancing cursor
- Original text: `GAIA_C05_VERIFIED_DELTA_REGISTER.md` / C05-W07, C05-W08, C05-W09.

## X8-05

- Precondition: Verified durable capsule before SUSPENDED
- Durability: Payload durable, then one ControlCommit with lifecycle and obligations
- Failure: Corrupted capsule -> INVALID/UNKNOWN; no automatic shell replay
- Original text: `GAIA_C05_VERIFIED_DELTA_REGISTER.md` / C05-W10, C05-W11, C05-W12.

## X8-06

- Precondition: Action/attempt/dispatch distinct; current owner and epoch
- Durability: Claimed dispatch ownership, durable DISPATCH_INTENT before external mutation
- Failure: Ambiguous effect -> IN_DOUBT/reconciliation; not speculative exactly-once
- Original text: `GAIA_C05_VERIFIED_DELTA_REGISTER.md` / C05-W04, C05-W05, C05-W06.

## X8-07

- Precondition: Raw observation carries immutable trust context; no authority from content
- Durability: Observation amendment is explicit separate canonical record
- Failure: EvidenceBasis invalid when required observations unusable
- Original text: `GAIA_C05_VERIFIED_DELTA_REGISTER.md` / C05-W01, C05-W02, C05-W03.

## Gate preserved

All routes still need a single approved source-backed producer/consumer contract, required/optional fields, identity and authority binding, failure transitions and durable handoff proof. Global L0-L7 freeze remains HOLD.