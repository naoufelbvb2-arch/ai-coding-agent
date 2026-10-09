<!-- GAIA-C01-PHASE13-CURRENT-STATUS START -->
# CURRENT READING GUIDE — GAIA-C01 Phase 13

**STATUS: CONSOLIDATION DRAFT; NOT FROZEN.**  
**Owned responsibility:** Constitutional authority and trust principles.  
**Source rule:** Full original normative texts remain unmodified in the archived source set and the source annex of this document. A historical draft is NOT automatically the effective current law: approved C01/C02/C03 corrections and final freeze decisions must be incorporated before the consolidated layer supersedes those sources. Phase 11 reference tests are not production/runtime verification.  
**Forbidden:** silent defaulting, missing-authority inference, lossy migration, or treating transport wrappers as canonical entities.

**FCA source sections/appendices assigned:** 19.  
**RDMS source sets assigned:** 0; **approved original message parts:** 0.  
**27-name ownership subset present here:** 0.

| Attached RDMS source | Original message parts | Source interpretation |
|---|---:|---|
| — | — | FCA constitutional source |

| Canonical-type ownership candidate | Source | Current migration decision |
|---|---|---|
| — | — | No audited reused-name contract owned here |

**Freeze blocker:** An independently usable, contradiction-free, *effective* contract and law text has not yet been consolidated from draft plus correction overlays. See `../reviews/GAIA_C01_PHASE13_FREEZE_REVIEW_AR.md`, `GAIA_C01_PHASE13_LAYER_COVERAGE.json`, and the Phase-12 contract decision register. Runtime validation belongs to a separate implementation stage; existing architectural ambiguities cannot be waived by deferring tests.
<!-- GAIA-C01-PHASE13-CURRENT-STATUS END -->

---

<!-- GAIA-C01-PHASE12-DECISION-INDEX START -->
## GAIA-C01 Phase 12 — Effective owner & change-control index (DRAFT)

**Not a new frozen law.** Original source sections and approved overlays below retain authority. Do not infer legal equivalence of transport projections or historical migrations. Global layer freeze remains unauthorized.

**Source-owned reused contracts in this layer:** 0.

No repeated-name contracts from the 27-name audit are owned here; other original legal entities remain in the source annex below.

Refer to `../reviews/GAIA_C01_PHASE12_CONTROLLED_CONTRACT_DECISIONS.md` and the JSON decision ledger for exact source anchors and remaining proof gates.
<!-- GAIA-C01-PHASE12-DECISION-INDEX END -->

---

<!-- GAIA-C01-PHASE9 CONTRACT PUBLICATION START -->
## GAIA-C01 Phase 9 — Curated source-backed contract publication (NOT RE-FROZEN)

**Status: VERBATIM SOURCE BASELINES ONLY — effective cross-layer projections remain unapproved.**

This section is a navigation and source-publication aid. It does not overwrite historical FCA or RDMS source sections. Corrections/overlays must be applied according to the approved original source history, not inferred from an earlier draft.

**Owning layer:** `L0`. **Published reused names:** `0`.

No audited duplicate canonical data type in the 27-name registry is primarily owned by this layer. Consult the original FCA/RDMS source annex below for this layer’s other definitions.

**Publication guard:** No inferred fields, default values, status promotions, action permissions, or silent renames are authorized by this section.
<!-- GAIA-C01-PHASE9 CONTRACT PUBLICATION END -->


---

# L0 — Foundation & Constitutional Contracts

> **CONSOLIDATION DRAFT — NOT FROZEN.** This file is a working per-layer consolidation, **not** an independently approved replacement for the frozen FCA/RDMS source specifications. Normative FCA source: `../reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md` (SHA-256 `74d0923cbd343b71740da0fc2368a84aad2ea97f8e4e15f156122f48ebe53539`). RDMS-01…10 original source sets arrived in GAIA-C01 Phase 4. Effective cross-source schemas and ownership remain **PENDING RECONCILIATION**; the archived original text below is untouched.

> **Phase 5:** source-name audit and non-normative proposals: `../reviews/GAIA_C01_PHASE5_CONTRACT_RECONCILIATION.md`. Original FCA and RDMS annexes below retain their historical authority/status; proposed aliases are not approved laws.

**Layer owner:** FCA constitutional principles  
**Authoritative FCA trace:** FCA §§0–4, 19–21, 41–45, 48–52, 72–78, 84, 86–87  
**Migration status:** CONSOLIDATED DRAFT / REVIEW REQUIRED  
**Source status:** FCA v1.0.1 hash-verified; RDMS source sets imported; effective contract reconciliation pending.

## 1. Scope and charter

The foundation is the constitutional reference for the agent. It is **not** another owner of the persistence engine, action executor, or memory store. The project identity is **one persistent canonical cognitive system** with optional temporary specialists and replaceable reasoning providers.

## 2. Fundamental identity

> Agent = persistent cognitive state + Executive control + capabilities + memory + control/action/observation runtime + tools/reality + reasoning providers + temporary specialists.

The provider proposes; deterministic machinery enforces machine-checkable constraints; external reality supplies observations; the current Executive gives semantic authorization. The provider cannot directly mutate canonical state or production resources.

## 3. Four planes

| Plane | Purpose | Rule |
|---|---|---|
| Cognitive | Executive, Workspace, capabilities, reasoning, memory views | Cannot bypass legal write paths |
| Control | Epoch, CommitGate, ActionGate, Control Ledger and lifecycle guards | Enforces authoritative transitions |
| Action | Journal, Reality Executor, isolated workspaces | Durable intent before shared-world dispatch |
| Observation | Source-validated ingress and evidence provenance | Records source events separately from interpretation |

Physical packaging of these planes is not mandated: a modular monolith with separate risky execution domains is an allowed integration candidate, not a frozen FCA requirement.

## 4. Normative authority boundaries

| Authority | Owner | Cannot delegate to |
|---|---|---|
| Semantic canonical mutation approval | Current Executive epoch | Provider, specialist, tool |
| Hard legal canonical mutation | CommitGate | Unvalidated direct writer |
| Shared-world mutation | Executive + ActionGate + Action protocol | Prompt instructions, Queue |
| Raw observation append | Observation Ingress with schema/provenance/integrity | Generated speculation |
| Knowledge promotion | Learning Gate + Executive | Automatic memory summary |
| Recovery | RDMS-09 under authoritative control state | Shadow Executive |

## 5. Legal paths

```text
CognitivePatch → Executive authorization → CommitGate → canonical state/control commit
ActionProposal → Executive authorization → ActionGate → durable AUTHORIZED
               → durable DISPATCH_INTENT → Executor → Observation → Reconciliation
Reality/Source → Observation Ingress → immutable raw observation → epistemic assessment
Episode → Reflection → MemoryProposal → Learning Gate → Executive → memory commit
```

The `EPHEMERAL_SANDBOX` fast path only applies after actual reachable-effect containment proof; mutating shared-world effects never use that bypass.

