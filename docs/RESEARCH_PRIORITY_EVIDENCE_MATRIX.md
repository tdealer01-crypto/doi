# DSG Research Priority & Evidence Matrix

**Status:** PROVIDER-VERIFIED Zenodo metadata + scoped empirical snapshot; not a patentability opinion or a claim of first inventorship.  
**Prepared:** 2026-10-30  
**Scope:** Public-safe research provenance. No private production source, solver internals, credentials, or customer data.

## Interpretation rules

- **REPOSITORY-VERIFIED:** statement is supported by a cited public repository file or commit.
- **PROVIDER-VERIFIED:** DOI identity, metadata date, or archived checksum independently read from the publicly accessible Zenodo record API on 2026-10-30.
- **OWNER-SUPPLIED:** date/identifier appears in owner-supplied provenance preserved in this repository; direct provider verification pending.
- **NOT VERIFIED:** missing independently checked publication metadata, exact source revision, independent test, or replay artifact.
- A DOI, repository commit, and provider timestamp are distinct evidence types. An uploaded or privately timestamped artifact is **not automatically** a public disclosure.
- Prior publication does not establish first inventorship, patent ownership, freedom to operate, novelty, or non-obviousness. Legal analysis requires jurisdiction-specific professional review.
- A successful governance decision is not equivalent to successful provider execution. Do not label E2E VERIFIED without independent execution observation and replay evidence.

## Publication and claim matrix

