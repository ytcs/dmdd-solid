"""Shared inputs for Sect. 16.6 (color centers and broken bonds): masses, halo, displacement and bond kinematics,
Lindhard damage energy, and the momentum distribution of a diatomic bond.  Used by fig16_6.py, limit16_6a.py and
we16_6.py; run directly to print the constants.

Sources of every input (natural units, eV):
  Halo: the book's halo (Sects. 1.2-1.3), eta(v_min) from figscripts/ch11/phon11.py (Baxter et al. 2021, Table 1:
        v0 = 238, v_esc = 544, v_E = 250.5 km/s), v_max = 794.5 km/s = 2.650e-3.
  Atomic masses (u): 19F 18.998403, 7Li 7.016004, 1H 1.007825 (standard values); m_u = 931.494 MeV.
  [C21] Cogswell, Goel, Huber, Phys. Rev. Applied 16, 064060 (2021), arXiv:2104.13926, Table I: LiF threshold damage
        energy (the displacement threshold of their TRIM runs) E_d = 27 eV; nuclear-recoil energy at half the asymptotic
        vacancy efficiency E_1/2 = 80 eV.  Text p. 2: Kinchin-Pease count n_v = 0 (T_d < E_d), 1 (E_d <= T_d < 2E_d),
        T_d/(2E_d) for T_d >> E_d, with T_d the damage energy.
  [G20] Griffin et al., Phys. Rev. D 101, 055004 (2020), arXiv:1910.10716, Table I (computed): LiF optical phonon energies
        33.5 to 77.2 meV (the values of Sect. 11.2).  Used to bracket the mean phonon energy <omega>_F of the fluorine site,
        which sets the Doppler width of the impulse response, sigma^2 = E_R <omega> at T = 0 (eq. 11.4-IAgauss).
  [A18] Agnese et al. (CDMS II), NIM A 905, 71 (2018), arXiv:1803.02903, Eq. (3): Lindhard yield y_L = k g/(1 + k g),
        k = 0.133 Z^(2/3) A^(-1/2), eps = 11.5 E_R[keV] Z^(-7/3), g = 3 eps^0.15 + 0.7 eps^0.6 + eps.  Applied to a fluorine
        recoil with Z = 9, A = 19 (single-element form; model choice for the compound LiF).  Damage energy T_d = E_R(1 - y_L).
  [GP25] Guerrero Perez et al., J. Appl. Phys. 137, 244401 (2025), arXiv:2412.21060, p. 2: LiF band gap 14.2 eV
        (their ref. [2], Piacentini et al. 1976), F-band absorption about 5.1 eV (experiment, as they quote it).
  [B18] Budnik, Cheshnovsky, Slone, Volansky, Phys. Lett. B 782, 242 (2018), arXiv:1705.03016, Eq. (2) and Table I:
        q_min(Omega) = sqrt(2 m1 dE_B) (1 + a sin(4 theta) cos(4 phi)), a = 0.4.
  [E17] Essig, Mardon, Slone, Volansky, Phys. Rev. D 95, 056011 (2017), arXiv:1608.02940 (arXiv numbering): Eq. (3.3)
        q_min = (m1/mu12)(2 mu12 dE_B)^(1/2); Eq. (3.12) Gaussian radial ground state; Eq. (3.17) improved Born
        kinematics q~' = (2 mu12 (E_int + dE_B))^(1/2); Eqs. (4.3), (4.5) classical and quantum rates; H2 dE_B = 4.75 eV.
  [HH79] Huber and Herzberg, Constants of Diatomic Molecules (1979), as compiled in the NIST Chemistry WebBook:
        H2 X state omega_e = 4401.21 cm^-1, r_e = 0.74144 A; N2 omega_e = 2358.57 cm^-1, r_e = 1.09768 A.
"""
import os
import sys
import numpy as np
from scipy.special import erfc

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ch11"))
import phon11 as P  # noqa: E402

KMS = P.KMS
VMAX = P.VMAX                    # 2.650e-3
eta = P.eta                      # eta(v) in natural units
M_U = 931.494e6                  # eV
CM1 = 1.239841984e-4             # 1 cm^-1 in eV
HBARC_EV_A = 1973.269804         # eV Angstrom

M_F = 18.998403 * M_U
M_LI = 7.016004 * M_U
M_H = 1.007825 * M_U

E_D_LIF = 27.0                   # eV [C21]
E_HALF_LIF = 80.0                # eV [C21]
W_LIF = (33.5e-3, 77.2e-3)       # eV [G20]
GAP_LIF = 14.2                   # eV [GP25]
FBAND_LIF = 5.1                  # eV [GP25]

E_B_H2 = 4.75                    # eV [E17]
W_H2 = 4401.21 * CM1             # eV [HH79]
R_H2 = 0.74144 / HBARC_EV_A      # eV^-1 [HH79]
W_N2 = 2358.57 * CM1
R_N2 = 1.09768 / HBARC_EV_A


