"""Numbers of Worked example 8.6 (Sect. 8.4): the nucleon-number coupling of a
heavy scalar in GaAs, screened by the Born charges.

Finite-q vertex (corrected after the Sect. 11.2 check): read from the DFPT phonons at
q cached by figscripts/ch11/we8_6_check.py (gaas11_2_work/we86_*.npz); the earlier
zone-center-eigenvector-with-site-phase estimate (0.61, 4.5) was gauge dependent.

Prints every number quoted in the worked example and in the GaAs sentences of
Sect. 8.4, and checks the pole algebra of the rank-one screened response.
Runs in a second (numpy; imports figscripts/ch11/gaas11_2.py, reads its cache).

Inputs and sources
- omega_T = 8.13 THz = 33.62 meV, omega_L = 8.79 THz = 36.35 meV: inelastic
  neutron scattering, Strauch and Dorner (1990), as used in Worked example 5.6
  (we:5-lst); same values as there.
- eps_inf = 10.88, eps_0 = 12.9: infrared spectroscopy, Lockwood et al. (2005),
  as in Worked example 5.6.
- a = 5.638 Angstrom, Omega = a^3/4 = 44.80 Angstrom^3: Table E.functionals, as in
  Worked example 5.6.
- Atomic masses (u): 69Ga 68.925573528, 71Ga 70.924702554, 75As 74.921594562,
  AME2020 (Wang et al., Chin. Phys. C 45, 030003 (2021)), file mass_1.mas20.txt
  of the AMDC.
- Isotopic abundances of natural Ga: 69Ga 0.60108, 71Ga 0.39892 (IUPAC 2013,
  Meija et al., Pure Appl. Chem. 88, 293 (2016); CIAAW table). As is
  monoisotopic (75As).
- Z*: from the LO-TO splitting, Z*^2 = Omega eps_inf mu (wL^2 - wT^2)/e^2, as in
  Worked example 5.6 (2.11).
"""
import numpy as np

hbar_c_eVA = 1973.269804      # eV Angstrom
u_eV = 931.49410242e6          # eV per atomic mass unit (CODATA 2018)
alpha = 1 / 137.035999084
e2 = 4 * np.pi * alpha         # Heaviside-Lorentz

# --- measured GaAs inputs (Worked example 5.6) -----------------------------
wT = 33.62e-3                  # eV
wL = 36.35e-3                  # eV
eps_inf = 10.88
eps_0 = 12.9
a = 5.638                      # Angstrom
Omega_A3 = a**3 / 4
Omega = Omega_A3 / hbar_c_eVA**3   # eV^-3

# --- masses and abundances --------------------------------------------------
m69, m71, m75 = 68.925573528, 70.924702554, 74.921594562   # u, AME2020
x69, x71 = 0.60108, 0.39892                                 # IUPAC 2013
M_Ga = x69 * m69 + x71 * m71
A_Ga = x69 * 69 + x71 * 71
M_As, A_As = m75, 75
Z_Ga, Z_As = 31, 33
mu_u = M_Ga * M_As / (M_Ga + M_As)
M_cell = M_Ga + M_As
mu = mu_u * u_eV

print(f"Omega = {Omega_A3:.2f} A^3 = {Omega:.4g} eV^-3")
print(f"M_Ga (natural) = {M_Ga:.4f} u, mean A_Ga = {A_Ga:.4f}; M_As = {M_As:.4f} u")
print(f"mu_red = {mu_u:.2f} u = {mu/1e9:.2f} GeV; M_cell = {M_cell:.2f} u")

# Born charge from the splitting (as Worked example 5.6)
Zs = np.sqrt(Omega * eps_inf * mu * (wL**2 - wT**2) / e2)
print(f"Z* from LO-TO splitting = {Zs:.3f}")
print(f"wL^2 - wT^2 = {wL**2 - wT**2:.4g} eV^2; LST check eps0/epsinf = {eps_0/eps_inf:.3f}, (wL/wT)^2 = {(wL/wT)**2:.3f}")

# --- nucleon-number vertex of the optical mode ------------------------------
r_Ga, r_As = A_Ga / M_Ga, A_As / M_As
dA = r_Ga - r_As          # per u
print(f"A/M: Ga {r_Ga:.6f}, As {r_As:.6f} per u; Delta_A = {dA:.3e} per u")
print(f"  per Ga isotope: 69Ga {69/m69:.6f}, 71Ga {71/m71:.6f} per u; spread {69/m69 - 71/m71:.2e} per u")
muDA = mu_u * dA
print(f"mu*Delta_A = {muDA:.3e} (dimensionless)")

# proton-number (Z) vertex for contrast
dZ = Z_Ga / M_Ga - Z_As / M_As
print(f"Z/M: Ga {Z_Ga/M_Ga:.5f}, As {Z_As/M_As:.5f}; Delta_Z = {dZ:.3e} per u; mu*Delta_Z = {mu_u*dZ:.3f}")

# total-charge vertex of the LO mode after screening: Z*/eps_inf
print(f"Z*/eps_inf = {Zs/eps_inf:.3f}")

# --- ratios of LO weights per unit coupling squared -------------------------
# nucleon: R_NN = q^2 mu Delta^2 / (Omega (w^2 - wL^2))  [Delta in 1/mass]
# charge : R_ZZ = q^2 Z*^2 / (Omega mu eps_inf^2 (w^2 - wL^2))
ratio_N_vs_Z = (muDA * eps_inf / Zs) ** 2
ratio_p_vs_Z = (mu_u * dZ * eps_inf / Zs) ** 2
print(f"LO weight, nucleon number / total charge = {ratio_N_vs_Z:.2e}")
print(f"LO weight, proton number / total charge  = {ratio_p_vs_Z:.2f}")

