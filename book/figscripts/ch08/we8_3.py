"""Numbers of Sect. 8.2: Worked example 8.3 (density and spin couplings in a spin-polarized electron gas) and the
Born-approximation estimate of the conditions subsection. Natural units hbar = c = k_B = 1, energies in eV.

Model (derived in the text of Sect. 8.2 and in Sect. 4.2, Worked example 4.3):
  per-spin independent-particle structure factor of a free Fermi sphere of radius k_F (half of eq:4.2-gas):
    S_sigma(q, w) = (m / 4 pi q) (k_F^2 - k_min^2),  k_min = max(|m w/q - q/2|, sqrt(max(k_F^2 - 2 m w, 0))), if k_min < k_F
  linear region (w < q v_F - q^2/2m): S_sigma = m^2 w / (2 pi q), independent of k_F.
  2 x 2 response matrix in the rows (n_e, s^z_e) for spins quantized along z, spin-conserving channel:
    S_nn = S_up + S_dn,  S_ns = S_sn = (S_up - S_dn)/2,  S_ss = (S_up + S_dn)/4.
  Fully polarized gas (only the up sphere, radius 2^(1/3) k_F at the same density): S_ns = S_nn/2, S_ss = S_nn/4 (rank one).
Inputs (all as quoted earlier in the book):
  valence density of silicon n_e = 2.00e23 cm^-3 (Sects. 4.2, 4.5; App. A.2), m_e = 510998.95 eV,
  hbar c = 197.3269804 eV nm, q_0 = alpha m_e = 3.73 keV, w = 5 eV, m_chi = 100 MeV, v = 2.0e-3 (Worked example 8.2),
  v_max = 2.650e-3 (eq:A.8-ref).
  Dark-photon benchmark of Worked example 1.x / 8.1: m_chi = 10 MeV, m_V = 30 MeV, y_chi = 0.3, zeta = 1e-4, e = sqrt(4 pi alpha).
"""
import numpy as np

alpha = 1 / 137.035999
m = 510998.95
hbarc_eVcm = 197.3269804e-7
n_cm3 = 2.00e23
n = n_cm3 * hbarc_eVcm**3            # eV^3
kF = (3 * np.pi**2 * n) ** (1 / 3)   # unpolarized, two spins
kF_up_full = (6 * np.pi**2 * n) ** (1 / 3)
q0 = alpha * m
w = 5.0


def S_spin(q, w, kF):
    a = abs(m * w / q - q / 2)
    b = np.sqrt(max(kF**2 - 2 * m * w, 0.0))
    kmin = max(a, b)
    return (m / (4 * np.pi * q)) * (kF**2 - kmin**2) if kmin < kF else 0.0


print(f"k_F (unpolarized) = {kF/1e3:.3f} keV, v_F = {kF/m:.3e}")
vF_up = kF_up_full / m
EF_up = kF_up_full**2 / (2 * m)
print(f"fully polarized: k_F,up = {kF_up_full/1e3:.3f} keV, v_F,up = {vF_up:.3e}, E_F,up = {EF_up:.2f} eV")
print(f"q0 = {q0/1e3:.3f} keV; linear-region edge q v_F,up - q^2/2m = {q0*vF_up - q0**2/(2*m):.2f} eV (w = {w} eV)")
S_up = S_spin(q0, w, kF_up_full)
S_lin = m**2 * w / (2 * np.pi * q0)
assert np.isclose(S_up, S_lin, rtol=1e-12)
print(f"S_up(q0, 5 eV) = m^2 w/(2 pi q) = {S_up:.3e} eV^2")
S_unpol = 2 * S_spin(q0, w, kF)
print(f"unpolarized gas, same density: S_nn = {S_unpol:.3e} eV^2 (ratio polarized/unpolarized = {S_up/S_unpol:.3f})")

# 2x2 matrix, fully polarized
M = np.array([[S_up, S_up / 2], [S_up / 2, S_up / 4]])
print("2x2 matrix / S_nn:", M / S_up, " det =", np.linalg.det(M / S_up))

