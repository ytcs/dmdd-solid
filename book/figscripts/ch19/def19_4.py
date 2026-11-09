"""Defects and stored energy (Sect. 19.4): Limit Check 19.4a (lim:19.4a, fig:19-limit-nrt), the last column of
Table 19.1 (tab:19-bounds), worked example 19.4 (we:19-fp300) and every number printed in Sect. 19.4.  The
stored-energy bound itself, its conditions and its dependence on the collection ratio are computed in bal19_5.py
(Sect. 19.5, Limit Check 19.5b).
Log: def19_4.log.  Run: python def19_4.py > def19_4.log  (about a minute).

Part A. Displacement count of a cascade (Limit Check 19.4a).
  Counting rules (Kinchin and Pease, as quoted by Cogswell et al. 2021, Sect. II, and used in Sect. 16.6): an atom
  struck with energy transfer T > E_d is displaced; if the projectile is left with E - T < E_d it takes the vacated
  site (replacement) and the count does not grow; atoms struck with T < E_d stay and their energy becomes heat; no
  binding energy is spent and electronic losses are removed, so that the energy argument is the damage energy T_d.
  With n(E) the mean number of further displacements produced by a moving atom of energy E, the first-collision
  balance (Sect. 19.4, eq:19.4-count) is
      int dsigma(E,T) [ n(E) - n(E-T) - n(T) - Theta(T - E_d) Theta(E - T - E_d) ] = 0,   n(E) = 0 for E < 2 E_d,
  and N_FP(T_d) = 1 + n(T_d) for T_d >= E_d.
  Cross-sections (MODELLING CHOICES, named in the caption):
   (i) hard spheres, dsigma ~ dT/E: the equation reduces to Kinchin-Pease, N_FP = T_d/(2E_d) exactly (check);
   (ii) the screened Thomas-Fermi cross-section of Sect. 19.3 (impulse deflection, continued below x_L = 2e-3 as
        x_L^(1/3)), built here exactly as in lind19_3.py, with dsigma ~ f(eps sqrt(s)) s^(-3/2) ds, s = T/E,
        eps = c_L E (equal masses, silicon), at E_d = 36 eV (average Frenkel-pair threshold, Holmstrom et al. 2008
        Table IV, Sect. 7.4) and, as a check of the scale dependence, 12.5 and 20 eV;
   (iii) the pure power law dsigma ~ s^(-4/3) ds (m = 1/3), the low-energy limit of (ii).
  Published form compared: NRT, N_FP = 0.8 T_d/(2E_d) for T_d >= 2E_d/0.8, 1 for E_d <= T_d < 2E_d/0.8
  (Norgett, Robinson and Torrens 1975, as quoted in 1805.09942 Sect. V; the 0.8 as in WP literature on Kinchin-Pease).
Numerics: geometric grid in u = E/E_d from 2 to 3000 (NU points); at each step the unknown n(u_i) enters linearly
  (small-s part through the backward difference, the near-head-on part through linear interpolation), and is solved
  exactly; s-integrals on composite geometric grids.  Convergence: NU halved (printed).

Part B. Calibration data and the readings of the stored-energy bounds (Table 19.1).
  Si: CDMS II, 1803.02903: Y_ph = 0.952 (+0.009, -0.007) at 95 % C.L. (Sect. 3.2, Fig. 9 caption), 10-100 keV; the bound
      E_st/omega <= 1 - Y_lo = 0.055 under conditions (a)-(e) of Sect. 19.5 and 0.049 with the book's eps_eh (bal19_5.log).
  Ge: SuperCDMS Soudan, 1805.09942: f_DF = (6.08 +/- 0.18) % (abstract; Sect. V A), 206Pb at 103 keV; per-detector
      f = 5.52 +/- 0.10 and 6.67 +/- 0.11 %, f_sur = -0.75 +/- 0.06 and 0.85 +/- 0.08 %, f_DF = 6.22 +/- 0.11 and
      5.87 +/- 0.13 % (Table II); observed yield of the Pb surface recoils ~0.3 (Sect. II, Fig. 1), a lower edge of the
      electronic share since surface events lose charge (1803.02903 Sect. 2.1), so T_d/E_R <= 0.7.
  Damage fractions of Si at 10 and 100 keV: 1 - y_C with y_C = [1/(a E) + 1/y_L]^-1, a = 0.247/keV (1803.02903 Eq. (4)),
      the parameterization the CDMS II data follow; Lindhard (k_L = 0.146) as the variant.
  One-sided 95 % limit of a Gaussian: z = 1.645 (App. C.14).
  Reading: <E_st>/E_R = (xi/2)(T_d/E_R) p_surv E_FP/E_d (eq:19.4-loss) with xi = 0.8 (formula) and 0.70 (screened count).

Part C. Worked example 19.4: 300 eV silicon recoil.
  Measured Si yields 0.108 (0.22 keV) and 0.136 (0.46 keV) (2303.02196 Table II), log-interpolated to 0.30 keV;
  formation energies (Holmstrom et al. 2008 Table III, Sect. 7.4): close Frenkel pair 6.8-7.5 eV, vacancy 3.4-3.9 eV,
  interstitial 4.7-5.8 eV, bond defect 2.6-3.0 eV; E_d = 36 eV (Frenkel pair, average) and 24 eV (any defect).
"""
import os
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "..", "tex", "figures", "ch19"))
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- Thomas-Fermi cross-section (as lind19_3.py)
Z, A = 14, 28.0855
A0, E2G = 0.529177, 14.39965
aL = 0.8853 * A0 / (np.sqrt(2) * Z**(1 / 3))
cL = aL / (2 * Z**2 * E2G)               # eV^-1
kL = 0.133 * Z**(2 / 3) / np.sqrt(A)

