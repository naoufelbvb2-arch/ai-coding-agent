# Formal Cognitive Architecture v1.0 — FROZEN SPEC

**Document ID:** FCA-1.0-FROZEN-SPEC  
**Status:** **FROZEN**  
**Architecture identity:** **One mind, many temporary specialists.**  
**Scope:** Formal cognitive architecture for an LLM-agnostic artificial software engineer / coding agent.  
**Normative status:** This document is the single source of truth for FCA v1.0. It supersedes the original *Formal Cognitive Architecture v1.0* draft and all C01/C02/C03 correction notes as separate normative references.

---

## 0. Purpose, provenance, and freeze boundary

This specification consolidates the complete design path that preceded implementation:

1. the original cognitive-engineer model;
2. Studies 01–10 of expert human software-engineering cognition;
3. the conceptual **Human Expert Programmer Cognitive Model v1.0**;
4. **Formal Cognitive Architecture v1.0**;
5. **C01 — Epistemic, Executive & State Corrections**;
6. **C02 — Runtime & Authority Corrections**;
7. **C03 — Durability & Trust Closure**;
8. adversarial Freeze Reviews 01–04;
9. final failure-injection review with **Freeze Review 04: PASS**.

The purpose of this document is not to describe a particular codebase, programming language, database, LLM provider, process topology, or UI. It freezes the **semantics, authorities, persistent state, legal write paths, cognitive capabilities, runtime safety contracts, and multi-agent rules** that any conforming implementation must preserve.

### 0.1 Normative language

- **MUST / MUST NOT**: frozen architectural requirement.
- **SHOULD / SHOULD NOT**: strong default; deviations require explicit rationale.
- **MAY**: implementation choice that does not change frozen semantics.

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
- safe-cancellation and `IN_DOUBT` semantics.

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
- whether optional capabilities such as MMRT ship in implementation V1 or V2;
- exact sandbox technology.

A future implementation decision that requires changing a frozen authority, state meaning, legal write path, invariant, or recovery guarantee **reopens FCA** and requires an explicit architecture correction/revision.

---

# Part I — Architectural identity

## 1. The system we are building

FCA v1.0 defines a persistent software-engineering cognitive system that behaves more like an expert engineer than a prompt-driven coding loop.

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

## 5. Cognitive Kernel

The logical center of the system is:

```text
┌──────────────────────────────────────┐
│          COGNITIVE KERNEL            │
│                                      │
│  Cognitive Executive                 │
│             ↕                        │
│  Canonical Cognitive Workspace       │
└──────────────────────────────────────┘
```

The Executive selects what cognitive operation should occur next. The Workspace contains the persistent canonical state against which cognition is performed.

The Executive MUST NOT be implemented as “the LLM itself.” Semantic reasoning is requested through capabilities.

---

## 6. Canonical Cognitive Workspace

The Workspace is the structured, persistent representation of the current accepted cognitive state of the project.

It replaces the idea that chat history is the agent’s mind.

A canonical state contains at least:

```text
State {
    identity

    goals
    focus

    model

    epistemic

    engineering

    execution

    temporal

    specialists

    memory_refs

    meta
}
```

### 6.1 Identity

```text
Identity {
    project_id
    global_state_version
    repo_ref
    schema_version
    current_executive_epoch
}
```

`global_state_version` establishes historical order. It MUST NOT be treated as sufficient proof that a specialist result is stale.

### 6.2 Goals

The agent maintains a hierarchy:

```text
Mission
  ↓
Milestone
  ↓
Task
  ↓
Subgoal
  ↓
Current cognitive operation
```

Every executable Slice MUST trace to a Goal.

### 6.3 Focus

Working cognition is intentionally bounded. The Workspace represents what is actively relevant without loading the whole project.

### 6.4 System Mental Model

The mental model contains at least:

```text
SystemMentalModel {
    domain
    structure
    runtime
    causal
    risk
}
```

It is a revisable belief state, not immutable documentation.

---

# Part IV — Epistemic model

## 7. Epistemic separation

The architecture MUST preserve the distinction between:

```text
Claim
InformationNeed
Hypothesis
Observation
EvidenceLink
ContradictionRecord
```

These entities are not interchangeable.

---

## 8. Claim

```text
Claim {
    id

    kind:
        fact
        belief
        assumption

    statement
    scope

    support:
        unassessed
        weak
        moderate
        strong
        verified

    evidence_for[]
    evidence_against[]

    provenance[]

    status:
        active
        refuted
        superseded

    temporal_validity

    version
}
```

### 8.1 Fact Promotion Law

A Claim may be a `fact` only through one of three paths:

1. **Observed Fact** — faithful normalization of an accepted Observation.
2. **Deterministic Fact** — mechanically derived from accepted observations/facts.
3. **Authoritative Fact** — asserted by a source whose authority covers that exact domain.

Semantic reasoning alone MUST NOT promote a proposition to Fact.

Causal conclusions remain hypotheses, even when `causally_verified`.

---

## 9. InformationNeed

Unknowns are explicit state, not vague absence.

```text
InformationNeed {
    id
    question

    importance
    blocks[]

    source_candidates[]

    resolvable:
        internally
        reality
        human
        external_dependency

    status:
        open
        investigating
        resolved
        obsolete

    resolution?
}
```

