#!/usr/bin/env python3
"""WP8-R checks: mode-selective phonon collection as an NR/ER discriminant (order-of-magnitude screen).

Deterministic closed-form / linear-algebra checks only (no Monte Carlo, no first-principles numerics).
Cited in returns/R13/WP8-R.md as WP8R-Cn.  Run:  python3 checks.py   (< 30 s)
Units: SI inside this script; phonon frequencies f = omega/2pi in Hz (source form of the rate laws).
"""
import math, sys
import numpy as np
import sympy as sp
from scipy.linalg import expm

RESULTS = []
def check(name, cond, info=""):
    RESULTS.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}  {info}")

# ---------------------------------------------------------------- inputs (provenance in the return, Table 2.1/3.1)
# Source-form rates Gamma_anh = A f^5 (L phonons only), Gamma_iso = B f^4 (all acoustic modes).
SRC = {
 'Si': dict(A=7.41e-56, B=2.43e-42, vL=9000., vT=5400., rho=2330., xL=0.093, fD=1.5e13,  Eg=1.17, eps=3.75, Z=14, Am=28.09),
 'Ge': dict(A=1.61e-55, B=3.67e-41, vL=5310., vT=3250., rho=5320., xL=0.098, fD=0.864e13, Eg=0.75, eps=2.96, Z=32, Am=72.63),
}
A_GE_RANGE = [1.61e-55, 6.43e-55, 6.8e-55, 16.5e-55]   # Hertel-Pyle / Leman / 2408.04732 calc / 2408.04732 lit
h_meV_per_THz = 4.135667696   # meV per THz (h)
L_CRYS = 0.01                 # 1 cm crystal
T_COLL = [20e-6, 100e-6]      # collection-time range (CPD rise 20 us; CDMS/CPD fall ~100 us)

# ---------------------------------------------------------------- C1: crossover frequencies
def f_star(m, t, A=None):
    """frequency at which the mode-mixed L-decay rate x_L A f^5 equals 1/t"""
    A = m['A'] if A is None else A
    return (m['xL'] * A * t) ** (-0.2)

for mat, m in SRC.items():
    fs = {t: f_star(m, t) for t in (1e-9, 1e-7, 1e-6, 1e-5, 1e-4)}
    print(mat, 'f*(t) [THz]:', {f"{t:.0e}": round(v / 1e12, 2) for t, v in fs.items()})
    # isotope rate = full L-decay rate at f_eq = B/A
    f_eq = m['B'] / m['A']
    check(f"C1a {mat}: isotope scattering faster than L decay below f_eq=B/A = {f_eq/1e12:.0f} THz (> Debye)",
          f_eq > m['fD'])
    check(f"C1b {mat}: f*(1 us) in 1-4 THz (quasi-diffusive at 1 us)", 1e12 < fs[1e-6] < 4e12, f"{fs[1e-6]/1e12:.2f} THz")
    # ratio Gamma_iso/Gamma_anh,L at 10 THz (advisor: only ~3x in Si)
    print(f"   {mat}: Gamma_iso/Gamma_anh,L at 10 THz = {m['B']/(m['A']*1e13):.2f}")
# insensitivity of f* to the Ge A spread (A^-1/5)
fsr = [f_star(SRC['Ge'], 1e-6, A) for A in A_GE_RANGE]
check("C1c Ge: the factor-10 spread in A moves f*(1 us) only by (A_max/A_min)^(1/5) <= 1.6",
      abs(max(fsr) / min(fsr) - (max(A_GE_RANGE) / min(A_GE_RANGE)) ** 0.2) < 1e-9 and max(fsr) / min(fsr) < 1.6,
      f"{[round(x/1e12,2) for x in fsr]} THz")

