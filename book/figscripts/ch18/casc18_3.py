"""Cascade distributions of Sect. 18.3: P_casc(N_eh | E_e, E_h) of the energy-only cascade, seeded with the electron-hole
shares of seeds18_3.py, the step model and the Ramanathan-Kurinsky split distributions.

Output: casc18_3.json (curves for fig18_3.py and limit18_3a.py) and casc18_3.log (every number printed in Sect. 18.3).

Cascade model: the energy-only random-k cascade of Sect. 18.1 with the one silicon set of Chap. 18 (si_cascade18.py):
  E_g = 1.160 eV (123 K), omega_AB = 63 meV, theta_ii = 1, parabolic densities of states rho_t(x) ~ x^(1/2), hole
  density of states cut at the valence bandwidth W_h = 12 eV, ratio of phonon to impact-ionization rates
  Gamma_ph/Gamma_ii = A_AB rho_t(x - omega_AB)/Phi_t(x - E_g) with Phi_t = rho_t * rho_t * rho_tbar (= (105/2pi)... for
  the uncut case, Eq. (8) of arXiv:2004.10709), A_AB = 5.703 eV^3, the continuum calibration on
  eps_eh = 3.749 eV (si_cascade18.log). Impact ionization splits x - E_g among (t, t, tbar) with density rho_t rho_t rho_tbar / Phi_t.
Generating function: for a carrier of type t at energy x, G_t(x; s) = <s^(number of impact ionizations in its subtree)>,
  obeying G_t(x; s) = p_t(x) s <G_t G_t G_tbar> + (1 - p_t(x)) G_t(x - omega_AB; s), G_t = 1 below theta_ii E_g
  (Sect. 18.1). A pair seed (E_e, E_h) gives P_casc(N | E_e, E_h) = [s^N] s G_e(E_e; s) G_h(E_h; s) (eq:18.3-pcasc).
  Coefficients are extracted at the NZ roots of unity (exact when P(N >= NZ) = 0; NZ = 32, and pair() refuses any seed
  with <N> + 10 sigma_N > NZ); Gat refuses energies above the grid top X E_g instead of extrapolating.
Discretisation (units of E_g): grid h = 1/NG, NG = 184, so that omega_AB/E_g = 0.054310 is 10 grid steps to 0.07 %
  (omega_AB on the grid is 63.04 meV). The densities enter as exact cell masses int rho over each cell (hole cut exact);
  p_t uses the closed form of Phi_t; the three-fold convolutions are done by FFT in blocks of one gap. Check printed:
  NG = 92 (5 steps per phonon) changes every printed probability by less than the stated amount.
Seeds (all at the same electronic energy omega, E_e + E_h = omega - E_g):
  DM     : dark-matter kick at q0 = alpha m_e along [100], independent-particle pair weights (seeds18_3.py);
  photon : optical limit, the q -> 0 seed of absorbed photons and dark photons (seeds18_3.py);
  RET10  : the screened (RPA + local fields, out-state) seed at 10 eV of Worked example 8.7 (we8_pairs, NK = 24),
           20 bins in x; used only as a check of the screening-free DM seed at 10 eV;
  RK beta: the split distributions of 2004.10709 Eq. (7), P(x|alpha) ~ x^(alpha-1)(1-x)^(alpha-1) on the electron share
           x = E_e/(omega - E_g): alpha -> 0 ("all to one": x = 0 or 1 with probability 1/2 each), alpha = 1 ("uniform"),
           alpha -> infinity ("equal split", x = 1/2); seeds with a hole above W_h are dropped (their constraint E_h < W);
  step   : N = 1 + floor((omega - E_g)/eps_eh), eps_eh = 3.749 eV (eq:1.5-step).
  The band-model seeds are tabulated against the excess energy omega - E_g of the model bands (gap 0.82 eV) and used
  here at the same excess energy above E_g = 1.160 eV (seeds18_3.py states this mapping).
Run: python3 casc18_3.py (about 1 min).
"""
import os
import json
import time
from math import gamma
import numpy as np
from scipy import fft as sf
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from si_cascade18 import A_AB, EG_SI, OM_SI, BH_SI, EPS_MEAS