The agent SHOULD ask a human only when a high-impact unknown cannot be discovered from available technical evidence and requires human policy/requirement authority.

---

## 10. Hypothesis

```text
Hypothesis {
    id
    explanation

    explains[]
    assumptions[]

    predictions[]

    evidence_for[]
    evidence_against[]

    competing_hypotheses[]
    experiments[]

    support:
        untested
        plausible
        supported
        strong
        causally_verified
        refuted

    status:
        active
        rejected
        confirmed
        superseded
}
```

A suspicion is not permission to modify the system.

> **Suspicion is not authorization for action.**

---

## 11. Observation

An Observation represents what was actually observed, measured, read, or authoritatively stated.

```text
Observation {
    id

    source
    source_authority?

    world_ref
    repo_ref?
    environment_ref?

    observed_at

    content
    raw_ref?

    provenance

    integrity:
        verified
        unverified
        degraded
}
```

Observations enter only through `Observation Ingress`.

Reasoning providers MUST NOT manufacture canonical Observations.

---

## 12. EvidenceLink

Observation and interpretation are deliberately separate.

```text
EvidenceLink {
    id

    observation_id

    target_type:
        claim
        hypothesis
        decision
        risk
        model_element

    target_id

    relation:
        supports
        weakens
        contradicts
        relevant

    rationale

    derivation:
        deterministic
        semantic
        authoritative

    status:
        proposed
        accepted
        rejected
        superseded
}
```

A reasoning capability MAY propose an EvidenceLink. Canonical acceptance requires the cognitive commit path.

> **Reality supplies observations; cognition assigns meaning to them.**

---

## 13. Contradictory observations

Observations MUST NOT use “latest wins” semantics.

```text
ContradictionRecord {
    id

    observations[]
    subject
    compared_scope

    status:
        candidate
        confirmed
        explained
        unresolved

    possible_dimensions:
        time
        input
        environment
        world_version
        nondeterminism
        measurement_error

    information_need_id?
}
```

Before observations are treated as contradictory, the system compares their time, input identity, environment, and world/repository scope.

A verified Fact whose supporting observation becomes materially disputed MUST be re-evaluated.

---

## 14. Confidence

A naked uncalibrated probability such as `0.83` is not the default confidence representation.

```text
ConfidenceAssessment {
    level:
        unknown
        low
        medium
        high
        verified

    basis: EvidenceLinkId[]
    residual_uncertainty[]
    assessed_at
}
```

For multi-dimensional decisions:

```text
ConfidenceProfile {
    functional_correctness
    architecture
    concurrency
    security
    migration
    performance
    operability
}
```

Confidence MUST identify its basis and scope.

---

# Part V — Goals, focus, decisions, and engineering state

## 15. Goal and Goal Stack

```text
Goal {
    id
    parent_id?

    intent
    acceptance[]
    priority

    status:
        backlog
        ready
        active
        suspended
        blocked
        waiting
        deferred
        verified
        closed
        obsolete

    created_from
}
```

```text
GoalStack {
    mission
    milestone?
    task?
    subgoal?
    current_operation?
}
```

No active engineering action should exist without a parent intent.

Side discoveries do not automatically replace the active goal. They become backlog items unless their severity justifies an explicit priority transition.

---

## 16. Focus State

```text
FocusState {
    current_goal
    current_subgoal

    active_entities[]
    active_files[]
    active_symbols[]
    active_concepts[]

    active_hypotheses[]

    information_needs[]

    current_information_patch?
    ignored_context[]

    reason_for_focus
}
```

The agent SHOULD seek the smallest correct amount of information rather than maximize context.

---

## 17. Decision

```text
Decision {
    id

    question
    context

    gravity:
        low
        medium
        high

    quality_drivers[]
    constraints[]

    alternatives[]

    chosen

    rejected[] {
        option
        reason
    }

    assumptions[]

    accepted_tradeoffs[]

    evidence_refs[]

    expected_consequences[]
    risks[]

    revisit_triggers[]

    status:
        proposed
        accepted
        superseded
        invalidated

    version
}
```

A Decision records not only *what* was chosen, but *why, under what conditions, with what trade-offs, and when it should be reopened*.

---

## 18. Decision Gravity

Decision Gravity controls cognitive depth.

It considers, conceptually:

```text
irreversibility
blast radius
uncertainty
security / data risk
external compatibility
expected lifetime
future change cost
```

Low-gravity decisions use fast paths. High-gravity decisions may require:

- deeper information gathering;
- multiple alternatives;
- future/evolution simulation;
- experiments;
- independent review;
- stronger proof obligations.

Decision Gravity is a policy concept. Exact numeric thresholds are not frozen.

---

# Part VI — Typed invariants, contracts, and vocabulary

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

## 21. Canonical vocabulary

The project SHOULD maintain a canonical lexicon of important concepts and terms.

Naming consistency is not cosmetic; it supports shared mental-model reconstruction across time, humans, and specialists.

---

# Part VII — Capabilities

## 22. Capability is not a module, service, agent, or LLM call

A cognitive capability is a semantic ability. It may compose several execution mechanisms.

```text
Capability
    ├── Deterministic Atom
    ├── Reality Atom
    └── Reasoning Atom
```

