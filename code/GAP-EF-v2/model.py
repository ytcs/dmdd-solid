"""GAP-EF-v2 model layer: grid choice (omega_0 on the grid), material runs, calibration of the single parameter A.
v2 fix (REF-GAP-EF-B 2.7): grid() now enforces its tolerance. v1 returned the best grid below Nmax silently, so CsI
(w = 0.00163) ran with n_w/N = 2.04 w. Nmax is raised to ceil(2/w) automatically, and a grid outside tol raises."""
import numpy as np
from cascade import Cascade

def grid(w, Nmin=60, Nmax=400, tol=0.01, nwmin=2):
    """Smallest points-per-E_g N >= Nmin with n_w/N within tol of w (n_w >= nwmin phonon steps); returns (N, n_w, rel. err).
    Raises ValueError if no such grid exists up to max(Nmax, ceil(2 nwmin/w))."""
    best = None
    Nmax = max(Nmax, int(np.ceil(2.0 * nwmin / w)))
    for N in range(Nmin, Nmax + 1):
        nw = max(nwmin, int(round(w * N)))
        err = abs(nw / N - w) / w
        if err < tol:
            return (N, nw, err)
        if best is None or err < best[2]:
            best = (N, nw, err)
    raise ValueError(f"grid(): no grid with |n_w/N - w|/w < {tol} up to N = {Nmax} (best {best})")

def run(A, Eg, om0, theta=1.0, a=0.5, Wv=None, X=40.0, N=None, frac=0.5, decomp=False, Nmax=400, nwmin=2):
    """A [eV^3], Eg, om0, Wv [eV]; theta = E_th^ii/E_g (both carriers); returns eps [eV], F, b (+ decomposition)."""
    lam = A / Eg ** 3; w = om0 / Eg
    if N is None:
        N, nw, err = grid(w, Nmax=Nmax, nwmin=nwmin)
    else:
        nw = max(1, int(round(w * N)))
    h = 1.0 / N; w_eff = nw * h
    sets = ("N", "R", "P", "H", "D", "R2", "C", "Re", "Rh", "R2e", "R2h", "Ce", "Ch") if decomp else ("N", "R", "P")
    c = Cascade(lam, w_eff, X=X, h=h, a=(a, a), W=(None, None if Wv is None else Wv / Eg), theta=(theta, theta), sets=sets)
    eps, F, b = c.asym(0, frac)
    out = dict(eps=eps * Eg, eps_over_Eg=eps, F=F, b=b, lam=lam, w=w, w_eff=w_eff, N=N, Eres=c.energy_residual(0))
    if decomp:
        out.update({k: v for k, v in c.decomposition(0, frac).items() if k not in ("eps", "F")})
    return out

def calibrate_A(eps_meas, Eg, om0, theta=1.0, lo=1.0, hi=20.0, tol=1e-4, **kw):
    """Bisection on A so that the model eps equals eps_meas (the only calibrated parameter)."""
    while run(lo, Eg, om0, theta, **kw)["eps"] > eps_meas: lo /= 4
    while run(hi, Eg, om0, theta, **kw)["eps"] < eps_meas: hi *= 4
    while hi - lo > tol * lo:
        mid = 0.5 * (lo + hi); fm = run(mid, Eg, om0, theta, **kw)["eps"] - eps_meas
        if fm < 0: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)
