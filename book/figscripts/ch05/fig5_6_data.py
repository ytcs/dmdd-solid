"""Extract the silicon force constants of Sect. 5.2 into fig5_6_fc.npz, for the decay kinematics of Sect. 5.7 (Fig. 5.6, WE 5.9).
Source: Si.fc in /root/work/5.2, written by q2r.x from the DFPT run of fig5_2_qe.sh (Quantum ESPRESSO 7.6, PBE, SG15 ONCV
Si_ONCV_PBE-1.2.upf, 60 Ry, Gamma-centered 12^3 k grid, a = 5.431 A, 6^3 Q grid). No new electronic-structure run.
q2r writes the constants without the acoustic sum rule; fig5_6.py imposes it by the on-site correction of Eq. (5.4-asrfix).
Units in the file: Rydberg atomic units (force constants Ry/bohr^2, mass in units of m_e/2, lengths in bohr / alat).
Run: python fig5_6_data.py   (numpy only)
"""
import os
import numpy as np

W = "/root/work/5.2"
HERE = os.path.dirname(os.path.abspath(__file__))

lines = open(os.path.join(W, "Si.fc")).read().splitlines()
ntyp, nat, ibrav = map(int, lines[0].split()[:3])
celldm1 = float(lines[0].split()[3])
amass = float(lines[1].split()[-1])                   # Ry units (amu * 911.444)
tau = np.array([list(map(float, lines[2 + i].split()[2:5])) for i in range(nat)])   # alat units
i = 2 + nat
has_zeu = lines[i].split()[0] == "T"
i += 1
if has_zeu:
    i += 3 + nat * 4                                   # epsilon (3 lines) + nat x (index + 3 lines)
nr = tuple(map(int, lines[i].split()))
i += 1
phi = np.zeros((3, 3, nat, nat) + nr)
nblock = nr[0] * nr[1] * nr[2]
for _ in range(9 * nat * nat):
    a, b, na, nb = map(int, lines[i].split())
    i += 1
    for k in range(nblock):
        m1, m2, m3, v = lines[i + k].split()
        phi[a - 1, b - 1, na - 1, nb - 1, int(m1) - 1, int(m2) - 1, int(m3) - 1] = float(v)
    i += nblock
np.savez(os.path.join(HERE, "fig5_6_fc.npz"), phi=phi, tau=tau, amass=amass, celldm1=celldm1, nr=np.array(nr))
print("ibrav", ibrav, "nat", nat, "grid", nr, "alat (bohr)", celldm1, "mass (Ry units)", amass, "zeu", has_zeu)
