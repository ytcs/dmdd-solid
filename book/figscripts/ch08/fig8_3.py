"""Fig. 8.3 (fig:8-chain, Sect. 8.7): the chain from the final-state-resolved response S_ab(q, omega; Lambda) to the quanta a
sensor counts, annotated with the chapters of Parts II and III that treat each step. Output: tex/figures/ch08/fig8_3.pdf.
Schematic: no measured numbers are plotted. The final-state classes are those of Sect. 8.7 and lie in the sectors of
Sect. 8.6 (P_ad, P_0, P_+). Chapter numbers follow the book's table of contents; the caption repeats them with live
cross-references.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(6.0, 7.0))   # narrower: at 0.92 linewidth the smallest text prints at about 6 pt
ax.set_xlim(0, 12)
ax.set_ylim(0, 14.2)
ax.axis("off")


def box(x, y, w, h, title, body="", where="", shade="0.95", fs=7.0):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08", fc=shade, ec="0.3", lw=0.8))
    ax.text(x + w / 2, y + h - 0.15, title, fontsize=fs + 0.8, weight="bold", ha="center", va="top")
    if body:
        ax.text(x + w / 2, y + h - 0.52, body, fontsize=fs, ha="center", va="top", linespacing=1.5)
    if where:
        ax.text(x + w / 2, y + 0.1, where, fontsize=fs - 0.2, ha="center", va="bottom", color="0.3", style="italic")


def arrow(x1, y1, x2, y2, label=None, lx=0.0, ly=0.0):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", color="0.3", lw=0.9))
    if label:
        ax.text((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, label, fontsize=6.5, color="0.25", ha="left", va="center")


# 1. dark matter side and response
box(0.3, 12.4, 5.4, 1.7, "Dark matter", r"$\mathfrak{D}_{ab}(\mathbf{q},\mathbf{v})$ at each $(\mathbf{q},\mathbf{v})$;"
    "\n" r"$g^\phi_a$ for absorption", "Sects. 8.1, 8.2")
box(6.3, 12.4, 5.4, 1.7, "Resolved response", r"$S_{ab}(\mathbf{q},\omega;\Lambda)$, one matrix per class $\Lambda$;"
    "\n" r"summed over $\Lambda$ it is $S_{ab}(\mathbf{q},\omega)$", "Sects. 8.6, 8.7; Chaps. 10-16")
box(1.3, 9.75, 9.4, 2.3, r"Rate into each class $\Lambda$",
    r"$\dfrac{\rho_\chi}{m_\chi\rho_T}\int\!\mathrm{d}^3v\,f_\chi(\mathbf{v})\int\!\dfrac{\mathrm{d}^3q}{(2\pi)^3}\,\sum_{a,b}"
    r"\mathfrak{D}_{ab}\,S_{ab}(\mathbf{q},\omega_{\mathbf{q}};\Lambda)$",
    r"Sect. 8.7. Prompt classes: after dressing ($\sim 1/\delta_{\mathrm{F}}$), before relaxation ($\sim 1/\mathit{\Gamma}$)", shade="0.97")
# second body line set on its own: the display fractions are taller than one text line
ax.text(6.0, 10.85, r"$\mathbf{q}$, $\mathbf{v}$ and the operator rows stay inside the sum over $\Lambda$", fontsize=7.0,
        ha="center", va="top")
arrow(3.0, 12.4, 4.0, 12.05)
arrow(9.0, 12.4, 8.0, 12.05)

# 2. prompt final-state classes (sectors of Sect. 8.6)
y2, h2 = 6.6, 2.55
cls = [
    (r"Pair, no phonon", r"$c, v, \mathbf{k}$" "\n" r"$E_{\mathrm{e}}, E_{\mathrm{h}}$, valleys" "\n" r"in $\mathcal{P}_0$", "Chap. 10"),
    (r"Pair + phonons", r"$c, v, \mathbf{k}$;" "\n" r"$\mathbf{Q}\nu$, $\omega_{\mathbf{Q}\nu}$" "\n" r"in $\mathcal{P}_+$", "Chaps. 12, 13"),
    (r"Core hole", "shell; Auger" "\n" "electron" "\n" r"in $\mathcal{P}_0$", "Sect. 10.6"),
    (r"Recoil, phonons", r"$E_R$, direction;" "\n" r"phonon content" "\n" r"in $\mathcal{P}_{\mathrm{ad}}$", "Chap. 11"),
    (r"Spins, pairs", "magnons," "\n" "quasiparticles", "Chaps. 14, 15"),
]
wcl, gap = 2.15, 0.21
for i, (t, b, wh) in enumerate(cls):
    x = 0.3 + i * (wcl + gap)
    box(x, y2, wcl, h2, t, b, wh, shade="0.93", fs=6.6)
    ax.annotate("", xy=(x + wcl / 2, y2 + h2), xytext=(6.0, 9.75),
                arrowprops=dict(arrowstyle="-|>", color="0.45", lw=0.7))

# 3. cascades
y3, h3 = 3.75, 1.9
box(0.3, y3, 5.4, h3, "Carrier cascade", r"impact ionization, phonon emission;" "\n"
    r"seeded by $\Lambda$: $P_{\mathrm{casc}}(N_{\mathrm{eh}}|\Lambda)$", "Chap. 18", shade="0.98")
box(6.3, y3, 5.4, h3, "Recoil hand-over", "heat, defects and charge" "\n" r"from a nuclear recoil", "Chap. 19", shade="0.98")
for i in range(3):
    x = 0.3 + i * (wcl + gap) + wcl / 2
    arrow(x, y2, min(x, 4.9), y3 + h3)
arrow(0.3 + 3 * (wcl + gap) + wcl / 2, y2, 8.0, y3 + h3)
arrow(0.3 + 4 * (wcl + gap) + wcl / 2, y2, 10.6, y3 + h3)

# 4. quanta, readout, limits
box(0.3, 2.15, 11.4, 1.2, "Quanta", r"$N_{\mathrm{eh}}$ pairs; phonon energy; energy stored in defects $E_{\mathrm{st}}$;"
    " escaping quanta; quasiparticles", "Sect. 19.5 (energy balance)", shade="0.98")
arrow(3.0, y3, 3.0, 3.35)
arrow(9.0, y3, 9.0, 3.35)
box(0.3, 0.03, 5.4, 1.82, "Readout", "charge drift, phonon and" "\n" "quasiparticle sensors", "Chap. 20", shade="0.98")
box(6.3, 0.03, 5.4, 1.82, "Counts and limits", "rate assembly, nuisance parameters," "\n" "exclusion limits", "Chap. 21", shade="0.98")
arrow(3.0, 2.15, 3.0, 1.85)
arrow(5.7, 0.94, 6.3, 0.94)

fig.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch08", "fig8_3.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
