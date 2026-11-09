"""Sect. 22.3 (channels outside the framework): every number printed in Sect. 22.3 that is not quoted from another section.
Log: scope22_3.log.   Run: python scope22_3.py > scope22_3.log   (< 1 s).

Part A. Charged-current absorption chi + (A,Z) -> (A,Z+1) + e-, worked example 22.3 (we:22-cc).
  Fermi function: the point-charge function evaluated at the nuclear radius,
      F_0(Z, W) = 4 (2 p R)^(2(gamma-1)) exp(pi y) |Gamma(gamma + i y)|^2 / Gamma(1 + 2 gamma)^2,
      gamma = sqrt(1 - (Z alpha)^2),  y = Z alpha W / p,
  with W the total electron energy and p its momentum in units of m_e (c = 1), R in units of 1/m_e,
  Hayen et al., Rev. Mod. Phys. 90, 015008 (2018), arXiv:1709.07530, Eq. (6).  Z is the DAUGHTER charge.
  Nuclear radius R = 1.2 fm A^(1/3), the convention of Dror, Elor, McGehee, arXiv:1908.10861, below Eq. (4.10).
  Their printed Eq. (4.10) has 2(1+gamma) |Gamma(gamma+iy)|^2 / Gamma(1+gamma)^2; the prefactor 2(1+gamma) instead of 4 is
  a known convention (Hayen et al., text after Eq. (9): "the factor 4 ... replaced by (1+gamma)/2" -> 4(1+gamma)/2);
  the Gamma(1+gamma)^2 in place of Gamma(1+2 gamma)^2 makes the gamma-function factor alone larger by
  Gamma(1+2gamma)^2/Gamma(1+gamma)^2, printed below (a statement about that factor only: the prefactors differ too).
  The book's formula is eq:21.7-fermi (Sect. 21.7); Sect. 22.3 evaluates it and does not redisplay it.
  Phase space of the two-body absorption with a heavy recoil: proportional to p_e E_e (E_e = m_e + E_ej total energy).
  Size of the finite-size Coulomb correction L_0: of order alpha Z W R (W = E_e/m_e, R in units of 1/m_e), Hayen et al.
  Sect. II (L_0 differs from 1 by "a few 0.1 % up to several %"); the allowed-operator correction is (p R)^2.
  Target: 125Te (Z = 52, A = 125, N = 73, natural abundance not used), Gamow-Teller threshold 374 keV quoted from
  arXiv:1908.10861 Table 1.  Kinematics: E_ej = m_chi - m_th (nuclear recoil neglected, O(m_chi^2/2M)).
  Check: Z -> 0 limit against the nonrelativistic 2 pi y / (1 - exp(-2 pi y)).
Part B. Isospin sum rules for 125Te: Fermi strength N - Z in the isobaric analog state; Ikeda sum 3(N - Z);
  naive neutron count A - Z.  Uniform-sphere estimate of the Coulomb displacement energy of the analog state,
  Delta E_C = (6/5) Z alpha hbar c / R with R = 1.2 fm A^(1/3) (energy of the (Z+1)th proton in a uniformly charged sphere
  of Z protons); threshold to reach the analog state m_th(IAS) = Delta E_C - (m_n - m_p) + m_e (nuclear masses).
  m_n - m_p = 1.29333 MeV (CODATA), m_e = 0.51099895 MeV.  Labelled an estimate in the text.
  Exchange correction of the uniform sphere: the Slater exchange energy of Z protons of uniform density in a sphere of
  radius R, E_x = -(3/4)(3/pi)^(1/3) e^2 Int rho^(4/3) d^3r = -(3/4)(3/(2 pi))^(2/3) Z^(4/3) e^2/R, lowers the displacement
  energy by dE_x/dZ = -(3/4)(3/(2pi))^(2/3)(4/3) Z^(1/3) e^2/R; printed below as the lower end of "about 13 to 14 MeV".
Part C. Charge-density wave: kinematic numbers.
  (TaSe4)2I values quoted from Kim et al., arXiv:2210.14207: massive (Lee-Fukuyama) phason at 0.23 THz,
  single-particle gap 2 Delta_CDW = 250-300 meV, T_CDW ~ 260 K.  Here: 0.23 THz in meV; the smallest dark-matter mass that
  can deposit that energy, 2 omega / v_max^2; and the mass needed to transfer |q| = 1 keV, |q|/(2 v_max).
  v_max = 2.650e-3 (book, eq:1.2-vmax).
"""
import numpy as np
from scipy.special import loggamma, gamma as G