def tf_shoot(B, xmax=40.0):
    x0 = 1e-6
    y0 = [1 + B * x0 + 4 / 3 * x0**1.5, B + 2 * x0**0.5]
    def rhs(x, y):
        return [y[1], max(y[0], 0.0)**1.5 / np.sqrt(x)]
    ev1 = lambda x, y: y[0]; ev1.terminal = True
    ev2 = lambda x, y: y[1]; ev2.terminal = True
    return solve_ivp(rhs, (x0, xmax), y0, rtol=1e-12, atol=1e-14, events=(ev1, ev2), dense_output=True)

lo, hi = -1.60, -1.57
for _ in range(60):
    mid = 0.5 * (lo + hi)
    if tf_shoot(mid).t_events[0].size:
        lo = mid
    else:
        hi = mid
B = 0.5 * (lo + hi)
sol = tf_shoot(B)
xm = sol.t[-1] * 0.6
phim = sol.sol(xm)[0]
def phi(r):
    r = np.asarray(r, float); out = np.empty_like(r); m = r <= xm
    if m.any(): out[m] = sol.sol(np.maximum(r[m], 1e-6))[0]
    out[~m] = phim * (xm / r[~m])**3
    return out
def dphi(r):
    r = np.asarray(r, float); out = np.empty_like(r); m = r <= xm
    if m.any(): out[m] = sol.sol(np.maximum(r[m], 1e-6))[1]
    out[~m] = -3 * phim * xm**3 / r[~m]**4
    return out
uu = np.linspace(0, 12, 6001)
def dIdb(beta):
    r = beta * np.cosh(uu)
    return np.trapezoid((beta / r) * (dphi(r) / r - phi(r) / r**2) * beta * np.cosh(uu), uu)
betas = np.geomspace(1e-4, 60, 900)
xs = np.array([-0.5 * dIdb(b) for b in betas])
dlx = np.gradient(np.log(xs), np.log(betas))
fx = 2 * xs**2 * betas / (xs * np.abs(dlx) / betas)
o = np.argsort(xs); X, F = xs[o], fx[o]
XC = 2e-3
def f_tf(x):
    x = np.asarray(x, float)
    out = np.exp(np.interp(np.log(x), np.log(X), np.log(F)))
    big = x > X[-1]; out[big] = 0.5 / x[big]
    return out
FC = float(f_tf(np.array([XC]))[0])
def f_of_x(x):
    x = np.asarray(x, float); out = f_tf(x); sm = x < XC
    out[sm] = FC * (x[sm] / XC)**(1 / 3)
    return out
print(f"Thomas-Fermi phi'(0) = {B:.6f}; f(1e-3) = {float(f_of_x(np.array([1e-3]))[0]):.4f} "
      f"(lind19_3.log: 0.1283); c_L = {cL*1e3:.5f} keV^-1")

