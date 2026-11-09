"""Shared model of the Sect. 16.1 scripts: the dielectric function of a Dirac target with the background dielectric
constant placed in the total epsilon, its loss function, the published screening rules, and the scattering and
absorption rates.  Natural units hbar = c = 1, Heaviside-Lorentz e^2 = 4 pi alpha; energies and momenta in eV.

Dielectric function (Sect. 7.3, eq:7.3-epsbg, eq:7.3-eps = eq:D.22-eps, hard cutoff):
  eps(q, omega) = eps_bg(qhat) + eps_D(q, omega),   eps_D = -v_C R0_D  (independent of eps_bg),
  eps_D = (g alpha / 6 pi) (sum_i v_i^2 qhat_i^2) / (v_1 v_2 v_3) * B(s),   s = omega^2 - sum_i v_i^2 q_i^2,
  B(s) = ln(4 Lt^2/Delta^2) - 5/3 - 6 int_0^1 dx x(1-x) ln(1 - x(1-x) s/Delta^2 - i0),   Lt = v_D Lambda_D,
  Im B = pi rho(s) Theta(s - 4 Delta^2) Theta(4 Lt^2 - s),  rho = (1 - 4Delta^2/s)^(1/2) (1 + 2Delta^2/s)
  (pairs exist only inside the cutoff, u < 4 Lt^2 in eq:D.22-R).  Gapless: B = ln(4 Lt^2/|s|) + i pi Theta(s).
  For an isotropic cone eps_D = (g alpha/(6 pi v_D)) B; anisotropic: Geilhufe et al. (arXiv:1910.02091) Eq. (3.10)
  with their mu~ = 2 e^(-5/6) Lt is the same bracket (their Lt is a hard cutoff in our sense, Sect. 7.3 WE).
Loss functions at one (q, omega):
  book (total eps):      L = Im eps_D / |qhat.eps_bg.qhat + eps_D|^2
  published, isotropic:  L_src = Im eps_D / |1 + eps_D/eps_bg|^2    (Hochberg et al. arXiv:1708.08929 Eqs. (3.7),
                         (3.11): vacuum sigma_e, F_med = 1/eps_r with eps_r = eps/eps_bg)  = eps_bg^2 L exactly
  published, anisotropic: L_src = Im eps_D / |1 + sum_i qhat_i^2 v_i^2 (g alpha/6 pi v1v2v3) B / eps_bg,ii|^2
                         (Geilhufe et al. Eq. (3.14), with the q_x^2 v_x^2 term in place of the printed q_x^2 v_z^2)
Rates: scattering, eq:10.2-rate with this L averaged over qhat (rate averaged over crystal orientations);
absorption per polarization i (q -> 0), Gamma_i = zeta^2 m Im(-1/eps_ii) (eq:10.7-dp), unpolarized average;
published absorption rule Gamma_i,src = eps_bg,ii Gamma_i (1708.08929 Eqs. (4.4)-(4.5); 1910.02091 Eqs. (2.25)-(2.27)).
Halo, constants, eta: figscripts/ch10/rate10_2.py (book values: v0 = 238, v_E = 250.5, v_esc = 544 km/s,
rho_chi = 0.3 GeV cm^-3, CODATA 2018 constants).
"""
import os
import sys
import warnings
import numpy as np
from scipy.integrate import quad, IntegrationWarning
from numpy.polynomial.legendre import leggauss

warnings.simplefilter("ignore", IntegrationWarning)   # integrable log endpoint singularities of B(s)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
import rate10_2 as R  # noqa: E402

ALPHA, ME, HBARC, CM, KG_EV, EV_S, YR_S = R.ALPHA, R.ME, R.HBARC, R.CM, R.KG_EV, R.EV_S, R.YR_S
VMAX = R.VMAX
RHO_CHI = R.RHO_CHI
Q0 = R.Q0
KGYR = KG_EV * YR_S * EV_S          # 1 kg yr in natural units (eV * eV^-1)
GCM3 = 1e-3 * KG_EV / CM**3         # 1 g cm^-3 in eV^4
SIG1 = CM**2                         # 1 cm^2 in eV^-2

# --- targets ---------------------------------------------------------------------------------------------------
# ZrTe5, Geilhufe, Kahlhoefer and Winkler, arXiv:1910.02091: Table 1 row ISIF7 (bold, implemented): v_i, Delta
# (half-gap, text below Table 1: gap 31.2 meV <-> Delta = 15.6 meV), Lambda_i; Table 2 'This work' kappa_ii, g = 2;
# Fig. 3(d) densities 6.089 g/cm^3 (Exp., their Ref. [47]) and 6.135 g/cm^3 ('this work', used in their reach).
ZRTE5 = dict(v=np.array([1.1e-3, 4.4e-4, 9.1e-4]), D=15.6e-3, Lam=np.array([0.23, 0.216, 0.1]),
             ebg=np.array([308.4, 20.75, 126.1]), g=2, rho_exp=6.089, rho_src=6.135)
