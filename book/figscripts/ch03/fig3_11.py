"""Fig. 3.11 (fig:3-wf): one maximally localized sp3 Wannier function of silicon.

Data: fig3_11_w90.npz, written by fig3_11_w90.py (QE 7.6 + wannier90; PBE, SG15 ONCV Si_ONCV_PBE-1.2, 40 Ry,
a = 5.431 A, 8x8x8 coarse grid, 16 bands, 8 Wannier functions from sp3 projections, frozen window up to VBM + 2.5 eV).
(a) w_1(r) on the (1-10) plane through the atom on which it is centred (this plane contains the [111] bond and [001]);
    normalized to one over the 3x3x3-cell box that wannier90 writes; real-valued (wannier90 removes the global phase).
(b) largest |w_1| on spherical shells of width 0.25 A around the Wannier centre, against the distance from the centre.
Printed: spreads, centres, Omega_I / Omega_D / Omega_OD, decay length of the fitted exponential.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch03", "fig3_11.pdf")
A = 5.431
d = np.load(os.path.join(HERE, "fig3_11_w90.npz"))
s, plane, atoms = d["s"], d["plane"], d["atoms"]
print("spreads (A^2):", np.round(d["spreads"], 4), " sum:", d["spreads"].sum())
print("Omega_I, Omega_D, Omega_OD, total (A^2):", d["OmI"], d["OmD"], d["OmOD"], d["OmT"])
print("centres (A):", np.round(d["centres"], 4))
c = d["centres"][0]
bond_mid = np.array([A / 8] * 3)
print("centre 1 distance from atom at 0: %.3f A; from bond midpoint: %.3f A; bond length %.3f A"
      % (np.linalg.norm(c), np.linalg.norm(c - bond_mid), np.sqrt(3) * A / 4))

rmid, wmax = d["rmid"], d["wmax"]
ok = np.isfinite(wmax) & (rmid > 2.0) & (rmid < 5.5)
p = np.polyfit(rmid[ok], np.log(wmax[ok]), 1)
xi = -1 / p[0]
print("exponential fit 2-5.5 A: decay length of |w| = %.2f A (|w|^2: %.2f A)" % (xi, xi / 2))
for r0 in (1.0, 2.0, 3.0, 4.0, 5.0, 6.0):
    i = np.argmin(abs(rmid - r0))
    print(f"  shell max |w| at {rmid[i]:.2f} A: {wmax[i]:.2e} A^-3/2  (rel. to peak {wmax[i]/np.nanmax(wmax):.1e})")

plt.rcParams.update({"font.size": 9})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.6, 3.0), gridspec_kw={"width_ratios": [1.0, 1.05], "wspace": 0.62})
vmax = np.abs(plane).max()
levels = np.linspace(-vmax, vmax, 23)
cf = ax.contourf(s, s, plane.T, levels=levels, cmap="RdBu_r")
ax.contour(s, s, plane.T, levels=[l for l in levels if abs(l) > 1e-9][::2], colors="k", linewidths=0.25)
for (x, y) in atoms:
    ax.plot(x, y, "o", ms=4.5, mfc="0.2", mec="w", mew=0.6)
# bonds between atoms in the plane closer than 2.4 A
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        if np.linalg.norm(atoms[i] - atoms[j]) < 2.4:
            ax.plot(*zip(atoms[i], atoms[j]), color="0.3", lw=0.6)
ax.plot(0, 0, "+", color="k", ms=6, mew=0.8)
ax.set_xlim(s[0], s[-1]); ax.set_ylim(s[0], s[-1]); ax.set_aspect("equal")
ax.set_xlabel(r"along $[\bar{1}10]$ (Å)"); ax.set_ylabel(r"along $[001]$ (Å)")
cb = fig.colorbar(cf, ax=ax, fraction=0.046, pad=0.03)
cb.set_label(r"$w$ (Å$^{-3/2}$)", fontsize=8, labelpad=1); cb.ax.tick_params(labelsize=6.5)
cb.set_ticks(np.round(np.linspace(-0.6, 0.6, 7), 1))
ax.set_title("(a)", loc="left", fontsize=9)

bx.semilogy(rmid, wmax, "o", ms=3, color="C0")
rr = np.linspace(1.5, 6.5, 50)
bx.semilogy(rr, np.exp(np.polyval(p, rr)), "--", color="C1", lw=0.9, label=rf"$\propto e^{{-r/{xi:.2f}\,\mathrm{{Å}}}}$")
bx.axvline(np.sqrt(3) * A / 4, color="0.7", lw=0.6, ls=":")
bx.text(np.sqrt(3) * A / 4 + 0.08, 2 * np.nanmax(wmax), "bond", fontsize=7, color="0.4", va="top")
bx.set_xlabel(r"distance from the Wannier center (Å)")
bx.set_ylabel(r"largest $|w|$ on the shell (Å$^{-3/2}$)")
bx.set_xlim(0, 7.5)
bx.legend(loc="upper right", fontsize=7.5, frameon=False)
bx.set_title("(b)", loc="left", fontsize=9)
plt.rcParams["text.usetex"] = False
fig.savefig(OUT, bbox_inches="tight")
print("wrote", OUT)
