# DSG ONE — Production website ship proof / หลักฐาน Release เว็บไซต์ (2 Nov 2026)

**Publication class:** public-safe observation and repeatable no-login website probe.  
**Result:** **PASS for the scoped website release**; **NOT VERIFIED for whole-system Agent/Workroom v1.3.0 E2E**.  
**Version boundary:** This is an update to public documentation, **not** a v1.3.0 GitHub Release or Zenodo version DOI. The last verified immutable public archive remains [v1.2.0](https://github.com/tdealer01-crypto/doi/releases/tag/v1.2.0) / [10.5281/zenodo.23796173](https://doi.org/10.5281/zenodo.23796173).

## Exact published identifiers

| Field | Observed value |
| --- | --- |
| Product / public target | DSG ONE — https://dsg.pics |
| UTC date of private ship job | 2026-11-02 |
| Immutable source SHA | `ccee11e6220af294da39353192622d99844de1b5` |
| ECR image digest / production metadata digest | `sha256:e375163cc279ce39f03acfbf1f5220354f21ee99e56f5dc1fad9b918f99a6320` |
| GitHub Actions run / successful job | [Run 41481778354](https://github.com/tdealer01-crypto/DSG-Private-Production-Runtime/actions/runs/41481778354) / job `125413476223` |
| Source of CI, AWS and deploy claims | Authenticated private job log and read-only AWS SSM/ECR metadata observations |
| Independent, anonymous CURRENT PUBLIC WEBSITE replay | **PASS** — full no-login Python verifier executed on third-party environment, 2026-11-02T17:00:57Z |

**Access limitation:** The Actions link targets a **private** repository. Anonymous readers cannot independently retrieve its original job logs. The abbreviated markers below are sanitized owner-observed facts, **not** a cryptographically signed or publicly downloadable original CI attestation.

## What the actual release job and AWS readback showed

- `RELEASE_SOURCE_AND_CI=PASS` for the exact source SHA.
- OIDC AWS role assumption: job step **SUCCESS**, after a narrow trust-subject correction. Neither an IAM policy nor an identity token is published here.
- `RELEASE_PREFLIGHT=PASS` for the same source, pinned image digest and existing running host.
- `DSG_ONE_RELEASE=DEPLOYED` — existing-host release path; no new server claimed.
- `DSG_ONE_PUBLIC_SERVING=VERIFIED_COMPLETED` for the exact SHA, obtained by the owner release workflow via public HTTPS.
- `DSG_ONE_ACTIVE_METADATA=PASS` for the exact SHA and ECR digest.
- `PUBLIC_DOCS_SERVING=PASS` for 9 URLs: `/capabilities`, `/architecture`, `/verification`, `/releases`, `/llms.txt`, `/api/public/capabilities.json`, `/openapi-public-capabilities.json`, `/sitemap.xml`, `/robots.txt`.
- **Second readback after completion:** Authenticated AWS `GetParameters` and ECR `DescribeImages` returned the same SHA and image digest. A match of private AWS metadata is **not** independently repeatable without authorized AWS read access.
- GitHub job `125413476223` finished with `conclusion=success`, including public-serving and metadata steps.

## External no-login public status readback — PASS (separate observation)

At approximately 2026-11-02T16:59:48Z, a fresh third-party public HTTP fetch (Firecrawl; no DSG/AWS credentials) requested `https://dsg.pics/api/agent/status` and received **HTTP 200**. The response's own `ts` field was `2026-11-02T16:59:29.404Z`; its `version`, `deployment.buildSourceSha`, `deployment.expectedSourceSha` and `deployment.imageDigest` matched the exact identifiers above; `sourceBound` and `digestBound` were both true. This is a *fresh external current-serving read*, **not** replay of historical private OIDC/CI or a full external nine-URL check. The manifest records this distinct observation. A verifier can independently fetch the same endpoint; timestamps and future deployment identities may differ.

## Independent full public-site replay — PASS / ผลรันทดสอบซ้ำภายนอก

**New primary observation (2 Nov 2026):** At approximately `2026-11-02T17:00:57Z`, the publicly published Python 3 script and evidence manifest were downloaded together from **public Git commit `aeccf89a097d6187a375cd47f4163ba74bac4116`** and executed in a third-party Firecrawl Python session without DSG or AWS credentials.

**Actual execution result:** `exit_code=0`; `PASS /api/agent/status exact source + digest`, all nine documented public URLs **PASS**, `PUBLIC_WEBSITE_CURRENT_SERVING_REPLAY=PASS`. The stdout also explicitly states `PRIVATE_OIDC_AND_DEPLOY_ATTESTATION=NOT_PUBLICLY_REPLAYED` and `WORKROOM_AGENT_V1_3_E2E=NOT_VERIFIED`.

This confirms **a real anonymous current-serving rerun**, stronger than instructions-only publication. It does **not** independently reproduce the protected historical GitHub/AWS OIDC handshake or demonstrate same-job Agent/Workroom completion. This observation is recorded as a separate external run in the [manifest](evidence/DSG_ONE_WEBSITE_SHIP_20261102.json), without upgrading any whole-system claims.

## Independent repeat: verify the current public serving / วิธีรันตรวจซ้ำได้เอง

You need **Python 3 and internet access only**; no AWS or DSG login and no third-party packages. Use the public [machine-readable snapshot](evidence/DSG_ONE_WEBSITE_SHIP_20261102.json) and the [verification script](verify_dsg_one_website_ship.py):

```bash
git clone https://github.com/tdealer01-crypto/doi.git
cd doi
python3 docs/verify_dsg_one_website_ship.py
```

The script fails closed on any of these mismatches:

1. Public `/api/agent/status` must return HTTP 200, `ok=true`, the exact recorded `version`, `deployment.buildSourceSha`, `deployment.expectedSourceSha`, `deployment.imageDigest`, `sourceBound=true` and `digestBound=true`.
2. All 9 documented public URLs must return HTTP 200.
3. The public capabilities JSON must match the **dated** 2026-11-01 configured snapshot (20 nodes, 39 routes) and explicitly say `e2eWholeSystem=NOT_VERIFIED`.
4. Sitemap and `llms.txt` must contain the expected public discovery pointers.
5. The local manifest must continue to say v1.3.0 release **not published** and Workroom Claim → Checkpoint → Resume **not verified**.

On success the command prints `PUBLIC_WEBSITE_CURRENT_SERVING_REPLAY=PASS`. **The output is about the currently reachable public website; it is not an independent replay of the historical GitHub OIDC exchange, AWS deployment, signed CI evidence or Workroom task.**

On failure it exits nonzero and prints `FAIL_OR_BLOCKED` plus a reason. A newer deployment may legitimately change the serving SHA; that means **this exact pinned historical-release check no longer matches the current website**, not that the previous dated release never happened.

To preserve reproducibility over time, pin the public repository's commit (shown by `git rev-parse HEAD`) and keep the manifest, script and document from the **same commit**. `main` can advance and is not an immutable archival version. Do not change the expected SHA/digest merely to force PASS.

## Verification boundaries / ข้อจำกัดตามหลักฐานจริง

| Claim | Classification |
| --- | --- |
| Owner-authenticated source-bound website build and deployment | **PASS — private primary evidence** |
| Owner-authenticated AWS SSM metadata equals ECR digest | **PASS — private readback** |
| Website version/digest and public pages checked in the release job | **PASS — owner workflow** |
| Public unauthenticated current-website rerun | **PASS — 10 endpoints (status + 9 public paths), third-party Python, exit 0** |
| Publicly downloadable original signed OIDC/CI attestation | **NOT AVAILABLE** |
| Same-job Workroom goal → claim → checkpoint → resume → visible completion | **NOT VERIFIED** |
| Agent-v0 / Cinema / Native end-to-end user task | **NOT VERIFIED as whole-system acceptance** |
| Immutable v1.3.0 release + Zenodo version DOI | **NOT PUBLISHED** |

**Privacy boundary:** No credentials, identity tokens, private repo contents, full runner logs, IAM policy, customer data, device details or secret values are published. The raw owner-only records remain access restricted.

**ถอดความ:** ปิดงาน Release เว็บไซต์จริงพร้อม SHA และ Digest ที่ตรวจได้ ส่วนการทำงาน Agent / Workroom แบบจบงานยังต้องมีหลักฐานจาก Job จริงแยกต่างหาก ไม่ใช้ผล CI ของเว็บไซต์แทนหลักฐาน E2E ของเอเจนต์
