#!/usr/bin/env python3
"""CW6 checks (R16 closure of LE-20, LE-118 ... LE-126) and the numbers of returns/R16/WP8-R-v2.md.

Deterministic: sympy algebra, numpy/scipy linear algebra and quadrature. No Monte Carlo, no CMPMC run, no QE run.
Cited as CW6-Kn in returns/R16/CW6.md, returns/R16/WP8-R-v2.md and returns/R16/CW6-errata.md.   Run: python3 checks.py   (< 1 min)
ERR-CW6 revision (R16 errata, VER-CW6): tolerances tightened to the printed numbers, circular or withdrawn checks replaced (K2d hard-coded overlap,
K5f reciprocity map of the 1805.02495 fit, K5g DMM identity, K6c 'x3'), checks added for every correction (K3m, K5h, K6d-f, K7d-f, K8e-g,
K10d-f, K11a-d): 62 checks. The only random numbers are
in K11a (numpy default_rng, fixed seed 20261101), so the output is deterministic.
Stage 1 (K1) reproduces the published WP8-R numbers with WP8-R's own conventions; later groups apply the corrections.
Units SI; phonon frequency f = omega/2pi in Hz (source form of the rate laws, WP8-R Symbols).
"""
import math, sys
import numpy as np
import sympy as sp
from scipy.linalg import expm

RES = []
def check(name, cond, info=""):
    RES.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}  {info}")

h_meV_THz = 4.135667696
SRC = {  # WP8-R Table 1.1 / 2.1 inputs [FT 1109.1193 Table I p.16; 1109.4343 p.2; 2302.05998 p.4]
 'Si': dict(A=7.41e-56, B=2.43e-42, vL=9000., vT=5400., rho=2330., xL=0.093, fD=1.5e13, Eg=1.17, eps=3.75, Z=14, Am=28.09),
 'Ge': dict(A=1.61e-55, B=3.67e-41, vL=5310., vT=3250., rho=5320., xL=0.098, fD=0.864e13, Eg=0.75, eps=2.96, Z=32, Am=72.63)}

def lindhard(Z, Am, EkeV):
    k = 0.133 * Z ** (2 / 3) * Am ** -0.5; e = 11.5 * Z ** (-7 / 3) * EkeV
    g = 3 * e ** 0.15 + 0.7 * e ** 0.6 + e
    return k * g / (1 + k * g)
yL = lambda E: lindhard(14, 28.09, E / 1000)
# measured Si NR yield (2303.02196 Table II, PDF p.5 [FT]); (Y, Y-, Y+), F_NR (central, -, +)
YMEAS = {100: (0.102, 0.072, 0.136), 220: (0.108, 0.098, 0.117), 460: (0.136, 0.128, 0.145)}
FMEAS = {100: (0.9, 0.5, 1.6), 220: (0.5, 0.4, 0.7), 460: (1.8, 1.3, 2.4)}
def Ymeas(E):  # log-linear interpolation of the central values, held flat outside [100, 460] eV  [E]
    Es = np.array([100, 220, 460.]); Ys = np.array([YMEAS[e][0] for e in (100, 220, 460)])
    return float(np.interp(np.log(E), np.log(Es), Ys))

# =====================================================================================================  K1  reproduction of WP8-R
def fs_t(m, t): return (m['xL'] * m['A'] * t) ** -0.2
c = SRC['Si']; g_ = SRC['Ge']
nmix = lambda m: 5 * m['B'] * (m['xL'] * m['A']) ** -0.8 * 1e-6 ** 0.2
vbar = lambda m: (m['vL'] + 2 * m['vT']) / 3
def r_rms(m, t): return math.sqrt(6 * vbar(m) ** 2 / (3 * m['B']) * (m['xL'] * m['A']) ** 0.8 * t ** 1.8 / 1.8)
check("K1a f_*(1 us) = 2.71/2.29 THz, N_mix(1 us) = 652/5072, r_rms(100 ns) = 77/16 um (WP8-R C1, C2)",
      abs(fs_t(c, 1e-6) / 1e12 - 2.71) < 0.01 and abs(fs_t(g_, 1e-6) / 1e12 - 2.29) < 0.01 and round(nmix(c)) == 652
      and round(nmix(g_)) == 5072 and round(r_rms(c, 1e-7) * 1e6) == 77 and round(r_rms(g_, 1e-7) * 1e6) == 16)

def fom_wp8r(ER, Vb, C, da, yy, sigE=2.65, F_ER=0.15, F_NR=1.0, eps=3.75):  # WP8-R fom() verbatim (frozen y passed in)
    gg = Vb / eps; Etot = ER * (1 + yy * gg); E_er = Etot / (1 + gg)
    n_nr, n_er = yy * ER / eps, E_er / eps
    dO = C * (gg / (1 + gg) - yy * gg / (1 + yy * gg)); sn = sigE / Etot
    s_nr = math.sqrt(sn ** 2 + da ** 2 + (C * Vb * math.sqrt(F_NR * n_nr) / Etot) ** 2)
    s_er = math.sqrt(sn ** 2 + da ** 2 + (C * Vb * math.sqrt(F_ER * n_er) / Etot) ** 2)
    return dO / math.sqrt(0.5 * (s_nr ** 2 + s_er ** 2))
def fom_prim_wp8r(ER, yy, C=1.0, sigE=2.65, da=0.0): return C * (1 - yy) * 0.017 / math.sqrt((math.sqrt(2) * sigE / ER) ** 2 + da ** 2)
y100 = yL(100)
def cmin(f, E, da, **kw):
    best = None
    for Vb in np.arange(1, 40.5, 0.5):
        for C in np.arange(0.02, 1.0001, 0.01):
            if f(E, Vb, C, da, **kw) >= 2:
                if best is None or C < best[0]: best = (round(C, 2), Vb)
                break
    return best
cm0 = [cmin(lambda E, Vb, C, da: fom_wp8r(E, Vb, C, da, y100), 100, d)[0] for d in (0.02, 0.05, 0.10)]
check("K1b WP8-R FOM reproduced: S_prim(100/300) = 0.38/1.15, S_int(100 V; 100/300 eV) = 0.53/0.91, zeta_min = 0.15/0.28/0.53",
      abs(fom_prim_wp8r(100, y100) - 0.38) < 0.01 and abs(fom_prim_wp8r(300, y100) - 1.15) < 0.01
      and abs(fom_wp8r(100, 100, 1, 0, y100, 1e-9) - 0.53) < 0.01 and abs(fom_wp8r(300, 100, 1, 0, y100, 1e-9) - 0.91) < 0.01
      and cm0 == [0.15, 0.28, 0.53], f"{cm0}")

# =====================================================================================================  K2  primary route, Sec. 4.1 convention
def sig_Nph(Etot, f_THz=1.0, eps_ph=0.13):            # phonon-number term (WP8-R C9b form), fraction of O
    return math.sqrt(0.25 * f_THz * h_meV_THz * 1e-3 / (eps_ph * Etot))
def S_prim(ER, yy, C=1.0, da=0.0, fs=0.017, Nph=True, sigE=2.65):
    s2 = (sigE / ER) ** 2 + da ** 2 + (sig_Nph(ER) ** 2 if Nph else 0)
    return C * (1 - yy) * fs / math.sqrt(s2)
def E2s(yfun, C=1.0, Nph=False):
    return min(E for E in np.arange(10, 2e4, 1.0) if S_prim(E, yfun(E), C, Nph=Nph) >= 2)
eA, eB = E2s(yL), E2s(lambda E: y100)
eM, eM3 = E2s(Ymeas), E2s(Ymeas, 0.3)
eMN = E2s(Ymeas, Nph=True)
print(f"   E_2sigma (zeta=1, sigma_pos=0): Lindhard(E) {eA:.0f}, frozen y {eB:.0f}, measured Y {eM:.0f} (zeta 0.3: {eM3:.0f}); with sigma_Nph {eMN:.0f} eV")
check("K2a Sec. 4.1 convention reproduces the referees: E_2sigma = 382 eV (REF-A, Lindhard(E)) and 368-369 eV (REF-B 368, frozen y)",
      abs(eA - 382) <= 1 and 368 <= eB <= 369, f"{eA:.0f}, {eB:.0f} eV")
