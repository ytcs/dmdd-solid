"""ERR-CW7: build returns/R16/WP8-U-table-v4.csv from returns/R16/WP8-U-table-v3.csv (same 11 columns).
Changes (each recorded in data/v4_changes.json; every changed or dropped v3 row is listed there verbatim):
 (1) column `verdict` set to the material's final verdict (the last `verdict` property row) on every row of that material;
 (2) screening keys unique: for each (material, screen_S*) the last superseding row is kept and the R13-rename row it supersedes is
     dropped (13 keys, VER-CW7 §A); every remaining screening row with "[E]" as evidence is retagged: "[E]" -> "[UNVERIFIED]", tag
     UNVERIFIED, and a PASS/FAIL resting on that evidence alone reads COND (the WP8-U one rule, WP8-U-v3 §2);
 (3) elastic tensors re-indexed: JARVIS `elastic_tensor` shear order is (xy, yz, zx), not Voigt (yz, zx, xy) (proved below by the
     hexagonal/trigonal identity C66 = (C11 - C12)/2 at JARVIS index 3); new Voigt rows with C44, C55, C66, C14; Christoffel speeds,
     the [001] transverse degeneracy check, and the heavy-mediator NR-1ph scalar c_NR1 = <sum_nu (q.e_nu)^2 / c_nu>^-1 recomputed;
 (4) flags: TeO2 / LiAlO2 rho_T DFT proxy; Pb salts 210Pb S4 condition (with the [E] activity threshold); CaWO4 3H "inferred";
     Ge EC L-lines above the < 1 keV ROI; E_g(T_op) GAP rows; per-channel GAP-input coverage rows (Li2MoO4 in no channel).
Offline; inputs: v3 CSV, code/WP8-U-TOP/data/jarvis_top.json (cached JARVIS dft_3d 9-24-2025 extract)."""
import csv, json, math, os, re
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
V3 = os.path.join(ROOT, "returns/R16/WP8-U-table-v3.csv")
V4 = os.path.join(ROOT, "returns/R16/WP8-U-table-v4.csv")
JT = os.path.join(ROOT, "code/WP8-U-TOP/data/jarvis_top.json")
COLS = ["material", "label", "group", "verdict", "property", "value", "unit", "tag", "source", "locator", "note"]
DBJ = "JARVIS-DFT dft_3d 9-24-2025"

rows = [dict(x) for x in csv.DictReader(open(V3))]
log = {"verdict_column": [], "dropped": [], "retagged": [], "corrected": [], "added": 0}
final = {}
for x in rows:
    if x["property"] == "verdict":
        final[x["material"]] = x["value"]
meta = {}
for x in rows:
    meta.setdefault(x["material"], (x["label"], x["group"]))

# (1) verdict column
for x in rows:
    v = final.get(x["material"])
    if v and x["verdict"] != v:
        log["verdict_column"].append((x["material"], x["property"], x["verdict"], v))
        x["verdict"] = v
for m in final:
    if m not in meta:
        continue

# (2) screening rows
scr = [i for i, x in enumerate(rows) if re.fullmatch(r"screen_S[123]", x["property"])]
groups = {}
for i in scr:
    groups.setdefault((rows[i]["material"], rows[i]["property"]), []).append(i)
drop = set()
for key, idx in groups.items():
    if len(idx) > 1:
        sup = [i for i in idx if rows[i]["note"].startswith("supersedes")]
        keep = sup[-1] if sup else idx[-1]
        for i in idx:
            if i != keep:
                drop.add(i)
                log["dropped"].append(dict(rows[i], reason="superseded by the row kept for key %s/%s (VER-CW7 §A)" % key))
