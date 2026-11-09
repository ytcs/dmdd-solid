"""Fig. 3.5: tight-binding s band of a face-centred cubic lattice (Sect. 3.2). Output: tex/figures/ch03/fig3_5.pdf.

Model (definitions and modelling choices): one s orbital per fcc site, hopping -t_hop between the 12 nearest neighbours
at (a/2)(+-1,+-1,0) and permutations, no hopping beyond them, and the overlap of orbitals on different sites neglected.
Then eps_k = E_s - t_hop * gamma(k), gamma(k) = sum_{nn} exp(ik.R) = 4[cos(k_x a/2)cos(k_y a/2) + cyclic] (Sect. 3.2).
The band is plotted as (eps_k - E_s)/t_hop, so no value of t_hop is assumed. Path L-Gamma-X-W-K-Gamma through the
high-symmetry points of Sect. 3.1 (units of 2pi/a): L = (1/2,1/2,1/2), X = (1,0,0), W = (1,1/2,0), K = (3/4,3/4,0).
The right panel is the density of states per cell, histogrammed from a uniform grid of 160^3 points in the cube
[-2pi/a, 2pi/a)^3 (which holds four zone volumes, so every k is counted four times; the normalization divides by this).
No external input.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def gamma(k):
    """k in units of 2pi/a; returns the nearest-neighbour sum."""
    x, y, z = np.pi * k[..., 0], np.pi * k[..., 1], np.pi * k[..., 2]   # k_i a/2
    return 4 * (np.cos(x) * np.cos(y) + np.cos(y) * np.cos(z) + np.cos(z) * np.cos(x))


def band(k):
    return -gamma(np.asarray(k, float))


P = {"L": (0.5, 0.5, 0.5), r"$\Gamma$": (0, 0, 0), "X": (1, 0, 0), "W": (1, 0.5, 0), "K": (0.75, 0.75, 0)}
for name, k in P.items():
    print(f"{name:10s} (eps - E_s)/t_hop = {band(k):+.4f}")
assert abs(band(P[r"$\Gamma$"]) + 12) < 1e-12 and abs(band(P["X"]) - 4) < 1e-12 and abs(band(P["W"]) - 4) < 1e-12
assert abs(band(P["L"])) < 1e-12

# effective mass at Gamma: eps ~ E_s - 12 t + t a^2 k^2  ->  1/(2 m*) = t a^2 (k in absolute units)
kk = 1e-3
curv = (band((kk, 0, 0)) + 12) / (2 * np.pi * kk) ** 2       # coefficient of (k a)^2 in units of t
print(f"curvature at Gamma: (eps - eps_Gamma)/(t (k a)^2) = {curv:.6f} (expected 1)")
assert abs(curv - 1) < 1e-5
# group velocity vanishes at X along Gamma-X (and on the whole X-W line the band is flat at +4 t)
for s in np.linspace(0, 0.5, 6):
    assert abs(band((1, s, 0)) - 4) < 1e-12
print("band is flat at +4 t_hop along X-W (k = (1, s, 0) 2pi/a)")

# density of states per cell, normalized to one state per cell (spin not counted)
n = 160
g = (np.arange(n) / n) * 4 - 2 + 2 / n
KX, KY, KZ = np.meshgrid(g, g, g, indexing="ij")
E = band(np.stack([KX, KY, KZ], axis=-1)).ravel()
assert abs(E.mean()) < 1e-9          # the band centre of gravity sits at E_s (sum over the zone of gamma(k) vanishes)
hist, edges = np.histogram(E, bins=112, range=(-12, 4.0), density=True)
print(f"band from -12 to +4 t_hop (width 16 t_hop); mean energy {E.mean():.2e} t_hop; "
      f"fraction of states above 0: {np.mean(E > 0):.3f}")

# ---- figure -------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(5.6, 3.2), sharey=True, gridspec_kw={"width_ratios": [3, 1], "wspace": 0.05})
path = ["L", r"$\Gamma$", "X", "W", "K", r"$\Gamma$"]
xs, ys, ticks = [], [], [0.0]
x0 = 0.0
for a, b in zip(path[:-1], path[1:]):
    ka, kb = np.array(P[a], float), np.array(P[b], float)
    L = np.linalg.norm(kb - ka)
    t = np.linspace(0, 1, 200)
    ks = ka[None, :] + t[:, None] * (kb - ka)[None, :]
    xs.append(x0 + t * L)
    ys.append(band(ks))
    x0 += L
    ticks.append(x0)
for x, y in zip(xs, ys):
    ax.plot(x, y, color="#08519c", lw=1.4)
for t in ticks:
    ax.axvline(t, color="0.75", lw=0.6)
ax.axhline(0, color="0.6", lw=0.6, ls="--")
ax.set_xticks(ticks)
ax.set_xticklabels(path)
ax.set_xlim(0, ticks[-1])
ax.set_ylim(-13, 5.5)
ax.set_ylabel(r"$(\varepsilon_{1\boldsymbol{k}} - E_s)/t_{\mathrm{hop}}$")
ax.text(0.04, 4.6, "(a)", fontsize=9)
centres = 0.5 * (edges[1:] + edges[:-1])
bx.fill_betweenx(centres, 0, hist, color="#9ecae1", lw=0)
bx.plot(hist, centres, color="#08519c", lw=0.8)
bx.axhline(0, color="0.6", lw=0.6, ls="--")
bx.set_xlim(0, 1.05 * hist.max())
bx.set_xticks([])
bx.set_xlabel("DOS")
bx.text(0.05 * hist.max(), 4.6, "(b)", fontsize=9)
fig.subplots_adjust(left=0.13, right=0.97, bottom=0.12, top=0.97)
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch03", "fig3_5.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
