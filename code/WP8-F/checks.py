#!/usr/bin/env python3
"""WP8-F checks: figures of merit per interaction channel (R13).

Closed-form and numpy/sympy checks only (no DFT/DFPT/MC). Each check is labelled WP8F-Cn and
compares two independent routes or verifies an identity used in returns/R13/WP8-F.md.
Inputs: [FT] values quoted in the return (page/table given there) and JARVIS-DFT [DB] fields
(JVASP IDs in the return). Run: python3 checks.py  (≈ 2 s; 39 checks).
"""
import math
import numpy as np
import sympy as sp
from scipy import integrate

RESULTS = []


def check(label, cond, msg=""):
    RESULTS.append((label, bool(cond), msg))
    print(f"{'PASS' if cond else 'FAIL'}  {label}  {msg}")


# ---------------------------------------------------------------- constants
alpha = 1 / 137.035999
c_kms = 299792.458
v_max = 794.5 / c_kms          # CONVENTIONS §8
m_u = 931.494e6                # eV
cm_inv_to_meV = 0.123984

# ---------------------------------------------------------------- C1: per-mass coherent acoustic one-phonon term
# WP2-v3 (2.2), n_ph = 1, G = 0, q << q_BZ, rigid acoustic eigenvector e_k = sqrt(M_k/M_cell) q_hat, c_k = A_k.
q, w, Om, c = sp.symbols('q omega Omega c', positive=True)
A1, A2, M1, M2 = sp.symbols('A1 A2 M1 M2', positive=True)
Mc = M1 + M2
amp = (A1 * q * sp.sqrt(M1 / Mc) / sp.sqrt(M1) + A2 * q * sp.sqrt(M2 / Mc) / sp.sqrt(M2))**2
S1_coef = (2 * sp.pi / Om) * amp / (2 * w)              # coefficient of delta(omega - c q)
per_mass = sp.simplify(S1_coef * Om / Mc)                 # 1/rho_T = Omega/M_cell
target = sp.pi * q**2 * (A1 + A2)**2 / (Mc**2 * w)
check("WP8F-C1a", sp.simplify(per_mass - target) == 0, "S^(1)_LA/rho_T = pi q^2 A_cell^2/(M_cell^2 omega)")
mu_ = sp.symbols('m_u', positive=True)
lim = sp.simplify(target.subs({M1: A1 * mu_, M2: A2 * mu_, w: c * q}))
check("WP8F-C1b", sp.simplify(lim - sp.pi * q / (mu_**2 * c)) == 0,
      "with M_k = A_k m_u: per-mass coefficient = pi q/(m_u^2 c_LA), A-independent")

# C1c: incoherent moments per mass with M_k = A_k m_u: first moment composition-free, zeroth moment ∝ <A>
mom1 = sp.simplify((2 * sp.pi / (A1 * mu_ + A2 * mu_)) * (A1**2 * q**2 / (2 * A1 * mu_) + A2**2 * q**2 / (2 * A2 * mu_)))
mom0 = sp.simplify((2 * sp.pi / (A1 * mu_ + A2 * mu_)) * (A1**2 + A2**2))
check("WP8F-C1c", sp.simplify(mom1 - sp.pi * q**2 / mu_**2) == 0 and sp.simplify(mom0 - 2 * sp.pi * (A1**2 + A2**2) / ((A1 + A2) * mu_)) == 0,
      "incoherent per-mass f-sum = pi q^2/m_u^2 (A-free); zeroth moment = 2 pi sum A^2/(A_cell m_u) ~ <A>")

# ---------------------------------------------------------------- C2: acoustic reach edge
m, v, wth = sp.symbols('m_chi v omega_th', positive=True)
# omega = c q <= q v - q^2/2m  ->  q <= 2 m (v - c); omega_max = 2 m c (v - c)
qmax = sp.solve(sp.Eq(c * q, q * v - q**2 / (2 * m)), q)
qmax = [s for s in qmax if s != 0][0]
check("WP8F-C2a", sp.simplify(qmax - 2 * m * (v - c)) == 0, "q_max = 2 m (v - c_LA)")
mmin = sp.solve(sp.Eq(c * qmax, wth), m)[0]
check("WP8F-C2b", sp.simplify(mmin - wth / (2 * c * (v - c))) == 0, "m_min = omega_th/(2 c (v_max - c))")
# numbers: Si c_LA from JARVIS K, G, rho (C12) and GaAs FT c_s = 4000 m/s; threshold 1 meV

