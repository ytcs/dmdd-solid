"""The energy balance law, heat quenching, the phonon-yield ratio and the stored-energy bound (Sect. 19.5).

Every number printed in Sect. 19.5, its worked example (we:19-degeneracy), Appendix D.45, Table 19.1 (bounds column
<E_st>/E_R) and the two Limit Checks 19.5a, 19.5b, plus Fig. 19.4.  Run:  python bal19_5.py > bal19_5.log  (seconds).
Outputs: tex/figures/ch19/fig19_4.pdf (fig:19-shares), limit19_5a.pdf (fig:19-limit-heat), limit19_5b.pdf
(fig:19-limit-yield; two panels: phonon-yield ratio and stored-energy bound against the collection ratio).

Inputs (book values and sources)
  E_g      = 1.17 eV      silicon gap at low temperature (Sect. 3.3, tab:3-materials)
  eps_eh   = 3.75 eV      true silicon pair energy, measured 3.749 eV rounded (Sect. 18.4, rodrigues2021absolute);
                          the computed 3.7468 eV of the book's cascade agrees (Sect. 18.4)
  eps_cal  = 3.82 eV      pair energy ADOPTED by the CDMS II reconstruction (1803.02903, footnote 2: "For silicon,
                          eps = 3.82 eV above 77 K"); it enters both the phonon scale and the Luke subtraction,
                          E_R = E_phi - E_Q eV_b/eps (Eq. (1)), the phonon scale being set so that bulk electron recoils
                          (ionization yield y = 1) read E_phi = E_R(1 + eV_b/eps) (Sect. 2.1).  The Luke phonons follow the
                          TRUE pair number omega/eps_eh.
  V_bias   = 4 V          CDMS II silicon detectors, 4 V across 1 cm (1803.02903, Sect. 2)
  Y_ph     = 0.952 +0.009 -0.007 (95 % C.L.), NR over ER phonon collection efficiency, 10-100 keV, 252Cf neutrons,
             fit dominated by the elastic resonance near E_R = 20 keV (1803.02903, abstract, Sects. 3.2, 4)
  Ionized fraction f_ion: the source's own yield parameterization y_C = [1/(a E_R) + 1/y_L]^(-1), a = 0.247 keV^-1
             (1803.02903 Eq. (4), Fig. 11), which the CDMS II data follow below 20 keV and relative to which their
             ionization collection efficiency is ~100 % below 20 keV and ~75 % at 100 keV (Sect. 4.1, Fig. 12).
             Variant: Lindhard y_L, k_L = 0.133 Z^(2/3) A^(-1/2), eps_L = 11.5 Z^(-7/3) E_R/keV (eq:16.6-lindhard),
             which the source says over-estimates the yield below ~20 keV (Sect. 5).
  Y_q      = 0.102 (0.10 keV), 0.127 (0.89 keV), 0.236 (3.91 keV): measured silicon yields (albakry2023first =
             arXiv:2303.02196, Table II), as in Sect. 19.2
  Phonon absorption time of the crystal in Fig. 19.4: 58 us, the pulse fall time tau_f of the 10.6 g silicon detector
             of alkhatib2021light (arXiv:2007.14289, p. 2). MODELLING CHOICE: single exponential absorption.
  Pair kinetics at zero field in Fig. 19.4: the illustrative rates of Fig. 18.4 (figscripts/ch18/end18_5.py),
             copied here: G_FX = 1e9/s, trapped fraction 0.05, G_X = 1e5/s with luminescent fraction 0.1,
             G_XB = 1e6/s, bound-exciton Auger decay 250 ns (Lo et al., quoted in Sect. 18.5).
  Stored energy in Fig. 19.4: E_st = 0.055 E_R, set equal to the silicon bound of Table 19.1 for display, frozen.
             ILLUSTRATIVE.
  Germanium: f_DF = 0.0608 +/- 0.0018 (1805.09942, Sect. V A); one-sided 95 % limit 0.0608 + 1.645 x 0.0018 (App. C.14);
             damage fraction T_d/E_R <= 0.7 from the observed surface-event yield ~0.3 (1805.09942, Sect. II).
  Zero-point change per surviving displacement, for the sign discussion of condition (c): |Delta E_zp| ~ 0.1 eV, the
             estimate of Sect. 19.5; displacement count 0.8 T_d/(2 E_d) (lim:19.4a), E_d = 36 eV (Si), 19.7 eV (Ge).

Model of the phonon signal (Sect. 19.5, App. D.45), per unit deposit omega, with g_t = eV_bias/eps_eh (Luke gain,
g_Luke in the text) and g_c = eV_bias/eps_cal (the gain the reconstruction assumes, g_cal in the text):
  S_ER = eps_p [ (1 - d_ER) + r g_t ]             (ER: all pairs drifted, bias work g_t omega)
  S_NR = eps_p [ (1 - delta)(1 - d_NR) + r g_t f ]
  ER calibration: E_R^rec = (1 + g_c) S/S_ER omega - f g_c omega,  Y_ph = E_R^rec / omega
  r = collection ratio (Luke over ER primary), delta = collection offset, f = ionized fraction, d = missing energy/omega.
  For eps_cal = eps_eh (g_c = g_t) every formula reduces to the single-gain form.
"""
import os
import numpy as np
import sympy as sp
from scipy.optimize import brentq
from scipy.linalg import expm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch19")
os.makedirs(FIG, exist_ok=True)

