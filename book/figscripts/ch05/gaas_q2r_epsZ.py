"""GaAs force constants with a converged dielectric tensor and Born charges (Sect. 5.5, Fig. 5.4, Table 5.1).
The phonon run of tab5_1_gaas_qe.sh used an 8^3 k grid. That grid is enough for the analytic force constants but not for
eps_inf and Z* of PBE GaAs, whose Kohn-Sham gap at a = 5.638 A is only 0.57 eV (fig5_4_epsk.sh: eps_inf = 26.0, 16.8,
14.7, ... on 8^3, 12^3, 16^3, ... grids). This script replaces the dielectric tensor and the Born charges in the Gamma
dynamical matrix (GaAs.dyn1, blocks 'Dielectric Tensor', 'Effective Charges E-U' and 'U-E') by the values of the densest
k grid in gaas_cache/epsZ.json (charges as computed, before the sum rule; q2r imposes zasr='crystal'), and reruns
  q2r.x (zasr='crystal')  -> GaAs.fc   (dipole part subtracted with the new eps_inf and Z*, so that subtraction and
                                         re-addition in matdyn are consistent)
  matdyn.x                -> GaAs.freq (Gamma[100], X, L, Gamma[001]; as tab5_1_gaas_qe.sh)
  matdyn.x                -> GaAs.dos  (32^3 grid, tetrahedra, 0.25 cm^-1; total and atom-projected)
in a scratch directory, and copies the results into gaas_cache/ (the 8^3-eps versions are kept as *.k8).
The original GaAs.dyn1 is kept as gaas_cache/GaAs.dyn1.k8 and is never modified.
Run: python gaas_q2r_epsZ.py   (needs q2r.x, matdyn.x of QE 7.6 on PATH: /root/mamba/envs/qe/bin)
"""
import json
import os
import shutil
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "gaas_cache")
W = "/root/work/5.5/q2r"
os.makedirs(W, exist_ok=True)
d = json.load(open(os.path.join(C, "epsZ.json")))
nk = max(d, key=int)
eps, zga, zas = d[nk]["eps"], d[nk]["Z_Ga"], d[nk]["Z_As"]
print(f"using k {nk}^3: eps_inf = {eps:.4f}, Z_Ga = {zga:.5f}, Z_As = {zas:.5f}")
for k in ("GaAs.fc", "GaAs.freq", "GaAs.dos", "GaAs.dyn1"):
    if not os.path.exists(os.path.join(C, k + ".k8")):
        shutil.copy(os.path.join(C, k), os.path.join(C, k + ".k8"))
for i in range(9):
    shutil.copy(os.path.join(C, f"GaAs.dyn{i}"), W)
shutil.copy(os.path.join(C, "GaAs.dyn1.k8"), os.path.join(W, "GaAs.dyn1"))


def diag(v, fmt):
    return [fmt % (v, 0.0, 0.0), fmt % (0.0, v, 0.0), fmt % (0.0, 0.0, v)]


L = open(os.path.join(W, "GaAs.dyn1")).read().splitlines()
i = next(k for k, s in enumerate(L) if "Dielectric Tensor:" in s)
L[i + 2:i + 5] = diag(eps, "%24.12f%24.12f%24.12f")
for tag, fmt in (("Effective Charges E-U", "%24.12f%24.12f%24.12f"), ("Effective Charges U-E", "%20.12E%20.12E%20.12E")):
    j = next(k for k, s in enumerate(L) if tag in s)
    a1 = next(k for k in range(j, j + 5) if "atom #    1" in L[k])
    L[a1 + 1:a1 + 4] = diag(zga, fmt)
    a2 = next(k for k in range(a1, a1 + 8) if "atom #    2" in L[k])
    L[a2 + 1:a2 + 4] = diag(zas, fmt)
open(os.path.join(W, "GaAs.dyn1"), "w").write("\n".join(L) + "\n")


def run(exe, text, log):
    open(os.path.join(W, log + ".in"), "w").write(text)
    with open(os.path.join(W, log + ".in")) as fi, open(os.path.join(W, log + ".out"), "w") as fo:
        subprocess.run([exe], stdin=fi, stdout=fo, cwd=W, check=True)


run("q2r.x", "&input\n  fildyn='GaAs.dyn', zasr='crystal', flfrc='GaAs.fc'\n/\n", "q2r")
M = "amass(1)=69.723, amass(2)=74.9216"
run("matdyn.x", f"&input\n  asr='crystal', flfrc='GaAs.fc', {M}, flfrq='GaAs.freq', q_in_cryst_coord=.false.\n/\n4\n"
    "0.001 0.0 0.0\n1.0 0.0 0.0\n0.5 0.5 0.5\n0.0 0.0 0.001\n", "disp")
run("matdyn.x", f"&input\n  asr='crystal', flfrc='GaAs.fc', {M}, dos=.true., fldos='GaAs.dos',\n"
    "  nk1=32, nk2=32, nk3=32, deltaE=0.25\n/\n", "dos")
for f in ("GaAs.fc", "GaAs.freq", "GaAs.dos"):
    shutil.copy(os.path.join(W, f), C)
print(open(os.path.join(C, "GaAs.freq")).read())
