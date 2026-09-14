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

## Browser App capability in v1.1.0

The v1.1.0 publication candidate documents **Browser App**, a governed browser-workflow capability that represents approved web work as a bounded mission and routes execution through DSG Spacetime governance and evidence boundaries.

This update is intentionally implementation-safe. It does not publish the private compiler, policy logic, security controls, deployment topology, secret handling, or production source. See [`docs/BROWSER_APP_PUBLIC_OVERVIEW.md`](docs/BROWSER_APP_PUBLIC_OVERVIEW.md).

The archived v1.0.0 DOI remains immutable. The v1.1.0 GitHub/Zenodo release is being prepared; no v1.1.0 version DOI is claimed until Zenodo publishes it.

## Public release version

The next public archival release is **DSG Spacetime 1.1.0**, prepared from the sanitized public publication/citation surface. The existing **v1.0.0** archive remains immutable.

Versioning here identifies sanitized publication/citation packages. It is not a claim that the private production runtime has been relicensed or published.

## DOI

**v1.1.0 status: PREPARED — exact version DOI pending Zenodo publication.**

- Existing v1.0.0 DOI: **10.5281/zenodo.22172533**
- Concept DOI (all versions): **10.5281/zenodo.22172532**

Use the concept DOI for the DSG Spacetime record while v1.1.0 is being published. The exact v1.1.0 DOI will be recorded only after Zenodo returns it.

## Related and prior publications

Earlier owner-supplied Zenodo publications that may form part of the research lineage are recorded separately in [`docs/RELATED_PUBLICATIONS.md`](docs/RELATED_PUBLICATIONS.md).

Those records are not automatically treated as DSG Spacetime releases. Ambiguous or not-yet-directly-verified DOI relationships are explicitly marked as such.

## License

Unless a file states otherwise, material actually published in this repository is licensed under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**. See `LICENSE.md`.

This license applies only to material contained in this public repository. It does **not** license the private DSG Spacetime production implementation, DSG Fabric internals, production runtime binaries, undisclosed algorithms, private schemas, private tests, anti-bypass mechanisms, customer data, credentials, or other proprietary DSG material outside this repository.

## Public material in this repository

- architecture-level documentation
- citation and Zenodo metadata
- high-level security/threat-model statements
- redacted verification/evidence summaries
- compliance-support mappings
- related/prior-publication lineage notes
- publication guard CI

No production source is intentionally included.

## Current publication state

**PREPARED — public v1.1.0 release metadata is ready; Zenodo version DOI is not yet claimed. v1.0.0 remains VERIFIED and archived.**
