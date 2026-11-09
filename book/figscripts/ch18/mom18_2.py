"""Shared solver for Sect. 18.2 (imported by fig18_2.py, limit18_2a.py, limit18_2b.py, limit18_2c.py, we18_2.py).

Energy-only carrier cascade of Sect. 18.1, solved for the first and second moments of additive deposits by the first-step
recursions of App. C.11 (eq:C.11-mean, eq:C.11-second), one upward sweep on an energy grid.  Units: E_g = 1.

Model (the random-k reduction with one phonon, as in Ramanathan and Kurinsky, arXiv:2004.10709, Sect. II and Eq. (8)):
  * a carrier of type t (0 = electron, 1 = hole) has kinetic energy x >= 0 above its band edge;
  * for x >= theta_ii it ionizes, t(x) -> t(x1) + t(x2) + tbar(x3), x1 + x2 + x3 = x - 1, with density
    rho_t(x1) rho_t(x2) rho_tbar(x3) / Phi_t(x - 1), Phi_t = rho_t * rho_t * rho_tbar (three-body phase space);
    rho_t(x) = x^a (a = 1/2: parabolic band), cut at the valence bandwidth W_h for holes if given;
  * or it emits one phonon of energy w = omega_AB/E_g, with rate ratio Gamma_ph/Gamma_ii = lam rho_t(x - w)/Phi_t(x - 1),
    lam = A_AB/E_g^3 (for a = 1/2, Phi = (2 pi/105) y^(7/2), which is Eq. (8) of 2004.10709);
  * below theta_ii the carrier is terminal; its kinetic energy x is the residual heat.
  Subtrees of the three products are independent (Sect. 18.1).
Deposits (d_ii, d_ph, d_term): N = (1, 0, 0); E_< = (0, 0, x); E_> = (0, w, 0); E_< + E_> = (0, w, x); E_< - E_> = (0, -w, x).
Terminal statistics per carrier type (first moments only): counts, sum of residuals, sum of squared residuals.

Grid: h = 1/Ngrid must divide 1, theta_ii and w; the phonon energy is reached by Lagrange interpolation in w over commensurate
nodes k/Ngrid on one grid (so h never mixes).  With phonons the error of the scheme falls as h^(3/2); without, as h.
Seed: one electron at x0 = omega - 1 with its hole at the band edge, omega = 1 + x0, N = 1 + N_sub.
eps_eh and F_eh are the slopes of <N> and Var N in omega, fitted over [X/2, X].
"""
import numpy as np


def _divides(h, v, tol=1e-9):
    r = v / h
    return abs(r - round(r)) <= tol * max(1.0, abs(r))


