"""Reduce the published germanium dielectric tables of Knapen, Kozaczuk and Lin to binned loss functions for Sect. 12.5
(Table 12.1, germanium valence Migdal moments).  Natural units, energies and momenta in eV.

Source (public data, not computed here): S. Knapen, J. Kozaczuk, T. Lin, Phys. Rev. D 104, 015031 (2021),
arXiv:2101.08275, Sect. III B (GPAW, 3d electrons in the frozen core, scissor to the measured gap); distributed with
DarkELF (arXiv:2104.12786), github.com/tongylin/DarkELF commit 2f01cd5501d8f9c0dfdc3a011973dab9da718498, files
data/Ge/Ge_gpaw_noLFE.dat and data/Ge/Ge_gpaw_withLFE.dat (47 MB each, not kept).
Columns: omega [eV], k [eV], eps1, eps2.  Same reduction as figscripts/ch10/si_elf_reduce.py: r_RPA = Im(-1/eps_noLF),
r_LF = Im(-1/eps_LF), r_IP = eps2_noLF, averaged over |q| in 100-eV bins from 400 eV to 22.6 keV.
Output: figscripts/ch12/ge_elf_binned.npz.   Usage: python ge_elf_reduce.py <dir with the two .dat files>
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
from si_elf_reduce import load  # noqa: E402


def main(src):
    om, k, e1n, e2n = load(os.path.join(src, "Ge_gpaw_noLFE.dat"))
    om2, k2, e1l, e2l = load(os.path.join(src, "Ge_gpaw_withLFE.dat"))
    assert np.allclose(om, om2) and np.allclose(k, k2)
    e2n, e2l = np.maximum(e2n, 0.0), np.maximum(e2l, 0.0)
    r = {"ip": e2n, "rpa": e2n / (e1n**2 + e2n**2), "lf": e2l / (e1l**2 + e2l**2)}
    edges = np.arange(400.0, 22601.0, 100.0)
    qc, out = [], {key: [] for key in r}
    for a, b in zip(edges[:-1], edges[1:]):
        m = (k >= a) & (k < b)
        if m.any():
            qc.append(k[m].mean())
            for key in r:
                out[key].append(r[key][:, m].mean(axis=1))
    np.savez_compressed(os.path.join(HERE, "ge_elf_binned.npz"), omega=om, q=np.array(qc),
                        **{key: np.array(v).T for key, v in out.items()},
                        eps_opt_noLF=e1n[0, 0], eps_opt_LF=e1l[0, 0])
    print("raw grid:", len(om), "energies to", om[-1], "eV;", len(k), "momenta to", k[-1], "eV")
    print("first nonzero energy row of eps2 (noLF):", om[np.argmax(e2n.max(axis=1) > 1e-6)], "eV")
    print("eps1(0,0) noLF = %.3f, LF = %.3f" % (e1n[0, 0], e1l[0, 0]))


if __name__ == "__main__":
    main(sys.argv[1])