## 6. Cross-layer canonical vocabulary and legal types

The foundational distinctions are: `Claim`, `InformationNeed`, `Hypothesis`, `Observation`, `EvidenceLink`, `ContradictionRecord`, `Decision`, `Goal`, `Slice`, `CapabilityResult`, `ActionProposal`, `ActionRecord`, `Trigger`, `Specialist`, `DependencyStamp`, `MemoryProposal`, `ContentEnvelope`, `LeadershipGrant`. Ownership of concrete schemas is delegated to layers L1–L6, except FCA-defined semantics that none may reinterpret.

**Schema collision GAIA-B01:** FCA §23 defines `CapabilityResult` as a semantic result with fields `patch_proposal?`, `proposed_claims[]`, `proposed_hypotheses[]`, `proposed_information_needs[]`, `evidence_refs[]`, `tool_requests[]`, `experiment_requests[]`, `confidence_assessment?`, `specialist_request?`, `needs[]`, `rationale_summary?`. RDMS-10's identically named transport form is **not canonical** and must be renamed (see L7).

## 7. Source-derived non-bypassable principles

- Provider substitution never changes identity, control authority, canonical workspace or action history.
- Global event-version change is not by itself proof that an individual specialist result is stale.
- Tool exit code, fluent prose and LLM confidence are not proof of external effect or engineering acceptance.
- Current epoch fences new legal authorizations from previous Executive epochs; it does not erase already-dispatched effects.
- Unknown non-idempotent external outcomes cannot be blindly retried.
- Temporal continuation comes from durable state, not conversation logs.
- Source content never self-assigns instruction authority.

## 8. Constitutional non-goals

The foundation is not a token generator, inference framework, prompt library or implementation package specification; it defines the irreducible authority/evidence boundaries that implementation choices must conserve.

## 9. Review and change control

Changing authority, legal write paths, epistemic meanings, action semantics, memory promotion, specialist authority, recovery, or trigger durability reopens FCA through explicit governance; editing one layer's Markdown is never sufficient authorization.


## 10. Dependency and interface register

- Downstream: L1 control, L2 cognition, L3 actions, L4 temporal/specialists, L5 memory, L6 recovery, L7 integration.
- Upstream: immutable frozen FCA source archive.
- Any type name defined here is a pointer to its original owner rather than a second schema implementation.

## 11. Pending effective-contract verification

- **PENDING EFFECTIVE CONTRACT AUDIT:** verify the complete frozen RDMS-01…09 corpus against this foundation.
- **GAIA-B01:** replace the colliding RDMS-10 transport `CapabilityResult` type; retain FCA §23 semantics.

## 12. Layer conformance requirements

A layer cannot be marked `FROZEN_CONSOLIDATED` until: (a) the owning legal contracts are imported from their frozen source version without loss; (b) all cross-layer projections are typed and referenced; (c) invariants, authority, failure and recovery paths are covered by normative acceptance scenarios; (d) source hashes and changes are recorded in `ARCHITECTURE_MANIFEST.md`; (e) the layer's review explicitly approves the consolidated text.

---

# SOURCE-PRESERVED FCA v1.0.1 BASELINE ANNEX

**Source authority:** the immutable `Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md` file in `reviews/source_archive/`. These copied sections are exact FCA source excerpts, not newly approved RDMS definitions. Layer prose above remains a consolidation draft pending full RDMS source validation.
**Source SHA-256:** `74d0923cbd343b71740da0fc2368a84aad2ea97f8e4e15f156122f48ebe53539`

**Ownership note:** This document embeds its assigned FCA source sections once. Do not redefine these names in a second layer; refer to the original owner or validated public projection.

<!-- GAIA-SOURCE FCA-SECTION 00 SHA256=3fabf86f22106407652c23d8ae5a1187c9693253d32a71fdb60ffb5ad3ab7eda -->
## 0. Purpose, provenance, and freeze boundary

This specification consolidates the complete design path that preceded implementation:

1. the original cognitive-engineer model;
2. Studies 01–10 of expert human software-engineering cognition;
3. the conceptual **Human Expert Programmer Cognitive Model v1.0**;
4. **Formal Cognitive Architecture v1.0**;
5. **C01 — Epistemic, Executive & State Corrections**;
6. **C02 — Runtime & Authority Corrections**;
7. **C03 — Durability & Trust Closure**;
8. **C04 — Operational Efficiency & Epistemic Closure**;
9. adversarial Freeze Reviews 01–05;
10. targeted operational review with **Freeze Review 05: PASS**.

The purpose of this document is not to describe a particular codebase, programming language, database, LLM provider, process topology, or UI. It freezes the **semantics, authorities, persistent state, legal write paths, cognitive capabilities, runtime safety contracts, and multi-agent rules** that any conforming implementation must preserve.

### 0.1 Normative language

- **MUST / MUST NOT**: frozen architectural requirement.
- **SHOULD / SHOULD NOT**: strong default; deviations require explicit rationale.
- **MAY**: implementation choice that does not change frozen semantics.

### 0.1.1 Version relationship

FCA v1.0.1 is a narrow operational amendment to the frozen FCA v1.0 baseline. It preserves the architecture identity, authority model, recovery model, and multi-agent model. The only normative changes are the C04 efficiency/causal-closure refinements documented in Appendix E.

### 0.2 What is frozen

FCA v1.0 freezes:

- one canonical cognitive authority;
- Executive-control semantics;
- Canonical Cognitive Workspace semantics;
- epistemic-state separation;
- capability contracts and execution-atom model;
- observation/evidence semantics;
- world-action authority and recovery semantics;
- CommitGate / ActionGate boundaries;
- Action Journal and write-ahead dispatch semantics;
- typed invariants;
- experiment lifecycle;
- memory governance and transfer rules;
- temporal cognition, suspension/resumption, and durable triggers;
- specialist creation, isolation, integration, and authority limits;
- Executive epochs and fencing;
- dependency-freshness semantics;
- trust/instruction boundaries;
- safe-cancellation and `IN_DOUBT` semantics;
- gravity-gated MMRT activation semantics when MMRT is enabled;
- fine-grained negative-knowledge invalidation semantics;
- action-class separation between disposable sandbox effects and shared-world mutation;
- Operationally Verified Causal Claim semantics and causal-closure governance.

### 0.3 What is not frozen

The following are implementation/evaluation choices unless they force a change to frozen semantics:

- Python vs Rust vs another language;
- SQLite vs PostgreSQL vs another storage engine;
- exact class names;
- exact process/service boundaries;
- ORM choice;
- exact numeric detector thresholds;
- reasoning-provider selection;
- benchmark suite;
- UI / CLI design;
- whether optional capabilities such as MMRT ship in implementation V1 or V2; when MMRT is present, its gravity/change-surface activation policy in §36 is normative;
- exact sandbox technology.

A future implementation decision that requires changing a frozen authority, state meaning, legal write path, invariant, or recovery guarantee **reopens FCA** and requires an explicit architecture correction/revision.