check("K2b with the measured Y (2303.02196, WP5-AUD rule): E_2sigma = 357 eV (zeta=1; 442 eV with sigma_Nph), 1.2 keV (zeta=0.3); sub-keV only at zeta ~ 1",
      abs(eM - 357) <= 1 and abs(eMN - 442) <= 1 and 1150 <= eM3 <= 1250, f"{eM:.0f}, {eM3:.0f}, with sigma_Nph {eMN:.0f} eV")
cap = (1 - Ymeas(100)) * 0.017 / 2
check("K2c sigma_pos cap: S_prim < 2 at every E_R once sigma_pos >= zeta (1 - Y) f_s / 2 = 0.76% zeta (sigma_pos = 0.01, zeta = 1)",
      all(S_prim(E, Ymeas(E), 1.0, 0.01) < 2 for E in (1e2, 1e3, 1e4, 1e5, 1e6)) and abs(cap - 0.0076) < 3e-4, f"cap={cap:.4f}")
arr = (fs_t(c, 1e-3) / 1e12, fs_t(c, 1e-6) / 1e12)     # arrival band = f_*(tau_abs), tau_abs in [1 us, 1 ms] (absorption times of the 4-mm device) [E]
ov = min(1.4, arr[1]) - max(0.3, arr[0])               # soft band 0.3-1.4 THz: WP8-R-v2 Sec. 1.2 input [E]
check("K2d soft band 0.3-1.4 THz [E input] overlaps the computed arrival band f_*(1 ms)-f_*(1 us) = 0.68-2.71 THz by 0.72 THz (zeta_soft-hard << 1 for a frequency cut)",
      abs(arr[0] - 0.68) < 0.01 and abs(arr[1] - 2.71) < 0.01 and ov > 0.7, f"arrival {arr[0]:.2f}-{arr[1]:.2f} THz, overlap {ov:.2f} THz")

# =====================================================================================================  K3  NTL route with gap population, measured inputs
def S_ntl(ER, Vb, C, da, yy, Cg=0.0, sigE=2.65, F_ER=0.119, F_NR=0.9, q=1.0, Nph=True, Eg=1.17, eps=3.75):
    """O_obs = a_p + zeta_O phi_L + zeta_gap phi_gap (CW6 eq. (A.1)); equal E_tot; Gaussian spreads; Sec. 4.1 convention."""
    gg = q * Vb / eps; Etot = ER * (1 + yy * gg); E_er = Etot / (1 + gg)
    n_nr, n_er = yy * ER / eps, E_er / eps
    dphiL = gg / (1 + gg) - yy * gg / (1 + yy * gg)
    dphig = (Eg / eps) * (1 / (1 + gg) - yy / (1 + yy * gg))
    dO = C * dphiL + Cg * dphig
    w = (C * q * Vb + Cg * Eg) / Etot                      # O shift per created pair
    base = (sigE / Etot) ** 2 + da ** 2 + (sig_Nph(Etot) ** 2 if Nph else 0)
    s_nr = base + w ** 2 * F_NR * n_nr; s_er = base + w ** 2 * F_ER * n_er
    return abs(dO) / math.sqrt(0.5 * (s_nr + s_er))
dg = (1.17 / 3.75) * (1 - y100) / ((1 + 1 / math.sqrt(y100)) * (1 + math.sqrt(y100)))
check("K3a gap-population contrast at g_Luke = y^-1/2 (Lindhard 100 eV): Delta phi_gap = 0.053 (REF-A F7: 0.054)", abs(dg - 0.053) < 0.002, f"{dg:.4f}")
check("K3b S_ntl reduces to the WP5-AUD re-implementation at Cg = 0, no sigma_Nph, F_ER = 0.15: zeta_min = 0.13/0.24/0.44 (Y = 0.102, F_NR = 0.9)",
      [cmin(lambda E, Vb, C, da: S_ntl(E, Vb, C, da, 0.102, F_ER=0.15, Nph=False), 100, d)[0] for d in (0.02, 0.05, 0.10)] == [0.13, 0.24, 0.44])
ZM = {}
for rg in (-1.0, -0.5, 0.0, 0.5, 1.0):
    ZM[rg] = [cmin(lambda E, Vb, C, da: S_ntl(E, Vb, C, da, Ymeas(100), Cg=rg * C), 100, d) for d in (0.02, 0.05, 0.10)]
print("   zeta_O,min(100 eV; sigma_pos 0.02/0.05/0.10) vs zeta_gap/zeta_O:", {k: [x[0] if x else None for x in v] for k, v in ZM.items()})
check("K3c corrected low-bias route (measured Y, F_NR, F_ER = F_meas^obs = 0.119, sigma_Nph, zeta_gap = 0): zeta_min = 0.13/0.24/0.44 within 0.01",
      all(abs(ZM[0.0][i][0] - v) <= 0.011 for i, v in enumerate((0.13, 0.24, 0.44))), f"{[x[0] for x in ZM[0.0]]}")
spread = [ZM[r][1][0] for r in (-1.0, 1.0)]
mid = [ZM[r][1][0] for r in (-1.0, -0.5, 0.0, 0.5, 1.0)]
check("K3d zeta_gap/zeta_O = -1, -0.5, 0, +0.5, +1 gives zeta_O,min(sigma_pos = 0.05) = 0.27/0.25/0.24/0.22/0.21 (same orientation convention for both contrasts, errata A7)",
      [round(v, 2) for v in mid] == [0.27, 0.25, 0.24, 0.22, 0.21], f"{mid}")
# off-100-eV entries with energy-dependent measured Y
row10 = [S_ntl(E, 10, 0.3, 0.05, Ymeas(E)) for E in (50, 100, 300, 1000)]
print("   NTL 10 V, zeta 0.3, sigma_pos 0.05 (measured Y(E)):", [round(x, 2) for x in row10])
check("K3e NTL 10 V row (zeta 0.3, sigma_pos 0.05) with measured Y(E), F_meas^obs, sigma_Nph: 1.94/2.44/2.70/2.70 at 50/100/300/1000 eV (WP8-R: 1.63/2.04/2.41/2.56)",
      [round(x, 2) for x in row10] == [1.94, 2.44, 2.7, 2.7], f"{[round(x, 2) for x in row10]}")
# HV ceiling with energy-matched measured bands (WP5-AUD AUD-C7c): <= 1.999 at the band edge
bands = {100: ((0.072, 0.102, 0.136), (0.5, 0.9, 1.6)), 220: ((0.098, 0.108, 0.117), (0.4, 0.5, 0.7)), 300: ((0.098, 0.12, 0.145), (0.4, 0.9, 2.4))}
smax = max(fom_wp8r(E, 100 * qq, 1, 0, yy, 1e-9, fe, fn) for E, (Ys, Fs) in bands.items() for yy in Ys for fn in Fs
           for fe in (0.119, 0.15, 0.3) for qq in (0.873, 1.0))
check("K3f HV (100 V) ceiling with measured bands: max S_int = 1.9986 < 2 (eps 3.75; the '300-eV band' is a constructed envelope of the 220/460 rows, not a measured row)",
      abs(smax - 1.9986) < 1e-4, f"{smax:.4f}")
pe = {(E, k): max(fom_wp8r(E, 100 * qq, 1, 0, yy * 3.75 / k, 1e-9, fe, fn) for yy in Ys for fn in Fs for fe in (0.119, 0.15, 0.3) for qq in (0.873, 1.0))
      for E, (Ys, Fs) in bands.items() for k in (3.75, 3.8)}
