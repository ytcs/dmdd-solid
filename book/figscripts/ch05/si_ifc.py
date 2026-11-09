"""Fourier interpolation of the silicon force constants of Sect. 5.2 (fig5_6_fc.npz), used by fig5_6.py and we5_9.py.
Wigner-Seitz weights as in matdyn.x: each constant Phi(R; kappa, kappa') of the 6^3 supercell is shared equally among the
images R + T (T a supercell vector) of minimal length |R + tau_kappa - tau_kappa'|. The acoustic sum rule is imposed by the
on-site correction of Eq. (5.4-asrfix) (modelling choice; the dispersion of Sect. 5.2 used q2r's 'crystal' rule instead;
the two differ by less than 0.1 meV away from the zone center, checked by check_path() against fig5_2_data.npz).
Wavevectors are Cartesian in units of 2pi/a. Frequencies are returned in meV, sorted, with polarization vectors.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RY_MEV = 13605.693122994     # meV per Ry

_d = np.load(os.path.join(HERE, "fig5_6_fc.npz"))
PHI, TAU, AMASS, NR = _d["phi"].copy(), _d["tau"], float(_d["amass"]), tuple(_d["nr"])
NAT = TAU.shape[0]
A1 = 0.5 * np.array([[-1, 0, 1], [0, 1, 1], [-1, 1, 0]], float)   # QE ibrav = 2 primitive vectors, alat units

# acoustic sum rule, on-site correction: Phi(0; k, k) -= sum_{R k'} Phi(R; k, k')
for k in range(NAT):
    s = PHI[:, :, k, :, :, :, :].sum(axis=(2, 3, 4, 5))
    PHI[:, :, k, k, 0, 0, 0] -= s

# Wigner-Seitz images
_T = np.array([(i, j, l) for i in range(-2, 3) for j in range(-2, 3) for l in range(-2, 3)], float)
_TS = (_T * np.array(NR)) @ A1            # supercell vectors (alat)
_terms = []                               # (k, k', m1, m2, m3, R_image (alat), weight)
for k in range(NAT):
    for kp in range(NAT):
        for m1 in range(NR[0]):
            for m2 in range(NR[1]):
                for m3 in range(NR[2]):
                    R = np.array([m1, m2, m3], float) @ A1
                    imgs = R + _TS
                    dist = np.linalg.norm(imgs + TAU[k] - TAU[kp], axis=1)
                    sel = np.where(dist < dist.min() + 1e-6)[0]
                    w = 1.0 / len(sel)
                    for s in sel:
                        _terms.append((k, kp, m1, m2, m3, imgs[s], w))
_K = np.array([t[0] for t in _terms]); _KP = np.array([t[1] for t in _terms])
_M = np.array([t[2:5] for t in _terms]); _RI = np.array([t[5] for t in _terms]); _W = np.array([t[6] for t in _terms])
_PH = np.stack([PHI[:, :, _K[n], _KP[n], _M[n, 0], _M[n, 1], _M[n, 2]] for n in range(len(_terms))])  # (nterm,3,3)


def dynmat(q):
    """Dynamical matrices (Ry^2 per Ry-mass units) at Cartesian wavevectors q (n,3) in 2pi/a."""
    q = np.atleast_2d(q)
    ph = np.exp(-2j * np.pi * (q @ _RI.T)) * _W            # (nq, nterm)
    D = np.zeros((len(q), 3 * NAT, 3 * NAT), complex)
    for k in range(NAT):
        for kp in range(NAT):
            sel = (_K == k) & (_KP == kp)
            D[:, 3 * k:3 * k + 3, 3 * kp:3 * kp + 3] = np.einsum("qt,tab->qab", ph[:, sel], _PH[sel])
    D = 0.5 * (D + np.conj(np.transpose(D, (0, 2, 1))))
    return D / AMASS


def phonons(q):
    """Frequencies (meV, ascending; imaginary as negative) and eigenvectors at wavevectors q (n,3) in 2pi/a."""
    w2, ev = np.linalg.eigh(dynmat(q))
    return np.sign(w2) * np.sqrt(np.abs(w2)) * RY_MEV, ev


def check_path():
    """Largest deviation (meV) from the matdyn dispersion of Sect. 5.2, overall and away from Gamma (|q| > 0.1)."""
    d = np.load(os.path.join(HERE, "fig5_2_data.npz"))
    w, _ = phonons(d["q"])
    ref = d["f"] * 0.123984198
    dev = np.abs(w - ref).max(axis=1)
    far = np.linalg.norm(d["q"], axis=1) > 0.1
    return dev.max(), dev[far].max()


if __name__ == "__main__":
    print("terms", len(_terms), "; max |dev| from matdyn path (meV): all %.4f, |q|>0.1: %.4f" % check_path())
    print("Gamma (meV):", np.round(phonons([[0, 0, 0]])[0][0], 3))