alpha = 1 / 137.035999084
me = 510.99895          # keV
hbarc = 197.3269804     # MeV fm
lam_e = hbarc / (me / 1000.0)   # hbar/(m_e c) in fm = 386.159 fm


def F0(Z, Ekin_keV, A):
    W = 1.0 + Ekin_keV / me
    p = np.sqrt(W * W - 1.0)
    g = np.sqrt(1.0 - (Z * alpha) ** 2)
    y = Z * alpha * W / p
    R = 1.2 * A ** (1 / 3) / lam_e
    lg = 2 * loggamma(g + 1j * y).real - 2 * loggamma(1 + 2 * g).real
    return 4 * (2 * p * R) ** (2 * (g - 1)) * np.exp(np.pi * y + lg)


def Fnr(Z, Ekin_keV):
    W = 1.0 + Ekin_keV / me
    p = np.sqrt(W * W - 1.0)
    y = Z * alpha * W / p
    return 2 * np.pi * y / (1 - np.exp(-2 * np.pi * y))


print("Part A. Charged-current absorption on 125Te")
Z, A = 53, 125
R_fm = 1.2 * A ** (1 / 3)
print(f"  nuclear radius 1.2 A^(1/3) = {R_fm:.3f} fm; hbar/m_e c = {lam_e:.3f} fm")
g = np.sqrt(1 - (Z * alpha) ** 2)
print(f"  daughter Z = {Z}: gamma = sqrt(1-(Z alpha)^2) = {g:.4f}, 2(gamma-1) = {2*(g-1):.4f}")
print(f"  misprint factor Gamma(1+2gamma)^2/Gamma(1+gamma)^2 at Z = 53: {G(1+2*g)**2/G(1+g)**2:.3f}; at Z = 1: "
      f"{G(1+2*np.sqrt(1-alpha**2))**2/G(1+np.sqrt(1-alpha**2))**2:.4f}")
# Z -> 0 check
for Ek in (10.0, 626.0):
    print(f"  check Z=1, E_ej = {Ek:.0f} keV: F_0 = {F0(1, Ek, 1):.5f}, nonrelativistic 2 pi y/(1-e^-2piy) = {Fnr(1, Ek):.5f}")
m_th = 374.0
mchi = 1000.0
Ek = mchi - m_th
W = 1 + Ek / me
p = np.sqrt(W * W - 1)
print(f"  m_chi = {mchi/1000:.3f} MeV, GT threshold {m_th:.0f} keV: E_ej = {Ek:.0f} keV, p_ej = {p*me:.1f} keV, "
      f"y = Z alpha W/p = {Z*alpha*W/p:.3f}, p_ej R = {p*R_fm/lam_e:.4f}")
for Zd in (53, 52, 1):
    print(f"    F_0(Z={Zd}, {Ek:.0f} keV) = {F0(Zd, Ek, A):.4f}")
print(f"    ratio F_0(52)/F_0(53) = {F0(52, Ek, A)/F0(53, Ek, A):.4f}  (parent charge instead of daughter)")
print(f"    ratio F_0(53)/F_0(52) = {F0(53, Ek, A)/F0(52, Ek, A):.4f}  (daughter above parent)")
print(f"  allowed-operator correction (p_ej R)^2 = {(p*R_fm/lam_e)**2:.1e}; finite-size Coulomb scale alpha Z W R = "
      f"{Z*alpha*W*R_fm/lam_e:.4f}")
