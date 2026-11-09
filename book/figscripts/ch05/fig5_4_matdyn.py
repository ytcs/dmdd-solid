"""Fig. 5.4 (Sect. 5.5): interpolated PBE phonon dispersion of GaAs along Gamma-X-K-Gamma-L, from the force constants of
tab5_1_gaas_qe.sh (QE 7.6 DFPT, PBE, SG15 ONCV Ga (3d in valence) and As, 60 Ry, 8^3 k grid, 4^3 Q grid, a = 5.638 A,
natural masses Ga 69.723 u, As 74.9216 u; q2r with zasr='crystal'), cached in gaas_cache/GaAs.fc.
Runs matdyn.x once (acoustic sum rule 'crystal' on force constants and Born charges; the dipole term is subtracted and
added back with the Born charges and eps_inf of the file header, in the Ewald form of Gonze and Lee as implemented in QE).
(A variant with the measured eps_inf patched into the header was tried and rejected: the Ewald dipole sum then no longer
matches the one subtracted by q2r, and it shifts even the zone-boundary frequencies, e.g. TA at X 10.45 -> 12.20 meV.
The measured-eps_inf LO at Gamma is instead computed exactly from eq:5.5-LOTO in fig5_4.py.)
Path (Cartesian, units 2pi/a): Delta Gamma(0,0,0)->X(0,0,1), 61 points; Sigma X'(1,1,0)->K(3/4,3/4,0)->Gamma, 81;
Lambda Gamma->L(1/2,1/2,1/2), 41 (as fig5_2_qpath.py, without the small-Q points). matdyn takes the direction of
approach at a Gamma point of the list from the neighboring point.
Output: gaas_cache/disp_comp.freq (frequencies in cm^-1).
Run: python fig5_4_matdyn.py   (needs matdyn.x of QE 7.6 on PATH: /root/mamba/envs/qe/bin)
"""
import os
import subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "gaas_cache")


def path():
    d = [np.array([0, 0, z]) for z in np.linspace(0, 1, 61)]
    s = [np.array([z, z, 0]) for z in np.linspace(1, 0, 81)]
    l = [np.array([z, z, z]) for z in np.linspace(0, 0.5, 41)]
    return d, s, l


def run(fc, out):
    d, s, l = path()
    pts = d + s + l
    inp = ["&input", f"  asr='crystal', flfrc='{fc}', amass(1)=69.723, amass(2)=74.9216,",
           f"  flfrq='{out}', q_in_cryst_coord=.false.", "/", str(len(pts))]
    inp += ["%.8f %.8f %.8f" % tuple(p) for p in pts]
    open(os.path.join(C, "path.in"), "w").write("\n".join(inp) + "\n")
    with open(os.path.join(C, "path.in")) as fi, open(os.path.join(C, out + ".log"), "w") as fo:
        subprocess.run(["matdyn.x"], stdin=fi, stdout=fo, cwd=C, check=True)
    for junk in ("matdyn.modes", "matdyn.vec", "matdyn.eig", "path.in", out + ".gp"):
        if os.path.exists(os.path.join(C, junk)):
            os.remove(os.path.join(C, junk))


if __name__ == "__main__":
    run("GaAs.fc", "disp_comp.freq")
    print("wrote", os.path.join(C, "disp_comp.freq"))
