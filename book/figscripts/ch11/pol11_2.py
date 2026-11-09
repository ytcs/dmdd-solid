"""Shared inputs and kinematic kernels for Sect. 11.2 (polar single-phonon rates). Every number is sourced here.

Halo [B]: D. Baxter et al., Eur. Phys. J. C 81, 907 (2021), arXiv:2105.00599, Table 1: v0 = 238, v_esc = 544 km/s,
  |v_sun| = 250.5 km/s (reference Earth speed of App. A.8), rho_chi = 0.3 GeV/cm^3; v_max = 794.5 km/s = 2.650e-3 (eq:A.8-ref).
  eta(v_min): closed form of App. D.1, as figscripts/ch01/fig1_6.py (checked there against quadrature).
GaAs, measured [5.5]: omega_T = 33.62, omega_L = 36.35 meV (Strauch and Dorner 1990, as tabulated by Dehghani et al. 2025,
  Table I); eps_0 = 12.9, eps_inf = 10.88 (Lockwood et al. 2005, as quoted by Knapen et al. 2018); a = 5.638 A (zero-temperature
  measured value of tab:E-functionals); natural masses 69.723 and 74.9216 u; Z* = 2.11 from the splitting (WE 5.6, we5_6.py).
GaAs and LiF, computed [T1]: S. Griffin et al., Phys. Rev. D 101, 055004 (2020), arXiv:1910.10716, Table I (DFT): GaAs
  Zbar* = 2.27, eps_inf = 10.9, omega_O = 31.8-34.9 meV; LiF Zbar* = 1.05, eps_inf = 2.02, omega_O = 33.5-77.2 meV
  (range over the optical modes near k = 0; for a cubic diatomic its ends are the TO and LO energies).
Sapphire [G18]: S. Griffin, S. Knapen, T. Lin, K. Zurek, Phys. Rev. D 98, 115034 (2018), arXiv:1807.10291 v1, Table II
  (LO and TO frequencies in cm^-1, ordinary and extraordinary rays; frequencies from their Ref. [68], errors < 0.5 %) and
  Table I (eps_inf = 3.2; eps_0 = 9.3 perpendicular and 11.5 parallel to the c axis; rho_T = 3.98 g/cm^3).
Standard atomic weights (u): Li 6.941, F 18.998, Ga 69.723, As 74.9216; 1 u = 931.494 MeV.
Constants: e^2 = 4 pi alpha = 0.091701 (Heaviside-Lorentz); hbar c = 1973.2698 eV A; 1 eV = 1.78266e-33 g;
  1 cm^-3 = 7.6835e-15 eV^3 (App. A.1); c = 299792.458 km/s; 1 cm^-1 = 0.1239842 meV.
"""
import numpy as np
from scipy.special import erf

# ---------------------------------------------------------------- constants
ALPHA = 1 / 137.035999
E2 = 4 * np.pi * ALPHA
HBARC = 1973.2698          # eV A
U_EV = 931.494e6           # eV per u
EV_G = 1.78266192e-33      # g per eV
CM3_EV3 = 7.6835e-15       # eV^3 per cm^-3, so 1 eV^-3 = CM3_EV3 cm^3
C_KMS = 299792.458
CM_MEV = 0.1239841984
ME = 0.51099895e6          # eV
Q0 = ALPHA * ME            # reference momentum alpha m_e (eq:1.4-Vsq)
RHO_CHI = 0.3e9 * CM3_EV3  # eV^4
KG_YR = 1.0e3 / EV_G * 3.15576e7 / 6.582119569e-16   # (eV per kg) x (eV^-1 per year): converts eV^-1 rate per eV mass

# ---------------------------------------------------------------- halo [B]
V0, VESC, VE = 238.0, 544.0, 250.5
VMAX = (VESC + VE) / C_KMS                 # 2.650e-3
_Z = VESC / V0
N_ESC = np.pi**1.5 * V0**3 * (erf(_Z) - 2 / np.sqrt(np.pi) * _Z * np.exp(-_Z**2))


def eta(vmin):
    """Mean inverse speed above vmin (vmin dimensionless); returns eta in natural units (1/c)."""
    u = np.maximum(np.asarray(vmin, float) * C_KMS, 0.0)
    k = np.pi * V0**2 / (VE * N_ESC)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + VE) / V0) - erf((u - VE) / V0)) - 2 * VE * np.exp(-_Z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(_Z) - erf((u - VE) / V0)) - (VESC + VE - u) * np.exp(-_Z**2))
    out = np.where(u < VESC - VE, b1, np.where(u < VESC + VE, b2, 0.0))
    return out * C_KMS


def vmin(q, w, m):
    return q / (2 * m) + w / q


def qgrid(w, m, n=4000):
    """Log grid over the kinematically open q range for energy w (eV) and mass m (eV)."""
    disc = 1 - 2 * w / (m * VMAX**2)
    if disc <= 0:
        return None
    qm, qp = m * VMAX * (1 - np.sqrt(disc)), m * VMAX * (1 + np.sqrt(disc))
    return np.geomspace(qm * (1 + 1e-12), qp * (1 - 1e-12), n)


def K_light(w, m):
    """K(omega, m) = int dq/q eta(vmin(q, omega)): light-mediator kinematic weight of one branch."""
    q = qgrid(w, m)
    if q is None:
        return 0.0
    return np.trapezoid(eta(vmin(q, w, m)) / q, q)