---

# Part I — Architectural identity

<!-- GAIA-SOURCE FCA-SECTION 01 SHA256=a4e7558382f382499ebae0ef3a3c5d9f582abf77ab2ed8ddf1afd6320f173620 -->
## 1. The system we are building

FCA v1.0.1 defines a persistent software-engineering cognitive system that behaves more like an expert engineer than a prompt-driven coding loop.

It is intended to:

- understand the real goal before modifying code;
- build and continuously revise a mental model of the system;
- direct attention toward the highest-value missing information;
- distinguish facts, beliefs, assumptions, unknowns, hypotheses, and observations;
- reason causally instead of patching symptoms;
- design discriminating experiments;
- compare engineering alternatives and their future consequences;
- plan work as safe transitions between valid system states;
- generate code under explicit semantic and architectural constraints;
- verify behavior, structure, invariants, and semantic intent;
- monitor the quality of its own reasoning;
- learn conservatively from experience;
- preserve cognitive continuity across interruptions, crashes, days, and long projects;
- recruit isolated temporary specialists only when independence, parallelism, specialization, context isolation, or hypothesis diversity has real value.

The system is best summarized as:

> **An artificial software engineer — one persistent mind that can temporarily become a team.**

---

<!-- GAIA-SOURCE FCA-SECTION 02 SHA256=183691329c465ec5351ac79a6e1cb39c79e4396342c39eaa3f69113995d5e39b -->
## 2. Agent ≠ LLM

The reasoning model is a replaceable provider, not the identity of the agent.

```text
Agent
=
Persistent Cognitive State
+
Executive Control
+
Cognitive Capabilities
+
Memory
+
Control / Action / Observation Runtime
+
Tools / Reality
+
Reasoning Providers
+
Temporary Specialists
```

A conforming system MAY use GPT, Claude, Gemini, local models, DGCA LITE, or future models. Replacing the reasoning provider MUST NOT erase project identity, canonical state, memory, authority, action history, or recovery state.

### 2.1 Core rule

> **The LLM proposes. Deterministic systems validate what can be validated. Reality supplies observations. The Executive provides semantic authorization. Hard law remains non-bypassable.**

### 2.2 Reasoning providers have no direct mutation authority

A reasoning provider MUST NOT directly possess:

- unrestricted filesystem mutation;
- shell authority;
- production credentials;
- database mutation authority;
- deployment authority;
- direct Canonical Workspace write access;
- memory-promotion authority.

Any requested effect becomes a typed proposal that enters the appropriate legal path.

---

# Part II — The four runtime planes

<!-- GAIA-SOURCE FCA-SECTION 03 SHA256=9152a998b18ebe255cd960a0ca8e76924d9dbf572c72487b9231e9f422020635 -->
## 3. High-level runtime

FCA separates cognition from control, action, and observation.

```text
┌─────────────────────────────────────────────┐
│              COGNITIVE PLANE                │
│                                             │
│ Cognitive Executive                         │
│ Canonical Cognitive Workspace               │
│ Capability Runtime                          │
│ Memory System                               │
│ Reasoning Gateway                           │
└───────────────────┬─────────────────────────┘
                    │ semantic authorization
                    ▼
┌─────────────────────────────────────────────┐
│               CONTROL PLANE                 │
│                                             │
│ Control Ledger                              │
│ CommitGate                                  │
│ ActionGate                                  │
│ Trigger lifecycle                           │
│ Specialist lifecycle                        │
│ Executive epoch / fencing                   │
└───────────────────┬─────────────────────────┘
                    │ durable intent
                    ▼
┌─────────────────────────────────────────────┐
│                ACTION PLANE                 │
│                                             │
│ Action Journal                              │
│ Reality Executor                            │
│ Isolated Specialist Workspaces              │
└───────────────────┬─────────────────────────┘
                    │ changes / probes reality
                    ▼
                 REAL WORLD
                    │
                    ▼
┌─────────────────────────────────────────────┐
│             OBSERVATION PLANE               │
│                                             │
│ Observation Ingress                         │
│ Provenance / integrity                      │
│ Contradiction detection                     │
└───────────────────┬─────────────────────────┘
                    │ observations
                    ▼
              COGNITIVE PLANE
```

These planes are not separate minds. There is one canonical cognitive identity. The other planes protect it from unsafe authority, ambiguous world effects, and observational contamination.

---

<!-- GAIA-SOURCE FCA-SECTION 04 SHA256=55ed20e1bb3533ac200e139d9b068ec71b61f5d04db4db25e2d4ae0485e6b8fe -->
## 4. Authority model

FCA recognizes distinct authorities:

### 4.1 Semantic authority

The current **Cognitive Executive epoch** is the sole authority that may semantically authorize mutation of canonical cognitive state.

### 4.2 Structural/legal authority

`CommitGate` and `ActionGate` enforce non-bypassable rules. The Executive cannot make an illegal operation legal.

### 4.3 World authority

Reality determines what actually happened. Intention, generated code, or an LLM statement cannot substitute for observation.

### 4.4 Learning authority

Experience may be captured automatically as history, but semantic promotion into reusable learned knowledge is governed by the Learning Gate and Executive authorization.

### 4.5 Human authority is domain-specific

A human source is not universally authoritative. Authority depends on the claim domain.

Examples:

```text
"Refunds use the original exchange rate."
→ authoritative requirement if stated by the requirement owner.

"I think PostgreSQL is causing the bug."
→ technical advice / hypothesis, not a fact.
```

Authority comes from trusted control metadata, not from wording inside content.

---

# Part III — Canonical cognition

<!-- GAIA-SOURCE FCA-SECTION 19 SHA256=f3ec13fd846dae3b3045ad230c49d0aa10c00d42374988a4f02f5da4741903a9 -->
## 19. Invariant

```text
Invariant {
    id
    statement
    scope

    kind:
        state
        architectural
        behavioral
        business
        security
        semantic

    severity:
        hard
        critical
        advisory

    enforcement:
        commit_gate
        pre_action_gate
        post_action_verify
        runtime_monitor
        semantic_review

    predicate?
    verification_spec?

    source_authority

    version

    status:
        active
        superseded
        retired
}
```

Every invariant MUST declare who or what enforces it.

Examples:

```text
State.version increases monotonically
→ state / hard / commit_gate

Domain must not import Infrastructure
→ architectural / hard / pre/post verification

Payment captured at most once
→ business / critical / behavioral verification

Code should preserve conceptual clarity
→ semantic / advisory / semantic review
```

A hard invariant cannot be silently weakened by the operation it constrains.

Changing a hard invariant requires an explicit `InvariantChangeProposal`, proper authority, a Decision, and a new invariant version.

---

<!-- GAIA-SOURCE FCA-SECTION 20 SHA256=7c575f0d124801852dd325143ed841ded74502d2f161c78a9dd60233e24ae19c -->
## 20. Contracts

