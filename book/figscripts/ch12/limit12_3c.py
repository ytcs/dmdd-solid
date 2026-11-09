"""Limit 12.3c (Sect. 12.3): the per-mass Migdal rate with the valence ionization factor, against the dark-matter mass.
Output: tex/figures/ch12/limit12_3c.pdf. Prints the validity range and the numbers quoted in the box and the text.

Literature form (factorized soft limit; Knapen, Kozaczuk and Lin, arXiv:2011.09496, Eq. (6) with their Eq. (1)):
  dR/domega = (rho_chi / m_chi) (1/M) int d^3v f(v) v int dE_N (dsigma/dE_N) (dP/domega)(E_N), with the free-recoil range
  0 < E_N < 2 mu_N^2 v^2 / M, i.e. omega dropped from energy conservation; equivalently v_min = q / 2 mu_N in eq:12.3-rate.
  It factorizes into (halo and coupling) x 4 alpha Q_Mig(omega), with Q_Mig per unit mass entering as Q_Mig/A_cell.
Fuller result: eq:12.3-rate with exact free-recoil kinematics, v_min = (omega + q^2/2M)/q + q/2 m_chi.
Both: silicon, heavy mediator (F_DM = F_N = 1), sigma_n = 1e-38 cm^2, halo of Sect. 1.2, Z_ion(k) and 'lf' loss function
  of mig12, momentum transfers above the impulse onset q >= 92.5 keV (x_R = 4, Sect. 11.4), omega >= 1.11 eV (tables).
Plotted against m_chi: total rate (omega >= E_g) of the literature form over the fuller one. Gray band: the masses where
  the ratio is within 10 % of one. Dotted: the same ratio at omega = 10 eV, where the omega dependence of the kinematics
  is larger.
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

MS = np.geomspace(18e6, 3e9, 60)


def totals(m):
    w = G.OM
    sel = w >= G.EG
    ex = G.rate_free(m, qmin=G.Q_ONSET, exact=True)
    ap = G.rate_free(m, qmin=G.Q_ONSET, exact=False)
    i10 = np.argmin(abs(w - 10.0))
    return np.trapezoid(ex[sel], w[sel]), np.trapezoid(ap[sel], w[sel]), ex[i10], ap[i10]


def main():
    res = np.array([totals(m) for m in MS])
    r_tot = res[:, 1] / res[:, 0]
    r_10 = res[:, 3] / np.where(res[:, 2] > 0, res[:, 2], np.nan)
    good = np.abs(r_tot - 1) <= 0.10
    mlo = MS[np.argmax(good)]
    print(f"per-mass form within 10 % of exact kinematics for m_chi >= {mlo/1e6:.0f} MeV")
    for m in [20e6, 30e6, 50e6, 100e6, 300e6, 1e9]:
        ex, ap, e10, a10 = totals(m)
        print(f"  m = {m/1e6:6.0f} MeV: exact {ex:.3e}, factorized {ap:.3e} /kg/yr, ratio {ap/ex:.3f}; "
              f"at 10 eV ratio {a10/e10 if e10 > 0 else float('nan'):.3f}")
    # power laws of the factorized rate
    for (m1, m2) in [(20e6, 40e6), (400e6, 800e6), (1.5e9, 3e9)]:
        a1, a2 = totals(m1)[1], totals(m2)[1]
        print(f"  local power of the factorized rate between {m1/1e6:.0f} and {m2/1e6:.0f} MeV: "
              f"{np.log(a2/a1)/np.log(m2/m1):.2f}")
    # the kinematic factor of the source: [(1 + sqrt(1 - 2 w/(mu v^2)))/2]^4
    for x in [0.07, 0.29]:
        print(f"  E_N^2 weight at 2 omega/mu v^2 = {x}: {((1 + np.sqrt(1 - x)) / 2)**4:.3f}")
    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.axvspan(mlo / 1e6, MS[-1] / 1e6, color="0.88", lw=0)
    ax.axhline(1.0, color="k", ls="--", lw=1.0, label="exact free-recoil kinematics")
    ax.plot(MS / 1e6, r_tot, color="C3", lw=1.5, label=r"factorized per-mass form, $\omega \geq E_{\mathrm{g}}$")
    ax.plot(MS / 1e6, r_10, color="C3", lw=1.0, ls=":", label=r"same at $\omega = 10$ eV")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(MS[0] / 1e6, MS[-1] / 1e6)
    ax.set_ylim(0.8, 30)
    ax.set_xlabel(r"$m_\chi$ (MeV)")
    ax.set_ylabel("rate ratio")
    ax.legend(fontsize=6.5, frameon=False, loc="upper right")
    fig.tight_layout()
    out = os.path.join(HERE, "..", "..", "tex", "figures", "ch12", "limit12_3c.pdf")
    fig.savefig(out)
    print("wrote", os.path.normpath(out))


if __name__ == "__main__":
    main()
