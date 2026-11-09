"""Shared inputs of the Sect. 15.1 scripts: aluminum constants, the clean quasiclassical BCS density response
(bare quasiparticle bubble and conserving response with the pair-field ladder), loss functions and the rate.

Units: hbar = c = k_B = 1, Heaviside-Lorentz e^2 = 4 pi alpha.  Inside the response functions energies are in
units of Delta_BCS: y = omega/Delta_BCS, Q = q v_F/Delta_BCS (local to these scripts), mu = cosine of the
angle between k and q, s = Q mu the Doppler shift v_F q mu in units of Delta_BCS.

Hypotheses (Sect. 15.1): T = 0; constant density of states N_F per spin over the energies involved
(particle-hole symmetric, so the amplitude channel s_1 decouples, Sect. 7.2); linearized band xi' = xi + v_F q mu
(q^2/2m_e dropped: q <= 5.3 eV here, q^2/2m_e <= 2.7e-5 eV, negligible against q v_F >= 2 eV); q << k_F, k_TF;
clean (no impurity scattering).

Normalized responses P = R/(2 N_F), so that eps = 1 - (k_TF^2/q^2) P with k_TF^2 = 2 e^2 N_F (Sect. 4.5).
With the pair function  F(y, s) = Int dxi (E + E')/[E E' (omega^2 - (E + E')^2)]  (units Delta^-2; here Delta = 1)
and p = (y^2 - s^2)/4:
    F = -asinh(sqrt|p|)/sqrt(|p|(1+|p|))          (p < 0)
      = -asin(sqrt p)/sqrt(p(1-p))                (0 < p < 1)
      = [acosh(sqrt p) - i pi/2]/sqrt(p(p-1))     (p > 1, omega + i0, retarded),
the bubbles (Sect. 15.1 derivation; Eq. 7.2-Rc for the ladder; <X> = Int_0^1 dmu X(s = Q mu)):
    P_bare = < (s^2 + y^2 F)/(y^2 - s^2) >,
    P_cons = P_bare - y^2 <F>^2 / < (y^2 - s^2) F >.
Normal metal at q << k_F (Lindhard, Eq. 4.5-lindhard with nu_pm -> x = y/Q = omega/(q v_F)):
    P_nor = -1 + (x/2) ln|(1+x)/(1-x)| - i (pi/2) x Theta(1 - x).
Loss function L = Im(-1/eps).  Case-I coherence integral (= S_I/S_n of Eq. 7.2-pairspec):
    g_I(y) = 4 y Int_2^y du / [u^2 sqrt(u^2-4) sqrt(y^2-u^2)] = (1 + 2/y) E(k) - 4 K(k)/(y + 2), k = (y-2)/(y+2).
First-order Kramers-Kronig function (Sect. 15.1):
    s_BCS(y) = PV Int_0^inf dy' y'^2 [g_I(y') Theta(y'-2) - 1]/(y'^2 - y^2).

The mu quadrature (Gauss-Legendre panels graded at the inverse-square-root edge s* = sqrt(y^2-4) and at s = y)
follows the closed-form evaluation specified for App. E.20.

Aluminum inputs (book values):
  Delta_BCS = 0.18 meV, measured (Savrasov and Savrasov 1996, Table III; Sects. 7.2, 15.1);
  film convention Delta = 0.30 meV (2 Delta = 0.6 meV, Sect. 1.5; Hochberg et al. arXiv:2109.04473 p. 2:
     "Delta is half of the superconducting gap", "For aluminum (Al), with Delta = 0.3 meV");
  free-electron gas with m* = m_e from al_constants.py (one aluminum set book-wide): a = 4.05 A, three valence
  electrons per atom, k_F = (3 pi^2 n_e)^(1/3) = 1.749 A^-1, v_F = k_F/m_e = 6.753e-3, E_F = 11.65 eV,
  k_TF^2 = 4 alpha m_e k_F/pi (k_TF = 4048 eV); rho_T = 2.70 g cm^-3; c_LA from the 0 K C_11 = 114.3 GPa and rho(0 K) = 2.73 g cm^-3.
Halo and constants: figscripts/ch10/rate10_2.py (Baxter et al. 2105.00599 Table 1; v0 = 238, v_esc = 544,
  v_E = 250.5 km/s; v_max = 794.5 km/s = 2.650e-3; rho_chi = 0.3 GeV/cm^3; CODATA 2018).
"""
import os
import sys
import numpy as np
from scipy import integrate
from scipy.special import ellipk, ellipe

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
import rate10_2 as r10  # noqa: E402  (constants, halo eta)
sys.path.insert(0, HERE)
import al_constants as alc  # noqa: E402

