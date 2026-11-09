"""The one silicon parameter set of Chap. 18, shared by every Ch18 script, and its continuum calibration.
Run: python si_cascade18.py > si_cascade18.log  (about 3 min).  Imported by fig18_1.py, fig18_2.py, num18_2.py, limit18_2a/c.py,
casc18_3.py, table18_4.py, limit18_4a/c.py.

Model: the energy-only random-k cascade of Sects. 18.1-18.2 (free-particle densities of states rho_t ~ x^(1/2), threshold ratio
theta_ii = 1, one optical phonon, rate ratio Gamma_ph/Gamma_ii = A_AB rho_t(x - omega_AB)/Phi_t(x - E_g), Eq. (8) of Ramanathan and
Kurinsky, arXiv:2004.10709, with A_AB in eV^3).  Inputs, each with its source:
  E_g = 1.160 eV, silicon at 123 K, from Ramanathan and Kurinsky's Eq. (11): 1.1692 - 4.9e-4 T^2/(T + 655) at T = 123 K (App. E.13);
  omega_AB = 63 meV and the hole band width B_h = 12 eV (arXiv:2004.10709, Sects. II B and II A; App. E.13);
  calibration datum eps_eh = 3.749 +- 0.001 eV (and the test datum F_eh = 0.119 +- 0.002) at 123 K for 5.9 keV X-rays
  (Rodrigues et al., arXiv:2004.11499, abstract and Sect. 5).
A_AB is fixed by eps_eh alone, in the continuum limit of the moment recursions: each solver converges as h^(3/2) in the grid step
h (printed below), so the value at steps h and h/2 is extrapolated as f(h/2) + [f(h/2) - f(h)]/(2^(3/2) - 1).  The grid value of
an earlier calibration, 5.674 eV^3 at h = E_g/73, lies 0.5 % below the continuum value because the grid overestimates eps_eh by
0.06 % at fixed A_AB.
"""
import os
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

EG_SI = 1.160          # eV, 123 K
OM_SI = 0.063          # eV
BH_SI = 12.0           # eV
EPS_MEAS, DEPS_MEAS = 3.749, 0.001
F_MEAS, DF_MEAS = 0.119, 0.002
A_AB = 5.703           # eV^3, continuum calibration (main() below prints it)
LAM_SI = A_AB / EG_SI ** 3
W_SI = OM_SI / EG_SI
P_RICH = 1.5


def richardson(fh, fh2, p=P_RICH):
    return fh2 + (fh2 - fh) / (2.0 ** p - 1.0)


def _rich_dict(r1, r2, p=P_RICH):
    out = {}
    for k, v in r2.items():
        if k in r1 and isinstance(v, (float, np.floating)) and k not in ("N", "lam", "w"):
            out[k] = richardson(r1[k], v, p)
        else:
            out[k] = v
    return out


def casc_cont(A=A_AB, Eg=EG_SI, om=OM_SI, Bh=BH_SI, N=None, X=40.0, theta=1.0, a=0.5, sets=("N", "R", "P")):
    """casc18_4 solver at steps E_g/N and E_g/(2N), extrapolated to the continuum.  Returns eps [eV], F, Rpair, Ppair [eV], b."""
    import casc18_4 as C
    if N is None:
        N = C.grid(om / Eg, theta=theta)
    r1 = C.run(A, Eg, om, theta=theta, a=a, Bh=Bh, X=X, N=N, sets=sets)
    r2 = C.run(A, Eg, om, theta=theta, a=a, Bh=Bh, X=X, N=2 * N, sets=sets)
    out = _rich_dict(r1, r2)
    out["eps_over_Eg"] = out["eps"] / Eg
    out.update(N=N, lam=A / Eg ** 3, w=om / Eg, grid=(r1, r2))
    return out