EG = 1.17
EPS = 3.75                         # true pair energy (book)
EPS_CAL = 3.82                     # pair energy adopted by the CDMS II reconstruction
GG = EG / EPS                      # gap share of an electron-recoil deposit, E_g/eps_eh
Y_MEAS, Y_UP, Y_DN = 0.952, 0.009, 0.007
Y_LO, Y_HI = Y_MEAS - Y_DN, Y_MEAS + Y_UP
Z, A = 14, 28.0855
A_C = 0.247                        # keV^-1, Chavarria parameter (1803.02903 Eq. (4))


def section(t):
    print("\n" + "=" * 100 + "\n" + t + "\n" + "=" * 100)


def lindhard(E_keV, k=None):
    """Lindhard electronic share y_L for a one-element target (eq:16.6-lindhard)."""
    if k is None:
        k = 0.133 * Z ** (2 / 3) * A ** -0.5
    e = 11.5 * E_keV * Z ** (-7 / 3)
    g = 3 * e ** 0.15 + 0.7 * e ** 0.6 + e
    return k * g / (1 + k * g)


def chavarria(E_keV):
    """y_C = [1/(a E) + 1/y_L]^-1 (1803.02903 Eq. (4))."""
    return 1.0 / (1.0 / (A_C * E_keV) + 1.0 / lindhard(E_keV))


def gains(V):
    return V / EPS, V / EPS_CAL


def yph(V, r, f, delta=0.0, dN=0.0, dE=0.0, eps_cal=EPS_CAL):
    """Exact phonon-yield ratio with ER calibration at pair energy eps_cal (eq:19.5-identity)."""
    gt, gc = V / EPS, V / eps_cal
    return (1 + gc) * ((1 - delta) * (1 - dN) + r * gt * f) / (1 - dE + r * gt) - f * gc


def ccal(V, r, f):
    gt = V / EPS
    return (1 + r * gt * f) / (1 + r * gt)


def yph_first(V, r, f, delta=0.0, dN=0.0, dE=0.0):
    """First-order form eq:19.5-first."""
    gt, gc = gains(V)
    return 1 - (r * gt - gc) * (1 - f) / (1 + r * gt) - (1 + gc) / (1 + r * gt) * (delta + dN - ccal(V, r, f) * dE)


def e_line(Y, r, f, V=4.0, eps_cal=EPS_CAL):
    """Inferred stored fraction at delta = x = 0 (eq:19.5-widen): e = 1 - Y + (g_c - r g_t)(Y - f)/(1 + g_c)."""
    gt, gc = V / EPS, V / eps_cal
    return (1 - Y) + (gc - r * gt) * (Y - f) / (1 + gc)


def r_only(Y, f, V=4.0, eps_cal=EPS_CAL):
    """Collection ratio that reproduces Y with no stored energy and no other deficit."""
    gt, gc = V / EPS, V / eps_cal
    return ((1 - Y) + gc * (1 - f)) / (gt * (Y - f))


# ------------------------------------------------------------------------------------------------ symbolic checks
section("1. Symbolic checks (sympy), reconstruction gain g_c and true Luke gain g_t kept apart")
gt_, gc_, r, f, dl, dN, dE, e, xN, xE, t = sp.symbols("g_t g_c r f delta d_N d_E e x_N x_E t", real=True)
Yex = (1 + gc_) * ((1 - dl) * (1 - dN) + r * gt_ * f) / (1 - dE + r * gt_) - f * gc_
Y0 = sp.simplify(Yex.subs({dl: 0, dN: 0, dE: 0}))
print("(a) zero deficits: 1 - Y - (r g_t - g_c)(1-f)/(1 + r g_t) =",
      sp.simplify(1 - Y0 - (r * gt_ - gc_) * (1 - f) / (1 + r * gt_)))
print("    at r = 1, no deficits: Y - 1 - (g_c - g_t)(1 - f)/(1 + g_t) =",
      sp.simplify(Y0.subs(r, 1) - 1 - (gc_ - gt_) * (1 - f) / (1 + gt_)))
