"""Fig. 5.2: phonon dispersion and density of states of silicon, with the Debye model (Sect. 5.2).
Output: tex/figures/ch05/fig5_2.pdf. Prints every computed number quoted in Sect. 5.2 and WE 5.3.
Data: fig5_2_data.npz from fig5_2_data.py (Quantum ESPRESSO 7.6 run of fig5_2_qe.sh: PBE, SG15 ONCV Si_ONCV_PBE-1.2.upf,
ecutwfc 60 Ry, Gamma-centered 12^3 k grid, a = 5.431 A, natural Si mass 28.0855 u; DFPT on a 6^3 Q grid; force constants
by q2r with the acoustic sum rule imposed ('crystal'); matdyn dispersion on the path of fig5_2_qpath.py; DOS on a 48^3
grid by tetrahedra, 0.25 cm^-1 bins).
Measured frequencies (THz), inelastic neutron scattering at room temperature (G. Dolling, in Inelastic Scattering of
Neutrons in Solids and Liquids, Vol. II, IAEA, Vienna 1963, p. 37; G. Nilsson and G. Nelin, Phys. Rev. B 6, 3777
(1972)), as tabulated in S. Y. Savrasov, Phys. Rev. B 54, 16470 (1996), Table I (arXiv cond-mat/9604125):
  Gamma_LTO 15.53; X_TA 4.49, X_LAO 12.32, X_TO 13.90; L_TA 3.43, L_LA 11.35, L_TO 14.68, L_LO 12.60.
Sound speeds from elastic constants: C11 165.6, C12 63.9, C44 79.5 GPa, rho 2.33 g/cm^3 (Martinez et al. 2019,
Table I; App. C.18), drawn as omega = c Q near Gamma along the three lines.
Debye model (modelling choice stated in the caption): atom-density sphere, Q_D = (6 pi^2 n_at/Omega)^(1/3), cbar from
3/cbar^3 = sum_nu <c_nu^-3> with the measured elastic constants (we5_3.py): cbar = 5.886 km/s, omega_D = 55.6 meV.
g_D(omega) = 9 n_at omega^2/omega_D^3 per two-atom cell (n_at = 2), states per meV.
PBE Debye fit: least-squares fit of g = A omega^2 to the computed DOS over FITLO..FITHI meV (modelling choice), giving
cbar_PBE = (3 Omega/(2 pi^2 A))^(1/3) and Theta_D,PBE.
Run: python fig5_2.py   (numpy, matplotlib)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from fig5_2_qpath import segments, SMALL

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch05", "fig5_2.pdf")
CM1 = 1.23984198e-1          # meV per cm^-1
THZ = 4.135667696            # meV per THz
HBAR = 6.582119569e-16       # eV s
KB = 8.617333262e-5          # eV/K
A = 5.431e-10                # m
OMEGA = A ** 3 / 4           # m^3
FITLO, FITHI = 1.0, 6.0      # meV, window of the PBE omega^2 fit
CBAR, WD = 5886.0, 55.61     # m/s, meV (we5_3.py)

d = np.load(os.path.join(HERE, "fig5_2_data.npz"))
q, f, dos = d["q"], d["f"] * CM1, d["dos"]
dl, sg, lm, sm = segments()
n1, n2, n3 = len(dl), len(sg), len(lm)
fd, fs, fl, fsm = f[:n1], f[n1:n1 + n2], f[n1 + n2:n1 + n2 + n3], f[n1 + n2 + n3:]

# --- numbers at the high-symmetry points
meas = {"G_LTO": 15.53, "X_TA": 4.49, "X_LAO": 12.32, "X_TO": 13.90,
        "L_TA": 3.43, "L_LA": 11.35, "L_LO": 12.60, "L_TO": 14.68}
G, X, L = np.sort(fd[0]), np.sort(fd[-1]), np.sort(fl[-1])
calc = {"G_LTO": G[3], "X_TA": X[0], "X_LAO": X[2], "X_TO": X[4],
        "L_TA": L[0], "L_LA": L[2], "L_LO": L[3], "L_TO": L[4]}
print("Gamma (meV):", np.round(G, 2)); print("X (meV):", np.round(X, 2)); print("L (meV):", np.round(L, 2))
dev = []
for k in meas:
    c_thz = calc[k] / THZ
    dev.append((c_thz - meas[k]) / meas[k])
    print(f"{k:6s} PBE {c_thz:6.2f} THz = {calc[k]:6.2f} meV   measured {meas[k]:6.2f} THz = {meas[k]*THZ:6.2f} meV   dev {100*dev[-1]:+5.1f} %")
print(f"max |dev| = {100*np.max(np.abs(dev)):.1f} %, mean |dev| = {100*np.mean(np.abs(dev)):.1f} %")
print("ASR violation at Gamma before correction: %.3f THz" % d["asr_THz"])

# --- PBE sound speeds from the small-Q points (Q = z 2pi/a, slope from the smallest two points' fit)
names = ["[100]", "[110]", "[111]"]
for i, nm in enumerate(names):
    w = np.sort(fsm[i * len(SMALL):(i + 1) * len(SMALL)], axis=1)[:, :3]   # meV
    Q = SMALL * 2 * np.pi / A                                                # 1/m
    c = (w[:2] * 1e-3 / HBAR / Q[:2, None]).mean(axis=0)                      # m/s, Q <= 0.01 (2pi/a)
    print(nm, "PBE c (km/s) TA, TA, LA:", np.round(c / 1e3, 2), " (from Q = 0.005, 0.01 x 2pi/a)")

# --- DOS
w = dos[:, 0] * CM1
g = dos[:, 1] / CM1
g *= 6 / np.trapezoid(g, w)
print("DOS max frequency (meV): %.2f" % w[g > 1e-6].max())
# peaks: local maxima above 5 % of the max
gs = np.convolve(g, np.ones(9) / 9, mode="same")
pk = [i for i in range(5, len(gs) - 5) if gs[i] == gs[i - 5:i + 6].max() and gs[i] > 0.15 * gs.max()]
print("DOS peaks (meV):", np.round(w[pk], 1), " heights (1/meV):", np.round(gs[pk], 3))
for E in (10.0, 20.0, 30.0):
    print(f"fraction of modes below {E:.0f} meV: {np.trapezoid(g[w < E], w[w < E]) / 6:.3f}")
m = (w > FITLO) & (w < FITHI)
Afit = np.sum(g[m] * w[m] ** 2) / np.sum(w[m] ** 4)                       # 1/meV^3 per cell
hb_meV = HBAR * 1e3
# g [1/meV] = 3 Omega omega^2/(2 pi^2 hbar^3 c^3) with omega in meV: c^3 = 3 Omega/(2 pi^2 A hbar_meV^3)
cbar_pbe = (3 * OMEGA / (2 * np.pi ** 2 * Afit * hb_meV ** 3)) ** (1 / 3)
QD = (6 * np.pi ** 2 * 8 / A ** 3) ** (1 / 3)
wd_pbe = hb_meV * cbar_pbe * QD
print(f"PBE omega^2 fit {FITLO}-{FITHI} meV: A = {Afit:.4e} /meV^3, cbar = {cbar_pbe/1e3:.3f} km/s, "
      f"omega_D = {wd_pbe:.2f} meV, Theta_D = {wd_pbe*1e-3/KB:.0f} K")
gD_el = lambda x: np.where(x < WD, 18 * x ** 2 / WD ** 3, 0.0)
print("ratio PBE/elastic omega^2 coefficient: %.3f" % (Afit / (18 / WD ** 3)))
print("measured Debye ratio check: g_D peak value at omega_D = %.3f /meV" % (18 / WD))

# --- figure
plt.rcParams.update({"font.size": 8, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
                     "font.family": "serif", "mathtext.fontset": "cm"})
fig = plt.figure(figsize=(6.3, 3.2))
ax = fig.add_axes([0.08, 0.12, 0.60, 0.76])
axd = fig.add_axes([0.72, 0.12, 0.26, 0.76], sharey=ax)
BLUE, GRAY = "#2a6fb0", "#777777"
# x coordinates: path length in units of 2pi/a
xd = np.linspace(0, 1, n1)
ls = np.sqrt(2)
xs = 1 + np.linspace(0, ls, n2)
lL = np.sqrt(3) / 2
xl = 1 + ls + np.linspace(0, lL, n3)
for x, ff in ((xd, fd), (xs, fs), (xl, fl)):
    ax.plot(x, ff, color=BLUE, lw=1.0)
ticks = [0, 1, 1 + ls / 4, 1 + ls, 1 + ls + lL]
ax.set_xticks(ticks)
ax.set_xticklabels([r"$\Gamma$", r"X$\,|\,$X$'$", "K", r"$\Gamma$", "L"])
for t in ticks[1:-1]:
    ax.axvline(t, color="0.8", lw=0.5, zorder=0)
ax.set_xlim(0, ticks[-1])
# measured points (Gamma at both ends of the Sigma line's Gamma and the path start; X at the X|X' tick; L at the end)
mk = dict(marker="o", ms=4, mfc="white", mec="black", mew=0.8, ls="none", zorder=5)
ax.plot([0, 1 + ls], [15.53 * THZ] * 2, **mk, label="measured")
ax.plot([1.0] * 3, [v * THZ for v in (4.49, 12.32, 13.90)], **mk)
ax.plot([1 + ls + lL] * 4, [v * THZ for v in (3.43, 11.35, 12.60, 14.68)], **mk)
# elastic sound speeds near Gamma, omega = hbar c Q, Q up to 0.25 (2pi/a)
c100 = [8.43, 5.84]; c110 = [9.13, 5.84, 4.67]; c111 = [9.35, 5.09]
zz = np.linspace(0, 0.25, 10)
Qz = zz * 2 * np.pi / A
for c in c100:
    ax.plot(zz, hb_meV * c * 1e3 * Qz, color="black", lw=0.7, ls=":")
for c in c110:
    ax.plot(1 + ls - zz * 1, hb_meV * c * 1e3 * Qz, color="black", lw=0.7, ls=":")
for c in c111:
    ax.plot(1 + ls + zz, hb_meV * c * 1e3 * Qz, color="black", lw=0.7, ls=":")
ax.plot([], [], color=BLUE, lw=1.0, label="PBE (DFPT)")
ax.plot([], [], color="black", lw=0.7, ls=":", label=r"$c_\nu Q$, elastic constants")
ax.set_ylabel(r"$\omega_{\mathbf{Q}\nu}$ (meV)")
ax.set_ylim(0, 70)
ax.text(0.01, 0.97, "(a)", transform=ax.transAxes, va="top")
# DOS panel
axd.plot(g, w, color=BLUE, lw=0.9, label=r"$g_{\mathrm{ph}}$ (PBE)")
xx = np.linspace(0, 70, 701)
axd.plot(gD_el(xx), xx, color="black", lw=0.8, ls="--", label=r"Debye, $\Theta_{\mathrm{D}} = 645$ K (elastic)")
axd.set_xlabel(r"$g_{\mathrm{ph}}(\omega)$ (meV$^{-1}$)")
axd.set_xlim(0, 1.08 * g.max())
plt.setp(axd.get_yticklabels(), visible=False)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = axd.get_legend_handles_labels()
fig.legend(h1 + h2, l1 + l2, loc="upper center", ncol=5, frameon=False, fontsize=6.5, bbox_to_anchor=(0.53, 1.0),
           handlelength=1.8, columnspacing=1.2)
axd.text(0.04, 0.97, "(b)", transform=axd.transAxes, va="top")
fig.savefig(OUT)
print("wrote", os.path.abspath(OUT))
