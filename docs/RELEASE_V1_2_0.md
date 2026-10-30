# DSG Spacetime v1.2.0 — Production Evidence and Reproduction Protocol

Release date: 2026-10-30. This version archives the sanitized public publication surface. It does not distribute the private production runtime.

## What is published

- [Research Priority & Evidence Matrix](RESEARCH_PRIORITY_EVIDENCE_MATRIX.md), linking existing public DOI records and separating archival facts from implementation and invention claims.
- [NVIDIA Production Empirical Evidence](DSG_NVIDIA_PRODUCTION_PUBLIC_PROOF_20261030.md), identifying source `ea73ac8d9aeada37c2cfeec158ff0dcda573d589`, image `sha256:94115f03476e93a8dbce43cbdcf37951c4a148d3c998ae87683c7185cd7a8f10`, model `nvidia/nemotron-3.5-lightning-30b-a3b`, and the observed read-only Workroom/browser/Memory acceptance.
- [Public Reproduction Protocol](PUBLIC_REPRODUCTION_PROTOCOL_20261030.md), including no-credential Zenodo API checks and access requirements for cryptographic and live execution verification.
- [Machine-readable empirical evidence](evidence/DSG_AGENT_V0_PUBLIC_EVIDENCE_20261030.json), retaining earlier blocked results separately from later scoped acceptance.

## What the evidence supports

Primary private records report a successful NVIDIA API proposal, governed browser read and persistent Memory lifecycle for one exact Production image. The dated serving-control-plane audit observed 20 configured Nodes, 39 Routes and a valid local evidence chain with 532 records. These counts are a snapshot, not a promise of current provider availability.

The CI Ed25519 signature was verified during the original audit. The original signed payload is private, so anonymous public signature replay is not available. GitHub commit signatures, release gates, image digests, archive checksums and runtime hash-chain validation support different claims.

## What remains unverified

Independent public E2E reproduction; arbitrary desktop mutations; Kaggle Qwen3-30B GPU/32K inference; automatic worker reconnection/resume; and disk-capacity remediation. The NVIDIA result does not validate the separate Qwen3 training/evaluation paths.

## Verify and cite

Start with the reproduction protocol, compare the exact identifiers, then inspect the public provider records. Verified version DOI: [10.5281/zenodo.23796173](https://doi.org/10.5281/zenodo.23796173). [Verify the immutable archive bytes](VERIFY_RELEASE_V1_2_0.md); the post-publication receipt is in [publication status](../PUBLICATION_STATUS.md). Earlier archival records remain unchanged.

## Public announcement — English

DSG Spacetime v1.2.0 publishes a dated Production evidence inventory and a reproduction protocol. It documents one NVIDIA Nemotron API read-only Workroom/browser/Memory acceptance tied to an exact source and image digest. The package distinguishes publicly reproducible DOI metadata from private primary execution evidence and internally verified signatures. Independent public E2E reproduction remains open. Read the evidence, limits and reproduction steps in this repository.

## Public announcement — ภาษาไทย

DSG Spacetime รุ่น 1.2.0 เผยแพร่ชุดข้อมูลหลักฐาน Production และขั้นตอนตรวจซ้ำ โดยระบุผลทดสอบ NVIDIA Nemotron API → Workroom → อ่านข้อมูลผ่าน Browser → บันทึก Memory ที่ผูกกับ Source และ Image Digest ชัดเจน เอกสารแยกข้อมูล DOI ที่ทุกคนตรวจซ้ำได้ออกจากหลักฐานการทำงานและลายเซ็นต้นฉบับที่ยังเป็นข้อมูลภายใน การทดสอบ E2E ซ้ำโดยบุคคลภายนอกยังไม่ยืนยัน อ่านผล ข้อจำกัด และวิธีตรวจได้จากเอกสารในรีโพนี้