`Specialist` is not an atom type. It is an execution topology.

```text
ExecutionMode =
    LOCAL
    SPECIALIST
```

This prevents “one cognitive skill = one agent/service.”

---

## 23. Capability contract

A capability reads an explicitly scoped cognitive view and returns proposals.

```text
run(
    CognitiveView,
    Objective,
    Budget
) -> CapabilityResult
```

```text
CapabilityResult {
    patch_proposal?

    proposed_claims[]
    proposed_hypotheses[]
    proposed_information_needs[]

    evidence_refs[]

    tool_requests[]
    experiment_requests[]

    confidence_assessment?

    specialist_request?

    needs[]

    rationale_summary?
}
```

A Capability MUST NOT manufacture Observation/Evidence as if it came from reality.

It may request observations through tools and refer to existing observations/evidence links.

---

## 24. Core cognitive capabilities

FCA v1.0 includes these semantic capabilities:

### 24.1 Intent & Goal Modeling

Determines:

- what the user actually wants;
- constraints;
- acceptance criteria;
- ambiguity;
- non-goals;
- goal hierarchy.

### 24.2 System Mental Modeling

Builds and revises:

- domain model;
- structural model;
- runtime model;
- causal model;
- risk model.

### 24.3 Attention & Information Foraging

Chooses:

- which unknown matters now;
- which source is most informative;
- where to look;
- when to stay in or leave an information patch;
- when to zoom in/out.

### 24.4 Hypothesis & Causal Reasoning

Creates and revises competing explanations and causal models.

### 24.5 Experiment Design

Designs low-cost discriminating tests/experiments between hypotheses.

### 24.6 Engineering Judgment

Generates alternatives, reasons over quality attributes, simulates future consequences, compares trade-offs, and records decisions.

### 24.7 Adaptive Planning

Builds dependency-aware execution graphs and resolves high-risk knowledge dependencies early.

### 24.8 Code Construction

Converts semantic intent and constraints into candidate code.

### 24.9 Verification

Checks deterministic structure and orchestrates behavioral evidence.

### 24.10 Reader Simulation / MMRT

Reconstructs the mental model from code in an isolated context and compares it with the intended model.

### 24.11 Metacognition

Monitors reasoning quality, evidence/confidence mismatch, contradictions, stagnation, drift, and strategy.

### 24.12 Learning & Experience Consolidation

Extracts candidate lessons and routes them through memory governance.

---

# Part VIII — Executive control

## 25. Executive responsibilities

The Executive:

- owns semantic authorization;
- selects current goal/focus;
- selects the next capability;
- determines cognitive depth;
- decides whether more evidence is needed;
- decides whether to deliberate, investigate, execute, review, suspend, delegate, or ask a human;
- controls specialist recruitment;
- controls budgets and WIP;
- integrates results;
- authorizes legal proposals;
- controls transitions between cognitive states.

The Executive MUST NOT bypass CommitGate/ActionGate and MUST NOT treat a reasoning-provider output as evidence merely because it was produced.

---

## 26. Executive state machine

The normal cognitive state machine contains:

```text
INTAKE
ORIENT
INVESTIGATE
DELIBERATE
PLAN
EXECUTE_SLICE
VERIFY
DIAGNOSE
REVIEW

ASK_USER

SPAWN_SPECIALIST
INTEGRATE

BLOCKED
WAIT

SUSPEND
RESUME

FINALIZE
```

The architecture is recurrent, not a fixed pipeline. Any state may legally return to a higher reasoning level when new evidence invalidates a lower-level plan.

Examples:

```text
coding → new domain concept → ORIENT

verification mismatch → DIAGNOSE

complexity surprise → DELIBERATE / REPLAN

critical stakeholder ambiguity → ASK_USER
```

### 26.1 Transition authority

Capabilities produce structured signals. The Executive transition policy selects the next state.

A reasoning provider does not directly control the state machine.

---

## 27. Fast path and deep path

A trivial task may follow:

```text
Understand
→ local model
→ change
→ verify
→ review
→ done
```

A high-gravity task may follow:

```text
Understand
→ orient
→ investigate
→ competing hypotheses / alternatives
→ experiments
→ future stress simulation
→ decision
→ risk-first plan
→ incremental execution
→ independent review
→ full verification
→ learning
```

Same architecture; different depth.

---

# Part IX — Planning and safe execution

## 28. Execution plan

A plan is not merely a list of tasks.

It is a graph of safe transitions with dependencies, risk, uncertainty, and proof obligations.

Dependencies may include:

```text
structural
data
behavioral
knowledge
validation
rollout
```

The agent SHOULD resolve knowledge dependencies early when they could invalidate large amounts of downstream work.

---

## 29. Slice

```text
Slice {
    id

    goal_id
    parent_slice?

    intent

    dependencies[]

    allowed_scope[]
    forbidden_scope[]

    preconditions[]

    invariants[]
    contracts[]

    expected_effects[]

    expected_change_surface {
        modules[]
        contracts[]
        state_owners[]
        public_apis[]
        persistent_data[]
    }

    risk_profile

    proof_obligations[]

    verification[]

    rollback

    base_state_version
    base_repo_ref

    status

    actual_effects[]
    actual_change_surface?
}
```

