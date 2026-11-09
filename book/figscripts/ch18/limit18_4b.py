"""Limit Check 18.4b (lim:18.4b, fig:18-limit-b): the cascade against Ramanathan and Kurinsky's fitted planes.
Run: python limit18_4b.py > limit18_4b.log  (about one minute).

Formula tested (Ramanathan and Kurinsky, arXiv:2004.10709, Eqs. (12)-(13), least-squares planes through their Monte Carlo at
~100 eV deposits):  eps_eh = 1.7 E_g + 0.084 A + 1.3,  F_eh = -0.028 E_g + 0.0015 A + 0.14  (eV; A in their units, numerically
A_AB in eV^3).  Their Monte Carlo states F constant at the 2 % level with point scatter from Monte Carlo statistics (p. 6 and
Fig. 3 caption).  Their parameters: omega = 63 meV, hole band width 12 eV, free particles (a = 1/2), threshold E_g (theta_ii = 1).
The fuller result here is the deterministic moment solution of the same energy-only random-k model (casc18_4.py) with these
parameters; it omits their explicit plasmon channel and their re-splitting of hole energy above the band width.
Scan: A from 1 to 12 at E_g = 1.124 eV (their 300 K slice); points E_g = 1.0, 1.2 eV at A = 5.2.
Validity region shaded: A where both ratios lie within 2 % of one (their stated Monte Carlo scatter), from the scan grid refined by
linear interpolation.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import casc18_4 as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch18")
os.makedirs(OUT, exist_ok=True)

def plane(Eg, A):
    return 1.7 * Eg + 0.084 * A + 1.3, -0.028 * Eg + 0.0015 * A + 0.14

OM, BH = 0.063, 12.0
pts = {}
print(" A     E_g    eps solver  eps plane  dev     F solver  F plane  dev")
for A, Eg in ((3.0, 1.124), (5.2, 1.124), (7.0, 1.124), (5.2, 1.0), (5.2, 1.2)):
    r = C.run(A, Eg, OM, Bh=BH, X=40.0)
    e, f = plane(Eg, A)
    pts[(A, Eg)] = (r["eps"], r["F"])
    print(" %.1f  %.3f  %.4f      %.4f     %+.2f%%  %.5f   %.5f  %+.2f%%" % (A, Eg, r["eps"], e, 100 * (r["eps"] / e - 1), r["F"], f, 100 * (r["F"] / f - 1)))
devE = [abs(pts[k][0] / plane(k[1], k[0])[0] - 1) for k in pts]
devF = [abs(pts[k][1] / plane(k[1], k[0])[1] - 1) for k in pts]
print("max |dev| over the five points: eps %.2f %%, F %.2f %%" % (100 * max(devE), 100 * max(devF)))
sl = lambda k1, k2, i, d: (pts[k2][i] - pts[k1][i]) / d
print("secant slopes: d eps/dA %.4f (plane 0.084), dF/dA %.5f (plane 0.0015), d eps/dE_g %.3f (plane 1.7), dF/dE_g %.4f (plane -0.028)"
      % (sl((3.0, 1.124), (7.0, 1.124), 0, 4.0), sl((3.0, 1.124), (7.0, 1.124), 1, 4.0), sl((5.2, 1.0), (5.2, 1.2), 0, 0.2), sl((5.2, 1.0), (5.2, 1.2), 1, 0.2)))
print("solver F at (5.2, 1.124) = %.4f against their asymptotic F_inf = 0.115 (p. 6): %+.2f %%" % (pts[(5.2, 1.124)][1], 100 * (pts[(5.2, 1.124)][1] / 0.115 - 1)))

As = np.arange(1.0, 12.001, 0.25)
rE, rF = [], []
for A in As:
    r = C.run(A, 1.124, OM, Bh=BH, X=40.0)
    e, f = plane(1.124, A)
    rE.append(r["eps"] / e)
    rF.append(r["F"] / f)
rE, rF = np.array(rE), np.array(rF)
ok = (np.abs(rE - 1) <= 0.02) & (np.abs(rF - 1) <= 0.02)
for i in range(0, len(As), 4):
    print("  A = %5.2f: eps ratio %.4f, F ratio %.4f" % (As[i], rE[i], rF[i]))
def cross(y, t):
    out = []
    for i in range(len(y) - 1):
        if (y[i] - t) * (y[i + 1] - t) < 0:
            out.append(As[i] + (t - y[i]) * (As[i + 1] - As[i]) / (y[i + 1] - y[i]))
    return out
print("F ratio = 0.98 at A =", ["%.2f" % v for v in cross(rF, 0.98)], "; = 1.02 at", ["%.2f" % v for v in cross(rF, 1.02)])
print("eps ratio = 0.98 at A =", ["%.2f" % v for v in cross(rE, 0.98)], "; = 1.02 at", ["%.2f" % v for v in cross(rE, 1.02)])
idx = np.where(ok)[0]
print("both within 2 %% for A in [%.2f, %.2f] on the 0.25 grid" % (As[idx[0]], As[idx[-1]]))
lo = max([As[idx[0]]] + [v for v in cross(rF, 0.98) + cross(rE, 0.98) if v <= As[idx[0]]])
lo = min([v for v in cross(rF, 0.98) + cross(rE, 0.98) + cross(rF, 1.02) + cross(rE, 1.02) if v <= As[idx[0]] + 1e-9] or [As[idx[0]]], key=lambda v: abs(v - As[idx[0]]))
hi = min([v for v in cross(rF, 0.98) + cross(rE, 0.98) + cross(rF, 1.02) + cross(rE, 1.02) if v >= As[idx[-1]] - 1e-9] or [As[idx[-1]]], key=lambda v: abs(v - As[idx[-1]]))
print("validity (both within 2 %%): A from %.2f to %.2f" % (lo, hi))

fig, ax = plt.subplots(figsize=(6.0, 3.5))
ax.axvspan(lo, hi, color="0.88", lw=0)
ax.axhspan(0.98, 1.02, color="C0", alpha=0.08, lw=0)
ax.plot(As, rE, color="C0", lw=1.6, label=r"$\varepsilon_{\mathrm{eh}}$: cascade / plane")
ax.plot(As, rF, color="C1", lw=1.6, ls="--", label=r"$F_{\mathrm{eh}}$: cascade / plane")
for (A, Eg), (e, f) in pts.items():
    if Eg != 1.124:
        ax.plot([A], [e / plane(Eg, A)[0]], "o", ms=4, mfc="none", color="C0")
        ax.plot([A], [f / plane(Eg, A)[1]], "s", ms=4, mfc="none", color="C1")
ax.axhline(1.0, color="k", lw=0.7)
ax.axvline(5.2, color="0.5", lw=0.6, ls=":")
ax.text(5.3, 1.046, r"$A = 5.2$", fontsize=8, color="0.3")
ax.set_xlim(1, 12)
ax.set_ylim(0.92, 1.06)
ax.set_xlabel(r"phonon-to-ionization constant $A_{\mathrm{AB}}$ (eV$^3$)")
ax.set_ylabel("cascade / fitted plane")
ax.legend(fontsize=7.5, loc="lower right", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit18_4b.pdf"))
print("wrote limit18_4b.pdf")
