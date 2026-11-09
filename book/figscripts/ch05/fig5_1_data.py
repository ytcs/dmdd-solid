"""Parse the Quantum ESPRESSO outputs of fig5_1_qe.sh (work directory /root/work/5.1) into fig5_1_data.npz.
Frozen zone-center optical displacement along [111]: atom 1 moves by -(u/2) n, atom 2 by +(u/2) n, n = (1,1,1)/sqrt(3),
so u is the change of the length of the bond along n. Energy per two-atom cell E(u); generalized force on the coordinate u,
F_u = (F_2 - F_1).n / 2, from the Hellmann-Feynman forces printed by pw.x. Hellmann-Feynman check: F_u = -dE/du.
Phonon DOS from matdyn (40^3 grid, Si.dos; columns: omega in cm^-1, total DOS per cm^-1 normalized to 6 modes).
Run: python fig5_1_data.py   (needs only numpy)
"""
import glob, os, re
import numpy as np

W = "/root/work/5.1"
HERE = os.path.dirname(os.path.abspath(__file__))
RY = 13.605693122994          # eV (CODATA 2018 Rydberg energy)
BOHR = 0.529177210903         # Angstrom (CODATA 2018)
n = np.ones(3) / np.sqrt(3.0)

us, Es, Fs = [], [], []
for f in glob.glob(os.path.join(W, "fp_*.out")):
    u = float(re.search(r"fp_(-?[0-9.]+)\.out", f).group(1))
    txt = open(f).read()
    E = float(re.findall(r"^!\s+total energy\s+=\s+(-?[0-9.]+) Ry", txt, re.M)[-1]) * RY
    fr = re.findall(r"atom\s+(\d) type  1   force =\s+(-?[0-9.]+)\s+(-?[0-9.]+)\s+(-?[0-9.]+)", txt)
    F = {int(a): np.array([float(x), float(y), float(z)]) * RY / BOHR for a, x, y, z in fr[:2]}
    us.append(u); Es.append(E); Fs.append((F[2] - F[1]) @ n / 2)
o = np.argsort(us)
u, E, Fu = np.array(us)[o], np.array(Es)[o], np.array(Fs)[o]
E = E - E[np.argmin(np.abs(u))]
dos = np.loadtxt(os.path.join(W, "Si.dos"))[:, :2] if os.path.exists(os.path.join(W, "Si.dos")) else None
np.savez(os.path.join(HERE, "fig5_1_data.npz"), u=u, E=E, Fu=Fu,
         dos=dos if dos is not None else np.zeros((0, 2)))
for a, b, c in zip(u, E, Fu):
    print(f"u = {a:+.2f} A   E = {b*1e3:9.3f} meV   F_u = {c:+.5f} eV/A")
