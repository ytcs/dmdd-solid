"""Worked example 12.4 (Sect. 12.4): the phonon-mediated Migdal term in silicon at q = 5 keV. Prints every number of the
example (log: we12_4.log).

Inputs (reused): soft-limit probability with Z_ion(p) and local fields, mig12.p_total / dP_domega (Sect. 12.3; KKL tables,
scissor gap 1.11 eV); phonon-number fractions and mean lattice energy from fig12_4.regime (lattice factor at |q - p|,
crystal-frame Condon; incoherent harmonic T = 0 response of the PBE DOS); the PBE DOS of Sect. 5.2 (imp11.G) for the
virtual-phonon propagator int dw g(w)/(omega_e^2 - w^2) and the one-phonon spectrum g(w)/w; the oscillator check from osc12_4.
Lattice factor at q (the linear-in-p truncation of the phonon-mediated form, 2205.03395 Eq. (3.3)): Poisson in 2W(q).
v_max = 794.5 km/s (Sect. 1.2).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
import mig12 as G  # noqa: E402
import imp11 as IMP  # noqa: E402
import fig12_4 as F  # noqa: E402
import osc12_4 as O  # noqa: E402

M = G.M
q = 5e3
ER = q**2 / (2 * M)
vN = q / M
tw = IMP.two_w(q)
print("q = 5 keV: E_R = %.4f meV, v_N = %.3e (%.1f m/s), 2W(q) = %.4f, e^-2W(q) = %.4f; m_chi >= q/2v_max = %.3f MeV; "
      "q/q_BZ = %.2f" % (ER * 1e3, vN, vN * 2.998e8, tw, np.exp(-tw), q / (2 * IMP.VMAX) / 1e6, q / G.QBZ))
P = G.p_total(ER)
print("Migdal probability (soft-limit form, Z_ion(p), local fields, omega_e >= 1.11 eV): P_Mig = %.3e (%.2e per eV of E_R)"
      % (P, P / ER))
# spectrum-averaged propagator factor
om = G.OM[G.OM >= G.EG]
dp = G.dP_domega(ER)[G.OM >= G.EG]
wg, g = IMP.WG, IMP.G * IMP.DW
fac = np.array([(w**2 * np.sum(g / (w**2 - wg**2)))**2 for w in om])
print("Virtual-phonon propagator over sudden, squared: at the gap 1.11 eV %.5f, at 1.17 eV %.5f; averaged over the spectrum "
      "%.5f" % (fac[0], (1.17**2 * np.sum(g / (1.17**2 - wg**2)))**2, np.trapezoid(fac * dp, om) / np.trapezoid(dp, om)))
w2 = np.sum(g * wg**2)
print("  <omega_ph^2>^(1/2) = %.2f meV; 2<w^2>/omega^2 at 1.17 eV = %.2e" % (np.sqrt(w2) * 1e3, 2 * w2 / 1.17**2))
fr, mw = F.regime(q)
print("Lattice factor at |q - p| (crystal frame, all orders in p): zero-phonon %.4f, one-phonon %.4f, two %.4f, >=3 %.1e; "
      "mean omega_l = %.3f meV = %.2f E_R" % (fr[0], fr[1], fr[2], fr[3:].sum(), mw * 1e3, mw / ER))
print("Lattice factor at q (linear in p): zero-phonon %.4f, one-phonon %.4f, two %.1e; phonon-emitting fraction ratio "
      "(|q-p| vs q) = %.2f" % (np.exp(-tw), tw * np.exp(-tw), tw**2 / 2 * np.exp(-tw), (1 - fr[0]) / (1 - np.exp(-tw))))
# one-phonon spectrum g(w)/w (incoherent, T = 0): mean energy of the emitted phonon
s1 = g / wg
print("One-phonon Migdal events: emitted phonon energy mean %.2f meV (= <w^-1>^-1), median %.2f meV; %.0f x E_R"
      % (np.sum(s1 * wg) / np.sum(s1) * 1e3, np.interp(0.5, np.cumsum(s1) / s1.sum(), wg) * 1e3,
         np.sum(s1 * wg) / np.sum(s1) / ER))
print("Zero-phonon events per Migdal event %.3f; probabilities: zero-phonon %.3e, phonon-emitting %.3e"
      % (fr[0], fr[0] * P, (1 - fr[0]) * P))
print("Without the zero-phonon term T_0 the rate keeps the fraction %.3f (factor %.0f low)" % (1 - fr[0], 1 / (1 - fr[0])))
# kinematics
for m in [1e6, 2e6, 5e6]:
    print("  m_chi = %.0f MeV: largest energy transfer at q = 5 keV, q v_max - q^2/2m = %.2f eV" % (m / 1e6, q * IMP.VMAX - q**2 / (2 * m)))
# oscillator check of the two forms at q = 5 keV, p = 5.7 keV, omega_e = 1.2 eV
r, rpm, tr, z = O.averaged(q, 5.7e3, 1.2)
print("Einstein-site check (w0 = 30.4 meV, p = 5.7 keV, omega_e = 1.2 eV): exact/leading %.5f, propagator/leading %.5f, "
      "exact zero-phonon fraction %.4f vs e^-2W(q) Einstein %.4f" % (r, rpm, z, np.exp(-q**2 / (2 * M * O.W_EIN))))
print("Coherent (Bragg) zero-phonon line / incoherent at 5 keV: %.3f" % F.coh_ratio(q))
