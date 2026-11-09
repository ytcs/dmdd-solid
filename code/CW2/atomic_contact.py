"""CW2 [CALC] all-electron atomic densities with QE ld1.x (QE 7.6, conda-forge build, code/ENV.md).
Outputs per species/setting: contact density n_e(0) (bohr^-3) and the eκ factor r_k(q) = 1 + Δn_k(q)/n_e(0),
Δn_k(q) = 6 ∫ n(ρ) j2(qρ) dρ/ρ (WP2-v3 (5.2″), spherical density), total and per shell.
Run: python3 atomic_contact.py  (single core, < 10 s; work files in /root/work/CW2/ld1, results -> ld1/results.json)
Settings: rel=0 (non-relativistic, the campaign's NR Coulomb theory), rel=1 (scalar-relativistic, sensitivity only);
dft = PBE (campaign standard) and PZ (LDA, functional sensitivity); grid dx = 0.008 (default-like) and 0.006 with rmax = 60 (convergence; ld1 ndmx limit)."""
import json, os, subprocess, numpy as np
from scipy.special import spherical_jn
LD1 = "/root/mamba/envs/qe/bin/ld1.x"
W = "/root/work/CW2/ld1"; os.makedirs(W, exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = {"Si": (14, "[Ne] 3s2 3p2"), "Ge": (32, "[Ar] 3d10 4s2 4p2"),
        "Ga": (31, "[Ar] 3d10 4s2 4p1"), "As": (33, "[Ar] 3d10 4s2 4p3")}
KEV_PER_INV_BOHR = 3.7289  # 1/a0 = 3.7289 keV (hbar c / a0)
QS = [10.0, 30.0, 51.1, 102.0, 300.0]   # keV

def run(el, rel, dft, dx):
    Z, cfg = SPEC[el]; tag = f"{el}_r{rel}_{dft}_dx{dx}"
    inp = (f"&input\n title='{el}', zed={Z}., rel={rel}, config='{cfg}', iswitch=1, dft='{dft}',\n"
           f" dx={dx}, xmin=-7.0, rmax={100.0 if dx > 0.007 else 60.0}, prefix='{tag}', file_charge='{tag}.rho'\n/\n")
    open(f"{HERE}/ld1/{tag}.in", "w").write(inp)
    out = subprocess.run([LD1], input=inp, capture_output=True, text=True, cwd=W, env={**os.environ, "OMP_NUM_THREADS": "1"}).stdout
    open(f"{W}/{tag}.out", "w").write(out)
    d = np.loadtxt(f"{W}/{tag}.wfc", comments="#"); r = d[:, 0]
    hdr = open(f"{W}/{tag}.wfc").readline().split()[2:]   # orbital labels, columns r*R(r)
    occ = {"S": 2, "P": 6, "D": 10}
    occs = []
    for lab in hdr:   # occupations from config (valence partially filled)
        occs.append(occ[lab[-1]])
    # valence occupations from the config string
    for tok in cfg.split()[1:]:
        lab = tok[:2].upper(); n = int(tok[2:])
        if lab in hdr: occs[hdr.index(lab)] = n
    # total density from the .rho file (4*pi*r^2*n on the same log grid); the .wfc file lists at most 7 orbitals
    dr = np.loadtxt(f"{W}/{tag}.rho"); assert np.allclose(dr[:, 0], r)
    tot = dr[:, 1]/(4*np.pi*r**2)
    val = np.zeros_like(r)
    for j, lab in enumerate(hdr):
        if lab in valence(el):
            val += occs[j]*d[:, j+1]**2/(4*np.pi*r**2)
    n0 = tot[0]
    f = lambda n, q: 6*np.trapezoid(n*spherical_jn(2, q*r)/r, r)
    rq = {}
    for qk in QS:
        q = qk/KEV_PER_INV_BOHR
        rq[str(qk)] = {"total": 1 + f(tot, q)/n0, "core": 1 + f(tot - val, q)/n0}
    res = {}
    Nel = float(np.trapezoid(4*np.pi*r**2*tot, r))
    return {"tag": tag, "n0": float(n0), "n0_r3": float(tot[3]), "r0": float(r[0]), "Nel": Nel,
            "n0_val_frac": float(val[0]/n0), "rq": rq,
            "Etot_line": [l.strip() for l in out.splitlines() if "Etot" in l][:1]}

def valence(el):
    return {"Si": ["3S", "3P"], "Ge": ["4S", "4P"], "Ga": ["4S", "4P"], "As": ["4S", "4P"]}[el]

if __name__ == "__main__":
    allres = {}
    for el in SPEC:
        for rel, dft, dx in [(0, "PBE", 0.008), (0, "PBE", 0.006), (0, "PZ", 0.008), (1, "PBE", 0.008)]:
            R = run(el, rel, dft, dx); allres[R["tag"]] = R
            print(R["tag"], f"n0={R['n0']:.2f} Nel={R['Nel']:.4f}",
                  {k: round(v["total"], 4) for k, v in R["rq"].items()})
    json.dump(allres, open(f"{HERE}/ld1/results.json", "w"), indent=1)
