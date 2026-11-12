"""Limit 10.3b (plasmon production from the pole of 1/epsilon) of Sect. 10.3: comparison plot and caption numbers.

Output: tex/figures/ch10/limit10_3b.pdf.  Share of the f-sum (pi/2) omega_p^2 of the silicon valence electrons, as a
function of q/q_c with q_c = 2.60 keV (exact zero of eps_Lin on the continuum edge, Sect. 4.5):
  * literature pole formula: L = (pi omega_pl/2) Z_L delta(omega - omega_pl) with omega_pl^2 = omega_p^2 + (3/5)q^2 v_F^2
    and Z_L = 1 - (3/5) q^2 v_F^2/omega_p^2 (Kozaczuk-Lin arXiv:2003.12077 Eqs. (5), (7)); first moment over the f-sum
    = omega_pl^2 Z_L/omega_p^2, drawn up to its own cutoff 2.24 keV where omega_pl meets omega_+ = q v_F + q^2/2m_e;
  * fuller result: the pole of the exact Lindhard function, 2 omega_pl/(omega_p^2 d eps_1/d omega), ending at q_c;
  * halo reach: first moment of L below omega = q v_max (m_chi -> infinity, the widest reach), for the gas (Lindhard
    continuum; the pole is above the reach) and for the silicon RPA + LF tables (valence f-sum, omega_p = 16.6 eV).
Shaded: q < q_c.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rate10_2 as R
import gas10_3 as G

QC = G.QC
FS = np.pi / 2 * G.WP**2
x_ex = np.concatenate([np.linspace(0.02, 0.98, 120), 1 - np.geomspace(2e-2, 1e-6, 60)])
sh_ex = np.array([G.pole_share(x * QC) for x in x_ex])
x_f = np.linspace(0.02, G.QC_QUAD / QC, 200)
sh_f = G.wpl_quad(x_f * QC)**2 * G.ZL(x_f * QC) / G.WP**2

xg = np.geomspace(0.1, 3.0, 120)
reach_gas = []
for x in xg:
    qq = x * QC
    w = np.linspace(1e-4, qq * R.VMAX, 4000)
    reach_gas.append(np.trapezoid(w * G.L_lin(qq, w), w) / FS)
reach_gas = np.array(reach_gas)
d = R.load()
q, om = d["q"], d["omega"]
FSI = np.pi / 2 * 16.6**2
reach_si = []
for j, qq in enumerate(q):
    w = np.linspace(0, qq * R.VMAX, 2000)
    reach_si.append(np.trapezoid(w * np.interp(w, om, d["lf"][:, j]), w) / FSI)
reach_si = np.array(reach_si)
for x in [0.5, 1.0, 2.0, 3.0]:
    print(f"  q/q_c = {x}: gas reach share {np.interp(x, xg, reach_gas):.2e}, "
          f"silicon reach share {np.interp(x * QC, q, reach_si):.2e}")
print(f"  exact pole share at 0.5, 0.9 q_c: {np.interp(0.5, x_ex, sh_ex):.3f}, {np.interp(0.9, x_ex, sh_ex):.3f}")
print(f"  formula share at its cutoff 2.24 keV: {sh_f[-1]:.3f}")
assert np.interp(1.0, xg, reach_gas) < 1e-2 and np.interp(QC, q, reach_si) < 1e-2

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 2.9))
ax.axvspan(0, 1, color="0.9", lw=0)
ax.semilogy(x_f, sh_f, color="k", lw=1.0, ls="--", label=r"pole formula, $Z_L$, quadratic $\omega_{\mathrm{pl}}$")
ax.semilogy(x_ex, sh_ex, color="k", lw=1.4, label="pole of the Lindhard function")
ax.semilogy(xg, reach_gas, color="C0", lw=1.2, label=r"gas, $\omega \leq qv_{\max}$")
sel = q <= 3 * QC
ax.semilogy(q[sel] / QC, reach_si[sel], color="C3", lw=1.4, label=r"silicon, $\omega \leq qv_{\max}$")
ax.set_xlim(0, 3)
ax.set_ylim(1e-5, 3)
ax.set_xlabel(r"$q/q_{\mathrm{c}}$")
ax.set_ylabel(r"share of $(\pi/2)\,\omega_p^2$")
ax.legend(frameon=False, fontsize=6.5, loc="lower right")
fig.tight_layout()
fig.savefig(os.path.join(G.OUT, "limit10_3b.pdf"))
print("written limit10_3b.pdf")