ALPHA, ME, HBARC, CM, KG_EV = r10.ALPHA, r10.ME, r10.HBARC, r10.CM, r10.KG_EV
VMAX, eta = r10.VMAX, r10.eta
RHO_CHI = r10.RHO_CHI
VF = alc.VF
DELTA_BULK = 0.18e-3      # eV
DELTA_FILM = 0.30e-3      # eV
EF_AL = alc.EF
A_AL = 4.05
NE_AL = 12 / (A_AL / HBARC) ** 3          # eV^3 (12 electrons per cubic cell)
KF_AL = (3 * np.pi**2 * NE_AL) ** (1 / 3)
KTF_AL = np.sqrt(4 * ALPHA * ME * KF_AL / np.pi)
RHO_AL = 2.70e-3 * KG_EV / CM**3            # 2.70 g cm^-3 in eV^4
Q0 = ALPHA * ME
XMAX = VMAX / VF                             # largest omega/(q v_F) reached by halo dark matter

# ----------------------------------------------------------------------------------------------------------
GL = {}


def gl(n):
    if n not in GL:
        GL[n] = np.polynomial.legendre.leggauss(n)
    return GL[n]


SER = [2 / 3, 8 / 15, 16 / 35, 128 / 315, 256 / 693, 1024 / 3003, 2048 / 6435, 32768 / 109395]


def Ffun(p):
    """Pair function Delta^2 F as a function of p = (y^2 - s^2)/4 (retarded branch); returns (F, c) with
    c = (-F - 1)/p, the combination that stays finite at p -> 0 (series arcsin(r)/(r sqrt(1-r^2)))."""
    p = np.asarray(p, float)
    F = np.empty(p.shape, complex)
    c = np.empty(p.shape, complex)
    small = np.abs(p) < 2e-2
    ps = p[small]
    cs = np.zeros(ps.shape)
    for a in SER[::-1]:
        cs = cs * ps + a
    c[small] = cs
    F[small] = -(1 + ps * cs)
    m = (p < 0) & ~small
    a = -p[m]
    F[m] = -np.arcsinh(np.sqrt(a)) / np.sqrt(a * (1 + a))
    m = (p >= 0) & (p < 1) & ~small
    a = p[m]
    F[m] = -np.arcsin(np.sqrt(a)) / np.sqrt(a * (1 - a))
    m = p >= 1
    a = np.maximum(p[m], 1 + 1e-15)
    F[m] = (np.arccosh(np.sqrt(a)) - 0.5j * np.pi) / np.sqrt(a * (a - 1))
    m = ~small
    c[m] = (-F[m] - 1) / p[m]
    return F, c


def _grade(p, lo, hi, nk=44):
    out = []
    for sgn, L in ((-1, p - lo), (1, hi - p)):
        if L <= 0:
            continue
        out += [p + sgn * L * 2.0 ** (-j) for j in range(1, nk)]
    return out


def _panels(y, S):
    b = [0.0, S]
    top = max(y, 2.0) * 2
    if y > 2:
        ss = np.sqrt(y * y - 4)
        b += _grade(ss, 0.0, 2 * ss + 2.0)
        b.append(ss)
    else:
        d = max(np.sqrt(max(4 - y * y, 0.0)), 1e-300)
        t = d / 16
        while t < top * 2:
            b.append(t)
            t *= 2
    b.append(y)
    t = top
    while t < S:
        b.append(t)
        t *= 1.5
    return np.array(sorted(x for x in set(b) if 0.0 <= x <= S))


