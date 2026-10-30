Publication state: TECHNICAL_DRAFT_ONLY. No DEV article or remote draft has been submitted. Review the current DEV AI-assisted-content policy and author accuracy before publication; this is not a release advertisement.

---

# Verify a Zenodo/GitHub release archive with Python—and state exactly what it proves

A public archive, a signed Git commit and a successful runtime test answer different questions. A small reproducible check can connect an archive's bytes to an exact source tree without turning that result into a claim about model performance or runtime safety.

This worked example uses a public documentation archive published on 30 October 2026. It requires Python 3's standard library and no account, API key or private repository access.

## The question

Do the downloaded archive bytes match the published fingerprints, and does every archived file match the exact GitHub release tree?

The example is the DSG Spacetime v1.2.0 documentation package, DOI [10.5281/zenodo.23796173](https://zenodo.org/records/23796173). Its private runtime implementation is not included. The verification observed 66,697 downloaded bytes and 24 file blobs.

## Check the identities before comparing files

The code pins the version DOI, concept DOI, release tag, release commit, tree SHA, archive size and complete archive SHA-256. It also compares Zenodo's advertised MD5 with the download.

For each file, it recreates Git's blob representation: the bytes `blob `, the decimal byte length, a zero byte, and the file content. The SHA-1 of that representation is compared with the blob ID in the exact Git tree. The check compares the complete file-name sets too, so an unexpected extra file cannot pass unnoticed.

The script asks GitHub's public API whether the release commit signature is verified. That API result is a provider statement; this code does not perform offline detached-signature verification.

## Run the public check

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

The exact command was executed during the publication audit and returned the PASS output for the pinned archive. A later mismatch should be reported as a mismatch, rather than hidden by switching to a floating branch or changing the expected hash.

## Keep the conclusion within the test

The result establishes agreement between the downloaded bytes, pinned fingerprints and the publicly reported Git tree. MD5 here cross-checks provider metadata; it is not a release signature. The full archive is also checked with SHA-256.

This does not execute an AI model, independently observe a Production action, prove the soundness of a formal model, or replay a private signed runtime attestation. A website returning HTTP 200 would establish a different, narrower fact again: that the resource was served.

In the example, the published runtime summary records a scoped NVIDIA API browser-read/Memory result using private primary evidence. Independent public Production E2E remains unverified, and the original Ed25519 CI payload is private. Those limitations stay separate from the archive check.

## Report a useful reproduction result

A useful report contains the UTC observation time, exact version DOI, release commit, archive SHA-256, command used and actual output. If a check fails, preserve the failing field and observed value. Do not attach credentials or private logs.

The pinned source for this worked example and the complete publication receipt are in the [public repository](https://github.com/tdealer01-crypto/doi).

AI-assistance disclosure: this technical draft was prepared with AI assistance from the project's published evidence and a verification command that was actually executed. It is an archive-verification case study, not a product advertisement or an independently reproduced Production E2E.

