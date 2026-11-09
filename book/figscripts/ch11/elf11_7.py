"""Direction-resolved electronic response of silicon and GaAs in the empirical pseudopotential model, for Sect. 11.7.
Writes figscripts/ch11/elf11_7_<MAT>_NK<NK>.npz; elf11_7_proj.py-like projection is done in limit11_7a.py / fig11_7.py / we11_8.py.

Model (a labelled model, not a first-principles response): the local empirical pseudopotential of Cohen and Bergstresser,
  Phys. Rev. 141, 789 (1966), via figscripts/ch03/epm.py (Si a = 5.43 A, GaAs a = 5.64 A, 113-vector basis |G|^2 <= 21 (2 pi/a)^2,
  no spin-orbit coupling; model indirect gap of Si 0.82 eV), as in Limit 10.1a (figscripts/ch10/limit10_1a.py).
Response: the head of the independent-particle response, S0(q, w) = -2 Im R0_00(q, w) (eq:4.6-R0, T = 0), and the head-only
  random-phase loss function L = Im[-1/eps_00] with eps_00 = 1 - v_C(q) R0_00 (eq:4.6-rpa), no local fields.  q is unreduced
  (never folded, Sect. 3.1).  Adler-Wiser sum with 4 valence and NC = 26 conduction bands, resonant and antiresonant terms,
  Lorentzian broadening ETA = 0.15 eV, then averaged over omega in 1-eV bins centred on 2, 3, ..., 14 eV.
k grid: Gamma-centred NK^3 grid in the primitive reciprocal basis (invariant under O_h, so the computed S(qhat) has exactly the
  cubic symmetry and every l = 2 or odd-l component vanishes identically: no symmetry-breaking artifact). Convergence of the
  l = 4 component is checked by NK = 10, 12, 14 at q = q0 (elf11_7_conv.log).
Directions: ten directions of the irreducible wedge of O_h, [100] [110] [111] [210] [211] [221] [310] [311] [321] [531]; the
  cubic-harmonic components S_l (l = 0, 4, 6, 8) are a least-squares fit to these ten (residual printed by the projection).
q grid: q/q0 = 0.4 ... 2.8 (QLIST default), plus a second run at 0.15, 0.25 (TAG=_lowq, elf11_7_<MAT>_NK12_lowq.npz); q0 = alpha m_e = 3.73 keV; the model has no true high-momentum tails (basis), so it stops at 2.8 q0.
Run: MAT=Si NK=12 python3 elf11_7.py   (parallel over directions with PAR=4)
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import time
import numpy as np
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
from epm import EPM, RY, BOHR, HBARC   # noqa: E402

HA = 2 * RY
ME = 510998.95
ALPHA = 1 / 137.035999177
MAT = os.environ.get("MAT", "Si")
NK = int(os.environ.get("NK", 12))
NC, NV = 26, 4
NB = NV + NC
ETA = 0.15
OM = np.round(np.arange(0.5, 15.5001, 0.05), 3)
BIN_C = np.arange(2.0, 14.01, 1.0)
DIRS = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (2, 1, 1), (2, 2, 1), (3, 1, 0), (3, 1, 1), (3, 2, 1), (5, 3, 1)]
QLIST = [float(x) for x in os.environ.get("QLIST", "0.4,0.55,0.7,0.85,1.0,1.2,1.4,1.7,2.0,2.4,2.8").split(",")]

mat = EPM(MAT)
a_A = mat.a
a = a_A / BOHR
Omega = a**3 / 4
tpa = 2 * np.pi / a
Gb = mat.G
NPW = len(Gb)
key = {tuple(np.rint(g).astype(int)): i for i, g in enumerate(Gb)}
unit_eV = 2 * np.pi * HBARC / a_A
q0 = ALPHA * ME
AU_R_TO_EV2 = (HBARC / BOHR) ** 3 / HA
B = np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], float)
_n = 8
_idx = np.array([(i, j, k) for i in range(-_n, _n + 1) for j in range(-_n, _n + 1) for k in range(-_n, _n + 1)])
cand = _idx @ B
cand = cand[(cand**2).sum(1) <= 80]
f = np.arange(NK) / NK
kc = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T
kpts = kc @ B
NKT = len(kpts)
pref_au = 2.0 / (NKT * Omega)
_maps = {}


def states(ks):
    w, v = np.linalg.eigh(mat.hamiltonian(ks))
    return w[:, :NB] * RY, v[:, :, :NB]


def fold(kq):
    return cand[np.argmin(((kq[None, :] - cand) ** 2).sum(1))]


def shift_map(GU):
    k_ = tuple(np.rint(GU).astype(int))
    if k_ not in _maps:
        _maps[k_] = np.array([key.get(tuple(np.rint(g + GU).astype(int)), -1) for g in Gb])
    return _maps[k_]


def spectra(qvec_unit):
    """Head R0_00 on the OM grid; qvec in units of 2pi/a."""
    w_au = OM / HA
    R0 = np.zeros(len(OM), complex)
    chunk = 64
    for c0 in range(0, NKT, chunk):
        ks = kpts[c0:c0 + chunk]
        GUs = np.array([fold(k + qvec_unit) for k in ks])
        e1, c1 = states(ks)
        e2, c2 = states(ks + qvec_unit - GUs)
        for i in range(len(ks)):
            SM = shift_map(GUs[i])                 # index of G + G_U in the basis, -1 if outside
            pad = np.vstack([c2[i], np.zeros((1, NB))])
            cs = pad[SM]                           # cs[G] = c_{k+q-GU}(G + GU)
            # <n', k+q | e^{i q.r} | n, k> = sum_G c*_{n',k'}(G + G_U) c_{n,k}(G)
            A = cs[:, NV:].conj().T @ c1[i][:, :NV]          # (c, v)
            Bm = cs[:, :NV].conj().T @ c1[i][:, NV:]         # (v', c)
            dEr = ((e2[i][NV:][:, None] - e1[i][:NV][None, :]) / HA).ravel()
            dEa = ((e1[i][NV:][None, :] - e2[i][:NV][:, None]) / HA).ravel()
            R0 += (np.abs(A.ravel())**2 / (w_au[:, None] - dEr[None, :] + 1j * ETA / HA)).sum(1) \
                - (np.abs(Bm.ravel())**2 / (w_au[:, None] + dEa[None, :] + 1j * ETA / HA)).sum(1)
    R0 *= pref_au
    qG2 = (qvec_unit**2).sum()
    vC = 4 * np.pi / (qG2 * tpa**2)
    S0 = -2 * R0.imag * AU_R_TO_EV2
    eps = 1 - vC * R0
    L = (-1 / eps).imag
    return S0, L, eps


def binned(y):
    return np.array([y[(OM >= c - 0.5) & (OM < c + 0.5)].mean() for c in BIN_C])


def run_dir(d):
    dh = np.array(d, float) / np.linalg.norm(d)
    out_S, out_L = [], []
    for qf in QLIST:
        t = time.time()
        S0, L, eps = spectra(qf * q0 / unit_eV * dh)
        out_S.append(binned(S0))
        out_L.append(binned(L))
        print("%s dir %s q = %.2f q0: S0(5 eV) = %.3e, L(5 eV) = %.3f (%.0f s)" % (MAT, d, qf, out_S[-1][3], out_L[-1][3], time.time() - t),
              flush=True)
    return np.array(out_S), np.array(out_L)


if __name__ == "__main__":
    t0 = time.time()
    with Pool(int(os.environ.get("PAR", 4))) as p:
        res = p.map(run_dir, DIRS)
    S = np.array([r[0] for r in res])      # (dir, q, bin)
    L = np.array([r[1] for r in res])
    out = os.path.join(HERE, "elf11_7_%s_NK%d%s.npz" % (MAT, NK, os.environ.get("TAG", "")))
    np.savez(out, DIRS=np.array(DIRS, float), Q=np.array(QLIST), BIN=BIN_C, S0=S, L=L, q0=q0, NK=NK)
    print("wrote", out, "(%.0f s)" % (time.time() - t0))
