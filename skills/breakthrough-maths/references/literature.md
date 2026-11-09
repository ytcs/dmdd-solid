# Open-access literature

Search to **recombine lemmas and techniques**. Do not search for "the proof of this conjecture." Do not search in order to report that a problem is open.

Always fetch full text before citing a result. Abstracts, zbMATH blurbs, and LLM memories of theorems are not substitutes for the paper.

Run searches with `scripts/lit.py` from this skill directory. Prefer that script over hand-rolled URLs so queries stay consistent.

## Query style

Write several queries, not one:

- objects and formulae (`Weil explicit formula`, `numerical range 2-spectral set`, `cycle double cover cubic 8-flow`)
- named inequalities and test functions
- MSC / arXiv category plus a phrase (`cat:math.NT AND pair correlation`)
- the **adjacent** problem (a bound, a special case, a dual picture), not the million-dollar name
- author+year of a paper you intend to combine with something later

For recombination: take the conclusion of paper A as a query into papers B that never cite A.

## Primary sources

### arXiv (default corpus)

- Script: `python scripts/lit.py arxiv "pair correlation zeta" --cat math.NT`
- **Use 2–4 terms.** A bare query is restricted to title+abstract and **every term is ANDed**, so a
  long query returns nothing *mechanically*. The script widens once and labels the result when that
  happens; heed the label. **An empty arXiv result is never evidence that the literature is empty** —
  and pre-2000 work is largely off arXiv, so a `n = 0` there says nothing about 1974 or 1992.
  Pass `--raw` to send the query verbatim.
- API: `https://export.arxiv.org/api/query?search_query=...&start=0&max_results=25`
  - Prefixes: `ti:`, `au:`, `abs:`, `cat:`, `all:`. Boolean: `AND`, `OR`, `ANDNOT`, parentheses.
  - Categories that matter: `math.NT`, `math.CO`, `math.GR`, `math.AG`, `math.FA`, `math.CA`, `math.DS`, `math.PR`, `math.OA`, `math.GT`, `math.RT`, `cs.CC`, `cs.IT`.
- HTML (readable, prefer this): `https://arxiv.org/html/<id>`
- PDF: `https://arxiv.org/pdf/<id>`
- Source tarball: `https://arxiv.org/e-print/<id>`
- Fetch: `python scripts/lit.py fetch 2306.04799`

Read the HTML or TeX, not just the abstract. For recombination you need the hypotheses of the lemmas.

### TheoremSearch (statement-level)

9M+ theorem/lemma/proposition statements from arXiv, Stacks Project, ProofWiki, and other corpora. This is how you search *for a lemma* rather than for a paper.

- Script: `python scripts/lit.py theorems "rank of a quadratic form from first and second moments"`
- REST: `POST https://api.theoremsearch.com/search` with JSON `{"query": "...", "n_results": 15, "tags": ["math.NT"]}`
- Graph of a paper: `GET https://api.theoremsearch.com/graph/paper?external_id=2306.04799`
- Semantic graph: `GET https://api.theoremsearch.com/graph/embedding?query=...&n_results=10`
- MCP (if the harness can register it): `https://api.theoremsearch.com/mcp`, tool `theorem_search`

Use TheoremSearch to find an existing lemma that already does the step you were about to reinvent, and to find two lemmas that have never been cited together.

### zbMATH Open

Reviews, MSC, and precise titles — still the best way to learn what a paper *actually proved*. The HTML UI is Cloudflare-gated from many datacenters; use the REST API.

- Script: `python scripts/lit.py zbmath "any:pair correlation" --msc 11M26`
- REST: `https://api.zbmath.org/v1/document/_search?search_string=...`
- Fields in `search_string`: `ti:`, `au:`, `py:`, `cc:` (MSC), `ab:`, `any:`
- UI (often 403 from bots): `https://zbmath.org/?q=<query>`

### OpenAlex, Crossref, Semantic Scholar (discovery, citation graph)

- Script: `python scripts/lit.py works "Montgomery pair correlation unconditional"`
- OpenAlex: `https://api.openalex.org/works?search=...&per-page=25` (mailto in User-Agent; this is the reliable default)
- Crossref: `https://api.crossref.org/works?query=...&rows=25`
- Semantic Scholar: optional. Unauthenticated search 429s quickly. Set `SEMANTIC_SCHOLAR_API_KEY` if you have one. OpenAlex already covers the citation-graph job.
- Unpaywall (OA PDF from DOI): `python scripts/lit.py unpaywall 10.1038/nature12373`