lam = sp.symbols("lam")
ser = sp.series(Yex.subs({dl: lam * dl, dN: lam * dN, dE: lam * dE}), lam, 0, 2).removeO().subs(lam, 1)
first = 1 - (r * gt_ - gc_) * (1 - f) / (1 + r * gt_) - (1 + gc_) / (1 + r * gt_) * (dl + dN - (1 + r * gt_ * f) / (1 + r * gt_) * dE)
print("(b) first-order expansion minus eq:19.5-first =", sp.simplify(ser - first))
Yb = Yex.subs({dN: e + xN, dE: xE})
rhs = ((r * gt_ - gc_) * (1 - e - f) + (1 + gc_) * dl * (1 - e) + (1 + gc_) * (1 - dl) * xN - (1 - e + f * gc_) * xE) / (1 - xE + r * gt_)
print("(c) 1 - Y - e minus the exact bound identity eq:19.5-bound =", sp.simplify(1 - Yb - e - rhs))
Y = sp.symbols("Y")
lin = (1 + gc_) * (1 - dl) * (1 - dN) - (Y + f * gc_) * (1 - dE) - r * gt_ * (Y - f)
print("(d) linear form (1+g_c)A - (Y + f g_c)B - r g_t (Y - f) at Y = Yexact:", sp.simplify(lin.subs(Y, Yex) * (1 - dE + r * gt_)))
esol = sp.solve(sp.Eq(Yex.subs({dl: 0, dN: e, dE: 0}), Y), e)[0]
print("(e) e(r) - [(1-Y) + (g_c - r g_t)(Y-f)/(1+g_c)] =", sp.simplify(esol - ((1 - Y) + (gc_ - r * gt_) * (Y - f) / (1 + gc_))))
Yh, rp = sp.symbols("Y_H rp")
calib = ((1 + gc_) * Yh + f * (rp * gt_ - gc_)) / (1 + rp * gt_)
print("(f) calibration identity: Yexact - [(1+g_c)Y(0) + f(r' g_t - g_c)]/(1 + r' g_t) with Y(0) = A/B, r' = r/B:",
      sp.simplify(Yex - calib.subs({Yh: (1 - dl) * (1 - dN) / (1 - dE), rp: r / (1 - dE)})))
n = sp.Function("n")
s1 = sp.dsolve(sp.Eq(n(t).diff(t), -n(t) ** 2), ics={n(0): 1})
s2 = sp.dsolve(sp.Eq(n(t).diff(t), -n(t) ** 3 / 2), ics={n(0): 1})
print("(g) dn/dt = -n^2, n(0) = 1:", s1, "; dn/dt = -n^3/2:", s2, "(time in units of t0)")
# two biases: g_t,i = kap g_c,i with kap = eps_cal/eps_eh
kap, c1, c2, Y1, Y2 = sp.symbols("kappa c1 c2 Y1 Y2", positive=True)
M2s = sp.Matrix([[1 + c1, -kap * c1 * (Y1 - f)], [1 + c2, -kap * c2 * (Y2 - f)]])
det = M2s.det()
print("(h) determinant (g_t,i = kappa g_c,i):", sp.factor(det), "; at Y1 = Y2 = Y:", sp.factor(det.subs({Y1: Y, Y2: Y})))
sol = M2s.LUsolve(sp.Matrix([Y1 + f * c1, Y2 + f * c2]))
print("    equal ratios Y1 = Y2 = Y: Y(0) =", sp.simplify(sol[0].subs({Y1: Y, Y2: Y})), "; r' =", sp.simplify(sol[1].subs({Y1: Y, Y2: Y})),
      "(= eps_eh/eps_cal)")
print("    large-bias limit of the calibration identity:", sp.simplify(sp.limit(calib.subs(gt_, kap * gc_), gc_, sp.oo)))

# ------------------------------------------------------------------------------------------------ Luke gain, f_ion
section("2. Luke gains and ionized fraction (silicon)")
kL = 0.133 * Z ** (2 / 3) * A ** -0.5
print(f"k_L = {kL:.4f} (rounded 0.146 in Sect. 19.3); eps_cal/eps_eh = {EPS_CAL/EPS:.5f}")
for V in (4.0, 40.0, 100.0):
    gt, gc = gains(V)
    print(f"V_bias = {V:5.1f} V: g_Luke = eV/eps_eh = {gt:.4f}; g_cal = eV/eps_cal = {gc:.4f}; g_cal - g_Luke = {gc-gt:+.4f}")
g4t, g4c = gains(4.0)
g40t, g40c = gains(40.0)
fC, fL = {}, {}
for E in (10.0, 20.0, 100.0):
    fC[E], fL[E] = chavarria(E), lindhard(E)
    print(f"E_R = {E:5.1f} keV: y_C = {fC[E]:.4f}   (Lindhard y_L = {fL[E]:.4f}; damage fractions 1 - y: {1-fC[E]:.4f}, {1-fL[E]:.4f})")
f20 = fC[20.0]
f100c = 0.75 * fC[100.0]
print(f"f_ion at the 20 keV resonance: {f20:.4f} (y_C, central); 0.75 y_C(100 keV) = {f100c:.4f}; E_g/eps_eh = {GG:.4f}")

# ------------------------------------------------------------------------------------------------ readings of the datum
section("3. The silicon datum (4 V): stored energy alone, collection alone, mixtures (WE 19.5)")
print(f"eps-mismatch term at r = 1, no deficits: Y - 1 = (g_cal - g_Luke)(1 - f)/(1 + g_Luke) = {(g4c-g4t)*(1-f20)/(1+g4t):+.4f}"
      f" (f = {f20:.4f}); Lindhard f: {(g4c-g4t)*(1-fL[20.0])/(1+g4t):+.4f}; half-width of the band {(Y_UP+Y_DN)/2:.4f}")
