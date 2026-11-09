"""Limit Check 14.6c (lim:14.6c, Sect. 14.6): sensitivity of the fixed-amplitude and Rayleigh-amplitude likelihoods
against the record length t_int/t_coh.  Output tex/figures/ch14/limit14_6c.pdf, log limit14_6c.log.
Run: python limit14_6c.py (seconds).

Literature formulas (the two power laws).  Budker et al. 1306.6089 Eqs. (A7)-(A8) (arXiv PDF numbering): threshold
amplitude B_s = sqrt(S_n) t^{-1/2} for t < tau and sqrt(S_n) (tau t)^{-1/4} for t > tau; Foster, Rodd and Safdi
1711.10489 Eq. (54) (95 % Asimov limit, long records) and Eqs. (63), (69) (S/N = |Phi|(T tau)^{1/4}/sqrt(lambda_B)).

Fuller result (this script).  Median expected 95 % CL upper limit on the signal power, by the exact Neyman construction,
for a white noise PSD b = S_n per periodogram bin and a signal of total mean power s_tot = A^2 t_int spread over the line.
  Line: the standard-halo line of coh14.py (book eq:14.6-Fphi), Fejer-windowed for a record t_int, bins of width
    2 pi/t_int with one bin centred on the line peak.  The signal is replaced by a box of N_eff equal bins, with
    N_eff = 1/sum_k p_k^2 the participation number of the windowed bin powers p_k (N_eff -> 1 for t_int << t_coh,
    N_eff -> t_int Delta omega_eq/2 pi for t_int >> t_coh, Delta omega_eq t_coh = DW_EQ = 1/int F_x^2 dx).
  Statistic: Q = sum of the N_eff box-bin periodogram values (sufficient for the box).
  Rayleigh amplitude (exponential-bin likelihood, signal a complex Gaussian): Q ~ Gamma(N_eff, scale b + s_tot/N_eff).
  Fixed amplitude (deterministic signal power in each bin, random phase): 2Q/b ~ noncentral chi^2(2 N_eff, 2 s_tot/b).
  Median of Q under background only, Q_med; upper limit s_up solves CDF(Q_med | s_up) = 0.05.
  Plotted: y = (A_up^2 t_coh/S_n)^{1/2} = (s_up/(b t_int/t_coh))^{1/2}, proportional to the coupling at the limit.
Asymptotes: y = (c1/x)^{1/2} for x = t_int/t_coh -> 0 (single bin, c1 = s_up/b of one bin) and
  y = (1.645 (DW_EQ/2pi)^{1/2})^{1/2} x^{-1/4} for x -> infinity (Gaussian limit of Q, same for both models).
Shaded: x where the Rayleigh curve is within 10 % of one of its asymptotes (contiguous from each end).  Crossover marked
where the local logarithmic slope of each curve is -3/8, midway between the two laws; the meeting point of the asymptotes
is logged as well.
"""
import os
import numpy as np
from scipy import stats, optimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import coh14 as C

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch14")
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(HERE, "limit14_6c.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


n_eff, s_up_stoch, s_up_det = C.n_eff, C.s_up_stoch, C.s_up_det


x = np.logspace(-2, 3, 121)
Ne = np.array([n_eff(T) for T in x])
ys = np.array([np.sqrt(s_up_stoch(N) / T) for N, T in zip(Ne, x)])
yd = np.array([np.sqrt(s_up_det(N) / T) for N, T in zip(Ne, x)])

c1s = s_up_stoch(1.0)
c1d = s_up_det(1.0)
cinf = 1.645 * np.sqrt(C.DW_EQ / (2 * np.pi))
out(f"line: equivalent width Delta omega_eq t_coh = {C.DW_EQ:.4f}; peak x = {C.X_PEAK:.4f}; mean x = {C.X_MEAN:.4f}")
out(f"single bin (t_int << t_coh): median 95% limit s_up/b = {c1s:.3f} (Rayleigh), {c1d:.3f} (fixed amplitude)")
out(f"  ratio of coupling limits Rayleigh/fixed = sqrt({c1s:.2f}/{c1d:.2f}) = {np.sqrt(c1s/c1d):.3f}")
# Same construction for data at the detection threshold of a single bin (Centers et al. 1905.13650 compare limits for
# data at the 95 % detection threshold): observed Q = b ln 20, the background-only 95 % quantile of an exponential bin.
q_thr = np.log(20.0)
su_thr_s = optimize.brentq(lambda s: stats.expon.cdf(q_thr, scale=1.0 + s) - 0.05, 1e-9, 1e6)
su_thr_d = optimize.brentq(lambda s: stats.ncx2.cdf(2 * q_thr, 2, 2 * s) - 0.05, 1e-9, 1e6)
out(f"construction: statistic Q = summed periodogram of the N_eff line bins; Rayleigh Q ~ Gamma(N_eff, b + s/N_eff);"
    f" fixed 2Q/b ~ noncentral chi2(2 N_eff, 2 s/b); s_up solves CDF(Q_obs | s_up) = 0.05")
out(f"single bin, data at the detection threshold Q = b ln 20 = {q_thr:.3f} b: s_up/b = {su_thr_s:.2f} (Rayleigh), {su_thr_d:.2f} (fixed);"
    f" ratio of coupling limits = {np.sqrt(su_thr_s/su_thr_d):.3f} [Centers et al.: 2.7 frequentist]")
out(f"long records: y -> {np.sqrt(cinf):.4f} x^(-1/4)  [s_up/b -> 1.645 sqrt(N_eff), N_eff = x DW/2pi]")
xc_s = (c1s / cinf) ** 2
xc_d = (c1d / cinf) ** 2
out(f"asymptotes meet at t_int/t_coh = {xc_s:.1f} (Rayleigh) and {xc_d:.1f} (fixed amplitude)")
for T, N, a, b in zip(x[::6], Ne[::6], ys[::6], yd[::6]):
    out(f"  x = {T:9.3f}  N_eff = {N:9.3f}  y_Rayleigh = {a:.4e}  y_fixed = {b:.4e}  ratio = {a/b:.3f}")
small = np.sqrt(c1s / x)
large = np.sqrt(cinf) * x ** -0.25
ok_small = np.abs(ys / small - 1) <= 0.1
ok_large = np.abs(ys / large - 1) <= 0.1
xs_hi = x[np.argmin(ok_small)- 1]          # end of the contiguous region from the left
xl_lo = x[len(x) - np.argmin(ok_large[::-1])]  # start of the contiguous region at the right
out(f"Rayleigh curve within 10 % of the t^-1/2 law for x <= {xs_hi:.3g}, of the (t t_coh)^-1/4 law for x >= {xl_lo:.3g}")
okd_s = np.abs(yd / np.sqrt(c1d / x) - 1) <= 0.1
okd_l = np.abs(yd / large - 1) <= 0.1
out(f"fixed-amplitude curve within 10 % of its t^-1/2 law for x <= {x[np.argmin(okd_s)-1]:.3g}, of the -1/4 law for x >= {x[len(x)-np.argmin(okd_l[::-1])]:.3g}")
sl_s = np.gradient(np.log(ys), np.log(x))
sl_d = np.gradient(np.log(yd), np.log(x))
def cross38(sl):
    j0 = np.argmin(sl)                      # past the steepest point (Rayleigh curve dips below -1/2)
    j = j0 + np.argmax(sl[j0:] >= -0.375)
    return np.exp(np.interp(-0.375, [sl[j - 1], sl[j]], [np.log(x[j - 1]), np.log(x[j])]))
xm_s = cross38(sl_s)
xm_d = cross38(sl_d)
out(f"steepest local slope of the Rayleigh curve: {sl_s.min():.3f} at x = {x[np.argmin(sl_s)]:.3g}")
out(f"local slope -3/8 (midway between -1/2 and -1/4) at t_int/t_coh = {xm_s:.2f} (Rayleigh), {xm_d:.2f} (fixed amplitude)")
for xv in (0.1, 1.0, 3.0, 10.0, 30.0, 100.0):
    j = np.argmin(np.abs(x - xv))
    out(f"  local slope at x = {x[j]:.3g}: Rayleigh {sl_s[j]:.3f}, fixed {sl_d[j]:.3f}")
i1 = np.argmin(np.abs(x - 1.0))
out(f"at t_int = t_coh: N_eff = {Ne[i1]:.3f}; Rayleigh/fixed coupling ratio = {ys[i1]/yd[i1]:.3f}")
i2 = np.argmin(np.abs(x - 100.0))
out(f"at t_int = 100 t_coh: Rayleigh/fixed coupling ratio = {ys[i2]/yd[i2]:.3f}")

fig, ax = plt.subplots(figsize=(4.3, 3.0))
ax.axvspan(x.min(), xs_hi, color="0.9", lw=0)
ax.axvspan(xl_lo, x.max(), color="0.9", lw=0)
ax.loglog(x, ys, color="C3", lw=1.6, label="Rayleigh amplitude (exponential bins)")
ax.loglog(x, yd, color="C0", lw=1.3, label="fixed amplitude")
ax.loglog(x, small, color="k", lw=0.8, ls="--", label=r"$t_{\mathrm{int}}^{-1/2}$")
ax.loglog(x, np.sqrt(c1d / x), color="k", lw=0.6, ls=":")
ax.loglog(x, large, color="k", lw=0.8, ls="-.", label=r"$(t_{\mathrm{int}}t_{\mathrm{coh}})^{-1/4}$")
ax.plot([xm_s], [np.interp(np.log(xm_s), np.log(x), ys)], "o", ms=4, mfc="w", mec="C3", zorder=5)
ax.plot([xm_d], [np.interp(np.log(xm_d), np.log(x), yd)], "o", ms=4, mfc="w", mec="C0", zorder=5)
ax.set_xlim(x.min(), x.max())
ax.set_ylim(0.02, 60)
ax.set_xlabel(r"$t_{\mathrm{int}}/t_{\mathrm{coh}}$")
ax.set_ylabel(r"$(A_{95}^2\,t_{\mathrm{coh}}/S_n)^{1/2}$")
ax.legend(fontsize=6.3, frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit14_6c.pdf"))
out("wrote limit14_6c.pdf")