# ---------------------------------------------------------------- C2: mean free paths and ballistic thresholds
for mat, m in SRC.items():
    vbar = (m['vL'] + 2 * m['vT']) / 3
    f_b_iso = (vbar / (m['B'] * L_CRYS)) ** 0.25           # l_iso = 1 cm
    f_b_anh = (vbar / (m['xL'] * m['A'] * L_CRYS)) ** 0.2   # one crossing per decay time
    l1 = vbar / (m['B'] * 1e48)
    print(f"{mat}: l_iso(1 THz) = {l1*1e3:.2f} mm; l_iso(10 THz) = {vbar/(m['B']*1e52)*1e6:.2f} um; "
          f"f_b(iso)={f_b_iso/1e12:.2f} THz, f_b(anh)={f_b_anh/1e12:.2f} THz")
    check(f"C2a {mat}: ballistic (1 cm) threshold below 1.5 THz", f_b_iso < 1.5e12 and f_b_anh < 3e12)
    # polarisation memory: number of isotope (mode-mixing) events integrated along f*(t), up to 1 us
    c = m['xL'] * m['A']
    nmix = 5 * m['B'] * c ** (-0.8) * (1e-6) ** 0.2
    check(f"C2b {mat}: >100 mode-mixing events by 1 us (polarisation memory lost)", nmix > 100, f"N_mix={nmix:.0f}")
    # diffusive spread up to t: <r^2> = 6 int D dt, D = vbar^2/(3 Gamma_iso(f*(t)))
    def r_rms(t):
        return math.sqrt(6 * vbar ** 2 / (3 * m['B']) * c ** 0.8 * t ** 1.8 / 1.8)
    print(f"   {mat}: r_rms(100 ns) = {r_rms(1e-7)*1e6:.0f} um, r_rms(1 us) = {r_rms(1e-6)*1e6:.0f} um")
    check(f"C2c {mat}: diffusive spread at 100 ns << 1 cm", r_rms(1e-7) < 1e-3)

# ---------------------------------------------------------------- C3: toy energy-cascade rate equation (deterministic, [E])
def cascade_distance(mat, ts):
    m = SRC[mat]
    edges = np.logspace(np.log10(0.05e12), np.log10(20e12), 241)
    fc = np.sqrt(edges[1:] * edges[:-1]); N = fc.size
    # daughter energy fraction x ~ Beta(3,3) (toy, symmetric, broad as Leman Fig. 8)
    xs = np.linspace(0.0005, 0.9995, 2000); px = 30 * xs ** 2 * (1 - xs) ** 2; px /= px.sum()
    K = np.zeros((N, N))
    for j in range(N):
        for frac in (xs, 1 - xs):
            idx = np.clip(np.searchsorted(edges, frac * fc[j]) - 1, 0, N - 1)
            np.add.at(K[:, j], idx, px * frac)
    colsum = K.sum(0)
    G = m['xL'] * m['A'] * fc ** 5
    Mgen = (K - np.eye(N)) * G[None, :]
    # initial energy spectra (normalised)
    fD = min(m['fD'], 19e12)
    nr = np.where(fc < fD, fc ** 3 * (fc[1] / fc[0] - 1) * fc, 0.0); nr /= nr.sum()       # Debye energy density x bin width
    hard = np.exp(-0.5 * ((fc - 0.95 * fD) / (0.05 * fD)) ** 2); hard /= hard.sum()       # optical / intervalley proxy
    soft = np.where((fc > 0.3e12) & (fc < 1.4e12), 1.0, 0.0); soft /= soft.sum()
    fs_ER = 0.017 if mat == 'Si' else 0.0125
    er = (1 - fs_ER) * hard + fs_ER * soft
    out = []
    for t in ts:
        E = expm(Mgen * t)
        a, b, b0 = E @ nr, E @ er, E @ hard
        tv = 0.5 * np.abs(a / a.sum() - b / b.sum()).sum()
        tv0 = 0.5 * np.abs(a / a.sum() - b0 / b0.sum()).sum()
        out.append((t, tv, tv0, (E @ nr).sum()))
    return colsum, out, fc

