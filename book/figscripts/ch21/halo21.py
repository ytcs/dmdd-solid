"""Shared halo functions for the Chapter 21 scripts (limit21_1a.py, fig21_1.py, we21_1.py).

Sources
  [B]   D. Baxter et al., Eur. Phys. J. C 81, 907 (2021), arXiv:2105.00599: Table 1 (rho = 0.3 GeV/cm^3, v0 = 238 km/s,
        v_esc = 544 km/s, LSR (0, 238, 0) + peculiar (11.1, 12.2, 7.3) km/s), Eq. (11) (Earth orbit, 29.8 km/s,
        t in days from 22 March). Book: Sect. 1.2, eq:1.2-vsun, eq:1.2-vorb; App. A.8 (v_E^ref = 250.5 km/s).
  [E16] R. Essig et al., JHEP 05 (2016) 046, arXiv:1509.01598, App. B, Eqs. (B.4)-(B.5): eta(v_min) of the truncated
        Maxwellian, the same branches as App. D.1 (eq:D.1-eta1, eq:D.1-eta2).
  [KLS] M. Kuhlen, M. Lisanti, D. N. Spergel, Phys. Rev. D 86, 063505 (2012), arXiv:1202.0007: debris-flow model,
        Eq. (7) (Earth-frame speed distribution of an isotropic shell of galactic speed v_flow), Eq. (8) (its g(v_min),
        the book's eta), Eq. (10) (two-component halo with density fraction eps), v_flow = 340 km/s and eps = 0.22
        from the Via Lactea II simulation (text below Fig. 6 and Fig. 6 caption).
"""
import numpy as np
from scipy.special import erf

CKM = 299792.458                      # km/s
V0, VESC = 238.0, 544.0               # km/s [B]
VSUN = np.array([11.1, 250.2, 7.3])   # km/s, eq:1.2-vsun
VE_REF = 250.5                        # km/s, |v_sun| rounded (App. A.8)
VMAX = VESC + VE_REF                  # 794.5 km/s
VORB = 29.8                           # km/s [B Eq. (13)]
E1 = np.array([0.9941, 0.1088, 0.0042])
E2 = np.array([-0.0504, 0.4946, -0.8677])
OMEGA_YR = 2 * np.pi / 365.25         # 1/d
Z = VESC / V0
N_ESC = np.pi**1.5 * V0**3 * (erf(Z) - 2 / np.sqrt(np.pi) * Z * np.exp(-Z**2))
V_FLOW, EPS_DF = 340.0, 0.22          # km/s, 1 [KLS]


def eta_shm(u, ve=VE_REF, vesc=VESC):
    """App. D.1 closed form, all branches, in (km/s)^-1; vesc = inf gives the untruncated Maxwellian."""
    u = np.maximum(np.asarray(u, dtype=float), 0.0)
    if np.isinf(vesc):
        return (erf((u + ve) / V0) - erf((u - ve) / V0)) / (2 * ve)
    z = vesc / V0
    nesc = np.pi**1.5 * V0**3 * (erf(z) - 2 / np.sqrt(np.pi) * z * np.exp(-z**2))
    k = np.pi * V0**2 / (ve * nesc)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + ve) / V0) - erf((u - ve) / V0)) - 2 * ve * np.exp(-z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(z) - erf((u - ve) / V0)) - (vesc + ve - u) * np.exp(-z**2))
    return np.where(u < vesc - ve, b1, np.where(u < vesc + ve, b2, 0.0))


def fspeed_shm(v, ve=VE_REF):
    """Laboratory speed distribution, eq:1.2-Fspeed (D.1 form), in (km/s)^-1."""
    v = np.asarray(v, dtype=float)
    k = np.pi * V0**2 / (ve * N_ESC)
    hi = np.where(v < VESC - ve, np.exp(-(v + ve)**2 / V0**2), np.exp(-Z**2))
    out = k * v * (np.exp(-(v - ve)**2 / V0**2) - hi)
    return np.where(v < VESC + ve, np.maximum(out, 0.0), 0.0)


def eta_df(u, ve=VE_REF, vf=V_FLOW):
    """[KLS] Eq. (8): eta of an isotropic shell of galactic speed vf, in (km/s)^-1."""
    u = np.asarray(u, dtype=float)
    mid = (vf + ve - u) / (2 * vf * ve)
    return np.where(u < vf - ve, 1 / vf, np.where(u < vf + ve, mid, 0.0)) if vf > ve else None


def fspeed_df(v, ve=VE_REF, vf=V_FLOW):
    """[KLS] Eq. (7), in (km/s)^-1 (valid for vf > ve)."""
    v = np.asarray(v, dtype=float)
    return np.where((v > vf - ve) & (v < vf + ve), v / (2 * vf * ve), 0.0)


def vE_of_t(t):
    """|v_E(t)| in km/s, eq:1.2-vE with eq:1.2-vorb (circular orbit), t in days from 22 March."""
    t = np.atleast_1d(t)
    v = VSUN[None, :] + VORB * (np.cos(OMEGA_YR * t)[:, None] * E1 + np.sin(OMEGA_YR * t)[:, None] * E2)
    return np.linalg.norm(v, axis=1)