Contracts define stable expectations across boundaries. They may describe:

- data shape;
- behavior;
- ownership;
- state transitions;
- error semantics;
- compatibility;
- external expectations.

Workers and specialists MUST NOT silently rewrite shared contracts to make their local task easier.

---

<!-- GAIA-SOURCE FCA-SECTION 21 SHA256=aa00af7b3690bec95e0efee8533cceadad24d9c1765c5978f2504a94d2f555c9 -->
## 21. Canonical vocabulary

The project SHOULD maintain a canonical lexicon of important concepts and terms.

Naming consistency is not cosmetic; it supports shared mental-model reconstruction across time, humans, and specialists.

---

# Part VII — Capabilities

<!-- GAIA-SOURCE FCA-SECTION 41 SHA256=c094687b52cd30548b46014b794d3bf556bd122e79f09840168aa4d09e894625 -->
## 41. Cognitive mutation vs world mutation

FCA distinguishes:

```text
CognitivePatch
→ changes canonical cognition

ActionProposal
→ requests a change to external reality

Observation
→ reports what reality did
```

No reasoning component may mutate shared external reality except through an authorized ActionProposal.

---

<!-- GAIA-SOURCE FCA-SECTION 72 SHA256=e98974896112dac605c7596a594ac8628f354d23eb3fa38d206f119893dc02e1 -->
## 72. Content envelope

All content entering reasoning carries explicit provenance and instruction authority.

```text
ContentEnvelope {
    source

    content_role:
        instruction
        requirement
        code
        documentation
        observation
        tool_output
        memory
        specialist_output
        external_content

    instruction_authority:
        SYSTEM
        PROJECT
        USER_TASK
        NONE

    provenance
    integrity
}
```

Authority comes from the trusted envelope/control channel, not from text inside the content.

> **Content cannot self-assign authority.**

Repository text, code comments, logs, web pages, tool outputs, memories, and specialist outputs default to `instruction_authority = NONE` unless a trusted control path explicitly says otherwise.

---

<!-- GAIA-SOURCE FCA-SECTION 73 SHA256=88538b3fc3717bc85284635dae144d0cd29746786d3d5fea465959b269bfae2f -->
## 73. Untrusted execution

Project scripts, generated code, build systems, and tests are treated as potentially untrusted execution.

A conforming implementation SHOULD use isolation that constrains:

- credentials;
- filesystem scope;
- network access;
- host effects;
- external mutation.

Unexpected effects are observations, not automatically intended effects.

---

# Part XX — Legal write paths

<!-- GAIA-SOURCE FCA-SECTION 84 SHA256=d32b3e13c46088f72b0ad7852bb93fae0e018a1588ff27c2514d287afc4404af -->
## 84. Frozen principles

1. **Agent is not the LLM.**
2. **One mind, many temporary specialists.**
3. **Cognitive state, not conversation, is the unit of continuity.**
4. **Capabilities are not automatically modules, agents, or LLM calls.**
5. **Reality outranks model output.**
6. **Observation and interpretation are distinct.**
7. **Facts, beliefs, assumptions, unknowns, and hypotheses remain distinct.**
8. **Suspicion is not permission to modify.**
9. **Confidence follows evidence.**
10. **Unexpected difficulty is information.**
11. **Activity is not progress.**
12. **Passing tests is not sufficient proof of architectural correctness.**
13. **Future-aware does not mean future-obsessed.**
14. **Do not implement speculative futures; preserve valuable options.**
15. **Every abstraction, layer, and indirection must buy something.**
16. **Important concepts, ownership, and invariants should be visible in architecture/code.**
17. **Plan through safe state transitions, not merely task lists.**
18. **Implementation and verification should stay close.**
19. **A retrieved experience is precedent, not authority.**
20. **Generalization is slower and more conservative than episode capture.**
21. **No significant implementation drift without model, plan, or decision reconciliation.**
22. **Independent specialists exist only when independence/separation itself has value.**
23. **Global coherence remains under one canonical cognitive authority.**
24. **Executive semantic authority does not override hard law.**
25. **Reasoning providers never own direct world-mutation authority.**
26. **World effects are inferred from observed effects, not from intent.**
27. **Unknown external outcomes remain explicitly `IN_DOUBT`.**
28. **Future commitments require durable reactivation.**
29. **Content cannot self-assign authority.**
30. **Recovery state is part of the architecture, not an afterthought.**

---

# Part XXIV — Formal invariants FCA-I01…FCA-I50

The following invariants are normative. Wording below reflects the final post-C01/C02/C03 semantics.

## Authority & epistemic invariants

**FCA-I01** — Only the current Executive may semantically authorize canonical cognitive-state mutation.

**FCA-I02** — Reality observations may enter canonical history only through Observation Ingress.

**FCA-I03** — Reasoning/LLM output may not manufacture canonical Observations.

**FCA-I04** — Specialists never commit directly to the Canonical Workspace.

**FCA-I05** — Fact, Belief, Assumption, InformationNeed, and Hypothesis remain semantically distinct.

**FCA-I06** — Every Fact requires an observed, deterministic, or domain-authoritative grounding path.

**FCA-I07** — Confidence must identify its evidence basis and scope.

**FCA-I08** — Retrieved memory is never automatically promoted to current Fact.

## Execution & temporal invariants

**FCA-I09** — Every executable Slice traces to a Goal.

**FCA-I10** — Every Slice executes against explicit state/repository references sufficient for reconciliation.

**FCA-I11** — Significant implementation deviation requires model, plan, or decision reconciliation.

**FCA-I12** — Verification distinguishes deterministic structure, behavioral observations, and semantic judgment.

**FCA-I13** — Suspended work has a Resumption Capsule.

**FCA-I14** — Resume reconciles stored cognition with relevant world/repository changes before execution continues.

**FCA-I15** — Temporary commitments require an explicit removal/revisit trigger.

## Multi-agent invariants

**FCA-I16** — There is exactly one canonical cognitive authority per project state.

**FCA-I17** — Specialist creation requires explicit value from parallelism, independence, specialization, context isolation, or hypothesis diversity.

**FCA-I18** — Specialist consensus never overrides stronger evidence.

## World-action & interpretation invariants

**FCA-I19** — Shared-world mutation requires an authorized ActionProposal.

**FCA-I20** — Intent, execution attempt, reported result, and verified world effect are distinct.

**FCA-I21** — An unreconciled mutation may not be blindly retried.

**FCA-I22** — Observation and interpretation are distinct entities.

**FCA-I23** — Semantic reasoning alone cannot create a Fact.

**FCA-I24** — Executive authorization cannot override currently valid hard architectural law.

**FCA-I25** — A hard invariant cannot be silently weakened by the operation it constrains.

**FCA-I26** — Global state version does not by itself define semantic staleness.

## Memory, triggers, and experiments

**FCA-I27** — Retrieved memory is precedent, not current truth.

**FCA-I28** — Semantic memory promotion requires governance.

