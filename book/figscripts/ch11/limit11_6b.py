"""Limit 11.6b (fig:11-limit-6b): local density of states of one mass defect in silicon (Lifshitz; Dawber and Elliott for cubic
crystals). STYLE fallback: no many-defect calculation is done, so the plot shows the exact single-defect result against frequency, with
the frequencies where the leading pair term exceeds 10 % shaded.
Single defect of mass M_i = Mbar (1 - delta): G_i = G_h/(1 + delta Mbar w^2 G_h) (Eq. 11.6-lifshitz), g_i = (2 w M_i/pi) 3 Im G_i.
Above the band a light defect (delta > delta_c) has a local mode where 1 + delta Mbar w^2 Re G_h = 0; its weight in g_i/3 is printed.
Pair term (leading, linear in the second defect's t-matrix): another defect j at site r changes the host Green function at site 0 to
  G' = G_h + G_0r t_j G_r0,  t_j = -delta_j Mbar w^2 / (1 + delta_j Mbar w^2 G_h),
and summed over all r != 0 with occupation x_j,  sum_r G_0r G_r0 = (G^2)_00 - G_00^2,  (G^2)_00 = dG_h/d(Mbar w^2),
so  Mbar dG' = -sum_j x_j delta_j w^2/(1 + delta_j u) [d(Mbar G_h)/d(w^2) - (Mbar G_h)^2],  u = Mbar w^2 G_h,
fed to first order into the Dyson equation of defect 0: dG_0 = dG'/(1 + delta_0 u)^2. Shaded where |Im dG_0/Im G_0| > 0.10.
Cases: 30Si in natural Si (environment: the natural mixture referenced to Mbar, whose first order cancels, sum x_j delta_j = 0);
a heavy defect delta = -0.5 and a light defect delta = +0.3 (M = 1.5 Mbar, 0.7 Mbar), each at concentration x = 1 % (modelling
choice, stated in the caption). Inputs: iso11.py (PBE DOS of Sect. 5.2).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import iso11 as I  # noqa: E402


def dmG(om, h=2e-4):
    """d(Mbar G_h)/d(omega^2) by a central difference in omega (checked against the Debye closed form to 1e-4)."""
    return (I.mG(om + h) - I.mG(om - h)) / (2 * h) / (2 * om)


def pair_ratio(om, d0, env):
    g = I.mG(om)
    u = om**2 * g
    corr = sum(-x * d * om**2 / (1 + d * u) for x, d in env) * (dmG(om) - g**2)
    return (corr / (1 + d0 * u)**2).imag / (g / (1 + d0 * u)).imag


om = np.linspace(0.6e-3, I.WMAX * 0.999, 1800)
Dh = np.interp(om, I.W, I.D)
nat = list(zip(I.X, I.DELTA))
cases = [("30Si", I.DELTA[2], nat, "C3"), ("heavy", -0.5, [(0.01, -0.5)], "C0"), ("light", 0.3, [(0.01, 0.3)], "C2")]

fig, ax = plt.subplots(figsize=(5.0, 3.3))
ax.plot(om * 1e3, Dh, color="k", ls="--", lw=1.0, label="host")
ymax = 220
for name, d, env, col in cases:
    r = I.ldos_ratio(om, d)
    pr = pair_ratio(om, d, env)
    big = np.abs(pr) > 0.10
    lab = {"30Si": r"$^{30}$Si, $\delta^M = -0.067$", "heavy": r"$\delta^M = -0.5$", "light": r"$\delta^M = +0.3$"}[name]
    ax.plot(om * 1e3, r * Dh, color=col, lw=1.3, label=lab)
    w_in = np.sum(0.5 * (r[1:] * Dh[1:] + r[:-1] * Dh[:-1]) * np.diff(om))
    first_big = om[big].min() * 1e3 if big.any() else np.nan
    print(f"{name}: delta = {d:+.4f}, in-band weight {w_in:.4f}; |pair| > 10 % at {big.sum()} of {om.size} points, "
          f"lowest {first_big:.2f} meV; max |pair| below 55 meV = {np.max(np.abs(pr[om < 0.055])):.2e}")
    if big.any():
        # shade contiguous runs of big pair terms at the height band of this curve
        idx = np.where(big)[0]
        runs = np.split(idx, np.where(np.diff(idx) > 1)[0] + 1)
        for rr in runs:
            ax.axvspan(om[rr[0]] * 1e3, om[rr[-1]] * 1e3, color=col, alpha=0.18, lw=0)
    lm = I.local_mode(d)
    if lm is not None:
        o, wgt = lm
        print(f"   local mode at {o*1e3:.2f} meV ({o/I.WMAX:.3f} omega_max), weight {wgt:.4f}; in-band + mode = {w_in + wgt:.4f}")
        # pair term at the local mode: the second defect shifts the pole; first-order shift of 1 + delta u
        ax.annotate("", xy=(o * 1e3, 0.0), xytext=(o * 1e3, ymax * 0.8),
                    arrowprops=dict(arrowstyle="<-", color=col, lw=1.3))
        ax.text(o * 1e3 + 0.6, ymax * 0.8, f"local\nmode,\nweight\n{wgt:.2f}", color=col, fontsize=7, ha="left", va="top")
gc = I.mG(np.array([I.WMAX * 1.0005]))[0].real * (I.WMAX * 1.0005)**2
print(f"critical light defect for a local mode: delta_c = {-1/gc:.3f} (M < {1 + 1/gc:.3f} Mbar)")
ax.set_xlim(0, 72)
ax.set_ylim(0, ymax)
ax.set_xlabel(r"$\omega$ (meV)")
ax.set_ylabel(r"$g_i(\omega)/3$ (eV$^{-1}$)")
ax.legend(fontsize=7, frameon=False, loc="upper left")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_6b.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
