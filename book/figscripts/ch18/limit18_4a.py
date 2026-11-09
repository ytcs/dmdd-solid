"""Limit Check 18.4a (lim:18.4a, fig:18-limit-a): the Klein relation eps_eh = (14/5) E_g + r_K omega_K as a truncation.
Run: python limit18_4a.py > limit18_4a.log  (about two minutes).  Reads table18_4.json (silicon w, and the constant of the
theta_ii = 3/2 model recalibrated to the silicon pair energy, which places the silicon marker).

Exact identity (two terminal carriers per pair, Sect. 18.4):  eps_eh = E_g + 2 E_f + r_K omega_K,
  E_res (printed E_f) = mean kinetic energy of a carrier when it falls below the impact threshold for good, r_K omega_K = phonon heat emitted above
  threshold per pair.  Klein's relation (Klein 1968, Eq. (3) of Wei, Wang and Mei, arXiv:1602.08005; quoted with the fitted
  r_K omega_K = 0.5 eV by Nielsen and Fischetti, arXiv:2610.16949, Sect. II) follows with
  (K1) threshold theta_ii = 3/2 and (K2) a population uniform in k below threshold, E_f = (3/5) theta_ii E_g = 0.9 E_g.
The fuller result is the energy-only random-k cascade (casc18_4.py) at theta_ii = 3/2, a = 1/2, no hole cutoff, w = omega/E_g of
silicon (63 meV / 1.160 eV), against the reduced phonon strength lambda = A_AB/E_g^3.  Klein's line is drawn with the cascade's
own phonon term, (14/5) + r_K omega_K/E_g, so the two curves differ only through (K2):  Klein - cascade = 2 (0.9 E_g - E_f)/E_g.
Validity region shaded: lambda where Klein lies within 10 % of the cascade (fine log grid, root by linear interpolation in ln lambda
between grid points 0.05 decades apart).
lambda -> 0 (no phonons): linear Richardson on h = 0.01, 0.005 (the scheme is O(h) without phonons).
"""
import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import casc18_4 as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch18")
os.makedirs(OUT, exist_ok=True)
J = json.load(open(os.path.join(HERE, "table18_4.json")))
W = J["w_Si"]

# lambda -> 0
for th in (1.0, 1.5):
    r = C.run_nophonon(th)
    c0 = r["eps"]
    Ef = r["Rpair"] / 2
    K2 = 1 + 2 * 0.6 * th
    print("lambda -> 0, theta_ii = %.1f: c0 = eps/E_g = %.4f, E_f/E_g = %.4f, phonon term %.1e (artefact of the threshold node)"
          % (th, c0, Ef, r["Ppair"]))
    print("   (K2) gives c0 = 1 + 1.2 theta = %.2f: overstates c0 by %+.1f %%; exact lies %.1f %% below (K2); (K2) E_f = %.2f E_g overstates E_f by %+.0f %%"
          % (K2, 100 * (K2 / c0 - 1), 100 * (1 - c0 / K2), 0.6 * th, 100 * (0.6 * th / Ef - 1)))

lams = 10 ** np.arange(-3.0, 2.0001, 0.05)
eg = 1.0
res = []
for lam in lams:
    X = 60.0 if lam > 5 else 40.0
    r = C.run(lam, 1.0, W, theta=1.5, X=X)
    res.append((r["eps_over_Eg"], r["Rpair"] / 2, r["Ppair"]))
res = np.array(res)
eps, Ef, Ph = res.T
klein = 2.8 + Ph
ratio = klein / eps
print("\n lambda    eps/E_g   E_f/E_g   r_K w   Klein/cascade")
for i in range(0, len(lams), 10):
    print(" %8.3g  %7.4f  %7.4f  %7.4f  %7.4f" % (lams[i], eps[i], Ef[i], Ph[i], ratio[i]))
