"""Quantum ESPRESSO calculations behind Figs. 3.6, 3.7 and 3.8 (Sects. 3.3, 3.4): the book's representative
first-principles calculation (App. E.1) applied to silicon, germanium and GaAs.

Writes the small caches read by the plotting scripts (all < 1 MB):
  qe_si_pbe.npz    Si PBE: bands on L-G-X-W-K-G, fine G-X scan and transverse lines at the valley (masses),
                   E_min(q) along [100], [110], [111] from the full 48^3 grid
  qe_ge_gaas.npz   Ge PBE with spin-orbit coupling (and scalar-relativistic, for comparison), GaAs PBE: bands on the
                   same path, band edges, GaAs Gamma-valley curvature points, Ge 80 Ry check
  qe_si_lda.npz    Si LDA bands on L-G-X with the fine G-X scan, and the 80 Ry and 16^3 checks
Work files go to /root/work/F3/ only; every pw.x run goes through code/run-heavy.sh (one heavy job at a time).

Calculation (App. E.1, worked example we:E-si-bands, at the measured lattice constants):
  - Quantum ESPRESSO 7.6 (conda-forge build, /root/mamba/envs/qe), pw.x, plane waves, norm-conserving SG15 ONCV
    pseudopotentials (Hamann, PRB 88, 085117 (2013); Schlipf and Gygi, CPC 196, 36 (2015)):
      Si_ONCV_PBE-1.2.upf (4 valence e), Ge_ONCV_PBE-1.2.upf (14 e, 3d included), Ga_ONCV_PBE-1.2.upf (13 e),
      As_ONCV_PBE-1.2.upf (5 e); spin-orbit runs: Ge_ONCV_PBE_FR-1.0.upf (fully relativistic, 14 e);
  - functional PBE (LDA, input_dft = 'pz' = Slater exchange + Perdew-Zunger 1981 correlation, only for Fig. 3.8, on
    the same PBE-generated pseudopotential: a functional inconsistency, stated in the caption);
  - cutoff 60 Ry for the states, 240 Ry for the density; Gamma-centred 12^3 grid for the self-consistent density;
    fixed occupations (insulators); Ge with spin-orbit coupling is (PBE-)metallic and uses Marzari-Vanderbilt cold
    smearing of 0.002 Ry; conv_thr 1e-12 Ry;
  - lattice constants (room temperature, Sect. 3.3 / editor ruling): Si 5.431 A, Ge 5.658 A, GaAs 5.653 A; diamond /
    zincblende, ibrav = 2;
  - bands non-self-consistently at explicit k lists (cartesian, units 2pi/a).
  qe_si_tm.npz     Si LDA and PBE gaps with a Troullier-Martins pair generated in each functional (ld1.x), which
                   measures the pseudopotential-functional mismatch of the LDA run
Usage: python3 qe_ch03.py [si|ge|gaas|lda|tm|all]   (runs missing stages, then writes the caches)
"""
import os
import re
import sys
import shutil
import subprocess
import xml.etree.ElementTree as ET
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = "/root/work/F3"
RUN = "/home/user/dmdd-solid/code/run-heavy.sh"
PSEUDO_DIR = "/root/pseudo/sg15"
BOHR = 0.529177210903          # Angstrom (CODATA 2018)
HA = 27.211386245988           # eV
ECUT = 60
NK_SCF = 12
MASS = dict(Si=28.0855, Ge=72.630, Ga=69.723, As=74.9216)
MAT = {
    "Si": dict(a=5.431, sp=[("Si", "Si_ONCV_PBE-1.2.upf")], at=["Si", "Si"], nel=8),
    "Ge": dict(a=5.658, sp=[("Ge", "Ge_ONCV_PBE-1.2.upf")], at=["Ge", "Ge"], nel=28),
    "GeSO": dict(a=5.658, sp=[("Ge", "Ge_ONCV_PBE_FR-1.0.upf")], at=["Ge", "Ge"], nel=28),
    "GaAs": dict(a=5.653, sp=[("Ga", "Ga_ONCV_PBE-1.2.upf"), ("As", "As_ONCV_PBE-1.2.upf")], at=["Ga", "As"], nel=18),
}
# k path of Fig. 3.6(a) (cartesian, 2pi/a) and the epm.py reciprocal basis used for the E_min grid
PTS = [(0.5, 0.5, 0.5), (0, 0, 0), (1, 0, 0), (1, 0.5, 0), (0.75, 0.75, 0), (0, 0, 0)]
LABS = ["L", r"$\Gamma$", "X", "W", "K", r"$\Gamma$"]
B = np.array([[-1.0, 1, 1], [1, -1, 1], [1, 1, -1]])      # rows b_i in units of 2pi/a (as in epm.py)
NGRID = 48