for i in scr:
    if i in drop:
        continue
    x = rows[i]
    if "[E]" in x["value"]:
        old = dict(x)
        val = x["value"].replace("[E]", "[UNVERIFIED]")
        other = re.search(r"\[(FT|ABS)[^\]]*\]", val)          # an ID'd [FT]/[ABS] item still supports the cell
        if not other:
            val = re.sub(r"^(PASS|FAIL)\b", "COND", val)
        x["value"] = val
        x["tag"] = "UNVERIFIED"
        x["note"] = "v4 retag (ERR-CW7; VER-CW7 §A): [E] is a step tag, not screening evidence; " + x["note"]
        log["retagged"].append((old["material"], old["property"], old["value"], val))
rows = [x for i, x in enumerate(rows) if i not in drop]

# CaWO4 3H wording (VER-CW7 §A; 1908.06755 p.4)
for x in rows:
    if x["material"] == "CaWO4" and x["property"] == "cosmo_identified":
        old = x["value"]
        x["value"] = ("179Ta (EC) and 181W (EC) observed in CRESST data; 3H inferred from the 181W activity (co-production "
                      "W + p -> 181W + 3H), not observed")
        x["locator"] = "p.4 §2.3.2 ('It is hard to be observed experimentally ... the observed 181W should be accompanied by a 3H component'); p.11"
        x["note"] = "v4 correction (ERR-CW7): v3 said '3H observed'; production rates at sea level not given; GAP for the rate"
        x["tag"] = "FT"
        x["source"] = "arXiv:1908.06755"
        log["corrected"].append(("CaWO4", "cosmo_identified", old, x["value"]))

new = []


def add(mat, prop, val, unit, tag, src, loc, note):
    lab, grp = meta.get(mat, (mat, "-"))
    new.append(dict(material=mat, label=lab, group=grp, verdict=final.get(mat, rows_verdict(mat)), property=prop, value=str(val),
                    unit=unit, tag=tag, source=src, locator=loc, note=note))


def rows_verdict(mat):
    for x in rows:
        if x["material"] == mat:
            return x["verdict"]
    return "-"


# (3) elastic tensors
J = json.load(open(JT))
PERM = [0, 1, 2, 4, 5, 3]          # Voigt index I (xx,yy,zz,yz,zx,xy) <- JARVIS index PERM[I] (xx,yy,zz,xy,yz,zx)
IDX = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]


def to_voigt(Cj):
    Cj = np.array(Cj, float)
    return Cj[np.ix_(PERM, PERM)]


def C4(Cv):
    C = np.zeros((3, 3, 3, 3))
    for I, (i, j) in enumerate(IDX):
        for K, (k, l) in enumerate(IDX):
            for a, b in ((i, j), (j, i)):
                for c, d in ((k, l), (l, k)):
                    C[a, b, c, d] = Cv[I, K]
    return C


def fib(N=4000):
    i = np.arange(N) + 0.5
    z = 1 - 2 * i / N
    ph = i * np.pi * (3 - 5 ** 0.5)
    return np.stack([np.sqrt(1 - z * z) * np.cos(ph), np.sqrt(1 - z * z) * np.sin(ph), z], 1)


def speeds(Cv, rho, n):
    """phase speeds (km/s, ascending) and eigenvectors for directions n (rows)"""
    G = np.einsum("ijkl,nj,nl->nik", C4(Cv), n, n) * 1e9 / (rho * 1e3)
    w, U = np.linalg.eigh(G)
    return np.sqrt(np.clip(w, 0, None)) / 1e3, U


