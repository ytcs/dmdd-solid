"""Numbers of Worked example 8.2 (Sect. 8.1): the operator O_2 = (v_perp)^2 for
electron scattering in silicon, with the silicon valence electrons modelled as a free
electron gas (no figure).

Model choices (named in the worked example):
  * valence electrons of silicon = free electron gas at n_e = 2.00e23 cm^-3,
    r_s = 2.0, k_F = 3.57 keV (Sect. 4.5 / eq. 2.5-fermi; n_e from App. A.2);
  * T = 0, one pair k -> k + q, Pauli blocking |k| < k_F < |k + q|;
  * momentum transfer q = q0 = alpha m_e = 3.73 keV (Sect. 1.3), energy deposited
    omega = 5 eV; dark-matter mass 100 MeV, lab speed v = 2.0e-3 (natural units),
    v_max = 2.650e-3 (Sect. 1.3).
Kinematics: for a free-gas pair, omega = q . (2k + q)/2m_e, so the parallel electron
momentum is fixed, k_par = m_e omega / q - q/2; the transverse momentum k_T fills an
annulus a < k_T < b, uniform in area (uniform in k_T^2).
Dark matter: v_chi_bar = v - q/2m_chi, q . v_chi_bar = omega (elastic), and its
transverse part has v_T^2 = v^2 - v_min^2 with v_min = omega/q + q/2m_chi.
Per pair (v_perp)^2 = |v_T - v_eT|^2 (parallel parts cancel); averaged over the
azimuth: <(v_perp)^4> = (A + B)^2 + 2AB with A = v_T^2, B = v_eT^2.
"""
import numpy as np

me = 510998.95          # eV, electron mass (CODATA)
alpha = 1/137.035999
q0 = alpha*me           # 3728.9 eV
ne_cm3 = 2.00e23        # valence density of Si, App. A.2 / Sect. 4.5
hbarc_eVcm = 1.973269804e-5
ne = ne_cm3*hbarc_eVcm**3        # eV^3
kF = (3*np.pi**2*ne)**(1/3)      # eV
print(f"k_F = {kF:.1f} eV, v_F = {kF/me:.4e}, E_F = {kF**2/2/me:.2f} eV")

q = q0
omega = 5.0
mchi = 100e6
v = 2.0e-3
vmax = 2.650e-3

kpar = me*omega/q - q/2
b2 = kF**2 - kpar**2                 # initial state inside the sphere
a2 = kF**2 - (kpar + q)**2           # final state outside the sphere
a2 = max(a2, 0.0)
assert b2 > a2
print(f"k_par = {kpar:.1f} eV, k_T in [{np.sqrt(a2):.1f}, {np.sqrt(b2):.1f}] eV")
B1 = (a2 + b2)/2/me**2               # <v_eT^2>
B2 = (a2**2 + a2*b2 + b2**2)/3/me**4 # <v_eT^4>
vmin = omega/q + q/(2*mchi)
A = v**2 - vmin**2
Amax = vmax**2 - vmin**2
print(f"v_min = {vmin:.4e}; v_T^2 = {A:.3e} (v = {v}); at v_max {Amax:.3e}")
print(f"<v_eT^2> = {B1:.3e}; <v_eT^4> = {B2:.3e}; sqrt<v_eT^2> = {np.sqrt(B1):.3e}")
print(f"ratio <v_eT^2>/v_T^2 = {B1/A:.1f}; at v_max {B1/Amax:.1f}")
tot = A**2 + 4*A*B1 + B2
print(f"<(v_perp)^4> = {tot:.3e}")
print(f"  halo-only A^2 : {A**2:.3e} ({A**2/tot*100:.2f} %)")
print(f"  cross 4A<B>   : {4*A*B1:.3e} ({4*A*B1/tot*100:.1f} %)")
print(f"  target <B^2>  : {B2:.3e} ({B2/tot*100:.1f} %)")
# Monte Carlo check of the annulus averages and of the azimuthal formula
rng = np.random.default_rng(1)
N = 400000
kT2 = rng.uniform(a2, b2, N)
phi = rng.uniform(0, 2*np.pi, N)
veT = np.sqrt(kT2)/me
vT = np.sqrt(A)
vperp2 = vT**2 + veT**2 - 2*vT*veT*np.cos(phi)
print(f"MC <(v_perp)^4> = {np.mean(vperp2**2):.3e}")
# naive estimate v^2 ~ 1e-6 squared
print(f"naive (v^2)^2 = {v**4:.2e}; ratio tot/naive = {tot/v**4:.0f}")
