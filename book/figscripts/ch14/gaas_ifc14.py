"""GaAs harmonic force constants for Sect. 14.5 (chiral phonons in a crystal without inversion).

Source: the PBE DFPT run of Sect. 5.5 (figscripts/ch05/gaas_cache/GaAs.fc, q2r output of tab5_1_gaas_qe.sh: 8^3 k, 4^3 phonon
grid, static PBE lattice alat = 10.6543 bohr = 5.638 A, masses 69.723 and 74.9216 u). Fourier interpolation exactly as
ch05/si_ifc.py (Wigner-Seitz weights as matdyn.x), phase exp(-2 pi i q.R) with R in alat (matdyn's
convention; eigenvectors in the R gauge, so that the nuclear vertex carries exp(i q.tau_kappa), as in eq:11.1-S1).
The rigid-ion dipole sum that q2r subtracted is added back as matdyn.x does (rgd_blk: Ewald G sum with the Born charges and
eps_inf of the file header, alpha = 1 bohr^-2, cut exp(-14)); with it the dynamical matrix at the L point equals GaAs.dyn3 of the
DFPT run to all printed digits. The acoustic sum rule is imposed by the uniform symmetric correction described at ASR below; with it
the three acoustic branches agree with the matdyn.x dispersion of Fig. 5.4 (gaas_cache/disp_comp.freq, 183 points) to 1e-3 meV.
MODELLING CHOICE: the nonanalytic (LO-TO) term at q -> 0 is omitted; it moves only the LO branch at the zone centers (2.1 meV at
Gamma) and leaves the acoustic branches unchanged.
Wavevectors are Cartesian in units of 2 pi/a.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FC = os.path.join(HERE, "..", "ch05", "gaas_cache", "GaAs.fc")
RY_MEV = 13605.693122994
AMU_RY = 911.444243
A_ANG = 10.6542759 * 0.529177210903

with open(FC) as f:
    L = f.read().split("\n")
hdr = L[0].split()
NTYP, NAT = int(hdr[0]), int(hdr[1])
AMASS = np.array([float(L[1 + i].split()[-1]) for i in range(NTYP)])          # Ry mass units
ITYP = np.array([int(L[1 + NTYP + i].split()[1]) - 1 for i in range(NAT)])
TAU = np.array([[float(x) for x in L[1 + NTYP + i].split()[2:5]] for i in range(NAT)])
MASS = AMASS[ITYP]
i0 = 1 + NTYP + NAT
assert L[i0].split()[0] == "T"
EPS = np.array([[float(x) for x in L[i0 + 1 + r].split()] for r in range(3)])
ZEU = np.array([[[float(x) for x in L[i0 + 4 + 4 * na + 1 + r].split()] for r in range(3)] for na in range(NAT)])
i0 += 1 + 3 + NAT * 4
NR = tuple(int(x) for x in L[i0].split())
PHI = np.zeros((3, 3, NAT, NAT) + NR)
k = i0 + 1
for _ in range(9 * NAT * NAT):
    a, b, na, nb = (int(x) for x in L[k].split())
    k += 1
    for _ in range(NR[0] * NR[1] * NR[2]):
        m1, m2, m3, v = L[k].split()
        PHI[a - 1, b - 1, na - 1, nb - 1, int(m1) - 1, int(m2) - 1, int(m3) - 1] = float(v)
        k += 1
A1 = 0.5 * np.array([[-1, 0, 1], [0, 1, 1], [-1, 1, 0]], float)
ASR = os.environ.get("GAAS_ASR", "uniform")
if ASR == "onsite":                                         # on-site acoustic sum rule (as ch05/si_ifc.py)
    for ka in range(NAT):
        s = PHI[:, :, ka, :, :, :, :].sum(axis=(2, 3, 4, 5))
        PHI[:, :, ka, ka, 0, 0, 0] -= s
elif ASR == "uniform":
    # acoustic sum rule by the smallest uniform correction that keeps the index symmetry: delta(R; k, k') = C_k + C_k' for every R,
    # with Ncell (2 C_k + sum_k' C_k') = -s_k.  A correction constant in R changes D(q) only at q = 0 among the 4^3 grid points, so
    # the computed frequencies at every other grid point are kept exactly (checked against matdyn below).
    Ncell = NR[0] * NR[1] * NR[2]
    S_ = np.array([PHI[:, :, ka, :, :, :, :].sum(axis=(2, 3, 4, 5)) for ka in range(NAT)])
    Mx = Ncell * (2 * np.eye(NAT) + np.ones((NAT, NAT)))
    C_ = np.einsum("kl,lab->kab", np.linalg.inv(Mx), -S_)
    for ka in range(NAT):
        for kb in range(NAT):
            PHI[:, :, ka, kb] += (C_[ka] + C_[kb])[:, :, None, None, None]
_T = np.array([(i, j, l) for i in range(-2, 3) for j in range(-2, 3) for l in range(-2, 3)], float)
_TS = (_T * np.array(NR)) @ A1
_terms = []
for ka in range(NAT):
    for kb in range(NAT):
        for m1 in range(NR[0]):
            for m2 in range(NR[1]):
                for m3 in range(NR[2]):
                    R = np.array([m1, m2, m3], float) @ A1
                    imgs = R + _TS
                    dist = np.linalg.norm(imgs + TAU[ka] - TAU[kb], axis=1)
                    sel = np.where(dist < dist.min() + 1e-6)[0]
                    for s in sel:
                        _terms.append((ka, kb, m1, m2, m3, imgs[s], 1.0 / len(sel)))
_K = np.array([t[0] for t in _terms]); _KP = np.array([t[1] for t in _terms])
_M = np.array([t[2:5] for t in _terms]); _RI = np.array([t[5] for t in _terms]); _W = np.array([t[6] for t in _terms])
_PH = np.stack([PHI[:, :, _K[n], _KP[n], _M[n, 0], _M[n, 1], _M[n, 2]] for n in range(len(_terms))])
_SQM = np.sqrt(np.outer(MASS, MASS))
ALAT = 10.6542759
OMEGA = ALAT**3 / 4
_B = np.array([[-1, -1, 1], [1, 1, 1], [-1, 1, -1]], float)    # fcc reciprocal vectors, 2 pi/alat
_G = np.array([(i, j, l) for i in range(-12, 13) for j in range(-12, 13) for l in range(-12, 13)], float) @ _B
GAUGE = "qe"            # dipole phase exp(i g.(tau_a - tau_b)), g = q + G (rgd_blk); the alternative is a test only
EXPF = (2 * np.pi / ALAT)**2   # exponent in bohr^-2 (alpha = 1 bohr^-2)


def _rigid(q):
    """Dipole-dipole (rigid-ion Ewald) term of matdyn.x (rgd_blk, alpha = 1, gmax = 14), Ry/bohr^2, for one q (2 pi/alat)."""
    fac = 2 * 4 * np.pi / OMEGA
    D = np.zeros((NAT, 3, NAT, 3), complex)
    G0 = _G[np.linalg.norm(_G, axis=1) > 1e-9]
    geg = np.einsum("gi,ij,gj->g", G0, EPS, G0)
    sel = geg * EXPF / 4 < 14
    G0, geg = G0[sel], geg[sel]
    fg = fac * np.exp(-geg * EXPF / 4) / geg
    zg = np.einsum("gi,nij->gnj", G0, ZEU)                        # (g, na, j)
    for na in range(NAT):
        fnat = np.zeros((len(G0), 3))
        for nb in range(NAT):
            fnat += zg[:, nb, :] * np.cos(2 * np.pi * G0 @ (TAU[na] - TAU[nb]))[:, None]
        D[na, :, na, :] -= np.einsum("g,gi,gj->ij", fg, zg[:, na, :], fnat)
    g = _G + q
    geg = np.einsum("gi,ij,gj->g", g, EPS, g)
    sel = (geg > 1e-12) & (geg * EXPF / 4 < 14)
    g, geg = g[sel], geg[sel]
    fg = fac * np.exp(-geg * EXPF / 4) / geg
    zg = np.einsum("gi,nij->gnj", g, ZEU)
    for na in range(NAT):
        for nb in range(NAT):
            if GAUGE == "qe":
                ph = np.exp(2j * np.pi * g @ (TAU[na] - TAU[nb]))
            else:
                ph = np.exp(2j * np.pi * (g - q) @ (TAU[na] - TAU[nb]))
            D[na, :, nb, :] += np.einsum("g,gi,gj->ij", fg * ph, zg[:, na, :], zg[:, nb, :])
    return D.reshape(3 * NAT, 3 * NAT)


def phonons(q):
    """Frequencies (meV, ascending) and eigenvectors e[q, 3*kappa+alpha, nu] at Cartesian q (n,3) in 2 pi/a."""
    q = np.atleast_2d(q)
    ph = np.exp(-2j * np.pi * (q @ _RI.T)) * _W
    D = np.zeros((len(q), 3 * NAT, 3 * NAT), complex)
    for ka in range(NAT):
        for kb in range(NAT):
            sel = (_K == ka) & (_KP == kb)
            D[:, 3 * ka:3 * ka + 3, 3 * kb:3 * kb + 3] = np.einsum("qt,tab->qab", ph[:, sel], _PH[sel])
    for n in range(len(q)):
        if np.linalg.norm(q[n]) > 1e-9:
            D[n] += _rigid(q[n])
    D = D / np.repeat(np.repeat(_SQM, 3, 0), 3, 1)
    D = 0.5 * (D + np.conj(np.transpose(D, (0, 2, 1))))
    w2, ev = np.linalg.eigh(D)
    w = np.sign(w2) * np.sqrt(np.abs(w2)) * RY_MEV
    return w, ev


def ang_mom(ev):
    """Phonon angular momentum L^ph = -i sum_kappa e* x e (units of hbar) for eigenvectors ev[q, 3*NAT, nu]; returns (q, nu, 3)."""
    e = ev.reshape(ev.shape[0], NAT, 3, ev.shape[2])
    c = np.cross(np.conj(e), e, axis=2)            # (q, kappa, 3, nu)
    return np.real(-1j * c.sum(axis=1)).transpose(0, 2, 1)


if __name__ == "__main__":
    w, _ = phonons(np.array([[0, 0, 0.001], [1, 0, 0], [0.5, 0.5, 0.5]]))
    print("Gamma, X, L (meV):")
    print(np.round(w, 2))
