"""Shared inputs and functions for Sect. 16.7 (glasses, random media and two-level systems).  Used by fig16_7.py,
we16_7.py and limit16_7a.py ... limit16_7d.py.  Run directly to print the constants and every derived number of the
scattering estimate of Sect. 16.7 (log: tls16_7.log).

Units: natural units, eV (the conversion constants of figscripts/ch11/phon11.py).

Sources of every input:
  [Bu20] U. Buchenau, "Sound absorption in glasses", arXiv:2012.10139, Table I (vitreous SiO2): rho = 2200 kg/m^3,
         v_l = 5800 m/s, v_t = 3800 m/s, tunneling strength C = 2.6e-4 (average of longitudinal and transverse).
         Text p. 13: Golding, Graebner and Schutz (500 MHz) find C_l = 1.9e-4, C_t = 2.0e-4 (quoted by [Bu20]).
         Eqs. (4)-(6), (9), (10): gamma = (1/2) d Delta/d strain; C = P0 gamma^2/(rho v^2); Q^-1_res = pi C tanh(w/2T);
         one-phonon relaxation rate (Jaeckle); relaxation plateau pi C/2.
  [Zh15] arXiv:1510.05528, abstract/p. 1: gamma_l/gamma_t lies between 1.44 and 1.84 for 18 glasses (Berret-Meissner data,
         quoted there).  We take 1.6.
  ASSUMED (stated in the text): gamma_l = 1 eV.  It enters only the relaxation rate (Limit Checks 16.7a,b) and the split of
         the scattering rate into host and core terms; P_bar gamma_l^2 is fixed by C_l alone.
  [OC08] O'Connell et al., Appl. Phys. Lett. 92, 112903 (2008), arXiv:0802.2404, Table I: intrinsic (low-power, T <= 100 mK,
         ~6 GHz) loss tangents: thermal SiO2 3.0-3.3e-4, PECVD SiO2 2.7-2.9e-3, SiNx 1.0-2.0e-4, a-Si:H 2.2-2.5e-5 (LC).
  [Ma05] Martinis et al., Phys. Rev. Lett. 95, 210503 (2005), arXiv:cond-mat/0507622: PECVD SiO2 (SiH4 + O2) about 5e-3.
  ASSUMED (stated in the text as the conventional static value): eps_r = 3.9 for amorphous SiO2.
  SiO2: 30 electrons per formula unit, M = 60.0843 g/mol (standard atomic weights); O: Z = 8.
  Halo: the book's halo (Sect. 1.2), eta(v_min) of figscripts/ch11/phon11.py; <v> = 354.1 km/s (Sect. 1.2).
"""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ch11"))
import phon11 as P  # noqa: E402

KMS, SEC, YEAR, KG, CM2, ANG = P.KMS, P.SEC, P.YEAR, P.KG, P.CM2, P.ANG
HBARC_EV_CM = P.HBARC_EV_CM
CM3 = HBARC_EV_CM**3              # 1 cm^-3 in eV^3
RHO_CHI = P.RHO_CHI               # eV^4
M_E = P.M_E
eta = P.eta
DAY = 86400 * SEC
KELVIN = 8.617333e-5              # eV
GHZ = 4.135667696e-6              # 1 GHz (h nu) in eV

# ---- vitreous SiO2 [Bu20] ------------------------------------------------------------------------------------------
G = KG * 1e-3                                     # 1 g in eV
RHO_T = 2.200 * G * CM3                           # 2.2 g/cm^3 in eV^4
C_L = 5800.0 / 299792458.0
C_T = 3800.0 / 299792458.0
C_TUN = 2.6e-4                                    # average tunneling strength [Bu20]
C_TUN_GOLDING = (1.9e-4, 2.0e-4)                  # C_l, C_t at 500 MHz (quoted by [Bu20])
GAMMA_L = 1.0                                     # eV, ASSUMED
GAMMA_T = GAMMA_L / 1.6                           # [Zh15]
EPS_R = 3.9                                       # ASSUMED conventional value
TAND_THERMAL = 3.0e-4                             # [OC08] lower end; range 3.0-3.3e-4
TAND_THERMAL_RANGE = (3.0e-4, 3.3e-4)
TAND_PECVD = 5.0e-3                               # [Ma05]
M_FU = 60.0843 * P.M_U / 1.000                    # g/mol -> eV per formula unit (m_u units)
N_FU = 2.200 / 60.0843 * 6.02214076e23            # formula units per cm^3
N_E = 30 * N_FU                                   # electrons per cm^3


def pbar(gamma_l=GAMMA_L, c=C_TUN):
    """P_bar = C rho v_l^2 / gamma_l^2 in eV^-1 cm^-3."""
    return c * RHO_T * C_L**2 / gamma_l**2 / CM3


