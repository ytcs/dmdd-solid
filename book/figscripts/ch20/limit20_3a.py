"""Limit Check 20.3a (lim:20.3a, fig:20-limit-amm): the normal-incidence impedance law against the angle- and
mode-averaged acoustic-mismatch transmission, for a family of aluminum-like films on silicon.  Log: limit20_3a.log.
Run: python limit20_3a.py > limit20_3a.log
Family (MODELLING CHOICE): film density 2.70 g/cm^3 and the aluminum ratio c_T/c_L of 0 K aluminum fixed (0.4982); both film speeds
scaled together, x = c_L(film)/c_L(Si); x = 0.7369 is 0 K aluminum.  Substrate: isotropic Si (Voigt, amm20_3.py).
Literature formula: t_12(0) = 4 Z1 Z2/(Z1 + Z2)^2, Z = rho c_L (eq:C.18-transmission; Swartz & Pohl, RMP 61, 605).
Fuller result: tbar_12 of amm20_3.py (P-SV and SH, all angles, weights c_nu^-2), both directions.
Leading correction: reciprocity applied to the impedance law on the slow side,
    tbar_{in->out} ~ t_12(0) min(1, n_out/n_in).
Validity (shaded): |t_12(0)/tbar - 1| <= 0.10 in both directions (root-finder on x).
DMM curves for comparison: n_out/(n_in + n_out).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from amm20_3 import SI, AL, Medium, averages, dmm

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch20")
R = AL.cT / AL.cL
XAL = AL.cL / SI.cL


def film(x):
    return Medium("film", AL.rho, cL=x * SI.cL, cT=x * SI.cL * R)


def quantities(x):
    f = film(x)
    t0 = 4 * SI.rho * SI.cL * f.rho * f.cL / (SI.rho * SI.cL + f.rho * f.cL) ** 2
    _, tsf = averages(SI, f)
    _, tfs = averages(f, SI)
    return dict(t0=t0, tsf=tsf, tfs=tfs, dsf=dmm(SI, f), dfs=dmm(f, SI),
                lsf=t0 * min(1, f.n / SI.n), lfs=t0 * min(1, SI.n / f.n), recip=SI.n * tsf / (f.n * tfs) - 1)


def worst(x):
    q = quantities(x)
    return max(abs(q["t0"] / q["tsf"] - 1), abs(q["t0"] / q["tfs"] - 1)) - 0.10


xs = np.linspace(0.35, 2.0, 166)
Q = [quantities(x) for x in xs]
w = np.array([worst(x) for x in xs])
inside = xs[w <= 0]
i0 = np.argmin(w)
lo = brentq(worst, xs[i0] - 0.3 if xs[i0] - 0.3 > 0.35 else 0.36, xs[i0])
hi = brentq(worst, xs[i0], xs[i0] + 0.4)
print(f"x = c_L(film)/c_L(Si); aluminum at x = {XAL:.4f}")
print(f"impedance law within 10% of tbar in both directions for {lo:.4f} <= x <= {hi:.4f}")
xeq = brentq(lambda x: film(x).n - SI.n, 0.5, 2.0)
print(f"equal interface densities n_film = n_Si at x = {xeq:.4f}")
print(f"max |reciprocity residual| over the grid: {max(abs(q['recip']) for q in Q):.1e}")
dev_l = max(max(abs(q["lsf"] / q["tsf"] - 1), abs(q["lfs"] / q["tfs"] - 1)) for q in Q)
print(f"leading-correction curve within {100*dev_l:.1f}% of tbar over 0.35 <= x <= 2")
for x in (0.5, XAL, 1.0, 1.5, 2.0):
    q = quantities(x)
    print(f"x = {x:.4f}: t(0) = {q['t0']:.4f}; tbar Si->film {q['tsf']:.4f}, film->Si {q['tfs']:.4f}; "
          f"reciprocity estimate {q['lsf']:.4f}/{q['lfs']:.4f}; DMM {q['dsf']:.4f}/{q['dfs']:.4f}")
qa = quantities(XAL)
print(f"Al: impedance law / tbar_esc = {qa['t0']/qa['tfs']:.3f}; reciprocity estimate / tbar_esc - 1 = {qa['lfs']/qa['tfs']-1:+.4f}")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.8, 3.6))
ax.axvspan(lo, hi, color="0.88", lw=0)
g = lambda k: np.array([q[k] for q in Q])
ax.plot(xs, g("t0"), color="k", lw=1.2, ls="--", label="impedance law $t_{12}(0)$")
ax.plot(xs, g("tsf"), color="C0", lw=1.3, label=r"$\bar t$, Si $\to$ film")
ax.plot(xs, g("tfs"), color="C3", lw=1.3, label=r"$\bar t$, film $\to$ Si")
ax.plot(xs, g("lsf"), color="C0", lw=0.8, ls="-.")
ax.plot(xs, g("lfs"), color="C3", lw=0.8, ls="-.")
# legend proxies in grey: these two line styles are drawn for both directions (blue, red)
ax.plot([], [], color="0.35", lw=0.8, ls="-.", label=r"$t_{12}(0)\min(1,\mathfrak{n}_{\rm out}/\mathfrak{n}_{\rm in})$")
ax.plot(xs, g("dsf"), color="C0", lw=0.8, ls=":")
ax.plot(xs, g("dfs"), color="C3", lw=0.8, ls=":")
ax.plot([], [], color="0.35", lw=0.8, ls=":", label="DMM")
ax.axvline(XAL, color="0.5", lw=0.6)
ax.text(XAL + 0.02, 0.03, "Al", fontsize=8, color="0.3")
ax.set_xlim(xs[0], xs[-1])
ax.set_ylim(0, 1.05)
ax.set_xlabel(r"$c_{\rm L}({\rm film})/c_{\rm L}({\rm Si})$")
ax.set_ylabel("transmission")
ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=7, frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit20_3a.pdf"))
print("wrote limit20_3a.pdf")