e_st = e_line(Y_MEAS, 1.0, f20)
e_edge = e_line(Y_LO, 1.0, f20)
print(f"stored energy alone (r = 1, delta = x = 0): E_st/omega = {e_st:.4f}; at the lower edge Y = {Y_LO:.3f}: {e_edge:.4f}"
      f"; check by root-finder: {brentq(lambda x: yph(4, 1, f20, 0, x, 0) - Y_MEAS, 0, 0.5):.5f}")
print(f"   variants: Lindhard f = {fL[20.0]:.4f}: {e_line(Y_MEAS, 1, fL[20.0]):.4f} (edge {e_line(Y_LO, 1, fL[20.0]):.4f}); "
      f"reconstruction with the true eps (g_cal = g_Luke): {e_line(Y_MEAS, 1, f20, eps_cal=EPS):.4f} (edge {e_line(Y_LO, 1, f20, eps_cal=EPS):.4f})")
r0 = r_only(Y_MEAS, f20)
print(f"collection alone (E_st = 0): r_coll = {r0:.4f}; root-finder {brentq(lambda x: yph(4, x, f20) - Y_MEAS, 0.5, 2):.5f}; "
      f"band {r_only(Y_HI, f20):.4f} .. {r_only(Y_LO, f20):.4f}")
print(f"   variants: Lindhard f: {r_only(Y_MEAS, fL[20.0]):.4f} (band {r_only(Y_HI, fL[20.0]):.4f}..{r_only(Y_LO, fL[20.0]):.4f}); "
      f"y_C with g_cal = g_Luke: {r_only(Y_MEAS, f20, eps_cal=EPS):.4f}; Lindhard with g_cal = g_Luke (earlier single-eps value): "
      f"{r_only(Y_MEAS, fL[20.0], eps_cal=EPS):.4f}")
print(f"   r_coll g_Luke/g_cal - 1 at r0 = {r0*EPS_CAL/EPS - 1:+.4f}")
num_ = (1 - Y_MEAS) + g4c * (1 - f20); den_ = g4t * (Y_MEAS - f20)
print(f"   formula pieces: (1 - Y) + g_cal(1 - f) = {1-Y_MEAS:.3f} + {g4c*(1-f20):.4f} = {num_:.4f}; g_Luke(Y - f) = {den_:.4f}")
print("energy dependence of the collection-alone reading at fixed r0:")
for lab, fv in (("10 keV, y_C", fC[10.0]), ("20 keV, y_C", f20), ("100 keV, y_C", fC[100.0]), ("100 keV, 0.75 y_C", f100c),
                ("10 keV, y_L", fL[10.0]), ("100 keV, y_L", fL[100.0]), ("100 keV, 0.75 y_L", 0.75 * fL[100.0])):
    print(f"   {lab:18s}: f = {fv:.4f}: Y_ph = {yph(4, r0, fv):.4f}")
print(f"   band {Y_LO:.3f} .. {Y_HI:.3f}; stored-alone reading at fixed e = {e_st:.4f}: Y_ph(10 keV) = {yph(4, 1, fC[10.0], 0, e_st):.4f}, "
      f"Y_ph(100 keV) = {yph(4, 1, fC[100.0], 0, e_st):.4f}")
for rr in (0.9, 0.95, 1.0, 1.05, 1.1, r0):
    print(f"   inferred E_st/omega (delta = x = 0) at r = {rr:.4f}: central {e_line(Y_MEAS, rr, f20):.4f} "
          f"(change from r = 1: {e_line(Y_MEAS, rr, f20) - e_st:+.4f}); lower edge {e_line(Y_LO, rr, f20):.4f}")
e_half = e_st / 2
rh = brentq(lambda x: e_line(Y_MEAS, x, f20) - e_half, 0.9, 1.3)
print(f"half of the stored-alone reading, E_st/omega = {e_half:.4f}, needs r = {rh:.4f}")
# gap-phonon offset: delta that alone reproduces the datum at r = 1, x = e = 0
d_alone = brentq(lambda d: yph(4, 1, f20, d) - Y_MEAS, 0, 0.3)
dgap = lambda rho, fv=f20: (1 - fv) * GG * (rho - 1) / (1 + GG * (rho - 1))
rho_a = brentq(lambda x: dgap(x) - d_alone, 1.0, 2.0)
print(f"collection offset alone (r = 1): delta_coll = {d_alone:.4f}; gap part reaches it for rho_g - 1 = {rho_a - 1:.4f} (f = {f20:.4f}); "
      f"a change of 0.02 in rho_g moves delta_gap by {dgap(rho_a + 0.02) - dgap(rho_a):+.4f}")
