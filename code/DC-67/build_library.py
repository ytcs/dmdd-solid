"""DC-67 library build: P_casc(N | x; theta) single-carrier tables for 30 materials and the theta set, at the TRUE omega_0.
N = GAP-EF-v3 model.grid (kept for comparability), true w by the convex phonon read of casc2 (frac = True; one solve); X rule = predict.R (X = 60 if lam > 5 else 25; Si calibration row X = 40).
Inputs are read from the copy src_copies/predict.py and from code/GAP-EF-v3/data/results.json (A per variant).  theta set:
  M factor on A_ph (one M-type factor, CW7 sec. 4(d), GAP-EF IF-EF2): m = 1/1.2, 1/1.1, 1, 1/0.9, 1/0.8 (spans theta_GW +-20%, theta_Z 0.8-1 taken singly; WP5-v4 sec. 8);
  structural: V1 (theta_ii = 3/2), V3 (a_DOS = 1), Wv (W_v = E_g, narrow-band rows only).
Output per material: data/lib/<mat>.npz + one line per (material, config) in data/library_summary.csv.  Resumable."""
import csv, json, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, "src_copies")]
import casc2
from model import grid, nodes, lagrange
from predict import PRED, VAL, SI

R3 = json.load(open(os.path.join(HERE, "..", "GAP-EF-v3", "data", "results.json")))
A = {v: R3["variants"][v]["A"] for v in ("V0", "V1", "V3")}
MFAC = {"m0.833": 1 / 1.2, "m0.909": 1 / 1.1, "m1": 1.0, "m1.111": 1 / 0.9, "m1.25": 1 / 0.8}
XSTEP = 0.25; XSTEP_F = 0.05; XFINE = 5.0


def materials():
    M = {"Si": dict(Eg=SI["Eg"], om=SI["om0"], Wv=SI["Wv"], narrow=False, grp="S", Xfix=40.0)}
    for k, (grp, Eg, om, prov, narrow) in PRED.items():
        M[k] = dict(Eg=Eg, om=om, Wv=None, narrow=narrow, grp=grp, Xfix=None)
    for k in ("3C-SiC", "6H-SiC"):
        Eg, om = VAL[k][0], VAL[k][1]
        M[k] = dict(Eg=Eg, om=om, Wv=None, narrow=False, grp="C", Xfix=None)
    return M


def configs(m):
    c = [(k, dict(A=A["V0"] * f, theta=1.0, a=0.5, Wv=m["Wv"], tag="V0")) for k, f in MFAC.items()]
    c.append(("V1", dict(A=A["V1"], theta=1.5, a=0.5, Wv=m["Wv"], tag="V1")))
    c.append(("V3", dict(A=A["V3"], theta=1.0, a=1.0, Wv=m["Wv"], tag="V3")))
    if m["narrow"]:
        c.append(("Wv", dict(A=A["V0"], theta=1.0, a=0.5, Wv=m["Eg"], tag="Wv")))
    return c


def nz_for(Nbar, sig):
    return int(2 ** np.ceil(np.log2(Nbar + 8 * sig + 2)))


def solve_cfg(m, cfg, N=None, Nz=None, X=None, ks=None):
    """Solve at the commensurate nodes and interpolate to the true w.  Returns dict with P[t] on the fine grid."""
    Eg = m["Eg"]; lam = cfg["A"] / Eg ** 3; w = m["om"] / Eg
    if X is None:
        X = m["Xfix"] or (60.0 if cfg["A"] / Eg ** 3 > 5.0 else 25.0)
    if N is None:
        N = grid(w, nwmin=1, theta=cfg["theta"])[0]
    W = None if cfg["Wv"] is None else cfg["Wv"] / Eg
    if Nz is None:
        e = 1.613 + 2.329 * (lam * w ** 0.965) ** 0.2395            # (EF9), first pass only; the main loop re-checks Nz >= Nbar + 8 sigma
        Nz = nz_for(X / e + 1, np.sqrt(0.17 * X / e))
    if ks is None:
        x, G = casc2.solve_gf(lam, w, X, N, Nz, a=cfg["a"], W=W, theta=cfg["theta"], frac=True)
        Pe = casc2.pmf(G[0]); Ph = None if W is None else casc2.pmf(G[1])
        return dict(x=x, Pe=Pe, Ph=Ph, N=N, Nz=Nz, X=X, lam=lam, w=w, W=W, ks=["frac"])
    res = []
    for k in ks:      # rejected node-interpolation of P, kept for the record (checks W1)
        x, G = casc2.solve_gf(lam, k / N, X, N, Nz, a=cfg["a"], W=W, theta=cfg["theta"])
        res.append((casc2.pmf(G[0]), None if W is None else casc2.pmf(G[1])))
    xs = [k / N for k in ks]
    Pe = lagrange(xs, [r[0] for r in res], w) if len(ks) > 1 else res[0][0]
    Ph = None if W is None else (lagrange(xs, [r[1] for r in res], w) if len(ks) > 1 else res[0][1])
    return dict(x=x, Pe=Pe, Ph=Ph, N=N, Nz=Nz, X=X, lam=lam, w=w, W=W, ks=ks)


