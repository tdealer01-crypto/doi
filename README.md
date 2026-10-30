# DSG Spacetime — Public Publication Surface

This repository is the public citation and archival surface for **DSG Spacetime**.

> **Let AI build the system. Not just the code.**

DSG Spacetime is a customer-hosted governed AI-agent system. It separates AI reasoning and workflow composition from execution authority, so agents can operate with high autonomy while exact actions remain bounded by explicit capabilities, approvals, policy and verifiable evidence.

## Publication boundary

This repository intentionally contains **public-safe material only**. It does **not** contain the proprietary production implementation, private algorithms, solver internals, policy/security internals, private tests, secrets, credentials, customer data, or sensitive deployment details.

The production runtime remains in a separate private repository and is not mirrored here.

## DSG AI Agent System

The v1.1.0 publication describes the **AI agent system as a whole**, not any single tool or browser capability.

```text
Goal / User Intent
        |
        v
AI Agent / Reasoning
        |
        v
Automation Spacetime
(workflow / handoff / retry / resume / checkpoint)
        |
        v
Core Spin
(stateful control loop)
        |
        v
Governance Spacetime
(exact-action authorization)
        |
        v
Nodes + Governed Routes
        |
        v
Execution Adapters / Customer Infrastructure
        |
        v
Evidence -> Verification -> Proof
        |
        +------ verified result/state ------> next Core Spin round
```

- **AI Agent / Reasoning** — proposes plans and next actions; proposal is not permission.
- **Automation Spacetime** — describes how work progresses across steps, agents, parallel work, handoffs, retry/resume and checkpoints at the orchestration level.
- **Governance Spacetime** — determines whether an exact requested action is authorized for the current identity, capability, Route, approval and policy context.
- **Core Spin** — the stateful control loop between reasoning, automation and governance. It carries job/session progress and verified results into the next round without gaining authority to bypass governance.
- **Node** — an approved capability boundary such as source control, cloud infrastructure, databases, models, browsers, payment systems or enterprise services.
- **Route** — a governed capability path between Nodes.
- **Execution** — an authorized action carried out through approved customer-owned/provider adapters.
- **Evidence / Proof** — durable records and verification material showing what actually executed.

The operating principle is **maximum autonomy inside provable boundaries**.

See [`docs/AI_AGENT_SYSTEM_OVERVIEW.md`](docs/AI_AGENT_SYSTEM_OVERVIEW.md) and [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## AI-first lifecycle

```text
discover -> compose -> bind -> authorize -> execute -> evidence -> verify -> continue/complete
```

The AI can reason, plan and select the next step. Automation can coordinate multi-step work. Neither layer self-authorizes side effects. Governance remains the execution boundary, while Core Spin uses verified results to continue, pause for approval, block, or complete the goal.

Individual capabilities — browser operation, source control, cloud, database, model, payment or enterprise integrations — are Nodes/tools inside this architecture. They are **not** the architecture itself.

## Public release version

The prepared public package is **DSG Spacetime 1.2.0 — Production Evidence and Reproduction Protocol** (2026-10-30).

**Archival state: ZENODO_PENDING.** A new DOI is not claimed until Zenodo ingests the release and its public API is checked. See [publication state](PUBLICATION_STATUS.md) and [release notes](docs/RELEASE_V1_2_0.md).

Versioning identifies sanitized publication/citation packages. It does not publish or relicense the private production runtime. Earlier version archives remain immutable.

## DOI

**Historical status: VERIFIED — Zenodo publication for v1.1.0 completed.**

- v1.2.0 DOI: pending verified ingestion.
- Version 1.1.0 DOI: **10.5281/zenodo.22755320**.
- Previous v1.0.0 DOI: **10.5281/zenodo.22172533**.
- Concept DOI (all versions): **10.5281/zenodo.22172532**.

The v1.1.0 DOI cites that earlier archive only. Use the concept DOI for the publication series; use the new version DOI only after it is verified and recorded.

## Research and public empirical evidence (2026-10-30)

- [Research Priority & Evidence Matrix](docs/RESEARCH_PRIORITY_EVIDENCE_MATRIX.md): Zenodo DOI provenance, publication dates and proof limits.
- [DSG-Agent-v0 Public Evidence Snapshot](docs/DSG_AGENT_V0_PUBLIC_EVIDENCE_20261030.md): historical Qwen3-8B evaluation, authenticated control-plane tests, observed BLOCKED cases and missing E2E acceptance.
- [Machine-readable Evidence Manifest](docs/evidence/DSG_AGENT_V0_PUBLIC_EVIDENCE_20261030.json): dated result fields and direct public Zenodo API references.
- [NVIDIA Production Empirical Evidence and Ed25519 Signature Scope](docs/DSG_NVIDIA_PRODUCTION_PUBLIC_PROOF_20261030.md): post-promotion exact-digest read-only Workroom E2E, Memory evidence, signature-verification status, reproducibility and exclusions.
- [Public Reproduction Protocol](docs/PUBLIC_REPRODUCTION_PROTOCOL_20261030.md): runnable Zenodo API metadata verification; authorized Ed25519 verification and exact-image read-only E2E acceptance steps.

**Scope:** This is a sanitized, time-bounded evidence inventory. The earlier pre-promotion audit reported blocked Brain planning, while a later exact-image NVIDIA Nemotron API read-only Workroom E2E passed. This does **not** establish Kaggle Qwen3-30B GPU acceptance, arbitrary mutations, automatic recovery, public third-party E2E replay or a new Zenodo DOI.

## Related and prior publications

Earlier owner-supplied Zenodo publications that may form part of the research lineage are recorded separately in [`docs/RELATED_PUBLICATIONS.md`](docs/RELATED_PUBLICATIONS.md).

Those records are not automatically treated as DSG Spacetime releases. Ambiguous or not-yet-directly-verified DOI relationships are explicitly marked as such.

## License

Unless a file states otherwise, material actually published in this repository is licensed under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**. See `LICENSE.md`.

This license applies only to material contained in this public repository. It does **not** license the private DSG Spacetime production implementation, DSG Fabric internals, production runtime binaries, undisclosed algorithms, private schemas, private tests, anti-bypass mechanisms, customer data, credentials, or other proprietary DSG material outside this repository.

## Public material in this repository

- AI-agent system architecture at a conceptual level
- citation and Zenodo metadata
- high-level security/threat-model statements
- redacted verification/evidence summaries
- compliance-support mappings
- related/prior-publication lineage notes
- publication guard CI

No production source is intentionally included.

## Current publication state

**v1.2.0: ZENODO_PENDING.** The earlier v1.1.0 and v1.0.0 releases remain verified and archived.
