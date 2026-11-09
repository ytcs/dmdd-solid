"""Worked example 5.3 (Sect. 5.2): silicon sound speeds from the elastic constants, and the Debye temperature they imply.
Elastic constants (room temperature): C11 = 165.6, C12 = 63.9, C44 = 79.5 GPa, rho_T = 2.33 g/cm^3
  [Martinez et al., Phys. Rev. Applied 11, 064025 (2019), Table I; the values of App. C.18].
Lattice constant a = 5.431 Angstrom (CODATA 2022, Sect. 3.1); 8 atoms per cubic cell a^3, n_at/Omega = 8/a^3.
Sound speeds: eigenvalues rho_T c^2 of the Christoffel matrix M_ik = C_ijkl Q_j Q_l (eq:C.18-christoffel).
Debye average (Sect. 5.2): 3/cbar^3 = sum_nu <c_nu^-3>, angular mean over the unit sphere (Lebedev-free: a fine
Gauss-Legendre x uniform-phi product grid). omega_D = cbar (6 pi^2 n_at/Omega)^(1/3), Theta_D = hbar omega_D / k_B.
Run: python we5_3.py   (numpy only). Prints every number quoted in WE 5.3.
"""
import numpy as np

GPA = 1e9
C11, C12, C44 = 165.6 * GPA, 63.9 * GPA, 79.5 * GPA
RHO = 2.33e3                      # kg/m^3
A = 5.431e-10                     # m
HBAR = 1.054571817e-34            # J s (CODATA)
KB = 1.380649e-23                 # J/K (exact)
EV = 1.602176634e-19              # J (exact)


def ctensor():
    C = np.zeros((3, 3, 3, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if i == j == k == l:
                        C[i, j, k, l] = C11
                    elif i == j and k == l:
                        C[i, j, k, l] = C12
                    elif (i == k and j == l) or (i == l and j == k):
                        C[i, j, k, l] = C44
    return C


C = ctensor()


def speeds(qhat):
    M = np.einsum('ijkl,j,l->ik', C, qhat, qhat)
    return np.sqrt(np.sort(np.linalg.eigvalsh(M))[::-1] / RHO)   # LA, TA1, TA2 (descending)


for name, d in [('[100]', [1, 0, 0]), ('[110]', [1, 1, 0]), ('[111]', [1, 1, 1])]:
    d = np.array(d, float) / np.linalg.norm(d)
    print(name, 'c (km/s) =', np.round(speeds(d) / 1e3, 2))

# angular average of c^-3, per branch and summed
x, w = np.polynomial.legendre.leggauss(200)
phis = np.linspace(0, 2 * np.pi, 400, endpoint=False)
inv3 = np.zeros(3)
for ct, wt in zip(x, w):
    st = np.sqrt(1 - ct ** 2)
    for p in phis:
        inv3 += wt * (2 * np.pi / len(phis)) * speeds(np.array([st * np.cos(p), st * np.sin(p), ct])) ** -3.0
inv3 /= 4 * np.pi
cbar = (3 / inv3.sum()) ** (1 / 3)
print('<c^-3>^(-1/3) per branch (km/s):', np.round(inv3 ** (-1 / 3) / 1e3, 3))
print('Debye average cbar = %.3f km/s' % (cbar / 1e3))
n = 8 / A ** 3
QD = (6 * np.pi ** 2 * n) ** (1 / 3)
wD = cbar * QD
print('n_at/Omega = %.4e cm^-3, Q_D = %.4f 1/Angstrom = %.4f (2pi/a)' % (n * 1e-6, QD * 1e-10, QD * A / (2 * np.pi)))
print('omega_D = %.2f meV = %.3f THz, Theta_D = %.1f K' % (HBAR * wD / EV * 1e3, wD / 2 / np.pi / 1e12, HBAR * wD / KB))
QDac = (6 * np.pi ** 2 * n / 2) ** (1 / 3)
print('acoustic-only convention (n = cells): Theta_D = %.1f K' % (HBAR * cbar * QDac / KB))
# isotropic convention of App. C.18 / E.12: c_LA^2 = C11/rho, c_TA^2 = C44/rho
cl, ct = np.sqrt(C11 / RHO), np.sqrt(C44 / RHO)
cbi = (3 / (cl ** -3 + 2 * ct ** -3)) ** (1 / 3)
print('isotropic convention: cLA %.2f, cTA %.2f km/s, cbar %.3f km/s, Theta_D %.1f K' % (cl / 1e3, ct / 1e3, cbi / 1e3, HBAR * cbi * QD / KB))
# Debye g at small omega in eV^-1 per cell: g = 3 Omega omega^2/(2 pi^2 cbar^3) with Omega = a^3/4
