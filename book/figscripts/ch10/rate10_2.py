"""Shared inputs of the Sect. 10.2 scripts: constants, halo, the binned silicon loss functions and the rate integral.
Natural units hbar = c = 1, Heaviside-Lorentz e^2 = 4 pi alpha; energies and momenta in eV.

Rate (Sect. 10.2, keyresult eq:10.2-rate; isotropic target, T = 0):
  dR/domega = rho_chi sigma_e / (8 pi^2 alpha rho_T m_chi mu^2) * int dq q^3 eta(v_min) F_DM(q)^2 L(q, omega),
  v_min = omega/q + q/(2 m_chi)  (Sect. 1.3, Delta_chi = 0).
  This is eq:1.5-rate with S = (2q^2/e^2) L (eq:4.4-SL); it agrees with Knapen et al. arXiv:2101.08275 Eq. (13) after
  the angular integral and with Barker et al. arXiv:2608.05282 Eq. (4).
Inputs
  [CODATA 2018] alpha = 1/137.035999084, m_e = 510998.95 eV, hbar c = 1973.269804 eV A, 1 eV = 1.519267e15 s^-1,
     1 kg = 5.609589e35 eV, 1 yr = 3.15576e7 s, 1 cm = 5.067731e4 eV^-1.
  [Baxter et al., arXiv:2105.00599, Table 1] v0 = 238, v_esc = 544 km/s; v_E = 250.5 km/s (book value, Sect. 1.2);
     rho_chi = 0.3 GeV cm^-3 (book value, Sect. 1.2).
  [eta] closed form of App. D.1 (same function as figscripts/ch01/fig1_9.py).
  Silicon: rho_T = 2.33 g cm^-3 (Sect. 1.2); a = 5.431 A, Omega = a^3/4; M_Si = 26.16 GeV (Sect. 5.3 uses M_cell =
     52.33 GeV); gap E_g = 1.11 eV (Sect. 1.4); omega_p = 16.6 eV valence, 31.1 eV all electrons (Sect. 4.3).
  Loss functions: si_elf_binned.npz, from si_elf_reduce.py (Knapen-Kozaczuk-Lin GPAW tables, see that script).
"""
import os
import numpy as np
from scipy.special import erf

HERE = os.path.dirname(os.path.abspath(__file__))
ALPHA = 1 / 137.035999084
ME = 510998.95
HBARC = 1973.269804           # eV A
CKM = 299792.458
EV_S = 1.519267e15            # s^-1 per eV
KG_EV = 5.609589e35
YR_S = 3.15576e7
CM = 5.067731e4               # eV^-1
V0, VESC, VE = 238.0, 544.0, 250.5
VMAX = (VESC + VE) / CKM      # 2.650e-3
RHO_CHI = 0.3e9 / CM**3        # 0.3 GeV cm^-3 in eV^4
RHO_T = 2.33e-3 * KG_EV / CM**3   # 2.33 g cm^-3 in eV^4
EG = 1.11
A_SI = 5.431
OMEGA_CELL = A_SI**3 / 4 / HBARC**3       # eV^-3
M_SI = 26.16e9
WP_VAL, WP_ALL = 16.6, 31.1
Q0 = ALPHA * ME
SIGMA_REF = 1e-37 * CM**2                 # reference cross section 1e-37 cm^2 in eV^-2

_Z = VESC / V0
_NESC = np.pi**1.5 * V0**3 * (erf(_Z) - 2 / np.sqrt(np.pi) * _Z * np.exp(-_Z**2))


def eta(vmin):
    """Mean inverse speed above v_min (App. D.1); v_min dimensionless (units of c); returns 1/v in units of 1/c."""
    u = np.maximum(np.asarray(vmin) * CKM, 0.0)
    k = np.pi * V0**2 / (VE * _NESC)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + VE) / V0) - erf((u - VE) / V0)) - 2 * VE * np.exp(-_Z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(_Z) - erf((u - VE) / V0)) - (VESC + VE - u) * np.exp(-_Z**2))
    return np.where(u < VESC - VE, b1, np.where(u < VESC + VE, b2, 0.0)) * CKM


def load():
    d = np.load(os.path.join(HERE, "si_elf_binned.npz"))
    return {k: d[k] for k in d.files}


