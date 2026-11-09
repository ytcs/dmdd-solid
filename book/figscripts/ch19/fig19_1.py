"""Fig. 19.1 (fig:19-recoil): (a) schematic of a 200 eV silicon recoil in a (1-10) plane; (b) the regime parameters
of recoil dynamics in silicon against the recoil energy, from rec19.py (numbers logged in rec19.log).

Panel (a) is a SCHEMATIC: atom positions are the diamond lattice projected on (1-10) (a = 5.431 A); the paths, the
end positions of the vacancy and the interstitial, and the heat rings are drawn by hand. Its labels carry only
sourced numbers: E_R = 200 eV; first bond crossed in ~6 fs (rec19.log: 2.352 A at 37.07 km/s = 6.3 fs);
head-on turning point 0.83 A at 200 eV (App. E.11, tab:E-md-si); close Frenkel pair 6.8-7.5 eV (Sect. 7.4,
Holmstrom et al.); t_pr = 10-100 ps (definition, Sect. 19.1).
Panel (b): (lambda_dB/l_R)^2, eta_R^2, exp(-xi_M) and x_R^(-1/2) = sigma_w/E_R against E_R, with the 0.1 criterion,
the impulse onset x_R = 4, the displacement thresholds 12.5 eV (<111>) and 36 eV (average), and the binary
electron-hole threshold 352 eV (Sect. 19.2). Top axis: smallest dark-matter mass reaching E_R at v_max = 2.650e-3.
Output: tex/figures/ch19/fig19_1.pdf
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import rec19 as R

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch19", "fig19_1.pdf")
plt.rcParams.update({"font.size": 8, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6})


def lattice_110(a=5.431, n=3):
    base = np.array([[0, 0, 0], [0, .5, .5], [.5, 0, .5], [.5, .5, 0]])
    basis = np.vstack([base, base + 0.25])
    pts = []
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            for k in range(-n, n + 1):
                for b in basis:
                    pts.append((np.array([i, j, k]) + b) * a)
    pts = np.array(pts)
    nrm = np.array([1, -1, 0]) / np.sqrt(2)
    e1 = np.array([1, 1, 0]) / np.sqrt(2)
    e2 = np.array([0, 0, 1.0])
    d = pts @ nrm
    sel = np.abs(d) < 2.0
    return np.c_[pts[sel] @ e1, pts[sel] @ e2, np.abs(d[sel]) < 0.1]


def panel_a(ax):
    xyz = lattice_110()
    box = (np.abs(xyz[:, 0]) < 9.5) & (np.abs(xyz[:, 1]) < 7.2)
    xyz = xyz[box]
    inpl = xyz[:, 2] > 0.5
    xy = xyz[inpl, :2]
    ax.scatter(xyz[~inpl, 0], xyz[~inpl, 1], s=10, c="0.8", zorder=2, lw=0)
    # heat rings (schematic)
    for r, al in [(6.5, 0.10), (4.5, 0.16), (2.6, 0.24)]:
        ax.add_patch(Circle((0.6, 0.4), r, color="tab:orange", alpha=al, lw=0))
    # struck atom site (vacancy at the end): left empty
    i0 = np.argmin(np.hypot(xy[:, 0], xy[:, 1]))
    p0 = xy[i0]
    keep = np.arange(len(xy)) != i0
    ax.scatter(xy[keep, 0], xy[keep, 1], s=18, c="0.45", zorder=3, lw=0)
    ax.add_patch(Circle(p0, 0.55, fill=False, ec="k", lw=0.8, zorder=5))
    # path of the primary: toward an upper-right neighbor, deflected
    d = np.hypot(xy[:, 0] - p0[0], xy[:, 1] - p0[1])
    nb = xy[(d > 2.0) & (d < 2.6) & (xy[:, 0] > p0[0]) & (xy[:, 1] > p0[1])][0]
    path = np.array([p0, p0 + 0.62 * (nb - p0), p0 + 0.62 * (nb - p0) + np.array([2.6, -1.4]),
                     p0 + 0.62 * (nb - p0) + np.array([4.6, -0.9])])
    ax.plot(path[:, 0], path[:, 1], color="tab:blue", lw=1.3, zorder=6)
    ax.add_patch(FancyArrowPatch(path[-2], path[-1], arrowstyle="-|>", mutation_scale=8, color="tab:blue", lw=1.3, zorder=6))
    ax.scatter([path[-1][0]], [path[-1][1]], s=26, c="tab:red", zorder=7, lw=0)
    # secondary recoil
    sec = np.array([nb, nb + np.array([0.9, 2.3])])
    ax.plot(sec[:, 0], sec[:, 1], color="tab:blue", lw=0.9, ls="--", zorder=6)
    ax.add_patch(FancyArrowPatch(sec[0], sec[1], arrowstyle="-|>", mutation_scale=7, color="tab:blue", lw=0.9, ls="--", zorder=6))
    # kick
    ax.add_patch(FancyArrowPatch(p0 + np.array([-3.4, -2.4]), p0 - np.array([0.45, 0.32]), arrowstyle="-|>",
                                 mutation_scale=9, color="k", lw=1.0, zorder=6))
    kw = dict(fontsize=7.3, zorder=8)
    ax.text(p0[0] - 8.9, p0[1] - 3.5, "kick $\\mathbf{q}$, $E_R = 200$ eV,\nzero-point positions", **kw)
    ax.text(nb[0] - 1.0, nb[1] + 2.75, "secondary recoil", **kw)
    ax.text(p0[0] + 0.55, p0[1] + 2.5, "first bond\nin $\\approx 6$ fs;\nclosest approach\n$\\approx 0.83$ Å", **kw, ha="right")
    ax.text(path[-1][0] - 1.7, path[-1][1] - 1.5, "interstitial", color="tab:red", **kw)
    ax.text(p0[0] - 1.0, p0[1] - 1.6, "vacancy", **kw)
    ax.text(-9.3, -7.0, "$\\lesssim 0.1$ ps: collisions; $\\sim 1$ ps: heat spreads", **kw)
    ax.text(-0.6, 6.0, "$t_{\\mathrm{pr}} = 10$–$100$ ps: quench;\nclose Frenkel pair 6.8–7.5 eV", **kw)
    ax.set_xlim(-9.5, 9.5)
    ax.set_ylim(-7.2, 7.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(a) schematic", fontsize=8, loc="left")


def panel_b(ax):
    E = np.logspace(-2, 4, 600)
    cl = (R.lam_dB(E) / R.ell_R(E))**2
    eta2 = R.eta_R(E)**2
    na = np.exp(-R.xi_M(E))
    dw = R.x_R(E)**-0.5
    ax.loglog(E, cl, color="tab:blue", lw=1.2, label=r"$(\lambda_{\mathrm{dB}}/\ell_R)^2$ quantum")
    ax.loglog(E, eta2, color="tab:green", lw=1.2, label=r"$\eta_R^2$ anharmonic")
    ax.loglog(E, na, color="tab:red", lw=1.2, label=r"$\mathrm{e}^{-\xi_{\mathrm{M}}}$ nonadiabatic")
    ax.loglog(E, dw, color="0.4", lw=1.0, ls="--", label=r"$x_R^{-1/2} = \sigma_\omega/E_R$")
    ax.axhline(0.1, color="0.6", lw=0.6, ls=":")
    E_cl = np.pi * R.W / np.sqrt(0.1)
    E_h = 0.1 * R.LANH**2 * R.k_spring() / 2
    # label heights chosen so that no rotated label crosses a curve
    for x, lab, ls, yl in [(4 * R.W, "$x_R = 4$", ":", 1.2), (12.5, "$E_{\\mathrm{d}}$ $\\langle111\\rangle$", "-", 6e-4),
                           (36.0, "$E_{\\mathrm{d}}$ avg", "--", 6e-4), (352.0, "binary\nthreshold", ":", 2e-6)]:
        ax.axvline(x, color="k", lw=0.6, ls=ls)
        ax.text(x * 1.12, yl, lab, fontsize=6.9, rotation=90, va="bottom")
    ax.axvspan(1e-2, E_cl, color="tab:blue", alpha=0.07, lw=0)
    ax.axvspan(E_cl, 12.5, color="tab:green", alpha=0.07, lw=0)
    ax.axvspan(12.5, 1e4, color="tab:orange", alpha=0.07, lw=0)
    ax.text(0.012, 20, "quantum:\nresponse's\nphonons", fontsize=6.8)
    ax.text(0.7, 20, "classical,\nin the basin:\nall heat", fontsize=6.9)
    ax.text(48, 20, "displacement\ncascade:\ndefects", fontsize=6.9)
    ax.set_xlim(1e-2, 1e4)
    ax.set_ylim(1e-6, 3e2)
    ax.set_xlabel(r"recoil energy $E_R$ (eV)")
    ax.set_ylabel("regime parameter")
    ax.legend(fontsize=6.8, loc="lower left", frameon=True, framealpha=1.0, edgecolor="none")
    Eg = np.logspace(-2.5, 4.5, 2000)
    mg = np.array([R.mchi_min(x) for x in Eg]) / 1e6
    sec = ax.secondary_xaxis("top", functions=(lambda e: np.interp(np.log10(np.clip(e, 1e-3, 1e5)), np.log10(Eg), mg),
                                                lambda m: 10**np.interp(m, mg, np.log10(Eg))))
    sec.set_xscale("log")
    sec.set_xticks([10, 30, 100, 300, 1000, 3000])
    sec.set_xticklabels(["10", "30", "100", "300", "1000", "3000"])
    sec.set_xlabel(r"smallest dark-matter mass $m_\chi$ (MeV)", fontsize=7)
    ax.set_title("(b)", fontsize=8, loc="left")
    print("fig19_1: classical boundary %.4f eV, harmonic boundary %.4f eV" % (E_cl, E_h))


def main():
    fig, (a, b) = plt.subplots(1, 2, figsize=(7.0, 3.6), gridspec_kw=dict(width_ratios=[1.0, 1.15]))
    panel_a(a)
    panel_b(b)
    fig.tight_layout(w_pad=0.6)
    fig.savefig(OUT)
    print("wrote", os.path.normpath(OUT))


if __name__ == "__main__":
    main()