# ---------------------------------------------------------------- Part A: displacement count
def kernel(kind, Ed):
    if kind == "hs":
        return lambda s, u: np.ones_like(s)
    if kind == "pl":
        return lambda s, u: s**(-4 / 3)
    if kind == "tf":
        return lambda s, u: f_of_x(cL * Ed * u * np.sqrt(s)) * s**(-1.5)
    raise ValueError(kind)

def sgrid(a, b, n):
    """geometric grid on [a, b] dense at both ends (a > 0, b < 1)."""
    m = 0.5 * (a + b)
    left = np.geomspace(a, m, n)
    right = 1 - np.geomspace(1 - b, 1 - m, n)[::-1]
    return np.concatenate([left, right[1:]])

def solve_count(kind, Ed=36.0, umax=1000.0, NU=3000, NS=700):
    K = kernel(kind, Ed)
    u = np.geomspace(2.0, umax, NU)
    n = np.zeros(NU)
    def n_at(v, i):
        v = np.asarray(v, float)
        res = np.interp(v, u[:i], n[:i], left=0.0, right=np.nan)
        res[v < 2.0] = 0.0
        return res
    for i in range(1, NU):
        ui, h = u[i], u[i] - u[i - 1]
        s0 = h / ui
        # A: small-s part, n(u) - n(u(1-s)) ~ n'(u) u s with n' = (n_i - n_{i-1})/h
        sa = np.geomspace(1e-14, s0, 200)
        IA = np.trapezoid(K(sa, ui) * sa, sa) * ui / h          # times (n_i - n_{i-1})
        # B and C on s in [s0, 1 - s0]; the last interval [1 - s0, 1] handled by interpolation in C
        s = sgrid(s0, 1 - 1e-12, NS)
        Ks = K(s, ui)
        IB_coef = np.trapezoid(Ks, s)                            # times n_i
        v1 = ui * (1 - s)                                         # <= u_{i-1}
        IB_known = -np.trapezoid(Ks * n_at(v1, i), s)
        v2 = ui * s
        up = v2 > u[i - 1]
        nk = np.where(up, 0.0, n_at(np.minimum(v2, u[i - 1]), i))
        wgt = np.where(up, (v2 - u[i - 1]) / h, 0.0)             # n(us) = n_{i-1}(1 - w) + n_i w on the top interval
        IC_coef = -np.trapezoid(Ks * wgt, s)
        IC_known = -np.trapezoid(Ks * (nk + np.where(up, n[i - 1] * (1 - wgt), 0.0)), s)
        # D: both atoms displaced
        if ui > 2.0:
            sd = sgrid(1 / ui, 1 - 1 / ui, NS)
            ID = -np.trapezoid(K(sd, ui), sd)
        else:
            ID = 0.0
        a = IA + IB_coef + IC_coef
        b = -IA * n[i - 1] + IB_known + IC_known + ID
        n[i] = -b / a
    return u, n

def NFP(u, n, T):
    T = np.asarray(T, float)
    out = np.where(T < 1, 0.0, 1.0)
    m = T >= 2
    out[m] = 1 + np.interp(T[m], u, n)
    return out

def nrt(T):
    T = np.asarray(T, float)
    return np.where(T < 1, 0.0, np.where(T < 2 / 0.8, 1.0, 0.8 * T / 2))

uh, nh = solve_count("hs", NU=1500, NS=400)
print("\nPart A. Displacement count N_FP(T_d), T_d in units of E_d")
print("  hard spheres (check against Kinchin-Pease T_d/2E_d):")
for T in (3, 10, 100, 1000):
    print(f"    T_d/E_d = {T:5d}: N_FP = {NFP(uh, nh, [T])[0]:.4f}, Kinchin-Pease {T/2:.4f}")

res = {}
for kind, Ed in (("tf", 36.0), ("tf", 12.5), ("tf", 20.0), ("pl", 36.0)):
    u, n = solve_count(kind, Ed=Ed)
    res[(kind, Ed)] = (u, n)