def K_heavy(w, m):
    """int dq q^3/q0^4 eta(vmin): heavy-mediator weight, normalized so that the prefactor is that of K_light."""
    q = qgrid(w, m)
    if q is None:
        return 0.0
    return np.trapezoid(eta(vmin(q, w, m)) * q**3 / Q0**4, q)


def prefactor(m, rho_T_eV4, sigma_cm2=1e-40):
    """rho_chi sigma_e q0^4/(2 pi m mu^2 e^2 rho_T): multiplies sum_nu (pi omega_L nu/2) w_nu K_nu; result in events/kg/yr."""
    mu = m * ME / (m + ME)
    sigma = sigma_cm2 / (HBARC * 1e-8)**2      # cm^2 -> eV^-2
    rate_per_mass = RHO_CHI * sigma * Q0**4 / (2 * np.pi * m * mu**2 * E2 * rho_T_eV4)   # eV^-1 per (eV of band integral)
    return rate_per_mass


def per_kg_yr(rate_eV_per_eVmass):
    """Rate per unit target mass in natural units (eV^-1 per eV of target mass) -> events per kg per year."""
    return rate_eV_per_eVmass / 6.582119569e-16 * 3.15576e7 * (1e3 / EV_G)


# ---------------------------------------------------------------- materials
M_GA, M_AS, M_LI, M_F = 69.723, 74.9216, 6.941, 18.998
GAAS = dict(wT=33.62e-3, wL=36.35e-3, eps0=12.9, epsinf=10.88, a=5.638, Zs=2.11)
GAAS_DFT_T1 = dict(Zs=2.27, epsinf=10.9, wT=31.8e-3, wL=34.9e-3)
LIF_T1 = dict(Zs=1.05, epsinf=2.02, wT=33.5e-3, wL=77.2e-3)
SAPH_O = dict(wL=np.array([906.6, 629.5, 481.7, 387.6]) * CM_MEV * 1e-3,
              wT=np.array([633.6, 569.0, 439.1, 385.0]) * CM_MEV * 1e-3, epsinf=3.2, eps0_tab=9.3)
SAPH_E = dict(wL=np.array([881.1, 510.9]) * CM_MEV * 1e-3,
              wT=np.array([582.4, 397.5]) * CM_MEV * 1e-3, epsinf=3.2, eps0_tab=11.5)
RHO_SAPH = 3.98   # g/cm^3 [G18 Table I]


def rho_eV4(rho_g_cm3):
    return rho_g_cm3 / EV_G * CM3_EV3


def mu_red(m1, m2):
    return m1 * m2 / (m1 + m2)


def band_integral_diatomic(Zs, epsinf, wL, m1, m2):
    """I_pol/rho_T = (pi/2) e^2 Z*^2/(M_cell mu eps_inf^2 omega_L), in meV cm^3/g (Omega-free form)."""
    Mc, mu = (m1 + m2) * U_EV, mu_red(m1, m2) * U_EV
    val = (np.pi / 2) * E2 * Zs**2 / (Mc * mu * epsinf**2 * wL)     # eV^-3
    return val * 1e3 * CM3_EV3 / EV_G                                   # eV^-3 = 1e3 meV x (cm^3/eV^4 ...)


def factorized_weights(wL, wT, epsinf):
    """Lossless factorized eps = eps_inf prod (wL^2 - w^2)/(wT^2 - w^2) on one principal axis.
    Returns w_pol (the residues: L = sum_nu (pi wL_nu/2) w_nu delta(w - wL_nu)), eps0 = eps_inf prod (wL/wT)^2, and the
    oscillator strengths S_nu (eps = eps_inf + sum_nu S_nu wT_nu^2/(wT_nu^2 - w^2))."""
    wL, wT = np.asarray(wL), np.asarray(wT)
    n = len(wL)
    wpol, S = np.zeros(n), np.zeros(n)
    for mu_ in range(n):
        A = np.prod(wT**2 - wL[mu_]**2) / np.prod([wL[j]**2 - wL[mu_]**2 for j in range(n) if j != mu_])
        wpol[mu_] = -A / (epsinf * wL[mu_]**2)
        B = np.prod(wL**2 - wT[mu_]**2) / np.prod([wT[j]**2 - wT[mu_]**2 for j in range(n) if j != mu_])
        S[mu_] = epsinf * B / wT[mu_]**2
    eps0 = epsinf * np.prod(wL**2 / wT**2)
    return wpol, eps0, S


if __name__ == "__main__":
    print("v_max =", VMAX)
    for nm, d in (("o", SAPH_O), ("e", SAPH_E)):
        wp, e0, S = factorized_weights(d["wL"], d["wT"], d["epsinf"])
        print(nm, "w_pol", wp.round(5), "sum", wp.sum().round(5), "1/einf-1/e0", (1 / d["epsinf"] - 1 / e0).round(5),
              "eps0(LST)", e0.round(3), "table", d["eps0_tab"], "sum S", S.sum().round(3), "S", S.round(3))
        I = (np.pi / 2) * np.sum(d["wL"] * wp)
        print("   I_pol/rho (meV cm3/g) =", (I * 1e3 / RHO_SAPH).round(3))