# ---------------------------------------------------------------- C3: Froehlich FOM identity (diatomic, LST)
e2, Z, mu, eps_inf, wT = sp.symbols('e2 Zstar mu epsinf omegaT', positive=True)
eps0 = eps_inf + e2 * Z**2 / (Om * mu * wT**2)
wL2 = wT**2 + e2 * Z**2 / (Om * mu * eps_inf)
check("WP8F-C3a", sp.simplify(eps0 / eps_inf - wL2 / wT**2) == 0, "LST eps0/epsinf = wL^2/wT^2 for the one-mode model")
lhs = sp.sqrt(wL2) * (1 / eps_inf - 1 / eps0)
rhs = e2 * Z**2 / (Om * mu * eps_inf**2 * sp.sqrt(wL2))
check("WP8F-C3b", sp.simplify(lhs - rhs) == 0, "omega_L(1/epsinf - 1/eps0) = e^2 Z*^2/(Omega mu epsinf^2 omega_L)")

# ---------------------------------------------------------------- C4: integrated ELF of a polar branch and the KK 1/omega identity
def eps_multi(wv, einf, wLs, wTs, gL=None, gT=None):
    """Factorised (Kurosawa/Gervais) dielectric function; widths optional."""
    out = np.full_like(wv, einf, dtype=complex)
    for i, (L, T) in enumerate(zip(wLs, wTs)):
        gl = 0.0 if gL is None else gL[i]
        gt = 0.0 if gT is None else gT[i]
        out *= (L**2 - wv**2 - 1j * wv * gl) / (T**2 - wv**2 - 1j * wv * gt)
    return out


def elf_integrals(einf, wLs, wTs, gL, gT, wmax):
    wv = np.linspace(1e-4, wmax, 2_000_001)
    L = np.imag(-1 / eps_multi(wv, einf, wLs, wTs, gL, gT))
    return np.trapezoid(L, wv), np.trapezoid(L / wv, wv)


# one branch, small damping
einf1, wT1, wL1 = 10.89, 33.0, 36.0
eps01 = einf1 * (wL1 / wT1)**2
I0, I1 = elf_integrals(einf1, [wL1], [wT1], [0.05], [0.05], 400.0)
pred0 = math.pi * wL1 / 2 * (1 / einf1 - 1 / eps01)
pred1 = math.pi / 2 * (1 / einf1 - 1 / eps01)
check("WP8F-C4a", abs(I0 / pred0 - 1) < 0.01, f"int L domega = (pi wL/2)(1/epsinf-1/eps0): {I0:.5f} vs {pred0:.5f}")
check("WP8F-C4b", abs(I1 / pred1 - 1) < 0.01, f"int L/omega domega = (pi/2)(1/epsinf-1/eps0): {I1:.6f} vs {pred1:.6f}")

# sapphire, ordinary ray, 1807.10291 Table II p.31 [FT] (cm^-1), eps_inf = 3.2 (Table I p.11 [FT])
sap_o = dict(wL=[906.6, 629.5, 481.7, 387.6], gL=[16, 4.4, 1.4, 1.4],
             wT=[633.6, 569.0, 439.1, 385.0], gT=[3.8, 3.2, 1.5, 1.4])
sap_e = dict(wL=[881.1, 510.9], gL=[16, 1.4], wT=[582.4, 397.5], gT=[3.2, 1.5])
einf_sap = 3.2
for tag, d, eps0_ft in [("o", sap_o, 9.3), ("e", sap_e, 11.5)]:
    wL = np.array(d['wL']) * cm_inv_to_meV
    wT = np.array(d['wT']) * cm_inv_to_meV
    eps0_lst = einf_sap * np.prod((wL / wT)**2)
    check(f"WP8F-C5{tag}", abs(eps0_lst / eps0_ft - 1) < 0.07,
          f"sapphire ({tag}) multi-mode LST eps0 = {eps0_lst:.2f} vs Table I {eps0_ft} [FT vs FT]")
    gL = np.array(d['gL']) * cm_inv_to_meV
    gT = np.array(d['gT']) * cm_inv_to_meV
    I0, I1 = elf_integrals(einf_sap, wL, wT, gL, gT, 1500.0)
    pred1 = math.pi / 2 * (1 / einf_sap - 1 / eps0_lst)
    check(f"WP8F-C4c{tag}", abs(I1 / pred1 - 1) < 0.02,
          f"KK: int L/omega = {I1:.5f} vs (pi/2)(1/epsinf-1/eps0) = {pred1:.5f}")
    lo = pred1 * wT.min()
    hi = pred1 * wT.max() * math.sqrt(eps0_lst / einf_sap)
    check(f"WP8F-C6{tag}", lo <= I0 <= hi,
          f"DB-only bracket {lo:.2f} <= int L domega = {I0:.2f} meV <= {hi:.2f}")
    if tag == "o":
        sap_int_o = I0

