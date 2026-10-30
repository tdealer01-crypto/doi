Source: https://raw.githubusercontent.com/tdealer01-crypto/doi/d26821e0e72830d187f281a02f13faef6f71fef5/docs/VERIFY_RELEASE_V1_2_0.md

# Verify the immutable DSG Spacetime v1.2.0 archive

Version DOI: [10.5281/zenodo.23796173](https://doi.org/10.5281/zenodo.23796173). Public record: [23796173](https://zenodo.org/records/23796173).

**Observed result on 2026-10-30:** archive MD5 and SHA-256 matched; all 24 archived file blobs matched the exact GitHub release tree; GitHub verified the release commit signature. The archive is 66,697 bytes.

This no-credential Python 3 check reproduces the publication/archive comparison. It does not execute the private Production runtime or replay its private Ed25519 CI attestation.

```bash
python3 - <<'PY_VERIFY'
import hashlib, io, json, urllib.request, zipfile

def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "DSG-Public-Archive-Verification/1"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()

commit_sha = "1880eb4519e0d1b7cf6b7b598d710d34779647c7"
tree_sha = "f78f45e58a934f32e8f61ad43ff0a8565b4dace3"
record = json.loads(get("https://zenodo.org/api/records/23796173"))
assert record["doi"] == "10.5281/zenodo.23796173"
assert record["conceptdoi"] == "10.5281/zenodo.22172532"
assert record["metadata"]["version"] == "1.2.0"
assert record["metadata"]["license"]["id"] == "cc-by-nc-nd-4.0"
file = next(f for f in record["files"] if f["key"] == "tdealer01-crypto/doi-v1.2.0.zip")
archive = get(file["links"]["self"])
assert len(archive) == file["size"] == 66697
assert hashlib.md5(archive).hexdigest() == "c4772614bdce84b343404a20b9eb3d5a"
assert file["checksum"] == "md5:c4772614bdce84b343404a20b9eb3d5a"
assert hashlib.sha256(archive).hexdigest() == "ded472103bba0dbf5518f7eaf869bdf5f7c1e10df611be427fc30916ddd4465b"
repo = "https://api.github.com/repos/tdealer01-crypto/doi"
tag = json.loads(get(repo + "/git/ref/tags/v1.2.0"))
assert tag["object"]["sha"] == commit_sha
commit = json.loads(get(repo + "/commits/" + commit_sha))
assert commit["commit"]["verification"]["verified"] is True
assert commit["commit"]["tree"]["sha"] == tree_sha
tree = json.loads(get(repo + "/git/trees/" + tree_sha + "?recursive=1"))
assert tree["truncated"] is False
expected = {f["path"]: f["sha"] for f in tree["tree"] if f["type"] == "blob"}
with zipfile.ZipFile(io.BytesIO(archive)) as zip_file:
    prefix = zip_file.namelist()[0].split("/")[0] + "/"
    files = {name[len(prefix):]: name for name in zip_file.namelist() if not name.endswith("/")}
    assert set(files) == set(expected) and len(files) == 24
    for path, name in files.items():
        data = zip_file.read(name)
        git_blob = b"blob " + str(len(data)).encode() + bytes([0]) + data
        assert hashlib.sha1(git_blob).hexdigest() == expected[path], path
print("PUBLIC_ARCHIVE_REPRODUCTION_PASS: DOI, hashes, signature API status, exact tag and all 24 file blobs")
PY_VERIFY
```

The check uses GitHub's public API result for commit signature status; it is not an offline detached-signature verifier. Git blob SHA-1 is used to compare archived file objects to GitHub's signed commit tree, while the complete archive also has a pinned SHA-256.

The immutable archived package contains the honest pending state from before Zenodo assigned its DOI. The later [publication receipt](https://raw.githubusercontent.com/tdealer01-crypto/doi/d26821e0e72830d187f281a02f13faef6f71fef5/docs/evidence/PUBLICATION_V1_2_0.json) records verified ingestion without retagging the release. Public evidence summaries, image digests, local evidence-chain validation and internal signature verification remain distinct from independently observed Production E2E.
