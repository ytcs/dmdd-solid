"""Maximally localized sp3 Wannier functions of silicon for Figs. 3.11 and 3.12 (Sect. 3.6).

Runs Quantum ESPRESSO 7.6 (pw.x, pw2wannier90.x) and wannier90 (conda-forge build shipped with QE 7.6) and caches the
small outputs that the plotting scripts read: fig3_11_w90.npz (Wannier function on a plane and along a line, spreads)
and fig3_12_w90.npz (interpolated and direct bands). Work files go to /root/work/S36/ only.

Calculation (the choices are named in the captions of Figs. 3.11 and 3.12):
  - functional PBE; SG15 ONCV norm-conserving pseudopotential Si_ONCV_PBE-1.2.upf (scalar-relativistic, four valence
    electrons per atom); kinetic cutoff 40 Ry; no spin-orbit coupling;
  - lattice: diamond, a = 5.431 Angstrom (room-temperature value of Sect. 3.1), primitive vectors of eq:3.1-fcc,
    a1 = (a/2)(0,1,1), a2 = (a/2)(1,0,1), a3 = (a/2)(1,1,0); atoms at 0 and (a/4)(1,1,1);
  - self-consistent density on an unshifted 8x8x8 grid;
  - Wannier step: 16 Bloch bands on unshifted coarse grids of 4^3, 6^3 and 8^3 points; 8 Wannier functions started
    from sp3 projections on both atoms; disentanglement with an outer window [bottom, VBM + 12 eV] and a frozen
    (inner) window [bottom, VBM + 2.5 eV]; spread minimized to convergence. Three starting gauges (PROJ below): the
    default Si:sp3 (mixed: atom 1 toward its bonds, atom 2 away; ends in a symmetry-broken stationary point), A (both
    toward the bonds) and B (both away from the bonds, toward the empty tetrahedral sites). B has the smallest spread
    and is the one plotted (6^3 grid) and interpolated;
  - valence only: 4 bond-centred Wannier functions (s-type trial functions at the bond centres), no disentanglement,
    on the same grids (the isolated-group test of Fig. 3.12(b));
  - direct reference: pw.x band calculation (16 bands) at exactly the k points of the interpolated path.
Usage: python fig3_11_w90.py   (runs every missing stage, then writes the two .npz caches)
"""
import os
import re
import glob
import subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = "/root/work/S36"
RUN = "/home/user/dmdd-solid/book/tools/qe/run-heavy.sh"
PSEUDO_DIR = "/root/pseudo/sg15"
PSEUDO = "Si_ONCV_PBE-1.2.upf"
A = 5.431                      # Angstrom, Sect. 3.1 (room temperature, CODATA 2022)
ECUT = 40.0                    # Ry
NBND = 16
NWANN = 8
FROZ_ABOVE_VBM = 2.5           # eV
WIN_ABOVE_VBM = 12.0           # eV
GRIDS = (4, 6, 8)
NPLOT = 6                      # coarse grid whose Wannier function is plotted (Fig. 3.11)
NSEG = 40                      # wannier90 bands_num_points (points on the first path segment)

CELL = (A / 2) * np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], float)
TAU = np.array([[0, 0, 0], [A / 4, A / 4, A / 4]])
PATH = [("L", (0.5, 0.5, 0.5)), ("G", (0, 0, 0)), ("X", (1, 0, 0)), ("W", (1, 0.5, 0)),
        ("K", (0.75, 0.75, 0)), ("G", (0, 0, 0))]      # Cartesian, units of 2pi/a (path of Fig. 3.5)


def frac(kc):
    """Cartesian k (units of 2pi/a) -> fractional coordinates along b_i, using a_i.b_j = 2pi delta_ij."""
    return CELL @ np.asarray(kc, float) / A


def sh(label, cmd, cwd=WORK):
    print("running", label, ":", cmd, flush=True)
    subprocess.run([RUN, label, "bash", "-c", cmd], cwd=cwd, check=True)


def structure():
    s = "CELL_PARAMETERS angstrom\n" + "".join(f"  {v[0]:.10f} {v[1]:.10f} {v[2]:.10f}\n" for v in CELL)
    s += f"ATOMIC_SPECIES\n  Si 28.0855 {PSEUDO}\n"
    s += "ATOMIC_POSITIONS angstrom\n" + "".join(f"  Si {t[0]:.10f} {t[1]:.10f} {t[2]:.10f}\n" for t in TAU)
    return s


