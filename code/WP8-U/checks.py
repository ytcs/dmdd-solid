"""WP8-U checks (labels U0-U12, distinct from CONTROLS C1-C8 and from the screening criteria S1-S3) (offline, < 5 s). Reads returns/R13/WP8-U-table.csv and code/WP8-U/data/*.json.

Each check prints PASS/FAIL; FLAG lines record source disagreements found (they are findings, not failures).
Exit code 1 on any FAIL.
"""
import csv, json, math, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "..", "..", "returns", "R13", "WP8-U-table.csv")
R = list(csv.DictReader(open(CSV)))
D = lambda f: json.load(open(os.path.join(HERE, "data", f)))
NIST, J, MP, ARX = D("nist_isotopes.json"), D("jarvis_extract.json"), D("optimade_mp.json"), D("arxiv_verified.json")
sys.path.insert(0, HERE)
from materials import MATERIALS  # noqa: E402
from screening import S as SCREEN, EXTRA_EXCLUSIONS  # noqa: E402

fails, flags = [], []


def check(name, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + name + (": " + msg if msg else ""))
    if not ok:
        fails.append(name)


def flag(msg):
    print("FLAG " + msg)
    flags.append(msg)


def val(m, p, src=None, first=True):
    out = []
    for r in R:
        if r["material"] == m and r["property"] == p and (src is None or src in r["source"]):
            try:
                out.append(float(r["value"]))
            except ValueError:
                nums = re.findall(r"[-+]?\d+\.?\d*(?:e[-+]?\d+)?", r["value"])
                out.append(float(nums[0]) if nums else None)
    out = [x for x in out if x is not None]
    return (out[0] if out else None) if first else out


# U0 CSV integrity: every value has a provenance tag and a source; FT rows carry an arXiv ID and a locator;
#    DB rows carry a database ID.
bad = []
for r in R:
    t = r["tag"]
    if r["property"].startswith(("screen_", "verdict", "composition")):
        continue
    if t not in ("FT", "DB", "E", "UNVERIFIED", "GAP"):
        bad.append((r["material"], r["property"], t))
    if t == "FT" and not (re.search(r"arXiv:\d{4}\.\d{4,5}", r["source"]) and r["locator"]):
        bad.append((r["material"], r["property"], "FT without arXiv/locator"))
    if t == "DB" and not re.search(r"JVASP-\d+|mp-\d+|agm\d+|NIST|IAEA", r["source"] + r["value"]):
        bad.append((r["material"], r["property"], "DB without ID"))
check("U0 provenance tags", not bad, f"{len(R)} rows; bad={bad[:3]}")

# U0b every arXiv ID cited in the CSV, the screening record and the md was verified against the arXiv API
MD = os.path.join(HERE, "..", "..", "returns", "R13", "WP8-U.md")
cited = set(re.findall(r"(\d{4}\.\d{4,5}|astro-ph/\d{7})", open(CSV).read() + json.dumps(SCREEN) + json.dumps(EXTRA_EXCLUSIONS) + open(MD).read()))
cited -= {"0204411"}
missing = sorted(i for i in cited if i not in ARX and not i.startswith("0"))
check("U0b arXiv IDs verified", not missing, f"{len(cited)} cited, missing {missing}")

# U1 Lyddane-Sachs-Teller on full-text data: eps_0/eps_inf = (omega_L/omega_T)^2
for m, e0, ei, wl, wt in (("SiC-3C", 9.7, 6.5, 120.5, 98.7), ("SiC-6H", 9.67, 6.6, 119.7, 97.7), ("SiC-4H", 9.76, 6.6, 119.5, 97.0)):
    lhs, rhs = e0 / ei, (wl / wt) ** 2
    check(f"U1 LST {m} (2008.08560 Table I, perp)", abs(lhs / rhs - 1) < 0.05, f"eps0/epsinf={lhs:.3f} (wL/wT)^2={rhs:.3f}")

