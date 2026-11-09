"""Shared functions for the halo-independent bounds of Sect. 21.2 (fig21_2.py, we21_2.py, limit21_2a.py).

Objects (book notation, App. C.12 and Sect. 21.2):
  stream kernel k_n(v)      expected count in pair bin n from a single stream of laboratory velocity v, per unit
                            measure Xi = (rho_chi sigma_e / m_chi) f d^3v (so that int dXi Theta(|v|-u0)/|v| = eta-tilde(u0)),
  step column  A_n(v)       = |v| k_n(v) for an angle-averaged response: the count in bin n for eta-tilde(u) = Theta(v - u)
                            (one unit of eta-tilde, in yr^-1, below the speed v); A_n has units of yr for an exposure in kg yr.
Electron-recoil channel of silicon, heavy mediator (F_DM = 1), from the tabulated crystal form factor of Essig et al.
  [E16] R. Essig et al., JHEP 05 (2016) 046, arXiv:1509.01598, Eqs. (3.13), (3.17) (lim:10.1a), loaded and normalized by
        figscripts/ch10/si_fcrys.py (its docstring gives the normalization checks). Rate per unit eta-tilde:
        N_n = Expo * alpha m_e^2 / (M_cell mu^2) * sum_{omega in bin n} d omega sum_q dq / q^2 |f_crys|^2 eta-tilde(v_min),
        v_min = omega/q + q/2m (eq:1.3-vmin). Replacing eta-tilde by Theta(v - v_min) gives A_n(v).
Pair bins: the energy-only cascade of Sect. 18.3, the book's calibrated model (E_g = 1.160 eV at 123 K, eps_eh = 3.749 eV),
  P_casc(N | omega) for the dark-matter seed (figscripts/ch18/casc18_3.json, key DM/P, omega = 1.41-21.16 eV in 0.25 eV
  steps; computed by casc18_3.py).  A table energy E_m = m x 0.1 eV contributes to bin n with weight P_casc(n | E_m),
  interpolated linearly in omega; P(1) = 1 for E_g <= E < 1.41 eV (the table itself has P(1) = 1
  up to 2.4 eV); for E above 21.16 eV the weights of N <= 3 are set to zero (P(3) = 8e-4 at 21.16 eV
  and falling); entries below 1e-6 (round-off of the root-of-unity extraction, down to
  -1e-16) are set to zero.  Caveats (stated in the text): the cascade gap 1.160 eV
  against the table scissor 1.11 eV, and a seed computed at q0 along [100] applied at all q.
  The step model eq:1.5-step (E_g = 1.11 eV, eps_eh = 3.6 eV, Sect. 1.5) is kept as MODEL = "step" for comparison.
Halo for comparisons: the book's standard halo (App. A.8; Baxter et al. arXiv:2105.00599 Table 1), eta in the closed form of
  App. D.1 at v_E^ref = 250.5 km/s (figscripts/ch21/halo21.py, eta_shm).
Directional extension (limit21_2a.py): the direction dependence of the silicon response is taken from the cubic-harmonic
  components of the independent-particle structure factor S0 of the empirical-pseudopotential model of Sect. 11.7
  (figscripts/ch11/elf11_7_Si_NK12*.npz: ten wedge directions, q = 0.15-2.8 q0, 1-eV bins centred on 2..14 eV, fitted with
  l = 0, 4, 6, 8 by aniso11.fit_cubic), as the ratios a_l(q, omega) = sqrt(4 pi) c_l / c_0, applied to the tabulated
  angle-average: S(q, omega, qhat) = Sbar(q, omega) [1 + sum_l a_l(q, omega) Y^c_l(qhat)]. a_l is interpolated linearly in
  ln q and in omega between bin centres and held at the end values outside the model range (q < 0.15 q0, q > 2.8 q0,
  omega < 2 eV). This is a labelled model: model gap 0.82 eV, no local fields.
  For a stream along vhat with speed v, the energy delta function puts qhat on the circle qhat.vhat = v_min/v, and the circle
  average of Y^c_l is P_l(v_min/v) Y^c_l(vhat) (addition theorem, App. C.3), so
        k_n(v, vhat) = K0_n(v) + sum_l K_l,n(v) Y^c_l(vhat),
        K_l,n(v) = (P/v) sum dq d omega q^-2 |f|^2 a_l P_l(v_min/v) Theta(v - v_min)       (a_0 = 1).
  check_circle() verifies the identity by direct quadrature over the circle.
"""
import os
import sys
import numpy as np
from scipy.special import eval_legendre

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
from si_fcrys import load, ALPHA, ME, M_CELL, Q0, DE  # noqa: E402
import halo21 as H  # noqa: E402

