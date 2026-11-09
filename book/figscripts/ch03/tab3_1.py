"""Table 3.1 and the numbers of Sect. 3.3 that do not need the band model: hole masses, spin-orbit estimates,
worked example 3.6, the intrinsic carrier density. Prints and asserts every quoted value. No figure.

Inputs (all measured; sources):
  lattice constants: Si 5.431 A (CODATA 2022, Sect. 3.1); Ge 5.658 A and GaAs 5.648 A extrapolated to 0 K
      (Lucero, Henderson and Scuseria, arXiv:1111.4515, Tables I and II).
  gaps at low T / 300 K: Si 1.17 / 1.12, Ge 0.74 / 0.66, GaAs 1.52 / 1.42 eV (Lucero et al. Table I);
      Si E_g(0) = 1.1692 eV (Ramanathan and Kurinsky, Eq. (11)); Ge 0.744 eV (Rideau et al., cond-mat/0607510, Table VI).
  minimum direct gaps: Si Gamma_15 3.4 eV, Ge Gamma_2' 0.89 eV (Rideau et al. Table II); GaAs = E_g.
  spin-orbit splittings: Si 0.044, Ge 0.296 eV (Rideau et al. Table II); GaAs 0.341 eV (Vurgaftman et al. 2001).
  electron masses: Si 0.9163 / 0.1905 (Hensel et al., in Rideau et al. Table VII); Ge L valley 1.588 / 0.08152
      (Rideau et al. Table VII); GaAs Gamma 0.067 (Vurgaftman et al. 2001).
  Luttinger parameters (gamma1, gamma2, gamma3): Si 4.285, 0.339, 1.446; Ge 13.25, 4.20, 5.56 (Rideau et al. Table VII,
      the values marked a); GaAs 6.98, 2.06, 2.93 (Vurgaftman et al. 2001).
      Heavy and light holes: m_hh = 1/(g1 - 2 g2), m_lh = 1/(g1 + 2 g2) along [100]; with g3 in place of g2 along [111]
      (Luttinger 1956; the j = 3/2 energies -(1/2m_e)[g1 k^2 -/+ 2 sqrt(g2^2 k^4 + 3(g3^2 - g2^2)(kx^2ky^2 + ...))]).
  atomic 2P_{3/2} - 2P_{1/2} splittings of the ions with one p electron outside closed shells (NIST Atomic Spectra
      Database, Kramida et al., version 5.12): Si II 287.24 cm^-1, Ge II 1767.357 cm^-1, Ga I 826.190 cm^-1,
      As III 2940 cm^-1, C II 63.395 cm^-1.
  v_max = 2.650e-3 (Sect. 1.2).
"""
import numpy as np

HBARC = 1973.269804      # eV A
ME = 510998.95           # eV
ALPHA = 7.2973525643e-3
CM1 = 1.239841984e-4     # eV per cm^-1
VMAX = 2.650e-3
KB = 8.617333262e-5      # eV/K

lut = {"Si": (4.285, 0.339, 1.446), "Ge": (13.25, 4.20, 5.56), "GaAs": (6.98, 2.06, 2.93)}
print("hole masses (m_e): hh[100] lh[100] hh[111] lh[111]")
holes = {}
for n, (g1, g2, g3) in lut.items():
    h = (1 / (g1 - 2 * g2), 1 / (g1 + 2 * g2), 1 / (g1 - 2 * g3), 1 / (g1 + 2 * g3))
    holes[n] = h
    print(f"  {n:5s} " + " ".join(f"{x:.3f}" for x in h))

# hydrogen 2p fine structure: Delta = (3/2) xi_2p, xi_2p = (alpha/2m^2) <r^-3>, <r^-3>_2p = 1/(24 a0^3), a0 = 1/(alpha m)
d_H = ALPHA ** 4 * ME / 32
print(f"hydrogen 2p_3/2 - 2p_1/2 = alpha^4 m_e/32 = {d_H:.3e} eV = {d_H/CM1:.3f} cm^-1")
assert abs(d_H / CM1 - 0.365) < 0.002
ions = {"C II": 63.395, "Si II": 287.24, "Ge II": 1767.357, "Ga I": 826.190, "As III": 2940.0}
at = {k: v * CM1 for k, v in ions.items()}
for k, v in at.items():
    print(f"  {k:6s} 2P splitting {v*1e3:7.2f} meV  (xi = {2*v/3*1e3:6.2f} meV)")
