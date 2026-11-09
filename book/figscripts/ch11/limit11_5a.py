"""Limit 11.5a (Sect. 11.5): first anharmonic correction to the multiphonon response, single-site model.
Output: tex/figures/ch11/limit11_5a.pdf. Prints every number of the box, of its F row and of the text paragraph on the model.

Model (labelled as a model in caption and text): one nucleus in the one-dimensional potential
    V(x) = (1/2) M w0^2 x^2 + lambda3 w0 (x/l0)^3 + lambda4 w0 (x/l0)^4,   l0 = (2 M w0)^(-1/2),
  the single-site potential of Lin, Shen, Sholapurkar and Villarama, arXiv:2309.10839, Eq. (26) (= their (67)), written with
  l0 (NOTATION l_0) so that sqrt(2 M w0) x = x/l0.  Their fitted silicon values (Sect. IV text, Tersoff-Buckingham-Coulomb
  potential, nearest-neighbour direction to an orthogonal one): lambda3 = 6e-3 .. 1e-2, lambda4 = (2..3)e-4.
  w0 = <omega^-1>^-1 = 30.42 meV of the silicon PBE density of states (imp11.py), as in their Eq. (69) (they quote 30.8 meV).
  M = 26.162 GeV (mph11.py).  Then (2 M w0)^(1/2) = 39.9 keV (their Table 1: 40.3 keV) and k = q l0 = q/(2 M w0)^(1/2).
Exact solution: H in the harmonic basis |n>, n < NB = 200 (x/l0 = a + a^dagger), diagonalized; matrix elements of
  e^{i k (a + a^dagger)} by matrix exponential; checked by doubling NB (changes < 1e-10 for the plotted levels).
  |M_n|^2 = |<Phi_n| e^{iqx} |Phi_0>|^2 is the weight of the n-th level (the "n-phonon" weight of the model, T = 0).
Harmonic reference: e^{-k^2} k^(2n)/n! (Poisson, eq:5.6-multi for one oscillator).
Leading term (derived in Sect. 11.5 by first-order perturbation theory): |M_2|^2 = e^{-k^2}[k^4/2 + 8 lambda3^2 k^2 + ...],
  so that |M_2|^2/harmonic = 1 + 16 lambda3^2/k^2.  The script checks the coefficient 8 and <p^2> = (M w0/2)(1 - 44 lambda3^2 +
  12 lambda4) of Ref. Eq. (65), and fits the coefficient of lambda3^2 k^4 in |M_3|^2 (printed; used only in the text as a number).
Gray band: k where the n = 2 and n = 3 leading formulas (a_2 = 16 derived, a_3 = 108 from the fitted 18) are both within 10 % of the exact ratio (lambda3 = 1e-2, lambda4 = 2.5e-4).
"""
import os
import sys
import numpy as np
from scipy.linalg import eigh, expm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import imp11 as I  # noqa: E402

NB = 200
_n = np.arange(NB)
_a = np.diag(np.sqrt(_n[1:]), 1)
X = _a + _a.T                      # x / l0
P = 1j * (_a.T - _a)               # p / p0, p0 = (M w0 / 2)^(1/2): <p^2> = (M w0/2) <P^2>
W0 = I.W_INV                       # eV
Q0 = np.sqrt(2 * I.M * W0)         # eV, (2 M w0)^(1/2)
QBZ = 2.25e3                       # eV, Sect. 11.1


def solve(l3, l4, nb=NB):
    n = np.arange(nb)
    a = np.diag(np.sqrt(n[1:]), 1)
    x = a + a.T
    H = np.diag(n + 0.5) + l3 * np.linalg.matrix_power(x, 3) + l4 * np.linalg.matrix_power(x, 4)
    E, V = eigh(H)
    return E, V, x