class Cascade:
    def __init__(self, lam, w, X=40.0, h=1 / 74, a=(0.5, 0.5), W=(None, None), theta=1.0, hole_delta=False,
                 phonon=True, decomp=True):
        for v in [1.0, theta] + ([w] if phonon else []):
            if not _divides(h, v):
                raise ValueError("grid h = %g does not divide %g" % (h, v))
        self.h = h
        K = int(round(X / h)) + 1
        self.K = K
        x = np.arange(K) * h
        self.x = x
        nG = int(round(1.0 / h))
        nw = max(1, int(round(w / h))) if phonon else 1
        self.w = nw * h if phonon else 0.0
        lam = lam if phonon else 0.0
        rho = []
        for t in (0, 1):
            if hole_delta and t == 1:
                r = np.zeros(K)
                r[0] = 1.0 / h
            else:
                r = x ** a[t]
                if W[t] is not None:
                    r = np.where(x <= W[t] + 1e-12, r, 0.0)
            rho.append(r)
        conv = lambda f, g: np.convolve(f, g)[:K] * h
        Dk = [conv(rho[0], rho[1]), conv(rho[1], rho[0])]   # rho_t * rho_tbar
        Ek = [conv(rho[0], rho[0]), conv(rho[1], rho[1])]   # rho_t * rho_t
        Phi = [conv(Dk[0], rho[0]), conv(Dk[1], rho[1])]
        nth = max(nG, int(round(theta / h)))
        p = [np.zeros(K), np.zeros(K)]
        for t in (0, 1):
            for n in range(nth, K):
                q = n - nG
                if Phi[t][q] <= 0:
                    continue
                ph = 1.0 if (hole_delta and t == 1) else rho[t][n - nw]
                p[t][n] = 1.0 / (1.0 + lam * ph / Phi[t][q])
        # deposits: (d_ii, d_ph, term kind, carrier type or None, second moment?)
        # term kind: 0 none, 1 residual x, 2 residual x^2, -1 count
        dep = [("N", 1.0, 0.0, 0, None, True)]
        if decomp:
            ww = self.w
            dep += [("R", 0.0, 0.0, 1, None, True), ("P", 0.0, ww, 0, None, True), ("H", 0.0, ww, 1, None, True),
                    ("D", 0.0, -ww, 1, None, True)]
            for tt, lab in ((0, "e"), (1, "h")):
                dep += [("C" + lab, 0.0, 0.0, -1, tt, False), ("R" + lab, 0.0, 0.0, 1, tt, False),
                        ("Q" + lab, 0.0, 0.0, 2, tt, False)]
        self.names = [d[0] for d in dep]
        nd = len(dep)
        dii = np.array([d[1] for d in dep])
        dph = np.array([d[2] for d in dep])
        sec = np.array([d[5] for d in dep])
        # terminal values per type
        term = np.zeros((2, nd, K))
        for i, d in enumerate(dep):
            for t in (0, 1):
                if d[4] is not None and d[4] != t:
                    continue
                term[t, i] = {0: 0 * x, 1: x, 2: x * x, -1: np.ones(K)}[d[3]]
        m = np.zeros((2, nd, K))
        s = np.zeros((2, nd, K))
        P = np.zeros((2, nd, K))
        S = np.zeros((2, nd, K))
        Hc = np.zeros((2, 2, nd, K))   # Hc[a, b] = (rho_a m_a) * rho_b
        for n in range(K):
            for t in (0, 1):
                tb = 1 - t
                if n < nth:
                    m[t, :, n] = term[t, :, n]
                    s[t, :, n] = term[t, :, n] ** 2
                    continue
                q = n - nG
                k = n - nw
                pt = p[t][n]
                if pt == 0.0:
                    if not phonon:          # threshold point with no phase space and no phonon: terminal
                        m[t, :, n] = term[t, :, n]
                        s[t, :, n] = term[t, :, n] ** 2
                    else:
                        m[t, :, n] = dph + m[t, :, k]
                        s[t, :, n] = dph ** 2 + 2 * dph * m[t, :, k] + s[t, :, k]
                    continue
                ph_ = Phi[t][q]
                Dr = Dk[t][q::-1]
                Er = Ek[t][q::-1]
                sm = h * (2 * P[t, :, :q + 1] @ Dr + P[tb, :, :q + 1] @ Er) / ph_
                ss = h * (2 * S[t, :, :q + 1] @ Dr + S[tb, :, :q + 1] @ Er) / ph_
                cr = h * (np.sum(P[t, :, :q + 1] * Hc[t, tb, :, q::-1], axis=1)
                          + 2 * np.sum(P[t, :, :q + 1] * Hc[tb, t, :, q::-1], axis=1)) / ph_
                if phonon and k >= 0:
                    mk, sk = m[t, :, k], s[t, :, k]
                else:
                    mk, sk = 0 * dii, 0 * dii
                m[t, :, n] = pt * (dii + sm) + (1 - pt) * (dph + mk)
                sii = dii ** 2 + 2 * dii * sm + ss + 2 * cr
                s[t, :, n] = np.where(sec, pt * sii + (1 - pt) * (dph ** 2 + 2 * dph * mk + sk), 0.0)
            for t in (0, 1):
                P[t, :, n] = rho[t][n] * m[t, :, n]
                S[t, :, n] = rho[t][n] * s[t, :, n]
            for a_ in (0, 1):
                for b in (0, 1):
                    Hc[a_, b, :, n] = h * (P[a_, :, :n + 1] @ rho[b][n::-1])
        self.m, self.s = m, s

    def mean(self, name, t=0):
        return self.m[t, self.names.index(name)]

    def var(self, name, t=0):
        i = self.names.index(name)
        return self.s[t, i] - self.m[t, i] ** 2

    def slopes(self, frac=0.5):
        """Asymptotic quantities from linear fits in omega = 1 + x over [frac X, X] (electron seed, hole at the edge)."""
        x = self.x
        sel = x >= frac * x[-1]
        om = 1.0 + x[sel]
        A = np.vstack([om, np.ones_like(om)]).T
        fit = lambda y: np.linalg.lstsq(A, y[sel], rcond=None)[0]
        sN, bN = fit(1.0 + self.mean("N"))
        eps = 1.0 / sN
        out = dict(eps=eps, bN=bN, F=fit(self.var("N"))[0] * eps)
        if "R" in self.names:
            for k_ in ("R", "P", "H", "D"):
                out["V" + k_] = fit(self.var(k_))[0] * eps
            out["Cov2"] = 0.5 * (out["VH"] - out["VD"])          # 2 Cov(E_<, E_>)/(E_g^2 <N>), independent route
            out["Cov2_rem"] = out["VH"] - out["VR"] - out["VP"]   # same from the remainder
            out["F_heat"] = out["VH"]
            vt, carriers = 0.0, 0.0
            res = 0.0
            for lab in ("e", "h"):
                ct = fit(self.mean("C" + lab))[0]
                r1 = fit(self.mean("R" + lab))[0] / ct
                r2 = fit(self.mean("Q" + lab))[0] / ct
                vt += (r2 - r1 ** 2) * ct * eps
                carriers += ct * eps
                res += r1 * ct * eps
            mP = fit(self.mean("P"))[0] * eps                     # mean phonon heat per pair (units E_g)
            out.update(sig2_res=vt, carriers_per_pair=carriers, resid_per_pair=res, phon_per_pair=mP,
                       F_ren=(vt + self.w * mP) / eps ** 2)
        return out


