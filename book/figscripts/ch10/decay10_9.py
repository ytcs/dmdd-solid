"""In-medium decay of an excited dark-matter state chi_2 -> chi_1 + photon in silicon (Sect. 10.9, Limit 10.9d).
Natural units, Heaviside-Lorentz.

Physics (derived in Sect. 10.9): a magnetic transition dipole mu_M between chi_2 and chi_1 decays in vacuum at
  Gamma_vac = mu_M^2 |Delta_chi|^3 / pi   (mass splitting |Delta_chi| << m_chi; Baryakhtar et al. arXiv:2006.13918
  Eq. (2) quotes the order of magnitude pi |Delta|^3 / Lambda_d^2 for the operator of its Eq. (1), mu_M = 2/Lambda_d).
  In a medium, Gamma = (2 mu_M^2/pi^2) int dq q^4 Im[1/(q^2 - omega^2 eps_T(q, omega))] at omega = |Delta_chi|; where the
  medium is transparent (eps_2 -> 0) the pole at q = omega n_r gives Gamma/Gamma_vac = n_r^3; an electric dipole gives
  n_r (per-photon field |E|^2 proportional to 1/(n_r n_g), |B|^2 = n_r^2 |E|^2, density of states n_r^2 n_g).
  Where eps_2 is not small the q integral is dominated by large q: the decay is a non-radiative transfer to the target,
  the master formula with Delta_chi and a dipole vertex, and needs eps_T(q, omega) at finite q.
Plot: Re(n_r)^3 and Re(n_r) of silicon against |Delta_chi|/omega_p with omega_p = 16.6 eV (valence plasma frequency,
  Sect. 4.3); n_r = sqrt(eps), measured eps (Franta et al. 2017, 300 K, 4 meV - 40 eV; Henke-Gullikson-Davis atomic
  scattering factors above 40 eV, loaded by abs10_7.eps_si).  Hatched: Im n_r > 0.1 Re n_r (absorbing medium; the
  radiative factor loses its meaning there).  Shaded: Re(n_r)^3 within 10 % of one and Im n_r < 0.1 Re n_r.
  Asymptote of a free electron gas: n_r^3 ~ 1 - 3 omega_p^2/(2 omega^2), drawn with the valence omega_p (below the 2p
  edge) and with the all-electron 31.1 eV (Sect. 4.3).
Output: tex/figures/ch10/limit10_9d.pdf and the numbers quoted in Sect. 10.9.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import abs10_7 as A

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")
WP, WP_ALL = 16.6, 31.1


def main():
    w = np.geomspace(0.3, 2000.0, 3000)
    n = np.sqrt(A.eps_si(w))
    m3, e1 = n.real**3, n.real
    absorb = n.imag > 0.1 * n.real
    ok = (np.abs(m3 - 1) < 0.10) & ~absorb
    for x in (0.5, 1.0, 1.11, 2.0, 3.0, 3.4, 5.0, 10.0, 16.6, 20.0, 30.0, 50.0, 60.0, 80.0, 99.0, 110.0, 150.0, 300.0, 1000.0):
        nn = np.sqrt(A.eps_si(np.array([x])))[0]
        print("|Delta| = %7.2f eV (%.2f omega_p): n = %.4f + %.4f i, Re n^3 = %.4f, Im n/Re n = %.3g, free gas 1 - 3wp^2/2w^2 = %.4f (val), %.4f (all)"
              % (x, x / WP, nn.real, nn.imag, nn.real**3, nn.imag / nn.real, 1 - 1.5 * WP**2 / x**2, 1 - 1.5 * WP_ALL**2 / x**2))
    # first energy above which the vacuum formula holds everywhere on the grid
    bad = ~ok & (w > 10)
    wlast = w[bad].max()
    print("vacuum rate within 10%% (and Im n < 0.1 Re n) for all |Delta| above %.1f eV = %.2f omega_p" % (wlast, wlast / WP))
    print("transparent window below the gap: Re n^3 = %.1f at 0.5 eV, %.1f at 1.1 eV" % (np.sqrt(A.eps_si(np.array([0.5])))[0].real**3,
                                                                                         np.sqrt(A.eps_si(np.array([1.1])))[0].real**3))
    print("absorbing (Im n > 0.1 Re n) between %.2f and %.2f eV" % (w[absorb].min(), w[absorb].max()))

    plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
    fig, ax = plt.subplots(figsize=(4.6, 2.9))
    x = w / WP
    ax.fill_between(x, 1e-3, 1e3, where=ok & (w > wlast), color="0.9", lw=0)
    ax.fill_between(x, 1e-3, 1e3, where=absorb, facecolor="none", edgecolor="0.6", hatch="////", lw=0)
    ax.loglog(x, m3, color="C3", lw=1.5, label=r"magnetic dipole, $(\mathrm{Re}\,n_r)^3$")
    ax.loglog(x, e1, color="C0", lw=1.1, ls="--", label=r"electric dipole, $\mathrm{Re}\,n_r$")
    xa = np.geomspace(1.8, 6.0, 50)
    ax.loglog(xa, 1 - 1.5 / xa**2, color="k", lw=0.8, ls=":")
    xb = np.geomspace(7.0, 120, 50)
    ax.loglog(xb, 1 - 1.5 * (WP_ALL / WP)**2 / xb**2, color="k", lw=0.8, ls=":")
    ax.axhline(1, color="0.4", lw=0.8)
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(5e-3, 5e2)
    ax.set_xlabel(r"$|\Delta_\chi|/\omega_p$")
    ax.set_ylabel(r"$\mathit{\Gamma}_{\rm rad}/\mathit{\Gamma}_{\rm vac}$")
    ax.legend(frameon=False, fontsize=7, loc="upper right")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "limit10_9d.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
