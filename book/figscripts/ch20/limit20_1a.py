"""Limit Check 20.1a (lim:20.1a, fig:20-limit-hecht): the Hecht relation in its voltage form against drift with a
saturating velocity.  Log: limit20_1a.log.  Run: python limit20_1a.py > limit20_1a.log  (seconds).

Literature form (Hecht 1932, as quoted by Lachish, arXiv:1701.03459 Eqs. (1)-(4)): charge generated at one face, one
carrier crosses the gap d, exponential trapping with lifetime tau, drift velocity mu E with E = V/d:
    Q/Q0 = (lam/d)(1 - exp(-d/lam)),   lam = mu tau V/d.
Fuller result (derived in Sect. 20.1 for any velocity law): the same survival law with lam = v_dr(E) tau.
MODELLING CHOICE: the saturating interpolation v_dr = mu E/(1 + mu E/v_sat), with kappa = v_sat tau/d = 2 (one
illustrative value; no number of a specific crystal is plotted).  Controlling parameter x = mu tau V/d^2 = lam_ohm/d;
mu E/v_sat = x/kappa.  Leading correction: lam = lam_ohm (1 - x/kappa) to first order.
Validity region shaded: mu E/v_sat <= 0.1.
"""
import os
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from charge20_1 import hecht_face, FIG

KAPPA = 2.0
x = np.logspace(-2, 2, 500)
lit = hecht_face(x)
full = hecht_face(x / (1 + x / KAPPA))
lead = hecht_face(np.maximum(x * (1 - x / KAPPA), 1e-6))
xe = 0.1 * KAPPA
print("kappa = v_sat tau/d = %.1f; saturation limit of the collected fraction kappa(1 - exp(-1/kappa)) = %.4f"
      % (KAPPA, hecht_face(KAPPA)))
for xv in [0.05, 0.1, xe, 0.5, 1.0, 3.0, 10.0]:
    h = hecht_face(xv)
    f = hecht_face(xv / (1 + xv / KAPPA))
    print("x = mu tau V/d^2 = %6.2f (mu E/v_sat = %.3f): Hecht %.4f, saturating %.4f, ratio %.4f, first order %.4f"
          % (xv, xv / KAPPA, h, f, f / h, hecht_face(xv * (1 - xv / KAPPA))))
r10 = brentq(lambda t: hecht_face(t / (1 + t / KAPPA)) / hecht_face(t) - 0.9, 0.01, 100)
r1 = brentq(lambda t: hecht_face(t / (1 + t / KAPPA)) / hecht_face(t) - 0.99, 0.001, 100)
print("saturating curve 1 %% below Hecht at x = %.4f (mu E/v_sat = %.4f); 10 %% below at x = %.4f (mu E/v_sat = %.4f)"
      % (r1, r1 / KAPPA, r10, r10 / KAPPA))
print("at the edge of the shaded region (mu E/v_sat = 0.1): deficit %.2f %%"
      % (100 * (1 - hecht_face(xe / (1 + xe / KAPPA)) / hecht_face(xe))))
# small-x limit of the deficit: Q ~ lam/d so the deficit equals x/kappa to first order
print("small-x deficit/(x/kappa) at x = 1e-3: %.4f" % ((1 - hecht_face(1e-3 / (1 + 1e-3 / KAPPA)) / hecht_face(1e-3)) / (1e-3 / KAPPA)))

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.8, 3.0))
ax.axvspan(x.min(), xe, color="0.88", lw=0)
ax.axhline(1.0, color="k", lw=1.5, label=r"Hecht, $\lambda_{\mathrm{d}} = \mu_{\mathrm{mob}}\tau_{\mathrm{tr}}V_{\mathrm{bias}}/d_{\mathrm{det}}$")
ax.semilogx(x, full / lit, "b-", lw=1.5, label=r"saturating drift, $v_{\mathrm{sat}}\tau_{\mathrm{tr}} = 2d_{\mathrm{det}}$")
m = x < 1.0
ax.semilogx(x[m], lead[m] / lit[m], "r:", lw=1.3, label="leading correction")
ax.set_xlim(x.min(), x.max())
ax.set_ylim(0.6, 1.05)
ax.set_xlabel(r"$\mu_{\mathrm{mob}}\tau_{\mathrm{tr}}V_{\mathrm{bias}}/d_{\mathrm{det}}^2$")
ax.set_ylabel("collected fraction / Hecht")
ax.legend(loc="lower left", fontsize=7, frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit20_1a.pdf"))
print("wrote limit20_1a.pdf")
