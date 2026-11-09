"""Shared formulas of the Sect. 15.4 scripts: absorption of a uniform field by the current and by the spin current of a
superconducting metal (Holstein, Mattis-Bardeen, direct spin-current pair breaking), aluminum inputs.

Units: hbar = c = k_B = 1, Heaviside-Lorentz e^2 = 4 pi alpha; energies in eV unless stated; conductivities in eV
(sigma_1 = omega eps_2, Sect. 4.4).

Formulas (Sect. 15.4 and App. D.40; T = 0, Fermi-surface approximation, uniform field q -> 0):
  coherence integrals of Eq. 7.2-pairspec at pair energy x = y Delta_BCS, modulus k = sqrt(1 - 4/y^2) (m = k^2):
      g_I(y)  = E(k)                    case I  (density-type vertex),  g_I(2) = pi/2, g_I(inf) = 1;
      g_II(y) = E(k) - (4/y^2) K(k)     case II (current-type vertex), g_II(2) = 0, g_II(inf) = 1.
    Both are checked against direct quadrature of Eq. 7.2-pairspec below.
  Holstein (phonon-assisted) conductivity, current vertex (D.40):
      sigma_1^S(omega) = (omega_p^2/omega^2)(2 pi/omega) Int_0^{omega - 2 Delta} dW a2F_tr(W)(omega - W) g_I((omega - W)/Delta);
    normal metal (Delta = 0, g -> 1): Allen's sigma_1^N = (omega_p^2/omega^2) gamma_H, gamma_H = (2 pi/omega) Int_0^omega dW (omega - W) a2F_tr(W).
  Debye transport function (Hochberg, Lin, Zurek, arXiv:1604.06800, below Eq. 16):
      a2F_tr(W) = 2 lambda_tr W^4/omega_D^4 for W < omega_D, so that lambda_tr = 2 Int a2F_tr/W dW;
    it gives their Eq. (16) for gamma_H and their Eq. (17) for sigma_1^S/sigma_1^N (checked below).
  Mattis-Bardeen (impurity-assisted, dirty limit 1/tau_imp >> Delta):
      sigma_1^MB(omega) = sigma_N(omega) g_II(omega/Delta),  sigma_N = omega_p,free^2 tau/(1 + omega^2 tau^2),  1/tau = v_F/l_e.
  Spin current (axion-like particle), conductivity normalized as in Eq. 10.7-alp (sigma^J = sigma_1 for independent
  electrons without spin-orbit coupling in the normal state):
      clean, direct pair breaking: sigma^J_dir(omega) = 2 pi omega_p^2 Delta^2/[omega^2 sqrt(omega^2 - 4 Delta^2)],
        whose integral over omega > 2 Delta is (pi/2) omega_p^2 (checked below);
      dirty limit: sigma^J_imp(omega) = sigma_N(omega) g_I(omega/Delta).
  Dark-photon rate (Eq. 10.7-dp): R = (rho_chi/rho_T) zeta^2 L(m_phi), L = eps_2/|eps|^2,
      eps = 1 - sigma_2/omega + i sigma_1/omega with the condensate sigma_2 = omega_p^2/omega (clean, T = 0).
  Axion-like particle rate (Eq. 10.7-alp with sigma_1 -> sigma^J):
      R = (rho_chi/(rho_T m_phi)) (3 m_phi^2 g_aee^2/(4 m_e^2 e^2)) sigma^J(m_phi).

Aluminum inputs:
  Delta_BCS = 0.18 meV, measured (Savrasov and Savrasov, PRB 54, 16487 (1996), arXiv:cond-mat/9604124, Table III; Sect. 7.2);
  omega_p = 12.29 eV, intraband plasma frequency computed by Savrasov and Savrasov (Table IV), with which they extract
    lambda_tr = 0.39 from the measured resistivity (Table IV; their linear-response value 0.37);
  omega_D = 37 meV, the Debye cutoff of Hochberg, Lin and Zurek (arXiv:1604.06800, text below Eq. 2: "omega_D ~ 0.037 eV");
  v_F = 6.753e-3 and the free-electron plasma frequency 15.78 eV from al_constants.py (m* = m_e); rho_T = 2.70 g cm^-3;
  impurity-assisted parts: the 50 nm aluminum film of Sect. 15.3 (Worked example 15.3), mean free path l_e = 50 nm,
    gamma_rel = v_F/l_e, free-electron plasma frequency (three electrons per atom, a = 4.05 A), so that
    sigma_dc = omega_p^2/gamma_rel corresponds to the residual resistivity 0.79 micro-ohm cm used there.
Constants and halo: figscripts/ch10/rate10_2.py (CODATA 2018; rho_chi = 0.3 GeV cm^-3).
"""
import os
import sys
import numpy as np
from scipy import integrate
from scipy.special import ellipk, ellipe

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
import rate10_2 as r10  # noqa: E402
sys.path.insert(0, HERE)
import al_constants as alc  # noqa: E402