for mat in ('Si', 'Ge'):
    ts = [0.0, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4]
    colsum, out, fc = cascade_distance(mat, ts)
    check(f"C3a {mat}: cascade kernel conserves energy per decay", np.allclose(colsum, 1, atol=1e-9))
    check(f"C3b {mat}: total energy conserved by the evolution", all(abs(o[3] - 1) < 1e-6 for o in out))
    tv_full = [o[1] for o in out]; tv_hard = [o[2] for o in out]
    print(f"   {mat} TV(NR,ER) vs t:", [f"{o[0]:.0e}:{o[1]:.3f}/{o[2]:.3f}" for o in out])
    check(f"C3c {mat}: hard-part distance decreases monotonically for t >= 1 ns",
          all(tv_hard[i + 1] <= tv_hard[i] + 1e-9 for i in range(2, len(ts) - 1)))
    i100n = ts.index(1e-7)
    check(f"C3d {mat}: hard-part memory lost (TV < 0.05) by 100 ns", tv_hard[i100n] < 0.05, f"{tv_hard[i100n]:.4f}")
    i10u = ts.index(1e-5)
    check(f"C3e {mat}: full NR/ER spectral distance at 10 us <= ER soft fraction (+ binning)",
          tv_full[i10u] <= 0.02, f"{tv_full[i10u]:.4f}")

# ---------------------------------------------------------------- C4: AMM / DMM interface transmission
MAT = {  # rho [kg/m3], vL, vT [m/s]
 'Si': (2330., 9000., 5400.), 'Ge': (5320., 5310., 3250.),
 'Al2O3': None, 'Al': (2720., None, None), 'W': (18560., None, None), 'Ti': (4265., None, None), 'Ir': (21980., None, None)}
def from_moduli(rho, K=None, G=None, lam=None, mu=None):
    if lam is not None:
        return rho, math.sqrt((lam + 2 * mu) * 1e9 / rho), math.sqrt(mu * 1e9 / rho)
    return rho, math.sqrt((K + 4 * G / 3) * 1e9 / rho), math.sqrt(G * 1e9 / rho)
MAT['Al2O3'] = from_moduli(3866., lam=139.8, mu=166.24)  # 2408.04732 Table 3 [FT]; rho AFLOW [DB]
MAT['Al'] = from_moduli(2720., K=76., G=26.)             # moduli [UNVERIFIED]; rho AFLOW [DB]
MAT['W'] = from_moduli(18560., K=297.672, G=150.536)     # AFLOW aflow:b36865785bd06095 [DB]
MAT['Ti'] = from_moduli(4265., K=113.529, G=63.5361)     # AFLOW aflow:ece991e1e336aa44 [DB]
MAT['Ir'] = from_moduli(21980., K=320., G=210.)          # moduli [UNVERIFIED]; rho AFLOW [DB]
for k, v in MAT.items():
    print(f"   {k}: rho={v[0]:.0f}, vL={v[1]:.0f}, vT={v[2]:.0f}")
check("C4a Si sound speeds from 2408.04732 (mu, lambda) agree with Leman Table I to 1%",
      abs(from_moduli(2330., lam=53.68, mu=68.58)[1] / 9000 - 1) < 0.01 and abs(from_moduli(2330., lam=53.68, mu=68.58)[2] / 5400 - 1) < 0.01)

def T_norm(Z1, Z2): return 4 * Z1 * Z2 / (Z1 + Z2) ** 2
def T_SH(m1, m2, th1):
    r1, _, v1 = m1; r2, _, v2 = m2
    s2 = v2 / v1 * np.sin(th1)
    c1 = np.cos(th1); c2 = np.sqrt(np.clip(1 - s2 ** 2, 0, None))
    Z1, Z2 = r1 * v1, r2 * v2
    T = 4 * Z1 * c1 * Z2 * c2 / (Z1 * c1 + Z2 * c2) ** 2
    return np.where(s2 < 1, T, 0.0)
