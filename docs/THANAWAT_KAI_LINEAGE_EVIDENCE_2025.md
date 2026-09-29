# THANAWAT / KAI Lineage Evidence — 2025

## Scope

This record preserves public-safe evidence relevant to the historical development of the user's mobile/Termux AI-node and KAI agent work.

It separates:

1. externally timestamped public Git history,
2. uploaded snapshots with cryptographic hashes,
3. archive-internal timestamps,
4. media-container metadata,
5. technical-content observations.

This is a provenance record, not a legal conclusion. It does not by itself establish patent priority, novelty, inventorship, ownership against third parties, or that every artifact belongs to one legally identical invention.

## E-TH-001 — public Git repository initial commit

Repository: `Taraaaa1111/thanawat-network`

- Initial commit SHA: `31bf392dcbad796389318ab11828869afb91a83f`
- Commit message: `Initial commit`
- GitHub commit timestamp observed: **2025-12-08T14:32:01+07:00**

**Evidence status:** **PUBLIC GIT TIMESTAMP.**

This is an external timestamp showing that the THANAWAT repository existed publicly on GitHub by the observed commit time.

## E-TH-002 — public Termux AI-node installer

Repository: `Taraaaa1111/thanawat-network`

Commit:

- SHA: `814625bb928bcbff82358e75c61f726ef9ebf82b`
- Commit message: `Create install script for THANAWAT node setup`
- GitHub commit timestamp observed: **2025-12-08T14:42:37+07:00**
- File: `install.sh`
- Blob SHA observed at that commit: `221771be0c7e0c4177afdddd120500427d16255d`

The public script at that commit:

- initializes a decentralized AI node on Termux;
- installs an ARM64 scientific stack;
- installs Flower, Web3, and IPFS;
- configures IPFS low-power mode;
- creates a Flower `NumPyClient`;
- simulates local model training;
- prints `THANAWAT NODE IS READY`;
- prints a local-data/privacy-preserved training step and a blockchain-weight submission step.

**Evidence status:** **PUBLIC GIT / EXECUTABLE TECHNICAL ARTIFACT.**

## E-TH-003 — public repository architecture description

Commit:

- SHA: `d7f49415bcf1f66af93b70c0079da067059c3251`
- Commit message: `Revise README with THANAWAT details and features`
- GitHub commit timestamp observed: **2025-12-08T14:51:36+07:00**
- README blob SHA: `1e9a96413c4f72083d4acf4294a090f2ac925c0d`

The README at that commit describes:

- Android / Termux as the platform;
- a decentralized AI / federated-learning network;
- Termux + IPFS + Federated Learning;
- privacy-preserving local compute where model weights, not raw data, are shared;
- a one-click deployment path;
- a roadmap covering node visualization and blockchain incentives.

**Evidence status:** **PUBLIC GIT / ARCHITECTURE DESCRIPTION.**

## E-TH-004 — recorded Termux demonstration video

Uploaded artifact: `received_-251769136.mp4`

- SHA-256: `1e186aac4c3e4c3dfc88ab6e09d4ee57eb06596bcbf550cec25bdf9ea066d83b`
- Duration: approximately 58.3 seconds
- Video: H.264, 720 × 1600
- Audio: AAC
- MP4 container `creation_time`: **2025-12-08T15:06:17Z**

Visual inspection of representative frames shows:

- the public GitHub repository `Taraaaa1111/thanawat-network`;
- the README title `THANAWAT: Decentralized AI & Federated Learning Network`;
- a Termux session displaying decentralized-node initialization;
- Flower/Web3 federation setup;
- IPFS low-power storage;
- `THANAWAT NODE IS READY`;
- local-data training and model-weight submission messages.

**Evidence status:** **HASHED MEDIA SNAPSHOT + CONTAINER TIMESTAMP, CORROBORATED BY SAME-DAY PUBLIC GIT HISTORY.**

The MP4 container timestamp is not treated as independently immutable because media metadata can be edited. Its evidentiary value is strengthened by the separate public Git commits from the same date.

Additional internal-consistency check: **2025-12-08T15:06:17Z equals 22:06:17 in UTC+07**, while the phone status bar visible in the inspected video frames shows approximately **22:05–22:06**. This consistency supports the media timeline but still does not convert container metadata into an immutable external timestamp.

## E-TH-005 — THANAWAT Protocol proposal / whitepaper snapshot

Uploaded artifact title: `เอกสารไม่มีชื่อ`

- SHA-256: `d5ea2bd9ffe4e9e4f27b35fb2bb077bb40219789b2a87875b810ad960c4b8ca5`

The preserved document contains:

- `THANAWAT PROTOCOL: The Self-Healing Decentralized AI Network`;
- a self-healing architecture for Android/mobile nodes;
- an APR (Automated Program Repair) engine using AST manipulation;
- automatic patch/restart concepts;
- Termux and IPFS;
- federated learning;
- Proof-of-Uptime;
- a sandbox fitness function for candidate repair patches.

