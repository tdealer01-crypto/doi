Source: https://raw.githubusercontent.com/tdealer01-crypto/doi/v1.2.0/docs/DSG_NVIDIA_PRODUCTION_PUBLIC_PROOF_20261030.md

# DSG ONE — NVIDIA Production Empirical Evidence and Signature Boundaries

**Evidence date:** 2026-10-30 UTC  
**Classification:** PUBLIC-SAFE DERIVED SUMMARY — not a copy of private operational logs or attestations  
**Overall claim:** VERIFIED for the **specified read-only NVIDIA Workroom → governed browser read → durable Memory** slice, based on private primary records and an independent serving-control-plane read; **not** independent public E2E replay or proof of arbitrary autonomous tasks.

## Provenance: exact version, not a floating "latest"

| Evidence component | Pinned identifier | Verified scope |
| --- | --- | --- |
| Source built into serving image | `ea73ac8d9aeada37c2cfeec158ff0dcda573d589` | Exact-source CI/build lineage |
| Production OCI image | `sha256:94115f03476e93a8dbce43cbdcf37951c4a148d3c998ae87683c7185cd7a8f10` | Immutable **Spacetime** container image observed healthy |
| Evidence/checkpoint merge | `d8fe636f3c1c3fd8ddec4ed699eeff49c6952d06` | Later documentation/test merge (PR #871); **not** an image rebuilt from this head |
| Source CI | GitHub Actions run `41006714978` | SUCCESS for source commit above |
| Container build | GitHub Actions run `41006714979` | SUCCESS for same source; SHA-256 digest above |
| Protected owner release | GitHub Actions run `41010617597` | SUCCESS; production release attestation gate passed on specified source and image |
| Post-merge documentation CI | GitHub Actions run `41015153555` | SUCCESS; **3,108 passed, 2 skipped** Python tests; 85 frontend tests separately observed |
| Signed CI ledger | Same post-merge run; issued 2026-10-30T06:40:56Z | Ed25519 signed exact post-merge CI payload; signature cryptographically validated during this audit |
| Live read-only control-plane verification | 2026-10-30, post-promotion | 20 configured Nodes / 39 Routes; evidence chain `valid=true`, `records=532` |

The production repository, GitHub job logs and raw release receipts are private. Their URLs may be accessible to authorized reviewers but are **not public third-party evidence**. This page preserves independently checkable fingerprints and an explicit source/privacy boundary rather than copying raw protected material.

## What was observed in the scoped production acceptance

The pinned source was built and scanned, the same image digest was read back from the serving Production container, and a protected owner release completed. The serving control plane returned the configured NVIDIA Brain route under `action.plan`; provider identity for the bounded test was `nvidia` and model `nvidia/nemotron-3.5-lightning-30b-a3b`. The canonical read-only proposal yielded a real provider-issued inference reference and a locally independently recomputed result hash matching the stored evidence.

A real **read-only browser extraction** goal completed under the Workroom path. Memory start/end receipts were persisted and matched an independent storage readback; associated ledger entries fall within indices 525–531, with the evidence chain reaching **532 valid records**. The independent final readback reported **healthy** container state, preserved peer services, 20 Nodes, 39 Routes and expected image digest. Public health 200 and anonymous MCP 401 were reported by the primary readback.

**Bounded claims only:** this is evidence of one live safe browser-read workflow with a proposed tool and verified Memory persistence. It is **not** proof of unrestricted desktop mutations, Google/MFA sign-in, autonomous workflow recovery, every route, universal fail-closed correctness or model truthfulness. The model was NVIDIA Nemotron over an API, **not** Qwen3-30B on Kaggle. The prior Qwen3-8B trained-adapter benchmark remains a separate historical result.

## Cryptographic evidence — independently checked, with disclosure limits

1. **Image integrity:** production readback matched the immutable OCI `sha256` digest. A matching digest links observed bytes to a content address, but does not itself authenticate a release signer.
2. **GitHub merge authenticity:** GitHub's commit API returned `verification.verified=true` for PR #871's signed merge commit. This attests to the commit's cryptographic verification by GitHub, not the runtime outcome.
3. **Ed25519 CI attestation:** private post-merge ledger document has an exact CI payload and `signature_b64`. In this audit the signature was **independently verified** against the corresponding 32-byte production change-control **public verification key**, using the canonical UTF-8 JSON serialization (`sort_keys=True`, `separators=(',', ':')`, `ensure_ascii=False`). Outcome: **SIGNATURE_VALID**. Its payload binds PR #871, merged commit `d8fe636f3c1c3fd8ddec4ed699eeff49c6952d06`, and CI run `41015153555`. The SHA-256 fingerprint of the Ed25519 **public key bytes** was `3a5373195002566c2d1b4626619fd3b7ae98c2a4e9d47d2f0d3174ee084d8c19`.
4. **Signed release gate:** the protected release log reports `Production release attestation: PASS` and binds source `ea73ac8d9aeada37c2cfeec158ff0dcda573d589` to the same image digest. This is a primary-log verification, not independent public inspection of the release signature.
5. **Evidence-chain integrity:** serving `verify_evidence` returned `valid=true, records=532`. It checks the runtime's local tamper-evident chain and **does not** independently prove each physical side effect or a separately witnessed provider result.

**Public signature limitation:** the complete Ed25519-signed payload, trusted public key and raw hosted CI ledger have **not** been exported onto this public repository because the original private operational record requires explicit disclosure review. A changed or redacted signed payload cannot preserve its old signature. Thus the **cryptographic signature was independently verified by the auditor but is not yet third-party publicly replayable**. No substitute signature or fabricated public attestation is asserted.

## Reproduction protocol and status

The following are separated by access level, so a reader can reproduce what is actually available:

| Check | Procedure | Publicly reproducible now? |
| --- | --- | --- |
| Zenodo DOI/archive provenance | Use the provider API URLs in [research matrix](https://raw.githubusercontent.com/tdealer01-crypto/doi/v1.2.0/docs/RESEARCH_PRIORITY_EVIDENCE_MATRIX.md), compare publication dates, concept/version relations, file checksums | **YES** (metadata; re-download optional) |
| Public evidence/manifest consistency | Inspect pinned hashes and outcome fields in [machine-readable summary](https://raw.githubusercontent.com/tdealer01-crypto/doi/v1.2.0/docs/evidence/DSG_AGENT_V0_PUBLIC_EVIDENCE_20261030.json) | **YES** for reading/comparing public assertions; **NO** for independent model execution |
| Source + build + signed release | With authorized private GitHub and production access, inspect Runs `41006714978`, `41006714979`, `41010617597` and serving image readback | **ACCESS-RESTRICTED** |
| Post-merge signed CI attestation | With authorized access to the original CI ledger and pinned verification key, verify Ed25519 over canonically serialized `payload` and compare PR/commit/run IDs | **ACCESS-RESTRICTED** |
| Exact NVIDIA governed execution + Memory | On authorized Production tenant, run a new read-only `action.plan` and governed browser extraction, capture independent observer + Memory readback + evidence verification | **NOT YET REPRODUCED BY PUBLIC THIRD PARTY** |
| Unauthorized mutation, tamper-negative and replay-negative | Run controlled fixture against a disposable tenant with full independent observer and signed negative receipt | **NOT VERIFIED FOR THIS RELEASE** |
| Kaggle 30B GPU/32K context training/evaluation | Separate held-out evaluation and live GPU inference | **NOT VERIFIED** |

An authorized verifier should use a **new request key** and a **safe read-only test** to avoid replaying production changes. Record exact source and serving-image digests, model/provider identity, plan and decision hashes, provider receipt hash, observer result, persisted Memory hash, signed evidence verdict, and UTC timestamp. Require agreement across independent provider observation and audit logs. A heartbeat, plan-binding success, or internally reported `PASS` is insufficient for independent E2E acceptance.

## Known constraints and negative outcomes

- **Capacity:** root disk measured at **1,828,524,032 available bytes** following image activation. Old images were preserved pending rollback-copy/retention review; no destructive pruning was performed.
- **Recovery:** one UI job initially stalled and was canceled without provider execution. A bounded **manual same-image UI restart** preserved its identity, image and peer containers; a fresh read-only goal then passed. This is **not evidence of automatic worker reconnection/resume**.
- **Previous live attempt:** before the exact-source promotion, an earlier authenticated audit found `action.plan` blocked by Brain endpoint configuration. That outcome is preserved in the dated [prior snapshot](https://raw.githubusercontent.com/tdealer01-crypto/doi/v1.2.0/docs/DSG_AGENT_V0_PUBLIC_EVIDENCE_20261030.md); it is superseded for the specified promoted image, not erased.
- **Attestation disclosure:** no complete public detached-signature/replay bundle for protected Production yet, despite internally verified cryptographic CI evidence.

## Publication boundary

This document is a redacted research/evidence **supplement**, not a new Zenodo release, safety certification, independent peer review or new license grant. No private implementation, private host identifiers, signing secret, provider credential, confidential test code or raw private runtime ledger is included. A future truly public verifiable **signed** package requires a separately owner-approved, non-sensitive canonical payload signed by the authoritative release key (or another explicitly trusted public issuer) plus the matching public verification key and reproducible verifier inputs. It must be checked by an independent verifier before describing it as public-proof PASS.
