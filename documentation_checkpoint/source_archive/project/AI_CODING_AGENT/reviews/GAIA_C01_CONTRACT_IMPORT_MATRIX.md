# GAIA-C01 Phase 3 — Canonical contract compatibility register

**Status:** preliminary mapping table, NOT final RDMS-to-RDMS compatibility certification. FCA §23 is the only exact canonical CapabilityResult verified here.

| Contract / lifecycle | Canonical parent (known) | Owning layer target | Exact RDMS verified? | Collision / review task |
|---|---|---|---|---|
| `CapabilityResult` semantic | FCA §23 | L2 | NO, RDMS-10 source pending | GAIA-B01: forbid redefinition; proposed `CapabilityTransportResult` |
| `LeadershipGrant`, epoch fencing | FCA §50 | L1 | NO, RDMS-01 pending | Verify schema/operation admission and fencing |
| `ActionProposal`, `ActionEffectSemantics` | FCA §§42–43 | L3 | NO, RDMS-04 pending | Verify exactly which effect fields and retry categories are normative |
| `ActionLifecycle`, `ActionRecord` | FCA §§44–46 | L3 | NO, RDMS-04 pending | Control Ledger + Journal atomic correspondence |
| `Trigger` and reaction identity | FCA §§55–56 | L4 | NO, RDMS-05 pending | Reconstructable derived continuation |
| `Specialist` and lifecycle | FCA §65 | L4 | NO, RDMS-06 pending | Scope, sandbox and integration |
| `DependencyStamp` & freshness | FCA §§69–71 | L4 | NO, RDMS-06 pending | VALID/STALE/PARTIALLY_STALE/UNKNOWN |
| `MemoryProposal` and learned memory | FCA §§58–62 | L5 | NO, RDMS-07 pending | Promotion and derived suppression |
| Recovery protocol | FCA §§48–52, 82 | L6 | NO, RDMS-09 pending | Restricted activation and epoch adoption |
| Transport and sealed envelopes | FCA §72 plus RDMS-10 discussions | L7 | NO, RDMS-10 pending | No self-authenticating authority or lossy projection |

## Formal closeout rules

- Exact source match means identical semantic field domains, transition preconditions, control ownership and recovery behavior; matching type names alone does not qualify.
- If a contract needs a new name, register it as an integration projection and document the converter input/output/failure behavior.
- No duplicate legal type definitions across layer documents, even when their data shapes happen to match.
- Keep all original sources immutable and put corrective discussions under `reviews/`.
