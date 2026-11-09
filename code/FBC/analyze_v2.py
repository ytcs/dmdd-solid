"""FBC v2 analysis (referee corrections A1-A7, B1-B4): v2 primary (threshold R_x = 0.75), joint corners
(screening x phonon set x threshold R_x), asymmetric phonon variants, rate-region decomposition, matched (recalibrated)
energy-only distances at both edges of the eps band, matched-grid photon vs DM.  Writes data/summary_v2.json.
Run: python3 analyze_v2.py
"""
import fbc_common  # noqa: F401
import os
import sys
import json
import numpy as np
from scipy.optimize import brentq
from fbc_common import DATA, WORK, EG, HERE

sys.path.insert(0, os.path.join(HERE, "..", "..", "book", "figscripts", "ch18"))
import casc18_3 as bk   # noqa: E402

OUT = {}
BOOKA = 5.6737


def tv(P, Q):
    m = max(len(P), len(Q))
    return 0.5 * np.abs(np.pad(P, (0, m - len(P))) - np.pad(Q, (0, m - len(Q)))).sum()


def load(name):
    f = os.path.join(DATA, f"mc_{name}.npz")
    if not os.path.exists(f):
        return None
    d = np.load(f)
    r = {"omegas": d["omegas"], "he": json.loads(str(d["he"]))}
    for k in d.files:
        if k not in ("he", "omegas"):
            r[k] = d[k]
    return r


def ge2(P):
    return 1 - P[..., 0] - P[..., 1]


_CASC = {}


def casc(A):
    key = round(A, 4)
    if key not in _CASC:
        bk.AAB = A
        _CASC[key] = bk.Casc()
        bk.AAB = BOOKA
    return _CASC[key]


def eps_book(A):
    bk.AAB = A
    c = bk.Casc(X=46.0)
    bk.AAB = BOOKA
    m = [(c.pair(o - EG, 0.0) * np.arange(bk.NZ)).sum() for o in (20 * EG, 40 * EG)]
    return 20 * EG / (m[1] - m[0])


SD = json.load(open(os.path.join(HERE, "..", "..", "book", "figscripts", "ch18", "seeds18_3.json")))
EXC = np.array(SD["exc"])


def book_dm_hist(ex):
    jj = min(max(int(np.searchsorted(EXC, ex)) - 1, 0), len(EXC) - 2)
    f = np.clip((ex - EXC[jj]) / (EXC[jj + 1] - EXC[jj]), 0, 1)
    return (1 - f) * np.array(SD["hist"]["DM"][jj]) + f * np.array(SD["hist"]["DM"][jj + 1])


def split_pair(c, H, o, db=0.05):
    ex = o - EG
    j = int(round(o / db))
    row = H[j - 2:j + 3].sum(0)
    Ee = (np.arange(len(row)) + 0.5) * db
    ok = (Ee < ex) & (row > 0)
    if not ok.any():
        return None
    return c.pair(Ee[ok], ex - Ee[ok], row[ok])


def model_curves(A, oms, eps_step, H):
    c = casc(A)
    out = {k: [] for k in ("bookDM", "split", "rk1", "rkinf", "step")}
    for o in oms:
        ex = o - EG
        out["bookDM"].append(c.pair(*bk.share_seed(book_dm_hist(ex), ex)))
        out["split"].append(split_pair(c, H, o))
        out["rk1"].append(c.pair(*bk.beta_seed(1.0, ex)))
        out["rkinf"].append(c.pair(*bk.beta_seed(np.inf, ex)))
        st = np.zeros(32)
        st[1 + int(np.floor(ex / eps_step))] = 1
        out["step"].append(st)
    return out


def distances(Pfull, oms, curves, lo=4.4):
    res = {}
    for k, v in curves.items():
        t = np.array([tv(Pfull[i], v[i]) for i in range(len(oms))])
        sel = oms >= lo
        res[k] = dict(max=float(t[sel].max()), at=float(oms[sel][np.argmax(t[sel])]),
                      rep={f"{o}": float(t[int(np.argmin(np.abs(oms - o)))]) for o in (5, 6, 8, 10, 15, 20)})
    return res


