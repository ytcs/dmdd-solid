"""Limit Check 16.3b (lim:16.3b, fig:16-limit-qd): the quantum-dot pair response in the envelope-function approximation
against its bulk limit with the gap scissored to the dot gap (the published form: Blanco et al. arXiv:2208.05967,
Eqs. (6), (10)-(12), with bulk tables and the gap set to Delta E_QD).

Model (a test of the counting, not of a material): electron and hole in an infinite spherical well of radius R
(2208.05967 Eqs. (2)-(4)), parabolic bands with equal masses m_e* = m_h* = m (model choice), Bloch factor at the band
edge taken q-independent (it multiplies dot and bulk alike and cancels in the ratio).  Units: R = 1, m = 1/2, so that
a level is eps_nl = chi_nl^2 with chi_nl the n-th zero of j_l, and the lowest pair energy above E_g is
E_conf = 2 pi^2 (= (pi^2/2R^2)(1/m_e* + 1/m_h*), 2208.05967 Eq. (5)).
  dot:   S_env(q, Omega) = sum_{e,h} sum_L (2l+1)(2l'+1)(2L+1) (l l' L; 0 0 0)^2 I_L^2 delta(Omega - eps_e - eps_h),
         I_L = int_0^1 r^2 R_e R_h j_L(q r) dr, R_nl = sqrt(2) j_l(chi r)/j_{l+1}(chi)  (direction-averaged, m summed)
  bulk:  S_env = V (mu sqrt(2 mu)/(2 pi^2)) sqrt(Omega - q^2/2M), mu = m/2, M = 2m, V = 4 pi/3  (plane waves in volume V)
  scissor: bulk with Omega -> Omega - E_conf (the gap set to the dot gap).
Both are integrated from the gap up to Omega; plotted is the ratio dot/scissored bulk of these integrals against x = (Omega - E_conf)/E_conf,
the energy above the dot gap in units of the confinement energy, for qR = 3 and 8; dashed: dot/unscissored bulk at qR = 8; dotted: 1 - 9 pi/(8 k R), the surface term of
Weyl's law for the Dirichlet sphere (N = V k^3/6pi^2 - S k^2/16pi) at q -> 0, k the common envelope momentum, Omega = 2k^2.
Shaded: x where both solid curves stay within 10 % of 1.  The window of 2208.05967 (2.5-10 eV deposits, d = 3.3 nm,
measured Delta E_QD = 1.2 eV from bulk 0.41 eV, so E_conf = 0.79 eV; q >= 0.9 keV, qR >= 7.5) is marked.
Checks printed: closure sum_e |<e|e^{iqr}|h>|^2 -> 2l'+1 at large cutoff; q -> 0 counting against Weyl's law.
Run: python limit16_3b.py  (under a minute)
"""
import os
import numpy as np
from math import lgamma, exp
from scipy.special import spherical_jn
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch16")
ECONF = 2 * np.pi**2
XMAX = 150.0
OMAX = ECONF * (XMAX + 2)                  # largest pair energy kept
CHIMAX = np.sqrt(OMAX - np.pi**2)          # one particle may carry all but the other's 1s energy


def zeros_jl(l, chimax):
    xs = np.linspace(0.5, chimax + 1, 4000)
    v = spherical_jn(l, xs)
    out = []
    for a, b, fa, fb in zip(xs[:-1], xs[1:], v[:-1], v[1:]):
        if fa * fb < 0 and a > 0.9 * l ** 0.5:
            r = brentq(lambda x: spherical_jn(l, x), a, b)
            if r < chimax:
                out.append(r)
    return out


levels = []                                 # (l, chi)
l = 0
while True:
    z = zeros_jl(l, CHIMAX)
    if not z:
        break
    levels += [(l, c) for c in z]
    l += 1
print(f"levels with chi < {CHIMAX:.2f}: {len(levels)}, l up to {max(L for L, _ in levels)}")

xr, wr = leggauss(240)
r = 0.5 * (xr + 1)
wr = 0.5 * wr
Rr = np.array([np.sqrt(2) * spherical_jn(L, c * r) / spherical_jn(L + 1, c) for L, c in levels])   # (nlev, nr)
eps = np.array([c * c for _, c in levels])
ls = np.array([L for L, _ in levels])


def threej0_sq(l1, l2, l3):
    J = l1 + l2 + l3
    if J % 2 or l3 < abs(l1 - l2) or l3 > l1 + l2:
        return 0.0
    g = J // 2
    a = lgamma(J - 2 * l1 + 1) + lgamma(J - 2 * l2 + 1) + lgamma(J - 2 * l3 + 1) - lgamma(J + 2)
    b = lgamma(g + 1) - lgamma(g - l1 + 1) - lgamma(g - l2 + 1) - lgamma(g - l3 + 1)
    return exp(a + 2 * b)


LMAX = 2 * ls.max()
TJ = np.zeros((ls.max() + 1, ls.max() + 1, LMAX + 1))
for a in range(ls.max() + 1):
    for b in range(ls.max() + 1):
        for c in range(abs(a - b), a + b + 1):
            TJ[a, b, c] = threej0_sq(a, b, c)


def pair_weights(qR, emax=OMAX):
    """Return pair energies and m-summed, direction-averaged weights for all (e, h) with eps_e + eps_h < emax."""
    jL = np.array([spherical_jn(L, qR * r) for L in range(LMAX + 1)])      # (L, nr)
    W, Om, hidx = [], [], []
    for h in range(len(levels)):
        for e in range(len(levels)):
            if eps[e] + eps[h] >= emax:
                continue
            le, lh = ls[e], ls[h]
            Ls = np.arange(abs(le - lh), le + lh + 1)
            prod = Rr[e] * Rr[h] * r**2 * wr
            I = jL[Ls] @ prod
            w = np.sum((2 * le + 1) * (2 * lh + 1) * (2 * Ls + 1) * TJ[le, lh, Ls] * I**2)
            W.append(w)
            Om.append(eps[e] + eps[h])
            hidx.append(h)
    return np.array(Om), np.array(W), np.array(hidx)


