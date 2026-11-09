"""Fig. 8.1: supports of the master rate formula in the (q, omega) plane (Sect. 8.2).
Output: tex/figures/ch08/fig8_1.pdf. Natural units hbar = c = k_B = 1; q in keV, omega in eV.

Kinematics (eq:1.3-omegaq, eq:1.4-absorption, eq:8.1-omega-ferm; no target data enter):
  scattering, speeds v <= v_max, all directions: -q v_max - q^2/2m_chi - Delta <= omega <= q v_max - q^2/2m_chi - Delta.
  The band edges are the extreme values of omega_q = q.v - q^2/2m_chi - Delta over |v| <= v_max.
  bosonic absorption: the point (q, omega) = (m_phi v, m_phi), drawn at v = 1e-3; its emission partner (-p_phi, -m_phi).
  fermionic absorption (massless outgoing fermion, v -> 0): omega = m_chi - q, at q ~ m_chi = 10 MeV, off this plot.
Modelling choices (illustrative values, stated in the caption):
  m_chi = 10 MeV; v_max = 2.650e-3 (eq:A.8-ref); exothermic splitting Delta = -20 eV; m_phi = 40 eV.
The omega < 0 part of the elastic band is open only to a warm target: its weight relative to omega > 0 at the same
|omega| is exp(-|omega|/T) by detailed balance (eq:2.5-db).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

mchi = 10e6          # eV
vmax = 2.650e-3
Delta = -20.0        # eV, exothermic
mphi = 40.0          # eV

q = np.linspace(0, 70e3, 800)    # eV
up = q * vmax - q**2 / (2 * mchi)
lo = -q * vmax - q**2 / (2 * mchi)
qk = q / 1e3

# numbers quoted in the caption and text
qpeak = mchi * vmax
print(f"elastic: max omega = m v_max^2/2 = {mchi*vmax**2/2:.2f} eV at q = m v_max = {qpeak/1e3:.1f} keV")
print(f"elastic: upper edge returns to omega = 0 at q = 2 m v_max = {2*qpeak/1e3:.1f} keV")
print(f"absorption point: q = m_phi * 1e-3 = {mphi*1e-3*1e3:.0f} meV")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(5.2, 4.2))

# elastic band, omega > 0 (any temperature)
ax.fill_between(qk, np.maximum(lo, 0), np.maximum(up, 0), where=up > 0, color="0.75", lw=0,
                label=r"elastic scattering, $\omega > 0$")
# elastic band, omega < 0 (warm target only)
ax.fill_between(qk, lo, np.minimum(up, 0), facecolor="white", hatch="////", edgecolor="0.45", lw=0,
                label=r"elastic, $\omega < 0$: warm target, weight $\mathrm{e}^{-|\omega|/T}$")
ax.plot(qk, up, color="0.3", lw=0.8)
ax.plot(qk, lo, color="0.3", lw=0.8)
# exothermic band: shifted up by |Delta|
ax.plot(qk, up - Delta, color="C3", lw=1.2, ls="--", label=r"exothermic, $\Delta_\chi = -20$ eV")
ax.plot(qk, lo - Delta, color="C3", lw=1.2, ls="--")
# absorption and its emission partner
ax.plot([mphi * 1e-3 / 1e3], [mphi], "o", color="C0", ms=6, label=r"absorption, $(m_\phi v,\, m_\phi)$")
ax.plot([mphi * 1e-3 / 1e3], [-mphi], "o", mfc="none", color="C0", ms=6,
        label=r"stimulated emission, $\omega = -m_\phi$")
ax.axhline(0, color="k", lw=0.5)
ax.set_xlim(-1.5, 70)
ax.set_ylim(-75, 75)
ax.set_xlabel(r"momentum transfer $q$ (keV)")
ax.set_ylabel(r"energy deposited $\omega$ (eV)")
ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=2, fontsize=7.5, frameon=False)
fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch08", "fig8_1.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)
fig.savefig(out)
print("wrote", os.path.normpath(out))