def asym(x, P, frac=0.5):
    """eps/E_g, F, b from the fit on omega in [frac X, X], electron seed with sibling at the band edge (cascade.py asym)."""
    n = np.arange(P.shape[1]); m = P @ n; v = P @ (n * n) - m ** 2
    sel = x >= frac * x[-1]; om = 1.0 + x[sel]
    Am = np.vstack([om, np.ones_like(om)]).T
    sm, b = np.linalg.lstsq(Am, 1.0 + m[sel], rcond=None)[0]
    sv, _ = np.linalg.lstsq(Am, v[sel], rcond=None)[0]
    return 1.0 / sm, sv / sm, b


def table(r):
    x, N = r["x"], r["N"]
    grid_x = np.concatenate([np.arange(0.0, XFINE, XSTEP_F), np.arange(XFINE, x[-1] + 1e-9, XSTEP)])   # fine rows at the ii thresholds: P rises within ~0.3 E_g in wide gaps
    idx = np.unique(np.round(grid_x * N).astype(int))
    idx = idx[idx < len(x)]
    Pe = r["Pe"][idx]; Ph = None if r["Ph"] is None else r["Ph"][idx]
    nmax = int(np.max(np.nonzero(np.abs(r["Pe"][-1]) > 1e-13)[0])) + 3
    return idx, Pe, Ph, nmax


if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "data", "lib"), exist_ok=True)
    M = materials()
    only = sys.argv[1:] or None
    summ = os.path.join(HERE, "data", "library_summary.csv")
    hdr = ["material", "cfg", "tag", "E_g", "om0", "A", "lam", "w", "theta", "a", "W", "N", "X", "Nz", "nodes", "eps_eV", "eps_over_Eg", "F", "b",
           "sumP_err", "Pmin", "tail_mass", "Nbar_X", "sig_X", "Nz_rule_ok", "runtime_s"]
    done = set()
    if os.path.exists(summ):
        done = {(r["material"], r["cfg"]) for r in csv.DictReader(open(summ))}
    else:
        with open(summ, "w", newline="") as f_:
            csv.writer(f_).writerow(hdr)
    order = sorted(M, key=lambda k: grid(M[k]["om"] / M[k]["Eg"], nwmin=1)[0])
    for mat in order:
        if only and mat not in only: continue
        m = M[mat]
        fn = os.path.join(HERE, "data", "lib", mat.replace("/", "_") + ".npz")
        store = dict(np.load(fn)) if os.path.exists(fn) else {}
        for cname, cfg in configs(m):
            if (mat, cname) in done: continue
            t0 = time.time()
            r = solve_cfg(m, cfg)
            n = np.arange(r["Pe"].shape[1])
            mX = r["Pe"][-1] @ n; sX = np.sqrt(max(r["Pe"][-1] @ (n * n) - mX ** 2, 0))
            ok = r["Nz"] >= mX + 8 * sX
            if not ok:
                r = solve_cfg(m, cfg, Nz=nz_for(mX, sX)); n = np.arange(r["Pe"].shape[1])
                mX = r["Pe"][-1] @ n; sX = np.sqrt(max(r["Pe"][-1] @ (n * n) - mX ** 2, 0)); ok = r["Nz"] >= mX + 8 * sX
            e, F, b = asym(r["x"], r["Pe"])
            idx, Pe, Ph, nmax = table(r)
            store["x_" + cname] = r["x"][idx]
            store["Pe_" + cname] = np.where(np.abs(Pe[:, :nmax + 1]) < 1e-15, 0.0, Pe[:, :nmax + 1])
            if Ph is not None:
                store["Ph_" + cname] = np.where(np.abs(Ph[:, :nmax + 1]) < 1e-15, 0.0, Ph[:, :nmax + 1])
            np.savez_compressed(fn, **store)
            allP = r["Pe"] if r["Ph"] is None else np.concatenate([r["Pe"], r["Ph"]])
            row = [mat, cname, cfg["tag"], m["Eg"], m["om"], cfg["A"], r["lam"], r["w"], cfg["theta"], cfg["a"], r["W"], r["N"], r["X"], r["Nz"],
                   "/".join(map(str, r["ks"])), e * m["Eg"], e, F, b, np.abs(allP.sum(1) - 1).max(), allP.min(), r["Pe"][-1][nmax + 1:].sum(), mX, sX, bool(ok),
                   round(time.time() - t0, 1)]
            with open(summ, "a", newline="") as f:
                csv.writer(f).writerow(row)
            print(mat, cname, "N", r["N"], "X", r["X"], "Nz", r["Nz"], "eps", round(e * m["Eg"], 4), "F", round(F, 4), "Pmin", allP.min(), "t", row[-1], flush=True)
