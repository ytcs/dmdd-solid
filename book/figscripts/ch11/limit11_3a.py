"""Limit 11.3a: the incoherent approximation (Poisson weights of the self part) against the exact harmonic n-phonon weight.
Output: tex/figures/ch11/limit11_3a.pdf. Prints the numbers quoted in Sect. 11.3, the box caption and Appendix F.

Quantity: the coherence correction of the omega-integrated n-phonon weight, direction-averaged at fixed |q|, T = 0,
   delta_n(q) = < W^(n)(q) / W^(n)_inc(q) > - 1,
   W^(n)(q) = (1/n!) sum_{dR,k,k'} c_k c_k' e^{-i q.d} e^{-W_k - W_k'} [q.B_kk'(dR).q]^n,   d = dR + tau_k - tau_k'   (eq:E.17-Wn),
   W^(n)_inc = the terms d = 0.  For silicon (one species, cubic sites, B_k = <u_x^2> 1) the couplings and the Debye-Waller
   factors cancel in the ratio:  delta_n = (1/n_at) sum_{pairs != self} < e^{-i q.d} b(qhat)^n >,  b = qhat.B_kk'(dR).qhat/<u_x^2>.
   It therefore holds for any coupling that multiplies the density of each nucleus by the same number.
B_kk'(dR): T = 0, PBE phonons of Sect. 5.2 on a 48^3 grid (mph11.py); pairs with |d| <= 40 A (the result changes by < 1e-3
   between 30 and 40 A, printed).  Direction average done exactly: in the frame z || d, the phi average of b^n is a polynomial
   of degree 2n in mu = cos(theta), expanded in Legendre polynomials, and <e^{-i q d mu} P_l(mu)> = (-i)^l j_l(q d).
n = 1 (thin line): the one-phonon weight cannot be summed in real space (B ~ 1/dR^2); it is computed in momentum space,
   sum_nu |sum_k e^{i q.tau_k} q.e*_k nu(Q)|^2 / (2 M omega_Q nu) over n_at q^2 <u_x^2>, averaged over 96 x 192 directions
   (agrees with 144 x 288 to 1e-3 at 2, 7.85, 10 and 20 q_BZ; printed).
Leading correction (dotted): the nearest-neighbour shell alone (four bonds per atom, |d| = 2.352 A).
q_BZ = 2.248 keV (Sect. 11.1).  Gray: q where |delta_2| and |delta_3| both stay below 0.10 from there on.
"""
import os
import sys
import numpy as np
from scipy.special import spherical_jn
from numpy.polynomial import legendre as Lg
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mph11 as MP  # noqa: E402
import phon11 as P  # noqa: E402
import si_ifc  # noqa: E402

N = 48
Bd = MP.B_tensor(N)
UX2 = Bd["B"][0, 0, 0, 0, 0].real[0, 0]
print("grid %d^3: <u_x^2> = %.4e A^2; max |Im B| = %.1e" % (N, UX2, np.abs(Bd["B"].imag).max()))
d, kk, Bp = MP.pair_table(Bd, rmax=40.0)
Bp = Bp.real / UX2
r = np.linalg.norm(d, axis=1)
notself = r > 1e-6
d, kk, Bp, r = d[notself], kk[notself], Bp[notself], r[notself]
print("pairs (not self) within 40 A: %d" % len(r))


def legendre_coeffs(n):
    """For every pair, Legendre coefficients a_l (l = 0..2n) of the phi-average of b(qhat)^n in the frame z || d."""
    zh = d / r[:, None]
    tmp = np.where(np.abs(zh[:, 0:1]) < 0.9, np.array([[1.0, 0, 0]]), np.array([[0, 1.0, 0]]))
    xh = np.cross(zh, tmp)
    xh /= np.linalg.norm(xh, axis=1)[:, None]
    yh = np.cross(zh, xh)
    mu, _ = Lg.leggauss(2 * n + 1)
    phi = 2 * np.pi * np.arange(16) / 16
    vals = np.zeros((len(r), len(mu)))
    for i, m in enumerate(mu):
        s = np.sqrt(1 - m * m)
        qh = (s * np.cos(phi)[None, :, None] * xh[:, None, :] + s * np.sin(phi)[None, :, None] * yh[:, None, :]
              + m * zh[:, None, :])                                   # (pairs, phi, 3)
        b = np.einsum("pfa,pab,pfb->pf", qh, Bp, qh)
        vals[:, i] = (b ** n).mean(1)
    # exact interpolation of a degree-2n polynomial at 2n+1 Gauss nodes
    V = Lg.legvander(mu, 2 * n)                                       # (nodes, l)
    return np.linalg.solve(V, vals.T).T                               # (pairs, l)


COEF = {n: legendre_coeffs(n) for n in (2, 3)}


def delta(n, q_keV, sel=None):
    qA = q_keV * 1e3 / MP.HBARC
    a = COEF[n] if sel is None else COEF[n][sel]
    x = qA * (r if sel is None else r[sel])
    tot = 0.0
    for l in range(2 * n + 1):
        tot = tot + a[:, l] * ((-1j) ** l) * spherical_jn(l, x)
    return np.real(tot.sum()) / MP.NAT


nn = np.abs(r - 2.352) < 0.01
far = r <= 30.0
print("nearest pairs:", nn.sum(), "; longitudinal b along a bond = %.3f" %
      (np.einsum("a,ab,b->", d[nn][0] / r[nn][0], Bp[nn][0], d[nn][0] / r[nn][0])))

