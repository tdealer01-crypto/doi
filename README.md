# DSG Spacetime — Public Publication Surface

This repository is the public citation and archival surface for **DSG Spacetime**.

> **Let AI build the system. Not just the code.**

DSG Spacetime is customer-hosted governance infrastructure for AI agents. It provides a Node-to-Node (N2N) model in which agents can discover approved capabilities, compose systems, execute within bounded authority, and produce verifiable evidence without requiring a central DSG SaaS control plane.

## Publication boundary

This repository intentionally contains **public-safe material only**. It does **not** contain the proprietary DSG Spacetime production implementation, private algorithms, solver internals, policy/security internals, private tests, secrets, credentials, customer data, or sensitive deployment details.

The production runtime remains in a separate private repository and is not mirrored here.

## Public architecture

DSG Spacetime can be understood as six public concepts:

```text
DSG Spacetime
├── Nodes
├── Routes
├── Governance
├── Execution
├── Evidence
└── Proof
```

- **Node** — an approved capability boundary, such as a source-control service, cloud platform, database, AI model, enterprise system, or internal API.
- **Route** — an authorized capability path between Nodes.
- **Governance** — identity, entitlement, policy, approval, and evidence requirements that bound execution.
- **Execution** — customer-hosted action through approved adapters/capabilities.
- **Evidence** — durable records of what actually executed.
- **Proof** — verification material derived from execution evidence.

The design goal is **maximum autonomy inside provable boundaries**.

## Public release version

The first public archival release is **DSG Spacetime 1.0.0**, GitHub tag **`v1.0.0`**.

The version identifies the sanitized public publication/citation package. It is not a claim that the private production runtime has been relicensed or published.

## DOI

**VERIFIED — Zenodo publication completed.**

- Version 1.0.0 DOI: **10.5281/zenodo.22172533**
- Concept DOI (all versions): **10.5281/zenodo.22172532**

Use the version DOI when citing this exact archived release. Use the concept DOI when you want a citation that follows the DSG Spacetime record across future Zenodo versions.

## License

Unless a file states otherwise, material actually published in this repository is licensed under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**. See `LICENSE.md`.

This license applies only to material contained in this public repository. It does **not** license the private DSG Spacetime production implementation, DSG Fabric internals, production runtime binaries, undisclosed algorithms, private schemas, private tests, anti-bypass mechanisms, customer data, credentials, or other proprietary DSG material outside this repository.

## Public material in this repository

- architecture-level documentation
- citation and Zenodo metadata
- high-level security/threat-model statements
- redacted verification/evidence summaries
- compliance-support mappings
- publication guard CI

No production source is intentionally included.

## Current publication state

**VERIFIED — public v1.0.0 archival release is published on Zenodo and DOI identifiers are recorded.**