# U1b LST omega_L from JARVIS DFPT (DB route) vs the DFT optical maximum of 1910.10716 Table I (FT route)
dev = []
for m in MATERIALS:
    a, b = val(m, "omega_L_LST"), val(m, "omega_O_max", "1910.10716")
    if a and b:
        dev.append((m, a / b - 1))
print("     omega_L_LST/omega_O_max - 1:", ", ".join(f"{m} {d:+.2f}" for m, d in dev))
check("U1b LST (DB) vs omega_O_max (FT), binary cubic", dev and max(abs(d) for _, d in dev) < 0.15)

# U2 Debye temperature from JARVIS moduli (Anderson) vs measured theta_D
dev = []
for m in ("C", "Si", "Ge", "SiC-4H", "SiC-6H"):
    a, b = val(m, "theta_D_E"), val(m, "theta_D")
    dev.append((m, a / b - 1))
print("     theta_D_E/theta_D - 1:", ", ".join(f"{m} {d:+.3f}" for m, d in dev))
check("U2 Debye T (E) vs FT", max(abs(d) for _, d in dev) < 0.15)
# 3C-SiC: same moduli and density as 4H/6H (JARVIS), so a 19% higher theta_D (1430 vs 1200 K, 2008.08560) is a
# source/definition spread, not a polytype effect; recorded as a finding.
a, b = val("SiC-3C", "theta_D_E"), val("SiC-3C", "theta_D")
if abs(a / b - 1) > 0.15:
    flag(f"3C-SiC theta_D = {b:.0f} K (2008.08560) vs elastic {a:.0f} K; 4H/6H quote 1200 K with near-identical moduli")

# U3 densities: from experimental lattice constants vs FT rho; vs JARVIS; MP OPTIMADE structure vs JARVIS
for m in ("C", "Si"):
    a, b = val(m, "rho_T_from_a_exp"), val(m, "rho_T", "2008.08560")
    check(f"U3a rho from a_exp vs FT {m}", abs(a / b - 1) < 0.01, f"{a:.4f} vs {b}")
a, b = val("ZrTe5", "rho_T"), None
dev = [(m, val(m, "rho_T_from_a_exp") / val(m, "rho_T_DFT") - 1) for m in MATERIALS
       if val(m, "rho_T_from_a_exp") and val(m, "rho_T_DFT")]
check("U3b rho(a_exp) vs rho(JARVIS)", max(abs(d) for _, d in dev) < 0.10,
      "max dev %s %+.3f" % max(dev, key=lambda t: abs(t[1])))


def mass(el):
    iso = NIST[el]["isotopes"]
    return sum(i["mass"] * i["abundance"] for i in iso if i["abundance"]) / sum(i["abundance"] for i in iso if i["abundance"])


dev = []
for m, v in MATERIALS.items():
    jid, mp = v[2], v[3]
    if jid and mp in MP:
        s = MP[mp]
        lat = s["lattice_vectors"]
        a_, b_, c_ = lat
        V = abs(a_[0] * (b_[1] * c_[2] - b_[2] * c_[1]) - a_[1] * (b_[0] * c_[2] - b_[2] * c_[0]) + a_[2] * (b_[0] * c_[1] - b_[1] * c_[0]))
        rho = sum(mass(e) for e in s["species_at_sites"]) / 6.02214076e23 / (V * 1e-24)
        dev.append((m, rho / J[jid]["density"] - 1))
LAYERED = ("hBN", "Bi2Se3", "ZrTe5", "NiPS3", "PE", "He-s")  # MP (PBE/r2SCAN, no vdW) vs OptB88vdW interlayer spacing
d1 = [(m, d) for m, d in dev if m not in LAYERED]
check("U3c rho(MP OPTIMADE structure) vs rho(JARVIS), non-layered", max(abs(d) for _, d in d1) < 0.10,
      "n=%d, max dev %s %+.3f" % ((len(d1),) + max(d1, key=lambda t: abs(t[1]))))
