# Publication Status

Status: **PREPARED — NOT YET DOI-VERIFIED**

Release readiness: **READY FOR GITHUB RELEASE `v1.0.0`**

This public repository is the sanitized publication/citation surface for DSG Spacetime. It is separate from the private production repository.

## Completed preparation

- public repository exists
- public-safe README prepared
- `CITATION.cff` prepared
- `.zenodo.json` prepared
- architecture-level documentation prepared
- high-level security/threat-model material prepared
- redacted evidence summary prepared
- compliance-support matrix prepared
- publication guard hardened and verified green on `main`
- current public tree and repository history reviewed for the publication boundary; no production source was observed in the reviewed tree/history, and the automated source/sensitive-file/obvious-secret history guard passed
- first public semantic version selected: **1.0.0** (GitHub release tag: `v1.0.0`)
- public repository license selected: **CC BY-NC-ND 4.0** (`CC-BY-NC-ND-4.0`)
- license boundary recorded in `LICENSE.md`; the license applies only to material actually published in this public repository and does not license private DSG production implementation or undisclosed proprietary material
- creator metadata confirmed as **Thanawat Suparongsuwan**; no ORCID is asserted in metadata because none has been provided for this release
- Zenodo GitHub repository enablement was owner-confirmed in the publication session; the actual archive/DOI remains unverified until a release is processed and the resulting DOI resolves
- PR #5 (`release: prepare DSG Spacetime v1.0.0 metadata`) passed the publication guard on head run `33306855533`
- PR #5 merged to `main` at `dc564c5bded9a66338d0e41ba59b641feecae6ec`
- post-merge `main` publication guard run `33306886006` passed all checks, including current-tree/history secret screening, source/sensitive-file rejection, Zenodo metadata validation, citation validation, and pre-DOI enforcement

## Required before DOI can become VERIFIED

- create the GitHub Release/tag `v1.0.0`
- wait for Zenodo to ingest/process the release
- inspect the resulting Zenodo record and archived files
- verify the real DOI resolves
- record the real DOI in repository metadata only after that verification

The disclosure review above is a publication-boundary review, not a claim of exhaustive security audit or secret detection.

**No DOI is claimed in this repository yet.**