print(f"   variants: rho_g - 1 = 0.25 gives delta_gap = {dgap(1.25):.4f}; Lindhard f: rho_g - 1 = "
      f"{brentq(lambda x: dgap(x, fL[20.0]) - brentq(lambda d: yph(4, 1, fL[20.0], d) - Y_MEAS, 0, 0.3), 1, 2) - 1:.4f}")

# ------------------------------------------------------------------------------------------------ bound
section("4. The bound E_st/omega <= 1 - Y_ph under (a)-(e); first-order accuracy; C_cal")
rng = np.random.default_rng(1)
worst = 1.0
for _ in range(200000):
    V = rng.uniform(0, 100); epsc = rng.uniform(EPS, 4.5)             # (e): eps_eh <= eps_cal
    rr = rng.uniform(1, 2); fv = rng.uniform(0, 1); ev = rng.uniform(0, 1 - fv)
    dv = rng.uniform(0, 0.3); xE_ = rng.uniform(-0.05, 0.2)
    gcv = V / epsc
    xmin = (1 - ev + fv * gcv) * xE_ / ((1 + gcv) * (1 - dv))
    xN_ = xmin + rng.uniform(0, 0.2)
    if ev + xN_ >= 1 or xE_ >= 1:
        continue
    Yv = yph(V, rr, fv, dv, ev + xN_, xE_, eps_cal=epsc)
    worst = min(worst, (1 - Yv) - ev)
print(f"random scan, 2e5 points under (a)-(e): min of (1 - Y_ph) - E_st/omega = {worst:.3e} (>= 0)")
# violation of (e) loosens: example eps_eh = 3.9 eV > eps_cal
gt_x = 4 / 3.9
print(f"if (e) fails, e.g. eps_eh = 3.90 eV: r = 1 stored-alone reading at the lower edge = "
      f"{(1 - Y_LO) + (g4c - gt_x) * (Y_LO - f20) / (1 + g4c):.4f} (> {1 - Y_LO:.3f})")
print(f"Si 95 % bound: E_st/omega <= 1 - Y_lo = {1 - Y_LO:.4f} under (a)-(e); with the book's eps_eh = 3.75 eV at r = 1, "
      f"delta = x = 0: {e_edge:.4f}")
# zero-point sign: widening for Delta E_zp < 0
for lab, TdER, Ed, base in (("Si 10 keV", 1 - fC[10.0], 36.0, 1 - Y_LO), ("Si 100 keV", 1 - fC[100.0], 36.0, 1 - Y_LO),
                            ("Ge 103 keV", 0.7, 19.7, 0.0608 + 1.645 * 0.0018)):
    wz = 0.1 * 0.8 * TdER / (2 * Ed)
    print(f"   |Delta E_zp|/omega for 0.1 eV per displacement, {lab}: {wz:.2e}; bound for either sign of Delta E_zp: {base + wz:.4f}")
rrg = np.linspace(0.8, 1.3, 501)
dif = np.abs(yph(4, rrg, f20, 0, e_st, 0) - yph_first(4, rrg, f20, 0, e_st, 0))
print(f"first order vs exact at E_st/omega = {e_st:.3f}, r in [0.8, 1.3]: max |difference| = {dif.max():.2e} (linear in d_NR)")
worst2, worst3 = 0.0, 0.0
grid = np.linspace(0, 0.05, 11)
for dv in grid:
    for dn in grid:
        for de in grid:
            for V in (4.0, 40.0):
                worst2 = max(worst2, np.abs(yph(V, rrg, f20, dv, dn, de) - yph_first(V, rrg, f20, dv, dn, de)).max())
for dv in np.linspace(-0.05, 0.05, 11):
    for dn in np.linspace(-0.05, 0.05, 11):
        for de in np.linspace(-0.05, 0.05, 11):
            worst3 = max(worst3, np.abs(yph(4.0, rrg, f20, dv, dn, de) - yph_first(4.0, rrg, f20, dv, dn, de)).max())
print(f"first order vs exact, delta, d_NR, d_ER each in [0, 0.05], r in [0.8, 1.3], 4 and 40 V: max |difference| = {worst2:.2e}; "
      f"each in [-0.05, 0.05] at 4 V: {worst3:.2e}")
for E in (10.0, 20.0, 100.0):
    print(f"C_cal(r = 1) at 4 V, f = y_C({E:g} keV) = {fC[E]:.4f}: {ccal(4, 1, fC[E]):.4f}; at 40 V: {ccal(40, 1, fC[E]):.4f}")
print(f"C_cal at r = r0, 4 V: {ccal(4, r0, f20):.4f}")