def T_SH_avg(m1, m2, n=20001):
    th = np.linspace(0, np.pi / 2, n)
    w = 2 * np.sin(th) * np.cos(th)
    return np.trapezoid(T_SH(m1, m2, th) * w, th)
def T_DMM(m1, m2):
    s1 = m1[1] ** -2 + 2 * m1[2] ** -2; s2 = m2[1] ** -2 + 2 * m2[2] ** -2
    return s2 / (s1 + s2)
PAIRS = [('Si', 'Al'), ('Si', 'W'), ('Si', 'Ti'), ('Si', 'Ir'), ('Ge', 'Al'), ('Al2O3', 'Al')]
amm = {}
for s, f in PAIRS:
    m1, m2 = MAT[s], MAT[f]
    TL = T_norm(m1[0] * m1[1], m2[0] * m2[1]); TT = T_norm(m1[0] * m1[2], m2[0] * m2[2])
    Tsh = T_SH_avg(m1, m2); Td = T_DMM(m1, m2)
    amm[(s, f)] = (TL, TT, Tsh, Td)
    print(f"   {s}/{f}: AMM normal L {TL:.3f}, T {TT:.3f}; SH flux-avg {Tsh:.3f}; DMM {Td:.3f}; L/T contrast {TL/TT:.2f}")
# reciprocity of SH transmission T12(th1) = T21(th2) and T+R=1 at normal incidence
m1, m2 = MAT['Si'], MAT['Al']; th1 = 0.6
th2 = math.asin(m2[2] / m1[2] * math.sin(th1))
check("C4b SH-AMM reciprocity T_12(th1) = T_21(th2) (Si/Al)", abs(float(T_SH(m1, m2, th1)) - float(T_SH(m2, m1, th2))) < 1e-12)
Z1, Z2 = sp.symbols('Z1 Z2', positive=True)
check("C4c AMM normal incidence T + R = 1 (symbolic)", sp.simplify(4 * Z1 * Z2 / (Z1 + Z2) ** 2 + ((Z1 - Z2) / (Z1 + Z2)) ** 2 - 1) == 0)
check("C4d DMM detailed balance T_12 + T_21 = 1", abs(T_DMM(MAT['Si'], MAT['Al']) + T_DMM(MAT['Al'], MAT['Si']) - 1) < 1e-12)
check("C4e all listed pairs: AMM normal-L transmission in [0.3, 1]", all(0.3 <= v[0] <= 1 for v in amm.values()))
# NR/ER contrast from mode-selective transmission after mixing: Delta x_L ~ exp(-N_mix) -> 0
check("C4f mode-selective (L vs T) NR/ER contrast <= |T_L/T_T - 1| * exp(-N_mix) < 1e-6",
      max(abs(v[0] / v[1] - 1) for v in amm.values()) * math.exp(-100) < 1e-6)

# ---------------------------------------------------------------- C5: pair-breaking efficiency vs phonon frequency (WP5 (W13))
Delta_Al_meV = 0.18   # [UNVERIFIED]
f2D = 2 * Delta_Al_meV / h_meV_per_THz; f4D = 2 * f2D
def eta_pb(f):  # WP5 (W13) limits: 2Delta/Omega for 2Delta<=Omega<4Delta; asymptote ~0.57-0.6 (1401.1937 via WP5-v3)
    if f < f2D: return 0.0
    if f < f4D: return f2D / f
    return None
check("C5a eta_pb = 2Delta/Omega in [1/2, 1] on [2Delta, 4Delta)",
      all(0.5 - 1e-12 <= eta_pb(f) <= 1 for f in np.linspace(f2D, f4D * 0.999, 50)))
check("C5b 4Delta_BCS(Al) < 0.2 THz: every arriving primary/NTL phonon (>= 0.3 THz) is on the flat (asymptotic) branch",
      f4D < 0.2, f"2D={f2D*1e3:.0f} GHz, 4D={f4D*1e3:.0f} GHz")