def path(points, n=80):
    ks, xs, ticks, x0 = [], [], [0.0], 0.0
    for p, q in zip(points[:-1], points[1:]):
        p, q = np.array(p, float), np.array(q, float)
        t = np.linspace(0, 1, n)[:, None]
        ks.append(p + t * (q - p))
        L = np.linalg.norm(q - p)
        xs.append(x0 + t[:, 0] * L)
        x0 += L
        ticks.append(x0)
    return np.vstack(ks), np.concatenate(xs), ticks


def pw_input(mat, calc, prefix, kblock, nbnd=None, dft=None, ecut=ECUT, smear=False, conv="1.0d-12"):
    m = MAT[mat]
    sysx = f", nbnd = {nbnd}" if nbnd else ""
    if dft:
        sysx += f", input_dft = '{dft}'"
    if mat == "GeSO":
        sysx += ", noncolin = .true., lspinorb = .true."
    sysx += ", occupations = 'smearing', smearing = 'mv', degauss = 0.002" if smear else ", occupations = 'fixed'"
    sp = "".join(f"  {e} {MASS[e]} {f}\n" for e, f in m["sp"])
    return f"""&control
  calculation = '{calc}', prefix = '{prefix}', outdir = './tmp', pseudo_dir = '{PSEUDO_DIR}'
/
&system
  ibrav = 2, celldm(1) = {m['a'] / BOHR:.8f}, nat = 2, ntyp = {len(m['sp'])}, ecutwfc = {ecut}, ecutrho = {4 * ecut}{sysx}
/
&electrons
  conv_thr = {conv}, mixing_beta = 0.7, diago_full_acc = .true.
/
ATOMIC_SPECIES
{sp}ATOMIC_POSITIONS crystal
  {m['at'][0]} 0.00 0.00 0.00
  {m['at'][1]} 0.25 0.25 0.25
{kblock}"""


def kauto(n):
    return f"K_POINTS automatic\n  {n} {n} {n} 0 0 0\n"


def klist(k):
    k = np.asarray(k, float)
    return f"K_POINTS tpiba\n  {len(k)}\n" + "".join(f"  {a:.10f} {b:.10f} {c:.10f} 1\n" for a, b, c in k)


def run(wd, name, text):
    """Run pw.x (4 MPI ranks, 4 pools) through the heavy-job lock; keep a copy of the XML of this stage."""
    os.makedirs(wd, exist_ok=True)
    xml = os.path.join(wd, name + ".xml")
    if os.path.exists(xml):
        return xml
    open(os.path.join(wd, name + ".in"), "w").write(text)
    print("running", wd, name, flush=True)
    subprocess.run([RUN, f"F3-{os.path.basename(wd)}-{name}", "bash", "-c",
                    f"mpirun -np 4 pw.x -nk 4 -in {name}.in > {name}.out 2>&1"], cwd=wd, check=True)
    prefix = re.search(r"prefix = '(\w+)'", text).group(1)
    shutil.copy(os.path.join(wd, "tmp", prefix + ".save", "data-file-schema.xml"), xml)
    return xml


def read_xml(fn):
    r = ET.parse(fn).getroot()
    K, E = [], []
    for ks in r.iter("ks_energies"):
        K.append([float(x) for x in ks.find("k_point").text.split()])
        E.append([float(x) * HA for x in ks.find("eigenvalues").text.split()])
    ef = r.find(".//fermi_energy")
    ho = r.find(".//highestOccupiedLevel")
    return np.array(K), np.array(E), (float(ho.text) * HA if ho is not None else None), \
        (float(ef.text) * HA if ef is not None else None)


def oh_ops():
    import itertools
    ops = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3))
            for i in range(3):
                M[i, p[i]] = s[i]
            ops.append(M)
    return np.array(ops)


def grid_irr(N):
    """Full N^3 grid k = m.B/N (epm.py basis); representatives under O_h (48 operations, energies only)."""
    m = np.arange(N)
    M = np.stack(np.meshgrid(m, m, m, indexing="ij"), -1).reshape(-1, 3)
    K = M @ B / N
    Binv = np.linalg.inv(B)
    idx = lambda mm: (mm[..., 0] % N) * N * N + (mm[..., 1] % N) * N + (mm[..., 2] % N)
    best = np.arange(len(M))
    for R in oh_ops():
        mr = np.rint((K @ R.T) @ Binv * N).astype(int)
        best = np.minimum(best, idx(mr))
    rep, inv = np.unique(best, return_inverse=True)
    return K, rep, inv


