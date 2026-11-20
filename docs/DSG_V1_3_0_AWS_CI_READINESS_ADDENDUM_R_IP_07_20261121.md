# DSG v1.3.0 — AWS Formal Verification Status Addendum

**Dated:** 21 November 2026 (Asia/Bangkok). **Release status:** REVIEW-ONLY / NOT PUBLISHED.

This addendum records a **narrower verified CI milestone**, not a new DSG Spacetime version release and not an independent production deployment certification.

## CI evidence, scoped to formal model and isolated integration tests

- The owner-authenticated AWS CodeBuild project checked out an exact source commit and independently enforced checkout/source matching before executing the existing repository test commands.
- Formal model v2 original runner: Z3 `4.13.3`; T1–T6 returned `unsat`, witness/mutant checks `sat`; 16 reference pairs agreed; historical v1 proof defect reproduced; original Pytest suite **18 tests passed, 0 skipped**.
- Subsequent scoped integration suite: **6/6 system checks passed** (formal model ↔ lifecycle gate, sample HTTP backend, local Ed25519/tamper cases and browser verifier parity); **88 tests passed, 0 skipped**. These checks were on a CI runner and do **not** independently replay a live Production Workroom execution.
- Provider log and exact build identifiers are preserved in private source-bound audit materials. This text is a public-safe status statement, not anonymous reproduction of protected provider-side CI logs.
- The historical `v1.2.0` DOI remains [10.5281/zenodo.23796173](https://doi.org/10.5281/zenodo.23796173). No v1.3.0 GitHub Release or Zenodo Version DOI is claimed.

## Still required before v1.3.0

1. Job-bound, requirement-by-requirement durable Workroom acceptance and verified original job completion, not an unrelated status heartbeat or separate CI PASS.
2. Independent replay of live provider behavior, negative cases and signed evidence with authenticated provenance that can be independently validated.
3. Jurisdiction-specific research/IP ownership and disclosure review, plus accurate scope of public claims.
4. Reviewed public-safe release content, exact tag/archival integrity verification, and actual Zenodo provider DOI assignment.

**Status:** Formal verification and scoped isolated conformance **PASS**; external Production Workroom E2E and v1.3.0 publication **NOT VERIFIED / NOT RELEASED**.