def prefactor(m):
    mu = m * ME / (m + ME)
    return RHO_CHI * SIGMA_REF / (8 * np.pi**2 * ALPHA * RHO_T * m * mu**2)


def to_per_kg_yr(x):
    """Rate per unit target mass in natural units (dimensionless) -> events kg^-1 yr^-1."""
    return x * EV_S * KG_EV * YR_S


def fdm2(q, light):
    return (Q0 / q)**4 if light else np.ones_like(q)


def spectrum(m, resp, data, light=False, wfine=None):
    """dR/domega [events kg^-1 yr^-1 eV^-1] at sigma_e = 1e-37 cm^2 on the energy grid wfine (default: data grid
    from E_g); resp = 'ip' (S from eps2 of the head), 'rpa' or 'lf' (loss functions).  The IP structure factor is
    (2q^2/e^2) eps2, the same prefactor as the loss function, so one formula serves all three."""
    om, q = data["omega"], data["q"]
    r = data[resp]                              # shape (n_omega, n_q)
    if wfine is None:
        wfine = np.arange(EG, om[-1], 0.05)
    rf = np.array([np.interp(wfine, om, r[:, j]) for j in range(len(q))]).T
    W, Q = np.meshgrid(wfine, q, indexing="ij")
    vmin = W / Q + Q / (2 * m)
    integrand = Q**3 * eta(vmin) * fdm2(Q, light) * rf
    dRdw = np.trapezoid(integrand, q, axis=1) * prefactor(m)
    return wfine, to_per_kg_yr(dRdw)


def total(m, resp, data, light=False, wth=EG):
    w, s = spectrum(m, resp, data, light)
    s = np.where(w >= wth, s, 0.0)
    return np.trapezoid(s, w)


# --- sum-rule bounds and the acoustic peak of an electron-only coupling (Sect. 10.2, Limit 10.2b, WE 10.2) ----------
C_LA = 8.43 / CKM               # longitudinal sound speed of Si along [100], 8.43 km/s (App. C.18, Sect. 5.2)
N_E_CELL = 28.0                 # electrons per two-atom cell that follow the nuclei at q -> 0: Z = 14 per atom, Z* = 0
M_CELL = 2 * M_SI
Q_X = 2 * np.pi / A_SI * HBARC  # |Gamma-X| = 2 pi / a = 2.283 keV: cutoff of the linear LA model
OMEGA_PE = np.sqrt(4 * np.pi * ALPHA * N_E_CELL**2 / (OMEGA_CELL * M_CELL))   # e^2 n_e^2 / rho_T, all electrons


def coeff(m):
    """C of the bound: R = C int dq q^3 F^2 int domega eta L (natural units)."""
    mu = m * ME / (m + ME)
    return RHO_CHI * SIGMA_REF / (8 * np.pi**2 * ALPHA * RHO_T * m * mu**2)


def eta_max(q, m, n, wth, npts=4000):
    """max over wth <= omega <= q v_max of omega^(-n) eta(v_min(q, omega)); zero if the window is closed."""
    q = np.atleast_1d(q)
    out = np.zeros_like(q, dtype=float)
    for i, qq in enumerate(q):
        wmax = qq * VMAX - qq**2 / (2 * m)
        if wmax <= wth:
            continue
        w = np.geomspace(wth, wmax, npts)
        out[i] = np.max(w**(-n) * eta(w / qq + qq / (2 * m)))
    return out


def phonon_dRdq(q, m, light=False):
    """Per-q rate [natural units per eV of q] of the acoustic peak of an electron-only coupling: isotropic linear LA
    branch omega = c_LA q up to |q| = Q_X, electron-following charge N_E_CELL per cell, no Debye-Waller factor and no
    Umklapp (modelling choices).  S = 2 pi N^2 q^2/(2 M_cell omega_q Omega) delta(omega - omega_q), so
    int domega L = pi e^2 N^2 / (2 M_cell Omega omega_q)."""
    q = np.asarray(q, dtype=float)
    wq = C_LA * q
    intL = np.pi * 4 * np.pi * ALPHA * N_E_CELL**2 / (2 * M_CELL * OMEGA_CELL * wq)
    vmin = C_LA + q / (2 * m)
    val = coeff(m) * q**3 * fdm2(q, light) * eta(vmin) * intL
    return np.where(q <= Q_X, val, 0.0)
