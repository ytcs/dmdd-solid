"""Fig. 11.6 (fig:11-iso): absorption of a B - L vector in natural silicon, per absorbed quantum and per unit squared coupling.
Isotope-disorder one-phonon channel, Eq. (11.6-Giso): Gamma_iso/g^2 = (pi/2 Omega_at) sum_i x_i M_i (b_i - bbar)^2 D_i(omega), with
the exact single-defect local densities of states D_i (Lifshitz, Eq. 11.6-lifshitz) of the three isotopes (solid) and with the host
D(omega) for all of them (dashed). Electromagnetic-like channel, Eq. (11.6-GEM): Gamma_EM/g^2 = omega Im[-1/eps(omega)]/e^2, from the
measured 293 K two-phonon absorption of Ikezawa and Ishigame (J. Phys. Soc. Jpn. 50, 3734 (1981)) as plotted in Deinzer and Strauch,
PRB 69, 045205 (2004), Fig. 3, read at the points of iso11.ALPHA_293 (reading uncertainty about 0.05 cm^-1 + 10 %), with
eps_2 = alpha n_r c/omega, n_r = 3.42, eps_1 = 11.7. At millikelvin temperatures this is an upper bound (Eq. 11.6-Tbound).
Inputs: iso11.py (PBE DOS of Sect. 5.2, omega_max = 63.7 meV; AME2020 masses; IUPAC abundances).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import iso11 as I  # noqa: E402

om = np.linspace(1e-3, I.WMAX * 0.999, 2000)
gex = I.gamma_iso(om)
g0 = I.gamma_iso(om, exact=False)
pts = I.ALPHA_293.copy()
oe = pts[:, 0] * I.CM
gem = np.array([I.gamma_em(o, a)[0] for o, a in pts])
inb = oe < I.WMAX
ratio = np.interp(oe[inb], om, gex) / gem[inb]
print("in-band 293 K points: omega (meV), Gamma_iso/Gamma_EM (exact LDOS)")
for o, r in zip(oe[inb], ratio):
    print(f"   {o*1e3:5.1f}  {r:.3e}")
print(f"range {ratio.min():.2e} - {ratio.max():.2e}")
o50 = 0.050
print(f"50 meV: Gamma_iso/g^2 = {I.gamma_iso(np.array([o50]))[0]:.3e} eV (host {I.gamma_iso(np.array([o50]), False)[0]:.3e}); "
      f"Gamma_EM/g^2 (293 K) = {I.gamma_em(o50, 0.55)[0]:.3e} eV")
# above the band: the 610 cm^-1 peak
print(f"76 meV (610 cm^-1, alpha 9.5): Gamma_EM/g^2 = {I.gamma_em(610*I.CM, 9.5)[0]:.3e} eV; Gamma_iso = 0")
# band-averaged ratio of exact to host-DOS Gamma_iso
print(f"band-integrated Gamma_iso exact/host = {np.sum(gex)/np.sum(g0):.4f}")

fig, ax = plt.subplots(figsize=(5.0, 3.3))
ax.plot(om * 1e3, g0, color="0.4", ls="--", lw=1.0, label="isotope channel, host density of states")
ax.plot(om * 1e3, gex, color="C3", lw=1.4, label="isotope channel, single-defect densities")
ax.plot(oe * 1e3, gem, "D", color="C0", ms=3.5, label="EM-like channel, 293 K data (bound at mK)")
ax.plot([610 * I.CM * 1e3], [I.gamma_em(610 * I.CM, 9.5)[0]], "D", color="C0", ms=3.5)
ax.axvline(I.WMAX * 1e3, color="0.5", lw=0.7, ls=":")
ax.set_yscale("log")
ax.set_xlim(0, 80)
ax.set_ylim(1e-8, 1e-1)
ax.set_xlabel(r"$\omega = m_\phi$ (meV)")
ax.set_ylabel(r"$\mathit{\Gamma}/g_{B-L}^2$ (eV)")
ax.legend(fontsize=7, frameon=False, loc="lower right")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "fig11_6.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