HERE = os.path.dirname(os.path.abspath(__file__))
EG, WAB, WH, AAB, EPS = EG_SI, OM_SI, BH_SI, A_AB, EPS_MEAS
THETA, NZ = 1.0, 32
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def masses(a, h, K, W=None):
    up = (np.arange(K) + .5) * h
    lo = np.maximum(up - h, 0.0)
    if W is not None:
        up, lo = np.minimum(up, W), np.minimum(lo, W)
    return (up ** (a + 1) - lo ** (a + 1)) / (a + 1)


def phi(t, y, W):
    """Phi_e = rho_e*rho_e*rho_h with the hole <= W; Phi_h = rho_h*rho_h*rho_e (uncut on physical rows, y < W). a = 1/2."""
    y = np.asarray(y, float)
    if t == 1 or W is None:
        return (gamma(1.5) ** 3 / gamma(4.5)) * y ** 3.5
    m = np.minimum(y, W)
    return (np.pi / 8) * (y * y * (2 / 3) * m ** 1.5 - 2 * y * (2 / 5) * m ** 2.5 + (2 / 7) * m ** 3.5)


class Casc:
    def __init__(s, NG=184, X=22.0):
        s.NG, s.h = NG, 1.0 / NG
        s.K = int(round(X * NG)) + 1
        s.x = np.arange(s.K) * s.h
        s.nw = int(round(WAB / EG * NG))
        s.lam, s.W = AAB / EG ** 3, WH / EG
        s.mu = (masses(.5, s.h, s.K), masses(.5, s.h, s.K, s.W))
        s.Kh = min(s.K, int(np.floor(s.W * NG + .5)) + 1)
        s.nth = int(round(THETA * NG))
        s.p = []
        for t in (0, 1):
            y = s.x - 1.0
            ok = (y > 0) & (s.x >= THETA - 1e-12)
            ph = np.zeros(s.K)
            ph[ok] = phi(t, y[ok], s.W if t == 0 else None)
            pt = np.zeros(s.K)
            pt[ok] = 1.0 / (1.0 + s.lam * np.sqrt(np.maximum(s.x[ok] - s.nw * s.h, 0)) / ph[ok])
            s.p.append(pt)
        s.z = np.exp(2j * np.pi * np.arange(NZ) / NZ)[:, None]
        s._solve()

    def _solve(s):
        K, nG, nw = s.K, s.NG, s.nw
        G = [np.ones((NZ, K), complex), np.ones((NZ, K), complex)]
        b = s.nth
        while b < K:
            e = min(b + nG, K)
            q0, q1 = b - nG, e - nG
            L = sf.next_fast_len(3 * b)
            FF = [sf.fft(s.mu[t][None, :b] * G[t][:, :b], L, axis=1) for t in (0, 1)]
            U = [sf.fft(s.mu[t][:b], L) for t in (0, 1)]
            I = []
            for t in (0, 1):
                tb = 1 - t
                S = np.real(sf.ifft(U[t] * U[t] * U[tb]))[q0:q1]
                c = sf.ifft(FF[t] * FF[t] * FF[tb], axis=1)[:, q0:q1]
                ok = S > 1e-300
                I.append(np.where(ok[None, :], c / np.where(ok, S, 1)[None, :], 1.0))
            for lo in range(b, e, nw):
                hi = min(lo + nw, e)
                for t in (0, 1):
                    h2 = hi if t == 0 else min(hi, s.Kh)
                    if h2 <= lo:
                        continue
                    p = s.p[t][None, lo:h2]
                    G[t][:, lo:h2] = p * s.z * I[t][:, lo - b:h2 - b] + (1 - p) * G[t][:, lo - nw:h2 - nw]
            b = e
        s.G = G

    def Gat(s, t, E):
        """G_t at kinetic energies E (eV), linear interpolation on the grid; holes above W_h held at W_h."""
        xx = np.atleast_1d(np.asarray(E, float)) / EG
        if np.any(xx > (s.K - 1) * s.h + 1e-12):     # no extrapolation beyond the grid top X E_g
            raise ValueError("energy %.2f eV above the grid top %.2f eV" % (xx.max() * EG, (s.K - 1) * s.h * EG))
        if t == 1:
            xx = np.minimum(xx, (s.Kh - 1) * s.h)
        u = xx / s.h
        i = np.clip(np.floor(u).astype(int), 0, s.K - 2)
        f = u - i
        return s.G[t][:, i] * (1 - f) + s.G[t][:, i + 1] * f            # (NZ, n)

    def pair(s, Ee, Eh, wts=None):
        """P(N) for pair seeds (arrays Ee, Eh in eV) with weights wts (normalized here); N counts the primary pair."""
        Ee, Eh = np.atleast_1d(Ee), np.atleast_1d(Eh)
        wts = np.ones(len(Ee)) if wts is None else np.asarray(wts, float)
        g = (s.z * s.Gat(0, Ee) * s.Gat(1, Eh)) @ (wts / wts.sum())     # (NZ,)
        P = np.real(np.fft.fft(g)) / NZ
        n = np.arange(NZ)
        m = (n * P).sum()
        sd = np.sqrt(max((n * n * P).sum() - m * m, 0.0))
        if NZ < m + 10 * sd:                            # aliasing guard: NZ >= <N> + 10 sigma_N
            raise ValueError("NZ = %d below <N> + 10 sigma = %.1f" % (NZ, m + 10 * sd))
        return P


