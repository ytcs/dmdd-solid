"""Worked example 21.4 (we:21-rpaband) and the statistics numbers of Sect. 21.4 and App. D.47 (log: we21_4.log).

Part 1. Poisson upper limits with a known background b (Sect. 21.4.1).
  Classical (Neyman) 90% upper limit: the signal s_up with sum_{n <= N_obs} P(n | s_up + b) = 0.10 (eq:21.4-classical);
  negative s_up means an empty interval.
  Likelihood-ratio ordering of Feldman and Cousins (physics/9711021, Sect. IV A, Eq. (4.1)): at each s on a grid of step
  0.005 (their step), outcomes n enter the acceptance region in decreasing order of R = P(n|s)/P(n|s_best),
  s_best = max(0, n - b), until the summed probability reaches 0.90; the upper end for N_obs is the largest s whose
  region contains N_obs.  Checked against their Table IV (b = 0, 1, 3; N_obs = 0, 1, 2).
Part 2. Worked example: silicon at 3 MeV, heavy mediator, 1 kg yr, zero events, zero background (nuis21.py inputs).
  Random-phase level: RPA tables (their scissor gives the measured T = 0 gap, 1.17 eV; nuis21.py).  Computed correction:
  RPA + LF (central value).  Band: beta_k = -c_k (one bin), sigma_beta.  Profiled limit: the book's construction, the
  Neyman construction of Sect. 21.5 with the nuisance at its conditional best fit: exp(sigma_beta^2 N_90) at zero counts
  (nuis21.profile_ratio); the fixed calibrated threshold of Sect. 8.8 is printed for comparison only.  Detector
  efficiency: a 10 percent normalization uncertainty, beta = -ln 1.10 (illustrative assumption).  One-sided attraction:
  theta_X >= 0 with a half-normal constraint.
Part 3. Checks for App. D.47: Neyman construction at the conditional best fit, one bin, against exp(sigma^2 Q'/2).
Part 4. Excluded cells; Si Migdal shares 0.33 (2 MeV), 0.07 (3 MeV) of tab:12-nuisances; aluminum at 1 keV, light mediator (WE 15.x numbers of Sect. 15.1): the window 2 Delta < omega <
  3 Delta carries 20 % (bulk gap) and 37 % (film gap) of the conserving rate; excluding it raises the limit by 1/(1 - f).
Run: python we21_4.py (about 30 s).
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq
from scipy.stats import poisson

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nuis21 as N  # noqa: E402

LOG = open(os.path.join(HERE, "we21_4.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


# ---- Part 1 ------------------------------------------------------------------------------------------------------
def classical(nobs, b, cl=0.90):
    f = lambda s: poisson.cdf(nobs, s + b) - (1 - cl)
    lo = -b
    if f(lo) < 0:
        return lo  # not reached
    return brentq(f, lo, 100.0)


def fc_upper(nobs, b, cl=0.90, step=0.005, smax=20.0):
    ns = np.arange(0, 80)
    sbest = np.maximum(0.0, ns - b)
    pbest = poisson.pmf(ns, sbest + b)
    up = 0.0
    for s in np.arange(0.0, smax, step):
        p = poisson.pmf(ns, s + b)
        order = np.argsort(-(p / pbest))
        acc, tot = [], 0.0
        for i in order:
            acc.append(ns[i])
            tot += p[i]
            if tot >= cl:
                break
        if nobs in acc:
            up = s
    return up


out("Part 1: 90% upper limits on the signal mean with known background b")
for nobs, b in ((0, 0.0), (0, 1.0), (0, 3.0), (1, 1.0), (2, 2.0), (1, 0.0)):
    out("  N_obs = %d, b = %.1f: classical %.3f ; Feldman-Cousins %.2f" % (nobs, b, classical(nobs, b), fc_upper(nobs, b)))
out("  quoted from FC Table IV: (0,0) 2.44, (0,1) 1.61, (0,3) 1.08, (1,1) 3.36, (2,2) 3.91, (1,0) 4.36")
out("  (the reproduction differs at (0,3), 0.95 against 1.08, because FC lengthen intervals to make the upper end")
out("   non-increasing in b, Sect. IV A; and by one grid step at (0,1), (1,1))")
out("  classical N_obs = 0: s_up = ln 10 - b, empty for b > %.3f" % np.log(10))

# ---- Part 2 ------------------------------------------------------------------------------------------------------
M = 3e6
rc, c, fx = N.nuisances(M)
r_rpa = N.tot(M, resp="rpa")
lim = lambda r: N.N90 * N.SIG_REF / (r * N.YR_EXPO)
out("\nPart 2: silicon, 3 MeV, heavy mediator, 1 kg yr, zero events, zero background (tables' gap = measured 1.17 eV)")
out("  RPA: rate %.4g -> limit %.3e cm2" % (r_rpa, lim(r_rpa)))
out("  RPA + LF (central): rate %.4g -> limit %.3e cm2 (x%.3f weaker than RPA)" % (rc, lim(rc), r_rpa / rc))
keys = ["attraction", "tabulation", "gap", "large-q LF"]
for k in keys:
    out("  beta_%s = %+.3f" % (k, -c[k]))
sg = np.sqrt(sum(c[k] ** 2 for k in keys))
L0 = lim(rc)
out("  sigma_beta = %.3f ; band x%.3f : %.3e - %.3e cm2" % (sg, np.exp(sg), L0 / np.exp(sg), L0 * np.exp(sg)))
out("  attraction + tabulation share of sigma_beta^2: %.3f" % ((c["attraction"] ** 2 + c["tabulation"] ** 2) / sg**2))
out("  envelope one at a time (theta_k = +-1): " + "; ".join("%s x%.3f" % (k, np.exp(abs(c[k]))) for k in keys))
pr = N.profile_ratio(sg)
out("  profiled/nominal, Neyman construction with theta at its conditional best fit (Sect. 21.5): exp(sigma^2 N_90) = %.3f"
    " -> %.3e cm2" % (pr, L0 * pr))
out("    (for comparison, fixed calibrated threshold t* = 2 N_90 of Sect. 8.8: %.3f; second order exp(sigma^2 t*/4) %.3f)"
    % (N.fixed_threshold_ratio(sg), np.exp(sg**2 * N.TSTAR / 4)))
out("  RPA limit / central limit = %.3f ; RPA limit inside the band: %s ; lower band edge / central = %.3f"
    % (lim(r_rpa) / L0, L0 / np.exp(sg) <= lim(r_rpa) <= L0 * np.exp(sg), np.exp(-sg)))
ce = np.log(1.10)
sge = np.sqrt(sg**2 + ce**2)
out("  with a 10 %% efficiency nuisance (beta = -%.4f): sigma_beta = %.3f, band x%.3f, profiled/nominal %.3f"
    % (ce, sge, np.exp(sge), N.profile_ratio(sge)))
s3 = np.sqrt(c["tabulation"] ** 2 + c["gap"] ** 2 + c["large-q LF"] ** 2)
out("  one-sided attraction (theta_X >= 0): profile pins theta_X = 0; other three sigma = %.3f ; profiled/nominal %.3f"
    " -> %.3e cm2 ; attraction at theta_X = 1 lowers the limit by 1/%.3f"
    % (s3, N.profile_ratio(s3), L0 * N.profile_ratio(s3), np.exp(c["attraction"])))
s2 = np.hypot(c["gap"], c["large-q LF"])
out("  without attraction and tabulation spread: sigma_beta = %.3f, band x%.3f" % (s2, np.exp(s2)))
out("  tabulation spread as a bound (set at its weaker end, theta_tab = 1, not in the band): limit x%.3f -> %.3e cm2;"
    " band of the other three x%.3f" % (np.exp(abs(c["tabulation"])), L0 * np.exp(abs(c["tabulation"])),
                                        np.exp(np.sqrt(c["attraction"]**2 + c["gap"]**2 + c["large-q LF"]**2))))

# ---- Part 3 ------------------------------------------------------------------------------------------------------
out("\nPart 3 (App. D.47): Neyman construction with the nuisance at its conditional best fit, one bin, one lognormal")
out("  nuisance of log-width sigma; exact limit against the second-order form exp(sigma^2 Q'/2)")


def neyman_one_bin(sig, nobs, b, cl=0.90):
    """Signal s at which P(N <= nobs | s e^{sig th} + b) = 1 - cl, th the conditional best fit of
    2[(s e^{sig th} + b) - nobs ln(s e^{sig th} + b)] + th^2 (for one bin the outcomes with t >= t_obs are N <= nobs)."""
    from scipy.optimize import minimize_scalar

    def p(s):
        f = lambda th: 2 * ((s * np.exp(sig * th) + b) - nobs * np.log(s * np.exp(sig * th) + b)) + th**2
        th = minimize_scalar(f, bounds=(-10, 10), method="bounded", options={"xatol": 1e-10}).x
        return poisson.cdf(nobs, s * np.exp(sig * th) + b) - (1 - cl)
    return brentq(p, 1e-6, 200.0)


for nobs, b in ((0, 0.0), (0, 1.0), (1, 1.0), (2, 2.0)):
    s0 = classical(nobs, b)
    Qp = 2 * s0 * (1 - nobs / (s0 + b))
    for sig in (0.1, 0.3, 0.393):
        sp = neyman_one_bin(sig, nobs, b)
        out("  N_obs %d, b %.1f: s_up %.3f, Q' = %.3f ; sigma %.3f: exact %.4f, second order exp(sigma^2 Q'/2) %.4f"
            % (nobs, b, s0, Qp, sig, sp / s0, np.exp(sig**2 * Qp / 2)))
out("  fixed threshold (Sect. 8.8, eq:8.8-cost), zero counts, t* = 4.605: exact against exp(sigma^2 t*/4):")
for sig in (0.3, 0.5):
    out("  sigma %.3f: exact %.4f ; second order %.4f" % (sig, N.fixed_threshold_ratio(sig), np.exp(sig**2 * N.TSTAR / 4)))

# ---- Part 4 ------------------------------------------------------------------------------------------------------
out("\nPart 4: excluded cells, Al at 1 keV, light mediator (Sect. 15.1 worked example)")
for lab, f in (("bulk gap", 0.20), ("film gap", 0.37)):
    out("  %s: window share %.2f -> limit x%.3f" % (lab, f, 1 / (1 - f)))
out("Excluded cells, Si Migdal: unsized coherent zero-phonon band (0.75 keV to 2 q_BZ) holds 33 % of the rate at 2 MeV and")
out("  7 % at 3 MeV (tab:12-nuisances); excluding it raises the limit by")
for m, f in ((2, 0.33), (3, 0.07)):
    out("  %d MeV: x%.3f" % (m, 1 / (1 - f)))