ALPHA, ME, HBARC, CM, KG_EV, YR_S, EV_S = r10.ALPHA, r10.ME, r10.HBARC, r10.CM, r10.KG_EV, r10.YR_S, r10.EV_S
E2 = 4 * np.pi * ALPHA
RHO_CHI = r10.RHO_CHI
RHO_AL = 2.70e-3 * KG_EV / CM**3
DELTA = 0.18e-3
WP = 12.29
LAM_TR = 0.39
WD = 37e-3
VF = alc.VF
HBAR_EVS = 6.582119569e-16
C_MS = 2.99792458e8
WP_FREE = alc.WP   # free-electron plasma frequency of Al, eV


def tau_inv(le_m):
    """1/tau_imp = v_F/l_e in eV for a mean free path in metres."""
    return VF * C_MS * HBAR_EVS / le_m


def gI(y):
    y = np.asarray(y, float)
    m = np.clip(1 - 4 / np.maximum(y, 2.0) ** 2, 0, 1)
    return np.where(y >= 2, ellipe(m), 0.0)


def gII(y):
    y = np.asarray(y, float)
    yy = np.maximum(y, 2.0)
    m = np.clip(1 - 4 / yy**2, 0, 1 - 1e-16)
    return np.where(y >= 2, ellipe(m) - 4 / yy**2 * ellipk(m), 0.0)


def g_quad(y, sign):
    """Direct quadrature of Eq. 7.2-pairspec (Delta = 1, omega = y): (1/y) Int_1^{y-1} dE [E(y-E) +- 1]/sqrt(...)sqrt(...).
    Substitution E = 1 + (y - 2) sin^2(t) removes both edge singularities."""
    if y <= 2:
        return 0.0
    d = y - 2

    def f(t):
        E = 1 + d * np.sin(t) ** 2
        Ep = y - E
        # dE / sqrt((E - 1)(E' - 1)) = 2 dt
        return 2 * (E * Ep + sign) / (np.sqrt(E + 1) * np.sqrt(Ep + 1))

    return integrate.quad(f, 0, np.pi / 2, limit=200, epsabs=1e-13, epsrel=1e-11)[0] / y


def a2f_debye(W, lam=LAM_TR, wd=WD):
    W = np.asarray(W, float)
    return np.where((W > 0) & (W < wd), 2 * lam * W**4 / wd**4, 0.0)


def sigma_holstein(w, a2f=a2f_debye, delta=DELTA, coh="I", wmax=None):
    """Holstein conductivity at T = 0 (eV). coh = 'I' (current vertex, the result), 'II' (case-II factor, for comparison),
    'N' (normal metal)."""
    w = float(w)
    if coh == "N":
        top = w
        g = lambda x: 1.0  # noqa: E731
    else:
        top = w - 2 * delta
        if top <= 0:
            return 0.0
        g = (lambda x: float(gI(x / delta))) if coh == "I" else (lambda x: float(gII(x / delta)))
    if wmax is not None:
        top = min(top, wmax)
    f = lambda W: float(a2f(W)) * (w - W) * g(w - W)  # noqa: E731
    pts = [p for p in (WD,) if 0 < p < top]
    val = integrate.quad(f, 0, top, points=pts or None, limit=400, epsabs=0, epsrel=1e-10)[0]
    return WP**2 / w**2 * 2 * np.pi / w * val


def gammaH_debye_closed(w, lam=LAM_TR, wd=WD):
    """Hochberg-Lin-Zurek Eq. (16)."""
    if w >= wd:
        return 4 / 5 * np.pi * lam * wd * (1 - 5 / 6 * wd / w)
    return 2 / 15 * np.pi * lam * w**5 / wd**4


def sigma_N_imp(w, tinv):
    """Drude conductivity of the normal film, free-electron plasma frequency (as in Sect. 15.3)."""
    tau = 1 / tinv
    return WP_FREE**2 * tau / (1 + (w * tau) ** 2)


def sigma_MB(w, tinv, delta=DELTA):
    return sigma_N_imp(w, tinv) * float(gII(w / delta))