# ---------------------------------------------------------------- C6b: bracket evaluated from JARVIS [DB] fields
# (dfpt_piezo_max_dielectric_electronic, _ionic, max_ir_mode, min_ir_mode in cm^-1); OptB88vdW DFPT.
jarvis = {  # JVASP id: (eps_el, eps_ion, w_min_ir, w_max_ir, rho_DB)
    "Al2O3 JVASP-32": (3.204, 8.803, 369.01, 613.17, 3.882),
    "AlN JVASP-39": (4.573, 4.976, 600.05, 653.02, 3.195),
    "GaN JVASP-30": (6.066, 5.250, 512.97, 532.99, 5.942),
    "MgO JVASP-116": (3.136, 7.148, 386.0, 386.0, 3.543),
}
brackets = {}
for k, (ee, ei, wmn, wmx, rho) in jarvis.items():
    e0 = ee + ei
    D = 1 / ee - 1 / e0
    lo = math.pi / 2 * D * wmn * cm_inv_to_meV
    hi = math.pi / 2 * D * wmx * cm_inv_to_meV * math.sqrt(e0 / ee)
    brackets[k] = (lo / rho, hi / rho)
    print(f"      {k}: int L domega / rho_T in [{lo/rho:.2f}, {hi/rho:.2f}] meV cm^3/g")
check("WP8F-C6db", all(a < b for a, b in brackets.values()), "DB brackets well ordered")
# sapphire FT value per mass lies in the JARVIS-based bracket (cross-source consistency)
lo, hi = brackets["Al2O3 JVASP-32"]
check("WP8F-C6x", lo <= sap_int_o / 3.98 <= hi,
      f"FT sapphire (o) int L/rho_T = {sap_int_o/3.98:.2f} within DB bracket [{lo:.2f}, {hi:.2f}]")

# GaAs one-branch Froehlich FOM [FT]: eps_inf 10.89, eps0 12.9 (1807.10291 Table I), omega_LO <= 34 meV (1910.08092 p.30)
gaas = math.pi / 2 * 34.0 * (1 / 10.89 - 1 / 12.9) / 5.32
print(f"      GaAs (pi wL/2)(1/epsinf-1/eps0)/rho_T <= {gaas:.3f} meV cm^3/g")
check("WP8F-C15", gaas < sap_int_o / 3.98, f"GaAs {gaas:.3f} < sapphire(o) {sap_int_o/3.98:.2f} meV cm^3/g (factor {sap_int_o/3.98/gaas:.0f})")

# ---------------------------------------------------------------- C7: ER q-weights and n_e/rho_T near-universality
qq = sp.symbols('q', positive=True)
qe = sp.symbols('q0', positive=True)
S_bar = qq**2                                            # (q^2/2 pi alpha) L with L flat in q
heavy = sp.simplify(qq * 1 * S_bar)
light = sp.simplify(qq * (qe / qq)**4 * S_bar)
check("WP8F-C7a", sp.simplify(heavy - qq**3) == 0 and sp.simplify(light - qe**4 / qq) == 0,
      "q-weights: heavy q^3 L, light (alpha m_e)^4 L/q")
Zs = {"H": 1, "Li": 3, "C": 6, "N": 7, "O": 8, "F": 9, "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "Ca": 20, "Ga": 31,
      "Ge": 32, "As": 33, "Cd": 48, "In": 49, "Sb": 51, "Te": 52, "I": 53, "W": 74}
As = {"H": 1.008, "Li": 6.94, "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "Na": 22.990, "Mg": 24.305,
      "Al": 26.982, "Si": 28.085, "Ca": 40.078, "Ga": 69.723, "Ge": 72.630, "As": 74.922, "Cd": 112.41,
      "In": 114.82, "Sb": 121.76, "Te": 127.60, "I": 126.90, "W": 183.84}
