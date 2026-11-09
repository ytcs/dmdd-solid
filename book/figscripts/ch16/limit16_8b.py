"""Limit Check 16.8b (lim:16.8b, fig:16-limit-ohmic): the ohmic scaling limit of a symmetric tunneling defect.

Literature form: Qureshi (cond-mat/9409105), Eq. (10), K << 1: relaxation (overdamped) rate of the symmetric
defect gamma = Dt0^2/gamma0 with Dt0 = Delta0 (Theta/w_c)^K [Gamma(1-2K) cos(pi K)]^(1/2), gamma0 = K Theta,
Theta = 2 pi T.  His K is the ohmic coupling alpha_ohm of App. C.20 (normalization of eq:C.20-ohmic).
Fuller result: the incoherent (noninteracting-blip) relaxation rate Gamma_LR + Gamma_RL = 2 Gamma_LR of eq:C.20-rate,
which is also Qureshi's Eqs. (8)-(9) at eps = 0, z -> 0.  In the scaling limit it is eq:C.20-ohmrate; the ratio to
the literature form is Gamma(1+alpha)/Gamma(1-alpha) (Sect. 16.8).  Check: the time integral of eq:C.20-rate is
done numerically with the full ohmic Q(t) at finite cutoff (exponential cutoff, eq:C.20-ohmic):
  Q(t) = alpha ln(1 + w_c^2 t^2) + 2 alpha ln[sinh(pi T t)/(pi T t)] + 2 i alpha arctan(w_c t),
the thermal part with the cutoff dropped (error O(T/w_c)).  w_c/T = 1e4.
Plotted: ratio against alpha_ohm.  Dashed: leading correction 1 - 2 gamma_E alpha.  Grey: within 10 %.
Markers: alpha_ohm = 0.28 and 0.44, the Born values of the aluminum resonator fits (Sect. 16.8).
"""
import os
import numpy as np
from scipy.special import gamma as G
from scipy.optimize import brentq
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch16")


def ratio_closed(a):
    return G(1 + a) / G(1 - a)


def qureshi(a, T, wc, D0=1.0):
    Th = 2 * np.pi * T
    Dt2 = D0**2 * (Th / wc)**(2 * a) * G(1 - 2 * a) * np.cos(np.pi * a)
    return Dt2 / (a * Th)


def niba_numeric(a, T, wc, D0=1.0):
    """2 Gamma_LR = 2 (D0^2/4) int dt Re[e^{-Q(t)}] over the real line = D0^2 int_0^inf Re e^{-Q} dt."""
    def f(t):
        if t == 0:
            return 1.0
        x = np.pi * T * t
        lnsh = x + np.log1p(-np.exp(-2 * x)) - np.log(2 * x) if x > 1e-3 else x * x / 6
        ReQ = a * np.log1p((wc * t)**2) + 2 * a * lnsh
        ImQ = 2 * a * np.arctan(wc * t)
        return np.exp(-ReQ) * np.cos(ImQ)
    # integrate in log-spaced pieces
    edges = np.concatenate(([0.0], np.geomspace(1e-3 / wc, 60 / T, 80)))
    tot = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        tot += quad(f, lo, hi, limit=200, epsabs=0, epsrel=1e-9)[0]
    return D0**2 * tot


a10 = brentq(lambda a: ratio_closed(a) - 0.9, 1e-4, 0.5)
print(f"Gamma(1+a)/Gamma(1-a) = 0.9 at alpha_ohm = {a10:.4f}; leading term 1 - 2 gamma_E a = 0.9 at {0.1/(2*np.euler_gamma):.4f}")
for a in (0.05, 0.1, 0.2, 0.28, 0.3, 0.44, 0.49):
    print(f"  alpha = {a}: closed ratio {ratio_closed(a):.4f}")
T, wc = 1.0, 1e4
for a in (0.05, 0.1, 0.2, 0.28, 0.4):
    num = niba_numeric(a, T, wc)
    print(f"  numeric time integral, w_c/T = {wc:.0e}, alpha = {a}: ratio to Qureshi Eq. (10) = {num/qureshi(a, T, wc):.4f} "
          f"(closed form {ratio_closed(a):.4f})")
# anti-Arrhenius exponent and crossover to coherence (symmetric defect): Dt0(T) = gamma0/2
for a in (0.05, 0.28):
    print(f"  alpha = {a}: rate ~ T^({2*a-1:.2f})")

for a in (0.05, 0.1, 0.28):
    print(f"  coherence below T_coh = (Delta_r/2pi)(2/alpha)^(1/(1-alpha)) = {(2/a)**(1/(1-a))/(2*np.pi):.3f} Delta_r "
          f"(alpha = {a}; small-alpha form 1/(pi alpha) = {1/(np.pi*a):.3f})")
al = np.linspace(0.0, 0.5, 300)[1:]
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.0))
ax.axvspan(0, a10, color="0.88", lw=0)
ax.plot(al, ratio_closed(al), "C3", lw=1.5, label=r"$\Gamma(1+\alpha_{\mathrm{ohm}})/\Gamma(1-\alpha_{\mathrm{ohm}})$")
anum = np.array([0.05, 0.1, 0.2, 0.3, 0.4])
ax.plot(anum, [niba_numeric(a, T, wc) / qureshi(a, T, wc) for a in anum], "ko", ms=3.5, mfc="none",
        label=r"time integral, $\omega_{\mathrm{cut}} = 10^4\,T$")
ax.plot(al, 1 - 2 * np.euler_gamma * al, "k--", lw=0.9, label=r"$1 - 2\gamma_{\mathrm{E}}\alpha_{\mathrm{ohm}}$")
for a in (0.28, 0.44):
    ax.axvline(a, color="0.5", lw=0.6, ls=":")
ax.axhline(1, color="k", lw=0.6)
ax.set_xlim(0, 0.5); ax.set_ylim(0.4, 1.05)
ax.set_xlabel(r"$\alpha_{\mathrm{ohm}}$")
ax.set_ylabel(r"incoherent rate / small-$\alpha$ form")
ax.legend(frameon=False, fontsize=7.5, loc="lower left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_8b.pdf"))
print("saved limit16_8b.pdf")
