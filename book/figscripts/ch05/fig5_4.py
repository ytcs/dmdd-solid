"""Fig. 5.4 (Sect. 5.5): phonon dispersion of GaAs with the LO-TO splitting.
Output: tex/figures/ch05/fig5_4.pdf. Prints every computed number quoted in Sect. 5.5 about the dispersion.
Data (gaas_cache/, written by fig5_4_matdyn.py from the force constants of tab5_1_gaas_qe.sh: QE 7.6 DFPT, PBE, SG15 ONCV
Ga (13 e, 3d included) and As (5 e), 60 Ry, Gamma-centered 8^3 k grid, 4^3 Q grid, measured a = 5.638 A [Csonka et al.
2009, Table II, as Table E.1], natural masses; acoustic sum rule 'crystal' on force constants and Born charges):
  disp_comp.freq : dipole term with the computed eps_inf and Z* of the densest k grid (28^3: eps_inf = 13.70, Z* = 2.094;
                   gaas_q2r_epsZ.py), sum rule imposed.
Diamond in panel (b): LO at Gamma from eq:5.5-LOTO with the computed TO and Z* but the measured eps_inf = 10.88
  [Lockwood et al. 2005, as quoted by Knapen et al., arXiv:1712.06598]; exact for the analytic part of the calculation.
Constants: a = 5.638 A, Omega = a^3/4; mu_red from 69.723 u and 74.9216 u; e^2 = 4 pi alpha; hbar c = 1973.27 eV A.
Measured Gamma TO 8.13 THz, LO 8.79 THz [Strauch and Dorner, JPCM 2, 1457 (1990), as tabulated in Dehghani et al.,
arXiv:2506.16977, Table I].
Colors validated with the dataviz palette validator (light surface) in fig5_3.py: #2a6fb0, #c4661f.
Run: python fig5_4.py   (numpy, matplotlib)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "gaas_cache")
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch05", "fig5_4.pdf")
CM1 = 1.23984198e-1          # meV per cm^-1
THZ = 4.135667696            # meV per THz
TO_M, LO_M = 8.13 * THZ, 8.79 * THZ
N1, N2, N3 = 61, 81, 41


def read(fn):
    txt = open(os.path.join(C, fn)).read()
    head, body = txt.split("/", 1)
    nbnd = int(head.split("nbnd=")[1].split(",")[0])
    nks = int(head.split("nks=")[1].split()[0].rstrip(","))
    v = np.array(body.split(), float).reshape(nks, -1)       # q columns (version dependent), then nbnd frequencies
    return v[:, -nbnd:] * CM1


fc = read("disp_comp.freq")
G0, X, L = np.sort(fc[0]), np.sort(fc[N1 - 1]), np.sort(fc[-1])
print("Gamma (approached along [001]): " + " ".join("%.2f" % x for x in G0) + " meV")
print(f"TO {G0[3]:.2f} meV, LO {G0[5]:.2f} meV, splitting {G0[5]-G0[3]:.2f} meV; TO/LO {G0[3]/THZ:.2f}/{G0[5]/THZ:.2f} THz")
print("X: " + " ".join("%.2f" % x for x in X) + " meV;  L: " + " ".join("%.2f" % x for x in L) + " meV")
print("Gamma end of Sigma line: " + " ".join("%.2f" % x for x in np.sort(fc[N1 + N2 - 1]))
      + " ; Gamma start of Lambda: " + " ".join("%.2f" % x for x in np.sort(fc[N1 + N2])))
print(f"measured TO {TO_M:.2f}, LO {LO_M:.2f}, splitting {LO_M-TO_M:.2f} meV")
print(f"computed TO vs measured {100*(G0[3]/TO_M-1):+.1f} %, LO {100*(G0[5]/LO_M-1):+.1f} %")
srt = np.sort(fc, axis=1)
print(f"optical band {srt[:,3].min():.2f}-{srt.max():.2f} meV; acoustic max {srt[:,2].max():.2f} meV;"
      f" gap {srt[:,3].min()-srt[:,2].max():.2f} meV")
U, HBARC, E2 = 931.49410242e6, 1973.269804, 4 * np.pi / 137.035999084
Om = 5.638 ** 3 / 4 / HBARC ** 3
mu = 69.723 * 74.9216 / (69.723 + 74.9216) * U
import json
_d = json.load(open(os.path.join(C, "epsZ.json")))
_k = max(_d, key=int)                      # densest k grid: the values in the force-constant file (gaas_q2r_epsZ.py)
Zs, eps_c, eps_m = (_d[_k]["Z_Ga"] - _d[_k]["Z_As"]) / 2, _d[_k]["eps"], 10.88
print(f"dipole term from k {_k}^3: eps_inf = {eps_c:.3f}, Z* (sum rule) = {Zs:.4f}")
wt = G0[3] * 1e-3
for ep, lab in ((eps_c, "computed eps_inf (check of matdyn)"), (eps_m, "measured eps_inf")):
    wl = np.sqrt(wt ** 2 + E2 * Zs ** 2 / (Om * ep * mu)) * 1e3
    print(f"eq:5.5-LOTO with computed TO, Z* = {Zs:.3f}, {lab} {ep:.2f}: LO {wl:.2f} meV, splitting {wl-G0[3]:.2f} meV")
LO_EPSM = np.sqrt(wt ** 2 + E2 * Zs ** 2 / (Om * eps_m * mu)) * 1e3
# LO at small Q along [001] and [111]: drop from Gamma
for k, lab in ((N1 // 10, "[001] Q=0.1"), (N1 // 4, "[001] Q=0.25")):
    print(f"LO along {lab}: {np.sort(fc[k])[5]:.2f} meV")

plt.rcParams.update({"font.size": 8, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
                     "font.family": "serif", "mathtext.fontset": "cm"})
BLUE, ORANGE = "#2a6fb0", "#c4661f"
fig = plt.figure(figsize=(6.3, 3.0))
ax = fig.add_axes([0.08, 0.13, 0.58, 0.74])
az = fig.add_axes([0.73, 0.13, 0.25, 0.74])
ls = np.sqrt(2); lL = np.sqrt(3) / 2
xd = np.linspace(0, 1, N1); xs = 1 + np.linspace(0, ls, N2); xl = 1 + ls + np.linspace(0, lL, N3)
segs = ((xd, slice(0, N1)), (xs, slice(N1, N1 + N2)), (xl, slice(N1 + N2, N1 + N2 + N3)))
for x, sl in segs:
    ax.plot(x, fc[sl], color=BLUE, lw=1.0)
ticks = [0, 1, 1 + ls / 4, 1 + ls, 1 + ls + lL]
ax.set_xticks(ticks); ax.set_xticklabels([r"$\Gamma$", r"X$\,|\,$X$'$", "K", r"$\Gamma$", "L"])
for t in ticks[1:-1]:
    ax.axvline(t, color="0.85", lw=0.5, zorder=0)
ax.set_xlim(0, ticks[-1]); ax.set_ylim(0, 40)
mk = dict(marker="o", ms=4, mfc="white", mec="black", mew=0.8, ls="none", zorder=5)
ax.plot([0, 0, 1 + ls, 1 + ls], [TO_M, LO_M, TO_M, LO_M], **mk)
ax.set_ylabel(r"$\omega_{\mathbf{Q}\nu}$ (meV)")
ax.text(0.035, 0.97, "(a)", transform=ax.transAxes, va="top")
# (b) optical branches near Gamma: [001] to the left (negative axis), [111] to the right, Q in units of 2pi/a
qd = np.linspace(0, 1, N1); ql = np.linspace(0, 0.5, N3) * np.sqrt(3)
az.plot(-qd, fc[0:N1, 3:], color=BLUE, lw=1.0)
az.plot(ql, fc[N1 + N2:, 3:], color=BLUE, lw=1.0)
az.plot([0, 0], [TO_M, LO_M], **mk)
dm = dict(marker="D", ms=4, mfc=ORANGE, mec=ORANGE, ls="none", zorder=6)
az.plot([0], [LO_EPSM], **dm)
az.axvline(0, color="0.85", lw=0.5, zorder=0)
az.set_xlim(-0.35, 0.35); az.set_ylim(31, 38.5)
az.set_xticks([-0.3, 0, 0.3]); az.set_xticklabels([r"$0.3$", r"$\Gamma$", r"$0.3$"])
az.set_xlabel(r"$\leftarrow[001]\quad |\mathbf{Q}|\,(2\pi/a)\quad[111]\rightarrow$", fontsize=7)
az.text(0.04, 0.97, "(b)", transform=az.transAxes, va="top")
ax.plot([], [], color=BLUE, lw=1.0, label=r"PBE (DFPT)")
ax.plot([], [], **dm, label=r"PBE LO with measured $\varepsilon_\infty$")
ax.plot([], [], **mk, label=r"measured TO, LO at $\Gamma$")
fig.legend(*ax.get_legend_handles_labels(), loc="upper center", ncol=3, frameon=False, fontsize=6.8,
           bbox_to_anchor=(0.53, 1.0), handlelength=2.0, columnspacing=1.4)
fig.savefig(OUT)
print("wrote", os.path.abspath(OUT))