print("   HV per-energy maxima (eps 3.75 / 3.8):", {E: (round(pe[(E, 3.75)], 4), round(pe[(E, 3.8)], 4)) for E in bands})
check("K3m HV per-energy maxima (eps 3.75/3.8): 1.26/1.27 (100 eV), 1.71/1.72 (220 eV) on measured rows; 1.9986/2.0136 on the constructed 300-eV envelope: firm NO-GO at <= 220 eV (VER-CW6 14)",
      abs(pe[(100, 3.75)] - 1.2595) < 5e-4 and abs(pe[(220, 3.75)] - 1.7115) < 5e-4 and abs(pe[(220, 3.8)] - 1.7243) < 5e-4
      and abs(pe[(300, 3.75)] - 1.9986) < 1e-4 and abs(pe[(300, 3.8)] - 2.0136) < 1e-4, f"{ {k: round(v, 4) for k, v in pe.items()} }")
check("K3g HV ceiling with F_NR = 0.15 and Y = 0.102 exceeds 2 at 300 eV (WP8-R C7l 'robust' fails; WP5-AUD AUD-C7c')",
      fom_wp8r(300, 100, 1, 0, 0.102, 1e-9, 0.15, 0.15) > 2)
# source definition <n_eh> = Y E_r/3.8 (2303.02196 Eq. (1); CW5-C2)
s38 = max(fom_wp8r(E, 100 * qq, 1, 0, yy * 3.75 / 3.8, 1e-9, fe, fn) for E, (Ys, Fs) in bands.items() for yy in Ys for fn in Fs
           for fe in (0.119, 0.15, 0.3) for qq in (0.873, 1.0))
check("K3j CW5 OC-7 reproduced: 1-sigma corner (Y 0.098, F_NR 0.4, <q> 0.873, F_ER 0.119) gives S_int(300 eV) = 2.014 with eps = 3.8 eV -> (c) CONDITIONAL",
      abs(s38 - 2.0136) < 1e-4, f"{s38:.4f}")
G_, yv, rE, rN, d1 = sp.symbols('G y r_E r_N d', positive=True)
O_ER = 1 - G_ * rE; O_NR = 1 - yv * G_ * rN        # two-window ratio E_sig(t1)/E_sig(t2), r_g(t2) = 0, d'_oth common, (CW5-3) to first order
check("K3k route (b) as a two-window observable: Delta O_b = G_gap (r_g^ER - y r_g^NR); = zeta_gap Delta f_g with zeta_gap = r_g(t1) if r_g^NR = r_g^ER",
      sp.simplify((O_NR - O_ER) - G_ * (rE - yv * rN)) == 0 and sp.simplify((O_NR - O_ER).subs(rN, rE) - rE * (1 - yv) * G_) == 0)
tt, t0 = sp.symbols('t t_0', positive=True)
flip = sp.solve(sp.Eq(sp.exp(-tt / t0), sp.Rational(102, 1000) / (1 + tt / t0)), tt)
check("K3l bimolecular NR tail r_g^NR = 1/(1+t/t0) vs exponential ER r_g^ER = e^{-t/t0} (CW5-4 (ii)): Delta O_b changes sign at t1 = 3.86 t0 (Y = 0.102)",
      len(flip) >= 1 and any(abs(float(f / t0) - 3.865) < 0.01 for f in flip), f"{[float(f/t0) for f in flip]}")
# route (b): zero-field gap channel
def S_b(ER, yy, Cg, da=0.0, sigE=2.65, F_ER=0.119, F_NR=0.9, Eg=1.17, eps=3.75):
    dfg = (1 - yy) * Eg / eps
    nr, ne = yy * ER / eps, ER / eps
    w = Cg * Eg / ER
    s2 = (sigE / ER) ** 2 + da ** 2 + sig_Nph(ER) ** 2 + 0.5 * w ** 2 * (F_NR * nr + F_ER * ne)
    return Cg * dfg / math.sqrt(s2)
sb = [S_b(100, Ymeas(100), 1.0), S_b(100, Ymeas(100), 1.0, 0.05), S_b(100, Ymeas(100), 0.3, 0.05)]
print("   S_b(100 eV): zeta_g=1 no pos", round(sb[0], 2), "; sigma_pos 0.05:", round(sb[1], 2), "; zeta_g 0.3, 0.05:", round(sb[2], 2))
check("K3h route (b) at 100 eV if the gap energy is released inside t_win as a distinguishable population: S_b = 8.2 zeta-scale (zeta_gap = 1, sigma_pos = 0), 4.6 at sigma_pos 0.05, 1.46 at zeta_gap 0.3",
      [round(x, 2) for x in sb] == [8.2, 4.63, 1.46], f"{[round(x, 2) for x in sb]}")
zgmin = min(z for z in np.arange(0.01, 1.0001, 0.01) if S_b(100, Ymeas(100), z, 0.05) >= 2)
check("K3i route (b): zeta_gap,min(100 eV, sigma_pos 0.05) = 0.42 (UNRESOLVED channel, conditional on G-R2)", abs(zgmin - 0.42) < 0.005, f"{zgmin:.2f}")

# =====================================================================================================  K4  memory scope: Ge window, near-face shell, Al2O3
def cascade(mat, ts, absorb=None, u0s=None):
    m = SRC[mat]
    edges = np.logspace(np.log10(0.05e12), np.log10(20e12), 241); fc = np.sqrt(edges[1:] * edges[:-1]); N = fc.size
    xs = np.linspace(0.0005, 0.9995, 2000); px = 30 * xs ** 2 * (1 - xs) ** 2; px /= px.sum()
    K = np.zeros((N, N))
    for j in range(N):
        for fr in (xs, 1 - xs):
            idx = np.clip(np.searchsorted(edges, fr * fc[j]) - 1, 0, N - 1); np.add.at(K[:, j], idx, px * fr)
    G = m['xL'] * m['A'] * fc ** 5
    M = (K - np.eye(N)) * G[None, :]
    return fc, M
fcG, MG = cascade('Ge', [])
fD = SRC['Ge']['fD']
nrG = np.where(fcG < fD, fcG ** 4, 0.); nrG /= nrG.sum()
hdG = np.exp(-0.5 * ((fcG - 0.95 * fD) / (0.05 * fD)) ** 2); hdG /= hdG.sum()
tv = {}
for t in (1e-8, 3e-8, 1e-7):
    E = expm(MG * t); a, b = E @ nrG, E @ hdG; tv[t] = 0.5 * np.abs(a / a.sum() - b / b.sum()).sum()
print("   Ge hard-part TV at 10/30/100 ns:", {k: f"{v:.1e}" for k, v in tv.items()})
check("K4a Ge hard-part TV: 0.022 at 10 ns, ~2.5e-3 at 30 ns, < 1e-3 at 100 ns (REF-B A1: window 30-100 ns right)",
      abs(tv[1e-8] - 0.022) < 0.001 and abs(tv[3e-8] - 2.5e-3) < 3e-4 and abs(tv[1e-7] - 4e-4) < 1e-4, f"{[f'{v:.2e}' for v in tv.values()]}")
d_cpd = 4e-3   # 2012.12430 p.4: 1 cm x 1 cm x 0.4 cm Si [FT]
shell = {t: r_rms(c, t) / d_cpd for t in (1e-8, 1e-7)}   # both QET arrays on the top surface (2012.12430 p.4 [FT]): one instrumented face
check("K4b near-face shell (events within r_rms(t) of the one instrumented face, 4 mm): 0.24% (10 ns) and 1.9% (100 ns) of the volume (VER-CW6 6; CW6 had 2 r_rms/d)",
      abs(shell[1e-8] - 0.00241) < 1e-5 and abs(shell[1e-7] - 0.01918) < 1e-5, f"{ {k: round(v, 5) for k, v in shell.items()} }")
Bs, As = 0.025e-42, (12.7e-55, 1.88e-55)   # 2408.04732 Tables 3-4 [FT]
feq = [Bs / a for a in As]
nm = [Bs * f ** 4 * 1e-6 for f in (1e12, 2e12, 5e12)]
check("K4c Al2O3: f_eq = B/A = 0.020-0.13 THz << primary band; B f^4 x 1 us = 0.025/0.4/16 at 1/2/5 THz (REF-B A2; mixing hypothesis fails)",
      abs(feq[0] / 1e12 - 0.0197) < 1e-3 and abs(feq[1] / 1e12 - 0.133) < 2e-3 and abs(nm[0] - 0.025) < 1e-3 and abs(nm[2] - 15.6) < 0.1)