# one-phonon, momentum space
qh, wq = P.sphere_grid(96, 192)


def ratio1(q_keV, grid=None):
    gh, gw = (qh, wq) if grid is None else P.sphere_grid(*grid)
    qA = q_keV * 1e3 / MP.HBARC
    tot = 0.0
    for c in np.array_split(np.arange(len(gh)), max(1, len(gh) // 6000)):
        qv = qA * gh[c] / (2 * np.pi / MP.A_ANG)
        w, ev = si_ifc.phonons(qv)
        w = np.maximum(w, 1e-3) * 1e-3                               # eV
        ph = np.exp(2j * np.pi * (qv @ MP.TAU.T))
        amp = np.zeros((len(c), 6), complex)
        for k in range(2):
            amp += ph[:, k:k + 1] * np.einsum("ni,nij->nj", gh[c], np.conj(ev[:, 3 * k:3 * k + 3, :]))
        num = (np.abs(amp) ** 2 / (2 * MP.M_SI * w)).sum(1) * MP.HBARC ** 2   # A^2 per q^2
        tot += np.sum(gw[c] * num)
    return tot / (MP.NAT * UX2) - 1


for xv in (2.0, 7.85, 10.0, 20.0):
    print("direction-grid check, n = 1 at q = %.2f q_BZ: delta_1 = %+.4f (48x96), %+.4f (96x192), %+.4f (144x288)"
          % (xv, ratio1(xv * MP.QBZ_KEV, (48, 96)), ratio1(xv * MP.QBZ_KEV), ratio1(xv * MP.QBZ_KEV, (144, 288))))


x = np.geomspace(0.1, 20, 120)
qk = x * MP.QBZ_KEV
D2 = np.array([delta(2, q) for q in qk])
D3 = np.array([delta(3, q) for q in qk])
D2nn = np.array([delta(2, q, nn) for q in qk])
D3nn = np.array([delta(3, q, nn) for q in qk])
D1 = np.array([ratio1(q) for q in qk])
D2far = np.array([delta(2, q, far) for q in qk])
print("max |delta_2(40 A) - delta_2(30 A)| = %.1e" % np.abs(D2 - D2far).max())

for xv in (0.1, 0.5, 1, 2, 4.45, 10):
    q = xv * MP.QBZ_KEV
    print("q = %.2f q_BZ = %6.2f keV: delta_1 = %+.3f, delta_2 = %+.4f (nn %+.4f), delta_3 = %+.4f (nn %+.4f)"
          % (xv, q, ratio1(q), delta(2, q), delta(2, q, nn), delta(3, q), delta(3, q, nn)))
for q in (2.0, 5.0, 10.0, 20.0):
    print("q = %5.1f keV: delta_2 = %+.4f, delta_3 = %+.4f" % (q, delta(2, q), delta(3, q)))
print("q -> 0 limits: delta_2 = %+.4f, delta_3 = %+.4f (sum over all pairs of b^n /n_at, angular average)"
      % (delta(2, 1e-4), delta(3, 1e-4)))


def boundary(D, tol=0.10):
    bad = np.where(np.abs(D) > tol)[0]
    return x[bad[-1] + 1] if len(bad) else x[0]


xb = max(boundary(D2), boundary(D3))
print("|delta_2|, |delta_3| < 0.10 for q/q_BZ >= %.2f (q >= %.2f keV); delta_2 alone from %.2f, delta_3 alone from %.2f"
      % (xb, xb * MP.QBZ_KEV, boundary(D2), boundary(D3)))
print("|delta_1| < 0.10 from q/q_BZ = %.2f" % boundary(D1))
print("|delta_2| < 0.05 from %.2f; < 0.02 from %.2f" % (boundary(D2, 0.05), boundary(D2, 0.02)))

fig, ax = plt.subplots(figsize=(5.0, 3.3))
ax.axvspan(xb, x[-1], color="0.88", lw=0)
ax.axhline(1.0, color="k", ls="--", lw=1.0, label="incoherent (Poisson) weight")
ax.plot(x, 1 + D2, color="C3", lw=1.5, label=r"exact, $n = 2$")
ax.plot(x, 1 + D3, color="C0", lw=1.5, label=r"exact, $n = 3$")
ax.plot(x, 1 + D2nn, color="C3", ls=":", lw=1.2, label="nearest neighbors only")
ax.plot(x, 1 + D3nn, color="C0", ls=":", lw=1.2)
ax.plot(x, 1 + D1, color="0.45", lw=0.9, label=r"exact, $n = 1$")
ax.set_xscale("log")
ax.set_xlim(x[0], x[-1])
ax.set_ylim(0.0, 1.8)
ax.set_xlabel(r"$q/q_{\mathrm{BZ}}$")
ax.set_ylabel(r"$\mathfrak{W}^{(n)}/\mathfrak{W}^{(n)}_{\mathrm{inc}}$")
sec = ax.secondary_xaxis("top", functions=(lambda t: t * MP.QBZ_KEV, lambda k: k / MP.QBZ_KEV))
sec.set_xlabel(r"$q$ [keV] (silicon)")
ax.legend(fontsize=6.5, frameon=False, loc="lower left", ncol=2)
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_3a.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
