"""WP8-U-TOP: build returns/R14/WP8-U-table-v2.csv = the R13 WP8-U table + top-up rows (offline).

Inputs: returns/R13/WP8-U-table.csv (unchanged rows, except the verdict column of S4 failures, see below);
code/WP8-U/{materials.py,data/nist_isotopes.json,data/iaea_gs.json}; data/jarvis_top.json (fetch_db.py); lit_values.py.
Tags: FT, DB, E, UNVERIFIED, GAP (as R13). Every [E] formula is in `locator`/`note` and recomputed in checks.py.
Supersession rule: R13 rows are kept verbatim; a new row whose value replaces an R13 value carries
'supersedes R13 <property>=<value>' at the start of `note`. The only edited R13 cells are the `verdict` column of
materials that fail S4 (EXCLUDED-RADIO), and their `verdict` row carries the supersedes note.
"""
import csv, json, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "code", "WP8-U"))
sys.path.insert(0, HERE)
from materials import MATERIALS, VALENCE  # noqa: E402
from lit_values import ROWS as LIT  # noqa: E402

R13 = os.path.join(ROOT, "returns", "R13", "WP8-U-table.csv")
OUT = os.path.join(ROOT, "returns", "R14", "WP8-U-table-v2.csv")
J = json.load(open(os.path.join(HERE, "data", "jarvis_top.json")))
NIST = json.load(open(os.path.join(ROOT, "code", "WP8-U", "data", "nist_isotopes.json")))
IA = json.load(open(os.path.join(ROOT, "code", "WP8-U", "data", "iaea_gs.json")))["rows"]
DBJ = "JARVIS-DFT dft_3d 9-24-2025"
NA, YEAR, DAY = 6.02214076e23, 3.15576e7, 86400.0
ME = 510.99895  # keV
ALPHA = 1 / 137.035999
HBARC = 197.3269804  # MeV fm
E2_SI = 1.602176634e-19 ** 2
EPS0_SI, U_KG, MEV_J = 8.8541878128e-12, 1.66053906660e-27, 1.602176634e-22

COLS = ["material", "label", "group", "verdict", "property", "value", "unit", "tag", "source", "locator", "note"]
old = list(csv.DictReader(open(R13)))
META = {}
for r in old:
    META.setdefault(r["material"], (r["label"], r["group"], r["verdict"]))
NEWMAT = {"CdTe": ("CdTe", "detector-reference", "NOT-SCREENED"), "CZT": ("Cd0.9Zn0.1Te", "detector-reference", "NOT-SCREENED"),
          "HgI2": ("HgI2", "detector-reference", "NOT-SCREENED"), "TlBr": ("TlBr", "detector-reference", "NOT-SCREENED"),
          "Ir": ("Ir (sensor film metal)", "sensor-film", "NOT-SCREENED"),
          "ALL": ("all materials", "-", "-"), "ALL-SEMI": ("semiconductors (generic)", "-", "-")}
META.update(NEWMAT)
new = []


def add(m, prop, value, unit, tag, source, locator="", note=""):
    lab, grp, ver = META[m]
    new.append(dict(material=m, label=lab, group=grp, verdict=ver, property=prop, value=value, unit=unit, tag=tag,
                    source=source, locator=locator, note=note))


def r13(m, prop):
    return [r for r in old if r["material"] == m and r["property"] == prop]


def r13f(m, prop):
    for r in r13(m, prop):
        try:
            return float(r["value"])
        except ValueError:
            pass
    return None


SCREENED = [m for m, (l, g, v) in META.items() if v in ("SURVIVOR", "SURVIVOR-COND")]

# ------------------------------------------------------------------------------------------------ 1. full-text rows
for (m, p, v, u, s, loc, note) in LIT:
    add(m, p, v, u, "FT", s, loc, note)

# ------------------------------------------------------------------------------------------------ helpers (composition)
def mean_mass(e):
    iso = [i for i in NIST[e]["isotopes"] if i["abundance"]]
    return sum(i["mass"] * i["abundance"] for i in iso) / sum(i["abundance"] for i in iso)


def comp(m):
    return MATERIALS[m][1]


def Mfu(m):
    return sum(n * mean_mass(e) for e, n in comp(m).items())


def rho_best(m):
    for p in ("rho_T", "rho_T_from_a_exp", "rho_T_DFT"):
        v = r13f(m, p)
        if v:
            return v, p
    return None, None