def emin_curves(c5, v4, N, a):
    hbarc = 1973.269804       # eV A
    G1 = 2 * np.pi * hbarc / a
    dirs = {"[100]": ((0, 1, 1), 2.0), "[110]": ((1, 1, 2), 2 * np.sqrt(2)), "[111]": ((1, 1, 1), np.sqrt(3))}
    out = {}
    for name, (sh, L) in dirs.items():
        qs, es = [], []
        for j in range(N + 1):
            cs = np.roll(c5, shift=(-j * sh[0], -j * sh[1], -j * sh[2]), axis=(0, 1, 2))
            qs.append(L * j / N * G1)
            es.append(np.min(cs - v4))
        out[name] = (np.array(qs), np.array(es))
    return out


# ---------------------------------------------------------------------------------------------------- silicon PBE
def si():
    wd = os.path.join(WORK, "si")
    run(wd, "scf", pw_input("Si", "scf", "si", kauto(NK_SCF)))
    kp, xp, ticks = path(PTS)
    xb = run(wd, "bands", pw_input("Si", "bands", "si", klist(kp), nbnd=12))
    # fine Gamma-X scan (step 0.005) and transverse lines (step 0.005) through four points near the minimum
    s = np.round(np.arange(0.70, 1.0000001, 0.005), 6)
    line = np.column_stack([s, 0 * s, 0 * s])
    tr = np.array([(kx, j * 0.005, 0) for kx in (0.835, 0.840, 0.845, 0.850) for j in range(-4, 5)])
    xs = run(wd, "scan", pw_input("Si", "bands", "si", klist(np.vstack([line, tr])), nbnd=8))
    # E_min grid: irreducible O_h representatives of the 48^3 grid
    K, rep, inv = grid_irr(NGRID)
    xg = run(wd, "grid", pw_input("Si", "bands", "si", klist(K[rep]), nbnd=8))
    _, Eb, _, _ = read_xml(xb)
    _, Es, _, _ = read_xml(xs)
    Kg, Eg, _, _ = read_xml(xg)
    assert np.allclose(Kg, K[rep], atol=1e-6)
    E = Eg[inv]
    v4, c5 = E[:, 3].reshape((NGRID,) * 3), E[:, 4].reshape((NGRID,) * 3)
    cur = emin_curves(c5, v4, NGRID, MAT["Si"]["a"])
    np.savez(os.path.join(HERE, "qe_si_pbe.npz"), kp=kp, xp=xp, ticks=ticks, bands=Eb, scan_k=np.vstack([line, tr]),
             scan_e=Es, grid_v4_max=v4.max(), grid_c5_min=c5.min(), grid_edir=np.min(c5 - v4),
             **{f"q{k}": v[0] for k, v in cur.items()}, **{f"E{k}": v[1] for k, v in cur.items()},
             N=NGRID, nirr=len(rep), a=MAT["Si"]["a"])
    print("wrote qe_si_pbe.npz; irreducible grid points", len(rep))


# ------------------------------------------------------------------------------------------- germanium and GaAs
def ge_gaas():
    kp, xp, ticks = path(PTS)
    res = {}
    edge_k = np.array([(0, 0, 0), (0.5, 0.5, 0.5), (1, 0, 0)])
    for mat, nb, smear in (("GeSO", 40, True), ("Ge", 22, False), ("GaAs", 16, False)):
        wd = os.path.join(WORK, mat.lower())
        run(wd, "scf", pw_input(mat, "scf", mat.lower(), kauto(NK_SCF), nbnd=nb if smear else None, smear=smear))
        xb = run(wd, "bands", pw_input(mat, "bands", mat.lower(), klist(kp), nbnd=nb, smear=smear))
        s = np.round(np.arange(0.0, 1.0000001, 0.01), 6)
        extra = np.column_stack([s, 0 * s, 0 * s])
        if mat == "GaAs":   # Gamma-valley curvature: steps of 0.0025 (2pi/a) along [100] and [111]
            j = np.arange(-4, 5) * 0.0025
            extra = np.vstack([extra, np.column_stack([j, 0 * j, 0 * j]), np.column_stack([j, j, j]) / np.sqrt(3)])
        xs = run(wd, "scan", pw_input(mat, "bands", mat.lower(), klist(np.vstack([edge_k, extra])), nbnd=nb,
                                      smear=smear))
        _, Eb, _, _ = read_xml(xb)
        _, Es, ho, ef = read_xml(xs)
        res[mat] = dict(bands=Eb, scan=Es, scan_k=np.vstack([edge_k, extra]))
    # germanium with spin-orbit coupling at 80 Ry: band edges at Gamma, L, X
    wd = os.path.join(WORK, "geso80")
    run(wd, "scf", pw_input("GeSO", "scf", "geso", kauto(NK_SCF), nbnd=40, smear=True, ecut=80))
    _, E80, _, _ = read_xml(run(wd, "edges", pw_input("GeSO", "bands", "geso", klist(edge_k), nbnd=40, smear=True,
                                                       ecut=80)))
    np.savez(os.path.join(HERE, "qe_ge_gaas.npz"), kp=kp, xp=xp, ticks=ticks, geso80_edges=E80,
             **{f"{m}_{k}": v for m, d in res.items() for k, v in d.items()})
    print("wrote qe_ge_gaas.npz")