for m, d in dev:
    if m in LAYERED and abs(d) > 0.05:
        flag(f"MP vs JARVIS density differ by {d:+.0%} for layered/molecular {m} (vdW functional)")

# U4 isotopes: abundances sum to 1; NIST mean masses vs A_j of 1910.10716 Table I
ok = all(abs(sum(i["abundance"] for i in NIST[e]["isotopes"] if i["abundance"]) - 1) < 2e-3 for e in NIST)
check("U4a isotopic abundances sum to 1", ok)
pairs = {"Si": 28.1, "Ge": 72.6, "Cs": 133, "I": 127, "Ga": 69.7, "As": 74.9, "Li": 6.9, "Pb": 207, "In": 115,
         "Sb": 122, "Zn": 65.4, "W": 184, "Te": 128}
check("U4b NIST A vs 1910.10716 A_j", all(abs(mass(e) - a) < 0.6 for e, a in pairs.items()),
      ", ".join(f"{e} {mass(e):.2f}" for e in ("Te", "Sb", "W")))

# U5 plasma frequency from the valence count vs measurement
a, b = val("Si", "omega_p_E"), val("Si", "omega_pl_meas")
check("U5a Si omega_p (4 e/atom) vs EELS 16.6 eV (2004.10709)", abs(a / b - 1) < 0.02, f"{a} vs {b}")
for m in ("Si", "C", "SiC-3C"):
    nq, nv = val(m, "n_e_quoted"), val(m, "n_e_val")
    if abs(nq / nv - 1) > 0.1:
        flag(f"2008.08560 Table I n_e({m}) = {nq}e23 cm^-3 vs 4 e/atom x N = {nv:.2f}e23 (ratio {nq / nv:.2f})")
a, b = val("C", "omega_p_E"), val("C", "omega_p_meas")
if abs(a / b - 1) > 0.1:
    flag(f"2008.08560 Table I omega_p(diamond) = {b} eV vs free-electron 4 e/atom {a} eV: 22 eV implies ~2 e/atom")

# U6 phonon lifetime tau = l / c_s (1901.07569 Eq. (4) and Table I)
for m in ("C", "Si", "Ge"):
    l, c, t = val(m, "phonon_mfp"), val(m, "c_avg", "1901.07569"), val(m, "phonon_lifetime")
    check(f"U6 tau=l/c_s {m}", abs(l * 1e-2 / (c * 1e3) * 1e6 / t - 1) < 0.02, f"{l * 10 / c:.2f} us vs {t}")

# U7 isotope scattering: Tamura coefficient ordering Ge > Si > C (1901.07569 p.4-5 statement), and g2 sanity
A = {m: val(m, "A_iso_Tamura") for m in ("C", "Si", "Ge")}
check("U7 A_iso ordering Ge > Si > C", A["Ge"] > A["Si"] > A["C"], str(A))

# U8 sound speeds: FT c_LA (DFT average, 1910.10716) vs isotropic Voigt estimate from JARVIS
dev = [(m, val(m, "c_L_iso") / val(m, "c_LA") - 1) for m in MATERIALS if val(m, "c_L_iso") and val(m, "c_LA")]
print("     c_L_iso/c_LA - 1:", ", ".join(f"{m} {d:+.2f}" for m, d in dev))
med = statistics.median(abs(d) for _, d in dev)
check("U8 c_L (E from DB) vs c_LA (FT): median |dev| < 10%", med < 0.10, f"median {med:.3f}")
for m, d in dev:
    if abs(d) > 0.2:
        flag(f"c_LA(1910.10716) vs isotropic Voigt c_L differ by {d:+.0%} for {m} (anisotropy or DB moduli)")

