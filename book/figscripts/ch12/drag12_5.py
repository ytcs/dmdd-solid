"""Sect. 12.5: on-site drag mass versus the translation (trace) rule in a one-dimensional model insulator.
Run: python drag12_5.py  (< 1 min). Prints the numbers quoted in Sect. 12.5 ("the on-site element and the trace").

Model (a labelled model, not silicon): independent electrons (atomic units, hbar = m_e = 1) in a periodic chain of
Gaussian wells V(x) = -V0 sum_J exp[-(x - X_J)^2/(2 s^2)], lattice constant a, two electrons per well (one band filled,
spin 2). Supercell of N wells, periodic, plane waves |G| <= G_max (equivalent to N k-points of the primitive cell).
Drag-mass matrix (eq:8.6-fsum-k, independent pairs, spin factor 2):
    dM_IJ = 2 * 2 sum_{v occ, c empty} Re[<v|dV/dX_I|c><c|dV/dX_J|v>] / (e_c - e_v)^3 .
Translation rule: sum_J dV/dX_J = -dV/dx, <c|V'|v> = -(e_c - e_v)^2 <c|x|v> (m_e = 1), and the f-sum over empty states
give sum_J dM_IJ = 2 m_e per well exactly (= N_e m_e). On site: dM_II, the Brillouin-zone average of dM(Q).
Isolated well (one well in a large box): dM = 2 m_e by the Thomas-Reiche-Kuhn rule (check).
"""
import numpy as np

A = 4.0        # lattice constant (bohr)
S = 0.6        # well width (bohr)


def drag(V0, N=24, a=A, s=S, nmax=None):
    L = N * a
    if nmax is None:
        nmax = int(np.ceil(14.0 / s * L / (2 * np.pi)))
    n = np.arange(-nmax, nmax + 1)
    G = 2 * np.pi * n / L
    K = G[:, None] - G[None, :]
    X = a * np.arange(N)
    form = -V0 * np.sqrt(2 * np.pi) * s * np.exp(-K**2 * s**2 / 2) / L        # one well at the origin, V(K)
    H = np.diag(G**2 / 2) + form * np.exp(-1j * K * X[:, None, None]).sum(0)
    e, U = np.linalg.eigh(H)
    nocc = N                                       # one band, two electrons per well
    v, c = U[:, :nocc], U[:, nocc:]
    dE = e[nocc:][None, :] - e[:nocc][:, None]
    I = 0
    dVI = -1j * K * form * np.exp(-1j * K * X[I])   # dV/dX_I in plane waves
    Fi = v.conj().T @ dVI @ c                       # <v|dV/dX_I|c>
    onsite = 4 * np.sum(np.abs(Fi)**2 / dE**3)
    tot = 0.0
    for J in range(N):
        dVJ = -1j * K * form * np.exp(-1j * K * X[J])
        FJ = v.conj().T @ dVJ @ c
        tot += 4 * np.sum(np.real(Fi * FJ.conj()) / dE**3)
    gap = e[nocc] - e[nocc - 1]
    width = e[nocc - 1] - e[0]
    return onsite, tot, gap, width


if __name__ == "__main__":
    # isolated well: one well, large box
    on, tot, gap, _ = drag(3.0, N=1, a=40.0)
    print(f"isolated well V0 = 3: dM = {on:.4f} m_e (TRK: 2), excitation threshold {gap:.3f} Ha")
    print(" V0 (Ha) | gap (eV) | occ. width (eV) | on-site dM_II (m_e) | sum_J dM_IJ (m_e) | on-site / 2 m_e")
    for V0 in [8.0, 4.0, 2.0, 1.0, 0.6, 0.4]:
        on, tot, gap, w = drag(V0)
        print(f" {V0:6.2f}  | {gap*27.2114:8.3f} | {w*27.2114:10.3f}      | {on:12.3f}        | {tot:10.4f}        | {on/2:.2f}")
    # k convergence at the smallest gap
    for N in [16, 24, 32]:
        on, tot, gap, w = drag(0.4, N=N)
        print(f"   V0 = 0.4, N = {N}: on-site {on:.3f}, trace {tot:.4f}")
