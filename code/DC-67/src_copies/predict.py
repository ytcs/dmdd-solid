"""GAP-EF-v3 predict.py (R17 FIX-GAP-EF-GRID): v2's predict.py on the commensurate solver (cascade.py strict grid; model.run
interpolates in w over commensurate nodes on one grid; theta = 3/2 runs on even N).  Inputs, variants, statistics and band rules are
v2's unchanged.  Parallel over rows (multiprocessing, 4 workers); identical (A, E_g, omega_0, variant) runs are shared.
table1 (lam = 0 rows): copied from code/GAP-EF-v2/data/results.json -- omega_0 never enters at lam = 0 (phonon=False) and its grids
h = 0.01, 0.005 divide 1 and 3/2 (GAP-EF-v3-C1 checks this), so the strict solver returns the same numbers.
GAP-EF-v2 predict.py: calibration (A on Si eps_eh only), validation against measured (eps_eh, F_eh), predictions for the
WP8-U survivors lacking data, and the section-1 tables. Writes data/results.json (read by checks.py; quoted in returns/R16/GAP-EF-v2.md).
Run: python3 -I predict.py   (deterministic quadrature, no Monte Carlo; ~20-30 min).
v2 changes: CsI grid bug fixed in model.grid (REF-B 2.7); GaN validated at the EBIC value 9.59 eV (8.9 is not a named measurement,
REF-A K3); beta-Ga2O3 added as an extended-set row (REF-B 2.6); optional EF-LIT rows (VAL_LIT); section-1 tables (lam -> 0 on one
grid pair, Richardson, every column), R&K Eqs. (12)-(13) slopes, dF/dA, renewal ratios."""
import json, os, sys, time
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import run, calibrate_A

# ---- calibration datum [FT 2004.11499 p.1, p.5]: eps_eh = 3.749 +- 0.001 eV, F = 0.119 +- 0.002 at 123 K, 5.9 keV.
# E_g(110 K) = 1.164 eV [FT 2004.10709 Table I p.5]; omega_0 = 63 meV [FT 2004.10709 p.3]; W_v = 12 eV [FT 2004.10709 p.3].
SI = dict(Eg=1.164, om0=0.063, Wv=12.0, eps=3.749)
VARIANTS = {"V0": dict(theta=1.0, a=0.5), "V1": dict(theta=1.5, a=0.5), "V3": dict(theta=1.0, a=1.0)}