# ------------------------------------------------------------------------------------------------ 2. Z/A
for m in MATERIALS:
    if m not in META or m == "He-l":
        continue
    Z = sum(n * NIST[e]["Z"] for e, n in comp(m).items())
    add(m, "Z_over_A", round(Z / Mfu(m), 4), "-", "E", "NIST ascii2", "sum n Z / sum n A_r over the formula unit",
        "enters the f-sum ceiling (WP8-F 2.1(a))")

# ------------------------------------------------------------------------------------------------ 3. elastic tensors
IDX = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]


def C4(Cv):
    Cv = np.array(Cv, float)
    C = np.zeros((3, 3, 3, 3))
    for I, (i, j) in enumerate(IDX):
        for K, (k, l) in enumerate(IDX):
            for a, b in ((i, j), (j, i)):
                for c, d in ((k, l), (l, k)):
                    C[a, b, c, d] = Cv[I, K]
    return C


def fib(N=2000):
    i = np.arange(N) + 0.5
    z = 1 - 2 * i / N
    ph = i * np.pi * (3 - 5 ** 0.5)
    return np.stack([np.sqrt(1 - z * z) * np.cos(ph), np.sqrt(1 - z * z) * np.sin(ph), z], 1)


def christoffel(Cv, rho):
    """Phase speeds (km/s) on a Fibonacci sphere: Gamma_ik = C_ijkl n_j n_l / rho; sorted eigenvalues."""
    C = C4(Cv)
    n = fib()
    G = np.einsum("ijkl,nj,nl->nik", C, n, n) * 1e9 / (rho * 1e3)
    w = np.linalg.eigvalsh(G)
    return np.sqrt(np.clip(w, 0, None)) / 1e3, w.min()


def along(Cv, rho, n):
    C = C4(Cv)
    n = np.array(n, float) / np.linalg.norm(n)
    G = np.einsum("ijkl,j,l->ik", C, n, n) * 1e9 / (rho * 1e3)
    return np.sqrt(np.sort(np.linalg.eigvalsh(G))) / 1e3


def hill(Cv):
    C = np.array(Cv, float)
    S = np.linalg.inv(C)
    BV = (C[0, 0] + C[1, 1] + C[2, 2] + 2 * (C[0, 1] + C[1, 2] + C[0, 2])) / 9
    GV = (C[0, 0] + C[1, 1] + C[2, 2] - C[0, 1] - C[1, 2] - C[0, 2] + 3 * (C[3, 3] + C[4, 4] + C[5, 5])) / 15
    BR = 1 / (S[0, 0] + S[1, 1] + S[2, 2] + 2 * (S[0, 1] + S[1, 2] + S[0, 2]))
    GR = 15 / (4 * (S[0, 0] + S[1, 1] + S[2, 2]) - 4 * (S[0, 1] + S[1, 2] + S[0, 2]) + 3 * (S[3, 3] + S[4, 4] + S[5, 5]))
    B, G = (BV + BR) / 2, (GV + GR) / 2
    return B, G, 9 * B * G / (3 * B + G)


C_LA_1910 = {}  # c_LA in km/s from the R13 rows (1910.10716 Table I)
for m in MATERIALS:
    v = r13f(m, "c_LA")
    if v:
        C_LA_1910[m] = v