# ---------------------------------------------------------------------------------------------------- silicon LDA
def lda():
    pts = [(0.5, 0.5, 0.5), (0, 0, 0), (1, 0, 0)]
    kp, xp, ticks = path(pts, n=61)
    s = np.round(np.arange(0.70, 1.0000001, 0.005), 6)
    line = np.column_stack([s, 0 * s, 0 * s])
    chk_k = np.vstack([np.array([(0, 0, 0), (0.5, 0.5, 0.5), (1, 0, 0)]), line])
    out = {}
    for tag, ecut, nk in (("lda", 60, 12), ("lda80", 80, 12), ("lda16", 60, 16), ("pbe16", 60, 16)):
        wd = os.path.join(WORK, "si" + tag)
        dft = None if tag.startswith("pbe") else "pz"
        run(wd, "scf", pw_input("Si", "scf", "si", kauto(nk), dft=dft, ecut=ecut))
        out[tag + "_chk"] = read_xml(run(wd, "chk", pw_input("Si", "bands", "si", klist(chk_k), nbnd=8, dft=dft,
                                                             ecut=ecut)))[1]
        if tag == "lda":
            out["bands"] = read_xml(run(wd, "bands", pw_input("Si", "bands", "si", klist(kp), nbnd=8, dft=dft)))[1]
    np.savez(os.path.join(HERE, "qe_si_lda.npz"), kp=kp, xp=xp, ticks=ticks, chk_k=chk_k, **out)
    print("wrote qe_si_lda.npz")


# ------------------------------------------- pseudopotential-consistency check for the LDA of Fig. 3.8 (caption)
TM_IN = """&input
  title='Si', zed=14., config='[Ne] 3s2 3p2', iswitch=3, dft='{dft}', rel=1, beta=0.2, prefix='si_{tag}'
/
&inputp
  pseudotype=1, file_pseudopw='Si_tm_{tag}.UPF', author='book', lloc=-1, rcloc=2.40, tm=.true., nlcc=.false.
/
2
3S  1  0  2.00  0.00  2.40  2.40  0.0
3P  2  1  2.00  0.00  3.56  3.56  0.0
"""


def ppcheck():
    """LDA and PBE gaps of Si with a pair of Troullier-Martins potentials generated (ld1.x) in each functional with
    identical radii (those of the Fig. 3.9 potential): measures the error of running LDA on a PBE-generated potential."""
    wd0 = os.path.join(WORK, "tm")
    os.makedirs(wd0, exist_ok=True)
    out = {}
    chk_k = np.vstack([np.array([(0, 0, 0), (0.5, 0.5, 0.5), (1, 0, 0)]),
                       np.column_stack([np.round(np.arange(0.70, 1.0000001, 0.005), 6), np.zeros(61), np.zeros(61)])])
    for tag, dft in (("lda", "PZ"), ("pbe", "PBE")):
        if not os.path.exists(os.path.join(wd0, f"Si_tm_{tag}.UPF")):
            open(os.path.join(wd0, f"{tag}.in"), "w").write(TM_IN.format(dft=dft, tag=tag))
            subprocess.run(["bash", "-c", f"/root/mamba/envs/qe/bin/ld1.x < {tag}.in > {tag}.out"], cwd=wd0, check=True)
        wd = os.path.join(wd0, tag)
        for name, calc, kb, nb in (("scf", "scf", kauto(NK_SCF), None), ("chk", "bands", klist(chk_k), 8)):
            t = pw_input("Si", calc, "si", kb, nbnd=nb).replace(PSEUDO_DIR, wd0).replace(
                "Si_ONCV_PBE-1.2.upf", f"Si_tm_{tag}.UPF")
            x = run(wd, name, t)
        out["tm_" + tag] = read_xml(x)[1]
    np.savez(os.path.join(HERE, "qe_si_tm.npz"), chk_k=chk_k, **out)
    print("wrote qe_si_tm.npz")


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("si", "all"):
        si()
    if what in ("lda", "all"):
        lda()
    if what in ("ge", "gaas", "all"):
        ge_gaas()
    if what in ("tm", "all"):
        ppcheck()
