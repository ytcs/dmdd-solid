"""Fig. 6.7 (fig:6-orderings): the two time orderings of phonon-assisted absorption across the indirect gap of silicon,
drawn in the one-electron picture on schematic bands along Gamma-X.

Schematic: the band curves are drawn by hand (cosines and parabolas), not computed. Only the labelled energies are
measured values used in the text: Eg = 1.17 eV (indirect gap, low T), E_dir = 3.4 eV (smallest vertical gap, at Gamma),
k_c = 0.85 (2 pi/a) along <100> (all Sect. 3.3). The phonon arrow is drawn with an exaggerated energy for visibility.
Run: python fig6_7.py   (numpy, matplotlib)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch06", "fig6_7.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

Eg, Edir, kc = 1.17, 3.4, 0.85
k = np.linspace(0, 1, 400)
val = -2.6 * k**2                                    # top valence band, maximum 0 at Gamma
cond = Eg + (Edir - Eg) * ((k - kc) / kc) ** 2 * np.where(k < kc, 1.0, 3.0)   # minimum Eg at k_c, Edir at Gamma
cond2 = 4.6 - 0.8 * k**2                            # a higher band, for the eye

plt.rcParams.update({"font.size": 8, "font.family": "serif", "mathtext.fontset": "cm"})
fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.0), sharey=True)
PH, LT = "#c4661f", "#2a6fb0"


def bands(ax):
    for b in (val, cond, cond2):
        ax.plot(k, b, color="0.55", lw=1.0)
    ax.set_xlim(-0.05, 1.05); ax.set_ylim(-3.0, 5.6)
    ax.set_xticks([0, kc, 1]); ax.set_xticklabels([r"$\Gamma$", r"$\mathbfit{k}_{\mathrm{c}}$", r"X"])
    ax.axhline(0, color="0.85", lw=0.5, zorder=0)
    ax.plot([0], [0], "o", color="k", ms=4)                       # initial: electron at the VBM
    ax.plot([kc], [Eg], "o", color="k", ms=4)                     # final: electron at the CBM


def wavy(ax, x0, y0, x1, y1, color):
    t = np.linspace(0, 1, 200)
    x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
    L = np.hypot(x1 - x0, (y1 - y0) / 8)
    nx, ny = -(y1 - y0) / 8 / L, (x1 - x0) / L
    amp = 0.012
    ax.plot(x + amp * nx * np.sin(2 * np.pi * 9 * t), y + 8 * amp * ny * np.sin(2 * np.pi * 9 * t), color=color, lw=1.0)
    ax.annotate("", xy=(x1, y1), xytext=(x0 + 0.97 * (x1 - x0), y0 + 0.97 * (y1 - y0)),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.0))


# (a) photon first: vertical at Gamma to the conduction state at Edir (virtual), then phonon to k_c
ax = axs[0]; bands(ax)
ax.annotate("", xy=(0, Edir), xytext=(0, 0.05), arrowprops=dict(arrowstyle="-|>", color=LT, lw=1.4))
ax.plot([0], [Edir], "o", mfc="white", mec="k", ms=5)
wavy(ax, 0.02, Edir - 0.05, kc - 0.02, Eg + 0.08, PH)
ax.text(0.03, 1.6, r"photon $\omega$", color=LT, fontsize=7)
ax.text(0.40, 2.75, r"phonon $\mathbfit{Q} \approx \mathbfit{k}_{\mathrm{c}}$", color=PH, fontsize=7)
ax.text(0.03, -2.55, r"denominator $\omega - (\varepsilon_{p\mathbfit{k}} - \varepsilon_{v\mathbfit{k}}) \approx \omega - E_{\mathrm{dir}}$",
        fontsize=7)
ax.text(0.03, 5.05, r"(a) photon first", fontsize=8)
ax.set_ylabel("electron energy (eV)")

# (b) phonon first: scattered from the VBM to a valence state at k_c (virtual), then vertical photon at k_c
ax = axs[1]; bands(ax)
vk = -2.6 * kc**2
wavy(ax, 0.02, -0.06, kc - 0.01, vk + 0.08, PH)
ax.plot([kc], [vk], "o", mfc="white", mec="k", ms=5)
ax.annotate("", xy=(kc, Eg - 0.05), xytext=(kc, vk + 0.07), arrowprops=dict(arrowstyle="-|>", color=LT, lw=1.4))
ax.text(kc - 0.02, -0.2, r"photon $\omega$", color=LT, fontsize=7, ha="right")   # left of the arrow, inside the frame
ax.text(0.10, -1.55, r"phonon", color=PH, fontsize=7)
ax.text(0.03, -2.55, r"denominator $\varepsilon_{v\mathbfit{k}} - \varepsilon_{p,\mathbfit{k}+\mathbfit{Q}} \mp \omega_{\mathbfit{Q}\nu}$",
        fontsize=7)
ax.text(0.03, 5.05, r"(b) phonon first", fontsize=8)

for ax in axs:
    ax.text(kc + 0.03, Eg - 0.15, r"$E_{\mathrm{g}}$", fontsize=7, va="top")
    ax.text(-0.04, Edir + 0.2, r"$E_{\mathrm{dir}}$", fontsize=7)
fig.tight_layout()
fig.savefig(OUT)
print("wrote", OUT)
