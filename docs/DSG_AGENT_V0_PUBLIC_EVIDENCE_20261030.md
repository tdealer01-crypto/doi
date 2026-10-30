# DSG-Agent-v0 — Public Evidence Snapshot (2026-10-30)

**Classification:** PUBLIC (sanitized outcome summary; no source code or private runtime artifacts)  
**Status:** PARTIAL — historical training evidence + current read-only verification, **not** current-release neural execution E2E proof.  
**Test date:** 2026-10-30 (UTC/ICT).  
**Research linkage:** [DSG Research Priority & Evidence Matrix](RESEARCH_PRIORITY_EVIDENCE_MATRIX.md).

## Interpretation

- **PROVIDER-VERIFIED**: metadata obtained directly from the publicly readable provider record.
- **HISTORICAL-VERIFIED**: private source/job evidence was inspected, but the original artifact or reproducible raw records are not published here.
- **LIVE-VERIFIED**: an authenticated request was issued to the serving DSG control plane during this audit; validity applies only to the returned result.
- **BLOCKED**: the attempted operation was not completed. BLOCK is **not** an execution receipt, side-effect proof, or a replay pass.
- **NOT VERIFIED**: requirements are unmet or no independent supporting artifact was obtained.

## A. Public Zenodo provenance (provider-verified 2026-10-30)

The following dates are Zenodo **metadata publication dates**, not assertions of patent priority, first inventorship, or verified model correctness.

