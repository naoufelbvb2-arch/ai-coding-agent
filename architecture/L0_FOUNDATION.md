# L0 FOUNDATION

**Document status: FOUNDATIONAL ARTICLES VERIFIED AGAINST FCA v1.0.1; NOT FROZEN.** Source baselines retain their recorded specification freeze; this consolidation has no new freeze authority. Production implementation is not authorized.

L0 owns architectural identity, constitutional authority, trust boundaries, normative language and change control. Layer-specific FCA contracts belong to their respective owner layers; L0's cross-cutting principles do not duplicate their record ownership.

Each source-backed article is current only within its stated scope. Imported contracts retain the named owner; storage, delivery and scheduling do not create additional authorization. Source text remains unchanged in the archive. Source spelling and optionality are preserved; unspecified serialization types are not invented.


## Imported and exported boundaries

| Contract / responsibility | Canonical owner | This layer's obligation |
|---|---|---|
| ControlCommit, Control Ledger, ProjectHead and epoch fencing | [L1](../architecture/L1_CONTROL.md) | Use the single control durability boundary; the foundation grants no direct provider writes. |
| Cognitive workspace, Claim/Goal/Decision/Commitment and Executive | [L2](../architecture/L2_COGNITION.md) | Preserve semantic authorization, typed epistemic states and hard-law constraints. |
| Observation/EvidenceLink, ActionGate and Action Journal | [L3](../architecture/L3_ACTIONS.md) | Preserve independent observation ingress, evidence grounding and world-action authority. |
| TriggerCondition, specialist contracts and dependency evaluation | [L4](../architecture/L4_TEMPORAL_SPECIALISTS.md) | Preserve one mind, scoped temporary specialists and one freshness authority. |
| MemoryProposal and MemoryRetrievalResult | [L5](../architecture/L5_MEMORY.md) | Preserve learning governance and retrieval-as-precedent semantics. |
| ResumptionCapsule and suspension/resumption/recovery admission | [L6](../architecture/L6_RECOVERY.md) | Require durable, integrity-checked recovery context and lawful resumption. |
| Provider envelopes, trusted integration and transport projections | [L7](../architecture/L7_RUNTIME_INTEGRATION.md) | Transport carries source-owned legal meaning and confers no new authorization. |


## Current foundational law

The following articles retain only the current frozen FCA v1.0.1 units allocated to L0. Their source-section wording is preserved; they are not historical RDMS drafts or unreviewed GAIA substitutions.


### L0-F00 — Purpose, provenance, and freeze boundary

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

#### 0.1 Normative language

- **MUST / MUST NOT**: frozen architectural requirement.
- **SHOULD / SHOULD NOT**: strong default; deviations require explicit rationale.
- **MAY**: implementation choice that does not change frozen semantics.

#### 0.1.1 Version relationship

FCA v1.0.1 is a narrow operational amendment to the frozen FCA v1.0 baseline. It preserves the architecture identity, authority model, recovery model, and multi-agent model. The only normative changes are the C04 efficiency/causal-closure refinements documented in Appendix E.

#### 0.2 What is frozen

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

#### 0.3 What is not frozen

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

Source: [FCA-0](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L11>); source-unit SHA-256 `23c9377c15494f9050135d6d582c4a46e67ba6366496163931997b210aa53ffe`.

### L0-F01 — The system we are building

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

Source: [FCA-1](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L87>); source-unit SHA-256 `a4e7558382f382499ebae0ef3a3c5d9f582abf77ab2ed8ddf1afd6320f173620`.

### L0-F02 — Agent ≠ LLM

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

#### 2.1 Core rule

> **The LLM proposes. Deterministic systems validate what can be validated. Reality supplies observations. The Executive provides semantic authorization. Hard law remains non-bypassable.**

#### 2.2 Reasoning providers have no direct mutation authority

A reasoning provider MUST NOT directly possess:

- unrestricted filesystem mutation;
- shell authority;
- production credentials;
- database mutation authority;
- deployment authority;
- direct Canonical Workspace write access;
- memory-promotion authority.

Any requested effect becomes a typed proposal that enters the appropriate legal path.

Source: [FCA-2](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L114>); source-unit SHA-256 `1e3c2bdfdde657c48915fd327c3466475fde77ca47234f69229bd509ae4bcfb5`.

### L0-F03 — High-level runtime

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

Source: [FCA-3](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L162>); source-unit SHA-256 `9152a998b18ebe255cd960a0ca8e76924d9dbf572c72487b9231e9f422020635`.

### L0-F04 — Authority model

FCA recognizes distinct authorities:

#### 4.1 Semantic authority

The current **Cognitive Executive epoch** is the sole authority that may semantically authorize mutation of canonical cognitive state.

#### 4.2 Structural/legal authority

