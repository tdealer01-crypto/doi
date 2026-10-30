# Public agent access — 2026-10-30

**Result: PASS for the tested anonymous HTTP documentation reads and Firecrawl discovery flow.**
**Scope:** public evidence access, not independent Production execution or original private-attestation replay.

## Start

Give an agent this public URL:

https://dsg-public-evidence.shipstatic.com/llms.txt

A direct request can also read:

- [Empirical evidence JSON](https://dsg-public-evidence.shipstatic.com/evidence.json)
- [Publication fingerprints](https://dsg-public-evidence.shipstatic.com/publication.json)
- [Agent resource index](https://dsg-public-evidence.shipstatic.com/agent-index.json)
- [Markdown overview](https://dsg-public-evidence.shipstatic.com/index.md)
- [Read-only OpenAPI](https://dsg-public-evidence.shipstatic.com/openapi.json)
- [Reproduction protocol](https://dsg-public-evidence.shipstatic.com/reproduction.md)
- [Archive verification command](https://dsg-public-evidence.shipstatic.com/verify-archive.md)

No account, API key, session cookie or client-side JavaScript is required. The human page has a **สำหรับเอเจนต์ / For agents** link to the same resources.

## Observed verification

| Check | Actual result |
| --- | --- |
| Initial llms.txt and evidence.json reads | Both 404 before this change |
| Live public GET | 13/13 resources returned 200 with expected content and MIME type |
| HEAD evidence.json | 200 |
| CORS | Access-Control-Allow-Origin: * |
| Robots policy | User-agent wildcard permits evidence reads |
| Stable domain indexing header | X-Robots-Tag: index, follow; no noindex |
| Discovery | llms.txt links to empirical and publication JSON |
| Firecrawl fresh external read | llms.txt 200, followed evidence.json 200 |
| Externally returned JSON | Parsed object matches the archived public empirical evidence |
| Model and scope fields | NVIDIA model/digest preserved; independent public replay and public private-signature replay remain false |
| Browser UI | Agent entrypoint and JSON/Markdown/OpenAPI links observed on the live page |

Verified HTTP observation: `2026-10-30T07:39:30.291376+00:00`.
Deployment: `liminal-mesh-8fc6tmr.shipstatic.com`; no expiry requested.
[Machine-readable request results and response hashes](evidence/PUBLIC_AGENT_ACCESS_20261030.json).

The deployment's own temporary hostname is noindex by platform policy. The named public domain is the canonical agent entrypoint. Use the stable URLs above.

One other retrieval client (Search service open) returned an unavailable-for-URL result. The successful direct HTTP and Firecrawl reads do not claim compatibility with every agent or that a search engine has already indexed the site.

## Repeat the public metadata read

```bash
python3 - <<'PY_AGENT'
import json, urllib.request, urllib.robotparser

base = "https://dsg-public-evidence.shipstatic.com"
def read(path):
    request = urllib.request.Request(
        base + path,
        headers={"User-Agent": "Public-Evidence-Agent-Check/1", "Origin": "https://example.org"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        assert response.status == 200
        assert response.headers.get("Access-Control-Allow-Origin") == "*"
        assert "noindex" not in response.headers.get("X-Robots-Tag", "").lower()
        return response.read()

index = read("/llms.txt").decode()
assert base + "/evidence.json" in index
evidence = json.loads(read("/evidence.json"))
publication = json.loads(read("/publication.json"))
nvidia = evidence["live_nvidia_workroom_20261030"]
assert nvidia["model"] == "nvidia/nemotron-3.5-lightning-30b-a3b"
assert nvidia["image_digest"] == "sha256:94115f03476e93a8dbce43cbdcf37951c4a148d3c998ae87683c7185cd7a8f10"
assert nvidia["signature"]["publicly_replayable"] is False
assert nvidia["independent_public_replay"] is False
assert publication["version_doi"] == "10.5281/zenodo.23796173"
assert publication["independent_public_production_e2e"] is False
robots = urllib.robotparser.RobotFileParser()
robots.parse(read("/robots.txt").decode().splitlines())
assert robots.can_fetch("Public-Evidence-Agent", base + "/evidence.json")
print("PUBLIC_AGENT_METADATA_READ_PASS")
PY_AGENT
```

This command checks public data delivery and interpretation fields. It does not run the private runtime or turn its internal acceptance into an independently reproduced E2E result.

## Publication lineage

The existing v1.2.0 Zenodo archive and release tag remain immutable. New static access files are a post-publication distribution layer. The empirical JSON is served from the existing public archived snapshot; publication JSON is a scoped view pinned to public source commit `d26821e0e72830d187f281a02f13faef6f71fef5`.

The original private Ed25519 CI payload remains private. Public material retains its existing CC BY-NC-ND 4.0 license.

## Implementation references

- [ShipStatic response-header configuration](https://docs.shipstatic.com/ship-json)
- [llms.txt proposal and Markdown discovery links](https://llmstxt.org/)
