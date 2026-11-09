"""Limit Check 15.1a (lim:15.1a, fig:15-limit-chain): the loss function of aluminum near the pair-breaking edge in the
chain conserving response -> bare quasiparticle bubble -> case-I factor times the normal loss function -> Lindhard.

x axis: y = omega/Delta_BCS at the kinematic edge q = omega/v_max, where Delta_BCS/(q v_F) = (v_max/v_F)/y takes its
largest value for each omega (top axis).  y axis: each approximation divided by the conserving loss function L_cons.
  red solid    L_bare/L_cons    bare quasiparticle bubble with Coulomb RPA (Gan et al. arXiv:2609.06423 Eqs. (7)-(9))
  red dotted   g_I (1 - 2 s_BCS Delta/(q v_F)) L_nor / L_cons   first-order Kramers-Kronig correction (Sect. 15.1)
  blue         g_I L_nor/L_cons  (Gan et al. Eq. (10); Hochberg et al. arXiv:2109.04473 Eq. (2) with Im eps_BCS/|eps_L|^2)
  black        L_nor/L_cons      Lindhard loss function (Hochberg et al. arXiv:2101.08263 Eq. (1); for omega << q v_F the
               structure factor of Hochberg et al. arXiv:1512.04533 Eq. (14), screened)
  dashed       the same ratios at four times the edge momentum.
Shaded: y where the Lindhard loss function lies within 10 % of L_cons at the edge (root-finder; 'within 10 %' means
smaller/larger >= 0.9; checked at all larger y and on the 4x curve).  Clean, T = 0, quasiclassical (bcs15.py).  Output: tex/figures/ch15/limit15_1a.pdf, limit15_1a.log.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
import bcs15 as b

out = []


def pr(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


D = b.DELTA_BULK
ys = np.geomspace(2.02, 50, 70)
sb = np.array([b.s_bcs(y) for y in ys])
res = {}
for fac in (1.0, 4.0):
    R = np.zeros((len(ys), 4))
    for i, y in enumerate(ys):
        Q = fac * y / b.XMAX
        pb, pc = b.P_resp(y, Q, n=16)
        pn = b.P_nor(y, Q)
        Lb, Lc, Ln = b.loss(pb, Q, D), b.loss(pc, Q, D), b.loss(pn, Q, D)
        g = float(b.gI(y))
        R[i] = [Lb / Lc, g * Ln / Lc, Ln / Lc, g * (1 - 2 * sb[i] / Q) * Ln / Lc]
    res[fac] = R

pr("y      | edge: Lb/Lc  gI Ln/Lc  Ln/Lc  first/Lc | 4x edge: Lb/Lc  gI Ln/Lc  Ln/Lc  first/Lc")
for i in range(0, len(ys), 5):
    a, c = res[1.0][i], res[4.0][i]
    pr(f"{ys[i]:6.3f} | {a[0]:.4f} {a[1]:.4f} {a[2]:.4f} {a[3]:+.4f} | {c[0]:.4f} {c[1]:.4f} {c[2]:.4f} {c[3]:+.4f}")
from scipy.optimize import brentq


def ratio(y, fac, which):
    """Smaller over larger of (approximation, conserving) at q = fac * omega/v_max: the book's 'within 10 %'
    means this ratio is at least 0.9."""
    Q = fac * y / b.XMAX
    pb, pc = b.P_resp(y, Q, n=24)
    pn = b.P_nor(y, Q)
    Lc = b.loss(pc, Q, D)
    La = {"bare": b.loss(pb, Q, D), "lin": b.loss(pn, Q, D), "gI": float(b.gI(y)) * b.loss(pn, Q, D)}[which]
    return min(La, Lc) / max(La, Lc)


ylo = brentq(lambda y: ratio(y, 1.0, "lin") - 0.9, 5.0, 15.0, xtol=1e-4)
ylo4 = brentq(lambda y: ratio(y, 4.0, "lin") - 0.9, 3.0, 12.0, xtol=1e-4)
ylob = brentq(lambda y: ratio(y, 1.0, "bare") - 0.9, 6.0, 15.0, xtol=1e-4)
ylog = brentq(lambda y: ratio(y, 1.0, "gI") - 0.9, 2.1, 2.5, xtol=1e-4)
pr("Thresholds by root-finding (smaller/larger >= 0.9 on the kinematic edge unless stated):")
pr(f"  Lindhard within 10% of L_cons at the edge for y >= {ylo:.2f} (Delta/(q v_F) <= {b.XMAX / ylo:.4f})")
pr(f"  Lindhard within 10% at 4x the edge momentum for y >= {ylo4:.2f}")
pr(f"  bare bubble within 10% of L_cons at the edge for y >= {ylob:.2f}")
pr(f"  g_I L_nor within 10% of L_cons at the edge for y >= {ylog:.3f}")
gs = np.geomspace(ylo, 50, 25)
pr(f"  check: Lindhard ratio on [{ylo:.2f}, 50] at the edge has min {min(ratio(y, 1.0, 'lin') for y in gs):.4f}, at 4x edge min "
   f"{min(ratio(y, 4.0, 'lin') for y in gs):.4f}")
pr(f"max |gI Ln/Lc - 1| on y >= 3 (grid): {np.max(np.abs(res[1.0][ys >= 3, 1] - 1)):.4f}")
pr(f"bare/conserving at the edge: y = 2.2: {ratio(2.2, 1.0, 'bare'):.3f}; y = 3: {ratio(3.0, 1.0, 'bare'):.3f}; "
   f"Lindhard/conserving at y = 3: {ratio(3.0, 1.0, 'lin'):.3f}; at y = 5: {ratio(5.0, 1.0, 'lin'):.3f}")

fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.axvspan(ylo, 50, color="0.88", lw=0)
cols = ["#c0392b", "#1f5fa8", "k"]
labs = ["bare bubble", r"$\mathfrak{g}_{\mathrm{I}}L^{\mathrm{nor}}$", r"Lindhard $L^{\mathrm{nor}}$"]
for j in range(3):
    ax.plot(ys, res[1.0][:, j], color=cols[j], lw=1.4, label=labs[j])
    ax.plot(ys, res[4.0][:, j], color=cols[j], lw=0.9, ls="--")
ax.plot(ys, res[1.0][:, 3], color=cols[0], lw=1.0, ls=":", label="first order")
ax.axhline(1, color="0.5", lw=0.6)
ax.set_xscale("log")
ax.set_xlim(2, 50)
ax.set_ylim(0, 1.25)
ax.set_xticks([2, 3, 5, 10, 20, 50])
ax.set_xticklabels(["2", "3", "5", "10", "20", "50"])
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_xlabel(r"$y = \omega/\Delta_{\mathrm{BCS}}$ at $q = \omega/v_{\mathrm{max}}$")
ax.set_ylabel(r"$L/L^{\mathrm{cons}}$")
top = ax.secondary_xaxis("top", functions=(lambda y: b.XMAX / np.maximum(y, 1e-9), lambda t: b.XMAX / np.maximum(t, 1e-9)))
top.set_xticks([0.2, 0.1, 0.05, 0.02, 0.01])
top.set_xticklabels(["0.2", "0.1", "0.05", "0.02", "0.01"])
top.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
top.set_xlabel(r"$\Delta_{\mathrm{BCS}}/qv_F$ at the edge", fontsize=8)
ax.legend(fontsize=7, loc="lower right", frameon=False)
fig.tight_layout()
od = os.path.join(b.HERE, "..", "..", "tex", "figures", "ch15")
os.makedirs(od, exist_ok=True)
fig.savefig(os.path.join(od, "limit15_1a.pdf"))
with open(os.path.join(b.HERE, "limit15_1a.log"), "w") as f:
    f.write("\n".join(out) + "\n")