A Slice SHOULD be semantically small, not merely low in line count.

---

## 30. Valid state transitions

The planning principle is:

```text
Valid State S0
    ↓ change + proof
Valid State S1
    ↓ change + proof
Valid State S2
```

The system SHOULD minimize the distance between implementation and verification.

---

## 31. Deviation

A significant unexpected expansion of change surface, violated assumption, or architectural deviation MUST trigger reconciliation of at least one of:

```text
mental model
plan
decision
```

Silent architectural drift is forbidden.

---

# Part X — Code construction and verification

## 32. Constrained synthesis

Generated code is candidate code.

Before code synthesis, the system SHOULD provide only the relevant bounded context including:

```text
intent
current slice
relevant mental model
responsibility
allowed / forbidden dependencies
contracts
invariants
canonical vocabulary
expected behavior
failure semantics
proof obligations
complexity budget
```

The reasoning model does not receive unlimited context by default.

---

## 33. Concept-to-code mapping

Code SHOULD preserve important domain and system concepts sufficiently that a future reader can reconstruct the intended mental model.

Abstraction exists to compress and protect meaning, not merely to create more files/layers.

> **Every abstraction, layer, and indirection must pay rent.**

Legitimate rent may include:

- stable conceptual boundary;
- state ownership;
- protocol translation;
- invariant locality;
- isolation;
- substitution;
- security;
- testability;
- change locality.

---

## 34. State-space discipline

Representations and types SHOULD reduce illegal states where doing so meaningfully improves reasoning or correctness.

Assignments and mutations are treated as state transitions with:

- authority;
- legality;
- invariants;
- side effects;
- concurrency semantics.

---

## 35. Verification layers

Verification is explicitly separated into:

### 35.1 Structural Diff — deterministic

Examples:

- files changed;
- AST changes;
- dependency changes;
- public API changes;
- schema changes;
- architecture-rule violations.

### 35.2 Behavioral Evidence — reality

Examples:

- tests;
- runtime traces;
- benchmarks;
- debugger observations.

### 35.3 Semantic Change Analysis — reasoning

```text
SemanticChangeProposal {
    intended_behavior_change[]
    responsibility_changes[]
    ownership_changes[]
    invariant_implications[]
    likely_unintended_effects[]
}
```

Semantic analysis is a proposal, not a deterministic truth source.

### 35.4 Conformance Evaluation

Compares:

```text
Expected Effects
vs
Structural Diff
vs
Behavioral Observations/Evidence
vs
Semantic Analysis
```

Machine-expressible rules are enforced deterministically. Semantic judgments become structured signals to the Executive.

---

## 36. Reader Simulation / MMRT

MMRT operates in an isolated context.

A reviewer reconstructs from the code:

```text
responsibilities
state ownership
main flow
invariants
failure behavior
extension boundaries
```

The reconstructed model is compared against the intended model.

MMRT is not a deterministic Verification Engine function.

---

# Part XI — Metacognition

## 37. Metacognitive laws

The system follows these laws:

> **Fluency is not evidence.**

> **The agent’s previous output is not evidence merely because it produced it.**

> **Confidence follows evidence; evidence is not selected to defend confidence.**

> **Unexpected difficulty is information.**

> **Activity is not progress.**

> **A successful outcome does not prove that the reasoning that produced it was correct.**

> **A failed experiment is useful if it reduces uncertainty.**

---

## 38. Prediction error

Whenever:

```text
Expected ≠ Observed
```

the system asks:

```text
Which model may be wrong?

Mental model?
Requirement interpretation?
Hypothesis?
Architecture?
Plan?
Implementation?
Test expectation?
External assumption?
```

It does not automatically assume “the code needs another patch.”

---

## 39. Detectors

Architecture freezes detector semantics, not arbitrary numeric thresholds.

### PatchCascadeDetector

May track:

- repeated repair attempts;
- recurring failure signature;
- new failures introduced;
- expanding scope;
- repeated revisits;
- evidence gained.

### BlastRadiusDetector

Compares expected vs actual change surface across more than file count.

### StagnationDetector

May track:

- repeated files;
- repeated hypothesis;
- same failed tests;
- low information gain;
- repeated tool actions.

### DriftDetector

At minimum, a Slice without a parent Goal is an immediate drift violation.

Numeric policy thresholds remain configurable according to project profile, gravity, risk, and budget.

---

# Part XII — Experiments

## 40. Experiment

```text
Experiment {
    id

    question

    target_hypotheses[]

    method

    predictions[] {
        hypothesis_id
        expected_observation
        discriminates_from[]
    }

    required_actions[]

    risk_profile

    status:
        designed
        authorized
        running
        completed
        failed
        cancelled

    observation_ids[]

    conclusion_proposal?

    designed_at
    executed_at?
}
```

Predictions MUST become durable before the experiment begins.

After execution starts, the prediction record for that Experiment is immutable.

Diagnostic interventions still require legal ActionProposal paths when they mutate reality.

---

# Part XIII — World actions

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

## 42. ActionProposal

