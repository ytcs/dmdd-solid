"""Fig. 7.3 (Dirac cones and their particle-hole continuum), the limit-box plot of Sect. 7.3, and every number quoted
in Sect. 7.3 and its worked example on ZrTe5.  Natural units hbar = c = k_B = 1, Heaviside-Lorentz charge e^2 = 4 pi alpha.

Outputs (tex/figures/ch07/):
  fig7_3.pdf        (a) gapless and gapped Dirac bands; (b) the (q, omega) plane: interband continuum of a gapless and of
                    a gapped cone, and the region open to dark matter of mass 10, 20 and 50 keV.
  limit7_gapless.pdf static dielectric function of a gapped cone against the gapless formula and its leading correction.

Inputs and their sources
  Constants (CODATA 2018): alpha = 1/137.035999, hbar c = 1973.269804 eV A, k_B = 8.617333e-5 eV/K, m_e = 510998.95 eV.
  v_max = 794.5 km/s = 2.650e-3 (Sect. 1.3; v_max^2 = 7.023e-6 as in Sect. 3.3).
  ZrTe5 (Geilhufe, Kahlhoefer and Winkler, arXiv:1910.02091, Phys. Rev. D 101, 055005):
     Table 1, row for the measured crystal structure (central, as Sect. 16.1 and zrte5_16.py):
       v_x, v_y, v_z = 1.1e-3, 4.5e-4, 1.0e-3;  Delta = 11.8 meV (half of the 23.6 meV gap, text below Table 1);
       Lambda_x, Lambda_y, Lambda_z = 0.23, 0.215, 0.1 A^-1.
     Table 1, row ISIF7 (relaxed cell; the row the authors implement in their rates), printed for comparison:
       v_x, v_y, v_z = 1.1e-3, 4.4e-4, 9.1e-4;  Delta = 15.6 meV (half of the 31.2 meV gap); Lambda_y = 0.216 A^-1.
     Table 2: ion-clamped DFPT dielectric tensor, diagonal kappa_xx, kappa_yy, kappa_zz = 308.4, 20.75, 126.1; g = 2.
     Eq. (2.21): energy cutoff  Lambda~ = min_i(v_i Lambda_i).
  ZrTe5 (Hochberg et al., arXiv:1708.08929, Phys. Rev. D 97, 015004), Table 1 (th.):
       v = 2.9e-3, 5.0e-4, 2.1e-3; 2 Delta = 35 meV; Lambda = 0.14 keV; g = 4; kappa = 187.5, 9.8, 90.9;
     text before Eq. (2.8) and App. D: harmonic-mean kappa~ = 25.3, alpha~(theirs) = g alpha/(kappa~ vbar) = 0.80,
     vbar the geometric mean.
  Silicon-type Kane numbers (Sect. 3.3): |v_cX| = 4.7e-3 (E_P = 22.9 eV), GaAs E_g = 1.52 eV.
Formulas (App. D.22): eq:D.22-eps (static, omega = 0), eq:D.22-static, eq:D.22-gapless; anisotropic cone by rescaling
  k_i -> k_i / v_i (end of D.22): along principal axis i the Dirac term carries v_i/(v_j v_k) in place of 1/v_D.
Modelling choices (named in the captions and the text)
  "ZrTe5-like" isotropic cone: v_D = geometric mean of the three velocities, eps_bg = harmonic mean of kappa_ii,
  energy cutoff v_D Lambda_D = min_i v_i Lambda_i = 0.191 eV (the convention of Eq. (2.21) of 1910.02091), hard cutoff on
  |k| (on |k~| for the anisotropic cone), g_deg = 2.  Fig. 7.3(b) uses Delta_D = 11.8 meV, v_D = 7.9e-4.
"""
import os
import numpy as np
from scipy import integrate, optimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(BOOK, "tex", "figures", "ch07")
os.makedirs(OUT, exist_ok=True)

alpha = 1 / 137.035999
hbarc_A = 1973.269804       # eV A
hbarc_cm = 197.3269804e-7   # eV cm
kB = 8.617333e-5            # eV/K
me = 510998.95
vmax = 2.650e-3


