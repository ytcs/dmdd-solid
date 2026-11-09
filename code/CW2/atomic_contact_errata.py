"""R16 ERR-CW2 [CALC]: r_min and relativity sensitivity of the ld1.x all-electron contact densities (QE 7.6 ld1.x, as atomic_contact.py).
For each species: rel = 0 (NR), 1 (scalar-relativistic), 2 (Dirac, spin-orbit) x xmin = -7, -8 (first grid point r_min = e^xmin/Z), dx = 0.008, PBE.
Outputs per run: n(r_min) [bohr^-3], the log slope d ln n / d ln r over the first 4 grid points, N_el, and the numerator
Delta n(q) = 6 int n(rho) j2(q rho) drho/rho of the e-kappa factor (WP2-v3 (5.2'')), which does not depend on n(0).
Run: python3 atomic_contact_errata.py  (single core, < 30 s; work files in $CW2_WORK or a temporary directory; results -> ld1/results-errata.json)."""
import json, os, subprocess, tempfile, numpy as np
from scipy.special import spherical_jn
LD1 = "/root/mamba/envs/qe/bin/ld1.x"
HERE = os.path.dirname(os.path.abspath(__file__))
W = os.environ.get("CW2_WORK") or tempfile.mkdtemp(prefix="cw2err_")
os.makedirs(W, exist_ok=True)
SPEC = {"Si": (14, "[Ne] 3s2 3p2"), "Ge": (32, "[Ar] 3d10 4s2 4p2"),
        "Ga": (31, "[Ar] 3d10 4s2 4p1"), "As": (33, "[Ar] 3d10 4s2 4p3")}
KEV_PER_INV_BOHR = 3.7289
QS = [10.0, 30.0, 51.1, 102.0, 300.0]


def run(el, rel, xmin, dx=0.008):
    Z, cfg = SPEC[el]; tag = f"{el}_rel{rel}_x{int(-xmin)}"
    inp = (f"&input\n title='{el}', zed={Z}., rel={rel}, config='{cfg}', iswitch=1, dft='PBE',\n"
           f" dx={dx}, xmin={xmin}, rmax=100.0, prefix='{tag}', file_charge='{tag}.rho'\n/\n")
    out = subprocess.run([LD1], input=inp, capture_output=True, text=True, cwd=W, env={**os.environ, "OMP_NUM_THREADS": "1"}).stdout
    assert "final scf error" in out, out[-2000:]
    d = np.loadtxt(f"{W}/{tag}.rho"); r = d[:, 0]; n = d[:, 1]/(4*np.pi*r**2)
    slope = np.polyfit(np.log(r[:4]), np.log(n[:4]), 1)[0]
    dn = {str(qk): float(6*np.trapezoid(n*spherical_jn(2, qk/KEV_PER_INV_BOHR*r)/r, r)) for qk in QS}
    return {"tag": tag, "input": inp, "r0": float(r[0]), "n_r0": float(n[0]), "slope": float(slope),
            "Nel": float(np.trapezoid(4*np.pi*r**2*n, r)), "dn": dn}


if __name__ == "__main__":
    res = {}
    for el in SPEC:
        for rel in (0, 1, 2):
            for xmin in (-7.0, -8.0):
                R = run(el, rel, xmin); res[R["tag"]] = R
                print(R["tag"], f"r0={R['r0']:.3e} n(r0)={R['n_r0']:.2f} slope={R['slope']:+.4f} Nel={R['Nel']:.5f}",
                      {k: round(v, 2) for k, v in R["dn"].items()})
    json.dump(res, open(f"{HERE}/ld1/results-errata.json", "w"), indent=1)