def pw_input(calc, kblock, nbnd=None, nosym=False):
    extra = f", nbnd = {nbnd}" if nbnd else ""
    extra += ", nosym = .true., noinv = .true." if nosym else ""
    return f"""&control
  calculation = '{calc}', prefix = 'si', outdir = './tmp', pseudo_dir = '{PSEUDO_DIR}', verbosity = 'high'
/
&system
  ibrav = 0, nat = 2, ntyp = 1, ecutwfc = {ECUT}{extra}
/
&electrons
  conv_thr = 1e-11, diago_full_acc = .true.
/
{structure()}{kblock}"""


def uniform(n):
    return [(i / n, j / n, k / n) for i in range(n) for j in range(n) for k in range(n)]


def kblock_list(ks, weights=True):
    s = f"K_POINTS crystal\n  {len(ks)}\n"
    w = 1.0 / len(ks)
    return s + "".join(f"  {k[0]:.12f} {k[1]:.12f} {k[2]:.12f} {w if weights else 1.0:.12e}\n" for k in ks)


def eigenvalues(outfile):
    """Band energies (eV) at each k point from a verbose pw.x output (nscf or bands)."""
    txt = open(outfile).read().split("End of band structure calculation")[-1]
    parts = re.split(r"k =[^\n]*bands \(ev\):", txt)[1:]
    rows = []
    for p in parts:
        body = re.split(r"occupation numbers|highest|Writing|the Fermi", p)[0]
        rows.append([float(x) for x in re.findall(r"-?\d+\.\d+", body)][:NBND])
    return np.array(rows)


def vbm_from_scf():
    m = re.search(r"highest occupied, lowest unoccupied level \(ev\):\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)",
                  open(os.path.join(WORK, "scf.out")).read())
    if m:
        return float(m.group(1))
    return float(re.search(r"highest occupied level \(ev\):\s+(-?\d+\.\d+)", open(os.path.join(WORK, "scf.out")).read()).group(1))


def win_input(n, vbm, plot):
    ks = uniform(n)
    path = ""
    for (l1, k1), (l2, k2) in zip(PATH[:-1], PATH[1:]):
        f1, f2 = frac(k1), frac(k2)
        path += f"{l1} {f1[0]:.6f} {f1[1]:.6f} {f1[2]:.6f}  {l2} {f2[0]:.6f} {f2[1]:.6f} {f2[2]:.6f}\n"
    s = f"""num_bands = {NBND}
num_wann = {NWANN}
dis_win_max = {vbm + WIN_ABOVE_VBM:.4f}
dis_froz_max = {vbm + FROZ_ABOVE_VBM:.4f}
dis_num_iter = 2000
dis_conv_tol = 1e-10
num_iter = 4000
conv_tol = 1e-12
conv_window = 5
guiding_centres = true
write_hr = true
write_xyz = true
use_ws_distance = true
translate_home_cell = false
bands_plot = true
bands_num_points = {NSEG}
"""
    if plot:
        s += "wannier_plot = true\nwannier_plot_format = cube\nwannier_plot_list = 1\nwannier_plot_supercell = 3\n"
    s += "begin kpoint_path\n" + path + "end kpoint_path\n"
    s += "begin unit_cell_cart\nang\n" + "".join(f"{v[0]:.10f} {v[1]:.10f} {v[2]:.10f}\n" for v in CELL)
    s += "end unit_cell_cart\nbegin atoms_cart\nang\n" + "".join(f"Si {t[0]:.10f} {t[1]:.10f} {t[2]:.10f}\n" for t in TAU)
    s += "end atoms_cart\nbegin projections\nSi:sp3\nend projections\n"
    s += f"mp_grid = {n} {n} {n}\nbegin kpoints\n" + "".join(f"{k[0]:.12f} {k[1]:.12f} {k[2]:.12f}\n" for k in ks)
    s += "end kpoints\n"
    return s


def parse_wout(wout):
    txt = open(wout).read()
    final = txt.split("Final State")[-1]
    spreads = [float(m) for m in re.findall(r"WF centre and spread\s+\d+\s+\([^)]*\)\s+(-?\d+\.\d+)", final)]
    centres = [[float(x) for x in m] for m in re.findall(
        r"WF centre and spread\s+\d+\s+\(\s*(-?\d+\.\d+),\s*(-?\d+\.\d+),\s*(-?\d+\.\d+)\s*\)", final)]
    oi = float(re.search(r"Omega I\s+=\s+(-?\d+\.\d+)", final).group(1))
    od = float(re.search(r"Omega D\s+=\s+(-?\d+\.\d+)", final).group(1))
    ood = float(re.search(r"Omega OD\s+=\s+(-?\d+\.\d+)", final).group(1))
    ot = float(re.search(r"Omega Total\s+=\s+(-?\d+\.\d+)", final).group(1))
    return dict(spreads=np.array(spreads), centres=np.array(centres), OmI=oi, OmD=od, OmOD=ood, OmT=ot)


