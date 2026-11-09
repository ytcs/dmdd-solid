"""Rate kernel of the silicon electron-recoil channel from the tabulated crystal form factor (Sect. 21.1; used by
fig21_1.py and we21_1.py).

For an angle-averaged response the kernel of eq:21.1-functional depends on the speed only,
    k(v) = (rho_chi / m_chi rho_T) Gamma(v) = P(m_chi) * C(v) / v ,      (v in units of c)
    C(v) = int d omega int dq/q^2 F_DM(q)^2 |f_crys(q, omega)|^2 Theta(v - v_min(q, omega)) ,
    P(m_chi) = rho_chi sigma_e alpha m_e^2 / (m_chi M_cell mu_chi e^2),
which follows from lim:10.1a (Essig et al. [E16] Eqs. (3.13), (3.17) per unit target mass) with eta(v_min) replaced by
Theta(v - v_min)/v, the integrand of eq:1.3-eta. Then R = int dv F_chi(v) k(v) for any speed distribution, and
R = P * sum_bins w_bin eta(v_min,bin) for any eta, w_bin = dq d omega F^2 |f|^2 / q^2.
Table: figscripts/ch10/si_fcrys.py (normalization and its checks); onset 1.2 eV (scissor gap 1.11 eV of [E16]).
Halo inputs: rho_chi = 0.3 GeV/cm^3 ([B] Table 1).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
from si_fcrys import load, ALPHA, ME, M_CELL, Q0, DE  # noqa: E402

RHO = 0.3e9                    # eV/cm^3 [B]
SIG = 1e-37                    # cm^2, illustrative (as WE 10.1)
CCMS = 2.99792458e10
YR = 365.25 * 86400
EV_PER_KG = 5.609588603e35
CKM = 299792.458

_q, _E, _f2 = load()
_dq = _q[1] - _q[0]


def prefactor(mchi):
    mu = mchi * ME / (mchi + ME)
    return (RHO / mchi) * SIG * CCMS * ALPHA * ME**2 / mu**2 / M_CELL * EV_PER_KG * YR   # kg^-1 yr^-1


def bins(mchi, mediator="heavy"):
    """Return v_min (km/s) and weights w (dimensionless) of all table bins, flattened."""
    F2 = np.ones_like(_q) if mediator == "heavy" else (Q0 / _q) ** 4
    w = (_dq * DE / _q[:, None] ** 2 * F2[:, None] * _f2)
    vm = (_E[None, :] / _q[:, None] + _q[:, None] / (2 * mchi)) * CKM
    return vm.ravel(), w.ravel()


def cumulative(mchi, v, mediator="heavy"):
    """C(v) on an array of speeds v (km/s)."""
    vm, w = bins(mchi, mediator)
    o = np.argsort(vm)
    cs = np.concatenate([[0.0], np.cumsum(w[o])])
    return cs[np.searchsorted(vm[o], v, side="right")]


def kernel(mchi, v, mediator="heavy"):
    """k(v) in kg^-1 yr^-1 at sigma_e = 1e-37 cm^2; v in km/s."""
    v = np.asarray(v, dtype=float)
    return prefactor(mchi) * cumulative(mchi, v, mediator) / np.maximum(v / CKM, 1e-300)


def rate_eta(mchi, eta_fun, mediator="heavy"):
    """R = P sum w eta(v_min) for an eta given in (km/s)^-1; returns kg^-1 yr^-1."""
    vm, w = bins(mchi, mediator)
    return prefactor(mchi) * np.sum(w * eta_fun(vm) * CKM)


def spectrum_eta(mchi, eta_fun, mediator="heavy"):
    """dR/d omega on the table's energy points (kg^-1 yr^-1 eV^-1)."""
    F2 = np.ones_like(_q) if mediator == "heavy" else (Q0 / _q) ** 4
    vm = (_E[None, :] / _q[:, None] + _q[:, None] / (2 * mchi)) * CKM
    integ = _dq / _q[:, None] ** 2 * F2[:, None] * _f2 * eta_fun(vm) * CKM
    return _E, prefactor(mchi) * integ.sum(0)


def vth(mchi):
    """Smallest v_min (km/s) over the bins with nonzero weight."""
    vm, w = bins(mchi)
    return vm[w > 0].min()
