"""Limit 11.3b: second-order thermal diffuse scattering near a reciprocal-lattice vector, W^(2),th ~ 1/|q - G|.
Output: tex/figures/ch11/limit11_3b.pdf. Prints the numbers quoted in Sect. 11.3, the box caption and Appendix F.

Model (a labelled model; the full coherent two-phonon response at T > 0 is not computed):
  isotropic elastic continuum for the acoustic branches of silicon, longitudinal and transverse speeds v_L = 8.95 and
  v_T = 5.34 km/s (the Hill-averaged speeds of Sect. 11.1, from the measured room-temperature elastic tensor, Martinez et al.
  2019 Table I via phon11.py), polarizations exactly longitudinal and transverse, every wavevector cut at |Q| < q_BZ = 2.248 keV
  (one acoustic wavevector per primitive cell; modelling choice), acoustic eigenvectors e_k = ehat sqrt(M_k/M_cell).
  The two-phonon omega-integrated weight per cell near G (eq:11.3-tds2, from eq:11.3-weight in momentum space, App. D.31):
     W^(2)(q) = (1/2) |S_G|^2 Omega int d^3Q1/(2pi)^3 sum_{nu1 nu2} (q.e1)^2 (q.e2)^2/M_cell^2 coth(w1/2T) coth(w2/2T)/(4 w1 w2),
     Q2 = k - Q1, k = q - G, S_G = sum_k c_k e^{-W_k} e^{i G.tau_k};
  its thermal part replaces coth coth by coth coth - 1.  Formula (dashed): the classical limit coth(w/2T) -> 2T/w with no cut,
     k W^(2),th -> |S_G|^2 Omega T^2 J /(16 pi^3 M_cell^2), J = k int d^3Q1 h(Q1) h(Q2)/(Q1^2 Q2^2), h = sum_nu (q.e_nu)^2/c_nu^2,
  a number for each direction of k relative to q; here k || q (approach to G along the scattering vector).
  Bound (eq:11.3-tds): h <= q^2/c_T^2 and int d^3Q/(Q^2 |k - Q|^2) = pi^3/k give J <= pi^3 q^4/c_T^4; the plot is normalized to it.
  Plotted: k W^(2),th(k) / [|S_G|^2 Omega T^2 q^4/(16 M_cell^2 c_T^4)] against k/q_BZ at 77 K and 293 K, with q = |G_111| = 3.95 keV.
  Validity boundary: the soft pair is classical for c_T k << T, marked at k = T/c_T (vertical lines); gray: within 10 % of the
  classical formula at 293 K.  At 10 mK the boundary is at k = T/c_T = 48 meV, 2.2e-5 q_BZ, and the thermal part is (T/293 K)^2 ~ 1e-9 of it.
Integration: by the Q1 <-> Q2 symmetry, twice the region |Q1| < |Q2|, in spherical coordinates about the origin with the axis
  along k (axisymmetric for k || q: 2D Gauss-Legendre in log rho and cos theta).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mph11 as MP  # noqa: E402

C = 1 / 299792.458
CL, CT = 8.95 * C, 5.34 * C
KB = 8.617333262e-5
QBZ = MP.QBZ_KEV * 1e3                 # eV
G111 = np.sqrt(3) * 2 * np.pi / MP.A_ANG * MP.HBARC   # eV
print("|G_111| = %.3f keV, q_BZ = %.3f keV" % (G111 / 1e3, QBZ / 1e3))


def hfun(cosang):
    """sum_nu (qhat.e_nu)^2 / c_nu^2 for a wavevector at angle arccos(cosang) to qhat."""
    return cosang**2 / CL**2 + (1 - cosang**2) / CT**2


def integrand_pairs(rho, mu, k):
    """Q1 = rho (sin th, 0, cos th) about axis k zhat; returns |Q2|, cos of Q1 and Q2 with zhat (= qhat)."""
    q1z = rho * mu
    q1x = rho * np.sqrt(1 - mu**2)
    q2z, q2x = k - q1z, -q1x
    Q2 = np.hypot(q2z, q2x)
    return Q2, mu, q2z / Q2


def J_weight(k, T=None, cut=True, nr=160, nm=160):
    """k * int d^3Q1 sum (qhat.e1)^2 (qhat.e2)^2 F(w1)F(w2)/(...): classical (T None): h1 h2/(Q1^2 Q2^2) in units 1/c_T^4;
    thermal: [coth coth - 1]/(4 w1 w2) * (with c factors) normalized so that the classical limit equals the T None value."""
    rmax = QBZ if cut else 2e3 * k
    xs, xw = np.polynomial.legendre.leggauss(nr)
    lr0, lr1 = np.log(1e-6 * k), np.log(rmax)
    lr = 0.5 * (lr1 - lr0) * xs + 0.5 * (lr1 + lr0)
    wr = 0.5 * (lr1 - lr0) * xw
    rho = np.exp(lr)
    mu, wm = np.polynomial.legendre.leggauss(nm)
    R, MU = np.meshgrid(rho, mu, indexing="ij")
    W = np.outer(wr * rho, wm)                      # d rho = rho d(log rho)
    Q2, c1, c2 = integrand_pairs(R, MU, k)
    region = (R < Q2) & ((Q2 < QBZ) if cut else True)
    tot = 0.0
    for nu1, cnu1, p1 in ((0, CL, c1**2), (1, CT, 1 - c1**2)):
        for nu2, cnu2, p2 in ((0, CL, c2**2), (1, CT, 1 - c2**2)):
            w1, w2 = cnu1 * R, cnu2 * Q2
            if T is None:
                f = p1 * p2 / (w1**2 * w2**2)                    # (2T/w)(2T/w)/(4 w w) / T^2
            else:
                f = (1 / (np.tanh(w1 / (2 * T)) * np.tanh(w2 / (2 * T))) - 1) / (4 * w1 * w2) / T**2 * p1 * p2
            tot = tot + np.sum(np.where(region, f * R**2 * 2 * np.pi * W, 0.0))
    return 2 * tot * k * CT**4                      # factor 2: the region |Q1| > |Q2|; units of 1/c_T^4


bound = np.pi**3
Jcl = J_weight(1.0, None, cut=False)
print("classical coefficient J (k || q) = %.3f, bound pi^3 = %.3f, ratio %.3f" % (Jcl, bound, Jcl / bound))
# check of the integral used in the bound: int d^3Q/(Q^2 |k-Q|^2) = pi^3/k (k = 1), by the same quadrature with h = const
_h, _CL, _CT = hfun, CL, CT
CL = CT
Jiso = J_weight(1.0, None, cut=False)
CL = _CL
print("isotropic check: k int d^3Q/(Q^2|k-Q|^2) = %.4f (pi^3 = %.4f)" % (Jiso, np.pi**3))
x = np.geomspace(3e-3, 1.0, 50)
res = {}
for TK in (77.0, 293.0):
    T = TK * KB
    vals = np.array([J_weight(xi * QBZ, T) for xi in x]) / bound
    res[TK] = vals
    kb = T / CT / QBZ
    print("T = %3.0f K: T/c_T = %.3f keV = %.3f q_BZ" % (TK, T / CT / 1e3, kb))
    for xi in (0.003, 0.01, 0.03, 0.1, 0.3, 1.0):
        j = np.argmin(np.abs(x - xi))
        print("   k/q_BZ = %.3f: k W_th / bound-coef = %.3f (classical %.3f), ratio to classical %.3f"
              % (x[j], vals[j], Jcl / bound, vals[j] / (Jcl / bound)))
    ok = np.abs(vals / (Jcl / bound) - 1) < 0.10
    last = np.where(~ok)[0]
    print("   within 10 %% of the classical law for k/q_BZ <= %.4f (= %.2f T/c_T)" %
          (x[last[0] - 1] if len(last) and last[0] > 0 else np.nan,
           (x[last[0] - 1] if len(last) and last[0] > 0 else np.nan) / kb))

print("T = 10 mK: T/c_T = %.1f meV = %.2e q_BZ" % (0.01 * KB / CT * 1e3, 0.01 * KB / CT / QBZ))
# size at room temperature next to the incoherent two-phonon weight, (111), k = 0.1 q_BZ
T = 293 * KB
k = 0.1 * QBZ
Mcell = 2 * MP.M_SI
q = G111
ux2_293 = 6.38e-3 / MP.HBARC**2                     # DFPT 293 K (WE 5.7)
W2 = q**2 * ux2_293
SG2_over_A2 = 2 * np.exp(-W2)                        # |1 + e^{-i 3pi/2}|^2 e^{-2W}
Jk = J_weight(k, T) * bound / bound                  # in units 1/c_T^4, times 1/k
Wth = SG2_over_A2 * MP.OMEGA / MP.HBARC**3 * T**2 * q**4 * Jk / (16 * np.pi**3 * Mcell**2 * CT**4) / k
Winc = 2 * np.exp(-W2) * W2**2 / 2                   # sum over two nuclei, per A^2
print("293 K, q = |G_111|, k = 0.1 q_BZ: 2W = %.4f; W^(2),th = %.3e, W^(2)_inc = %.3e (per cell, in units of A_k^2), ratio %.2f"
      % (W2, Wth, Winc, Wth / Winc))

fig, ax = plt.subplots(figsize=(5.0, 3.3))
TKb = 293 * KB / CT / QBZ
okx = x[np.abs(res[293.0] / (Jcl / bound) - 1) < 0.10]
ax.axvspan(x[0], okx.max(), color="0.88", lw=0)
ax.axhline(1.0, color="0.4", ls=":", lw=1.0, label=r"bound, $c_{\nu}\to c_{\mathrm{T}}$")
ax.axhline(Jcl / bound, color="k", ls="--", lw=1.0, label=r"classical $1/|\mathbf{q}-\mathbf{G}|$ law")
ax.plot(x, res[293.0], color="C3", lw=1.5, label="model, 293 K")
ax.plot(x, res[77.0], color="C0", lw=1.5, label="model, 77 K")
for TK, col in ((293.0, "C3"), (77.0, "C0")):
    ax.axvline(TK * KB / CT / QBZ, color=col, lw=0.7, ls="-.")
ax.set_xscale("log")
ax.set_xlim(x[0], x[-1])
ax.set_ylim(0, 1.1)
ax.set_xlabel(r"$|\mathbf{q}-\mathbf{G}|/q_{\mathrm{BZ}}$")
ax.set_ylabel(r"$|\mathbf{q}-\mathbf{G}|\,\mathfrak{W}^{(2),\mathrm{th}}$ / bound")
ax.legend(fontsize=7, frameon=False, loc="lower left")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_3b.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
