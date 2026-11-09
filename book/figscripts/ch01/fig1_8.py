"""Fig. 1.8 (prints as the first figure of Sect. 1.5): the signal chain from dark matter to sensor, annotated with the
sections and chapters of the book that treat each step. Output: tex/figures/ch01/fig1_8.pdf.
No measured numbers are plotted. The quanta and their energies printed in the boxes are sourced:
  [RK]  K. Ramanathan and N. Kurinsky, Phys. Rev. D 102, 063026 (2020), arXiv:2004.10709, Eq. (1) and Table 1:
        mean energy per electron-hole pair in silicon 3.62-3.66 eV (300 K), 3.70-3.75 eV (5-123 K).
  [KL]  T. Lin and Y. Kahn, Rep. Prog. Phys. 85, 066901 (2022), arXiv:2108.03239, Sect. VII: charge, heat, light readout.
  [HZZ] Y. Hochberg, Y. Zhao, K. Zurek, Phys. Rev. Lett. 116, 011301 (2016), arXiv:1512.04533, Sect. 2: Cooper-pair
        binding 2 Delta below a meV in aluminum.
Chapter numbers follow the book's table of contents (they are repeated with live cross-references in the caption).
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

steps = [
    ("Dark matter in the halo", r"$\rho_\chi$, $f_\chi(\mathbf{v})$, $\eta(v_{\mathrm{min}})$", "Sects. 1.2, 1.3"),
    ("Interaction", r"$\bar\sigma_e$, $F_{\mathrm{DM}}(q)$; absorption couplings", "Sect. 1.4; Chaps. 2, 8"),
    ("Target response", r"rate for each transfer $(q, \omega)$", "Chaps. 3-7"),
    ("Energy deposit", r"$\omega$ in electron-hole pairs, phonons," "\n" r"quasiparticles, magnons", "Chaps. 4-7"),
    ("Quanta", r"$N_{\mathrm{eh}}$ pairs (3.6-3.75 eV each in Si);" "\n" r"athermal phonons; quasiparticles ($2\Delta_{\mathrm{BCS}} < 1$ meV in Al); photons",
     "Chaps. 18-20"),
    ("Sensor", "charge amplifier, transition-edge sensor," "\n" "kinetic-inductance detector, photon detector", "Chap. 20"),
    ("Events and limit", r"counts in an exposure; $\bar\sigma_e$ limit", "Sect. 1.5; Chap. 21"),
]

fig, ax = plt.subplots(figsize=(5.4, 6.4))
ax.set_xlim(0, 10)
ax.set_ylim(0, len(steps) * 1.3 + 0.2)
ax.axis("off")
h, w, x0 = 0.95, 6.6, 0.2
for i, (title, body, where) in enumerate(steps):
    y = (len(steps) - 1 - i) * 1.3 + 0.3
    shade = "0.93" if i < 4 else "0.98"
    ax.add_patch(FancyBboxPatch((x0, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc=shade, ec="0.3", lw=0.8))
    ax.text(x0 + 0.15, y + h - 0.18, title, fontsize=8.5, weight="bold", va="top")
    ax.text(x0 + 0.15, y + h - 0.47, body, fontsize=7, va="top", linespacing=1.15)
    ax.text(x0 + w + 0.25, y + h / 2, where, fontsize=7.5, va="center", color="0.25")
    if i < len(steps) - 1:
        ax.annotate("", xy=(x0 + w / 2, y - 0.33), xytext=(x0 + w / 2, y - 0.02),
                    arrowprops=dict(arrowstyle="-|>", color="0.3", lw=0.9))
# theory / measurement bracket
ax.annotate("", xy=(9.75, 4.15), xytext=(9.75, 9.25), arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
ax.text(9.85, 6.7, "theory", rotation=90, fontsize=7, va="center", color="0.4")
ax.annotate("", xy=(9.75, 0.3), xytext=(9.75, 3.95), arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
ax.text(9.85, 2.1, "detector: calibrated and measured", rotation=90, fontsize=7, va="center", color="0.4")
fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch01", "fig1_8.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
