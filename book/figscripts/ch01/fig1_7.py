"""Squared dark-matter form factor F_DM(q)^2 against q/q0 for several mediator masses, with the heavy and light limits
and the regions where each limit holds within 10% (limit box 'Heavy and light mediators', Sect. 1.4).
Output: tex/figures/ch01/fig1_7.pdf. Every plotted number is sourced below.
  [KKL] S. Knapen, J. Kozaczuk and T. Lin, Phys. Rev. D 104, 015031 (2021), arXiv:2101.08275, Eq. (12):
        F_DM(q) = (m_V^2 + alpha^2 m_e^2)/(m_V^2 + q^2).
  [EMV] R. Essig, J. Mardon and T. Volansky, Phys. Rev. D 85, 076007 (2012), arXiv:1108.5383, Eq. (15):
        limits F_DM -> 1 (m_V >> alpha m_e) and (alpha m_e/q)^2 (m_V << alpha m_e).
  [CODATA] alpha = 1/137.035999084, m_e = 510998.95 eV (CODATA 2018 recommended values).
Criterion (stated in the caption): a limit "holds" where |F_DM^2/limit - 1| <= 0.1.
Kinematic marker: q = 0.12 q0, the smallest momentum transfer that crosses the 1.17 eV low-temperature silicon gap
  at v_max = 2.650e-3
  (Sect. 1.3).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ALPHA = 1 / 137.035999084          # [CODATA]
M_E = 510998.95                    # eV [CODATA]
Q0 = ALPHA * M_E                   # reference momentum q0 = alpha m_e = 3.73 keV
TOL = 0.1
X_GAP = 1.17 / 2.650e-3 / Q0       # Sect. 1.3: 0.44 keV = 0.12 q0


def f_dm2(x, r):
    """[KKL Eq. (12)] squared, x = q/q0, r = m_V/q0."""
    return ((r**2 + 1) / (r**2 + x**2))**2


x = np.logspace(-1, 2, 600)        # q/q0 from 0.1 to 100: the range of electronic excitations in solids
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.4, 3.0))

# left: curves; segments within 10% of a limit drawn thick
ax.loglog(x, np.ones_like(x), color="k", lw=1.0, label=r"heavy limit, $F_{\mathrm{DM}} = 1$")
ax.loglog(x, x**-4.0, color="C3", lw=1.0, label=r"light limit, $F_{\mathrm{DM}} = (q_0/q)^2$")
for r, ls in [(10.0, "--"), (1.0, "-."), (0.1, ":")]:
    f = f_dm2(x, r)
    ax.loglog(x, f, color="C0", ls=ls, lw=1.0, label=rf"$m_V = {r:g}\,q_0$")
    heavy = np.abs(f - 1) <= TOL
    light = np.abs(f * x**4 - 1) <= TOL
    ax.loglog(np.where(heavy, x, np.nan), np.where(heavy, f, np.nan), color="k", lw=3.2, alpha=0.35)
    ax.loglog(np.where(light, x, np.nan), np.where(light, f, np.nan), color="C3", lw=3.2, alpha=0.35)
    print(f"m_V = {r} q0: heavy within 10% for q/q0 in "
          f"[{x[heavy].min() if heavy.any() else np.nan:.3g}, {x[heavy].max() if heavy.any() else np.nan:.3g}]; "
          f"light within 10% for q/q0 >= {x[light].min() if light.any() else np.nan:.3g}")
ax.axvline(1.0, color="0.6", lw=0.6)
ax.axvline(X_GAP, color="0.6", lw=0.6, ls=":")
ax.set_xlim(0.1, 100)
ax.set_ylim(1e-8, 1e4)
ax.set_xlabel(r"$q/q_0$")
ax.set_ylabel(r"$F_{\mathrm{DM}}(q)^2$")
ax.legend(fontsize=6.5, frameon=False, loc="lower left")

# right: region map in (q/q0, m_V/q0)
r = np.logspace(-2, 2, 400)
XX, RR = np.meshgrid(x, r)
F = f_dm2(XX, RR)
heavy = (np.abs(F - 1) <= TOL).astype(float)
light = (np.abs(F * XX**4 - 1) <= TOL).astype(float)
bx.contourf(XX, RR, heavy, levels=[0.5, 1.5], colors=["0.75"])
bx.contourf(XX, RR, light, levels=[0.5, 1.5], colors=["C3"], alpha=0.35)
bx.contour(XX, RR, heavy, levels=[0.5], colors="k", linewidths=0.6)
bx.contour(XX, RR, light, levels=[0.5], colors="C3", linewidths=0.6)
for rr, ls in [(10.0, "--"), (1.0, "-."), (0.1, ":")]:
    bx.axhline(rr, color="C0", ls=ls, lw=0.8)
bx.axvline(X_GAP, color="0.6", lw=0.6, ls=":")
bx.set_xscale("log")
bx.set_yscale("log")
bx.set_xlim(0.1, 100)
bx.set_ylim(1e-2, 1e2)
bx.set_xlabel(r"$q/q_0$")
bx.set_ylabel(r"$m_V/q_0$")
bx.text(0.13, 30, "heavy limit\nwithin 10%", fontsize=7)
bx.text(8, 0.02, "light limit\nwithin 10%", fontsize=7, color="C3")
# where in m_V the heavy limit holds for every q from the gap threshold to q0, and the light limit above the threshold
print("heavy within 10% for all q in [0.12, 1] q0 needs m_V/q0 >=",
      f"{r[np.all(np.abs(f_dm2(x[(x >= X_GAP) & (x <= 1)][None, :], r[:, None]) - 1) <= TOL, axis=1)].min():.3g}")
print("light within 10% for all q >= 0.12 q0 needs m_V/q0 <=",
      f"{r[np.all(np.abs(f_dm2(x[x >= X_GAP][None, :], r[:, None]) * x[x >= X_GAP]**4 - 1) <= TOL, axis=1)].max():.3g}")
fig.tight_layout()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch01", "fig1_7.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
