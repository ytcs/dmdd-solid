"""GaAs phonons at arbitrary wavevectors for Sect. 11.2 (Born-charge one-phonon weights, Limit 11.2a, Fig. 11.2, and the
check of Worked example 8.6 against full phonons).

Input: the interatomic force constants of Sect. 5.5, figscripts/ch05/gaas_cache/GaAs.fc (QE 7.6 DFPT, PBE, SG15 ONCV with
Ga 3d, 60 Ry, 8^3 k grid, 4^3 Q grid, a = 5.638 A; dipole term with the 28^3-grid eps_inf = 13.70 and Z* = 2.094 of the file
header, see gaas_q2r_epsZ.py). Natural masses Ga 69.723 u, As 74.9216 u (as fig5_4_matdyn.py).
matdyn.x (QE 7.6, /root/mamba/envs/qe/bin) interpolates the dynamical matrix to any q, adding the Ewald dipole term of
Gonze and Lee at each q (for q -> 0 along a direction, the nonanalytic term of eq:5.5-na). No new first-principles run.

Conventions (checked against the matdyn output below):
  * fleig gives the eigenvectors of the dynamical matrix, e_{kappa nu}(q), orthonormal, mass-weighted (not displacements).
  * QE uses the lattice-vector phase, D(q) = sum_R Phi(0k; R k') exp(-i q.R), the convention of eq:A.6-u. The density
    row n_kappa(q) = sum_R exp(i q.(R + tau_kappa + u)) then carries the site phase exp(i q.tau_kappa) explicitly.
  * Positions (file header, alat units): Ga (0,0,0), As (-1/4, 1/4, 1/4). The bond direction from Ga to the As of the
    same cell is [-1,1,1] in these axes; [111] of Worked example 8.6 (As at +a(1,1,1)/4) maps onto it by x -> -x.
Units: q in units of 2 pi/a (Cartesian), frequencies in meV.
"""
import os
import subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FC = os.path.join(HERE, "..", "ch05", "gaas_cache", "GaAs.fc")
WORK = os.path.join(HERE, "gaas11_2_work")
QE_BIN = "/root/mamba/envs/qe/bin"
CM_MEV = 0.1239841984          # meV per cm^-1
A_ANG = 5.638                  # lattice constant of the force-constant file (tab:E-functionals; WE 5.6)
M_GA, M_AS = 69.723, 74.9216   # u, natural masses (as fig5_4_matdyn.py)
TAU = np.array([[0.0, 0.0, 0.0], [-0.25, 0.25, 0.25]])   # alat units, from the GaAs.fc header


def run_matdyn(qs, tag):
    """Frequencies (meV, shape n x 6) and eigenvectors (n x 6 modes x 2 atoms x 3, complex) at Cartesian q (2pi/a).
    Results are cached in gaas11_2_work/<tag>.npz."""
    os.makedirs(WORK, exist_ok=True)
    cache = os.path.join(WORK, tag + ".npz")
    qs = np.atleast_2d(np.asarray(qs, float))
    if os.path.exists(cache):
        d = np.load(cache)
        if d["q"].shape == qs.shape and np.allclose(d["q"], qs):
            return d["w"], d["e"]
    if not os.path.exists(os.path.join(WORK, "GaAs.fc")):
        os.symlink(os.path.abspath(FC), os.path.join(WORK, "GaAs.fc"))
    inp = ["&input", f"  asr='crystal', flfrc='GaAs.fc', amass(1)={M_GA}, amass(2)={M_AS},",
           f"  flfrq='{tag}.freq', fleig='{tag}.eig', flvec='{tag}.vec', q_in_cryst_coord=.false.", "/", str(len(qs))]
    inp += ["%.10f %.10f %.10f" % tuple(q) for q in qs]
    env = dict(os.environ, PATH=QE_BIN + ":" + os.environ["PATH"])
    with open(os.path.join(WORK, tag + ".log"), "w") as fo:
        subprocess.run(["matdyn.x"], input="\n".join(inp) + "\n", text=True, stdout=fo, cwd=WORK, env=env, check=True)
    w, e = parse_eig(os.path.join(WORK, tag + ".eig"), len(qs))
    np.savez(cache, q=qs, w=w, e=e)
    for ext in (".freq", ".freq.gp", ".vec", ".eig"):
        p = os.path.join(WORK, tag + ext)
        if os.path.exists(p):
            os.remove(p)
    return w, e


def parse_eig(path, nq):
    lines = open(path).read().splitlines()
    w = np.zeros((nq, 6))
    e = np.zeros((nq, 6, 2, 3), complex)
    iq, nu, at = -1, -1, 0
    for ln in lines:
        s = ln.strip()
        if s.startswith("q ="):
            iq += 1
            nu = -1
        elif s.startswith("freq"):
            nu += 1
            at = 0
            w[iq, nu] = float(s.split("=")[2].split("[")[0]) * CM_MEV
        elif s.startswith("(") and nu >= 0:
            v = [float(x) for x in s.strip("()").split()]
            e[iq, nu, at] = np.array(v[0::2]) + 1j * np.array(v[1::2])
            at += 1
    assert iq == nq - 1
    return w, e


def born_weights(q, w, e, zstar=1.0):
    """Born-charge one-phonon weights |sum_kappa exp(i q.tau) qhat.Z*_kappa.e_{kappa nu}/sqrt(M_kappa)|^2 / (2 omega_nu),
    with Z*_Ga = -Z*_As = zstar (cubic sites), masses in u and omega in meV (arbitrary common units; used in ratios).
    Shape (n, 6)."""
    q = np.atleast_2d(q)
    qh = q / np.linalg.norm(q, axis=1)[:, None]
    ph = np.exp(2j * np.pi * q @ TAU.T)                       # (n, 2) site phases, q in 2pi/a and tau in a
    z = np.array([zstar, -zstar])
    m = np.array([M_GA, M_AS])
    amp = np.einsum("nk,nvkc,nc->nv", ph * z / np.sqrt(m), e.conj(), qh)
    return np.abs(amp) ** 2 / (2 * np.maximum(w, 1e-9))


def nucleon_amplitude(q, w, e, A=(69.723 * 1.001072, 74.9216 * 1.001046)):
    """Nucleon-number one-phonon amplitude per branch, sum_kappa A_kappa exp(i q.tau) qhat.e_{kappa nu}/sqrt(M_kappa)
    (mass numbers per atom: natural masses times the A/M of Worked example 8.6). Shape (n, 6), complex."""
    q = np.atleast_2d(q)
    qh = q / np.linalg.norm(q, axis=1)[:, None]
    ph = np.exp(2j * np.pi * q @ TAU.T)
    m = np.array([M_GA, M_AS])
    return np.einsum("nk,nvkc,nc->nv", ph * np.array(A) / np.sqrt(m), e.conj(), qh)


if __name__ == "__main__":
    w, e = run_matdyn([[0.001, 0, 0], [0, 0.001, 0.001], [0.001, 0.001, 0.001]], "gamma")
    print("Gamma along [100], [011], [111] (meV):")
    print(np.round(w, 3))
    print("SEAM 5.5: TO 34.22, LO 36.34 meV")
