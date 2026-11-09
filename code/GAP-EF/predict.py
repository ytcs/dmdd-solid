"""GAP-EF predict.py: calibration (A on Si eps_eh only), validation against measured (eps_eh, F_eh), predictions for the
WP8-U survivors lacking data. Writes data/results.json (read by checks.py and quoted in returns/R14/GAP-EF.md).
Run: python3 -I predict.py   (deterministic quadrature, no Monte Carlo; ~10-20 min)."""
import json, os, sys, time
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
 "GaN":  (3.43, 0.0889, 8.9, 8.9, 9.59, None, "E_g, omega_O_max [FT 1910.10716 Table I p.2 via WP8-U CSV]; eps 8.9, 9.59 (EBIC) [FT 2308.03893 pp.18-19]"),
 "SiO2": (9.2, 0.149, 18.0, 16.4, 18.0, None, "E_g, omega_O_max (alpha-quartz) [FT 1910.10716 Table I p.2 via WP8-U CSV]; eps 18.0 (one sample 16.4), 1975 oxide data [FT 2610.16949 p.8]"),
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
    return run(X=X, Nmax=300, nwmin=1, **k)

if __name__ == "__main__":
    t0 = time.time(); out = {"variants": {}, "validation": {}, "unverified": {}, "predictions": {}}
    A = {}
    for v, kw in VARIANTS.items():
        A[v] = calibrate_A(SI["eps"], SI["Eg"], SI["om0"], Wv=SI["Wv"], X=40.0, **kw)
        r = run(A[v], SI["Eg"], SI["om0"], Wv=SI["Wv"], X=40.0, decomp=True, **kw)
        out["variants"][v] = dict(A=A[v], kw=kw, Si=r); print(v, A[v], r["F"], time.time() - t0, flush=True)
    for k, (Eg, om, em, elo, ehi, Fm, prov) in VAL.items():
        row = {}
        for v, kw in VARIANTS.items():
            r = R(A=A[v], Eg=Eg, om0=om, **kw); row[v] = dict(eps=r["eps"], F=r["F"], lam=r["lam"], w=r["w"], N=r["N"])
        row.update(meas=em, lo=elo, hi=ehi, F_meas=Fm, prov=prov, resid=em / row["V0"]["eps"] - 1)
        out["validation"][k] = row; print(k, row["V0"], em, time.time() - t0, flush=True)
    for k, (Eg, om, em, prov) in UNVER.items():
        r = R(A=A["V0"], Eg=Eg, om0=om, **VARIANTS["V0"]); out["unverified"][k] = dict(eps=r["eps"], F=r["F"], meas=em, prov=prov)
    res = [row["resid"] for row in out["validation"].values()]
    rlo, rhi = min(res), max(res); out["resid_range"] = [rlo, rhi]
    out["resid_rms"] = (sum(x * x for x in res) / len(res)) ** 0.5; out["resid_mean"] = sum(res) / len(res)
    FSi = out["variants"]["V0"]["Si"]["F"]; fres = 0.119 / FSi - 1; out["F_resid_Si"] = fres
    for k, (grp, Eg, om, prov, narrow) in PRED.items():
        row = {}
        for v, kw in VARIANTS.items():
            r = R(A=A[v], Eg=Eg, om0=om, **kw); row[v] = dict(eps=r["eps"], F=r["F"], lam=r["lam"], w=r["w"], N=r["N"])
        if narrow:
            r = R(A=A["V0"], Eg=Eg, om0=om, Wv=Eg, **VARIANTS["V0"]); row["Wv"] = dict(eps=r["eps"], F=r["F"])
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
    print("done", time.time() - t0)
