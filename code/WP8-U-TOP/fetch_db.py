"""WP8-U-TOP network/one-off step (run once; build_v2.py and checks.py are offline).

1. JARVIS-DFT dft_3d (release 9-24-2025, figshare file 64391379, the same dump WP8-U used) -> data/jarvis_top.json:
   elastic_tensor (Voigt, GPa), density, bulk/shear Voigt moduli, epsx/y/z, mepsx/y/z, modes, Tc_supercon, for the WP8-U
   registry plus the sensor metals Ir (JVASP-901), W (JVASP-14830 is non-ground; JVASP-79561 has no tensor) and Ti.
2. arXiv API verification of every arXiv ID cited in WP8-U-top.md / the v2 CSV -> data/arxiv_verified.json.
Usage: python3 fetch_db.py <path to jdft_3d-9-24-2025.json>
"""
import json, sys, time, urllib.request, re, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "WP8-U"))
from materials import MATERIALS
HERE = os.path.dirname(os.path.abspath(__file__))
EXTRA = {"Ir": "JVASP-901", "Ti": "JVASP-1029", "W": "JVASP-14830"}
FIELDS = ["jid", "formula", "spg_symbol", "spg_number", "density", "elastic_tensor", "bulk_modulus_kv", "shear_modulus_gv",
          "epsx", "epsy", "epsz", "mepsx", "mepsy", "mepsz", "modes", "Tc_supercon", "ehull", "reference", "crys"]
ARXIV = ["2610.16949", "2311.05011", "2311.03902", "1308.2886", "1602.08005", "1706.05818", "2506.06568", "1705.06594",
         "1704.01758", "1806.07968", "2609.20122", "2010.08926", "1807.10291", "1910.10716", "2008.08560", "2004.11499",
         "1901.07569", "1905.13744", "2004.10709", "2210.13516", "2109.04473"]

def main(path):
    d = {x["jid"]: x for x in json.load(open(path))}
    want = {k: v[2] for k, v in MATERIALS.items() if v[2]}
    want.update(EXTRA)
    out = {k: {f: d[j].get(f) for f in FIELDS} for k, j in want.items()}
    json.dump(out, open(os.path.join(HERE, "data", "jarvis_top.json"), "w"), indent=0)
    ver = {}
    for i in range(0, len(ARXIV), 10):
        ids = ",".join(ARXIV[i:i + 10])
        url = f"http://export.arxiv.org/api/query?id_list={ids}&max_results=20"
        x = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "paer-campaign/1.0"}), timeout=90).read().decode()
        for e in re.findall(r"<entry>(.*?)</entry>", x, re.S):
            aid = re.search(r"<id>http[s]?://arxiv.org/abs/([^<]+)</id>", e).group(1)
            t = re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", e, re.S).group(1)).strip()
            ver[re.sub(r"v\d+$", "", aid)] = t
        time.sleep(3)
    json.dump(ver, open(os.path.join(HERE, "data", "arxiv_verified.json"), "w"), indent=1)
    print(len(out), "materials;", len(ver), "/", len(ARXIV), "arXiv IDs verified")

if __name__ == "__main__":
    main(sys.argv[1])