def _snodes(y, S, n=12):
    b = _panels(y, S)
    xg, wg = gl(n)
    a, c = b[:-1, None], b[1:, None]
    return (0.5 * (c - a) * xg + 0.5 * (c + a)).ravel(), (0.5 * (c - a) * wg).ravel()


def averages(y, Q, n=12):
    """<c>, <F>, <p F> over mu in [0, 1] (s = Q mu)."""
    s, w = _snodes(y, Q, n)
    w = w / Q
    p = 0.25 * (y * y - s * s)
    F, c = Ffun(p)
    return w @ c, w @ F, w @ (p * F)


def P_resp(y, Q, n=12):
    """(P_bare, P_cons) at (y, Q).  P_bare = <(s^2 + y^2 F)/(y^2 - s^2)> = -1 - (y^2/4)<c>;
    ladder term y^2 <F>^2/<(y^2 - s^2)F> = (y^2/4)<F>^2/<pF>."""
    C, F, PF = averages(y, Q, n)
    pb = -1 - 0.25 * y * y * C
    return pb, pb - 0.25 * y * y * F * F / PF


def P_nor(y, Q):
    x = y / Q
    re = -1 + 0.5 * x * np.log(abs((1 + x) / (1 - x)))
    return re + (-0.5j * np.pi * x if x < 1 else 0.0)


def loss(P, Q, delta, one=True):
    """Loss function Im(-1/eps) with eps = [1 -] (k_TF^2/q^2) P; q = Q delta/v_F."""
    q = Q * delta / VF
    eps = (1.0 if one else 0.0) - (KTF_AL**2 / q**2) * P
    return np.imag(-1.0 / eps)


def gI(y):
    y = np.asarray(y, float)
    k = (y - 2) / (y + 2)
    return (1 + 2 / y) * ellipe(k * k) - 4 * ellipk(k * k) / (y + 2)


def gI_int(y):
    """Integral form 4y Int_2^y du/[u^2 sqrt(u^2-4) sqrt(y^2-u^2)], u = 2 + (y-2) sin^2 th removes both edges."""
    def fn(th):
        u = 2 + (y - 2) * np.sin(th) ** 2
        return 4 * y / (u**2 * np.sqrt(u + 2) * np.sqrt(y + u)) * 2
    return integrate.quad(fn, 0, np.pi / 2, limit=400)[0]


def s_bcs(y, top=None):
    """s_BCS(y) = PV Int_0^inf dy' y'^2 [g_I(y')Theta(y'-2) - 1]/(y'^2 - y^2); top = finite cut if given."""
    def fI(yp):
        return np.where(yp > 2, gI(np.maximum(yp, 2.0000001)) - 1, -1.0)

    def gg(yp):
        return yp**2 * fI(yp)
    T = 1e4 if top is None else top

    def hf(yp):
        return (gg(yp) - gg(y)) / (yp**2 - y**2) if abs(yp - y) > 1e-9 else 0.0
    I1 = integrate.quad(hf, 0, T, points=[2.0, y] if T > y else [2.0], limit=800)[0]
    I2 = gg(y) / (2 * y) * np.log(abs((T - y) / (T + y)))
    tail = (integrate.quad(lambda yp: yp**2 * (gI(yp) - 1) / (yp**2 - y**2), 1e4, np.inf, limit=200)[0]
            if top is None else 0.0)
    return float(I1 + I2 + tail)


# ---------------------------------------------------------------- rate (Eq. 10.2-rate, isotropic, T = 0)
def prefactor(m, sigma_cm2):
    mu = m * ME / (m + ME)
    return RHO_CHI * sigma_cm2 * CM**2 / (8 * np.pi**2 * ALPHA * RHO_AL * m * mu**2)


def per_kg_yr(x):
    return r10.to_per_kg_yr(x)