CHR4 = {}
for m, x in J.items():
    if m not in meta or x.get("elastic_tensor") in (None, "na"):
        continue
    Cv = to_voigt(x["elastic_tensor"])
    if np.linalg.eigvalsh(Cv).min() <= 0:
        continue
    rho = x["density"]
    crys = x.get("crys", "")
    src = "%s %s" % (DBJ, x["jid"])
    n = fib()
    c, U = speeds(Cv, rho, n)
    cLA = c[:, 2].mean()
    proj = np.einsum("nk,nkv->nv", n, U) ** 2                      # (q.e_nu)^2, sums to 1 over nu
    s_nr1 = np.mean(np.sum(proj / c, axis=1))                       # <sum_nu (q.e_nu)^2 / c_nu>
    c_nr1 = 1 / s_nr1
    l100, _ = speeds(Cv, rho, np.array([[1.0, 0, 0]]))
    l001, _ = speeds(Cv, rho, np.array([[0, 0, 1.0]]))
    l100, l001 = l100[0], l001[0]
    CHR4[m] = dict(crys=crys, cLA=cLA, cLA_min=c[:, 2].min(), cLA_max=c[:, 2].max(), c_nr1=c_nr1, T001=(l001[0], l001[1]),
                   C44=Cv[3, 3], C55=Cv[4, 4], C66=Cv[5, 5], C14=Cv[0, 3])
    if crys == "cubic":
        add(m, "c_NR1_heavy", round(c_nr1, 3), "km/s", "E", src, "<sum_nu (q.e_nu)^2/c_nu(q)>^-1 on a 4000-point sphere (WP8-F-v3 (2.3a''))",
            "heavy-mediator NR-1ph scalar (rate per mass prop. to 1/c_NR1 at 0.1 <~ m_chi <~ q_BZ/2v_max); cubic: shear order irrelevant")
        continue
    vo = "C11=%.1f; C22=%.1f; C33=%.1f; C12=%.1f; C13=%.1f; C23=%.1f; C44=%.1f; C55=%.1f; C66=%.1f; C14=%.1f; C24=%.1f; C56=%.1f; C15=%.1f" % (
        Cv[0, 0], Cv[1, 1], Cv[2, 2], Cv[0, 1], Cv[0, 2], Cv[1, 2], Cv[3, 3], Cv[4, 4], Cv[5, 5], Cv[0, 3], Cv[1, 3], Cv[4, 5], Cv[0, 4])
    add(m, "C_ij_Voigt_DFT_v4", vo, "GPa", "DB", src, "elastic_tensor re-indexed: JARVIS shear order (xy,yz,zx) -> Voigt (yz,zx,xy)",
        "supersedes R14 C_ij_Voigt_DFT (C44 and C66 were swapped for every non-cubic entry; C14 was read as C15); ERR-CW7")
    add(m, "c_LA_Christoffel_avg", round(cLA, 3), "km/s", "E", src, "Christoffel, 4000-point sphere, mean of omega_LA/q, Voigt-ordered tensor",
        "supersedes R14 c_LA_Christoffel_avg (shear-order defect, REF-WP8-S-A §5c); directional range %.2f-%.2f" % (c[:, 2].min(), c[:, 2].max()))
    add(m, "c_dir_100_001", "[100]: L %.2f, T %.2f/%.2f; [001]: L %.2f, T %.2f/%.2f" % (l100[2], l100[0], l100[1], l001[2], l001[0], l001[1]),
        "km/s", "E", src, "Christoffel along the JARVIS cell axes (z = c for hexagonal/trigonal/tetragonal)",
        "supersedes R14 c_dir_100_001; [001] transverse pair degenerate for 3-, 4-, 6-fold c axes (check CW7-C33)")
    add(m, "c_NR1_heavy", round(c_nr1, 3), "km/s", "E", src, "<sum_nu (q.e_nu)^2/c_nu(q)>^-1 on a 4000-point sphere (WP8-F-v3 (2.3a''))",
        "heavy-mediator NR-1ph scalar; differs from c_LA_Christoffel_avg by branch mixing and Jensen (REF-WP8-S-A §5b)")
    add(m, "c_LA_max_dir", round(c[:, 2].max(), 3), "km/s", "E", src, "max over directions of the LA phase speed",
        "sets the NR-1ph edge m_min^ac in anisotropic crystals (fastest direction), WP8-F-v3 §2.3(b)")
    old = [y for y in rows if y["material"] == m and y["property"] == "c_LA_recommended"]
    if old:
        add(m, "c_LA_recommended", round(cLA, 3), "km/s", "E", src, "Christoffel mean, Voigt-ordered tensor",
            "supersedes R14 c_LA_recommended=%s (shear-order defect); 1910.10716 value still 'suspect, pending measured C_ij'" % old[-1]["value"])
