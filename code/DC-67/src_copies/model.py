"""GAP-EF-v3 model layer: commensurate grids, value at the true omega_0 by interpolation in w, calibration of the single parameter A.
R17 FIX-GAP-EF-GRID (returns/R17/GAP-EF-v3-errata.md).  v2 solved every row at w_eff = n_w/N (|w_eff/w - 1| < 1%, grid()) and, for
theta_ii = 3/2 on an odd N, at theta_eff = h round(3N/2) (half to even) -- and reported the result as the value at (w, theta).
v3:
  * grid() is v2's search (smallest N >= Nmin with |n_w/N - w|/w < tol) restricted to N with N theta integer (theta = 3/2 -> N even);
    for theta = 1 it returns v2's N exactly, so the discretisation level (O(h), GAP-EF-v2-C5) is unchanged.
  * run() solves on that one grid h = 1/N at the commensurate nodes w_k = k/N, k in {n_w - 1, n_w, n_w + 1} (or {n_w, n_w+1, n_w+2}
    when n_w = 1), each an exact (strict) Cascade, and Lagrange-interpolates every output to the true w.  Same h for every node, so no
    discretisation mixing; the offset delta = wN - n_w is <= 0.01 n_w, interpolation error O(delta^3) (GAP-EF-v3-C3).
    If wN is an integer (to 1e-9) a single solve is made.
v2 fix kept (REF-GAP-EF-B 2.7): grid() enforces its tolerance and raises; Nmax raised to ceil(2 nwmin/w)."""
import numpy as np
from cascade import Cascade


def _int(v, tol=1e-9):
    return abs(v - round(v)) <= tol * max(1.0, abs(v))


def grid(w, Nmin=60, Nmax=400, tol=0.01, nwmin=2, theta=1.0):
    """Smallest N >= Nmin with N theta integer and |n_w/N - w|/w < tol (n_w >= nwmin); returns (N, n_w, rel. err).
    Raises ValueError if no such grid exists up to max(Nmax, ceil(2 nwmin/w))."""
    best = None
    Nmax = max(Nmax, int(np.ceil(2.0 * nwmin / w)))
    for N in range(Nmin, Nmax + 1):
        if not _int(N * theta):
            continue
        nw = max(nwmin, int(round(w * N)))
        err = abs(nw / N - w) / w
        if err < tol:
            return (N, nw, err)
        if best is None or err < best[2]:
            best = (N, nw, err)
    raise ValueError(f"grid(): no grid with |n_w/N - w|/w < {tol} and N theta integer up to N = {Nmax} (best {best})")


def nodes(w, N):
    """Commensurate interpolation nodes k (w_k = k/N) around w on the grid 1/N."""
    x = w * N
    if _int(x):
        return [int(round(x))]
    n = int(round(x))
    return [n - 1, n, n + 1] if n >= 2 else [1, 2, 3]


def lagrange(xs, ys, x):
    out = 0.0
    for i, xi in enumerate(xs):
        L = 1.0
        for j, xj in enumerate(xs):
            if j != i:
                L *= (x - xj) / (xi - xj)
        out = out + L * ys[i]
    return out


def _solve(lam, wk, X, h, a, Wv, Eg, theta, frac, decomp):
    sets = ("N", "R", "P", "H", "D", "R2", "C", "Re", "Rh", "R2e", "R2h", "Ce", "Ch") if decomp else ("N", "R", "P")
    c = Cascade(lam, wk, X=X, h=h, a=(a, a), W=(None, None if Wv is None else Wv / Eg), theta=(theta, theta), sets=sets)
    eps, F, b = c.asym(0, frac)
    o = dict(eps_over_Eg=eps, F=F, b=b, Eres=c.energy_residual(0))
    if decomp:
        o.update({k: v for k, v in c.decomposition(0, frac).items() if k not in ("eps", "F")})
    return o


def run(A, Eg, om0, theta=1.0, a=0.5, Wv=None, X=40.0, N=None, frac=0.5, decomp=False, Nmax=400, nwmin=2, order=None, w_override=None):
    """A [eV^3], Eg, om0, Wv [eV]; theta = E_th^ii/E_g (both carriers); returns eps [eV], F, b (+ decomposition) AT THE TRUE w.
    order: None = the nodes() rule (3 nodes, or 1 if exact); an int k uses the k nodes nearest w (GAP-EF-v3-C3 uses 2 and 5).
    w_override: solve at this w instead of om0/Eg (must then be commensurate with the grid; used for the v2-equivalent value)."""
    lam = A / Eg ** 3; w = om0 / Eg if w_override is None else w_override
    if N is None:
        N, nw, err = grid(om0 / Eg, Nmax=Nmax, nwmin=nwmin, theta=theta)
    elif not _int(N * theta):
        raise ValueError(f"run(): N = {N} does not make theta = {theta} commensurate")
    h = 1.0 / N
    ks = nodes(w, N)
    if order is not None and len(ks) > 1:
        c = int(round(w * N)); cand = sorted(range(max(1, c - order), c + order + 1), key=lambda k: (abs(k - w * N), k))
        ks = sorted(cand[:order])
    res = [_solve(lam, k / N, X, h, a, Wv, Eg, theta, frac, decomp) for k in ks]
    xs = [k / N for k in ks]
    out = {key: (lagrange(xs, [r[key] for r in res], w) if len(ks) > 1 else res[0][key]) for key in res[0]}
    out.update(eps=out["eps_over_Eg"] * Eg, lam=lam, w=w, w_nodes=xs, N=N, delta=w * N - int(round(w * N)),
               w_eff_v2=max(1, int(round(w * N))) / N, Eres=max(r["Eres"] for r in res))
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