CHR = {}
for m, x in J.items():
    if m not in META or x["elastic_tensor"] in (None, "na"):
        continue
    Cv, rho = x["elastic_tensor"], x["density"]
    src = f"{DBJ} {x['jid']}"
    eig = np.linalg.eigvalsh(np.array(Cv, float))
    stable = eig.min() > 0
    add(m, "C_ij_Voigt_DFT", "; ".join(f"C{a}{b}={Cv[a-1][b-1]}" for a, b in ((1, 1), (3, 3), (1, 2), (1, 3), (4, 4), (6, 6))),
        "GPa", "DB", src, "elastic_tensor (finite-difference, OptB88vdW, 0 K)",
        "" if stable else "NOT positive definite (min eigenvalue %.1f GPa): DFT cell mechanically unstable; speeds not usable" % eig.min())
    if not stable:
        add(m, "GAP:c_dir", "GAP", "-", "GAP", "-", "", "DB elastic tensor not positive definite; directional speeds need measured C_ij")
        continue
    sp, _ = christoffel(Cv, rho)
    cLA, cT1, cT2 = sp[:, 2].mean(), sp[:, 0].mean(), sp[:, 1].mean()
    CHR[m] = (cLA, sp[:, 2].min(), sp[:, 2].max())
    loc = "Christoffel eq. on 2000-point sphere, mean of omega_LA/q (the 1910.10716 App. A3 definition)"
    add(m, "c_LA_Christoffel_avg", round(cLA, 3), "km/s", "E", src, loc,
        f"DFT C_ij and DFT density {rho}; directional range {sp[:, 2].min():.2f}-{sp[:, 2].max():.2f}")
    add(m, "c_TA_Christoffel_avg", f"{cT1:.3f}, {cT2:.3f}", "km/s", "E", src, "Christoffel, two TA branches, sphere means", "")
    l100, l001 = along(Cv, rho, (1, 0, 0)), along(Cv, rho, (0, 0, 1))
    add(m, "c_dir_100_001", f"[100]: L {l100[2]:.2f}, T {l100[0]:.2f}/{l100[1]:.2f}; [001]: L {l001[2]:.2f}, T {l001[0]:.2f}/{l001[1]:.2f}",
        "km/s", "E", src, "Christoffel along Cartesian axes of the JARVIS cell (z = c for hexagonal/trigonal/tetragonal)", "")
    B, G, Y = hill(Cv)
    add(m, "Y_mod_Hill", round(Y, 1), "GPa", "E", src, "Voigt-Reuss-Hill B, G; Y = 9BG/(3B+G)", f"B_H {B:.1f}, G_H {G:.1f} GPa; DFT 0 K")
    if m in C_LA_1910:
        ratio = C_LA_1910[m] / cLA
        if abs(ratio - 1) > 0.2:
            add(m, "c_LA_recommended", round(cLA, 3), "km/s", "E", src, loc,
                f"supersedes R13 c_LA={C_LA_1910[m]} (1910.10716 Table I): ratio {ratio:.2f}, outside the max directional c_L "
                f"{sp[:, 2].max():.2f}; use measured C_ij when available")
        else:
            add(m, "c_LA_check_1910", f"{ratio:.3f}", "-", "E", src, "1910.10716 c_LA / Christoffel average",
                "1910.10716 value confirmed within 20 %" + ("" if abs(ratio - 1) <= 0.1 else " (10-20 %: use either; spread is the DFT spread)"))

# ------------------------------------------------------------------------------------------------ 4. 2008.08560 n_e and omega_p
N1023 = {"C": 1.76, "Si": 0.5, "SiC-3C": 0.96, "SiC-4H": 0.96, "SiC-6H": 0.96}  # 2008.08560 Table I p.5, atoms/1e23 cm^-3
QUOTED = {"C": 3.54, "Si": 1.0, "SiC-3C": 1.95, "SiC-4H": 1.95, "SiC-6H": 1.95}
WP_Q = {"C": 22.0, "Si": 16.6, "SiC-3C": 22.1, "SiC-4H": 22.1, "SiC-6H": 22.1}


def hw_p(n_cm3):  # free-electron plasma energy, eV
    return 1.0545718e-34 * math.sqrt(n_cm3 * 1e6 * 1.602176634e-19 ** 2 / (8.8541878128e-12 * 9.1093837e-31)) / 1.602176634e-19


for m, N in N1023.items():
    n4 = 4 * N
    add(m, "n_e_val_recommended", round(n4, 3), "1e23 cm^-3", "E", "arXiv:2008.08560", "Table I p.5 row N x 4 valence e/atom",
        f"supersedes R13 n_e_quoted={QUOTED[m]} (= {QUOTED[m] / N:.2f} e/atom x N); free-electron hbar*omega_p(4 e/atom) = {hw_p(n4 * 1e23):.1f} eV")
add("C", "omega_p_recommended", round(hw_p(4 * 1.76e23), 1), "eV", "E", "arXiv:2008.08560", "Table I p.5 N; 4 e/atom",
    "supersedes 2008.08560 hbar*omega_p(diamond)=22 eV (= its 2 e/atom n_e); measured EELS value: GAP in sources read")

nv = sum(n * VALENCE[e] for e, n in comp("Li2MoO4").items())
n_l = 3.04 * NA / Mfu("Li2MoO4") * nv
add("Li2MoO4", "n_e_val", round(n_l / 1e23, 4), "1e23 cm^-3", "E", "arXiv:1704.01758", "p.22 rho 3.04 g/cm3 x N_A x n_val/M_fu",
    f"n_val = {nv} e/f.u. (WP8-U VALENCE convention); fills R13 GAP:n_e,omega_p")
add("Li2MoO4", "omega_p_E", round(hw_p(n_l), 2), "eV", "E", "arXiv:1704.01758", "free-electron plasma energy of n_e_val", "")