CKM = 299792.458
YR = 365.25 * 86400
EV_PER_KG = 5.609588603e35
EG, EPS = 1.160, 3.749          # eV, cascade of Sect. 18.3 (calibrated pair energy)
EG_STEP, EPS_STEP = 1.11, 3.6   # eV, step model of Sect. 1.5 (eq:1.5-step), comparison only
MODEL = "casc"
EXPO = 1.0                      # kg yr
NUP = np.log(30.0)              # 3.401: Poisson zero-event upper count at 96.7 % per bin; three bins -> >= 90 % jointly
LS = (4, 6, 8)

_q, _E, _f2 = load()
_dq = _q[1] - _q[0]


def pref(m):
    """Expo * alpha m_e^2 / (M_cell mu^2) in yr (count per unit eta-tilde in yr^-1)."""
    mu = m * ME / (m + ME)
    return EXPO * ALPHA * ME**2 / mu**2 / (M_CELL / EV_PER_KG)


def bin_index(E):
    """Step-model bin (comparison only)."""
    return np.where(E >= EG_STEP, 1 + np.floor((E - EG_STEP) / EPS_STEP), 0).astype(int)


_CASC = None


def pbin(nbin, E=None, model=None):
    """Probability P(nbin | E) that a deposit E lands in pair bin nbin (cascade of Sect. 18.3, or the step model)."""
    global _CASC
    E = _E if E is None else np.asarray(E, float)
    model = MODEL if model is None else model
    if model == "step":
        return (bin_index(E) == nbin).astype(float)
    if _CASC is None:
        import json
        d = json.load(open(os.path.join(HERE, "..", "ch18", "casc18_3.json")))
        P = np.array(d["DM"]["P"])
        _CASC = (np.array(d["omega"]), np.where(P < 1e-6, 0.0, P))
    om, P = _CASC
    p = np.interp(E, om, P[:, nbin])
    p = np.where(E < om[0], 1.0 if nbin == 1 else 0.0, p)
    p = np.where(E > om[-1], 0.0 if nbin <= 3 else p, p)
    return np.where(E >= EG, p, 0.0)


def cells(m, nbin, model=None):
    """v_min (km/s) and weights (pref * dq dE |f|^2 / q^2 * P(nbin|E)) of the table cells that reach pair bin nbin."""
    pb = pbin(nbin, model=model)
    sel = pb > 0
    E = _E[sel]
    w = pref(m) * _dq * DE * _f2[:, sel] / _q[:, None]**2 * pb[sel][None, :]
    vm = (E[None, :] / _q[:, None] + _q[:, None] / (2 * m)) * CKM
    return vm, w, E


def column(m, nbin, v, model=None):
    """Step column A_n(v) in yr, on an array of speeds v (km/s): cumulative weight of cells with v_min <= v."""
    vm, w, _ = cells(m, nbin, model)
    vm, w = vm.ravel(), w.ravel()
    o = np.argsort(vm)
    cs = np.concatenate([[0.0], np.cumsum(w[o])])
    return cs[np.searchsorted(vm[o], np.asarray(v, float), side="right")]


def counts_eta(m, nbin, eta_kms, model=None):
    """N_n for a given eta-tilde(v_min) function returning yr^-1 (argument km/s)."""
    vm, w, _ = cells(m, nbin, model)
    return np.sum(w * eta_kms(vm))


def etatilde_unit(m, sigma=1.0):
    """Factor turning eta in (km/s)^-1 into eta-tilde in yr^-1: rho_chi sigma_e / m_chi with c factors (sigma in cm^2)."""
    rho = 0.3e9                                     # eV/cm^3
    return (rho / m) * sigma * 2.99792458e10 * YR * CKM   # (cm^-3)(cm^2)(cm/s)(s/yr) x (km/s per c): eta[(km/s)^-1]*CKM = eta_nat


# ---------------------------------------------------------------- directional model
def _aniso_ratios():
    import aniso11 as AN
    zs = [np.load(os.path.join(HERE, "..", "ch11", "elf11_7_Si_NK12%s.npz" % t)) for t in ("_lowq", "")]
    Q = np.concatenate([z["Q"] for z in zs])
    S = np.concatenate([z["S0"] for z in zs], axis=1)
    o = np.argsort(Q)
    Q, S = Q[o], S[:, o]
    c, res = AN.fit_cubic(zs[0]["DIRS"], S)
    a = {l: np.sqrt(4 * np.pi) * c[l] / c[0] for l in LS}
    return Q, zs[0]["BIN"], a, res


_AQ, _AB, _A, _ARES = None, None, None, None