# ---- validation set: (E_g [eV], omega_0 [eV], eps_meas, eps_lo, eps_hi, F_meas or None, tag/provenance)
VAL = {
 "Ge":   (0.73, 0.037, 2.96, 2.95, 3.10, "0.06-0.13 (secondary quote)", "E_g, eps: [FT 1909.05806 p.14-15] (77 K); omega_LO 37 meV [FT 1901.07569 Table I p.2]; F range [FT 1909.05806 p.14]"),
 "C":    (5.47, 0.163, 12.95, 12.82, 13.25, None, "E_g, omega_L [FT 1901.07569 Table I p.2]; eps 13.1+-0.2, 13.25+-0.5, 13.05+-0.2, 12.82+-0.13 [FT 2311.05011 p.5]"),
 "4H-SiC": (3.26, 0.120, 7.83, 7.81, 7.85, "0.1 (2011 linewidth); <=0.04 (2005 limit)", "E_g, omega_L [FT 2008.08560 Table I p.5]; eps [FT 2311.03902 p.1, p.5]; F [FT 2311.03902 Table 2 p.2]"),
 "6H-SiC": (3.02, 0.120, 6.7, 6.7, 6.7, None, "E_g, omega_L, eps [FT 2008.08560 Table I p.5]"),
 "3C-SiC": (2.39, 0.1205, 6.90, 6.90, 6.90, None, "E_g, omega_L [FT 2008.08560 Table I p.5]; eps [FT 2610.16949 Table II p.8]"),
 "GaN":  (3.43, 0.0889, 9.59, 9.59, 9.59, None, "E_g, omega_O_max [FT 1910.10716 Table I p.2 via WP8-U CSV]; eps 9.59 (EBIC, Ref. [100] of 2308.03893) [FT 2308.03893 p.19]; 8.9 there is the paper's own calculation and an unspecified review value (not used)"),
 "SiO2": (9.2, 0.149, 18.0, 16.4, 18.0, None, "E_g, omega_O_max (alpha-quartz) [FT 1910.10716 Table I p.2 via WP8-U CSV]; eps 18.0 (one sample 16.4), 1975 oxide data [FT 2610.16949 p.8]"),
}
# extended set: [FT] values that are model-assisted estimates, reported with their residual, kept out of the primary statistic
VAL_EXT = {
 "b-Ga2O3": (4.8, 0.0973, 15.6, 15.6, 15.6, None, "E_g 4.8 [FT 2311.05011 p.1] (4.5 [FT 1902.02687 p.1]); omega_max 784.92 cm^-1 = 97.3 meV (DFPT-LDA) [FT 1902.02687 p.6]; eps 15.6 'experimental estimation' EBIC + MC (Yakimov et al.) [FT 2311.05011 p.6]"),
}
# EF-LIT rows (returns/R16/EF-LIT.md), [FT] only; filled if that return exists when validation is run
# Neither is a measurement (EF-LIT bottom line), so both are reported with residuals and kept out of the primary statistic.
VAL_LIT = {
 "Al2O3": (8.8, 0.104, 27.0, 27.0, 27.0, None, "E_g, omega_O_max as in PRED [FT 1910.10716 Table I p.2]; eps 27 eV, vendor-datasheet value tabulated in Karacheban et al. arXiv:1504.04023 Table 1 p.3 [FT via returns/R16/EF-LIT.md row 1]; not a measurement"),
 "CaWO4": (5.2, 0.106, 29.8, 29.8, 29.8, None, "E_g, omega_O_max as in PRED [FT 1910.10716 Table I p.2]; eps = 2.35 E_g/B = 29.8 eV with B = 0.41, Robbins-Lempicki model, Mikhailik-Kraus arXiv:1001.5461 Table 2 [FT via returns/R16/EF-LIT.md row 3]; model value, thermalised-pair definition"),
}
UNVER = {  # remembered values: shown, excluded from every residual statistic
 "GaAs": (1.42, 0.0349, 4.2, "E_g, omega_O_max [FT 1910.10716 Table I p.2]; eps ~4.2 [UNVERIFIED; Bertuccio-Maiocchi, J. Appl. Phys. (2002), DOI 10.1063/1.1490158, no open full text; plotted in 2610.16949 Fig. 1]"),
}
# ---- prediction targets: WP8-U survivors (S) and survivor-cond (C) semiconductors/insulators with E_g and omega_max in the CSV
PRED = {
 "GaAs":    ("S", 1.42, 0.0349, "FT 1910.10716 Table I p.2 (E_g, omega_O_max)", False),
 "Al2O3":   ("S", 8.8, 0.104, "FT 1910.10716 Table I p.2", True),
 "TeO2":    ("S", 4.645, 0.0890, "DB JARVIS JVASP-57128 (mbj_bandgap; modes)", True),
 "CaWO4":   ("S", 5.2, 0.106, "FT 1910.10716 Table I p.2", True),
 "LiF":     ("S", 14.2, 0.0772, "FT 1910.10716 Table I p.2", True),
 "NaF":     ("S", 11.5, 0.0499, "FT 1910.10716 Table I p.2", True),
 "GaN":     ("C", 3.43, 0.0889, "FT 1910.10716 Table I p.2", False),
 "AlN":     ("C", 6.2, 0.109, "FT 1910.10716 Table I p.2", False),
 "InSb":    ("C", 0.24, 0.0215, "FT 1910.10716 Table I p.2", False),
 "GaSb":    ("C", 0.72, 0.0273, "FT 1910.10716 Table I p.2", False),
 "SiO2-q":  ("C", 9.2, 0.149, "FT 1910.10716 Table I p.2", True),
 "ZnO":     ("C", 3.3, 0.0634, "FT 1910.10716 Table I p.2", True),
 "MgO":     ("C", 7.83, 0.0826, "FT 1910.10716 Table I p.2", True),
 "NaCl":    ("C", 8.75, 0.0306, "FT 1910.10716 Table I p.2", True),
 "NaI":     ("C", 5.8, 0.0200, "FT 1910.10716 Table I p.2", True),
 "CsI":     ("C", 6.14, 0.0100, "FT 1910.10716 Table I p.2", True),
 "CaF2":    ("C", 11.81, 0.0556, "FT 1910.10716 Table I p.2", True),
 "MgF2":    ("C", 12.4, 0.0737, "FT 1910.10716 Table I p.2", True),
 "ZnS":     ("C", 3.8, 0.0410, "FT 1910.10716 Table I p.2", False),
 "PbTe":    ("C", 0.19, 0.0135, "FT 1910.10716 Table I p.2", False),
 "PbS":     ("C", 0.29, 0.0269, "FT 1910.10716 Table I p.2", False),
 "PbSe":    ("C", 0.17, 0.0171, "FT 1910.10716 Table I p.2", False),
 "SrTiO3":  ("C", 2.302, 0.0656, "DB JARVIS JVASP-8082 (mbj_bandgap; modes)", True),
 "KTaO3":   ("C", 3.326, 0.0652, "DB JARVIS JVASP-1127 (mbj_bandgap; modes)", True),
 "C":       ("C", 5.47, 0.163, "FT 1901.07569 Table I p.2", False),
 "4H-SiC":  ("C", 3.26, 0.120, "FT 2008.08560 Table I p.5", False),
 "Ge":      ("S", 0.73, 0.037, "FT 1909.05806 p.15; FT 1901.07569 Table I", False),
}
# the last bool = narrow-valence-band (ionic/oxide) flag: adds the W_v = E_g variant to the error band [E]