# film-gap selectivity: a higher-gap film (Nb, 2Delta ~ 3.0 meV [UNVERIFIED]) cuts at:
f_Nb = 3.0 / h_meV_per_THz
check("C5c Nb-like 2Delta cut (~0.73 THz) lies between Ge NTL (0.3/0.7 THz) and primary arrival (>=0.7 THz)", 0.6 < f_Nb < 0.8,
      f"{f_Nb:.2f} THz")

# ---------------------------------------------------------------- C6: Lindhard yield (WP5 L20 form)
def lindhard(Z, Am, ER_keV):
    k = 0.133 * Z ** (2 / 3) * Am ** -0.5
    e = 11.5 * Z ** (-7 / 3) * ER_keV
    g = 3 * e ** 0.15 + 0.7 * e ** 0.6 + e
    return k * g / (1 + k * g)
y100 = {m: lindhard(SRC[m]['Z'], SRC[m]['Am'], 0.1) for m in SRC}
print("   Lindhard yield at 100 eV:", {k: round(v, 3) for k, v in y100.items()})
check("C6a Lindhard yield (100 eV): Si in [0.12, 0.18], Ge in [0.08, 0.14]", 0.12 < y100['Si'] < 0.18 and 0.08 < y100['Ge'] < 0.14)
check("C6b Lindhard yield monotone increasing 50 eV -> 10 keV (Si)",
      all(lindhard(14, 28.09, a) < lindhard(14, 28.09, b) for a, b in zip([0.05, 0.1, 0.3, 1], [0.1, 0.3, 1, 10])))

# ---------------------------------------------------------------- C7: figure of merit algebra
aP, aL, P, L = sp.symbols('alpha_p alpha_L P L', positive=True)
O = (aP * P + aL * L) / (P + L)
FL = sp.Symbol('F_L')
check("C7a O = alpha_p + (alpha_L - alpha_p) F_L with F_L = L/(P+L)",
      sp.simplify(O - (aP + (aL - aP) * L / (P + L))) == 0)
g, y = sp.symbols('g y', positive=True)
FER = g / (1 + g); FNR = y * g / (1 + y * g)
dF = sp.simplify(FER - FNR)
check("C7b Delta F_L = g(1-y)/((1+g)(1+yg))", sp.simplify(dF - g * (1 - y) / ((1 + g) * (1 + y * g))) == 0)
gopt = sp.solve(sp.diff(dF, g), g)
check("C7c Delta F_L maximal at g = y^(-1/2), value (1-sqrt y)/(1+sqrt y)",
      any(sp.simplify(go - 1 / sp.sqrt(y)) == 0 for go in gopt) and
      sp.simplify(dF.subs(g, 1 / sp.sqrt(y)) - (1 - sp.sqrt(y)) / (1 + sp.sqrt(y))) == 0)

def fom(ER, mat='Si', Vb=4.0, C=0.3, dalpha=0.05, sigE=2.65, F_ER=0.15, F_NR=1.0, y=None):
    """pooled separation of O between NR (recoil ER [eV]) and ER of equal total phonon energy (HV/NTL route)."""
    m = SRC[mat]; eps = m['eps']; yy = y100[mat] if y is None else y
    gg = Vb / eps
    Etot = ER * (1 + yy * gg)
    E_er = Etot / (1 + gg)
    n_nr, n_er = yy * ER / eps, E_er / eps
    dO = C * (gg / (1 + gg) - yy * gg / (1 + yy * gg))
    s_noise = sigE / Etot
    s_nr = math.sqrt(s_noise ** 2 + dalpha ** 2 + (C * Vb * math.sqrt(F_NR * n_nr) / Etot) ** 2)
    s_er = math.sqrt(s_noise ** 2 + dalpha ** 2 + (C * Vb * math.sqrt(F_ER * n_er) / Etot) ** 2)
    return dO / math.sqrt(0.5 * (s_nr ** 2 + s_er ** 2))
def fom_int(ER, mat='Si', Vb=4.0, F_ER=0.15, F_NR=1.0):
    """pair-number ceiling: C = 1, no noise, no position term"""
    return fom(ER, mat, Vb, 1.0, 0.0, 1e-9, F_ER, F_NR)
