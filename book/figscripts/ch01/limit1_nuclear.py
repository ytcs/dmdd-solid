"""Limit box 'Elastic nuclear recoil' (Sect. 1.3): free-recoil response delta(omega - E_R) against a nucleus bound in a
harmonic (Einstein) potential, as a function of E_R/omega_0 for silicon. Output: tex/figures/ch01/limit1_nuclear.pdf.

Model [KL] Y. Kahn and T. Lin, Rep. Prog. Phys. 85, 066901 (2022), arXiv:2108.03239, Sect. IV A:
  single nucleus in V(r) = (1/2) M omega_0^2 r^2, Eq. (80), at zero temperature. The probability of exciting
  n quanta (phonons) after a momentum transfer q is Poisson, Eq. (90):
      |f(n, q)|^2 = exp(-nbar) nbar^n / n!,   nbar = q^2/(2 M omega_0) = E_R/omega_0,   Eq. (91),
  so the deposited energy omega = n omega_0 has mean E_R (exactly) and rms width (E_R omega_0)^(1/2).
  omega_0 = 60 meV, "a typical phonon energy for silicon" [KL, below Eq. (80)].
Free nucleus: omega = q^2/2M = E_R, a delta function [KL Eq. (78); Lin, arXiv:1904.07915, Eqs. (77), (78)].
Panel (b) plots, against nbar, the mean and rms of the deposit among scatterings that excite the lattice (n >= 1):
  <omega | n>=1> = E_R/(1 - e^-nbar),  <omega^2 | n>=1> = omega_0^2 (nbar + nbar^2)/(1 - e^-nbar).
Shading (stated in the caption): free formula holds where the rms width is below a third of E_R, i.e.
  E_R >= 9 omega_0 = 0.54 eV; single- and few-phonon regime E_R <= 3 omega_0, where n <= 3 carries most weight.
"""
import os
import numpy as np
from scipy.stats import poisson
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OMEGA0 = 0.060                     # eV [KL, below Eq. (80)]
X_FREE = 9.0                       # E_R/omega_0 at which rms/E_R = 1/3
X_FEW = 3.0

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.4, 2.9), gridspec_kw={"width_ratios": [1, 1.25]})

# (a) spectra at three values of E_R/omega_0
for nbar, col, off in [(0.5, "C0", -0.02), (5.0, "C2", 0.0), (50.0, "C3", 0.02)]:
    n = np.arange(0, int(nbar + 8 * np.sqrt(nbar) + 6))
    w = poisson.pmf(n, nbar)
    x = n / nbar                   # omega/E_R
    m = n >= 1
    ax1.vlines(x[m] + off, 0, w[m], color=col, lw=1.2)
    ax1.plot(x[m] + off, w[m], "o", color=col, ms=3,
             label=rf"$E_R/\omega_0 = {nbar:g}$")
    if nbar >= 5:
        xs = np.linspace(0, 2.5, 400)
        sig = np.sqrt(1 / nbar)    # rms of omega/E_R
        ax1.plot(xs, np.exp(-(xs - 1)**2 / (2 * sig**2)) / (np.sqrt(2 * np.pi) * sig * nbar), color=col, lw=0.6, ls="--")
    print(f"nbar = {nbar}: P(n=0) = {np.exp(-nbar):.3g}, P(n=1) = {w[1]:.3g}, rms/E_R = {np.sqrt(1 / nbar):.3f}")
ax1.annotate("", xy=(1, 0.62), xytext=(1, 0), arrowprops=dict(arrowstyle="->", color="k", lw=1.2))
ax1.text(0.96, 0.6, r"free, $\delta(\omega - E_R)$", fontsize=7, ha="right")
ax1.set_xlim(0, 2.6)
ax1.set_ylim(0, 0.66)
ax1.set_xlabel(r"$\omega/E_R$")
ax1.set_ylabel(r"probability of $n$ phonons")
ax1.legend(fontsize=6.5, frameon=False, loc="upper right")

# (b) mean and rms of the deposit, given that the lattice is excited, against E_R/omega_0
nb = np.logspace(-2, 3, 500)
p1 = 1 - np.exp(-nb)
mean = 1 / p1                                         # <omega>/E_R
rms = np.sqrt((nb + nb**2) / p1 / nb**2 - mean**2)    # rms of omega/E_R
ax2.axvspan(X_FREE, nb[-1], color="0.88", lw=0)
ax2.axvspan(nb[0], X_FEW, facecolor="none", edgecolor="0.7", hatch="////", lw=0)
ax2.fill_between(nb, np.maximum(mean - rms, 1e-3), mean + rms, color="C3", alpha=0.25, lw=0)
ax2.loglog(nb, mean, "C3", lw=1.4, label="bound: mean deposit")
ax2.loglog(nb, np.ones_like(nb), "k", lw=1.4, label=r"free: $\omega = E_R$")
ax2.loglog(nb, 1 + np.sqrt(1 / nb), "k", lw=0.8, ls="--", label=r"$1 \pm (\omega_0/E_R)^{1/2}$")
ax2.loglog(nb[nb > 1.2], 1 - np.sqrt(1 / nb[nb > 1.2]), "k", lw=0.8, ls="--")
ax2.loglog(nb, 1 / nb, color="0.5", lw=0.8, ls=":", label=r"one phonon, $\omega = \omega_0$")
ax2.set_xlim(nb[0], nb[-1])
ax2.set_ylim(0.05, 100)
ax2.set_xlabel(r"$E_R/\omega_0$")
ax2.set_ylabel(r"$\omega/E_R$")
ax2.text(1.3e-2, 0.07, "few phonons", fontsize=7, color="0.3")
ax2.text(12, 0.07, "free recoil", fontsize=7, color="0.3")
ax2.legend(fontsize=6.5, frameon=False, loc="upper right")
top = ax2.secondary_xaxis("top", functions=(lambda x: x * OMEGA0, lambda e: e / OMEGA0))
top.set_xlabel(r"$E_R$ [eV], silicon", fontsize=8)
top.tick_params(labelsize=7)
print(f"free region E_R >= {X_FREE * OMEGA0:.2f} eV; few-phonon E_R <= {X_FEW * OMEGA0:.2f} eV")
fig.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch01", "limit1_nuclear.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