PROJ = {
    # sp3 hybrids pointing along the four bonds of each atom ("A") or away from them, toward the empty tetrahedral
    # sites of the diamond structure ("B"). A 90-degree rotation about z (local x along y) turns one tetrahedron of
    # directions (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1) into the other. The default "Si:sp3" uses the first tetrahedron
    # on both atoms, which points along the bonds of atom 1 but away from those of atom 2 (a mixed start).
    "A": "f=0,0,0:sp3\nf=0.25,0.25,0.25:sp3:z=0,0,1:x=0,1,0\n",
    "B": "f=0,0,0:sp3:z=0,0,1:x=0,1,0\nf=0.25,0.25,0.25:sp3\n",
}
BOND_S = ("f=0.125,0.125,0.125:s\nf=0.125,0.125,-0.375:s\nf=0.125,-0.375,0.125:s\nf=-0.375,0.125,0.125:s\n")
SERIAL = "export PATH=/root/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1; "


def serial(cmd, cwd):
    """Single-core post-processing (wannier90.x, serial pw2wannier90.x): run directly, outside the 4-core lock."""
    print("serial:", cmd, "in", cwd, flush=True)
    subprocess.run(["bash", "-c", SERIAL + cmd], cwd=cwd, check=True)


def done(d):
    f = os.path.join(d, "si.wout")
    return os.path.exists(f) and "All done" in open(f).read()


def gauge_run(n, vbm, tag, proj, valence=False, plot=False):
    """Wannier run on the nscf states of w{n}: tag oA/oB (8 sp3 functions) or v (4 bond functions, valence only)."""
    d = os.path.join(WORK, f"{tag}{n}")
    os.makedirs(d, exist_ok=True)
    if not os.path.exists(os.path.join(d, "tmp")):
        os.symlink(os.path.join(WORK, f"w{n}", "tmp"), os.path.join(d, "tmp"))
    if done(d) and (not plot or glob.glob(os.path.join(d, "si_*00001.cube"))):
        return d
    win = win_input(n, vbm, plot)
    if valence:
        win = win.replace(f"num_bands = {NBND}", "num_bands = 4").replace(f"num_wann = {NWANN}", "num_wann = 4\nexclude_bands = 5-16")
        win = re.sub(r"dis_\w+ = [^\n]*\n", "", win)
    win = win.replace("begin projections\nSi:sp3\nend projections", "begin projections\n" + proj + "end projections")
    open(os.path.join(d, "si.win"), "w").write(win)
    reuse_mmn = not valence and os.path.exists(os.path.join(WORK, f"w{n}", "si.mmn"))
    if reuse_mmn:   # overlaps do not depend on the projections; only the amn (and UNK for plots) are recomputed
        for f in ("si.mmn", "si.eig"):
            subprocess.run(["cp", os.path.join(WORK, f"w{n}", f), d], check=True)
    open(os.path.join(d, "pw2wan.in"), "w").write(
        f"&inputpp\n  outdir = './tmp', prefix = 'si', seedname = 'si', write_mmn = {'.false.' if reuse_mmn else '.true.'},"
        f" write_amn = .true., write_unk = {'.true.' if plot else '.false.'}\n/\n")
    serial("wannier90.x -pp si && pw2wannier90.x -in pw2wan.in > pw2wan.out && wannier90.x si", d)
    return d