# primary (zero-field, mode-selective) route: only the soft-fraction difference survives
def fom_prim(ER, mat='Si', C=1.0, sigE=2.65, dalpha=0.0):
    fs = 0.017 if mat == 'Si' else 0.0125
    d = C * (1 - y100[mat]) * fs
    return d / math.sqrt((math.sqrt(2) * sigE / ER) ** 2 + dalpha ** 2)
print("   primary-route S (C=1, no position term):", {E: round(fom_prim(E), 2) for E in (50, 100, 300, 1000, 3000)})
E2 = {C: min(E for E in np.arange(10, 1e5, 1.0) if fom_prim(E, C=C) >= 2) for C in (1.0, 0.3)}
print("   primary route: E_R at which S = 2 (no position term):", E2)
check("C7d primary route: S < 2 for E_R <= 300 eV even at C = 1 and zero position spread; 2 sigma needs >= 0.5 keV (C=1), >= 1.5 keV (C=0.3)",
      all(fom_prim(E) < 2 for E in (50, 100, 300)) and E2[1.0] > 500 and E2[0.3] > 1500)
check("C7e primary route with 2% residual position spread: S < 1 at every energy",
      all(fom_prim(E, dalpha=0.02) < 1 for E in (50, 100, 300, 1e3, 1e4, 1e5)))
print("   NTL route S table (Si, sigma_E=2.65 eV):")
grid = {}
for Vb in (2, 4, 10, 100):
    for C in (0.1, 0.3, 0.5, 1.0):
        for da in (0.02, 0.05, 0.1):
            row = [fom(E, 'Si', Vb, C, da) for E in (50, 100, 300, 1000)]
            grid[(Vb, C, da)] = row
    print(f"     Vb={Vb:>3} V: C=0.3,da=0.05 -> {[round(x,2) for x in grid[(Vb,0.3,0.05)]]};"
          f"  C=0.5,da=0.02 -> {[round(x,2) for x in grid[(Vb,0.5,0.02)]]};  ceiling {[round(fom_int(E,'Si',Vb),2) for E in (50,100,300,1000)]}")
check("C7f NTL route: with C = 0.1, S(100 eV) < 2 for every bias and da >= 0.02",
      all(grid[(Vb, 0.1, da)][1] < 2 for Vb in (2, 4, 10, 100) for da in (0.02, 0.05, 0.1)))
check("C7g HV mode (100 V): pair-number ceiling S_int < 2 for every E_R <= 1 keV, so S < 2 at any C, da",
      all(fom_int(E, 'Si', 100.0) < 2 for E in (50, 100, 300, 1000)))
check("C7l HV ceiling robust to the Fano input: with F_NR = F_eh = 0.15, S_int(100 V) < 2 for E_R <= 300 eV",
      all(fom(E, 'Si', 100.0, 1.0, 0.0, 1e-9, 0.15, 0.15) < 2 for E in (50, 100, 300)))
def Cmin(E, da, Vbs=np.arange(1, 40.5, 0.5)):
    best = None
    for Vb in Vbs:
        for C in np.arange(0.02, 1.0001, 0.01):
            if fom(E, 'Si', Vb, C, da) >= 2:
                if best is None or C < best[0]: best = (round(C, 2), Vb)
                break
    return best
cm = {da: Cmin(100, da) for da in (0.02, 0.05, 0.1)}
print("   minimum C for S=2 at E_R = 100 eV (Si) vs da -> (C_min, best V_b):", cm)
check("C7j NTL route at 100 eV: C_min(da) = 0.15 / 0.28 / 0.53 for da = 0.02 / 0.05 / 0.10, at V_b = 7.5-10 V (Si)",
      all(cm[d] is not None for d in cm) and cm[0.02][0] < cm[0.05][0] < cm[0.1][0]
      and abs(cm[0.02][0] - 0.15) < 0.02 and abs(cm[0.05][0] - 0.28) < 0.02 and abs(cm[0.1][0] - 0.53) < 0.02)
