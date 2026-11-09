"""Loader for the tabulated silicon crystal form factor of Sect. 10.1 (used by fig10_1.py and we10_1.py).

Source
  [E16]  R. Essig, M. Fernandez-Serra, J. Mardon, A. Soto, T. Volansky, T.-T. Yu, JHEP 05 (2016) 046, arXiv:1509.01598:
         definition Eq. (3.17), rate Eq. (3.13), binning Eq. (4.1) (500 bins of 0.1 eV in E_e, 900 bins of 0.02 alpha m_e in q),
         numerical form Eq. (4.4) (k weights summing to 2, QE convention, Eq. (4.2)); PBE bands, ultrasoft pseudopotentials,
         scissor to E_g = 1.11 eV (Sect. 4.1), 4 valence and 52 conduction bands, 70 Ry, 243 k points (Sect. 4.2).
         The tabulation was released with the paper's public analysis code (QEdark analysis notebooks, file Si_f2.txt;
         copy in book/sources/10.1/). Layout: first line "900 500", then 450000 numbers, E index fastest after the
         notebook's reshape (np.resize(..., (nE, nq)) then transpose -> T[iq, iE]).
Normalization (inferred from the released notebook and checked three ways)
  The notebook computes, per 0.1 eV energy point E_m = m dE and per q point q_i = i dq,
      rate += prefactor * Eprefactor * (1/q_i) * eta * F_DM^2 * (w_k/4) * T[i, m]
  with Eprefactor = 2 pi^2 / (alpha m_e^2 Omega) = 2.0 eV (Si; [E16] text below Eq. (3.17)), w_k = 2/137, and it sums
  these per-point values over a bin without a factor dE: its "dR/dE" is a rate per 0.1 eV point. Comparing with
  Eq. (3.13) per unit energy, dR/dE = (rho/m)(sigma alpha m_e^2 / M_cell mu^2) int dq/q^2 eta F^2 |f_crys|^2, gives
      |f_crys(q_i, E_m)|^2 = Eprefactor * (w_k/4) * i * T[i, m] / (dE / 1 eV) .
  Check 1: with the notebook's own halo (rho = 0.4 GeV/cm^3, v0 = 220, vE = 232, vesc = 544 km/s), m_chi = 10 MeV,
           sigma_e = 1e-37 cm^2, F_DM = 1, the 1.2-4.9 eV bin, this reproduces the notebook's printed 75276.69 events/kg/yr
           to all printed digits (scratch check; same loops and float binning as the notebook).
  Check 2: f-sum rule eq:4.3-fsum with the valence density 8/Omega: first moment of S-bar over 0-50 eV, divided by
           pi n_e q^2/m_e, is printed by fig10_1.py (about 1.0 at q0).
  Check 3: pointwise against the book's empirical-pseudopotential S0 at q0 along [100] (figscripts/ch08/we8_10.py,
           NK = 20): within about 10-20 percent at 5-20 eV (printed by fig10_1.py).
Conversions (eq:A.8-fcrys): Omega * S-bar = 4 pi alpha m_e^2 |f_crys|^2 / q^3 ; eps2 = 8 pi^2 alpha^2 m_e^2 |f|^2/(q^5 Omega).
The table's own unit alpha m_e uses alpha = 1/137, m_e = 0.511 MeV (the notebook's constants); physics below uses CODATA.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TABLE = os.path.join(HERE, "..", "..", "sources", "10.1", "Si_f2.txt")

NQ, NE = 900, 500
ALPHA_TAB, ME_TAB = 1 / 137.0, 0.511e6          # notebook constants, define the table's q unit
DQ = 0.02 * ALPHA_TAB * ME_TAB                     # eV (74.6 eV)
DE = 0.1                                           # eV
WK = 2 / 137.0                                     # notebook k weight
EPREF = 2.0                                        # eV, 2 pi^2/(alpha m_e^2 Omega) for Si [E16]

ALPHA = 1 / 137.035999177                          # CODATA 2022
ME = 510998.95                                     # eV, CODATA 2022
HBARC = 1973.269804                                # eV Angstrom
A_SI = 5.431                                       # Angstrom (Sect. 1.3)
OMEGA = A_SI**3 / 4 / HBARC**3                     # eV^-3 (40.05 A^3)
M_CELL = 2 * 28.0855 * 931.49410242e6              # eV (52.33 GeV; Sect. 1.5)
Q0 = ALPHA * ME                                    # 3.73 keV


def load():
    """Return q (eV), E (eV), |f_crys|^2 [iq, iE] in the normalization of [E16] Eq. (3.17)."""
    T = np.loadtxt(TABLE, skiprows=1)
    T = np.transpose(np.resize(T, (NE, NQ)))
    i = np.arange(1, NQ + 1)
    q = i * DQ
    E = np.arange(1, NE + 1) * DE
    f2 = EPREF * (WK / 4) * T * i[:, None] / DE
    return q, E, f2


def omega_sbar(q, f2):
    """Omega * S-bar(q, omega) in eV^-1 (eq:A.8-fcrys)."""
    return 4 * np.pi * ALPHA * ME**2 * f2 / q[:, None] ** 3