def weights(l3, l4, ks, nmax=5, nb=NB):
    E, V, x = solve(l3, l4, nb)
    out = np.empty((len(ks), nmax))
    for i, k in enumerate(ks):
        M = V.T @ (expm(1j * k * x) @ V[:, 0])
        out[i] = np.abs(M[:nmax])**2
    return out, E[:nmax] - E[0]


def harm(k, n):
    from math import factorial
    return np.exp(-k**2) * k**(2 * n) / factorial(n)


if __name__ == "__main__":
    print("w0 = <w^-1>^-1 = %.2f meV; (2 M w0)^1/2 = %.1f keV; q_BZ/(2Mw0)^1/2 = %.4f" % (W0 * 1e3, Q0 / 1e3, QBZ / Q0))
    # <p^2> check of Ref. Eq. (65)
    for l3, l4 in ((0, 1e-3), (1e-2, 2.5e-4), (6e-3, 2e-4)):  # a pure cubic is unbounded below: no exact check
        E, V, x = solve(l3, l4)
        n = np.arange(NB); a = np.diag(np.sqrt(n[1:]), 1); p = 1j * (a.T - a)
        p2 = np.real(V[:, 0] @ (p @ p) @ V[:, 0])
        print("lambda3 = %.3g, lambda4 = %.3g: <p^2>/(M w0/2) = %.6f, Eq. (65) 1 - 44 l3^2 + 12 l4 = %.6f; "
              "E^kin change %.3f %%" % (l3, l4, p2, 1 - 44 * l3**2 + 12 * l4, (p2 - 1) * 100))
    # coefficient of lambda3^2 k^2 in |M_2|^2 and of lambda3^2 k^4 in |M_3|^2 (small lambda3, small k)
    for l3 in (1e-3, 2e-3):
        w, _ = weights(l3, 0.0, [1e-3])
        print("lambda3 = %g: |M_2|^2/(lambda3^2 k^2) at k = 1e-3: %.4f (derived: 8, harmonic k^4/2 adds %.4f)"
              % (l3, w[0, 2] / (l3**2 * 1e-6), 1e-12 / 2 / (l3**2 * 1e-6)))
    for k in (0.02, 0.05):
        r = []
        for l3 in (1e-3, 2e-3):
            w, _ = weights(l3, 0.0, [k])
            r.append((w[0, 3] - harm(k, 3)) / (k**4 * l3**2))
        print("k = %.2f: |M_3|^2 coefficient of lambda3^2 k^4 = %.2f, %.2f (lambda3 = 1e-3, 2e-3)" % (k, r[0], r[1]))
    # convergence in the basis size
    w1, _ = weights(1e-2, 2.5e-4, [0.05, 0.5], nb=NB)
    w2, _ = weights(1e-2, 2.5e-4, [0.05, 0.5], nb=2 * NB)
    print("basis check, max relative change of |M_n|^2 (n <= 4) on doubling NB: %.1e" % np.max(np.abs(w2 / w1 - 1)))

    ks = np.geomspace(0.01, 2.0, 160)
    res = {}
    for l3, l4 in ((1e-2, 2.5e-4), (6e-3, 2e-4)):
        w, dE = weights(l3, l4, ks)
        res[(l3, l4)] = w
        print("lambda3 = %.3g, lambda4 = %.3g: level spacings E_n - E_0 = %s w0" % (l3, l4, np.array2string(dE, precision=4)))
    w = res[(1e-2, 2.5e-4)]
    r2 = w[:, 2] / harm(ks, 2)
    r3 = w[:, 3] / harm(ks, 3)
    r4 = w[:, 4] / harm(ks, 4)
    form2 = 1 + 16 * 1e-2**2 / ks**2
    form3 = 1 + 108 * 1e-2**2 / ks**2
    ok2 = np.abs(form2 / r2 - 1) <= 0.10
    ok3 = np.abs(form3 / r3 - 1) <= 0.10
    ok = ok2 & ok3
    print("n = 2 formula within 10 %% of exact on %.3f <= k <= %.3f (whole plotted range %.2f-%.2f: %s)"
          % (ks[ok2].min(), ks[ok2].max(), ks[0], ks[-1], ok2.all()))
    print("n = 3 formula 1 + 108 l3^2/k^2 within 10 %% of exact for k >= %.3f (q >= %.2f keV)" % (ks[ok3].min(), ks[ok3].min() * Q0 / 1e3))
    j = 0
    print("at k = %.3f: n = 3 exact/harmonic %.1f, formula %.1f (lambda3^4 k^2 term)" % (ks[j], r3[j], form3[j]))
    for kk in (QBZ / Q0, 0.1, 0.2, 0.5, 1.0):
        j = np.argmin(np.abs(ks - kk))
        print("k = %.3f (q = %.1f keV): exact/harmonic n=2 %.3f (formula %.3f), n=3 %.3f, n=4 %.3f"
              % (ks[j], ks[j] * Q0 / 1e3, r2[j], form2[j], r3[j], r4[j]))
    for l3 in (1e-2, 6e-3):
        print("lambda3 = %.3g: n = 2 crossover 16 l3^2/k^2 = 1 at k = 4 l3 = %.3f, q = %.2f keV; at q_BZ correction %.2f"
              % (l3, 4 * l3, 4 * l3 * Q0 / 1e3, 16 * l3**2 / (QBZ / Q0)**2))
        print("            n = 3 crossover 108 l3^2/k^2 = 1 at k = %.3f, q = %.2f keV" % (np.sqrt(108) * l3, np.sqrt(108) * l3 * Q0 / 1e3))
    for n, rr in ((2, r2), (3, r3), (4, r4)):
        above = ks[np.abs(rr - 1) > 0.10]
        print("n = %d: exact/harmonic deviates by more than 10 %% for k < %.3f (q < %.1f keV)" % (n, above.max(), above.max() * Q0 / 1e3))

    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.axvspan(ks[ok].min(), ks[ok].max(), color="0.88", lw=0)
    ax.axvline(QBZ / Q0, color="0.4", lw=0.8, ls="-.")
    ax.text(QBZ / Q0 * 1.06, 1.5e3, r"$q_{\mathrm{BZ}}$", fontsize=7, color="0.3")
    ax.axhline(1.0, color="k", lw=0.6)
    ax.plot(ks, r2, color="C3", lw=1.5, label=r"$n = 2$, exact")
    ax.plot(ks, form2, color="C3", lw=1.0, ls="--", label=r"$n = 2$, $1 + 16\lambda_3^2/k^2$")
    ax.plot(ks, r3, color="C0", lw=1.5, label=r"$n = 3$, exact")
    ax.plot(ks, form3, color="C0", lw=1.0, ls="--", label=r"$n = 3$, $1 + 108\lambda_3^2/k^2$")
    ax.plot(ks, r4, color="C2", lw=1.5, label=r"$n = 4$, exact")
    w6 = res[(6e-3, 2e-4)]
    ax.plot(ks, w6[:, 2] / harm(ks, 2), color="C3", lw=0.8, ls=":")
    ax.plot(ks, w6[:, 3] / harm(ks, 3), color="C0", lw=0.8, ls=":")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(ks[0], ks[-1])
    ax.set_ylim(0.5, 3e3)
    ax.set_xlabel(r"$k = q/(2M_\kappa\omega_0)^{1/2}$")
    ax.set_ylabel(r"$n$-phonon weight / harmonic")
    sec = ax.secondary_xaxis("top", functions=(lambda k: k * Q0 / 1e3, lambda q: q * 1e3 / Q0))
    sec.set_xlabel(r"$q$ (keV), silicon", fontsize=8)
    sec.tick_params(labelsize=7)
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    fig.tight_layout()
    outp = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_5a.pdf")
    fig.savefig(outp)
    print("wrote", os.path.normpath(outp))
