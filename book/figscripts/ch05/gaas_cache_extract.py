"""Copies the small outputs of the GaAs DFPT runs into gaas_cache/ (so that the work directories can be deleted) and
extracts eps_inf, the Born charges (dF/dE, before the charge sum rule) and the Kohn-Sham gap into gaas_cache/epsZ.json.
Sources: /root/work/5.3 (tab5_1_gaas_qe.sh: 8^3 k, full 4^3 phonon grid) and /root/work/5.5 (fig5_4_epsk.sh: 12^3, 16^3 k,
Gamma field response only). The TO frequency at Gamma (wT_meV) is taken from GaAs.freq (matdyn, sum rule imposed) and
attached to every entry, since the k grid of the eps/Z* runs does not enter it.
Run: python gaas_cache_extract.py   (after both runs; idempotent)
"""
import json
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "gaas_cache")
W3, W5 = "/root/work/5.3", "/root/work/5.5"
CM = 0.123984198                 # meV per cm^-1
os.makedirs(C, exist_ok=True)
for fn in os.listdir(W3) if os.path.isdir(W3) else []:
    if fn.startswith("GaAs.") or fn in ("disp.out", "dos.out", "q2r.out", "scf.in", "ph.in", "disp.in", "dos.in", "q2r.in"):
        shutil.copy(os.path.join(W3, fn), C)
for fn in os.listdir(W5) if os.path.isdir(W5) else []:
    if re.match(r"(scf|eps)\d+\.(in|out)$", fn):
        shutil.copy(os.path.join(W5, fn), C)
if os.path.exists(os.path.join(W3, "ph.out")):
    shutil.copy(os.path.join(W3, "ph.out"), os.path.join(C, "ph8.out"))


def parse(phout, scfout=None):
    t = open(phout).read()
    blk = t.split("Dielectric constant in cartesian axis")[1]
    eps = float(re.search(r"\(\s*([-\d.]+)", blk).group(1))
    zb = t.split("Effective charges (d Force / dE) in cartesian axis without acoustic sum rule applied")[1]
    zs = [float(x) for x in re.findall(r"Mean Z\*:\s*([-\d.]+)", zb)[:2]]
    d = {"eps": eps, "Z_Ga": zs[0], "Z_As": zs[1]}
    if scfout and os.path.exists(scfout):
        m = re.search(r"highest occupied, lowest unoccupied level \(ev\):\s*([-\d.]+)\s+([-\d.]+)", open(scfout).read())
        if m:
            d["gap"] = float(m.group(2)) - float(m.group(1))
    return d


out = {}
if os.path.exists(os.path.join(C, "ph8.out")):
    out["8"] = parse(os.path.join(C, "ph8.out"))
for nk in (12, 16, 20, 24, 28):
    p = os.path.join(C, f"eps{nk}.out")
    if os.path.exists(p) and "Dielectric constant in cartesian" in open(p).read():
        out[str(nk)] = parse(p, os.path.join(C, f"scf{nk}.out"))
fq = os.path.join(C, "GaAs.freq")
if os.path.exists(fq):
    vals = open(fq).read().split("/", 1)[1].split()
    per = len(vals) // 4                  # four points; q columns (3 or 4, version dependent) then 6 frequencies
    wt = float(vals[per - 3]) * CM        # first point (0.001,0,0): modes sorted; fourth mode = TO
    for k in out:
        out[k]["wT_meV"] = wt
json.dump(out, open(os.path.join(C, "epsZ.json"), "w"), indent=1)
print(json.dumps(out, indent=1))
