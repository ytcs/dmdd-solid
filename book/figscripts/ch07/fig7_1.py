"""Fig. 7.1: magnetic structure of NiO and its linear spin-wave dispersion (Sect. 7.1, worked example 7.2).
Output: tex/figures/ch07/fig7_1.pdf. Prints every number quoted in Sect. 7.1 and in worked example 7.2.

Model (modelling choices, also named in the caption):
  Heisenberg model H = sum_<ij> J_ij S_i.S_j, each pair once, J > 0 antiferromagnetic (eq:E.9-heis), on the
  undistorted fcc lattice of Ni2+ ions; type-II order (ferromagnetic (111) planes alternating in sign);
  nearest-neighbour J1 and next-nearest-neighbour J2 only; no anisotropy; no rhombohedral distortion; |S| = 1.
  Linear spin-wave theory of App. D.19, eq:D.19-omega:
    omega_k = |S| sqrt(A_k^2 - B_k^2), A_k = J_AB(0) - J_AA(0) + J_AA(k), B_k = J_AB(k).
Inputs (sources):
  J2 = 19.01 meV, J1 = -1.37 meV in the convention H^{1,2} = J S1.S2 per pair (same as the book's):
     Hutchings and Samuelsen, PRB 6, 3447 (1972), abstract.
  Measured (same abstract, 78 K): initial slope ~250 meV A, maximum ~117 meV.
  a = 4.17 A, experimental lattice constant of NiO: Fischer et al., PRB 80, 014408 (2009), Table I.
  hbar c = 1973.2698 eV A; c = 299792.458 km/s (CODATA).
  v_max = 2.650e-3 (Sect. 1.3); silicon LA speed along [100] 8.43 km/s (App. C.18).
Zone scan: 400,000 random wavevectors in the cube |k_i| <= 2 pi/a (covers the zone of one sublattice), then a local
  maximization from the best sample.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch07", "fig7_1.pdf")
HC = 1973.2698e3          # meV A
CKMS = 299792.458
J1, J2, S, A = -1.37, 19.01, 1.0, 4.17
VMAX, C_LA_SI = 2.650e-3, 8.43

# neighbours of a site of sublattice A; a site R = (a/2) n is on A if (n1+n2+n3)/2 is even
nn = []
for v in [(1, 1, 0), (1, 0, 1), (0, 1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1)]:
    nn += [np.array(v), -np.array(v)]
nn = np.array(nn, float)
par = nn[np.isclose(nn.sum(1), 0)] * A / 2        # 6 nearest neighbours in the same (111) plane: parallel
anti = nn[~np.isclose(nn.sum(1), 0)] * A / 2      # 6 nearest neighbours in adjacent planes: antiparallel
nnn = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)], float) * A  # all antiparallel


def omega(k, j1=J1, j2=J2):
    k = np.atleast_2d(k)
    jaa = j1 * np.cos(k @ par.T).sum(1)
    jab = j1 * np.cos(k @ anti.T).sum(1) + j2 * np.cos(k @ nnn.T).sum(1)
    a_k = (6 * j1 + 6 * j2) - 6 * j1 + jaa
    return S * np.sqrt(np.maximum(a_k**2 - jab**2, 0.0))


G = 2 * np.pi / A
# ---- numbers of the text --------------------------------------------------------------------------------------
v2 = 2 * np.sqrt(3) * J2 * S * A
v111 = 2 * np.sqrt(3) * (J1 + J2) * S * A
print(f"J2 only: velocity 2 sqrt3 J2 |S| a = {v2:.1f} meV A = {v2/HC:.3e} = {v2/HC*CKMS:.1f} km/s")
print(f"[111] with J1: 2 sqrt3 (J1+J2)|S| a = {v111:.1f} meV A = {v111/HC:.3e}")
dirs = {"[111]": (1, 1, 1), "[11-1]": (1, 1, -1), "[100]": (1, 0, 0), "[110]": (1, 1, 0), "[1-10]": (1, -1, 0)}
sl = {}
for name, d in dirs.items():
    d = np.array(d, float) / np.linalg.norm(d)
    sl[name] = omega(1e-5 * d)[0] / 1e-5
    print(f"  numerical slope along {name}: {sl[name]:.1f} meV A")
print(f"slope range with J1: {min(sl.values()):.0f}-{max(sl.values()):.0f} meV A; measured ~250 meV A")
print(f"v/v_max = {v2/HC/VMAX:.3f}, v_max/v = {VMAX/(v2/HC):.1f}; v/c_LA(Si) = {v2/HC*CKMS/C_LA_SI:.1f}")
print(f"zone maximum J2 only 6 J2 |S| = {6*J2*S:.2f} meV; bound with J1 |S|(6 J2 - 3 J1) = {S*(6*J2-3*J1):.2f} meV")
rng = np.random.default_rng(1)
ks = rng.uniform(-1, 1, (400000, 3)) * G
ww = omega(ks)
k0 = ks[np.argmax(ww)]
res = minimize(lambda x: -omega(x)[0], k0)
print(f"zone scan maximum {-res.fun:.2f} meV at k = {res.x/G} (2pi/a); J2-only scan max {omega(ks, j1=0).max():.2f} meV")
for p in [(0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (1, 0, 0)]:
    print(f"omega at {p} (2pi/a): {omega(np.array(p)*G)[0]:.3e} meV")
# superexchange inversion t ~ (J U)^(1/2) for U_H = 4.6 and 8.17 eV (App. E.9)
for U in (4.6, 8.17):
    print(f"(J2 U_H)^(1/2) for U_H = {U} eV: {np.sqrt(J2*1e-3*U):.2f} eV; (J2 U_H/4)^(1/2): {np.sqrt(J2*1e-3*U/4):.2f} eV")

# ---- figure ---------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 8.5})
fig = plt.figure(figsize=(7.0, 3.0))
ax = fig.add_axes([0.0, 0.02, 0.38, 0.92], projection="3d")
bx = fig.add_axes([0.47, 0.15, 0.48, 0.76])

# (a) conventional cubic cell: Ni at fcc sites, O at edge centres and body centre
ni, ox = [], []
for i in range(3):
    for j in range(3):
        for k in range(3):
            n = np.array([i, j, k])
            if n.sum() % 2 == 0:
                ni.append(n)
            else:
                ox.append(n)
ni, ox = np.array(ni), np.array(ox)
sign = np.where((ni.sum(1) // 2) % 2 == 0, 1, -1)
for e in [((0, 0, 0), (2, 0, 0)), ((0, 0, 0), (0, 2, 0)), ((0, 0, 0), (0, 0, 2)), ((2, 2, 2), (0, 2, 2)),
          ((2, 2, 2), (2, 0, 2)), ((2, 2, 2), (2, 2, 0)), ((2, 0, 0), (2, 2, 0)), ((2, 0, 0), (2, 0, 2)),
          ((0, 2, 0), (2, 2, 0)), ((0, 2, 0), (0, 2, 2)), ((0, 0, 2), (2, 0, 2)), ((0, 0, 2), (0, 2, 2))]:
    p, q = np.array(e)
    ax.plot(*zip(p, q), color="0.7", lw=0.6)
ax.scatter(*ox.T, s=10, color="0.55", depthshade=False)
cu, cd = "#1f5fa8", "#c0392b"
for n, s in zip(ni, sign):
    col = cu if s > 0 else cd
    ax.scatter(*n, s=22, color=col, depthshade=False)
    ax.quiver(*(n - 0.35 * s * np.array([0, 0, 1])), 0, 0, 0.7 * s, color=col, lw=1.1, arrow_length_ratio=0.35)
# one (111) plane of up spins: n1+n2+n3 = 4
tri = np.array([[2, 2, 0], [2, 0, 2], [0, 2, 2]])
ax.plot_trisurf(*tri.T, color=cu, alpha=0.25, edgecolor=cu, linewidth=0.5)
tri2 = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
ax.plot_trisurf(*tri2.T, color=cd, alpha=0.25, edgecolor=cd, linewidth=0.5)
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=22, azim=-28)
ax.set_axis_off()
ax.set_title("(a) NiO, type-II order", fontsize=8.5, loc="left")

# (b) dispersion along three lines from Gamma
segs = [((0.5, 0.5, 0.5), (0, 0, 0)), ((0, 0, 0), (0.5, 0.5, -0.5)), ((0, 0, 0), (1, 0, 0))]
x0, ticks, labs = 0.0, [0.0], []
for i, (p, q) in enumerate(segs):
    p, q = np.array(p, float) * G, np.array(q, float) * G
    t = np.linspace(0, 1, 400)
    k = p[None, :] + t[:, None] * (q - p)[None, :]
    L = np.linalg.norm(q - p)
    x = x0 + t * L
    bx.plot(x, omega(k), color="k", lw=1.2, label=r"$J_1$ and $J_2$" if i == 0 else None)
    bx.plot(x, omega(k, j1=0.0), color="#1f5fa8", lw=1.0, ls="--", label=r"$J_2$ only" if i == 0 else None)
    x0 += L
    ticks.append(x0)
    if i < len(segs) - 1:
        bx.axvline(x0, color="0.6", lw=0.6)
# linear law near Gamma along [111] and from J2 alone
xg = ticks[1]
kk = np.linspace(0, 0.36, 50)
bx.plot(xg - kk, v111 * kk, color="0.3", lw=1.0, ls=":", label="linear law")
bx.plot(xg + kk, v2 * kk, color="#1f5fa8", lw=1.0, ls=":")
bx.axhline(117, color="#c0392b", lw=0.8, ls="-.", label="measured maximum")
bx.set_xticks(ticks)
bx.set_xticklabels([r"$(\frac{1}{2},\frac{1}{2},\frac{1}{2})$", r"$\Gamma$", r"$(\frac{1}{2},\frac{1}{2},-\frac{1}{2})\,|\,\Gamma$", r"$(1,0,0)$"])
bx.set_xlim(0, ticks[-1])
bx.set_ylim(0, 150)
bx.set_ylabel(r"$\omega^{\mathrm{M}}_{\vect{k}}$ (meV)".replace(r"\vect{k}", r"\mathbf{k}"))
bx.set_title(r"(b) linear spin waves, wavevectors in units of $2\pi/a$", fontsize=8.5, loc="left")
bx.legend(fontsize=6.5, frameon=False, loc="upper center", ncol=4, bbox_to_anchor=(0.5, 1.0), handlelength=1.8, columnspacing=1.0)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT)
print("wrote", os.path.relpath(OUT, HERE))
