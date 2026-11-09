"""Shared model for Sect. 16.3 (vacuum ejection from graphene): plane-wave (PW) and orthogonalized-plane-wave (OPW)
ejection amplitudes of one carbon 2p_z orbital, orientation-averaged, and the halo-integrated ejection spectra.

Model (every input sourced):
  orbital      hydrogenic 2p_z, psi(r) = N r exp(-beta r) cos(theta), beta = Z_eff/(2 a0), Z_eff = 4.03
               (Hochberg, Kahn, Lisanti, Tully, Zurek, arXiv:1606.08849, Eq. (2) and text after it); N^2 = beta^5/pi.
               Momentum wavefunction psi~(k) = int d^3r exp(-i k.r) psi = -32 pi i N beta (k.e)/(beta^2 + k^2)^3
               (1606.08849 Eq. (4) up to normalization).  BETA_ALT = 1.568/a0 is kept only for a sensitivity line.
  amplitudes   M_PW(p, q)  = psi~(p - q)                          (plane wave, eq:2.2-ff with a plane-wave final state)
               M_OPW(p, q) = psi~(p - q) - psi~(p) F(q),  F(q) = <psi| exp(i q.r) |psi>  (final plane wave orthogonalized
               to the initial orbital only).  F(q) = J0(q) - 2 J2(q) P2(qhat.e), J_L = int rho(r) j_L(q r) dr,
               rho(r) = (2 beta)^5 r^4 exp(-2 beta r)/24 (radial density, int rho dr = 1).
  orientation  the sheet (orbital axis e) is averaged over all orientations relative to q (isotropic average, which is
               what an isotropic velocity integral needs); K(p, q) = int dOmega_p <|M|^2>_{orientations}  [eV^-3].
  kinematics   omega = E_ej + PHI_WF + E_B, E_ej = p^2/2m_e; PHI_WF = 4.3 eV (graphene work function quoted by
               1606.08849, text after Eq. (5)); E_B >= 0 the binding below the Fermi level (Dirac point).
  pi band      binding energies from nearest-neighbour tight binding, E_B = t |1 + exp(i k.a1) + exp(i k.a2)| over the
               Brillouin zone, t = 2.8 eV (Castro Neto et al., arXiv:0709.1163, text after Eq. (5) and Eq. (7)); one pi
               electron per carbon atom (both spins); the momentum density of each pi electron is that of the isolated
               orbital (Bloch interference between neighbours dropped: a model).
  halo         book standard halo (App. A.8, Table 1.1): rho_chi = 0.3 GeV/cm^3, v0 = 238, v_esc = 544,
               v_E^ref = 250.5 km/s, eta(v_min) in the closed form of App. D.1 (same code as figscripts/ch10/we10_1.py).
  rate         dvsigma/dE_ej = sigma_e m_e p/(16 pi^3 mu^2) int q dq eta(v_min) F_DM^2 K(p, q)   (derived in Sect. 16.3
               from eq:A.8-eta; for a full shell and PW it reduces to eq:2.2-ion with eq:2.2-fion-pw: checked below)
               dR/dlnE_ej = E_ej (rho_chi/m_chi) N_pi <dvsigma/dE_ej>_{E_B},  N_pi = 1/m_C pi electrons per kg.
"""
import os
import numpy as np
from scipy.special import erf, spherical_jn
from numpy.polynomial.legendre import leggauss
from math import factorial

HERE = os.path.dirname(os.path.abspath(__file__))
ALPHA = 1 / 137.035999
ME = 510998.95                      # eV
A0 = 1 / (ALPHA * ME)               # eV^-1
ZEFF = 4.03
BETA = ZEFF / (2 * A0)              # eV
BETA_ALT = 1.568 / A0               # eV (sensitivity only)
PHI_WF = 4.3                        # eV
T_HOP = 2.8                         # eV
CKM = 299792.458
V0, VESC, VE = 238.0, 544.0, 250.5
VMAX = (VESC + VE) / CKM
RHO = 0.3e9                         # eV/cm^3
CCMS = 2.99792458e10
YR = 365.25 * 86400
M_C_KG = 12.011 * 1.66053907e-27    # kg
N_PI = 1 / M_C_KG                   # pi electrons per kg (one per atom)
Z = VESC / V0
NESC = np.pi**1.5 * V0**3 * (erf(Z) - 2 / np.sqrt(np.pi) * Z * np.exp(-Z**2))


def eta(u_nat):
    """Book standard halo eta(v_min), App. D.1 closed form; argument and result in natural units."""
    u = np.maximum(np.asarray(u_nat, float) * CKM, 0.0)
    k = np.pi * V0**2 / (VE * NESC)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + VE) / V0) - erf((u - VE) / V0)) - 2 * VE * np.exp(-Z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(Z) - erf((u - VE) / V0)) - (VESC + VE - u) * np.exp(-Z**2))
    return np.where(u < VESC - VE, b1, np.where(u < VESC + VE, b2, 0.0)) * CKM


def norm(beta):
    return np.sqrt(beta**5 / np.pi)


def psit_amp(kdote, k2, beta):
    """|psi~| without the -i: 32 pi N beta (k.e)/(beta^2+k^2)^3."""
    return 32 * np.pi * norm(beta) * beta * kdote / (beta**2 + k2) ** 3


