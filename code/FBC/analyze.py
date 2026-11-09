"""FBC step 6-7: comparisons and uncertainty bands. Reads data/mc_*.npz, the seeds, and the book's energy-only
cascade (book/figscripts/ch18/casc18_3.py, A_AB = 5.6737 eV^3, E_g = 1.160 eV; read-only import) and writes
data/summary.json with every number quoted in returns/R19/FBC.md.
Run: python3 analyze.py
"""
import fbc_common  # noqa: F401
import os
import sys
import json
import numpy as np
from fbc_common import DATA, WORK, EG, HERE

sys.path.insert(0, os.path.join(HERE, "..", "..", "book", "figscripts", "ch18"))
import casc18_3 as bk   # noqa: E402

SEEDS = "refit_n12_m100_q4"
OUT = {}
OM_REP = [3.0, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 10.0, 12.0, 15.0, 20.0]


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
        if "_" in k and k.split("_")[0] in ("heavy", "light", "photon", "q0"):
            r[k] = d[k]
    return r


def book_curves(oms, Hs):
    """book energy-only cascade with: the book DM and photon seeds, RK alpha = 1 and inf, step, and the
    full-band computed splits (share histograms H[seed][omega_bin, E_e_bin] of seeds.py)."""
    c = bk.Casc()
    sd = json.load(open(os.path.join(HERE, "..", "..", "book", "figscripts", "ch18", "seeds18_3.json")))
    exc = np.array(sd["exc"])

    def hist_at(name, ex):
        jj = min(max(int(np.searchsorted(exc, ex)) - 1, 0), len(exc) - 2)
        f = np.clip((ex - exc[jj]) / (exc[jj + 1] - exc[jj]), 0, 1)
        return (1 - f) * np.array(sd["hist"][name][jj]) + f * np.array(sd["hist"][name][jj + 1])

    out = {k: [] for k in ("bookDM", "bookPH", "rk1", "rkinf", "step")}
    for s in Hs:
        out[f"split_{s}"] = []
    db = 0.05
    for o in oms:
        ex = o - EG
        out["bookDM"].append(c.pair(*bk.share_seed(hist_at("DM", ex), ex)))
        out["bookPH"].append(c.pair(*bk.share_seed(hist_at("OPT", ex), ex)))
        out["rk1"].append(c.pair(*bk.beta_seed(1.0, ex)))
        out["rkinf"].append(c.pair(*bk.beta_seed(np.inf, ex)))
        out["step"].append(bk.delta(bk.step(o)))
        for s, H in Hs.items():
            j = int(round(o / db))
            row = H[j - 2:j + 3].sum(0)                    # +-0.1 eV in omega
            Ee = (np.arange(len(row)) + 0.5) * db
            ok = (Ee < ex) & (row > 0)
            out[f"split_{s}"].append(c.pair(Ee[ok], ex - Ee[ok], row[ok]))
    return {k: np.array(v) for k, v in out.items()}


def summarize_run(r, ty):
    return r[f"{ty}_P"], r[f"{ty}_mean"]