def aniso_on_table():
    """a_l(q_i, E_m) on the full table grid."""
    global _AQ, _AB, _A, _ARES
    if _A is None:
        _AQ, _AB, _A, _ARES = _aniso_ratios()
    lq = np.log(np.clip(_q / Q0, _AQ[0], _AQ[-1]))
    lQ = np.log(_AQ)
    Ec = np.clip(_E, _AB[0], _AB[-1])
    out = {}
    for l in LS:
        tmp = np.array([np.interp(lq, lQ, _A[l][:, j]) for j in range(len(_AB))])   # (nbin, nq)
        out[l] = np.array([np.interp(Ec, _AB, tmp[:, i]) for i in range(len(_q))])  # (nq, nE)
    return out


def multipole_kernels(m, nbin, v, a=None, scale=1.0):
    """K0_n(v), K_l,n(v) (yr per unit Xi, i.e. count per unit eta-tilde x speed in natural units) on speeds v (km/s).
    k_n(v, vhat) = K0 + sum_l K_l Y^c_l(vhat).  scale multiplies every a_l."""
    if a is None:
        a = aniso_on_table()
    pb = pbin(nbin)
    sel = pb > 0
    E = _E[sel]
    w = (pref(m) * _dq * DE * _f2[:, sel] / _q[:, None]**2 * pb[sel][None, :]).ravel()
    vm = ((E[None, :] / _q[:, None] + _q[:, None] / (2 * m)) * CKM).ravel()
    al = {l: (scale * a[l][:, sel]).ravel() for l in LS}
    v = np.atleast_1d(np.asarray(v, float))
    K = {0: np.zeros(v.shape)}
    for l in LS:
        K[l] = np.zeros(v.shape)
    for i, vv in enumerate(v):
        s = vm <= vv
        if not s.any():
            continue
        x = vm[s] / vv
        K[0][i] = w[s].sum() / (vv / CKM)
        for l in LS:
            K[l][i] = np.sum(w[s] * al[l][s] * eval_legendre(l, x)) / (vv / CKM)
    return K


# laboratory geometry (Sect. 1.2, eq:1.2-local): a direction of declination dec and hour angle Hh in (east, north, up) axes
LAT = 45.0


def local_dir(dec, Hh, lat=LAT):
    la = np.radians(lat)
    e = -np.cos(dec) * np.sin(Hh)
    n = np.cos(la) * np.sin(dec) - np.sin(la) * np.cos(dec) * np.cos(Hh)
    u = np.sin(la) * np.sin(dec) + np.cos(la) * np.cos(dec) * np.cos(Hh)
    return np.stack([e, n, u], axis=-1)


def daily_harmonics(decs, nh=720):
    """G_l(dec) = sidereal-day average of Y^c_l(vhat) for a stream of fixed declination; crystal [100] east, [010] north,
    [001] up (the orientation of WE 11.8)."""
    import aniso11 as AN
    Hh = (np.arange(nh) + 0.5) * 2 * np.pi / nh
    G = {}
    for l in LS:
        G[l] = np.array([AN.ycub(l, local_dir(d, Hh)).mean() for d in np.atleast_1d(decs)])
    return G


DEC_E = np.radians(47.5)          # declination of v_E (direction of v_sun), as aniso11.DELTA_E (Sect. 1.2)
VE = H.VE_REF
VESC = H.VESC
VMAX = H.VMAX


def feasible(v, dec):
    """True if a laboratory velocity of speed v (km/s) and declination dec lies inside the galactic support |v + v_E| <= v_esc
    for some right ascension: needs cos(angle to v_E) <= (v_esc^2 - v^2 - v_E^2)/(2 v v_E), smallest cosine -cos(dec + dec_E)."""
    cmax = (VESC**2 - v**2 - VE**2) / (2 * v * VE)
    return -np.cos(dec + DEC_E) <= cmax + 1e-12


def check_circle(m=2e6, nbin=1, v=600.0, vhat=(0.3, 0.5, 0.81), nphi=720):
    """Direct circle quadrature of S(qhat) = Sbar[1 + sum a_l Y^c_l] against the P_l(v_min/v) Y^c_l(vhat) identity, for one
    table cell set; returns the largest relative difference of the anisotropic part."""
    import aniso11 as AN
    vh = np.asarray(vhat, float)
    vh = vh / np.linalg.norm(vh)
    a = aniso_on_table()
    e1 = np.cross(vh, [0, 0, 1.0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(vh, e1)
    ph = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi
    worst = 0.0
    for x in (0.2, 0.5, 0.8, 0.95):
        s = np.sqrt(1 - x**2)
        qh = x * vh[None, :] + s * (np.cos(ph)[:, None] * e1[None, :] + np.sin(ph)[:, None] * e2[None, :])
        for l in LS:
            direct = AN.ycub(l, qh).mean()
            ident = eval_legendre(l, x) * AN.ycub(l, vh)
            worst = max(worst, abs(direct - ident))
    return worst
