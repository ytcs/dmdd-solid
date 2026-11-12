"""Reduce the published germanium independent-particle dielectric table of Knapen, Kozaczuk and Lin to a binned file
used by the Sect. 10.6 scripts.  Natural units, energies and momenta in eV.

Source (public data, not computed here)
  S. Knapen, J. Kozaczuk, T. Lin, Phys. Rev. D 104, 015031 (2021), arXiv:2101.08275, Sect. III B: dielectric function
  of germanium from GPAW (TB09 functional, scissor to the measured gap at T = 0, 12^3 k points, 70 bands, plane-wave
  cutoff 500 eV, i.e. |k| < 22 keV; the 3d electrons are in the frozen core).  Distributed with DarkELF
  (arXiv:2104.12786), github.com/tongylin/DarkELF, commit 2f01cd5501d8f9c0dfdc3a011973dab9da718498, file
  data/Ge/Ge_gpaw_noLFE.dat (47 MB, not kept).  Columns: omega [eV], k [eV], eps1, eps2.
  Without local fields eps2 is the independent-particle eps2 of the valence electrons (Sect. 4.6), so the valence
  structure factor is S = (2q^2/e^2) eps2 and, per atom, S_at = q^2 Omega eps2 / (8 pi^2 alpha) (two atoms per cell).

Reduction (same as si_elf_reduce.py): eps2 averaged over |q| in bins of 100 eV from 400 eV to 22.6 keV (an average over
directions).  Output: figscripts/ch10/ge_ip_binned.npz (omega, q, ip).

Usage: python ge_ip_reduce.py <dir with Ge_gpaw_noLFE.dat>
"""
import os
import sys
import numpy as np
from si_elf_reduce import load

HERE = os.path.dirname(os.path.abspath(__file__))


def main(src):
    om, k, e1, e2 = load(os.path.join(src, "Ge_gpaw_noLFE.dat"))
    e2 = np.maximum(e2, 0.0)
    edges = np.arange(400.0, 22601.0, 100.0)
    qc, IP = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        m = (k >= a) & (k < b)
        if m.any():
            qc.append(k[m].mean())
            IP.append(e2[:, m].mean(axis=1))
    out = os.path.join(HERE, "ge_ip_binned.npz")
    np.savez_compressed(out, omega=om, q=np.array(qc), ip=np.array(IP).T, eps_opt=e1[0, 0])
    print("raw grid:", len(om), "energies to", om[-1], "eV;", len(k), "momenta to", k[-1], "eV; eps1(0,0) =", e1[0, 0])
    print("written", out)


if __name__ == "__main__":
    main(sys.argv[1])
