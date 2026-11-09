"""Limit 12.3a (Sect. 12.3): the soft-limit Migdal probability with the 4 alpha coefficient, against the momentum k given
to the electrons. Output: tex/figures/ch12/limit12_3a.pdf. Prints the validity boundary and the numbers of the box.

Literature formula (Knapen, Kozaczuk and Lin, arXiv:2011.09496, Eq. (6)): dP/domega = 4 alpha int d^3k/(2pi)^3 Z_ion(k)^2
  |v_N.k|^2 Im[-1/eps(k, omega)] / (omega^4 k^2), stated "only valid for k in the first Brillouin zone", with eps the
  scalar dielectric function. Here evaluated with the head of the RPA dielectric matrix without local fields at |k|
  ('rpa' column of si_elf_binned.npz: Im(-1/eps_GG) at |q_r + G| = |k|).
Fuller result: the diagonal element of the inverse dielectric matrix with local fields, Im[-(eps^-1)_GG(k_r, omega)]
  (eq:E.6-L; 'lf' column), which is the loss function the derivation of Sect. 12.3 produces at momentum k after the
  diagonal truncation. Off-diagonal elements G != G' (Limit 12.3b's form) are NOT included; Knapen et al. report that
  they change the rate by at most O(1).
Plotted, against k/q_BZ (q_BZ = 2.25 keV, eq:11.1-qBZ):
  solid: ratio of the per-k Migdal weight w(k) = k^2 Z_ion(k)^2 int_{E_g}^{89 eV} domega L(k, omega)/omega^4,
         scalar RPA over local fields (one minus this is the leading correction);
  dashed (right axis): cumulative fraction of the probability (local fields) carried by momenta below k.
  Gray band: k where the ratio stays within 10 % of one, from k = 0 up to its first exit. Both weights are smoothed
  with a 7-bin (0.7 keV) running mean before the ratio is formed, to remove the bin-to-bin noise of the tables.
Z_ion(k) from mig12.z_ion (ld1 core orbitals); E_g = 1.11 eV (the tables' scissor); E_R drops out of both ratios.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mig12 as G  # noqa: E402


def weight(tab):
    m = G.OM >= G.EG
    w = G.OM[m]
    return G.KG**2 * G.ZG**2 * np.trapezoid(tab[m] / w[:, None]**4, w, axis=0)


def main():
    wl = weight(G.LF_G)
    wr = weight(G.RPA_G)
    # bin-to-bin noise of the 100-eV bins: both weights are smoothed with a 7-bin running mean before the ratio
    ker = np.ones(7) / 7
    wl_s = np.convolve(wl, ker, mode="same")
    wr_s = np.convolve(wr, ker, mode="same")
    x = G.KG / G.QBZ
    ratio = np.where(wl_s > 0, wr_s / np.where(wl_s > 0, wl_s, 1), np.nan)
    ratio[-4:] = np.nan
    cum = np.concatenate([[0], np.cumsum(0.5 * (wl[1:] + wl[:-1]) * np.diff(G.KG))])
    cum /= cum[-1]
    ok = x > 0.05
    bad = ok & (np.abs(ratio - 1) > 0.10)
    xb = x[np.argmax(bad)]
    print(f"ratio within 10 % of one for k < {xb:.2f} q_BZ = {xb*G.QBZ/1e3:.2f} keV")
    for xx in [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]:
        print(f"  k = {xx:.1f} q_BZ ({xx*G.QBZ/1e3:.2f} keV): ratio {np.interp(xx, x, ratio):.3f}, "
              f"cumulative fraction {np.interp(xx, x, cum):.3f}")
    print(f"probability fraction from k < q_BZ: {np.interp(1.0, x, cum):.3f}; from k < {xb:.2f} q_BZ: {np.interp(xb, x, cum):.3f}")
    i50 = np.interp(0.5, cum, x)
    print(f"median k of the probability: {i50:.2f} q_BZ = {i50*G.QBZ/1e3:.2f} keV; peak of w(k) at "
          f"{x[np.argmax(wl)]:.2f} q_BZ")
    tot_ratio = np.trapezoid(wr, G.KG) / np.trapezoid(wl, G.KG)
    print(f"whole-k ratio (scalar RPA / local fields) = {tot_ratio:.3f}")

    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.axvspan(0, xb, color="0.88", lw=0)
    ax.axhline(1.0, color="k", ls="--", lw=1.0)
    ax.plot(x[ok], ratio[ok], color="C3", lw=1.5, label="soft limit, scalar RPA $\\varepsilon$ / local fields")
    ax.set_xlim(0, 8)
    ax.set_ylim(0.6, 2.2)
    ax.set_xlabel(r"$p/q_{\mathrm{BZ}}$")
    ax.set_ylabel("Migdal weight per $p$: ratio")
    ax2 = ax.twinx()
    ax2.plot(x, cum, color="C0", lw=1.2, ls="--", label="cumulative probability (local fields)")
    ax2.set_ylim(0, 1.0)
    ax2.set_ylabel("fraction of $P$ below $p$", color="C0")
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, fontsize=6.5, frameon=False, loc="lower right")
    fig.tight_layout()
    out = os.path.join(HERE, "..", "..", "tex", "figures", "ch12", "limit12_3a.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out)
    print("wrote", os.path.normpath(out))


if __name__ == "__main__":
    main()