def R(**k):
    X = 60.0 if k["A"] / k["Eg"] ** 3 > 5.0 else 25.0     # large lam: slower approach to the asymptote (few pairs per E_g)
    return run(X=X, nwmin=1, **k)                        # v2: no Nmax cap; model.grid enforces |w_eff/w - 1| < 1%

def table1():
    """Section-1 decomposition table. lam -> 0 rows: Richardson on (h, h/2) = (0.01, 0.005) for every column (REF-B 2.1).
    Phonon rows: Si V0 (B_h = 12 eV, the calibration run), Si V1 (theta = 3/2), Ge (V0 A, 77 K inputs); RPP limit."""
    from cascade import Cascade
    keys = ("eps", "F", "VR", "VP", "Cov2", "Cov2_direct", "F_ren", "rbar", "carriers_per_pair")
    sets = ("N", "R", "P", "H", "D", "R2", "C", "Re", "Rh", "R2e", "R2h", "Ce", "Ch")
    T = {}
    for lab, kw in (("lam0_th1", dict(theta=(1.0, 1.0))), ("lam0_th15", dict(theta=(1.5, 1.5))),
                    ("RPP", dict(a=(0.0, 0.0), hole_delta=True))):
        d = [Cascade(0.0, 0.05, X=30, h=h, phonon=False, sets=sets, **kw).decomposition(0) for h in (0.01, 0.005)]
        T[lab] = {k: 2 * d[1][k] - d[0][k] for k in keys}
        T[lab]["h001"] = {k: d[0][k] for k in keys}
        print(lab, T[lab]["F"], T[lab]["F_ren"], flush=True)
    return T

def rk_slopes():
    """R&K 2004.10709 Eqs. (12)-(13) p.6: eps = 1.7 E_g + 0.084 A + 1.3, F = -0.028 E_g + 0.0015 A + 0.14 (W = 12 eV, omega_0 = 63 meV)."""
    pts = [(3.0, 1.124), (5.2, 1.124), (7.0, 1.124), (5.2, 1.0), (5.2, 1.2)]
    out = []
    for A_, Eg in pts:
        r = run(A_, Eg, 0.063, Wv=12.0, X=40.0)
        out.append(dict(A=A_, Eg=Eg, eps=r["eps"], F=r["F"], eps_RK=1.7 * Eg + 0.084 * A_ + 1.3, F_RK=-0.028 * Eg + 0.0015 * A_ + 0.14))
    return out

def _cal(v):
    kw = VARIANTS[v]
    A_ = calibrate_A(SI["eps"], SI["Eg"], SI["om0"], Wv=SI["Wv"], X=40.0, **kw)
    return v, A_, run(A_, SI["Eg"], SI["om0"], Wv=SI["Wv"], X=40.0, decomp=True, **kw)

