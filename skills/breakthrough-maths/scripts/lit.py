#!/usr/bin/env python3
"""Open-access math literature search.

Sources that return JSON: arXiv, TheoremSearch, OpenAlex, Crossref,
zbMATH Open, HAL/TEL, Unpaywall. Semantic Scholar is optional (API key
or unauthenticated with retries). SSRN is queried via Crossref (prefix
10.2139) because SSRN's HTML/API is gated.

No required API keys. Be polite: identifiable UA, retries on 429.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

UA = (
    "breakthrough-maths/0.1 "
    "(https://github.com/ytcs/breakthrough-maths; mailto:stevenytc@gmail.com)"
)
ARXIV_API = "https://export.arxiv.org/api/query"
THEOREM_SEARCH = "https://api.theoremsearch.com/search"
THEOREM_GRAPH_PAPER = "https://api.theoremsearch.com/graph/paper"
OPENALEX = "https://api.openalex.org/works"
CROSSREF = "https://api.crossref.org/works"
S2 = "https://api.semanticscholar.org/graph/v1/paper/search"
ZBMATH = "https://api.zbmath.org/v1/document/_search"
HAL_TEL = "https://api.archives-ouvertes.fr/search/tel/"
UNPAYWALL = "https://api.unpaywall.org/v2/"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"
ARXIV_ID_RE = re.compile(
    r"(?:arXiv:|https?://arxiv\.org/(?:abs|pdf|html|e-print)/)?"
    r"((?:[a-z\-]+/\d{7}|\d{4}\.\d{4,5})(?:v\d+)?)",
    re.I,
)


def _dump(obj) -> None:
    json.dump(obj, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


# Combined `search` sets this so one rate-limited source cannot stall the run.
FAST = False


def _request(
    url: str,
    *,
    data: bytes | None = None,
    timeout: int = 45,
    extra_headers: dict | None = None,
    retries: int = 3,
) -> bytes:
    headers = {"User-Agent": UA, "Accept": "application/json, application/atom+xml, */*"}
    if extra_headers:
        headers.update(extra_headers)
    if data is not None:
        headers.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data is not None else "GET")
    last_err: Exception | None = None
    if FAST:
        retries, timeout = min(retries, 1), min(timeout, 20)
    attempts = max(1, retries + 1)
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code == 429 and attempt < attempts - 1:
                retry = e.headers.get("Retry-After")
                try:
                    wait = float(retry) if retry else 1.5 * (2**attempt)
                except ValueError:
                    wait = 1.5 * (2**attempt)
                time.sleep(min(wait, 3.0 if FAST else 12.0))
                continue
            raise
        except urllib.error.URLError as e:
            last_err = e
            if attempt < attempts - 1:
                time.sleep(1.0 * (attempt + 1))
                continue
            raise
    raise last_err or RuntimeError("request failed")


def _get(url: str, timeout: int = 45, extra_headers: dict | None = None, retries: int = 3) -> bytes:
    return _request(url, timeout=timeout, extra_headers=extra_headers, retries=retries)


def _post_json(url: str, payload: dict, timeout: int = 45) -> bytes:
    return _request(url, data=json.dumps(payload).encode("utf-8"), timeout=timeout)


def _get_json(url: str, timeout: int = 45, extra_headers: dict | None = None, retries: int = 3):
    return json.loads(_get(url, timeout=timeout, extra_headers=extra_headers, retries=retries).decode("utf-8"))


def normalize_arxiv_id(raw: str, *, strip_version: bool = False) -> str:
    m = ARXIV_ID_RE.search(raw.strip())
    aid = m.group(1) if m else raw.strip()
    if strip_version:
        aid = re.sub(r"v\d+$", "", aid)
    return aid


ARXIV_FIELD_RE = re.compile(r"\b(ti|abs|au|cat|all|co|jr|rn|id):", re.I)
ARXIV_BOOL_RE = re.compile(r"\b(AND|OR|ANDNOT)\b")


def arxiv_query(q: str) -> str:
    """Field-qualify a bare query.

    arXiv's API matches a bare term across ALL fields, authors included, so
    `Skorokhod embedding local time` ranks a gr-qc paper by an author named
    "Time" first. Restrict a bare query to title and abstract; leave a query
    that already names a field or uses a boolean operator exactly as written.
    """
    if ARXIV_FIELD_RE.search(q) or ARXIV_BOOL_RE.search(q):
        return q
    terms = [t for t in q.split() if t]
    if not terms:
        return q
    return " AND ".join(f'(ti:"{t}" OR abs:"{t}")' for t in terms)


def cmd_arxiv(args: argparse.Namespace) -> int:
    raw = getattr(args, "raw", False)
    q = args.query if raw else arxiv_query(args.query)
    root, q_used, widened = _arxiv_fetch(args, q), q, False
    # Every term is ANDed, so a long bare query can return nothing mechanically
    # rather than because the literature is empty. Widen once and say so: an
    # empty result is otherwise read as "no prior art exists".
    if not raw and not root.findall(f"{ATOM}entry") and q != args.query:
        widened = True
        q_used = args.query
        root = _arxiv_fetch(args, q_used)
    papers = []
    for entry in root.findall(f"{ATOM}entry"):
        arxiv_id = (entry.findtext(f"{ATOM}id") or "").rsplit("/", 1)[-1]
        cats = [c.attrib.get("term", "") for c in entry.findall(f"{ARXIV_NS}primary_category")]
        cats += [c.attrib.get("term", "") for c in entry.findall(f"{ATOM}category")]
        papers.append(
            {
                "id": arxiv_id,
                "title": " ".join((entry.findtext(f"{ATOM}title") or "").split()),
                "published": (entry.findtext(f"{ATOM}published") or "")[:10],
                "authors": [a.findtext(f"{ATOM}name") for a in entry.findall(f"{ATOM}author")],
                "categories": list(dict.fromkeys(cats)),
                "summary": " ".join((entry.findtext(f"{ATOM}summary") or "").split())[:500],
                "abs": f"https://arxiv.org/abs/{arxiv_id}",
                "html": f"https://arxiv.org/html/{arxiv_id}",
                "pdf": f"https://arxiv.org/pdf/{arxiv_id}",
                "source": f"https://arxiv.org/e-print/{arxiv_id}",
            }
        )
    out = {"query": q_used, "n": len(papers), "papers": papers}
    if widened:
        out["widened_from"] = q
        out["note"] = (
            "The title+abstract query returned nothing, so this is the unrestricted "
            "query. A field-qualified query ANDs every term: an empty result there is "
            "not evidence that the literature is empty. Shorten the query to 2-4 terms."
        )
    elif not papers:
        out["note"] = "No hits. Try 2-4 terms, or a different vocabulary; not evidence of absence."
    _dump(out)
    return 0


def _arxiv_fetch(args: argparse.Namespace, q: str) -> "ET.Element":
    if args.cat:
        q = f"({q}) AND cat:{args.cat}"
    params = {
        "search_query": q,
        "start": str(args.start),
        "max_results": str(args.n),
        "sortBy": args.sort,
        "sortOrder": "descending",
    }
    return ET.fromstring(_get(ARXIV_API + "?" + urllib.parse.urlencode(params)))


def cmd_theorems(args: argparse.Namespace) -> int:
    payload = {"query": args.query, "n_results": args.n}
    if args.cat:
        payload["tags"] = [args.cat]
    if args.source:
        payload["sources"] = [args.source]
    _dump(json.loads(_post_json(THEOREM_SEARCH, payload).decode("utf-8")))
    return 0


def _slim_openalex(payload: dict) -> dict:
    results = []
    for w in payload.get("results") or []:
        oa = w.get("open_access") or {}
        results.append(
            {
                "id": w.get("id"),
                "title": w.get("display_name"),
                "year": w.get("publication_year"),
                "type": w.get("type"),
                "doi": w.get("doi"),
                "cited_by_count": w.get("cited_by_count"),
                "oa_url": oa.get("oa_url"),
                "is_oa": oa.get("is_oa"),
            }
        )
    meta = payload.get("meta") or {}
    return {"count": meta.get("count"), "results": results}


def _slim_crossref(payload: dict) -> dict:
    msg = payload.get("message") or {}
    items = []
    for it in msg.get("items") or []:
        title = it.get("title") or [""]
        items.append(
            {
                "doi": it.get("DOI"),
                "title": title[0] if title else None,
                "year": ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0],
                "type": it.get("type"),
                "url": it.get("URL"),
                "container": (it.get("container-title") or [None])[0],
                "is_oa": (it.get("license") or None) is not None,
            }
        )
    return {"count": msg.get("total-results"), "results": items}


def _slim_s2(payload: dict) -> dict:
    results = []
    for p in payload.get("data") or []:
        ext = p.get("externalIds") or {}
        oa = p.get("openAccessPdf") or {}
        results.append(
            {
                "paperId": p.get("paperId"),
                "title": p.get("title"),
                "year": p.get("year"),
                "citationCount": p.get("citationCount"),
                "url": p.get("url"),
                "arxiv": ext.get("ArXiv"),
                "doi": ext.get("DOI"),
                "oa_pdf": oa.get("url"),
                "abstract": (p.get("abstract") or "")[:400] or None,
            }
        )
    return {"count": payload.get("total"), "results": results}


def cmd_works(args: argparse.Namespace) -> int:
    out = {"openalex": None, "crossref": None, "semantic_scholar": None, "errors": []}
    oa_url = OPENALEX + "?" + urllib.parse.urlencode(
        {"search": args.query, "per-page": args.n, "sort": "cited_by_count:desc"}
    )
    try:
        out["openalex"] = _slim_openalex(_get_json(oa_url))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        out["errors"].append(f"openalex: {e}")
    time.sleep(0.3)
    cr_url = CROSSREF + "?" + urllib.parse.urlencode({"query": args.query, "rows": args.n})
    try:
        out["crossref"] = _slim_crossref(_get_json(cr_url))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        out["errors"].append(f"crossref: {e}")
    time.sleep(0.3)
    s2_url = S2 + "?" + urllib.parse.urlencode(
        {
            "query": args.query,
            "limit": args.n,
            "fields": "title,year,externalIds,openAccessPdf,citationCount,abstract,url",
        }
    )
    s2_headers = {}
    key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY") or os.environ.get("S2_API_KEY")
    if key:
        s2_headers["x-api-key"] = key
    try:
        # Unauthenticated S2 429s immediately; one retry then fall back to OpenAlex/Crossref.
        out["semantic_scholar"] = _slim_s2(
            _get_json(s2_url, extra_headers=s2_headers or None, retries=1)
        )
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        out["errors"].append(f"semantic_scholar: {e}")
    _dump(out)
    # S2 unauthenticated 429 is common; OpenAlex + Crossref are enough.
    if out["openalex"] is None and out["crossref"] is None:
        return 2
    return 0


def _slim_hal(payload: dict) -> dict:
    resp = payload.get("response") or {}
    docs = []
    for d in resp.get("docs") or []:
        title = d.get("title_s") or []
        authors = d.get("authFullName_s") or []
        docs.append(
            {
                "title": title[0] if title else None,
                "authors": authors,
                "year": d.get("producedDateY_i"),
                "uri": d.get("uri_s"),
                "doi": d.get("doiId_s"),
                "pdf": d.get("fileMain_s"),
            }
        )
    return {"count": resp.get("numFound"), "results": docs}


def _slim_dissertations(payload: dict) -> dict:
    return _slim_openalex(payload)


def cmd_theses(args: argparse.Namespace) -> int:
    q = args.query
    hal_url = HAL_TEL + "?" + urllib.parse.urlencode(
        {
            "q": q,
            "wt": "json",
            "rows": args.n,
            "fl": "title_s,authFullName_s,producedDateY_i,uri_s,doiId_s,fileMain_s",
        }
    )
    oa_url = OPENALEX + "?" + urllib.parse.urlencode(
        {"search": q, "filter": "type:dissertation", "per-page": args.n}
    )
    out = {
        "hal_tel": None,
        "openalex_dissertations": None,
        "search_pages": {
            "oatd": "https://oatd.org/oatd/search?" + urllib.parse.urlencode({"q": q}),
            "ndltd": "https://ndltd.org/",
            "harvard_dash": "https://dash.harvard.edu/search?" + urllib.parse.urlencode({"q": q}),
            "ethos": "https://ethos.bl.uk/",
            "eudml": "https://eudml.org/search?" + urllib.parse.urlencode({"q": q}),
        },
        "notes": [
            "OATD HTML is often Cloudflare-blocked from datacenters; use OpenAlex dissertations + HAL instead.",
            "NDLTD's search.ndltd.org is frequently 503; ndltd.org is the landing page.",
        ],
        "errors": [],
    }
    try:
        out["hal_tel"] = _slim_hal(_get_json(hal_url))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        out["errors"].append(f"hal_tel: {e}")
    time.sleep(0.3)
    try:
        out["openalex_dissertations"] = _slim_dissertations(_get_json(oa_url))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        out["errors"].append(f"openalex_dissertations: {e}")
    _dump(out)
    if out["hal_tel"] is None and out["openalex_dissertations"] is None:
        return 2
    return 0


def cmd_ssrn(args: argparse.Namespace) -> int:
    q = args.query
    cr_url = CROSSREF + "?" + urllib.parse.urlencode(
        {"query": q, "filter": "prefix:10.2139", "rows": args.n}
    )
    out = {
        "crossref_ssrn": None,
        "search_pages": {
            "ssrn_home": "https://www.ssrn.com/",
            "repec": "https://ideas.repec.org/cgi-bin/htsearch?" + urllib.parse.urlencode({"q": q}),
            "eudml": "https://eudml.org/search?" + urllib.parse.urlencode({"q": q}),
            "numdam": "https://www.numdam.org/",
            "zbmath_ui": "https://zbmath.org/?q=" + urllib.parse.quote(q),
        },
        "notes": [
            "SSRN HTML and api.ssrn.com are gated (Cloudflare / 401). Crossref prefix 10.2139 is the unauthenticated JSON path.",
            "zbMATH HTML is Cloudflare-gated; use the `zbmath` subcommand (REST API).",
            "NUMDAM has no working public search query string; browse from the homepage or use EuDML.",
        ],
        "errors": [],
    }
    try:
        out["crossref_ssrn"] = _slim_crossref(_get_json(cr_url))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        out["errors"].append(f"crossref_ssrn: {e}")
    _dump(out)
    return 0 if out["crossref_ssrn"] is not None else 2


def cmd_zbmath(args: argparse.Namespace) -> int:
    q = args.query
    if args.msc:
        q = f"({q}) AND cc:{args.msc}"
    url = ZBMATH + "?" + urllib.parse.urlencode({"search_string": q, "results_per_page": args.n})
    try:
        raw = _get_json(url)
    except urllib.error.HTTPError as e:
        if e.code != 404:  # zbMATH answers 404, not an empty list, when nothing matches
            raise
        raw = {"result": []}
    docs = []
    for x in raw.get("result") or []:
        title = x.get("title") or {}
        if isinstance(title, dict):
            title = title.get("title") or title.get("original")
        authors = []
        contrib = (x.get("contributors") or {}).get("authors") or []
        for a in contrib:
            if isinstance(a, dict) and a.get("name"):
                authors.append(a["name"])
        links = x.get("links") or []
        doi = next((L.get("identifier") for L in links if L.get("type") == "doi"), None)
        docs.append(
            {
                "id": x.get("id"),
                "zbmath_url": x.get("zbmath_url"),
                "title": title,
                "year": x.get("year"),
                "authors": authors,
                "msc": x.get("msc"),
                "doi": doi,
                "document_type": x.get("document_type"),
            }
        )
    _dump({"query": q, "n": len(docs), "status": raw.get("status"), "documents": docs})
    return 0


def cmd_unpaywall(args: argparse.Namespace) -> int:
    doi = args.doi.replace("https://doi.org/", "").replace("http://doi.org/", "").strip()
    email = os.environ.get("UNPAYWALL_EMAIL", "stevenytc@gmail.com")
    url = UNPAYWALL + urllib.parse.quote(doi) + "?" + urllib.parse.urlencode({"email": email})
    raw = _get_json(url)
    loc = raw.get("best_oa_location") or {}
    _dump(
        {
            "doi": raw.get("doi"),
            "title": raw.get("title"),
            "year": raw.get("year"),
            "is_oa": raw.get("is_oa"),
            "oa_status": raw.get("oa_status"),
            "oa_url": loc.get("url_for_pdf") or loc.get("url"),
            "version": loc.get("version"),
            "host": loc.get("host_type"),
        }
    )
    return 0


def cmd_fetch(args: argparse.Namespace) -> int:
    arxiv_id = normalize_arxiv_id(args.arxiv_id)
    bare = normalize_arxiv_id(arxiv_id, strip_version=True)
    dest = Path(args.out or ".")
    dest.mkdir(parents=True, exist_ok=True)
    saved = []
    errors = []
    stem = arxiv_id.replace("/", "_")
    for kind, url in (
        ("html", f"https://arxiv.org/html/{arxiv_id}"),
        ("pdf", f"https://arxiv.org/pdf/{arxiv_id}"),
    ):
        target = dest / f"{stem}.{kind}"
        try:
            data = _get(url, timeout=90)
            target.write_bytes(data)
            saved.append({"path": str(target), "bytes": len(data)})
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            errors.append(f"{kind}: {e}")
        time.sleep(0.4)
    try:
        graph = _get_json(THEOREM_GRAPH_PAPER + "?" + urllib.parse.urlencode({"external_id": bare}))
        gpath = dest / f"{stem}.graph.json"
        gpath.write_text(json.dumps(graph, indent=2), encoding="utf-8")
        n_stmt = len(graph.get("statements") or [])
        saved.append({"path": str(gpath), "bytes": gpath.stat().st_size, "statements": n_stmt})
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        errors.append(f"theorem_graph: {e}")
    _dump({"id": arxiv_id, "bare_id": bare, "saved": saved, "errors": errors})
    return 0 if saved else 2


def cmd_search(args: argparse.Namespace) -> int:
    """Combined run: capture each subcommand's JSON by calling the functions with a buffer."""
    chunks = {}

    def capture(fn, ns):
        buf = []
        g = globals()
        prev = g["_dump"]
        g["_dump"] = lambda obj: buf.append(obj)
        try:
            rc = fn(ns)
        except Exception as e:  # one failing source must not sink the combined run
            print(f"  source failed: {type(e).__name__}: {e}", file=sys.stderr)
            return 1, {"error": f"{type(e).__name__}: {e}"}
        finally:
            g["_dump"] = prev
        return rc, (buf[-1] if buf else None)

    global FAST
    FAST = True

    ns = argparse.Namespace(
        query=args.query, cat=args.cat, n=args.n, start=0, sort="relevance", source=None, msc=None
    )
    print("=== arXiv ===", file=sys.stderr)
    _, chunks["arxiv"] = capture(cmd_arxiv, ns)
    time.sleep(0.4)
    print("=== theorems ===", file=sys.stderr)
    _, chunks["theorems"] = capture(cmd_theorems, ns)
    time.sleep(0.4)
    print("=== works ===", file=sys.stderr)
    _, chunks["works"] = capture(cmd_works, ns)
    time.sleep(0.4)
    print("=== theses ===", file=sys.stderr)
    _, chunks["theses"] = capture(cmd_theses, ns)
    time.sleep(0.4)
    print("=== ssrn/crossref + zbmath ===", file=sys.stderr)
    _, chunks["ssrn"] = capture(cmd_ssrn, ns)
    time.sleep(0.4)
    _, chunks["zbmath"] = capture(cmd_zbmath, ns)
    _dump(chunks)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_q(sp):
        sp.add_argument("query")
        sp.add_argument("-n", type=int, default=15)
        sp.add_argument("--cat", default=None, help="arXiv category or TheoremSearch tag, e.g. math.NT")

    a = sub.add_parser("arxiv", help="Search arXiv")
    add_q(a)
    a.add_argument("--start", type=int, default=0)
    a.add_argument("--sort", default="relevance", choices=["relevance", "lastUpdatedDate", "submittedDate"])
    a.add_argument(
        "--raw",
        action="store_true",
        help="pass the query to arXiv verbatim instead of restricting bare terms to title+abstract",
    )
    a.set_defaults(func=cmd_arxiv)

    t = sub.add_parser("theorems", help="Semantic theorem search (TheoremSearch)")
    add_q(t)
    t.add_argument("--source", default=None, help="arXiv, Stacks Project, ProofWiki, ...")
    t.set_defaults(func=cmd_theorems)

    w = sub.add_parser("works", help="OpenAlex + Crossref + Semantic Scholar")
    add_q(w)
    w.set_defaults(func=cmd_works)

    th = sub.add_parser("theses", help="HAL/TEL + OpenAlex dissertations")
    add_q(th)
    th.set_defaults(func=cmd_theses)

    s = sub.add_parser("ssrn", help="SSRN via Crossref prefix 10.2139")
    add_q(s)
    s.set_defaults(func=cmd_ssrn)

    z = sub.add_parser("zbmath", help="zbMATH Open REST search")
    add_q(z)
    z.add_argument("--msc", default=None, help="MSC class, e.g. 11M26")
    z.set_defaults(func=cmd_zbmath)

    u = sub.add_parser("unpaywall", help="Resolve a DOI to an OA PDF via Unpaywall")
    u.add_argument("doi")
    u.set_defaults(func=cmd_unpaywall)

    f = sub.add_parser("fetch", help="Download arXiv HTML+PDF and TheoremSearch graph")
    f.add_argument("arxiv_id")
    f.add_argument("-o", "--out", default="campaign/papers")
    f.set_defaults(func=cmd_fetch)

    sm = sub.add_parser("search", help="Run arxiv + theorems + works + theses + ssrn + zbmath")
    add_q(sm)
    sm.set_defaults(func=cmd_search)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} on {e.geturl()}: {e.reason}", file=sys.stderr)
        return 2
    except urllib.error.URLError as e:
        print(f"network error: {e.reason}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