ZRTE5["Lt"] = float(np.min(ZRTE5["Lam"] * HBARC * ZRTE5["v"]))       # 1910.02091 Eq. (2.21): min_i Lambda_i v_i
# Ideal isotropic benchmark of Hochberg et al., arXiv:1708.08929 Fig. 4 caption and Sect. 3.3: v_F = 4e-4,
# kappa = 40, g = 2, Lambda = 0.2 keV (taken here as a hard cutoff on |k|), gapped Delta = 2.5 meV or gapless.
BENCH = dict(vD=4e-4, D=2.5e-3, ebg=40.0, g=2, Lt=4e-4 * 200.0)
# ZrTe5 'th.' of 1708.08929 (their App. D Table 1, as quoted in Sect. 7.3 WE): kappa_ii = 187.5, 9.8, 90.9;
# the harmonic mean is the isotropic kappa of their reach (Sect. 3.3, text after Fig. 4).
KAPPA_1708 = np.array([187.5, 9.8, 90.9])
EBG_1708 = 3.0 / np.sum(1.0 / KAPPA_1708)


def harmonic(x):
    return len(x) / np.sum(1.0 / np.asarray(x))


# --- the bracket B(s) ------------------------------------------------------------------------------------------
def B_exact(s, D, Lt):
    """Bracket of eq:7.3-eps at real s (scalar), hard cutoff; Im part from rho(s) inside the cutoff."""
    if D == 0.0:
        re = np.log(4 * Lt**2 / abs(s))
        im = np.pi if (0 < s < 4 * Lt**2) else 0.0
        return re + 1j * im
    z = s / D**2
    f = lambda x: x * (1 - x) * np.log(abs(1 - x * (1 - x) * z))  # noqa: E731
    if z > 4:
        b = np.sqrt(1 - 4 / z)
        pts = [0.5 * (1 - b), 0.5 * (1 + b)]
        J = sum(quad(f, a, c, limit=200)[0] for a, c in [(0, pts[0]), (pts[0], 0.5), (0.5, pts[1]), (pts[1], 1)])
        rho = b * (1 + 2 / z)
        im = np.pi * rho if s < 4 * Lt**2 else 0.0
    else:
        J = quad(f, 0, 1, limit=200)[0]
        im = 0.0
    return np.log(4 * Lt**2 / D**2) - 5.0 / 3.0 - 6 * J + 1j * im


class Btab:
    """Table of B(s) for s in (4 Delta^2, 4 Lt^2], on a grid in log(s - 4 Delta^2); B = 0 outside (no pairs)."""

    def __init__(self, D, Lt, n=1500):
        self.D, self.Lt, self.s0 = D, Lt, 4 * D**2
        lo = 1e-9 * max(self.s0, 1e-6)
        hi = 4 * Lt**2 - self.s0
        self.t = np.linspace(np.log(lo), np.log(hi), n)
        v = np.array([B_exact(self.s0 + np.exp(t), D, Lt) for t in self.t])
        self.re, self.im = v.real, v.imag

    def __call__(self, s):
        s = np.asarray(s, float)
        ok = (s > self.s0) & (s <= 4 * self.Lt**2)
        t = np.log(np.where(ok, s - self.s0, 1.0))
        out = np.interp(t, self.t, self.re) + 1j * np.interp(t, self.t, self.im)
        return np.where(ok, out, 0.0)


# --- dielectric function and loss functions --------------------------------------------------------------------
def epsD_iso(q, w, vD, g, Bt):
    s = w**2 - (vD * q) ** 2
    return g * ALPHA / (6 * np.pi * vD) * Bt(s)


def L_iso(q, w, vD, g, ebg, Bt, rule="book"):
    e = epsD_iso(q, w, vD, g, Bt)
    if rule == "book":
        return e.imag / np.abs(ebg + e) ** 2
    if rule == "src":
        return e.imag / np.abs(1 + e / ebg) ** 2
    if rule == "lead":
        return e.imag / ebg**2
    raise ValueError(rule)


_ct, _wct = leggauss(24)
_ph, _wph = leggauss(24)
CT = 0.5 * (_ct + 1)                 # cos(theta) in [0, 1]
WCT = 0.5 * _wct
PH = 0.25 * np.pi * (_ph + 1)        # phi in [0, pi/2]
WPH = 0.25 * np.pi * _wph
_C, _P = np.meshgrid(CT, PH, indexing="ij")
QH = np.stack([np.sqrt(1 - _C**2) * np.cos(_P), np.sqrt(1 - _C**2) * np.sin(_P), _C], -1).reshape(-1, 3)
WQH = (np.outer(WCT, WPH) / (np.pi / 2)).ravel()      # weights of the octant average, sum = 1


