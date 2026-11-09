"""Fig. 5.3 (Sect. 5.4): Fourier interpolation of DFPT force constants and the acoustic sum rule in silicon.
Output: tex/figures/ch05/fig5_3.pdf. Prints every number quoted in Sect. 5.4 about interpolation and the sum rule.
Data: fig5_3_data.npz from fig5_3_data.py, i.e. the representative DFPT run of Sect. 5.2 (fig5_2_qe.sh: Quantum ESPRESSO 7.6,
PBE, SG15 ONCV, 60 Ry, 12^3 k, a = 5.431 A, natural Si mass 28.0855 u, 6^3 Q grid), re-interpolated by fig5_3_qe.sh from its
2^3, 3^3 subgrids and from the full 6^3 grid (sum rule imposed, asr='crystal'; and asr='no' on the 6^3 grid), plus direct ph.x
runs at three points on none of the grids (Delta (0,0,1/2), Sigma (1/2,1/2,0), Lambda (1/4,1/4,1/4), in 2pi/a).
Measured frequencies (THz): Dolling 1963; Nilsson and Nelin, Phys. Rev. B 6, 3777 (1972); as tabulated in Savrasov,
Phys. Rev. B 54, 16470 (1996), Table I (same values as fig5_2.py).
Elastic sound speeds along [100]: c_LA = 8.43, c_TA = 5.84 km/s (C11, C44 of Martinez et al. 2019 Table I, rho 2.33 g/cm^3; App. C.18).
Panel (c): Frobenius norm of the 3x3 force-constant blocks of the 6^3 grid vs the minimum-image distance (fig5_3_data.py).
Colors validated with the dataviz palette validator (light surface): #2a6fb0, #c4661f, #8a4fa0 all checks pass; line styles
give secondary encoding.
Run: python fig5_3.py   (numpy, matplotlib)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from fig5_3_qpath import points, FINE, OFFNAME

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch05", "fig5_3.pdf")
CM1 = 1.23984198e-1          # meV per cm^-1
THZ = 4.135667696            # meV per THz
HBAR_MEV = 6.582119569e-13   # meV s
A = 5.431e-10                # m

d = np.load(os.path.join(HERE, "fig5_3_data.npz"))
dl, sg, lm, fine, off = points()
n1, n2, n3, nf = len(dl), len(sg), len(lm), len(fine)


def split(f):
    f = np.sort(f * CM1, axis=1)
    return f[:n1], f[n1:n1 + n2], f[n1 + n2:n1 + n2 + n3], f[n1 + n2 + n3:n1 + n2 + n3 + nf], f[n1 + n2 + n3 + nf:]


G = {N: split(d[f"f{N}"]) for N in (2, 3, 6)}
NO = split(d["f6no"])
foff = np.sort(d["foff"] * CM1, axis=1)

# --- on-grid and off-grid comparisons
for N in (2, 3, 6):
    fd, fs, fl, ff, fo = G[N]
    print(f"{N}^3 grid: Gamma {np.round(fd[0],2)}  X {np.round(fd[-1],2)}  L {np.round(fl[-1],2)} meV")
    for k in range(3):
        dev = fo[k] - foff[k]
        print(f"   off-grid {OFFNAME[k]:20s} interp {np.round(fo[k],2)}  direct {np.round(foff[k],2)}  "
              f"max|dev| {np.abs(dev).max():.2f} meV ({100*np.max(np.abs(dev)/np.maximum(foff[k],1)):.1f} %)")
allmax = {N: max(np.abs(G[N][4] - foff).max(), 0) for N in (2, 3, 6)}
print("max |interp - direct| over the three off-grid points (meV):", {N: round(v, 2) for N, v in allmax.items()})
for N in (2, 3):
    full = np.concatenate([G[N][i] for i in range(3)]); ref = np.concatenate([G[6][i] for i in range(3)])
    print(f"max |{N}^3 - 6^3| along the path: {np.abs(full-ref).max():.2f} meV; TA at X: {G[N][0][-1][0]:.2f} vs {G[6][0][-1][0]:.2f}")

# --- sum rule: Gamma and small Q along [100]
fno = NO[3]; fas = G[6][3]
print("asr='no' Gamma frequencies (meV):", np.round(fno[0], 3), " = THz", np.round(fno[0] / THZ, 3))
Q = FINE * 2 * np.pi / A
for z in (0.01, 0.02, 0.05, 0.1):
    i = int(np.argmin(np.abs(FINE - z)))
    print(f"Q = {z:.2f} (2pi/a): TA asr {fas[i,0]:.3f}  no-asr {fno[i,0]:.3f} meV; LA asr {fas[i,2]:.3f} no-asr {fno[i,2]:.3f}")
i = int(np.argmin(np.abs(FINE - 0.02)))
print("PBE slopes at Q = 0.02 (km/s), TA, LA:", np.round(fas[i, [0, 2]] / HBAR_MEV / Q[i] / 1e3, 2))
w0 = fno[0, :3]
print("check omega^2 = omega0^2 + (asr omega)^2 at Q = 0.05 (TA):",
      round(float(np.sqrt(w0[0] ** 2 + fas[10, 0] ** 2)), 3), "vs", round(float(fno[10, 0]), 3))

# --- force-constant decay
dist, nrm = d["dist"], d["phinorm"]
o = np.argsort(dist)
dist, nrm = dist[o], nrm[o]
bond = np.sqrt(3) / 4 * 5.431
shells = np.unique(np.round(dist, 2))
print("on-site norm %.2f eV/A^2; first shells (distance A: max norm eV/A^2):" % nrm[0])
for s in shells[:8]:
    m = np.abs(dist - s) < 0.01
    print(f"   {s:5.2f} A ({s/bond:4.2f} bonds): {nrm[m].max():.4f}")
far = dist > 3 * bond
print(f"largest block beyond 3 bond lengths: {nrm[far].max():.4f} eV/A^2 at {dist[far][np.argmax(nrm[far])]:.2f} A; "
      f"ratio to nearest neighbor {nrm[far].max()/nrm[(np.abs(dist-bond)<0.01)].max():.4f}")

# --- figure
plt.rcParams.update({"font.size": 8, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
                     "font.family": "serif", "mathtext.fontset": "cm"})
BLUE, ORANGE, PURPLE = "#2a6fb0", "#c4661f", "#8a4fa0"
sty = {6: dict(color=BLUE, lw=1.0, ls="-"), 3: dict(color=ORANGE, lw=0.9, ls="--"), 2: dict(color=PURPLE, lw=0.9, ls=":")}
fig = plt.figure(figsize=(6.3, 3.4))
ax = fig.add_axes([0.075, 0.12, 0.52, 0.74])
axb = fig.add_axes([0.715, 0.585, 0.25, 0.33])   # x0 moved right: room for the (c) axis label
axc = fig.add_axes([0.715, 0.12, 0.25, 0.33])
ls2, lL = np.sqrt(2), np.sqrt(3) / 2
xd, xs, xl = np.linspace(0, 1, n1), 1 + np.linspace(0, ls2, n2), 1 + ls2 + np.linspace(0, lL, n3)
for N in (2, 3, 6):
    fd, fs, fl = G[N][:3]
    for x, ff in ((xd, fd), (xs, fs), (xl, fl)):
        ax.plot(x, ff, **sty[N])
    ax.plot([], [], **sty[N], label=rf"${N}^3$ grid")
ticks = [0, 1, 1 + ls2 / 4, 1 + ls2, 1 + ls2 + lL]
ax.set_xticks(ticks); ax.set_xticklabels([r"$\Gamma$", r"X$\,|\,$X$'$", "K", r"$\Gamma$", "L"])
for t in ticks[1:-1]:
    ax.axvline(t, color="0.85", lw=0.5, zorder=0)
ax.set_xlim(0, ticks[-1]); ax.set_ylim(0, 70)
mk = dict(marker="o", ms=4, mfc="white", mec="black", mew=0.8, ls="none", zorder=5)
ax.plot([0, 1 + ls2], [15.53 * THZ] * 2, **mk, label="measured")
ax.plot([1.0] * 3, [v * THZ for v in (4.49, 12.32, 13.90)], **mk)
ax.plot([1 + ls2 + lL] * 4, [v * THZ for v in (3.43, 11.35, 12.60, 14.68)], **mk)
xoff = [0.5, 1 + 0.5 * ls2, 1 + ls2 + 0.25 * np.sqrt(3)]
for k in range(3):
    ax.plot([xoff[k]] * 6, foff[k], marker="D", ms=3.5, mfc="black", mec="white", mew=0.6, ls="none", zorder=6,
            label="direct DFPT, off grid" if k == 0 else None)
ax.set_ylabel(r"$\omega_{\mathbf{Q}\nu}$ (meV)")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=5, frameon=False, fontsize=6.5, handlelength=1.8,
          columnspacing=1.0)
ax.text(0.01, 0.97, "(a)", transform=ax.transAxes, va="top")
# (b) sum rule near Gamma along [100]
axb.plot(FINE, fas[:, 0], color=BLUE, lw=1.0, label="rule imposed")
axb.plot(FINE, fas[:, 2], color=BLUE, lw=1.0)
axb.plot(FINE, fno[:, 0], color=BLUE, lw=0.9, ls="--", label="not imposed")
axb.plot(FINE, fno[:, 2], color=BLUE, lw=0.9, ls="--")
for c in (8.43, 5.84):
    axb.plot(FINE, HBAR_MEV * c * 1e3 * Q, color="black", lw=0.7, ls=":")
axb.plot([], [], color="black", lw=0.7, ls=":", label=r"$c_\nu Q$, elastic")
axb.set_xlim(0, 0.06); axb.set_ylim(0, 4.2); axb.set_xticks([0, 0.02, 0.04, 0.06])
axb.set_xlabel(r"$Q$ along $[100]$ $(2\pi/a)$", labelpad=1); axb.set_ylabel("meV", labelpad=1)
axb.legend(loc="upper left", frameon=False, fontsize=6.5, handlelength=1.8, borderaxespad=0.2)
axb.text(0.97, 0.06, "(b)", transform=axb.transAxes, ha="right")
# (c) force-constant decay
axc.semilogy(dist / bond, nrm, ls="none", marker="o", ms=2.6, mfc=BLUE, mec="none", alpha=0.8)
axc.set_xlabel(r"distance (bond lengths, $\sqrt{3}a/4$)", labelpad=1)
axc.set_ylabel(r"$\|\Phi^{(2)}\|$ (eV Å$^{-2}$)", labelpad=1)
axc.set_xlim(-0.2, dist.max() / bond + 0.3); axc.set_ylim(1e-4, 50)
axc.text(0.97, 0.88, "(c)", transform=axc.transAxes, ha="right")
fig.savefig(OUT)
print("wrote", os.path.abspath(OUT))