def moments(P):
    n = np.arange(len(P))
    m = (n * P).sum()
    return m, (n * n * P).sum() - m * m


def share_seed(hist, exc, nsub=8):
    """electron share histogram (nbin bins on [0, 1]) -> (Ee, Eh, w) sampled at nsub points per bin, total exc (eV)."""
    hist = np.asarray(hist, float)
    nb = len(hist)
    xs = (np.arange(nb * nsub) + 0.5) / (nb * nsub)
    w = np.repeat(hist / nsub, nsub)
    return xs * exc, (1 - xs) * exc, w


def beta_seed(alpha, exc, n=4000):
    """2004.10709 Eq. (7) on the electron share, with its constraint E_h < W_h on the seed hole (their Sect. IV A, step 1):
    weights with a hole above W_h are dropped and the rest renormalized."""
    xs = (np.arange(n) + 0.5) / n
    if alpha == 0:
        Ee, Eh, w = np.array([exc, 0.0]), np.array([0.0, exc]), np.array([0.5, 0.5])
    elif alpha == np.inf:
        Ee, Eh, w = np.array([exc / 2]), np.array([exc / 2]), np.array([1.0])
    else:
        Ee, Eh, w = xs * exc, (1 - xs) * exc, xs ** (alpha - 1) * (1 - xs) ** (alpha - 1)
    w = np.where(Eh <= WH, w, 0.0)
    return Ee, Eh, w


def step(omega):
    return 1 + int(np.floor((omega - EG) / EPS)) if omega >= EG else 0


def tv(P, Q):
    n = max(len(P), len(Q))
    P = np.pad(P, (0, n - len(P)))
    Q = np.pad(Q, (0, n - len(Q)))
    return 0.5 * np.abs(P - Q).sum()


def delta(n):
    P = np.zeros(NZ)
    P[n] = 1.0
    return P


