"""Worked example 21.6 (we:21-libentry) and the size estimates of Sect. 21.6.  Every number printed in Sect. 21.6 is
in we21_6.log.  Natural units hbar = c = 1, e^2 = 4 pi alpha; energies and momenta in eV.

Public data used (not computed here)
  S. Knapen, J. Kozaczuk, T. Lin, Phys. Rev. D 104, 015031 (2021), arXiv:2101.08275, Sect. III B: RPA dielectric
  function of silicon from GPAW; Kohn-Sham states with the TB09 functional, plane-wave cutoff 500 eV, Gamma-centred
  8x8x8 Monkhorst-Pack grid, 70 bands per spin, scissor to the measured T = 0 gap.  Tables distributed with DarkELF
  (Knapen, Kozaczuk, Lin, arXiv:2104.12786), github.com/tongylin/DarkELF commit
  2f01cd5501d8f9c0dfdc3a011973dab9da718498, data/Si/Si_gpaw_noLFE.dat and data/Si/Si_gpaw_withLFE.dat.  Columns
  omega [eV], k [eV], eps1, eps2; the first line of each file is the GPAW citation.  As in figscripts/ch10/si_elf_reduce.py:
    noLFE  : eps = eps_00, the head of the RPA dielectric matrix; L_RPA = eps2/|eps|^2, and eps2 is the IP eps2;
    withLFE: eps = eps_mac = 1/(eps^-1)_00;                        L_LF  = Im(-1/eps_mac) = Im[-(eps^-1)_00].
  The k column is |q + G| on the calculation's mesh, so nodes with nearly equal k differ in direction.
  Book values: a_Si = 5.431 A (Sect. 1.2), valence omega_p = 16.6 eV (Sect. 4.3), q0 = alpha m_e.
  EPM comparison (Sect. 8.8, we8_10 log): S(RPA+LF) at q0 along [100], omega = 10 eV, 4.888e7 eV^2; delta_X = -0.06.
  Grid of the electronic library (App. E.16): |q| <= 25 alpha m_e in steps of 0.1 alpha m_e, 30 directions,
  omega <= 50 eV in steps of 0.05 eV, 10^3 k points, 60 bands (silicon: 4 occupied, 56 empty).
  Lattice library grid (App. E.17): 400 values of q, omega 0-1 eV in 0.1 meV steps, 3 temperatures.

Conversion (eq:4.4-SL, T = 0):  S = (2 q^2/e^2) L  [eV^2, per volume];  per cell Omega*S [eV^-1], Omega = a^3/4.
f-sum of the loss function (Sect. 4.4): int_0^inf omega L domega = (pi/2) omega_p^2; the fraction below the table's
top energy (89.2 eV) is printed for the node's k.

Usage:  python we21_6.py extract <dir with the two .dat files>   (writes we21_6_raw.npz, the rows with 3.4 < k < 4.1 keV)
        python we21_6.py                                         (prints everything from we21_6_raw.npz)
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ALPHA = 1 / 137.035999084
ME = 510998.95
HBARC = 1973.269804           # eV A
A_SI = 5.431                  # A
OMEGA_CELL = A_SI**3 / 4 / HBARC**3     # eV^-3
WP_VAL = 16.6
Q0 = ALPHA * ME
E2 = 4 * np.pi * ALPHA
S_EPM, DX_EPM = 4.888e7, -0.06


def extract(src):
    out = {}
    for tag, f in (("n", "Si_gpaw_noLFE.dat"), ("l", "Si_gpaw_withLFE.dat")):
        d = np.loadtxt(os.path.join(src, f), skiprows=1)
        sel = (d[:, 1] > 3400) & (d[:, 1] < 4100)
        out[tag] = d[sel]
    assert np.allclose(out["n"][:, :2], out["l"][:, :2])
    np.savez(os.path.join(HERE, "we21_6_raw.npz"), om=out["n"][:, 0], k=out["n"][:, 1],
             e1n=out["n"][:, 2], e2n=out["n"][:, 3], e1l=out["l"][:, 2], e2l=out["l"][:, 3])


def main():
    r = np.load(os.path.join(HERE, "we21_6_raw.npz"))
    om, k = r["om"], r["k"]
    ks = np.unique(k)
    oms = np.unique(om)
    k0 = ks[np.argmin(abs(ks - Q0))]
    w0 = oms[np.argmin(abs(oms - 10.0))]
    print(f"q0 = alpha m_e = {Q0:.1f} eV; table k nodes in [3.4, 4.1] keV: {len(ks)}; omega nodes {len(oms)}, "
          f"top {oms.max():.1f} eV")
    print(f"node nearest (q0, 10 eV): k = {k0:.2f} eV (k/q0 = {k0/Q0:.4f}), omega = {w0:.4f} eV")
    i = np.where((k == k0) & (om == w0))[0][0]
    e1n, e2n, e1l, e2l = r["e1n"][i], r["e2n"][i], r["e1l"][i], r["e2l"][i]
    L_rpa = e2n / (e1n**2 + e2n**2)
    L_lf = e2l / (e1l**2 + e2l**2)
    pref = 2 * k0**2 / E2
    print(f"head eps_00 = {e1n:.4f} + {e2n:.4f} i;  eps_mac = {e1l:.4f} + {e2l:.4f} i")
    print(f"eps2_IP = {e2n:.4f}; L_RPA = {L_rpa:.4f}; L_LF = {L_lf:.4f}")
    print(f"2q^2/e^2 = {pref:.4e} eV^2")
    for name, x in (("S_IP", e2n), ("S_RPA", L_rpa), ("S_LF", L_lf)):
        print(f"{name} = {pref*x:.4e} eV^2 per volume;  Omega*S = {pref*x*OMEGA_CELL:.4e} eV^-1 per cell")
    print(f"Omega = {OMEGA_CELL:.4e} eV^-3 = {A_SI**3/4:.3f} A^3")
    dX = L_lf / L_rpa - 1
    print(f"delta_X = L_LF/L_RPA - 1 = {dX:+.4f}")
    print(f"IP/LF = {e2n/L_lf:.3f}  (screening factor of the node, LF/IP = {L_lf/e2n:.3f})")
    print(f"EPM (Sect. 8.8) S_LF = {S_EPM:.3e}; ratio table/EPM = {pref*L_lf/S_EPM:.3f}; EPM delta_X = {DX_EPM}")
    # f-sum at k0
    m = k == k0
    o = om[m]; srt = np.argsort(o); o = o[srt]
    Llf = (r["e2l"][m] / (r["e1l"][m]**2 + r["e2l"][m]**2))[srt]
    Lrp = (r["e2n"][m] / (r["e1n"][m]**2 + r["e2n"][m]**2))[srt]
    fs = 0.5 * np.pi * WP_VAL**2
    print(f"f-sum fraction below {o.max():.1f} eV at k0: LF {np.trapezoid(o*Llf, o)/fs:.3f}, RPA {np.trapezoid(o*Lrp, o)/fs:.3f}")
    j = np.searchsorted(o, 10.0)
    L10 = np.interp(10.0, o, Llf)
    print(f"L_LF at k0 on the omega nodes {o[j-1]:.4f}, {o[j]:.4f} eV: {Llf[j-1]:.4f}, {Llf[j]:.4f}; linear at 10 eV "
          f"{L10:.4f}, S_LF(10 eV) = {pref*L10:.4e} eV^2, ratio to EPM {pref*L10/S_EPM:.3f}")
    e2i = np.interp(10.0, o, r["e2n"][m][srt])
    Lr10 = np.interp(10.0, o, Lrp)
    print(f"linear at 10 eV: S_IP = {pref*e2i:.4e} (EPM 1.7e8), S_RPA = {pref*Lr10:.4e}, LF/IP = {L10/e2i:.3f} "
          f"(EPM 0.29), delta_X = {L10/Lr10-1:+.3f}")
    print("package metadata (DarkELF data/Si/Si.yaml, same commit): E_gap = 1.11 eV, e0 = 3.6 eV (pair energy), "
          "omegap = 16.6 eV; omega node spacing near 1.1 eV: "
          f"{oms[np.searchsorted(oms, 1.1)] - oms[np.searchsorted(oms, 1.1) - 1]:.3f} eV")
    print("specification tolerances quoted in Sect. 21.6 (App. E.16, E.24; acceptance values, not computed): "
          "symmetry-forbidden parts < 1e-3 of the allowed ones; f-sum of loss functions within 2 %; "
          "smallest eigenvalue of S_ab >= -1e-6 of its trace; Kramers-Kronig residual < 1 %; "
          "cascade moments to 1e-9")
    # direction spread: nodes within +-50 eV of k0 at w0
    near = ks[abs(ks - k0) <= 50]
    vals = []
    for kk in near:
        j = np.where((k == kk) & (om == w0))[0][0]
        vals.append(r["e2l"][j] / (r["e1l"][j]**2 + r["e2l"][j]**2))
    vals = np.array(vals)
    print(f"nodes within 50 eV of k0: k = {np.round(near,1).tolist()}; L_LF = {np.round(vals,4).tolist()}; "
          f"spread (max-min)/mean = {(vals.max()-vals.min())/vals.mean():.3f}")
    # sizes
    nq, nd, nw = round(25 / 0.1), 30, round(50 / 0.05)
    npts = nq * nd * nw
    print(f"E.16 grid: {nq} x {nd} x {nw} = {npts:.3e} points; 12 functions in double precision = "
          f"{12*8*npts/1e6:.0f} MB")
    npair = 1000 * 4 * 56
    print(f"pairs per point (10^3 k, 4 x 56 bands) = {npair:.3e}; full pair list = {npair*npts:.3e} numbers = "
          f"{8*npair*npts/1e12:.1f} TB per coupling row")
    nb = 20
    print(f"seed binned in {nb} electron-share bins: {nb*npts:.2e} numbers = {8*nb*npts/1e9:.1f} GB per row pair")
    nl = 400 * round(1 / 1e-4) * 3
    print(f"E.17 lattice table: 400 x {round(1/1e-4)} x 3 = {nl:.2e} values = {8*nl/1e6:.0f} MB per quantity")
    print(f"E.16 omega step 50 meV vs 1.3 meV x^3 range at the PA edge: ratio {50/1.3:.0f}")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "extract":
        extract(sys.argv[2])
    else:
        main()