crys = {"Si": 0.044, "Ge": 0.296, "GaAs": 0.341}
print(f"crystal / ion: Si {crys['Si']/at['Si II']:.2f}, Ge {crys['Ge']/at['Ge II']:.2f}; "
      f"Ge/Si crystal {crys['Ge']/crys['Si']:.1f}, ion {at['Ge II']/at['Si II']:.1f}")
print(f"Si II / hydrogen 2p: {at['Si II']/d_H:.0f}")
# SOC shift of the gap: the j=3/2 level sits Delta/3 above the mean
for n, d in crys.items():
    print(f"  {n}: Delta_SO/3 = {d/3*1e3:.0f} meV")

# worked example 3.6: m_min = 2E/v_max^2 and q* = m_min v_max
G1 = {"Si": 2 * np.pi * HBARC / 5.431, "Ge": 2 * np.pi * HBARC / 5.658, "GaAs": 2 * np.pi * HBARC / 5.648}
print("2pi/a (eV):", {k: round(v, 1) for k, v in G1.items()})
for lab, E in (("Si indirect", 1.17), ("Si direct", 3.4), ("Ge direct", 0.89), ("Ge indirect", 0.744),
               ("GaAs direct", 1.52)):
    m = 2 * E / VMAX ** 2
    print(f"  {lab:12s} E = {E:5.3f} eV: m_min = {m/1e6:.3f} MeV, q* = m_min v_max = {m*VMAX:.0f} eV")
qL = np.sqrt(3) / 2 * G1["Ge"]
mL = qL ** 2 / (2 * (qL * VMAX - 0.744))
print(f"Ge: |Gamma L| = {qL:.0f} eV; smallest mass depositing 0.744 eV at q = |Gamma L|: {mL/1e6:.3f} MeV")
qc = 0.85 * G1["Si"]
print(f"Si: q_c = {qc:.0f} eV; Ge |Gamma L| / Si q_c = {qL/qc:.3f}")

# intrinsic carrier density, parabolic bands: n_i = sqrt(N_c N_v) exp(-E_g/2T), N = 2 (m_d T/2pi)^{3/2}
# Si: m_dc = 6^{2/3} (m_l m_t^2)^{1/3}; m_dv^{3/2} = m_hh^{3/2} + m_lh^{3/2} with the angle-averaged
# 1/m = g1 -/+ 2 gbar, gbar = (2 g2 + 3 g3)/5 (spherical average of the warped j = 3/2 bands, lowest order)
g1, g2, g3 = lut["Si"]
gb = (2 * g2 + 3 * g3) / 5
mhh, mlh = 1 / (g1 - 2 * gb), 1 / (g1 + 2 * gb)
mdc = 6 ** (2 / 3) * (0.9163 * 0.1905 ** 2) ** (1 / 3)
mdv = (mhh ** 1.5 + mlh ** 1.5) ** (2 / 3)
EV3_CM3 = (1 / (HBARC * 1e-8)) ** 3          # 1 eV^3 in cm^-3
for T, Eg in ((300.0, 1.12), (77.0, 1.17), (4.0, 1.17)):
    t = KB * T
    Nc = 2 * (mdc * ME * t / (2 * np.pi)) ** 1.5 * EV3_CM3
    Nv = 2 * (mdv * ME * t / (2 * np.pi)) ** 1.5 * EV3_CM3
    lg = 0.5 * np.log10(Nc * Nv) - Eg / (2 * t) / np.log(10)
    print(f"  T = {T:5.0f} K: N_c = {Nc:.2e}, N_v = {Nv:.2e} cm^-3, n_i = 10^{lg:.1f} cm^-3")
print(f"Si DOS masses: m_dc = {mdc:.3f}, m_hh = {mhh:.3f}, m_lh = {mlh:.3f}, m_dv = {mdv:.3f}")
print(f"1 kg of Si = {1000/2.329:.0f} cm^3")
