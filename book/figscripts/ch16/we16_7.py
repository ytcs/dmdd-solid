"""Worked example 16.7 (we:16-tls-dp): the dark-photon rate on thermal SiO2.
Inputs: tan delta_0 = 3.0e-4 (thermal SiO2, low power, T <= 100 mK, ~6 GHz; O'Connell et al. arXiv:0802.2404 Table I,
range 3.0-3.3e-4); PECVD SiO2 5e-3 (Martinis et al. cond-mat/0507622) for comparison; eps_r = 3.9 (assumed);
rho_T = 2.2 g/cm^3 [Bu20]; rho_chi = 0.3 GeV/cm^3; T = 10 mK; m_phi = 6 GHz x h = 24.81 ueV.
Formula: R = (rho_chi/rho_T) zeta^2 tan(delta_0) tanh(m/2T)/eps_r  (Sect. 16.7).
Dipole check: tan delta_0 = pi P_bar p^2/(3 eps_r) (Heaviside-Lorentz, e^2 = 4 pi alpha), with P_bar from tls16_7.py.
Run: python we16_7.py > we16_7.log
"""
import numpy as np
import tls16_7 as L

T = 0.010 * L.KELVIN
m = 6.0 * L.GHZ
print("m_phi = %.4e eV (6 GHz); T = %.4e eV; m/2T = %.4f; tanh = %.6f" % (m, T, m / (2 * T), np.tanh(m / (2 * T))))
Lval = L.TAND_THERMAL * np.tanh(m / (2 * T)) / L.EPS_R
print("L = tan d0 tanh / eps_r = %.4e" % Lval)
rate_nat = L.RHO_CHI / L.RHO_T * Lval
per_kg_yr = rate_nat * L.KG * L.YEAR
print("rho_chi/rho_T = %.4e GeV/g; /hbar = %.4e per g per s" % (0.3 / 2.2, 0.3 / 2.2 / 6.582119569e-25))
print("R = %.4e zeta^2 per kg per yr" % per_kg_yr)
print("zeta for 3 events in 1 kg yr: %.4e" % np.sqrt(3 / per_kg_yr))
print("tan d0 = 3.3e-4: R x %.3f, zeta x %.3f" % (3.3 / 3.0, np.sqrt(3.0 / 3.3)))
print("tan d0 = 5e-3: R x %.2f, zeta x %.3f" % (5e-3 / 3e-4, np.sqrt(3e-4 / 5e-3)))
film = 100 * 1e-4 * 2.2e-3   # kg: 100 cm^2 x 1 um x 2.2 g/cm^3
print("film 100 cm^2 x 1 um: mass %.4e kg; zeta for 3 events in 1 yr: %.4e" % (film, np.sqrt(3 / (per_kg_yr * film))))
for TK in (0.02, 0.05, 0.1):
    print("T = %.0f mK: tanh(m/2T) = %.4f" % (TK * 1e3, np.tanh(m / (2 * TK * L.KELVIN))))
# dipole check
Pb = L.pbar()                           # eV^-1 cm^-3
e2 = 4 * np.pi / 137.035999 * L.HBARC_EV_CM     # eV cm
p2 = 3 * L.EPS_R * L.TAND_THERMAL / (np.pi * Pb)   # eV cm^3
d = np.sqrt(p2 / e2) * 1e8               # Angstrom
print("P_bar = %.3e eV^-1 cm^-3 -> p = %.4f e A = %.3f D" % (Pb, d, d * 4.80320))
# energy per event and power at the reach
print("deposit per absorption = m_phi = %.2f ueV" % (m * 1e6))
# drive strength of the dark-matter field on one two-level system: E = zeta (2 rho_chi)^(1/2) (Sect. 11.8),
# Rabi frequency Omega_R = 2 p E (Delta_0/Delta_tl) <= 2 p E, against the one-phonon rate at Delta_tl = m (u = 1, T -> 0)
zeta = np.sqrt(3 / per_kg_yr)
E = zeta * np.sqrt(2 * L.RHO_CHI)
p_nat = np.sqrt(4 * np.pi / 137.035999) * d * L.ANG       # e d in eV^-1
Om = 2 * p_nat * E
tau = L.k_jackle() * m**3
print("field at zeta = %.3e: E = %.4e eV^2; p = %.4e eV^-1; Omega_R <= %.4e eV = %.4e s^-1; tau1^-1(m) = %.4e s^-1"
      % (zeta, E, p_nat, Om, Om * L.SEC, tau * L.SEC))
v = 354.1 * L.KMS
pphi = m * v
print("p_phi = m v (v = 354.1 km/s) = %.4e eV; wavelength 2 pi/p = %.2f m" % (pphi, 2 * np.pi / pphi * L.HBARC_EV_CM / 100))
lam = 2 * np.pi / (20.0 * 1e-3) * L.HBARC_EV_CM * 1e4
print("de Broglie wavelength of 20 eV at v = 1e-3: %.1f um" % lam)
