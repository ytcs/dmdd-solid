"""Fig. 11.4 (Sect. 11.4): the silicon nuclear response approaching the impulse peak as q grows.
Output: tex/figures/ch11/fig11_4.pdf. Prints the numbers quoted in the caption and the text.

Model: incoherent T = 0 self response of one nucleus (eq:11.3-inc, one species), from the PBE density of states of Sect. 5.2,
evaluated by FFT of the generating function (imp11.spectrum); zero-phonon term e^{-2W} delta(omega) removed and its weight
printed. Plotted as E_R s(q, omega) against omega/E_R, so that the free recoil is delta(omega/E_R - 1) and the impulse Gaussian
(eq:11.4-IAgauss, variance 4 E_R K, K = <omega>/4 = 10.2 meV) has rms width x_R^{-1/2}. q = 50, 100, 200, 400 keV.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import imp11 as I  # noqa: E402

QS = (50e3, 100e3, 200e3, 400e3)
COL = ("C1", "C3", "C0", "k")
fig, ax = plt.subplots(figsize=(5.0, 3.3))
for q, c in zip(QS, COL):
    ER = I.e_r(q)
    xr = ER / I.W_MEAN
    w, s, e0 = I.spectrum(q, h=I.DW, wtop=3.2 * ER + 0.1)
    # resolve the plotted curve on 0.2 % of E_R
    x = w / ER
    y = s * ER
    g = I.gauss(w, q) * ER
    m = x <= 3
    ax.plot(x[m], y[m], color=c, lw=1.1, label=r"$q = %d$ keV, $x_R = %.1f$" % (q / 1e3, xr))
    ax.plot(x[m], g[m], color=c, lw=0.9, ls="--")
    imax = np.argmax(s)
    half = s >= s.max() / 2
    print("q = %3.0f keV: E_R = %6.1f meV, x_R = %5.2f, 2W = %5.2f, zero-phonon weight e^-2W = %.2e, mode/E_R = %.3f, "
          "peak height exact/Gaussian = %.2f, FWHM/E_R exact %.3f vs Gaussian %.3f, max|exact-Gauss|/Gauss peak = %.3f"
          % (q / 1e3, ER * 1e3, xr, I.two_w(q), e0, w[imax] / ER, s.max() / I.gauss(ER, q),
             (w[half].max() - w[half].min()) / ER, 2.3548 * np.sqrt(4 * ER * I.kin_q(0)) / ER,
             np.max(np.abs(s - I.gauss(w, q))) / I.gauss(ER, q)))
ax.axvline(1.0, color="0.5", lw=0.8, ls=":")
ax.set_xlim(0, 3)
ax.set_ylim(0, None)
ax.set_xlabel(r"$\omega/E_R$")
ax.set_ylabel(r"$E_R\,\Omega S_A/(2\pi n_{\mathrm{at}}A^2)$")
ax.legend(fontsize=7, frameon=False, loc="upper right")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "fig11_4.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