u2, n2 = solve_count("tf", Ed=36.0, NU=1500, NS=350)
u1, n1 = res[("tf", 36.0)]
print("  screened Thomas-Fermi cross-section (silicon), E_d = 36 eV; xi_eff = 2 N_FP E_d/T_d:")
print("    T_d/E_d   N_FP     N_FP(half grid)   xi_eff    NRT N_FP   NRT/computed")
for T in (2.5, 3, 5, 7.36, 10, 20, 50, 100, 300, 1000):
    a1 = NFP(u1, n1, [T])[0]; a2 = NFP(u2, n2, [T])[0]
    print(f"    {T:7.2f}  {a1:7.4f}  {a2:7.4f}          {2*a1/T:.4f}    {nrt([T])[0]:7.4f}    {nrt([T])[0]/a1:.4f}")
for key in (("tf", 12.5), ("tf", 20.0), ("pl", 36.0)):
    u, n = res[key]
    vals = [2 * NFP(u, n, [T])[0] / T for T in (10, 100, 300, 1000)]
    print(f"  {key}: xi_eff at T_d/E_d = 10, 100, 300, 1000: " + ", ".join(f"{v:.4f}" for v in vals))
# asymptotic xi from the slope of N_FP between 1000 and 3000 E_d
for key in (("tf", 36.0), ("tf", 12.5), ("pl", 36.0)):
    u, n = res[key]
    sl = (NFP(u, n, [1000])[0] - NFP(u, n, [300])[0]) / 700 * 2
    print(f"  {key}: asymptotic slope 2 dN_FP/d(T_d/E_d) (300-1000 E_d) = {sl:.4f}")

# independent check of the count: direct Monte Carlo of the same rules with the power law dsigma ~ T^(-4/3) dT
rng = np.random.default_rng(1)
def mc_cascade(E0, Tmin=1e-4, m=1/3):
    count, stack = 1, [E0]
    while stack:
        E = stack.pop()
        while E >= 2:
            sc = Tmin / E; a = sc**(-m)
            s_ = (a - rng.random() * (a - 1))**(-1 / m)
            E -= E * (sc**(1 - m) / (1 - m)) / ((a - 1) / m)     # transfers below Tmin as a continuous loss
            Tt = s_ * E
            if Tt > 1:
                if E - Tt > 1:
                    count += 1; stack.append(Tt); E -= Tt
                else:
                    E = Tt                                      # replacement: the struck atom moves on
            else:
                E -= Tt
    return count
for E0 in (10.0, 100.0):
    c = np.array([mc_cascade(E0) for _ in range(4000)])
    upl_, npl_ = res[("pl", 36.0)]
    print(f"  Monte Carlo check (power law, 4000 cascades): T_d/E_d = {E0:.0f}: N_FP = {c.mean():.3f} +/- "
          f"{c.std()/np.sqrt(c.size):.3f}; integral equation {NFP(upl_, npl_, [E0])[0]:.3f}")
# where NRT is within 10 % (5 %) of the screened solution, on a fine grid
Tg = np.geomspace(1.0, 1000, 200001)
rat = nrt(Tg) / NFP(u1, n1, Tg)
for lev in (0.10, 0.05):
    ok = np.abs(rat - 1) <= lev
    if ok.any():
        print(f"  NRT within {lev*100:.0f} % of the screened solution on T_d/E_d in [{Tg[ok].min():.3f}, {Tg[ok].max():.3f}]"
              f" (fraction of the grid inside: {ok.mean():.3f})")
    else:
        print(f"  NRT nowhere within {lev*100:.0f} %")
print(f"  NRT/computed - 1 below 2.5 E_d: max {np.max(rat[(Tg < 2.5)]-1):+.3f}, min {np.min(rat[Tg<2.5]-1):+.3f} "
      f"(at T_d/E_d = {Tg[Tg<2.5][np.argmin(rat[Tg<2.5])]:.3f})")
for T_ in (10, 30):
    print(f"  NRT/computed over T_d >= {T_} E_d: {rat[Tg >= T_].min():.4f} .. {rat[Tg >= T_].max():.4f}")
TE = Tg[Tg >= 1]
r_hi = rat[Tg >= 2.5]
print(f"  NRT/computed over T_d >= 2.5 E_d: {r_hi.min():.4f} .. {r_hi.max():.4f}")
print(f"  Kinchin-Pease/computed at T_d/E_d = 100, 1000: {50/NFP(u1,n1,[100])[0]:.4f}, {500/NFP(u1,n1,[1000])[0]:.4f}")

