"""Fig. 11.8 (fig:11-dpabs): dark-photon absorption on optical phonons in GaAs and sapphire.

(a) Loss function L(omega) = Im[-1/eps(omega)] at q -> 0 from the damped factorized dielectric function
    eps = eps_inf prod_nu (wL_nu^2 - w^2 - i w gL_nu)/(wT_nu^2 - w^2 - i w gT_nu)  (Griffin et al., arXiv:1807.10291 v1, Eq. (37)).
    GaAs: measured wT = 33.62, wL = 36.35 meV, eps_inf = 10.88 (Sect. 5.5, WE 5.6); widths gL = gT = 1e-2 x frequency
    (modelling choice of Mitridate et al., arXiv:2308.06314, Sect. III A). The one-branch weight is the splitting value
    (1 - wT^2/wL^2)/eps_inf = 0.01329 (Sect. 11.2), not 1/eps_inf - 1/eps_0 = 0.01439.
    Sapphire: frequencies and 77 K widths of Griffin et al. Table II (e-ray widths adopted from the o-ray, as their table states),
    eps_inf = 3.2, rho_T = 3.98 g/cm^3 (their Table I); polarization average 2/3 ordinary + 1/3 extraordinary (their Eq. (40)).
(b) Reach: zeta for three events in one kilogram-year without background, R = (rho_chi/rho_T) zeta^2 L(m_phi) (Sect. 8.4,
    Gamma_net = zeta^2 m L), rho_chi = 0.3 GeV/cm^3. Single-phonon lines only: no multiphonon sidebands, no electronic part.
Prints the peak values and the line integrals quoted in the text.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
import abs11_8 as A

w = np.linspace(20e-3, 130e-3, 220001)
Lg = A.loss(w, *A.GAAS_ARGS)
Ls = A.loss_saph(w)
Rg = A.events_per_kgyr(Lg, A.RHO_GAAS)
Rs = A.events_per_kgyr(Ls, A.RHO_SAPH)
# The four-parameter factorized model with gL > gT turns Im(-1/eps) slightly negative below the lowest TO line of sapphire
# (ordinary ray below 42.0 meV, extraordinary below 34.1 meV, |L| < 1.2e-4); the sapphire curves are drawn from 45 meV.
SAPH_MIN = 45e-3
ms = w >= SAPH_MIN

print("GaAs: L peak %.3f at %.3f meV; int L = %.4f meV (lossless (pi/2) wL w = %.4f)" %
      (Lg.max(), w[np.argmax(Lg)] * 1e3, np.trapezoid(Lg, w) * 1e3, np.pi / 2 * A.WL * (1 - A.WT**2 / A.WL**2) / A.EPSINF * 1e3))
print("GaAs reach at peak %.2e; sapphire reach at peak %.2e at %.2f meV" %
      (np.sqrt(3 / Rg.max()), np.sqrt(3 / Rs.max()), w[np.argmax(Ls)] * 1e3))
for lo, hi in ((40e-3, 60e-3), (60e-3, 90e-3), (100e-3, 125e-3)):
    m = (w > lo) & (w < hi)
    i = np.argmax(Ls[m])
    print("  sapphire local peak %.2f meV: L = %.3f, zeta = %.2e" % (w[m][i] * 1e3, Ls[m][i], np.sqrt(3 / Rs[m][i])))
print("sapphire int L (2/3 o + 1/3 e) above 45 meV = %.3f meV" % (np.trapezoid(Ls[ms], w[ms]) * 1e3))
# width independence of the line integral (GaAs): gamma = 1e-3 and 1e-2
for g in (1e-3, 1e-2, 3e-2):
    ww = np.linspace(25e-3, 50e-3, 400001)
    L = A.loss(ww, A.WL, A.WT, g * A.WL, g * A.WT, A.EPSINF)
    print("  GaAs gamma/omega = %g: peak %.2f, int over 25-50 meV %.4f meV" % (g, L.max(), np.trapezoid(L, ww) * 1e3))

fig, ax = plt.subplots(1, 2, figsize=(7.0, 2.9))
ax[0].semilogy(w * 1e3, Lg, color="k", lw=1.2, label="GaAs")
ax[0].semilogy(w[ms] * 1e3, Ls[ms], color="tab:blue", lw=1.2, label=r"Al$_2$O$_3$ (avg.)")
ax[0].set_ylim(1e-4, 30)
ax[0].set_xlabel(r"$\omega$ [meV]")
ax[0].set_ylabel(r"$L(\omega) = \mathrm{Im}[-1/\varepsilon(\omega)]$")
ax[0].legend(frameon=False, fontsize=8, loc="upper left")
ax[0].text(0.97, 0.04, "(a)", transform=ax[0].transAxes, ha="right")
ax[1].loglog(w * 1e3, np.sqrt(3 / Rg), color="k", lw=1.2, label="GaAs")
ax[1].loglog(w[ms] * 1e3, np.sqrt(3 / Rs[ms]), color="tab:blue", lw=1.2, label=r"Al$_2$O$_3$")
ax[1].set_xlim(20, 130)
ax[1].set_ylim(5e-18, 1e-14)
ax[1].set_xlabel(r"$m_\phi$ [meV]")
ax[1].set_ylabel(r"$\zeta$ (3 events, kg yr)")
ax[1].set_xticks([20, 30, 50, 100])
ax[1].set_xticklabels(["20", "30", "50", "100"])
ax[1].xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax[1].text(0.03, 0.04, "(b)", transform=ax[1].transAxes)
fig.tight_layout()
fig.savefig("../../tex/figures/ch11/fig11_8.pdf")
print("wrote fig11_8.pdf")
