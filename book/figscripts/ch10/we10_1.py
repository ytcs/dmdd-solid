"""Worked example 10.1: the silicon electron-recoil rate at m_chi = 10 MeV, heavy and light mediator, from the tabulated
crystal form factor of Essig et al. [E16] (normalization and checks in si_fcrys.py). Prints every number of the example.

Rate (Limit 10.1a in book notation; [E16] Eq. (3.13) per unit target mass, N_cell/M_target = 1/M_cell):
    dR/d omega = (rho_chi / m_chi) * sigma_e * alpha m_e^2 / (M_cell mu^2) * int dq/q^2 eta(v_min) F_DM(q)^2 |f_crys(q, omega)|^2
with v_min = omega/q + q/(2 m_chi) (eq:1.3-vmin, Delta_chi = 0).
Halo (book standard, App. A.8 / [B] Baxter et al. 2105.00599 Table 1): rho_chi = 0.3 GeV/cm^3, v0 = 238, v_esc = 544,
v_E^ref = 250.5 km/s; eta(v_min) in closed form (App. D.1; same code as figscripts/ch01/fig1_9.py).
Mediators (eq:1.4-yukawa-sigma limits): F_DM = 1 (heavy), F_DM = (q0/q)^2 (light), q0 = alpha m_e.
Reference cross section: sigma_e = 1e-37 cm^2 (illustrative). Energies: the table's bins, onset at 1.2 eV (scissor gap
1.11 eV of [E16], a 300 K value; the 0 K gap of Sect. 3.3 is 1.17 eV). q sum over the table's 900 bins (up to 18 q0).
Ionization bins for orientation: n_e = 1 + floor((omega - E_g)/3.8 eV) with E_g = 1.2 eV, the binning of [E16]'s notebook
(the book's own yield model is Sect. 1.5 / Chap. 18; quoted only as the share of events below 4.9 eV).
"""
import os
import sys
import numpy as np
from scipy.special import erf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from si_fcrys import load, ALPHA, ME, M_CELL, Q0, DE  # noqa: E402

CKM = 299792.458
V0, VESC, VE = 238.0, 544.0, 250.5
RHO = 0.3e9                    # eV/cm^3
SIG = 1e-37                    # cm^2
CCMS = 2.99792458e10           # cm/s
YR = 365.25 * 86400
EV_PER_KG = 5.609588603e35     # eV per kg (c = 1)
MCHI = 10e6
Z = VESC / V0
NESC = np.pi**1.5 * V0**3 * (erf(Z) - 2 / np.sqrt(np.pi) * Z * np.exp(-Z**2))


def eta(u):
    """App. D.1 closed form at v_E^ref; argument and result in km/s and (km/s)^-1."""
    k = np.pi * V0**2 / (VE * NESC)
    u = np.maximum(u, 0.0)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + VE) / V0) - erf((u - VE) / V0)) - 2 * VE * np.exp(-Z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(Z) - erf((u - VE) / V0)) - (VESC + VE - u) * np.exp(-Z**2))
    return np.where(u < VESC - VE, b1, np.where(u < VESC + VE, b2, 0.0))


q, E, f2 = load()
dq = q[1] - q[0]
mu = MCHI * ME / (MCHI + ME)
# prefactor (rho/m) sigma alpha m_e^2/(M_cell mu^2): per second per kg; the q integral carries 1/eV, d omega carries eV
pref = (RHO / MCHI) * SIG * CCMS * ALPHA * ME**2 / mu**2 / M_CELL * EV_PER_KG * YR   # kg^-1 yr^-1 (times eV^-1 eV)
print(f"m_chi = 10 MeV: mu = {mu/1e3:.2f} keV, m_e^2/mu^2 = {ME**2/mu**2:.4f}")
print(f"rho_chi/m_chi = {RHO/MCHI:.0f} cm^-3; flux scale (rho/m) c = {RHO/MCHI*CCMS:.3e} cm^-2 s^-1")
print(f"prefactor (rho/m) sigma alpha m_e^2 /(M_cell mu^2) = {pref:.3e} kg^-1 yr^-1")

VM = (E[None, :] / q[:, None] + q[:, None] / (2 * MCHI)) * CKM
ETA = eta(VM) * CKM            # dimensionless (natural units)
print(f"eta(0) = {eta(np.array(0.0))*CKM:.1f} (natural units) = <1/v>")

for name, F2 in [("heavy", np.ones_like(q)), ("light", (Q0 / q) ** 4)]:
    integ = (dq / q[:, None] ** 2 * ETA * F2[:, None] * f2)        # eV^-1 per (q bin, omega point)
    I_om = integ.sum(0)                                            # eV^-1
    dRdw = pref * I_om                                             # kg^-1 yr^-1 eV^-1
    R = np.sum(dRdw) * DE
    jpk = np.argmax(dRdw)
    wmean = np.sum(E * dRdw) / np.sum(dRdw)
    low = np.sum(dRdw[E < 4.95]) * DE / R
    # q weight at the spectrum peak
    qw = integ[:, jpk]
    iq = np.argmax(np.convolve(qw, np.ones(5) / 5, mode="same"))
    # share of rate from q < q0 and q > 2 q0
    qs = integ.sum(1)
    sh_lo = qs[q < Q0].sum() / qs.sum()
    sh_hi = qs[q > 2 * Q0].sum() / qs.sum()
    print(f"\n{name} mediator:")
    print(f"  int d omega int dq/q^2 eta F^2 |f|^2 = {np.sum(I_om)*DE:.3e} (dimensionless)")
    print(f"  total rate above the gap R = {R:.3e} per kg-yr at sigma_e = 1e-37 cm^2 ({R/365.25:.1f} per kg-day)")
    print(f"  dR/d omega peaks at {E[jpk]:.1f} eV with {dRdw[jpk]:.3e} /kg/yr/eV; mean omega = {wmean:.2f} eV;"
          f" share below 4.9 eV = {low:.2f}")
    print(f"  at the peak energy the q integrand peaks at q = {q[iq]/Q0:.2f} q0 = {q[iq]/1e3:.2f} keV")
    print(f"  share of the rate from q < q0: {sh_lo:.2f}; from q > 2 q0: {sh_hi:.3f}")
    # largest omega with nonzero rate
    nz = np.nonzero(dRdw > 0)[0]
    print(f"  spectrum ends at {E[nz[-1]]:.1f} eV (kinematic maximum q v_max - q^2/2m at q = m v_max: "
          f"{0.5*MCHI*((VESC+VE)/CKM)**2:.1f} eV)")
