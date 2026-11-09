"""Shared constants and rate functions for Sect. 16.8 (two-level systems at millikelvin).

Natural units hbar = c = k_B = 1, energies in eV.  Conversions: 1 eV = 1.519267e15 s^-1, k_B = 8.617333e-5 eV/K,
hbar c = 1.973270e-5 eV cm.

Aluminum (book values, Sects. 7.2, 15.1, 20.3): T_c = 1.18 K (measured), Delta_BCS(0) = 1.764 T_c = 0.179 meV;
isotropic (Voigt) sound speeds of Sect. 20.3 from the zero-temperature elastic constants C_11, C_12, C_44 =
114.3, 61.9, 31.6 GPa (Malica and Dal Corso, arXiv:2109.13551, Table 2): c_LA = 6.63 km/s, c_TA = 3.30 km/s at the
density 2.70 g/cm^3 that the book's rates use.

Rates (Sect. 16.8, App. D.42):
  one phonon (Jaeckle):  G1_ph = (Delta0/E)^2 E^3 coth(E/2T) (gl^2/cl^5 + 2 gt^2/ct^5) / (2 pi rho)
                         = 2103.06977 Eq. (7) = 1610.03974 Eqs. (4)-(5)
  electrons (Black):     G1_el = pi alpha_ohm (Delta0/E)^2 E coth(E/2T)   = 2103.06977 Eq. (8) with W_el^2 = 4 alpha_ohm
                                                                          = 2009.03804 Eq. (4) with alpha_ohm = 4K
  superconductor:        G1_el x R_s(E,T); R_s -> 2/(1+exp(Delta/T)) for E << T, E << Delta (2103.06977 Eq. (9))
                         R_s = 2 int_Delta^inf dE' c(E',E'+E) [f(E')(1-f(E'+E)) + f(E'+E)(1-f(E'))] / (E coth(E/2T)),
                         c(E1,E2) = (E1 E2 - Delta^2)/sqrt((E1^2-Delta^2)(E2^2-Delta^2))   (case-I coherence factor)
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import expit

EV_S = 1.519267e15          # s^-1 per eV
KB = 8.617333e-5            # eV/K
HBARC_CM = 1.973270e-5      # eV cm
GCM3 = 5.609589e32 * HBARC_CM**3   # 1 g/cm^3 in eV^4  (5.6096e32 eV/c^2 per g)
C_LIGHT = 2.99792458e5      # km/s

TC_AL = 1.18                # K
DELTA0_AL = 1.764 * KB * TC_AL   # eV
CLA_AL = 6.63 / C_LIGHT
CTA_AL = 3.30 / C_LIGHT
RHO_AL = 2.70 * GCM3


def coth(x):
    return 1.0 / np.tanh(x)


def jph_coeff(gl, gt, cl, ct, rho):
    """J_s^ph(w) = coeff * w^3, coeff = (gl^2/cl^5 + 2 gt^2/ct^5)/(pi rho)."""
    return (gl**2 / cl**5 + 2 * gt**2 / ct**5) / (np.pi * rho)


def g1_ph(E, D0, T, gl, gt, cl, ct, rho):
    return 0.5 * (D0 / E)**2 * jph_coeff(gl, gt, cl, ct, rho) * E**3 * coth(E / (2 * T))


def g1_el(E, D0, T, alpha):
    return np.pi * alpha * (D0 / E)**2 * E * coth(E / (2 * T))


def bcs_gap(T, D0=DELTA0_AL, Tc=TC_AL * KB):
    """Weak-coupling BCS gap Delta(T): solve int_0^inf dxi [tanh(E/2T)/E - 1/sqrt(xi^2+D0^2)] = 0."""
    if T >= Tc:
        return 0.0
    if T < 0.05 * Tc:
        return D0

    def g(D):
        f = lambda xi: np.tanh(np.sqrt(xi**2 + D**2) / (2 * T)) / np.sqrt(xi**2 + D**2) - 1 / np.sqrt(xi**2 + D0**2)
        return quad(f, 0, 50 * D0, points=[D, D0, 10 * T], limit=1000, epsabs=1e-12)[0] + quad(f, 50 * D0, 400 * D0, limit=400)[0]
    return brentq(g, 1e-9 * D0, D0 * 1.0000001)


def fermi(E, T):
    return expit(-E / T)


def rs_full(E, T, D):
    """Ratio of the superconducting to the normal-state electron relaxation rate (E < 2 Delta)."""
    def integrand(x):            # E1 = D + x^2
        E1 = D + x * x
        E2 = E1 + E
        c = (E1 * E2 - D * D) / np.sqrt((E1 + D) * (E2 * E2 - D * D))   # sqrt(E1^2-D^2) = x sqrt(E1+D)
        occ = fermi(E1, T) * (1 - fermi(E2, T)) + fermi(E2, T) * (1 - fermi(E1, T))
        return c * occ * 2.0          # c dE1 = (c x) 2 dx
    xmax = np.sqrt(60 * T + 5 * E)
    val = quad(integrand, 0, xmax, limit=400, epsabs=0, epsrel=1e-10)[0]
    return 2 * val / (E * coth(E / (2 * T)))


def rs_lit(T, D):
    return 2.0 / (1.0 + np.exp(D / T))