# dark-matter side, elastic, WE 8.2 kinematics
mchi = 100e6
v = 2.0e-3
vmin = w / q0 + q0 / (2 * mchi)
vT = np.sqrt(v**2 - vmin**2)
print(f"v_min = {vmin:.3e}, v_T = {vT:.3e}, v_T^2 = {vT**2:.3e}")
vmax = 2.650e-3
vTmax = np.sqrt(vmax**2 - vmin**2)
print(f"at v = v_max: v_T = {vTmax:.3e}")
# cross term relative to O_1 at c7 = c1, v_T along z: c1 c7 v_T S / (c1^2 S) = v_T
print(f"cross/O1 (c7 = c1, v_T || z) = {vT:.2e}")
# electron velocities: upper bound on |v_perp|^2 for the O_7 diagonal (second order)
vperp_max = vmax + vF_up
print(f"(v_max + v_F,up)^2 = {vperp_max**2:.2e}; /4 = {vperp_max**2/4:.2e}")

# partial polarization: S_ns = (S_up - S_dn)/2 vanishes while both spheres are in the linear region
for P, ww in [(0.5, 5.0), (0.5, 10.0)]:
    kup = kF * (1 + P) ** (1 / 3)
    kdn = kF * (1 - P) ** (1 / 3)
    su, sd = S_spin(q0, ww, kup), S_spin(q0, ww, kdn)
    edge_dn = q0 * kdn / m - q0**2 / (2 * m)
    print(f"P = {P}, w = {ww} eV: k_up = {kup/1e3:.3f}, k_dn = {kdn/1e3:.3f} keV, down linear edge = {edge_dn:.2f} eV, "
          f"S_ns/S_nn = {(su - sd)/2/(su + sd):.3f}")

# Born estimate for the heavy dark-photon benchmark: |f| = mu |V~(0)| / 2 pi against the range 1/m_V
mchi_b, mV, ychi, zeta = 10e6, 30e6, 0.3, 1e-4
e = np.sqrt(4 * np.pi * alpha)
Vt = ychi * zeta * e / mV**2
mu = mchi_b * m / (mchi_b + m)
f = mu * Vt / (2 * np.pi)
print(f"benchmark: V~ = {Vt:.2e} eV^-2, mu = {mu/1e3:.1f} keV, |f| = {f:.2e} eV^-1 = {f*hbarc_eVcm:.2e} cm, "
      f"|f| m_V = {f*mV:.1e}")
sig = mu**2 * Vt**2 / np.pi
print(f"sigma_e = {sig*hbarc_eVcm**2:.2e} cm^2")

# bound on the O_7 rate alone (second order in c7), at c7 = c1, against the cross term c1 c7 v_T S_up:
#   |<f|S_e . v_perp|i>|^2 summed over the final spin = |v_perp|^2 / 4,
#   |v_perp| <= |vbar_chi| + |(k + k')/2m| <= v_max + v_F,up + q/2m;
#   spin-conserving channel: S_up; spin-flip channel into the empty minority band (no Pauli blocking, energies shifted
#   by the exchange splitting): per-spin S <= m k_F,up^2 / (4 pi q).
vperp_b = vmax + vF_up + q0 / (2 * m)
Sflip_max = m * kF_up_full**2 / (4 * np.pi * q0)
O7_bound = vperp_b**2 / 4 * (S_up + Sflip_max)
cross = vT * S_up
print(f"|v_perp| <= {vperp_b:.3e}; |v_perp|^2/4 = {vperp_b**2/4:.2e}; S_flip <= {Sflip_max:.3e} eV^2 = {Sflip_max/S_up:.2f} S_up")
print(f"O_7 alone <= {O7_bound:.3e} c7^2 eV^2; cross = {cross:.3e} c1 c7 eV^2; ratio >= {cross/O7_bound:.1f} (c1/c7)")
vE = 250.5 / 299792.458
print(f"|v_E| = {vE:.3e}")

# absorption: occupation of a volume (1/m v)^3 and coherence time (Sect. 8.2, absorption subsection; App. D.25)
rho = 0.3e9 * hbarc_eVcm**3            # 0.3 GeV/cm^3 in eV^4 (eq:A.8 halo)
print(f"occupation N = rho/(m^4 v^3) = 1 at m_phi = {(rho/1e-3**3)**0.25:.1f} eV (v = 1e-3)")
v0 = 238 / 299792.458
print(f"t_coh ~ 1/(m v0^2) at 1 eV = {1/(v0**2)*6.582119569e-16:.2e} s")
