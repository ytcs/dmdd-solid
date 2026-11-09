"""Sect. 8.8, subsection on the likelihood: cost of one theory nuisance on a zero-count, zero-background limit.

Setting (stated in the text): one bin, N_obs = 0, N_bkg = 0, expected signal N(theta) = N_nom (1 + delta)^theta with a
standard-normal constraint on theta (eq:8.8-M, eq:8.8-like). Then -2 ln L = 2 N(theta) + theta^2 + const.
Threshold: t* = 2 N_90 = 2 ln 10 = 4.605, the value of -2 ln[L(N)/L(0)] = 2N at which the nuisance-free limit equals the exact
N_90 = 2.303 of eq:1.5-N90 (a calibration choice for this illustration; Sect. 21.4 builds the limit properly).
Profile: d/dtheta = 0 -> theta_hat = -k u with k = ln(1 + delta), u = N(theta_hat); profiled statistic 2u + k^2 u^2 = t*,
so w = k^2 u = sqrt(1 + k^2 t*) - 1 and N_nom,lim = u e^{k^2 u}; ratio to t*/2 is 2 w e^w / (k^2 t*) = 1 + k^2 t*/4 + O(k^3).
Envelope (worst case |theta| <= 1): ratio 1 + delta.
Linear nuisance N = N_nom (1 + theta delta): profiled statistic 2N_nom(1 - N_nom delta^2) + ... ; solution exists only for
delta^2 t* < 1 (printed for contrast).
Also checks the profiled minimum numerically.
"""
import numpy as np
from scipy.optimize import minimize_scalar, brentq

N90 = np.log(10)
ts = 2 * N90
print(f"N_90 = {N90:.4f}, t* = {ts:.4f}")


def prof_lim(delta):
    k = np.log1p(delta)
    w = np.sqrt(1 + k * k * ts) - 1
    u = w / k**2
    return u * np.exp(w), w, k


def numeric(delta):
    k = np.log1p(delta)

    def tprof(N):
        f = lambda th: 2 * N * np.exp(k * th) + th**2
        return minimize_scalar(f, bounds=(-20, 20), method="bounded").fun
    return brentq(lambda N: tprof(N) - ts, 1e-3, 100)


for d in (0.05, 0.1, 0.2, 0.3, 0.5, 1.0):
    lim, w, k = prof_lim(d)
    print(f"delta = {d:4.2f}: profiled N_lim = {lim:.4f} (numeric {numeric(d):.4f}), ratio {lim/N90:.4f}, "
          f"series 1 + k^2 t*/4 = {1 + k*k*ts/4:.4f}, envelope {1 + d:.3f}, theta_hat = {-k * w / k**2:.3f}")


def lin_lim(delta):
    # linear nuisance N(theta) = N (1 + theta delta), min over theta of 2N(1 + theta delta) + theta^2 at theta = -N delta
    # -> 2N - N^2 delta^2 = t*  -> N = (1 - sqrt(1 - delta^2 t*)) / delta^2 (smaller root)
    disc = 1 - delta * delta * ts
    return (1 - np.sqrt(disc)) / delta**2 if disc >= 0 else np.nan


for d in (0.1, 0.3, 0.4, 0.466, 0.5):
    print(f"linear nuisance delta = {d}: profiled N_lim = {lin_lim(d):.4f}; ratio {lin_lim(d)/N90:.4f}")
print(f"linear nuisance has no limit for delta > t*^(-1/2) = {ts**-0.5:.3f}")