```text
ActionProposal {
    id

    requested_by
    slice_id
    goal_id

    kind:
        file_write
        file_delete
        shell
        git
        database
        network
        deployment
        debugger_control
        other

    target_scope[]

    intent
    expected_effects[]

    preconditions[]

    risk_profile

    reversibility:
        reversible
        compensatable
        partially_reversible
        irreversible

    rollback_or_compensation?

    mode:
        diagnostic
        production

    base_world_ref

    authority_required

    effect_semantics

    status
}
```

---

## 43. Action Effect Semantics

Every mutating Action declares retry/outcome semantics before execution.

```text
ActionEffectSemantics {
    effect_identity?

    retry_policy:
        IDEMPOTENT
        PROBE_THEN_RETRY
        NO_AUTOMATIC_RETRY

    idempotency_key?

    outcome_probe?

    compensation?

    verification_mode:
        DIRECT_EFFECT
        ACKNOWLEDGEMENT_ONLY
        BEST_EFFORT

    timeout_policy
}
```

The architecture does not claim exactly-once external effects when the underlying domain cannot provide them.

---

## 44. Action lifecycle

```text
ActionLifecycle {
    PROPOSED
    AUTHORIZED
    DISPATCH_INTENT
    RESULT_REPORTED
    EFFECT_VERIFIED

    PARTIAL
    FAILED
    IN_DOUBT

    RECONCILING
    RECONCILED
}
```

`IN_DOUBT` is neither success nor failure.

An unknown non-idempotent outcome MUST NOT be blindly retried.

---

## 45. Write-Ahead Action Protocol

The legal order for external mutation is:

```text
ActionProposal
    ↓
Executive semantic authorization
    ↓
ActionGate
    ↓
persist AUTHORIZED
    ↓
persist DISPATCH_INTENT
    ↓
durable acknowledgement
    ↓
ONLY NOW dispatch world mutation
    ↓
record reported result
    ↓
observe actual effect
    ↓
reconcile
```

No externally mutating call may begin before durable dispatch intent exists.

---

## 46. Action Record

```text
ActionRecord {
    action_id
    proposal_ref

    lifecycle

    world_ref_before
    world_ref_after?

    execution_result?

    observation_ids[]

    compensation_action_id?

    started_at?
    finished_at?
}
```

Intent, execution attempt, returned result, and verified world effect are distinct.

---

## 47. Safe cancellation

Budget exhaustion may stop new work. It MUST NOT abandon an unresolved world mutation.

A `SafetyReserve` may be consumed for reconciliation.

If reconciliation cannot complete, the action becomes durably `IN_DOUBT`, dependent work is blocked, and the task may then suspend safely.

A timeout MUST NOT be interpreted as proof that an external effect stopped.

---

# Part XIV — Durable control and recovery

## 48. Control Ledger

The Control Ledger is the authoritative durability boundary for control-plane state.

It stores or atomically references at least:

```text
Executive Epoch
Canonical cognitive commits
Action lifecycle
Trigger lifecycle
Specialist lifecycle
Memory promotions
Goal/task lifecycle
```

Large artifacts may live elsewhere, but recoverability-critical references and lifecycle metadata belong to the authoritative control boundary.

Each canonical event includes at least:

```text
event_id
schema_version
idempotency_key
```

---

## 49. Atomic control transitions

Transitions whose control metadata is jointly required for recovery MUST commit atomically.

Example:

```text
DecisionAccepted
+
TriggerArmed
+
StateVersionAdvanced
```

must appear together or not at all.

---

## 50. Executive epoch and fencing

```text
LeadershipGrant {
    project_id
    executive_id
    epoch
    status
    acquired_at
}
```

Only the current epoch may authorize new canonical effects.

Every authority-bearing operation includes `executive_epoch`.

If a new Executive acquires epoch N+1, requests from older epochs are fenced.

Loss of leadership does not erase world effects already durably dispatched.

---

## 51. Leadership handoff

A new Executive performs:

```text
1. acquire new epoch
2. fence old authority
3. inspect unfinished actions
4. inspect specialists
5. inspect pending triggers
6. inspect blocked/waiting work
7. reconcile before new conflicting effects
```

An action that was only `AUTHORIZED` under an old epoch requires explicit adoption by the new Executive.

An action at `DISPATCH_INTENT` or later enters reconciliation.

---

## 52. Startup recovery

A complete process restart restores cognition from durable state, not chat history.

Recovery sequence:

```text
1. Restore canonical snapshot.
2. Replay Control Ledger.
3. Obtain a valid Executive epoch.
4. Inspect unresolved ActionRecords.
5. Reconcile possibly dispatched effects.
6. Replay/evaluate durable triggers.
7. Inspect Specialist workspaces.
8. Validate dependency freshness.
9. Restore active/suspended/blocked work.
10. Resume normal Executive control.
```

---

# Part XV — Temporal cognition

## 53. Resumption Capsule

Every suspended task has:

```text
ResumptionCapsule {
    task_id

    suspended_from_state

    base_state_version
    repo_ref

    goal
    subgoal

    current_focus

    current_hypotheses[]
    relevant_evidence[]

    rejected_paths[]

    temporary_changes[]

    open_information_needs[]

    next_concrete_action?

    created_at
}
```

Resume does not mean blindly continuing the old next step.

It means:

```text
restore capsule
+
compute world/repository diff
+
mark stale dependencies
+
reconcile
+
resume
```

---

