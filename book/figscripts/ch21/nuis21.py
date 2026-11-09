"""Shared module of Sect. 21.4: the silicon electron-recoil rate at its central value and its four theory nuisances,
as functions of the dark-matter mass.  Imported by fig21_4.py and we21_4.py; prints nothing on import.

The rate and the nuisances are those of Sect. 10.10 (figscripts/ch10/nuis10_10.py), evaluated at any mass with the same
inputs and the same modelling choices:
  rate10_2.py         constants, standard halo (rho_chi = 0.3 GeV/cm^3, v0 = 238, v_esc = 544, v_E = 250.5 km/s), eta of
                      App. D.1, the loss-function rate eq:10.2-rate.
  si_elf_binned.npz   GPAW tables of Knapen, Kozaczuk and Lin (arXiv:2101.08275) via DarkELF: IP head, RPA, RPA + LF loss
                      functions, direction-averaged, q <= 22.5 keV, omega <= 89 eV.  The tables carry a scissor to the
                      measured gap at T = 0 (arXiv:2101.08275 Sect. III B: "a scissor correction is applied to match the
                      experimentally measured Si and Ge bandgaps at T = 0"), i.e. 1.17 eV; the 1.11 eV of the DarkELF
                      constants file is the step-model conversion constant (with eps = 3.6 eV), not the gap of the tables.
                      The omega nodes are 0.2 eV apart (first nonzero node 1.043 eV) and do not resolve the edge.
  si_fcrys.py         crystal form factor of Essig et al. (arXiv:1509.01598), onset 1.2 eV (normalization of Sect. 10.1).
Central value: RPA + LF tables as published (no shift: their scissor already gives the low-temperature gap), counted from
  the one-pair threshold omega >= E_g = 1.17 eV.  (An earlier version shifted the spectrum by a further 0.06 eV; that
  double-counted the cold gap and is removed.)
Nuisances (templates of Sect. 10.10; each enters as c_k = ln(rate at theta_k = 1 / central rate)):
  attraction (RPA + LF -> BSE): delta_X = +0.28 for omega <= 10.5 eV, the model window of Sect. 10.10 (largest energy at
     3 MeV); above 10.5 eV the template is set to zero.  For m_chi > 3 MeV this omits the compensating loss that the
     f-sum rule eq:8.8-fsum puts above the window, so it overstates |c_X| there (modelling choice, stated in the caption).
  gap (non-rigid scissor): spectrum and threshold shifted up by 0.10 eV.
  large-q local fields: RPA in place of RPA + LF for q > 2 q0 = 7.46 keV.
  tabulation spread: ratio of the two independent-particle rates (Essig table / KKL IP head), each table from its own
     onset, minus one, as in Sect. 10.10 (carried there as an upper bound for the screened rate).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
import rate10_2 as R  # noqa: E402
from si_fcrys import load as fload, M_CELL, Q0 as Q0F, DE  # noqa: E402

D = R.load()
Q, OM = D["q"], D["omega"]
EG_TAB = EG_PHYS = 1.17          # the tables' gap is the measured T = 0 gap (scissor of arXiv:2101.08275 Sect. III B)
DSHIFT = 0.0
WX, DELTA_X = 10.5, 0.28          # attraction template window and size (Sect. 10.10)
DGAP = 0.10                       # gap nuisance (Sect. 10.10)
Q2 = 2 * R.Q0                     # 7.46 keV
YR_EXPO = 1.0                     # exposure, kg yr
SIG_REF = 1e-37                   # cm^2, the reference cross section of the rates
_QF, _EF, _F2 = fload()
_DQF = _QF[1] - _QF[0]


def spec(m, resp="lf", light=False, dE=DSHIFT, qcut=None):
    """dR/domega [per kg yr eV] at sigma_e = 1e-37 cm^2, spectrum shifted up by dE and counted from the shifted gap.
    qcut = (qlo, qhi) restricts the q integral."""
    w = np.arange(EG_TAB + dE, OM[-1] + dE, 0.01)
    r = D[resp]
    rf = np.array([np.interp(w - dE, OM, r[:, j], left=0.0) for j in range(len(Q))]).T
    W, QQ = np.meshgrid(w, Q, indexing="ij")
    integ = QQ**3 * R.eta(W / QQ + QQ / (2 * m)) * R.fdm2(QQ, light) * rf
    if qcut is not None:
        integ = np.where((QQ >= qcut[0]) & (QQ < qcut[1]), integ, 0.0)
    return w, R.to_per_kg_yr(np.trapezoid(integ, Q, axis=1) * R.prefactor(m))


def tot(m, **kw):
    w, s = spec(m, **kw)
    return np.trapezoid(s, w)


def essig_total(m, light=False):
    """Rate from the Essig et al. table from its own onset (Sect. 10.10, nuis10_10.py)."""
    mu = m * R.ME / (m + R.ME)
    pref = (0.3e9 / m) * SIG_REF * 2.99792458e10 * R.ALPHA * R.ME**2 / mu**2 / M_CELL * 5.609588603e35 * 365.25 * 86400
    vm = _EF[None, :] / _QF[:, None] + _QF[:, None] / (2 * m)
    F2 = (Q0F / _QF) ** 4 if light else np.ones_like(_QF)
    integ = _DQF / _QF[:, None] ** 2 * R.eta(vm) * F2[:, None] * _F2
    return pref * integ.sum() * DE


def nuisances(m, light=False):
    """Central rate [per kg yr at 1e-37 cm^2] and the dictionary of c_k = ln(1 + delta_k) on the rate."""
    w, s = spec(m, light=light)
    rc = np.trapezoid(s, w)
    fx = np.trapezoid(np.where(w <= WX, s, 0.0), w) / rc
    c = {}
    c["attraction"] = np.log(1 + DELTA_X * fx)
    c["gap"] = np.log(tot(m, light=light, dE=DSHIFT + DGAP) / rc)
    hi_lf = tot(m, light=light, qcut=(Q2, 1e9))
    hi_rpa = tot(m, resp="rpa", light=light, qcut=(Q2, 1e9))
    c["large-q LF"] = np.log(1 + (hi_rpa - hi_lf) / rc)
    ip = R.total(m, "ip", D, light)
    c["tabulation"] = np.log(essig_total(m, light) / ip) if ip > 0 else np.nan
    return rc, c, fx


def mmin(eg):
    return 2 * eg / R.VMAX**2 / 1e6


# --- statistics ---------------------------------------------------------------------------------------------------
N90 = np.log(10.0)                # 2.303, eq:1.5-N90
TSTAR = 2 * N90                   # calibrated threshold of the zero-count statistic (Sect. 8.8; comparison only)


def profile_ratio(sig, nup=N90):
    """Profiled limit over nominal in the book's construction (Sect. 21.5, we21_5.py): Neyman construction with each
    nuisance at its conditional best fit to the observed counts, constraint term held fixed.  One bin, zero counts, any
    background: the p-value is exp(-(u e^{k theta} + b)) with theta = -k u e^{k theta} at the conditional best fit, so the
    effective signal u e^{k theta} must equal the classical N^up, and u/N^up = exp(sig^2 N^up) exactly (sig = sigma_beta,
    all nuisances along beta)."""
    return np.exp(sig**2 * nup)


def fixed_threshold_ratio(sig, tstar=TSTAR):
    """Exact zero-count, zero-background profiled limit over nominal for one lognormal nuisance of log-width sig,
    threshold tstar (eq:8.8-cost): 2 w e^w / (sig^2 t*), w = sqrt(1 + sig^2 t*) - 1."""
    if sig == 0:
        return 1.0
    w = np.sqrt(1 + sig**2 * tstar) - 1
    return 2 * w * np.exp(w) / (sig**2 * tstar)