check("C7h NTL route: S >= 2 at 100 eV is reachable at low bias (2-10 V) for C >= 0.5, da <= 0.05",
      any(grid[(Vb, C, da)][1] >= 2 for Vb in (2, 4, 10) for C in (0.5, 1.0) for da in (0.02, 0.05)))
check("C7i pair-number ceiling at 100 eV, 4 V: finite (2 < S_int < 10)", 2 < fom_int(100, 'Si', 4.0) < 10,
      f"{fom_int(100,'Si',4.0):.2f}")

# calibration on the precedent: 1109.4343 (Ge, +-2 V -> 4 V across, 7-20 keV_nr, ER leakage < 1e-3 -> ~3.1 sigma one-sided)
yGe10 = lindhard(32, 72.63, 10.0); gGe = 4.0 / SRC['Ge']['eps']
dF_cdms = gGe * (1 - yGe10) / ((1 + gGe) * (1 + yGe10 * gGe))
ratio = 3.1 / dF_cdms   # implied zeta_O / sigma_pos when noise and pair terms are negligible
ext = {E: max(fom(E, 'Si', Vb, 0.3, 0.3 / ratio) for Vb in (2, 4, 6, 8, 10)) for E in (50, 100, 300, 1000)}
print(f"   CDMS-calibrated zeta/sigma_pos = {ratio:.1f}; extrapolated Si S (zeta=0.3, sigma_ph=2.65 eV):",
      {k: round(v, 2) for k, v in ext.items()})
check("C7k CDMS-PSD calibration (zeta/sigma_pos ~ 9) extrapolated to Si 100 eV at 2-10 V gives 2 < S < 3.5",
      8 < ratio < 10.5 and 2 < ext[100] < 3.5)

# ---------------------------------------------------------------- C8: IF-E7 (delta, r) bounds
fsSi = 0.017
for rel in (0.5,):
    d_prim = (1 - y100['Si']) * fsSi * rel
check("C8a |delta_prim| <= (1-y) f_s |1 - eps_s/eps_p| <= 0.01 (cannot alone give the 0.048 deficit)", d_prim <= 0.01,
      f"{d_prim:.4f}")
# r-only fit of 1803.02903 (WP7-E-v3 C7e): eta = 1 + g(1-r)(1-y)/(1+rg); r = 1.14 reproduces 0.952 for some (g, y) in the quoted ranges
gs, ys, rs = sp.symbols('g y r', positive=True)
eta = 1 + gs * (1 - rs) * (1 - ys) / (1 + rs * gs)
# delta_prim and the gap term enter additively at first order; requirement on r for delta = d_prim
check("C8b eta(r=1) = 1 identically (no NTL/primary collection difference -> no deficit)", sp.simplify(eta.subs(rs, 1) - 1) == 0)

# ---------------------------------------------------------------- C9: zero-field gap-energy channel
for mat in SRC:
    m = SRC[mat]
    dfg = (1 - y100[mat]) * m['Eg'] / m['eps']
    print(f"   {mat}: gap-energy fraction difference (1-y)E_g/eps = {dfg:.3f}")
check("C9a Si gap-energy fraction difference ~0.26 (only timing can read it; C_g from mode selectivity = 0)",
      0.2 < (1 - y100['Si']) * SRC['Si']['Eg'] / SRC['Si']['eps'] < 0.3)
check("C9b phonon-number fluctuation at 100 eV (f ~ 1 THz, eps_ph = 0.13) below 2% of the fast fraction",
      math.sqrt(0.25 / (0.13 * 100 / (1.0 * h_meV_per_THz * 1e-3))) < 0.02)

n_pass = sum(ok for _, ok in RESULTS)
print(f"\n{n_pass}/{len(RESULTS)} PASS")
sys.exit(0 if n_pass == len(RESULTS) else 1)
