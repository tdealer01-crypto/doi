# DSG Spacetime — Public AI Agent System Architecture

## Scope

This document describes the DSG AI Agent System at a conceptual, publication-safe level. It is intentionally about the **whole agent system**, not one browser, cloud, database, model or provider integration.

## System model

```text
Goal / User Intent
        |
        v
AI Agent / Reasoning Layer
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
Nodes + Governed Routes
        |
        v
Execution Adapters
        |
        v
Customer / Provider Systems
        |
        v
Evidence -> Verification -> Proof
        |
        +------ verified state/result ------> Core Spin
```

## AI Agent / Reasoning Layer

The AI layer interprets goals, inspects available context and proposes plans or next actions. It may select among approved capabilities, but its proposal does not grant execution authority.

The architecture separates **reasoning authority** from **execution authority**. A more capable model can improve planning without automatically receiving broader permissions.

## Automation Spacetime

Automation Spacetime represents how a goal progresses through work. At the public level this includes sequencing, parallel work, agent assignment, handoff, retry/resume behavior and checkpoints.

Automation decides **how work should proceed**. It does not decide that a side effect is authorized merely because the workflow requests it.

## Governance Spacetime

Governance Spacetime evaluates whether an exact requested action is allowed in the current context. Publicly described inputs may include identity/context, capability and Route scope, entitlement where applicable, required approval, policy conditions and evidence requirements.

Missing required authorization is expected to block execution rather than silently downgrade the control.

## Core Spin

Core Spin is the stateful control loop connecting AI reasoning, automation, governance, execution results and the next decision round.

Conceptually, Core Spin carries goal/job state, prior verified outcomes and continuation status so the system can continue, pause for approval, retry within allowed bounds, block, or complete. Core Spin is orchestration state; it is not a bypass around Governance Spacetime.

## Nodes

A Node is an approved capability boundary. Examples include source control, cloud infrastructure, databases, AI/model providers, browsers, payment systems, enterprise applications, monitoring systems and internal customer APIs.

A Node defines what capability exists. Existence alone does not authorize its use.

## Routes

A Route is a governed capability path between Nodes. It binds a requested operation to the governance requirements that apply before execution.

## Execution adapters

Approved actions execute through configured customer-owned or provider adapters rather than unrestricted model-to-provider access. Existing systems remain authoritative for their own data and side effects.

A browser, shell, source-control API, cloud API, database or payment integration is an execution capability inside this layer — not the control architecture itself.

## Evidence and proof

Material execution produces durable evidence within the supported scope. Verified results are fed back into the control loop rather than relying on an AI assertion that an action succeeded.

Proof is verification material derived from execution evidence and governed context. Public proof may be redacted to protect customer and implementation details while preserving the claim boundary.

## AI-first lifecycle

```text
intent
  -> discover approved capabilities
  -> compose proposed work
  -> bind execution context
  -> authorize exact Routes/actions
  -> execute through approved adapters
  -> record evidence
  -> verify result
  -> update Core Spin state
  -> continue / wait for approval / block / complete
```

## Design objective

**Maximum autonomy inside provable boundaries.**

The system is designed so AI agents can reason and operate continuously without equating intelligence, orchestration or persistence with permission.

## Public/private boundary

This document intentionally omits production source, proprietary policy algorithms, solver internals, private schemas, prompt/instruction internals, credential handling internals, anti-bypass implementation, detailed deployment topology and private test mechanics.
