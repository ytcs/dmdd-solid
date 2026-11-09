"""Sensitivity of the GaAs lowest-band average <|L^ph|> (Sect. 14.5, Limit Check 14.5a panel a) to the grid, the masses,
the weighting, the long-range dipole part of the force constants and the definition of the average.
Log lph14_5.log.  Run: python lph14_5.py (about a minute).

Force constants: gaas_ifc14.py (PBE DFPT of Sect. 5.5).  L^ph = -i sum_kappa e* x e (eq:14.5-Lph), eigenvectors mass-weighted.
Matas, Krizek and Romao (2511.20461 Sect. III) quote 0.07 for GaAs from another dynamical matrix, on a 10^3 grid with
every lowest-band mode equally likely; their kappa = <||J_1||>/hbar.  The tests below vary one ingredient at a time.
"""
import os
import numpy as np
import gaas_ifc14 as G

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "lph14_5.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


B = np.array([[-1, -1, 1], [1, 1, 1], [-1, 1, -1]], float)
N = 10


def grid(shift):
    f = (np.arange(N) + shift) / N
    Q = np.array([(a, b, c) for a in f for b in f for c in f]) @ B
    return Q[np.linalg.norm(Q, axis=1) > 1e-9]


def lowest(Q, mass=None, dip=1.0):
    m0, r0 = G._SQM.copy(), G._rigid
    if mass is not None:
        G._SQM = np.sqrt(np.outer(mass, mass))
    G._rigid = lambda q, l=dip: l * r0(q)
    w, ev = G.phonons(Q)
    G._SQM, G._rigid = m0, r0
    return w, ev, G.ang_mom(ev)


Qs, Q0 = grid(0.5), grid(0.0)
w, ev, L = lowest(Qs)
Lm = np.linalg.norm(L, axis=2)[:, 0]
out(f"baseline, 10^3 shifted grid: lowest-band <|L|> = {Lm.mean():.3f}")
w0, ev0, L0 = lowest(Q0)
out(f"10^3 Gamma-centred grid: {np.linalg.norm(L0, axis=2)[:, 0].mean():.3f}")
for lab, mass in (("equal Ga and As masses", np.array([1, 1]) * G.MASS.mean()), ("Ga and As masses swapped", G.MASS[::-1])):
    out(f"{lab}: {np.linalg.norm(lowest(Qs, mass=mass)[2], axis=2)[:, 0].mean():.3f}")
ok = w0[:, 0] > 0
L0m = np.linalg.norm(L0, axis=2)[:, 0]
out(f"energy-weighted average: {np.sum(L0m[ok]*w0[ok,0])/np.sum(w0[ok,0]):.3f}; 1/omega-weighted: {np.sum(L0m[ok]/w0[ok,0])/np.sum(1/w0[ok,0]):.3f}")
for lam in (0.0, 0.5, 1.5):
    wl, _, Ll = lowest(Q0, dip=lam)
    okl = wl[:, 0] > 0
    out(f"long-range dipole part x{lam}: {np.linalg.norm(Ll, axis=2)[okl, 0].mean():.3f} (unstable modes {np.sum(~okl)})")
e = ev.reshape(ev.shape[0], 2, 3, ev.shape[2])
u = e / np.sqrt(G.MASS)[None, :, None, None]
u = u / np.sqrt((np.abs(u)**2).sum(axis=(1, 2), keepdims=True))
Lu = np.real(-1j * np.cross(np.conj(u), u, axis=2).sum(axis=1)).transpose(0, 2, 1)
out(f"displacement-normalized (not mass-weighted) vectors: {np.linalg.norm(Lu, axis=2)[:, 0].mean():.3f}")
out(f"one Cartesian component, <|L_x|>: {np.abs(L[:, 0, 0]).mean():.3f}; <|L_z|>: {np.abs(L[:, 0, 2]).mean():.3f}")
LOG.close()