`CommitGate` and `ActionGate` enforce non-bypassable rules. The Executive cannot make an illegal operation legal.

#### 4.3 World authority

Reality determines what actually happened. Intention, generated code, or an LLM statement cannot substitute for observation.

#### 4.4 Learning authority

Experience may be captured automatically as history, but semantic promotion into reusable learned knowledge is governed by the Learning Gate and Executive authorization.

#### 4.5 Human authority is domain-specific

A human source is not universally authoritative. Authority depends on the claim domain.

Examples:

```text
"Refunds use the original exchange rate."
→ authoritative requirement if stated by the requirement owner.

"I think PostgreSQL is causing the bug."
→ technical advice / hypothesis, not a fact.
```

Authority comes from trusted control metadata, not from wording inside content.

Source: [FCA-4](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L218>); source-unit SHA-256 `1906648da5554a989ad97d000bc32a9dc41507c2d7e2657b4b6ad80ac2dc47c1`.

### L0-F20 — Contracts

Contracts define stable expectations across boundaries. They may describe:

- data shape;
- behavior;
- ownership;
- state transitions;
- error semantics;
- compatibility;
- external expectations.

Workers and specialists MUST NOT silently rewrite shared contracts to make their local task easier.

Source: [FCA-20](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L950>); source-unit SHA-256 `7c575f0d124801852dd325143ed841ded74502d2f161c78a9dd60233e24ae19c`.

### L0-F21 — Canonical vocabulary

The project SHOULD maintain a canonical lexicon of important concepts and terms.

Naming consistency is not cosmetic; it supports shared mental-model reconstruction across time, humans, and specialists.

Source: [FCA-21](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L966>); source-unit SHA-256 `ee99b052449fb4e7ea51364d2e88d7fb9c6df935229de7f58712accc4a3b7a4f`.

### L0-F72 — Content envelope

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

Source: [FCA-72](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2618>); source-unit SHA-256 `e98974896112dac605c7596a594ac8628f354d23eb3fa38d206f119893dc02e1`.

### L0-F73 — Untrusted execution

Project scripts, generated code, build systems, and tests are treated as potentially untrusted execution.

A conforming implementation SHOULD use isolation that constrains:

- credentials;
- filesystem scope;
- network access;
- host effects;
- external mutation.

Unexpected effects are observations, not automatically intended effects.

Source: [FCA-73](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2656>); source-unit SHA-256 `abe467ed1424ecac6dd4102b0d4cd11ef86dccfc47ea6022de3d1e3af9c29483`.

### L0-F84 — Frozen principles

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

Source: [FCA-84](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2874>); source-unit SHA-256 `213cfa92e6c8646b50337b8cd6f532438e33797eb2d0845a9d8a2b6d5adb2fde`.

### L0-F87 — Change-control rule

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

Source: [FCA-87](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L3241>); source-unit SHA-256 `0ea449058d74fd838615cd5aae10c202ed902bb2ad34b93f2ee553e2231897cc`.

### L0-APP-C — Appendix C — Final authority matrix

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

Source: [FCA-APP-C](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L3517>); source-unit SHA-256 `1ff476779bede12807fb9f24e91585412cbea30fdf875ebcd0d7708052ef2aaf`.

### L0-APP-F — Appendix F — Minimum conformance scenario suite

A future implementation SHOULD convert at least the following into automated or semi-automated acceptance scenarios.

#### F.1 Authority

- stale Executive epoch cannot commit;
- stale Executive epoch cannot authorize a new Action;
- Specialist cannot commit canonical state;
- LLM cannot directly invoke a mutating world adapter;
- Executive cannot bypass a hard CommitGate violation.

#### F.2 Action durability

- crash before `DISPATCH_INTENT`;
- crash after durable `DISPATCH_INTENT` but before external call is known to leave the process;
- crash after external call but before result persistence;
- partial world effect;
- unknown non-idempotent result enters `IN_DOUBT`;
- no blind retry of `IN_DOUBT`;
- safety reconciliation continues after task budget exhaustion.

#### F.3 Observation/epistemic integrity

- LLM output cannot create Observation;
- semantic reasoning cannot directly promote causal interpretation to generic Fact;
- causal closure cannot occur without the Causal Closure Gate;
- a valid OperationalCausalClaim may be used as a settled premise only inside its recorded scope;
- contradictory observations are retained and scoped;
- disputed support lowers/reopens Fact confidence as appropriate;
- EvidenceLink requires an existing Observation target/source relationship.

#### F.4 Specialist concurrency

- unrelated global state changes do not falsely stale a Specialist result;
- changed actual dependency does stale/revalidate the result;
- overlapping write sets require reconciliation rather than last-write-wins;
- negative-search dependency invalidates after relevant repo/search-scope change;
- old-epoch Specialist output may integrate only under the current Executive after freshness validation.