inside = np.abs(ratio - 1) <= 0.10
# boundaries
def roots(y, target):
    out = []
    ll = np.log(lams)
    for i in range(len(y) - 1):
        if (y[i] - target) * (y[i + 1] - target) < 0:
            out.append(np.exp(ll[i] + (target - y[i]) * (ll[i + 1] - ll[i]) / (y[i + 1] - y[i])))
    return out
print("\nKlein/cascade = 1.10 at lambda =", ["%.3g" % v for v in roots(ratio, 1.10)])
print("Klein/cascade = 0.90 at lambda =", ["%.3g" % v for v in roots(ratio, 0.90)])
print("Klein/cascade = 1 (E_f = 0.9 E_g) at lambda =", ["%.3g" % v for v in roots(ratio, 1.0)])
print("ratio range over the scan: %.3f to %.3f" % (ratio.min(), ratio.max()))
# silicon point of the plot: the theta_ii = 3/2 cascade at its own silicon constant (recalibrated to 3.749 eV, table18_4.json)
lam_si = J["A_theta32"] / J["Eg_Si_123"] ** 3
rs = C.run(lam_si, 1.0, W, theta=1.5, X=40.0)
print("silicon, theta_ii = 3/2 model (A_AB = %.4f eV^3, lambda = %.3f): eps/E_g = %.4f, E_f/E_g = %.4f, Klein/cascade = %.4f"
      % (J["A_theta32"], lam_si, rs["eps_over_Eg"], rs["Rpair"] / 2, (2.8 + rs["Ppair"]) / rs["eps_over_Eg"]))
r1 = C.run(J["lam_Si"], 1.0, W, theta=1.0, X=40.0)
print("calibrated theta_ii = 1 silicon model (lambda = %.3f), for contrast: eps/E_g = %.4f, E_f/E_g = %.4f, "
      "(14/5 + r_K w)/(eps/E_g) = %.4f" % (J["lam_Si"], r1["eps_over_Eg"], r1["Rpair"] / 2, (2.8 + r1["Ppair"]) / r1["eps_over_Eg"]))

fig, ax = plt.subplots(figsize=(6.0, 3.6))
# shade between the interpolated 10 % crossings printed above (the range quoted in the caption)
x_lo = (roots(ratio, 1.10) or [lams[0]])[0]
x_hi = (roots(ratio, 0.90) or [lams[-1]])[0]
ax.axvspan(x_lo, x_hi, color="0.88", lw=0)
ax.plot(lams, eps, color="C0", lw=1.6, label=r"cascade, $\theta_{\mathrm{ii}} = 3/2$")
ax.plot(lams, klein, color="k", ls="--", lw=1.2, label=r"Klein, $14/5 + r_K\omega_K/E_{\mathrm{g}}$")
ax.plot(lams, 2 * Ef, color="C2", lw=1.0, ls="-.", label=r"$2\bar E_{\mathrm{res}}/E_{\mathrm{g}}$ (cascade)")
ax.axhline(1.8, color="C2", lw=0.7, ls=(0, (1, 3)))
ax.text(1.3e-3, 1.72, r"$2\bar E_{\mathrm{res}} = 1.8E_{\mathrm{g}}$ (uniform population)", fontsize=7.5, color="C2", va="top")
ax.axvline(lam_si, color="0.5", lw=0.6)
ax.text(lam_si * 1.1, 0.75, "Si", fontsize=8, color="0.3")
ax.set_xscale("log")
ax.set_xlim(1e-3, 100)
ax.set_ylim(0.5, 6.5)
ax.set_xlabel(r"phonon strength $\lambda_{\mathrm{AB}} = A_{\mathrm{AB}}/E_{\mathrm{g}}^3$")
ax.set_ylabel(r"$\varepsilon_{\mathrm{eh}}/E_{\mathrm{g}}$")
ax.legend(fontsize=7.5, loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit18_4a.pdf"))
print("wrote limit18_4a.pdf")
