"""Shared linear spin-wave model of the Sect. 14.1 scripts (two-sublattice Heisenberg antiferromagnet).
Natural units hbar = c = 1 where rates are computed; magnon energies in meV, lengths in Angstrom.

Model (named in the captions and the text):
  Heisenberg model H = sum_<ij> J_ij S_i.S_j, each pair once, J > 0 antiferromagnetic (eq:7.1-heis), undistorted
  fcc lattice of Ni2+ with type-II order (ferromagnetic (111) planes alternating in sign); J1 (nearest) and J2
  (next-nearest) only; no anisotropy unless K_ANI is given; no rhombohedral distortion.
  Linear spin-wave theory of App. D.19 (eq:D.19-Hk, eq:D.19-omega):
     A_k = J_AB(0) - J_AA(0) + J_AA(k) [+ K for a single-ion easy-axis term], B_k = J_AB(k),
     omega_k = |S| sqrt(A_k^2 - B_k^2),  v_k^2 = (A_k / sqrt(A_k^2 - B_k^2) - 1)/2.
  One-magnon weight of App. D.38 (eq:D.38-weight): w_q = |S| (A_q - B_q) / omega_q with B_q = J_AB(q) evaluated at
  the full momentum transfer q (not reduced to the zone), which carries the sublattice phase exp(i G.delta).
Inputs (sources):
  J2 = 19.01 meV, J1 = -1.37 meV (book convention): Hutchings and Samuelsen, PRB 6, 3447 (1972), abstract
     (sources/7.1/hutchings1972_abstract.txt), as eq:7.1-NiO.
  a = 4.17 A: Fischer et al., PRB 80, 014408 (2009), Table I (as Sect. 7.1). |S| = 1 for Ni2+ (Sect. 7.1).
  Ni2+ <j0> analytic fit A exp(-a s^2) + B exp(-b s^2) + C exp(-c s^2) + D, s = q/(4 pi) in A^-1:
     (0.0163, 35.8826, 0.3916, 13.2233, 0.6052, 4.3388, -0.0133): P. J. Brown, International Tables for
     Crystallography Vol. C, Sect. 4.4.5, Table 4.4.5.2 (the values distributed with the `periodictable` package,
     magnetic_ff[Ni][2].j0, checked at run time when that package is installed).
  Simple-cubic check lattice: 6 antiparallel nearest neighbours, no parallel bonds.
"""
import numpy as np

HBARC_MEV_A = 1973.269804e3       # meV A
J1, J2, S_NIO, A_NIO = -1.37, 19.01, 1.0, 4.17
NI2_J0 = (0.0163, 35.8826, 0.3916, 13.2233, 0.6052, 4.3388, -0.0133)

# neighbours of a site of sublattice A: a site (a/2) n is on A if (n1 + n2 + n3)/2 is even
_nn = []
for v in [(1, 1, 0), (1, 0, 1), (0, 1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1)]:
    _nn += [np.array(v), -np.array(v)]
_nn = np.array(_nn, float)
PAR = _nn[np.isclose(_nn.sum(1), 0)] * A_NIO / 2           # 6 nearest neighbours in the same (111) plane
ANTI = _nn[~np.isclose(_nn.sum(1), 0)] * A_NIO / 2         # 6 nearest neighbours in adjacent planes
NNN = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)], float) * A_NIO
Q_AF = np.array([0.5, 0.5, 0.5]) * 2 * np.pi / A_NIO      # ordering wavevector (pi/a)(1,1,1)


def ab_nio(k, j1=J1, j2=J2, kani=0.0):
    """A_k, B_k (meV) of type-II NiO for wavevectors k (A^-1), shape (n, 3); B at the full k."""
    k = np.atleast_2d(k)
    jaa = j1 * np.cos(k @ PAR.T).sum(1)
    jab = j1 * np.cos(k @ ANTI.T).sum(1) + j2 * np.cos(k @ NNN.T).sum(1)
    a_k = (6 * j1 + 6 * j2) - 6 * j1 + jaa + kani
    return a_k, jab


def ab_sc(k, j=1.0, a=1.0):
    """A_k, B_k of the simple-cubic antiferromagnet with nearest-neighbour exchange j (units of j)."""
    k = np.atleast_2d(k)
    b = 2 * j * np.cos(k * a).sum(1)
    return np.full(len(k), 6 * j), b


def omega(a_k, b_k, s=S_NIO):
    return s * np.sqrt(np.maximum(a_k**2 - b_k**2, 0.0))


def v2(a_k, b_k):
    """(v^M_k)^2 = (A/sqrt(A^2 - B^2) - 1)/2."""
    r = np.sqrt(np.maximum(a_k**2 - b_k**2, 1e-300))
    return 0.5 * (a_k / r - 1.0)


def weight(a_k, b_k):
    """one-magnon weight w = (A - B)/sqrt(A^2 - B^2) = |S|(A - B)/omega, B at the full momentum transfer."""
    r = np.sqrt(np.maximum(a_k**2 - b_k**2, 1e-300))
    return (a_k - b_k) / r


def zone_grid(n, period):
    """offset midpoint grid of n^3 points in the cube [-period/2, period/2)^3 (avoids the Goldstone points)."""
    x = (np.arange(n) + 0.5) / n - 0.5
    g = np.stack(np.meshgrid(x, x, x, indexing="ij"), -1).reshape(-1, 3)
    return g * period


def fmag_ni2(q_inv_a):
    """<j0(q)> of Ni2+ (Brown's fit), q in A^-1; set to zero beyond its first zero (fit range)."""
    s2 = (np.asarray(q_inv_a) / (4 * np.pi))**2
    A, a, B, b, C, c, D = NI2_J0
    f = A * np.exp(-a * s2) + B * np.exp(-b * s2) + C * np.exp(-c * s2) + D
    return np.where(f > 0, f, 0.0)


def check_brown():
    try:
        import periodictable as pt
        ref = tuple(round(x, 4) for x in pt.Ni.magnetic_ff[2].j0)
        return ref == tuple(round(x, 4) for x in NI2_J0)
    except Exception:
        return None