def close(a, b, rtol=5e-3, name=""):
    assert abs(a - b) <= rtol * abs(b), f"{name}: {a} vs {b}"
    print(f"  {name:64s} {a:.6g}   (quoted {b})")


# ---------------------------------------------------------------- Kane two-level model as a Dirac cone (Sect. 3.3)
print("Kane two-level model as a massive Dirac cone")
EP = 22.9                    # eV, Gawarecki et al. Table VIII as quoted in Sect. 3.3
vcX = np.sqrt(EP / (2 * me))
close(vcX, 4.7e-3, 0.01, "|v_cX| = (E_P/2m_e)^1/2")
close(vcX / vmax, 1.8, 0.02, "|v_cX|/v_max")
Eg_GaAs = 1.52
mstar = (Eg_GaAs / 2) / vcX**2 / me
close(mstar, Eg_GaAs / EP, 1e-9, "Delta/v^2 = m_e E_g/E_P")
close(mstar, 0.066, 0.01, "m* = Delta/v^2 for GaAs [m_e]")
close(abs(mstar - 0.067) / 0.067, 0.01, 1.0, "deviation from measured 0.067 (< 2 percent)")

# ---------------------------------------------------------------- ZrTe5 parameters
print("ZrTe5 (1910.02091 Tables 1, 2, measured-structure row)")
v = np.array([1.1e-3, 4.5e-4, 1.0e-3])
Lam_A = np.array([0.23, 0.215, 0.1])            # A^-1
Lam = Lam_A * hbarc_A                            # eV
kap = np.array([308.4, 20.75, 126.1])
Delta = 11.8e-3
g = 2
close(1 / 1 * hbarc_A, 1973.3, 1e-4, "1 A^-1 in eV")
vL = v * Lam
for i, n in enumerate("xyz"):
    print(f"   v_{n} Lambda_{n} = {vL[i]*1e3:.1f} meV")
close(vL[0], 0.499, 3e-3, "v_x Lambda_x [eV]")
close(vL[1], 0.191, 3e-3, "v_y Lambda_y [eV]")
close(vL[2], 0.197, 3e-3, "v_z Lambda_z [eV]")
Ltil = vL.min()
vbar = np.prod(v) ** (1 / 3)
kbar = 3 / np.sum(1 / kap)
close(vbar, 7.9e-4, 5e-3, "geometric-mean velocity")
close(kbar, 50.5, 3e-3, "harmonic-mean kappa")
at = alpha / (kbar * vbar)
close(at, 0.18, 0.02, "alpha~ = alpha/(eps_bg v_D)")
close(g * at, 0.37, 0.02, "g alpha~")
LamD = Ltil / vbar
close(LamD, 241, 5e-3, "Lambda_D = 0.191 eV / v_D [eV]")
close(LamD / hbarc_A, 0.12, 0.03, "Lambda_D in A^-1")
mstarZ = Delta / vbar**2
close(mstarZ / me, 0.037, 0.02, "band-edge mass Delta/v_D^2 [m_e]")
close(2 * Delta / vbar, 30, 0.01, "2 Delta/v_D [eV]")

# Hochberg et al. (1708.08929) Table 1
vH = np.array([2.9e-3, 5.0e-4, 2.1e-3])
kH = np.array([187.5, 9.8, 90.9])
kbarH = 3 / np.sum(1 / kH)
close(kbarH, 25.3, 3e-3, "Hochberg harmonic-mean kappa")
vbarH = np.prod(vH) ** (1 / 3)
atH = alpha / (kbarH * vbarH)
close(4 * atH, 0.80, 0.01, "Hochberg alpha~ incl. g = 4")
close(atH, 0.20, 0.02, "Hochberg alpha~ in book notation (no g)")

# ---------------------------------------------------------------- polarization functions (App. D.22)
def J(Q2):
    """6 int_0^1 x(1-x) ln(1 + x(1-x) Q2) dx, Q2 = -s/Delta^2 >= 0 (static or spacelike)."""
    f = lambda x: x * (1 - x) * np.log1p(x * (1 - x) * Q2)
    return 6 * integrate.quad(f, 0, 1, limit=200)[0]


