"""Fig. 11.5 (Sect. 11.5): the Markov-Krein band around the cumulative nuclear response of silicon.
Output: tex/figures/ch11/fig11_5.pdf. Prints the numbers quoted in the caption and the text.

Response: incoherent self response of silicon at T = 0 from the PBE density of states of Sect. 5.2 (imp11.py, mk11.py), all
  phonon orders, zero-phonon weight e^{-2W} at omega = 0 included in the cumulative F(omega).  Panels: q = 100 keV (x_R = 4.67,
  the momentum of WE 11.5) and q = 50 keV (x_R = 1.17, phonon bands still visible).
Band: eq:C.10-band from the five moments mu_0..mu_4, which are those of the cumulants c_k = E_R <omega^(k-1)> (eq:D.32-ck);
  the numerical moments of the spectrum are printed as a check.
Half line: the response vanishes for omega < 0 at T = 0.  Where all three nodes of the canonical representation through xi
  are >= 0, the extremal distribution is itself admissible on omega >= 0 and the band is sharp there too; elsewhere the
  half-line band is narrower than the one drawn (hatched range printed and marked by a bar).
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
import mk11 as K  # noqa: E402

if __name__ == "__main__":
    fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.9), sharey=True)
    for ax, qk, tag in zip(axs, (100, 50), ("(a)", "(b)")):
        q = qk * 1e3
        w, s, e0, F, mu, num = K.si_response(q)
        ER = I.e_r(q)
        zm, m1, sig = K.standardize(mu)
        print("q = %d keV: E_R = %.1f meV, x_R = %.2f, e^-2W = %.3e, sigma_omega = %.1f meV" % (qk, ER * 1e3, ER / I.W_MEAN, e0, sig * 1e3))
        print("   moments mu_1..mu_4 analytic %s; numerical/analytic %s" % (np.array2string(mu[1:], precision=4),
              np.array2string(num[1:] / mu[1:], precision=6)))
        print("   standardized skewness %.3f, kurtosis %.3f (Gaussian 3)" % (zm[3], zm[4]))
        x = w / ER
        xis = np.linspace(-1.0, 4.0, 1001) * ER
        z = (xis - m1) / sig
        lo, hi, rho, nmin = K.band(zm, z)
        pos = xis >= 0
        neg_in = (nmin * sig + m1 < 0) & pos
        # intervals of xi >= 0 in which a canonical node lies below omega = 0
        edges = np.flatnonzero(np.diff(neg_in.astype(int)))
        ivs, start = [], (xis[0] if neg_in[0] else None)
        for e in edges:
            if neg_in[e + 1]:
                start = xis[e + 1]
            else:
                ivs.append((start, xis[e])); start = None
        if start is not None:
            ivs.append((start, xis[-1]))
        print("   xi >= 0 with a canonical node below omega = 0: " + ", ".join("[%.3f, %.3f] E_R" % (a / ER, b / ER) for a, b in ivs))
        print("   width of the band on those intervals: max rho = %.3f" % (rho[neg_in].max() if neg_in.any() else 0))
        # half-line point-mass bound eq:C.10-stieltjes, second entry [xi u^T H1^-1 u]^-1 with raw moments
        H1 = np.array([[mu[1], mu[2]], [mu[2], mu[3]]])
        st = np.array([1 / (x0 * np.array([1, x0]) @ np.linalg.solve(H1, np.array([1, x0]))) if x0 > 0 else np.inf for x0 in xis])
        red = np.where(pos, np.minimum(1, st / rho), 1)
        jr = np.argmin(red)
        print("   half-line point-mass bound (eq:C.10-stieltjes) below rho_MK by at most %.1f %% (at xi = %.3f E_R: %.3f vs %.3f)"
              % ((1 - red[jr]) * 100, xis[jr] / ER, st[jr], rho[jr]))
        for a, b in ivs:
            m = (xis >= a) & (xis <= b)
            print("      on [%.3f, %.3f] E_R: largest reduction %.1f %%" % (a / ER, b / ER, (1 - red[m].min()) * 100))
        j = np.argmin(np.abs(xis - ER))
        Fe = np.interp(ER, w, F)
        print("   at xi = E_R: rho = %.3f, band [%.3f, %.3f], F(E_R) = %.3f" % (rho[j], lo[j], hi[j], Fe))
        jm = np.argmax(s)
        print("   maximum of the spectrum at %.1f meV = %.3f E_R; rho there %.3f" % (w[jm] * 1e3, w[jm] / ER,
              rho[np.argmin(np.abs(xis - w[jm]))]))
        Fint = np.interp(xis, w, F, left=0.0)
        inside = np.all((Fint[pos] >= lo[pos] - 2e-3) & (Fint[pos] <= hi[pos] + 2e-3))
        print("   F inside the band on the plotted range: %s" % inside)
        ax.fill_between(xis / ER, lo, hi, color="C0", alpha=0.25, lw=0, label="Markov\u2013Krein band")
        ax.plot(x, F, color="k", lw=1.4, label="harmonic response")
        ax.plot([-1, 0, 0], [0, 0, e0], color="k", lw=1.4)
        for a, b in ivs:
            ax.plot([a / ER, b / ER], [1.04, 1.04], color="C3", lw=2.5, solid_capstyle="butt")
        ax.axvline(1.0, color="0.5", lw=0.6, ls=":")
        ax.set_xlim(-0.5, 3.0)
        ax.set_ylim(0, 1.08)
        ax.set_xlabel(r"$\omega/E_R$")
        ax.text(0.03, 0.86, r"%s $q = %d$ keV" % (tag, qk), transform=ax.transAxes, fontsize=8)
    axs[0].set_ylabel(r"cumulative $F(\omega)$")
    axs[0].legend(fontsize=7, frameon=False, loc="lower right")
    fig.tight_layout()
    outp = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "fig11_5.pdf")
    fig.savefig(outp)
    print("wrote", os.path.normpath(outp))
