"""Worked example 13.4 (we:13-external) and the silicon numbers of Sect. 13.4: the external screening factor
1/eps1(q, omega)^2 of the phonon-assisted loss function at |q| = 1 keV, its variation across the off-shell window, the
frequency shift omega -> omega - omega_Q, and the dielectric function at the pinned pair momentum q + Q = k_c that
enters the applied-potential limit of the pair channel.  Also the exchange estimate of the adiabatic local-density
source term.

Data (published, not computed here)
  S. Knapen, J. Kozaczuk, T. Lin, Phys. Rev. D 104, 015031 (2021), arXiv:2101.08275, Sect. III B: dielectric function of
  silicon in the random-phase approximation from GPAW, without local fields (eps = eps_00, the head) and with local fields
  (eps = eps_mac = 1/(eps^-1)_00).  Files data/Si/Si_gpaw_noLFE.dat and data/Si/Si_gpaw_withLFE.dat of the DarkELF package
  (arXiv:2104.12786; github.com/tongylin/DarkELF, commit 2f01cd5501d8f9c0dfdc3a011973dab9da718498), the same files that
  figscripts/ch10/si_elf_reduce.py reduces for Sect. 10.2.  Columns omega [eV], |q| [eV], eps1, eps2.  The raw momenta are
  lengths |q + G| on the calculation's mesh, so each mesh point is one direction; the example quotes the RANGE over the mesh
  points in a window of |q| (a modelling choice, named in the text), not a fit.
  omega is interpolated linearly between the raw energies 1.043 and 1.263 eV (and 1.263, 1.486 eV for 1.47 eV).

Other inputs (book values)
  eps_inf = 11.7, measured (Sect. 4.4; Franta et al. 2017).
  k_c = 0.85 (2 pi / a), a = 5.431 A (Sects. 3.3, 13.1): |k_c| = 0.983 A^-1 = 1.94 keV, the pinned pair momentum.
  Window at |q| = 1.0 keV: onset Eg + omega_TA = 1.184 eV, window edge Eg + 0.30 eV = 1.47 eV (WE 13.3, fig13_3.log).
  omega_TA(k_c - q) = 13.98 meV (WE 13.3).
  Valence density of silicon: 32 electrons per conventional cell a^3 (8 atoms x 4).
  Exchange kernel of the gas f_x = -e^2/(4 k_F^2) (Sect. 4.6); third derivative k_x = -(2/3) f_x / n (derived in App. D.36).

Usage:  python we13_4.py [DIR]   with DIR holding Si_gpaw_noLFE.dat and Si_gpaw_withLFE.dat.  Without DIR (or if the
files are absent) the reduced cache eps13_4.npz next to this script is used.  Output: we13_4.log.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "eps13_4.npz")
LOG = os.path.join(HERE, "we13_4.log")

HBARC = 1973.269804  # eV A
A_SI = 5.431         # A
EPS_INF = 11.7
OMEGAS = (1.184, 1.20, 1.47)     # eV: onset at 1 keV, working point, window edge (WE 13.3)
OMEGA_TA = 0.01398               # eV (WE 13.3)
QWIN = (900.0, 1100.0)           # eV: mesh points quoted for |q| = 1 keV
PWIN = (1850.0, 2050.0)          # eV: mesh points quoted for the pinned pair momentum 1.94 keV


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
    return om, k, e1, e2


def build_cache(src):
    om, k, e1n, e2n = load(os.path.join(src, "Si_gpaw_noLFE.dat"))
    om2, k2, e1l, e2l = load(os.path.join(src, "Si_gpaw_withLFE.dat"))
    assert np.allclose(om, om2) and np.allclose(k, k2)
    keep_k = (k < 2600.0)
    keep_o = (om < 2.5)
    np.savez_compressed(CACHE, omega=om[keep_o], q=k[keep_k],
                        e1n=e1n[np.ix_(keep_o, keep_k)], e2n=e2n[np.ix_(keep_o, keep_k)],
                        e1l=e1l[np.ix_(keep_o, keep_k)], e2l=e2l[np.ix_(keep_o, keep_k)])


def main():
    if len(sys.argv) > 1 and os.path.exists(os.path.join(sys.argv[1], "Si_gpaw_noLFE.dat")):
        build_cache(sys.argv[1])
    d = np.load(CACHE)
    om, k = d["omega"], d["q"]
    e1n, e2n, e1l, e2l = d["e1n"], d["e2n"], d["e1l"], d["e2l"]

    def at(e, j, w):
        return float(np.interp(w, om, e[:, j]))

    out = []
    p = out.append
    p("Sect. 13.4 / WE 13.4: silicon dielectric function in the phonon-assisted window (KKL 2101.08275, GPAW RPA)")
    p("q -> 0, omega = 0:  eps_00 = %.2f (no local fields), eps_mac = %.2f (local fields); measured eps_inf = %.1f"
      % (e1n[0, 0], e1l[0, 0], EPS_INF))
    p("   RPA below measured by %.0f %% and %.0f %%" % (100 * (1 - e1n[0, 0] / EPS_INF), 100 * (1 - e1l[0, 0] / EPS_INF)))

    def block(win, label):
        js = np.where((k >= win[0]) & (k <= win[1]))[0]
        p("")
        p("%s: mesh points |q| = %s eV" % (label, ", ".join("%.0f" % k[j] for j in js)))
        p("  static (omega = 0): eps_00 = %s ; eps_mac = %s" % (" ".join("%.2f" % e1n[0, j] for j in js),
                                                            " ".join("%.2f" % e1l[0, j] for j in js)))
        res = {}
        for w in OMEGAS:
            a = [at(e1n, j, w) for j in js]
            b = [at(e1l, j, w) for j in js]
            c = [at(e2n, j, w) for j in js]
            p("  omega = %.3f eV: eps1_00 = %s ; eps1_mac = %s ; max eps2 = %.4f"
              % (w, " ".join("%.3f" % x for x in a), " ".join("%.3f" % x for x in b), max(c)))
            res[w] = (np.array(a), np.array(b))
        return js, res

    js, r = block(QWIN, "|q| = 1 keV")
    a, b = r[1.20]
    p("  at 1.20 eV: eps1_00 %.2f-%.2f, eps1_mac %.2f-%.2f" % (a.min(), a.max(), b.min(), b.max()))
    p("  1/eps1^2: head %.4f-%.4f ; macroscopic %.4f-%.4f" % (1 / a.max()**2, 1 / a.min()**2, 1 / b.max()**2, 1 / b.min()**2))
    p("  unscreened / screened = eps1^2: head %.0f-%.0f ; macroscopic %.0f-%.0f"
      % (a.min()**2, a.max()**2, b.min()**2, b.max()**2))
    p("  optical 1/eps_inf^2 = %.4f ; (eps_inf/eps1)^2 head %.2f-%.2f, macroscopic %.2f-%.2f"
      % (1 / EPS_INF**2, (EPS_INF / a.max())**2, (EPS_INF / a.min())**2, (EPS_INF / b.max())**2, (EPS_INF / b.min())**2))
    p("  head local-field change (eps1_00/eps1_mac)^2 per point: %s" % " ".join("%.3f" % x for x in (a / b)**2))
    a0, b0 = r[1.184]
    a1, b1 = r[1.47]
    p("  window 1.184 -> 1.47 eV: change of 1/eps1^2: head %s %% ; macroscopic %s %%"
      % (" ".join("%.1f" % x for x in 100 * ((a0 / a1)**2 - 1)), " ".join("%.1f" % x for x in 100 * ((b0 / b1)**2 - 1))))
    # logarithmic slope and the frequency shift omega -> omega - omega_TA
    i5, i6 = 5, 6
    for j in js:
        s_n = np.log(e1n[i6, j] / e1n[i5, j]) / np.log(om[i6] / om[i5])
        s_l = np.log(e1l[i6, j] / e1l[i5, j]) / np.log(om[i6] / om[i5])
        dfrac = s_n * OMEGA_TA / 1.20
        p("  |q| = %.0f: dln eps1/dln omega = %.3f (head), %.3f (mac); eps1(omega)/eps1(omega - omega_TA) - 1 = %.2e,"
          " in L %.2e" % (k[j], s_n, s_l, dfrac, 2 * dfrac))

    js, r = block(PWIN, "pair momentum q + Q = k_c (1.94 keV)")
    a, b = r[1.20]
    p("  at 1.20 eV: eps1_00 %.2f-%.2f, eps1_mac %.2f-%.2f" % (a.min(), a.max(), b.min(), b.max()))
    p("  applied-potential factor 1/eps1^2: head %.3f-%.3f ; macroscopic %.3f-%.3f"
      % (1 / a.max()**2, 1 / a.min()**2, 1 / b.max()**2, 1 / b.min()**2))
    p("  all: %.3f-%.3f" % (min(1 / a.max()**2, 1 / b.max()**2), max(1 / a.min()**2, 1 / b.min()**2)))

    # pinned momentum and the adiabatic local-density estimate
    kc = 0.85 * 2 * np.pi / A_SI
    n_val = 32.0 / A_SI**3
    kF = (3 * np.pi**2 * n_val) ** (1.0 / 3.0)
    ratio = (kc / (2 * kF)) ** 2
    p("")
    p("k_c = %.4f A^-1 = %.0f eV" % (kc, kc * HBARC))
    p("valence density %.4f A^-3, k_F = %.3f A^-1 ; |f_x / v_C(k_c)| = (k_c/2k_F)^2 = %.4f ; (2/3) of it = %.4f"
      % (n_val, kF, ratio, 2 * ratio / 3))
    txt = "\n".join(out)
    print(txt)
    with open(LOG, "w") as f:
        f.write(txt + "\n")


if __name__ == "__main__":
    main()
