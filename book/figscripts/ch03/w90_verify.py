"""Independent check of the silicon Wannier results of Sect. 3.6 (Figs. 3.11, 3.12): which sp3 set is maximally
localized (bond-directed or anti-bond-directed hybrids), with what spread, and how fast the isolated valence group
interpolates. Writes w90_verify.json (a few kB) next to this script. Work files: /root/work/F3W/ (deleted afterwards).

Calculation: QE 7.6 pw.x + pw2wannier90.x, wannier90 3.x; PBE, SG15 Si_ONCV_PBE-1.2.upf, 60 Ry (240 Ry density),
a = 5.431 A, fcc vectors a1 = (a/2)(0,1,1), a2 = (a/2)(1,0,1), a3 = (a/2)(1,1,0), atoms at 0 and (a/4)(1,1,1) (so that
the default wannier90 sp3 tetrahedron (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1) points along the bonds of atom 1 and away
from those of atom 2); SCF on a Gamma-centred 12^3 grid; nscf on full unshifted n^3 grids (n = 4, 6, 8), 20 bands.
Wannier runs (8 functions, disentanglement): starting gauges
  A  sp3 along the bonds on both atoms        B  sp3 away from the bonds on both atoms
  M  default Si:sp3 on both atoms (mixed)     SP Si:s;p (no hybrid direction imposed)    R  random centres
windows: outer max VBM + 8, 12, 16 eV; frozen max VBM + 1.0 and + 2.5 eV; band count 16 (bands 17-20 excluded) or 20.
Valence: 4 functions, bands 1-4 only, s trial orbitals at the bond centres; errors against direct pw.x bands on the
wannier90 band path L-G-X-W-K-G (40 points on the first segment), and the largest |H^W(R)| per shell.
"""
import os
import re
import json
import shutil
import subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = "/root/work/F3W"
RUN = "/home/user/dmdd-solid/book/tools/qe/run-heavy.sh"
A = 5.431
ECUT = 60
NB = 20
CELL = (A / 2) * np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], float)
TAU = np.array([[0, 0, 0], [A / 4, A / 4, A / 4]])
PATH = [("L", (0.5, 0.5, 0.5)), ("G", (0, 0, 0)), ("X", (1, 0, 0)), ("W", (1, 0.5, 0)),
        ("K", (0.75, 0.75, 0)), ("G", (0, 0, 0))]
ENV = "export PATH=/root/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1; "
PROJ = {
    "A": "f=0,0,0:sp3\nf=0.25,0.25,0.25:sp3:z=0,0,1:x=0,1,0\n",
    "B": "f=0,0,0:sp3:z=0,0,1:x=0,1,0\nf=0.25,0.25,0.25:sp3\n",
    "M": "Si:sp3\n",
    "SP": "Si:s;p\n",
    "R": "random\n",
}
BOND_S = "f=0.125,0.125,0.125:s\nf=0.125,0.125,-0.375:s\nf=0.125,-0.375,0.125:s\nf=-0.375,0.125,0.125:s\n"


def frac(kc):
    return CELL @ np.asarray(kc, float) / A


def heavy(label, cmd, cwd):
    subprocess.run([RUN, label, "bash", "-c", cmd], cwd=cwd, check=True)


def serial(cmd, cwd):
    subprocess.run(["bash", "-c", ENV + cmd], cwd=cwd, check=True)


def struct():
    s = "CELL_PARAMETERS angstrom\n" + "".join(f"  {v[0]:.10f} {v[1]:.10f} {v[2]:.10f}\n" for v in CELL)
    s += "ATOMIC_SPECIES\n  Si 28.0855 Si_ONCV_PBE-1.2.upf\nATOMIC_POSITIONS angstrom\n"
    return s + "".join(f"  Si {t[0]:.10f} {t[1]:.10f} {t[2]:.10f}\n" for t in TAU)


def pw_in(calc, kb, nbnd=None, nosym=False):
    x = (f", nbnd = {nbnd}" if nbnd else "") + (", nosym = .true., noinv = .true." if nosym else "")
    return (f"&control\n  calculation = '{calc}', prefix = 'si', outdir = './tmp', pseudo_dir = '/root/pseudo/sg15',"
            f" verbosity = 'high'\n/\n&system\n  ibrav = 0, nat = 2, ntyp = 1, ecutwfc = {ECUT}, ecutrho = {4*ECUT}{x}\n/\n"
            f"&electrons\n  conv_thr = 1e-12, diago_full_acc = .true.\n/\n{struct()}{kb}")