**Evidence status:** **HASHED TECHNICAL / COMMERCIAL-DOCUMENT SNAPSHOT.**

No independent original-creation or publication timestamp was established from this uploaded PDF.

## E-KAI-006 — Kai Node archive

Uploaded artifact: `kai_node_final.zip`

- Archive SHA-256: `9b2c9994144a2c65171b1df66c62161fd4162c528c2c07d48a1585333a3702a4`
- ZIP member timestamps: **2025-11-23 15:25** (archive-local metadata)

Members and SHA-256 values:

- `server.js` — `becea752a802dcfc49d43f619daf819177ec0640e73eee04936dc8fce9c7e49c`
- `executor.js` — `7905245450f88156f9be9d214a0023cdb02375d3963d954629c623d74116f582`
- `config.json` — `03c8f8dca1c2eec77aebd02712d472cbbc05a7ccdbfa5af99dae257b3343fe86`
- `README.txt` — `a89ec1bb8772abc481a3d57fb0246319fe7c87760596ae59e2c4143566016f5d`

Observed content is explicitly placeholder-level:

- `server.js` identifies a `KaiMaster` placeholder;
- `executor.js` identifies an executor placeholder;
- `README.txt` says `Kai Node Placeholder Build`;
- `config.json` uses development mode.

**Evidence status:** **HASHED ARCHIVE / ARCHIVE-INTERNAL TIMESTAMP / EARLY KAI-NODE PLACEHOLDER.**

The ZIP member timestamps are not treated as external provider timestamps and do not independently prove creation on 2025-11-23.

## E-KAI-007 — Kai Panel / Atlas source snapshot

Uploaded artifact: `kai.txt`

- SHA-256: `11863423b2cb5315903d839b3c5017833db985414c50a4a90b569e27440f5402`

The HTML source identifies:

- `Kai Panel Combo (Minimal + Atlas)`;
- Minimal and Atlas operating layouts;
- modes for core reasoning, code, business, automation, and integration;
- Termux / Node.js / Android as a code-target environment;
- workflow automation and webhook / n8n concepts;
- external integration examples including OpenAI API;
- an Atlas prompt example explicitly referencing a `Kai Gen12` workflow integrating n8n, Bybit, and Termux.

Two uploaded PDF exports contain text-equivalent content:

- `kai` SHA-256: `4f994c7cc3d9a462376af6fce71127b7bf92bb5c80983d863009f26d55ba0d60`
- `rttttrtt.html` SHA-256: `1cdec87d599913c82b97126962831e950eeaee9df2e699cba8055e9848921c0b`

Their extracted text was byte-identical after PDF-to-text normalization in this evidence session.

**Evidence status:** **HASHED KAI-UI / WORKFLOW-ORCHESTRATION SNAPSHOT.**

No independent original-creation timestamp was established from these uploaded snapshots.

## E-KAI-008 — KAI GEN12 OpenAI API integration report

Uploaded artifact: `KAI GEN12: OpenAI API Integration`

- SHA-256: `161a17535b542fe393a0c69a1a99b4c7144dd5471c85e562e6c97686078a1d9a`
- PDF title metadata: `KAI GEN12: OpenAI API Integration`

The report explicitly describes a `KAI GEN12 Multi-Agent` architecture and discusses:

- Node.js as the runtime;
- Android / Termux edge deployment;
- GPT-4.1-mini as a proposed core cognitive model;
- Supervisor / sub-agent patterns;
- STT and TTS modules;
- environment-variable handling for API credentials;
- a cognitive agent loop connecting speech input, model reasoning, speech output, and Termux execution;
- retry / recovery considerations and continuous monitoring.

**Evidence status:** **HASHED GEN12 TECHNICAL-REPORT SNAPSHOT.**

This report is useful for KAI GEN12 architecture provenance, but the uploaded snapshot does not independently establish its original creation date.

## Credential-bearing artifact excluded from public evidence

One uploaded PDF (`tarai`) contains what appears to be an OpenAI project API credential.

It is intentionally **not** copied, quoted, hashed into this public evidence document, or committed to the repository.

The credential should be treated as exposed and rotated/revoked if it is still active.

## Chronology boundary

The strongest externally timestamped evidence in this record is the public GitHub history on **2025-12-08**.

The `kai_node_final.zip` archive contains earlier internal timestamps (**2025-11-23**), but those are archive-local metadata and therefore weaker than public/provider timestamps.

Accordingly, this record supports the following narrower chronology:

`early Kai node placeholder snapshot (archive-internal date only) → public THANAWAT Android/Termux decentralized AI node (GitHub, 2025-12-08) → later KAI panel / Gen12 integration snapshots`

This is a provenance hypothesis supported by the preserved artifacts, not a legal finding that each stage is the same invention or that the sequence establishes novelty over all prior art.