**FCA-I29** — Future commitments require an operational reactivation mechanism.

**FCA-I30** — Every invariant declares an enforcement mechanism.

**FCA-I31** — Experiment predictions become immutable for that experiment before execution begins.

## Durability & trust invariants

**FCA-I32** — Only the current Executive epoch may authorize new canonical effects.

**FCA-I33** — Leadership loss fences future authority but does not erase already-dispatched world effects.

**FCA-I34** — Unknown world-action outcomes remain explicitly `IN_DOUBT`.

**FCA-I35** — `IN_DOUBT` actions cannot be blindly retried.

**FCA-I36** — External mutations require durable dispatch intent before execution.

**FCA-I37** — Recoverability-critical control metadata commits atomically.

**FCA-I38** — Trigger detection may repeat; canonical trigger reactions must deduplicate.

**FCA-I39** — Edge-triggered commitments require a replayable source capable of proving the edge.

**FCA-I40** — Content cannot self-assign instruction authority.

**FCA-I41** — Reasoning providers possess no direct shared-world mutation authority.

**FCA-I42** — Dependency freshness follows actual dependencies, including negative-query dependencies.

**FCA-I43** — Conflicting observations are preserved, scoped, and investigated rather than overwritten.

**FCA-I44** — Safety reconciliation outranks ordinary budget exhaustion.

## Operational-efficiency & causal-closure invariants

**FCA-I45** — When MMRT is available, its invocation is governed by Decision Gravity and semantic change surface; routine low-gravity edits are not required to undergo MMRT.

**FCA-I46** — MMRT disagreement alone is not a hard rejection condition; blocking requires a hard violation, contradictory evidence, or an Executive-reviewed material semantic mismatch.

**FCA-I47** — Negative knowledge freshness follows its typed dependency frontier; unrelated repository changes do not by themselves invalidate a still-valid scoped negative conclusion.

**FCA-I48** — The ephemeral sandbox fast path is legal only when the execution boundary proves that all reachable effects are disposable and isolated from canonical/shared world state; uncertainty defaults to `SHARED_WORLD`.

**FCA-I49** — Semantic causal interpretation may be closed into an `OperationalCausalClaim` only through the Causal Closure Gate; it is never promoted directly to a generic Fact.

**FCA-I50** — An `OperationalCausalClaim` is scope- and dependency-bound and MUST become stale, contradicted, or reopened when its validity conditions fail or unresolved contradictory observations arise.

---

# Part XXV — Study-to-architecture traceability

The architecture was derived from ten human-cognition studies.

## Study 01 — Mental Model

Architectural consequences:

- System Mental Model;
- hierarchical/compressed representation;
- dynamic belief revision;
- runtime evidence as model correction;
- top-down/bottom-up navigation.

## Study 02 — Attention & Information Foraging

Architectural consequences:

- FocusState;
- InformationNeed;
- bounded CognitiveView;
- deliberate search/information patches;
- smallest-correct-context principle.

## Study 03 — Hypothesis, Causality & Experimentation

Architectural consequences:

- Hypothesis entity;
- Observation/Evidence separation;
- first-class Experiment;
- competing hypotheses;
- falsifiable predictions;
- causal closure;
- suspicion-not-action rule.

## Study 04 — Design Deliberation & Engineering Judgment

Architectural consequences:

- Decision schema;
- Decision Gravity;
- alternative generation;
- future/evolution simulation;
- quality drivers;
- reversibility;
- complexity/indirection discipline;
- revisit triggers.

## Study 05 — Hierarchical Planning & Incremental Execution

Architectural consequences:

- Goal hierarchy;
- Execution Graph;
- rich Slice;
- proof obligations;
- safe state transitions;
- expected change surface;
- architecture conformance;
- replanning.

## Study 06 — Code Construction as Cognitive Translation

Architectural consequences:

- constrained synthesis;
- Concept-to-Code Mapping;
- canonical vocabulary;
- semantic cohesion;
- state-space discipline;
- reader simulation / MMRT;
- code as externalized cognition.

## Study 07 — Self-Review & Metacognition

Architectural consequences:

- Fact/Belief/Assumption separation;
- ConfidenceProfile;
- contradiction and prediction-error state;
- stagnation/drift detectors;
- independent review;
- evidence-over-voting;
- bounded stopping/escalation logic.

## Study 08 — Learning, Experience & Transfer

Architectural consequences:

- Memory maturity;
- Learning Gate;
- MemoryProposal;
- provenance/scope/applicability;
- procedural memory;
- retrieved experience as precedent, not fact;
- conservative generalization.

## Study 09 — Team Cognition

Architectural consequences:

- one canonical mind;
- temporary specialists;
- shared canonical state + private local cognition;
- specialist authority contracts;
- dynamic team formation;
- integration and dependency freshness;
- independent reviewer.

## Study 10 — Temporal Cognition & Long-Horizon Engineering

Architectural consequences:

- Goal Stack;
- Resumption Capsule;
- BLOCKED/WAIT/SUSPEND/RESUME;
- temporal validity;
- durable commitments/triggers;
- recovery protocol;
- cognitive continuity independent of chat history.

---

# Part XXVI — Final runtime flow

<!-- GAIA-SOURCE FCA-SECTION 86 SHA256=168ddf6cb73c925906ef7db4848bb7d5e88f69ca32c406bf3cfccf590a7e573e -->
## 86. Final freeze verdict

Adversarial reviews progressed as follows:

```text
Freeze Review 01
→ architecture not frozen
→ C01

Freeze Review 02
→ runtime/action authority blockers
→ C02

Freeze Review 03
→ durability/trust blockers
→ C03

Freeze Review 04
→ failure-injection authority/recovery review
→ PASS
```

Final verdict:

# **Formal Cognitive Architecture v1.0 — FROZEN**

No remaining learned-state, authority, concurrency, durability, trust, or recovery ambiguity was identified that required altering the formal architecture.

---

<!-- GAIA-SOURCE FCA-SECTION 87 SHA256=1d317d316ab92c2fff1ca61222e7d9c5bccfa7bfeeffbaa086826fcc45cbaf18 -->
## 87. Change-control rule

A future change requires reopening FCA if it alters any of:

```text
canonical authority
legal write paths
epistemic meanings
world-action semantics
observation semantics
persistent-state ownership
hard-invariant enforcement
memory-promotion authority
specialist authority
recovery semantics
trust boundary
trigger durability
```

Implementation choices that preserve all frozen semantics do not reopen FCA.

---

# Part XXVIII — Next phase

The architecture is frozen. The next phase is not another cognition study.

The implementation program should proceed from this spec into:

1. **Runtime/Data Model Specification**
   - exact persisted schemas;
   - event types;
   - entity IDs/versions;
   - transaction boundaries;
   - dependency-stamp representation;
   - recovery records.

2. **Implementation Boundary Design**
   - packages/modules;
   - interfaces;
   - process boundaries;
   - sandbox boundary;
   - provider adapters.

