"""Table 8.4 and Worked example 8.7 (Sect. 8.5): the small parameters of the expansion hierarchy with silicon values.
Prints every number quoted in Sect. 8.5 and asserts the identities the section states. No new first-principles input.

Inputs and sources (all already used in earlier sections):
  kappa_BO = (m_e/M)^{1/4} with M = 26.16 GeV (natural silicon), as Sect. 5.1 / WE 5.1 and App. D.13.
  eta_anh = 0.049 (Sect. 5.7, we5_9.py: |Phi3| l_zp / (3 Phi2) with Phi2 = 13.6 eV/A^2, Phi3 = -41.5 eV/A^3, l_zp = 0.048 A).
  Electron-phonon vertices (Sect. 6.2): optical deformation potential of the Si holes, |g| ~ 0.25 eV; LA vertex of the Si
    conduction valleys at Q = 0.01 A^-1, |g| = 26 meV. Off-shell distance of the photon-first ordering at the Si absorption
    edge ~ 2 eV, denominators 2-3 eV (Sect. 6.5).
  Phonon density of states: DFPT (PBE) of Sect. 5.2, fig5_2_data.npz, per atom normalized to 3, as in we5_7.py.
    Natural Si mass 28.0855 u = 26.16 GeV for recoil energies (as Sect. 5.6).
  Phonon energies at X: TA 18.57 meV, TO 57.49 meV (neutron, Sect. 5.2); optical phonon at Gamma 64.1 meV (Sect. 5.1).
  omega_D = 55.6 meV from the measured elastic constants (WE 5.3, we5_3.py).
  Gap E_g = 1.17 eV (Sect. 3.3). Detector temperature 10 mK (Sects. 5.7, 6.5).
  Kick duration of a Si nucleus ~ 4e-21 s (contact interaction, R = 3.5 fm, v_max; Sect. 6.1).
  Si nucleus kicked by 1 GeV dark matter at the largest momentum transfer, v_N = 1.95e-4, m_e v_N = 100 eV (Sect. 6.1).
  q_0 = alpha m_e = 3.73 keV = 1.89 A^-1 (Sect. 1.3); v ~ 1e-3 for the dark-matter speed.
Modelling choice: the "size of the excited orbital" in xi_D is taken as 1 A (half the Si bond, 2.35 A), an order-of-magnitude length.
Run: python tab8_4.py   (numpy)
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CH5 = os.path.join(HERE, '..', 'ch05')
U_EV = 931.49410242e6          # eV per u (CODATA 2018)
HBARC = 1973.269804            # eV Angstrom
KB = 8.617333262e-5            # eV/K
CM = 1.239841984e-4            # eV per cm^-1
HBAR = 6.582119569e-16         # eV s
ME = 0.51099895e6              # eV

print('=' * 30, 'Sect. 8.5, Table 8.4', '=' * 30)

# --- kappa_BO -------------------------------------------------------------------------------------------------
MNAT = 28.0855 * U_EV   # natural silicon
kBO = (ME / MNAT) ** 0.25
print('kappa_BO = %.4f, kappa^2 = %.3e, kappa^4 = m_e/M = %.3e' % (kBO, kBO ** 2, kBO ** 4))

# --- theta_ep -------------------------------------------------------------------------------------------------
for g, lab in ((0.25, 'optical, holes'), (0.026, 'LA, Q = 0.01/A')):
    for d in (2.0, 2.5, 0.5, 0.25):
        print('theta_ep: |g| = %.3f eV (%s), delta_off = %.2f eV -> %.2e' % (g, lab, d, g ** 2 / d ** 2))
print('theta_ep = 1 at delta_off = |g| = 0.25 eV (optical vertex)')

# --- eta_anh ----------------------------------------------------------------------------------------------------
eta = 0.049
print('eta_anh = %.3f, eta^2 = %.1e' % (eta, eta ** 2))

# --- thermal ----------------------------------------------------------------------------------------------------
T = 10e-3 * KB
print('T = 10 mK = %.3f micro-eV' % (T * 1e6))
for w, lab in ((18.57e-3, 'TA(X)'), (57.49e-3, 'TO(X)'), (64.1e-3, 'optical Gamma'), (1.17, 'E_g')):
    print('  T/omega (%s) = %.2e, omega/T = %.3g, n_B = exp(-%.0f)' % (lab, T / w, w / T, w / T))
wD = 55.6e-3
print('  Debye fraction of modes with omega < T: (T/omega_D)^3 = %.1e' % ((T / wD) ** 3))

# --- x_R and 2W ---------------------------------------------------------------------------------------------------
d = np.load(os.path.join(CH5, 'fig5_2_data.npz'))
w = d['dos'][:, 0] * CM
g = d['dos'][:, 1] / CM
g *= 6 / np.trapezoid(g, w)
ga = g / 2                     # per atom, normalized to 3
m = w > 0
w, ga = w[m], ga[m]
norm = np.trapezoid(ga, w)
mean_w = np.trapezoid(ga * w, w) / norm            # arithmetic mean over the per-atom DOS
inv_mean = norm / np.trapezoid(ga / w, w)         # harmonic mean <omega^-1>^-1
print('<omega> (arithmetic, per-atom DOS) = %.2f meV; <omega^-1>^-1 = %.2f meV; ratio %.3f'
      % (mean_w * 1e3, inv_mean * 1e3, mean_w / inv_mean))
assert mean_w >= inv_mean                         # Jensen: x_R <= 2W(T = 0)
M = 28.0855 * U_EV
for q in (10e3, 20e3, 40e3, 50e3, 100e3, 200e3):
    ER = q ** 2 / (2 * M)
    xR = ER / mean_w
    W2 = ER / inv_mean
    print('q = %5.0f keV: E_R = %7.3f meV, x_R = %.3f, 2W(T=0) = %.3f, rms/E_R = x_R^-1/2 = %.2f'
          % (q / 1e3, ER * 1e3, xR, W2, xR ** -0.5))
print('x_R = 1 at q = %.1f keV; 2W(T=0) = 1 at q = %.1f keV'
      % (np.sqrt(2 * M * mean_w) / 1e3, np.sqrt(2 * M * inv_mean) / 1e3))
# T = 0 cumulants of the self response: kappa_n = E_R <omega^{n-1}> (per-atom DOS normalized to 3, cubic site)
kap2 = np.trapezoid(ga * w, w) / norm
assert abs(kap2 / mean_w - 1) < 1e-12
# impulse: rms width below E_R/3 for x_R >= 9
print('x_R = 9 at q = %.0f keV (E_R = %.2f eV)' % (np.sqrt(2 * M * 9 * mean_w) / 1e3, 9 * mean_w))

# --- suddenness ---------------------------------------------------------------------------------------------------
tau = 4e-21
Eg = 1.17
print('1/E_g = %.3f fs; E_g tau_acc = %.1e' % (HBAR / Eg * 1e15, Eg * tau / HBAR))
r = 64.1e-3 / Eg
print('omega_opt/E_g = %.4f; lattice factor [1-(omega/E)^2]^-2 = %.4f' % (r, (1 - r ** 2) ** -2))

# --- xi_D ---------------------------------------------------------------------------------------------------------
L = 1.0 / HBARC                # 1 A in eV^-1
print('xi_D: electron scattering q_0 = 3.73 keV x 1 A = %.2f' % (3.73e3 * L))
print('xi_D: Migdal boost m_e v_N = 100 eV x 1 A = %.3f' % (100 * L))
for mphi in (1.0, 10.0, 100.0):
    print('xi_D: absorption m_phi = %5.0f eV, q = 1e-3 m_phi -> %.1e' % (mphi, 1e-3 * mphi * L))
