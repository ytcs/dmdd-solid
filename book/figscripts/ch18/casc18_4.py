"""Moment solver of the energy-only random-k cascade, used by the Sect. 18.4 scripts (table18_4.py, limit18_4a/b/c.py).

Model (Sects. 18.1-18.2; free-particle kernels of App. E.13, eq:E.13-ab).  Units E_g = 1.  A carrier of type t (0 electron,
1 hole) has kinetic energy x >= 0 above its band edge.
  impact ionization, x >= theta_ii:  t(x) -> t(x1) + t(x2) + tbar(x3),  x1 + x2 + x3 = x - 1,
      joint density rho_t(x1) rho_t(x2) rho_tbar(x3) / Phi_t(x - 1),  Phi_t = rho_t * rho_t * rho_tbar  (threefold convolution),
      rho_t(x) = x^a (a = 1/2: parabolic bands), the hole density cut at the valence width B_h when given (random final momenta,
      equal matrix elements: Alig, Bloom and Struck, as described by Nielsen and Fischetti, arXiv:2610.16949, Sect. II).
  phonon emission: t(x) -> t(x - w),  w = omega_AB/E_g,  rate ratio  Gamma_ph/Gamma_ii = lam rho_t(x - w)/Phi_t(x - 1),
      lam = A_AB/E_g^3.  For a = 1/2, Phi(y) = (2 pi/105) y^{7/2} and the ratio is Ramanathan and Kurinsky's Eq. (8),
      arXiv:2004.10709, A (105/2pi)(E - w)^{1/2}/(E - E_g)^{7/2}, with A_AB = A in eV^3.
  x < theta_ii: terminal; the residual x becomes heat.
The first and second moments of an additive deposit Y (d_ii per ionization, d_ph per phonon, d_term(x) at termination) obey the
first-step recursions of the branching process (sibling subtrees independent):
  m_t(x) = p [d_ii + <m(x1) + m(x2) + m(x3)>] + (1 - p) [d_ph + m_t(x - w)],
  s_t(x) = p [d_ii^2 + 2 d_ii <sum m> + <sum s> + 2 <sum_{i<j} m_i m_j>] + (1 - p) [d_ph^2 + 2 d_ph m_t(x - w) + s_t(x - w)],
with p = 1/(1 + Gamma_ph/Gamma_ii).  Every term is a one-dimensional convolution of quantities known at lower energy, so one upward
sweep solves the system.  Deposits: N (pair number, d_ii = 1), R (residual heat, d_term = x), P (phonon heat, d_ph = w).
Seed: one electron at x0 = omega - E_g with its hole at the band edge (residual 0); N = 1 + N_sub, so omega = N E_g + R + P on
every path.  eps_eh and F_eh are the slopes of the mean and variance of N in omega, fitted on [X/2, X].

Grid (commensurate): h = 1/N must divide E_g, theta_ii E_g and the phonon step, because the sweep reads x - E_g and x - w.  The
solver runs at the commensurate nodes w_k = k/N around the true w and interpolates every output to it (3-point Lagrange).  The
scheme converges as h^{3/2} with phonons (as h without); at N >= 60 the discretization error is <= 0.07 % in eps and F for silicon
(printed by table18_4.py).
"""
import numpy as np


def _divides(h, v, tol=1e-9):
    r = v / h
    return abs(r - round(r)) <= tol * max(1.0, abs(r))