# LO vs LA, first-moment (energy-weighted) weights at the same small q
# LA: q^2 (A_cell)^2/(2 M_cell); LO: q^2 mu Delta^2 / 2
A_cell = A_Ga + A_As
ratio_LO_LA = mu_u * dA**2 * M_cell / A_cell**2
print(f"energy-weighted LO/LA weight for nucleon number = {ratio_LO_LA:.2e}")

# --- finite q: the vertex with the phonons at q (Sect. 11.2 cache) -----------
# The zone-center eigenvectors combined with the site phases exp(i q.tau) give a gauge-dependent vertex (it changes
# when another As is assigned to the cell); the corrected numbers use the DFPT eigenvectors at q, interpolated by
# figscripts/ch11/gaas11_2.py and cached in figscripts/ch11/gaas11_2_work/we86_{111,100}.npz by we8_6_check.py.
# Only the cache is read here; no QE run. [111] of this example is [-1,1,1] in the axes of the force-constant file.
import os, sys
CH11 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ch11")
sys.path.insert(0, CH11)
import gaas11_2 as G
dtau_A = np.sqrt(3) * a / 4
vmax = 2.650e-3                      # Sect. 8.2 (fig. 8.1), v_esc + v_E
qmin = wL / vmax                     # smallest q that deposits omega_L
print(f"|tau_As - tau_Ga| = {dtau_A:.3f} A; q_min for omega_L at v_max: {qmin:.1f} eV")
muG = G.M_GA * G.M_AS / (G.M_GA + G.M_AS)
McG = G.M_GA + G.M_AS
for name, tag in (("[111] (bond)", "we86_111"), ("[100]", "we86_100")):
    cache = os.path.join(G.WORK, tag + ".npz")
    if not os.path.exists(cache):
        raise SystemExit(f"missing {cache}: run figscripts/ch11/we8_6_check.py first (needs QE matdyn.x)")
    d = np.load(cache)
    qs, w, e = d["q"], d["w"], d["e"]
    qeV = np.linalg.norm(qs, axis=1) * 2 * np.pi / G.A_ANG * hbar_c_eVA
    amp = G.nucleon_amplitude(qs, w, e)
    ampM = G.nucleon_amplitude(qs, w, e, A=(G.M_GA, G.M_AS))
    aN = np.abs(np.sqrt(muG) * amp[:, 5])
    aLA = np.abs(amp[:, 2]) * np.sqrt(McG)
    share = aN**2 * McG / (muG * aLA**2)
    for i, q in enumerate(qeV):
        print(f"  {name:12s} q = {q:6.2f} eV: |a_N| = {aN[i]:.3g} ({aN[i]/muDA:.0f} x q->0 value); "
              f"LA vertex {aLA[i]:.1f}; energy-weighted optical share {share[i]:.2g}; mass-density vertex {abs(np.sqrt(muG)*ampM[i,5]):.3g}")
    if "111" in name:
        k = np.argmin(abs(qeV - 13.7))
        slope = aN[k] / qeV[k]
        print(f"  [111] drag slope {slope:.4f} per eV (13.7 eV), {aN[-1]/qeV[-1]:.4f} per eV (100 eV); "
              f"overtakes the q->0 value {muDA:.2e} near q = {muDA/slope:.3f} eV")

# --- algebra check of the rank-one screened response ------------------------
# proper: R_NN~ = q^2 mu D^2/(Omega (w^2-wT^2)), R_NZ~ = q^2 D Z*/(Omega (w^2-wT^2)),
# eps = eps_inf - e^2 Z*^2/(mu Omega (w^2 - wT^2)); full = R_NN~ + vC R_NZ~^2/eps
q = 3.0e3          # eV, any value
vC = e2 / q**2
D = dA / u_eV      # 1/eV
for w in [0.010, 0.030, 0.0345, 0.040]:
    den = w**2 - wT**2
    Rnn = q**2 * mu * D**2 / (Omega * den)
    Rnz = q**2 * D * Zs / (Omega * den)
    eps = eps_inf - e2 * Zs**2 / (mu * Omega * den)
    full = Rnn + vC * Rnz**2 / eps
    lo = q**2 * mu * D**2 / (Omega * (w**2 - wL**2))
    print(f"  w = {w*1e3:5.1f} meV: full/LO-pole form = {full/lo:.12f}; eps = {eps:+.3f}")

# eps at omega_L vanishes: 1/|eps|^2 diverges there
den = wL**2 - wT**2
print(f"eps(omega_L) = {eps_inf - e2*Zs**2/(mu*Omega*den):.2e}")

# --- ionic part of eps at electronic energies (Coulomb-line classes) --------
for w in [1.5]:
    eps_ion = -(eps_0 - eps_inf) * wT**2 / (w**2 - wT**2)
    print(f"ionic part of eps at {w} eV: {eps_ion:.2e} (absolute), relative to eps_inf {abs(eps_ion)/eps_inf:.1e}")

# --- transverse-photon line in scattering: Pi/q^2 ~ omega_p^2/q^2 at q0 -----
wp = 16.6          # eV, Si valence plasma energy (Sect. 4.3)
q0 = 3.73e3        # eV
print(f"omega_p^2/q0^2 (Si) = {(wp/q0)**2:.1e}")
