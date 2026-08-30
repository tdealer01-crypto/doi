# DSG Spacetime — High-Level Threat Model

This document describes public security objectives only. It intentionally omits implementation-level anti-bypass logic, private schemas, solver constraints, secret identifiers, and defensive assumptions that would weaken the proprietary security boundary.

## Assets to protect

- customer-controlled systems and credentials
- deployment identity and entitlement scope
- approved Node/Route capability boundaries
- execution authorization decisions
- durable evidence and proof records
- seller-controlled commercial trust root

## Threat classes

### Untrusted AI proposal

An AI-generated plan may request capabilities beyond the intended scope. The architecture therefore treats composition as a proposal rather than authorization.

### Unauthorized Route use

An actor may attempt to execute a Route that is not approved, licensed, or valid for the deployment context. The intended behavior is fail-closed blocking.

### Entitlement tampering or substitution

Commercial authorization material may be modified, replaced, or self-issued by an unauthorized party. The runtime is designed to trust seller-controlled signing authority and reject invalid deployment/signature scope.

### Credential overreach

An agent may attempt to obtain unrestricted provider credentials or bypass the approved adapter/capability boundary. The architecture avoids direct unbounded model-to-provider credential use.

### Evidence tampering

A party may attempt to modify execution history after the fact. DSG Spacetime is designed to produce tamper-evident evidence suitable for later verification within the tested scope.

### Replay or duplicate side effects

Commerce and governed execution paths may be retried or replayed. Idempotency and fail-closed validation are required where duplicate side effects would be unsafe.

## Public security invariants

- proposal is not permission
- missing authorization blocks execution
- wrong deployment/license binding blocks execution
- customer-controlled systems remain behind explicit capability boundaries
- evidence is part of the execution contract, not optional marketing telemetry

This document is not a complete penetration-test report or disclosure of private defensive mechanisms.