def _job(args):
    key, kw = args
    if key[0] == "R": r = R(**kw)
    elif key[0] == "rk": r = run(**kw)
    elif key[0] == "run": r = run(**kw)
    return key, {k: r[k] for k in r}

if __name__ == "__main__":
    t0 = time.time(); out = {"variants": {}, "validation": {}, "unverified": {}, "predictions": {}}
    A = {}
    with Pool(3) as pool:
        for v, A_, r in pool.map(_cal, list(VARIANTS)):
            A[v] = A_; out["variants"][v] = dict(A=A_, kw=VARIANTS[v], Si=r); print(v, A_, r["F"], time.time() - t0, flush=True)
    # every remaining solver call, deduplicated, in parallel
    jobs = {}
    def want(key, kw): jobs.setdefault(key, kw)
    for table in (VAL, VAL_EXT, VAL_LIT):
        for k, (Eg, om, *_r) in table.items():
            for v, kw in VARIANTS.items(): want(("R", v, Eg, om, None), dict(A=A[v], Eg=Eg, om0=om, **kw))
    for k, (Eg, om, em, prov) in UNVER.items(): want(("R", "V0", Eg, om, None), dict(A=A["V0"], Eg=Eg, om0=om, **VARIANTS["V0"]))
    for k, (grp, Eg, om, prov, narrow) in PRED.items():
        for v, kw in VARIANTS.items(): want(("R", v, Eg, om, None), dict(A=A[v], Eg=Eg, om0=om, **kw))
        if narrow: want(("R", "V0", Eg, om, Eg), dict(A=A["V0"], Eg=Eg, om0=om, Wv=Eg, **VARIANTS["V0"]))
    for s_ in (1.1, 0.9): want(("run", "dFdA", s_), dict(A=s_ * A["V0"], Eg=SI["Eg"], om0=SI["om0"], Wv=SI["Wv"], X=40.0))
    for A_, Eg in [(3.0, 1.124), (5.2, 1.124), (7.0, 1.124), (5.2, 1.0), (5.2, 1.2)]:
        want(("rk", A_, Eg), dict(A=A_, Eg=Eg, om0=0.063, Wv=12.0, X=40.0))
    want(("run", "Ge_decomp"), dict(A=A["V0"], Eg=0.73, om0=0.037, X=60.0, decomp=True))
    items = sorted(jobs.items(), key=lambda kv: -(kv[1]["Eg"] ** 0 / min(kv[1]["om0"] / kv[1]["Eg"], 1)))   # slow (small w) first
    with Pool(4) as pool:
        RES = dict(pool.map(_job, items, chunksize=1))
    print("solves", len(RES), time.time() - t0, flush=True)
    def Rc(v, Eg, om, Wv=None): return RES[("R", v, Eg, om, Wv)]
    out["validation_ext"] = {}; out["validation_lit"] = {}
    for dest, table in (("validation", VAL), ("validation_ext", VAL_EXT), ("validation_lit", VAL_LIT)):
        for k, (Eg, om, em, elo, ehi, Fm, prov) in table.items():
            row = {}
            for v, kw in VARIANTS.items():
                r = Rc(v, Eg, om); row[v] = dict(eps=r["eps"], F=r["F"], lam=r["lam"], w=r["w"], w_nodes=r["w_nodes"], delta=r["delta"], N=r["N"])
            row.update(meas=em, lo=elo, hi=ehi, F_meas=Fm, prov=prov, resid=em / row["V0"]["eps"] - 1)
            out[dest][k] = row; print(k, row["V0"], em, time.time() - t0, flush=True)
    for k, (Eg, om, em, prov) in UNVER.items():
        r = Rc("V0", Eg, om); out["unverified"][k] = dict(eps=r["eps"], F=r["F"], meas=em, prov=prov)
    res = [row["resid"] for row in out["validation"].values()]
    rlo, rhi = min(res), max(res); out["resid_range"] = [rlo, rhi]
    out["resid_rms"] = (sum(x * x for x in res) / len(res)) ** 0.5; out["resid_mean"] = sum(res) / len(res)
    FSi = out["variants"]["V0"]["Si"]["F"]; fres = 0.119 / FSi - 1; out["F_resid_Si"] = fres
    out["F_Si_sigma"] = (0.119 - FSi) / 0.002
    ext = res + [row["resid"] for row in out["validation_ext"].values()]
    alls = ext + [row["resid"] for row in out["validation_lit"].values()]
    out["resid_all"] = dict(range=[min(alls), max(alls)], rms=(sum(x * x for x in alls) / len(alls)) ** 0.5, mean=sum(alls) / len(alls), n=len(alls))
    out["resid_ext"] = dict(range=[min(ext), max(ext)], rms=(sum(x * x for x in ext) / len(ext)) ** 0.5, mean=sum(ext) / len(ext), n=len(ext))
    # GaN-excluded variant and GaN at 8.9 (both quoted in sec. 2 for transparency)
    noG = [row["resid"] for kk, row in out["validation"].items() if kk != "GaN"]
    out["resid_noGaN"] = dict(range=[min(noG), max(noG)], rms=(sum(x * x for x in noG) / len(noG)) ** 0.5, mean=sum(noG) / len(noG), n=len(noG))
    out["GaN_8p9_resid"] = 8.9 / out["validation"]["GaN"]["V0"]["eps"] - 1
    # dF/dA at Si (V0 structure, B_h = 12 eV): central difference +-10%
    rp = RES[("run", "dFdA", 1.1)]; rm = RES[("run", "dFdA", 0.9)]
    out["Si_dFdA"] = (rp["F"] - rm["F"]) / (0.2 * A["V0"]); out["Si_F_pm10A"] = [rm["F"], rp["F"]]
    out["rk_slopes"] = [dict(A=A_, Eg=Eg, eps=RES[("rk", A_, Eg)]["eps"], F=RES[("rk", A_, Eg)]["F"], eps_RK=1.7 * Eg + 0.084 * A_ + 1.3,
                             F_RK=-0.028 * Eg + 0.0015 * A_ + 0.14) for A_, Eg in [(3.0, 1.124), (5.2, 1.124), (7.0, 1.124), (5.2, 1.0), (5.2, 1.2)]]
    out["table1"] = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "GAP-EF-v2", "data", "results.json")))["table1"]
    out["table1_note"] = "copied from GAP-EF-v2 (lam = 0: omega_0 never enters; h = 0.01, 0.005 commensurate with theta = 1, 3/2)"
    rg = RES[("run", "Ge_decomp")]; out["Ge_decomp"] = {k: rg[k] for k in ("eps", "F", "VR", "VP", "Cov2", "F_ren", "rbar")}
    out["Ge_decomp"]["eps_over_Eg"] = rg["eps_over_Eg"]
    for k, (grp, Eg, om, prov, narrow) in PRED.items():
        row = {}
        for v, kw in VARIANTS.items():
            r = Rc(v, Eg, om); row[v] = dict(eps=r["eps"], F=r["F"], lam=r["lam"], w=r["w"], w_nodes=r["w_nodes"], delta=r["delta"], N=r["N"])
        if narrow:
            r = Rc("V0", Eg, om, Eg); row["Wv"] = dict(eps=r["eps"], F=r["F"])
        e0, F0 = row["V0"]["eps"], row["V0"]["F"]
        es = [row[v]["eps"] for v in row]; Fs = [row[v]["F"] for v in row]
        slo, shi = max(0.0, 1 - min(es) / e0), max(0.0, max(es) / e0 - 1)
        dlo = (slo ** 2 + max(0.0, -rlo) ** 2) ** 0.5; dhi = (shi ** 2 + max(0.0, rhi) ** 2) ** 0.5
        Flo, Fhi = max(0.0, 1 - min(Fs) / F0), max(0.0, max(Fs) / F0 - 1)
        dFlo = (Flo ** 2 + fres ** 2) ** 0.5; dFhi = (Fhi ** 2 + fres ** 2) ** 0.5
        row.update(group=grp, Eg=Eg, om0=om, prov=prov, narrow=narrow,
                   eps=e0, eps_lo=e0 * (1 - dlo), eps_hi=e0 * (1 + dhi), F=F0, F_lo=F0 * (1 - dFlo), F_hi=F0 * (1 + dFhi))
        out["predictions"][k] = row; print(k, round(e0, 3), round(F0, 4), round(time.time() - t0), flush=True)
    os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"), exist_ok=True)
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "results.json"), "w"), indent=1, default=float)
    out["runtime_s"] = time.time() - t0
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "results.json"), "w"), indent=1, default=float)
    print("done", time.time() - t0)
