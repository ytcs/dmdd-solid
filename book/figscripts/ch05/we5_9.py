"""Worked example 5.9 (Sect. 5.7): Klemens decay of the silicon zone-center optical phonon against the measured width.
Prints every number of the worked example and of the small-parameter estimates of Sect. 5.7.
Inputs and sources:
  omega0 = 64.1 meV (15.5 THz), Nilsson and Nelin, Phys. Rev. B 6, 3777 (1972) (book value, Sects. 5.1-5.3).
  Low-temperature Raman width (FWHM) 1.45 cm^-1, measured by Menendez and Cardona, Phys. Rev. B 29, 2051 (1984), as tabulated
    with the three-phonon DFPT (LDA) result 1.43 cm^-1, the channel shares LA+TA 94.3 %, LA+LA 5.7 % and the experimental
    spread 1.24-2.1 cm^-1 in Debernardi, Baroni and Molinari, arXiv cond-mat/9408051, Table 1 and text ("full widths 2Gamma").
  Bond-coordinate surface of Fig. 5.1(c) (fig5_1.py, WE 5.1, WE 5.5): Phi_opt = 13.6 eV/A^2, Phi3_opt = -41.5 eV/A^3,
    Phi4_opt ~ 90 eV/A^4, zero-point length l_zp = 0.048 A; kappa_BO = 0.0665 (WE 5.1).
  Constant-vertex temperature factor at 300 K and the PBE kinematics: printed by fig5_6.py (2.014; TA max 26.4 meV).
Run: python we5_9.py   (numpy only)
"""
import numpy as np

CM1 = 0.123984198      # meV per cm^-1
HBAR = 6.582119569e-13  # meV s
KB = 8.617333262e-2     # meV/K
w0 = 64.1
g_meas, g_calc = 1.45, 1.43        # cm^-1, FWHM
nB = lambda w, T: 1.0 / np.expm1(w / (KB * T))

g = g_meas * CM1
print("measured width %.2f cm^-1 = %.4f meV; gamma/omega0 = %.2e; omega0/gamma = %.0f" % (g_meas, g, g / w0, w0 / g))
tau = HBAR / g
print("lifetime 1/gamma = %.2f ps (rate %.2e s^-1); period 2pi/omega0 = %.1f fs; periods per lifetime %.0f; "
      "amplitude oscillations in 1/(pi gamma)... %.0f"
      % (tau * 1e12, 1 / tau, 2 * np.pi * HBAR / w0 * 1e15, tau / (2 * np.pi * HBAR / w0), w0 / (np.pi * g)))
print("DFPT three-phonon %.2f cm^-1 = %.4f meV, %.1f %% of measured; spread 1.24-2.1 cm^-1 = %.3f-%.3f meV"
      % (g_calc, g_calc * CM1, 100 * g_calc / g_meas, 1.24 * CM1, 2.1 * CM1))

# small parameter
Phi2, Phi3, Phi4, l, kap = 13.6, 41.5, 90.0, 0.048, 0.0665
eta = Phi3 * l / (3 * Phi2)
print("eta_anh = |Phi3| l/(3 Phi2) = %.3f; eta^2 = %.2e; kappa^2 = %.2e; (gamma/omega0)/eta^2 = %.2f"
      % (eta, eta ** 2, kap ** 2, (g / w0) / eta ** 2))
print("quartic/harmonic energy at l: Phi4 l^2/(12 Phi2) = %.2e" % (Phi4 * l ** 2 / (12 * Phi2)))
print("length scale of the cubic term 3 Phi2/|Phi3| = %.2f A" % (3 * Phi2 / Phi3))

# Klemens
for T in (0.01, 77.0, 300.0):
    n = nB(w0 / 2, T) if T > 1 else 0.0
    print("T = %6.2f K: n_B(omega0/2) = %.4f, Klemens factor %.3f, width %.2f cm^-1"
          % (T, n, 1 + 2 * n, g_meas * (1 + 2 * n)))
print("at 10 mK: omega0/(2 kB T) = %.3e (n_B = exp(-that))" % (w0 / 2 / (KB * 0.01)))
print("constant-vertex model at 300 K (fig5_6.py factor 2.014): %.2f cm^-1" % (g_meas * 2.014))
print("omega0/kB = %.0f K" % (w0 / KB))