# ---------------------------------------------------------------- Part B: bounds (Table 19.1)
# The bound on <E_st>/E_R itself, its conditions (a)-(e) and every collection-ratio dependence are computed in
# bal19_5.py (Sect. 19.5, one script for the calibration chain).  Here: the germanium datum, the 95 % limits that
# do not depend on the collection ratio, and their reading through eq:19.4-loss.
print("\nPart B. Calibration data and stored-energy bounds (Table 19.1)")
A_C = 0.247   # keV^-1, Chavarria parameterization y_C = [1/(a E) + 1/y_L]^-1 (1803.02903 Eq. (4)), which the CDMS II
              # silicon data follow below 20 keV (Sect. 4.1); Lindhard is the variant
def yL(ER_keV, k=kL):
    e = cL * 1e3 * ER_keV
    g = 3 * e**0.15 + 0.7 * e**0.6 + e
    return k * g / (1 + k * g)
def yC(ER_keV):
    return 1.0 / (1.0 / (A_C * ER_keV) + 1.0 / yL(ER_keV))
YqSi = {10: yC(10.0), 100: yC(100.0)}
YqSiL = {10: yL(10.0), 100: yL(100.0)}
print(f"  Si yields: y_C(10 keV) = {YqSi[10]:.4f}, y_C(100 keV) = {YqSi[100]:.4f} -> T_d/E_R = {1-YqSi[10]:.4f}, {1-YqSi[100]:.4f}"
      f"; Lindhard variant (k_L = {kL:.4f}): {YqSiL[10]:.4f}, {YqSiL[100]:.4f} -> {1-YqSiL[10]:.4f}, {1-YqSiL[100]:.4f}")
YphSi, YphSi_lo, YphSi_hi = 0.952, 0.945, 0.961
fSi = 1 - YphSi; fSi_max = 1 - YphSi_lo
fSi_book = 0.0491   # bound with the book's eps_eh = 3.75 eV at r_coll = 1 (bal19_5.log, Sect. 4)
print(f"  Si: f_DF = {fSi:.3f}; 95 % C.L. bound 1 - Y_lo = {fSi_max:.3f} (conditions (a)-(e)); with the book's eps_eh: {fSi_book}")
fGe, sGe = 0.0608, 0.0018
fGe_95 = fGe + 1.645 * sGe; fGe_2s = fGe + 2 * sGe
print(f"  Ge: f_DF = {fGe:.4f} +/- {sGe:.4f}; one-sided 95 % (z = 1.645): {fGe_95:.4f}; at 2 sigma: {fGe_2s:.4f}")
d1 = (6.22, 0.11); d2 = (5.87, 0.13)
w1, w2 = 1 / d1[1]**2, 1 / d2[1]**2
mw = (w1 * d1[0] + w2 * d2[0]) / (w1 + w2); sw = (w1 + w2)**-0.5
print(f"    detectors: weighted mean {mw:.3f} +/- {sw:.3f} %, difference {(d1[0]-d2[0])/np.hypot(d1[1], d2[1]):.2f} sigma; "
      f"inflated {sw*(d1[0]-d2[0])/np.hypot(d1[1], d2[1]):.3f} %")
for (f, fs) in ((5.52, -0.75), (6.67, 0.85)):
    print(f"    check Eq. (4): f = {f}, f_sur = {fs}: f_DF = {100*(1-(1-f/100)/(1-fs/100)):.3f} %")
YqGe = 0.3
print(f"  Ge Pb recoils: observed surface-event yield ~ {YqGe} is a lower edge of the electronic share (surface events lose "
      f"charge), so T_d/E_R <= {1-YqGe:.2f}")
# NRT and screened readings, <E_st>/E_R = (xi/2)(T_d/E_R) p_surv E_FP/E_d
print("  reading through eq:19.4-loss, p_surv E_FP/E_d <= 2 bound/(xi T_d/E_R):")
xi_comp = 2 * NFP(u1, n1, [1000])[0] / 1000
for xi, lab in ((0.8, "NRT 0.8"), (0.70, "screened 0.70"), (xi_comp, "screened (1000 E_d)"), (1.0, "Kinchin-Pease")):
    for E in (10, 100):
        print(f"    Si {E:3d} keV, {lab:20s}: {2*fSi_max/(xi*(1-YqSi[E])):.3f} (Lindhard damage fraction: "
              f"{2*fSi_max/(xi*(1-YqSiL[E])):.3f}; book-eps bound {fSi_book}: {2*fSi_book/(xi*(1-YqSi[E])):.3f})")
    print(f"    Ge 103 keV, {lab:20s}: >= {2*fGe_95/(xi*(1-YqGe)):.3f} (central {2*fGe/(xi*(1-YqGe)):.3f}); "
          f"at T_d/E_R = 0.6: {2*fGe_95/(xi*0.6):.3f}")