| DOI identifier / record | Publication date | GitHub commit / provenance | Core claim or architecture component | Reproducible test / benchmark | Status and limitations |
| --- | --- | --- | --- | --- | --- |
| [10.5281/zenodo.18212854](https://doi.org/10.5281/zenodo.18212854) — Universal Deterministic Gate | **2026-01-11 Zenodo publication date VERIFIED** ([provider API](https://zenodo.org/api/records/18212854)) | [Related Publications](RELATED_PUBLICATIONS.md); exact publication-time source commit **NOT VERIFIED** | Deterministic gate for state-transition control | Public PDF MD5 `9b5d3fa54aa1605ed1758704753e8235`; full independent replay **NOT VERIFIED** | **PROVIDER-VERIFIED metadata/archive**; publication does not establish legal inventorship or mathematical correctness. |
| [10.5281/zenodo.18225586](https://doi.org/10.5281/zenodo.18225586) — Formal Verification of Deterministic Safety Gate | **2026-01-12 Zenodo publication date VERIFIED** ([provider API](https://zenodo.org/api/records/18225586)) | [Related Publications](RELATED_PUBLICATIONS.md); exact publication-time source commit **NOT VERIFIED** | Historical SMT/Z3 publication; claims require a separate soundness review | Archived `dsg_full_proof.smt2` MD5 `a62f7e0b1561fd2cdb355b16d157bf73`; v1 proof formulation caveat in [evidence snapshot](DSG_AGENT_V0_PUBLIC_EVIDENCE_20261030.md) | **PROVIDER-VERIFIED metadata/archive**; proof soundness or live Runtime conformance not established by DOI. |
| UDG v159 dataset — identifier relationship unresolved | 2026-01-14 (owner-supplied upload date) | [Related Publications](RELATED_PUBLICATIONS.md); exact publication-time source commit **NOT VERIFIED** | Deterministic governance, SMT/Z3, integrity anchoring (owner-supplied description) | Independent proof and replay **NOT VERIFIED** | **AMBIGUOUS**: supplied DOI repeats `10.5281/zenodo.18212854`; do not claim unique DOI. |
| [10.5281/zenodo.22172533](https://doi.org/10.5281/zenodo.22172533) — DSG Spacetime v1.0.0 | **2026-08-30 Zenodo publication date VERIFIED** ([provider API](https://zenodo.org/api/records/22172533)) | [README](../README.md); exact archival commit **NOT VERIFIED** | Public-safe DSG Spacetime architecture and evidence boundary | Archived ZIP MD5 `348b023d4af727e1bae0fb2d46ef799f`; independent execution replay **NOT VERIFIED** | **PROVIDER-VERIFIED metadata/archive**; not live DSG execution proof. |
| [10.5281/zenodo.22755320](https://doi.org/10.5281/zenodo.22755320) — DSG Spacetime v1.1.0 | **2026-09-14 Zenodo publication date VERIFIED** ([provider API](https://zenodo.org/api/records/22755320)) | [README](../README.md), [CITATION.cff](../CITATION.cff), [Architecture](ARCHITECTURE.md); exact archival commit **NOT VERIFIED** | AI reasoning separate from execution authority | Archived ZIP MD5 `1f3b879bd54e8ded7c1411d72deb1522`; independent DGAB replay **NOT VERIFIED** | **PROVIDER-VERIFIED metadata/archive**; public benchmark E2E still missing. |
| [10.5281/zenodo.22172532](https://doi.org/10.5281/zenodo.22172532) — DSG Spacetime concept DOI | Parent/concept identifier confirmed via Zenodo v1.0/v1.1 record relations; no separate version publication date | [v1.0.0 metadata](https://zenodo.org/api/records/22172533), [v1.1.0 metadata](https://zenodo.org/api/records/22755320) | Concept-level identifier across versions | Not an execution benchmark | **PROVIDER-VERIFIED DOI relationship**; not a third published version. |

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

## DSG-Agent-v0 empirical evidence (2026-10-30)

See [Public DSG-Agent-v0 Evidence Snapshot](DSG_AGENT_V0_PUBLIC_EVIDENCE_20261030.md). Historical Qwen3-8B training evaluation: 30 held-out worlds / 181 cases, action accuracy 0.9005524861878453, valid candidate rate 1.0, teacher-path exactness 0.5666666666666667, adapter SHA-256 `44a9f90158a0f702acba25bb210dd0d7e1029335567f4e9b2e1ac95549b1aee2`. This is **HISTORICAL-VERIFIED**, not public independently replayed or current AWS adapter proof.

Authenticated DSG control-plane test on 2026-10-30: catalog **PASS** (19 configured nodes, 38 routes), evidence chain **PASS** (523 records, valid=true), read-only plan **BOUND**, Brain `action.plan` **BLOCKED** (endpoint configuration), Cinema status **BLOCKED** (provider action refused). Both blocked attempts returned no provider receipt/evidence; current Neural → Gate → Execute → Evidence and independent replay remain **NOT VERIFIED**. Publication omits private operational identifiers and raw logs.

## DGAB reproducibility requirements

A future public-safe DGAB artifact should record: test case ID, specification version, source commit, deployed image digest, runtime/provider identity (redacted), UTC timestamp, plan hash, route, decision and reason, approval scope, provider receipt hash, independent observer result, evidence-chain verification, replay result, and a clear **PASS / FAILED / BLOCKED / NOT VERIFIED** verdict.

**Release claim rule:** A plan binding PASS or a status heartbeat alone must never be promoted to `E2E VERIFIED`. Publish redacted receipts and verifier outputs only after confirming no private operational details are disclosed.

## Next verification tasks

1. **Completed for identified Zenodo records on 2026-10-30:** direct API verification of DOI, publication date, version relation, creator and archived checksum. Independent re-download and hash recomputation remains a separate follow-up.
2. Match the exact publicly disclosed content to GitHub release tags and commit SHAs at each date; avoid backdating current files.
3. Compare narrowly scoped claims against independently dated earlier literature, distinguishing known components from any specific integrated mechanism.
4. **Partial:** publish the dated sanitized evidence snapshot and blocked live cases; independently replayable DGAB fixtures and signed receipts remain pending.
5. Obtain qualified IP review before legal priority, novelty, patentability or ownership assertions.

**Public/private boundary:** This matrix is documentation only. It does not expose or relicense the private production implementation.
