"""Limit 10.3a (Lindhard and Mermin loss-function rates) of Sect. 10.3: comparison plot and the numbers in its caption.

Output: tex/figures/ch10/limit10_3a.pdf.  Spectrum dR/domega of silicon at m_chi = 100 MeV, heavy mediator,
sigma_e = 1e-37 cm^2, rho_chi = 0.3 GeV/cm^3, standard halo (rate10_2.py), against omega/E_g with E_g = 1.11 eV (the
scissor of the tables; physical low-temperature gap 1.17 eV):
  * eq:10.2-rate with the Lindhard loss function of the gas at the silicon valence density (r_s = 2; gas10_3.py),
    Knapen et al. arXiv:2101.08275 Eq. (17);
  * the same with the Mermin function, gamma_rel = 3.66 eV (the measured width of the silicon loss peak, a fit
    parameter), Knapen et al. Eq. (19);
  * the fuller result: the RPA + LF loss function of silicon (Knapen-Kozaczuk-Lin tables via DarkELF, Sect. 10.2).
All three on the same momentum bins (|q| from 0.49 to 22.5 keV), energies on a 0.05 eV grid.
Shaded: 4.2 eV <= omega <= k_F v_max = 9.46 eV, between the upper absorption peak of silicon (Sect. 4.4, Fig. 4.5) and
the largest energy the halo deposits at q = k_F (modelling choice of the validity band, stated in the caption).
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

d = R.load()
q = d["q"]
m = 100e6
ws, ss = G.table_spectrum(m, d)
wg, sg = G.gas_spectrum(m, "lin", q)
wm, sm = G.gas_spectrum(m, "mer", q)
assert np.allclose(ws[:len(wg)], wg[:len(ws)])
n = min(len(ws), len(wg))
lo, hi = 4.2, G.KF * R.VMAX
for w0 in [lo, 5.0, 7.0, hi, 15.0]:
    i = np.argmin(abs(wg - w0))
    print(f"  omega = {wg[i]:.2f} eV: Lindhard/Si = {sg[i]/ss[i]:.2f}, Mermin/Si = {sm[i]/ss[i]:.2f}")
i_lo, i_hi = np.argmin(abs(wg - lo)), np.argmin(abs(wg - hi))
r_band = sg[i_lo:i_hi] / ss[i_lo:i_hi]
print(f"  Lindhard/Si in the band: {r_band.min():.2f} to {r_band.max():.2f}")
assert 0.6 < r_band.min() and r_band.max() < 1.6
Rs, Rg, Rm = np.trapezoid(ss, ws), np.trapezoid(sg, wg), np.trapezoid(sm, wm)
print(f"  totals: Si {Rs:.3g}, Lindhard {Rg:.3g} ({Rg/Rs:.2f}), Mermin {Rm:.3g} ({Rm/Rs:.2f}) /kg/yr")
fb = np.trapezoid(np.where((ws >= lo) & (ws <= hi), ss, 0), ws) / Rs
print(f"  share of the silicon rate inside the band: {fb:.2f}")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 2.9))
ax.axvspan(lo / R.EG, hi / R.EG, color="0.9", lw=0)
ax.loglog(ws / R.EG, ss, color="C3", lw=1.6, label="silicon, RPA + LF")
ax.loglog(wg / R.EG, sg, color="k", lw=1.2, label=r"Lindhard, $r_s = 2$")
ax.loglog(wm / R.EG, sm, color="k", lw=1.0, ls="--", label=r"Mermin, $\gamma_{\mathrm{rel}} = 3.66$ eV")
ax.set_xlim(1, 40)
ax.set_ylim(1, 5e4)
ax.set_xlabel(r"$\omega/E_{\mathrm{g}}$")
ax.set_ylabel(r"$\mathrm{d}\mathcal{R}/\mathrm{d}\omega$ [kg$^{-1}$ yr$^{-1}$ eV$^{-1}$]")
ax.legend(frameon=False, fontsize=7, loc="lower left")
fig.tight_layout()
fig.savefig(os.path.join(G.OUT, "limit10_3a.pdf"))
print("written limit10_3a.pdf")