def L_aniso_avg(q, w, mat, Bt, rule="book"):
    """Loss function averaged over the directions of q (octant quadrature), for arrays q at fixed omega w."""
    v, ebg, g = mat["v"], mat["ebg"], mat["g"]
    vvv = np.prod(v)
    q = np.atleast_1d(q)
    q2 = QH**2                                         # (ndir, 3)
    vq2 = q2 @ (v**2)                                  # sum_i v_i^2 qhat_i^2
    s = w**2 - np.outer(q**2, vq2)                     # (nq, ndir)
    Bv = Bt(s)
    pref = g * ALPHA / (6 * np.pi * vvv)
    eD = pref * vq2[None, :] * Bv
    if rule == "book":
        den = np.abs((q2 @ ebg)[None, :] + eD) ** 2
    elif rule == "src":
        den = np.abs(1 + pref * (q2 @ (v**2 / ebg))[None, :] * Bv) ** 2
    elif rule == "lead":
        den = (q2 @ ebg)[None, :] ** 2
    else:
        raise ValueError(rule)
    L = np.where(eD.imag > 0, eD.imag / den, 0.0)
    return L @ WQH


# --- rates -------------------------------------------------------------------------------------------------------
def prefactor(m, rhoT):
    """rho_chi sigma_e/(8 pi^2 alpha rho_T m mu^2) of eq:10.2-rate per unit sigma_e (sigma in eV^-2)."""
    mu = m * ME / (m + ME)
    return RHO_CHI / (8 * np.pi**2 * ALPHA * rhoT * m * mu**2)


def scatter_rate(m, Lfun, wmin, wmax, qmax, rhoT, light=True, nw=260, nq=500):
    """Total rate per unit sigma_e [events per kg yr per cm^2] for an isotropic or orientation-averaged L(q, w)."""
    ws = wmin + (wmax - wmin) * np.linspace(0, 1, nw) ** 2           # dense near threshold
    qlo = max(wmin / VMAX * 0.999, 1e-3)
    qs = np.geomspace(qlo, qmax, nq)
    dR = np.zeros(nw)
    for i, w in enumerate(ws):
        vmin = w / qs + qs / (2 * m)
        et = R.eta(vmin)
        if not np.any(et > 0):
            continue
        L = Lfun(qs, w)
        F2 = (Q0 / qs) ** 4 if light else 1.0
        dR[i] = np.trapezoid(qs**3 * et * F2 * L, qs)
    tot = np.trapezoid(dR, ws) * prefactor(m, rhoT)
    return tot * KGYR * SIG1


def sigma_lim(rate_per_cm2, nev=3.0, expo=1.0):
    return nev / (rate_per_cm2 * expo)


def abs_L_pol(m, mat, Bt):
    """Per-polarization loss function Im(-1/eps_ii) at q -> 0, omega = m (anisotropic cone)."""
    v, ebg, g = mat["v"], mat["ebg"], mat["g"]
    vvv = np.prod(v)
    Bv = Bt(np.asarray(m) ** 2)
    eD = g * ALPHA / (6 * np.pi * vvv) * np.multiply.outer(Bv, v**2)       # (..., 3)
    return eD.imag / np.abs(ebg + eD) ** 2


def zeta_lim(Lavg, rhoT, nev=3.0, expo=1.0):
    """3-event mixing reach from R = (rho_chi/rho_T) zeta^2 Lavg (eq:10.7-dp), per kg yr."""
    rate = RHO_CHI / rhoT * Lavg * KGYR
    return np.sqrt(nev / (rate * expo))


def check_im_by_pair_sum(q, w, vD, D, g, Lt, dw_frac=2e-3, nk=3000, nc=3000):
    """Direct check of Im eps_D: (pi e^2/q^2) (g/(2pi)^3) int d^3k F(k,k+q) delta(w - E - E') with F of eq:D.22-F,
    the delta function smeared over a bin of relative width dw_frac.  Returns (direct, formula)."""
    E = lambda k: np.sqrt((vD * k) ** 2 + D**2)  # noqa: E731
    kmax = Lt / vD
    k = np.linspace(0, kmax, nk)[1:]
    c = np.linspace(-1, 1, nc)
    K, Cc = np.meshgrid(k, c, indexing="ij")
    kp = np.sqrt(K**2 + q**2 + 2 * K * q * Cc)
    E1, E2 = E(K), E(kp)
    kdotkp = K**2 + K * q * Cc
    F = 0.5 * (1 - (vD**2 * kdotkp + D**2) / (E1 * E2))
    dw = dw_frac * w
    ind = (np.abs(E1 + E2 - w) < dw / 2) & (kp < kmax)
    integ = 2 * np.pi * K**2 * F * ind / dw
    val = np.trapezoid(np.trapezoid(integ, c, axis=1), k)
    direct = np.pi * 4 * np.pi * ALPHA / q**2 * g / (2 * np.pi) ** 3 * val
    s = w**2 - (vD * q) ** 2
    rho = np.sqrt(1 - 4 * D**2 / s) * (1 + 2 * D**2 / s)
    formula = g * ALPHA / (6 * vD) * rho
    return direct, formula
