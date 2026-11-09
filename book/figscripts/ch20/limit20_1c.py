"""Limit Check 20.1c (lim:20.1c, fig:20-limit-fano): Fano factor of the measured charge.  Log: limit20_1c.log.
Run: python limit20_1c.py > limit20_1c.log  (about 10 s).

Literature form (Ramanathan and Kurinsky, arXiv:2004.10709 Eqs. (A6)-(A7), as printed): F_meas = F/eta + (1 - eta),
eta the charge collection efficiency (= f_det).  Book results (Sect. 20.1, App. C.11):
  exact binomial thinning (position-independent, all-or-nothing collection) f F + 1 - f (eq:C.11-thinfano);
  fuller result eq:20.1-Fpos with the two-carrier Hecht induced charge (charge20_1.py):
    (i) every pair at mid-plane, equal drift lengths (partial charges, no position spread);
    (ii) uniform event depth, equal drift lengths, N = 100 eV / 3.75 eV = 26.7 pairs (position spread included).
F = F_eh = 0.114 (Sect. 18.2/18.4).  Controlling parameter: mean collected fraction f_det = <qbar>.
Shaded: the printed form within 10 % of exact thinning.  Leading correction of the printed form: F(1/f - f).
"""
import os
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from charge20_1 import (F_EH, EPS_EH, thin, rk_printed, fmeas_fixed, fmeas_uniform, lam_for_midplane,
                        lam_for_uniform, FIG)

f = np.linspace(0.5, 0.9999, 300)
ex = thin(F_EH, f)
rk = rk_printed(F_EH, f)
fm = np.linspace(0.5, 0.995, 80)
mid = [fmeas_fixed(F_EH, 0.5, lam_for_midplane(v), lam_for_midplane(v))[0] for v in fm]
N100 = 100 / EPS_EH
uni = [fmeas_uniform(F_EH, N100, lam_for_uniform(v), lam_for_uniform(v))[0] for v in fm]
e10 = brentq(lambda t: rk_printed(F_EH, t) / thin(F_EH, t) - 1.10, 0.5, 0.9999)
print("printed form within 10 %% of exact thinning for f_det >= %.4f" % e10)
for v in [0.6, 0.8, 0.9, 0.95, 0.98, 0.99]:
    lm, lu = lam_for_midplane(v), lam_for_uniform(v)
    print("f_det = %.2f: thinning %.4f; printed %.4f (excess %.4f = F(1/f - f) %.4f); mid-plane Hecht %.4f; "
          "uniform depth, 100 eV %.4f"
          % (v, thin(F_EH, v), rk_printed(F_EH, v), rk_printed(F_EH, v) - thin(F_EH, v), F_EH * (1 / v - v),
             fmeas_fixed(F_EH, 0.5, lm, lm)[0], fmeas_uniform(F_EH, N100, lu, lu)[0]))
# the published 0.130 / 0.160 at 98 / 95 %
for v, pub in [(0.98, 0.130), (0.95, 0.160)]:
    print("Ramanathan-Kurinsky text value %.3f at %.2f: exact thinning %.4f (F = 0.115), %.4f (F = 0.112); printed form %.4f (F = 0.115)"
          % (pub, v, thin(0.115, v), thin(0.112, v), rk_printed(0.115, v)))

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.8, 3.1))
ax.axvspan(e10, 1.0, color="0.88", lw=0)
ax.plot(f, rk, "k--", lw=1.3, label=r"published form $F_{\mathrm{eh}}/f_{\mathrm{det}} + 1 - f_{\mathrm{det}}$")
ax.plot(f, ex, "k-", lw=1.5, label=r"binomial thinning $f_{\mathrm{det}}F_{\mathrm{eh}} + 1 - f_{\mathrm{det}}$")
ax.plot(fm, mid, "b-", lw=1.3, label="partial charges, pair at mid-plane")
ax.plot(fm, uni, "r-", lw=1.3, label=r"partial charges, uniform depth, $\omega = 100$ eV")
ax.set_xlim(0.5, 1.0)
ax.set_ylim(0.0, 0.8)
ax.set_xlabel(r"mean collected fraction $f_{\mathrm{det}}$")
ax.set_ylabel(r"$F_{\mathrm{meas}}$")
ax.legend(loc="upper right", fontsize=6.8, frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit20_1c.pdf"))
print("wrote limit20_1c.pdf")