## 54. Temporal validity

State that can become stale carries validity metadata.

```text
TemporalValidity {
    observed_at?
    verified_at?

    repo_ref?
    state_version?

    valid_until_condition?

    freshness:
        current
        stale
        unknown
}
```

---

## 55. Commitments

Temporary engineering state must not become permanent by forgetting.

A Commitment records:

```text
why temporary?
until when / under what condition?
removal or revisit trigger?
owner?
```

A future commitment without a reactivation mechanism is invalid.

---

## 56. Durable Trigger Condition

```text
TriggerCondition {
    id
    generation

    semantics:
        ONE_SHOT
        REARMABLE
        LEVEL_TRIGGERED
        EDGE_TRIGGERED

    kind:
        state_event
        repo_change
        metric_threshold
        temporal
        external_event
        human_event
        semantic_review

    watches[]
    predicate?

    source_cursor?

    reaction_key

    linked_object
    on_fire

    status:
        armed
        fired
        satisfied
        cancelled

    last_evaluated_at
    last_fire_id?
}
```

Trigger detection may be at-least-once. Its canonical reaction must be idempotent.

Edge-triggered commitments require a replayable source capable of proving the edge occurred during downtime.

---

# Part XVI — Memory and learning

## 57. Memory categories

FCA conceptually distinguishes:

```text
Working Memory
Project Semantic Memory
General Semantic Memory
Episodic Memory
Procedural Memory
Decision Memory
Failure / Anti-pattern Experience
Project Lexicon
Temporal Commitments
```

These categories need not map one-to-one to physical databases.

---

## 58. Episode vs learned knowledge

An episode is historical experience and MAY be captured automatically.

Learned knowledge is semantic promotion and requires governance.

```text
Episode
  ↓
Reflection
  ↓
MemoryProposal
  ↓
Learning Gate
  ↓
Executive authorization
  ↓
Memory Store
```

---

## 59. Memory maturity

```text
EPISODE
↓
TASK_LESSON
↓
PROJECT_LESSON
↓
CANDIDATE_GENERALIZATION
↓
CORROBORATED_SCHEMA
```

A single successful event MUST NOT automatically become a general engineering rule.

---

## 60. MemoryProposal

```text
MemoryProposal {
    claim

    proposed_scope

    source_episodes[]

    causal_basis?

    applicability_conditions[]
    counter_conditions[]
    counterexamples[]

    evidence_refs[]

    confidence_assessment

    maturity_target
}
```

---

## 61. Memory metadata

```text
MemoryMetadata {
    scope:
        task
        project
        organization
        domain
        ecosystem
        general

    provenance[]

    applicability_conditions[]
    counter_conditions[]

    confidence_assessment

    stability:
        transient
        version_sensitive
        project_stable
        general_stable

    derived_from[]
    supersedes[]
}
```

Memory is fallible, scoped, versioned, and provenance-bearing.

---

## 62. Retrieval law

Retrieved memory enters current cognition as:

```text
precedent
analogy candidate
procedural suggestion
```

not as current Fact.

> **Experience → hypothesis / precedent, not authority.**

Transfer is based preferentially on structural and causal similarity, not surface textual similarity.

---

# Part XVII — Specialists and team cognition

## 63. One mind, many temporary specialists

FCA does not define permanent agents such as:

```text
Architect Agent
Planner Agent
Coder Agent
Tester Agent
Reviewer Agent
```

by default.

A single cognitive system contains multiple cognitive capabilities.

A Specialist is recruited only when separation itself has value.

---

## 64. Specialist creation conditions

A Specialist MAY be created when at least one is true:

- parallel work can proceed safely;
- independent judgment is valuable;
- context isolation is valuable;
- specialized tools/knowledge are valuable;
- deliberate hypothesis/design diversity is valuable.

Otherwise the central cognitive system performs the work itself.

---

## 65. Specialist

```text
Specialist {
    id

    parent_task
    goal
    scope

    workspace_id

    base_state_version
    base_repo_ref

    dependency_set[]

    authority {
        read[]
        modify_local[]
        propose[]
        forbidden[]
    }

    isolation_mode

    expected_output
    proof_obligations[]

    budget

    status:
        spawned
        working
        completed
        failed
        expired
        integrating
        integrated
        rejected
}
```

A Specialist:

- may reason;
- may observe within its permitted scope;
- may perform explicitly authorized local/sandbox actions;
- may propose shared-world actions;
- may return findings and proposals.

A Specialist MUST NOT:

- commit canonical cognitive state;
- promote memory;
- weaken hard invariants;
- authorize its own global effect;
- merge itself;
- spawn child specialists in FCA v1.0.

---

## 66. Specialist contract

On creation it receives:

```text
goal
scope
bounded canonical context
allowed authority
forbidden changes
expected output
proof obligations
budget
dependency stamps
base repository/world references
```

It returns:

```text
result
observation/evidence references
proposed claims/hypotheses
semantic analysis
risks
proposed canonical changes
residual uncertainty
dependency set
```

---

## 67. Independent reviewer

An independent reviewer may intentionally begin without the author’s conclusion or confidence in order to preserve cognitive independence.

Its orientation is:

> **How could this be wrong?**

not:

> How can I justify the proposed solution?

