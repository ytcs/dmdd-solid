"""WP8-U-TOP checks (offline, < 5 s). Labels T0-T15 (prefix WP8-U-TOP; distinct from WP8-U U0-U12, CONTROLS C1-C8).
Run after build_v2.py. Exit code 1 on any FAIL."""
import csv, json, math, os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import build_v2 as B  # rebuilds the table (deterministic)

v2 = list(csv.DictReader(open(B.OUT)))
r13 = list(csv.DictReader(open(B.R13)))
ver = json.load(open(os.path.join(HERE, "data", "arxiv_verified.json")))
res = []


def check(name, ok, msg=""):
    res.append((name, bool(ok), msg))


new = v2[len(r13):]
# T0 provenance integrity
bad = [r for r in new if r["tag"] not in ("FT", "DB", "E", "GAP", "UNVERIFIED")]
badft = [r for r in new if r["tag"] == "FT" and (not r["locator"] or not (r["source"].startswith("arXiv:") or "PMC" in r["source"]))]
baddb = [r for r in new if r["tag"] == "DB" and not re.search(r"JVASP-\d+|doi:|NIST|IAEA", r["source"])]
check("T0 provenance tags/locators", not (bad or badft or baddb), f"{len(bad)} bad tags, {len(badft)} FT w/o locator, {len(baddb)} DB w/o ID")
# T1 arXiv IDs verified (CSV + md)
ids = set(re.findall(r"arXiv:(\d{4}\.\d{4,5})", " ".join(r["source"] + " " + r["locator"] + " " + r["note"] for r in new)))
md = os.path.join(ROOT, "returns", "R14", "WP8-U-top.md")
if os.path.exists(md):
    ids |= set(re.findall(r"(?<![\d.])(\d{4}\.\d{5})(?![\d])", open(md).read()))
missing = sorted(i for i in ids if i not in ver)
check("T1 arXiv IDs verified", not missing, f"{len(ids)} IDs; missing {missing}")
# T2 R13 rows preserved (only verdict of S4 failures changed)
diff = []
FAIL = {m for m, v in B.S4.items() if v[0] == "FAIL"}
for a, b in zip(r13, v2[:len(r13)]):
    for k in B.COLS:
        if a[k] != b[k] and not (a["material"] in FAIL and (k == "verdict" or (a["property"] == "verdict" and k in ("value", "note")))):
            diff.append((a["material"], a["property"], k))
check("T2 R13 rows preserved", not diff and len(v2) >= len(r13), f"{len(diff)} unexpected cell changes")
# T3 Christoffel: isotropic tensor -> constant speeds sqrt(C11/rho), sqrt(C44/rho); 1910.10716 c_LA outliers
lam, mu, rho = 60.0, 40.0, 3.0
Ci = [[lam + 2 * mu, lam, lam, 0, 0, 0], [lam, lam + 2 * mu, lam, 0, 0, 0], [lam, lam, lam + 2 * mu, 0, 0, 0],
      [0, 0, 0, mu, 0, 0], [0, 0, 0, 0, mu, 0], [0, 0, 0, 0, 0, mu]]
sp, _ = B.christoffel(Ci, rho)
cl, ct = math.sqrt((lam + 2 * mu) * 1e9 / (rho * 1e3)) / 1e3, math.sqrt(mu * 1e9 / (rho * 1e3)) / 1e3
check("T3a Christoffel isotropic limit", np.allclose(sp[:, 2], cl, rtol=1e-9) and np.allclose(sp[:, :2], ct, rtol=1e-9))
rat = {m: B.C_LA_1910[m] / B.CHR[m][0] for m in B.C_LA_1910 if m in B.CHR}
out = {m for m, x in rat.items() if abs(x - 1) > 0.2}
within10 = [m for m, x in rat.items() if abs(x - 1) <= 0.1]
check("T3b 1910.10716 c_LA vs Christoffel", out == {"GaN", "AlN", "ZnO", "SiO2-q", "NaCl"} and len(within10) >= 12,
      f"outliers {sorted(out)}; {len(within10)}/{len(rat)} within 10 %; ratios " + ", ".join(f"{m} {x:.2f}" for m, x in sorted(rat.items())))
check("T3c outliers exceed the max directional c_L", all(B.C_LA_1910[m] > B.CHR[m][2] * 1.3 for m in out - {"NaCl"}) and B.C_LA_1910["NaCl"] < B.CHR["NaCl"][1],
      "no propagation direction reproduces the 1910.10716 hexagonal/trigonal values; NaCl below the min")
