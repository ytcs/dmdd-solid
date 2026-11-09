"""Limit 11.5c (Sect. 11.5): the Markov-Krein band, absolute and not relative.  STYLE fallback: the band around model
distributions with given first five moments (no exact anharmonic response is computed).
Output: tex/figures/ch11/limit11_5c.pdf. Prints every number of the box and of its F row.

x = xi = (omega - mu_1)/sigma (threshold in units of the rms width).  Curves (log scale):
  rho_MK(xi), the width of the band eq:C.10-band, for the standard Gaussian (eq:C.10-gauss, 2/(3 + xi^4)) and for the silicon
    response at q = 100 keV (mk11.py; T = 0, harmonic, PBE density of states, skewness 0.553, kurtosis 3.333);
  the tail asymptote eq:C.10-tail, (mubar_4 - mubar_2^2 - mubar_3^2/mubar_2)/xi^4 in these units (the leading correction to the
    band far from the mean);
  1 - F(xi), the weight above a threshold at xi, for the same two distributions (what a threshold rate needs).
Gray band: thresholds xi at which the band fixes the silicon weight above threshold to 10 %, rho_MK <= 0.1 (1 - F).
"""
import os
import sys
import numpy as np
from scipy.special import erfc
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import imp11 as I  # noqa: E402
import mk11 as K  # noqa: E402

if __name__ == "__main__":
    q = 100e3
    w, s, e0, F, mu, num = K.si_response(q)
    zm, m1, sig = K.standardize(mu)
    xs = np.linspace(-m1 / sig, 6, 1001)            # omega >= 0
    lo, hi, rho, nmin = K.band(zm, xs)
    rg = K.gauss_rho(xs)
    with np.errstate(divide="ignore"):
        tail_g = 2 / xs**4
        tail_si0 = 1 / xs**4
    num_si = zm[4] - 1 - zm[3]**2
    tail_si = num_si * tail_si0
    Fsi = np.interp(m1 + sig * xs, w, F, left=0.0, right=1.0)
    Fsi = np.where(m1 + sig * xs < 0, 0.0, Fsi)
    Gs = 1 - Fsi
    Gg = 0.5 * erfc(xs / np.sqrt(2))
    print("silicon q = 100 keV: tail numerator mubar4 - 1 - mubar3^2 = %.3f (Gaussian 2)" % num_si)
    for x in (-2, -1, 0, 1, 2, 3, 4, 5):
        _, _, rx, _ = K.band(zm, [float(x)])
        gx = 1 - np.interp(m1 + sig * x, w, F)
        print("xi = %+d: rho Gauss %.4f, rho Si %.4f, tail form Si %.4f; 1-F Gauss %.3e, 1-F Si %.3e; ratio rho/(1-F) Si %.3g"
              % (x, K.gauss_rho(x), rx[0], num_si / x**4 if x else np.nan, 0.5 * erfc(x / np.sqrt(2)), gx, rx[0] / gx))
    ok = rho <= 0.1 * Gs
    print("band fixes the Si weight above threshold to 10 %% for xi <= %.2f (omega <= %.1f meV = %.3f E_R)"
          % (xs[ok].max(), (m1 + sig * xs[ok].max()) * 1e3, (m1 + sig * xs[ok].max()) / I.e_r(q)))
    okg = rg <= 0.1 * Gg
    print("Gaussian: same for xi <= %.2f" % xs[okg].max())
    for x in (3, 4, 5, 6):
        _, _, rx, _ = K.band(zm, [float(x)])
        print("xi = %d: exact rho Si / tail form = %.3f; rho Gauss / (2/xi^4) = %.3f" % (x, rx[0] / (num_si / x**4), K.gauss_rho(x) / (2 / x**4)))
    g3 = 0.5 * erfc(3 / np.sqrt(2))
    print("Gaussian at xi = 3: 1 - F = %.3e, band upper end of 1 - F = rho = %.3e, ratio %.0f" % (g3, K.gauss_rho(3), K.gauss_rho(3) / g3))

    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.axvspan(xs[0], xs[ok].max(), color="0.88", lw=0)
    ax.plot(xs, rho, color="C0", lw=1.5, label=r"$\varrho_{\mathrm{MK}}$, silicon, 100 keV")
    ax.plot(xs, rg, color="C3", lw=1.2, label=r"$\varrho_{\mathrm{MK}}$, Gaussian")
    m = xs > 1.2
    ax.plot(xs[m], tail_si[m], color="C0", lw=0.9, ls="--", label=r"tail form, silicon")
    ax.plot(xs, Gs, color="C0", lw=1.0, ls=":", label=r"$1 - F$, silicon")
    ax.plot(xs, Gg, color="C3", lw=1.0, ls=":", label=r"$1 - F$, Gaussian")
    ax.set_yscale("log")
    ax.set_xlim(xs[0], xs[-1])
    ax.set_ylim(1e-6, 1.5)
    ax.set_xlabel(r"threshold $\xi = (\omega - \mu_1)/\sigma$")
    ax.set_ylabel("weight")
    ax.legend(fontsize=7, frameon=False, loc="lower left")
    fig.tight_layout()
    outp = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_5c.pdf")
    fig.savefig(outp)
    print("wrote", os.path.normpath(outp))
