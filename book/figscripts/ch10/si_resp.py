"""The silicon response of the Chapter 21 kernel scripts (kernel21.py, hib21.py), selected by the environment variable
SI_RESP:
  lf (default)     the book's rate model;
  essig            the crystal form factor of Essig et al. (si_fcrys.load), for comparison;
  lf | rpa | ip    the Knapen-Kozaczuk-Lin GPAW tables of si_elf_binned.npz (the rate model of Sect. 10.2 / 10.10 and
                   Sect. 21.4: RPA + LF loss function, RPA loss function, IP head eps2), converted to the |f_crys|^2 of
                   [E16] Eq. (3.17) by eq:A.8-fcrys with S = (2q^2/e^2) L (eq:4.4-SL):
                       |f|^2 = Omega q^5 L / (8 pi^2 alpha^2 m_e^2)
                   and resampled on a regular cell grid: q cells of width DQ_KKL between the first and last table
                   momentum (493 eV - 22.52 keV), omega cells of width DE_KKL from the tables' gap 1.17 eV (the measured
                   T = 0 gap, as nuis21.py) to 89.2 eV, L interpolated linearly in q and omega at the cell centres.
                   Nothing below 493 eV or above 22.52 keV (the table range).
Returns the same objects as si_fcrys: load() -> q (eV, cell centres), E (eV, cell centres), f2[iq, iE]; DE is the
energy cell width.
"""
import os
import numpy as np
import si_fcrys as F

RESP = os.environ.get("SI_RESP", "lf")
ALPHA, ME, M_CELL, Q0, OMEGA = F.ALPHA, F.ME, F.M_CELL, F.Q0, F.OMEGA
EG_KKL = 1.17
DQ_KKL = float(os.environ.get("SI_DQ", "50.0"))
DE_KKL = float(os.environ.get("SI_DE", "0.01"))
EMAX = float(os.environ.get("SI_EMAX", "89.2"))

if RESP == "essig":
    DE = F.DE
else:
    DE = DE_KKL


def load():
    if RESP == "essig":
        return F.load()
    d = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "si_elf_binned.npz"))
    om, qn, L = d["omega"], d["q"], d[RESP]
    nq = int(round((qn[-1] - qn[0]) / DQ_KKL))
    dq = (qn[-1] - qn[0]) / nq
    q = qn[0] + (np.arange(nq) + 0.5) * dq
    ne = int(np.floor((min(EMAX, om[-1]) - EG_KKL) / DE_KKL))
    E = EG_KKL + (np.arange(ne) + 0.5) * DE_KKL
    Lq = np.array([np.interp(q, qn, L[i, :]) for i in range(len(om))])        # (n_om, nq)
    LqE = np.array([np.interp(E, om, Lq[:, j]) for j in range(nq)])          # (nq, nE)
    f2 = OMEGA * q[:, None] ** 5 * LqE / (8 * np.pi**2 * ALPHA**2 * ME**2)
    return q, E, f2
