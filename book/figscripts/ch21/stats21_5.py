"""Numbers of Sect. 21.5 (unknown background, coverage of a minimum over bins, recast of a binned silicon limit).

Sources
  [Y02] S. Yellin, Phys. Rev. D 66, 032005 (2002), arXiv:physics/0203002: Eq. (2), the probability C_0(x, mu) that the
        maximum gap of a Poisson process of mean mu (unit density after the change of variable to expected counts) is
        smaller than x; m = floor(mu/x). The 90 % upper limit is the signal for which C_0(x_obs, mu) = 0.90.
  [B]   D. Baxter et al., arXiv:2105.00599, Table 1: book halo v0 = 238, v_esc = 544 km/s, v_E^ref = 250.5 km/s (App. A.8).
  [E16] R. Essig et al., JHEP 05 (2016) 046, arXiv:1509.01598, App. B: halo v0 = 230, v_esc = 600, v_E = 240 km/s,
        rho = 0.4 GeV/cm^3 (the convention of that paper; quoted in the book as a published convention).
  Silicon response: the tabulated crystal form factor of [E16] via figscripts/ch21/hib21.py (heavy mediator, pair bins of the
  energy-only cascade of Sect. 18.3, hib21.pbin: E_g = 1.160 eV, eps_eh = 3.749 eV), as in Sect. 21.2.

Sections of the log
  (1) C_0: closed form checked against a Monte Carlo of the maximum gap (unit-density uniform events).
  (2) Zero and one event: maximum-gap limits against the Poisson limit that counts every event as signal.
  (3) Coverage of a limit defined as the minimum over n independent bins, each at 90 %; Bonferroni counts ln(10 n).
  (4) Recast of a three-bin silicon limit from the halo of [E16] to the book halo: per-bin factors, exact recast of the
      minimum-over-bins limit, the single-factor rescaling and the bracket [min_i K_i, K_j*] of Sect. 21.5.
Run: python stats21_5.py > stats21_5.log  (about 20 s)
"""
import os
import sys
import numpy as np
from math import factorial, floor
from scipy.optimize import brentq
from scipy.special import erf, gammaincc

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hib21 as HB  # noqa: E402


# ------------------------------------------------------------------ (1) maximum gap
def C0(x, mu):
    """[Y02] Eq. (2), written as sum_k e^{-kx}/k! [(kx - mu)^k - k (kx - mu)^(k-1)], which equals
    (kx - mu)^k (1 + k/(mu - kx)) and stays finite at kx = mu."""
    if x > mu:
        return 1.0
    m = int(floor(mu / x))
    s = 0.0
    for k in range(m + 1):
        a = k * x - mu
        term = a**k - (k * a**(k - 1) if k > 0 else 0.0)
        s += np.exp(-k * x) / factorial(k) * term
    return s


def mc_maxgap(mu, nsim=200000, seed=1):
    rng = np.random.default_rng(seed)
    out = np.empty(nsim)
    for i in range(nsim):
        n = rng.poisson(mu)
        e = np.sort(rng.uniform(0, mu, n))
        out[i] = np.max(np.diff(np.concatenate([[0.0], e, [mu]])))
    return out


def poisson_up(nobs, cl=0.9):
    """Classical upper limit with no background: P(n <= nobs | N) = 1 - cl (eq:1.5-N90 for nobs = 0)."""
    return brentq(lambda N: gammaincc(nobs + 1, N) - (1 - cl), 1e-9, 100)


def maxgap_limit(g, cl=0.9):
    """Signal N at which C_0(g N, N) = cl, for a largest gap holding the fraction g of the expected signal."""
    return brentq(lambda N: C0(g * N, N) - cl, 1e-6, 40)


print("(1) Maximum-gap function C_0(x, mu), [Y02] Eq. (2)")
print(f"  C_0(mu, mu) = 1 - e^-mu check at mu = 2.303: {C0(2.302585, 2.302585):.6f} vs {1 - np.exp(-2.302585):.6f}")
for mu in (3.0, 5.0, 8.0):
    sim = mc_maxgap(mu, nsim=100000, seed=int(10 * mu))
    for frac in (0.5, 0.7, 0.9):
        x = frac * mu
        print(f"  mu = {mu:.1f}, x = {x:.2f}: C_0 = {C0(x, mu):.4f}, Monte Carlo P(max gap < x) = {np.mean(sim < x):.4f}")

print("\n(2) 90 % limits with an unknown background")
print(f"  Poisson, every event counted as signal: N_obs = 0: {poisson_up(0):.3f}; 1: {poisson_up(1):.3f}; 2: {poisson_up(2):.3f}; 3: {poisson_up(3):.3f}")
for g in (1.0, 0.9, 0.75, 0.6, 0.5):
    print(f"  maximum gap holding the fraction g = {g:.2f} of the expected signal: N_sig^lim = {maxgap_limit(g):.3f}")
