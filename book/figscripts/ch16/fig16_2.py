"""Fig. 16.2 of Sect. 16.2: plasmon dispersions in three, two and one dimensions against the reach of halo dark matter.

Output: tex/figures/ch16/fig16_2.pdf.
  * 3D: silicon valence gas, omega_pl^2 = omega_p^2 + (3/5) v_F^2 q^2 (Eq. 4.5-dispersion to O(q^2)), omega_p = 16.6 eV,
    k_F = 3.57 keV (Sect. 4.5), drawn to its quadratic cutoff 2.24 keV (Sect. 10.3).
  * 2D: doped graphene in vacuum, model Fermi energy E_F = 0.2 eV (an illustrative choice), long-wavelength form
    omega^2 = v2D(q) D q^2 with the Drude weight D = g_deg E_F/(4 pi), g_deg = 4 (spin x valley), v2D = e^2/(2q)
    (eps_a = eps_b = 1): omega^2 = 2 alpha E_F q.  Drawn while it lies above the intraband edge v_D q and below the
    interband edge 2 E_F - v_D q, where the long-wavelength form ends.
  * 1D: metallic nanotube, omega = v_D q/g_c(q), N_ch = 4, shell kernel with r_t = 0.7 nm, drawn to q = 1/r_t.
  * Halo: omega = q v_max (Eq. 1.2-vmax); horizontal ticks omega_max = m_chi v_max^2/2 for m_chi = 10 keV, 100 keV, 1 MeV.
A bulk mode is reached only if its own (omega, q) lies below the line; a mode of a sheet or a tube depends only on q_par,
and a halo particle reaches it with any total momentum q >= omega/v_max (q_perp taken by the form factor).
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lowd16_2 as L

EF = 0.2
GDEG = 4

q3 = np.geomspace(1.0, 2240.0, 300)
w3 = np.sqrt(L.WP_SI ** 2 + 0.6 * L.VF_SI ** 2 * q3 ** 2)


def w2(q):
    return np.sqrt(L.v2D(q) * GDEG * EF / (4 * np.pi) * q ** 2)


print(f"v_D = {L.V_D:.4e} = {L.V_D*L.C_KMS:.0f} km/s = {L.V_D/L.VMAX:.3f} v_max; v_max = {L.VMAX:.4e}")
print(f"2D graphene check: omega^2 = 2 alpha E_F q: at q = 10 eV {w2(10.0):.4f} eV vs {np.sqrt(2*L.ALPHA*EF*10):.4f} eV")
q2max = brentq(lambda q: w2(q) - (2 * EF - L.V_D * q), 1.0, 2 * EF / L.V_D)
q2 = np.geomspace(0.01, q2max, 300)
print(f"  graphene plasmon meets the interband edge 2E_F - v_D q at q = {q2max:.1f} eV, omega = {w2(q2max):.3f} eV")
print(f"  graphene phase velocity / v_max at q = 1, 10 eV: {w2(1.0)/1.0/L.VMAX:.1f}, {w2(10.0)/10.0/L.VMAX:.1f}")
q1 = np.geomspace(0.01, 1 / L.R_T, 300)
w1 = L.V_D * q1 / L.g_c(q1)
for q in [1.0, 10.0, 100.0]:
    print(f"  nanotube q = {q} eV: g_c = {L.g_c(q):.3f} (log form {L.g_c(q, kern=L.v1D_log):.3f}), "
          f"omega = {L.V_D*q/L.g_c(q)*1e3:.2f} meV, v_pl = {L.V_D/L.g_c(q):.4e} = {L.V_D/L.g_c(q)/L.VMAX:.1f} v_max")
for m in [1e4, 1e5, 1e6]:
    wmax = m * L.VMAX ** 2 / 2
    print(f"  m_chi = {m/1e3:.0f} keV: omega_max = {wmax:.4f} eV, q_max = 2 m v_max = {2*m*L.VMAX:.1f} eV, "
          f"q needed for omega_max = {wmax/L.VMAX:.2f} eV")
print(f"  bulk Si: line omega = q v_max reaches omega_p at q = {L.WP_SI/L.VMAX:.0f} eV (Sect. 4.5: 6.27 keV)")
print(f"  form factor scale 1/r_t = {1/L.R_T:.0f} eV: largest omega reachable with q_perp <~ 1/r_t: v_max/r_t = {L.VMAX/L.R_T:.3f} eV")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.8, 3.2))
qq = np.geomspace(0.01, 1e4, 10)
ax.loglog(qq, qq * L.VMAX, color="k", lw=1.0, ls="--", label=r"$\omega = qv_{\max}$")
ax.fill_between(qq, 1e-6, qq * L.VMAX, color="0.92", lw=0)
ax.loglog(q3, w3, color="C3", lw=1.5, label="3D: silicon valence gas")
ax.loglog(q2, w2(q2), color="C0", lw=1.5, label=r"2D: graphene, $E_{\mathrm{F}} = 0.2$ eV")
ax.loglog(q1, w1, color="C2", lw=1.5, label=r"1D: nanotube, $N_{\mathrm{ch}} = 4$, $r_{\mathrm{t}} = 0.7$ nm")
for m, lab in [(1e4, "10 keV"), (1e5, "100 keV"), (1e6, "1 MeV")]:
    wmax = m * L.VMAX ** 2 / 2
    ax.axhline(wmax, color="0.5", lw=0.6, ls=":")
    ax.text(1.3e-2, wmax * 1.15, r"$\omega_{\max}$, " + lab, fontsize=6.5, color="0.35")
ax.set_xlim(1e-2, 1e4)
ax.set_ylim(1e-5, 60)
ax.set_xlabel(r"momentum $q$ (eV); $q_\parallel$ for the sheet and the tube")
ax.set_ylabel(r"$\omega$ (eV)")
ax.legend(fontsize=7, frameon=False, loc="lower right")
fig.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tex/figures/ch16/fig16_2.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