print("  near threshold (rate per unit of the operator strength proportional to p_ej F_0; free final state: p_ej):")
ref = p * F0(53, Ek, A)
for Ek2 in (1.0, 10.0, 100.0, 626.0):
    W2 = 1 + Ek2 / me
    p2 = np.sqrt(W2 * W2 - 1)
    print(f"    E_ej = {Ek2:6.1f} keV: p_ej = {p2*me:7.2f} keV, F_0 = {F0(53, Ek2, A):8.3f}, "
          f"p_ej F_0 / (p_ej F_0 at 626 keV) = {p2*F0(53, Ek2, A)/ref:.4f}, p_ej/p_ej(626) = {p2/p:.4f}")
print("  with the full phase space p_e E_e (E_e = m_e + E_ej):")
refE = p * W * F0(53, Ek, A)
for Ek2 in (1.0, 10.0, 626.0):
    W2 = 1 + Ek2 / me
    p2 = np.sqrt(W2 * W2 - 1)
    print(f"    E_ej = {Ek2:6.1f} keV: p E F_0 / (same at 626 keV) = {p2*W2*F0(53, Ek2, A)/refE:.4f}, "
          f"p E / (p E at 626 keV) = {p2*W2/(p*W):.4f}")
# Bohr radius of the daughter K shell, for the screening statement
a0 = 0.529177210903e5  # fm
p10 = np.sqrt((1 + 10.0/me)**2 - 1)
print(f"  K-shell radius a0/Z of iodine = {a0/Z:.0f} fm; 1/p_ej at 626 keV = {lam_e/p:.0f} fm; at 10 keV = {lam_e/p10:.0f} fm")

print()
print("Part B. Isospin sum rules, 125Te (Z = 52, N = 73)")
Zp, N = 52, 73
print(f"  Fermi strength N - Z = {N-Zp}; naive neutron count A - Z = {N}; ratio = {N/(N-Zp):.2f}")
print(f"  Ikeda sum S(n->p) - S(p->n) = 3(N - Z) = {3*(N-Zp)} (free neutron: 3)")
dEC = 1.2 * Zp * alpha * hbarc / R_fm
mnmp = 1.29333236
print(f"  uniform-sphere Coulomb displacement (6/5) Z alpha hbar c/R = {dEC:.2f} MeV")
print(f"  analog-state threshold dE_C - (m_n - m_p) + m_e = {dEC - mnmp + me/1000:.2f} MeV (estimate)")
cx = 0.75 * (3 / (2 * np.pi)) ** (2 / 3)
dEx = cx * (4 / 3) * Zp ** (1 / 3) * alpha * hbarc / R_fm
print(f"  exchange term of the uniform sphere: coefficient {cx:.4f}, d(E_x)/dZ = -{dEx:.2f} MeV;"
      f" threshold with it = {dEC - dEx - mnmp + me/1000:.2f} MeV")
print("  g_A quenching q ~ 0.75 (Gysbers et al., arXiv:1903.00047, text): lambda_A^2 weight changes by 1/q^2 = "
      f"{1/0.75**2:.2f}")
print(f"  Gamow-Teller: one conversion per neutron, 3(A - Z) = {3*N}, against the Ikeda difference 3(N - Z) = {3*(N-Zp)}")

print()
print("Part C. Charge-density wave kinematics")
h_eVs = 4.135667696e-15
w_phi = 0.23e12 * h_eVs * 1e3
print(f"  0.23 THz = {w_phi:.3f} meV;  0.25 THz = {0.25e12*h_eVs*1e3:.3f} meV")
vmax = 2.650e-3
print(f"  smallest m_chi to deposit {w_phi:.3f} meV: 2 omega/v_max^2 = {2*w_phi*1e-3/vmax**2:.0f} eV")
print(f"  m_chi to transfer |q| = 1 keV: |q|/(2 v_max) = {1.0/(2*vmax):.1f} keV per keV of |q|")
print(f"  gap 2Delta = 250-300 meV vs phason: ratio {250/w_phi:.0f}-{300/w_phi:.0f}")