def headline(r):
    oms = r["omegas"]
    h = {"eps": r["he"].get("eps"), "F": r["he"].get("F"), "bN": r["he"].get("bN")}
    P = r["heavy_P"]
    for o in (4.5, 5.0, 6.0, 8.0):
        h[f"Pge2_{o}"] = float(ge2(P)[int(np.argmin(np.abs(oms - o)))])
    h["mean_10"] = float(r["heavy_mean"][int(np.argmin(np.abs(oms - 10)))])
    h["mean_20"] = float(r["heavy_mean"][int(np.argmin(np.abs(oms - 20)))])
    h["overcount_5"] = 1 / h["Pge2_5.0"]
    if "100.0" in r["he"]:
        hh = r["he"]["100.0"]
        h["heat_100"] = (hh["Eph"] + hh["Eres"]) / 100.0
        h["pairs_100"] = hh["mean"] * EG / 100.0
        h["Eph_100"] = hh["Eph"] / 100.0
        h["Eres_100"] = hh["Eres"] / 100.0
    return h


def main():
    S = np.load(os.path.join(WORK, "seeds_refit_n12_m100_q4.npz"))
    H12 = {"heavy": S["H_heavy"], "photon": S["H_photon"]}
    prim = load("v2primary")
    oms = prim["omegas"]
    OUT["omegas"] = oms.tolist()
    OUT["primary"] = headline(prim)
    OUT["primary_P"] = {t: prim[f"{t}_P"][:, :8].tolist() for t in ("heavy", "light", "photon")}
    OUT["primary_mean"] = {t: prim[f"{t}_mean"].tolist() for t in ("heavy", "light", "photon")}
    OUT["primary_part"] = {t: prim[f"{t}_part"].tolist() for t in ("heavy", "photon")}
    OUT["primary_he"] = prim["he"]
    # ---- variants
    names = ["v2rpaw", "v2fp", "v2thr050", "v2thr100", "v2e052", "v2h30", "v2wlo3", "v2whi2"]
    corners = [f"c_{s}_{p}_{t}" for s in (0, 1, 3) for p in ("JR", "FP") for t in ("050", "100")] + ["c_lo", "c_hi"]
    V = {}
    for n in names + corners:
        r = load(n)
        if r is None:
            continue
        rp = load(n + "_p")           # P(N) rerun with a random seed subset (v2 fix; the eps/F runs keep `he`)
        if rp is not None:
            for k in list(rp):
                if k.startswith("heavy_"):
                    r[k] = rp[k]
        elif n not in ("v2rpaw", "v2fp", "v2thr050", "v2thr100"):
            print("warning: no random-subset P(N) for", n)
        V[n] = headline(r)
        V[n]["_r"] = r
    OUT["variants"] = {k: {kk: vv for kk, vv in v.items() if kk != "_r"} for k, v in V.items()}
    allv = [OUT["primary"]] + [OUT["variants"][n] for n in names[:6] + corners if n in OUT["variants"]]
    keys = [k for k in OUT["primary"] if OUT["primary"][k] is not None]
    OUT["envelope_joint"] = {k: [min(v[k] for v in allv if v.get(k) is not None),
                                 max(v[k] for v in allv if v.get(k) is not None)] for k in keys}
    # grid term (REF-FBC-B sec. 4, eo runs 8^3/10^3/12^3/14^3: P(>=2, 5 eV) 0.129/0.117/0.105/0.109, 4.5 eV
    # 0.055/0.047/0.041/0.045): relative grid uncertainty taken as the 12^3 -> 14^3 shift doubled
    OUT["grid_rel"] = {"Pge2_5.0": 2 * (0.1094 - 0.1053) / 0.1053, "Pge2_4.5": 2 * (0.0448 - 0.0413) / 0.0413}
    env = OUT["envelope_joint"]
    for k, g in OUT["grid_rel"].items():
        env[k + "_withgrid"] = [env[k][0] * (1 - g), env[k][1] * (1 + g)]
    env["overcount_5_withgrid"] = [1 / env["Pge2_5.0_withgrid"][1], 1 / env["Pge2_5.0_withgrid"][0]]
    # ---- book comparisons (as-is) and matched at primary and at the eps band edges
    Ph = prim["heavy_P"]
    cur0 = model_curves(BOOKA, oms, 3.749, H12["heavy"])
    OUT["asis"] = distances(Ph, oms, cur0)
    OUT["asis_P"] = {k: [float(ge2(np.asarray(v[int(np.argmin(np.abs(oms - 5)))])))] for k, v in cur0.items()}
    epsv = {n: v["eps"] for n, v in OUT["variants"].items() if n in corners or n in names[:6]}
    epsv["v2primary"] = OUT["primary"]["eps"]
    lo_n = min(epsv, key=epsv.get)
    hi_n = max(epsv, key=epsv.get)
    OUT["matched"] = {}
    for n in ("v2primary", lo_n, hi_n):
        r = prim if n == "v2primary" else V[n]["_r"]
        target = epsv[n]
        A = brentq(lambda a: eps_book(a) - target, 2.0, 60.0, xtol=1e-3)
        cur = model_curves(A, oms, target, H12["heavy"])
        OUT["matched"][n] = dict(eps=target, A=A, d=distances(r["heavy_P"], oms, cur),
                                 Pge2_5={k: float(ge2(np.asarray(v[int(np.argmin(np.abs(oms - 5)))])))
                                         for k, v in cur.items()})
        print(f"matched {n}: eps {target:.3f} A {A:.2f}", {k: (round(x['max'], 3), x['at']) for k, x in
                                                           OUT['matched'][n]['d'].items()}, flush=True)
    # ---- alpha_RK: computed-split agreement (precision, not accuracy)
    # ---- photon vs DM at matched grids
    ph = {}
    c0 = casc(BOOKA)
    grids = {"12": (S["H_heavy"], S["H_photon"])}
    f20 = os.path.join(WORK, "seedsH_refit_n20_m100_q4.npz")
    if os.path.exists(f20):
        d20 = np.load(f20)
        grids["20"] = (d20["H_heavy"], d20["H_photon"])
    P28 = np.load(os.path.join(WORK, "photon_fine_refit_n28.npz"))["H"]
    sel = oms >= 4.5
    eo = {}
    for g, (Hh, Hp) in grids.items():
        t = np.array([tv(split_pair(c0, Hh, o), split_pair(c0, Hp, o)) if o >= 4.5 else 0 for o in oms])
        eo[g] = t
        ph[f"energyonly_{g}"] = dict(max=float(t[sel].max()), at=float(oms[sel][np.argmax(t[sel])]))
    if "20" in grids:
        t = np.array([tv(split_pair(c0, grids["20"][1], o), split_pair(c0, P28, o)) if o >= 4.5 else 0 for o in oms])
        ph["photon20_vs_photon28"] = float(t[sel].max())
        t = np.array([tv(split_pair(c0, grids["20"][0], o), split_pair(c0, grids["12"][0], o)) if o >= 4.5 else 0
                      for o in oms])
        ph["dm20_vs_dm12"] = float(t[sel].max())
        t = np.array([tv(split_pair(c0, grids["20"][1], o), split_pair(c0, grids["12"][1], o)) if o >= 4.5 else 0
                      for o in oms])
        ph["photon20_vs_photon12"] = float(t[sel].max())
    rf = load("phdm20")
    if rf is not None:
        kp = [k for k in rf if k.endswith("_P") and "H_photon" in k][0]
        kd = [k for k in rf if k.endswith("_P") and "H_heavy" in k][0]
        t = np.array([tv(rf[kp][i], rf[kd][i]) for i in range(len(oms))])
        ph["fullband_20"] = dict(max=float(t[sel].max()), at=float(oms[sel][np.argmax(t[sel])]),
                                 rep={f"{o}": float(t[int(np.argmin(np.abs(oms - o)))]) for o in (5, 6, 8, 10, 15, 20)},
                                 P2ratio_5=float(ge2(rf[kp])[int(np.argmin(np.abs(oms - 5)))] /
                                                 ge2(rf[kd])[int(np.argmin(np.abs(oms - 5)))]))
    OUT["photon_dm"] = ph
    # ---- independent halves (C11)
    a, b = load("halfA"), load("halfB")
    if a is not None and b is not None:
        OUT["halves"] = {t: float(max(tv(a[f"{t}_P"][i], b[f"{t}_P"][i]) for i in range(len(oms))))
                         for t in ("heavy", "photon")}
    json.dump(OUT, open(os.path.join(DATA, "summary_v2.json"), "w"), indent=0, default=float)
    print(json.dumps({k: OUT[k] for k in ("primary", "envelope_joint", "photon_dm")}, indent=0, default=float)[:5000])
    for n, v in OUT["variants"].items():
        print(f"{n:12s} eps {v['eps']:.3f} F {v['F']:.4f} P5 {v['Pge2_5.0']:.3f} P4.5 {v['Pge2_4.5']:.3f} "
              f"N10 {v['mean_10']:.3f} over {v['overcount_5']:.1f}")
    print("as-is:", {k: (round(x['max'], 3), x['at']) for k, x in OUT["asis"].items()})
    print("halves:", OUT.get("halves"))


if __name__ == "__main__":
    main()