def bracket_static(q, vD, LD, D):
    """bracket of eq:D.22-eps at omega = 0: ln(4 v^2 L^2/D^2) - 5/3 - J(v^2 q^2/D^2)."""
    return np.log(4 * vD**2 * LD**2 / D**2) - 5 / 3 - J((vD * q / D) ** 2)


print("Static dielectric function, ZrTe5-like isotropic cone")
B0 = bracket_static(0.0, vbar, LamD, Delta)
close(B0, 2 * (np.log(2 * Ltil / Delta) - 5 / 6), 1e-9, "bracket at q = 0 equals 2[ln(2 v L/D) - 5/6]")
close(np.log(2 * Ltil / Delta), 3.48, 3e-3, "ln(2 v_D Lambda_D/Delta_D)")
close(2 * Ltil / Delta, 32.4, 3e-3, "2 v_D Lambda_D/Delta_D")
corr0 = g * at / (6 * np.pi) * B0
close(corr0, 0.102, 0.02, "eps(0,0)/eps_bg - 1")
close(kbar * (1 + corr0), 55.7, 3e-3, "eps(0,0)")
# finite q
for qq, quoted in [(2 * Delta / vbar, None), (0.5 * LamD, None)]:
    c = g * at / (6 * np.pi) * bracket_static(qq, vbar, LamD, Delta)
    print(f"   eps(q,0)/eps_bg - 1 at q = {qq:.1f} eV: {c:.4f}")
c41 = g * at / (6 * np.pi) * bracket_static(2 * Delta / vbar, vbar, LamD, Delta)
close(c41, 0.091, 0.01, "eps(q,0)/eps_bg - 1 at q = 2 Delta/v_D")
cL2 = g * at / (6 * np.pi) * bracket_static(0.5 * LamD, vbar, LamD, Delta)
close(cL2, 0.052, 0.01, "eps(q,0)/eps_bg - 1 at q = Lambda_D/2")
close(0.5 * LamD, 121, 0.01, "Lambda_D/2 [eV]")
# validity of perturbation theory: g alpha~ ln(Lambda/q) at q = 2Delta/v
close(g * at * np.log(LamD / (2 * Delta / vbar)), 0.76, 0.03, "g alpha~ ln(Lambda_D v_D/2Delta_D)")
close(g * at * np.log(Ltil / Delta), 1.0, 0.03, "expansion parameter g alpha~ ln(v_D Lambda_D/Delta_D)")
close(7.5 * Delta / vbar, 112, 0.01, "q at v_D q = 7.5 Delta_D [eV]")
# hard cutoff versus the MS-bar/Lambda convention of 1708.08929: Lambda -> e^{-5/6} Lambda
close(np.exp(-5 / 6), 0.435, 2e-3, "e^{-5/6}")

print("Anisotropic cone, principal axes (rescaling k_i -> k_i/v_i)")
B0a = 2 * (np.log(2 * Ltil / Delta) - 5 / 6)
add = np.empty(3)
for i, n in enumerate("xyz"):
    j, k = [m for m in range(3) if m != i]
    add[i] = g * alpha / (6 * np.pi) * v[i] / (v[j] * v[k]) * B0a
    print(f"   eps_{n}{n}(0,0) = {kap[i]:.2f} + {add[i]:.2f}  (+{100*add[i]/kap[i]:.1f} %)")