# ------------------------------------------------------------------------------------------------ two biases
section("5. Two-bias inversion (4 and 40 V), reconstruction with eps_cal at both biases")
kap = EPS_CAL / EPS
res2 = {}
for lab, rr, ev in (("collection only", r0, 0.0), ("stored energy only", 1.0, e_st), ("half and half", rh, e_half)):
    y4, y40 = yph(4, rr, f20, 0, ev, 0), yph(40, rr, f20, 0, ev, 0)
    res2[lab] = (y4, y40)
    print(f"{lab:20s}: r = {rr:.4f}, E_st/omega = {ev:.4f}: Y_ph(4 V) = {y4:.5f}, Y_ph(40 V) = {y40:.5f}")
    M2 = np.array([[1 + g4c, -g4t * (y4 - f20)], [1 + g40c, -g40t * (y40 - f20)]])
    YHs, rts = np.linalg.solve(M2, [y4 + f20 * g4c, y40 + f20 * g40c])
    print(f"{'':20s}  inversion returns Y_ph(0) = {YHs:.6f}, r' = {rts:.6f}")
dread = res2["stored energy only"][1] - res2["collection only"][1]
print(f"difference of the two readings at 40 V: {dread:.4f} = {dread/((Y_UP+Y_DN)/2):.2f} x the half-width of the band")
print(f"single-eps comparison (reconstruction with eps_eh): stored-only Y(40 V) = {yph(40, 1, f20, 0, e_line(Y_MEAS,1,f20,eps_cal=EPS), 0, eps_cal=EPS):.4f}")
for lab in ("stored energy only", "collection only"):
    y4, y40 = res2[lab]
    for dY in (+0.005, -0.005):
        M2 = np.array([[1 + g4c, -g4t * (y4 - f20)], [1 + g40c, -g40t * (y40 + dY - f20)]])
        YHs, rts = np.linalg.solve(M2, [y4 + f20 * g4c, y40 + dY + f20 * g40c])
        print(f"{lab}: Y_ph(40 V) shifted by {dY:+.3f} -> r' = {rts:.4f}, Y_ph(0) = {YHs:.4f}")
print(f"large-bias limit f + (Y_ph(0) - f) eps_eh/(eps_cal r'): collection only (Y(0) = 1, r' = r0): "
      f"{f20 + (1 - f20) / (kap * r0):.4f}; stored only (Y(0) = {1-e_st:.4f}... see note) ")
print(f"   note: stored only at r = 1 has Y(0) = 1 - e = {1-e_st:.4f}, limit {f20 + (1 - e_st - f20) / kap:.4f}")
# ------------------------------------------------------------------------------------------------ heat quenching
section("6. Heat quenching at zero field and the release of the gap energy")
YQ = {0.10: 0.102, 0.89: 0.127, 3.91: 0.236}
yh = lambda b, yq, ev=0.0: (1 - yq * GG * (1 - b) - ev) / (1 - GG * (1 - b))
for E, yq in YQ.items():
    b1 = brentq(lambda b: yh(b, yq) - 1.01, 0.0, 1.0)
    print(f"E_R = {E:4.2f} keV, Y_q = {yq}: Y_ph(0) with no gap energy released = {yh(0, yq):.4f}; "
          f"within 1 % of one for b >= {b1:.4f} (held fraction 1 - b <= {1 - b1:.4f}); first-order excess "
          f"(1 - Y_q)(E_g/eps) = {(1 - yq) * GG:.4f}")
yq = 0.102
print(f"source pair energy 3.8 eV: Y_ph(0) at 100 eV, nothing released = "
      f"{(1 - yq * EG / 3.8) / (1 - EG / 3.8):.4f}")
# Fig 18.4 kinetics
G_FX = 1.0e9; bt = 0.05; G_FT = G_FX * bt / (1 - bt); G_X = 1.0e5; eta_X = 0.1; G_XB = 1.0e6; G_B = 1 / 250e-9
Mk = np.array([[-(G_FX + G_FT), 0, 0], [G_FX, -(G_X + G_XB), 0], [0, G_XB, -G_B]])
p0 = np.array([1.0, 0, 0])


def kin(tt):
    q = -np.linalg.solve(Mk, (np.eye(3) - expm(Mk * tt)) @ p0)
    held = (expm(Mk * tt) @ p0).sum()
    tr = G_FT * q[0]
    li = G_X * eta_X * q[1]
    return held, tr, li, 1 - held - tr - li


for tt in (1e-6, 1e-5, 1e-3):
    h, tr, li, ph = kin(tt)
    print(f"Fig. 18.4 rates, window {tt:.0e} s: held {h:.4f}, trapped {tr:.4f}, light {li:.4f}, phonons b = {ph:.4f}; "
          f"Y_ph(0) at 100 eV = {yh(ph, 0.102):.4f}, at 3.91 keV = {yh(ph, 0.236):.4f}")
h, tr, li, ph = kin(1.0)
print(f"asymptotic split: trapped {tr:.4f}, light {li:.4f}, phonons {ph:.4f}; Y_ph(0) at 100 eV = {yh(ph, 0.102):.4f}")
print("bimolecular release (t0 per channel, text convention): annihilation dn/dt = -n^2/(n0 t0): 1-b = 1/(1 + t/t0); Auger dn/dt = -n^3/(2 n0^2 t0): 1-b = (1 + t/t0)^(-1/2)")
for ratio in (1e-3, 1e-2):
    print(f"   t0/t_win = {ratio:g}: annihilation term Y_q(E_g/eps) t0/t_win at 100 eV = {0.102*GG*ratio:.2e}; "
          f"Auger Y_q(E_g/eps)(t0/t_win)^(1/2) = {0.102*GG*np.sqrt(ratio):.2e}")