json.dump({m: {k: (list(v) if isinstance(v, tuple) else v) for k, v in d.items()} for m, d in CHR4.items()},
          open(os.path.join(HERE, "data", "christoffel_v4.json"), "w"), indent=1)

# (4) flags
for m in ("TeO2", "LiAlO2"):
    add(m, "flag_rho_T_DFT_proxy", "rho_T is the OptB88vdW-relaxed DFT density (no a_exp row): a proxy, not a measurement", "-", "DB",
        DBJ, "density", "REF-WP8-U-B (e)(v); VER-CW7 §A; the summary prints it with the superscript d and this flag")


def frac_beta_below(Q, Z, Ecut=1.0, n=20001):
    """allowed-shape beta spectrum with the non-relativistic Fermi function (Z of the daughter); fraction below Ecut (keV)"""
    me = 511.0
    T = np.linspace(1e-6, Q, n)
    W = T / me + 1
    p = np.sqrt(W ** 2 - 1)
    eta = Z / 137.036 * W / p
    F = 2 * np.pi * eta / (1 - np.exp(-2 * np.pi * eta))
    s = F * p * W * (Q - T) ** 2
    cdf = np.concatenate([[0], np.cumsum((s[1:] + s[:-1]) / 2 * np.diff(T))])
    return np.interp(Ecut, T, cdf) / cdf[-1]


f_pb = frac_beta_below(63.5, 83)        # 210Pb -> 210Bi g.s. branch (16%) [UNVERIFIED scheme]
f_bi = frac_beta_below(1162.0, 84)      # 210Bi -> 210Po (100%) [UNVERIFIED scheme]
rate_per_Bq = 86400 * (0.16 * f_pb + f_bi)          # /(kg d keV) per Bq/kg in the <1 keV bin, secular equilibrium
a_max = 1 / rate_per_Bq
for m, wpb in (("PbTe", 207.2 / (207.2 + 127.6)), ("PbS", 207.2 / (207.2 + 32.06)), ("PbSe", 207.2 / (207.2 + 78.97))):
    add(m, "S4_cond_Pb210", "COND: bulk 210Pb from the element; S4 needs a(210Pb) <~ %.1e Bq per kg of compound (%.1e Bq/kg Pb)" % (a_max, a_max / wpb),
        "Bq/kg", "E", "decay scheme [UNVERIFIED]: Q 63.5 keV, 84% via the 46.5 keV level (deposit >= 46.5 keV in bulk), 16% to g.s.; 210Bi Q 1162 keV",
        "allowed shape x non-relativistic Fermi function: f_<1keV = %.4f (210Pb g.s.), %.5f (210Bi); 1 Bq/kg -> %.1f /(kg d keV)" % (f_pb, f_bi, rate_per_Bq),
        "REF-WP8-S-A §8: 210Pb is a material property of lead compounds; modern lead is typically far above this threshold and only "
        "selected low-210Pb lead may meet it [UNVERIFIED]; S4 for PbS/PbSe/PbTe is COND until a(210Pb) of the lead is measured")
add("Ge", "cosmo_EC_lines_subkeV", "K lines ~10 keV; L lines 1.1-1.3 keV (65Zn, 68Ge) lie ABOVE the < 1 keV ROI; only M lines (~0.1 keV) and resolution tails of L enter",
    "-", "FT", "arXiv:1607.04560", "p.3 ('L- and M-shell captures ... approximately 1 and 0.1 keV'); p.10 ('between 1.1 and 1.3 keV (the energies of the L-shell lines for 65Zn and 68Ge')",
    "v4 correction (ERR-CW7, VER-CW7 §B9) of the CW7 LE-177 wording 'EC nuclides land in the sub-keV ROI through their L/M fractions'")
