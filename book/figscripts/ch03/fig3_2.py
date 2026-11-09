"""Fig. 3.2: the first Brillouin zone of the fcc lattice with its high-symmetry points (Sect. 3.1), and the zone numbers
quoted in Sect. 3.1. Output: tex/figures/ch03/fig3_2.pdf.

Geometry (definitions, no external input). Units of 2pi/a. Reciprocal primitive vectors of the fcc lattice
  b1 = (-1,1,1), b2 = (1,-1,1), b3 = (1,1,-1)   (from a_i . b_j = 2 pi delta_ij with a1 = (a/2)(0,1,1) etc.).
The zone is the Wigner-Seitz cell of the reciprocal lattice: bounded by the bisecting planes of the eight (111)-type and six
(200)-type vectors. Its 24 vertices are the W points, all permutations of (+-1, +-1/2, 0). High-symmetry points:
  Gamma = 0, X = (1,0,0), L = (1/2,1/2,1/2), K = (3/4,3/4,0), W = (1,1/2,0).
Silicon: a = 5.431 A (CODATA 2022, Mohr et al., RMP 97, 025002 (2025)); hbar c = 1973.2698 eV A (CODATA 2018).
"""
import os
import itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

A = 5.431
HBARC = 1973.2698          # eV A
U = 2 * np.pi * HBARC / A  # 2pi/a in eV

b = np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], float)
assert np.allclose(np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) / 2 @ b.T, np.eye(3))   # a_i . b_j = delta_ij (units 2pi)

# Wigner-Seitz cell: check every W point is equidistant from 0 and its nearest G, and nothing is closer
Gs = np.array([m @ b for m in itertools.product(range(-3, 4), repeat=3)])
def nearestG(k):
    d = np.linalg.norm(Gs - k, axis=1)
    return d.min(), np.linalg.norm(k)
verts = set()
for perm in itertools.permutations([1.0, 0.5, 0.0]):
    for sg in itertools.product([1, -1], repeat=3):
        verts.add(tuple(np.array(perm) * sg))
verts = np.array(sorted(verts))
assert len(verts) == 24
for v in verts:
    dmin, d0 = nearestG(v)
    assert abs(dmin - d0) < 1e-12        # on the zone boundary
edges = [(p, q) for p, q in itertools.combinations(verts, 2) if abs(np.linalg.norm(p - q) - np.sqrt(0.5)) < 1e-9]
assert len(edges) == 36                  # truncated octahedron: 24 vertices, 36 edges, 14 faces

pts = {"Γ": np.zeros(3), "X": np.array([1, 0, 0.]), "L": np.array([.5, .5, .5]), "K": np.array([.75, .75, 0]),
       "W": np.array([1, .5, 0])}
for name, p in pts.items():
    print(f"|Gamma{name}| = {np.linalg.norm(p):.4f} (2pi/a) = {np.linalg.norm(p) * U / 1e3:.3f} keV")
print(f"2pi/a = {U:.1f} eV = {2*np.pi/A:.4f} A^-1; |G_111| = {np.sqrt(3)*U:.1f} eV; |G_200| = {2*U:.1f} eV;"
      f" |G_220| = {np.sqrt(8)*U:.1f} eV")
vol = abs(np.linalg.det(b))           # units (2pi/a)^3
print(f"zone volume = {vol:.1f} (2pi/a)^3 = (2pi)^3/Omega with Omega = a^3/4")
k_bz = (3 * vol / (4 * np.pi)) ** (1 / 3)
print(f"radius of the sphere of zone volume = {k_bz:.4f} (2pi/a) = {k_bz*U/1e3:.3f} keV")
print(f"Fermi sphere holding 8 electrons per cell = 4 zone volumes: k_F = 4^(1/3) k_BZ = {4**(1/3)*k_bz*U/1e3:.3f} keV"
      " (Sect. 2.5: 3.57 keV)")

# ---- figure -------------------------------------------------------------------------------------------------------
fig = plt.figure(figsize=(4.0, 4.0))
ax = fig.add_subplot(111, projection="3d")
ax.set_proj_type("ortho")
elev, azim = 18, 22
ax.view_init(elev=elev, azim=azim)
# visibility of an edge: hidden if both adjacent faces face away from the viewer
view = np.array([np.cos(np.radians(elev)) * np.cos(np.radians(azim)),
                 np.cos(np.radians(elev)) * np.sin(np.radians(azim)), np.sin(np.radians(elev))])
normals = [np.array(n, float) for n in itertools.product([1, -1], repeat=3)] + \
          [s * e for e in np.eye(3) for s in (1, -1)]
offsets = [1.5] * 8 + [1.0] * 6            # face planes n.k = offset (units 2pi/a): (111) faces at |n|^2*... see below
def on_face(p, n, off):
    return abs(np.dot(p, n) - off) < 1e-9
for p, q in edges:
    faces = [n for n, off in zip(normals, offsets) if on_face(p, n, off) and on_face(q, n, off)]
    visible = any(np.dot(n, view) > 0 for n in faces)
    ax.plot(*zip(p, q), color="0.15" if visible else "0.6", lw=1.1 if visible else 0.7, ls="-" if visible else "--")
for name, p in pts.items():
    ax.plot([0, p[0]], [0, p[1]], [0, p[2]], color="#cb181d", lw=1.0)
    ax.scatter(*p, color="#cb181d", s=14, depthshade=False)
    # label offsets chosen to keep each label off the zone edges and the k axes
    off = {"Γ": (0.0, -0.22, 0.04), "X": (0.0, -0.16, 0.03), "L": (0.03, 0.0, 0.06), "K": (0.0, 0.06, -0.12),
           "W": (0.0, -0.08, -0.2)}[name]
    ax.text(*(p + np.array(off)), r"$\mathrm{%s}$" % ("\\Gamma" if name == "Γ" else name), fontsize=11, color="#cb181d")
for e, lab in zip(np.eye(3) * 1.5, [r"$k_x$", r"$k_y$", r"$k_z$"]):
    ax.plot(*zip(np.zeros(3), e), color="0.5", lw=0.6)
    ax.text(*(1.03 * e + (np.array([0, 0.12, -0.08]) if lab == r"$k_x$" else np.array([0, 0.04, 0.03]))), lab,
            fontsize=9, color="0.35", ha="left")
ax.set_box_aspect((1, 1, 1))
lim = 1.12
ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
ax.set_axis_off()
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch03", "fig3_2.pdf")
fig.savefig(out, bbox_inches="tight", pad_inches=0.02)
print("wrote", os.path.normpath(out))
