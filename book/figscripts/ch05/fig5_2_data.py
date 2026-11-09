"""Parse the Quantum ESPRESSO outputs of fig5_2_qe.sh (work directory /root/work/5.2) into fig5_2_data.npz.
Si.freq: matdyn frequencies (cm^-1) at the wavevectors of fig5_2_qpath.py (Cartesian, units 2pi/a), same order.
Si.dos : matdyn density of states, columns omega (cm^-1), total DOS (states per cm^-1), normalized by matdyn to
         3 n_at = 6 modes per two-atom cell (renormalized to 6 in fig5_2.py after the unit change).
ph.out : the Gamma frequencies before the acoustic sum rule is imposed (ASR violation).
Run: python fig5_2_data.py   (numpy only)
"""
import os
import re
import numpy as np

W = "/root/work/5.2"
HERE = os.path.dirname(os.path.abspath(__file__))

txt = open(os.path.join(W, "Si.freq")).read()
nb, nk = map(int, re.search(r"nbnd=\s*(\d+), nks=\s*(\d+)", txt).groups())
vals = np.array(txt.split("/", 1)[1].split(), float).reshape(nk, 4 + nb)
q, f = vals[:, :3], vals[:, 4:]   # 4th column of the q line is the path coordinate
dos = np.loadtxt(os.path.join(W, "Si.dos"))[:, :2]
ph = open(os.path.join(W, "ph.out")).read()
g0 = re.search(r"freq \(\s*1\) =\s+(-?[0-9.]+) \[THz\]", ph)
np.savez(os.path.join(HERE, "fig5_2_data.npz"), q=q, f=f, dos=dos, asr_THz=float(g0.group(1)) if g0 else np.nan)
print(nk, "wavevectors,", nb, "branches; DOS rows", len(dos), "; Gamma acoustic before ASR (THz):", g0.group(1) if g0 else "?")
