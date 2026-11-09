"""Fig. 20.3 (fig:20-amm): acoustic-mismatch transmission of the silicon/aluminum interface against the angle of
incidence, for phonons incident from silicon and from aluminum.  Log: fig20_3.log.
Run: python fig20_3.py > fig20_3.log
Media and solver: amm20_3.py (isotropic Voigt media from the App. C.18 constants; welded plane interface;
P-SV 4x4 boundary problem and decoupled SH).  Plotted: total transmitted energy fraction (all modes on the far side)
for incident L (P), SV and SH, and, dotted, the mode-converted part (transmitted SV) for incident L.
Horizontal dash-dot lines: diffuse-mismatch value n_2/(n_1 + n_2).  Vertical ticks: critical angles.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from amm20_3 import SI, AL, t_mode, psv, dmm, averages, crit_angles

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch20")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.75), sharey=True)
th = np.radians(np.linspace(0, 89.95, 1800))
cols = {"P": "C0", "SV": "C3", "SH": "C2"}
labs = {"P": "L", "SV": "SV", "SH": "SH"}
for ax, (a, b), title in zip(axs, ((SI, AL), (AL, SI)), ("(a) incident from Si", "(b) incident from Al")):
    for mode in ("P", "SV", "SH"):
        t = np.array([t_mode(a, b, mode, x) for x in th])
        ax.plot(np.degrees(th), t, color=cols[mode], lw=1.2, label=labs[mode])
    conv = np.array([psv(a, b, "P", x)[3] for x in th])
    ax.plot(np.degrees(th), conv, color=cols["P"], lw=0.9, ls=":", label="L$\\to$SV")
    ax.axhline(dmm(a, b), color="0.35", lw=0.8, ls="-.", label="DMM")
    avg, tbar = averages(a, b)
    print(f"{a.name}->{b.name}: tbar = {tbar:.4f}, DMM = {dmm(a, b):.4f}, <t> P/SV/SH = "
          f"{avg['P']:.4f}/{avg['SV']:.4f}/{avg['SH']:.4f}")
    crit = sorted(set(crit_angles(a, b, "P") + crit_angles(a, b, "SV")))
    for c in crit:
        ax.axvline(np.degrees(c), color="0.75", lw=0.6, zorder=0)
        print(f"  critical angle {np.degrees(c):.2f} deg")
    ax.set_xlim(0, 90)
    ax.set_ylim(0, 1.02)
    ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
    ax.set_xlabel("angle of incidence (deg)")
    ax.set_title(title, fontsize=9)
axs[0].set_ylabel("transmitted energy fraction")
axs[1].legend(loc="upper right", fontsize=7.5, frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig20_3.pdf"))
print("wrote fig20_3.pdf")
