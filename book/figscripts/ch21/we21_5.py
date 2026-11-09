"""Worked example 21.5: combining two silicon exposures with a shared theory nuisance.

Setup (illustrative searches, not real data)
  m_chi = 10 MeV, heavy mediator, book halo (App. A.8; [B] arXiv:2105.00599 Table 1), rho = 0.3 GeV/cm^3.
  Silicon response: tabulated crystal form factor of Essig et al. (arXiv:1509.01598, Eqs. (3.13), (3.17)) via
  figscripts/ch21/hib21.py; one-pair bin of the energy-only cascade of Sect. 18.3 (hib21.pbin,
  E_g = 1.160 eV, eps_eh = 3.749 eV), the bin that sets the standard-halo limit at 10 MeV in Sect. 21.2. r = expected count per kg yr per unit sigma_e.
  Exposure A: 1 kg yr, N_obs = 0, no background.  Exposure B: 4 kg yr, N_obs = 3, known background 2.5.
  Theory nuisance: one normalization of the silicon response, (1 + delta)^theta with delta = 0.25 (the size of the largest
  truncations of the silicon rate at 10 MeV, Sect. 10.10), standard-normal constraint exp(-theta^2/2) (eq:8.8-like).

Statistic and construction
  t(sigma) = -2 ln [L(sigma, theta_hathat(sigma)) / L(sigma_hat, theta_hat)], sigma_hat >= 0, set to 0 when
  sigma_hat > sigma (one-sided, App. C.14; Cowan et al. arXiv:1007.1727 Eq. (14)). Neyman construction by exact enumeration
  of the Poisson outcomes (n_A, n_B) <= 60: p(sigma) = P(t >= t_obs | sigma, theta = theta_hathat_obs(sigma)); the 90 %
  limit is the sigma with p = 0.10 (brentq). The constraint term is held fixed in the construction (a theory nuisance has no
  auxiliary measurement to repeat). Nuisances are profiled on a grid of 3201 points in [-8, 8] with parabolic refinement.
  Cases: each exposure alone; combined without nuisance; combined, one theta shared; combined, one theta per exposure;
  envelope (theta = -1 for the shared nuisance).
Run: python we21_5.py > we21_5.log   (about 1 min)
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.stats import poisson

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hib21 as HB  # noqa: E402
import halo21 as H  # noqa: E402

M = 10e6
NBIN = 1
r = HB.counts_eta(M, NBIN, lambda u: H.eta_shm(u) * HB.etatilde_unit(M))   # per kg yr per cm^2
U = 1e-42                                                                   # sigma unit, cm^2
rU = r * U
EXPO = {"A": 1.0, "B": 4.0}
NOBS = {"A": 0, "B": 3}
BKG = {"A": 0.0, "B": 2.5}
DELTA = 0.25
K = np.log(1 + DELTA)
NMAX = 60
TH = np.linspace(-8, 8, 3201)

print(f"m_chi = 10 MeV, cascade bin N = {NBIN}: r = {r:.4e} per kg yr per cm^2 = {rU:.4f} per kg yr per 1e-42 cm^2")
for x in "AB":
    print(f"  exposure {x}: {EXPO[x]:.0f} kg yr, N_obs = {NOBS[x]}, background {BKG[x]}; signal per 1e-42 cm^2 = {EXPO[x]*rU:.4f}")
print(f"  shared normalization nuisance delta = {DELTA}, ln(1 + delta) = {K:.4f}")


def nll_counts(mu, n):
    """2[mu - n ln mu] (Poisson -2 ln L up to n-dependent constants)."""
    mu = np.maximum(mu, 1e-300)
    return 2 * (mu - n * np.log(mu))


def prof_theta(fun):
    """min over theta of fun(theta) + theta^2 on the grid, with a parabolic refinement; returns (value, theta)."""
    v = fun(TH) + TH**2
    i = int(np.argmin(v))
    i = min(max(i, 1), len(TH) - 2)
    y0, y1, y2 = v[i - 1], v[i], v[i + 1]
    den = y0 - 2 * y1 + y2
    d = 0.5 * (y0 - y2) / den if den > 0 else 0.0
    h = TH[1] - TH[0]
    return y1 - 0.25 * (y0 - y2) * d, TH[i] + d * h


def make_nll(exps, mode):
    """-2 ln L at (sigma, outcome) after profiling the nuisance; mode in {"none", "shared", "indep"}."""
    def nll(sig, n):
        if mode == "none":
            return sum(nll_counts(sig * EXPO[x] * rU + BKG[x], n[x]) for x in exps), {}
        if mode == "shared":
            f = lambda th: sum(nll_counts(sig * EXPO[x] * rU * (1 + DELTA)**th + BKG[x], n[x]) for x in exps)
            v, th = prof_theta(f)
            return v, {x: th for x in exps}
        tot, ths = 0.0, {}
        for x in exps:
            f = lambda th, x=x: nll_counts(sig * EXPO[x] * rU * (1 + DELTA)**th + BKG[x], n[x])
            v, th = prof_theta(f)
            tot += v
            ths[x] = th
        return tot, ths
    return nll


def global_min(nll, n):
    res = minimize_scalar(lambda ls: nll(np.exp(ls), n)[0], bounds=(-12, 6), method="bounded", options={"xatol": 1e-7})
    v0 = nll(0.0, n)[0]
    if v0 <= res.fun:
        return v0, 0.0
    return res.fun, float(np.exp(res.x))


def limit(exps, mode, cl=0.9):
    nll = make_nll(exps, mode)
    grids = [range(NMAX + 1) for _ in exps]
    outcomes = [dict(zip(exps, o)) for o in np.array(np.meshgrid(*grids, indexing="ij")).reshape(len(exps), -1).T]
    gmin = [global_min(nll, o) for o in outcomes]
    nobs = {x: NOBS[x] for x in exps}
    gobs = global_min(nll, nobs)

    def tstat(sig, o, g):
        v, _ = nll(sig, o)
        return 0.0 if g[1] > sig else max(v - g[0], 0.0)

    def pval(sig):
        tobs = tstat(sig, nobs, gobs)
        _, ths = nll(sig, nobs)
        mu = {x: sig * EXPO[x] * rU * (1 + DELTA)**ths.get(x, 0.0) + BKG[x] for x in exps}
        p = 0.0
        for o, g in zip(outcomes, gmin):
            w = np.prod([poisson.pmf(o[x], mu[x]) for x in exps])
            if w < 1e-14:
                continue
            if tstat(sig, o, g) >= tobs - 1e-9:
                p += w
        return p

    s = brentq(lambda sg: pval(sg) - (1 - cl), 0.05, 50, xtol=1e-5)
    _, ths = nll(s, nobs)
    return s, ths


results = {}
for exps, mode, label in ((("A",), "none", "A alone"), (("B",), "none", "B alone"),
                          (("A", "B"), "none", "combined, no nuisance"),
                          (("A", "B"), "shared", "combined, one theta shared"),
                          (("A", "B"), "indep", "combined, one theta per exposure"),
                          (("A",), "shared", "A alone with the nuisance"),
                          (("B",), "shared", "B alone with the nuisance")):
    s, ths = limit(exps, mode)
    results[label] = s
    nsig = {x: s * EXPO[x] * rU for x in exps}
    print(f"{label:34s}: sigma_lim = {s:.4f}e-42 cm^2; expected signal at the limit " +
          ", ".join(f"{x}: {nsig[x]:.3f}" for x in exps) +
          ("" if not ths else "; theta_hathat = " + ", ".join(f"{x}: {ths[x]:+.3f}" for x in ths)))

c0 = results["combined, no nuisance"]
print(f"check: A alone = 2.303 / {EXPO['A']*rU:.4f} = {2.302585/(EXPO['A']*rU):.4f}e-42")
print(f"cost of the shared nuisance: {results['combined, one theta shared']/c0:.4f}; one per exposure: "
      f"{results['combined, one theta per exposure']/c0:.4f}; envelope (theta = -1): {1 + DELTA:.4f} -> {c0*(1+DELTA):.4f}e-42")
print(f"combined / best single (A): {c0/results['A alone']:.4f}; shared-nuisance combined / A alone with nuisance: "
      f"{results['combined, one theta shared']/results['A alone with the nuisance']:.4f}")
print(f"zero-count cost formula eq:8.8-cost with t* = 4.61 and k = {K:.4f}: "
      f"{(lambda w: 2*w*np.exp(w)/(K**2*4.6052))(np.sqrt(1+K**2*4.6052)-1):.4f}")
print(f"combined / B alone: {c0/results['B alone']:.4f}; per-exposure / shared limit: "
      f"{results['combined, one theta per exposure']/results['combined, one theta shared']:.4f}; "
      f"cost ratio (per-exposure - 1)/(shared - 1): {(results['combined, one theta per exposure']/c0-1)/(results['combined, one theta shared']/c0-1):.3f}")
print(f"closed form for A alone with the nuisance: N_90 exp(k^2 N_90) / N_90 = {np.exp(K**2*2.302585):.4f}")
