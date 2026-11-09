"""Fig. 3.12 (fig:3-wint): Wannier-interpolated and directly computed bands of silicon.

Data: fig3_12_w90.npz, written by fig3_11_w90.py (QE 7.6 + wannier90; PBE, SG15 ONCV Si_ONCV_PBE-1.2, 40 Ry,
a = 5.431 A; direct pw.x bands at the same path points).
(a) direct bands (lines) and the bands of the eight sp3 Wannier functions (gauge B of fig3_11_w90.py: outer window up to
    VBM + 12 eV, frozen window up to VBM + 2.5 eV) interpolated from the 8^3 coarse grid (dots); frozen window shaded.
(b) |interpolated - direct| of the four valence bands from four bond-centred Wannier functions (isolated group, no
    disentanglement), coarse grids 4^3, 6^3, 8^3; the error is zero at Gamma, X and L, which lie on all three grids.
Energies relative to the PBE valence-band maximum. Printed: every number quoted in Sect. 3.6 about this figure.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch03", "fig3_12.pdf")
d = np.load(os.path.join(HERE, "fig3_12_w90.npz"))
x, direct = d["x"], d["direct"]
vbm = direct[:, 3].max()
froz = float(d["froz"]) - vbm
labx, labels = d["labx"], [str(l).replace("G", r"$\Gamma$") for l in d["labels"]]
print("VBM from scf (eV) %.4f, from path %.4f" % (float(d["vbm"]), vbm))
cbm = direct[:, 4].min()
kf = d["kfrac"][np.argmin(direct[:, 4])]
CELL = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) / 2.0          # units of a
print("PBE gap along the path: %.3f eV at k =" % (cbm - vbm), np.round(np.linalg.solve(CELL, kf), 4), "(2pi/a)")
seg = {"L-G": slice(0, 41), "G-X": slice(41, 87), "X-W-K": slice(87, 126), "K-G": slice(126, len(x))}

for n in (4, 6, 8):
    ev = np.abs(d[f"val_{n}"] - direct[:, :4]).max(1)
    print(f"valence (4 bond WFs), {n}^3: max {1e3*ev.max():.1f} meV, median {1e3*np.median(ev):.1f} meV;",
          " ".join(f"{k} {1e3*ev[s].max():.0f}" for k, s in seg.items()),
          f"; Omega_W = {float(d[f'v{n}_OmT']):.3f} A^2")
    sh = d[f"hrshell_{n}"]
    print("   |H^W(R)| shells (A: eV):", " ".join(f"{r:.2f}:{h:.1e}" for r, h in sh[:10]))
for n in (4, 6, 8):
    sp = d[f"sp3_{n}"]
    m = direct[:, :8] - vbm < froz - 0.05
    e = np.where(m, np.abs(sp - direct[:, :8]), 0)
    print(f"sp3 (gauge B), {n}^3: max error in the frozen window {1e3*e.max():.0f} meV (valence {1e3*e[:, :4].max():.0f},"
          f" conduction {1e3*e[:, 4:].max():.0f}); Omega_W = {float(d[f'B{n}_OmT']):.3f}, Omega_I = {float(d[f'B{n}_OmI']):.3f} A^2;"
          f" spreads {np.round(d[f'spreads_B{n}'], 3)}")
print("6^3 orientation comparison: Omega_W A %.3f, B %.3f, mixed %.3f A^2; Omega_I A %.3f, B %.3f"
      % (float(d["A6_OmT"]), float(d["B6_OmT"]), float(d["mixed6_OmT"]), float(d["A6_OmI"]), float(d["B6_OmI"])))

plt.rcParams.update({"font.size": 9})
fig, (ax, bx) = plt.subplots(2, 1, figsize=(4.8, 5.0), sharex=True, gridspec_kw={"height_ratios": [2.2, 1], "hspace": 0.08})
ax.axhspan(-15, froz, color="C0", alpha=0.07, lw=0)
for b in range(direct.shape[1]):
    ax.plot(x, direct[:, b] - vbm, color="k", lw=0.8)
sp = d["sp3_8"]
for b in range(8):
    ax.plot(x[::2], sp[::2, b] - vbm, "o", ms=1.8, color="C1", mew=0)
ax.plot([], [], color="k", lw=0.8, label="direct (plane waves)")
ax.plot([], [], "o", ms=3, color="C1", label=r"8 $sp^3$ functions, $8^3$ grid")
ax.axhline(froz, color="C0", lw=0.6, ls="--")
ax.plot([], [], color="C0", lw=0.6, ls="--", label="frozen window")   # in the legend: no free spot on the bands
for t in labx:
    ax.axvline(t, color="0.8", lw=0.5, zorder=0)
    bx.axvline(t, color="0.8", lw=0.5, zorder=0)
ax.set_ylim(-14.5, 12)                    # room for the legend below the lowest band
ax.set_ylabel(r"$\varepsilon_{n\mathbf{k}}$ (eV)")
ax.legend(loc="lower center", bbox_to_anchor=(0.62, 0.0), fontsize=7, frameon=False, ncol=1)   # below the X-W-K bands
ax.set_title("(a)", loc="left", fontsize=9)
for n, col in zip((4, 6, 8), ("C1", "C2", "C3")):
    ev = np.abs(d[f"val_{n}"] - direct[:, :4]).max(1)
    bx.semilogy(x, np.maximum(ev, 1e-5), color=col, lw=0.8, label=rf"${n}^3$")
bx.set_ylim(1e-4, 1)
bx.set_ylabel("valence error (eV)")
bx.set_xticks(labx, labels)
bx.set_xlim(x[0], max(x[-1], labx[-1]) + 1e-9)   # keep the closing Gamma tick inside the limits
bx.legend(loc="lower right", bbox_to_anchor=(0.96, 0.0), fontsize=7, frameon=False, ncol=1, handlelength=1.5,
          labelspacing=0.2)   # in the empty corner of the K-Gamma segment, clear of the dips
bx.set_title("(b)", loc="left", fontsize=9, y=0.78, x=0.01)
fig.savefig(OUT, bbox_inches="tight")
print("wrote", OUT)