def main():
    prim = load("primary")
    oms = prim["omegas"]
    S = np.load(os.path.join(WORK, f"seeds_{SEEDS}.npz"))
    Hs = {"heavy": S["H_heavy"], "light": S["H_light"], "photon": S["H_photon"]}
    Ssc = os.path.join(WORK, "seeds_scissor_n12_m100_q4.npz")
    if os.path.exists(Ssc):
        Hs["heavy_scissor"] = np.load(Ssc)["H_heavy"]
        Hs["light_scissor"] = np.load(Ssc)["H_light"]
    Pf = os.path.join(WORK, "photon_fine_refit_n28.npz")
    if os.path.exists(Pf):
        Hs["photon_fine"] = np.load(Pf)["H"]
    BK = book_curves(oms, Hs)
    # ---------------- seeds: share statistics
    sh = {}
    for s, H in Hs.items():
        rows = {}
        for o in (5.0, 10.0, 15.0, 20.0):
            j = int(round(o / 0.05))
            row = H[j - 2:j + 3].sum(0)
            Ee = (np.arange(len(row)) + 0.5) * 0.05
            ex = o - EG
            ok = Ee < ex
            w = row[ok] / row[ok].sum()
            x = Ee[ok] / ex
            rows[str(o)] = dict(meanEe=float((w * Ee[ok]).sum()), Pxgt=float(w[x > 0.5].sum()),
                                Pext=float(w[(x < 0.25) | (x > 0.75)].sum()))
        sh[s] = rows
    OUT["shares"] = sh
    # ---------------- primary curves and comparisons
    P = {t: prim[f"{t}_P"] for t in ("heavy", "light", "photon")}
    comp = {}
    for ref in ("bookDM", "rk1", "rkinf", "step", "split_heavy"):
        comp[ref] = [float(tv(P["heavy"][i], BK[ref][i])) for i in range(len(oms))]
    comp["photon_vs_heavy"] = [float(tv(P["photon"][i], P["heavy"][i])) for i in range(len(oms))]
    comp["light_vs_heavy"] = [float(tv(P["light"][i], P["heavy"][i])) for i in range(len(oms))]
    comp["book_photon_vs_DM"] = [float(tv(BK["bookPH"][i], BK["bookDM"][i])) for i in range(len(oms))]
    OUT["omegas"] = oms.tolist()
    OUT["tv"] = comp
    OUT["P_heavy"] = P["heavy"][:, :8].tolist()
    OUT["P_light"] = P["light"][:, :8].tolist()
    OUT["P_photon"] = P["photon"][:, :8].tolist()
    OUT["P_book"] = BK["bookDM"][:, :8].tolist()
    OUT["mean"] = {t: prim[f"{t}_mean"].tolist() for t in P}
    OUT["mean_book"] = (BK["bookDM"] * np.arange(BK["bookDM"].shape[1])).sum(1).tolist()

    def ge2(Pm):
        return 1 - Pm[..., 0] - Pm[..., 1]
    OUT["P2"] = {t: P[t][:, 2].tolist() for t in P}
    OUT["Pge2"] = {t: ge2(P[t]).tolist() for t in P}
    for k in ("bookDM", "rk1", "rkinf", "step", "split_heavy"):
        OUT["P2"][k] = BK[k][:, 2].tolist()
        OUT["Pge2"][k] = ge2(BK[k]).tolist()
    # ---------------- alpha_RK spread and what the computed split removes (inside the book cascade)
    rk_spread = np.array([tv(BK["rk1"][i], BK["rkinf"][i]) for i in range(len(oms))])
    splits = [k for k in BK if k.startswith("split_") and "photon" not in k]
    comp_spread = np.array([max(tv(BK[a][i], BK[b][i]) for a in splits for b in splits) if len(splits) > 1 else 0
                            for i in range(len(oms))])
    win = (oms >= 4.4) & (oms <= 13.0)
    OUT["rk_spread"] = rk_spread.tolist()
    OUT["computed_split_spread"] = comp_spread.tolist()
    OUT["rk_removed"] = dict(max_rk=float(rk_spread[win].max()), max_comp=float(comp_spread[win].max()),
                             frac_removed_of_max=float(1 - comp_spread[win].max() / rk_spread[win].max()),
                             median_frac=float(np.median(1 - comp_spread[win] / np.maximum(rk_spread[win], 1e-9))),
                             splits=splits)
    # ---------------- variants
    variants = {"resta": "scr1", "rpa0": "scr2", "rpaw": "scr3", "D2x0.6": "ph06", "D2x1.6": "ph16",
                "scissor": "scissor", "noexch": "rx0", "eo": "eo", "nophonon": "nophon", "hefree": "hefree",
                "half2": "primary_half2", "rxthr": "rxthr", "T123": "T123"}
    var = {}
    for lab, nm in variants.items():
        r = load(nm)
        if r is None:
            continue
        v = {"he": r["he"]}
        for t in ("heavy", "photon", "light"):
            if f"{t}_P" in r and len(r["omegas"]) == len(oms):
                v[f"tv_{t}"] = [float(tv(r[f"{t}_P"][i], P[t][i])) for i in range(len(oms))]
                v[f"mean_{t}"] = r[f"{t}_mean"].tolist()
                v[f"Pge2_{t}"] = ge2(r[f"{t}_P"]).tolist()
                v[f"tvbook_{t}"] = [float(tv(r[f"{t}_P"][i], BK["bookDM"][i])) for i in range(len(oms))]
                v[f"tvstep_{t}"] = [float(tv(r[f"{t}_P"][i], BK["step"][i])) for i in range(len(oms))]
                v[f"part_{t}"] = r[f"{t}_part"].tolist()
        var[lab] = v
    OUT["variants"] = var
    # energy-only (book) cascade with the computed splits: seed-only effects
    eo_cmp = {}
    for a, b in (("split_heavy", "bookDM"), ("split_light", "split_heavy"), ("split_photon", "split_heavy"),
                 ("split_photon_fine", "split_heavy"), ("split_photon", "split_photon_fine"),
                 ("split_heavy_scissor", "split_heavy"), ("bookPH", "bookDM")):
        if a in BK and b in BK:
            eo_cmp[f"{a}|{b}"] = [float(tv(BK[a][i], BK[b][i])) for i in range(len(oms))]
    OUT["tv_energyonly"] = eo_cmp
    OUT["Pge2"]["split_photon_fine"] = ge2(BK["split_photon_fine"]).tolist() if "split_photon_fine" in BK else None
    # uncertainty envelopes of headline numbers over the variants
    groups = {"screening": ["resta", "rpa0", "rpaw"], "phonon": ["D2x0.6", "D2x1.6"], "bands": ["scissor"],
              "exchange": ["noexch", "rxthr"], "highE": ["hefree"], "MC": ["half2"], "T123K": ["T123"]}

    def headline(src):
        h = {}
        if src is None:
            return h
        he_ = src["he"]
        for k in ("eps", "F", "bN"):
            if k in he_:
                h[k] = he_[k]
        mh = src.get("mean_heavy")
        pg = src.get("Pge2_heavy")
        if pg is not None:
            for o in (4.5, 5.0, 6.0, 8.0):
                i = int(np.argmin(np.abs(oms - o)))
                h[f"Pge2_{o}"] = pg[i]
            for o in (10.0, 20.0):
                i = int(np.argmin(np.abs(oms - o)))
                h[f"mean_{o}"] = mh[i]
            win = (oms >= 4.4) & (oms <= 13)
            h["maxTVbook"] = max(src["tvbook_heavy"])
            h["maxTVstep"] = max(src["tvstep_heavy"])
            i5 = int(np.argmin(np.abs(oms - 5.0)))
            h["step_over_cascade_5eV"] = 1.0 / pg[i5]
        return h
    prim_v = {"he": prim["he"], "mean_heavy": OUT["mean"]["heavy"], "Pge2_heavy": OUT["Pge2"]["heavy"],
              "tvbook_heavy": comp["bookDM"], "tvstep_heavy": comp["step"]}
    H0 = headline(prim_v)
    env = {"primary": H0}
    for gname, labs in groups.items():
        vals = [headline(var[l]) for l in labs if l in var]
        env[gname] = {k: [min(v[k] for v in vals if k in v), max(v[k] for v in vals if k in v)]
                      for k in H0 if any(k in v for v in vals)}
    allv = [headline(var[l]) for g in groups.values() for l in g if l in var]
    env["all"] = {k: [min([H0[k]] + [v[k] for v in allv if k in v]), max([H0[k]] + [v[k] for v in allv if k in v])]
                  for k in H0}
    OUT["envelope"] = env
    OUT["he"] = prim["he"]
    OUT["part"] = {t: prim[f"{t}_part"].tolist() for t in P}
    OUT["nfirst"] = {t: prim[f"{t}_nfirst"].tolist() for t in P}
    json.dump(OUT, open(os.path.join(DATA, "summary.json"), "w"), indent=0, default=float)
    # ---------------- print
    print("omega |  <N> heavy light photon book |  P(>=2) heavy book step | TV(heavy, book) TV(rk1) TV(rkinf) TV(step) "
          "TV(split_heavy in book) | TV(photon,heavy)")
    for o in OM_REP:
        i = int(np.argmin(np.abs(oms - o)))
        print(f"{oms[i]:5.2f} | {OUT['mean']['heavy'][i]:.3f} {OUT['mean']['light'][i]:.3f} {OUT['mean']['photon'][i]:.3f} "
              f"{OUT['mean_book'][i]:.3f} | {OUT['Pge2']['heavy'][i]:.3f} {OUT['Pge2']['bookDM'][i]:.3f} "
              f"{OUT['Pge2']['step'][i]:.3f} | {comp['bookDM'][i]:.3f} {comp['rk1'][i]:.3f} {comp['rkinf'][i]:.3f} "
              f"{comp['step'][i]:.3f} {comp['split_heavy'][i]:.3f} | {comp['photon_vs_heavy'][i]:.3f}")
    print("max TV over omega:", {k: round(max(v), 3) for k, v in comp.items()})
    print("RK spread removal:", OUT["rk_removed"])
    print("shares:", json.dumps(sh, indent=0)[:1500])
    print("high-energy:", {k: OUT["he"][k] for k in ("eps", "deps", "F", "dF", "bN") if k in OUT["he"]})
    for lab, v in var.items():
        h = v["he"]
        mt = max(v.get("tv_heavy", [0]))
        print(f"variant {lab:9s}: eps = {h.get('eps', float('nan')):.3f}, F = {h.get('F', float('nan')):.4f}, "
              f"max TV vs primary (heavy) = {mt:.3f}")


if __name__ == "__main__":
    main()