#### F.5 Trigger durability

- temporal trigger fires after downtime;
- level trigger re-evaluates after restart;
- event trigger replays from durable cursor;
- duplicate fire does not duplicate canonical reaction;
- edge trigger without replayable history is rejected or represented differently;
- Decision and its mandatory Trigger persist atomically.

#### F.6 Trust boundary

- README/code comment containing fake “system instruction” remains data;
- tool output cannot self-promote to instruction authority;
- retrieved memory cannot self-promote to project policy;
- Specialist output cannot self-promote to authority;
- untrusted build/test scripts execute within the chosen isolation policy.

#### F.7 Memory governance

- Episode can be stored automatically;
- one Episode cannot jump directly to corroborated general schema;
- retrieved cross-project memory remains precedent;
- counterexample can refine applicability without deleting provenance;
- superseded knowledge remains historically traceable.

#### F.8 Operational-efficiency and causal-closure

- routine low-gravity internal edits do not require MMRT;
- MMRT disagreement alone cannot reject a change;
- high-gravity interface/ownership/invariant changes invoke MMRT when the capability is available and no stronger semantic review substitutes;
- negative symbol knowledge survives unrelated repository changes;
- relevant symbol/index/frontier changes mark the negative conclusion stale;
- dynamic-dispatch uncertainty prevents overclaiming static negative knowledge as total runtime absence;
- disposable sandbox micro-actions can use the aggregated fast path;
- any reachable canonical/shared effect prevents `EPHEMERAL_SANDBOX` classification;
- sandbox output enters canonical/shared state only through the normal shared-world action path;
- “fix makes test pass” alone cannot create an OperationalCausalClaim;
- reproduced + predicted + targeted-intervention + regression-supported causal closure can create an OVC;
- contradictory observations or dependency/scope changes stale/reopen the OVC.

#### F.9 Temporal continuity

- suspended task always has a Resumption Capsule;
- resume checks relevant repo/world/dependency changes;
- blocked/waiting/deferred states remain distinct;
- obsolete goals can be retired without erasing history;
- temporary commitment cannot exist without a reactivation/removal mechanism.

Source: [FCA-APP-F](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L3742>); source-unit SHA-256 `94b091d3a85d654881fb7618023485f60267074cf74eb6a38003a0eed22eb3d8`.

### L0-APP-G — Appendix G — Frozen architecture in one page

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

Source: [FCA-APP-G](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L3832>); source-unit SHA-256 `673e93febb524cf3f14e8821497d37112554dc5ff73614407285ffd9cf84b48b`.

## Cross-cutting invariant responsibilities


**FCA-I01** — Only the current Executive may semantically authorize canonical cognitive-state mutation.

Source: [FCA-I01](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2915>).


**FCA-I16** — There is exactly one canonical cognitive authority per project state.

Source: [FCA-I16](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2949>).


**FCA-I24** — Executive authorization cannot override currently valid hard architectural law.

Source: [FCA-I24](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2967>).


**FCA-I25** — A hard invariant cannot be silently weakened by the operation it constrains.

Source: [FCA-I25](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L2969>).


**FCA-I40** — Content cannot self-assign instruction authority.

Source: [FCA-I40](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L3003>).


**FCA-I41** — Reasoning providers possess no direct shared-world mutation authority.

Source: [FCA-I41](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L3005>).


## Source coverage, exports and verification

L0 exports the constitutional authority and trust obligations above to L1–L7. ContentEnvelope is owned here; owner-specific record refinements remain in the relevant layer. FCA §§0–4, 20–21, 72–73, 84 and 87 are incorporated with exact source units. §86 is a historical source freeze verdict, retained by reference rather than asserted as a new consolidated freeze. Appendix A and the Studies trace explain provenance; Appendix B is explicitly non-normative; Appendices C/F/G constrain authority and conformance without creating duplicate contract owners; Appendix D is the L2 composite view; Appendix E records approved FCA history. Layer-specific FCA sections, decimal subsections and remaining invariants are allocated in the architecture manifest/trace ledger.


Source freeze evidence: [FCA-86](<../documentation_checkpoint/source_archive/project/AI_CODING_AGENT/reviews/source_archive/Formal_Cognitive_Architecture_v1.0.1_FROZEN_SPEC.md#L3211>). FCA's v1.0.1 header and §0 explicitly establish precedence over the v1.0 historical baseline. No RDMS or GAIA artifact is admitted as a constitutional amendment. Verification checks the incorporated source-unit hashes, preserved source archive, single ContentEnvelope owner, imported-owner references and absence of independent provider authority. Consolidated freeze remains HOLD pending independent review and remaining layer/interface issues.
