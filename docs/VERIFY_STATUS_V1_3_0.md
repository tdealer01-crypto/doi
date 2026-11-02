# Public reproduction for the v1.3.0 status document

This is **public metadata consistency**, not a live agent test or a v1.3.0 release. Requires Python 3 with a network connection, no account or third-party packages.

```bash
python3 - <<'PY'
import json, urllib.request
def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent":"DSG-Public-Status-Check/1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)
m = fetch("https://raw.githubusercontent.com/tdealer01-crypto/doi/main/docs/evidence/STATUS_V1_3_0_20261102.json")
assert m["schema"] == "dsg-public-status/v1" and m["target_version"] == "1.3.0"
assert m["public_v13_release_published"] is False
assert m["public_v13_version_doi"] is None
assert m["public_v13_production_e2e_reproducible"] is False
assert m["public_v13_original_signed_receipts_available"] is False
assert any(o["area"] == "workroom-claim-checkpoint-resume" and o["status"] == "NOT_VERIFIED" for o in m["observations"])
release = fetch("https://api.github.com/repos/tdealer01-crypto/doi/releases/tags/v1.2.0")
assert release["tag_name"] == "v1.2.0" and not release["draft"] and not release["prerelease"]
record = fetch("https://zenodo.org/api/records/23796173")
assert record["doi"] == m["last_verified_immutable_archive"]["doi"]
assert record["metadata"]["version"] == "1.2.0"
assert any(f.get("checksum") == "md5:c4772614bdce84b343404a20b9eb3d5a" for f in record.get("files", []))
print("PUBLIC_METADATA_CONSISTENCY_PASS")
print("V1_3_RELEASE=NOT_PUBLISHED; V1_3_PRODUCTION_E2E=NOT_VERIFIED")
PY
```

To **hash actual archive bytes** (stronger than API metadata), run [VERIFY_RELEASE_V1_2_0.md](VERIFY_RELEASE_V1_2_0.md). An unavailable API or failed assertion must be reported as FAIL/BLOCKED, never inferred as PASS. For a private runtime replay, first obtain separately authorized original receipts and independently validate signer trust/provenance; see [PUBLIC_REPRODUCTION_PROTOCOL_20261030.md](PUBLIC_REPRODUCTION_PROTOCOL_20261030.md).

**This new public script was not independently executed against live URLs during preparation in this session.** It is a reproducible procedure, not a recorded PASS.
