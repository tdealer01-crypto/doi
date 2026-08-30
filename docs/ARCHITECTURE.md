# DSG Spacetime — Public Architecture Overview

## Product model

DSG Spacetime provides a governed environment in which AI agents can discover capabilities, compose systems, execute through customer-controlled infrastructure, and produce verifiable evidence.

The public architecture is intentionally described at a conceptual level:

```text
Intent / AI agent
       |
       v
   Discovery
       |
       v
   Composition
       |
       v
   Bound Plan
       |
       v
Governance / Entitlement / Approval
       |
       v
   Route Execution
       |
       v
 Evidence -> Verification / Proof
```

## Nodes

A Node represents an approved capability boundary. Examples include source-control systems, cloud services, databases, AI/model providers, enterprise applications, monitoring systems, and internal customer APIs.

A Node describes what an agent may discover or request; it does not by itself authorize execution.

## Routes

A Route represents an authorized capability path between Nodes. Route use is subject to the deployment context and governance requirements defined for the requested operation.

## AI composition

AI is expected to propose and compose systems dynamically. A proposal remains untrusted until it is bound to the required execution context. Composition does not grant permission by itself.

## Governance

Before execution, DSG Spacetime evaluates the required authorization boundary for the requested Route. Publicly described boundary inputs include identity/context, approved capability scope, commercial entitlement where applicable, required approval, policy requirements, and evidence availability.

The private implementation of those controls is intentionally not published in this repository.

## Execution

DSG Spacetime is designed for customer-hosted/BYOC operation. Existing provider and enterprise systems remain in their own infrastructure. DSG Spacetime is not required to become a central SaaS control plane.

Execution occurs through approved capability/adaptor boundaries rather than unrestricted model-to-API access.

## Evidence and proof

Execution produces durable evidence intended to support later verification. Public claims are limited to the scopes actually proven by execution or CI evidence; static code existence alone is not treated as proof of production behavior.

## Design objective

**Maximum autonomy inside provable boundaries.**

Agents do not need to trust one another merely because they collaborate. They operate inside a world where capability, authorization, execution, and evidence can be checked against explicit boundaries.
