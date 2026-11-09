"""Worked example 11.3 and the numbers of the running text of Sect. 11.2. Inputs and sources: pol11_2.py.
Prints: I_pol/rho_T of GaAs on three routes and of LiF; the mass edges 2 omega_L/v_max^2; the ratio of light-mediator rates of
LiF and GaAs at several masses (one branch each, kinematic weight K of eq:11.2-K); the temperature factor at 10 mK; the
Debye-Waller exponent at the LO edge momentum; and the check of eq:11.2-onebranch against eq:11.2-SZZ (Gamma eigenvector).
"""
import numpy as np
import pol11_2 as P

g = P.GAAS
Om = (g["a"]**3 / 4) / P.HBARC**3
Mc = (P.M_GA + P.M_AS) * P.U_EV
rho = Mc / Om
rho_g = rho * P.EV_G / P.CM3_EV3
to_meV_cm3_g = 1e3 / rho_g
D = 1 / g["epsinf"] - 1 / g["eps0"]
I_eps = np.pi / 2 * g["wL"] * D
I_split = np.pi / 2 * (g["wL"]**2 - g["wT"]**2) / (g["epsinf"] * g["wL"])
print(f"GaAs rho_T = {rho_g:.3f} g/cm^3 (a = {g['a']} A, M_cell = {(P.M_GA+P.M_AS):.3f} u)")
print(f"GaAs 1/eps_inf - 1/eps_0 = {D:.5f}; I_pol (eps route) = {I_eps*1e3:.4f} meV -> {I_eps*to_meV_cm3_g:.4f} meV cm^3/g")
print(f"GaAs I_pol (splitting route) = {I_split*1e3:.4f} meV -> {I_split*to_meV_cm3_g:.4f} meV cm^3/g;"
      f" ratio eps/split = {I_eps/I_split:.4f}")
I_dft = P.band_integral_diatomic(2.27, 10.9, 34.9e-3, P.M_GA, P.M_AS)
I_meas = P.band_integral_diatomic(2.11, 10.88, 36.35e-3, P.M_GA, P.M_AS)
I_lif = P.band_integral_diatomic(1.05, 2.02, 77.2e-3, P.M_LI, P.M_F)
print(f"Omega-free form: GaAs (Z* 2.11, eps 10.88, wL 36.35) = {I_meas:.4f}; GaAs (Table I DFT: 2.27, 10.9, 34.9) = {I_dft:.4f};"
      f" LiF (Table I: 1.05, 2.02, 77.2) = {I_lif:.3f} meV cm^3/g")
print(f"LiF/GaAs = {I_lif/(I_split*to_meV_cm3_g):.1f} (vs splitting route), {I_lif/I_dft:.1f} (both Table I)")
mu_lif = P.mu_red(P.M_LI, P.M_F)
print(f"LiF M_cell = {P.M_LI+P.M_F:.3f} u, mu = {mu_lif:.4f} u; GaAs mu = {P.mu_red(P.M_GA,P.M_AS):.3f} u")
# Omega-free pieces for the text: factors that make LiF larger
fac = {"Z*^2": (1.05 / 2.27)**2, "1/eps_inf^2": (10.9 / 2.02)**2, "1/(M_cell mu)": (P.M_GA + P.M_AS) * P.mu_red(P.M_GA, P.M_AS) /
       ((P.M_LI + P.M_F) * mu_lif), "1/omega_L": 34.9 / 77.2}
print("LiF/GaAs factors (Table I values):", {k: round(v, 3) for k, v in fac.items()}, " product", round(np.prod(list(fac.values())), 1))
for nm, wl in (("GaAs", g["wL"]), ("LiF", 77.2e-3), ("sapphire top LO", 906.6 * P.CM_MEV * 1e-3)):
    print(f"edge 2 omega_L/v_max^2 {nm}: {2*wl/P.VMAX**2/1e3:.2f} keV")
for m in (25e3, 30e3, 50e3, 100e3, 1e6):
    kg, kl = P.K_light(g["wL"], m), P.K_light(77.2e-3, m)
    print(f"m = {m/1e3:6.0f} keV: K(GaAs) = {kg:.4f}, K(LiF) = {kl:.4f}, K ratio = {kl/kg:.3f};"
          f" rate ratio LiF/GaAs (Table I LiF, splitting-route GaAs) = {I_lif*kl/(I_split*to_meV_cm3_g*kg):.2f}")
T = 10e-3 * 8.617333e-5
print(f"10 mK: omega_L/T = {g['wL']/T:.3e}")
# Debye-Waller exponent at q = omega_L/v_max using the DFPT <u_x^2> of Table 5.1 (0.040 A rms, Ga, 0 K)
q = g["wL"] / P.VMAX / P.HBARC     # A^-1
print(f"q = omega_L/v_max = {g['wL']/P.VMAX:.2f} eV = {q:.5f} A^-1; 2W = q^2 <u_x^2> = {q**2*0.040**2:.2e}")
# one-branch from the Born-charge form with the Gamma eigenvector (exact identity, numerical check)
mu = P.mu_red(P.M_GA, P.M_AS) * P.U_EV
lhs = np.pi * 2.108**2 / (Om * mu * g["epsinf"]**2 * g["wL"])
rhs = np.pi * g["wL"] / P.E2 * (1 / g["epsinf"] - 1 / (g["epsinf"] * g["wL"]**2 / g["wT"]**2))
print(f"S_ZZ/q^2 one-branch: Born form {lhs:.5e}, LST form {rhs:.5e}")
