"""WP8-U database pull (network; run once). Writes small extracts to code/WP8-U/data/.

Sources (all public, no key):
  JARVIS-DFT dft_3d, figshare file 64391379 (jdft_3d-9-24-2025.json), path given as argv[1] (downloaded to scratchpad).
  OPTIMADE: Materials Project https://optimade.materialsproject.org/v1 ; Alexandria PBE https://alexandria.icams.rub.de/pbe/v1
  NIST Atomic Weights and Isotopic Compositions (ascii2) https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl
  IAEA LiveChart ground states (ENSDF) https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all
Usage: python3 -I fetch_db.py /path/to/jdft_3d-9-24-2025.json
"""
import csv, io, json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from materials import MATERIALS, ELEMENTS  # noqa: E402

OUT = os.path.join(HERE, "data")
os.makedirs(OUT, exist_ok=True)
UA = {"User-Agent": "breakthrough-maths WP8-U data compilation (mailto via repo owner)"}


def get(url, tries=3):
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # pragma: no cover
            if k == tries - 1:
                raise
            time.sleep(3)


JKEYS = ["jid", "formula", "spg_symbol", "spg_number", "nat", "ehull", "optb88vdw_bandgap", "mbj_bandgap", "hse_gap",
         "epsx", "epsy", "epsz", "mepsx", "mepsy", "mepsz", "dfpt_piezo_max_dielectric",
         "dfpt_piezo_max_dielectric_electronic", "dfpt_piezo_max_dielectric_ionic", "max_ir_mode", "min_ir_mode",
         "bulk_modulus_kv", "shear_modulus_gv", "density", "avg_elec_mass", "avg_hole_mass", "magmom_outcar",
         "Tc_supercon", "modes", "reference", "func", "atoms"]


def jarvis(path):
    want = {v[2] for v in MATERIALS.values() if v[2]}
    d = json.load(open(path))
    out = {}
    for x in d:
        if x["jid"] in want:
            y = {k: x.get(k) for k in JKEYS}
            at = y.pop("atoms")
            y["lattice_mat"] = at["lattice_mat"]
            y["elements"] = at["elements"]
            out[x["jid"]] = y
    missing = want - set(out)
    assert not missing, missing
    json.dump(out, open(os.path.join(OUT, "jarvis_extract.json"), "w"), indent=0)
    print("JARVIS", len(out))


def optimade_mp():
    out = {}
    for key, v in MATERIALS.items():
        mp = v[3]
        if not mp:
            continue
        url = ("https://optimade.materialsproject.org/v1/structures/" + mp +
               "?response_fields=lattice_vectors,species_at_sites,nsites,chemical_formula_reduced,_mp_stability")
        a = json.loads(get(url))["data"]["attributes"]
        st = a.get("_mp_stability") or {}
        eh = {k: st[k].get("energy_above_hull") for k in st}
        out[mp] = {"lattice_vectors": a["lattice_vectors"], "species_at_sites": a["species_at_sites"],
                   "nsites": a["nsites"], "formula": a["chemical_formula_reduced"], "e_above_hull": eh}
        time.sleep(0.3)
    json.dump(out, open(os.path.join(OUT, "optimade_mp.json"), "w"), indent=0)
    print("MP OPTIMADE", len(out))


def optimade_alex():
    out = {}
    for key, v in MATERIALS.items():
        if not v[4]:
            continue
        f, spg = v[4]
        flt = urllib.parse.quote(f'chemical_formula_reduced="{f}"')
        url = ("https://alexandria.icams.rub.de/pbe/v1/structures?filter=" + flt + "&page_limit=50&response_fields="
               "id,nsites,_alexandria_space_group,_alexandria_band_gap,_alexandria_band_gap_direct,"
               "_alexandria_hull_distance,_alexandria_magnetization,_alexandria_xc_functional")
        rows = [dict(id=r["id"], **r["attributes"]) for r in json.loads(get(url))["data"]]
        rows = [r for r in rows if r.get("_alexandria_space_group") == spg]
        rows.sort(key=lambda r: (r.get("_alexandria_hull_distance") is None, r.get("_alexandria_hull_distance") or 0))
        out[key] = rows[:3]
    json.dump(out, open(os.path.join(OUT, "optimade_alex.json"), "w"), indent=0)
    print("Alexandria", {k: [r["id"] for r in v] for k, v in out.items()})


def nist():
    t = get("https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=&ascii=ascii2&isotype=some")
    t = re.sub(r"<[^>]+>", "", t).replace("&nbsp;", " ")
    out = {}
    for blk in t.split("Atomic Number = ")[1:]:
        kv = dict(re.findall(r"^\s*([A-Za-z ]+?) = (.*)$", "Atomic Number = " + blk, re.M))
        sym = kv.get("Atomic Symbol", "").strip()
        if sym not in ELEMENTS:
            continue
        comp = kv.get("Isotopic Composition", "").strip()
        if not comp:
            continue
        num = lambda s: float(re.sub(r"\(.*?\)|#", "", s).strip("[] ").split(",")[0]) if s.strip() else None
        sw = kv.get("Standard Atomic Weight", "").strip()
        out.setdefault(sym, {"Z": int(kv["Atomic Number"]), "std_weight": sw, "isotopes": []})
        out[sym]["isotopes"].append({"A": int(kv["Mass Number"]), "mass": num(kv["Relative Atomic Mass"]),
                                     "abundance": num(comp)})
    assert set(out) == set(ELEMENTS), set(ELEMENTS) - set(out)
    json.dump(out, open(os.path.join(OUT, "nist_isotopes.json"), "w"), indent=0)
    print("NIST", len(out))


def iaea():
    t = get("https://nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all")
    out = []
    for r in csv.DictReader(io.StringIO(t)):
        if r["symbol"] in ELEMENTS and (r["abundance"] or r["symbol"] == "H"):
            A = int(r["z"]) + int(r["n"])
            out.append({"sym": r["symbol"], "A": A, "abundance_pct": r["abundance"], "jp": r["jp"],
                        "half_life": r["half_life"], "operator_hl": r["operator_hl"], "unit_hl": r["unit_hl"], "half_life_sec": r["half_life_sec"],
                        "decay_1": r["decay_1"]})
    # cosmogenic/primordial reference nuclides that have no natural abundance but are tabulated for notes
    json.dump({"source": "IAEA LiveChart ground_states (ENSDF)", "rows": out},
              open(os.path.join(OUT, "iaea_gs.json"), "w"), indent=0)
    print("IAEA", len(out))


if __name__ == "__main__":
    if sys.argv[1:] == ["--iaea-only"]:
        iaea(); sys.exit(0)
    jarvis(sys.argv[1])
    optimade_mp()
    optimade_alex()
    nist()
    iaea()