def main():
    os.makedirs(WORK, exist_ok=True)
    if not os.path.exists(os.path.join(WORK, "scf.out")):
        open(os.path.join(WORK, "scf.in"), "w").write(pw_input("scf", "K_POINTS automatic\n  8 8 8 0 0 0\n"))
        sh("S36-scf", "mpirun -np 4 pw.x -in scf.in > scf.out")
    vbm = vbm_from_scf()
    print("VBM (eV) =", vbm)
    for n in GRIDS:   # nscf states, overlaps, and the run started from the default (mixed) projections
        d = os.path.join(WORK, f"w{n}")
        os.makedirs(d, exist_ok=True)
        if not done(d):
            if not os.path.exists(os.path.join(d, "tmp")):
                subprocess.run(["cp", "-r", os.path.join(WORK, "tmp"), os.path.join(d, "tmp")], check=True)
            open(os.path.join(d, "nscf.in"), "w").write(pw_input("nscf", kblock_list(uniform(n)), NBND, True))
            open(os.path.join(d, "si.win"), "w").write(win_input(n, vbm, False))
            open(os.path.join(d, "pw2wan.in"), "w").write(
                "&inputpp\n  outdir = './tmp', prefix = 'si', seedname = 'si', write_mmn = .true., write_amn = .true.\n/\n")
            sh(f"S36-nscf{n}", "mpirun -np 4 pw.x -in nscf.in > nscf.out", d)
            sh(f"S36-w90pp{n}", "wannier90.x -pp si", d)
            sh(f"S36-pw2wan{n}", "mpirun -np 4 pw2wannier90.x -in pw2wan.in > pw2wan.out", d)
            sh(f"S36-w90{n}", "wannier90.x si", d)
    res = {}
    for n in GRIDS:
        res[("mixed", n)] = parse_wout(os.path.join(WORK, f"w{n}", "si.wout"))
        res[("B", n)] = parse_wout(os.path.join(gauge_run(n, vbm, "oB", PROJ["B"], plot=(n == NPLOT)), "si.wout"))
        res[("v", n)] = parse_wout(os.path.join(gauge_run(n, vbm, "v", BOND_S, valence=True), "si.wout"))
    res[("A", 6)] = parse_wout(os.path.join(gauge_run(6, vbm, "oA", PROJ["A"]), "si.wout"))
    for k, r in sorted(res.items(), key=str):
        print(k, "Omega_I, D, OD, total (A^2): %.4f %.4f %.4f %.4f" % (r["OmI"], r["OmD"], r["OmOD"], r["OmT"]),
              "spreads:", np.round(r["spreads"], 4))
    # direct bands at the k points of the interpolated path
    kpt = np.loadtxt(os.path.join(WORK, "w8", "si_band.kpt"), skiprows=1)[:, :3]
    if not os.path.exists(os.path.join(WORK, "bands.out")):
        open(os.path.join(WORK, "bands.in"), "w").write(pw_input("bands", kblock_list(kpt, weights=False), NBND))
        sh("S36-bands", "mpirun -np 4 pw.x -in bands.in > bands.out")
    direct = eigenvalues(os.path.join(WORK, "bands.out"))
    nk = len(kpt)
    out = {}
    for n in GRIDS:
        dat = np.loadtxt(os.path.join(WORK, f"oB{n}", "si_band.dat"))
        out[f"sp3_{n}"] = dat[:, 1].reshape(NWANN, nk).T
        dv = np.loadtxt(os.path.join(WORK, f"v{n}", "si_band.dat"))
        out[f"val_{n}"] = dv[:, 1].reshape(4, nk).T
        out[f"hrshell_{n}"] = hr_shells(os.path.join(WORK, f"v{n}", "si_hr.dat"))
    x = dat[:nk, 0]
    lab = open(os.path.join(WORK, "oB8", "si_band.labelinfo.dat")).read().split()
    labels = [lab[i] for i in range(0, len(lab), 6)]
    labx = [float(lab[i + 2]) for i in range(0, len(lab), 6)]
    spr = {f"{g}{n}_{q}": res[(g, n)][q] for (g, n) in res for q in ("OmI", "OmD", "OmOD", "OmT")}
    np.savez(os.path.join(HERE, "fig3_12_w90.npz"), vbm=vbm, kfrac=kpt, x=x, direct=direct, labels=np.array(labels),
             labx=np.array(labx), froz=vbm + FROZ_ABOVE_VBM, win=vbm + WIN_ABOVE_VBM, **out, **spr,
             **{f"spreads_{g}{n}": res[(g, n)]["spreads"] for (g, n) in res},
             **{f"centres_{g}{n}": res[(g, n)]["centres"] for (g, n) in res})
    cube = sorted(glob.glob(os.path.join(WORK, f"oB{NPLOT}", "si_*00001.cube")))
    print("cube file:", cube)
    slice_and_profile(cube[0], res[("B", NPLOT)])


def hr_shells(fn):
    """Largest |H^W_mn(R)| on each shell of |R| (Angstrom) from a wannier90 _hr.dat file."""
    with open(fn) as f:
        f.readline(); nw = int(f.readline()); nr = int(f.readline())
        deg = []
        while len(deg) < nr:
            deg += [int(v) for v in f.readline().split()]
        dat = np.loadtxt(f)
    R = dat[:, :3].reshape(nr, nw * nw, 3)[:, 0, :]
    H = np.abs(dat[:, 5] + 1j * dat[:, 6]).reshape(nr, nw * nw).max(1)
    dist = np.round(np.linalg.norm(R @ CELL, axis=1), 2)
    shells = sorted(set(dist))
    return np.array([[r, H[dist == r].max()] for r in shells])


