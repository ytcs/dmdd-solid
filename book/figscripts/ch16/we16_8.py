"""Worked example 16.8 (we:16-heat): heat release of 1 g of fused silica after cooling to 10 mK.

Formula: Qdot = (pi^2/24) Pbar V (T_hi^2 - T_lo^2)/t (eq:16.8-heat; Sahling et al., arXiv:1610.03974, Eq. (6)),
with T_hi replaced by the freezing temperature when the starting temperature is higher (its Eq. (7)).
Inputs (Sahling et al., arXiv:1610.03981, Table 1, a-SiO2, from their ref. [7]):
  P_Q = 2.0e44 J^-1 m^-3 (from heat release, t longer than the 'anomalous' relaxation time),
  P_C = 8.0e44 J^-1 m^-3 (from heat capacity), T*_n = 4.8 K (freezing temperature of the normal defects),
  T*_a0 = 14.5 K (of the small anomalous fraction); text: P_a0/P_a = 0.05, P_a/P_n = 3.
Density rho_T = 2.2 g/cm^3, the value used in Sect. 16.7 (Buchenau et al., arXiv:2012.10139, Table I).
Final temperature 10 mK.
"""
import numpy as np

KB_J = 1.380649e-23
EV_J = 1.602176634e-19
m, rho = 1.0, 2.2                         # g, g/cm^3
V_cm3 = m / rho
V_m3 = V_cm3 * 1e-6
PQ, PC = 2.0e44, 8.0e44                    # J^-1 m^-3
Tfrz, Ta0, Tlo = 4.8, 14.5, 0.010          # K
conv = EV_J * 1e-6                          # J^-1 m^-3 -> eV^-1 cm^-3
print(f"V = {V_cm3:.4f} cm^3; P_Q = {PQ*conv:.3g} eV^-1 cm^-3; P_C = {PC*conv:.3g} eV^-1 cm^-3")
pref = np.pi**2 / 24 * KB_J**2 * PQ * V_m3 * (Tfrz**2 - Tlo**2)   # J (Qdot * t)
print(f"t*Qdot = (pi^2/24) k_B^2 P_Q V (T_frz^2 - T_lo^2) = {pref:.4g} J = {pref/EV_J:.4g} eV; "
      f"T_lo^2/T_frz^2 = {Tlo**2/Tfrz**2:.2e}")
for lab, t in (("1 h", 3600.0), ("1 day", 86400.0), ("1 week", 7 * 86400.0), ("1 month (30 d)", 30 * 86400.0)):
    print(f"  t = {lab}: Qdot = {pref/t*1e12:.4g} pW")
E_hw = pref * np.log(7 * 86400 / 3600)
print(f"energy released between 1 h and 1 week: {E_hw:.4g} J = {E_hw/EV_J:.4g} eV (ln 168 = {np.log(168):.3f})")
# the anomalous fraction: P_a0 = 0.05 P_a = 0.15 P_n, with T*_a0 = 14.5 K (Sahling et al. 1610.03981 text and Table 1)
ratio_a0 = 0.05 * 3 * (Ta0**2) / (Tfrz**2)
print(f"anomalous fraction with T*_a0: (P_a0/P_n)(T*_a0/T*_n)^2 = 0.15 x {(Ta0/Tfrz)**2:.2f} = {ratio_a0:.3f} of the normal release")
# heat capacity value instead of heat-release value
print(f"with P_C instead of P_Q the release would be x{PC/PQ:.1f}: {pref*PC/PQ/3600*1e12:.4g} pW at 1 h")
# stored energy per unit lambda per gram, and per decade of time (dlambda = ln(10)/2 per decade)
Est = np.pi**2 / 12 * KB_J**2 * PQ * V_m3 * Tfrz**2
print(f"stored energy per unit lambda: {Est:.4g} J; per decade of time: {Est*np.log(10)/2:.4g} J = t Qdot ln 10 = {pref*np.log(10):.4g} J")
# Sect. 16.7 value of Pbar from the tunneling strength C = 2.6e-4 with gamma_l = 1 eV: 1.2e20 eV^-1 cm^-3 (quoted, not recomputed here)

# the same fraction with the freezing temperatures of the text of Sahling et al. 2014 (5.5 K and 14.1 K), and the
# source's own statement (anomalous part "roughly 2 times larger" than the normal one); P_a/P_n = 3 is the ratio of the
# stress-lowered defects to the normal (heat-release) density, (P_C - P_Q)/P_Q = (8.0 - 2.0)/2.0
print(f"P_a/P_n = (P_C - P_Q)/P_Q = {(8.0 - 2.0) / 2.0:.1f}")
print(f"anomalous fraction with the text freezing temperatures 5.5 K and 14.1 K: 0.15 x (14.1/5.5)^2 = {0.15 * (14.1 / 5.5)**2:.2f}")