3. **Implementation Plan**
   - dependency-ordered milestones;
   - proof obligations;
   - verification gates;
   - minimal walking skeleton;
   - progressive activation of cognitive capabilities.

4. **Conformance Test Suite**
   - FCA-I01…I50;
   - crash/retry scenarios;
   - split-brain/fencing;
   - stale specialist integration;
   - prompt-injection/trust-boundary tests;
   - trigger replay/deduplication;
   - memory-promotion tests;
   - `IN_DOUBT` action tests.

No implementation is compliant with FCA v1.0.1 merely because it “works.” It is compliant only if it preserves the authority, state, evidence, durability, trust, and recovery semantics frozen here.

---

# Closing definition

> **FCA v1.0 defines a persistent, evidence-grounded software-engineering cognitive system with one canonical executive authority, dynamically recruited isolated specialists, explicit separation between cognition, control, action, and observation, durable recoverable control state, conservative experience learning, and replaceable reasoning providers.**

And the architectural identity remains:

# **One mind, many temporary specialists.**

---

<!-- GAIA-SOURCE FCA-APPENDIX A SHA256=39dd78570d0f82a96f70bfb6238c03980aa182a651fd590c8b73b08dd192dbe5 -->
# Appendix A — Mapping from the original cognitive-engineer document

The original design contained eight named units. None of them was discarded; each matured into a broader capability or control responsibility.

| Original concept | FCA v1.0 final form | Main change |
|---|---|---|
| `IntentAnalyzer` | Intent & Goal Modeling | From one-shot parsing to persistent goal hierarchy, acceptance, ambiguity, non-goals, and stakeholder authority. |
| `WorldModel` | System Mental Model | Expanded into Domain, Structural, Runtime, Causal, and Risk models; explicitly revisable by evidence. |
| `Planner` | Adaptive Execution Planning | Replaced linear task lists with dependency graphs, proof obligations, coherent Slices, and safe state transitions. |
| `Deliberator` | Engineering Judgment | Expanded to alternatives, quality attributes, future/evolution simulation, reversibility, complexity, risk, and Decision Gravity. |
| `Simulator` | Runtime/Causal/Future Simulation | Split semantically across causal reasoning, experiment design, behavioral prediction, and evolution simulation. |
| `CausalReasoner` | Hypothesis + Causal Reasoning + Experiment Design | Added competing hypotheses, predictions, falsification, EvidenceLinks, causal closure, and first-class Experiments. |
| `Critic` | Review + Metacognition + Executive Control | Separated artifact criticism from monitoring the quality of reasoning, confidence, stagnation, drift, and strategy. |
| `Reflector` | Experience Consolidation + Learning Gate | Replaced direct “lesson storage” with episode capture, scoped lessons, provenance, applicability, counterexamples, and conservative promotion. |

The original fixed loop:

```text
understand → imagine → plan → compare → simulate → execute → critique → learn
```

was superseded by an adaptive recurrent loop. FCA does not force every capability on every task. Cognitive depth is selected according to uncertainty, risk, gravity, and evidence.

---

<!-- GAIA-SOURCE FCA-APPENDIX B SHA256=213d559986c10db501bef7b302486ab28d9401b13cf146833c0a0029577c6aea -->
# Appendix B — Non-normative engineering heuristics preserved from Studies 01–10

These heuristics influenced FCA but are not all Hard Invariants. Implementations SHOULD preserve their intent unless evidence shows a better policy.

## B.1 Mental-model heuristics

- Reduce the problem space before reading the codebase broadly.
- Prefer concept nodes, landmarks, relationships, ownership, and invariants over memorizing files/lines.
- Maintain both a **program/structural model** and a **domain/situation model**.
- Treat pattern recognition as prior generation, not proof.
- Use forward reasoning (“if I change X, what happens?”) and backward reasoning (“what could produce Y?”).
- Execution is epistemic: model → prediction → action/experiment → observation → model correction.
- The repository remains external high-fidelity memory; cognition stores compressed meaning.

## B.2 Attention and information-foraging heuristics

- Working memory is a bounded set of goal, subgoal, active entities, active hypothesis, unknowns, and next information need.
- Search should be driven by **information need**, not by broad context acquisition.
- Prefer cheap evidence that discriminates hypotheses or reduces risk.
- A useful transition can often be represented as:

```text
ACTION
REASON
EXPECTED INFORMATION
WHAT WOULD CHANGE THE MODEL
```

- Re-retrieve details when needed rather than keeping large context active.
- Use cognitive landmarks.
- Zoom out when navigation becomes repetitive or evidence gain stagnates.
- Stop gathering when enough evidence exists to act safely; risk changes the stopping threshold.

## B.3 Causal-debugging heuristics

- Separate symptom, fault, trigger, enabling condition, and causal chain.
- Generate multiple plausible, distinct, testable hypotheses for ambiguous failures.
- Turn hypotheses into predictions before running experiments.
- Prefer discriminating experiments over random data collection.
- Negative evidence is valuable.
- Correlation is not causation; interventions and counterfactual reasoning strengthen causal claims.
- Repair success is not equivalent to diagnostic success.
- Diagnostic interventions and production fixes may be different.
- Reproduction/minimal reproduction is a causal laboratory.
- Nondeterministic bugs require repeated/sampled evidence and temporal ordering models.
- Close important bugs only when mechanism, intervention point, regression capture, and relevant alternative paths are understood.

## B.4 Engineering-judgment heuristics

- Requirement → design space, not immediate implementation.
- There is no universal best architecture; fit depends on context, constraints, quality attributes, and expected future.
- Generate alternatives before commitment when Decision Gravity justifies it.
- Simulate futures selectively: change, scale, team, failure, debug, test, data, deploy, security, reversal.
- Preserve cheap seams/options instead of implementing speculative futures.
- Track change surface and blast radius.
- Coupling is also cognitive cost: it increases how much of the system must be loaded to reason locally.
- Keep important invariants close to the state and authority that own them when possible.
- Preserve local correctness and global coherence together.
- Record rejected alternatives and the conditions that would reopen the decision.
- Reversibility reduces decision risk.
- Technical debt may be intentional only when benefit, cost, owner, and revisit/removal trigger are explicit.
- Maintain a complexity budget: abstractions, layers, services, queues, and stores must buy something real.
- Do not apply “clean code” rules mechanically.

## B.5 Planning/execution heuristics

- Preserve architecture during implementation; avoid patch → workaround → special case cascades.
- Plan hierarchically but allow evidence-driven opportunistic discovery.
- Define important invariants/contracts before decomposing risky work.
- Resolve the **cognitive critical path**: unknowns capable of invalidating much downstream work.
- Use exploration/spikes to retire risk, but separate exploratory artifacts from production state.
- Prefer coherent slices over arbitrary small commits.
- Every important task should carry a proof obligation.
- Verification should cover behavior, regression, contract, invariant, architecture, operational, and security dimensions as appropriate.
- Passing tests does not prove architecture conformance.
- Checkpoints synchronize model and reality.
- Replanning is not failure; silent drift is failure.
- Far-future planning may remain coarse; near-term work becomes detailed (rolling-wave planning).
- Reversibility affects sequencing; migrations may use expand/contract patterns.
- Multi-agent parallelism begins only after shared boundaries/contracts are sufficiently stable.