comp = {"Si": {"Si": 1}, "Ge": {"Ge": 1}, "C": {"C": 1}, "GaAs": {"Ga": 1, "As": 1}, "SiC": {"Si": 1, "C": 1},
        "Al2O3": {"Al": 2, "O": 3}, "CaWO4": {"Ca": 1, "W": 1, "O": 4}, "NaI": {"Na": 1, "I": 1},
        "LiF": {"Li": 1, "F": 1}, "CdTe": {"Cd": 1, "Te": 1}, "InSb": {"In": 1, "Sb": 1}, "W": {"W": 1},
        "C8H8 (polystyrene-like)": {"C": 8, "H": 8}}
ZA = {k: sum(n * Zs[e] for e, n in d.items()) / sum(n * As[e] for e, n in d.items()) for k, d in comp.items()}
print("      Z/A:", {k: round(v_, 3) for k, v_ in ZA.items()})
inorg = [v_ for k, v_ in ZA.items() if "C8H8" not in k]
check("WP8F-C7b", 0.40 <= min(inorg) and max(inorg) <= 0.50, f"Z/A in [{min(inorg):.3f}, {max(inorg):.3f}] for inorganic targets")
# f-sum per mass (pi/2) omega_p^2 / rho_T = (pi/2)(4 pi alpha/m_e)(Z/A)/m_u : ratio max/min
check("WP8F-C7c", max(inorg) / min(inorg) < 1.26, f"per-mass f-sum spread x{max(inorg)/min(inorg):.3f} (organics x{ZA['C8H8 (polystyrene-like)']/min(inorg):.2f})")

# ---------------------------------------------------------------- C8: Migdal per-mass scaling for m_chi << M
A, mchi, vv, mn, sig, ENs, M = sp.symbols('A m_chi v m_n sigma_n E_N M', positive=True)
dsig = M * A**2 * sig / (2 * mn**2 * vv**2)           # fixed sigma_n; regime m_n << m_chi << M (mu_n ~ m_n, mu_N ~ m_chi)
P = 2 * ENs / M                                         # v_N^2 times the ELF moment (factored out)
Emax = 2 * mchi**2 * vv**2 / M
rate_pm = sp.simplify((1 / M) * sp.integrate(dsig * P, (ENs, 0, Emax)))
check("WP8F-C8", sp.simplify(rate_pm - 2 * A**2 * sig * mchi**4 * vv**2 / (mn**2 * M**3)) == 0,
      "Migdal per mass ∝ A^2 m_chi^4/M^3 (m_n << m_chi << M, fixed sigma_n) = (1/A) m_chi^4/m_u^3 (×Z_k^2 ELF moment)")

# ---------------------------------------------------------------- C9: free-NR edge
Eth = sp.symbols('E_th', positive=True)
mu_chiN = mchi * M / (mchi + M)
sol = sp.solve(sp.Eq(2 * mu_chiN**2 * vv**2 / M, Eth), mchi)
sol = [s for s in sol if s.is_positive is not False]
mm = sp.simplify(sol[0])
approx = sp.sqrt(M * Eth / 2) / vv
ratio = sp.limit(mm / approx, M, sp.oo)
check("WP8F-C9a", sp.simplify(ratio - 1) == 0, "m_min -> sqrt(M E_th/2)/v_max for m_chi << M")
for name, A_ in [("Si", 28.085), ("Ge", 72.63), ("O(in Al2O3)", 15.999)]:
    Mv = A_ * m_u
    val = float(mm.subs({M: Mv, Eth: 10.0, vv: v_max})) / 1e6
    print(f"      free NR m_min({name}, E_th = 10 eV) = {val:.0f} MeV")
check("WP8F-C9b", 130 < float(mm.subs({M: 28.085 * m_u, Eth: 10.0, vv: v_max})) / 1e6 < 145, "Si m_min(10 eV) ≈ 0.14 GeV")

# ---------------------------------------------------------------- C10: background-free vs background-limited reach
def asimov_Z2(s, b):
    return 2 * np.sum((s + b) * np.log1p(s / b) - s)