def uniform(n):
    return [(i / n, j / n, k / n) for i in range(n) for j in range(n) for k in range(n)]


def klist(ks, w=True):
    return f"K_POINTS crystal\n  {len(ks)}\n" + "".join(
        f"  {k[0]:.12f} {k[1]:.12f} {k[2]:.12f} {1/len(ks) if w else 1.0:.12e}\n" for k in ks)


def win(n, vbm, proj, nw=8, nbands=NB, excl=None, outer=12.0, froz=2.5, valence=False):
    p = ""
    for (l1, k1), (l2, k2) in zip(PATH[:-1], PATH[1:]):
        f1, f2 = frac(k1), frac(k2)
        p += f"{l1} {f1[0]:.6f} {f1[1]:.6f} {f1[2]:.6f}  {l2} {f2[0]:.6f} {f2[1]:.6f} {f2[2]:.6f}\n"
    s = f"num_bands = {nbands}\nnum_wann = {nw}\n"
    if excl:
        s += f"exclude_bands = {excl}\n"
    if not valence:
        s += (f"dis_win_max = {vbm + outer:.4f}\ndis_froz_max = {vbm + froz:.4f}\ndis_num_iter = 5000\n"
              "dis_conv_tol = 1e-11\ndis_conv_window = 5\n")
    s += ("num_iter = 20000\nconv_tol = 1e-11\nconv_window = 5\nwrite_hr = true\nuse_ws_distance = true\n"
          "translate_home_cell = false\nbands_plot = true\nbands_num_points = 40\n")
    s += "begin kpoint_path\n" + p + "end kpoint_path\n"
    s += "begin unit_cell_cart\nang\n" + "".join(f"{v[0]:.10f} {v[1]:.10f} {v[2]:.10f}\n" for v in CELL)
    s += "end unit_cell_cart\nbegin atoms_cart\nang\n" + "".join(f"Si {t[0]:.10f} {t[1]:.10f} {t[2]:.10f}\n" for t in TAU)
    s += "end atoms_cart\nbegin projections\n" + proj + "end projections\n"
    s += f"mp_grid = {n} {n} {n}\nbegin kpoints\n" + "".join(f"{k[0]:.12f} {k[1]:.12f} {k[2]:.12f}\n" for k in uniform(n))
    return s + "end kpoints\n"


def parse_wout(fn):
    t = open(fn).read()
    f = t.split("Final State")[-1]
    sp = [float(x) for x in re.findall(r"WF centre and spread\s+\d+\s+\([^)]*\)\s+(-?\d+\.\d+)", f)]
    ce = [[float(y) for y in x] for x in re.findall(
        r"WF centre and spread\s+\d+\s+\(\s*(-?\d+\.\d+),\s*(-?\d+\.\d+),\s*(-?\d+\.\d+)\s*\)", f)]
    g = lambda k: float(re.search(k + r"\s+=\s+(-?\d+\.\d+)", f).group(1))
    conv = "All done" in t
    return dict(spreads=sp, centres=ce, OmI=g("Omega I"), OmD=g("Omega D"), OmOD=g("Omega OD"),
                OmT=g("Omega Total"), done=conv)


def orient(centres):
    """For each centre: distance from its atom and cosine with the nearest bond direction of that atom."""
    out = []
    bonds1 = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / np.sqrt(3)
    for c in np.array(centres):
        best = None
        for sh in np.array(np.meshgrid(*[range(-2, 3)] * 3)).reshape(3, -1).T:
            for ia, t in enumerate(TAU):
                r = c - (CELL.T @ sh + t)
                if best is None or np.linalg.norm(r) < np.linalg.norm(best[1]):
                    best = (ia, r)
        ia, r = best
        b = bonds1 if ia == 0 else -bonds1
        cos = float(np.max(b @ r / np.linalg.norm(r))) if np.linalg.norm(r) > 1e-3 else 0.0
        out.append((ia, float(np.linalg.norm(r)), cos))
    return out


