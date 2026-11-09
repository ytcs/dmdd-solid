"""Fig. 16.8 (fig:16-tlsrates): relaxation rates of one two-level system in aluminum against temperature.

Defect: Delta_tl = 20.7 ueV (5.0 GHz), Delta0 = 0.3 Delta_tl.  Phonons: eq:16.8-jackle with gamma_l = gamma_t = 1 eV
(the typical deformation potential of glasses, quoted by Mueller et al., arXiv:1705.01108, Sect. II; a model value
here) and the aluminum sound speeds and density of tls16_8.py (c_LA 6.63, c_TA 3.30 km/s, 2.70 g/cm^3).
Electrons: Black rate eq:16.8-black with alpha_ohm = 0.28, the Born value 4 K_b of the resonator fit K_b = 0.07
(Maillet et al., arXiv:2009.03804); normal state (dashed) continued below T_c as for a film driven normal; superconducting:
the quasiparticle integral (solid) and the literature factor 2/(1 + e^{Delta/T}) (dotted), BCS Delta(T), T_c = 1.18 K.
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tls16_8 as t  # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch16")
E = 2 * np.pi * 5.0e9 / t.EV_S          # 5 GHz in eV
D0 = 0.3 * E
ALPHA = 0.28
gl = gt = 1.0
print(f"Delta_tl = {E*1e6:.2f} ueV = {E/t.KB*1e3:.1f} mK; Delta0/Delta_tl = 0.3; alpha_ohm = {ALPHA}")
print(f"J_ph coefficient = {t.jph_coeff(gl, gt, t.CLA_AL, t.CTA_AL, t.RHO_AL):.4g} eV^-2; "
      f"transverse/longitudinal = {2*(t.CLA_AL/t.CTA_AL)**5:.1f}")

# vitreous silica, sound speeds 5.8 (LA) and 3.8 km/s (TA) as used in Sect. 16.7 (Buchenau et al., arXiv:2012.10139, Table I)
print(f"transverse/longitudinal one-phonon weight 2 (c_LA/c_TA)^5 (gamma_t/gamma_l)^2 at equal gammas: Al {2*(t.CLA_AL/t.CTA_AL)**5:.1f}, "
      f"v-SiO2 {2*(5.8/3.8)**5:.1f}")
# crossover temperature of a barrier of curvature 10 meV
print(f"T_x = w/2pi for w = 10 meV: {10e-3/(2*np.pi)/t.KB:.1f} K")
# long-wavelength check (App. D.42): wavelength of a 0.1 meV phonon at 4 km/s
print(f"wavelength 2 pi c/omega at omega = 0.1 meV, c = 4 km/s: {2*np.pi*4e3/(1e-4*t.EV_S)*1e9:.0f} nm")
TK = np.geomspace(0.01, 1.5, 200)
ph = np.array([t.g1_ph(E, D0, T * t.KB, gl, gt, t.CLA_AL, t.CTA_AL, t.RHO_AL) for T in TK]) * t.EV_S
el = np.array([t.g1_el(E, D0, T * t.KB, ALPHA) for T in TK]) * t.EV_S
gaps = np.array([t.bcs_gap(T * t.KB) for T in TK])
sc_full = np.where(TK < t.TC_AL, el * np.array([t.rs_full(E, T * t.KB, D) if D > 0 else 1.0
                                                for T, D in zip(TK, gaps)]), np.nan)
sc_lit = np.where(TK < t.TC_AL, el * np.array([t.rs_lit(T * t.KB, D) for T, D in zip(TK, gaps)]), np.nan)
for T in (0.01, 0.05, 0.1, 0.3, 0.6, 1.0):
    Te = T * t.KB; D = t.bcs_gap(Te)
    gph = t.g1_ph(E, D0, Te, gl, gt, t.CLA_AL, t.CTA_AL, t.RHO_AL) * t.EV_S
    gel = t.g1_el(E, D0, Te, ALPHA) * t.EV_S
    print(f"T = {T} K: phonon {gph:.3g} /s, electrons normal {gel:.3g} /s (Gamma_1/Delta_tl = {gel/t.EV_S/E:.3f}), "
          f"superconducting {gel*t.rs_full(E, Te, D):.3g} /s (literature factor gives {gel*t.rs_lit(Te, D):.3g})")


def diff(T):
    Te = T * t.KB; D = t.bcs_gap(Te)
    return np.log(t.g1_el(E, D0, Te, ALPHA) * t.rs_full(E, Te, D)) - np.log(t.g1_ph(E, D0, Te, gl, gt, t.CLA_AL, t.CTA_AL, t.RHO_AL))


Tcr = brentq(diff, 0.1, 1.1)
print(f"superconducting electron rate equals the phonon rate at T = {Tcr:.3f} K (T/T_c = {Tcr/t.TC_AL:.3f})")
Tb = brentq(lambda T: t.g1_el(E, D0, T * t.KB, ALPHA) / E - 1, 0.1, 10)
print(f"normal-state Born rate reaches Delta_tl at T = {Tb:.2f} K")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.plot(TK, ph, "C0", lw=1.4, label="one phonon")
ax.plot(TK, el, "C3--", lw=1.2, label="electrons, normal")
ax.plot(TK, sc_full, "C3", lw=1.4, label="electrons, superconducting")
ax.plot(TK, sc_lit, "k:", lw=1.0, label=r"$\times\,2/(1+e^{\Delta_{\mathrm{BCS}}/T})$")
ax.axhline(E * t.EV_S, color="0.5", lw=0.6)
ax.text(0.012, E * t.EV_S * 1.4, r"$\Gamma_1 = \Delta_{\mathrm{tl}}$", fontsize=7.5, color="0.4")
ax.axvline(t.TC_AL, color="0.5", lw=0.6, ls=":")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(TK[0], TK[-1]); ax.set_ylim(1e-6, 1e12)
ax.set_xlabel(r"$T$ (K)")
ax.set_ylabel(r"$\Gamma_1$ (s$^{-1}$)")
ax.legend(frameon=False, fontsize=7.5, loc="lower right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig16_8.pdf"))
print("saved fig16_8.pdf")