for m, note in (("Ge", "low-T gap not in the table (0.67 eV is room T); 0.7437 eV at 0 K [UNVERIFIED memory]"),
                ("GaAs", "low-T gap not in the table (1.42 eV is room T); 1.519 eV at 0 K [UNVERIFIED memory]"),
                ("GaSb", "low-T gap not in the table (0.72 eV is room T); ~0.81 eV at 0 K [UNVERIFIED memory]")):
    add(m, "GAP:E_g_Top", "GAP", "eV", "GAP", "-", "-", note + "; edges need E_g(T_op) to 1% (WP8-F-v3 §5.2); REF-WP8-S-A §3")

# per-channel GAP-input coverage (REF-WP8-S-A §2; uses the same input names as code/CW7/rank.py)
by = {}
for x in rows + new:
    by.setdefault(x["material"], []).append(x)


def has(mat, props, tags=("FT", "E", "DB")):
    return any(x["property"] in props and x["tag"] in tags and x["value"] not in ("GAP", "") and not x["property"].startswith("GAP")
               for x in by.get(mat, []))


cov = {}
for mat, xs in by.items():
    if final.get(mat, xs[0]["verdict"]) not in ("SURVIVOR", "SURVIVOR-COND"):
        continue
    miss = []
    if not has(mat, ["E_g"], ("FT",)):
        miss.append("ER edge (measured E_g)")
    if not has(mat, ["eps_eh"], ("FT",)) and not has(mat, ["eps_eh_pred_GAPEF"], ("E",)):
        miss.append("threshold in quanta (eps_eh)")
    if not has(mat, ["c_LA_recommended", "c_LA_Christoffel_avg", "c_LA", "c_L_iso"]):
        miss.append("NR-1ph (c_LA)")
    vetted_bad = any(x["property"] == "GAP:eps_0_DFT_vetted" for x in xs)      # rule V2: the DFPT eps_0 of a failed run is not an input
    e0props = ["eps_0", "eps_0_par", "eps_0_perp"] + ([] if vetted_bad else ["eps_0_DFT"])
    pol = (has(mat, ["Zstar_bar", "Zstar_LST"]) and has(mat, ["eps_inf"], ("FT",))) or \
          (has(mat, e0props) and has(mat, ["eps_inf", "eps_inf_DFT"]))
    if not pol and mat not in ("Si", "Ge", "C"):
        miss.append("POL (Z* or eps pair)")
    if not has(mat, ["composition"], ("-", "FT", "E", "DB", "D", "see text")):
        miss.append("Migdal (composition)")
    if mat in ("Al", "Nb"):
        miss.append("ER edge: superconductor, the floor is 2 Delta_BCS (pair breaking), not 2E_g (separate SC-edge line)")
    cov[mat] = miss
    if miss:
        add(mat, "GAP:channel_inputs", "; ".join(miss), "-", "GAP", "-", "-",
            "channels this material cannot enter with the table's inputs; a ranking must list it as 'not ranked (GAP)' (REF-WP8-S-A §2)")
json.dump(cov, open(os.path.join(HERE, "data", "coverage_v4.json"), "w"), indent=1)

log["added"] = len(new)
log["Pb210"] = dict(f_pb=f_pb, f_bi=f_bi, rate_per_Bq=rate_per_Bq, a_max=a_max)
json.dump(log, open(os.path.join(HERE, "data", "v4_changes.json"), "w"), indent=1, ensure_ascii=False)
with open(V4, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    for x in rows + new:
        w.writerow({k: x[k] for k in COLS})
print("v3 rows", len(rows) + len(drop), "dropped", len(drop), "retagged", len(log["retagged"]), "verdict cells", len(log["verdict_column"]),
      "corrected", len(log["corrected"]), "added", len(new), "v4 rows", len(rows) + len(new))
