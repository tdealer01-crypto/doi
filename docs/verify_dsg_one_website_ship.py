#!/usr/bin/env python3
"""Public, no-login current-serving replay for the 2026-11-02 DSG ONE website release.

This does NOT independently replay private GitHub/AWS CI, STS, SSM or Workroom E2E.
Exit 0 only on exact expected live public responses; nonzero on mismatch/network block.
"""
import json
import pathlib
import sys
import urllib.error
import urllib.request

SOURCE_SHA = "ccee11e6220af294da39353192622d99844de1b5"
IMAGE_DIGEST = "sha256:e375163cc279ce39f03acfbf1f5220354f21ee99e56f5dc1fad9b918f99a6320"
BASE = "https://dsg.pics"
MANIFEST = pathlib.Path(__file__).with_name("evidence") / "DSG_ONE_WEBSITE_SHIP_20261102.json"

def require(condition, reason):
    if not condition:
        raise ValueError(reason)

def get(url):
    req = urllib.request.Request(
        url, headers={"User-Agent": "DSG-Independent-Public-Website-Check/1"}
    )
    with urllib.request.urlopen(req, timeout=15) as response:
        require(response.status == 200, "HTTP_NOT_200 " + url)
        return response.read(2_000_001)

def load_json(raw, label):
    require(len(raw) <= 2_000_000, "BODY_TOO_LARGE " + label)
    return json.loads(raw)

def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    require(manifest["schema"] == "dsg-public-website-ship-evidence/v1", "BAD_MANIFEST_SCHEMA")
    require(manifest["verified_source_sha"] == SOURCE_SHA, "MANIFEST_SOURCE_MISMATCH")
    require(manifest["verified_ecr_image_digest"] == IMAGE_DIGEST, "MANIFEST_DIGEST_MISMATCH")
    require(manifest["production_base_url"] == BASE, "MANIFEST_URL_MISMATCH")
    require(manifest["scope"] == "WEBSITE_RELEASE_ONLY", "SCOPE_MISMATCH")
    require(manifest["boundaries"]["v130_release_published"] is False, "FALSE_V130_RELEASE_CLAIM")
    require(manifest["boundaries"]["workroom_claim_checkpoint_resume_proved"] is False, "FALSE_WORKROOM_CLAIM")
    require(manifest["public_replay"]["private_ci_replayed_anonymously"] is False,
            "UNSUPPORTED_PRIVATE_CI_REPLAY_CLAIM")

    status = load_json(get(BASE + "/api/agent/status"), "agent/status")
    deployment = status.get("deployment") or {}
    require(status.get("ok") is True, "PRODUCTION_STATUS_NOT_OK")
    require(status.get("version") == SOURCE_SHA, "PUBLIC_SOURCE_SHA_MISMATCH")
    require(deployment.get("imageDigest") == IMAGE_DIGEST, "PUBLIC_IMAGE_DIGEST_MISMATCH")
    require(deployment.get("buildSourceSha") == SOURCE_SHA, "PUBLIC_BUILD_SHA_MISMATCH")
    require(deployment.get("expectedSourceSha") == SOURCE_SHA, "PUBLIC_EXPECTED_SHA_MISMATCH")
    require(deployment.get("sourceBound") is True, "PUBLIC_SOURCE_NOT_BOUND")
    require(deployment.get("digestBound") is True, "PUBLIC_DIGEST_NOT_BOUND")
    print("PASS /api/agent/status exact source + digest")

    for path in manifest["public_replay"]["expected_http_200_paths"]:
        raw = get(BASE + path)
        if path == "/api/public/capabilities.json":
            data = load_json(raw, path)
            expected = manifest["public_replay"]["expected_capability_snapshot"]
            require(data.get("observedDate") == expected["observedDate"], "CAPABILITY_DATE_MISMATCH")
            require((data.get("configured") or {}).get("nodes") == expected["nodes"],
                    "CAPABILITY_NODES_MISMATCH")
            require((data.get("configured") or {}).get("routes") == expected["routes"],
                    "CAPABILITY_ROUTES_MISMATCH")
            require(data.get("e2eWholeSystem") == "NOT_VERIFIED", "CAPABILITY_E2E_SCOPE_MISMATCH")
        elif path == "/sitemap.xml":
            require(b"https://dsg.pics/capabilities" in raw, "SITEMAP_CAPABILITIES_MISSING")
        elif path == "/llms.txt":
            require(b"DSG ONE" in raw, "LLMS_DISCOVERY_MISSING")
        print("PASS", path)
    print("PUBLIC_WEBSITE_CURRENT_SERVING_REPLAY=PASS")
    print("SOURCE_SHA=" + SOURCE_SHA)
    print("IMAGE_DIGEST=" + IMAGE_DIGEST)
    print("PRIVATE_OIDC_AND_DEPLOY_ATTESTATION=NOT_PUBLICLY_REPLAYED")
    print("WORKROOM_AGENT_V1_3_E2E=NOT_VERIFIED")

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError,
            urllib.error.URLError) as exc:
        print("PUBLIC_WEBSITE_CURRENT_SERVING_REPLAY=FAIL_OR_BLOCKED", file=sys.stderr)
        print(type(exc).__name__ + ": " + str(exc), file=sys.stderr)
        sys.exit(1)
