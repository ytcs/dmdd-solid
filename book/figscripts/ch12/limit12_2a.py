"""Limit 12.2a (Sect. 12.2): the atomic Migdal probability at dipole order (Ibe et al., arXiv:1707.07258, Eqs. (86)-(90))
against the full boost exp(-i q_e . sum r) to all multipoles, as a function of xi_D = q_e a0 = v/alpha.

Curves (ratio full / dipole):
  hydrogen, all final states: [1 - F_1s(xi)^2]/xi^2, exact (eq:6.1-P0; dipole: xi^2 <z^2> = xi^2); leading correction
      1 - (5/8) xi^2 (dashed), from F_1s^2 = (1 + xi^2/4)^-4.
  Si, Ge, exclusive single ionization: Cox et al. (arXiv:2208.12222) table with multipoles L <= 10 (*_DM), minus its
      velocity-independent part c0 (fit c0 + a v^2 + b v^4 below v = 6e-4 (Si), 4e-4 (Ge); a/a_dipole = 0.985, 0.978),
      divided by the dipole table scaled as v^2. Modelling choice stated in the caption.
Shaded: xi_D where Si and Ge stay within 10 % of the dipole result.
Marks: largest recoil velocity v = 2 mu v_max/m_A, v_max = 2.650e-3 (Sect. 1.2), for m_chi = 1 and 10 GeV.
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

VMAX = 2.650e-3


def vmax_recoil(el, mchi):
    mu = mchi * A.MA[el] / (mchi + A.MA[el])
    return 2 * mu * VMAX / A.MA[el]


if __name__ == "__main__":
    xi = np.geomspace(5e-3, 1.0, 400)
    rH = A.p_inel_H(xi) / xi**2
    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    edges = {}
    curves = {}
    for el, col in (("Si", "C1"), ("Ge", "C0")):
        c0, a, b = A.cox_constant(el)
        vs, P = A.cox_full(el)
        Pd = A.cox_dipole_total(el) / 1e-6 * vs**2
        r = (P - c0) / Pd
        x = vs / A.ALPHA
        m = x >= 0.012
        curves[el] = (x[m], r[m])
        ax.plot(x[m], r[m], color=col, lw=1.5, label=f"{el}, single ionization")
        bad = np.where(r < 0.9)[0]
        edges[el] = np.interp(0.9, r[bad[0]:bad[0] - 2:-1], x[bad[0]:bad[0] - 2:-1])
        print(f"{el}: c0 = {c0:.3e}, a/a_dip = {a / (A.cox_dipole_total(el) / 1e-6):.4f}; ratio 0.9 at xi = {edges[el]:.3f} "
              f"(v = {edges[el] * A.ALPHA:.3e}); ratio at xi = 0.05, 0.1, 0.2: "
              + ", ".join(f"{np.interp(z, x, r):.3f}" for z in (0.05, 0.1, 0.2)))
        print(f"    raw (with c0) ratio at xi = 0.02, 0.05: " + ", ".join(f"{np.interp(z, x, P / Pd):.3f}" for z in (0.02, 0.05)))
    print("H: ratio 0.9 at xi = %.3f; at 0.1, 0.2: %.4f, %.4f" % (np.interp(0.9, rH[::-1], xi[::-1]),
                                                             np.interp(0.1, xi, rH), np.interp(0.2, xi, rH)))
    lo = min(edges.values())
    ax.axvspan(xi[0], lo, color="0.88", lw=0)
    ax.plot(xi, rH, color="k", lw=1.5, label="hydrogen, all final states")
    ax.plot(xi, 1 - 5 / 8 * xi**2, color="k", lw=1.0, ls="--", label=r"hydrogen, $1 - \frac{5}{8}\xi_D^2$")
    ax.axhline(1.0, color="0.4", lw=0.8, ls=":")
    for el, col in (("Si", "C1"), ("Ge", "C0")):
        for m, ls in ((1e9, "-"), (1e10, "--")):
            x0 = vmax_recoil(el, m) / A.ALPHA
            ax.plot([x0, x0], [1.02, 1.08], color=col, lw=1.2, ls=ls)
            print(f"{el}: m_chi = {m / 1e9:.0f} GeV: largest recoil v = {vmax_recoil(el, m):.3e}, xi = {x0:.4f}")
    ax.text(0.031, 1.10, r"$m_\chi$ = 1, 10 GeV", fontsize=6.5)
    ax.set_xscale("log")
    ax.set_xlim(xi[0], xi[-1])
    ax.set_ylim(0.0, 1.18)
    ax.set_xlabel(r"$\xi_D = q_e a_0 = v_A/\alpha$")
    ax.set_ylabel("all multipoles / dipole order")
    ax.legend(fontsize=7, frameon=False, loc="lower left")
    fig.tight_layout()
    out = os.path.join(HERE, "..", "..", "tex", "figures", "ch12", "limit12_2a.pdf")
    fig.savefig(out)
    print("shaded xi <", round(lo, 3), "; wrote", os.path.abspath(out))
    for el in ("Si", "Ge"):
        v = edges[el] * A.ALPHA
        mu = v * A.MA[el] / (2 * VMAX)
        print(f"{el}: dark-matter mass whose largest recoil reaches xi = {edges[el]:.3f}: {mu * A.MA[el] / (A.MA[el] - mu) / 1e9:.1f} GeV")