# T4 Hill Young's modulus, isotropic: Y = mu(3 lam + 2 mu)/(lam + mu)
_, _, Y = B.hill(Ci)
check("T4 VRH Young modulus isotropic", abs(Y - mu * (3 * lam + 2 * mu) / (lam + mu)) < 1e-9)
# T5 2008.08560 n_e column = 2 e/atom; omega_p(Si, 4 e/atom) = 16.6; SiC measured 22.1 within 5 % of 4 e/atom
r = [B.QUOTED[m] / B.N1023[m] for m in B.N1023]
check("T5a 2008.08560 n_e/N = 2.0", all(abs(x - 2) < 0.05 for x in r), f"{[round(x, 3) for x in r]}")
check("T5b hbar omega_p", abs(B.hw_p(2.0e23) - 16.6) < 0.1 and abs(B.hw_p(3.54e23) - 22.0) < 0.2 and abs(22.1 / B.hw_p(3.84e23) - 1) < 0.05,
      f"Si(4e) {B.hw_p(2e23):.2f}; C(quoted n_e) {B.hw_p(3.54e23):.2f} = the quoted 22 eV; SiC 22.1/{B.hw_p(3.84e23):.1f}")
# T6 LST Born-charge formula reproduces 1910.10716 Zbar* (same paper's eps_inf, omega_O range)
V = json.load(open(os.path.join(HERE, "data", "zstar_validation.json")))
dev = {m: z / q - 1 for m, (z, q) in V.items()}
check("T6 Z*_LST vs 1910.10716 Zbar*", len(dev) >= 10 and max(abs(x) for x in dev.values()) < 0.15 and np.median([abs(x) for x in dev.values()]) < 0.05,
      ", ".join(f"{m} {x:+.3f}" for m, x in dev.items()))
# T7 empirical eps_eh bracket contains measured values (Eg at the measurement temperature)
MEAS = {"Si": (3.62, 1.12), "Ge(77K)": (2.96, 0.73), "C": (13.1, 5.47), "3C-SiC": (6.90, 2.39), "4H-SiC": (7.83, 3.26),
        "6H-SiC": (6.7, 3.02), "GaAs": (4.2, 1.42), "GaN": (8.9, 3.43), "a-SiO2": (18.0, 9.0), "CdTe": (4.43, 1.44),
        "CZT": (4.6, 1.57), "TlBr": (6.5, 2.68), "HgI2": (4.2, 2.13)}
inside = {k: min(1.54 * g + 1.89, 2.8 * g + 0.5) * 0.99 <= e <= max(1.54 * g + 1.89, 2.8 * g + 0.5) * 1.01 for k, (e, g) in MEAS.items()}
check("T7 eps_eh bracket covers measurements (HgI2 the documented exception)", [k for k, v in inside.items() if not v] == ["HgI2"],
      f"{sum(inside.values())}/{len(inside)} inside (1 % tolerance); a-SiO2 Eg 9.0 eV [E]; Ge Eg(77 K) 0.73 eV from 1602.08005 p.9")
# T8 3H shape against full-text rates
F = json.load(open(os.path.join(HERE, "data", "s4_fractions.json")))
ge = 75 * F["f3H_1to7"] / 6
nai = 83 * F["f3H_1to7"] / 6
si = 124 * (1 - math.exp(-B.lam3)) * F["f3H_0to5"] / 5
check("T8 3H shape vs 1706.05818 p.20 and 2506.06568 p.1", abs(ge / 7.2 - 1) < 0.1 and abs(nai / 7.9 - 1) < 0.1 and abs(si / 0.002 - 1) < 0.1,
      f"Ge {ge:.2f} vs 7.2; NaI {nai:.2f} vs 7.9; Si {si:.5f} vs 0.002 /(kg keV day)")
# T9 beta-shape normalisation and unique-forbidden coefficients
check("T9a beta fraction [0,Q] = 1", abs(B.frac(1311.07, 20, 0, 1311.07, 3) - 1) < 1e-9 and abs(B.frac(18.591, 2, 0, 18.591) - 1) < 1e-9)
p, q = 2.0, 3.0
S3 = sum(p ** (2 * k) * q ** (2 * (3 - k)) / (math.factorial(2 * k + 1) * math.factorial(2 * (3 - k) + 1)) for k in range(4))
check("T9b unique-3rd shape = (q^6+7q^4p^2+7q^2p^4+p^6)/5040", abs(S3 - (q ** 6 + 7 * q ** 4 * p ** 2 + 7 * q ** 2 * p ** 4 + p ** 6) / 5040) < 1e-12)
# T10 Klein-Nishina small-T limit vs full formula at T = 0.5 keV
def kn(Eg, T):
    re2, k, s = (2.8179403262e-13) ** 2, Eg / B.ME, T / Eg
    return math.pi * re2 / (B.ME * k * k) * (2 + s * s / (k * k * (1 - s) ** 2) + s / (1 - s) * (s - 2 / k))
