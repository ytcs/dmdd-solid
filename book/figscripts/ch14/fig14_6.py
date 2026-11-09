"""Fig. 14.6 (fig:14-spectrum, Sect. 14.6): power spectrum of the axion-like field (and of any signal linear in it) for
records of different length t_int relative to the coherence time t_coh = 1/(m_phi v0^2).
Output tex/figures/ch14/fig14_6.pdf, log fig14_6.log.  Run: python fig14_6.py (seconds).

Model: coh14.py (standard halo of Sect. 1.2, v0 = 238, v_esc = 544, v_E = 250.5 km/s; book eq:14.6-Fphi).  One Monte Carlo
realization of the unit-power field (3000 plane-wave modes, random phases) per panel, periodogram P(x_k)/(2 pi) at the
bins x_k = 2 pi k/t_int (exact transform of each mode), x = (omega - m_phi)/(m_phi v0^2).  Bins drawn as steps of width 2 pi/t_int.  Grey: the mean periodogram of a
record of that length (line shape convolved with the Fejer kernel); black dashed: the long-record line shape F_x(x), the
mean of Foster, Rodd and Safdi's exponential bins (1711.10489 Eq. (24)).  Panels t_int/t_coh = 0.3, 3, 30, 300.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import coh14 as C

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch14")
LOG = open(os.path.join(HERE, "fig14_6.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


rng = np.random.default_rng(14063)
fig, axs = plt.subplots(2, 2, figsize=(5.6, 3.8), sharex=True)
xs = np.linspace(0, 6, 1200)
for ax, T in zip(axs.ravel(), (0.3, 3.0, 30.0, 300.0)):
    dk = 2 * np.pi / T
    k0 = C.X_PEAK / dk
    ks = np.arange(np.floor(-3 / dk), np.ceil(6 / dk) + 1)
    xk = (ks + (k0 - np.round(k0))) * dk          # one bin centred on the line peak
    xk = xk[(xk > -3 - dk) & (xk < 6 + dk)]
    edges = np.concatenate([xk - dk / 2, [xk[-1] + dk / 2]])
    P = C.mc_periodogram(T, xk, 3000, 1, rng)[0]
    mean = np.array([C.fejer_mean(x, T) for x in xk])
    ax.stairs(P, edges, color="C3", lw=0.8, label="one record")
    ax.stairs(mean, edges, color="0.5", lw=1.2, label="mean, this record length")
    ax.plot(xs, C.Fx(xs), color="k", lw=0.8, ls="--", label=r"long-record line $F_\phi$")
    ax.set_title(rf"$t_{{\mathrm{{int}}}} = {T:g}\,t_{{\mathrm{{coh}}}}$", fontsize=8)
    ax.set_xlim(-1, 6)
    top = max(P.max(), mean.max(), C.F_PEAK)
    ax.set_ylim(0, 1.15 * top)
    tot = P.sum() * dk
    out(f"t_int/t_coh = {T:6.1f}: bin width {dk:.4f}; bins in the line ~ {T*C.DW_EQ/(2*np.pi):.2f}; "
        f"sum P dx = {tot:.3f} (mean 1); max P/F_peak = {P.max()/C.F_PEAK:.2f}; mean peak/F_peak = {mean.max()/C.F_PEAK:.3f}")
for ax in axs[1]:
    ax.set_xlabel(r"$(\omega - m_\phi)\,t_{\mathrm{coh}}$")
for ax in axs[:, 0]:
    ax.set_ylabel(r"$P/2\pi$ (units of $t_{\mathrm{coh}}$)")
axs[0, 1].legend(fontsize=6.0, frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig14_6.pdf"))
out(f"line peak at x = {C.X_PEAK:.3f}, F_peak = {C.F_PEAK:.4f}; mean x = {C.X_MEAN:.3f}; equivalent width {C.DW_EQ:.3f}")
out("wrote fig14_6.pdf")