# two events, both in the lowest tenth of the expected signal: largest gap 0.9 (if they sit at 0.05 and 0.1)
print(f"  two events at expected-count fractions 0.05 and 0.10: largest gap 0.90 -> {maxgap_limit(0.90):.3f} (Poisson, 2 events: {poisson_up(2):.3f})")
print(f"  two events at fractions 1/3 and 2/3: largest gap 1/3 -> {maxgap_limit(1/3):.3f}")
g1 = brentq(lambda g: maxgap_limit(g) - poisson_up(1), 0.6, 0.99)
print(f"  one event: the maximum-gap limit equals the one-event Poisson limit {poisson_up(1):.3f} at g = {g1:.4f}; stronger for g > {g1:.3f}")

print("\n(3) Minimum over n independent bins, each at 90 %")
for n in (1, 2, 3, 5, 10):
    print(f"  n = {n:2d}: coverage 0.9^n = {0.9**n:.3f}; Bonferroni per-bin zero-event count ln(10 n) = {np.log(10 * n):.3f}"
          f" (per-bin confidence {1 - 0.1 / n:.3f})")


# ------------------------------------------------------------------ (4) recast of a binned silicon limit
def eta_halo(v0, vesc, ve):
    """App. D.1 closed form of eta (km/s)^-1 for a truncated Maxwellian (v0, vesc) seen at speed ve."""
    z = vesc / v0
    nesc = np.pi**1.5 * v0**3 * (erf(z) - 2 / np.sqrt(np.pi) * z * np.exp(-z**2))
    k = np.pi * v0**2 / (ve * nesc)

    def eta(u):
        u = np.maximum(np.asarray(u, float), 0.0)
        b1 = k * (np.sqrt(np.pi) * v0 / 2 * (erf((u + ve) / v0) - erf((u - ve) / v0)) - 2 * ve * np.exp(-z**2))
        b2 = k * (np.sqrt(np.pi) * v0 / 2 * (erf(z) - erf((u - ve) / v0)) - (vesc + ve - u) * np.exp(-z**2))
        return np.where(u < vesc - ve, b1, np.where(u < vesc + ve, b2, 0.0))
    return eta


eta_book = eta_halo(238.0, 544.0, 250.5)
eta_pub = eta_halo(230.0, 600.0, 240.0)
NUP3 = np.log(30.0)
print("\n(4) Recast of a three-bin silicon limit (1 kg yr, zero events per bin, N^up = ln 30 = %.3f per bin)" % NUP3)
print("    published halo (230, 600, 240) km/s, rho = 0.4; new halo (238, 544, 250.5) km/s, rho = 0.3; heavy mediator")
print(f"    v_max = v_esc + v_E: published {600 + 240:.1f} km/s, new {544 + 250.5:.1f} km/s")
for m in (2e6, 10e6):
    for label, rho_pub in (("same density 0.3", 0.3), ("published density 0.4", 0.4)):
        s_pub, s_new = [], []
        for nb in (1, 2, 3):
            cp = HB.counts_eta(m, nb, lambda u: eta_pub(u) * HB.etatilde_unit(m)) * rho_pub / 0.3
            cn = HB.counts_eta(m, nb, lambda u: eta_book(u) * HB.etatilde_unit(m))
            s_pub.append(cp)
            s_new.append(cn)
        s_pub, s_new = np.array(s_pub), np.array(s_new)       # counts per kg yr at sigma = 1 cm^2
        ok = (s_pub > 0) & (s_new > 0)
        K = np.where(ok, s_pub / np.where(ok, s_new, 1), np.nan)
        lim_pub_bins = np.where(s_pub > 0, NUP3 / np.where(s_pub > 0, s_pub, 1), np.inf)
        lim_new_bins = np.where(s_new > 0, NUP3 / np.where(s_new > 0, s_new, 1), np.inf)
        jp, jn = int(np.argmin(lim_pub_bins)), int(np.argmin(lim_new_bins))
        sp, sn = lim_pub_bins[jp], lim_new_bins[jn]
        print(f"  m = {m/1e6:.0f} MeV, {label}: counts per unit sigma (pub) = " + ", ".join(f"{x:.3e}" for x in s_pub)
              + "; (new) = " + ", ".join(f"{x:.3e}" for x in s_new))
        print(f"     K_i = r_i^pub / r_i^new = " + ", ".join("—" if np.isnan(x) else f"{x:.3f}" for x in K))
        print(f"     published limit {sp:.4e} cm^2 (bin {jp+1}); exact recast {sn:.4e} cm^2 (bin {jn+1}); ratio {sn/sp:.4f}")
        Kj = K[jp]
        print(f"     single-factor rescaling with K_j* = {Kj:.4f} -> {Kj*sp:.4e}; bracket [min K, K_j*] = [{np.nanmin(K):.4f}, {Kj:.4f}];"
              f" without the limiting bin [min K, max K] = [{np.nanmin(K):.4f}, {np.nanmax(K):.4f}]")

print("\n(5) Boosted flux: events scale as sigma^2 (flux itself proportional to sigma), so a rate ratio R moves the limit by R^(-1/2)")
for R in (0.93, 0.65, 0.17, 0.05):
    print(f"  R = {R:.2f}: limit x {R**-0.5:.3f}")
print(f"  density convention 0.4 -> 0.3 GeV/cm^3: common recast factor {0.4/0.3:.4f}")
