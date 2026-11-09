"""GAP-EF-v2: deterministic moment solver for the energy-only reduction of WP5 (W3) (GAP-EF-v2 (H-EF1)-(H-EF7)).
v2: adds the deposit D = H_< - H_> (independent route to Cov(H_<, H_>), REF-GAP-EF-A K10). Code names Phi = 3-body phase space
(written P_t, fraktur P, in the return; v1 Phi_t renamed, NOTATION W5).
No Monte Carlo: the exact first and second moment recursions of the branching process, by quadrature on an energy grid.
Units E_g = 1. A carrier of type t (0 = electron, 1 = hole) has kinetic energy x >= 0 above its band edge.
  ii : x >= theta_t:  t(x) -> t(x1) + t(x2) + tbar(x3),  x1 + x2 + x3 = x - 1,  density rho_t rho_t rho_tbar / Phi_t
       (random-k, constant matrix element: the Alig-Bloom-Struck 'scattering-rate' assumption)
  ph : t(x) -> t(x - w), w = omega_0/E_g, rate ratio R_t(x) = Gamma_ph/Gamma_ii = lam rho_t(x - w)/Phi_t(x - 1),
       lam = A/E_g^3 (R&K 2004.10709 Eq. (8) when rho = sqrt)
  x < theta_t: terminal, the residual x goes to heat.
Additive deposits Y with (d_ii, d_ph, d_term(x)): N = (1, 0, 0), residual heat R = (0, 0, x), phonon heat P = (0, w, 0).
Subtrees of the three ii products are independent (WP5 (B2)); the recursion is the first-step analysis of WP5 (W3)."""
import numpy as np