# =====================================================================================================  K5  isotropic AMM: full P-SV solver
def medium(rho, vL, vT): return dict(rho=rho, a=vL, b=vT, lam=rho * (vL ** 2 - 2 * vT ** 2), mu=rho * vT ** 2)
def vs(c, p, sign):  # vertical slowness, sign +1 (towards +z) / -1; evanescent branch decays away from the interface
    arg = 1 / c ** 2 - p ** 2
    if abs(arg) < 1e-12 / c ** 2: arg = abs(arg)
    q = np.sqrt(complex(arg))
    if q.imag < 0: q = -q
    return sign * q if q.imag == 0 else (q if sign > 0 else -q)
def wave(m, typ, p, sign):
    if typ == 'P':
        s = vs(m['a'], p, sign); d = m['a'] * np.array([p, s])
    else:
        s = vs(m['b'], p, sign); d = m['b'] * np.array([s, -p])
    szz = m['lam'] * p * d[0] + (m['lam'] + 2 * m['mu']) * s * d[1]
    sxz = m['mu'] * (s * d[0] + p * d[1])
    return np.array([d[0], d[1], szz, sxz]), s
def flux(m, typ, s, A):
    cc = m['a'] if typ == 'P' else m['b']
    return m['rho'] * cc ** 2 * s.real * abs(A) ** 2 if abs(s.imag) < 1e-30 else 0.0
def psv(m1, m2, inc, th):
    c1 = m1['a'] if inc == 'P' else m1['b']; p = math.sin(th) / c1
    vi, si = wave(m1, inc, p, +1)
    cols, info = [], []
    for med, typ, sg in ((m1, 'P', -1), (m1, 'S', -1), (m2, 'P', +1), (m2, 'S', +1)):
        v, s = wave(med, typ, p, sg); cols.append(v * (-1 if med is m1 else 1)); info.append((med, typ, s))
    Mx = np.array(cols).T
    amp = np.linalg.solve(Mx, vi)
    Fi = flux(m1, inc, si, 1.0)
    if not Fi > 0: return dict(RP=1.0, RS=0.0, TP=0.0, TS=0.0)   # grazing limit: total reflection
    F = [abs(flux(med, typ, s, a)) / Fi for (med, typ, s), a in zip(info, amp)]
    return dict(RP=F[0], RS=F[1], TP=F[2], TS=F[3])
def sh(m1, m2, th):
    s1 = math.sin(th); s2 = m2['b'] / m1['b'] * s1
    if s2 >= 1: return 0.0
    Z1, Z2 = m1['rho'] * m1['b'] * math.cos(th), m2['rho'] * m2['b'] * math.sqrt(1 - s2 ** 2)
    return 4 * Z1 * Z2 / (Z1 + Z2) ** 2
def flux_avg(fun, n=4001):
    th = np.linspace(0, math.pi / 2 * (1 - 1e-9), n); w = 2 * np.sin(th) * np.cos(th)
    return np.trapezoid([fun(t) * wi for t, wi in zip(th, w)], th)
SI = medium(2330., 9000., 5400.)
AL = medium(2720., math.sqrt((76 + 4 * 26 / 3) * 1e9 / 2720), math.sqrt(26e9 / 2720))   # WP8-R Al (K = 76, G = 26 GPa [UNVERIFIED]); rho AFLOW
GE = medium(5320., 5310., 3250.)
ALc = medium(2700., math.sqrt((58.63 + 2 * 26.16) * 1e9 / 2700), math.sqrt(26.16e9 / 2700))   # CMPMC presets.hpp:281,287-288 (cd56e1b)
r0P, r0S = psv(SI, AL, 'P', 1e-6), psv(SI, AL, 'S', 1e-6)
check("K5a P-SV solver at normal incidence reproduces WP8-R Si/Al: t_L = 0.991, t_T = 0.960",
      abs(r0P['TP'] - 0.991) < 1e-3 and abs(r0S['TS'] - 0.960) < 1e-3, f"{r0P['TP']:.4f}, {r0S['TS']:.4f}")
err = max(abs(sum(psv(m1, m2, inc, th).values()) - 1) for m1, m2 in ((SI, AL), (AL, SI), (GE, AL), (AL, GE))
          for inc in ('P', 'S') for th in np.linspace(0.01, 1.55, 60))
check("K5b energy-flux conservation R_P + R_S + T_P + T_S = 1 at every angle, both directions, Si/Al and Ge/Al", err < 1e-12, f"max err {err:.1e}")
res = {}
for nm_, m1, m2 in (('Si->Al', SI, AL), ('Al->Si', AL, SI), ('Ge->Al', GE, AL), ('Al->Ge', AL, GE), ('Si->Al(CMPMC)', SI, ALc), ('Al(CMPMC)->Si', ALc, SI)):
    tP = flux_avg(lambda t: (lambda r: r['TP'] + r['TS'])(psv(m1, m2, 'P', t)))
    tSV = flux_avg(lambda t: (lambda r: r['TP'] + r['TS'])(psv(m1, m2, 'S', t)))
    tSH = flux_avg(lambda t: sh(m1, m2, t))
    S1 = m1['a'] ** -2 + 2 * m1['b'] ** -2
    tbar = (m1['a'] ** -2 * tP + m1['b'] ** -2 * (tSV + tSH)) / S1
    res[nm_] = dict(P=tP, SV=tSV, SH=tSH, bar=tbar, S=S1)
    print(f"   AMM flux-averaged {nm_}: P {tP:.3f}, SV {tSV:.3f}, SH {tSH:.3f}; mode+angle average t_bar {tbar:.3f}")
check("K5c SH flux average reproduces WP8-R (Si/Al 0.960, Ge/Al 0.905)", abs(res['Si->Al']['SH'] - 0.960) < 2e-3 and abs(res['Ge->Al']['SH'] - 0.905) < 2e-3)
db = [abs(res[a]['bar'] * res[a]['S'] / (res[b]['bar'] * res[b]['S']) - 1) for a, b in (('Si->Al', 'Al->Si'), ('Ge->Al', 'Al->Ge'))]
check("K5d detailed balance (reciprocity) t_bar_12 Sigma_1 = t_bar_21 Sigma_2 holds for the AMM averages (< 1e-5; quadrature error of the 4001-point grid)", max(db) < 1e-5, f"{[f'{x:.1e}' for x in db]}")
thc = math.degrees(math.asin(GE['a'] / AL['a']))
cont = res['Ge->Al']['P'] / (0.5 * (res['Ge->Al']['SV'] + res['Ge->Al']['SH']))
cont_si = res['Si->Al']['P'] / (0.5 * (res['Si->Al']['SV'] + res['Si->Al']['SH']))
check("K5e Ge/Al: L critical angle 56.4 deg; flux-averaged L/T contrast 0.745 (Ge/Al), 1.055 (Si/Al): the normal-incidence 0.95-1.10 range does not hold off normal (REF-A F5)",
      abs(thc - 56.4) < 0.1 and abs(cont - 0.745) < 0.005 and abs(cont_si - 1.055) < 0.005, f"Ge/Al {cont:.3f}, Si/Al {cont_si:.3f}")
ratio = SI['a'] ** -2 + 2 * SI['b'] ** -2
ratio = ratio / (AL['a'] ** -2 + 2 * AL['b'] ** -2)
# 1805.02495 p.7 [FT]: the MC "does not implement phonon propagation in Al", so (1 - T_Si->Al) includes entry + reflection back: T_fit = t_bar_Si->Al * P_abs
Pfit = {k: (0.30 / res[k]['bar'], 0.55 / res[k]['bar']) for k in ('Si->Al',)}
SIGd = lambda m: m['a'] ** -2 + 2 * m['b'] ** -2
dmm = SIGd(AL) / (SIGd(SI) + SIGd(AL))
Pfit['DMM'] = (0.30 / dmm, 0.55 / dmm)
check("K5f Sigma_Si/Sigma_Al = 0.346 (reciprocity weight of the AMM/DMM only). The fitted Si->Al 0.30-0.55 (1805.02495) is t_bar*P_abs, not a transmission: P_abs = 0.321-0.589 (AMM), 0.404-0.740 (DMM); it is NOT mapped to t_esc (VER-CW6 3)",
      abs(ratio - 0.346) < 5e-4 and abs(Pfit['Si->Al'][0] - 0.321) < 1e-3 and abs(Pfit['Si->Al'][1] - 0.589) < 1e-3
      and abs(Pfit['DMM'][0] - 0.404) < 1e-3 and abs(Pfit['DMM'][1] - 0.740) < 1e-3, f"ratio {ratio:.4f}; P_abs {Pfit}")