Use these to walk **references of a key paper** and **later papers that cite it**, which is the usual place uncombined tools hide.

## Theses (tribal knowledge)

Doctoral and master's theses routinely contain: attempted proofs that died, lemmas the advisor judged "not enough for a paper," computational tables, and folklore. Journals suppress this. Search them on purpose.

| Source | What | How |
| --- | --- | --- |
| OpenAlex `type:dissertation` | Global dissertations, OA URLs when present | via `python scripts/lit.py theses "..."` |
| HAL / TEL | French theses, often full PDF | same command; API `https://api.archives-ouvertes.fr/search/tel/` |
| OATD | Global OA theses UI | `https://oatd.org/oatd/search?q=...` (Cloudflare-blocked from many datacenters; do not depend on scraping it) |
| NDLTD | Union catalog landing page | `https://ndltd.org/` (`search.ndltd.org` is often 503) |
| EThOS | UK theses (metadata; PDF often OA) | `https://ethos.bl.uk/` |
| Networked Digital Library / university DSpace, ePrints, Hyrax | Institutional | Search the university of the specialist whose papers you are combining |
| Harvard DASH | Harvard theses | `https://dash.harvard.edu/search?q=...` |
| MIT DSpace, Princeton Dataspace, Stanford SDR, Berkeley eScholarship | US institutional theses | Site search `thesis <topic>` |
| DiVA, dissertations.se | Nordic | `https://www.diva-portal.org/` (DiVA often times out from datacenter IPs) |
| Dart-Europe | European theses | `https://www.dart-europe.org/` (if reachable; else OATD) |

When you find a thesis, read the "failed attempts" and appendix chapters, not only the main theorem.

## Working papers

| Source | What | How |
| --- | --- | --- |
| SSRN | Working papers, including math-adjacent and "too rough for a journal" | `python scripts/lit.py ssrn "cycle double cover"` (Crossref prefix `10.2139`; SSRN HTML/API are gated) |
| arXiv already covers most math | Prefer arXiv for math; use SSRN when the topic sits against econ/CS/applied | |
| RePEc / IDEAS | Economics working papers with math content | `https://ideas.repec.org/` |

## Other OA corpora worth a pass

- **EuDML** / **NUMDAM** / **Gallica** / **GDZ** — older European journals; classical papers here are often the ones nobody has combined with recent arXiv work. EuDML has a working search (`https://eudml.org/search?q=...`). NUMDAM's search query string returns 400; start from `https://www.numdam.org/`.
- **Project Euclid** (open subset), **MSP**, **EMS Press** open issues.
- **Stacks Project**, **Kerodon**, **nLab**, **Clowder** — living references; good for definitions, not for priority.
- **openai/math** (`https://github.com/openai/math`) — AI-produced manuscripts, part Lean-formalized. A source of lemmas; check `history.md` for withdrawals and `lean/formalization.yaml` for formal status, and never cite an unformalized manuscript as a theorem.
- **MathOverflow** — for "has anyone tried combining A with B?" and for pointers to theses. Not a proof.
- **LMFDB**, **OEIS**, **House of Graphs**, **FindStat** — when the object is concrete.

## Novelty review (mandatory before claiming a theorem)

1. Run `theorems` and `arxiv` queries for the **statement you proved**, not the original conjecture name.
2. Fetch the 20–50 nearest papers and actually open them.
3. Check theses of the authors in the citation neighborhood.
4. If a paper already contains the argument, you do not have a theorem. If it contains a lemma you used without knowing, **cite it** and keep the recombination claim if that is the actual contribution.
5. An independent re-prover agent then rebuilds the argument from the cited lemmas only.

## Fetching full text

Order:

1. arXiv HTML / PDF / e-print
2. `openAccessPdf` from Semantic Scholar or Unpaywall
3. NUMDAM / EuDML / HAL
4. Author homepage / institutional repository
5. Stop. Do not bypass paywalls.

Convert PDF only when HTML/TeX is missing. Prefer TeX source for equations you will re-check.