class Cascade:
    def __init__(self, lam, w, X=40.0, h=0.02, a=(0.5, 0.5), W=(None, None), theta=(1.0, 1.0),
                 hole_delta=False, phonon=True, sets=("N", "R", "P", "H", "R2", "C", "Re", "Rh", "R2e", "R2h", "Ce", "Ch")):
        self.h = h; K = int(round(X / h)) + 1; self.K = K
        x = np.arange(K) * h; self.x = x
        self.nG = int(round(1.0 / h)); self.nw = max(1, int(round(w / h))) if phonon else 1
        self.w = self.nw * h
        self.lam = lam if phonon else 0.0
        rho = []
        for t in (0, 1):
            if hole_delta and t == 1:
                r = np.zeros(K); r[0] = 1.0 / h
            else:
                r = x ** a[t]
                if W[t] is not None:
                    r = np.where(x <= W[t], r, 0.0)
            rho.append(r)
        self.rho = rho; self.delta = (False, hole_delta)
        c = lambda f, g: np.convolve(f, g)[:K] * h
        self.D = [c(rho[0], rho[1]), c(rho[1], rho[0])]          # rho_t * rho_tbar
        self.E = [c(rho[0], rho[0]), c(rho[1], rho[1])]          # rho_t * rho_t
        self.Phi = [c(self.D[0], rho[0]), c(self.D[1], rho[1])]  # rho_t * rho_t * rho_tbar
        self.nth = [max(self.nG, int(round(theta[0] / h))), max(self.nG, int(round(theta[1] / h)))]
        self.p = [np.zeros(K), np.zeros(K)]
        for t in (0, 1):
            for n in range(self.nth[t], K):
                q = n - self.nG; k = n - self.nw
                if self.Phi[t][q] <= 0: continue
                ph = 1.0 if self.delta[t] else rho[t][k]
                self.p[t][n] = 1.0 / (1.0 + self.lam * ph / self.Phi[t][q])
        self.res = {}
        deps = {"N": (1.0, 0.0, 0, False), "R": (0.0, 0.0, 1, False), "P": (0.0, self.w, 0, False), "H": (0.0, self.w, 1, False),
                "D": (0.0, -self.w, 1, False),   # H_< - H_>: Cov = [Var H - Var D]/4, independent of Var R, Var P
                "R2": (0.0, 0.0, 2, True),    # sum of squared terminal residuals (renewal estimate)
                "C": (0.0, 0.0, -1, True)}    # number of terminal carriers
        for tt, lab in ((0, "e"), (1, "h")):   # type-resolved terminal statistics (renewal estimate per carrier type)
            deps["R" + lab] = (0.0, 0.0, 1, True, tt); deps["R2" + lab] = (0.0, 0.0, 2, True, tt); deps["C" + lab] = (0.0, 0.0, -1, True, tt)
        for name in sets:
            d = deps[name]
            self.res[name] = self._moments(d[0], d[1], d[2], first_only=d[3], ttype=d[4] if len(d) > 4 else None)

    def _moments(self, dii, dph, term, first_only=False, ttype=None):
        K, h, nG, nw, rho = self.K, self.h, self.nG, self.nw, self.rho
        def dterm(x, t=None):
            if ttype is not None and t != ttype: return 0.0
            return {0: 0.0, 1: x, 2: x * x, -1: 1.0}[term]
        m = [np.zeros(K), np.zeros(K)]; s = [np.zeros(K), np.zeros(K)]
        P = [np.zeros(K), np.zeros(K)]; S = [np.zeros(K), np.zeros(K)]
        H = [[np.zeros(K), np.zeros(K)], [np.zeros(K), np.zeros(K)]]   # H[a][b] = (rho_a m_a) * rho_b
        def dot(f, g, q):
            return h * np.dot(f[:q + 1], g[q::-1])
        for n in range(K):
            xn = n * h
            for t in (0, 1):
                tb = 1 - t
                if n < self.nth[t]:
                    m[t][n] = dterm(xn, t); s[t][n] = dterm(xn, t) ** 2
                    continue
                q = n - nG; Phi = self.Phi[t][q]; p = self.p[t][n]; k = n - nw
                if p == 0.0:          # Phi_t(x - 1) = 0 at the threshold: phonon branch only
                    m[t][n] = dph + m[t][k]
                    s[t][n] = dph ** 2 + 2 * dph * m[t][k] + s[t][k]
                    continue
                sm = (2 * dot(P[t], self.D[t], q) + dot(P[tb], self.E[t], q)) / Phi
                Mii = dii + sm
                m[t][n] = p * Mii + (1 - p) * (dph + m[t][k])
                if not first_only:
                    ss = (2 * dot(S[t], self.D[t], q) + dot(S[tb], self.E[t], q)) / Phi
                    cr = (dot(P[t], H[t][tb], q) + 2 * dot(P[t], H[tb][t], q)) / Phi
                    Sii = dii ** 2 + 2 * dii * sm + ss + 2 * cr
                    s[t][n] = p * Sii + (1 - p) * (dph ** 2 + 2 * dph * m[t][k] + s[t][k])
            for t in (0, 1):
                P[t][n] = rho[t][n] * m[t][n]; S[t][n] = rho[t][n] * s[t][n]
            if not first_only:
                for a_ in (0, 1):
                    for b in (0, 1):
                        H[a_][b][n] = dot(P[a_], rho[b], n)
        return m, s

    def var(self, name, t=0):
        m, s = self.res[name]; return s[t] - m[t] ** 2

    def asym(self, t=0, frac=0.5):
        """eps, F, b from a linear fit of the pair-number mean and variance on omega in [frac X, X];
        seed = one carrier of type t at energy x with its sibling at the band edge, omega = 1 + x, N = 1 + N_sub."""
        x = self.x; sel = x >= frac * x[-1]; om = 1.0 + x[sel]
        m, s = self.res["N"]
        A = np.vstack([om, np.ones_like(om)]).T
        sm, b = np.linalg.lstsq(A, 1.0 + m[t][sel], rcond=None)[0]
        sv, c = np.linalg.lstsq(A, (s[t] - m[t] ** 2)[sel], rcond=None)[0]
        eps = 1.0 / sm
        return eps, sv * eps, b

    def decomposition(self, t=0, frac=0.5):
        """Asymptotic slopes per unit omega of Var R, Var P, 2 Cov(R,P) and Var H, plus the renewal estimate."""
        x = self.x; sel = x >= frac * x[-1]; om = 1.0 + x[sel]
        A = np.vstack([om, np.ones_like(om)]).T
        sl = lambda y: np.linalg.lstsq(A, y[sel], rcond=None)[0][0]
        vR, vP, vH = sl(self.var("R", t)), sl(self.var("P", t)), sl(self.var("H", t))
        vN = sl(self.var("N", t))
        mR, mR2, mC, mP = (sl(self.res[k][0][t]) for k in ("R", "R2", "C", "P"))
        eps = 1.0 / sl(self.res["N"][0][t] + 0.0)
        r1 = mR / mC; r2 = mR2 / mC; sig2 = r2 - r1 ** 2            # per terminal carrier (2 per pair)
        Pc = mP / mC                                                   # mean phonon heat per carrier
        vt = 0.0                                                       # per-type terminal-residual variances, one e and one h per pair
        for lab in ("e", "h"):
            ct = sl(self.res["C" + lab][0][t]); r1t = sl(self.res["R" + lab][0][t]) / ct; r2t = sl(self.res["R2" + lab][0][t]) / ct
            vt += (r2t - r1t ** 2) * ct * eps
        F_ren = (vt + 2 * self.w * Pc) / eps ** 2                      # renewal (final-state, uncorrelated, Poisson phonons)
        Cov2_direct = 0.5 * (vH - sl(self.var("D", t))) * eps if "D" in self.res else float("nan")
        return dict(eps=eps, F=vN * eps, F_from_H=vH * eps, VR=vR * eps, VP=vP * eps, Cov2=(vH - vR - vP) * eps, Cov2_direct=Cov2_direct,
                    rbar=r1, sig_r=np.sqrt(sig2), Pc=Pc, F_ren=F_ren, carriers_per_pair=mC * eps)

    def energy_residual(self, t=0):
        if "R" not in self.res: return float("nan")
        x = self.x; sel = x >= 2
        tot = self.res["N"][0][t] + self.res["R"][0][t] + self.res["P"][0][t]
        return np.max(np.abs(x[sel] - tot[sel]) / x[sel])
