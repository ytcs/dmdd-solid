"""Limit 10.7b (Sect. 10.7): the energy-weighted sum rule of the kinetic-energy row,
    sum_f (E_f - E_0) |<f|T|0>|^2 = <|grad V|^2> / (2 m_e)        (one electron, local one-body potential V),
against the cumulative spectral sum up to a maximum excitation energy Lambda, for one electron in three central
potentials: the Coulomb potential -1/r (hydrogen 1s) and two regular potentials -1/sqrt(r^2 + r_c^2), r_c = 0.3 and
0.1 a_0.  Atomic units (hbar = m_e = e^2/(4 pi) = 1; energies in hartree, Ha = 27.2114 eV).
T conserves angular momentum, so only s -> s transitions enter; for f != 0, <f|T|0> = -<f|V|0> (eigenstates of T + V).
Coulomb asymptote: with box states sqrt(2/R) sin(k r), sum_f -> (R/pi) int dk, and <k|V|1s> = -2 sqrt(2/R) k/(1 + k^2),
so the cumulative sum approaches (4/pi) k_Lambda = (4/pi) sqrt(2 Lambda): it grows without bound, <|grad V|^2> = <1/r^4>
diverges for an s state.  For the regular potentials the sum saturates at <|grad V|^2>/2, reached once Lambda is
well above 1/(2 r_c^2).
Numerics (modelling choices, named in the caption): radial equation for u = r R on a uniform grid r_i = i dr,
dr = 0.004 a_0, box R = 30 a_0 (u(R) = 0), three-point second difference; eigenpairs below Lambda_max = 2000 Ha.
The discrete identity sum over all box states = -(1/2)<[[T,V],V]> is checked on the full grid for r_c = 0.3.
Output: tex/figures/ch10/limit10_7b.pdf
"""
import os
import numpy as np
from scipy.linalg import eigh_tridiagonal
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")
DR, RBOX, LMAX = 0.004, 30.0, 2000.0
r = np.arange(1, int(RBOX / DR)) * DR
N = len(r)


def solve(V, emax=LMAX):
    d = 1.0 / DR**2 + V
    e = -0.5 / DR**2 * np.ones(N - 1)
    w, u = eigh_tridiagonal(d, e, select="v", select_range=(-10.0, emax))
    return w, u


def cumulative(rc):
    V = -1.0 / np.sqrt(r**2 + rc**2)
    w, u = solve(V)
    u0 = u[:, 0]
    Vf0 = u.T @ (V * u0)
    om = w - w[0]
    terms = om[1:] * Vf0[1:]**2
    dV = r / (r**2 + rc**2)**1.5
    sumrule = 0.5 * np.sum(u0**2 * dV**2)
    return w[0], om[1:], np.cumsum(terms), sumrule


def main():
    res = {}
    for rc in (0.0, 0.3, 0.1):
        e0, om, cum, sr = cumulative(rc)
        res[rc] = (om, cum, sr)
        print(f"r_c = {rc}: E_0 = {e0:.5f} Ha; <|V'|^2>/2 = {sr:.4f} Ha^3 (grid value); cumulative at 100, 500, 2000 Ha:"
              f" {np.interp(100, om, cum):.4f}, {np.interp(500, om, cum):.4f}, {cum[-1]:.4f}")
        if rc > 0:
            frac = cum / sr
            i = np.argmax(frac >= 0.9)
            print(f"   reaches 90 % of the sum rule at Lambda = {om[i]:.1f} Ha; 1/(2 r_c^2) = {0.5/rc**2:.1f} Ha")
    om, cum, _ = res[0.0]
    for L in (100.0, 500.0, 2000.0):
        print(f"Coulomb: cumulative / (4/pi) sqrt(2 Lambda) at {L:.0f} Ha = {np.interp(L, om, cum)/(4/np.pi*np.sqrt(2*L)):.3f}")
    # discrete identity check on the full grid (r_c = 0.3, all eigenpairs)
    rc = 0.3
    V = -1.0 / np.sqrt(r**2 + rc**2)
    Nc = 3000
    rr, VV = r[:Nc], V[:Nc]
    d = 1.0 / DR**2 + VV
    e = -0.5 / DR**2 * np.ones(Nc - 1)
    w, u = eigh_tridiagonal(d, e)
    T = np.diag(np.full(Nc, 1.0 / DR**2)) + np.diag(e, 1) + np.diag(e, -1)
    Vm = np.diag(VV)
    X = T @ Vm - Vm @ T
    Y = X @ Vm - Vm @ X
    u0 = u[:, 0]
    dc = -0.5 * u0 @ Y @ u0
    Vf0 = u.T @ (VV * u0)
    spec = np.sum((w - w[0]) * Vf0**2)
    print(f"discrete identity (box {rr[-1]:.0f} a0, r_c = 0.3): spectral {spec:.6f} vs -(1/2)<[[T,V],V]> {dc:.6f}")

    fig, ax = plt.subplots(figsize=(4.6, 3.5))
    Lg = np.logspace(0, np.log10(LMAX), 400)
    ax.loglog(Lg, 4 / np.pi * np.sqrt(2 * Lg), color="0.4", lw=0.8, ls="--", label=r"Coulomb asymptote $(4/\pi)\sqrt{2E_{\mathrm{cut}}}$")
    ax.loglog(om, cum, color="k", lw=1.2, label=r"Coulomb, $-1/r$")
    for rc, col in ((0.3, "C0"), (0.1, "C3")):
        o, c, sr = res[rc]
        ax.loglog(o, c, color=col, lw=1.2, label=rf"regular, $r_{{\mathrm{{c}}}} = {rc}\,a_0$")
        ax.axhline(sr, color=col, lw=0.8, ls=":")
        i = np.argmax(c / sr >= 0.9)
        ax.axvspan(o[i], LMAX, ymin=0, ymax=1, color=col, alpha=0.08, lw=0)
    ax.set_xlim(1, LMAX)
    ax.set_ylim(0.05, 200)
    ax.set_xlabel(r"$E_{\mathrm{cut}}$  [hartree]")
    ax.set_ylabel(r"$\sum_{f}\,(E_f - E_0)\,|\langle f|T|0\rangle|^2$ up to $E_{\mathrm{cut}}$  [hartree$^3$]", fontsize=9)
    ax.legend(fontsize=7, frameon=False, loc="upper left")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "limit10_7b.pdf"))
    print("wrote limit10_7b.pdf")


if __name__ == "__main__":
    main()
