# Security

## Scope of this public repository

This repository is a publication and citation surface. It does not contain the DSG Spacetime production implementation or private security-control internals.

Do not submit production credentials, customer data, private keys, exploit details, or confidential DSG implementation material to public issues or pull requests.

## Public security model

DSG Spacetime is designed around fail-closed execution boundaries:

- AI proposals are not self-authorizing.
- Execution is bound to approved capabilities and deployment context.
- Commercial execution is constrained by signed entitlements.
- Missing or invalid authorization conditions block execution.
- Execution produces evidence intended for verification.

These are architecture-level statements, not disclosure of the private implementation.

## Reporting

For security-sensitive reports, use a private DSG contact channel rather than a public issue. Do not publish exploitable details before coordinated review.

Public documentation in this repository must remain implementation-safe and must not expose anti-bypass logic, private policy rules, secret identifiers, solver internals, or sensitive deployment topology.
