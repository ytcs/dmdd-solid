"""Fig. 11.7 (tex/figures/ch11/fig11_7.pdf), two panels; numbers in fig11_7.log.
(a) The hexadecapole of the silicon loss function, L_4/L_0 (cubic-harmonic components, eq:11.7-rate), against q at omega = 3, 5 and
    8 eV (1-eV bins), empirical pseudopotential model, random-phase head, no local fields (elf11_7.py, NK = 12, ten directions,
    least-squares fit with l = 0, 4, 6, 8); GaAs at 5 eV dashed.  Thin gray: L_6/L_0 of silicon at 5 eV.
(b) Sapphire: rate for a wind at angle theta to the c axis, divided by the rate averaged over all wind directions (the l = 0 term),
    m_chi = 10 MeV, heavy mediator, nucleon coupling, incoherent response with the site tensors of Stratman and Lin (sap11_7.py):
    one phonon above 1 meV and above 80 meV, all phonon numbers above 300 meV.  Bar: the range of theta swept in one sidereal day by
    a c axis along the vertical at 45 deg N (2.5 to 87.5 deg, eq:1.2-angle).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import aniso11 as AN  # noqa: E402
import lat11_7 as L  # noqa: E402
import sap11_7 as SP  # noqa: E402

fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.9))
ax = axs[0]
z = np.load(os.path.join(HERE, "elf11_7_Si_NK12.npz"))
c, res = AN.fit_cubic(z["DIRS"], z["L"])
Q = z["Q"]
for w, col in ((3.0, "C0"), (5.0, "C3"), (8.0, "C2")):
    ib = int(np.argmin(np.abs(z["BIN"] - w)))
    ax.plot(Q, c[4][:, ib] / c[0][:, ib], "o-", ms=2.5, color=col, lw=1.2, label=r"Si, %g eV" % w)
    print("Si L4/L0 at %g eV:" % w, np.round(c[4][:, ib] / c[0][:, ib], 3))
ib5 = int(np.argmin(np.abs(z["BIN"] - 5.0)))
ax.plot(Q, c[6][:, ib5] / c[0][:, ib5], color="0.6", lw=0.8, label=r"Si, 5 eV, $L_6/L_0$")
gpath = os.path.join(HERE, "elf11_7_GaAs_NK12.npz")
if os.path.exists(gpath):
    zg = np.load(gpath)
    cg, rg = AN.fit_cubic(zg["DIRS"], zg["L"])
    ax.plot(zg["Q"], cg[4][:, ib5] / cg[0][:, ib5], "s--", ms=2.5, color="C3", lw=1.0, label=r"GaAs, 5 eV")
    for w in (3.0, 5.0, 8.0):
        ib = int(np.argmin(np.abs(zg["BIN"] - w)))
        print("GaAs L4/L0 at %g eV:" % w, np.round(cg[4][:, ib] / cg[0][:, ib], 3))
ax.axhline(0, color="k", lw=0.5)
ax.set_xlabel(r"$q/q_0$")
ax.set_ylabel(r"$L_4/L_0$")
ax.set_xlim(0.35, 2.85)
ax.set_ylim(-0.2, 0.36)
ax.legend(fontsize=6.3, frameon=False, loc="upper right", ncol=2, handlelength=1.6, columnspacing=1.0)
ax.text(0.03, 0.96, "(a)", transform=ax.transAxes, ha="left", va="top")

ax = axs[1]
sap = L.Incoherent("darkelf_Al2O3_pDoS_anisotropic.dat", L.SAPPHIRE)
th = np.radians(np.linspace(0, 90, 46))
vh = np.stack([np.sin(th), 0 * th, np.cos(th)], axis=1)
for (single, wth, lab, col) in ((True, 1e-3, r"one phonon, $\omega > 1$ meV", "C0"),
                                (True, 80e-3, r"one phonon, $\omega > 80$ meV", "C3"),
                                (False, 300e-3, r"all, $\omega > 300$ meV", "k")):
    r = SP.rate_curve(sap, 10e6, wth, single=single, vhats=vh)
    iso = r["Rl"][0][0] * AN.ylm_real(0, np.array([0, 0, 1.0]))[0]
    y = r["R"] / iso
    ax.plot(np.degrees(th), y, color=col, lw=1.3, label=lab)
    print("%-30s R(theta)/R_iso at 0, 54.7, 90 deg: %.4f %.4f %.4f" % (lab, y[0], np.interp(54.74, np.degrees(th), y), y[-1]))
ax.axhline(1, color="k", lw=0.5)
yl = ax.get_ylim()
ax.plot([2.5, 87.5], [yl[0] + 0.04 * (yl[1] - yl[0])] * 2, color="0.5", lw=3, solid_capstyle="butt")
ax.text(45, yl[0] + 0.08 * (yl[1] - yl[0]), r"$45^\circ$N, $c$ vertical", ha="center", fontsize=6.5, color="0.4")
ax.set_ylim(yl)
ax.set_xlim(0, 90)
ax.set_xticks([0, 30, 60, 90])
ax.set_xlabel(r"angle between wind and $c$ axis [deg]")
ax.set_ylabel(r"rate / direction average")
ax.legend(fontsize=6.3, frameon=False, loc="upper left", bbox_to_anchor=(0.07, 1.0))
ax.text(0.03, 0.96, "(b)", transform=ax.transAxes, ha="left", va="top")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "fig11_7.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