for (EFP, lab) in (((6.8, 7.5), "close pair"), ((3.4 + 4.7, 3.9 + 5.8), "separated pair")):
    for E in (10, 100):
        for xi in (0.8, 0.70):
            v = 2 * fSi_max / (xi * (1 - YqSi[E]))
            print(f"    Si {E} keV, xi = {xi}, {lab} {EFP[0]:.1f}-{EFP[1]:.1f} eV, E_d = 36 eV: p_surv <= "
                  f"{v*36/EFP[1]:.2f} .. {v*36/EFP[0]:.2f}")
    full = [0.4 * (1 - YqSi[E]) * np.array(EFP) / 36 for E in (10, 100)]
    print(f"    NRT <E_st>/E_R at p_surv = 1, {lab}: 10 keV {full[0][0]:.4f}-{full[0][1]:.4f}, "
          f"100 keV {full[1][0]:.4f}-{full[1][1]:.4f}")
pE = 2 * fGe * 19.7 / (0.8 * (1 - YqGe))
print(f"  Ge: E_d = 19.7 eV within NRT corresponds to p_surv E_FP = 2 f_DF E_d/(0.8 T_d/E_R) = {pE:.2f} eV; "
      f"E_d per eV of p_surv E_FP = {19.7/pE:.2f} eV")
for pE_ in (3.0, 6.0, 9.0):
    print(f"    p_surv E_FP = {pE_} eV -> E_d = {0.8*(1-YqGe)*pE_/(2*fGe):.1f} eV (NRT), "
          f"{xi_comp*(1-YqGe)*pE_/(2*fGe):.1f} eV (screened xi), {1.0*(1-YqGe)*pE_/(2*fGe):.1f} eV (Kinchin-Pease)")

# ---------------------------------------------------------------- Part C: worked example, 300 eV Si recoil
print("\nPart C. Worked example: 300 eV silicon recoil")
EA, YA, EB, YB = 0.22, 0.108, 0.46, 0.136
Y300 = np.exp(np.interp(np.log(0.30), np.log([EA, EB]), np.log([YA, YB])))
Td = 300 * (1 - Y300)
print(f"  Y_q(0.30 keV) log-interpolated = {Y300:.4f}; T_d = E_R(1 - Y_q) = {Td:.1f} eV (Y_q E_R = {300*Y300:.1f} eV "
      f"is an upper value of the electronic share, Sect. 19.2)")
for Ed in (36.0, 24.0):
    T = Td / Ed
    u, n = res[("tf", 36.0)] if Ed == 36.0 else solve_count("tf", Ed=24.0)
    kp = T / 2; nr = nrt([T])[0]; tf = NFP(u, n, [T])[0]
    print(f"  E_d = {Ed}: T_d/E_d = {T:.3f}; Kinchin-Pease {kp:.3f}, NRT {nr:.3f}, screened {tf:.3f}")
    for (EFP, lab) in (((6.8, 7.5), "close"), ((8.1, 9.7), "separated"), ((2.6, 3.0), "bond defect")):
        lo_, hi_ = tf * EFP[0], tf * EFP[1]
        print(f"     stored (p_surv = 1, {lab} {EFP[0]}-{EFP[1]} eV, screened count): {lo_:.1f}-{hi_:.1f} eV = "
              f"{100*lo_/300:.1f}-{100*hi_/300:.1f} % of E_R")
    lo_, hi_ = nr * 6.8, nr * 9.7
    print(f"     NRT count x 6.8-9.7 eV: {lo_:.1f}-{hi_:.1f} eV = {100*lo_/300:.1f}-{100*hi_/300:.1f} %")
