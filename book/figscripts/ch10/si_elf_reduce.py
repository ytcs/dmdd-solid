"""Reduce the published silicon loss-function tables of Knapen, Kozaczuk and Lin to a binned file used by every
script of Sect. 10.2.  Natural units, energies and momenta in eV.

Source (public data, not computed here)
  S. Knapen, J. Kozaczuk, T. Lin, Phys. Rev. D 104, 015031 (2021), arXiv:2101.08275, Sect. III B: dielectric function
  of silicon in the random-phase approximation from GPAW (J. Enkovaara et al., J. Phys.: Condens. Matter 22, 253202
  (2010)), with and without local-field effects.  Distributed with the DarkELF package (S. Knapen, J. Kozaczuk, T. Lin,
  Phys. Rev. D 105, 015014 (2022), arXiv:2104.12786), github.com/tongylin/DarkELF, commit
  2f01cd5501d8f9c0dfdc3a011973dab9da718498, files data/Si/Si_gpaw_noLFE.dat and data/Si/Si_gpaw_withLFE.dat
  (downloaded 2026-11-02).  Columns: omega [eV], k [eV], eps1, eps2; 96 energies from 0 to 89.2 eV and 2094 values of
  |q| from 0 to 22.5 keV.
  * noLFE: eps = eps_00 (head of the RPA dielectric matrix).  Its eps2 is the independent-particle eps2 exactly
    (Sect. 4.6), so  IP:  S = (2q^2/e^2) eps2_noLF,   RPA:  L = eps2/|eps|^2 of the same file.
  * withLFE: eps = eps_mac = 1/(eps^{-1})_00 (KKL Sect. III B), so  RPA + LF:  L = Im(-1/eps_mac) = Im[-(eps^{-1})_00].

Reduction (a modelling choice of this book, stated in the caption of Fig. 10.2): the three response functions
  r_IP = eps2_noLF, r_RPA = Im(-1/eps_noLF), r_LF = Im(-1/eps_LF), and eps2_LF (eps2 of eps_mac, for comparison)
are formed point by point on the raw grid and then averaged over |q| in bins of 100 eV from 400 eV to 22.6 keV; the
raw momenta are the lengths of q + G on the calculation's mesh, so the bin average is an average over directions
(the isotropic rate needs the direction-averaged L, App. A.8).  The static step 1 - 1/eps(q, 0) is averaged in the
same bins from the omega = 0 rows.  Output: figscripts/ch10/si_elf_binned.npz.

Usage: python si_elf_reduce.py <dir with Si_gpaw_noLFE.dat and Si_gpaw_withLFE.dat>
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path):
    d = np.loadtxt(path, skiprows=1)
    om = np.unique(d[:, 0])
    k = np.unique(d[:, 1])
    io = np.searchsorted(om, d[:, 0])
    ik = np.searchsorted(k, d[:, 1])
    e1 = np.full((len(om), len(k)), np.nan)
    e2 = np.full((len(om), len(k)), np.nan)
    e1[io, ik] = d[:, 2]
    e2[io, ik] = d[:, 3]
    assert not np.isnan(e1).any() and not np.isnan(e2).any(), "grid not rectangular"
    return om, k, e1, e2


def main(src):
    om, k, e1n, e2n = load(os.path.join(src, "Si_gpaw_noLFE.dat"))
    om2, k2, e1l, e2l = load(os.path.join(src, "Si_gpaw_withLFE.dat"))
    assert np.allclose(om, om2) and np.allclose(k, k2)
    e2n = np.maximum(e2n, 0.0)
    e2l = np.maximum(e2l, 0.0)
    r_ip = e2n
    r_rpa = e2n / (e1n**2 + e2n**2)
    r_lf = e2l / (e1l**2 + e2l**2)
    r_e2lf = e2l                       # eps2 of eps_mac: absorption with local fields (unscreened, LF)
    step_rpa = 1 - 1 / e1n[0]          # omega = 0 row: eps is real there
    step_lf = 1 - 1 / e1l[0]
    edges = np.arange(400.0, 22601.0, 100.0)
    qc, IP, RPA, LF, E2L, SR, SL, nb = [], [], [], [], [], [], [], []
    for a, b in zip(edges[:-1], edges[1:]):
        m = (k >= a) & (k < b)
        if not m.any():
            continue
        qc.append(k[m].mean())
        IP.append(r_ip[:, m].mean(axis=1))
        RPA.append(r_rpa[:, m].mean(axis=1))
        LF.append(r_lf[:, m].mean(axis=1))
        E2L.append(r_e2lf[:, m].mean(axis=1))
        SR.append(step_rpa[m].mean())
        SL.append(step_lf[m].mean())
        nb.append(m.sum())
    out = os.path.join(HERE, "si_elf_binned.npz")
    np.savez_compressed(out, omega=om, q=np.array(qc), ip=np.array(IP).T, rpa=np.array(RPA).T,
                        lf=np.array(LF).T, e2lf=np.array(E2L).T, step_rpa=np.array(SR), step_lf=np.array(SL), nbin=np.array(nb),
                        eps_opt_noLF=e1n[0, 0], eps_opt_LF=e1l[0, 0])
    print("raw grid:", len(om), "energies to", om[-1], "eV;", len(k), "momenta to", k[-1], "eV")
    print("bins kept:", len(qc), " points per bin min/median/max:", min(nb), int(np.median(nb)), max(nb))
    print("q -> 0 rows: eps1(0,0) noLF = %.3f, LF = %.3f" % (e1n[0, 0], e1l[0, 0]))
    print("written", out)


if __name__ == "__main__":
    main(sys.argv[1])
