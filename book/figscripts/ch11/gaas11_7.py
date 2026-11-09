"""GaAs one-phonon nuclear response resolved in the direction of q, for Sect. 11.7 (lattice part of the GaAs daily modulation).
Phonons: matdyn.x interpolation of the DFPT force constants of Sect. 5.5 (figscripts/ch11/gaas11_2.py, no new first-principles
run).  Weight per direction, coupling c_kappa = A_kappa (nucleon number):
   w1(q, qhat) = sum_nu |sum_kappa A_kappa e^{i q.tau_kappa} qhat.e*_{kappa nu}(q) / sqrt(M_kappa)|^2 / (2 omega_nu)   (eq:11.1-S1, omega-integrated)
q unreduced (all branches, Umklapp included).  Cubic-harmonic components on a 32 x 64 Gauss-Legendre x phi grid; output
gaas11_7.npz with s_l(q)/s_0(q), l = 4, 6, 8.  Check: 48 x 96 at three q.
"""
import os
import sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gaas11_2 as G  # noqa: E402
import aniso11 as AN  # noqa: E402

HBARC = 1973.269804
unit = 2 * np.pi * HBARC / G.A_ANG          # eV per (2 pi/a)
# q_BZ of GaAs (sphere of the zone volume), primitive cell a^3/4
QBZ = (6 * np.pi**2 / (G.A_ANG**3 / 4))**(1 / 3) * HBARC / 1e3      # keV


def comps(qk, nt, nphi, tag):
    qh, wq = AN.sphere_grid(nt, nphi)
    qs = np.concatenate([qk_ * 1e3 / unit * qh for qk_ in qk])
    w, e = G.run_matdyn(qs, tag)
    amp = G.nucleon_amplitude(qs, w, e)
    w1 = (np.abs(amp)**2 / (2 * np.maximum(w, 1e-6))).sum(1).reshape(len(qk), len(qh))
    return {l: np.sum(wq * AN.ycub(l, qh) * w1, axis=1) for l in (0, 4, 6, 8)}


if __name__ == "__main__":
    qk = QBZ * np.geomspace(0.1, 25, 40)
    c = comps(qk, 32, 64, "aniso_32x64")
    for i in range(0, len(qk), 3):
        print("GaAs one phonon q = %6.2f keV (%5.2f q_BZ): S4/S0 = %+.4f S6/S0 = %+.4f S8/S0 = %+.4f"
              % (qk[i], qk[i] / QBZ, c[4][i] / c[0][i], c[6][i] / c[0][i], c[8][i] / c[0][i]))
    chk = QBZ * np.array([0.3, 2.0, 5.0])
    a = comps(chk, 32, 64, "aniso_chk32")
    b = comps(chk, 48, 96, "aniso_chk48")
    for i, x in enumerate(chk):
        print("grid check q = %.2f keV: S4/S0 = %+.4f (32x64), %+.4f (48x96)" % (x, a[4][i] / a[0][i], b[4][i] / b[0][i]))
    np.savez(os.path.join(HERE, "gaas11_7.npz"), q=qk, qbz=QBZ, s=np.array([c[l] for l in (0, 4, 6, 8)]))
    print("q_BZ(GaAs) = %.3f keV; wrote gaas11_7.npz" % QBZ)
