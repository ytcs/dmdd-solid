"""Limit 10.2a (the loss-function rate) of Sect. 10.2: comparison plot and the numbers quoted with it.

Output: tex/figures/ch10/limit10_2a.pdf.  Spectrum dR/domega of silicon at m_chi = 1 MeV, heavy mediator,
sigma_e = 1e-37 cm^2, against omega/omega_max (omega_max = 64.1 meV, the top of the phonon band, Sect. 5.2):
  * loss-function rate (eq:10.2-rate) with the RPA + LF tables (si_elf_binned.npz); for a dark photon (total-charge
    coupling) it is the whole rate in silicon, whose Born charges vanish (the acoustic weight of S_ZZ starts at O(q^4)
    and is dropped, Sect. 8.4);
  * electron-only (electrophilic) coupling: the same electronic continuum plus the acoustic peak of S_ee carried by the
    electrons that follow the nuclei (Sect. 8.4, 8.6), from rate10_2.phonon_dRdq.
Modelling choices of the acoustic peak (pedagogical model, stated in the caption): isotropic linear longitudinal
branch omega = c_LA q with c_LA = 8.43 km/s (measured, along [100]; App. C.18) up to |q| = 2 pi / a = 2.28 keV (the
X point, where c_LA q = 64.2 meV ~ omega_max); electron-following charge 14 per atom (all electrons, Z* = 0, valid for
q well below the inverse 1s radius, ~30 keV); no Debye-Waller factor, no Umklapp, no transverse branches, no
multiphonon or Migdal terms.  Then  dR/domega = rho_chi sigma_e N^2 q^2 eta(c_LA + q/2m) / (4 rho_T m mu^2 M_cell
Omega c_LA^2)  at q = omega/c_LA (derived in the script docstring of rate10_2.phonon_dRdq).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rate10_2 as R

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch10")
WMAX_PH = 0.0641
d = R.load()
m = 1e6
conv = R.to_per_kg_yr(1.0)

# electronic continuum (both couplings)
w_el, s_el = R.spectrum(m, "lf", d)
s_el = np.where(w_el <= m * R.VMAX**2 / 2, s_el, 0.0)
R_el = np.trapezoid(s_el, w_el)

# acoustic peak (electron-only coupling): dR/domega = (dR/dq)/c_LA at q = omega/c_LA
qph = np.linspace(1.0, R.Q_X, 4000)
dRdq = R.phonon_dRdq(qph, m) * conv
w_ph = R.C_LA * qph
s_ph = dRdq / R.C_LA
R_ph = np.trapezoid(dRdq, qph)
print("m = 1 MeV heavy, sigma_e = 1e-37 cm^2:")
print("  electronic (loss-function) rate above the gap: %.2f /kg/yr" % R_el)
print("  acoustic peak of the electron-only coupling (model): %.3g /kg/yr = %.0f x electronic" % (R_ph, R_ph / R_el))
print("  acoustic peak spans omega up to %.1f meV (c_LA q_X); mean omega = %.1f meV"
      % (w_ph[-1] * 1e3, np.trapezoid(w_ph * s_ph, w_ph) / np.trapezoid(s_ph, w_ph) * 1e3))
print("  electronic spectrum spans %.2f to %.2f eV = %.0f to %.0f omega_max" % (R.EG, m * R.VMAX**2 / 2,
                                                                          R.EG / WMAX_PH, m * R.VMAX**2 / 2 / WMAX_PH))
# share of the f-sum carried by the electron-following sector (Sect. 8.6): 14 m_e / M_Si
print("  f-sum share of the acoustic peak, 14 m_e/M = %.2e" % (14 * R.ME / R.M_SI))
assert R_ph > 10 * R_el

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 2.9))
ax.axvspan(1.0, 200, color="0.92", lw=0)
ax.loglog(w_ph / WMAX_PH, s_ph, color="k", lw=1.3, label="electron-only coupling, lattice free")
ax.loglog(w_el / WMAX_PH, s_el, color="C3", lw=1.6, label="loss-function rate (both couplings)")
ax.loglog(w_el / WMAX_PH, s_el, color="k", lw=1.0, ls=(0, (2, 2)))
ax.set_xlim(0.03, 100)
ax.set_ylim(1e-1, 1e8)
ax.set_xlabel(r"$\omega/\omega_{\max}$")
ax.set_ylabel(r"$\mathrm{d}\mathcal{R}/\mathrm{d}\omega$ [kg$^{-1}$ yr$^{-1}$ eV$^{-1}$]")
ax.text(1.3, 2e7, r"$\omega > \omega_{\max}$", fontsize=8, color="0.3")
ax.text(25, 2.2, r"$E_{\mathrm{g}}$", fontsize=8)
ax.axvline(R.EG / WMAX_PH, color="0.5", lw=0.6, ls=":")
ax.legend(frameon=False, fontsize=7, loc="lower left")
fig.tight_layout()
os.makedirs(OUT, exist_ok=True)
fig.savefig(os.path.join(OUT, "limit10_2a.pdf"))
print("written limit10_2a.pdf")
