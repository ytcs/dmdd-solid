"""Section 19.1 (nuclear recoil on the Born-Oppenheimer surface): every number printed in s19-1.tex,
Worked example 19.1 and Fig. 19.1(b). Shared by fig19_1.py.

Run:  python rec19.py > rec19.log

Inputs (book values; sources in the comments):
  M(Si) = 28.0855 u, u = 931.49410 MeV          -- standard atomic weight; Sect. 7.4 prints 26.16 GeV
  <w> = 40.90 meV  arithmetic mean phonon energy of the PBE DOS (Sect. 11.4, imp11.log; NOTATION x_R row)
  E^kin = <w>/4 at T = 0 (harmonic, Sect. 11.4, eq:11.4-IAgauss)
  zero-point energy 123 meV per cell = 3 <w> (Sect. 5.3)
  Phi^(2) = 13.6 eV/A^2, Phi^(3) = -41.5 eV/A^3 along the [111] bond coordinate (Sect. 5.1, 5.7)
  bond length 2.352 A (Sect. 11.3, mph11.log); shortest phonon period 2 pi/omega_opt, measured omega_opt = 64.1 meV
  (Sect. 5.7), PBE 63.6 meV
  E_g = 1.17 eV, physical low-T Si gap (Sect. 3.3)
  E_d(Si): 12.5 eV <111>, 20 eV <100>, 36 eV direction average for a Frenkel pair (DFT MD, Holmstrom et al.,
           as in Sect. 7.4); measured 12.9 +- 0.6 eV (Loferski-Rappaport, Sect. 7.4)
  v_max = 794.5 km/s = 2.650e-3 c (Sect. 1.3 halo; phon11.py)
  interaction length l = 1 A for the Massey parameter (App. E.23 convention)
  binary e-h threshold 352 eV (Si), App. E.23 / Sect. 19.2 (marked on Fig. 19.1b only)
Conventions: hbar = c = 1 internally; hbar c = 1973.26980 eV A; hbar = 6.582119569e-16 eV s.
Criteria (stated in the text): impulse onset x_R = 4 (Sect. 11.4); classical motion (lambda_dB/l_R)^2 <= 0.1;
harmonic motion eta_R^2 <= 0.1 with eta_R = l_R |Phi3| / (3 Phi2); nonadiabatic: exp(-xi_M) = 0.1 and xi_M = 1.
Every boundary energy is found with brentq (root finder), not from a plotting grid.
"""
import numpy as np
from scipy.optimize import brentq

HBARC = 1973.26980          # eV A
HBAR = 6.582119569e-16      # eV s
C = 2.99792458e8            # m/s
U = 931.49410e6             # eV
M = 28.0855 * U             # eV, silicon nucleus (atomic mass; electrons' share negligible here)
W = 40.90e-3                # eV, <omega>
EKIN = W / 4.0              # eV, harmonic T = 0
PHI2, PHI3 = 13.6, -41.5    # eV/A^2, eV/A^3
LANH = 3 * PHI2 / abs(PHI3) # A
BOND = 2.352                # A
EG = 1.17                   # eV
LINT = 1.0                  # A
VMAX = 794.5e3 / C          # units of c
ED = {"<111>": 12.5, "<100>": 20.0, "average (Frenkel pair)": 36.0}
ED_EXP = 12.9
ERTH = 352.0


def k_spring():
    """M <w>^2 in eV/A^2 (Einstein cage of the struck atom)."""
    return M * W**2 / HBARC**2


def ell_R(E):
    """Amplitude (2 E / (M <w>^2))^(1/2) in A of an Einstein oscillator of energy E."""
    return np.sqrt(2 * E / k_spring())


def lam_dB(E):
    """de Broglie wavelength 2 pi / p, p = (2 M E)^(1/2), in A."""
    return 2 * np.pi * HBARC / np.sqrt(2 * M * E)


def eta_R(E):
    return ell_R(E) / LANH