## B.6 Code-construction heuristics

- Translate requirement → conceptual intention → responsibilities → state/invariants → operations → control/data flow → language constructs.
- Code should preserve the shape of important ideas when practical.
- Every construct should have a cognitive role.
- Abstraction is good when it compresses a stable concept; abstraction is harmful when it conceals or speculates.
- Small duplication can be cheaper than a wrong abstraction.
- Naming difficulty can reveal unclear conceptual boundaries.
- Prefer canonical project vocabulary over isolated naming cleverness.
- Function boundaries should follow conceptual responsibility and semantic cohesion, not line-count dogma.
- Make state ownership and transition authority visible.
- Treat APIs as cognitive surfaces; unnecessary public surface increases long-term cost.
- Types/representations can suppress illegal states.
- Comments should preserve WHY, constraints, and rationale rather than restating syntax.
- Error handling is domain semantics; retries have causal consequences.
- Every layer must pay rent.
- Complexity is mental simulation cost, not merely LOC or a metric score.
- Unexpected coding friction may be a prediction error indicating a wrong model or abstraction.
- Separate author mode from structural/reviewer mode.
- Run semantic diff: compare intended conceptual change with actual conceptual change.
- Optimize conceptual locality, not tiny files.
- Prefer the principle of least cognitive surprise.

## B.7 Metacognitive heuristics

- Continuously ask what is being proved, which assumptions remain, what evidence changed, and whether uncertainty is shrinking.
- Search for disconfirming evidence.
- Use independent review when cognitive independence has value.
- Use pre-mortem reasoning for high-gravity decisions.
- Productive skepticism should be proportional to risk; permanent red-team mode causes paralysis.
- Confidence must be scoped by dimension.
- Track assumption dependencies so downstream decisions can be reconsidered when an assumption fails.
- Treat prediction error as a cross-cutting metacognitive signal.
- Detect local maxima: “tests pass” plus growing special cases may indicate a worse representation.
- Search for counterexamples, especially empty/extreme/concurrent/reordered/partial-failure/repeated/malicious cases.
- Distinguish technical uncertainty that can be investigated from business/policy uncertainty requiring stakeholder authority.
- Reasoning has marginal value; stop thinking when evidence is sufficient for the gravity of the decision.
- Record structured metacognitive events, not raw private chain-of-thought.
- Know tool coverage and capability limits; absence of evidence is not evidence of absence.
- False completion: “tests passed” is not equivalent to “task complete.”
- False progress: activity is not progress.

## B.8 Learning/transfer heuristics

- Remember reasons and applicability conditions, not merely solutions.
- A retrieved experience is a hypothesis about relevance, not an instruction.
- Generalization should be slower than episodic memorization.
- Failed/rejected designs are first-class experience when the causal reason for failure is retained.
- Consolidate repeated structurally similar experiences into schemas; keep episode provenance.
- Counterexamples refine applicability boundaries instead of necessarily deleting a schema.
- Preserve “what was believed then” to resist hindsight bias.
- Distinguish decision quality from lucky/unlucky outcome quality.
- Project-specific knowledge must not silently become cross-project general knowledge.
- Structural/causal similarity matters more than surface similarity for transfer.
- Procedural learning (“how to diagnose/plan/review”) may be more valuable than accumulating facts.
- Memory should support forgetting/archival of low-value noise.
- Model-specific operating lessons must be scoped to the reasoning provider when appropriate.

## B.9 Team-cognition heuristics

- Multi-agent does not mean multiple independent canonical minds.
- Shared mental model + distributed expertise is the target.
- Team intelligence is not the sum of individual model intelligence; coordination and integration quality matter.
- Cognitive role ≠ agent instance.
- Dynamic agent count should follow task topology.
- High coupling favors fewer workers; stable low-coupling boundaries favor parallelism.
- Communication should be event/need-driven rather than unrestricted agent chat.
- Duplication can be deliberate when independence/diversity is valuable.
- Consensus is not truth; weigh evidence.
- Decompose disagreement into differences in facts, assumptions, goals, predictions, trade-off weights, or risk tolerance.
- Integration includes semantic/architectural merge, not only textual merge.
- Specialists can preserve the central mind’s deep context by absorbing bounded side work.

## B.10 Temporal/long-horizon heuristics

- Resume task ≠ reopen file; resume = reconstruct/reconcile cognitive state.
- Externalize state before interruption.
- Keep a concrete next cognitive action in suspended work when possible.
- Self-interruption can be as damaging as external interruption; side discoveries should not hijack the active goal.
- Priority is multidimensional: urgency, impact, dependency, risk, information value, blocking power, reversibility, cost, and cognitive momentum.
- Global importance ≠ best next action.
- Waiting is a legitimate state when evidence/dependency is unavailable.
- Prefer safe suspension points.
- Switch cost grows with cognitive distance between tasks.
- Cluster related tasks when priorities allow.
- Temporary specialists can preserve context across unrelated concurrent goals.
- Compare present reality with milestone/architecture/mission periodically to detect silent drift.
- Progress is semantic: verified capability, risk retired, uncertainty reduced, dependencies unlocked.
- Unexpectedly long tasks are diagnostic signals.
- Limit WIP; stored tasks need not all be cognitively active.
- A “temporary” path needs expiry/removal/revisit semantics.
- The persistent system stores current accepted state plus provenance/history on demand, not months of raw conversational context.

---

<!-- GAIA-SOURCE FCA-APPENDIX C SHA256=1ff476779bede12807fb9f24e91585412cbea30fdf875ebcd0d7708052ef2aaf -->
# Appendix C — Final authority matrix

| Artifact / effect | Who may propose | Who semantically authorizes | Non-bypassable gate / owner | Direct LLM authority? |
|---|---|---|---|---|
| Claim / Mental Model update | Capability | Current Executive epoch | CommitGate | No |
| Goal / Plan / Decision | Capability | Current Executive epoch | CommitGate | No |
| Hard Invariant change | Engineering Judgment capability | Proper domain authority + Executive | CommitGate + explicit invariant-change path | No |
| World Action | Capability / Specialist | Current Executive epoch | ActionGate + Action Journal | No |
| Observation | Reality / authoritative human channel | No semantic approval for raw append | Observation Ingress | No |
| EvidenceLink | Capability | Current Executive epoch | CommitGate | May propose only |
| Experiment | Experiment Design capability | Executive; ActionGate for mutations | Experiment lifecycle + CommitGate/ActionGate | May design only |
| Memory lesson | Reflection / Learning capability | Executive under Learning Gate | Memory governance | May propose only |
| Episode archive | Runtime | Automatic allowed | Provenance/integrity rules | No |
| Specialist spawn | Capability / Executive policy | Current Executive epoch | Specialist Manager + epoch fencing | No |
| Specialist result integration | Specialist returns result | Current Executive epoch | Dependency freshness + verification + CommitGate | No |
| Trigger reaction | Trigger runtime | Policy/Executive according to reaction type | Control Ledger + idempotency key | No |