def radial_JL(q, beta, L):
    """J_L(q) = int rho(r) j_L(q r) dr with rho = (2 beta)^5 r^4 e^{-2 beta r}/24, in closed form from
    int_0^inf r^n e^{-a r} e^{i q r} dr = n!/(a - i q)^{n+1} (a = 2 beta); L = 0 or 2."""
    q = np.atleast_1d(np.asarray(q, float))
    a = 2 * beta
    z = a - 1j * q
    c = a**5 / 24.0
    S = lambda n: factorial(n) * np.imag(z ** (-(n + 1)))   # noqa: E731  int r^n e^{-ar} sin(qr)
    C = lambda n: factorial(n) * np.real(z ** (-(n + 1)))   # noqa: E731  int r^n e^{-ar} cos(qr)
    if L == 0:
        return c * S(3) / q
    if L == 2:
        return c * (3 / q**3 * S(1) - S(3) / q - 3 / q**2 * C(2))
    raise ValueError(L)


def K_table(pvals, qvals, beta=BETA, n_th=48, n_ph=48, n_q=16, kind="both", fixed_cq=None):
    """K(p,q) = int dOmega_p <|M|^2>, orbital along z, q at polar angle theta_q averaged over cos(theta_q) in [0,1]
    (|M|^2 is even under q -> reflected q about the orbital plane).  fixed_cq: evaluate at one cos(theta_q) instead.
    Returns (K_PW, K_OPW) arrays of shape (len(p), len(q))."""
    ct, wt = leggauss(n_th)                     # cos(theta_p)
    ph = (np.arange(n_ph) + 0.5) * 2 * np.pi / n_ph
    wph = 2 * np.pi / n_ph
    st = np.sqrt(1 - ct**2)
    px_u = (st[:, None] * np.cos(ph)[None, :]).ravel()
    py_u = (st[:, None] * np.sin(ph)[None, :]).ravel()
    pz_u = np.repeat(ct, n_ph)
    wp = np.repeat(wt, n_ph) * wph               # sum = 4 pi
    if fixed_cq is None:
        cq, wq = leggauss(n_q)
        cq = 0.5 * (cq + 1)                      # cos(theta_q) in [0,1]
        wq = 0.5 * wq                            # sum = 1 (average)
    else:
        cq, wq = np.array([fixed_cq]), np.array([1.0])
    sq = np.sqrt(1 - cq**2)
    J0 = radial_JL(qvals, beta, 0)
    J2 = radial_JL(qvals, beta, 2)
    KPW = np.zeros((len(pvals), len(qvals)))
    KOP = np.zeros_like(KPW)
    for i, p in enumerate(pvals):
        pz = p * pz_u
        amp_p = psit_amp(pz, p * p, beta)                        # psi~(p), e = z
        for a, (c, s, w) in enumerate(zip(cq, sq, wq)):
            # q = q (s, 0, c)
            qx = qvals[:, None] * s
            qz = qvals[:, None] * c
            dx = p * px_u[None, :] - qx
            dy = p * py_u[None, :]
            dz = pz[None, :] - qz
            k2 = dx * dx + dy * dy + dz * dz
            mpw = psit_amp(dz, k2, beta)
            P2 = 0.5 * (3 * c * c - 1)
            F = (J0 - 2 * J2 * P2)[:, None]
            mop = mpw - amp_p[None, :] * F
            KPW[i] += w * (mpw**2 * wp[None, :]).sum(1)
            KOP[i] += w * (mop**2 * wp[None, :]).sum(1)
    return KPW, KOP


def K_pw_analytic(p, q, beta=BETA):
    """Orientation-averaged PW K: (1/3) (32 pi N beta)^2 int dOmega_p k^2/(beta^2+k^2)^6, k = |p - q|."""
    from scipy.integrate import quad
    c = (32 * np.pi * norm(beta) * beta) ** 2 / 3
    f = lambda k: k * k**2 / (beta**2 + k**2) ** 6  # noqa: E731
    val, _ = quad(f, abs(p - q), p + q, limit=200)
    return c * 2 * np.pi / (p * q) * val


def pi_dos(nk=600, nbins=400):
    """Normalized distribution of E_B = t|f(k)| over the Brillouin zone (lower pi band, occupied)."""
    u = (np.arange(nk) + 0.5) / nk
    U, V = np.meshgrid(u, u)
    # k = U b1 + V b2 ; k.a1 = 2 pi U, k.a2 = 2 pi V
    f = np.abs(1 + np.exp(2j * np.pi * U) + np.exp(2j * np.pi * V))
    E = T_HOP * f.ravel()
    h, edges = np.histogram(E, bins=nbins, range=(0, 3 * T_HOP))
    cen = 0.5 * (edges[1:] + edges[:-1])
    return cen, h / h.sum(), E.mean()


def spectrum(Eej, KPW, KOP, pgrid, qgrid, mchi, EB, wEB, light=False):
    """dR/dlnE_ej (kg^-1 yr^-1 at sigma_e = 1e-37 cm^2) for PW and OPW, on the E_ej grid that defines pgrid."""
    SIG = 1e-37
    mu = mchi * ME / (mchi + ME)
    FDM2 = (ALPHA * ME / qgrid) ** 4 if light else np.ones_like(qgrid)
    lq = np.log(qgrid)
    out = []
    for KK in (KPW, KOP):
        R = np.zeros(len(Eej))
        for i, (E, p) in enumerate(zip(Eej, pgrid)):
            om = E + PHI_WF + EB                                       # (nEB,)
            vmin = om[:, None] / qgrid[None, :] + qgrid[None, :] / (2 * mchi)
            integrand = qgrid[None, :] ** 2 * eta(vmin) * FDM2[None, :] * KK[i][None, :]   # q dq = q^2 dlnq
            I = np.trapezoid(integrand, lq, axis=1)                        # (nEB,)  eV^-1
            dvs = SIG * ME * p / (16 * np.pi**3 * mu**2) * I           # cm^2 eV^-1 (times c)
            R[i] = E * (RHO / mchi) * CCMS * N_PI * YR * np.sum(wEB * dvs)
        out.append(R)
    return out