# ------------------------------------------------------------------------------------------------ 5. Born charges from LST [E]
def zstar(eps0, epsinf, wT_meV, wL_meV, rho, M_fu, M1, M2):
    """Diatomic rigid-ion relation eps0 - epsinf = Z*^2 e^2 /(eps0_SI Omega mu wT^2), with LST eps0/epsinf = (wL/wT)^2 used
    only through the measured pair actually given. Omega = M_fu/(rho N_A) per formula unit (one cation-anion pair)."""
    Om = M_fu * 1e-3 / (rho * 1e3 * NA)
    mu = M1 * M2 / (M1 + M2) * U_KG
    wT = wT_meV * 1e-3 * 1.602176634e-19 / 1.0545718e-34
    if eps0 is None:
        eps0 = epsinf * (wL_meV / wT_meV) ** 2
    return math.sqrt((eps0 - epsinf) * EPS0_SI * Om * mu * wT ** 2 / E2_SI)


mSi, mC = mean_mass("Si"), mean_mass("C")
for m, e0, ei, wT, wL in (("SiC-3C", 9.7, 6.5, 98.7, 120.5), ("SiC-4H", 9.76, 6.6, 98.8, 120.0), ("SiC-6H", 9.67, 6.6, 98.8, 120.3)):
    z = zstar(e0, ei, wT, wL, 3.21, mSi + mC, mSi, mC)
    add(m, "Zstar_LST", round(z, 2), "e", "E", "arXiv:2008.08560", "Table I p.5: eps0(perp), epsinf(perp), omega_TO, rho 3.21",
        "rigid-ion diatomic formula (eps0-epsinf)=Z*^2 e^2/(eps0 Omega mu wT^2), perpendicular components (E1, higher TO of each pair) for 4H/6H; fills R13 GAP:Z*")
# validation set: 1910.10716 cubic diatomics (omega_O range = TO..LO, epsinf, Zbar*) -> Z* reproduced?
VAL = {}
for m in ("GaAs", "InSb", "GaSb", "MgO", "LiF", "NaF", "NaCl", "NaI", "CsI", "ZnS", "PbTe", "PbS", "PbSe"):
    ei, zq = r13f(m, "eps_inf"), r13f(m, "Zstar_bar")
    wT, wL = r13f(m, "omega_O_min"), r13f(m, "omega_O_max")
    rho, _ = rho_best(m)
    e = list(comp(m))
    if None in (ei, zq, wT, wL, rho):
        continue
    z = zstar(None, ei, wT, wL, rho, Mfu(m), mean_mass(e[0]), mean_mass(e[1]))
    VAL[m] = (z, zq)
json.dump(VAL, open(os.path.join(HERE, "data", "zstar_validation.json"), "w"), indent=1)
# GaAs omega_T from LST with FT eps0/epsinf (1807.10291) and the 1910.10716 omega_O max (LO, DFT)
wT_GaAs = 34.9 * math.sqrt(10.89 / 12.9)
add("GaAs", "omega_T_LST", round(wT_GaAs, 2), "meV", "E", "arXiv:1807.10291 + arXiv:1910.10716",
    "omega_L = 34.9 meV (1910.10716 Table I omega_O max, DFT); eps0/epsinf = 12.9/10.89 (1807.10291 Table I)",
    "fills R13 GAP:omega_T; 1910.10716 omega_O min 31.8 meV agrees to 1 %")
add("GaAs", "omega_L", 34.9, "meV", "FT", "arXiv:1910.10716", "Table I p.2 omega_O max", "DFT number from a paper; fills R13 GAP:omega_L")

