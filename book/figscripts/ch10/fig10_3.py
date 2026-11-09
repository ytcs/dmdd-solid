"""Fig. 10.3 of Sect. 10.3: the silicon plasmon against the reach of halo dark matter.

Output: tex/figures/ch10/fig10_3.pdf.  Color: the RPA + LF loss function of silicon, L(q, omega), from the
Knapen-Kozaczuk-Lin tables (DarkELF; averaged over directions in 100 eV bins of |q|, from 0.49 keV; si_elf_binned.npz),
logarithmic scale.  Overlays:
  * dots: the position of the maximum of L in each bin (the loss peak), every third bin;
  * red: the plasmon of the electron gas at the valence density (exact zero of eps_Lin, gas10_3.wpl) up to
    q_c = 2.60 keV (Sect. 4.5), and its continuum edge omega_+ = q v_F + q^2/2m_e (thin);
  * dashed: omega = q v_max, v_max = 2.650e-3, the largest energy a halo particle deposits at momentum q;
  * dotted: omega = q v_th, v_th = v_F + q_c/2m_e = 9.54e-3, the slowest particle that reaches the gas plasmon.
The tables put the small-q loss peak at 18.9 eV (measured 16.4 eV, Sect. 4.4): the scissor that fixes the gap also
raises the interband energies.  Numbers printed: the half-maximum width of the peak in selected bins.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rate10_2 as R
import gas10_3 as G

d = R.load()
q, om, L = d["q"], d["omega"], d["lf"]
sel = q <= 8000
qk = q[sel] / 1e3
Ls = np.maximum(L[:, sel], 1e-4)
ipk = np.argmax(L[:, sel], axis=0)
for j in [0, 16, 27, 37]:
    ab = om[L[:, j] > L[:, j].max() / 2]
    print(f"  q = {q[j]/1e3:.2f} keV: peak {om[np.argmax(L[:, j])]:.1f} eV, half maximum {ab.min():.1f}-{ab.max():.1f} eV")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(5.2, 3.4))
pc = ax.pcolormesh(qk, om, Ls, norm=LogNorm(1e-2, 5), cmap="Greys", shading="nearest", rasterized=True)
cb = fig.colorbar(pc, ax=ax, pad=0.02)
cb.set_label(r"$L(q,\omega)$, silicon")
ax.plot(qk[::3], om[ipk][::3], "o", ms=2.2, color="C0", label="loss peak, silicon")
qg = np.linspace(0.02, 0.9999, 300) * G.QC
ax.plot(qg / 1e3, [G.wpl(x) for x in qg], color="C3", lw=1.5, label=r"gas plasmon to $q_{\mathrm{c}}$")
qe = np.linspace(0.0, 8000, 300)
ax.plot(qe / 1e3, G.wplus(qe), color="C3", lw=0.6)
ax.plot(qe / 1e3, qe * R.VMAX, color="k", lw=1.2, ls="--", label=r"$\omega = qv_{\max}$")
vth = G.wplus(G.QC) / G.QC
ax.plot(qe / 1e3, qe * vth, color="k", lw=0.9, ls=":", label=r"$\omega = qv_{\mathrm{th}}$")
ax.plot([G.QC / 1e3], [G.wplus(G.QC)], "o", color="C3", ms=3.5)
ax.set_xlim(0, 8)
ax.set_ylim(0, 60)
ax.set_xlabel(r"$q$ [keV]")
ax.set_ylabel(r"$\omega$ [eV]")
ax.legend(frameon=True, framealpha=0.9, fontsize=6.5, loc="upper left")
fig.tight_layout()
fig.savefig(os.path.join(G.OUT, "fig10_3.pdf"), dpi=300)
print("written fig10_3.pdf")
