"""Local empirical pseudopotential bands of Si, Ge and GaAs (shared by fig3_6.py and fig3_7.py, Sect. 3.3).

Model (the modelling choice behind Figs. 3.6 and 3.7): the local empirical pseudopotential method of
M. L. Cohen and T. K. Bergstresser, Phys. Rev. 141, 789 (1966), doi:10.1103/PhysRev.141.789. The one-electron
Hamiltonian of Sect. 3.2, Eq. (3.2-central), is diagonalized in plane waves with the potential
    U(G) = V_S(|G|^2) cos(G.tau) + i V_A(|G|^2) sin(G.tau),   tau = (a/8)(1,1,1),
with the origin at the bond centre, so that the two atoms sit at -tau and +tau. Only the shells |G|^2 = 3, 4, 8, 11
(2pi/a)^2 are nonzero. Form factors in Rydberg (Cohen and Bergstresser, table of pseudopotential form factors;
the full text was not available to us, the values are the widely reproduced ones of that paper):
    Si:   V_S(3) = -0.21, V_S(8) = 0.04, V_S(11) = 0.08                       (a = 5.43 A in the original fit)
    Ge:   V_S(3) = -0.23, V_S(8) = 0.01, V_S(11) = 0.06                       (a = 5.66 A)
    GaAs: V_S as Ge;  V_A(3) = 0.07, V_A(4) = 0.05, V_A(11) = 0.01            (a = 5.64 A)
We use the lattice constants of the original fit (the form factors were fitted at them). The model has no
spin-orbit coupling and no nonlocal (angular-momentum-dependent) terms; Chelikowsky and Cohen, Phys. Rev. B 14, 556
(1976) add both. Kinetic energy |k+G|^2 in Ry with k in bohr^-1 (hbar^2/2m_e = 1 Ry bohr^2).
Plane-wave cutoff: |k+G|^2 <= ECUT (in units of (2pi/a)^2); ECUT = 21 is converged to < 1 meV for the band edges
(checked in fig3_6.py).
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")   # batched small eigenproblems run fastest single-threaded
import numpy as np

RY = 13.605693122994        # eV (CODATA 2022)
BOHR = 0.529177210544       # Angstrom (CODATA 2022)
HBARC = 1973.269804         # eV Angstrom (CODATA 2022)

MATERIALS = {
    "Si":   dict(a=5.43, VS={3: -0.21, 8: 0.04, 11: 0.08}, VA={}),
    "Ge":   dict(a=5.66, VS={3: -0.23, 8: 0.01, 11: 0.06}, VA={}),
    "GaAs": dict(a=5.64, VS={3: -0.23, 8: 0.01, 11: 0.06}, VA={3: 0.07, 4: 0.05, 11: 0.01}),
}

# fcc reciprocal primitive vectors in units of 2pi/a (Sect. 3.1)
B = np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], float)


class EPM:
    def __init__(self, name, ecut=21.0, kmax=1.2):
        m = MATERIALS[name]
        self.name, self.a = name, m["a"]
        n = 6
        idx = np.array([(i, j, k) for i in range(-n, n + 1) for j in range(-n, n + 1) for k in range(-n, n + 1)])
        G = idx @ B                                      # units 2pi/a
        # keep a basis that is fixed for all k in the zone (|G| <= sqrt(ecut) + kmax), then cut per k by energy
        G = G[np.linalg.norm(G, axis=1) <= np.sqrt(ecut)]
        self.G = G
        self.ecut = ecut
        dG = G[:, None, :] - G[None, :, :]
        d2 = np.rint((dG ** 2).sum(-1)).astype(int)
        phase = 2 * np.pi * (dG @ np.array([1, 1, 1]) / 8.0)   # G.tau with tau = (a/8)(1,1,1)
        U = np.zeros(d2.shape, complex)
        for s, v in m["VS"].items():
            U += np.where(d2 == s, v * np.cos(phase), 0)
        for s, v in m["VA"].items():
            U += np.where(d2 == s, 1j * v * np.sin(phase), 0)
        self.U = U                                       # Ry; Hermitian since U(-G) = U(G)^*
        self.k2unit = (2 * np.pi / (self.a / BOHR)) ** 2  # (2pi/a)^2 in bohr^-2 -> Ry

    def hamiltonian(self, k):
        """k: (..., 3) in units of 2pi/a. Returns H (..., NG, NG) in Ry."""
        k = np.asarray(k, float)
        kin = ((k[..., None, :] + self.G) ** 2).sum(-1) * self.k2unit
        H = np.broadcast_to(self.U, k.shape[:-1] + self.U.shape).copy()
        i = np.arange(len(self.G))
        H[..., i, i] += kin
        return H

    def bands(self, k, nb=8, vectors=False, chunk=256):
        """Eigenvalues in eV (lowest nb) for k in units of 2pi/a; optionally eigenvectors."""
        k = np.asarray(k, float)
        if k.ndim == 2 and len(k) > chunk and not vectors:
            return np.concatenate([self.bands(k[i:i + chunk], nb) for i in range(0, len(k), chunk)])
        H = self.hamiltonian(k)
        if vectors:
            w, v = np.linalg.eigh(H)
            return w[..., :nb] * RY, v[..., :, :nb]
        w = np.linalg.eigvalsh(H)
        return w[..., :nb] * RY

    def velocity(self, k, nb=8):
        """Band energies (eV, all bands) and velocity matrix elements v_mn = <m|(p+k)/m_e|n> (units of c) at one k."""
        w, v = self.bands(k, nb=len(self.G), vectors=True)
        kG = (np.asarray(k, float) + self.G) * (2 * np.pi * HBARC / self.a)    # eV
        me = 510998.95
        vel = np.einsum("gm,gi,gn->imn", v.conj(), kG, v) / me                   # (3, NB, NB)
        return w, vel


def path(points, labels, n=60):
    """Piecewise-linear path through points (units 2pi/a); returns k, cumulative distance, tick positions."""
    ks, xs, ticks = [], [], [0.0]
    x0 = 0.0
    for p, q in zip(points[:-1], points[1:]):
        p, q = np.array(p, float), np.array(q, float)
        t = np.linspace(0, 1, n)[:, None]
        seg = p + t * (q - p)
        L = np.linalg.norm(q - p)
        ks.append(seg)
        xs.append(x0 + t[:, 0] * L)
        x0 += L
        ticks.append(x0)
    return np.vstack(ks), np.concatenate(xs), ticks
