"""Fig. 15.1 (fig:15-alloss): loss function of aluminum near the pair-breaking edge at two fixed momentum transfers,
q = 0.3 eV and q = 1 eV, against the energy omega, for Delta_BCS = 0.18 meV (bulk, measured; Sect. 15.1).
Curves: conserving response (pair-field ladder + Coulomb RPA), bare quasiparticle bubble, g_I(omega/Delta) L_nor,
Lindhard L_nor.  The energies reachable by halo dark matter at this q, omega <= q v_max, are left unshaded.
Clean, T = 0, quasiclassical, q << k_F (bcs15.py).  L is printed in units of 10^-8.
Output: tex/figures/ch15/fig15_1.pdf, fig15_1.log.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import bcs15 as b

out = []


def pr(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


D = b.DELTA_BULK
qs = [0.3, 1.0]
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.7))
for ax, q, lab in zip(axs, qs, "ab"):
    Q = q * b.VF / D
    wmax = q * b.VMAX
    ws = np.concatenate([np.linspace(0.02 * D, 2 * D * (1 - 1e-6), 30), 2 * D + (wmax * 1.25 - 2 * D) *
                         np.linspace(0, 1, 400)[1:] ** 1.6])
    L = np.zeros((len(ws), 4))
    for i, w in enumerate(ws):
        y = w / D
        pn = b.P_nor(y, Q)
        Ln = b.loss(pn, Q, D)
        if y <= 2:
            L[i] = [0, 0, 0, Ln]
            continue
        pb, pc = b.P_resp(y, Q, n=16)
        L[i] = [b.loss(pc, Q, D), b.loss(pb, Q, D), float(b.gI(y)) * Ln, Ln]
    L *= 1e8
    pr(f"q = {q} eV: Q = q v_F/Delta = {Q:.2f}, omega_max = q v_max = {wmax * 1e3:.3f} meV (y = {wmax / D:.2f})")
    for yy in (2.2, 3.0, 4.0, wmax / D):
        w = yy * D
        pb, pc = b.P_resp(yy, Q, n=16)
        pn = b.P_nor(yy, Q)
        Lc, Lb, Ln = b.loss(pc, Q, D), b.loss(pb, Q, D), b.loss(pn, Q, D)
        pr(f"   omega = {w * 1e3:.3f} meV (y = {yy:.2f}): 1e8 L_cons = {Lc * 1e8:.4f}, L_bare = {Lb * 1e8:.4f},"
           f" g_I L_nor = {float(b.gI(yy)) * Ln * 1e8:.4f}, L_nor = {Ln * 1e8:.4f}; L_cons/L_nor = {Lc / Ln:.3f},"
           f" L_bare/L_nor = {Lb / Ln:.3f}")
    ax.axvspan(wmax * 1e3, ws[-1] * 1e3, color="0.88", lw=0)
    ax.axvline(2 * D * 1e3, color="0.6", lw=0.6, ls=":")
    ax.plot(ws * 1e3, L[:, 3], color="k", lw=1.0, label=r"Lindhard $L^{\mathrm{nor}}$")
    ax.plot(ws * 1e3, L[:, 2], color="#1f5fa8", lw=1.0, label=r"$\mathfrak{g}_{\mathrm{I}}L^{\mathrm{nor}}$")
    ax.plot(ws * 1e3, L[:, 0], color="#c0392b", lw=1.6, label="conserving")
    ax.set_xlim(0, ws[-1] * 1e3)
    ax.set_ylim(0, 1.15 * np.max(L[ws <= wmax]))
    ax.set_xlabel(r"$\omega$ (meV)")
    ax.set_title(f"({lab}) $q = {q}$ eV", fontsize=9, loc="left")
axs[0].set_ylabel(r"$L(q,\omega)\;(10^{-8})$")
axs[1].legend(fontsize=7, loc="upper left", bbox_to_anchor=(0.11, 1.0), frameon=False)
fig.tight_layout()
od = os.path.join(b.HERE, "..", "..", "tex", "figures", "ch15")
os.makedirs(od, exist_ok=True)
fig.savefig(os.path.join(od, "fig15_1.pdf"))
with open(os.path.join(b.HERE, "fig15_1.log"), "w") as f:
    f.write("\n".join(out) + "\n")