---

<!-- GAIA-SOURCE FCA-APPENDIX E SHA256=acde382026caa30ebcad924d9d0969819cb3a8f88aa36f79540b1292f0a06e53 -->
# Appendix E — Correction and freeze history

## E.1 Freeze Review 01 → C01

Resolved:

- capability classification was too exclusive;
- Reality Evidence writes conflicted with Patch-only writes;
- Claim mixed fact/belief/assumption/unknown/hypothesis;
- uncalibrated scalar confidence;
- Executive machine too pipeline-like and transitions too semantically vague;
- hard-coded detector thresholds;
- Capability contract allowed manufactured Evidence;
- semantic diff/MMRT incorrectly treated as deterministic verification;
- Canonical State lacked Focus, Goal Stack, temporal state, memory applicability, and rich specialist/slice state.

C01 also hardened Decision schema and domain-specific human authority.

## E.2 Freeze Review 02 → C02

Resolved:

- no formal authority path for world mutation;
- crash/partial-action reconciliation;
- Observation vs Evidence interpretation;
- Fact-promotion law;
- Executive semantic authority vs non-bypassable law;
- global base version unsuitable for parallel specialists;
- memory-promotion poisoning risk;
- non-operational future triggers;
- untyped invariant enforcement;
- Experiment not first-class state.

## E.3 Freeze Review 03 → C03

Resolved:

- split-brain Executives;
- unknown external-action outcomes;
- missing write-ahead action ordering;
- durability boundary across control metadata;
- trigger delivery/deduplication during downtime/restarts;
- untrusted content/prompt injection crossing into authority;
- dependency freshness broader than entity read sets;
- contradictory-observation policy;
- safe cancellation when budgets expire during mutation.

## E.4 Freeze Review 04

Failure-injection scenarios tested included:

- dual Executives;
- failover before/after dispatch intent;
- process crash during external mutation;
- unknown non-idempotent action result;
- partial migration;
- atomic Decision + Trigger durability;
- trigger occurrence during downtime;
- trigger redelivery;
- edge trigger without history;
- repository prompt injection;
- malicious project scripts;
- stale/partially-stale specialists;
- stale negative search conclusions;
- contradictory runtime observations;
- cross-project memory retrieval;
- poisoned generalization;
- budget exhaustion during mutation;
- hard-invariant rejection;
- experiment prediction integrity;
- reasoning-provider replacement;
- complete process recovery;
- technical vs human-authority ambiguity.

**Freeze Review 04: PASS.**

## E.5 Runtime operational review → C04

C04 addressed four implementation-friction findings without changing the architecture identity:

- MMRT could become an unnecessary latency/token multiplier if applied to routine internal edits;
- negative knowledge could thrash if every repository change invalidated broad text-search conclusions;
- full write-ahead action journaling was unnecessarily heavy for provably disposable sandbox micro-actions;
- `causally_verified` Hypotheses had no closure form suitable for efficient long-lived causal DAGs.

C04 therefore added:

- gravity/change-surface-gated MMRT activation and non-veto semantics;
- typed, fine-grained negative-knowledge dependency frontiers;
- an `EPHEMERAL_SANDBOX` fast path separated from `SHARED_WORLD` mutation;
- `OperationalCausalClaim` plus the Causal Closure Gate.

## E.6 Freeze Review 05

Targeted tests covered:

- low-gravity edits avoiding MMRT;
- high-gravity semantic-boundary changes invoking MMRT when available;
- MMRT wording disagreements remaining advisory;
- negative static-call conclusions surviving unrelated documentation changes;
- relevant symbol/index changes invalidating negative knowledge;
- dynamic-dispatch cases remaining conservatively scoped;
- disposable sandbox activity using aggregated records without per-file write-ahead entries;
- sandbox attempts to access canonical mounts, shared credentials, network side effects, or durable services being rejected/upgraded;
- causal closure refusing simple “patch succeeded” promotion;
- causal closure accepting reproduced, predicted, intervention-supported, regression-captured mechanisms;
- OVC invalidation on scope/dependency change or contradictory observation;
- cross-project OVC retrieval remaining precedent rather than universal truth.

**Freeze Review 05: PASS.**

---

<!-- GAIA-SOURCE FCA-APPENDIX G SHA256=dcce55f61f5484bf667c802bb0dfd9c973a57ef39b849a8cb30437dcc09795f5 -->
# Appendix G — Frozen architecture in one page

```text
USER / ENVIRONMENT
        │
        ▼
┌────────────────────────────────────┐
│        COGNITIVE EXECUTIVE         │
│   one current fenced epoch         │
└───────────────┬────────────────────┘
                ↕
┌────────────────────────────────────┐
│  CANONICAL COGNITIVE WORKSPACE     │
│                                    │
│ Goals / Focus                      │
│ Mental Model                       │
│ Claims / Unknowns / Hypotheses     │
│ Operational Causal Claims           │
│ Observations / EvidenceLinks       │
│ Decisions / Invariants / Contracts │
│ Plan / Slices / Experiments        │
│ Temporal / Memory / Meta           │
└───────────────┬────────────────────┘
                │
     ┌──────────┼───────────┐
     ▼          ▼           ▼
 Capabilities  Memory   Temporary Specialists
     │                      │
     └──────────┬───────────┘
                ▼
        REASONING GATEWAY
      replaceable LLM/provider
                │
                ▼ proposals only
┌────────────────────────────────────┐
│           CONTROL PLANE            │
│ CommitGate / ActionGate            │
│ Control Ledger / Epoch / Triggers  │
└───────────────┬────────────────────┘
                ▼ durable intent
┌────────────────────────────────────┐
│            ACTION PLANE            │
│ Shared Action Journal / Executor   │
│ Ephemeral Sandbox Fast Path        │
│ Isolated workspaces                │
└───────────────┬────────────────────┘
                ▼
              REALITY
                │
                ▼
┌────────────────────────────────────┐
│         OBSERVATION PLANE          │
│ provenance / integrity / conflict  │
└───────────────┬────────────────────┘
                ▼
       CANONICAL COGNITION
```

**Identity:** One mind, many temporary specialists.  
**Continuity:** Persistent cognitive state, not conversation history.  
**Truth discipline:** Reality supplies observations; cognition interprets them.  
**Action discipline:** Intent is not effect; effects are verified and recoverable.  
**Learning discipline:** Experience is precedent; generalization is governed.  
**Team discipline:** Specialists explore; one canonical mind accepts.  
**Provider discipline:** The LLM is replaceable and never owns world authority.