def lagrange(xs, ys, x0):
    out = 0.0
    for i, xi in enumerate(xs):
        L = 1.0
        for j, xj in enumerate(xs):
            if j != i:
                L *= (x0 - xj) / (xi - xj)
        out = out + L * ys[i]
    return out


def grid_for(w, Nmin=60, Nmax=400, tol=0.01):
    """Smallest N >= Nmin with |round(wN)/N - w|/w < tol (at least two phonon bins)."""
    Nmax = max(Nmax, int(np.ceil(4.0 / w)))
    for N in range(Nmin, Nmax + 1):
        nw = max(2, int(round(w * N)))
        if abs(nw / N - w) / w < tol:
            return N
    raise ValueError("no grid")


def run(lam, w, X=40.0, N=None, a=(0.5, 0.5), W=(None, None), theta=1.0, decomp=True, frac=0.5):
    """Asymptotic moments at the true phonon energy w (units E_g), by interpolation over commensurate nodes."""
    if N is None:
        N = grid_for(w)
    h = 1.0 / N
    c0 = w * N
    if abs(c0 - round(c0)) < 1e-9:
        ks = [int(round(c0))]
    else:
        n0 = int(round(c0))
        ks = [n0 - 1, n0, n0 + 1] if n0 >= 2 else [1, 2, 3]
    res = [Cascade(lam, k / N, X=X, h=h, a=a, W=W, theta=theta, decomp=decomp).slopes(frac) for k in ks]
    xs = [k / N for k in ks]
    out = {key: (lagrange(xs, [r[key] for r in res], w) if len(ks) > 1 else res[0][key]) for key in res[0]}
    out.update(N=N, nodes=xs)
    return out
