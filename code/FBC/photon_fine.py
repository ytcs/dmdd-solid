"""Photon seed share histogram on a fine grid (vertical transitions only, so a dense grid is cheap): used to size the
k-sampling noise of the 12^3 photon seed and for the photon-vs-DM comparison inside the energy-only cascade.
Writes WORK/photon_fine_<variant>_n<N>.npz with H[omega_bin, E_e_bin] (0.05 eV bins).
Run: python3 photon_fine.py [N]   (default 28; shifted Monkhorst-Pack grid over the full zone)
"""
import fbc_common  # noqa: F401
import os
import sys
import numpy as np
from fbc_common import make_epm, model_edges, RY, NV, EG, WORK, B, UNIT

N = int(sys.argv[1]) if len(sys.argv) > 1 else 28
VARIANT = os.environ.get("FBC_BANDS", "refit")
DB = 0.05
NBIN = int(22.0 / DB)
SIG = 0.10


def main():
    si = make_epm(VARIANT)
    ev, ec, _ = model_edges(si)
    delta = (EG - (ec - ev)) if VARIANT == "scissor" else 0.0
    f = (np.arange(N) + 0.5) / N
    k = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T @ B
    H = np.zeros((NBIN, NBIN))
    for c0 in range(0, len(k), 256):
        ks = k[c0:c0 + 256]
        w, v = np.linalg.eigh(si.hamiltonian(ks))
        e = w[:, :20] * RY - ev
        kG = (ks[:, None, :] + si.G[None]) * UNIT * 1973.269804
        p2 = np.zeros((len(ks), 16, NV))
        for a in range(3):
            pa = np.einsum("kgc,kg,kgv->kcv", v[:, :, NV:20].conj(), kG[:, :, a], v[:, :, :NV], optimize=True)
            p2 += np.abs(pa) ** 2 / 3
        dEr = e[:, NV:20, None] - e[:, None, :NV]
        wgt = p2 / dEr ** 2
        es = e.copy()
        es[:, NV:] += delta
        dE = es[:, NV:20, None] - es[:, None, :NV]
        Ee = (es[:, NV:20] - EG)[:, :, None] + 0 * dE
        xb = np.clip((dE / DB).astype(int), 0, NBIN - 1).ravel()
        eb = np.clip((Ee / DB).astype(int), 0, NBIN - 1).ravel()
        H += np.bincount(xb * NBIN + eb, weights=wgt.ravel(), minlength=NBIN * NBIN).reshape(NBIN, NBIN)
    np.savez(os.path.join(WORK, f"photon_fine_{VARIANT}_n{N}.npz"), H=H)
    print("done", len(k))


if __name__ == "__main__":
    main()