check("K5g DMM Si->Al = Sigma_Al/(Sigma_Si + Sigma_Al) = 0.743, Al->Si = 0.257 (reciprocity holds for the DMM by construction: not a test, so not checked)",
      abs(dmm - 0.7430) < 5e-4 and abs((1 - dmm) - 0.2570) < 5e-4, f"{dmm:.4f}")
# trapped film modes (VER-CW6 4): T modes in Al beyond the Si-T critical angle have t = 0 (P and T in Si evanescent; Al P evanescent too)
thT = math.asin(AL['b'] / SI['b']); thSVP = math.asin(AL['b'] / AL['a'])
tr_ang = np.linspace(thT + 1e-3, math.pi / 2 - 1e-3, 40)
tmax = max(max((lambda r: r['TP'] + r['TS'])(psv(AL, SI, 'S', t)), sh(AL, SI, t)) for t in tr_ang)
fT = 1 - (AL['b'] / SI['b']) ** 2; wT = 2 * AL['b'] ** -2 / SIGd(AL)
check("K5h Al->Si: SV and SH beyond 34.9 deg (Si c_T critical angle) have t = 0 in the solver; free-surface SV->P conversion is cut off above 29.0 deg; trapped share = 67.2% of T flux = 60.2% of all film flux",
      tmax < 1e-12 and abs(math.degrees(thT) - 34.93) < 0.01 and abs(math.degrees(thSVP) - 28.99) < 0.01 and abs(fT - 0.672) < 5e-4 and abs(fT * wT - 0.602) < 5e-4,
      f"max t beyond = {tmax:.1e}; {fT:.4f}, {fT * wT:.4f}")

# =====================================================================================================  K6  film escape with t_esc (LE-123)
a_, t_ = sp.symbols('a t', positive=True)
Pabs = (1 - sp.exp(-a_)) / (1 - (1 - t_) * sp.exp(-a_))
check("K6a film absorption per entry P_abs = (1-e^-a)/(1-(1-t)e^-a): -> 1-e^-a at t = 1 (CMPMC kaplan.hpp:51-58 path 4d), ~ a/t for a -> 0",
      sp.simplify(Pabs.subs(t_, 1) - (1 - sp.exp(-a_))) == 0 and sp.simplify(sp.limit(Pabs / a_, a_, 0) - 1 / t_) == 0)
# angle average for small a: <a/t> = (2d/lambda) <1/(t cos)>; with t = const: 4d/(lambda t)
th = sp.symbols('theta', positive=True)
check("K6b flux-weighted <2d/cos> = 4d (CMPMC's 'path = 4 d'): film loss time tau_l = 4 d/(v_film t_esc_bar)",
      sp.simplify(sp.integrate(2 / sp.cos(th) * 2 * sp.sin(th) * sp.cos(th), (th, 0, sp.pi / 2)) - 4) == 0)
t_esc_amm, t_esc_dmm = res['Al->Si']['bar'], 1 - dmm
check("K6c t_esc(Al->Si) = t_bar: AMM 0.323 (0.328 CMPMC Al), DMM 0.257; tau_l differs by x1.26 between the models (the fitted-effective x3 is withdrawn, VER-CW6 3)",
      abs(t_esc_amm - 0.323) < 5e-4 and abs(res['Al(CMPMC)->Si']['bar'] - 0.328) < 5e-4 and abs(t_esc_amm / t_esc_dmm - 1.257) < 2e-3, f"AMM {t_esc_amm:.4f}, DMM {t_esc_dmm:.4f}")
# K6d exact flux average at t = 1 (VER-CW6 4: Jensen): <1 - exp(-2b/mu)>_{2 mu dmu} = 1 - 2 E_3(2b), b = d/lambda_pb
from scipy.special import expn
from scipy.integrate import quad
bb = (0.01, 0.06, 0.2)
ex = [1 - quad(lambda mu: 2 * mu * math.exp(-2 * b / mu), 0, 1, epsabs=1e-14)[0] for b in bb]
e3 = [1 - 2 * expn(3, 2 * b) for b in bb]; cm = [1 - math.exp(-4 * b) for b in bb]
check("K6d t = 1, flux-averaged: <P_abs> = 1 - 2E_3(2d/lambda) exactly, below CMPMC's 1 - e^{-4d/lambda} (Jensen) by 2.9%/8.3%/11.8% at d/lambda = 0.01/0.06/0.2: equal only to O(a)",
      max(abs(x - y) for x, y in zip(ex, e3)) < 1e-10 and all(x < y for x, y in zip(e3, cm))
      and [round(1 - x / y, 3) for x, y in zip(e3, cm)] == [0.029, 0.083, 0.118], f"{[round(1 - x / y, 3) for x, y in zip(e3, cm)]}")
# K6e inversion of the 1805.02495 fit for the in-film optical depth (VER-CW6 3, Sec. A) [E]
def a_of(P, t): return -math.log((1 - P) / (1 - P * (1 - t)))
aA = [a_of(P, t_esc_amm) for P in Pfit['Si->Al']]; aD = [a_of(P, t_esc_dmm) for P in Pfit['DMM']]
lam = sorted([2 * 60e-9 / x for x in aA + aD] + [4 * 60e-9 / x for x in aA + aD])
check("K6e (CW6-4) inverted: P_abs -> a = 0.14-0.38 (AMM pair), 0.16-0.55 (DMM pair); lambda_pb = 2d/a ... 4d/a = 0.22-1.7 um for d = 60 nm: a constraint on lambda_pb/d, not on t_esc [E]",
      abs(aA[0] - 0.142) < 1e-3 and abs(aA[1] - 0.380) < 1e-3 and abs(aD[0] - 0.160) < 1e-3 and abs(aD[1] - 0.550) < 1e-3
      and abs(lam[0] * 1e6 - 0.22) < 0.01 and abs(lam[-1] * 1e6 - 1.69) < 0.01, f"a AMM {aA}, DMM {aD}; lambda {lam[0]*1e6:.2f}-{lam[-1]*1e6:.2f} um")
P_ = sp.symbols('P', positive=True)
check("K6f inversion exact: e^{-a} = (1 - P)/(1 - (1 - t) P) solves P_abs(a, t) = P (sympy)",
      sp.simplify(Pabs.subs(sp.exp(-a_), (1 - P_) / (1 - (1 - t_) * P_)) - P_) == 0)

# =====================================================================================================  K7  zeta_O, r_coll in a mean-field two-film model (LE-118, LE-121) [E]
fcS, MS = cascade('Si', [])
N = fcS.size; dlog = np.log(fcS[1] / fcS[0])
def collect(u0, d=4e-3, c1=0.05, c2=0.05, t1=0.9, t2=0.9, fcut=3.0 / h_meV_THz * 1e12, f2D=0.36 / h_meV_THz * 1e12, loss=1e-3):
    v = vbar(SRC['Si']); hit = v / (2 * d)
    G1 = hit * c1 * t1 * (fcS >= fcut); G2 = hit * c2 * t2 * (fcS >= f2D)
    Gl = hit * (1 - c1 - c2) * loss * np.ones(N)
    A = -(MS - np.diag(G1 + G2 + Gl))
    n = np.linalg.solve(A, u0)            # time-integrated spectrum: int u dt
    return float(G1 @ n), float(G2 @ n), float(Gl @ n)
