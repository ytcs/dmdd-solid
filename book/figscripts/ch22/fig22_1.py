"""Fig. 22.1 (fig:22-limits): channels of the book by the factor that limits them (Sect. 22.1).

Three classes, as defined in Sect. 16.9 (sec:16.9-limits) and applied here to every channel:
  theory       no controlled approximation at the values the inputs take; better inputs would not sharpen the rate;
  calculation  the next term has a known form and is computable, but no computation of it exists for the material;
  data         the response formula is in hand and the rate is as uncertain as a measured property of the sample.
Filled marker: the class of the item that dominates the channel's band at its reference point; open marker: a class
that contributes. The reading of each row is taken from the home named in the right column (nuisance tables
tab:10-nuisances ... tab:21-nuisances, the dominant-nuisance table tab:21-dominant of Sect. 21.4, and the open-problem
passages), and the per-row reasons are listed below and in fig22_1.log. The figure carries no numbers.
Run: python fig22_1.py   (writes ../../tex/figures/ch22/fig22_1.pdf and fig22_1.log)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch22", "fig22_1.pdf")

# (group, channel, home, {class: 'F' filled / 'O' open}, reason)
ROWS = [
    ("Electronic", "Electron recoil, Si, 1–10 MeV", "10.10", {"calc": "F"},
     "tab:21-dominant: tabulation spread and electron-hole attraction (finite-q BSE, converged IP table)"),
    ("Electronic", "Velocity couplings; Ge 3d core", "10.4, 10.6", {"calc": "F"},
     "cross term between bounds until current rows with local fields exist; 3d final states between bounds"),
    ("Electronic", "Phonon-assisted window, Si", "13.9", {"calc": "F", "data": "F"},
     "tab:21-dominant: finite-q form factor (calc) and cold absorption data, rate x9 at 0.36 MeV (data)"),
    ("Electronic", "Zero-phonon edge, Ge", "13.9, 17.1", {"calc": "F"},
     "quasiparticle bands with the measured valley order; TA phonons against neutron data"),
    ("Lattice and Migdal", "Nuclear recoil, Si lattice", "11.9", {"calc": "F", "data": "O"},
     "dominant item of tab:21-dominant has basis 'computed': computed against measured phonon frequencies, 0.24 % at 30 MeV;"
     " the measured dispersion contributes (revision, derivation-1 G4)"),
    ("Lattice and Migdal", "Polar phonons, GaAs", "11.9", {"data": "F", "calc": "O"},
     "Z*/eps_inf from the measured splitting; dynamical quadrupoles not computed"),
    ("Lattice and Migdal", "Anharmonic and quantum crystals", "11.5", {"theory": "F", "data": "O"},
     "no real-time method exact at low T; neutron Compton scattering would measure the momentum distribution"),
    ("Lattice and Migdal", "Migdal effect, Si, below 3 MeV", "12.3, 12.4", {"calc": "F", "data": "O"},
     "coherent region 0.75 keV to 2 q_BZ unsized; off-diagonal local fields; no crystal Migdal signal observed"),
    ("Lattice and Migdal", "Migdal ranking of crystals", "17.5, 21.7", {"calc": "F"},
     "L(k, omega) near the gap of every survivor"),
    ("Lattice and Migdal", "Heavy-mediator ranking", "17.6, 21.7", {"data": "F"},
     "computed elastic tensor of TeO2 and of the computed-tensor crystals"),
    ("Spin, superconducting, novel", "Magnons, NiO", "14.1", {"calc": "F"},
     "one-magnon weight beyond linear spin waves; anisotropy near the lightest masses"),
    ("Spin, superconducting, novel", "Superconductor, Al", "15.2", {"data": "F", "calc": "O"},
     "gap and mean free path of the absorber; strong-coupling superconducting form open"),
    ("Spin, superconducting, novel", "Dirac crystal, ZrTe$_5$", "16.1, 16.9", {"data": "F", "calc": "O"},
     "background dielectric tensor x2.8 (we:16-band); electron-hole ladder computable"),
    ("Spin, superconducting, novel", "Strong-coupling Dirac; dense donors", "16.1, 16.5", {"theory": "F"},
     "effective coupling near ten; isolated-donor response wrong at order one near the Mott density"),
    ("Spin, superconducting, novel", "Two-level systems in glass", "16.7", {"data": "F", "calc": "O", "theory": "O"},
     "parameters of a given film known only in combination (data); alpha_ohm from first principles (calc, sec:16.9);"
     " interacting systems outside the model (theory)"),
    ("Measurement chain", "Recoil charge below 352 eV", "19.2", {"calc": "F", "theory": "O"},
     "close-collision kernel not computed; exchange-correlation spread with known sign, unknown size"),
    ("Measurement chain", "Pair statistics, Si charge readout", "18.3, 18.5", {"calc": "F", "data": "O"},
     "first-principles cascade; binding, trapping and capture rates at mK neither measured nor computed"),
    ("Measurement chain", "Pair energies of new crystals", "18.4, 21.7", {"data": "F", "calc": "O"},
     "estimates outside the validated range; germanium at mK from a fit"),
    ("Measurement chain", "Phonon collection, stored energy", "19.5, 20.5", {"data": "F", "calc": "O"},
     "two-bias measurement decides; real-detector kernels from validated transport"),
    ("Measurement chain", "Delayed signals, low-energy excess", "19.6, 20.1", {"calc": "F"},
     "release paths, trap emission cross-sections, relaxable elastic energy not computed"),
    ("Measurement chain", "Internal backgrounds", "21.7", {"data": "F", "calc": "O"},
     "210Pb activity of growable lead; cosmogenic production measured only for Si and Ge"),
    ("Published limits", "Fermionic absorption; boosted recasts", "10.9", {"calc": "F"},
     "transverse current with Dirac-Hartree-Fock states; light-mediator boosted limit below about 3 keV"),
]

COLS = [("theory", "theory"), ("calc", "calculation"), ("data", "data")]

log = ["Fig. 22.1: channels by limiting factor (F = dominant, O = contributing)"]
for g, ch, home, cls, why in ROWS:
    tag = ", ".join(f"{k}:{v}" for k, v in cls.items())
    log.append(f"[{g}] {ch.replace('$', '').replace('_', '')} (Sect. {home}) -> {tag}; {why}")
n = {c: sum(1 for r in ROWS if r[3].get(c) == "F") for c, _ in COLS}
log.append(f"rows {len(ROWS)}; filled markers: theory {n['theory']}, calculation {n['calc']}, data {n['data']}")

plt.rcParams.update({"font.size": 8.0})
fig, ax = plt.subplots(figsize=(6.6, 6.4))
y = 0.0
yt, labels, groups = [], [], []
prev = None
for g, ch, home, cls, why in ROWS:
    if g != prev:
        if prev is not None:
            y += 0.6
        groups.append((y, g))
        y += 1.0
        prev = g
    for j, (c, _) in enumerate(COLS):
        mk = cls.get(c)
        if mk == "F":
            ax.plot(j, -y, "o", ms=8, color="k")
        elif mk == "O":
            ax.plot(j, -y, "o", ms=8, mfc="white", mec="k", mew=1.0)
        else:
            ax.plot(j, -y, ".", ms=2, color="0.75")
    ax.text(-0.45, -y, ch, ha="right", va="center")
    ax.text(2.45, -y, home, ha="left", va="center", color="0.25")
    y += 1.0
for yy, g in groups:
    ax.text(-3.55, -yy, g, ha="left", va="center", fontweight="bold")
for j, (_, name) in enumerate(COLS):
    ax.text(j, 1.0, name, ha="center", va="bottom", fontweight="bold")
ax.text(2.45, 1.0, "section", ha="left", va="bottom", fontweight="bold", color="0.25")
for j in range(3):
    ax.axvline(j, color="0.9", lw=0.6, zorder=0)
ax.set_xlim(-3.6, 3.3)
ax.set_ylim(-y + 0.4, 2.0)
ax.axis("off")
fig.tight_layout()
fig.savefig(OUT)
log.append(f"wrote {os.path.relpath(OUT, HERE)}")
with open(os.path.join(HERE, "fig22_1.log"), "w") as f:
    f.write("\n".join(log) + "\n")
print("\n".join(log))