# ------------------------------------------------------------------------------------------------ 6. eps_eh [E] bracket, F_eh
MEAS_EEH = {r[0] for r in LIT if r[1] == "eps_eh"} | {r["material"] for r in old if r["property"] == "eps_eh"}
MEAS_F = {r[0] for r in LIT if r[1] == "F_eh"} | {r["material"] for r in old if r["property"] == "F_eh"}
NOGAP = {"Al", "Nb"}
for m in SCREENED + ["SiO2-a"]:
    if m in NOGAP:
        continue
    Eg, src = r13f(m, "E_g"), "R13 E_g [FT]"
    if Eg is None:
        Eg, src = r13f(m, "E_g_DFT_TBmBJ"), "R13 E_g_DFT_TBmBJ [DB]"
    if m not in MEAS_EEH:
        if Eg is None or META[m][1] in ("magnetic", "Dirac") or Eg < 0.3:
            add(m, "GAP:eps_eh", "GAP", "-", "GAP", "-", "", "no measurement found; no usable gap for the empirical bracket"
                if Eg is None or Eg < 0.3 or META[m][1] in ("magnetic", "Dirac") else "")
        else:
            lo, hi = 1.54 * Eg + 1.89, 2.8 * Eg + 0.5
            scint = m in ("CaWO4", "Li2MoO4", "NaI", "CsI")
            add(m, "eps_eh_bracket_E", f"{min(lo, hi):.1f}-{max(lo, hi):.1f}", "eV", "E", "arXiv:2610.16949",
                "PDF p.4: [1.54Eg+1.89, (14/5)Eg+0.5] with Eg from " + src + f" = {Eg}",
                "supersedes R13 GAP:eps_eh only as a bracket; no measurement found"
                + ("; scintillator: charge not read out, eps_eh not directly measured (light yield is the observable)" if scint else "")
                + ("; bracket untested above Eg 9 eV and for ionic crystals" if Eg > 9 or META[m][1] in ("halide", "Li-rich") else ""))
    if m not in MEAS_F:
        add(m, "GAP:F_eh_v2", "GAP", "-", "GAP", "-", "", "no measured Fano factor found in the radiation-detector full texts read; generic semiconductor range 0.06-0.14 (DS09)")

# ------------------------------------------------------------------------------------------------ 7. metals: free-electron v_F, k_TF, E_F; Debye mean phonon energy
for m, nval in (("Al", 3), ("Nb", 5)):
    rho = r13f(m, "rho_T_DFT")
    n = rho * NA / Mfu(m) * nval  # cm^-3
    kF = (3 * math.pi ** 2 * n * 1e6) ** (1 / 3)  # 1/m
    EF = (1.0545718e-34 * kF) ** 2 / (2 * 9.1093837e-31) / 1.602176634e-19
    vF = 1.0545718e-34 * kF / 9.1093837e-31 / 1e3
    # k_TF^2 = e^2 N(E_F) = 4 pi alpha * 3n/(2 E_F)  (natural units); in keV
    n_nat = n * (HBARC * 1e-13 / 1e-3) ** 3 * 1e-0  # n in keV^3: n[cm^-3] * (hbar c [keV cm])^3
    n_nat = n * (1.973269804e-8) ** 3
    kTF = math.sqrt(4 * math.pi * ALPHA * 1.5 * n_nat / (EF * 1e-3))
    add(m, "v_F_free_E", round(vF, 0), "km/s", "E", "R13 rho_T_DFT [DB]", f"free electron, {nval} e/atom", "Nb: d-band metal, free-electron value is a scale only")
    add(m, "E_F_free_E", round(EF, 2), "eV", "E", "R13 rho_T_DFT [DB]", f"free electron, {nval} e/atom",
        "Al: 2109.04473 uses E_F = 11.7 eV (R13 [FT])" if m == "Al" else "scale only")
    add(m, "k_TF_free_E", round(kTF, 2), "keV", "E", "R13 rho_T_DFT [DB]", "k_TF^2 = 4 pi alpha (3 n/2E_F)", "")
add("Nb", "Delta_BCS_E", round(1.764 * 8.617333e-2 * 10.72, 2), "meV", "E", f"{DBJ} JVASP-934 Tc_supercon 10.72 K",
    "Delta = 1.764 k_B T_c (weak-coupling BCS) with the DFT McMillan T_c", "DFT T_c; measured Nb T_c/Delta: GAP in sources read (IF-U6 still open)")
for m in SCREENED:
    th = r13f(m, "theta_D") or r13f(m, "theta_D_E")
    if th:
        add(m, "omega_bar_Debye_E", round(0.75 * 8.617333e-2 * th, 1), "meV", "E", "R13 theta_D", "(3/4) k_B theta_D (Debye-model first DOS moment)",
            "acoustic Debye model only; optical weight ignored; the true omega_bar_kappa needs the partial DOS (GAP)")

# ------------------------------------------------------------------------------------------------ 8. Al, Ir (WP8-R G-R5)
for m in ("Al", "Ir"):
    x = J[m]
    if m == "Ir":
        add("Ir", "rho_T_DFT", x["density"], "g/cm3", "DB", f"{DBJ} {x['jid']}", "density", "OptB88vdW cell")
    add(m, "B_G_Voigt_DFT", f"B_V {x['bulk_modulus_kv']}, G_V {x['shear_modulus_gv']}", "GPa", "DB", f"{DBJ} {x['jid']}",
        "bulk_modulus_kv, shear_modulus_gv", "WP8-R G-R5; measured moduli: GAP in sources read (closes the [UNVERIFIED] tag with a DB value)")