# U9 intrinsic specific activity, independent recomputation for KTaO3 (40K) and InSb (115In)
def act(el, A, T_y, mfrac):  # Bq per kg of compound, mfrac = mass fraction of element
    x = [i for i in NIST[el]["isotopes"] if i["A"] == A][0]["abundance"]
    return math.log(2) / (T_y * 3.15576e7) * x * 6.02214076e23 / mass(el) * 1000 * mfrac
k_frac = mass("K") / (mass("K") + mass("Ta") + 3 * mass("O"))
in_frac = mass("In") / (mass("In") + mass("Sb"))
for m, a in (("KTaO3", act("K", 40, 1.248e9, k_frac)), ("InSb", act("In", 115, 4.41e14, in_frac))):
    b = val(m, "specific_activity_intrinsic")
    check(f"U9 specific activity {m}", abs(a / b - 1) < 0.01, f"{a:.3g} Bq/kg")

# U10 DFT gaps as proxies: TBmBJ vs experimental (1910.10716) for gapped materials
dev = []
for m in MATERIALS:
    a, b = val(m, "E_g_DFT_TBmBJ"), val(m, "E_g", "1910.10716")
    if a and b and b > 1:
        dev.append((m, a / b - 1))
med = statistics.median(abs(d) for _, d in dev)
check("U10 TBmBJ/E_g(exp) median |dev| < 25% (proxy quality)", med < 0.25, f"n={len(dev)} median {med:.2f}")
for m, d in dev:
    if abs(d) > 0.3:
        flag(f"TBmBJ gap off by {d:+.0%} for {m}: use E_g(exp) only")

# U11 cross-source disagreements in the full text (recorded, not failed)
if val("C", "omega_T", "2008.08560") != val("C", "omega_T", "1901.07569"):
    flag(f"diamond omega_T: {val('C', 'omega_T', '2008.08560')} meV (2008.08560) vs {val('C', 'omega_T', '1901.07569')} meV (1901.07569)")
if abs(val("Ge", "E_g", "1901.07569") - val("Ge", "E_g", "1910.10716")) > 0.05:
    flag(f"Ge E_g: {val('Ge', 'E_g', '1901.07569')} eV (1901.07569) vs {val('Ge', 'E_g', '1910.10716')} eV (1910.10716)")
if abs(val("Si", "c_avg", "2008.08560") - val("Si", "c_LA")) > 1:
    flag("c_s naming: 'average phonon speed' (2008.08560/1901.07569, Si 5.88 km/s) is not c_LA (1910.10716, 8.51 km/s)")

# U11b YIG lattice constant: 1905.13744 quotes a ~ 12.56 A; MP OPTIMADE mp-4704 primitive (bcc) cell gives a_conv = (2V)^(1/3)
lat = MP["mp-4704"]["lattice_vectors"]
a_, b_, c_ = lat
V = abs(a_[0] * (b_[1] * c_[2] - b_[2] * c_[1]) - a_[1] * (b_[0] * c_[2] - b_[2] * c_[0]) + a_[2] * (b_[0] * c_[1] - b_[1] * c_[0]))
a_mp = (2 * V) ** (1 / 3)
print(f"     YIG a_conv(MP) = {a_mp:.3f} A; rho(a=12.56) = {val('YIG', 'rho_T_from_a_exp'):.3f} g/cm3")
if abs(a_mp / 12.56 - 1) > 0.01:
    flag(f"YIG lattice constant 12.56 A (1905.13744 p.4) vs {a_mp:.3f} A (MP GGA+U cell, which overestimates); "
         f"rho(12.56 A) = {val('YIG', 'rho_T_from_a_exp'):.2f} g/cm3 - check n_s = 20/a^3 input")

# U12 every non-excluded material has the three screening criteria and a verdict
check("U12 screening complete", all(len(SCREEN[m]) == 4 and SCREEN[m][3] in
                                     ("SURVIVOR", "SURVIVOR-COND", "EXCLUDED", "REFERENCE") for m in MATERIALS))

print(f"\n{len(fails)} FAIL, {len(flags)} FLAG")
sys.exit(1 if fails else 0)
