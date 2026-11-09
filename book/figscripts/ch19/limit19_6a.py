"""Defecton diffusion in a phonon gas (Sect. 19.6): Limit Check 19.6a (lim:19.6a, fig:19-limit-defecton) and every
defecton number printed in Sect. 19.6.  Log: limit19_6a.log.  Run: python limit19_6a.py > limit19_6a.log  (seconds).

Published law (Pushkarov, arXiv:cond-mat/0310283, Eq. (61), valid for Delta << T << theta_p, Eq. (53)):
    D_T = a s/(3 alpha sigma_0) (eps(p)/theta_p)^2 (theta_p/T)^9,  theta_p = hbar s/(2a),
    alpha = pi^5 zeta(9)/(240 zeta(8)) = 1.27 (Eq. (58)); mean momentum diffusion <q^2> = alpha sigma_0 (s/a^3)(T/theta_p)^9 (Eq. (58)).
    Below the band width the same source gives D_B = 0.59 (a s/sigma_0)(theta_p/T)^7 (Eq. (64)).

Fuller model used here (MODELLING CHOICE, stated in the text and caption): simple-cubic tight-binding band
    eps(k) = -A sum_i cos(k_i a), band width Delta = 6A (Pushkarov Eq. (3), Delta = zA, z = 6),
with crystal momentum diffusing in small steps (each collision changes k by ~T/s << 1/a, Pushkarov Eq. (54)) at a
k-independent rate D_1 = <q^2>/6 per Cartesian component, and the drift that detailed balance at temperature T requires
(Fokker-Planck form of the heavy particle in a light gas).  The band is separable, so D = D_xx follows from the 1D
backward equation on theta = k_x a in [0, 2 pi):
    D_th (chi'' - U' chi') = -sin(theta),  U = -(A/T) cos(theta),  D_th = a^2 D_1,
    D = (A a/hbar)^2 <sin(theta) chi>_eq   (Green-Kubo),
whose solution in closed form is
    D = T^2/(hbar^2 D_1) [1 - I_0(A/T)^(-2)] = 6 T^2/(hbar^2 <q^2>) [1 - I_0(A/T)^(-2)].
Limits: T >> A gives D_9 = A^2/(2 hbar^2 D_1) = 3 A^2/(hbar^2 <q^2>) proportional to T^-9 (the published exponent and,
with eps(p) = 3A/2, the published prefactor of Eq. (61)); T << A gives the effective-mass law T^2/(hbar^2 D_1),
proportional to T^-7 (Eq. (64) up to its numerical factor).
Ratio plotted: R(T/Delta) = D/D_9 = 2 (T/A)^2 [1 - I_0(A/T)^(-2)].  Leading correction 1 - (5/16)(A/T)^2.
The closed form is checked against a finite-difference solution of the backward equation (printed).
"""
import os
import numpy as np
from scipy.special import i0e, zeta
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch19")
os.makedirs(FIG, exist_ok=True)

Z = 6  # nearest neighbours, simple cubic (Pushkarov: Delta = zA)


def ratio(x):
    """D/D_9 at x = T/Delta, simple-cubic band A = Delta/6."""
    y = 1.0 / (Z * x)  # A/T
    i0 = i0e(y) * np.exp(y)
    return 2.0 / y**2 * (1.0 - 1.0 / i0**2)


def ratio_fd(y, n=4000):
    """Finite-difference check: solve D_th (chi'' - U' chi') = -sin, D_th = 1, U = -y cos; return
    (2/y^2... ) normalised as D/D_9 with A = y T.  D/(A^2 a^2/hbar^2) = <sin chi>/ (a^2 D_1) with D_th = a^2 D_1 = 1."""
    th = np.linspace(0, 2 * np.pi, n, endpoint=False)
    h = th[1] - th[0]
    w = np.exp(y * np.cos(th))  # e^{-U}
    # flux form (w chi')' = -w sin  on a periodic grid
    wh = np.exp(y * np.cos(th + h / 2))
    M = np.zeros((n, n))
    for i in range(n):
        ip, im = (i + 1) % n, (i - 1) % n
        M[i, ip] += wh[i] / h**2
        M[i, im] += wh[im] / h**2
        M[i, i] -= (wh[i] + wh[im]) / h**2
    rhs = -w * np.sin(th)
    # fix gauge: add row enforcing sum chi = 0
    M[0, :] = 1.0
    rhs[0] = 0.0
    chi = np.linalg.solve(M, rhs)
    Zp = np.sum(w)
    val = np.sum(np.sin(th) * chi * w) / Zp  # <sin chi> with D_th = 1
    # D = (A a/hbar)^2 val / (a^2 D_1)... with D_th = a^2 D_1 = 1 ->  D = A^2 val/hbar^2 (units a^2 D_1 = 1)
    # D_9 = A^2/(2 hbar^2 D_1) -> ratio = 2 val
    return 2 * val