add("ALL", "Kaplan1979", "not accessed", "-", "GAP", "doi:10.1007/BF00119193", "Unpaywall: is_oa false (closed)", "Kaplan, JLTP 37, 343 (1979): G-R5 remains open for the tabulated transmissions")

# ------------------------------------------------------------------------------------------------ 9. S4 intrinsic radioactivity and cosmogenic 3H
def beta_shape(Q, Zd, T, unique=0):
    """Allowed (unique=0) or unique n-th forbidden beta spectrum dN/dT (unnormalised), T in keV.
    Non-relativistic Fermi function F0 = 2 pi eta/(1 - exp(-2 pi eta)), eta = alpha Zd W/p."""
    W = T + ME
    p = np.sqrt(np.clip(W ** 2 - ME ** 2, 1e-30, None))
    q = np.clip(Q - T, 0, None)
    eta = ALPHA * Zd * W / p
    F = 2 * np.pi * eta / (1 - np.exp(-2 * np.pi * eta))
    S = sum(p ** (2 * k) * q ** (2 * (unique - k)) / (math.factorial(2 * k + 1) * math.factorial(2 * (unique - k) + 1))
            for k in range(unique + 1))
    return F * p * W * q ** 2 * S


def frac(Q, Zd, a, b, unique=0, n=400001):
    T = np.linspace(1e-6, Q, n)
    y = beta_shape(Q, Zd, T, unique)
    tot = np.trapezoid(y, T)
    s = (T >= a) & (T <= b)
    return np.trapezoid(y[s], T[s]) / tot


def kn_dsdT0(Eg):
    """Klein-Nishina d sigma/dT at T -> 0 per electron (cm^2/keV): 2 pi r_e^2/(m_e k^2), k = E_g/m_e."""
    re2 = (2.8179403262e-13) ** 2
    k = Eg / ME
    return 2 * math.pi * re2 / (ME * k * k)


BUDGET = 1.0  # events/(kg day keV) below 1 keV (coordinator)
TAU = (1e-3, 1e-5)  # s, pile-up resolving times (phonon/TES readout, fast charge readout) [E]
F40K = frac(1311.07, 20, 0, 1.0, unique=3)
F115_allowed = frac(497.49, 50, 0, 1.0, unique=0)
F115_u4 = frac(497.49, 50, 0, 1.0, unique=4)
F3H = frac(18.591, 2, 0, 1.0)
json.dump({"f40K_sub1keV": F40K, "f115In_allowed": F115_allowed, "f115In_unique4": F115_u4, "f3H_sub1keV": F3H,
           "f3H_1to7": frac(18.591, 2, 1, 7), "f3H_0to5": frac(18.591, 2, 0, 5)},
          open(os.path.join(HERE, "data", "s4_fractions.json"), "w"), indent=1)


def iso_acts(m):
    out = []
    for e, n in comp(m).items():
        for r in IA:
            if r["sym"] == e and r["abundance_pct"] and r["half_life"] not in ("STABLE", "") and r["unit_hl"] == "Y":
                N = n * float(r["abundance_pct"]) / 100 * NA / Mfu(m) * 1000
                a = math.log(2) / (float(r["half_life"]) * YEAR) * N
                out.append((f"{r['A']}{e}", r["decay_1"], a, r["operator_hl"] in ("GT", "GE")))
    return out


def ne_cm3(m, rho):
    return rho * NA / Mfu(m) * sum(n * NIST[e]["Z"] for e, n in comp(m).items())