def k_jackle(gl=GAMMA_L, gt=GAMMA_T):
    """Prefactor K of the one-phonon relaxation rate tau^-1 = K E^3 u^2 coth(E/2T), u = Delta_0/Delta_tl (eV^-2)."""
    return (gl**2 / C_L**5 + 2 * gt**2 / C_T**5) / (2 * np.pi * RHO_T)


# ---- ensemble response of the standard tunneling model --------------------------------------------------------------
_UX, _UW = np.polynomial.legendre.leggauss(200)


def relax_ratio(w, T, K=None):
    """Relaxation part of the loss, divided by the resonant T = 0 value pi C (or tan delta_0):
    (2/pi) int dE (1/2T) sech^2(E/2T) int_0^1 du sqrt(1-u^2)/u  w tau/(1 + w^2 tau^2),
    tau^-1 = K E^3 u^2 coth(E/2T).  Substitution u = exp(s), s in [-60, 0]; E = 2T x, x in (0, 30]."""
    if K is None:
        K = k_jackle()
    xs = np.linspace(1e-4, 30, 3000)
    s = np.linspace(-80.0, 0.0, 4000)
    u = np.exp(s)
    wu = np.sqrt(1 - u**2)                      # sqrt(1-u^2)/u du = sqrt(1-u^2) ds
    out = 0.0
    E = 2 * T * xs
    rate = K * E[:, None]**3 * u[None, :]**2 / np.tanh(xs)[:, None]
    y = w / rate
    inner = np.trapezoid(wu[None, :] * y / (1 + y**2), s, axis=1)
    out = np.trapezoid(inner / np.cosh(xs)**2, xs)
    return 2 / np.pi * out


def loss_ratio(w, T, K=None):
    """Full loss of the ensemble (resonant + one-phonon relaxation) over tan delta_0."""
    return np.tanh(w / (2 * T)) + relax_ratio(w, T, K)


# ---- dark-matter scattering on two-level systems ----------------------------------------------------------------------
def f_host_sq(gamma_l=GAMMA_L):
    """|f_host|^2 = (2 n_e gamma_l / rho c_l^2)^2 (longitudinal projection, static window)."""
    return (2 * N_E * CM3 * gamma_l / (RHO_T * C_L**2))**2


def f_core_sq(q, Z=8.0, d=1.0 * ANG):
    """Orientation average of |2 i Z sin(q.d/2)|^2 = 2 Z^2 (1 - sin(qd)/(qd))."""
    x = q * d
    return 2 * Z**2 * (1 - np.sinc(x / np.pi))


def q_integral(m, fsq, n=4000):
    """int q dq eta(q/2m) fsq(q) over 0 < q < 2 m v_max (omega -> 0)."""
    q = np.linspace(1e-6, 2 * m * P.VMAX, n)
    return np.trapezoid(q * eta(q / (2 * m)) * fsq(q), q)


def dRdw_scat(m, sbar=1e-38, fsq=None, P_bar=None, T=10e-3 * KELVIN, w=0.05e-3):
    """dR/domega (per eV per unit target mass, natural units) from eq. (10.1-rateiso) with S = (pi/2) P_bar <|f|^2>/(1+e^-w/T)."""
    if P_bar is None:
        P_bar = pbar() * CM3
    mu = m * M_E / (m + M_E)
    pre = RHO_CHI * sbar * CM2 / (4 * np.pi * m * RHO_T * mu**2)
    S_over_f = np.pi / 2 * P_bar / (1 + np.exp(-w / T))
    return pre * S_over_f * q_integral(m, fsq)


PER_KG_DAY_MEV = KG * DAY * 1e-3                  # converts natural-unit dR/domega per mass to /(kg day meV)


def mean_speed():
    """<v> = 2 int_0^inf u eta(u) du (check against 354.1 km/s)."""
    u = np.linspace(0, P.VMAX, 20000)
    return 2 * np.trapezoid(u * eta(u), u)


