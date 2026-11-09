"""Fig. 1.1: mass range of dark-matter candidates (top) and, for the keV-GeV window, the largest
kinetic energy against solid-state excitation energies (bottom). Output: tex/figures/ch01/fig1_1.pdf.
Every plotted number is sourced below.
  [Lin]  T. Lin, TASI lectures, arXiv:1904.07915, Sect. I.
  [KL]   Y. Kahn and T. Lin, Rep. Prog. Phys. 85, 066901 (2022), arXiv:2108.03239.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

eV = 1.0
keV, MeV, GeV, TeV = 1e3, 1e6, 1e9, 1e12
M_PL = 1.22e19 * GeV                # Planck mass [Lin Eq. (19)]
M_SUN = 1.115e57 * GeV              # solar mass, 1.988e30 kg / (1.783e-27 kg/GeV)

# Top panel: candidate classes (mass in eV).
classes = [
    # ultralight bosonic fields: from ~1e-22 eV [Lin Sect. I B] up to ~keV [Lin Sect. I B, first line]
    ("ultralight bosons", 1e-22 * eV, 1 * keV, "0.55"),
    # light dark matter: keV-10 GeV [Lin Sect. I D]; the book's window is keV-GeV
    ("light dark matter", 1 * keV, 1 * GeV, "C3"),
    # WIMPs: 10 GeV-10 TeV [Lin Sect. I D]
    ("WIMPs", 10 * GeV, 10 * TeV, "0.35"),
    # superheavy fundamental particles: ~100 TeV (unitarity) up to M_Pl [Lin Sects. I C, I D]
    ("superheavy particles", 100 * TeV, M_PL, "0.55"),
    # primordial black holes: open windows 1e-16-1e-14 and 1e-13-1e-11 M_sun; a 10% component up to ~50 M_sun [Lin Sect. I C]
    ("primordial black holes", 1e-16 * M_SUN, 50 * M_SUN, "0.35"),
]

# Bottom panel: excitation energies (eV) [KL].
v_dm = 1e-3                          # typical dark-matter speed in units of c [KL Eq. (2)]
bands = [
    ("superconducting gap", 1e-4, 1e-3),        # O(meV) and below [KL Sect. VI]; lower edge indicative
    ("acoustic phonons", 1e-3, 1e-2),           # ~8 meV scale [KL Eq. (50)]; meV threshold [KL Fig. 5]
    ("optical phonons", 30e-3, 150e-3),         # 30-150 meV [KL Sect. IV B]
    ("semiconductor gap", 0.5, 1.5),            # ~1 eV [KL Table I]; Si 1.1 eV
    ("atomic ionization", 5.0, 20.0),           # ~10 eV [KL Table I]
    ("nuclear-recoil thresholds", 1e2, 1e3),    # few hundred eV in tonne-scale xenon detectors [KL Sect. I]
]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.3, 6.4), gridspec_kw={"height_ratios": [1, 1.5]})

for i, (name, lo, hi, col) in enumerate(classes):
    y = len(classes) - i
    ax1.plot([np.log10(lo), np.log10(hi)], [y, y], lw=7, color=col, solid_capstyle="butt")
    if hi < 1e40:
        ax1.text(np.log10(hi) + 1.5, y, name, va="center", fontsize=8)
    else:
        # above the bar: to its left the label would run across the Planck-mass line
        ax1.text(0.5 * (np.log10(lo) + np.log10(hi)), y + 0.3, name, va="bottom", ha="center", fontsize=8)
ax1.axvline(np.log10(M_PL), color="0.5", ls=":", lw=0.8)
ax1.text(np.log10(M_PL), 0.3, r"$M_{\mathrm{Pl}}$", ha="center", fontsize=8)
ax1.set_xlim(-25, 72)
ax1.set_ylim(0, len(classes) + 1)
ax1.set_yticks([])
ax1.set_xlabel(r"$\log_{10}(m_\chi/\mathrm{eV})$")

m = np.logspace(3, 10, 200)
ax2.loglog(m, 0.5 * m * v_dm**2, color="k", lw=1.4)
ax2.text(3e7, 0.5 * 3e7 * v_dm**2 * 2.2, r"$\frac{1}{2}m_\chi v^2$, $v=10^{-3}$", rotation=26, fontsize=8)
for name, lo, hi in bands:
    ax2.axhspan(lo, hi, color="C0", alpha=0.18, lw=0)
    ax2.text(1.3e3, np.sqrt(lo * hi), name, va="center", fontsize=7.5)
ax2.axvspan(1e3, 1e9, color="C3", alpha=0.06, lw=0)
ax2.set_xlim(1e3, 1e10)
ax2.set_ylim(1e-4, 1e4)
ax2.set_xticks([1e3, 1e6, 1e9])
ax2.set_xticklabels(["1 keV", "1 MeV", "1 GeV"])
ax2.set_xlabel(r"dark-matter mass $m_\chi$")
ax2.set_ylabel(r"energy (eV)")
fig.tight_layout()
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "..", "..", "tex", "figures", "ch01", "fig1_1.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