if __name__ == "__main__":
    t0 = time.time()
    seeds = json.load(open(os.path.join(HERE, "seeds18_3.json")))
    seeds16 = json.load(open(os.path.join(HERE, "seeds18_3_NK16.json")))
    exc_grid = np.array(seeds["exc"])
    c = Casc()
    say(f"Energy-only cascade, E_g = {EG} eV, omega_AB = {WAB} eV (grid {c.nw * c.h * EG * 1e3:.2f} meV), A_AB = {AAB} eV^3, "
        f"W_h = {WH} eV, theta_ii = {THETA}; NG = {c.NG}, NZ = {NZ}; solve {time.time() - t0:.1f} s")

    # --- checks: normalization, positivity, forced region, one-sided asymptotics against Sect. 18.2 ---
    om = np.arange(21.0, 21.0 + 1e-9, 1.0)
    P = c.pair(0.9 * EG, 0.5 * EG)
    say(f"forced region (E_e = 0.9 E_g, E_h = 0.5 E_g): P(1) = {P[1]:.12f}")
    worst_norm, worst_neg = 0.0, 0.0
    for e in np.linspace(0.1, 20.0, 60):
        P = c.pair(e, 0.0)
        worst_norm = max(worst_norm, abs(P.sum() - 1))
        worst_neg = min(worst_neg, P.min())
    say(f"one-sided seeds up to 20 eV: max |sum P - 1| = {worst_norm:.1e}, min P = {worst_neg:.1e}")

    # --- seeded distributions over omega (Limit Check 18.3a) ---
    curves = dict(omega=[], DM={}, photon={}, uniform={}, all1={}, equal={}, step={}, DM16={})
    for k in curves:
        if isinstance(curves[k], dict):
            curves[k] = dict(mean=[], var=[], P=[], tv=[])
    for j, ex in enumerate(exc_grid):
        omega = ex + EG
        curves["omega"].append(omega)
        res = {}
        res["DM"] = c.pair(*share_seed(seeds["hist"]["DM"][j], ex))
        res["DM16"] = c.pair(*share_seed(seeds16["hist"]["DM"][j], ex))
        res["photon"] = c.pair(*share_seed(seeds["hist"]["OPT"][j], ex))
        res["uniform"] = c.pair(*beta_seed(1.0, ex))
        res["all1"] = c.pair(*beta_seed(0, ex))
        res["equal"] = c.pair(*beta_seed(np.inf, ex))
        res["step"] = delta(step(omega))
        for k, P in res.items():
            m, v = moments(P)
            curves[k]["mean"].append(m)
            curves[k]["var"].append(v)
            curves[k]["P"].append(P[:12].tolist())
            curves[k]["tv"].append(tv(P, res["DM"]))
    for k in curves:
        if isinstance(curves[k], dict):
            for kk in curves[k]:
                curves[k][kk] = np.array(curves[k][kk])
    omg = np.array(curves["omega"])
    say("\nomega  | mean: DM  photon uniform all1 equal step | TV to DM: photon uniform all1 equal step | DM(NK16) TV")
    for j in range(len(omg)):
        if abs((omg[j] - EG) % 1.0) < 1e-6 or abs(omg[j] - 10.0) < 0.13 or abs(omg[j] - 5.0) < 0.13:
            say(f"{omg[j]:6.2f} | {curves['DM']['mean'][j]:.3f} {curves['photon']['mean'][j]:.3f} {curves['uniform']['mean'][j]:.3f} "
                f"{curves['all1']['mean'][j]:.3f} {curves['equal']['mean'][j]:.3f} {curves['step']['mean'][j]:.0f} | "
                f"{curves['photon']['tv'][j]:.3f} {curves['uniform']['tv'][j]:.3f} {curves['all1']['tv'][j]:.3f} "
                f"{curves['equal']['tv'][j]:.3f} {curves['step']['tv'][j]:.3f} | {curves['DM16']['tv'][j]:.3f}")

    # validity: last omega above which TV(model, DM) stays <= 0.1, and mean ratio within 10 %
    def last_cross(y, thr=0.1):
        bad = np.where(y > thr)[0]
        return omg[bad[-1] + 1] if len(bad) and bad[-1] + 1 < len(omg) else (omg[0] if not len(bad) else None)
    for k in ("photon", "uniform", "all1", "equal", "step"):
        r = np.abs(curves[k]["mean"] / curves["DM"]["mean"] - 1)
        say(f"{k:7s}: TV to DM <= 0.1 for omega >= {last_cross(curves[k]['tv'])} eV (grid 0.25 eV); max TV {curves[k]['tv'].max():.3f} "
            f"at {omg[np.argmax(curves[k]['tv'])]:.2f} eV; |mean/mean_DM - 1| <= 0.1 for omega >= {last_cross(r)} eV, max {r.max():.3f} "
            f"at {omg[np.argmax(r)]:.2f} eV")
    for k in ("photon", "uniform", "step"):
        sel = omg > 15
        say(f"{k:7s}: max TV to DM for omega > 15 eV: {curves[k]['tv'][sel].max():.3f}; max |mean ratio - 1| "
            f"{np.abs(curves[k]['mean'][sel] / curves['DM']['mean'][sel] - 1).max():.3f}")
    say(f"seed k-grid check: max TV(DM NK24, DM NK16) over the grid = {curves['DM16']['tv'].max():.3f} at "
        f"{omg[np.argmax(curves['DM16']['tv'])]:.2f} eV")

    # --- omega = 10 eV in detail (Fig. 18.3) ---
    j10 = int(np.argmin(np.abs(omg - 10.0)))
    ex10 = 10.0 - EG
    say(f"\nomega = 10 eV (excess {ex10:.2f} eV; band-model shares interpolated linearly between the excess energies "
        f"{exc_grid[int(np.searchsorted(exc_grid, ex10)) - 1]:.2f} and {exc_grid[int(np.searchsorted(exc_grid, ex10))]:.2f} eV); "
        f"step model N = {step(10.0)}")
    P10 = {}
    def at10(hist):
        # interpolate the share histogram in excess energy to exactly omega = 10 eV
        jj = int(np.searchsorted(exc_grid, ex10)) - 1
        f = (ex10 - exc_grid[jj]) / (exc_grid[jj + 1] - exc_grid[jj])
        return (1 - f) * np.array(hist[jj]) + f * np.array(hist[jj + 1])
    P10["DM"] = c.pair(*share_seed(at10(seeds["hist"]["DM"]), ex10))
    P10["photon"] = c.pair(*share_seed(at10(seeds["hist"]["OPT"]), ex10))
    w8 = json.load(open(os.path.join(HERE, "..", "ch08", "we8_pairs_Si_NK24_gauss0.1_eta0.1.json")))["10"]["hist"]
    P10["RET10"] = c.pair(*share_seed(w8["RET"], ex10, nsub=16))
    P10["IP10"] = c.pair(*share_seed(w8["IP"], ex10, nsub=16))
    P10["OPT10"] = c.pair(*share_seed(w8["OPT"], ex10, nsub=16))
    P10["uniform"] = c.pair(*beta_seed(1.0, ex10))
    P10["all1"] = c.pair(*beta_seed(0, ex10))
    P10["equal"] = c.pair(*beta_seed(np.inf, ex10))
    P10["step"] = delta(step(10.0))
    for k, P in P10.items():
        m, v = moments(P)
        say(f"  {k:7s}: P(1..6) = " + " ".join(f"{P[n]:.3f}" for n in range(1, 7)) +
            f" | mean {m:.3f}, var {v:.3f}, var/mean {v / m:.3f} | TV to DM {tv(P, P10['DM']):.3f}")
    say(f"  screening at the band-model excess 9.18 eV (we8_pairs, 20 bins): TV(RET10, IP10) = {tv(P10['RET10'], P10['IP10']):.3f}; "
        f"TV(OPT10, IP10) = {tv(P10['OPT10'], P10['IP10']):.3f}")
    # law of total variance for the DM seed: Var = <v_e + v_h> + Var_seed(m_e + m_h)
    Ee, Eh, w = share_seed(at10(seeds["hist"]["DM"]), ex10)
    w = w / w.sum()
    mm, vv = [], []
    for a, b in zip(Ee, Eh):
        m_, v_ = moments(c.pair(a, b))
        mm.append(m_)
        vv.append(v_)
    mm, vv = np.array(mm), np.array(vv)
    Mbar = (w * mm).sum()
    say(f"  DM seed: <N> = {Mbar:.3f}; Var N = {(w * vv).sum() + (w * (mm - Mbar) ** 2).sum():.3f} = mean cascade variance "
        f"{(w * vv).sum():.3f} + seed variance {(w * (mm - Mbar) ** 2).sum():.3f}")
    for a in (0.5, 0.25, 0.0):
        m_, v_ = moments(c.pair(a * ex10, (1 - a) * ex10))
        say(f"  share x = {a:.2f} (E_e = {a * ex10:.2f} eV): <N> = {m_:.3f}, Var = {v_:.3f}")
    Ee, Eh, w = share_seed(at10(seeds["hist"]["photon"] if False else seeds["hist"]["OPT"]), ex10)
    w = w / w.sum()
    mm = np.array([moments(c.pair(a, b))[0] for a, b in zip(Ee, Eh)])
    say(f"  photon seed: seed variance {(w * (mm - (w * mm).sum()) ** 2).sum():.3f}")

    # --- omega = 5 eV (Worked example 18.3) ---
    ex5 = 5.0 - EG
    say(f"\nomega = 5 eV (excess {ex5:.3f} eV); step model N = {step(5.0)} (eps_eh = 3.749 eV); with eps_eh = 3.6 eV: "
        f"{1 + int(np.floor(ex5 / 3.6))}")
    def p_ii(t, E):
        return np.interp(E / EG, c.x, c.p[t])
    # no-ionization probability of a lone carrier: product over its phonon ladder
    for E0 in (ex5, ex5 / 2, 3.0, 2.0):
        Es = E0 - WAB * np.arange(0, int(E0 / WAB) + 2)
        Es = Es[Es >= THETA * EG]
        for t, nm in ((0, "electron"), (1, "hole")):
            pr = np.prod(1 - p_ii(t, Es))
            Pc = c.pair(E0, 0.0) if t == 0 else c.pair(0.0, E0)
            say(f"  lone {nm} at {E0:.3f} eV: {len(Es)} phonon steps above E_g, prod(1 - p_ii) = {pr:.4f}; "
                f"solver P(N = 1) = {Pc[1]:.4f}, P(2) = {Pc[2]:.4f}, P(3) = {Pc[3]:.5f}")
    say("  p_ii(E) (electron) at E = 1.5, 2, 2.5, 3, 3.5, 3.84 eV: " +
        " ".join(f"{p_ii(0, E):.4f}" for E in (1.5, 2.0, 2.5, 3.0, 3.5, ex5)))
    say("  p_ii(E) (hole)     at E = 1.5, 2, 2.5, 3, 3.5, 3.84 eV: " +
        " ".join(f"{p_ii(1, E):.4f}" for E in (1.5, 2.0, 2.5, 3.0, 3.5, ex5)))
    # CSDA estimate of the no-ionization probability: exp(-int dE p/(1-p) / omega_AB)
    for E0 in (ex5,):
        Eq = np.linspace(EG, E0, 4001)
        pq = p_ii(0, Eq)
        I = np.trapezoid(pq / (1 - pq), Eq) / WAB
        say(f"  CSDA (continuous slowing down) at {E0:.3f} eV: exp(-{I:.4f}) = {np.exp(-I):.4f}")
    j5 = int(np.searchsorted(exc_grid, ex5)) - 1
    f5 = (ex5 - exc_grid[j5]) / (exc_grid[j5 + 1] - exc_grid[j5])
    P5 = {}
    for k, hk in (("DM", "DM"), ("photon", "OPT")):
        h = (1 - f5) * np.array(seeds["hist"][hk][j5]) + f5 * np.array(seeds["hist"][hk][j5 + 1])
        P5[k] = c.pair(*share_seed(h, ex5))
        mE = (1 - f5) * seeds["mean"][hk]["Ee"][j5] + f5 * seeds["mean"][hk]["Ee"][j5 + 1]
        hh = h / h.sum()
        say(f"  {k} seed at 5 eV: <E_e> = {mE:.2f} eV of {ex5:.2f}; P(x > 1/2) = {hh[len(hh) // 2:].sum():.3f}; "
            f"P(x < 1/4 or > 3/4) = {hh[:len(hh) // 4].sum() + hh[3 * len(hh) // 4:].sum():.3f}")
    P5["uniform"] = c.pair(*beta_seed(1.0, ex5))
    P5["all1"] = c.pair(*beta_seed(0, ex5))
    P5["equal"] = c.pair(*beta_seed(np.inf, ex5))
    for k, P in P5.items():
        m, v = moments(P)
        say(f"  {k:7s}: P(1) = {P[1]:.4f}, P(2) = {P[2]:.4f}, P(3) = {P[3]:.5f} | mean {m:.4f}")

    # --- derived numbers quoted in the text ---
    m10 = moments(P10["DM"])[0]
    m5 = moments(P5["DM"])[0]
    say(f"\nderived: energy per pair at 10 eV (DM seed) 10/{m10:.3f} = {10 / m10:.2f} eV ({10 / m10 / EPS - 1:.4f} above eps_eh); step model overstates the mean by "
        f"{3 / m10 - 1:.3f}; at 5 eV 5/{m5:.3f} = {5 / m5:.2f} eV per pair")
    say(f"derived: two-pair threshold at 5 eV: step/cascade (DM) = 1/{P5['DM'][2]:.4f} = {1 / P5['DM'][2]:.2f}; "
        f"photon/DM two-pair probability = {P5['photon'][2] / P5['DM'][2]:.3f}; first impact-ionization channel at "
        f"(1 + theta_ii) E_g = {(1 + THETA) * EG:.3f} eV; step model's first step at E_g + eps_eh = {EG + EPS:.3f} eV")
    j20 = int(np.argmin(np.abs(omg - 20.16)))
    say(f"derived: DM seed at {omg[j20]:.2f} eV: mean {curves['DM']['mean'][j20]:.3f}, sigma_N = {np.sqrt(curves['DM']['var'][j20]):.3f} "
        f"(formula (F omega/eps)^(1/2) with F = 0.114: {np.sqrt(0.114 * omg[j20] / EPS):.3f}), "
        f"largest single-N probability {max(curves['DM']['P'][j20]):.3f}")

    # --- step model against the cascade: mean offset and where its single bin carries < 90 % ---
    say("\nstep model: mean over a period (omega - E_g)/eps + 1/2 against the one-sided asymptote omega/eps + b_N")
    xs = np.arange(20.0, 21.5 + 1e-9, 0.5)
    mo = [moments(c.pair(x * EG - EG, 0.0))[0] for x in xs]
    say(f"  E_g/eps_eh = {EG / EPS:.4f}; step offset 1/2 - E_g/eps_eh = {0.5 - EG / EPS:.4f}; "
        f"one-sided cascade <N> - omega/eps at omega = 20...21.5 E_g: " + " ".join(f"{m - x * EG / EPS:.3f}" for m, x in zip(mo, xs)))
    Pstep_hit = np.array([curves["DM"]["P"][j][step(o)] if step(o) < 12 else 0 for j, o in enumerate(omg)])
    say(f"  P_DM(N = N_step) at omega = 4.9, 6, 8, 10, 15, 20 eV: " +
        " ".join(f"{Pstep_hit[int(np.argmin(np.abs(omg - o)))]:.3f}" for o in (4.9, 6.0, 8.0, 10.0, 15.0, 20.0)))

    # --- fine omega grid (0.02 eV; seed shares interpolated linearly in excess energy between the 0.25 eV nodes) ---
    def hist_at(name, ex):
        jj = min(max(int(np.searchsorted(exc_grid, ex)) - 1, 0), len(exc_grid) - 2)
        f = np.clip((ex - exc_grid[jj]) / (exc_grid[jj + 1] - exc_grid[jj]), 0, 1)
        return (1 - f) * np.array(seeds["hist"][name][jj]) + f * np.array(seeds["hist"][name][jj + 1])
    fine = np.arange(EG + exc_grid[0], EG + exc_grid[-1] + 1e-9, 0.02)
    F = {k: [] for k in ("photon", "uniform", "all1", "equal", "step")}
    for o in fine:
        ex = o - EG
        PD = c.pair(*share_seed(hist_at("DM", ex), ex))
        F["photon"].append(tv(c.pair(*share_seed(hist_at("OPT", ex), ex)), PD))
        F["uniform"].append(tv(c.pair(*beta_seed(1.0, ex)), PD))
        F["all1"].append(tv(c.pair(*beta_seed(0, ex)), PD))
        F["equal"].append(tv(c.pair(*beta_seed(np.inf, ex)), PD))
        F["step"].append(tv(delta(step(o)), PD))
    F = {k: np.array(v) for k, v in F.items()}
    def first_above(y, thr=0.1):
        i = np.where(y > thr)[0]
        return fine[i[0]] if len(i) else None
    def last_above(y, thr=0.1):
        i = np.where(y > thr)[0]
        return fine[i[-1]] if len(i) else None
    say("\nfine grid (0.02 eV): TV to the DM-seeded cascade")
    for k in F:
        say(f"  {k:7s}: first omega with TV > 0.1: {first_above(F[k])}; last omega with TV > 0.1: {last_above(F[k])}; "
            f"max {F[k].max():.3f} at {fine[np.argmax(F[k])]:.2f} eV")
    env = np.maximum(F["uniform"], F["equal"])
    say(f"  envelope of the uniform and equal splits: TV <= 0.1 below {first_above(env):.2f} eV and above {last_above(env):.2f} eV")
    out_fine = dict(omega=fine.tolist(), **{k: v.tolist() for k, v in F.items()})

    # --- constant offset b_N of the mean at large omega, by seed type, with this grid's own pair energy ---
    cbig = Casc(X=46.0)
    xs_fit = np.arange(30.0, 44.0 + 1e-9, 0.5)
    m_one = np.array([moments(cbig.pair((xx - 1) * EG, 0.0))[0] for xx in xs_fit])
    slope, icpt = np.polyfit(xs_fit * EG, m_one, 1)
    eps_grid = 1.0 / slope
    say(f"\nconstant offset of the mean at large omega: this grid's own pair energy (slope of the one-sided mean over "
        f"30-44 E_g) eps = {eps_grid:.4f} eV; one-sided intercept b_N = {icpt:.4f}")
    say(f"  <N> - omega/eps at omega = 40, 42, 44 E_g with the grid's eps:")
    for nm, fn in (("one-sided", lambda ex: (np.array([ex]), np.array([0.0]), np.array([1.0]))),
                   ("uniform (hole <= W_h)", lambda ex: beta_seed(1.0, ex))):
        vals = []
        for xx in (40.0, 42.0, 44.0):
            ex = (xx - 1) * EG
            P = cbig.pair(*fn(ex))
            m, v = moments(P)
            vals.append((m - xx * EG / eps_grid, v / m, m - xx * EG / EPS))
        say(f"  {nm:22s}: " + " ".join(f"{a:.3f}" for a, b, c_ in vals) + "  (with 3.749 eV instead: " +
            " ".join(f"{c_:.3f}" for a, b, c_ in vals) + "; Var/mean " + " ".join(f"{b:.4f}" for a, b, c_ in vals) + ")")

    # --- grid check ---
    c2 = Casc(NG=92)
    d = 0.0
    for e in (3.0, 5.0, 8.84, 15.0):
        for a in (0.0, 0.5):
            d = max(d, np.abs(c.pair(a * e, (1 - a) * e) - c2.pair(a * e, (1 - a) * e)).max())
    say(f"\ngrid check: max |P(NG=184) - P(NG=92)| over seeds at 3, 5, 8.84, 15 eV = {d:.1e}")

    out = dict(omega=omg.tolist(), Eg=EG, eps=EPS)
    for k in ("DM", "photon", "uniform", "all1", "equal", "step"):
        out[k] = {kk: np.asarray(v).tolist() for kk, v in curves[k].items()}
    out["P10"] = {k: P[:10].tolist() for k, P in P10.items()}
    out["P5"] = {k: P[:10].tolist() for k, P in P5.items()}
    out["fine"] = out_fine
    json.dump(out, open(os.path.join(HERE, "casc18_3.json"), "w"))
    say(f"total {time.time() - t0:.0f} s")
    open(os.path.join(HERE, "casc18_3.log"), "w").write("\n".join(LOG) + "\n")
