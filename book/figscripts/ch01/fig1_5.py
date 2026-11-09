"""Fig. 1.5: kinematically accessible region of momentum transfer q and energy transfer omega for elastic dark
matter (Delta_chi = 0) at the maximum laboratory speed, for m_chi = 0.1, 1, 10 and 100 MeV, with the energy and
momentum scales of silicon overlaid. Output: tex/figures/ch01/fig1_5.pdf. Every plotted number is sourced below.
  [B]      D. Baxter et al., Eur. Phys. J. C 81, 907 (2021), arXiv:2105.00599, Table 1 (v_esc = 544 km/s,
           |v_sun| = 250.5 km/s adopted (250.55 exact), from the LSR and peculiar velocity); v_max = v_esc + |v_sun| = 794.5 km/s (Sect. 1.2).
  [KL]     Y. Kahn and T. Lin, Rep. Prog. Phys. 85, 066901 (2022), arXiv:2108.03239: Eq. (9) (omega_q),
           Fig. 1 (same construction at v = 1e-3); Sect. III A 2, Eq. (50) (sound speeds 3-10 km/s);
           Sect. IV A, text at Eq. (80) (60 meV, a typical phonon energy in silicon; superseded below).
  [NN72]   G. Nilsson and G. Nelin, Phys. Rev. B 6, 3777 (1972): neutron dispersion of Si, optical phonon at Gamma
           15.5 THz = 64 meV (book App. A.1: 15.5 THz = 64.1 meV), the book-wide value.
  [CODATA22] P. J. Mohr et al., Rev. Mod. Phys. 97, 025002 (2025), arXiv:2409.03787; NIST value "lattice parameter
           of silicon", a = 5.431020511e-10 m. Silicon is fcc (diamond structure), so the shortest reciprocal-lattice
           vector is |G_111| = sqrt(3) 2 pi/a = 3.95 keV (hbar c = 1973.27 eV A).
  [R20]    K. Ramanathan and N. Kurinsky, Phys. Rev. D 102, 063026 (2020), Eq. (11): silicon gap 1.1692 eV near
           zero temperature, rounded to 1.17 eV, the low-temperature gap used for all Chapter 1 threshold masses
           (Sect. 1.3; as in Ch. 10 and Sect. 13.1).
  [CODATA] alpha = 1/137.035999084, m_e = 510998.95 eV.
Region: omega <= q v_max - q^2/(2 m_chi) (Sect. 1.3, from omega_q with q parallel to v and v = v_max).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

C_KMS = 299792.458                  # km/s
V_MAX = (544.0 + 250.5) / C_KMS     # [B]; 2.650e-3 in natural units
ALPHA = 1 / 137.035999084           # [CODATA]
M_E = 510998.95                     # eV [CODATA]
Q0 = ALPHA * M_E                    # 3.73 keV, inverse Bohr radius
A_SI = 5.431020511                 # Angstrom, silicon lattice parameter [CODATA22]
HBARC = 1973.2698                   # eV Angstrom [CODATA]
Q_LATT = np.sqrt(3) * 2 * np.pi * HBARC / A_SI   # |G_111| = sqrt(3) 2 pi/a = 3.95 keV [CODATA22]
E_GAP = 1.17                        # eV, low-temperature silicon gap [R20 Eq. (11)]
W_PH = 0.064                        # eV, silicon optical phonon at Gamma [NN72]
C_SOUND = 5.0 / C_KMS               # sound speed 5 km/s, middle of the 3-10 km/s range [KL Eq. (50)]
M_SI = 28.0855 * 0.93149410242e9   # eV, natural Si mean atomic mass, 28.0855 u = 26.16 GeV (as App. D.13, C.6)
MEV = 1e6

masses = [0.1 * MEV, 1 * MEV, 10 * MEV, 100 * MEV]
colors = ["#6baed6", "#4292c6", "#2171b5", "#08306b"]

fig, ax = plt.subplots(figsize=(5.6, 4.2))
for m, col in zip(masses, colors):
    q = np.logspace(-1, np.log10(2 * m * V_MAX), 600)
    w = q * V_MAX - q**2 / (2 * m)
    ax.fill_between(q, 1e-6, w, color="#2171b5", alpha=0.07, lw=0)
    ax.plot(q, w, color=col, lw=1.4)
    # just right of the vertical edge q = 2 m v_max, below the peak, clear of the line omega = q v_max
    # (inside the edge for 100 MeV, which would otherwise run past the frame)
    inside = m > 50 * MEV
    ax.text(2 * m * V_MAX * (0.85 if inside else 1.12), 0.5 * m * V_MAX**2 * (0.12 if inside else 0.5), f"{m / MEV:g} MeV", color=col,
            ha="right" if inside else "left", va="bottom", fontsize=7)

qq = np.logspace(0, 7, 400)
ax.plot(qq, qq * V_MAX, color="0.4", lw=0.7, ls=":")                     # m_chi -> infinity envelope
ax.text(3.0, 3.0 * V_MAX * 2.2, r"$\omega = q v_{\mathrm{max}}$", color="0.35", fontsize=7, rotation=24)
ax.plot(qq, qq**2 / (2 * M_SI), color="0.4", lw=0.9, ls="--")            # free Si nucleus at rest
ax.text(6.0e4, (6.0e4)**2 / (2 * M_SI) * 0.06, "free Si nucleus", color="0.35", fontsize=7, rotation=45)

ax.axhline(E_GAP, color="C3", lw=1.0)
ax.text(1.3, E_GAP * 1.2, "Si band gap", color="C3", fontsize=7)
ax.axhline(W_PH, color="C2", lw=1.0)
ax.text(1.3, W_PH * 1.2, "optical phonons", color="C2", fontsize=7)
qa = np.logspace(0, np.log10(Q_LATT), 100)
ax.plot(qa, C_SOUND * qa, color="C1", lw=1.0)
ax.text(30, C_SOUND * 30 * 2.2, "acoustic phonons", color="C1", fontsize=7, rotation=27)

ax.axvline(Q0, color="0.5", lw=0.7)
ax.text(Q0 * 0.9, 2e-6, r"$q_0 = \alpha m_e$", color="0.3", fontsize=7, rotation=90, va="bottom", ha="right")
ax.axvline(Q_LATT, color="0.5", lw=0.7, ls="-.")
ax.text(Q_LATT * 1.1, 2e-6, r"$|\boldsymbol{G}_{111}|$", color="0.3", fontsize=7, rotation=90, va="bottom", ha="left")

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1, 2e6)
ax.set_ylim(1e-6, 1e3)
ax.set_xlabel(r"momentum transfer $q$ [eV]")
ax.set_ylabel(r"energy transfer $\omega$ [eV]")
fig.tight_layout()

out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch01", "fig1_5.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
