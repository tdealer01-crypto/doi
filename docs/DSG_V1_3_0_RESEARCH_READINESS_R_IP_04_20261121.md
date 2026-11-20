# DSG Spacetime — v1.3.0 Research Release Readiness (R-IP-04)

**Observed:** 2026-11-21 Asia/Bangkok  
**Status:** **CANDIDATE / NOT RELEASED** — this is a public-safe research status update, **not** a new DOI, patent grant, third-party certification, production E2E proof or replacement for a frozen archive.

## Published publication record (unchanged)

| Artifact | Provider | Published date | Meaning |
| --- | --- | --- | --- |
| Universal Deterministic Gate | [Zenodo 18212854](https://zenodo.org/api/records/18212854) | 2026-01-11 | Prior related research, not a DSG Spacetime version |
| Formal Verification of DSG (historical v1) | [Zenodo 18225586](https://zenodo.org/api/records/18225586) | 2026-01-12 | Historical SMT/Z3 artifact with known proof-formulation defect; not universal safety proof |
| DSG Spacetime v1.0.0 | [Zenodo 22172533](https://zenodo.org/api/records/22172533) | 2026-08-30 | Published version |
| DSG Spacetime v1.1.0 | [Zenodo 22755320](https://zenodo.org/api/records/22755320) | 2026-09-14 | Published version |
| DSG Spacetime v1.2.0 | [Zenodo 23796173](https://zenodo.org/api/records/23796173) | 2026-10-30 | **Most recent verified immutable version archive** |

The [concept DOI 10.5281/zenodo.22172532](https://doi.org/10.5281/zenodo.22172532) refers to the DSG Spacetime **version series**; it is **not** a new individual version publication. The public `doi` repository revision inspected for this status was `3bdad38b35417b6c7d4b22170abdcb1f59657752`.

These dated provider facts are documented in the existing [publication status](../PUBLICATION_STATUS.md) and [research evidence matrix](RESEARCH_PRIORITY_EVIDENCE_MATRIX.md). This status page did not alter Zenodo provider metadata or independently re-download all historical archives.

## Formal proof scope vs. actual production

| Item | Status | What it means |
| --- | --- | --- |
| Published proof-v1 metadata and file identity | VERIFIED HISTORICAL RECORD | Original archived source remains unchanged; its original all-states safety theorem is inconsistent with the transition axioms |
| Corrected abstract four-state proof-v2 | **LOCAL Z3 RESULTS PASS** | On a pinned source snapshot, T1–T6 returned UNSAT for negated claims, W1/M1 returned SAT, reference decision parity returned 0 mismatches over 16 state pairs |
| Original test runner under declared Python `z3-solver` package | **NOT VERIFIED IN LATEST CI** | The original runner's selected functions were checked via a local compatibility adapter for installed Z3; the full script timed out under that adapter; no complete official CI receipt was obtained |
| Production implementation-conformance / independent provider E2E | **NOT VERIFIED** | An abstract SMT model is not a proof that a deployed agent executes safely and completes a real job |
| Signed Workroom Claim→Checkpoint→Resume + independent observer | **NOT VERIFIED** | No newly verified original anonymized signed receipt, trusted key anchor, provider readback and completed same-job replay bundle |
| v1.3.0 GitHub Release, Zenodo version DOI | **NOT PUBLISHED** | No fabricated DOI, GitHub tag, release URL or claim of provider ingestion |

## Narrow prior-art context (not an IP opinion)

Previously published work covers constituent ideas including formal SMT solving ([Z3, 2008](https://www.microsoft.com/en-us/research/publication/z3-an-efficient-smt-solver/)), policy enforcement ([Open Policy Agent](https://www.openpolicyagent.org/docs)), authorization ([Zanzibar, USENIX ATC 2019](https://www.usenix.org/conference/atc19/presentation/pang)), signed multi-step provenance ([in-toto, USENIX Security 2019](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias)), workflow checkpoint recovery ([LangGraph v0.2, 2024](https://www.langchain.com/blog/langgraph-v0-2)) and LLM-agent runtime safety rules ([AgentSpec, initial preprint 2025](https://arxiv.org/abs/2503.18666)).

These sources show meaningful **overlap of individual ideas**, but **do not** establish whether a specific fully defined integration by DSG is patentable, was invented first, infringes a patent, or has freedom to operate. Patent publication, application/priority and public disclosure dates are different; jurisdiction-specific review is needed. **No new proprietary claim wording or unreleased implementation details are disclosed here.**

## v1.3.0 release acceptance — fail closed

1. Execute the original formal verification runner and repository tests with the declared dependency on an authorized source-bound CI runner; preserve complete exit status and signed/readable run receipt. Do not substitute the route-selection Z3/Ising kernel.
2. Record source- and image-bound negative tests, actual independent provider effect and verification of a stable user-visible result.
3. Complete the existing Workroom job's durable claim/checkpoint/resume chain with an independently observed same-job result and safe tamper/approval negative cases; no duplicate job or synthetic observer signature.
4. Verify privacy-reviewed signed production evidence against an independently pinned public trust anchor using the published [v1.3 proofpack verification contract](WORKROOM_V1_3_0_INDEPENDENT_VERIFICATION.md).
5. Obtain disclosure/legal review before adding potentially novel implementation details to a public archive.
6. Only after the preceding evidence and owner release decision: publish a new **immutable** GitHub version release, verify the actual newly assigned Zenodo version DOI and check archive bytes. Keep v1.2.0 unchanged.

## Conclusion

**v1.2.0 remains the latest published DSG Spacetime version.**  
**v1.3.0 remains an unreleased evidence candidate.**  
Local abstract mathematical checks and the existence of a runtime route must **not** be relabeled as independent production E2E, patent ownership or a new DOI.

See [original v1.3 status](STATUS_V1_3_0_20261102.md), [publication status](../PUBLICATION_STATUS.md) and [public verification protocol](PUBLIC_REPRODUCTION_PROTOCOL_20261030.md).
