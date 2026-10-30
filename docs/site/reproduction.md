Source: https://raw.githubusercontent.com/tdealer01-crypto/doi/v1.2.0/docs/PUBLIC_REPRODUCTION_PROTOCOL_20261030.md

# DSG Public Evidence — Reproduction Protocol (2026-10-30)

**Status:** public metadata verification executable now; cryptographic Production CI replay requires owner-authorized original attestation; live Workroom E2E is not anonymously reproducible.  
**Scope:** publication and empirical verification; no private source distribution or unsigned proof substitution.

## 1. Public no-credential metadata replay

The following Python 3 standard-library command checks Zenodo's **current provider metadata**, DOI/version identity, publication date, concept relation and advertised archived checksums. It runs from a shell (including Termux with Python) without access to DSG accounts:

```bash
python3 - <<'PY'
import json
import urllib.request

expected = {
    18212854: ("10.5281/zenodo.18212854", "2026-01-11", "10.5281/zenodo.18212853", "md5:9b5d3fa54aa1605ed1758704753e8235"),
    18225586: ("10.5281/zenodo.18225586", "2026-01-12", "10.5281/zenodo.18225585", "md5:a62f7e0b1561fd2cdb355b16d157bf73"),
    22172533: ("10.5281/zenodo.22172533", "2026-08-30", "10.5281/zenodo.22172532", "md5:348b023d4af727e1bae0fb2d46ef799f"),
    22755320: ("10.5281/zenodo.22755320", "2026-09-14", "10.5281/zenodo.22172532", "md5:1f3b879bd54e8ded7c1411d72deb1522"),
}
for record_id, (doi, pubdate, concept, checksum) in expected.items():
    url = f"https://zenodo.org/api/records/{record_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "DSG-Public-Verification/1"})
    with urllib.request.urlopen(req, timeout=20) as response:
        record = json.load(response)
    assert record["id"] == record_id, (record_id, "ID_MISMATCH")
    assert record["doi"] == doi, (record_id, "DOI_MISMATCH")
    assert record["metadata"]["publication_date"] == pubdate, (record_id, "PUBLICATION_DATE_MISMATCH")
    assert record["conceptdoi"] == concept, (record_id, "CONCEPT_DOI_MISMATCH")
    assert any(f.get("checksum") == checksum for f in record.get("files", [])), (record_id, "ARCHIVE_CHECKSUM_METADATA_MISMATCH")
    print("PROVIDER_METADATA_PASS", record_id, doi, pubdate)
print("METADATA_TESTS_PASS=4")
PY
```

**Meaning:** `METADATA_TESTS_PASS=4` verifies that Zenodo currently advertises the expected metadata and checksums. It does **not** hash the downloaded bytes, prove historical invention priority, establish Z3 proof soundness or verify DSG Production. A separate test can download each exact archive URL and compute its MD5 to cross-check provider-advertised checksums.

## 2. Authorized cryptographic CI-attestation replay

The Production post-merge CI attestation is an Ed25519 signature over the **exact canonical JSON payload**, not a signature over a redacted report. The source verifier canonicalizes with:

```python
json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
```

The authorized verifier obtains the **unmodified** original signed JSON and the pinned **public verification key** through the existing owner-authorized DSG repository/attestation workflow. Neither signing key nor private operational material should be pasted in chat or moved into this public repository.

Verification with `cryptography` installed:

```bash
# Local file paths point to owner-approved original files, not URLs or secrets in source.
python3 - "$DSG_SIGNED_CI_DOC" "$DSG_PUBLIC_KEY_FILE" <<'PY'
import base64, json, pathlib, sys
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

doc = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
payload = doc["payload"]
key = base64.b64decode(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").strip(), validate=True)
sig = base64.b64decode(doc["signature_b64"], validate=True)
assert len(key) == 32 and len(sig) == 64
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
Ed25519PublicKey.from_public_bytes(key).verify(sig, canonical)
assert payload["source_sha"] == "d8fe636f3c1c3fd8ddec4ed699eeff49c6952d06"
assert payload["ci"]["run_id"] == "41015153555"
assert payload["pull_request"]["number"] == 871
print("ED25519_CI_SIGNATURE_PASS")
PY
```

The verifier must **also** check the verification key's trust-anchor provenance and exact policy digest with the authorized production policy. A valid signature without a trusted key is not an authentic release proof. As a negative test, deliberately change a **copy** of the signed document's payload; `Ed25519PublicKey.verify` must reject the original signature. Do not mutate the original record.

**Public status:** the auditor validated the actual Ed25519 signature on 2026-10-30, but third-party anonymous signature replay remains **BLOCKED BY DISCLOSURE BOUNDARY** because the original signed payload is private. The public verification key fingerprint can be checked against the redacted [production report](https://raw.githubusercontent.com/tdealer01-crypto/doi/v1.2.0/docs/DSG_NVIDIA_PRODUCTION_PUBLIC_PROOF_20261030.md).

## 3. Independent E2E acceptance for an authorized test tenant

Use a dedicated test goal that cannot mutate customer data:

1. Capture UTC time, exact `source_sha`, pinned running image digest, model/provider identity and initial evidence-chain count.
2. In a permitted Workroom session, request one **read-only** `action.plan` proposal for a browser text extraction. The proposal must carry **no execution authority**.
3. Execute only the permitted browser-read route through its normal exact-action governed path. Record provider result/receipt and independently observe the browser state/result.
4. Commit a bounded Memory start/end record, read it back independently and compare state hash and sequence.
5. Re-verify signed/auditable evidence-chain status; bind outcome to exact plan/decision/result hash and source/image.
6. Test a deliberately invalid/missing approval **only inside an isolated fixture**, recording BLOCK and independent no-side-effect observation. Do not test unauthorized real customer mutations.
7. Repeat on a second verifier/tenant, compare proof fields and label discrepancies FAILED/NOT VERIFIED rather than fabricating matching outputs.

**Acceptance:** publish a redacted exact-source evidence bundle only when provider receipt, independent observer, Memory readback, signed verifiable audit chain and negative-case no-side-effect checks all agree. A model response, vendor request ID, plan BOUND or GitHub CI PASS alone is insufficient.

## 4. Status and exceptions

| Test | Status |
| --- | --- |
| Zenodo metadata API reproduction | **PUBLICLY REPLAYABLE** |
| Signed private CI attestation verification | **AUDITOR VERIFIED; ANONYMOUS PUBLIC REPLAY NOT AVAILABLE** |
| NVIDIA exact-image Workroom browser-read + durable Memory | **SCOPED PROD PASS (PRIVATE PRIMARY RECORDS)** |
| Independently repeat same E2E on another tenant | **NOT VERIFIED** |
| Kaggle Qwen3-30B GPU/32K/held-out benchmark | **NOT VERIFIED** |
| Autonomous worker reconnection after disconnection | **NOT VERIFIED** |
| Disk-capacity remediation after observed ~1.83 GB free | **NOT VERIFIED** |

The source Production repository remains private. This reproduction protocol has no execution authority, grants no access to signing keys, and does not alter any protected deployment.
