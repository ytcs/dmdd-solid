"""Limit Check 18.2a (lim:18.2a, fig:18-limit-moments): the energy-dependent pair energy and Fano factor of a finite deposit,
eps(omega) = omega/<N_eh>(omega) and F(omega) = Var N_eh(omega)/<N_eh>(omega) (the definitions of Ramanathan and Kurinsky,
arXiv:2004.10709, Eqs. (2)-(3), with constant high-energy limits), against the cascade moments eps_eh and F_eh (the asymptotic
slopes, Sect. 18.2).  Log: limit18_2a.log.  Run: python limit18_2a.py > limit18_2a.log  (about 1 min).  Solver: mom18_2.py.

Silicon model of fig18_2.py: E_g = 1.160 eV, omega_AB = 63 meV, W_h = 12 eV, theta_ii = 1, parabolic densities of states,
A_AB = 5.703 eV^3 (the one silicon set, si_cascade18.py).  Seed: the electron takes omega - E_g, its hole sits at
the band edge (one-sided seed).  Grid h = 1/74 with interpolation in w over commensurate nodes, X = 60 E_g; the asymptotic slopes
and offsets are fitted over [X/2, X].
Leading correction: <N> = omega/eps_eh + b_N + o(1), Var N = F_eh omega/eps_eh + c_V + o(1), so
  eps(omega)/eps_eh ~ 1/(1 + b_N eps_eh/omega),  F(omega)/F_eh ~ (1 + c_V eps_eh/(F_eh omega))/(1 + b_N eps_eh/omega).
Shaded: omega above which both ratios stay within 10 % of 1 (found on the energy grid of the solver, spacing E_g/74, by scanning
from the top down).
"""
import os
import re
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mom18_2 import Cascade, lagrange
from si_cascade18 import A_AB, EG_SI, OM_SI, BH_SI

OUT = os.path.abspath(os.path.join(HERE, "..", "..", "tex", "figures", "ch18"))
EG, OM, WH = EG_SI, OM_SI, BH_SI
w = OM / EG
A = A_AB
lam = A / EG**3
print("A_AB = %.3f eV^3 (si_cascade18.py), lam_ph = %.4f, w_ph = %.5f; ratios below are taken on one grid, E_g/74" % (A, lam, w))

N = 74
n0 = int(round(w * N))
ks = [n0 - 1, n0, n0 + 1]
xs = [k / N for k in ks]
cs = [Cascade(lam, k / N, X=60.0, h=1.0 / N, W=(None, WH / EG), decomp=False) for k in ks]
x = cs[0].x
om = 1.0 + x
mN = lagrange(xs, [1.0 + c.mean("N") for c in cs], w)
vN = lagrange(xs, [c.var("N") for c in cs], w)
sel = x >= 30.0
Afit = np.vstack([om[sel], np.ones(sel.sum())]).T
sN, bN = np.linalg.lstsq(Afit, mN[sel], rcond=None)[0]
sV, cV = np.linalg.lstsq(Afit, vN[sel], rcond=None)[0]
eps = 1 / sN
F = sV * eps
print("asymptote: eps_eh/E_g = %.4f (%.4f eV), F_eh = %.4f, b_N = %.4f, c_V = %.4f" % (eps, eps * EG, F, bN, cV))

ok = om > 1.0
er = np.full_like(om, np.nan)
fr = np.full_like(om, np.nan)
er[ok] = om[ok] / mN[ok] / eps
fr[ok] = vN[ok] / mN[ok] / F
lead_e = 1 / (1 + bN * eps / om)
lead_f = (1 + cV * eps / (F * om)) / (1 + bN * eps / om)
bad = (np.abs(er - 1) > 0.10) | (np.abs(fr - 1) > 0.10)
idx = np.where(bad & ok)[0]
om10 = om[idx[-1] + 1] if len(idx) else om[1]
print("both within 10 %% of the asymptote for omega >= %.3f E_g = %.2f eV" % (om10, om10 * EG))
for o in (2, 3, 5, 10, 20, 30, 50):
    i = int(round((o - 1) * N))
    print("  omega = %4.0f E_g (%5.1f eV): <N> = %.3f, eps(omega)/eps_eh = %.4f (leading %.4f), F(omega)/F_eh = %.4f (leading %.4f)" %
          (o, o * EG, mN[i], er[i], lead_e[i], fr[i], lead_f[i]))
print("largest F(omega)/F_eh: %.3f at omega = %.2f E_g" % (np.nanmax(fr), om[np.nanargmax(fr)]))
i10 = int(round((10 - 1) * N))
print("at omega = 10 E_g the residual after the leading correction: eps %.4f, F %.4f" % (er[i10] / lead_e[i10] - 1, fr[i10] / lead_f[i10] - 1))

fig, ax = plt.subplots(figsize=(6.0, 3.8))
ax.axvspan(om10, 60, color="0.88", lw=0)
ax.plot(om, er, "C0-", lw=1.4, label=r"$\varepsilon(\omega)/\varepsilon_{\mathrm{eh}}$, $\varepsilon(\omega) = \omega/\langle N_{\mathrm{eh}}\rangle$")
ax.plot(om, fr, "k-", lw=1.2, label=r"$F(\omega)/F_{\mathrm{eh}}$, $F(\omega) = \mathrm{Var}\,N_{\mathrm{eh}}/\langle N_{\mathrm{eh}}\rangle$")
m = om >= 3
ax.plot(om[m], lead_e[m], "C0--", lw=1.0, label="with the constant offsets only")
ax.plot(om[m], lead_f[m], "k--", lw=1.0)
ax.axhline(1.0, color="0.4", ls=":", lw=0.8)
ax.set_xscale("log")
ax.set_xlim(1.0, 60)
ax.set_ylim(0, 2.0)
ax.set_xlabel(r"deposited energy $\omega/E_{\mathrm{g}}$")
ax.set_ylabel("ratio to the cascade moment")
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit18_2a.pdf"))
print("wrote limit18_2a.pdf")