u_prim = np.where(fcS < 15e12, fcS ** 4, 0.); u_prim /= u_prim.sum()          # Debye-like NR/ER hard birth
def u_ntl(Emean_meV):                                                        # NTL birth: flat in f up to 2x mean (toy)
    fm = Emean_meV / h_meV_THz * 1e12; u = np.where(fcS < 2 * fm, fcS, 0.); return u / u.sum()
a1p, a2p, lp = collect(u_prim)
out = {}
for Em in (0.75, 2.0, 4.7):
    a1, a2, l = collect(u_ntl(Em)); out[Em] = (a1, a2, l)
print(f"   primaries: film1 {a1p:.3f}, Al {a2p:.3f}, loss {lp:.3f}; NTL <E_Luke> 0.75/2/4.7 meV:", {k: tuple(round(x, 3) for x in v) for k, v in out.items()})
# orientation convention (errata A7, VER-CW6 7): a_pop = E_2/(E_1 + E_2), film 2 = the LOWER-gap film (Al); zeta_O = a_NTL - a_prim as defined in (CW6-1)
zeta = {Em: v[1] / (v[0] + v[1]) - a2p / (a1p + a2p) for Em, v in out.items()}
zeta_old = {Em: a1p / (a1p + a2p) - v[0] / (v[0] + v[1]) for Em, v in out.items()}    # what CW6 printed: a_prim - a_NTL with a = film-1 share
rcoll = {Em: (v[0] + v[1]) / (a1p + a2p) for Em, v in out.items()}
clos = [abs(sum(v) - 1) for v in list(out.values()) + [(a1p, a2p, lp)]]
check("K7a mean-field two-film toy (Si 4 mm, 5% + 5% coverage, Nb-like cut 0.73 THz): energy closure film1 + film2 + loss = 1 for every population (< 1e-9)",
      max(clos) < 1e-9, f"max {max(clos):.1e}")
check("K7b toy zeta_O = a_NTL - a_prim with a = low-gap (Al) share: +0.420/+0.282/+0.107 at <E_Luke> = 0.75/2/4.7 meV; CW6's printed values were a_prim - a_NTL of the film-1 share (same numbers, sign convention fixed) [E]",
      [round(zeta[k], 3) for k in (0.75, 2.0, 4.7)] == [0.420, 0.282, 0.107] and all(abs(zeta[k] - zeta_old[k]) < 1e-12 for k in zeta),
      f"{ {k: round(v, 4) for k, v in zeta.items()} }")
check("K7c toy r_coll = eps_NTL/eps_prim = 0.8745/0.9552/0.9815 (< 1 because NTL energy born below 2Delta_Al is counted as lost, K7d) -> (B-b) r_coll >= 1 not supported by the toy [E]",
      [round(rcoll[k], 4) for k in (0.75, 2.0, 4.7)] == [0.8745, 0.9552, 0.9815], f"{ {k: round(v, 4) for k, v in rcoll.items()} }")
# K7d where the deficit comes from (VER-CW6 8): births below 2 Delta_Al, counted as lost; the toy grid truncates births at 0.05 THz
f2D = 0.36 / h_meV_THz * 1e12
def u_cut(Em): u = np.where(fcS >= f2D, u_ntl(Em), 0.); return u / u.sum()
sub = {Em: float(u_ntl(Em)[fcS < f2D].sum()) for Em in (0.75, 2.0, 4.7)}
rcut = {Em: (lambda v: (v[0] + v[1]) / (a1p + a2p))(collect(u_cut(Em))) for Em in (0.75, 2.0, 4.7)}
pAl = collect(u_prim, fcut=f2D)
rAl = {Em: (lambda v: (v[0] + v[1]) / (pAl[0] + pAl[1]))(collect(u_cut(Em), fcut=f2D)) for Em in (0.75, 2.0, 4.7)}
p10 = collect(u_prim, loss=1e-2)
r10 = {Em: (lambda v: (v[0] + v[1]) / (p10[0] + p10[1]))(collect(u_ntl(Em), loss=1e-2)) for Em in (0.75, 2.0, 4.7)}
print("   sub-2Delta_Al birth share", {k: round(v, 3) for k, v in sub.items()}, "; r_coll without them", {k: round(v, 4) for k, v in rcut.items()},
      "; all-Al films", {k: round(v, 4) for k, v in rAl.items()}, "; l_s x10", {k: round(v, 3) for k, v in r10.items()})
check("K7d the r_coll deficit is the sub-2Delta_Al NTL birth share (0.118/0.040/0.016, births truncated at the 0.05 THz grid edge), counted as lost: without it r_coll = 0.992/0.995/0.998 (Nb + Al) and 1.000 (all-Al)",
      [round(sub[k], 3) for k in (0.75, 2.0, 4.7)] == [0.118, 0.040, 0.016] and [round(rcut[k], 3) for k in (0.75, 2.0, 4.7)] == [0.992, 0.995, 0.998]
      and all(abs(v - 1) < 1e-3 for v in rAl.values()))
check("K7e bare-surface loss l_s x10 (1e-2 per bounce): r_coll(0.75 meV) 0.875 -> 0.819 (0.914, 0.965 at 2, 4.7 meV): the toy r_coll is a model choice [E]",
      abs(r10[0.75] - 0.819) < 1e-3 and abs(r10[2.0] - 0.914) < 1e-3 and abs(r10[4.7] - 0.965) < 1e-3)
# K7f effect of r_coll < 1 on the WP7-E-v3 bound (VER-CW6 Sec. B; errata rebuttal C1): exact, from the AUD-1 identity at delta_coll = X^oth = 0
gs, rs, ys, es, ss = sp.symbols('g r y eta s', positive=True)
s_sol = sp.solve(sp.Eq(1 - es - ss, gs * (rs - 1) * (1 - ys - ss) / (1 + rs * gs)), ss)[0]
shift = sp.simplify(s_sol - (1 - es))
wid = {Em: float(shift.subs({gs: sp.Rational(400, 382), ys: sp.Rational(3, 10), es: sp.Rational(952, 1000), rs: rcoll[Em]})) for Em in rcoll}
apx = {Em: float((gs * (1 - rs) * (1 - ys) / (1 + rs * gs)).subs({gs: sp.Rational(400, 382), ys: sp.Rational(3, 10), rs: rcoll[Em]})) for Em in rcoll}
print("   E_st/omega bound shift exact", {k: round(v, 4) for k, v in wid.items()}, "; VER-CW6 Sec. B approximation", {k: round(v, 4) for k, v in apx.items()})
check("K7f exact shift of the inferred E_st/omega at fixed eta: g(1 - r)(eta - y_ion)/(1 + g) = 0.042/0.015/0.006 at the toy r_coll (VER-CW6's g(1-r)(1-y)/(1+rg) = 0.048/0.016/0.007 is the change of 1-eta at fixed E_st)",
      sp.simplify(shift - gs * (1 - rs) * (es - ys) / (1 + gs)) == 0 and [round(wid[k], 3) for k in (0.75, 2.0, 4.7)] == [0.042, 0.015, 0.006])

# =====================================================================================================  K8  delta_coll decomposition and the bias scan (LE-121)
yi, rho_g, Eg_e = sp.symbols('y rho_g e_g', positive=True)
dgap = ((1 - yi) * Eg_e * (rho_g - 1)) / (1 + Eg_e * (rho_g - 1))
eh, eg_ = sp.symbols('eps_h eps_g', positive=True)
eER = eh * (1 - Eg_e) + eg_ * Eg_e; eNR = eh * (1 - yi * Eg_e) + eg_ * yi * Eg_e
check("K8a delta_coll^gap = (1 - y_ion) e_g (rho_g - 1)/[1 + e_g (rho_g - 1)], e_g = E_g/eps_eh, rho_g = eps_gap/eps_hard (exact)",
      sp.simplify((eER - eNR) / eER - dgap.subs(rho_g, eg_ / eh)) == 0)
