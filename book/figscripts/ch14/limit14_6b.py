"""Limit Check 14.6b (lim:14.6b, Sect. 14.6): the Gaussian-field signal, its power spectrum and the golden-rule mean.
Output tex/figures/ch14/limit14_6b.pdf, log limit14_6b.log.  Run: python limit14_6b.py (about a minute).

Literature formula.  Foster, Rodd and Safdi 1711.10489 Eqs. (8), (10), (24): the field is a sum of Rayleigh-distributed
  amplitudes with random phases, and each periodogram bin is exponentially distributed with mean
  lambda(omega) = A pi f(v)/(m v) at v = sqrt(2 omega/m - 2), i.e. proportional to F_phi(omega) (book eq:14.6-Fphi,
  eq:14.6-Sphi).  In the units of coh14.py: mean periodogram/(2 pi) = F_x(x).  For a target this is the golden-rule
  mean of eq:8.2-abs averaged over the line.
Fuller result.  A record of finite length t_int: the mean periodogram is F_x convolved with the Fejer kernel
  (t/2pi) sinc^2(x t/2) (coh14.fejer_mean), and the mean energy absorbed by linearly driven spins of coherence time T2,
  divided by (golden-rule rate) x t_int (coh14.absorbed_ratio).  For T2 -> infinity the two coincide.
  Curves: T2 = infinity, T2 = t_coh, T2 = 0.1 t_coh; Larmor frequency (bin) at the peak of the line.
  Monte Carlo: 1500 realizations of 2000 modes, exact transform, peak bin, for t_int/t_coh = 0.1 ... 100; the log also
  gives the ratio variance/mean^2 of the peak-bin power (1 for an exponential distribution).
Plotted: y = ratio to the golden-rule (t_int -> infinity) value against x = t_int/t_coh.
Shaded: x where the T2 = infinity curve is within 10 % of one.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import coh14 as C

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch14")
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(HERE, "limit14_6b.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


x = np.logspace(-2, 3, 161)
r_inf = np.array([C.fejer_mean(C.X_PEAK, t) / C.F_PEAK for t in x])
r_1 = np.array([C.absorbed_ratio(t, 1.0, C.X_PEAK) for t in x])
r_01 = np.array([C.absorbed_ratio(t, 0.1, C.X_PEAK) for t in x])
chk = np.array([C.absorbed_ratio(t, np.inf, C.X_PEAK) for t in x[::20]])
out("check: absorbed-energy ratio (T2 = inf) / Fejer ratio:", ", ".join(f"{a/b:.6f}" for a, b in zip(chk, r_inf[::20])))
for name, r in (("T2 = inf", r_inf), ("T2 = t_coh", r_1), ("T2 = 0.1 t_coh", r_01)):
    ok = np.abs(r - 1) <= 0.1
    xlo = x[len(x) - np.argmin(ok[::-1])]
    out(f"{name}: ratio at t/t_coh = 0.1, 1, 10, 100: " +
        ", ".join(f"{np.interp(np.log(v), np.log(x), r):.4f}" for v in (0.1, 1, 10, 100)) +
        f"; within 10 % of the golden rule for t >= {xlo:.3g} t_coh")
    if name == "T2 = inf":
        xshade = xlo
# large-t correction coefficient: 1 - r ~ c/x
for t in (100.0, 1000.0):
    out(f"  T2 = inf: (1 - ratio) x t/t_coh at t = {t:g}: {(1 - C.fejer_mean(C.X_PEAK, t)/C.F_PEAK)*t:.3f}")
# small-t: ratio ~ t/(2 pi F_peak), absorbed energy grows as t^2
for t in (0.01, 0.03):
    out(f"  T2 = inf: ratio at t = {t}: {C.fejer_mean(C.X_PEAK, t)/C.F_PEAK:.5f}; t/(2 pi F_peak) = {t/(2*np.pi*C.F_PEAK):.5f}")

rng = np.random.default_rng(14062)
tmc = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
mc_mean, mc_err = [], []
for t in tmc:
    P = C.mc_periodogram(t, np.array([C.X_PEAK]), 2000, 1500, rng)[:, 0]
    m, s = P.mean(), P.std()
    mc_mean.append(m / C.F_PEAK)
    mc_err.append(s / np.sqrt(len(P)) / C.F_PEAK)
    out(f"  MC t = {t:6.1f}: mean/F_peak = {m/C.F_PEAK:.4f} +- {s/np.sqrt(len(P))/C.F_PEAK:.4f}; analytic "
        f"{C.fejer_mean(C.X_PEAK, t)/C.F_PEAK:.4f}; var/mean^2 = {s**2/m**2:.3f}")

fig, ax = plt.subplots(figsize=(4.3, 3.0))
ax.axvspan(xshade, x.max(), color="0.9", lw=0)
ax.semilogx(x, r_inf, color="C3", lw=1.6, label=r"$T_2 \to \infty$ (= mean periodogram)")
ax.semilogx(x, r_1, color="C0", lw=1.3, label=r"$T_2 = t_{\mathrm{coh}}$")
ax.semilogx(x, r_01, color="C2", lw=1.3, label=r"$T_2 = 0.1\,t_{\mathrm{coh}}$")
ax.errorbar(tmc, mc_mean, yerr=mc_err, fmt="o", ms=3.5, mfc="w", mec="C3", ecolor="C3", lw=0.8,
            label="Monte Carlo field")
ax.axhline(1.0, color="k", lw=0.8, ls="--", label="golden rule / Gaussian-field spectrum")
ax.set_xlim(x.min(), x.max())
ax.set_ylim(0, 1.15)
ax.set_xlabel(r"$t_{\mathrm{int}}/t_{\mathrm{coh}}$")
ax.set_ylabel("ratio to the long-record value")
ax.legend(fontsize=6.0, frameon=False, loc="lower right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit14_6b.pdf"))
out("wrote limit14_6b.pdf")
