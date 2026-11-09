"""Fig. 2.4: the two time orderings of a second-order process in which a target absorbs one quantum (energy omega_1)
and emits another (energy omega_2), Sect. 2.4, Eq. (2.4-orderings).
Output: tex/figures/ch02/fig2_4.pdf. Schematic, no numbers: time runs to the right; the thick line is the target,
in state i_T, then an intermediate state m, then f_T; wavy lines are the quanta (absorbed: from below; emitted: upward).
Each panel prints the energy denominator E_i - E_I of its intermediate state, with E_i = E_{i_T} + omega_1 the energy of
the initial state and E_I = E_m (absorb first) or E_m + omega_1 + omega_2 (emit first).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})


def wavy(ax, p0, p1, n=6, amp=0.06, **kw):
    """Sinusoidal line from p0 to p1 (a quantum)."""
    p0, p1 = np.array(p0, float), np.array(p1, float)
    d = p1 - p0
    L = np.hypot(*d)
    s = np.linspace(0, 1, 400)
    perp = np.array([-d[1], d[0]]) / L
    pts = p0[None, :] + s[:, None] * d[None, :] + (amp * np.sin(2 * np.pi * n * s))[:, None] * perp[None, :]
    ax.plot(pts[:, 0], pts[:, 1], **kw)


def panel(ax, title, first, second, mid_label, denom):
    t1, t2 = 1.0, 2.0
    ax.plot([0, 3], [0, 0], color="k", lw=2.2)
    for t in (t1, t2):
        ax.plot([t], [0], "o", color="k", ms=4.5)
    ax.text(0.5, 0.1, r"$i_{\mathrm{T}}$", ha="center", va="bottom", fontsize=11)
    ax.text(1.5, 0.1, mid_label, ha="center", va="bottom", fontsize=11)
    ax.text(2.5, 0.1, r"$f_{\mathrm{T}}$", ha="center", va="bottom", fontsize=11)
    for t, (kind, lab) in ((t1, first), (t2, second)):
        if kind == "in":     # absorbed quantum arrives from the lower left
            wavy(ax, (t - 0.55, -0.6), (t, 0.0), color="C0", lw=1.2)
            ax.text(t - 0.66, -0.62, lab, ha="right", va="center", color="C0", fontsize=10)
        else:                # emitted quantum leaves to the upper right
            wavy(ax, (t, 0.0), (t + 0.55, 0.85), color="C3", lw=1.2)
            ax.text(t + 0.62, 0.92, lab, ha="center", va="bottom", color="C3", fontsize=10)
    ax.annotate("", xy=(3.0, -0.95), xytext=(1.6, -0.95),
                arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
    ax.text(2.3, -1.0, "time", ha="center", va="top", color="0.4", fontsize=8)
    ax.text(1.5, 1.32, denom, ha="center", va="bottom", fontsize=9)
    ax.set_title(title, fontsize=9, pad=14)
    ax.set_xlim(-0.2, 3.2); ax.set_ylim(-1.2, 1.6)
    ax.axis("off")


fig, (a, b) = plt.subplots(1, 2, figsize=(6.3, 2.5))
panel(a, "(a) absorb first", ("in", r"$\omega_1$"), ("out", r"$\omega_2$"), r"$m$",
      r"denominator $E_{i_{\mathrm{T}}} + \omega_1 - E_m$")
panel(b, "(b) emit first", ("out", r"$\omega_2$"), ("in", r"$\omega_1$"), r"$m$",
      r"denominator $E_{i_{\mathrm{T}}} - \omega_2 - E_m$")
fig.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch02", "fig2_4.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