rg_need = sp.nsolve(dgap.subs({yi: 0.3, Eg_e: 1.17 / 3.75}) - 0.048, rho_g, 1.2)
check("K8b the full 0.048 needs only rho_g - 1 = 0.24 (y_ion 0.3, Si): REF-B B3 confirmed", abs(float(rg_need) - 1.24) < 0.01, f"{float(rg_need):.3f}")
g, r, y, X = sp.symbols('g r y X', positive=True)   # X = delta_coll + (D'_NR - kappa_cal(r) D'_ER)/omega
one_m_eta = g * (r - 1) * (1 - y) / (1 + r * g) + (1 + g) / (1 + r * g) * X        # (AUD-1)
J = sp.Matrix([[sp.diff(one_m_eta, r), sp.diff(one_m_eta, X)]]).subs({r: 1, X: 0})
J1, J2 = J.subs(g, sp.Rational(400, 382)), J.subs(g, sp.Rational(4000, 382))
check("K8c bias scan breaks the r_coll/(delta_coll + E_st) degeneracy: Jacobian [d/dr, d/dX] at g = 1.05 and 10.5 has rank 2 (y = 0.3)",
      sp.Matrix([J1.subs(y, sp.Rational(3, 10)), J2.subs(y, sp.Rational(3, 10))]).rank() == 2)
d_r = sp.simplify(sp.diff(one_m_eta, r).subs({r: 1, X: 0}))
check("K8d d(1-eta)/dr_coll = g(1-y)/(1+g) at r = 1 (rises with V_b); d/dX = 1 (bias-independent at r = 1)",
      sp.simplify(d_r - g * (1 - y) / (1 + g)) == 0 and sp.simplify(sp.diff(one_m_eta, X).subs(r, 1) - 1) == 0)

# K8e general delta_coll^gap (VER-CW6 9): released gap fractions x_ER, x_NR per unit created-pair gap energy of an ER
xE, xN = sp.symbols('x_E x_N', positive=True)
eERg = eh * (1 - Eg_e * xE) + eg_ * Eg_e * xE; eNRg = eh * (1 - Eg_e * xN) + eg_ * Eg_e * xN
dgen = Eg_e * (rho_g - 1) * (xE - xN) / (1 + Eg_e * xE * (rho_g - 1))
qE, qN, yc = sp.symbols('q_E q_N yfrak', positive=True)
check("K8e delta_coll^gap = G(rho_g-1)(x_ER - x_NR)/[1 + G x_ER(rho_g-1)] (exact); (CW6-3) is x = (1, y_ion); all pairs release: x = (1, yfrak); trapped retain E_g: x = (<q>_ER, yfrak<q>_NR) = G -> G<q>_ER",
      sp.simplify((eERg - eNRg) / eERg - dgen.subs(rho_g, eg_ / eh)) == 0 and sp.simplify(dgen.subs({xE: 1, xN: yi}) - dgap) == 0
      and sp.simplify(dgen.subs({xE: qE, xN: yc * qN}) - dgap.subs({Eg_e: Eg_e * qE, yi: yc * qN / qE})) == 0)
rq = sp.nsolve(dgap.subs({yi: 0.3, Eg_e: 1.17 / 3.75 * 0.873}) - 0.048, rho_g, 1.2)
check("K8f with G -> G<q>_ER (<q>_ER = 0.873) the 0.048 needs rho_g - 1 = 0.27 instead of 0.24: numerically immaterial (VER-CW6 9)", abs(float(rq) - 1.270) < 2e-3, f"{float(rq):.4f}")
# K8g exact two-bias inversion of (AUD-1) for any r (linear in r and X), under bias-independent r, y_ion, X (VER-CW6 10)
m1, m2 = sp.symbols('m1 m2'); g1v, g2v = sp.Rational(400, 382), sp.Rational(4000, 382)
eqs = [sp.Eq(mm * (1 + r * gg_), gg_ * (r - 1) * (1 - y) + (1 + gg_) * X) for mm, gg_ in ((m1, g1v), (m2, g2v))]
solrx = sp.solve(eqs, [r, X], dict=True)[0]
rt, Xt = sp.Rational(9, 10), sp.Rational(2, 100)
mv = {m1: one_m_eta.subs({g: g1v, r: rt, X: Xt, y: sp.Rational(3, 10)}), m2: one_m_eta.subs({g: g2v, r: rt, X: Xt, y: sp.Rational(3, 10)})}
dX = sp.diff(one_m_eta, X)
check("K8g (AUD-1) is linear in (r_coll, X) after multiplying by 1 + r g: two biases invert it exactly for any r (round trip r = 0.9, X = 0.02); at r != 1 d/dX = (1+g)/(1+rg) varies with bias",
      sp.simplify(solrx[r].subs(y, sp.Rational(3, 10)).subs(mv) - rt) == 0 and sp.simplify(solrx[X].subs(y, sp.Rational(3, 10)).subs(mv) - Xt) == 0
      and sp.simplify(dX - (1 + g) / (1 + r * g)) == 0 and dX.subs({r: rt, g: g1v}) != dX.subs({r: rt, g: g2v}))

# =====================================================================================================  K9  A_iso (LE-124)
iso = [(27.9769265, 0.92223), (28.9764947, 0.04685), (29.9737702, 0.03092)]   # IUPAC/NIST natural Si [DB]
mb = sum(mm * x for mm, x in iso); g2 = sum(x * (1 - mm / mb) ** 2 for mm, x in iso)
Om = (5.431e-10) ** 3 / 8
c3 = 3 / (9000. ** -3 + 2 * 5400. ** -3)
B_iso = 4 * math.pi ** 3 * g2 * Om / c3
Aiso = lambda B: B / (2 * math.pi) ** 4
check("K9a Gamma_md(Si) = 2.01e-4 (2408.04732 Table 4: 2.02e-4) and isotropic <c^3> = 2.13e11 m^3/s^3 (Table 4: 2.13)",
      abs(g2 / 2.02e-4 - 1) < 0.01 and abs(c3 / 2.13e11 - 1) < 0.005, f"g2={g2:.3e}, <c3>={c3:.3e}")
check("K9b B = 4 pi^3 Gamma_md Omega/<c^3> = 2.33e-42 s^3 (2408.04732 Eq. (4), Table 4 'B' column)", abs(B_iso / 2.33e-42 - 1) < 0.01, f"{B_iso:.3e}")
vals = {k: Aiso(v) for k, v in (('calc', 2.33e-42), ('lit/CMPMC preset', 2.43e-42), ('meas lo', 2.42e-42), ('meas hi', 2.56e-42))}
print("   A_iso = B/(2 pi)^4 [1e-45 s^3]:", {k: round(v * 1e45, 3) for k, v in vals.items()})
check("K9c A_iso(Si) = 1.50 (calc) / 1.56 (Leman Table I = CMPMC presets.hpp:36) / 1.55-1.64 (measured) x1e-45 s^3; WP8-U's 1.65 [E] is 0.4% above the band",
      abs(vals['calc'] * 1e45 - 1.495) < 0.005 and abs(vals['lit/CMPMC preset'] * 1e45 - 1.559) < 0.005 and abs(1.65e-45 / vals['meas hi'] - 1) < 0.005)

# =====================================================================================================  K10 space charge, trapped-charge field (LE-122)
eps0 = 8.8541878128e-12; e = 1.602176634e-19
sig_1pct = 0.01 * 100.0 * 11.68 * eps0 / e     # areal trapped charge (e/m^2) that shifts a 1 V/cm field by 1%
check("K10a planar slab: a trapped sheet of areal density n_s shifts the field by e n_s/(eps_r eps0); 1% of 1 V/cm needs 6.5e8 e/m^2 = 6.5e4 e/cm^2 (Si)",
      abs(sig_1pct / 6.46e8 - 1) < 0.01, f"{sig_1pct:.3e} e/m^2")
