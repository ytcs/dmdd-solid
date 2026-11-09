"""Fig. 5.5 (Sect. 5.6): Franck-Condon progressions of a displaced oscillator for S_HR = 0.5, 2, 5.
Output: tex/figures/ch05/fig5_5.pdf. Prints the weights shown.
Model (Sect. 5.6, Eqs. 5.6-FC and 5.6-bessel): one mode of frequency omega_0, equal in both electronic states, Condon approximation.
  T = 0: w_p = e^{-S} S^p / p! (p >= 0).
  n_B = 0.5 (T = omega_0 / ln 3 = 0.91 omega_0): w_p = e^{-S(2n+1)} ((n+1)/n)^{p/2} I_p(2 S sqrt(n(n+1))), p any integer.
No external data. Colors: #2a6fb0, #c4661f (validated with the dataviz palette validator for the ch05 figures; fig5_3.py);
marker shape (bar vs open circle) gives secondary encoding.
Run: python fig5_5.py   (numpy, scipy, matplotlib)
"""
import os
from math import factorial
import numpy as np
from scipy.special import iv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch05", "fig5_5.pdf")
NB = 0.5
C0, C1, INK = "#2a6fb0", "#c4661f", "#444444"

plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
                     "pdf.fonttype": 42})
fig, axs = plt.subplots(1, 3, figsize=(6.6, 2.4), sharey=True)
for ax, S, lab in zip(axs, (0.5, 2.0, 5.0), "abc"):
    p0 = np.arange(0, 16)
    w0 = np.array([np.exp(-S) * S ** p / factorial(p) for p in p0])
    pT = np.arange(-6, 16)
    z = 2 * S * np.sqrt(NB * (NB + 1))
    wT = np.exp(-S * (2 * NB + 1)) * ((NB + 1) / NB) ** (pT / 2) * iv(pT, z)
    assert abs(sum(np.exp(-S) * S ** p / factorial(p) for p in range(60)) - 1) < 1e-9 and abs(np.sum(np.exp(-S * (2 * NB + 1)) * ((NB + 1) / NB) ** (np.arange(-40, 60) / 2)
                                                   * iv(np.arange(-40, 60), z)) - 1) < 1e-9
    print(f"S = {S}: T=0 weights p=0..6 " + " ".join(f"{x:.4f}" for x in w0[:7]) +
          f" | n_B=0.5: p=-2..3 " + " ".join(f"{x:.4f}" for x in wT[4:10]) + f" | ZPL T=0 {w0[0]:.4f}, n_B=0.5 {wT[6]:.4f}")
    ax.bar(p0, w0, width=0.55, color=C0, label=r"$T = 0$", zorder=2)
    ax.plot(pT, wT, "o", mfc="white", mec=C1, mew=1.2, ms=4.5, label=r"$n_{\mathrm{B}} = 0.5$", zorder=3)
    ax.axvline(S, color=INK, ls="--", lw=0.8, zorder=1)
    ax.set_xlim(-4.6, 12.6 if S < 5 else 13.6)
    ax.set_xticks(range(-4, 14, 2))
    ax.set_title(rf"({lab}) $S_{{\mathrm{{HR}}}} = {S:g}$", fontsize=9)
    ax.set_xlabel(r"net phonons emitted $p$")
    ax.spines[["top", "right"]].set_visible(False)
axs[0].set_ylabel("line weight")
axs[0].set_ylim(0, 0.65)
axs[0].legend(frameon=False, loc="upper right", fontsize=8)
fig.tight_layout(w_pad=0.8)
fig.savefig(OUT)
print("wrote", os.path.normpath(OUT))
