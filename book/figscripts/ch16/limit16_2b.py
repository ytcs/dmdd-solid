"""Limit Check 16.2b (acoustic plasmon of two components, Landau width) of Sect. 16.2: plot and caption numbers.

Output: tex/figures/ch16/limit16_2b.pdf.
Two species: a light one (Fermi velocity v_Fl) that screens, a heavy one treated as dynamic (cold), with
v_a = omega_ph/k_TFl in 3D and v_a = sqrt(n_h/(m_h N_l)) in both dimensions (Sect. 16.2).  With x = v_a/v_Fl and
nu = omega/(q v_Fl):
  3D: eps = 1 + (k_TFl/q)^2 [f3(nu) - x^2/nu^2],   2D: eps = 1 + (q_s/q) [f2(nu) - x^2/nu^2],
f3, f2 the q << k_F Lindhard functions of lowd16_2 (Eq. 4.5-lindhard; Stern's 2D function at q << k_F).
Literature form of the width (FWHM over frequency), 3D: Gamma_a/omega_a = (pi/2) x (2507.07164 demon; derived in
Sect. 16.2 from Im f3 = (pi/2) nu); the 2D analogue from Im f2 = nu/sqrt(1-nu^2) is x/sqrt(1-x^2).
Fuller result: FWHM of L = Im(-1/eps) computed with the full nu dependence of f3, f2, at q = 0.02 k_TFl (3D) and
q = 0.02 q_s (2D).  The 3D fuller curve is drawn to v_a/v_Fl = 0.4, beyond which the line is too broad for a width.
Shaded: dark, the 3D form within 10 % of its fuller result; light, the 2D form within 10 % of its fuller result.
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lowd16_2 as L

QR = 0.02   # q/k_TF (3D) and q/q_s (2D)


def width(x, dim):
    lo, hi = x * 0.3, min(x * 2.5, 0.9999)
    nu = np.linspace(lo, hi, 400001)
    if dim == 3:
        eps = 1 + (1 / QR) ** 2 * (L.f3(nu) - x ** 2 / nu ** 2)
    else:
        eps = 1 + (1 / QR) * (L.f2(nu) - x ** 2 / nu ** 2)
    Lf = np.imag(-1 / eps)
    pk, fw = L.fwhm(nu, Lf)
    if Lf[-1] > Lf.max() / 2 or Lf[0] > Lf.max() / 2:
        return np.nan, pk / x      # half maximum outside the sampled band: width not defined
    return fw / pk, pk / x


def form(x, dim):
    return np.pi / 2 * x if dim == 3 else x / np.sqrt(1 - x ** 2)


xs = np.geomspace(0.02, 0.6, 60)
ex3 = np.array([width(x, 3)[0] for x in xs])
ex2 = np.array([width(x, 2)[0] for x in xs])
f3 = form(xs, 3)
f2 = form(xs, 2)
r3 = lambda x: form(x, 3) / width(x, 3)[0] - 1
r2 = lambda x: form(x, 2) / width(x, 2)[0] - 1
for x in [0.02, 0.05, 0.1, 0.157, 0.2, 0.3, 0.5]:
    w3, s3 = width(x, 3)
    w2, s2 = width(x, 2)
    print(f"  v_a/v_Fl = {x}: 3D exact {w3:.4f} vs (pi/2)x {form(x,3):.4f} (peak at {s3:.4f} v_a q); "
          f"2D exact {w2:.4f} vs x/sqrt(1-x^2) {form(x,2):.4f} (peak at {s2:.4f} v_a q)")
x3 = brentq(lambda x: abs(r3(x)) - 0.1, 0.05, 0.75)
x2 = brentq(lambda x: abs(r2(x)) - 0.1, 0.05, 0.59)
print(f"  10% points: 3D at v_a/v_Fl = {x3:.3f}, 2D at v_a/v_Fl = {x2:.3f}")
print(f"  2D exact vs the 3D coefficient (pi/2)x at x = 0.1: ratio {form(0.1,3)/width(0.1,2)[0]:.3f}")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 2.9))
ax.axvspan(xs[0], x2, color="0.93", lw=0)
ax.axvspan(xs[0], x3, color="0.84", lw=0)
ax.loglog(xs, f3, color="k", lw=1.0, ls="--", label=r"$(\pi/2)\,v_a/v_{\mathrm{F},l}$ (3D)")
m3 = xs <= 0.4
ax.loglog(xs[m3], ex3[m3], color="C3", lw=1.4, label="3D, full Lindhard, light species")
ax.loglog(xs, f2, color="0.4", lw=1.0, ls=":", label=r"$v_a/v_{\mathrm{F},l}$ over $(1 - v_a^2/v_{\mathrm{F},l}^2)^{1/2}$ (2D)")
ax.loglog(xs, ex2, color="C0", lw=1.4, label="2D, full Lindhard, light species")
ax.set_xlabel(r"$v_a/v_{\mathrm{F},l}$")
ax.set_ylabel(r"$\Gamma_a/\omega_a$ (full width at half maximum)")
ax.set_xlim(xs[0], xs[-1])
from matplotlib.ticker import FixedLocator, FixedFormatter, NullFormatter
ax.xaxis.set_major_locator(FixedLocator([0.02, 0.05, 0.1, 0.2, 0.5]))
ax.xaxis.set_major_formatter(FixedFormatter(["0.02", "0.05", "0.1", "0.2", "0.5"]))
ax.xaxis.set_minor_formatter(NullFormatter())
ax.legend(fontsize=7, frameon=False, loc="upper left")
fig.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tex/figures/ch16/limit16_2b.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