def mom_cont(lam=LAM_SI, w=W_SI, Bh_over_Eg=BH_SI / EG_SI, N=74, X=40.0, theta=1.0, decomp=True):
    """mom18_2 solver (decomposition of F_eh) at steps E_g/N and E_g/(2N), extrapolated to the continuum (units E_g)."""
    from mom18_2 import run, grid_for
    if N is None:
        N = grid_for(w)
    W = (None, Bh_over_Eg)
    r1 = run(lam, w, X=X, N=N, W=W, theta=theta, decomp=decomp)
    r2 = run(lam, w, X=X, N=2 * N, W=W, theta=theta, decomp=decomp)
    out = _rich_dict(r1, r2)
    out.update(N=N, grid=(r1, r2))
    return out


def calibrate(eps=EPS_MEAS, lo=5.5, hi=5.9, tol=1e-5, **kw):
    """Bisection in A_AB on the continuum eps_eh (casc18_4 solver, pair-number moments only)."""
    while hi - lo > tol * lo:
        mid = 0.5 * (lo + hi)
        if casc_cont(mid, sets=("N",), **kw)["eps"] < eps:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    import casc18_4 as C
    t0 = time.time()
    print("Silicon parameter set: E_g = %.3f eV, omega_AB = %.0f meV, B_h = %.0f eV, theta_ii = 1, rho ~ x^(1/2)" %
          (EG_SI, 1e3 * OM_SI, BH_SI))
    Ac = calibrate()
    print("continuum calibration on eps_eh = %.3f eV: A_AB = %.4f eV^3 (used: A_AB = %.3f eV^3)" % (EPS_MEAS, Ac, A_AB))
    # convergence at the adopted constant, three grids of the casc18_4 solver
    N0 = C.grid(W_SI)
    rs = [C.run(A_AB, EG_SI, OM_SI, Bh=BH_SI, X=40.0, N=n) for n in (N0, 2 * N0, 4 * N0)]
    for n, r in zip((N0, 2 * N0, 4 * N0), rs):
        print("  grid E_g/%d: eps = %.5f eV, F = %.5f" % (n, r["eps"], r["F"]))
    d1, d2 = rs[0]["eps"] - rs[1]["eps"], rs[1]["eps"] - rs[2]["eps"]
    print("  successive differences in eps: %.2e, %.2e, ratio %.2f (2^(3/2) = 2.83: order h^(3/2))" % (d1, d2, d1 / d2))
    print("  extrapolated from E_g/%d, E_g/%d: eps = %.5f eV; from E_g/%d, E_g/%d: eps = %.5f eV" %
          (N0, 2 * N0, richardson(rs[0]["eps"], rs[1]["eps"]), 2 * N0, 4 * N0, richardson(rs[1]["eps"], rs[2]["eps"])))
    print("  at A_AB = 5.674 (the earlier grid calibration) the continuum gives eps = %.4f eV" %
          casc_cont(5.674, sets=("N",))["eps"])
    si = casc_cont(A_AB)
    print("continuum at A_AB = %.3f eV^3: lambda_AB = %.4f, w_AB = %.5f, eps = %.4f eV = %.4f E_g, F = %.5f, b_N = %.4f" %
          (A_AB, LAM_SI, W_SI, si["eps"], si["eps_over_Eg"], si["F"], si["b"]))
    print("  F against 0.119 +- 0.002: %.2f sigma; meas/model - 1 = %+.2f %%" %
          ((F_MEAS - si["F"]) / DF_MEAS, 100 * (F_MEAS / si["F"] - 1)))
    print("  eps = E_g + residual + phonon heat per pair: %.3f + %.4f + %.4f = %.4f eV; residual per carrier %.4f eV = %.4f E_g; "
          "phonons per pair above threshold %.2f" % (EG_SI, si["Rpair"], si["Ppair"], EG_SI + si["Rpair"] + si["Ppair"],
                                                      si["Rpair"] / 2, si["Rpair"] / 2 / EG_SI, si["Ppair"] / OM_SI))
    m = mom_cont()
    print("second solver (mom18_2, E_g/74 and E_g/148, extrapolated): eps = %.4f eV, F = %.5f, V_< = %.4f, V_> = %.4f, "
          "2V_<> = %.4f, phonon heat per pair %.4f eV, b_N = %.4f" % (m["eps"] * EG_SI, m["F"], m["VR"], m["VP"], m["Cov2"],
                                                                    m["phon_per_pair"] * EG_SI, m["bN"]))
    print("done in %.0f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
