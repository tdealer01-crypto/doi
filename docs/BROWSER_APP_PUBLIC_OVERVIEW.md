# DSG Spacetime — Browser App Public Overview

## Publication status

This page is included in the **DSG Spacetime v1.1.0 public release candidate**. The prior v1.0.0 Zenodo snapshot identified by DOI `10.5281/zenodo.22172533` remains immutable.

The exact v1.1.0 version DOI is intentionally left unclaimed until Zenodo publishes the new record. The concept DOI continues to identify DSG Spacetime across versions.

## What Browser App adds

Browser App lets an approved web workflow be represented as a bounded mission specification and executed through DSG Spacetime's governed capability model.

At a public architecture level:

```text
User / Agent Intent
        |
        v
Bounded Browser Mission
        |
        v
Validation + Plan Binding
        |
        v
Governed Browser Capability
        |
        v
Web Interaction
        |
        v
Evidence + Verification
```

The mission can describe ordinary browser work such as navigation, form interaction, extraction, upload/download handling, and verification. The browser capability remains subject to the same principle used across DSG Spacetime: **proposal is not permission**.

## Governance boundary

Browser App does not turn an AI model into an unrestricted browser operator.

Public safety properties include:

- browser work is bounded to an approved mission/capability scope;
- web content is treated as untrusted input, not authority;
- sensitive identity material is not intended to be placed in ordinary AI/browser mission content;
- higher-risk side effects remain subject to applicable approval and capability boundaries;
- execution results must be evidenced before they are represented as verified;
- a browser capability does not grant access to unrelated Nodes, Routes, credentials, or systems.

The private implementation of mission compilation, authorization logic, anti-bypass controls, security mechanisms, provider binding, and deployment mechanics is intentionally not published here.

## Public verification status

As of 2026-09-14, the private production change that introduced the governed Browser App surface passed the applicable private runtime CI and source-free packaging smoke checks before/after integration.

Provider deployment and live web-task claims remain separate evidence scopes. This public repository does not infer a live production result from source or CI alone.

## Relationship to the DOI record

- DSG Spacetime v1.0.0 remains archived at DOI `10.5281/zenodo.22172533`.
- Concept DOI `10.5281/zenodo.22172532` continues to identify the DSG Spacetime record across versions.
- This page is part of the v1.1.0 public release candidate.
- The exact v1.1.0 version DOI must be returned by Zenodo before this candidate is described as an archived Zenodo release.

## Intellectual-property boundary

This document describes only product-level behavior and safety properties. It does not publish production source code, proprietary governance algorithms, internal schemas, private security controls, private tests, deployment topology, credentials, or other confidential implementation know-how.
