"""Exact diagonalization check of the antiferromagnetic-resonance weight (Sect. 14.3, Limit Check 14.3a panel 2).

Model: easy-axis (XXZ) Heisenberg antiferromagnet on the 8-site cube (open boundaries, every site with z = 3 neighbors
on the other sublattice, 12 bonds), H = J sum_<ij> (S^x_i S^x_j + S^y_i S^y_j + Delta S^z_i S^z_j), J > 0, Delta >= 1.
Linear spin-wave theory at k = 0 gives A = zJ|S|Delta, B = zJ|S|, i.e. omega_E = zJ|S| and omega_A = zJ|S|(Delta - 1),
and the uniform transverse weight per antiparallel pair |S| omega_AFMR/(2 omega_E + omega_A) = |S| sqrt((Delta-1)/(Delta+1)).
Exact: the total weight of S^x_tot from the ground state, sum_f |<f|S^x_tot|0>|^2 = <0|(S^x_tot)^2|0> (since <S^x_tot> = 0),
per pair (4 pairs), for |S| = 1/2, 1, 3/2. Ground state found in the S^z_tot = 0 sector (Lanczos, eigsh).
Log: ed14_3.log; data cached in ed14_3.npz for limit14_3a.py.  Run: python ed14_3.py (about a minute).
"""
import os
import itertools
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "ed14_3.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


sites = list(itertools.product([0, 1], repeat=3))
N = len(sites)
bonds = [(i, j) for i in range(N) for j in range(i + 1, N) if sum(abs(a - b) for a, b in zip(sites[i], sites[j])) == 1]
assert len(bonds) == 12
z = 3


def build(S2):
    """S2 = 2|S|. Basis: m_i in {-S..S} encoded as integers 0..2S (value n -> m = n - S). Restrict to sum m = 0."""
    d = S2 + 1
    S = S2 / 2
    states = [st for st in itertools.product(range(d), repeat=N) if abs(sum(n - S for n in st)) < 1e-9]
    index = {st: k for k, st in enumerate(states)}
    return states, index, S


def splus(n, S):
    m = n - S
    return np.sqrt(S * (S + 1) - m * (m + 1))


def hamiltonian(states, index, S, Delta):
    rows, cols, vals = [], [], []
    for k, st in enumerate(states):
        diag = 0.0
        for (i, j) in bonds:
            mi, mj = st[i] - S, st[j] - S
            diag += Delta * mi * mj
            # S+_i S-_j + S-_i S+_j over 2
            if st[i] < 2 * S and st[j] > 0:
                new = list(st); new[i] += 1; new[j] -= 1
                amp = 0.5 * splus(st[i], S) * splus(st[j] - 1, S)
                rows.append(index[tuple(new)]); cols.append(k); vals.append(amp)
            if st[j] < 2 * S and st[i] > 0:
                new = list(st); new[j] += 1; new[i] -= 1
                amp = 0.5 * splus(st[j], S) * splus(st[i] - 1, S)
                rows.append(index[tuple(new)]); cols.append(k); vals.append(amp)
        rows.append(k); cols.append(k); vals.append(diag)
    n = len(states)
    return sp.csr_matrix((vals, (rows, cols)), shape=(n, n))


def weight(states, S, psi):
    """<(S^x_tot)^2> = (1/2) <S^- S^+> in an S^z_tot = 0 state with real amplitudes: compute |S^+ psi|^2 / 2."""
    acc = {}
    for k, st in enumerate(states):
        a = psi[k]
        if a == 0:
            continue
        for i in range(N):
            if st[i] < 2 * S:
                new = list(st); new[i] += 1
                key = tuple(new)
                acc[key] = acc.get(key, 0.0) + a * splus(st[i], S)
    return 0.5 * sum(v * v for v in acc.values())


xs = np.array([0.03, 0.06, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0])
res = {}
for S2 in [1, 2, 3]:
    states, index, S = build(S2)
    out(f"|S| = {S}: S^z_tot = 0 sector dimension {len(states)}")
    w = []
    gaps = []
    for x in xs:
        Delta = 1 + x
        H = hamiltonian(states, index, S, Delta)
        vals, vecs = eigsh(H, k=2, which="SA", tol=1e-10)
        o = np.argsort(vals)
        psi = vecs[:, o[0]]
        W = weight(states, S, psi) / (N / 2) / S
        lswt = np.sqrt(x / (2 + x))
        w.append(W)
        gaps.append(vals[o[1]] - vals[o[0]])
        out(f"  omega_A/omega_E = {x:5.2f}  E0/J = {vals[o[0]]:.5f}  gap to next (S^z=0) = {vals[o[1]]-vals[o[0]]:.2e}"
            f"  exact weight/pair/|S| = {W:.4f}  LSWT = {lswt:.4f}  ratio = {W/lswt:.3f}")
    res[S2] = np.array(w)
    res['g%d' % S2] = np.array(gaps)
np.savez(os.path.join(HERE, "ed14_3.npz"), x=xs, w1=res[1], w2=res[2], w3=res[3], g1=res['g1'], g2=res['g2'], g3=res['g3'])
LOG.close()