V = 4 * np.pi / 3
m = 0.5
mu, M = m / 2, 2 * m


def bulk_cum(Om, q, shift=0.0):
    """int_0^Omega S_bulk dOmega' (scissor: Omega -> Omega - shift)."""
    x = np.maximum(Om - shift - q * q / (2 * M), 0.0)
    return V * mu * np.sqrt(2 * mu) / (2 * np.pi**2) * (2.0 / 3.0) * x**1.5


# closure check at qR = 3 for the lowest hole states, e summed up to the cutoff
Om3, W3, h3 = pair_weights(3.0, emax=1e9)
for h in range(3):
    print(f"closure qR = 3, hole (l = {ls[h]}, chi = {levels[h][1]:.3f}): sum_e = {W3[h3 == h].sum():.4f} (exact {2*ls[h]+1})")

xg = np.geomspace(0.25, XMAX, 500)                 # energy above the dot gap in units of E_conf
Og = ECONF * (1 + xg)
res = {}
for qR in (3.0, 8.0):
    Om, W, _ = pair_weights(qR)
    o = np.argsort(Om)
    cum = np.interp(Og, Om[o], np.cumsum(W[o]), left=0.0)
    res[qR] = (cum / bulk_cum(Og, qR, ECONF), cum / bulk_cum(Og, qR, 0.0))
    print(f"\nqR = {qR}: x, cumulative dot / scissored bulk, cumulative dot / unscissored bulk")
    for x in (0.5, 1, 1.65, 2, 3, 5, 8, 11.14, 15, 20, 30, 40, 50, 60, 80, 100, 120, 150):
        i = np.argmin(abs(xg - x))
        print(f"   x = {xg[i]:5.2f}  {res[qR][0][i]:7.3f}  {res[qR][1][i]:7.3f}")
# q -> 0 counting check (Weyl): number of single-particle states below k^2 against V k^3/(6 pi^2)
for k in (10, 15):
    n = sum(2 * L + 1 for L, c in levels if c < k)
    print(f"states with chi < {k}: {n}; Weyl V k^3/6pi^2 = {V*k**3/(6*np.pi**2):.1f}; with surface term -S k^2/16 pi: "
          f"{V*k**3/(6*np.pi**2) - 4*np.pi*k**2/(16*np.pi):.1f}")

# 10 % band: first x beyond which both qR curves stay within 10 %
ok = np.ones_like(xg, bool)
for qR in (3.0, 8.0):
    ok &= np.abs(res[qR][0] - 1) <= 0.1
xs10 = None
for i in range(len(xg)):
    if ok[i:].all():
        xs10 = xg[i]
        break
print(f"\nboth qR curves within 10 % of the scissored bulk for x >= {xs10}")
# surface (Weyl) estimate of the deficit: per particle 9 pi/(8 k R), k = typical particle momentum sqrt(Omega/2)/... (m = 1/2)
for x in (2, 11.14, 40):
    k = np.sqrt(ECONF * (1 + x) / 2)
    print(f"   Weyl surface deficit per particle at x = {x}: 9 pi/(8 k R) = {9*np.pi/(8*k):.3f} (k R = {k:.1f})")
for qR in (3.0, 8.0):
    sel = (xg >= 3) & (xg <= 11.14)
    print(f"qR = {qR}: dot/scissored bulk over x = 3-11.14: {res[qR][0][sel].min():.3f} to {res[qR][0][sel].max():.3f}")
if xs10 is not None:
    print(f"k R at the 10 % edge (Omega = 2 k^2): {np.sqrt(ECONF*(1+xs10)/2):.1f}")
win = ((2.5 - 1.2) / 0.79, (10 - 1.2) / 0.79)
print(f"2208.05967 window (2.5-10 eV, E_conf = 0.79 eV): x = {win[0]:.2f} to {win[1]:.2f};"
      f" qR at q = 0.9 keV, R = 1.65 nm: {900*1.65e-9/1.973269804e-7:.2f}")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.0))
ax.plot(xg, res[3.0][0], "-", color="C0", lw=1.2, label=r"dot / scissored bulk, $qR = 3$")
ax.plot(xg, res[8.0][0], "-", color="C3", lw=1.2, label=r"dot / scissored bulk, $qR = 8$")
ax.plot(xg, res[8.0][1], "--", color="C3", lw=1.0, label=r"dot / bulk without scissor, $qR = 8$")
kw = np.sqrt(ECONF * (1 + xg) / 2)
ax.plot(xg, 1 - 9 * np.pi / (8 * kw), ":", color="k", lw=1.0, label=r"$1 - 9\pi/(8kR)$, surface term")
ax.axhline(1, color="k", lw=0.6)
if xs10 is not None:
    ax.axvspan(xs10, XMAX, color="0.85", lw=0)
ax.annotate("", xy=(win[1], 0.15), xytext=(win[0], 0.15), arrowprops=dict(arrowstyle="<->", lw=0.8))
ax.text(np.sqrt(win[0] * win[1]), 0.19, "PbS, 2.5–10 eV", ha="center", fontsize=7)
ax.set_xscale("log")
ax.set_xlim(0.5, XMAX)
ax.set_ylim(0, 2.3)
ax.set_xlabel(r"$(\omega - \Delta E_{\mathrm{QD}})/E_{\mathrm{conf}}$")
ax.set_ylabel("ratio of integrated pair responses")
ax.legend(fontsize=6.5, frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_3b.pdf"))
print("wrote limit16_3b.pdf")
