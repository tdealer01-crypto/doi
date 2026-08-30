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

## DOI status

**PREPARED — DOI NOT YET MINTED.**

`CITATION.cff` and `.zenodo.json` are included for citation/archive preparation. A DOI will be recorded only after an approved Zenodo record is actually published and the DOI resolves.

## License status

Public license/terms have **not yet been selected**. Repository visibility alone does not grant rights to proprietary DSG production implementation. The final public terms will be added before the first archival release.

## Public material in this repository

- architecture-level documentation
- citation and Zenodo metadata
- high-level security/threat-model statements
- redacted verification/evidence summaries
- compliance-support mappings
- publication guard CI

No production source is intentionally included.

## Current publication state

**PREPARED — not yet a DOI-verified archival release.**

Before the first Zenodo publication, the release still requires explicit public terms/license, final creator metadata, a public semantic version, repository change-control review, and Zenodo record verification.
