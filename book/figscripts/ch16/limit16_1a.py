"""Limit Check 16.1a (lim:16.1a, fig:16-limit-dirac): the published Dirac-material rates against the rates with the
background dielectric constant in the total epsilon, as functions of eps_bg.

Model: the gapped isotropic benchmark of Hochberg et al., arXiv:1708.08929 (Fig. 4 caption): v_D = 4e-4,
Delta_D = 2.5 meV, g = 2, Lambda_D = 0.2 keV read as a hard cutoff (Lt = 80 meV); eps_bg varied from 1 to 1000 at fixed
v_D, Delta_D, Lambda_D, so that eps_D = -v_C R0_D is fixed and only the background changes.
Scattering: total rate at m_chi = 100 keV, light mediator, book halo (rate10_2.py), eq:10.2-rate with
  total eps:    L = Im eps_D/|eps_bg + eps_D|^2                 (solid blue)
  published:    L_src = Im eps_D/|1 + eps_D/eps_bg|^2 = eps_bg^2 L   (dashed blue; 1708.08929 Eqs. (3.7), (3.11))
  leading form: Im eps_D/eps_bg^2                               (dotted blue; weak screening, Re eps_D dropped)
Absorption at m_phi = 50 meV (q -> 0): Gamma = zeta^2 m Im(-1/eps) (solid orange) against the published
  zeta^2 m Im(eps/eps_bg)/|eps/eps_bg|^2 = eps_bg Gamma (dashed orange; 1708.08929 Eqs. (4.4)-(4.5)).
All curves are divided by their common value at eps_bg = 1, where the two rules coincide.
Shaded gray: eps_bg^2 <= 1.1, where the published scattering rate is within 10 % (eps_bg <= 1.0488; absorption within
10 % for eps_bg <= 1.1).  Hatched: alpha~ = alpha/(eps_bg v_D) < 1, eps_bg > alpha/v_D = 18.24, where one-loop RPA is
used (the weak-screening condition).  Dash-dotted: eps_bg = 40, the published benchmark.
Run: python limit16_1a.py > limit16_1a.log   (a few seconds)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import dirac16 as d

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch16", "limit16_1a.pdf")
b = d.BENCH
vD, g, D, Lt = b["vD"], b["g"], b["D"], b["Lt"]
Bt = d.Btab(D, Lt)
m, mphi = 1e5, 0.05
E = np.geomspace(1, 1000, 61)
rho = 1.0 * d.GCM3          # cancels in the normalized curves
out = {k: [] for k in ("book", "src", "lead")}
for e in E:
    for rule in out:
        Lf = lambda q, w, rule=rule, e=e: d.L_iso(q, w, vD, g, e, Bt, rule)  # noqa: E731
        out[rule].append(d.scatter_rate(m, Lf, 2 * D * (1 + 1e-6), 2 * Lt, 2 * Lt / vD, rho))
out = {k: np.array(x) for k, x in out.items()}
eD = g * d.ALPHA / (6 * np.pi * vD) * Bt(mphi**2)
Ab = eD.imag / np.abs(E + eD) ** 2
As = (eD.imag / E) / np.abs(1 + eD / E) ** 2
n0 = out["book"][0]
print("eps_D at m_phi = 50 meV: %.3f + %.3fi (independent of eps_bg)" % (eD.real, eD.imag))
print("ratio published/total, scattering: min %.6f max %.6f of eps_bg^2" % ((out["src"] / out["book"] / E**2).min(), (out["src"] / out["book"] / E**2).max()))
print("ratio published/total, absorption: exactly eps_bg (%.3e deviation)" % np.max(np.abs(As / Ab / E - 1)))
for e in (1, 18.24, 40, 100, 1000):
    j = np.argmin(np.abs(E - e))
    print("eps_bg = %7.2f: scattering total %.3e, published %.3e, leading %.3e (total/leading %.3f) ; absorption total %.3e, published %.3e"
          % (E[j], out["book"][j] / n0, out["src"][j] / n0, out["lead"][j] / n0, out["book"][j] / out["lead"][j], Ab[j] / Ab[0], As[j] / Ab[0]))
print("published scattering rate at eps_bg = 1000 over the unscreened Dirac rate (eps_bg^2 x leading form): %.3f" % (out["src"][-1] / (E[-1]**2 * out["lead"][-1])))
e1 = np.sqrt(1.1)
eA = d.ALPHA / vD
print("published within 10 %% for eps_bg <= %.4f (scattering), %.2f (absorption); alpha~ < 1 for eps_bg > %.2f" % (e1, 1.1, eA))

fig, ax = plt.subplots(figsize=(5.2, 3.6))
ax.axvspan(1, e1, color="0.7", lw=0)
ax.annotate("published form\nwithin 10 %", xy=(1.03, 3e3), xytext=(1.6, 3e3), fontsize=7, color="0.25", va="center",
            arrowprops=dict(arrowstyle="->", color="0.4", lw=0.6))
ax.axvspan(eA, 1000, facecolor="none", edgecolor="0.82", hatch="///", lw=0)
ax.loglog(E, out["book"] / n0, color="C0", lw=1.6, label="scattering, total $\\varepsilon$")
ax.loglog(E, out["src"] / n0, color="C0", lw=1.2, ls="--", label="scattering, published form")
ax.loglog(E, out["lead"] / n0, color="C0", lw=1.0, ls=":", label="scattering, leading weak-screening form")
ax.loglog(E, Ab / Ab[0], color="C1", lw=1.6, label="absorption, total $\\varepsilon$")
ax.loglog(E, As / Ab[0], color="C1", lw=1.2, ls="--", label="absorption, published form")
ax.axvline(40, color="0.3", lw=0.8, ls="-.")
ax.text(42, 2e-5, "benchmark\n$\\varepsilon_{\\mathrm{bg}} = 40$", fontsize=7, color="0.25")
ax.text(eA * 1.15, 2e3, "$\\tilde\\alpha < 1$", fontsize=8, color="0.3")
ax.set_xlim(1, 1000)
ax.set_ylim(1e-6, 1e5)
ax.set_xlabel("background dielectric constant $\\varepsilon_{\\mathrm{bg}}$")
ax.set_ylabel("rate / rate at $\\varepsilon_{\\mathrm{bg}} = 1$")
ax.legend(fontsize=6.5, loc="lower left", frameon=False)
fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT)
print("wrote", os.path.relpath(OUT, HERE))
# maximum of the published absorption rate over eps_bg: d/de [e/|e + eps_D|^2] = 0 at e = |eps_D|
emax = abs(eD)
Eg = np.geomspace(1, 1000, 200001)
num = Eg / np.abs(Eg + eD) ** 2
print("published absorption rate is largest at eps_bg = |eps_D| = %.3f (fine grid: %.3f); total-eps rates fall monotonically: %s"
      % (emax, Eg[np.argmax(num)], bool(np.all(np.diff(out["book"]) < 0) and np.all(np.diff(Ab) < 0))))