# ------------------------------------------------------------------------------------------------ Fig 19.4 numbers
section("7. Fig. 19.4: shares of a 1 keV silicon recoil at zero field")
ER = 1000.0
YQ1 = 0.127
Neh = YQ1 * ER / EPS
Est = 0.055 * ER
Epair = Neh * EG
Eheat = ER - Epair - Est
TAU = 58e-6                       # fall time tau_f = 58 us of the pulse (2007.14289, p. 2)
print(f"Y_q = {YQ1} (measured at 0.89 keV): N_eh = {Neh:.2f}, pair energy N_eh E_g = {Epair:.1f} eV, E_st = {Est:.1f} eV, "
      f"heat at t_pr = {Eheat:.1f} eV ({100*Eheat/ER:.1f} %)")
print(f"phonon absorption time = pulse fall time tau_f = {TAU*1e6:.1f} us")
# phonon reservoir: dE/dt = source(t) - E/TAU; source = Eheat delta(t) + Epair * d b(t)/dt
tg = np.logspace(-12, -2, 801)
held, trp, lit, phb = np.array([kin(x) for x in tg]).T
# E_phon(t) = Eheat e^{-t/TAU} + Epair * int_0^t b'(s) e^{-(t-s)/TAU} ds  (numerical convolution on a fine linear grid)
tl = np.linspace(0, 1e-2, 400001)
dt = tl[1] - tl[0]
bl = np.interp(tl, np.concatenate([[0], tg]), np.concatenate([[0], phb]))
db = np.diff(bl, prepend=0.0)
decay = np.exp(-dt / TAU)
Eph = np.empty_like(tl)
acc = 0.0
for i in range(len(tl)):
    acc = acc * decay + Epair * db[i]
    Eph[i] = acc
Eph += Eheat * np.exp(-tl / TAU)
Ephg = np.interp(tg, tl, Eph)
Epairs = Epair * (held + trp)
Eesc = Epair * lit
Esens = ER - Ephg - Epairs - Eesc - Est
for x in (1e-10, 1e-6, 1e-4, 1e-3, 1e-2):
    i = np.argmin(abs(tg - x))
    print(f"t = {tg[i]:.1e} s: E_pairs {Epairs[i]:6.2f}  E_phon {Ephg[i]:7.2f}  E_st {Est:5.1f}  E_esc {Eesc[i]:5.2f}  "
          f"E_sens {Esens[i]:7.2f}  sum {Epairs[i]+Ephg[i]+Est+Eesc[i]+Esens[i]:.3f}")

# ------------------------------------------------------------------------------------------------ figures
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})

# Fig 19.4
fig, ax = plt.subplots(figsize=(6.0, 3.5))
lay = [Epairs, np.full_like(tg, Est), Eesc, Ephg, Esens]
labs = [r"pairs, excitons, traps $E_{\mathrm{pairs}}$", r"stored $E_{\mathrm{st}}$", r"escaped light $E_{\mathrm{esc}}$",
        r"phonons in the crystal $E_{\mathrm{phon}}$", r"absorbed at the surfaces $E_{\mathrm{sens}}$"]
cols = ["C0", "C3", "C4", "C1", "0.55"]
ax.stackplot(tg, *[l / ER for l in lay], labels=labs, colors=cols, alpha=0.85, lw=0)
ax.axvspan(1e-12, 1e-11, color="white", alpha=0.8, lw=0)
for xv in (1e-11, 1e-10):
    ax.axvline(xv, color="k", lw=0.6, ls=":")
ax.text(3.2e-12, 0.6, "collisions, cascade", fontsize=7, va="center", ha="center", rotation=90)
ax.text(3.2e-11, 0.6, r"$t_{\mathrm{pr}}$", fontsize=8, va="center", ha="center")
ax.set_xscale("log")
ax.set_xlim(1e-12, 1e-2)
ax.set_ylim(0, 1)
ax.set_xlabel(r"time after the recoil $t$ (s)")
ax.set_ylabel(r"share of $E_{\mathrm{dep}} = 1$ keV")
ax.legend(loc="lower center", fontsize=7, frameon=False, ncol=3, bbox_to_anchor=(0.5, 1.0))
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig19_4.pdf"))
plt.close(fig)

# Limit 19.5a
fig, ax = plt.subplots(figsize=(4.8, 3.1))
bb = np.linspace(0, 1, 401)
b1 = brentq(lambda b: yh(b, 0.102) - 1.01, 0, 1)
ax.axvspan(b1, 1, color="0.88", lw=0)
for (E, yq), c in zip(YQ.items(), ("C0", "C1", "C2")):
    ax.plot(bb, yh(bb, yq), color=c, lw=1.2, label=fr"$E_R = {E:g}$ keV, $Y_q = {yq}$")
