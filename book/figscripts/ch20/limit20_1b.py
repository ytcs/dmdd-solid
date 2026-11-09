"""Limit Check 20.1b (lim:20.1b, fig:20-limit-work): bias work with trapping against the full-collection form.
Log: limit20_1b.log.  Run: python limit20_1b.py > limit20_1b.log  (seconds).

Literature form (Agnese et al., arXiv:1803.02903 Eq. (1)): E_NTL = n_Q e V_b, the Luke phonon energy of n_Q fully
collected pairs.  Fuller result (eq:20.1-work with eq:20.1-Hecht2, Sect. 20.1): W_bias = e V_bias N_ind,
N_ind = N_eh <qbar>, with <qbar> the depth average (uniform events) of the two-carrier Hecht form,
    <qbar> = sum_c (lam_c/d)[1 - (lam_c/d)(1 - exp(-d/lam_c))]  (closed form, charge20_1.qbar_uniform).
Leading correction: 1 - d/(6 lam_e) - d/(6 lam_h).  Controlling parameter d/lam_e; two cases lam_h = lam_e, lam_e/3
(illustrative ratio).  Shaded: W_bias within 1 % of the literature form for lam_h = lam_e.
"""
import os
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from charge20_1 import qbar_uniform, FIG

y = np.logspace(-3, 1, 500)          # d / lam_e
eq = qbar_uniform(1 / y, 1 / y)
un = qbar_uniform(1 / y, 1 / (3 * y))
lead_eq = 1 - y / 3
lead_un = 1 - y / 6 - 3 * y / 6
e1 = brentq(lambda t: qbar_uniform(1 / t, 1 / t) - 0.99, 1e-4, 1)
e1u = brentq(lambda t: qbar_uniform(1 / t, 1 / (3 * t)) - 0.99, 1e-4, 1)
print("W_bias/(N_eh e V_bias) = 0.99 at d/lam = %.4f (equal), d/lam_e = %.4f (lam_h = lam_e/3)" % (e1, e1u))
for t in [0.01, 0.03, 0.1, 0.3, 1.0, 3.0]:
    print("d/lam_e = %5.2f: equal %.4f (leading %.4f); lam_h = lam_e/3 %.4f (leading %.4f)"
          % (t, qbar_uniform(1 / t, 1 / t), 1 - t / 3, qbar_uniform(1 / t, 1 / (3 * t)), 1 - 2 * t / 3))
# second-order coefficient check: <qbar> = 1 - y/3 + y^2/12 + ... for equal lam
t = 1e-2
print("second-order coefficient (equal): %.4f (expected 2 x 1/24 = 0.0833)" % ((qbar_uniform(1 / t, 1 / t) - 1 + t / 3) / t**2))

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.8, 3.0))
ax.axvspan(y.min(), e1, color="0.88", lw=0)
ax.axhline(1.0, color="k", lw=1.5, label=r"full collection, $N_{\mathrm{eh}}eV_{\mathrm{bias}}$")
ax.semilogx(y, eq, "b-", lw=1.5, label=r"trapping, $\lambda_{\mathrm{d}}^h = \lambda_{\mathrm{d}}^e$")
ax.semilogx(y, un, "g-", lw=1.5, label=r"trapping, $\lambda_{\mathrm{d}}^h = \lambda_{\mathrm{d}}^e/3$")
m = y < 1.5
ax.semilogx(y[m], lead_eq[m], "b:", lw=1.1, label="leading corrections")
m = y < 0.75
ax.semilogx(y[m], lead_un[m], "g:", lw=1.1)
ax.set_xlim(y.min(), y.max())
ax.set_ylim(0, 1.05)
ax.set_xlabel(r"$d_{\mathrm{det}}/\lambda_{\mathrm{d}}^e$")
ax.set_ylabel(r"$W_{\mathrm{bias}}/(N_{\mathrm{eh}}\,eV_{\mathrm{bias}})$")
ax.legend(loc="lower left", fontsize=7, frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit20_1b.pdf"))
print("wrote limit20_1b.pdf")
