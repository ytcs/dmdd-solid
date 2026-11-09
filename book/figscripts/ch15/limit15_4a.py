"""Limit Check 15.4a (lim:15.4a, fig:15-limit-holstein): phonon-assisted (Holstein) absorption of a superconductor against
the normal-metal formula of Allen, as a function of omega/Delta_BCS.

Plotted: y = sigma_1^S(omega)/sigma_1^N(omega) against x = omega/Delta_BCS from 2 to 400 (abs15.py formulas):
  solid black   the Nambu second-order result with the case-I factor g_I (Eq. 15.4-holstein), Debye a2F_tr
                (= Hochberg, Lin and Zurek, arXiv:1604.06800, Eq. (17), for omega < omega_D);
  dashed gray   the same phonon-assisted integral with the case-II factor g_II, the factor a Mattis-Bardeen treatment
                of the coherence would give (shown for comparison; not a result);
  dotted blue   Mattis-Bardeen, the impurity-assisted ratio sigma_1^MB/sigma_N = g_II(omega/Delta_BCS) (dirty limit);
  dash-dotted   case I with the softer low-frequency law a2F_tr proportional to omega'^2 below omega_D (a sensitivity
                test of the shape of a2F_tr, not a model of aluminum);
  thin line     1, the normal-metal formula (Allen; Hochberg et al. Eqs. (13), (16)), the literature limit omega >> Delta.
Shaded: omega where the case-I result stays within 10 % of the normal-metal formula.
Modelling choices: Debye transport function a2F_tr = 2 lambda_tr omega'^4/omega_D^4 (omega_D = 37 meV, lambda_tr = 0.39);
below omega_D the ratio depends only on the omega'^4 shape, not on lambda_tr or omega_D (checked with omega_D = 40 meV);
Delta_BCS = 0.18 meV for the top axis.  T = 0.
Run: python limit15_4a.py   (a few seconds)
"""
import os
import numpy as np
from scipy.optimize import brentq, minimize_scalar
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import abs15 as A

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch15", "limit15_4a.pdf")

A.checks()
D = A.DELTA


def a2f_sq(W):
    W = np.asarray(W, float)
    return np.where((W > 0) & (W < A.WD), W**2, 0.0)


def ratio(x, coh="I", wd=A.WD, f=None):
    w = x * D
    if f is None:
        f = lambda W: A.a2f_debye(W, wd=wd)  # noqa: E731
    return A.sigma_holstein(w, a2f=f, coh=coh) / A.sigma_holstein(w, a2f=f, coh="N")


x10 = brentq(lambda x: ratio(x) - 0.9, 3, 30)
opt = minimize_scalar(lambda lx: -ratio(np.exp(lx)), bounds=(np.log(15), np.log(150)), method="bounded")
xmax, rmax = np.exp(opt.x), -opt.fun
# beyond the maximum the ratio decreases to 1; check that it never leaves the 10 % band above x10
xs_chk = np.geomspace(x10, 400, 300)
rs_chk = np.array([ratio(x) for x in xs_chk])
assert np.all(np.abs(rs_chk - 1) <= 0.1 + 1e-12)
x1 = brentq(lambda x: ratio(x) - 1.0, 10, 30)
print("case I crosses the normal-metal value at omega = %.1f Delta = %.2f meV" % (x1, x1 * D * 1e3))
x10_II = brentq(lambda x: ratio(x, "II") - 0.9, 3, 200)
xMB = brentq(lambda x: float(A.gII(x)) - 0.9, 3, 200)
print("case I within 10 %% of the normal-metal formula for omega >= %.2f Delta = %.3f meV" % (x10, x10 * D * 1e3))
print("case I maximum %.4f at omega = %.1f Delta = %.2f meV" % (rmax, xmax, xmax * D * 1e3))
print("case-II factor within 10 %% for omega >= %.1f Delta; Mattis-Bardeen g_II within 10 %% for omega >= %.1f Delta" % (x10_II, xMB))
for x in (2.2, 3, 4, 1e-3 / D, 10, 20, 50, 100):
    print("  omega = %6.2f Delta (%.3f meV): case I %.4f   case II %.4f   g_II %.4f   g_I %.4f"
          % (x, x * D * 1e3, ratio(x), ratio(x, "II"), A.gII(x), A.gI(x)))
for x in (5, 10, 50):
    print("  omega_D = 40 meV instead of 37: case I at %g Delta %.6f vs %.6f" % (x, ratio(x, wd=40e-3), ratio(x)))
x10_sq = brentq(lambda x: ratio(x, f=a2f_sq) - 0.9, 3, 40)
print("omega'^2 law: within 10 %% for omega >= %.2f Delta = %.3f meV" % (x10_sq, x10_sq * D * 1e3))
for x in (3, 4, 1e-3 / D, 10, 20):
    print("  omega = %6.2f Delta: case I omega'^4 %.4f   omega'^2 %.4f" % (x, ratio(x), ratio(x, f=a2f_sq)))
print("omega_D/Delta = %.1f" % (A.WD / D))

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.0))
xs = np.geomspace(2.0005, 400, 500)
ax.axvspan(x10, 400, color="0.9", lw=0)
ax.axhline(1, color="k", lw=0.7)
ax.plot(xs, [ratio(x) for x in xs], color="k", lw=1.4, label=r"phonon-assisted, case I (Allen; Hochberg et al.)")
ax.plot(xs, [ratio(x, f=a2f_sq) for x in xs], color="k", lw=0.9, ls="-.", label=r"case I, $\alpha^2F_{\mathrm{tr}} \propto \omega'^2$")
ax.plot(xs, [ratio(x, "II") for x in xs], color="0.5", lw=1.1, ls="--", label=r"phonon-assisted with a case-II factor")
ax.plot(xs, A.gII(xs), color="tab:blue", lw=1.1, ls=":", label=r"impurity-assisted (Mattis–Bardeen)")
ax.axvline(A.WD / D, color="0.5", lw=0.6, ls="-.")
ax.text(A.WD / D * 1.05, 0.08, r"$\omega_{\mathrm{D}}$", fontsize=8, color="0.3")
ax.set_xscale("log")
ax.set_xlim(2, 400)
ax.set_ylim(0, 1.2)
ax.set_xlabel(r"$\omega/\Delta_{\mathrm{BCS}}$")
ax.set_ylabel(r"$\sigma_1^{\mathrm{S}}/\sigma_1^{\mathrm{N}}$")
ax.legend(frameon=False, fontsize=7, loc="lower right", bbox_to_anchor=(1.0, 0.05))
top = ax.secondary_xaxis("top", functions=(lambda x: x * D * 1e3, lambda m: m / (D * 1e3)))
top.set_xlabel(r"$\omega$ (meV), aluminum")
fig.tight_layout()
fig.savefig(OUT)
print("wrote", OUT)