close(np.log(2 * Ltil / Delta) - 5 / 6, 2.64, 3e-3, "ln(2 Lambda~/Delta) - 5/6")
close(add[0], 10.0, 0.01, "Dirac term along x")
close(add[1], 1.67, 0.01, "Dirac term along y")
close(add[2], 8.3, 0.01, "Dirac term along z")
close(100 * add[0] / kap[0], 3.2, 0.02, "percent along x")
close(100 * add[1] / kap[1], 8.1, 0.02, "percent along y")
close(100 * add[2] / kap[2], 6.6, 0.02, "percent along z")
# per-axis effective couplings alpha_i = alpha v_i/(kappa_ii v_j v_k)
ai = np.array([alpha * v[i] / (kap[i] * np.prod(np.delete(v, i))) for i in range(3)])
print("   alpha~_i =", np.round(ai, 3))
close(ai[0], 0.058, 0.02, "alpha~_x");  close(ai[1], 0.144, 0.02, "alpha~_y");  close(ai[2], 0.117, 0.02, "alpha~_z")

# ---------------------------------------------------------------- density of states and thermal carriers
print("Density of states and thermal carriers")
# check DOS formula numerically: g E sqrt(E^2 - D^2)/(2 pi^2 v^3)
vD_, D_ = vbar, Delta
E = 3 * D_
dE = 1e-7
N = lambda E: g * (np.sqrt(E**2 - D_**2) / vD_) ** 3 / (6 * np.pi**2)
close((N(E + dE) - N(E - dE)) / (2 * dE), g * E * np.sqrt(E**2 - D_**2) / (2 * np.pi**2 * vD_**3), 1e-5, "DOS formula")
for T_K, quoted in [(4.0, 0.4)]:
    T = kB * T_K
    ms = D_ / vD_**2
    # exact Boltzmann integral against the parabolic-edge formula
    ex = integrate.quad(lambda E: g * E * np.sqrt(E**2 - D_**2) / (2 * np.pi**2 * vD_**3) * np.exp(-(E - D_) / T),
                        D_, D_ + 60 * T)[0] * np.exp(-D_ / T)
    par = g * (ms * T / (2 * np.pi)) ** 1.5 * np.exp(-D_ / T)
    print(f"   T = {T_K} K: Delta/T = {D_/T:.1f}; n_c = {ex/hbarc_cm**3:.3g} cm^-3 (exact), {par/hbarc_cm**3:.3g} (parabolic)")
    close(D_ / T, 34, 0.01, "Delta/T at 4 K")
    close(ex / hbarc_cm**3, quoted, 0.03, "n_c at 4 K [cm^-3]")
    close(1 - par / ex, 0.05, 0.1, "parabolic below exact by (fraction)")
close(D_ / (kB * 300), 0.46, 0.01, "Delta/T at 300 K")

# ---------------------------------------------------------------- kinematics: threshold mass
print("Threshold mass for the ZrTe5-like cone")
def reach_ok(m, vD, D):
    f = lambda q: -(q * vmax - q**2 / (2 * m) - np.sqrt(vD**2 * q**2 + 4 * D**2))
    r = optimize.minimize_scalar(f, bounds=(1e-3, 2 * m * vmax), method="bounded", options={"xatol": 1e-9})
    return -r.fun
def mmin(vD, D):
    return optimize.brentq(lambda m: reach_ok(m, vD, D), 1e2, 1e7, xtol=1e-6)
m_naive = 2 * (2 * Delta) / vmax**2
close(m_naive, 6.7e3, 0.01, "2(2 Delta)/v_max^2 [eV]")
m_iso = mmin(vbar, Delta)
close(m_iso, 8.0e3, 0.01, "m_min ZrTe5-like isotropic [eV]")
m_y = mmin(v[1], Delta)
close(m_y, 7.1e3, 0.01, "m_min along y (v = 4.5e-4) [eV]")
m_x = mmin(v[0], Delta)
close(m_x, 9.6e3, 0.01, "m_min along x (v = 1.1e-3) [eV]")
print(f"   m_min along z: {mmin(v[2], Delta):.4g} eV")
close(mmin(vbar, Delta) / 1e3, 8.0, 0.01, "threshold mass [keV]")
# the 7 keV curve of Fig. 7.3(b) stays below the continuum
assert reach_ok(7e3, vbar, Delta) < 0
# relaxed-cell row (ISIF7) of 1910.02091 Table 1, for comparison
vI = np.array([1.1e-3, 4.4e-4, 9.1e-4]); DI = 15.6e-3
print(f"   ISIF7 row: v_D = {np.prod(vI)**(1/3):.3g}, Lambda~ = {min(vI * np.array([0.23, 0.216, 0.1]) * hbarc_A):.3f} eV, "
      f"m_min isotropic {mmin(np.prod(vI)**(1/3), DI):.4g} eV, slow axis {mmin(vI[1], DI):.4g} eV, fast axis {mmin(vI[0], DI):.4g} eV")