S4 = {}
for m in SCREENED:
    rho, _ = rho_best(m)
    acts = iso_acts(m)
    A_tot = sum(a for _, _, a, _ in acts)
    rate, parts, bound, cond = 0.0, [], 0.0, False
    for iso, mode, a, lower in acts:
        if iso == "40K":
            rb = a * 0.8928 * DAY * F40K
            L = (2 / 3) * (1000 / rho) ** (1 / 3)  # mean chord 4V/S of a 1 kg cube, cm
            rc = a * 0.1066 * DAY * ne_cm3(m, rho) * L * kn_dsdT0(1460.82)
            rate += rb + rc
            parts.append(f"40K beta {rb:.2e} (unique-3rd shape, f<1keV={F40K:.2e}) + 1461 keV Compton {rc:.2e} (cube chord {L:.1f} cm)")
        elif iso == "115In":
            rlo, rhi = a * DAY * F115_u4, a * DAY * F115_allowed
            rate += rhi
            parts.append(f"115In beta {rlo:.2e}-{rhi:.2e} (unique-4th to allowed shape bracket; upper used)")
        elif mode in ("A",):
            parts.append(f"{iso} alpha: deposit >> 1 keV, 0")
        elif "2B" in mode:
            K = np.linspace(1e-6, 1, 200001)
            Qr = {"48Ca": 4268, "100Mo": 3034, "82Se": 2998, "130Te": 2528, "128Te": 867, "70Zn": 997, "96Zr": 3356}.get(iso, 2000) / ME
            y = K * (K ** 4 + 10 * K ** 3 + 40 * K ** 2 + 60 * K + 30) * (Qr - K).clip(0) ** 5
            Kf = np.linspace(1e-6, Qr, 400001)
            yf = Kf * (Kf ** 4 + 10 * Kf ** 3 + 40 * Kf ** 2 + 60 * Kf + 30) * (Qr - Kf) ** 5
            kk = np.linspace(1e-9, 1 / ME, 2001)
            f = np.trapezoid(kk * (kk ** 4 + 10 * kk ** 3 + 40 * kk ** 2 + 60 * kk + 30) * (Qr - kk) ** 5, kk) / np.trapezoid(yf, Kf)
            rate += a * DAY * f
            parts.append(f"{iso} 2nu2beta (Primakoff-Rosen sum spectrum) {a * DAY * f:.1e}")
        else:  # EC / 2EC with only a lower half-life limit: conservative bound, all decays in the window
            b = a * DAY
            bound += b
            parts.append(f"{iso} {mode} (T1/2 lower limit) bound <= {b:.2e} if every capture deposited < 1 keV")
            cond = True
    pu = [1 - math.exp(-2 * A_tot * t) for t in TAU]
    if rate > BUDGET:
        v = "FAIL"
    elif cond and bound > BUDGET:
        v = "COND"
    else:
        v = "PASS"
    S4[m] = (v, rate, bound, A_tot, pu)
    add(m, "S4_intrinsic_sub1keV", f"{rate:.2e}", "/(kg day keV)", "E", "IAEA LiveChart + NIST (R13 a_rad) + decay shapes",
        "beta: allowed/unique-forbidden shape with non-rel. Fermi function; gamma: Klein-Nishina dsigma/dT(T->0) x n_e x mean chord of a 1 kg cube",
        "; ".join(parts) if parts else "no primordial radio-isotope among the constituents")
    add(m, "S4_pileup_1kg", f"{pu[0]:.2e} (1 ms); {pu[1]:.2e} (10 us)", "-", "E", "R13 specific_activity_intrinsic", "P = 1 - exp(-2 A tau), A for 1 kg",
        f"A = {A_tot:.3g} Bq at 1 kg")
    add(m, "S4_verdict", v, "-", "E", "S4 (coordinator criterion, budget 1 /(kg day keV) below 1 keV)", "",
        {"FAIL": "EXCLUDED-RADIO: intrinsic isotopes, not reducible", "COND": f"only a T1/2 lower limit: bound {bound:.2e} exceeds budget; measured EC branching needed",
         "PASS": "intrinsic sub-keV rate below budget"}[v])

# cosmogenic 3H (reducible): activity after t_exp at sea level and at saturation
lam3 = math.log(2) / (12.32 * 365.25)  # 1/day; T1/2 12.32 y (2506.06568 p.1 '12.3 years')
RATE3H = {"Si": 124, "Ge": 75, "NaI": 83}
for m in SCREENED:
    if m in RATE3H:
        R = RATE3H[m]
        for tag, t in (("100d", 100), ("sat", None)):
            A = R if t is None else R * (1 - math.exp(-lam3 * t))
            add(m, f"S4_cosmo_3H_{tag}", f"{A * F3H:.3g}", "/(kg day keV)", "E", "3H production rate [FT row cosmo_3H_rate]",
                "A(t) = R(1 - e^{-lambda t}); allowed 3H shape, f(<1 keV) = %.4f" % F3H,
                ("100 days sea-level exposure" if t else "saturation") + "; reducible (underground storage/fabrication; H outdiffusion, 2506.06568)")
        add(m, "S4_cosmo_verdict", "PASS (100 d) / " + ("FAIL" if R * F3H > BUDGET else "PASS") + " (saturation)", "-", "E", "S4 cosmogenic column", "",
            "reducible; other cosmogenics (Si: 32Si, 22Na, 7Be; Ge: 68Ge/68Ga, 65Zn, 55Fe; L/M-shell EC lines at 0.1-1.3 keV): GAP, rates not in full texts read")
    else:
        add(m, "GAP:S4_cosmo", "GAP", "-", "GAP", "-", "", "3H and other activation rates for this target not in full texts read; scale: 1706.05818 Table 1 gives 32-228 atoms/(kg day) over Na, I, Ge, Ar, Ne")

