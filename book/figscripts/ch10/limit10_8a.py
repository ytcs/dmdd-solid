"""Limit 10.8a: pair absorption as single absorption at (q -> 0, omega = 2 m_phi) against the halo average over the
pair's kinetic energy, for a target line of half-width gamma (model target).

Formula (Sect. 10.8, eq:10.8-contact): S(q, omega) evaluated at q -> 0, omega = 2 m_phi.
Fuller result (eq:10.8-pair): < S(p + pbar, 2 m_phi + K) > over the two laboratory velocities, K = m_phi (v^2 + vbar^2)/2;
  the q-dependence is dropped (q a < 1e-4 for electronic transitions, pair10_8.log), so only the spread of K matters.
Model response: one Lorentzian line, S ∝ (gamma/pi) / ((omega - DeltaE)^2 + gamma^2), detuning delta = DeltaE - 2 m_phi.
Controlling parameter: gamma / Kbar, Kbar = m_phi <v^2> = 1.60e-6 m_phi (lab-frame standard halo of Sect. 1.2,
  v0 = 238, v_esc = 544, v_E = 250.5 km/s; Monte Carlo with 2e6 velocity pairs, pair10_8.halo_samples).
Plotted: the peak of the fuller line shape over the peak of the formula (both maximized over delta), and the ratio at
  delta = 0; asymptotes 1 - Var(K)/gamma^2 (gamma >> Kbar) and pi gamma max p_K (gamma << Kbar, the discrete-line limit
  of arXiv:2507.14287 Eqs. (5)-(8)).  Shaded: peak ratio within 10 % of one.
Output: tex/figures/ch10/limit10_8a.pdf; log limit10_8a.log.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pair10_8 as P

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")


def main():
    mo = P.moments()
    s = mo["s"]
    t = s / s.mean()                      # K / Kbar
    var = t.var()
    hist, edges = np.histogram(t, bins=400, range=(0, 5), density=True)
    tc = 0.5 * (edges[1:] + edges[:-1])
    pmax = hist.max()
    print(f"Kbar = <s> m = {s.mean():.4e} m; Var(K)/Kbar^2 = {var:.4f}; max p(K) Kbar = {pmax:.4f} at K = {tc[np.argmax(hist)]:.3f} Kbar")
    gs = np.logspace(-2, 3, 61)
    peak, center = [], []
    w = hist * (tc[1] - tc[0])
    for g in gs:
        dl = np.linspace(-10 * g - 2, 10 * g + 6, 4001) if g > 0.05 else np.linspace(-1, 6, 14001)
        full = np.array([(g / np.pi * w / ((d - tc)**2 + g**2)).sum() for d in dl])
        peak.append(full.max() / (1 / (np.pi * g)))
        center.append((g / np.pi * w / (tc**2 + g**2)).sum() / (1 / (np.pi * g)))
    peak, center = np.array(peak), np.array(center)
    for g, p_, c_ in zip(gs[::6], peak[::6], center[::6]):
        print(f"gamma/Kbar = {g:9.3f}: peak ratio {p_:.4f}, ratio at delta = 0 {c_:.4f}; 1 - Var/g^2 = {1-var/g**2:.4f}; pi g pmax = {np.pi*g*pmax:.4f}")
    ok = gs[np.where(np.abs(peak - 1) <= 0.1)[0].min()]
    print(f"peak ratio within 10% of one for gamma >= {ok:.2f} Kbar")
    okc = gs[np.where(np.abs(center - 1) <= 0.1)[0].min()]
    print(f"ratio at delta = 0 within 10% of one for gamma >= {okc:.2f} Kbar")
    m = 1.0
    print(f"at m_phi = 1 eV: Kbar = {s.mean()*m*1e6:.2f} micro-eV; 10% boundary gamma = {ok*s.mean()*m*1e6:.2f} micro-eV")

    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    ax.axvspan(ok, gs[-1], color="0.88", lw=0)
    ax.semilogx(gs, peak, color="C3", lw=1.3, label="halo average, peak")
    ax.semilogx(gs, center, color="C3", lw=0.9, ls="--", label=r"halo average, $2m_\phi = \Delta E$")
    ax.axhline(1, color="k", lw=0.9, label=r"single absorption at $\omega = 2m_\phi$")
    gg = gs[gs > 1.5]
    ax.semilogx(gg, 1 - var / gg**2, color="0.3", lw=0.8, ls=":", label=r"$1 - \mathrm{Var}(K)/\gamma^2$")
    g2 = gs[gs < 0.5]
    ax.semilogx(g2, np.pi * g2 * pmax, color="0.3", lw=0.8, ls="-.", label=r"$\pi\gamma\,\max p_K$")
    ax.set_xlabel(r"line half-width $\gamma/\bar K$")
    ax.set_ylabel("peak rate / single-absorption formula")
    ax.set_ylim(0, 1.12)
    ax.set_xlim(gs[0], gs[-1])
    ax.legend(fontsize=6.5, frameon=False, loc="lower right")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "limit10_8a.pdf"))
    print("wrote limit10_8a.pdf")


if __name__ == "__main__":
    main()
