# GAIA-C06 — Twelve Interface Evidence Matrix

**EVIDENCE ONLY, NOT VERIFIED PUBLIC API SIGNATURES.** New source evidence is added for routes formerly lacking guards. Never infer a world-atomic transaction from a canonical ControlCommit.

| Route | Existing C05 guard witnesses | Added C06 source witnesses | Full signature |
|---|---|---|---|
| X8-01 | — | — | HOLD |
| X8-02 | — | C06-W03 | HOLD |
| X8-03 | — | — | HOLD |
| X8-04 | C05-W07, C05-W08, C05-W09 | C06-W15 | HOLD |
| X8-05 | C05-W10, C05-W11, C05-W12 | — | HOLD |
| X8-06 | C05-W04, C05-W05, C05-W06 | C06-W12 | HOLD |
| X8-07 | C05-W01, C05-W02, C05-W03 | C06-W13 | HOLD |
| X8-08 | — | — | HOLD |
| X8-09 | — | — | HOLD |
| X8-10 | — | C06-W01, C06-W02, C06-W07 | HOLD |
| X8-11 | — | C06-W04, C06-W05, C06-W11, C06-W14 | HOLD |
| X8-12 | — | C06-W08, C06-W09, C06-W10 | HOLD |

## Remaining architecture publication gates

- Complete typed command/response contracts: required fields, producer/consumer, authority proof, project/epoch/version, idempotency, pre/post-conditions, error and reconciliation states.
- Distinguish atomic legal ledger writes from external-world effects and cross-store repairable handoffs.
- Distinguish a source clause containing a guard from an approved integration signature connecting two components.
- Explain each source-to-corrected-clause relation and effective text with no missing correction or silent field deletion.
- Do not claim real runtime tests, storage semantics, or code implementation from this review.