zz, dd, ns = sp.symbols('z d n_s', positive=True)
# sheet at z0 between grounded-referenced electrodes at fixed V: field change below/above the sheet
z0 = sp.symbols('z_0', positive=True)
Eb = -e * ns * (dd - z0) / dd; Ea = e * ns * z0 / dd    # units of 1/(eps); continuity jump = e n_s, zero mean (fixed V)
check("K10b fixed-bias boundary condition: field jump e n_s at the sheet and zero average change (int dE dz = 0)",
      sp.simplify(Ea - Eb - e * ns) == 0 and sp.simplify(Eb * z0 + Ea * (dd - z0)) == 0)
# phonon-ionisation reach of shallow donors (45 meV ~ 10.9 THz): primaries above it survive < ~1 ns -> < ~1 um
f45 = 45 / h_meV_THz * 1e12
t45 = 1 / (SRC['Si']['xL'] * SRC['Si']['A'] * f45 ** 5)
check("K10c phonons above E_b(P) = 45 meV (10.9 THz) decay in ~1 ns (f_*(t) law): phonon-driven emission from shallow donors is local (< 1 um)",
      t45 < 2e-9 and r_rms(c, t45) < 2e-6, f"t={t45*1e9:.2f} ns, r={r_rms(c, t45)*1e6:.2f} um")

# K10d field correction of a sheet: max|dE| = jump * max(z0, d - z0)/d in [1/2, 1] jump (VER-CW6 15)
mx = sp.Max(sp.Abs(Eb), sp.Abs(Ea)) / (e * ns)
vals_ = [float(mx.subs({dd: 1, z0: zv})) for zv in (sp.Rational(1, 2), sp.Rational(1, 10), sp.Rational(9, 10))]
ns_rng = (sig_1pct * 1e-4, 2 * sig_1pct * 1e-4)
check("K10d max|dE| = jump max(z0, d-z0)/d: 1/2 (mid-plane) ... 1 (at a face); 1% of 1 V/cm needs n_s = 6.5-12.9e4 e/cm^2 (6.5e4 is the jump)",
      abs(vals_[0] - 0.5) < 1e-15 and abs(vals_[1] - 0.9) < 1e-15 and abs(vals_[2] - 0.9) < 1e-15 and abs(ns_rng[0] / 6.455e4 - 1) < 1e-3 and abs(ns_rng[1] / 1.291e5 - 1) < 1e-3,
      f"{ns_rng[0]:.3e}-{ns_rng[1]:.3e}")
# K10e LE-119 (ii): half-line exciton diffusion with a surface of recombination velocity S (Robin face): fraction recombining at the face (VER-CW6 22)
zq, z0q, Dq, Lq, Sq = sp.symbols('z z0 D L S', positive=True)
A1, B1, C1 = sp.symbols('A1 B1 C1')
nin = A1 * sp.exp(zq / Lq) + B1 * sp.exp(-zq / Lq); nout = C1 * sp.exp(-zq / Lq)    # D n'' - (D/L^2) n = -delta(z - z0), n -> 0 at infinity
sl = sp.solve([sp.Eq(Dq * sp.diff(nin, zq).subs(zq, 0), Sq * nin.subs(zq, 0)), sp.Eq(nin.subs(zq, z0q), nout.subs(zq, z0q)),
               sp.Eq(Dq * (sp.diff(nout, zq) - sp.diff(nin, zq)).subs(zq, z0q), -1)], [A1, B1, C1], dict=True)[0]
frac = sp.simplify((Sq * nin.subs(zq, 0)).subs(sl))
check("K10e fraction of excitons born at depth z0 that recombine at a face of velocity S: [S/(S + D_X/L_X)] e^{-z0/L_X} (-> e^{-z0/L_X} only for S -> infinity)",
      sp.simplify(frac - Sq / (Sq + Dq / Lq) * sp.exp(-z0q / Lq)) == 0 and sp.limit(frac, Sq, sp.oo) == sp.exp(-z0q / Lq))
# K10f cost of the LE-118 runs at 16 M steps/s (CMPMC-AUD T11) (VER-CW6 21)
cost = lambda nf, nr, nph, nst: nf * nr * nph * nst / 16e6 / 3600
check("K10f LE-118 cost: full 40 x 512 x 1e4 x 1e4 = 35.6 h; 1-D pass 40 x 64 x 1e4 x 1e4 = 4.44 h (not 1 h); box-runnable first pass at 1e3 phonons per cell = 0.44 h",
      abs(cost(40, 512, 1e4, 1e4) - 35.56) < 0.01 and abs(cost(40, 64, 1e4, 1e4) - 4.444) < 1e-3 and abs(cost(40, 64, 1e3, 1e4) - 0.444) < 1e-3)

# =====================================================================================================  K11 errata-only checks
# K11a (CW6-2) corrected (VER-CW6 11; errata A11, C2): |dO| <= ||du||_{1,f<f_m} + tau_h, for weights w in [0, 1] whose oscillation on f > f_m is <= tau_h
rng = np.random.default_rng(20261101)
nb, km, tau = 60, 20, 1e-3
worst, viol = 0.0, 0
for _ in range(4000):
    w = np.concatenate([rng.random(km), rng.random() * (1 - tau) + tau * rng.random(nb - km)])
    p, q_ = rng.random(nb) ** 3, rng.random(nb) ** 3; p /= p.sum(); q_ /= q_.sum(); du = p - q_
    bound = np.abs(du[:km]).sum() + tau
    worst = max(worst, abs(w @ du) / bound)
    if abs(w @ du) > abs(du[:km].sum()) + tau: viol += 1
wc = np.zeros(nb); wc[:2] = (1.0, 0.0); duc = np.zeros(nb); duc[:2] = (0.1, -0.1)           # counterexample: Delta_soft = 0, |dO| = 0.1
check("K11a corrected (CW6-2): |dO| <= ||du||_{1,low} + tau_h holds on 4000 random instances (max ratio < 1); Delta_soft + tau_h fails when du changes sign below f_m (counterexample |dO| = 0.1, Delta_soft = 0)",
      worst <= 1 + 1e-12 and viol > 0 and abs(wc @ duc - 0.1) < 1e-15 and abs(duc[:km].sum()) == 0, f"max ratio {worst:.3f}; {viol} instances violate Delta_soft + tau_h")
# K11b C4f (REF-B weak check) replaced: e^{-N_mix} from the computed N_mix(1 us), not hard-coded
lg = {k: -nmix(SRC[k]) / math.log(10) for k in ('Si', 'Ge')}
check("K11b NR/ER L-fraction memory ~ e^{-N_mix(1 us)}: log10 = -283 (Si), -2203 (Ge) from the computed N_mix = 652/5072 (replaces WP8R-C4f's hard-coded e^{-100})",
      round(lg['Si']) == -283 and round(lg['Ge']) == -2203, f"{lg}")
# K11c Delta_Al readings (VER-CW6 Sec. D; errata rebuttal C3): 4 Delta in GHz
GHz = lambda D_ueV: 4 * D_ueV * 1e-3 / h_meV_THz * 1e3
fd = {D: GHz(D) for D in (100.0, 173.715, 180.0, 200.0)}
check("K11c 4Delta(Al) = 97 (2Delta = 200 ueV), 168 (CMPMC), 174 (v1), 193 GHz (Delta = 200 ueV): '<= 174 GHz either way' is wrong, but all < 0.3 THz (conclusion unchanged)",
      [round(v) for v in fd.values()] == [97, 168, 174, 193] and max(fd.values()) < 300)
# K11d C5c (REF-B weak check) applied: Nb-like cut vs Ge hole NTL (0.7 THz, v1 Sec. 3.3 input [E]) and the Si arrival peak 0.7-0.9 THz (1805.02495 p.7)
fcutTHz = 3.0 / h_meV_THz
check("K11d C5c: the Nb-like cut 2Delta = 3 meV is 0.725 THz: the 0.7 THz Ge hole NTL band lies on it (3.5% below) and it sits inside the Si arrival peak 0.7-0.9 THz",
      abs(fcutTHz - 0.7254) < 1e-4 and abs(0.7 / fcutTHz - 1) < 0.04 and 0.7 <= fcutTHz <= 0.9)

n = sum(ok for _, ok in RES)
print(f"\n{n}/{len(RES)} PASS")
sys.exit(0 if n == len(RES) else 1)
