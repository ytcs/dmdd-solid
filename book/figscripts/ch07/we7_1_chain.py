"""Worked example 7.1 (Sect. 7.1): exact-diagonalization check of the ferromagnetic Heisenberg ring.
No figure; prints the numbers quoted in the worked example.
Model: H = J sum_j S_j.S_{j+1} on a ring of N sites (periodic), J = -1 (ferromagnetic; energies in units of |J|),
spin length |S| = 1/2 and 1. The Hamiltonian is built in the sectors S^z_tot = N|S| - 1 (one flip) and N|S| - 2 (two flips)
from the spin matrices, and diagonalized exactly.
Linear spin-wave theory (Sect. 7.1): omega_k = 2|J||S|(1 - cos k), k = 2 pi m/N.
"""
import itertools
import numpy as np


def spin_mats(s):
    m = np.arange(s, -s - 1, -1)
    sz = np.diag(m)
    sp = np.zeros((len(m), len(m)))
    for i in range(1, len(m)):
        sp[i - 1, i] = np.sqrt(s * (s + 1) - m[i] * (m[i] + 1))
    return m, sz, sp


def sector(N, s, nflip, J=-1.0):
    m, _, _ = spin_mats(s)
    dev = range(int(round(2 * s)) + 1)        # deviation d = s - m on each site
    states = [c for c in itertools.product(dev, repeat=N) if sum(c) == nflip]
    index = {c: i for i, c in enumerate(states)}
    H = np.zeros((len(states), len(states)))
    for c, i in index.items():
        for j in range(N):
            l = (j + 1) % N
            mj, ml = s - c[j], s - c[l]
            H[i, i] += J * mj * ml
            # S+_j S-_l /2 and S-_j S+_l /2
            for dj, dl in ((-1, +1), (+1, -1)):
                nj, nl = c[j] + dj, c[l] + dl
                if 0 <= nj <= 2 * s and 0 <= nl <= 2 * s:
                    # raising (d -> d-1) amplitude sqrt(s(s+1) - m(m+1)) with m the old projection
                    def amp(d_old, d_new, s=s):
                        m_old = s - d_old
                        m_new = s - d_new
                        return np.sqrt(s * (s + 1) - m_old * m_new)
                    cc = list(c); cc[j], cc[l] = nj, nl
                    H[index[tuple(cc)], i] += 0.5 * J * amp(c[j], nj) * amp(c[l], nl)
    return np.linalg.eigvalsh(H)


for s in (0.5, 1.0):
    N = 10 if s == 0.5 else 8
    E_F = -1.0 * N * s * s
    e1 = np.sort(sector(N, s, 1) - E_F)
    k = 2 * np.pi * np.arange(N) / N
    lswt = np.sort(2 * s * (1 - np.cos(k)))
    print(f"|S| = {s}, N = {N}: one-magnon max |ED - LSWT| = {np.abs(e1 - lswt).max():.2e} |J|; "
          f"zone-boundary energy 4|J||S| = {4*s:.2f} |J|")
    e2 = np.sort(sector(N, s, 2) - E_F)
    pairs = np.sort([lswt[a] + lswt[b] for a in range(N) for b in range(a, N)])
    print(f"   two flips: {len(e2)} exact levels, lowest nonzero {e2[e2 > 1e-9][:4]}; "
          f"LSWT pair sums lowest nonzero {pairs[pairs > 1e-9][:4]}")