# gapless cone: scattering possible only if v_D < v_max
print(f"   v_D/v_max ZrTe5-like = {vbar/vmax:.3f}")
close(vbar / vmax, 0.30, 0.02, "v_D/v_max")
# silicon comparison quoted from Sect. 1.3/3.3
print("   silicon m_min 0.333 MeV (Sect. 1.3): ratio", 0.333e6 / m_iso)

# ---------------------------------------------------------------- limit-box: gapless formula and its correction
print("Limit box: gapless formula")
# cutoff-independent form: y = (6 pi/g alpha~)(eps/eps_bg - 1) - ln(4 v^2 Lambda^2/Delta^2)
r = Ltil / Delta   # v_D Lambda_D / Delta_D for the ZrTe5-like cone
close(r, 16.2, 3e-3, "v_D Lambda_D/Delta_D")
Q = np.logspace(-1, 2, 500)
full = np.array([-5 / 3 - J(x**2) for x in Q])
gl = -2 * np.log(Q)
gl1 = gl - 6 / Q**2
# gapless formula within 0.1 of the full bracket (an error of 0.1 g alpha~/6 pi in eps/eps_bg)
Qstar = Q[np.argmax(np.abs(gl - full) < 0.1)]
close(Qstar, 7.5, 0.01, "gapless within 0.1 for v q/Delta >")
Qstar1 = Q[np.argmax(np.abs(gl1 - full) < 0.1)]
close(Qstar1, 3.7, 0.02, "with leading correction within 0.1 for v q/Delta >")
for x in [3.0, 10.0, 30.0]:
    f = -5 / 3 - J(x**2)
    print(f"   Q = {x}: full - gapless = {f+2*np.log(x):.5f}, -6/Q^2 = {-6/x**2:.5f}, residual {f+2*np.log(x)+6/x**2:.2e}")
close(-5 / 3 - J(100.0) + 2 * np.log(10.0), -0.057, 0.02, "full - gapless at Q = 10")
close(np.log(4 * r**2), 6.95, 3e-3, "ln(4 v^2 L^2/D^2)")
# ZrTe5-like at the end of the Dirac region, Q = r: relative error of the gapless induced term
fr = np.log(4 * r**2) - 5 / 3 - J(r**2); gr = np.log(4.0)
close(abs(gr - fr) / fr, 0.016, 0.1, "relative error of gapless form at q = Lambda_D (ZrTe5-like)")

# ---------------------------------------------------------------- figures
plt.rcParams.update({"font.size": 9, "axes.labelsize": 9, "legend.fontsize": 7.5, "pdf.fonttype": 42})
blue, orange, gray = "#2f6db5", "#d9822b", "0.55"

fig, ax = plt.subplots(1, 2, figsize=(6.3, 2.7), gridspec_kw={"width_ratios": [1, 1.25]})
# (a) bands in units of Delta: E/Delta vs v k/Delta
k = np.linspace(-4, 4, 400)
a = ax[0]
a.plot(k, np.abs(k), color=gray, lw=1.2, ls="--", label=r"$\Delta_{\mathrm{D}} = 0$")
a.plot(k, -np.abs(k), color=gray, lw=1.2, ls="--")
a.plot(k, np.sqrt(k**2 + 1), color=blue, lw=1.4, label=r"$\Delta_{\mathrm{D}} > 0$")
a.plot(k, -np.sqrt(k**2 + 1), color=blue, lw=1.4)
# a vertical-ish interband pair k -> k+q
k1, qv = -0.8, 1.6
a.annotate("", xy=(k1 + qv, np.sqrt((k1 + qv)**2 + 1)), xytext=(k1, -np.sqrt(k1**2 + 1)),
           arrowprops=dict(arrowstyle="->", color=orange, lw=1.1))