s = np.array([0.01, 0.02, 0.03]); b = np.array([10.0, 20.0, 5.0])
check("WP8F-C10a", abs(asimov_Z2(s, b) / np.sum(s**2 / b) - 1) < 2e-3, "Asimov Z^2 -> sum s^2/b for s << b")
# background-free 90% CL: s_up = -ln(0.1) = 2.303 events
check("WP8F-C10b", abs(-math.log(0.1) - 2.3026) < 1e-3, "zero-background 90% CL: 2.303 events")
# exposure scaling of the limit on the coupling^2 (sigma) for fixed rate FOM r and background b per exposure
r, bb = 1.0, 50.0
MT = np.array([1e2, 1e4])
sig_bl = 1.64 * np.sqrt(bb * MT) / (r * MT)            # Z = s/sqrt(b) = 1.64
check("WP8F-C10c", abs(np.log(sig_bl[0] / sig_bl[1]) / np.log(MT[1] / MT[0]) - 0.5) < 1e-9, "background-limited sigma ∝ (MT)^-1/2")
fsys = 0.05
sig_sys = 1.64 * np.sqrt(bb * MT + (fsys * bb * MT)**2) / (r * MT)
check("WP8F-C10d", abs(sig_sys[1] / (1.64 * fsys * bb / r) - 1) < 0.02, "systematics floor sigma -> Z f_sys b / r (exposure independent)")

# ---------------------------------------------------------------- C11: dark-photon absorption identity
e1, e2_ = sp.symbols('epsilon1 epsilon2', real=True)
wq = sp.symbols('omega', positive=True)
eps = e1 + sp.I * e2_
sigma1 = wq * e2_                                       # HL units: eps = 1 + i sigma/omega
lhs = sigma1 / (e1**2 + e2_**2)
rhs = wq * sp.im(-1 / eps)
check("WP8F-C11", sp.simplify(lhs - sp.simplify(rhs)) == 0, "kappa_eff^2 sigma_1 = kappa^2 omega Im[-1/eps]")

# ---------------------------------------------------------------- C12: sound speeds from JARVIS K, G, rho [DB]
GPa = 1e9
db = {"Si JVASP-1002": (87.27, 63.28, 2.25), "C JVASP-91": (437.4, 522.66, 3.50), "SiC JVASP-8158": (212.77, 197.62, 3.153),
      "GaAs JVASP-1174": (61.93, 42.32, 5.102), "Al2O3 JVASP-32": (241.28, 156.49, 3.882), "Ge JVASP-890": (58.07, 43.96, 5.054),
      "NaI JVASP-1996": (17.93, 10.88, 3.746), "CaF2 JVASP-20800": (88.13, 44.06, 3.175), "LiF JVASP-1130": (73.93, 55.28, 2.662)}
cs = {}
for k, (K, G, rho) in db.items():
    cL = math.sqrt((K + 4 * G / 3) * GPa / (rho * 1e3)) / 1e3
    cT = math.sqrt(G * GPa / (rho * 1e3)) / 1e3
    cs[k] = (cL, cT)
    print(f"      {k}: c_L = {cL:.2f}, c_T = {cT:.2f} km/s (isotropic Voigt average, DB)")
check("WP8F-C12a", cs["GaAs JVASP-1174"][1] < 4.0 < cs["GaAs JVASP-1174"][0],
      "GaAs DB c_T..c_L brackets the FT 'c_s ~ 4000 m/s' (1807.10291 p.6)")
check("WP8F-C12b", cs["Al2O3 JVASP-32"][0] > 9.0, "sapphire DB c_L ~ 1e4 m/s as in 1807.10291 p.6")
# acoustic per-mass rate coefficient pi q/(m_u^2 c_L) and edge m_min(1 meV): opposite orderings
order_rate = sorted(cs, key=lambda k: -1 / cs[k][0])
mmins = {k: 1e-3 / (2 * (cs[k][0] / c_kms) * (v_max - cs[k][0] / c_kms)) / 1e3 for k in cs}   # keV
print("      acoustic edge m_min(omega_th = 1 meV) [keV]:", {k.split()[0]: round(v_, 1) for k, v_ in mmins.items()})
check("WP8F-C12c", min(mmins, key=mmins.get) == "C JVASP-91" and min(cs, key=lambda k: cs[k][0]) == "NaI JVASP-1996",
      "highest c_L has the lowest acoustic edge (diamond); lowest c_L the largest per-mass coefficient (NaI)")