# ------------------------------------------------------------------------------------------------ 10. new GAP items from WP8-F 5.2
NONMETAL = [m for m in SCREENED if m not in NOGAP]
GAPS = [
    ("E_x_b", NONMETAL, "exciton binding energy not in the sources read"),
    ("E_min_q", NONMETAL, "indirect onset E_min(q) needs an ab initio band structure (tier H); not a tabulated property"),
    ("L_eps2_data", SCREENED, "measured L(q,omega)/eps2(omega) not tabulated here; WP8-F needs a src=data pointer per material"),
    ("phonon_DOS", SCREENED, "partial DOS D_kappa(omega) and omega_bar_kappa not in JARVIS dft_3d (Gamma modes only); needs DFPT or INS"),
    ("Zstar_tensor", [m for m in NONMETAL if META[m][1] not in ("elemental",)], "full Born tensors not in JARVIS dft_3d; only Zbar* (1910.10716) or Z*_LST [E]"),
    ("EPW_g_omegaTA_Qstar", NONMETAL, "tier H (EPW/ZG), pre-registered; not a database quantity"),
    ("tan_delta0_PSTM", SCREENED, "preparation-specific; measured per sample (WP8-F 5.2 row)"),
    ("E_st1_p_surv", SCREENED, "(prov.) WP7-E L36 caps exist for Si/Ge only; others need MD"),
    ("y_ion_QF", SCREENED, "(prov.) pending the joint WP5 + WP7-E audit (WP8-F IF-F3)"),
    ("alpha_th_integral", SCREENED, "integrated thermal contraction 300 K -> mK not in the sources read"),
    ("eps_bg", ["ZrTe5", "Bi2Se3"], "Dirac background dielectric not in the sources read (ZrTe5 DFPT eps are total, not eps_bg)"),
]
have = {(r["material"], r["property"]) for r in old + new}
for item, mats, why in GAPS:
    for m in mats:
        add(m, f"GAP:{item}", "GAP", "-", "GAP", "-", "", why)
for m in SCREENED:
    if J.get(m) is None or J[m]["elastic_tensor"] in (None, "na"):
        if (m, "GAP:c_dir") not in have:
            add(m, "GAP:c_dir", "GAP", "-", "GAP", "-", "", "no DB elastic tensor (JARVIS entry absent or without FD-ELAST); directional c_LA/c_TA and Y_mod need measured C_ij")
for m in ("CaWO4", "Li2MoO4"):
    add(m, "GAP:eps0_omegaLO_TO", "GAP", "-", "GAP", "-", "",
        "JARVIS " + ("JVASP-88542 has no DFPT/IR fields ('na')" if m == "CaWO4" else "has no Li2MoO4 entry") + "; no full-text IR/Raman data found on arXiv/Europe PMC")
add("YIG", "GAP:a_exp_measured", "GAP", "-", "GAP", "-", "", "experimental YIG lattice constant not in full texts read; IF-U7 remains open (1705.06594 gives no a)")

# ------------------------------------------------------------------------------------------------ 11. verdicts (S4)
FAIL = [m for m, v in S4.items() if v[0] == "FAIL"]
rows = []
for r in old:
    r = dict(r)
    if r["material"] in FAIL:
        if r["property"] == "verdict":
            r["value"] = "EXCLUDED-RADIO"
            r["note"] = f"supersedes R13 verdict={r['verdict']} (S4 FAIL, WP8-U-TOP)"
        r["verdict"] = "EXCLUDED-RADIO"
    rows.append(r)
for r in new:
    if r["material"] in FAIL:
        r["verdict"] = "EXCLUDED-RADIO"
rows += new
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, COLS)
    w.writeheader()
    w.writerows(rows)
json.dump({m: list(v) for m, v in S4.items()}, open(os.path.join(HERE, "data", "s4.json"), "w"), indent=1)
json.dump({m: list(v) for m, v in CHR.items()}, open(os.path.join(HERE, "data", "christoffel.json"), "w"), indent=1)
print(len(old), "R13 rows +", len(new), "new rows ->", OUT, "; S4 FAIL:", FAIL)
