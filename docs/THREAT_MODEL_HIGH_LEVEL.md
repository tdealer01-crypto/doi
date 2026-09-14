# DSG Spacetime — High-Level Threat Model

This document describes public security objectives for the DSG AI Agent System. It intentionally omits implementation-level anti-bypass logic, private schemas, solver constraints, secret identifiers, private prompts and defensive assumptions that would weaken the proprietary security boundary.

## Assets to protect

- customer-controlled systems and credentials
- deployment identity and entitlement scope
- approved Node/Route capability boundaries
- execution authorization decisions
- agent/job state and continuation integrity
- durable evidence and proof records
- seller-controlled commercial trust root

## Threat classes

### Untrusted AI proposal

An AI-generated plan or next action may request capabilities beyond the intended scope. The architecture therefore treats reasoning and composition as proposals rather than authorization.

### Orchestration drift

A long-running workflow may retry, resume, hand off work, branch in parallel or continue across multiple reasoning rounds. Orchestration state must not silently widen authority as the job progresses.

### Cross-agent authority confusion

One agent or model may produce context for another. A handoff must not cause the receiving agent to inherit permissions that were not independently valid for the requested action.

### Unauthorized Route use

An actor or agent may attempt to execute a Route that is not approved, licensed or valid for the deployment context. The intended behavior is fail-closed blocking.

### State or result substitution

A control loop may receive stale, fabricated or unverified results. Continuation decisions should rely on the supported evidence/verification boundary rather than treating an AI assertion as proof of successful execution.

### Entitlement tampering or substitution

Commercial authorization material may be modified, replaced or self-issued by an unauthorized party. The runtime is designed to trust seller-controlled signing authority and reject invalid deployment/signature scope.

### Credential overreach

An agent may attempt to obtain unrestricted provider credentials or bypass the approved adapter/capability boundary. The architecture avoids direct unbounded model-to-provider credential use.

### Untrusted tool or external-system output

Tool, browser, API, model or external-system output may be misleading or hostile. External output is treated as input to reasoning, not as authority to widen execution scope.

### Evidence tampering

A party may attempt to modify execution history after the fact. DSG Spacetime is designed to produce tamper-evident evidence suitable for later verification within the tested scope.

### Replay or duplicate side effects

Governed execution paths may be retried or replayed. Idempotency and fail-closed validation are required where duplicate side effects would be unsafe.

## Public security invariants

- reasoning is not permission
- orchestration is not permission
- memory/state is not permission
- tool availability is not permission
- missing authorization blocks execution
- wrong deployment/license binding blocks execution
- customer-controlled systems remain behind explicit capability boundaries
- verified results, not unsupported claims, drive trustworthy continuation
- evidence is part of the execution contract, not optional marketing telemetry

This document is not a complete penetration-test report or disclosure of private defensive mechanisms.