| Record | Version DOI | Published (UTC calendar date) | Relationship / artifact |
| --- | --- | --- | --- |
| Universal Deterministic Gate | [10.5281/zenodo.18212854](https://doi.org/10.5281/zenodo.18212854) | 2026-01-11 | Concept DOI `10.5281/zenodo.18212853`; archived public PDF, MD5 `9b5d3fa54aa1605ed1758704753e8235` |
| Formal Verification of Deterministic Safety Gate | [10.5281/zenodo.18225586](https://doi.org/10.5281/zenodo.18225586) | 2026-01-12 | Concept DOI `10.5281/zenodo.18225585`; archived SMT-LIB artifact `dsg_full_proof.smt2`, MD5 `a62f7e0b1561fd2cdb355b16d157bf73` |
| DSG Spacetime v1.0.0 | [10.5281/zenodo.22172533](https://doi.org/10.5281/zenodo.22172533) | 2026-08-30 | Version under concept DOI `10.5281/zenodo.22172532`, archive MD5 `348b023d4af727e1bae0fb2d46ef799f` |
| DSG Spacetime v1.1.0 | [10.5281/zenodo.22755320](https://doi.org/10.5281/zenodo.22755320) | 2026-09-14 | Same concept DOI `10.5281/zenodo.22172532`, archive MD5 `1f3b879bd54e8ded7c1411d72deb1522` |

Direct provider records: [UDG API](https://zenodo.org/api/records/18212854), [Formal Verification API](https://zenodo.org/api/records/18225586), [v1.0.0 API](https://zenodo.org/api/records/22172533), [v1.1.0 API](https://zenodo.org/api/records/22755320). The concept identifier resolves to a version record; it is not a separate executable benchmark. UDG v159 remains an ambiguous identity until a distinct provider record and archived content are established.

**Formal-proof caveat:** The earlier published SMT-LIB file is an archival fact, **not** proof of all runtime safety claims. A later private proof-v2 audit identifies defects in the v1 theorem formulation. Proof-v2 covers an abstract four-state gate, not all provider behavior or model truthfulness. Public independent reproduction of the corrected proof and code-conformance checks is **NOT VERIFIED** in this snapshot.

## B. DSG-Agent-v0 Qwen3-8B historical training

**Result: HISTORICAL-VERIFIED — not independently reproducible from this publication alone.**

- Base model: `Qwen/Qwen3-8B`; bounded candidate selector, 4-bit QLoRA configuration.
- Held-out evaluation: **30 worlds / 181 examples**; teacher selection accuracy **0.9005524861878453**; valid-candidate rate **1.0**; all-steps teacher-exact world rate **0.5666666666666667** (17/30).
- Adapter content SHA-256: `44a9f90158a0f702acba25bb210dd0d7e1029335567f4e9b2e1ac95549b1aee2`.
- Historical training evidence inspection completed on 2026-09-09; historical inference deployment and governed route execution checks subsequently reported success in September 2026.
- These values were read from the original private GitHub Actions training-evidence verification log and cross-checked against the historical release/route evidence. Private logs and adapter binaries are not replicated to this public surface.
- `valid_candidate_rate=1` means a regex-extracted candidate ID was in the offered set on the evaluated examples. It does **not** establish valid JSON on every output, successful autonomous rollout on every world, or zero hallucination.
- `full_teacher_path_world_pass_rate` is teacher-path exactness, **not** an independently measured free-running mission completion percentage.
- Current AWS serving-image linkage to this exact adapter: **NOT VERIFIED** in this audit.

## C. DSG-Agent-v0 Qwen3-30B-A3B

**Result: NOT VERIFIED (current live GPU + model + governed E2E).**

A separate `Qwen/Qwen3-30B-A3B` Kaggle/T4×2 proposal Brain and a trained-adapter on-demand path are documented internally. Source configuration, a declared adapter identity, and catalog presence do not prove that the requested 30B weights are loaded and executing now. This audit did not obtain fresh GPU device logs, evaluated 30B benchmark outputs, successful authenticated `/plan` provider receipt, 32K-context real inference, signed post-model receipt, or complete governed Spacetime E2E.

## D. Live DSG control-plane verification (2026-10-30)

The following checks were performed against an authenticated serving DSG Spacetime connection. Sensitive account/identity data, internal plan hash, decision hash, provider URLs, and private endpoint configuration are intentionally omitted.

| Test | Observed response | Classification | Limit |
| --- | --- | --- | --- |
| Capability catalog read | Response `PASS`; **19 configured nodes / 38 configured routes**; Agent Brain proposal route advertised | **LIVE-VERIFIED** | Catalog presence is not provider readiness |
| Evidence chain verification, before requests | `valid=true`, `records=523` | **LIVE-VERIFIED** | Chain validation is not independent provider-side execution observation |
| Bounded read-only audit plan | `BOUND` and returned a plan hash | **LIVE-VERIFIED** | Plan binding is not action authorization or execution |
| Read-only Brain planning route | `BLOCK`; provider endpoint configuration rejected | **BLOCKED** | No Brain result; no execution receipt; no per-action evidence |
| Cinema status route | `BLOCK`; provider rejected the requested status action | **BLOCKED** | No provider result or per-action evidence |
| Evidence chain verification, after requests | `valid=true`, `records=523` | **LIVE-VERIFIED** | Does not establish that blocked attempts produced signed audit receipts |
| Device mutation without approval | Not attempted | **NOT VERIFIED** | No side-effect/non-bypass claim |
| Cross-provider replay / independent observer | Not performed | **NOT VERIFIED** | No independent E2E verification |

**Truth boundary:** Returning BLOCK is a concrete negative response but, with `result=null` and `evidence=null`, it does not prove the state of a remote provider. No live 30B Neural → Gate → Execute → Evidence success is claimed here.

## D2. Later Production NVIDIA acceptance — 2026-10-30

**Later verification supersedes the earlier blocked Brain status for the exact promoted image, but not for all other providers or images.** GitHub PR #871 confirms successful owner release and a read-only NVIDIA Nemotron Workroom/Memory/browser goal. This is a **distinct API-hosted model** from the unverified Kaggle/Qwen3-30B path and from the historical trained Qwen3-8B adapter. Pin image `sha256:94115f03476e93a8dbce43cbdcf37951c4a148d3c998ae87683c7185cd7a8f10`, source commit `ea73ac8d9aeada37c2cfeec158ff0dcda573d589` and evidence merge `d8fe636f3c1c3fd8ddec4ed699eeff49c6952d06`. The serving chain returned `valid=true` at **532** records and catalog of **20 Nodes / 39 Routes** on the fresh authenticated audit. An Ed25519 CI attestation for PR #871 was cryptographically verified during the audit, but its original protected payload is not public and external replay remains access-restricted.

See [NVIDIA Production Empirical Evidence and Signature Boundaries](DSG_NVIDIA_PRODUCTION_PUBLIC_PROOF_20261030.md). **Do not conflate** this scoped read-only Production slice with independent public E2E reproduction, Kaggle GPU 32K acceptance, or automatic worker recovery.

## E. Public reproducibility and next acceptance

| Target | Status | Evidence required for promotion |
| --- | --- | --- |
| DOI metadata and archived file checksums | **PROVIDER-VERIFIED** | Public API pages linked above; independent readers can check dates, relations, and MD5 values |
| Qwen3-8B evaluation metrics | **HISTORICAL-VERIFIED** | Public-safe fixture, evaluator, anonymized per-case results and reproducible adapter provenance |
| Formal proof v2 / implementation conformance | **NOT VERIFIED for public replay** | Publicly approved proof obligations, exact tooling version, test output, independent replay |
| Qwen3-30B-A3B GPU + evaluation + context | **NOT VERIFIED** | Fresh GPU load, model/adaptor hash, held-out metrics, authenticated live /plan and context-boundary inference |
| Current AWS Agent → Gate → Execute → Evidence | **NOT VERIFIED** | Exact serving image digest, redacted signed provider result, independent observation, evidence verification, failed-case handling |
| Negative authorization and tamper/replay | **NOT VERIFIED for public reproduction** | Explicit negative acceptance cases with authenticated audit proofs and no-side-effect evidence |
| External independent reproduction | **NOT VERIFIED** | Third-party execution results and matching public fixture/evidence hashes |

## Disclosures and integrity

- This publication is **a dated evidence snapshot**, not a certification, regulatory attestation, patentability analysis, or guarantee of perfect safety.
- Past successful deployments do not imply that an unrelated current AWS deployment has passed.
- Private production code, deployment topology, credentials, approval tokens, sensitive logs, raw customer data, internal test mechanics, and secret identifiers are excluded.
- The DOI/publication archive and this research evidence snapshot are distinct artifacts; this snapshot has **no newly minted Zenodo DOI**.
- No production settings or GPU workloads were changed to create this public document. Live attempts were limited to governance/catalog/evidence reads, read-only composition, and proposed low-risk routes.

**Audit result:** `PUBLIC_METADATA_VERIFIED; HISTORICAL_8B_VERIFIED; LIVE_CONTROL_PLANE_PARTIAL; NEURAL_E2E_NOT_VERIFIED`.