alpha = np.pi**5 * zeta(9) / (240 * zeta(8))
print("Pushkarov alpha = pi^5 zeta(9)/(240 zeta(8)) = %.4f (source: 1.27)" % alpha)

# consistency of the two published laws through eps(p) = 3T/2 (Boltzmann, T < Delta)
print("Eq.(61) with eps = 3T/2: prefactor (3/2)^2/(3 alpha) = %.3f (source Eq.(64): 0.59)" % (2.25 / (3 * alpha)))
# effective-mass limit of the model against Eq.(64): D = 6T^2/(hbar^2 <q^2>) -> 6/(4 alpha) a s/sigma0 (theta_p/T)^7
print("model effective-mass limit: 6/(4 alpha) = %.3f  (Eq.(64): 0.59, an estimate 'of the order')" % (6 / (4 * alpha)))
# high-T limit vs Eq.(61): 3A^2 a^3/(alpha sigma0 hbar^2 s) vs 4 c^2 a^3 A^2/(3 alpha sigma0 hbar^2 s) for eps = cA
print("model T >> Delta limit equals Eq.(61) with eps(p) = c A, c = sqrt(9/4) = %.3f, i.e. eps = Delta/4 (simple cubic)" % np.sqrt(9 / 4))

# finite-difference check of the closed form
for y in [0.1, 1.0, 3.0, 10.0]:
    x = 1 / (Z * y)
    print("check A/T = %5.1f: closed form %.6f, finite difference %.6f" % (y, ratio(x), ratio_fd(y, 1200)))

# 10 % and 1 % crossings (root-finder on the closed form)
x10 = brentq(lambda x: ratio(x) - 0.9, 1e-3, 10)
x01 = brentq(lambda x: ratio(x) - 0.99, 1e-3, 100)
print("D/D_9 = 0.90 at T/Delta = %.4f ; 0.99 at T/Delta = %.4f" % (x10, x01))
print("leading correction 1 - (5/16)(A/T)^2 = 1 - (5/576)(Delta/T)^2; at T/Delta = %.3f it gives %.4f"
      % (x10, 1 - 5 / 576 / x10**2))
xs = 0.1
print("at T = 0.1 Delta: D/D_9 = %.4f ; effective-mass law 2(T/A)^2 = %.4f" % (ratio(xs), 2 * (Z * xs) ** 2))
# local exponent d ln D/d ln T = -9 + d ln R/d ln x
for x in [0.02, 0.05, 0.1, 0.2, 0.5, 1.0]:
    e = 1e-4
    s = (np.log(ratio(x * (1 + e))) - np.log(ratio(x * (1 - e)))) / (2 * e)
    print("local exponent of D in T at T/Delta = %.2f: %.3f" % (x, -9 + s))

# confinement by strain gradients (Pushkarov Eqs. (17), (20)): R0 = a (V0/Delta)^(1/n)
for V0, D, n in [(1.0, 25e-6, 3)]:
    print("confinement radius R0/a = (V0/Delta)^(1/n) = %.1f for V0 = %.1f eV, Delta = %.0f ueV, n = %d"
          % ((V0 / D) ** (1 / n), V0, D * 1e6, n))

# ---------------- figure ----------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.8, 3.1))
x = np.logspace(-2, 1.5, 600)
ax.axvspan(x10, x.max(), color="0.88", lw=0)
ax.semilogx(x, ratio(x), "r-", lw=1.6, label=r"band model, $D/D_9$")
ax.semilogx(x, np.minimum(2 * (Z * x) ** 2, 10), "b--", lw=1.0, label=r"effective-mass law $\propto T^{-7}$")
xc = x[x > 0.04]
ax.semilogx(xc, 1 - 5 / 576 / xc**2, "k:", lw=1.0, label=r"$1 - (5/576)(\Delta_{\mathrm{dfn}}/T)^2$")
ax.axhline(1.0, color="0.4", lw=0.6)
ax.set_xlim(1e-2, 10**1.5)
ax.set_ylim(0, 1.15)
ax.set_xlabel(r"$T/\Delta_{\mathrm{dfn}}$")
ax.set_ylabel(r"$D/D_9$")
ax.legend(loc="lower right", fontsize=7.5, frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit19_6a.pdf"))
print("wrote limit19_6a.pdf")