def speed(E):
    """speed (2E/M)^(1/2) in m/s."""
    return np.sqrt(2 * E / M) * C


def xi_M(E):
    """Massey parameter E_g l / (hbar v)."""
    return EG * LINT * 1e-10 / (HBAR * speed(E))


def x_R(E):
    return E / W


def sigma_w(E):
    """Doppler width (4 E_R E^kin)^(1/2) = (E_R <w>)^(1/2) at T = 0."""
    return np.sqrt(4 * E * EKIN)


def mchi_min(E, v=VMAX):
    """smallest dark-matter mass that reaches E_R: E_R = 2 mu^2 v^2 / M."""
    mu = np.sqrt(E * M / 2.0) / v
    if mu >= M:
        return np.inf
    return mu * M / (M - mu)


def main():
    print("# rec19.py: Sect. 19.1 numbers (silicon, T = 0)")
    print("M = %.4f GeV; <w> = %.2f meV; E^kin = %.3f meV; M<w>^2 = %.3f eV/A^2" % (M / 1e9, W * 1e3, EKIN * 1e3, k_spring()))
    print("L_anh = 3 Phi2/|Phi3| = %.4f A" % LANH)
    print("check: lambda_dB / l_R = pi <w>/E_R exactly: at 1 eV %.6f vs %.6f" % (lam_dB(1.0) / ell_R(1.0), np.pi * W / 1.0))
    print()
    print("## Boundaries (root finder)")
    E_xr1 = W
    E_imp = 4 * W
    E_cl = brentq(lambda E: (lam_dB(E) / ell_R(E))**2 - 0.1, 1e-3, 10)
    E_cl_exact = np.pi * W / np.sqrt(0.1)
    E_harm = brentq(lambda E: eta_R(E)**2 - 0.1, 1e-3, 10)
    E_na10 = brentq(lambda E: np.exp(-xi_M(E)) - 0.1, 1, 1e6)
    E_na1 = brentq(lambda E: xi_M(E) - 1.0, 1, 1e6)
    for name, E in [("x_R = 1", E_xr1), ("impulse onset x_R = 4", E_imp),
                    ("classical (lambda/l_R)^2 = 0.1", E_cl), ("harmonic eta_R^2 = 0.1", E_harm),
                    ("E_d <111> (DFT)", ED["<111>"]), ("E_d average FP", ED["average (Frenkel pair)"]),
                    ("binary e-h threshold (Sect. 19.2)", ERTH),
                    ("nonadiabatic exp(-xi_M) = 0.1", E_na10), ("nonadiabatic xi_M = 1", E_na1)]:
        print("%-36s E_R = %10.4g eV   m_chi,min = %9.4g MeV   x_R = %9.4g" % (name, E, mchi_min(E) / 1e6, x_R(E)))
    print("classical boundary analytic pi<w>/sqrt(0.1) = %.4f eV (root %.4f)" % (E_cl_exact, E_cl))
    print("harmonic boundary analytic 0.1 L_anh^2 M<w>^2/2 = %.4f eV" % (0.1 * LANH**2 * k_spring() / 2))
    print()
    print("## Pointwise values")
    for E in [0.1, 0.3, 0.5, 1.0, 12.5, 20.0, 36.0, 100.0, 200.0, 1000.0]:
        print("E_R = %7.1f eV: l_R = %.4f A, lambda_dB = %.5f A, (lam/l)^2 = %.3g, eta_R = %.3f, eta^2 = %.3g, "
              "v = %.2f km/s, xi_M = %.3g, exp(-xi) = %.3g, sigma_w = %.4f eV, sigma_w/E_R = %.4f, angle = %.4f rad = %.2f deg"
              % (E, ell_R(E), lam_dB(E), (lam_dB(E) / ell_R(E))**2, eta_R(E), eta_R(E)**2, speed(E) / 1e3, xi_M(E),
                 np.exp(-xi_M(E)), sigma_w(E), sigma_w(E) / E, np.sqrt(EKIN / E), np.degrees(np.sqrt(EKIN / E))))
    print()
    print("## Worked example 19.1 and text")
    for k, E in ED.items():
        print("E_d %s = %.1f eV: sigma_w = %.3f eV (%.1f %% of E_d), m_chi,min = %.4f GeV, v = %.2f km/s, "
              "bond crossing 2.352 A in %.1f fs" % (k, E, sigma_w(E), 100 * sigma_w(E) / E, mchi_min(E) / 1e9,
                                                    speed(E) / 1e3, BOND * 1e-10 / speed(E) * 1e15))
    print("measured 12.9 eV: sigma_w = %.3f eV" % sigma_w(ED_EXP))
    print("direction smearing (E^kin/E_R)^(1/2) at 12.5 eV: %.4f rad = %.2f deg" % (np.sqrt(EKIN / 12.5), np.degrees(np.sqrt(EKIN / 12.5))))
    print("   this is the rms deflection per transverse component; rms polar angle sqrt(2) x = %.2f deg" % (np.degrees(np.sqrt(2 * EKIN / 12.5))))
    for wopt in (64.1e-3, 63.6e-3):
        print("shortest phonon period 2 pi hbar/omega_opt at omega_opt = %.1f meV: %.1f fs" % (wopt * 1e3, 2 * np.pi * HBAR / wopt * 1e15))
    # 1 - P_Mig at 500 eV (soft limit, P_Mig = 6.068e-3 at 100 eV scaling as E_R, yield19_2.log) and with the exact
    # second-order bracket factor 0.62 at 500 eV (Sect. 12.3-validity)
    pm5 = 6.068e-3 * 5.0
    print("1 - P_Mig at 500 eV: soft limit P_Mig = %.4f (%.2f %%); with the exact bracket x 0.62: %.4f (%.2f %%)" % (pm5, 100 * pm5, 0.62 * pm5, 62 * pm5))
    print("Migdal part of Y_q, model-free lower edge (one pair per Migdal event, 3.8 eV per pair): %.2e" % (3.8 / 100 * 6.068e-3 * 1.0))
    print("200 eV: v = %.2f km/s, first bond crossed in %.1f fs" % (speed(200) / 1e3, BOND * 1e-10 / speed(200) * 1e15))
    print("100 eV: v = %.2f km/s" % (speed(100) / 1e3))
    print("Massey at 20 eV: v = %.3f km/s, xi_M = %.2f; at 1 keV: v = %.2f km/s, xi_M = %.3f" % (speed(20) / 1e3, xi_M(20), speed(1000) / 1e3, xi_M(1000)))
    print("Wigner initial potential energy 3<w>/4 = %.2f meV per atom; ZPE/cell/4 = %.2f meV; 4096 atoms: %.1f eV"
          % (0.75 * W * 1e3, 123.0 / 4, 4096 * 0.75 * W))
    print("zero-point energy per atom 3<w>/2 = %.1f meV (123 meV per two-atom cell / 2 = %.1f meV); estimate of Delta E_zp for a point "
          "defect: 4 neighbors x %.3f eV x 0.3 = %.3f eV" % (1.5 * W * 1e3, 123.0 / 2, 1.5 * W, 4 * 1.5 * W * 0.3))
    print("phonons of mean energy <w> carrying E_d<111>: %.0f" % (12.5 / W))
    m = 0.2e9
    mu = m * M / (m + M)
    Emax = 2 * mu**2 * VMAX**2 / M
    print("opening: m_chi = 200 MeV gives E_R,max = %.2f eV; v = %.2f km/s; bond in %.1f fs; sigma_w = %.3f eV" % (Emax, speed(Emax) / 1e3, BOND * 1e-10 / speed(Emax) * 1e15, sigma_w(Emax)))
    print("heat-only window: recoils below E_d<111> need m_chi < %.4f GeV" % (mchi_min(12.5) / 1e9))


if __name__ == "__main__":
    main()
