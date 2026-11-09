"""Fig. 3.1: the diamond structure (Sect. 3.1), and the structural numbers of silicon quoted in Sect. 3.1.
Output: tex/figures/ch03/fig3_1.pdf.

Geometry (definitions, no external input): fcc Bravais lattice with primitive vectors
  a1 = (a/2)(0,1,1), a2 = (a/2)(1,0,1), a3 = (a/2)(1,1,0),
two-atom basis tau_1 = 0, tau_2 = (a/4)(1,1,1). The figure draws one conventional cube of side a: the atoms of the
tau_1 sublattice (cube corners and face centers) and the four tau_2 atoms inside the cube, the bonds between nearest
neighbours (length sqrt(3) a/4), and the three primitive vectors from the origin. A display choice: the tau_1 atoms on the
cube surface are all drawn, including those whose bonding partners lie outside the cube.

Inputs and their sources:
  a = 5.431 A, silicon lattice parameter     (CODATA 2022, Mohr et al., RMP 97, 025002 (2025), "lattice parameter of silicon",
                                              5.431 020 511 A at 22.5 C; the book uses 5.431 A, as Sect. 1.3)
  M(Si) = 28.0855 u, standard atomic weight  (IUPAC; as the book's Sect. 1.3, 26.16 GeV)
  u = 1.66053907e-24 g                       (CODATA 2018)
"""
import os
import itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

A = 5.431            # Angstrom
U_G = 1.66053907e-24  # g
M_SI_U = 28.0855

# ---- numbers quoted in Sect. 3.1 -----------------------------------------------------------------------------------
a1, a2, a3 = (A / 2) * np.array([0, 1, 1]), (A / 2) * np.array([1, 0, 1]), (A / 2) * np.array([1, 1, 0])
omega = np.dot(a1, np.cross(a2, a3))
assert abs(omega - A**3 / 4) < 1e-9
d_nn = np.sqrt(3) * A / 4
n_atoms = 8 / (A * 1e-8) ** 3                  # atoms per cm^3
rho = n_atoms * M_SI_U * U_G                   # g/cm^3
n_e_val = 4 * n_atoms                          # valence electrons per cm^3
atoms_per_kg = 1000 / (M_SI_U * U_G)
cells_per_kg = atoms_per_kg / 2
print(f"Omega = a^3/4 = {omega:.2f} A^3; conventional cube a^3 = {A**3:.1f} A^3")
print(f"nearest-neighbour distance sqrt(3)a/4 = {d_nn:.3f} A; fcc neighbour distance a/sqrt2 = {A/np.sqrt(2):.3f} A")
print(f"atom density 8/a^3 = {n_atoms:.3e} cm^-3; mass density = {rho:.3f} g/cm^3 (Sect. 1.2: 2.33)")
print(f"valence electron density 32/a^3 = {n_e_val:.3e} cm^-3 (Sect. 2.5 / App. A.2: 2.00e23)")
print(f"atoms per kg = {atoms_per_kg:.3e}; cells (= k points per band) per kg = {cells_per_kg:.3e}")
# tetrahedral angle
b1v, b2v = np.array([1, 1, 1]), np.array([1, -1, -1])
print(f"bond angle = {np.degrees(np.arccos(np.dot(-b1v, -b2v) / 3)):.2f} deg")

# ---- figure -------------------------------------------------------------------------------------------------------
s1 = [np.array(p, float) for p in itertools.product([0, 1], repeat=3)]                  # corners
s1 += [np.array(p, float) for p in [(0.5, 0.5, 0), (0.5, 0.5, 1), (0.5, 0, 0.5), (0.5, 1, 0.5), (0, 0.5, 0.5), (1, 0.5, 0.5)]]
s2 = [np.array(p) + 0.25 for p in [(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)]]
bonds = []
for p in s2:
    for r in s1:
        if abs(np.linalg.norm(p - r) - np.sqrt(3) / 4) < 1e-9:
            bonds.append((p, r))
assert len(bonds) == 16                         # every interior atom has its four neighbours inside the cube

fig = plt.figure(figsize=(4.4, 4.0))
ax = fig.add_subplot(111, projection="3d")
ax.set_proj_type("ortho")
edges = [(p, q) for p, q in itertools.combinations(s1[:8], 2) if abs(np.linalg.norm(p - q) - 1) < 1e-9]
for p, q in edges:
    ax.plot(*zip(p, q), color="0.75", lw=0.6)
for p, r in bonds:
    ax.plot(*zip(p, r), color="0.25", lw=1.6, zorder=1)
P1, P2 = np.array(s1), np.array(s2)
ax.scatter(*P1.T, s=55, color="#2171b5", edgecolor="k", linewidth=0.4, depthshade=False, zorder=3)
ax.scatter(*P2.T, s=55, color="#fd8d3c", edgecolor="k", linewidth=0.4, depthshade=False, zorder=3)
offs = [np.array([-0.10, 0, 0.02]), np.array([0.0, -0.08, 0.10]), np.array([0.03, 0.0, -0.10])]   # label offsets (display); a2 kept off the bond
for v, lab, off in zip([a1, a2, a3], [r"$\mathbf{a}_1$", r"$\mathbf{a}_2$", r"$\mathbf{a}_3$"], offs):
    u = v / A
    ax.quiver(0, 0, 0, *u, color="#cb181d", lw=1.4, arrow_length_ratio=0.12)
    ax.text(*(0.55 * u + off), lab, color="#cb181d", fontsize=10)
ax.text(0.25 + 0.04, 0.25, 0.25 - 0.09, r"$\boldsymbol{\tau}_2$", fontsize=9, color="#a63603")
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=18, azim=-62)
ax.set_axis_off()
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_zlim(0, 1)
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch03", "fig3_1.pdf")
fig.savefig(out, bbox_inches="tight", pad_inches=0.02)
print("wrote", os.path.normpath(out))