a.text(-2.3, 0.6, r"$(\omega, \boldsymbol{q})$", color=orange, fontsize=8)
a.annotate("", xy=(3.2, 1.0), xytext=(3.2, -1.0), arrowprops=dict(arrowstyle="<->", color="k", lw=0.7))
a.text(3.3, -0.15, r"$2\Delta_{\mathrm{D}}$", fontsize=8)
a.set_xlabel(r"$v_{\mathrm{D}}k/\Delta_{\mathrm{D}}$")
a.set_ylabel(r"$E/\Delta_{\mathrm{D}}$")
a.set_xlim(-4, 4.6); a.set_ylim(-4, 4)
a.legend(loc="lower center", frameon=False)   # upper left lay on the band lines
a.set_title("(a)", loc="left", fontsize=9)
# (b) (q, omega) plane for the ZrTe5-like cone
b = ax[1]
q = np.linspace(0, 120, 600)            # eV
edge0 = vbar * q * 1e3                   # meV
edgeD = np.sqrt((vbar * q)**2 + 4 * Delta**2) * 1e3
b.fill_between(q, edgeD, 200, color=blue, alpha=0.18, lw=0)
b.plot(q, edgeD, color=blue, lw=1.4, label=r"gapped: $(v_{\mathrm{D}}^2q^2 + 4\Delta_{\mathrm{D}}^2)^{1/2}$")
b.plot(q, edge0, color=gray, lw=1.2, ls="--", label=r"gapless: $v_{\mathrm{D}}q$")
for m, ls, (xt, yt) in [(7e3, ":", (39, 3)),   # 7 keV label right of where its curve ends
                         (2e4, "-.", (46, 74)), (5e4, "-", (24, 96))]:
    w = (q * vmax - q**2 / (2 * m)) * 1e3
    b.plot(q, np.where(w > 0, w, np.nan), color=orange, lw=1.0, ls=ls)
    b.text(xt, yt, f"{m/1e3:.0f} keV", color=orange, fontsize=7.5)
b.set_xlim(0, 120); b.set_ylim(0, 160)
b.set_xlabel(r"$q$ [eV]")
b.set_ylabel(r"$\omega$ [meV]")
b.legend(loc="upper left", frameon=False, fontsize=7)
b.set_title("(b)", loc="left", fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig7_3.pdf"))
print("wrote fig7_3.pdf")

fig, a = plt.subplots(figsize=(4.6, 2.9))
a.axvspan(Qstar, Q[-1], color="0.88", lw=0)
a.semilogx(Q, full, color=blue, lw=1.5, label=r"gapped cone")
a.semilogx(Q, gl, color="k", lw=1.0, ls="--", label=r"gapless formula")
m1 = Q > 1.2
a.semilogx(Q[m1], gl1[m1], color=orange, lw=1.1, ls=":", label=r"gapless $- 6\Delta_{\mathrm{D}}^2/v_{\mathrm{D}}^2q^2$")
a.axvline(r, color=gray, lw=0.7, ls="-.")
a.text(r * 1.08, 1.2, "ZrTe$_5$-like\n$q = \\Lambda_{\\mathrm{D}}$", fontsize=7, color="0.35")
a.set_xlim(Q[0], Q[-1])
a.set_ylim(-9.5, 4.5)
a.set_xlabel(r"$v_{\mathrm{D}}q/\Delta_{\mathrm{D}}$")
a.set_ylabel(r"$\frac{6\pi}{g_{\mathrm{deg}}\tilde\alpha}\left(\frac{\varepsilon}{\varepsilon_{\mathrm{bg}}} - 1\right) - \ln\frac{4v_{\mathrm{D}}^2\Lambda_{\mathrm{D}}^2}{\Delta_{\mathrm{D}}^2}$", fontsize=8.5)
a.legend(frameon=False, loc="lower left")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit7_gapless.pdf"))
print("wrote limit7_gapless.pdf")
