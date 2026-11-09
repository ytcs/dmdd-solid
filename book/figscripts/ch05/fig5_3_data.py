"""Parse the Quantum ESPRESSO outputs of fig5_3_qe.sh (work directory /root/work/5.4) into fig5_3_data.npz.
Contents:
  f2, f3, f6   : matdyn frequencies (cm^-1) on the points of fig5_3_qpath.py from force constants of the 2^3, 3^3, 6^3 grids,
                 acoustic sum rule imposed (asr='crystal');
  f6no         : the same from the 6^3 grid with asr='no';
  qoff, foff   : the three off-grid points (2pi/a) and the frequencies of direct ph.x runs there (cm^-1);
  dist, phinorm: for the 6^3 force constants (q2r file Si.fc, units Ry/bohr^2), the distance |R + tau_k1 - tau_k2| (Angstrom; matdyn convention r_ws = R + tau(na) - tau(nb))
                 of each pair (k, k', R), with R folded to its shortest image modulo the 6^3 supercell (minimum image over
                 supercell translations 6 a_i, i.e. the Wigner-Seitz choice), and the Frobenius norm of the 3x3 block
                 Phi^{ab}_{kk'}(0,R) converted to eV/Angstrom^2 (1 Ry/bohr^2 = 13.6057/0.52918^2 eV/A^2).
Run: python fig5_3_data.py   (numpy only)
"""
import os, re, itertools
import numpy as np

W = "/root/work/5.4"
HERE = os.path.dirname(os.path.abspath(__file__))
RY, BOHR = 13.605693122994, 0.529177210903
A = 5.431
a = np.array([[-1, 0, 1], [0, 1, 1], [-1, 1, 0]]) * A / 2       # QE ibrav=2 primitive vectors (Angstrom)
tau = np.array([[0, 0, 0], [0.25, 0.25, 0.25]]) * A


def gp(path):
    return np.loadtxt(path)[:, 1:]


def offgrid():
    fs = []
    for i in (1, 2, 3):
        txt = open(os.path.join(W, f"off{i}.dyn")).read()
        fs.append([float(x) for x in re.findall(r"freq \(\s*\d+\) =\s+-?[0-9.]+ \[THz\] =\s+(-?[0-9.]+) \[cm-1\]", txt)])
    return np.array(fs)


def ifc(path):
    L = open(path).read().split("\n")
    i = 0
    while not L[i].strip().split()[0] in ("T", "F"):
        i += 1
    # skip epsilon (3 lines) and, per atom, an index line + 3 lines of Z*: the grid line is the first with three integers
    while len(L[i].split()) != 3 or not all(t.lstrip("-").isdigit() for t in L[i].split()):
        i += 1
    n1, n2, n3 = map(int, L[i].split()); i += 1
    blocks = {}
    while i < len(L) and L[i].strip():
        al, be, k1, k2 = map(int, L[i].split()); i += 1
        for _ in range(n1 * n2 * n3):
            m1, m2, m3, v = L[i].split(); i += 1
            blocks.setdefault((k1, k2, int(m1), int(m2), int(m3)), np.zeros((3, 3)))[al - 1, be - 1] = float(v)
    return (n1, n2, n3), blocks


(n1, n2, n3), B = ifc(os.path.join(W, "g6", "Si.fc"))
dist, norm = [], []
for (k1, k2, m1, m2, m3), blk in B.items():
    base = (m1 - 1) * a[0] + (m2 - 1) * a[1] + (m3 - 1) * a[2] + tau[k1 - 1] - tau[k2 - 1]
    d = min(np.linalg.norm(base + i * n1 * a[0] + j * n2 * a[1] + k * n3 * a[2])
            for i, j, k in itertools.product((-1, 0, 1), repeat=3))
    dist.append(d); norm.append(np.linalg.norm(blk) * RY / BOHR ** 2)
dist, norm = np.array(dist), np.array(norm)
np.savez(os.path.join(HERE, "fig5_3_data.npz"), f2=gp(f"{W}/g2/freq_crystal.gp"), f3=gp(f"{W}/g3/freq_crystal.gp"),
         f6=gp(f"{W}/g6/freq_crystal.gp"), f6no=gp(f"{W}/g6/freq_no.gp"),
         qoff=np.array([[0, 0, 0.5], [0.5, 0.5, 0], [0.25, 0.25, 0.25]]), foff=offgrid(), dist=dist, phinorm=norm)
print("pairs:", len(dist), " on-site norm (eV/A^2):", norm[dist < 1e-6])