# what the 10 keV bound on p_surv E_FP/E_d implies if carried to 300 eV
v10 = 2 * fSi_max / (0.8 * (1 - YqSi[10]))
print(f"  carrying p_surv E_FP/E_d <= {v10:.3f} (10 keV, NRT) to 300 eV: <E_st>/E_R <= 0.4 (T_d/E_R) x {v10:.3f} = "
      f"{0.4*(1-Y300)*v10:.4f}; with the screened count at T_d/E_d = {Td/36:.2f}: "
      f"{NFP(u1, n1, [Td/36])[0]*36*v10/300:.4f}")
EFPmax = v10 * 36
print(f"  equivalently p_surv E_FP <= {EFPmax:.2f} eV at E_d = 36 eV")
v10s = 2 * fSi_max / (xi_comp * (1 - YqSi[10]))
print(f"  consistent screened reading: p_surv E_FP/E_d <= {v10s:.3f} at 10 keV -> at 300 eV <E_st>/E_R <= "
      f"{NFP(u1, n1, [Td/36])[0]*36*v10s/300:.4f}")
from math import sqrt
print(f"  reduced mass needed for E_R = 300 eV in Si (eq:1.3-ERmax, M = 26.16 GeV, v_max = 2.650e-3): "
      f"{sqrt(26.16e9*300/2)/2.650e-3:.4e} eV")
M = 26.16e9; vmax = 2.650e-3
mchi = brentq(lambda m: 2 * (m * M / (m + M))**2 * vmax**2 / M - 300, 1e6, 1e11)
print(f"  exact: m_chi >= {mchi/1e9:.3f} GeV")
# electron recoils store no energy: largest transfer from an electron of kinetic energy E to a Si nucleus
me = 0.51099895e6
for Ed_ in (12.5, 36.0):
    Ee = brentq(lambda E: 2 * E * (E + 2 * me) / M - Ed_, 1.0, 1e8)
    print(f"  electron kinetic energy at which 2E(E + 2m_e)/M = {Ed_} eV (Si): {Ee/1e6:.3f} MeV")
print(f"  largest transfer from a 10 eV electron (non-relativistic 4 m_e E/M): {4*me*10/M*1e3:.3f} meV")


# ---------------------------------------------------------------- Figures
plt.rcParams.update({"font.size": 9})
# Limit Check 19.4a
fig, ax = plt.subplots(figsize=(6.0, 3.6))
T = np.geomspace(1.0, 1000, 3000)
T10 = 2.5
ax.axvspan(T10, 1000, color="0.88", lw=0)
ax.plot(T, 2 * NFP(u1, n1, T) / T, color="k", lw=1.5, label=r"screened cross-section, $E_{\mathrm{d}} = 36$ eV")
u12, n12 = res[("tf", 12.5)]
ax.plot(T, 2 * NFP(u12, n12, T) / T, color="k", lw=0.9, ls="--", label=r"screened cross-section, $E_{\mathrm{d}} = 12.5$ eV")
upl, npl = res[("pl", 36.0)]
ax.plot(T, 2 * NFP(upl, npl, T) / T, color="C0", lw=1.0, ls=":", label=r"power law $\mathrm{d}\sigma \propto T^{-4/3}\mathrm{d}T$")
ax.plot(T, 2 * NFP(uh, nh, T) / T, color="C2", lw=1.0, ls="-.", label="hard spheres (Kinchin–Pease)")
ax.plot(T, 2 * nrt(T) / T, color="C3", lw=1.3, label="NRT formula")
ax.set_xscale("log")
ax.set_xlim(1, 1000)
ax.set_ylim(0, 2.1)
ax.set_xlabel(r"damage energy $T_{\mathrm{d}}/E_{\mathrm{d}}$")
ax.set_ylabel(r"$2E_{\mathrm{d}}N_{\mathrm{FP}}/T_{\mathrm{d}}$")
ax.text(T10 * 1.15, 1.95, r"linear range of the formula, $T_{\mathrm{d}} \geq 2.5E_{\mathrm{d}}$", fontsize=8, color="0.3")
ax.legend(fontsize=7.5, loc="upper right", frameon=False, bbox_to_anchor=(1.0, 0.93))
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit19_4a.pdf"))
plt.close(fig)
print(f"\nLimit Check 19.4a: shaded T_d/E_d >= {T10:.3f} (the formula's linear range)")

print("wrote limit19_4a.pdf")
