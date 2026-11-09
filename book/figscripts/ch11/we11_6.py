"""Worked example 11.6 (Sect. 11.5): the Markov-Krein band at the peak.  Prints every number of the example.

Gaussian: mu_0..mu_4 = 1, 0, 1, 0, 3; rho_MK(0) = 2/3 with nodes 0, +-sqrt 3 and weights 2/3, 1/6, 1/6 (eq:C.10-gauss).
Silicon: the T = 0 harmonic self response at q = 100 keV (WE 11.5), moments from c_k = E_R <omega^(k-1)> (mk11.py), with
  the band of eq:C.10-band at xi = E_R and on the bin E_R +- sigma_omega:  for a <= b,
  F(b) - F(a-0) lies in [lo(b) - hi(a), hi(b) - lo(a)] (lo, hi the band edges; F(a-0) >= lo(a), F(b) <= hi(b)).
Anharmonic shift of the moments: E^kin changes by -0.137 % for the silicon-like single-site model (limit11_5a.log,
  lambda3 = 1e-2, lambda4 = 2.5e-4) and by +0.083 % for lambda3 = 6e-3, lambda4 = 2e-4; the variance 4 E_R E^kin scales with it.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import imp11 as I  # noqa: E402
import mk11 as K  # noqa: E402

if __name__ == "__main__":
    zg = np.array([1.0, 0.0, 1.0, 0.0, 3.0])
    n, wt, r = K.canonical(zg, 0.0)
    print("Gaussian through 0: nodes %s, weights %s, rho = %.4f" % (np.round(np.sort(n), 4), np.round(wt[np.argsort(n)], 4), r))
    q = 100e3
    ER = I.e_r(q)
    w, s, e0, F, mu, num = K.si_response(q)
    zm, m1, sig = K.standardize(mu)
    print("Si 100 keV: E_R = %.1f meV, sigma = %.1f meV, skewness %.3f, kurtosis %.3f" % (ER * 1e3, sig * 1e3, zm[3], zm[4]))
    n, wt, r = K.canonical(zm, 0.0)
    o = np.argsort(n)
    print("canonical through E_R: nodes %s meV, weights %s, rho %.3f" % (np.round((n[o] * sig + m1) * 1e3, 1), np.round(wt[o], 3), r))
    lo0 = wt[n < 0].sum()
    print("band at E_R: [%.3f, %.3f]; F(E_R) = %.3f; weight above E_R in [%.3f, %.3f] (true %.3f)"
          % (lo0, lo0 + r, np.interp(ER, w, F), 1 - lo0 - r, 1 - lo0, 1 - np.interp(ER, w, F)))
    a, b = -1.0, 1.0
    la, ha, _, _ = K.band(zm, [a])
    lb, hb, _, _ = K.band(zm, [b])
    true = np.interp(m1 + b * sig, w, F) - np.interp(m1 + a * sig, w, F)
    print("bin E_R +- sigma: band [%.3f, %.3f], true %.3f, Gaussian 0.683" % (max(lb[0] - ha[0], 0), hb[0] - la[0], true))
    lg, hg, _, _ = K.band(zg, [-1.0, 1.0])
    print("Gaussian bin +-1: band [%.3f, %.3f]" % (max(lg[1] - hg[0], 0), hg[1] - lg[0]))
    a, b = -2.0, 2.0
    la, ha, _, _ = K.band(zm, [a]); lb, hb, _, _ = K.band(zm, [b])
    true = np.interp(m1 + b * sig, w, F) - np.interp(m1 + a * sig, w, F)
    print("bin E_R +- 2 sigma: band [%.3f, %.3f], true %.3f" % (max(lb[0] - ha[0], 0), hb[0] - la[0], true))
    # threshold at E_R + 3 sigma
    l3, h3, r3, _ = K.band(zm, [3.0])
    print("threshold E_R + 3 sigma = %.0f meV: weight above in [%.3e, %.3e], true %.3e" %
          ((m1 + 3 * sig) * 1e3, 1 - h3[0], 1 - l3[0], 1 - np.interp(m1 + 3 * sig, w, F)))
    for dk in (-0.137e-2, 0.083e-2):
        print("anharmonic E^kin change %+.3f %%: sigma changes by %+.3f %% = %+.3f meV" % (dk * 100, (np.sqrt(1 + dk) - 1) * 100,
              (np.sqrt(1 + dk) - 1) * sig * 1e3))
    # effect of the anharmonic width change on F: F(omega) of a Gaussian with sigma scaled by (1 + e): max |dF| = e max phi(x)|x|
    from scipy.stats import norm
    xg = np.linspace(-5, 5, 20001)
    for dk in (-0.137e-2, 0.083e-2):
        e = np.sqrt(1 + dk) - 1
        dF = np.max(np.abs(norm.cdf(xg / (1 + e)) - norm.cdf(xg)))
        print("Kinetic-energy change %+.3f %%: largest change of a Gaussian cumulative %.2e; band width at E_R / change = %.0f"
              % (dk * 100, dF, r / dF))
