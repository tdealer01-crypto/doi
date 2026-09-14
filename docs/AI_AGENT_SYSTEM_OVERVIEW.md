# DSG Spacetime — AI Agent System Public Overview

## Release scope

DSG Spacetime v1.1.0 documents the public-safe architecture of the **DSG AI Agent System as a whole**.

The system is designed so an AI can keep working toward a goal while planning, orchestration, authorization, execution and proof remain separate responsibilities.

## Mental model

```text
User Goal
   |
   v
AI Agent / Reasoning
   |
   v
Automation Spacetime
   |
   v
Core Spin
   |
   v
Governance Spacetime
   |
   v
Governed Routes -> Execution Capabilities
   |
   v
Evidence / Verification / Proof
   |
   +---- verified state ----> next reasoning round
```

## AI Agent

The AI agent reasons about the goal, current state and available capabilities. It can propose plans and next actions, but a model response is never treated as permission by itself.

This allows the reasoning model to evolve independently from the execution trust boundary.

## Automation Spacetime

Automation Spacetime describes **how the job should move**: sequencing, parallel work, agent assignment, handoff, retry/resume and checkpoints.

It is the workflow/orchestration layer. Workflow intent does not override action authorization.

## Governance Spacetime

Governance Spacetime answers a different question: **is this exact action allowed now?**

The public boundary may consider identity/context, Node/Route scope, policy, approvals, commercial entitlement where applicable and required evidence. Missing required authority is expected to fail closed.

## Core Spin

Core Spin connects the rounds. It preserves the job/session progression and carries verified results back into the next planning cycle.

Core Spin can continue, pause, retry within allowed bounds, request approval, block or complete. It cannot grant itself authority that Governance Spacetime did not provide.

## Nodes, Routes and tools

Nodes expose approved capabilities. Routes define governed paths to use those capabilities. Execution adapters perform approved actions in customer-owned or provider systems.

Examples include source control, cloud infrastructure, databases, AI/model providers, browser automation, payments, monitoring and enterprise systems.

These tools are replaceable capabilities inside the system. The DSG architecture is the control relationship around them.

## Evidence-driven continuation

Execution does not end with an AI saying "done". Material results are recorded and verified, then fed back into the control loop.

This creates the intended cycle:

```text
reason -> orchestrate -> authorize -> execute -> prove -> continue
```

## Safety objective

The public design objective is **maximum autonomy inside provable boundaries**:

- reasoning is not permission;
- orchestration is not permission;
- memory/state is not permission;
- tool availability is not permission;
- only governed execution can cause an authorized side effect;
- evidence is required to support claims about what actually happened.

## Capability examples

Browser control, source control, cloud APIs, databases, models and payment systems may all participate as Nodes or adapters. No individual capability defines the architecture, and adding a new capability does not remove the same governance boundary.

## Intellectual-property boundary

This publication intentionally does not disclose production source, private prompts, proprietary governance algorithms, solver constraints, internal schemas, anti-bypass implementation, detailed deployment topology, credentials, private tests or confidential operational evidence.