class Cascade:
    def __init__(self, lam, w, X=40.0, h=0.02, a=0.5, Bh=None, theta=1.0, phonon=True, sets=("N", "R", "P")):
        for v in ([1.0, theta] + ([w] if phonon else [])):
            if not _divides(h, v):
                raise ValueError("grid h = %g does not divide %g" % (h, v))
        self.h = h
        K = int(round(X / h)) + 1
        self.K = K
        x = np.arange(K) * h
        self.x = x
        self.nG = int(round(1.0 / h))
        self.nw = max(1, int(round(w / h))) if phonon else 1
        self.w = self.nw * h
        self.lam = lam if phonon else 0.0
        rho = [x ** a, x ** a]
        if Bh is not None:
            rho[1] = np.where(x <= Bh, rho[1], 0.0)
        self.rho = rho
        c = lambda f, g: np.convolve(f, g)[:K] * h
        self.D = [c(rho[0], rho[1]), c(rho[1], rho[0])]
        self.E = [c(rho[0], rho[0]), c(rho[1], rho[1])]
        self.Phi = [c(self.D[0], rho[0]), c(self.D[1], rho[1])]
        self.nth = int(round(theta / h))
        self.p = [np.zeros(K), np.zeros(K)]
        for t in (0, 1):
            for n in range(self.nth, K):
                q = n - self.nG
                if self.Phi[t][q] <= 0:
                    continue
                self.p[t][n] = 1.0 / (1.0 + self.lam * rho[t][n - self.nw] / self.Phi[t][q])
        deps = {"N": (1.0, 0.0, 0), "R": (0.0, 0.0, 1), "P": (0.0, self.w, 0)}
        self.res = {k: self._moments(*deps[k]) for k in sets}

    def _moments(self, dii, dph, term):
        K, h, nG, nw, rho = self.K, self.h, self.nG, self.nw, self.rho
        m = [np.zeros(K), np.zeros(K)]
        s = [np.zeros(K), np.zeros(K)]
        P = [np.zeros(K), np.zeros(K)]
        S = [np.zeros(K), np.zeros(K)]
        H = [[np.zeros(K), np.zeros(K)], [np.zeros(K), np.zeros(K)]]

        def dot(f, g, q):
            return h * np.dot(f[:q + 1], g[q::-1])
        for n in range(K):
            xn = n * h
            for t in (0, 1):
                tb = 1 - t
                if n < self.nth:
                    d = xn if term == 1 else 0.0
                    m[t][n] = d
                    s[t][n] = d * d
                    continue
                q = n - nG
                p = self.p[t][n]
                k = n - nw
                if p == 0.0:
                    m[t][n] = dph + m[t][k]
                    s[t][n] = dph ** 2 + 2 * dph * m[t][k] + s[t][k]
                    continue
                Phi = self.Phi[t][q]
                sm = (2 * dot(P[t], self.D[t], q) + dot(P[tb], self.E[t], q)) / Phi
                ss = (2 * dot(S[t], self.D[t], q) + dot(S[tb], self.E[t], q)) / Phi
                cr = (dot(P[t], H[t][tb], q) + 2 * dot(P[t], H[tb][t], q)) / Phi
                m[t][n] = p * (dii + sm) + (1 - p) * (dph + m[t][k])
                s[t][n] = p * (dii ** 2 + 2 * dii * sm + ss + 2 * cr) + (1 - p) * (dph ** 2 + 2 * dph * m[t][k] + s[t][k])
            for t in (0, 1):
                P[t][n] = rho[t][n] * m[t][n]
                S[t][n] = rho[t][n] * s[t][n]
            for a_ in (0, 1):
                for b in (0, 1):
                    H[a_][b][n] = dot(P[a_], rho[b], n)
        return m, s

    def slopes(self, frac=0.5):
        """Asymptotic slopes in omega (units E_g) on [frac X, X] for a one-sided electron seed."""
        x = self.x
        sel = x >= frac * x[-1]
        om = 1.0 + x[sel]
        A = np.vstack([om, np.ones_like(om)]).T
        sl = lambda y: np.linalg.lstsq(A, y[sel], rcond=None)[0]
        mN, sN = self.res["N"]
        kN, bN = sl(1.0 + mN[0])
        kV, _ = sl(sN[0] - mN[0] ** 2)
        eps = 1.0 / kN
        out = dict(eps=eps, F=kV * eps, b=bN)
        if "R" in self.res:
            out["Rpair"] = sl(self.res["R"][0][0])[0] * eps      # residual heat per pair (two terminal carriers)
        if "P" in self.res:
            out["Ppair"] = sl(self.res["P"][0][0])[0] * eps      # phonon heat above threshold per pair
        return out


def _int(v, tol=1e-9):
    return abs(v - round(v)) <= tol * max(1.0, abs(v))


def grid(w, Nmin=60, Nmax=None, tol=0.01, theta=1.0):
    """Smallest N >= Nmin with N theta integer and the phonon step within 1 % of a whole number (>= 1) of grid steps."""
    Nmax = Nmax or max(600, int(np.ceil(3.0 / w)))
    for N in range(Nmin, Nmax + 1):
        if not _int(N * theta):
            continue
        nw = max(1, int(round(w * N)))
        if abs(nw / N - w) / w < tol:
            return N
    raise ValueError("no grid for w = %g" % w)


def lagrange(xs, ys, x):
    out = 0.0
    for i, xi in enumerate(xs):
        L = 1.0
        for j, xj in enumerate(xs):
            if j != i:
                L *= (x - xj) / (xi - xj)
        out = out + L * ys[i]
    return out


def run(A, Eg, om0, theta=1.0, a=0.5, Bh=None, X=40.0, N=None, sets=("N", "R", "P")):
    """A_AB [eV^3], Eg, om0, Bh [eV].  Returns eps [eV], F, residual and phonon heat per pair [eV] at the true w = om0/Eg."""
    lam = A / Eg ** 3
    w = om0 / Eg
    if N is None:
        N = grid(w, theta=theta)
    h = 1.0 / N
    xw = w * N
    ks = [int(round(xw))] if _int(xw) else ([int(round(xw)) - 1, int(round(xw)), int(round(xw)) + 1] if round(xw) >= 2 else [1, 2, 3])
    res = []
    for k in ks:
        c = Cascade(lam, k / N, X=X, h=h, a=a, Bh=None if Bh is None else Bh / Eg, theta=theta, sets=sets)
        res.append(c.slopes())
    xs = [k / N for k in ks]
    out = {key: (lagrange(xs, [r[key] for r in res], w) if len(ks) > 1 else res[0][key]) for key in res[0]}
    out["eps_over_Eg"] = out["eps"]
    out["eps"] = out["eps"] * Eg
    for key in ("Rpair", "Ppair"):
        if key in out:
            out[key] = out[key] * Eg
    out.update(lam=lam, w=w, N=N)
    return out


def run_nophonon(theta, a=0.5, X=25.0, hs=(0.01, 0.005)):
    """lambda -> 0 limit, linear Richardson on two grids (the scheme is O(h) without phonons)."""
    vals = []
    for h in hs:
        c = Cascade(0.0, 1.0, X=X, h=h, a=a, theta=theta, phonon=False, sets=("N", "R", "P"))
        vals.append(c.slopes())
    out = {k: 2 * vals[1][k] - vals[0][k] for k in vals[0]}
    out["raw"] = vals
    return out


def calibrate(eps_meas, Eg, om0, lo=3.0, hi=9.0, tol=2e-5, **kw):
    while hi - lo > tol * lo:
        mid = 0.5 * (lo + hi)
        if run(mid, Eg, om0, sets=("N",), **kw)["eps"] < eps_meas:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)