# ---------------------------------------------------------------- C13: tritium FT-vs-shape consistency (Si)
# 2506.06568 p.1 [FT]: 124 atoms/kg/day production, 0.002 /kg/keV/day (0-5 keV) per day of exposure.
T12_d = 12.32 * 365.25    # tritium half-life [UNVERIFIED, standard value]
decays = 124 * math.log(2) / T12_d               # decays /kg/day per exposure-day
Q = 18.6                                         # keV endpoint [FT, 2506.06568 p.1]
me = 511.0
def beta_shape(T):
    E = T + me; p = math.sqrt(E**2 - me**2); eta = 2 * alpha * E / p
    F = 2 * math.pi * eta / (1 - math.exp(-2 * math.pi * eta))
    return p * E * (Q - T)**2 * F
tot = integrate.quad(beta_shape, 0, Q)[0]; low = integrate.quad(beta_shape, 0, 5.0)[0]
pred = decays * low / tot / 5.0
check("WP8F-C13", abs(pred / 0.002 - 1) < 0.35, f"Si 3H: {pred:.4f} /kg/keV/day per exposure-day (0-5 keV) vs FT 0.002")

# ---------------------------------------------------------------- C14: required accuracy from log-sensitivities
d_rank = 0.2   # ranking resolution in ln(FOM) [E]
sens = {"E_th (ER edge, m_min ∝ E_th)": 1, "E_th (rate near edge, 7/2+k+p_on with p_on=3, Δm/m=5%)": None,
        "Z* (polar, ∝ Z*^2)": 2, "eps_inf (polar, ∝ eps_inf^-2)": 2, "c_L (acoustic rate ∝ 1/c_L)": 1,
        "rho_T (all per-mass FOMs)": 1, "n_s (magnon ∝ n_s)": 1, "A (Migdal ∝ 1/A)": 1, "tan delta0 (TLS abs)": 1}
acc = {k: (d_rank / s_ if s_ else None) for k, s_ in sens.items()}
check("WP8F-C14", abs(acc["Z* (polar, ∝ Z*^2)"] - 0.1) < 1e-12 and abs(acc["E_th (ER edge, m_min ∝ E_th)"] - 0.2) < 1e-12,
      "accuracy = 0.2/|dlnFOM/dlnx|: Z*, eps_inf 10%; rho, c_L, n_s 20% ")
# near-edge rate: ln R ∝ (13/2) ln δv0; δv0/v_max = 1 - sqrt(m_min/m): at m = 1.05 m_min, dlnR/dlnE_th
mm_ = 1.05
dv0 = 1 - math.sqrt(1 / mm_)
dlnR_dlnE = 6.5 * (0.5 * math.sqrt(1 / mm_)) / dv0      # d ln δv0/d ln E_th = -(1/2)(v*/δv0)
print(f"      near-edge |dlnR/dlnE_th| at 1.05 m_min = {dlnR_dlnE:.0f} -> E_th accuracy {d_rank/dlnR_dlnE*100:.2f}%")
check("WP8F-C14b", 100 < dlnR_dlnE < 200, "near-edge rate needs E_th to ~0.1-0.2% (≈ 1-2 meV at 1.17 eV)")

# ---------------------------------------------------------------- C16: ER edge numbers reproduce WP6-v3 (3.1)
for name, Eg, ref in [("Si E_g 1.170 eV", 1.170, 0.3332), ("Ge E_g 0.744 eV", 0.744, 0.212), ("Si E_x 1.1553 eV", 1.170 - 0.0147, 0.329)]:
    val = 2 * Eg / v_max**2 / 1e6
    check(f"WP8F-C16 {name}", abs(val - ref) < 0.0015, f"2E/v_max^2 = {val:.4f} MeV vs WP6-v3 {ref}")

# ---------------------------------------------------------------- C17: polar edge and one-branch edge masses
for name, wLO in [("GaAs omega_LO <= 34 meV [FT]", 0.034), ("sapphire top LO 906.6 cm^-1 [FT]", 906.6 * cm_inv_to_meV * 1e-3),
                  ("sapphire lowest LO 387.6 cm^-1 [FT]", 387.6 * cm_inv_to_meV * 1e-3)]:
    print(f"      optical edge 2 omega_LO/v_max^2 ({name}) = {2 * wLO / v_max**2 / 1e3:.1f} keV")
check("WP8F-C17", abs(2 * 0.034 / v_max**2 / 1e3 - 9.7) < 0.2, "GaAs LO edge ≈ 9.7 keV")

# ---------------------------------------------------------------- summary
n_pass = sum(1 for _, ok, _ in RESULTS if ok)
print(f"\n{n_pass}/{len(RESULTS)} checks PASS")
if n_pass != len(RESULTS):
    raise SystemExit(1)