def sigmaJ_direct(w, delta=DELTA):
    w = np.asarray(w, float)
    return np.where(w > 2 * delta, 2 * np.pi * WP**2 * delta**2 / (w**2 * np.sqrt(np.maximum(w**2 - 4 * delta**2, 1e-300))), 0.0)


def sigmaJ_imp(w, tinv, delta=DELTA):
    return sigma_N_imp(w, tinv) * float(gI(w / delta))


def loss_clean(w, s1):
    eps = 1 - WP**2 / w**2 + 1j * s1 / w
    return (s1 / w) / abs(eps) ** 2


def per_kg_yr(rate_ev4):
    """Convert a rate per unit target mass in natural units (eV^-... : events per time per mass, eV / eV) to /kg/yr."""
    return rate_ev4 * EV_S * YR_S * KG_EV


def rate_darkphoton(w, s1, zeta=1.0):
    """Events per kg per yr, Eq. 10.7-dp."""
    return per_kg_yr(RHO_CHI / RHO_AL * zeta**2 * loss_clean(w, s1))


def rate_alp(w, sJ, g=1.0):
    """Events per kg per yr, Eq. 10.7-alp with sigma^J."""
    return per_kg_yr(RHO_CHI / (RHO_AL * w) * 3 * w**2 * g**2 / (4 * ME**2 * E2) * sJ)


def checks(log=print):
    for y in (2.0001, 2.2, 3.0, 4.0, 10.0, 100.0):
        a, b = float(gI(y)), g_quad(y, +1)
        c, d = float(gII(y)), g_quad(y, -1)
        assert abs(a - b) < 1e-7 and abs(c - d) < 1e-7, (y, a, b, c, d)
    log("check: g_I, g_II closed forms = quadrature of Eq. 7.2-pairspec to 1e-7 at y = 2.0001, 2.2, 3, 4, 10, 100")
    log("       g_I(4) = %.4f, g_II(4) = %.4f (Sect. 7.2: 1.21 and 0.67)" % (gI(4.0), gII(4.0)))
    # App. D.40 forms with modulus kappa = (y - 2)/(y + 2):  g_I = (1 + 2/y)E - 4K/(y + 2),  g_II = (1 + 2/y)E - (4/y)K
    for y in (2.2, 3.0, 4.0, 10.0, 100.0):
        m = ((y - 2) / (y + 2)) ** 2
        aI = (1 + 2 / y) * ellipe(m) - 4 * ellipk(m) / (y + 2)
        aII = (1 + 2 / y) * ellipe(m) - 4 * ellipk(m) / y
        assert abs(aI - gI(y)) < 1e-12 and abs(aII - gII(y)) < 1e-12
    log("check: the modulus-(y-2)/(y+2) forms of App. D.40 agree with the forms above to 1e-12")
    for w in (5e-3, 20e-3, 37e-3, 60e-3, 0.3):
        num = sigma_holstein(w, coh="N") * w**2 / WP**2
        assert abs(num / gammaH_debye_closed(w) - 1) < 1e-8
    log("check: normal-state Holstein with the Debye a2F_tr reproduces Hochberg-Lin-Zurek Eq. (16) to 1e-8")
    # Eq. (17) of HLZ: tau_N/tau_S = Int_0^{w-2D} dW (w-W) W^4 E[sqrt(1 - 4D^2/(w-W)^2)] / Int_0^w dW (w-W) W^4 (w < omega_D)
    for w in (0.5e-3, 1e-3, 3e-3, 10e-3):
        num = integrate.quad(lambda W: (w - W) * W**4 * ellipe(1 - 4 * DELTA**2 / (w - W) ** 2), 0, w - 2 * DELTA,
                             epsrel=1e-11)[0]
        den = w**6 / 30
        r = sigma_holstein(w, coh="I") / sigma_holstein(w, coh="N")
        assert abs(r / (num / den) - 1) < 1e-7
    log("check: sigma_1^S/sigma_1^N with the Debye a2F_tr equals Hochberg-Lin-Zurek Eq. (17) to 1e-7")
    tot = integrate.quad(lambda t: float(sigmaJ_direct(2 * DELTA * np.cosh(t))) * 2 * DELTA * np.sinh(t), 1e-12, 40,
                         limit=400)[0]
    log("check: Int sigma^J_dir domega = %.6f (pi/2) omega_p^2" % (tot / (np.pi / 2 * WP**2)))
    assert abs(tot / (np.pi / 2 * WP**2) - 1) < 1e-6