if __name__ == "__main__":
    print("Sect. 16.7 constants (tls16_7.py)")
    print("n_fu = %.4e cm^-3, n_e = %.4e cm^-3" % (N_FU, N_E))
    rc2 = RHO_T * C_L**2 / CM3
    print("rho c_l^2 = %.4e eV/cm^3 = %.4e Pa" % (rc2, 2200 * 5800**2))
    print("P_bar (C = %.2e, gamma_l = %.2f eV) = %.3e eV^-1 cm^-3" % (C_TUN, GAMMA_L, pbar()))
    print("P_bar (C_l = 1.9e-4, Golding)        = %.3e eV^-1 cm^-3" % pbar(c=1.9e-4))
    print("f_host (gamma_l = 1 eV) = %.4f, |f_host|^2 = %.4f" % (np.sqrt(f_host_sq()), f_host_sq()))
    pf = 4 * N_E**2 * C_TUN / rc2
    print("P_bar |f_host|^2 = 4 n_e^2 C / rho c_l^2 = %.4e eV^-1 cm^-3 (independent of gamma_l); C_l = 1.9e-4: %.4e"
          % (pf, 4 * N_E**2 * 1.9e-4 / rc2))
    K = k_jackle()
    print("K = %.4e eV^-2 (gamma_l = 1, gamma_t = %.3f eV); longitudinal share %.3f"
          % (K, GAMMA_T, (GAMMA_L**2 / C_L**5) / (GAMMA_L**2 / C_L**5 + 2 * GAMMA_T**2 / C_T**5)))
    for nu in (0.5, 5.0):
        w = nu * GHZ
        print("  nu = %.1f GHz: w = %.4e eV, tau^-1(E = w, u = 1, T = 0) = %.4e s^-1, r = tau^-1/w = %.3e"
              % (nu, w, K * w**3 * SEC, K * w**2))
    print("<v> = %.2f km/s (book 354.1)" % (mean_speed() / KMS))
    # scattering estimate: host term fixed by the longitudinal tunneling strength C_l (eq:16.7-host); the core term
    # takes P_bar = C_l rho c_l^2/gamma_l^2.  Central: Golding's C_l = 1.9e-4; for comparison the polarization average
    # C = 2.6e-4 of [Bu20] Table I and C = 3.0e-4.
    q = None
    for m in (1e6,):
        mu = m * M_E / (m + M_E)
        print("m_chi = %.1f MeV: (1+m/m_e)^2 = %.3f" % (m / 1e6, (m / mu)**2))
        for cc, lab in [(1.9e-4, "C_l = 1.9e-4 (Golding, central)"), (C_TUN, "C = 2.6e-4 (polarization average)"),
                        (3.0e-4, "C = 3.0e-4")]:
            Pb = pbar(c=cc) * CM3
            hst = dRdw_scat(m, fsq=lambda q: f_host_sq() + 0 * q, P_bar=Pb) * PER_KG_DAY_MEV
            cor = dRdw_scat(m, fsq=f_core_sq, P_bar=Pb) * PER_KG_DAY_MEV
            print(" %s: P_bar = %.3e eV^-1 cm^-3, P_bar|f_host|^2 = %.4e eV^-1 cm^-3" % (lab, Pb / CM3, Pb / CM3 * f_host_sq()))
            print("  host term  dR/dw = %.4e /(kg day meV)" % hst)
            print("  core term (one O, Z = 8, d = 1 A) = %.4e /(kg day meV); ratio core/host = %.3f" % (cor, cor / hst))
            print("  total = %.4e /(kg day meV); over 0 < w < 0.1 meV: %.3e /(kg day)" % (hst + cor, (hst + cor) * 0.1))
        q = np.linspace(1e-6, 2 * m * P.VMAX, 4000)
        wq = q * eta(q / (2 * m))
        print("  median q of the heavy-mediator weight q eta(q/2m) = %.3f keV; q d at 1 A for that q = %.2f"
              % (np.interp(0.5, np.cumsum(wq) / np.sum(wq), q) / 1e3, np.interp(0.5, np.cumsum(wq) / np.sum(wq), q) * ANG))
        # host analytic check: (rho/m) <v> sbar (1+m/me)^2 P|f|^2 / (4 rho_T), C_l = 1.9e-4
        pf_l = 4 * N_E**2 * 1.9e-4 / rc2
        an = (RHO_CHI / m) * mean_speed() * 1e-38 * CM2 * (m / mu)**2 * pf_l * CM3 / (4 * RHO_T) * PER_KG_DAY_MEV
        print("  host analytic (rho/m)<v> sbar (1+m/m_e)^2 P|f|^2/4rho_T (C_l = 1.9e-4) = %.4e" % an)
        # crossover of host and core amplitudes at small qd: core displaced along q, |f_core| = Z q d = 8 q d;
        # orientation average <|f_core|^2>^(1/2) = (128/6)^(1/2) q d = 4.62 q d
        fh = np.sqrt(f_host_sq())
        print("  host = core at q_x = %.3f keV (core displacement along q, |f_core| = 8 q d); orientation-averaged core"
              " (|f_core| = %.3f q d): q_x = %.3f keV" % (fh / (8 * ANG) / 1e3, np.sqrt(128 / 6), fh / (np.sqrt(128 / 6) * ANG) / 1e3))
