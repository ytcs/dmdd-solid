"""CW7: verify every arXiv ID cited in the three R16 files against the arXiv API (network; run once). Writes data/arxiv_verified.json."""
import json, os, re, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LIT = os.path.abspath(os.path.join(ROOT, "..", "..", "skills/breakthrough-maths/scripts/lit.py"))
ids = set()
for fn in ("returns/R16/CW7.md", "returns/R16/WP8-U-v2.md", "returns/R16/WP8-F-v2.md", "returns/R16/CW7-errata.md",
           "returns/R16/WP8-U-v3.md", "returns/R16/WP8-F-v3.md"):  # ERR-CW7: v3 files added (1704.04320 verified 2026-11-01)
    ids |= set(re.findall(r"(?<![\d.])(\d{4}\.\d{4,5})(?![\d])", open(os.path.join(ROOT, fn)).read()))
out = {}
for i in sorted(ids):
    r = subprocess.run([sys.executable, LIT, "arxiv", "id:" + i, "--raw", "-n", "1"], capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
        p = d["papers"][0]
        if p["id"].split("v")[0] == i:
            out[i] = p["title"]
    except Exception as e:
        print("FAIL", i, e)
    time.sleep(0.5)
json.dump(out, open(os.path.join(HERE, "data", "arxiv_verified.json"), "w"), indent=1, ensure_ascii=False)
print(len(ids), "cited;", len(out), "verified;", sorted(ids - set(out)))
