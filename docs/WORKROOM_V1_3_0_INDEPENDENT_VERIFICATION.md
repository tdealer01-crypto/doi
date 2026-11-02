# DSG Workroom v1.3.0 — Independent Proofpack Verification Contract

**Public verification tooling — 2026-11-02. Runtime proof status: NOT VERIFIED.**

This is a verification contract for a **future, genuine** production receipt bundle. **No signed Workroom E2E proofpack or independent observer receipt has been published.** Running this procedure cannot turn the current `PLANNING` job into PASS. The existing [status report](STATUS_V1_3_0_20261102.md) and [v1.2.0 archive reproduction](VERIFY_RELEASE_V1_2_0.md) remain separate claims.

## Required immutable inputs

An approved, privacy-reviewed `proof.json`, a separately published `trust.json`, and an expected SHA-256 of the **exact trust.json bytes** pinned in a verified immutable public release. Never take the trust fingerprint from the proof itself. A private source commit reference, test report or healthy API alone is not proof of execution.

A proof package must have:
- A canonical JSON `payload` with `schema="dsg-workroom-e2e-proof/v1"`, a 40-character source SHA, SHA-256 image digest, plan-revision SHA-256, salted opaque job identifier hash, original ordered and chained evidence events, committed result hash, independent readback hash and signed execution outcomes. No credentials or customer data.
- Two separately issued Ed25519 signatures over the same **unmodified** `payload`: the governed production receipt signer and an external observer who actually inspected provider state and the UI result. The independent observer must not use the production signer key.
- The chain must bind the **same job** through `goal-submitted`, `worker-claimed`, `checkpoint-committed`, `worker-reclaimed`, `provider-result`, `job-completed`, `ui-result-readback`. One actual `native-dispatch` must appear; no duplicate effect on resume.
- Signed evidence chain records or a separately independently verified digest chain. A boolean `chain_valid` from a private service is insufficient for anonymous replay.

## Offline command (no DSG account)

Requires Python 3 and the published `cryptography` package. This intentionally **fails closed** if any evidence, trust anchor, observer signature or expected event is absent.

```bash
python3 -m pip install cryptography
python3 - "$PROOF_JSON" "$TRUST_JSON" "$PINNED_TRUST_SHA256" <<'PY'
import base64, hashlib, json, pathlib, re, sys
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

def canonical(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def sha(v):
    return hashlib.sha256(v).hexdigest()

assert len(sys.argv) == 4, "proof.json, trust.json, and independently pinned trust SHA-256 required"
proof = json.loads(pathlib.Path(sys.argv[1]).read_bytes())
trust_bytes = pathlib.Path(sys.argv[2]).read_bytes()
assert re.fullmatch(r"[0-9a-f]{64}", sys.argv[3])
assert sha(trust_bytes) == sys.argv[3], "UNTRUSTED_PUBLIC_KEY_FILE"
trust = json.loads(trust_bytes)
payload = proof["payload"]
assert payload["schema"] == "dsg-workroom-e2e-proof/v1"
assert re.fullmatch(r"[0-9a-f]{40}", payload["source_sha"])
assert re.fullmatch(r"sha256:[0-9a-f]{64}", payload["image_digest"])
assert re.fullmatch(r"[0-9a-f]{64}", payload["plan_revision_sha256"])
assert re.fullmatch(r"[0-9a-f]{64}", payload["job_id_sha256"])
assert payload["final_status"] == "COMPLETED"
assert payload["execution_result_sha256"] == payload["independent_ui_readback_sha256"]
assert payload["checkpoint_sha256"] == payload["resume_checkpoint_readback_sha256"]

signers = trust["signers"]
assert set(signers) == {"production", "independent_observer"}
assert signers["production"]["key_b64"] != signers["independent_observer"]["key_b64"]
for role in ("production", "independent_observer"):
    key = base64.b64decode(signers[role]["key_b64"], validate=True)
    sig = base64.b64decode(proof["signatures"][role], validate=True)
    assert len(key) == 32 and len(sig) == 64
    Ed25519PublicKey.from_public_bytes(key).verify(sig, canonical(payload))

events = payload["events"]
assert isinstance(events, list) and len(events) >= 8
assert [e["sequence"] for e in events] == list(range(1, len(events)+1))
assert len({e["job_id_sha256"] for e in events}) == 1
assert events[0]["job_id_sha256"] == payload["job_id_sha256"]
prev = "0"*64
for event in events:
    assert event["previous_hash"] == prev
    body = {k:v for k,v in event.items() if k != "record_hash"}
    assert event["record_hash"] == sha(canonical(body)), "EVIDENCE_RECORD_TAMPERED"
    prev = event["record_hash"]
assert prev == payload["evidence_head_hash"]
kinds = [e["kind"] for e in events]
required = ["goal-submitted","worker-claimed","checkpoint-committed",
            "worker-reclaimed","provider-result","job-completed","ui-result-readback"]
positions = [kinds.index(kind) for kind in required]
assert positions == sorted(positions), "EVENT_ORDER_INVALID"
assert kinds.count("native-dispatch") == 1, "DUPLICATE_OR_MISSING_PROVIDER_DISPATCH"
assert payload["independent_observer_method"] == "direct_provider_and_ui_readback"
print("SIGNED_WORKROOM_PROOFPACK_CONSISTENCY_PASS")
print("LIVE_THIRD_PARTY_E2E_REEXECUTION_NOT_PROVEN_BY_OFFLINE_SIGNATURE_CHECK")
PY
```

**Proof interpretation:** A PASS checks an authentic, trusted dual-signed evidence statement and its internal chain/consistency *if* separately sourced trust and actual proof bytes exist. It does not itself prove that a third party successfully re-executed the live agent. A second authorized real test tenant, fresh plan, independent provider observation and a corresponding signed run are required for the stronger claim **INDEPENDENT LIVE E2E REPRODUCED**.

## Current acceptance / สถานะจริง

| Requirement | Status |
| --- | --- |
| Public verification specification | **AVAILABLE** |
| Production same-job worker claim/checkpoint/resume | **NOT VERIFIED** |
| Genuine privacy-reviewed signed proof.json | **NOT PUBLISHED** |
| Separately anchored public trust.json | **NOT PUBLISHED** |
| Independent observer attestation | **NOT VERIFIED** |
| Offline verification using genuine v1.3.0 Workroom receipts | **NOT EXECUTED** |
| Independent live Workroom replay | **NOT VERIFIED** |
| Immutable v1.3.0 release and Zenodo version DOI | **NOT PUBLISHED** |

This procedure introduces **no** additional Production policy gate, role, cloud service or test bypass. Never substitute demonstration data for original receipts. This public document is **not** a product certification.
