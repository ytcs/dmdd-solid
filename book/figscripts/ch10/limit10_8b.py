"""Limit 10.8b: dark Compton scattering on a free electron at rest (Sect. 10.8).
Panel (a) vector: the non-relativistic seagull rate sigma v = zeta^2 sigma_Th omega'/(m (1 + omega'/m_e)),
  omega' + omega'^2/2m_e = m (eq:10.8-thomson), over the tree-level rate of arXiv:2109.08168 Eq. (2), shown in
  compton10_8.py to be the exact tree-level QED result at every x = m/m_e (Dirac traces, 1e-12).  Leading correction
  1 - (5/8) x^3 (series of compton10_8.py); also the seagull with the exact two-body omega' = m(m + 2m_e)/2(m + m_e).
  Shaded: ratio within 1 % of one (x < 0.32).
Panel (b) axion-like particle: the spin-seagull rate (eq:10.8-alpNR) over the tree-level rate
  e^2 g^2 m^2 (m + 2m_e) / [16 pi m_e^2 (m + m_e)^3] (eq:10.8-alpC, compton10_8.py).
Output: tex/figures/ch10/limit10_8b.pdf.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")
ME_KEV = 510.99895


def main():
    x = np.logspace(-2, np.log10(4), 600)
    F_ex = 0.25 * (x + 2) * (x**2 + 2 * x + 2) / (x + 1)**3
    y = -1 + np.sqrt(1 + 2 * x)
    F_nr = (y / x) / (1 + y)
    y2 = x * (x + 2) / (2 * (x + 1))
    F_nr2 = (y2 / x) / (1 + y2)
    Fa_ex = (x + 2) / (2 * (x + 1)**3)
    Fa_3 = (x + 2)**2 / (2 * (x + 1)**4)
    Fa_nr = F_nr                      # same omega' structure, normalized to e^2 g^2 m^2/(8 pi m_e^4)
    r = F_nr / F_ex
    ok = x[np.where(np.abs(r - 1) > 0.01)[0].min()]
    print(f"seagull within 1% of Eq. (2) for x < {ok:.3f} (m < {ok*ME_KEV:.0f} keV)")

    fig, axs = plt.subplots(1, 2, figsize=(8.0, 3.2))
    ax = axs[0]
    ax.axvspan(x[0], ok, color="0.88", lw=0)
    ax.semilogx(x, np.ones_like(x), color="k", lw=0.9, label="tree level (exact)")
    ax.semilogx(x, r, color="C3", lw=1.3, label="seagull, NR recoil")
    ax.semilogx(x, F_nr2 / F_ex, color="C3", lw=0.8, ls=":", label=r"seagull, exact $\omega_\gamma$")
    ax.semilogx(x, 1 - 5 / 8 * x**3, color="0.3", lw=0.8, ls="--", label=r"$1 - \frac{5}{8}x^3$")
    ax.set_ylim(0.5, 1.08)
    ax.set_xlabel(r"$x = m_\phi/m_e$")
    ax.set_ylabel("ratio to the tree-level rate")
    ax.set_title("(a) vector", fontsize=9)
    ax.legend(fontsize=8, frameon=False, loc="lower left")
    ax = axs[1]
    ax.semilogx(x, np.ones_like(x), color="k", lw=0.9, label="tree level")
    ax.semilogx(x, Fa_nr / Fa_ex, color="C0", lw=1.3, ls="--", label="spin seagull, NR recoil")
    ax.set_ylim(0.2, 1.2)
    ax.set_xlabel(r"$x = m_\phi/m_e$")
    ax.set_title("(b) axion-like particle", fontsize=9)
    ax.legend(fontsize=8, frameon=False, loc="lower left")
    for ax in axs:
        ax.set_xlim(x[0], x[-1])
        sec = ax.secondary_xaxis("top", functions=(lambda u: u * ME_KEV, lambda u: u / ME_KEV))
        sec.set_xlabel(r"$m_\phi$  [keV]", fontsize=8)
        sec.tick_params(labelsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "limit10_8b.pdf"))
    for xv in (0.01, 0.0959, 0.1957, 1.0):
        i = np.argmin(abs(x - xv))
        print(f"x = {x[i]:.4f}: vector NR/exact {r[i]:.4f}; ALP Eq.(3)/exact {Fa_3[i]/Fa_ex[i]:.4f}, NR/exact {Fa_nr[i]/Fa_ex[i]:.4f}")
    print("wrote limit10_8b.pdf")


if __name__ == "__main__":
    main()