Agent vote count never outweighs stronger evidence.

---

## 68. Integration

Integration is not only Git merge.

It includes:

```text
dependency freshness
repo merge validity
world validity
structural verification
behavioral verification
semantic reconciliation
authority checks
Executive decision
```

Parallel specialists may explore independently; only the canonical mind owns accepted cognition.

---

# Part XVIII — Dependency freshness

## 69. DependencySet

Staleness is based on what a result actually depended on.

```text
DependencyStamp {
    kind:
        state_entity
        repo_content
        query_scope
        observation
        memory
        tool
        environment
        external_contract
        human_requirement

    ref

    version_or_hash?

    validity_condition?

    freshness_requirement:
        exact
        compatible
        advisory
}
```

The runtime SHOULD stamp dependencies automatically whenever possible.

Examples:

```text
Workspace read → entity version stamped
Repo read → hash/repo ref stamped
Tool execution → tool/environment stamped
Memory retrieval → memory version stamped
```

---

## 70. Negative knowledge

A conclusion such as:

```text
"No caller of function X exists."
```

depends on a search query and its scope.

```text
QueryDependencyStamp {
    query
    search_scope
    repo_ref
    index/version
}
```

If the repository or search scope changes, the negative conclusion may become stale even though no named entity changed.

---

## 71. Integration freshness result

```text
VALID
STALE
PARTIALLY_STALE
UNKNOWN
```

`PARTIALLY_STALE` permits salvaging unaffected findings while revalidating affected claims.

Global event version alone MUST NOT determine semantic staleness.

---

# Part XIX — Trust boundary

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

## 74. Canonical cognitive mutation

```text
Capability
   ↓
PatchProposal
   ↓
Executive semantic authorization
   ↓
CommitGate
   ↓
Canonical Workspace commit
   ↓
Control Ledger
```

The Executive can authorize a legal change. It cannot make an illegal change legal.

---

## 75. World mutation

```text
Capability / Specialist
   ↓
ActionProposal
   ↓
Executive semantic authorization
   ↓
ActionGate
   ↓
Write-Ahead Action Journal
   ↓
Reality Executor
   ↓
Observation Ingress
   ↓
Reconciliation
```

---

## 76. Observation append

```text
Reality / authoritative observation
   ↓
Observation Ingress
   ↓
schema + provenance + integrity validation
   ↓
immutable Observation
```

Observation append does not require semantic approval because it does not interpret the observation.

---

## 77. Memory promotion

```text
Episode / Reflection
   ↓
MemoryProposal
   ↓
Learning Gate
   ↓
Executive authorization
   ↓
Memory commit
```

---

## 78. Specialist result

```text
Specialist Result
   ↓
INTEGRATE
   ↓
dependency validation
repo/world validity
verification
semantic reconciliation
   ↓
Executive authorization
   ↓
canonical commit
```

There is no legal direct Specialist → Canonical Workspace path.

---

# Part XXI — Reality and tools

## 79. Tools as epistemic instruments

Tools are not merely execution utilities.

```text
Repository
→ exact external project memory

Search
→ information navigation

Debugger
→ active observation

Tests
→ controlled experiments / behavioral evidence

Logs
→ historical observations

Git
→ software history

Runtime
→ current reality

Database
→ state observation

Documentation
→ external knowledge source
```

The agent uses tools to ask reality questions.

---

# Part XXII — Long-horizon operation

## 80. Cognitive continuity

The unit of continuity is not the conversation.

> **The unit of continuity is persistent cognitive state.**

The system maintains a current “Cognitive HEAD” and retrieves history on demand.

Chat history is not authoritative state.

---

## 81. WIP and task states

The architecture distinguishes:

```text
ACTIVE
SUSPENDED
BLOCKED
WAITING
DEFERRED
CLOSED
OBSOLETE
```

A large backlog does not imply a large active working set.

The Executive SHOULD keep the active-goal set intentionally small.

---

## 82. Safe suspension

Where possible, the system SHOULD suspend at a coherent boundary where:

- repository/world state is understood;
- temporary state is recorded;
- current reasoning is summarized;
- next action is explicit;
- no unresolved effect is silently abandoned.

---

## 83. Goal/architecture drift

Long-horizon review compares:

```text
Current reality
↕
Current milestone
↕
Architecture
↕
Current accepted mission
```

Intentional evolution is allowed. Silent drift is not.

---

# Part XXIII — System-wide governing principles

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

# Part XXIV — Formal invariants FCA-I01…FCA-I44

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

## 85. Normal cognitive loop

```text
USER GOAL
   ↓
INTAKE
   ↓
ORIENT
   ↓
facts / assumptions / unknowns
   ↓
Executive selects cognitive depth
   ↓
focus attention
   ↓
gather highest-value information
   ↓
need causal understanding?
   ├─ yes → hypotheses → experiments → observations
   ↓
need engineering decision?
   ├─ yes → alternatives → future simulation → trade-offs
   ↓
record legal Decision
   ↓
build adaptive execution graph
   ↓
choose coherent Slice
   ↓
constrained candidate-code synthesis
   ↓
ActionProposal(s)
   ↓
legal Action path
   ↓
structural + behavioral + semantic verification
   ↓
Expected == Observed?
   ├─ no → DIAGNOSE / ORIENT / REPLAN
   └─ yes
       ↓
REVIEW / metacognitive gate
       ↓
continue / integrate / finalize
       ↓
checkpoint canonical state
       ↓
Learning Gate when valuable
```

