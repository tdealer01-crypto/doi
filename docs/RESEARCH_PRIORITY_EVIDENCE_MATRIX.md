# DSG Research Priority & Evidence Matrix

**Status:** DRAFT — evidence inventory, not a patentability opinion or a claim of first inventorship.  
**Prepared:** 2026-10-30  
**Scope:** Public-safe research provenance. No private production source, solver internals, credentials, or customer data.

## Interpretation rules

- **REPOSITORY-VERIFIED:** statement is supported by the cited public repository file or commit; does not independently verify Zenodo metadata.
- **OWNER-SUPPLIED:** date/identifier appears in owner-supplied provenance preserved in this repository; direct provider verification pending.
- **NOT VERIFIED:** missing independently checked publication metadata, exact source revision, independent test, or replay artifact.
- A DOI, repository commit, and provider timestamp are distinct evidence types. An uploaded or privately timestamped artifact is **not automatically** a public disclosure.
- Prior publication does not establish first inventorship, patent ownership, freedom to operate, novelty, or non-obviousness. Legal analysis requires jurisdiction-specific professional review.
- A successful governance decision is not equivalent to successful provider execution. Do not label E2E VERIFIED without independent execution observation and replay evidence.

## Publication and claim matrix

| DOI identifier / record | Publication date | GitHub commit / provenance | Core claim or architecture component | Reproducible test / benchmark | Status and limitations |
| --- | --- | --- | --- | --- | --- |
| `10.5281/zenodo.18212854` — Universal Deterministic Gate | 2026-01-11 (owner-supplied upload date) | [Related Publications](RELATED_PUBLICATIONS.md); exact publication-time source commit **NOT VERIFIED** | Deterministic gate for state-transition control | Public independent replay artifact **NOT VERIFIED** | **OWNER-SUPPLIED**; verify Zenodo metadata and publicly disclosed contents before asserting public prior-art date. |
| Zenodo record `18225586` — Formal Verification of Deterministic Safety Gate | 2026-01-12 (owner-supplied upload date) | [Related Publications](RELATED_PUBLICATIONS.md); exact publication-time source commit **NOT VERIFIED** | Formal verification, SMT/Z3 and safety invariants (as described in owner-supplied listing) | Formal proof artifact and independent reproduction **NOT VERIFIED** | **OWNER-SUPPLIED**; DOI string not established in the existing repository evidence. Do not infer DOI from record ID. |
| UDG v159 dataset — identifier relationship unresolved | 2026-01-14 (owner-supplied upload date) | [Related Publications](RELATED_PUBLICATIONS.md); exact publication-time source commit **NOT VERIFIED** | Deterministic governance, SMT/Z3, integrity anchoring (owner-supplied description) | Independent proof and replay **NOT VERIFIED** | **AMBIGUOUS**: supplied DOI repeats `10.5281/zenodo.18212854`; do not claim unique DOI. |
| `10.5281/zenodo.22172533` — DSG Spacetime v1.0.0 | Exact Zenodo publication timestamp **NOT VERIFIED** in this audit | [README](../README.md); exact archival commit **NOT VERIFIED** | Public-safe DSG Spacetime architecture and evidence boundary | Release archive and independent execution replay **NOT VERIFIED** in this audit | **REPOSITORY-VERIFIED identifier**; README states archived and verified, but Zenodo metadata not independently rechecked here. |
| `10.5281/zenodo.22755320` — DSG Spacetime v1.1.0 | Exact Zenodo publication timestamp **NOT VERIFIED** in this audit | [README](../README.md), [CITATION.cff](../CITATION.cff), [Architecture](ARCHITECTURE.md); exact archival commit **NOT VERIFIED** | AI reasoning separated from execution authority; Automation Spacetime, Core Spin, Governance Spacetime, governed routes, evidence and verification | Public independent DGAB execution and replay artifact **NOT VERIFIED** | **REPOSITORY-VERIFIED identifier and documented architecture**; README records Zenodo release, but direct provider metadata and independently replayable E2E proof remain pending. |
| `10.5281/zenodo.22172532` — DSG Spacetime concept DOI | Exact Zenodo publication timestamp **NOT VERIFIED** | [README](../README.md) | Concept-level identifier across versions | Not an execution benchmark | **REPOSITORY-VERIFIED identifier**; concept DOI must not be conflated with version DOI. |

## Historical provenance — distinct from public publication

- [Harmonic Mean provider evidence](HARMONIC_MEAN_PROVIDER_EVIDENCE_2025.md) reports provider-timestamped private artifacts in 2025. These timestamps do **not** independently prove public disclosure.
- [THANAWAT / KAI lineage](THANAWAT_KAI_LINEAGE_EVIDENCE_2025.md), [CCVS / UDG snapshots](CCVS_UDG_SNAPSHOT_EVIDENCE_2026.md), and [V146/V159 workflow lineage](V146_V159_WORKFLOW_LINEAGE_EVIDENCE.md) document additional evidence with explicit prototype and simulation exclusions.
- [Provider revision KAI chronology](RELATED_PUBLICATIONS.md) is relevant to development history, not an automatic novelty or priority determination.

## Architecture-to-evidence map

| Public architecture claim | Source | Verification requirement | Current matrix status |
| --- | --- | --- | --- |
| Proposal is not execution permission | [Architecture](ARCHITECTURE.md) | Bind proposal to principal, route, exact action and authorization decision; negative test for bypass | Design documented; independent public test **NOT VERIFIED** |
| Approval and policy are exact-action bounded | [Architecture](ARCHITECTURE.md) | Test approved, missing, expired and changed-scope permits | Design documented; independent public test **NOT VERIFIED** |
| Authorized execution uses adapters | [Architecture](ARCHITECTURE.md) | Match plan hash, provider receipt, observed side effect and result | Design documented; independent public E2E **NOT VERIFIED** |
| Evidence informs stateful continuation | [Architecture](ARCHITECTURE.md) | Signed/hashed evidence chain, verifier decision, replay consistency and tamper-negative cases | Design documented; independent public replay **NOT VERIFIED** |
| Fail-closed behavior | [Architecture](ARCHITECTURE.md) | Deny when required authorization/evidence is absent without reporting completion | Design documented; independent public failure-path test **NOT VERIFIED** |

## DGAB reproducibility requirements

A future public-safe DGAB artifact should record: test case ID, specification version, source commit, deployed image digest, runtime/provider identity (redacted), UTC timestamp, plan hash, route, decision and reason, approval scope, provider receipt hash, independent observer result, evidence-chain verification, replay result, and a clear **PASS / FAILED / BLOCKED / NOT VERIFIED** verdict.

**Release claim rule:** A plan binding PASS or a status heartbeat alone must never be promoted to `E2E VERIFIED`. Publish redacted receipts and verifier outputs only after confirming no private operational details are disclosed.

## Next verification tasks

1. Query Zenodo record metadata directly for each DOI/record; capture `created`, `published`, `modified`, version relations, authors, file checksums, and stable source URLs.
2. Match the exact publicly disclosed content to GitHub release tags and commit SHAs at each date; avoid backdating current files.
3. Compare narrowly scoped claims against independently dated earlier literature, distinguishing known components from any specific integrated mechanism.
4. Publish reproducible, sanitized DGAB fixtures and independently checked replay receipts. Record failures and missing evidence explicitly.
5. Obtain qualified IP review before legal priority, novelty, patentability or ownership assertions.

**Public/private boundary:** This matrix is documentation only. It does not expose or relicense the private production implementation.
