"""Limit 12.2b (Sect. 12.2): Migdal excitation of bound final states, in the form of Kahlhoefer and Su (arXiv:2604.26773,
Eqs. (1), (6)): P_bound = sum over a finite list of bound levels f of |<f|exp(i q_e . sum r)|i>|^2, at dipole order
q_e^2 sum_f |<f|D_z|i>|^2. Hydrogen 1s, where every term is known exactly (a0 = 1, xi_D = q_e a0).

Curves, all divided by xi^2:
  exact: all bound n <= 40 and all l <= 12, full plane wave (radial integrals with j_l, atom12_2.p_bound_exact), n^-3 tail;
  dipole, all bound np levels: sum |<np|z|1s>|^2 = 0.7166;
  dipole, n <= 3 only (the truncation of the source, which keeps n <= 3): 0.5549 + 0.0890 = 0.6439;
  oscillator-strength share: (f_bound/N_e) x total dipole probability = 0.5650 xi^2, the lower bound of the text.
Shaded: xi_D where the dipole sum over all bound levels is within 10 % of the exact bound probability.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import atom12_2 as A  # noqa: E402

if __name__ == "__main__":
    n, z2, f = A.dipole_lines_H()
    dip_all = z2.sum() + z2[-1] * n[-1] / 2
    dip_3 = z2[:2].sum()
    fb = f.sum() + f[-1] * n[-1] / 2
    print(f"H dipole: |z|^2 2p {z2[0]:.5f}, 3p {z2[1]:.5f}; n<=3 {dip_3:.4f}; all bound {dip_all:.4f}; continuum {1 - dip_all:.4f}")
    print(f"H oscillator strengths: 2p {f[0]:.4f}, 3p {f[1]:.4f}; bound {fb:.4f}; continuum {1 - fb:.4f}")
    print(f"   bound share of probability {dip_all:.4f} >= bound share of f {fb:.4f}; n<=3 / all = {dip_3 / dip_all:.4f}")
    xi = np.geomspace(0.02, 2.0, 41)
    cache = os.path.join(HERE, "limit12_2b_exact.npz")
    if os.path.exists(cache) and np.allclose(np.load(cache)["xi"], xi):
        ex = np.load(cache)["ex"]
    else:
        ex = np.array([A.p_bound_exact(x) for x in xi])          # about 4 min
        np.savez(cache, xi=xi, ex=ex)
    r = ex / xi**2
    tot = A.p_inel_H(xi)
    for x0 in (0.02, 0.1, 0.3, 0.5, 1.0):
        print(f"xi = {x0}: exact bound / xi^2 = {np.interp(x0, xi, r):.4f}; bound/total = {np.interp(x0, xi, ex / tot):.4f}")
    bad = np.where(dip_all / r - 1 > 0.10)[0]
    edge = np.interp(0.10, (dip_all / r - 1)[bad[0] - 1:bad[0] + 1], xi[bad[0] - 1:bad[0] + 1])
    print(f"dipole (all levels) within 10 % of exact for xi <= {edge:.3f}")
    # check: 2p alone, exact closed form (2^15/3^10) xi^2/(1 + 4 xi^2/9)^6 (Sect. 2.2)
    r2p = np.trapezoid(A.R_nl(2, 1, A.R_GRID) * A.R10 * A.spherical_jn(1, 0.5 * A.R_GRID) * A.R_GRID**2, A.R_GRID)
    print("check 2p at xi = 0.5: numeric %.6f, closed form %.6f" % (3 * r2p**2, 2**15 / 3**10 * 0.25 / (1 + 4 * 0.25 / 9)**6))

    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.axvspan(xi[0], edge, color="0.88", lw=0)
    ax.plot(xi, r, color="k", lw=1.6, label="exact, all bound levels")
    ax.axhline(dip_all, color="C3", lw=1.2, ls="--", label="dipole, all bound levels")
    ax.axhline(dip_3, color="C0", lw=1.2, ls="-.", label=r"dipole, $n \leq 3$")
    ax.axhline(fb, color="C2", lw=1.2, ls=":", label=r"oscillator-strength share $f^{\mathrm{osc}}_{\mathrm{exc}}/N_e$")
    ax.set_xscale("log")
    ax.set_xlim(xi[0], xi[-1])
    ax.set_ylim(0, 0.8)
    ax.set_xlabel(r"$\xi_D = q_e a_0$")
    ax.set_ylabel(r"$P_{\mathrm{exc}}/\xi_D^2$")
    ax.legend(fontsize=7, frameon=False, loc="lower left")
    fig.tight_layout()
    out = os.path.join(HERE, "..", "..", "tex", "figures", "ch12", "limit12_2b.pdf")
    fig.savefig(out)
    print("wrote", os.path.abspath(out))