ax.plot(bb, yh(bb, 0.102, 0.05), color="C0", lw=1.0, ls="--", label=r"0.1 keV with $E_{\mathrm{st}} = 0.05\,\omega$")
ax.axhline(1.0, color="k", lw=0.9, label=r"unit heat quenching $Y_{\mathrm{ph}}(0) = 1$")
ax.axvline(kin(1.0)[3], color="0.4", lw=0.7, ls=":")
ax.set_xlabel(r"fraction $f_{\mathrm{ret}}$ of the pair gap energy returned as phonons")
ax.set_ylabel(r"$Y_{\mathrm{ph}}(0)$")
ax.set_xlim(0, 1)
ax.set_ylim(0.9, 1.45)
ax.legend(fontsize=6.5, loc="upper right", bbox_to_anchor=(0.93, 1.0), frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit19_5a.pdf"))
plt.close(fig)

# Limit 19.5b (merged): (a) phonon-yield ratio, (b) stored-energy bound, against the collection ratio
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.6, 3.1))
rr = np.linspace(0.8, 1.3, 501)
ax.axvspan(1.0, 1.3, color="0.90", lw=0)
ax.axhspan(Y_LO, Y_HI, color="C2", alpha=0.25, lw=0)
ax.fill_between(rr, yph(4, rr, fC[10.0]), yph(4, rr, fC[100.0]), color="k", alpha=0.10, lw=0)
ax.plot(rr, yph(4, rr, f20), color="k", lw=1.2, label=r"4 V, $E_{\mathrm{st}} = 0$")
ax.plot(rr, yph(4, rr, f20, 0, e_st), color="C0", lw=1.2, label=r"4 V, $E_{\mathrm{st}} = %.3f\,\omega$" % e_st)
ax.plot(rr, yph(40, rr, f20), color="k", lw=1.0, ls="--", label=r"40 V, $E_{\mathrm{st}} = 0$")
ax.plot(rr, yph(40, rr, f20, 0, e_st), color="C0", lw=1.0, ls="--", label=r"40 V, $E_{\mathrm{st}} = %.3f\,\omega$" % e_st)
ax.plot([r0], [Y_MEAS], "o", color="k", ms=3.5)
ax.set_xlim(0.8, 1.3)
ax.set_ylim(0.84, 1.12)
ax.set_xlabel(r"collection ratio $\mathfrak{r}_{\mathrm{coll}}$")
ax.set_ylabel(r"$Y_{\mathrm{ph}}$")
ax.set_title("(a) phonon-yield ratio", fontsize=8)
ax.legend(fontsize=6.6, loc="upper right", frameon=False)

bx.axvspan(1.0, 1.3, color="0.90", lw=0)
bx.fill_between(rr, e_line(Y_LO, rr, fC[10.0]), e_line(Y_LO, rr, fC[100.0]), color="k", alpha=0.10, lw=0)
bx.plot(rr, e_line(Y_LO, rr, f20), color="k", lw=1.3, label=r"Si, $\varepsilon_{\mathrm{cal}} = 3.82$ eV")
bx.plot(rr, e_line(Y_LO, rr, f20, eps_cal=EPS), color="C1", lw=1.0, ls="-.", label=r"Si, $\varepsilon_{\mathrm{cal}} = \varepsilon_{\mathrm{eh}}$")
bx.plot(rr, e_line(Y_MEAS, rr, f20), color="C0", lw=1.0, ls=":", label=r"Si, central $Y_{\mathrm{ph}}$")
bx.axhline(1 - Y_LO, color="0.5", lw=0.6, ls="--")
fGe95 = 0.0608 + 1.645 * 0.0018
bx.plot([1.0], [fGe95], "o", color="C3", ms=4, label=r"Ge, $^{206}$Pb, at $\mathfrak{r}_{\mathrm{coll}} = 1$")
bx.axhline(0, color="0.4", lw=0.6)
bx.set_xlim(0.8, 1.3)
bx.set_ylim(-0.06, 0.14)
bx.set_xlabel(r"collection ratio $\mathfrak{r}_{\mathrm{coll}}$")
bx.set_ylabel(r"upper bound on $E_{\mathrm{st}}/\omega$ (95 % C.L.)")
bx.set_title("(b) stored-energy bound", fontsize=8)
bx.legend(fontsize=6.6, loc="upper right", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit19_5b.pdf"))
plt.close(fig)
print(f"\nLimit Check 19.5b: dot at r = {r0:.4f}; panel (b) at r = 0.9: Si bound {e_line(Y_LO, 0.9, f20):.4f} "
      f"(f band {e_line(Y_LO, 0.9, fC[100.0]):.4f}..{e_line(Y_LO, 0.9, fC[10.0]):.4f}); at r = 1: {e_line(Y_LO, 1, f20):.4f}; "
      f"with eps_cal = eps_eh at r = 1: {e_line(Y_LO, 1, f20, eps_cal=EPS):.4f}; Ge point {fGe95:.4f}")
print("figures written: fig19_4.pdf, limit19_5a.pdf, limit19_5b.pdf")
