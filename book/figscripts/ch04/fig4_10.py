"""Fig. 4.10 for Sect. 4.8 (the cut of the bubble) and the numbers quoted in Worked example 4.13.

Output: tex/figures/ch04/fig4_10.pdf
  (a) the bubble with the cut through its two propagators;
  (b) the golden-rule sum of eq. (4.2-S0) for the free electron gas, done by brute force over on-shell pairs
      (Monte Carlo over occupied k, final state k + q kept if empty), against -2 Im R^0 from the cut of the bubble,
      which at T = 0 is the closed form eq. (4.2-gas).

Gas parameters: silicon valence density, k_F = 3.57 keV, E_F = 12.5 eV (Sect. 2.5 / 4.2); q = q_0 = alpha m_e = 3.73 keV
(Sect. 4.2). T = 0. S^0 = 4 pi int d^3k/(2pi)^3 Theta(k_F - k) Theta(|k+q| - k_F) delta(w - k.q/m_e - q^2/2m_e)
(two spins), estimated as 4 pi * (4 pi k_F^3/3)/(2 pi)^3 * (fraction of sampled k in the energy bin)/(bin width).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch04")
plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6, "pdf.fonttype": 42})

me = 510998.95          # eV
kF = 3.57e3             # eV
q = 3.73e3              # eV, q_0 = alpha m_e
EF = kF**2 / (2 * me)
assert abs(EF - 12.47) < 0.01


def S0_closed(w):
    """eq. (4.2-gas), T = 0, in eV^2."""
    a = np.abs(me * w / q - q / 2)
    b = np.sqrt(np.clip(kF**2 - 2 * me * w, 0, None))
    kmin = np.maximum(a, b)
    return np.where(kmin < kF, me / (2 * np.pi * q) * (kF**2 - kmin**2), 0.0)


rng = np.random.default_rng(1)
N = 4_000_000
u = rng.random(N) ** (1 / 3) * kF
c = rng.uniform(-1, 1, N)
k_par = u * c
kq2 = u**2 + 2 * u * c * q + q**2
dE = (kq2 - u**2) / (2 * me)
keep = kq2 > kF**2                      # final state empty (Pauli factor 1 - n_{k+q})
edges = np.linspace(0, 40, 81)
cnt, _ = np.histogram(dE[keep], bins=edges)
pref = 4 * np.pi * (4 * np.pi * kF**3 / 3) / (2 * np.pi) ** 3
S_mc = pref * cnt / N / np.diff(edges)
mid = 0.5 * (edges[1:] + edges[:-1])
S_cl = np.array([np.mean(S0_closed(np.linspace(a, b, 201))) for a, b in zip(edges[:-1], edges[1:])])
mask = S_cl > 0.2 * S_cl.max()
rel = np.sqrt(np.mean((S_mc[mask] / S_cl[mask] - 1) ** 2))
print(f"rms relative deviation over the continuum: {rel:.4f}")
assert rel < 0.01
# integrated weight: 2 pi n_e x unblocked fraction (WE 4.3)
ne = kF**3 / (3 * np.pi**2)
x = q / kF
frac = 3 * x / 4 - x**3 / 16
tot_mc = np.sum(S_mc * np.diff(edges))
assert abs(tot_mc / (2 * np.pi * ne * frac) - 1) < 3e-3
print("weight ratio MC / 2 pi n_e (3q/4kF - q^3/16kF^3):", tot_mc / (2 * np.pi * ne * frac))

fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.7), gridspec_kw=dict(width_ratios=[1, 1.25]))
ax = axs[0]
ax.set_aspect("equal"); ax.axis("off")
ax.set_xlim(-0.4, 3.0); ax.set_ylim(-1.0, 1.0)
t = np.linspace(0, np.pi, 81)
x0, x1, h = 0.4, 2.2, 0.5
xc, r = (x0 + x1) / 2, (x1 - x0) / 2
for xs, ys in [(xc - r * np.cos(t), h * np.sin(t)), (xc + r * np.cos(t), -h * np.sin(t))]:
    ax.plot(xs, ys, color="k", lw=1.0)
    i = 40
    ax.annotate("", xy=(xs[i + 1], ys[i + 1]), xytext=(xs[i - 1], ys[i - 1]),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=0.8, mutation_scale=9))
for a, b in [(-0.3, x0), (x1, 2.9)]:
    ax.plot([a, b], [0, 0], color="k", lw=0.9, ls=(0, (3, 2)))
ax.plot([x0, x1], [0, 0], "o", color="k", ms=3)
ax.plot([xc, xc], [-0.85, 0.85], color="C3", lw=1.6, ls=(0, (4, 2)))
ax.text(xc + 0.06, 0.62, r"$\boldsymbol{k}+\boldsymbol{q}$", fontsize=7.5)
ax.text(xc + 0.06, -0.78, r"$\boldsymbol{k}$", fontsize=7.5)
ax.text(-0.35, 0.8, "(a)")
ax = axs[1]
ax.step(mid, S_mc / (me * kF), where="mid", color="0.55", lw=1.0, label="sum over on-shell pairs")
w = np.linspace(0, 40, 801)
ax.plot(w, S0_closed(w) / (me * kF), color="k", lw=1.1, label=r"$-2\,\mathrm{Im}\,R^0$ (cut)")
ax.set_xlabel(r"$\omega$ (eV)")
ax.set_ylabel(r"$S^0(q_0,\omega)\;/\;m_ek_{\mathrm{F}}$")
ax.set_xlim(0, 40); ax.set_ylim(0, 0.32)
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.text(1, 0.29, "(b)")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_10.pdf"))
print("wrote fig4_10.pdf")