BOHR = 0.529177210903          # Angstrom (CODATA)


def read_cube(fn):
    """Gaussian cube written by wannier90: returns origin (A), voxel vectors (A, rows), data[n1,n2,n3], atoms (A)."""
    with open(fn) as f:
        f.readline(); f.readline()
        nat, *o = f.readline().split()
        nat = int(nat)
        origin = np.array(o[:3], float) * BOHR
        n, vox = [], []
        for _ in range(3):
            parts = f.readline().split()
            n.append(int(parts[0]))
            vox.append(np.array(parts[1:4], float) * BOHR)
        atoms = np.array([f.readline().split()[2:5] for _ in range(abs(nat))], float) * BOHR
        data = np.array(f.read().split(), float).reshape(n)
    return origin, np.array(vox), data, atoms


def slice_and_profile(fn, w):
    from scipy.ndimage import map_coordinates
    origin, vox, data, atoms = read_cube(fn)
    dv = abs(np.linalg.det(vox))
    norm = np.sqrt((data**2).sum() * dv)            # normalize to 1 over the plotted supercell
    data = data / norm
    inv = np.linalg.inv(vox.T)
    centre = w["centres"][0]                         # Wannier centre of function 1 (Angstrom)
    # plane (110) through the atom at the origin, spanned by e1 = [-110]/sqrt2 and e2 = [001]; it contains the axis
    # [-111] of Wannier function 1 (gauge B) and the bond from that atom to its neighbour at (a/4)(1,-1,-1)
    e1 = np.array([-1, 1, 0]) / np.sqrt(2)
    e2 = np.array([0, 0, 1.0])
    # place the cell copy of the atom at 0 that is nearest the centre of the cube box
    boxc = origin + 0.5 * vox.T @ np.array(data.shape)
    shift = np.round(np.linalg.solve(CELL.T, boxc - centre))
    R0 = CELL.T @ shift
    c0 = centre + R0
    s = np.linspace(-4.5, 4.5, 241)
    S1, S2 = np.meshgrid(s, s, indexing="ij")
    # origin of the plane: the projection of the centre onto the plane through atom R0
    a0 = R0
    pc = a0 + e1 * np.dot(c0 - a0, e1) + e2 * np.dot(c0 - a0, e2)
    pts = pc[None, None, :] + S1[..., None] * e1 + S2[..., None] * e2
    idx = np.einsum("ij,abj->iab", inv, pts - origin)
    plane = map_coordinates(data, idx, order=3, mode="nearest")
    # atoms in the plane (within 0.05 A), in plane coordinates
    atl = []
    for sh in np.array(np.meshgrid(*[range(-4, 5)] * 3)).reshape(3, -1).T:
        for t in TAU:
            r = CELL.T @ sh + t + R0
            dvec = r - pc
            off = dvec - e1 * np.dot(dvec, e1) - e2 * np.dot(dvec, e2)
            if np.linalg.norm(off) < 0.05 and abs(np.dot(dvec, e1)) < 4.6 and abs(np.dot(dvec, e2)) < 4.6:
                atl.append((np.dot(dvec, e1), np.dot(dvec, e2)))
    # radial profile: largest |w| on shells around the centre, from the whole cube box
    g = np.indices(data.shape).reshape(3, -1).T
    rr = origin + g @ vox
    dist = np.linalg.norm(rr - c0, axis=1)
    edges = np.arange(0, 9.01, 0.25)
    wmax = np.array([np.abs(data.ravel()[(dist >= lo) & (dist < hi)]).max() if np.any((dist >= lo) & (dist < hi)) else np.nan
                     for lo, hi in zip(edges[:-1], edges[1:])])
    # the box edge: largest radius fully inside the cube box
    fr = np.linalg.solve(vox.T, (c0 - origin)) / np.array(data.shape)
    np.savez(os.path.join(HERE, "fig3_11_w90.npz"), s=s, plane=plane, atoms=np.array(atl),
             centre_plane=np.array([0.0, 0.0]), rmid=0.5 * (edges[1:] + edges[:-1]), wmax=wmax,
             spreads=w["spreads"], centres=w["centres"], OmI=w["OmI"], OmD=w["OmD"], OmOD=w["OmOD"], OmT=w["OmT"],
             frac_centre_in_box=fr, imag_note="real part as written by wannier90")
    print("normalization factor", norm, "plane max", np.abs(plane).max(), "atoms in plane", atl)


if __name__ == "__main__":
    main()
