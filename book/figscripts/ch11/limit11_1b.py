"""Limit 11.1b: the light-mediator one-phonon rate per unit mass against its target-independent limit.
Output: tex/figures/ch11/limit11_1b.pdf. Prints the numbers quoted in the box, the caption, WE 11.2 and Appendix F.

Literature formula (dashed line at 1): R = rho_chi sigma_p q0^4 eta(0) / (4 m_chi mu_chip^2 m_u^2 omega_th), target independent
   (1910.10716 Eq. (35) in the book's normalization, eq:11.1-light).
Full result for one branch of speed c (solid): R / R_lead = (u_-/eta0) int_{u_-}^{u_+} eta(c + u) u^-2 du,
   u_- = omega_th/(2 m_chi c), u_+ = v_max - c, so that u_-/u_+ = m_min^ac/m_chi and the curve depends on x = m_chi/m_min^ac.
   c = 9.017 km/s (silicon c_LA averaged over directions); at x = 10 the curve changes by 2 % between c = 3 and 18 km/s (printed below).
Silicon, all branches and directions with the zone cut q <= q_BZ (red points): phon11.rate_per_mass / phon11.light_leading,
   with x = m_chi / m_min^ac evaluated at the effective speed 1/<sum (q.e)^2/c> = 8.956 km/s (Sect. 11.1).
Leading correction (dotted): 1 - (1 + kappa_eta) / x, kappa_eta = 3.14 (c -> 0) or 3.09 at c = 9 km/s (used here).
Halo: Sect. 1.2 standard halo model, eta from App. D.1 (phon11.eta). omega_th = 1 meV (the curve does not depend on it).
"""
import os
import sys
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import phon11 as P  # noqa: E402

C = 9.017 * P.KMS
UP = P.VMAX - C
KAP = P.kappa_eta(UP)
print("kappa_eta at c = 9.017 km/s: %.3f; at c -> 0: %.3f" % (KAP, P.kappa_eta()))


def ratio_branch(x, c=C):
    up = P.VMAX - c
    um = up / x
    f = lambda u: float(P.eta(c + u)) / u**2
    val = quad(f, um, up, limit=400, points=[p for p in [(P.VESC - P.VE) * P.KMS - c] if um < p < up])[0]
    return um / P.ETA0 * val


x = np.logspace(0.0, 3.0, 160)
r = np.array([ratio_branch(xi) for xi in x])
first = 1 - (1 + KAP) / x
i10 = np.where(np.abs(r / first - 1) > 0.10)[0]
x10 = x[i10[-1] + 1]
xlit = x[np.where(r < 0.9)[0][-1] + 1]
print("first-order form within 10 %% of the full curve for x >= %.1f; full curve within 10 %% of 1 for x >= %.1f"
      % (x10, x[np.where(r < 0.9)[0][-1] + 1]))
for xi in [1.5, 2, 3, 5, 10, 20, 30, 100]:
    rb = ratio_branch(xi)
    print("x = %5.1f: full %.4f, first order %.4f" % (xi, rb, 1 - (1 + KAP) / xi))
print("c-dependence: x = 10, c = 3, 9, 18 km/s:", [round(ratio_branch(10, cc * P.KMS), 4) for cc in (3.0, 9.017, 18.2)])

# silicon, full average with the zone cut
av = P.averages("Si")
mm = P.mmin_ac(av["cNR1"])
ms = np.logspace(np.log10(1.3 * mm), np.log10(3e3 * mm), 28)
rs = np.array([P.rate_per_mass(m, "Si", "light", av=av) / P.light_leading(m) for m in ms])
mhi = av["qBZ"] / (2 * P.VMAX)
print("Si: m_min^ac(c_eff) = %.2f keV; m_hi = %.3f MeV, x_hi = %.1f; residual at large mass 1 - w_th/(c q_BZ) = %.4f"
      % (mm / 1e3, mhi / 1e6, mhi / mm, 1 - 1e-3 / (av["cNR1"] * P.KMS * av["qBZ"])))
for m, rr in zip(ms, rs):
    if np.isclose(m / mm, [3, 10, 30, 100, 1000], rtol=0.15).any():
        print("Si m = %.1f keV (x = %.1f): R/R_lead = %.4f" % (m / 1e3, m / mm, rr))

fig, ax = plt.subplots(figsize=(5.0, 3.3))
ax.axvspan(xlit, 1e3, color="0.88", lw=0)
ax.axhline(1.0, color="k", ls="--", lw=1.0, label=r"target-independent limit $\propto 1/\omega_{\mathrm{th}}$")
ax.semilogx(x, r, color="C3", lw=1.5, label="one branch, full integral")
ax.semilogx(x, first, color="C0", ls=":", lw=1.4, label=r"$1 - (1 + \kappa_\eta)\,m_{\mathrm{min}}^{\mathrm{ac}}/m_\chi$")
ax.semilogx(ms / mm, rs, "o", ms=3, mfc="none", color="C3", label=r"silicon, all branches, $q \leq q_{\mathrm{BZ}}$")
ax.axvline(mhi / mm, color="0.5", lw=0.6)
ax.text(mhi / mm / 1.08, 0.62, r"$m_\chi = q_{\mathrm{BZ}}/2v_{\mathrm{max}}$" + "\n(Si)", fontsize=7, color="0.3", ha="right")
ax.set_xlim(1, 1e3)
ax.set_ylim(0, 1.1)
ax.set_xlabel(r"$m_\chi / m_{\mathrm{min}}^{\mathrm{ac}}$")
ax.set_ylabel("rate / limit")
ax.legend(fontsize=7, frameon=False, loc="lower right")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_1b.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