The loop may jump backward whenever reality invalidates the current model.

---

# Part XXVII — Freeze verdict and change control

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
   - FCA-I01…I44;
   - crash/retry scenarios;
   - split-brain/fencing;
   - stale specialist integration;
   - prompt-injection/trust-boundary tests;
   - trigger replay/deduplication;
   - memory-promotion tests;
   - `IN_DOUBT` action tests.

No implementation is compliant with FCA v1.0 merely because it “works.” It is compliant only if it preserves the authority, state, evidence, durability, trust, and recovery semantics frozen here.

---

# Closing definition

> **FCA v1.0 defines a persistent, evidence-grounded software-engineering cognitive system with one canonical executive authority, dynamically recruited isolated specialists, explicit separation between cognition, control, action, and observation, durable recoverable control state, conservative experience learning, and replaceable reasoning providers.**

And the architectural identity remains:

# **One mind, many temporary specialists.**

---

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

# Appendix D — Composite canonical-state view

The exact physical schema is implementation work, but the logical canonical state frozen by FCA can be summarized as:

```text
State {
  identity {
    project_id
    global_state_version
    repo_ref
    schema_version
    current_executive_epoch
  }

  goals {
    stack
    items[]
  }

  focus: FocusState

  model {
    domain
    structure
    runtime
    causal
    risk
  }

  epistemic {
    claims[]
    information_needs[]
    hypotheses[]
    observations[]
    evidence_links[]
    contradictions[]
    experiments[]
  }

  engineering {
    invariants[]
    contracts[]
    vocabulary[]
    decisions[]
    risks[]
  }

  execution {
    graph[]
    active_slice?
    deviations[]
    structural_diffs[]
    semantic_change_proposals[]
    verification_records[]
  }

  temporal {
    active_tasks[]
    suspended_tasks[]
    blocked_tasks[]
    waiting_tasks[]
    commitments[]
    triggers[]
    resumption_capsules[]
  }

  specialists[]

  memory_refs[]

  meta {
    confidence_profile
    contradictions[]
    prediction_errors[]
    stagnation_signals[]
    drift_signals[]
    residual_risks[]
    current_strategy
    cognitive_depth
  }

  control_refs {
    action_records[]
    control_events[]
    leadership_grant
  }
}
```

The physical implementation MAY normalize or separate these stores as long as authority, durability, consistency, and recovery semantics remain conformant.

---

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

---

# Appendix F — Minimum conformance scenario suite

A future implementation SHOULD convert at least the following into automated or semi-automated acceptance scenarios.

## F.1 Authority

- stale Executive epoch cannot commit;
- stale Executive epoch cannot authorize a new Action;
- Specialist cannot commit canonical state;
- LLM cannot directly invoke a mutating world adapter;
- Executive cannot bypass a hard CommitGate violation.

## F.2 Action durability

- crash before `DISPATCH_INTENT`;
- crash after durable `DISPATCH_INTENT` but before external call is known to leave the process;
- crash after external call but before result persistence;
- partial world effect;
- unknown non-idempotent result enters `IN_DOUBT`;
- no blind retry of `IN_DOUBT`;
- safety reconciliation continues after task budget exhaustion.

## F.3 Observation/epistemic integrity

- LLM output cannot create Observation;
- semantic reasoning cannot directly promote causal interpretation to Fact;
- contradictory observations are retained and scoped;
- disputed support lowers/reopens Fact confidence as appropriate;
- EvidenceLink requires an existing Observation target/source relationship.

## F.4 Specialist concurrency

- unrelated global state changes do not falsely stale a Specialist result;
- changed actual dependency does stale/revalidate the result;
- overlapping write sets require reconciliation rather than last-write-wins;
- negative-search dependency invalidates after relevant repo/search-scope change;
- old-epoch Specialist output may integrate only under the current Executive after freshness validation.

## F.5 Trigger durability

- temporal trigger fires after downtime;
- level trigger re-evaluates after restart;
- event trigger replays from durable cursor;
- duplicate fire does not duplicate canonical reaction;
- edge trigger without replayable history is rejected or represented differently;
- Decision and its mandatory Trigger persist atomically.

## F.6 Trust boundary

- README/code comment containing fake “system instruction” remains data;
- tool output cannot self-promote to instruction authority;
- retrieved memory cannot self-promote to project policy;
- Specialist output cannot self-promote to authority;
- untrusted build/test scripts execute within the chosen isolation policy.

## F.7 Memory governance

- Episode can be stored automatically;
- one Episode cannot jump directly to corroborated general schema;
- retrieved cross-project memory remains precedent;
- counterexample can refine applicability without deleting provenance;
- superseded knowledge remains historically traceable.

## F.8 Temporal continuity

- suspended task always has a Resumption Capsule;
- resume checks relevant repo/world/dependency changes;
- blocked/waiting/deferred states remain distinct;
- obsolete goals can be retired without erasing history;
- temporary commitment cannot exist without a reactivation/removal mechanism.

---

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
│ Action Journal / Executor          │
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