def hr_shells(fn):
    with open(fn) as f:
        f.readline(); nw = int(f.readline()); nr = int(f.readline())
        deg = []
        while len(deg) < nr:
            deg += [int(v) for v in f.readline().split()]
        dat = np.loadtxt(f)
    R = dat[:, :3].reshape(nr, nw * nw, 3)[:, 0, :]
    H = (np.abs(dat[:, 5] + 1j * dat[:, 6]).reshape(nr, nw * nw) / np.array(deg)[:, None]).max(1)
    d = np.round(np.linalg.norm(R @ CELL, axis=1), 2)
    return [[float(r), float(H[d == r].max())] for r in sorted(set(d))]


def main():
    os.makedirs(WORK, exist_ok=True)
    if not os.path.exists(os.path.join(WORK, "scf.out")):
        open(os.path.join(WORK, "scf.in"), "w").write(pw_in("scf", "K_POINTS automatic\n  12 12 12 0 0 0\n"))
        heavy("F3W-scf", "mpirun -np 4 pw.x -nk 4 -in scf.in > scf.out", WORK)
    vbm = float(re.search(r"highest occupied(?:, lowest unoccupied)? level \(ev\):\s+(-?\d+\.\d+)",
                          open(os.path.join(WORK, "scf.out")).read()).group(1))
    res = {"vbm": vbm}
    for n in (4, 6, 8):
        d = os.path.join(WORK, f"n{n}")
        os.makedirs(d, exist_ok=True)
        if not os.path.exists(os.path.join(d, "si.mmn")):
            if not os.path.exists(os.path.join(d, "tmp")):
                shutil.copytree(os.path.join(WORK, "tmp"), os.path.join(d, "tmp"))
            open(os.path.join(d, "nscf.in"), "w").write(pw_in("nscf", klist(uniform(n)), NB, True))
            open(os.path.join(d, "si.win"), "w").write(win(n, vbm, PROJ["M"]))
            open(os.path.join(d, "pw2wan.in"), "w").write(
                "&inputpp\n  outdir = './tmp', prefix = 'si', seedname = 'si', write_mmn = .true., write_amn = .false.\n/\n")
            heavy(f"F3W-nscf{n}", "mpirun -np 4 pw.x -nk 4 -in nscf.in > nscf.out", d)
            serial("wannier90.x -pp si", d)
            heavy(f"F3W-pw2wan{n}", "mpirun -np 4 pw2wannier90.x -in pw2wan.in > pw2wan.out", d)

    def wrun(n, tag, text, nwann_proj_needs_amn=True):
        d = os.path.join(WORK, f"n{n}", tag)
        if os.path.exists(os.path.join(d, "si.wout")) and "All done" in open(os.path.join(d, "si.wout")).read():
            return d
        os.makedirs(d, exist_ok=True)
        if not os.path.exists(os.path.join(d, "tmp")):
            os.symlink(os.path.join(WORK, f"n{n}", "tmp"), os.path.join(d, "tmp"))
        open(os.path.join(d, "si.win"), "w").write(text)
        excl = "exclude_bands" in text
        for f in ("si.mmn", "si.eig"):
            if not excl:
                shutil.copy(os.path.join(WORK, f"n{n}", f), d)
        open(os.path.join(d, "pw2wan.in"), "w").write(
            f"&inputpp\n  outdir = './tmp', prefix = 'si', seedname = 'si', write_mmn = {'.true.' if excl else '.false.'},"
            " write_amn = .true.\n/\n")
        serial("wannier90.x -pp si && pw2wannier90.x -in pw2wan.in > pw2wan.out && wannier90.x si", d)
        return d

    runs = []
    for n in (6, 8):
        for g in ("A", "B", "M", "SP", "R"):
            runs.append((n, f"{g}_o12_f2.5", dict(proj=PROJ[g], outer=12.0, froz=2.5)))
        for g in ("A", "B"):
            runs.append((n, f"{g}_o12_f1.0", dict(proj=PROJ[g], outer=12.0, froz=1.0)))
            runs.append((n, f"{g}_o14_f2.5", dict(proj=PROJ[g], outer=14.0, froz=2.5)))
            runs.append((n, f"{g}_o16_f2.5", dict(proj=PROJ[g], outer=16.0, froz=2.5)))
            runs.append((n, f"{g}_o12_f2.5_nb16", dict(proj=PROJ[g], outer=12.0, froz=2.5, nbands=16, excl="17-20")))
    for n, tag, kw in runs:
        try:
            d = wrun(n, tag, win(n, vbm, **kw))
        except subprocess.CalledProcessError:
            print(n, tag, "wannier90 refused (window)", flush=True)
            continue
        if "All done" not in open(os.path.join(d, "si.wout")).read():
            print(n, tag, "wannier90 refused (window)", flush=True)
            continue
        r = parse_wout(os.path.join(d, "si.wout"))
        r["orient"] = orient(r["centres"])
        res[f"n{n}_{tag}"] = r
        print(n, tag, "Omega I/D/OD/T = %.4f %.4f %.4f %.4f" % (r["OmI"], r["OmD"], r["OmOD"], r["OmT"]),
              "spreads", np.round(r["spreads"], 3), "cos", [round(o[2], 2) for o in r["orient"]], flush=True)
    # valence-only (isolated group): bond-centred s, bands 1-4
    for n in (4, 6, 8):
        d = wrun(n, "val", win(n, vbm, BOND_S, nw=4, nbands=4, excl="5-20", valence=True))
        r = parse_wout(os.path.join(d, "si.wout"))
        r["hr_shells"] = hr_shells(os.path.join(d, "si_hr.dat"))
        res[f"n{n}_val"] = r
    # direct bands on the wannier90 path
    kpt = np.loadtxt(os.path.join(WORK, "n8", "val", "si_band.kpt"), skiprows=1)[:, :3]
    bd = os.path.join(WORK, "bands")
    os.makedirs(bd, exist_ok=True)
    if not os.path.exists(os.path.join(bd, "bands.out")):
        if not os.path.exists(os.path.join(bd, "tmp")):
            shutil.copytree(os.path.join(WORK, "tmp"), os.path.join(bd, "tmp"))
        open(os.path.join(bd, "bands.in"), "w").write(pw_in("bands", klist(kpt, w=False), 12))
        heavy("F3W-bands", "mpirun -np 4 pw.x -nk 4 -in bands.in > bands.out", bd)
    import xml.etree.ElementTree as ET
    root = ET.parse(os.path.join(bd, "tmp", "si.save", "data-file-schema.xml")).getroot()
    direct = np.array([[float(x) * 27.211386245988 for x in ks.find("eigenvalues").text.split()]
                       for ks in root.iter("ks_energies")])
    nk = len(kpt)
    for n in (4, 6, 8):
        dv = np.loadtxt(os.path.join(WORK, f"n{n}", "val", "si_band.dat"))[:, 1].reshape(4, nk).T
        err = np.abs(dv - direct[:, :4])
        res[f"n{n}_val"]["maxerr_meV"] = float(err.max() * 1e3)
        res[f"n{n}_val"]["maxerr_k"] = kpt[int(np.argmax(err.max(1)))].tolist()
        res[f"n{n}_val"]["rmserr_meV"] = float(np.sqrt((err ** 2).mean()) * 1e3)
        for tag in ("B_o12_f2.5", "A_o12_f2.5"):
            if n in (6, 8):
                dw = np.loadtxt(os.path.join(WORK, f"n{n}", tag, "si_band.dat"))[:, 1].reshape(8, nk).T
                ev = np.abs(dw[:, :4] - direct[:, :4]).max()
                m = (direct[:, 4:8] - vbm) < 1.5           # every conduction band below VBM + 1.5 eV
                ec = np.abs(dw[:, 4:8] - direct[:, 4:8])[m].max()
                res[f"n{n}_{tag}"]["err_val_meV"] = float(ev * 1e3)
                res[f"n{n}_{tag}"]["err_cb1.5_meV"] = float(ec * 1e3)
        print(n, "valence maxerr %.1f meV rms %.1f" % (res[f"n{n}_val"]["maxerr_meV"], res[f"n{n}_val"]["rmserr_meV"]),
              "Omega", res[f"n{n}_val"]["OmT"], flush=True)
    json.dump(res, open(os.path.join(HERE, "w90_verify.json"), "w"), indent=1)
    print("wrote w90_verify.json")


if __name__ == "__main__":
    main()
