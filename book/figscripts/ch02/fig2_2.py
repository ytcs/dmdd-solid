"""Fig. 2.2: hydrogen 1s elastic form factor F_1s(q) = 16/(4 + q^2 a0^2)^2 against q a0 (Sect. 2.2, WE 2.2).
Output: tex/figures/ch02/fig2_2.pdf.

Curves: F_1s, F_1s^2 (elastic probability) and 1 - F_1s^2 (total inelastic probability, from closure, Sect. 2.2).
Marked: q0 = alpha m_e = 1/a0, i.e. q a0 = 1 exactly (a0 = 1/(alpha m_e) = 0.5292 Angstrom, App. A.1; q0 = 3.73 keV, Sect. 1.3).
No external data. Numbers printed below are quoted in the text.
"""
import os
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def F1s(x):
    return 16.0 / (4.0 + x**2)**2


# check the closed form against the radial integral (4/x) int_0^inf u e^{-2u} sin(xu) du, u = r/a0
for x in (0.3, 1.0, 3.0):
    num = quad(lambda u: 4 * u**2 * np.exp(-2 * u) * np.sinc(x * u / np.pi), 0, 60)[0]
    assert abs(num - F1s(x)) < 1e-8, (x, num, F1s(x))

print("F1s(q0) =", F1s(1.0), " F1s^2 =", F1s(1.0)**2, " 1-F^2 =", 1 - F1s(1.0)**2)
xh = np.sqrt(np.sqrt(32.0) - 4.0)
print("F = 1/2 at q a0 =", xh)
x2 = np.sqrt(np.sqrt(16 / np.sqrt(0.5)) - 4.0)
print("F^2 = 1/2 at q a0 =", x2)
print("F1s(2/a0) =", F1s(2.0), " F1s(5/a0) =", F1s(5.0), " 16/x^4 at 5 =", 16 / 5.0**4)
print("small-q: 1 - x^2/2 at x=0.2:", 1 - 0.02, " exact", F1s(0.2))

x = np.logspace(-2, 1.5, 600)
plt.rcParams.update({"font.size": 9})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.plot(x, F1s(x), "k-", label=r"$F_{1s}$")
ax.plot(x, F1s(x)**2, "C3--", label=r"$F_{1s}^2$ (elastic)")
ax.plot(x, 1 - F1s(x)**2, "C0-.", label=r"$1 - F_{1s}^2$ (inelastic)")
ax.axvline(1.0, color="0.5", lw=0.8, ls=":")
ax.text(0.93, 0.04, r"$q = q_0$", color="0.3", ha="right")   # left of the line, clear of the curves
ax.set_xscale("log")
ax.set_xlim(1e-2, 10**1.5)
ax.set_ylim(0, 1.05)
ax.set_xlabel(r"$q a_0$")
ax.set_ylabel("form factor, probability")
ax.legend(frameon=False, loc="center left")
fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch02", "fig2_2.pdf")
fig.savefig(out)
print("wrote", os.path.abspath(out))

# --- 1s -> 2p (m = 0, q along z): |f|^2 = 72 x^2/(9/4 + x^2)^6, x = q a0 (Sect. 2.2, after WE 2.2) ---------------
def f2p2(x):
    return 72 * x**2 / (2.25 + x**2)**6


# check the closed form by direct quadrature of <2p0| e^{i q z} |1s>, a0 = 1
from scipy.special import spherical_jn
for xx in (0.3, 1.0, 2.0):
    rad = quad(lambda r: r**3 * np.exp(-1.5 * r) * spherical_jn(1, xx * r), 0, 80)[0]
    amp = 4 * np.pi * rad / np.sqrt(32 * np.pi * np.pi)
    assert abs(amp**2 - f2p2(xx)) < 1e-10, (xx, amp**2, f2p2(xx))
xs = np.linspace(0.01, 3, 30000)
i = np.argmax(f2p2(xs))
print("1s->2p: small-q coeff 2^15/3^10 =", 2**15 / 3**10, " peak at x =", xs[i], " value", f2p2(xs[i]),
      " at x=1:", f2p2(1.0), " fraction of inelastic at q0:", f2p2(1.0) / (1 - F1s(1.0)**2))