check("T10 KN dsigma/dT(T->0)", abs(kn(1460.82, 0.5) / B.kn_dsdT0(1460.82) - 1) < 0.01, f"ratio {kn(1460.82, 0.5) / B.kn_dsdT0(1460.82):.4f}")
# T11 Al free-electron E_F vs 2109.04473 (11.7 eV)
EF = [float(r["value"]) for r in new if r["material"] == "Al" and r["property"] == "E_F_free_E"][0]
check("T11 Al E_F free electron", abs(EF / 11.7 - 1) < 0.02, f"{EF} eV")
# T12 GaAs omega_T from LST vs 1910.10716 omega_O min 31.8
check("T12 GaAs omega_T LST", abs(B.wT_GaAs / 31.8 - 1) < 0.02, f"{B.wT_GaAs:.2f} meV")
# T13 coverage: every SURVIVOR / SURVIVOR-COND material has a value or GAP row for each WP8-F 5.2 item
REQ = {"rho": ["rho_T", "rho_T_from_a_exp", "rho_T_DFT"], "E_g": ["E_g", "E_g_DFT_TBmBJ", "E_g_DFT_PBE", "E_g_DFT_OptB88vdW", "GAP:E_g"],
       "E_x_b": ["GAP:E_x_b"], "E_min": ["GAP:E_min_q"], "eps_inf": ["eps_inf", "eps_inf_DFT", "eps_tensor", "GAP:eps_inf"], "eps_0": ["eps_0", "eps_0_DFT", "eps_tensor", "eps_0_par", "GAP:eps_0", "GAP:eps0_omegaLO_TO"],
       "Zstar": ["Zstar_bar", "Zstar_LST", "GAP:Z*", "GAP:Zstar_tensor"], "omega_T/L": ["omega_T", "omega_T_LST", "omega_T_maxIR_DFT", "omega_L", "omega_L_LST", "GAP:omega_T", "GAP:omega_L"],
       "L_eps2": ["GAP:L_eps2_data"], "c_dir": ["c_LA_Christoffel_avg", "GAP:c_dir"], "DOS": ["GAP:phonon_DOS"],
       "omega_max": ["omega_O_max", "omega_Gamma_max_DFT", "GAP:omega_max"], "MAZ": ["composition"], "n_e": ["n_e_val"], "Z_over_A": ["Z_over_A"],
       "eps_eh": ["eps_eh", "eps_eh_bracket_E", "GAP:eps_eh", "eps_eh_calc"], "F_eh": ["F_eh", "GAP:F_eh", "GAP:F_eh_v2"], "EPW": ["GAP:EPW_g_omegaTA_Qstar"],
       "TLS": ["GAP:tan_delta0_PSTM"], "E_st": ["GAP:E_st1_p_surv"], "y_ion": ["GAP:y_ion_QF"], "Y_mod": ["Y_mod_Hill", "GAP:c_dir"],
       "alpha_th": ["GAP:alpha_th_integral"], "radio": ["primordial_radioisotopes"], "S4": ["S4_verdict"], "cosmo": ["S4_cosmo_verdict", "GAP:S4_cosmo"],
       "qualifiers": ["screen_C1"]}
METALS = {"Al", "Nb"}
props = {}
for rr in v2:
    props.setdefault(rr["material"], set()).add(rr["property"])
miss = []
for m in B.SCREENED:
    for item, names in REQ.items():
        if m in METALS and item in ("E_x_b", "E_min", "eps_inf", "eps_0", "Zstar", "omega_T/L", "eps_eh", "F_eh", "EPW", "E_g"):
            continue
        if not props.get(m, set()) & set(names):
            miss.append((m, item))
check("T13 WP8-F 5.2 coverage (value or GAP)", not miss, f"{len(B.SCREENED)} materials x {len(REQ)} items; missing {miss[:12]}")
# T14 S4 verdicts
check("T14 S4 FAIL set", FAIL == {"KTaO3", "InSb"} and all(rr["verdict"] == "EXCLUDED-RADIO" for rr in v2 if rr["material"] in FAIL),
      f"FAIL {sorted(FAIL)}; KTaO3 {B.S4['KTaO3'][1]:.2e}, InSb {B.S4['InSb'][1]:.2e} /(kg d keV)")
# T15 mechanically unstable DB tensors flagged
check("T15 non-PD tensor flagged (MnO)", any(rr["material"] == "MnO" and rr["property"] == "C_ij_Voigt_DFT" and "NOT positive" in rr["note"] for rr in new))

nf = sum(not ok for _, ok, _ in res)
for n, ok, msg in res:
    print(("PASS " if ok else "FAIL ") + n + (": " + msg if msg else ""))
print(f"{len(res)} checks, {nf} FAIL")
sys.exit(1 if nf else 0)
