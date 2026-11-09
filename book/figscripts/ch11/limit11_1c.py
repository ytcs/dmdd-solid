"""Limit 11.1c: the sphere-averaged longitudinal speed as the single sound speed of the one-phonon rate.
Output: tex/figures/ch11/limit11_1c.pdf. Prints the numbers quoted in the box, the caption and Appendix F.

Literature formula: one speed per material, c_bar_LA = <c_LA(q)> over the sphere (1910.10716 App. A3, there from omega_LA/q of
   DFT phonons; here from the Christoffel problem of App. C.18 with the measured tensor), entering the heavy-mediator rate as 1/c_bar_LA.
Full result: the direction- and branch-resolved coefficient <sum_nu (q.e_nu)^2 / c_nu> of eq:11.1-heavy.
Plotted: y = c_bar_LA * <sum_nu (q.e_nu)^2 / c_nu> (= 1 for an isotropic medium) against the Zener ratio A_Z = 2 C44/(C11 - C12),
   for cubic tensors with silicon's C11 = 165.6, C12 = 63.9 GPa and rho = 2.33 g/cm^3 [M19], C44 varied (A_Z = 1.563 is silicon).
   Points: silicon, germanium and diamond with their own tensors (phon11.MATS).
   Second-order expansion (dotted): Delta = C11 - C12 - 2 C44, s = sum_{i<j} q_i^2 q_j^2, p = sum q_i^6 - (sum q_i^4)^2,
      rho c_LA^2 = C11 - 2 Delta s + Delta^2 p/(C12 + C44),   sum_TA (q.e_TA)^2 = Delta^2 p/(C12 + C44)^2,
   both from second-order perturbation theory of the Christoffel matrix about M0 = C44 1 + (C12 + C44) q q (whose longitudinal
   eigenvalue is C12 + 2 C44 and transverse C44), with c_TA = sqrt(C44/rho) at zeroth order in the term that is already O(Delta^2).
Also printed: the pure-LA part c_bar_LA <1/c_LA> (Jensen gap) and the light-mediator edge speed c_LA,max/c_bar_LA.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import phon11 as P  # noqa: E402

C11, C12, RHO = 165.6, 63.9, 2.33e3
qh, wq = P.QH, P.WQ


def full(C11_, C12_, C44_, rho):
    c, ev = P.christoffel(P.ctensor(C11_, C12_, C44_), rho, qh)
    proj2 = np.einsum("ni,nik->nk", qh, ev)**2
    cbar = np.sum(wq * c[:, 2])
    return cbar * np.sum(wq * (proj2 / c).sum(1)), cbar * np.sum(wq / c[:, 2]), c[:, 2].max() / cbar


def second(C11_, C12_, C44_, rho):
    D = C11_ - C12_ - 2 * C44_
    q2 = qh**2
    s = q2[:, 0] * q2[:, 1] + q2[:, 1] * q2[:, 2] + q2[:, 2] * q2[:, 0]
    p = (q2**3).sum(1) - ((q2**2).sum(1))**2
    lamL = C11_ - 2 * D * s + D**2 * p / (C12_ + C44_)
    eps = D**2 * p / (C12_ + C44_)**2
    cL = np.sqrt(lamL * 1e9 / rho) / 1e3
    cT = np.sqrt(C44_ * 1e9 / rho) / 1e3
    cbar = np.sum(wq * cL)
    return cbar * np.sum(wq * ((1 - eps) / cL + eps / cT))


AZ = np.linspace(0.3, 4.0, 75)
C44s = AZ * (C11 - C12) / 2
Y = np.array([full(C11, C12, c44, RHO) for c44 in C44s])
Y2 = np.array([second(C11, C12, c44, RHO) for c44 in C44s])
for a, y, y2 in zip(AZ, Y, Y2):
    if np.isclose(a, [0.5, 1.0, 1.5, 2.0, 3.0, 4.0], atol=0.026).any():
        print("A_Z = %.2f: full y = %.4f (pure LA %.4f, c_LA,max/cbar %.4f), second order %.4f" % (a, y[0], y[1], y[2], y2))
lo = AZ[np.where(Y[:, 0] <= 1.01)[0]]
print("y within 1 %% of one for %.2f <= A_Z <= %.2f" % (lo.min(), lo.max()))
pts = {}
for nm in ("Si", "Ge", "C"):
    c11, c12, c44, a, m, n = P.MATS[nm]
    rho = P.density(nm)
    y = full(c11, c12, c44, rho)
    pts[nm] = (2 * c44 / (c11 - c12), y[0])
    print("%s: A_Z = %.3f, y = %.4f, pure LA %.4f, c_LA,max/cbar = %.4f, second order %.4f"
          % (nm, pts[nm][0], y[0], y[1], y[2], second(c11, c12, c44, rho)))

fig, ax = plt.subplots(figsize=(5.0, 3.3))
ax.axvspan(lo.min(), lo.max(), color="0.88", lw=0)
ax.axhline(1.0, color="k", ls="--", lw=1.0, label=r"one speed, $1/\bar c_{\mathrm{LA}}$")
ax.plot(AZ, Y[:, 0], color="C3", lw=1.5, label=r"direction- and branch-resolved")
ax.plot(AZ, Y2, color="C0", ls=":", lw=1.4, label=r"second order in $C_{11} - C_{12} - 2C_{44}$")
for nm, mk in (("Si", "o"), ("Ge", "s"), ("C", "^")):
    ax.plot(*pts[nm], mk, color="C3", ms=5, mfc="white")
    off = {"Si": (-12, 5), "Ge": (5, -3), "C": (-14, -11)}[nm]
    ax.annotate({"Si": "Si", "Ge": "Ge", "C": "diamond"}[nm], pts[nm], xytext=off, textcoords="offset points", fontsize=7)
ax.set_xlim(0.3, 4.0)
ax.set_ylim(0.99, 1.10)
ax.set_xlabel(r"Zener ratio $A_{\mathrm{Z}} = 2C_{44}/(C_{11} - C_{12})$")
ax.set_ylabel(r"$\bar c_{\mathrm{LA}}\,\langle\sum_\nu(\hat{q}\cdot\hat{e}_\nu)^2/c_\nu\rangle$")
ax.legend(fontsize=7, frameon=False, loc="upper center")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_1c.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