def mu(a, b):
    return a * b / (a + b)


def er_max(m, M, v=VMAX):
    """Largest recoil energy, eq. 1.3-ERmax."""
    return 2 * mu(m, M)**2 * v**2 / M


def m_threshold(E, M, v=VMAX):
    """Smallest dark-matter mass with er_max(m, M) = E: solve 2 mu^2 v^2 / M = E for m."""
    muv = np.sqrt(E * M / 2) / v      # required reduced mass
    return muv * M / (M - muv)


def lindhard(E, Z, A):
    """Lindhard yield y_L and damage energy T_d = E(1 - y_L), E in eV [A18]."""
    k = 0.133 * Z**(2 / 3) / np.sqrt(A)
    eps = 11.5 * (np.asarray(E) / 1e3) * Z**(-7 / 3)
    g = 3 * eps**0.15 + 0.7 * eps**0.6 + eps
    y = k * g / (1 + k * g)
    return y, np.asarray(E) * (1 - y), k, eps, g


def kinchin_pease(Td, Ed):
    """Kinchin-Pease count as quoted by [C21]: 0, 1, then Td/(2 Ed)."""
    Td = np.asarray(Td, float)
    return np.where(Td < Ed, 0.0, np.where(Td < 2 * Ed, 1.0, Td / (2 * Ed)))


# ---- diatomic bond: Gaussian radial ground state [E17 Eq. (3.12)], sigma0^2 = 1/(mu12 omega_vib) (harmonic) ----------
def bond_kgrid(mu12, wv, r0, nk=4000, kmax_sig=9.0):
    """Radial grid of the relative momentum k and the density |Psi(k)|^2 k^2 dk/(2 pi^2) (normalized to one).
    Psi(k) = sqrt(4 pi)(sigma0 sqrt(pi))^(-1/2) sqrt(2 pi) sigma0 sin(k r0) exp(-k^2 sigma0^2/2)/k (r0 >> sigma0)."""
    s0 = 1 / np.sqrt(mu12 * wv)
    k = np.linspace(1e-6 / s0, kmax_sig / s0, nk)
    dens = 8 * np.pi**1.5 * s0 * np.sin(k * r0)**2 * np.exp(-(k * s0)**2) / k**2 * k**2 / (2 * np.pi**2)
    dk = k[1] - k[0]
    w = dens * dk
    return k, w / w.sum(), w.sum(), s0


def p_diss(q, M1, mu12, Eb, kgrid, kw, mode="IA", nu=200):
    """Probability that a kick q on atom 1 dissociates the bond, averaged over the isotropic ground state.
    p = (mu12/M1) q is the kick on the relative coordinate.
      IA:   dissociation if p.k/mu12 + p^2/2mu12 > Eb  (internal energy change counts the initial kinetic energy)
      Born: dissociation if |k + p|^2/2mu12 > Eb       (improved Born kinematics of [E17] Eq. (3.17))
      cl:   p^2/2mu12 > Eb                             (classical, [E17] Eq. (3.3))"""
    p = mu12 / M1 * q
    if mode == "cl":
        return float(p**2 / (2 * mu12) > Eb)
    u, wu = np.polynomial.legendre.leggauss(nu)
    wu = wu / 2
    K, U = np.meshgrid(kgrid, u, indexing="ij")
    if mode == "IA":
        ok = p * K * U / mu12 + p**2 / (2 * mu12) > Eb
    else:
        ok = (K**2 + 2 * p * K * U + p**2) / (2 * mu12) > Eb
    return float(np.einsum("i,j,ij->", kw, wu, ok.astype(float)))


if __name__ == "__main__":
    print("v_max = %.4e (%.1f km/s), eta(0) = %.2f" % (VMAX, VMAX / KMS, float(eta(0.0))))
    for name, M in (("19F", M_F), ("7Li", M_LI), ("1H", M_H)):
        print("%s: M = %.4f GeV" % (name, M / 1e9))
    print("LiF: E_d = %.0f eV, E_1/2 = %.0f eV [C21]; optical phonons %.1f-%.1f meV [G20]; gap %.1f eV, F band %.1f eV [GP25]"
          % (E_D_LIF, E_HALF_LIF, W_LIF[0] * 1e3, W_LIF[1] * 1e3, GAP_LIF, FBAND_LIF))
    print("H2: E_bond = %.2f eV [E17]; omega_vib = %.4f eV, r_e = %.5f A [HH79]" % (E_B_H2, W_H2, R_H2 * HBARC_EV_A))
    print("N2: omega_vib = %.4f eV, r_e = %.5f A [HH79]" % (W_N2, R_N2 * HBARC_EV_A))
    print("alpha m_e = %.3f keV" % (P.Q0 / 1e3))
