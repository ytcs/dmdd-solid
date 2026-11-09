"""GAP-EF-v3 compare.py: v2 -> v3 change of every number in data/results.json and data/scan.json that GAP-EF-v2(-errata) quotes.
Reads ../GAP-EF-v2/data/{results,scan}.json and data/{results,scan}.json; writes data/delta_v2_v3.json; prints the tables used in
returns/R17/GAP-EF-v3-errata.md.  No solver call (< 1 s)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
L = lambda d, f: json.load(open(os.path.join(HERE, d, f)))
J2, J3 = L(os.path.join("..", "GAP-EF-v2", "data"), "results.json"), L("data", "results.json")
S2, S3 = L(os.path.join("..", "GAP-EF-v2", "data"), "scan.json"), L("data", "scan.json")
rel = lambda a, b: b / a - 1
out = dict(variants={}, validation={}, predictions={}, stats={}, scan={}, misc={})
print("== calibration (Si)")
for v in ("V0", "V1", "V3"):
    a, b = J2["variants"][v], J3["variants"][v]
    d = dict(A2=a["A"], A3=b["A"], dA=rel(a["A"], b["A"]), F2=a["Si"]["F"], F3=b["Si"]["F"], dF=rel(a["Si"]["F"], b["Si"]["F"]))
    for k in ("VR", "VP", "Cov2", "F_ren", "rbar", "carriers_per_pair"):
        d[k + "2"], d[k + "3"] = a["Si"][k], b["Si"][k]
    out["variants"][v] = d
    print(v, f"A {a['A']:.4f} -> {b['A']:.4f} ({100*d['dA']:+.3f}%)  F {a['Si']['F']:.5f} -> {b['Si']['F']:.5f} ({100*d['dF']:+.3f}%)",
          " ".join(f"{k} {a['Si'][k]:.4f}->{b['Si'][k]:.4f}" for k in ("VR", "VP", "Cov2", "F_ren", "rbar")))
print("== validation rows: eps V0 (V1, V3), F V0, residual")
for blk in ("validation", "validation_ext", "validation_lit", "unverified"):
    for k in J2[blk]:
        a, b = J2[blk][k], J3[blk][k]
        if blk == "unverified":
            out["validation"][k] = dict(eps2=a["eps"], eps3=b["eps"], deps=rel(a["eps"], b["eps"]), F2=a["F"], F3=b["F"], dF=rel(a["F"], b["F"]))
            print(f"{k:8s} eps {a['eps']:.4f}->{b['eps']:.4f} ({100*rel(a['eps'], b['eps']):+.3f}%) F {a['F']:.5f}->{b['F']:.5f}")
            continue
        row = {v: dict(eps2=a[v]["eps"], eps3=b[v]["eps"], deps=rel(a[v]["eps"], b[v]["eps"]), F2=a[v]["F"], F3=b[v]["F"], dF=rel(a[v]["F"], b[v]["F"]),
                       N2=a[v]["N"], N3=b[v]["N"], woff_v2=a[v]["w_eff"] / a[v]["w"] - 1) for v in ("V0", "V1", "V3")}
        row.update(resid2=a["resid"], resid3=b["resid"], dresid_pts=100 * (b["resid"] - a["resid"]), blk=blk)
        out["validation"][k] = row
        print(f"{k:8s}", " ".join(f"{v}: {row[v]['eps2']:.4f}->{row[v]['eps3']:.4f} ({100*row[v]['deps']:+.3f}%) F {100*row[v]['dF']:+.3f}% N {row[v]['N2']}->{row[v]['N3']};"
                                   for v in ("V0", "V1", "V3")), f"resid {100*a['resid']:+.2f}% -> {100*b['resid']:+.2f}%")
print("== statistics")
for k in ("resid_range", "resid_rms", "resid_mean", "F_resid_Si", "F_Si_sigma", "GaN_8p9_resid", "Si_dFdA"):
    out["stats"][k] = (J2[k], J3[k]); print(k, J2[k], "->", J3[k])
for k in ("resid_all", "resid_ext", "resid_noGaN"):
    out["stats"][k] = (J2[k], J3[k]); print(k, J2[k], "->", J3[k])
print("== predictions: eps (band), F (band)")
for k in J2["predictions"]:
    a, b = J2["predictions"][k], J3["predictions"][k]
    d = {q: (a[q], b[q], rel(a[q], b[q])) for q in ("eps", "eps_lo", "eps_hi", "F", "F_lo", "F_hi")}
    d["V1_N"] = (a["V1"]["N"], b["V1"]["N"])
    out["predictions"][k] = d
    print(f"{k:8s} eps {a['eps']:.3f} ({a['eps_lo']:.2f}-{a['eps_hi']:.2f}) -> {b['eps']:.3f} ({b['eps_lo']:.2f}-{b['eps_hi']:.2f}) [{100*d['eps'][2]:+.3f}%, lo {100*d['eps_lo'][2]:+.3f}%, hi {100*d['eps_hi'][2]:+.3f}%]"
          f"  F {a['F']:.4f} ({a['F_lo']:.3f}-{a['F_hi']:.3f}) -> {b['F']:.4f} ({b['F_lo']:.3f}-{b['F_hi']:.3f}) [{100*d['F'][2]:+.3f}%]")
out["max_abs_deps_pred"] = max(abs(d["eps"][2]) for d in out["predictions"].values())
out["max_abs_dF_pred"] = max(abs(d["F"][2]) for d in out["predictions"].values())
print("max |d eps/eps| pred", out["max_abs_deps_pred"], "max |dF/F| pred", out["max_abs_dF_pred"])
print("== rk_slopes, Ge_decomp")
for p2, p3 in zip(J2["rk_slopes"], J3["rk_slopes"]):
    print(p2["A"], p2["Eg"], f"eps {p2['eps']:.4f}->{p3['eps']:.4f} F {p2['F']:.5f}->{p3['F']:.5f}")
out["misc"]["rk"] = [(p2, p3) for p2, p3 in zip(J2["rk_slopes"], J3["rk_slopes"])]
out["misc"]["Ge_decomp"] = (J2["Ge_decomp"], J3["Ge_decomp"])
print("Ge", {k: (round(J2["Ge_decomp"][k], 5), round(J3["Ge_decomp"][k], 5)) for k in J2["Ge_decomp"]})
print("== scan fits")
for k in ("p_eps", "p_F", "eps_fit_maxrel", "eps_fit_rms", "F_fit_maxrel", "F_fit_rms"):
    out["scan"][k] = (S2[k], S3[k]); print(k, S2[k], "->", S3[k])
rows2 = {(r["lam"], r["w"]): r for r in S2["rows"]}
dd = [(r["lam"], r["w"], rel(rows2[(r["lam"], r["w"])]["e"], r["e"]), rel(rows2[(r["lam"], r["w"])]["F"], r["F"])) for r in S3["rows"]]
out["scan"]["max_row_de"] = max(abs(x[2]) for x in dd); out["scan"]["max_row_dF"] = max(abs(x[3]) for x in dd)
print("scan rows max |de/e|", out["scan"]["max_row_de"], "max |dF/F|", out["scan"]["max_row_dF"])
json.dump(out, open(os.path.join(HERE, "data", "delta_v2_v3.json"), "w"), indent=1, default=float)

# ---- printed-precision changes (the digits GAP-EF-v2 sec. 2, sec. 3 tables and sec. 1.6 / 1.7 print)
print("== printed-precision changes")
f2 = lambda x: f"{x:.2f}"; f3 = lambda x: f"{x:.3f}"; f4 = lambda x: f"{x:.4f}"
chg = []
for k in J2["predictions"]:
    a, b = J2["predictions"][k], J3["predictions"][k]
    for q, fm in (("eps", f2), ("eps_lo", f2), ("eps_hi", f2), ("F", f3), ("F_lo", f3), ("F_hi", f3)):
        if fm(a[q]) != fm(b[q]): chg.append(("sec3", k, q, fm(a[q]), fm(b[q])))
    if f2(a["eps"] / a["Eg"]) != f2(b["eps"] / b["Eg"]): chg.append(("sec3", k, "eps/Eg", f2(a["eps"] / a["Eg"]), f2(b["eps"] / b["Eg"])))
for blk in ("validation", "validation_ext", "validation_lit"):
    for k in J2[blk]:
        a, b = J2[blk][k], J3[blk][k]
        for v in ("V0", "V1", "V3"):
            if f2(a[v]["eps"]) != f2(b[v]["eps"]): chg.append(("sec2", k, v + " eps", f2(a[v]["eps"]), f2(b[v]["eps"])))
        if f3(a["V0"]["F"]) != f3(b["V0"]["F"]): chg.append(("sec2", k, "F V0", f3(a["V0"]["F"]), f3(b["V0"]["F"])))
        if f"{100*a['resid']:.1f}" != f"{100*b['resid']:.1f}": chg.append(("sec2", k, "resid %", f"{100*a['resid']:.1f}", f"{100*b['resid']:.1f}"))
a, b = J2["unverified"]["GaAs"], J3["unverified"]["GaAs"]
if f2(a["eps"]) != f2(b["eps"]): chg.append(("sec2", "GaAs", "eps", f2(a["eps"]), f2(b["eps"])))
for v, lab in (("V0", "Si V0"), ("V1", "Si V1"), ("V3", "Si V3")):
    a, b = J2["variants"][v]["Si"], J3["variants"][v]["Si"]
    for q in ("VR", "VP", "Cov2", "F", "F_ren", "rbar"):
        if f4(a[q]) != f4(b[q]): chg.append(("sec1.6", lab, q, f4(a[q]), f4(b[q])))
    if f3(a["eps_over_Eg"]) != f3(b["eps_over_Eg"]): chg.append(("sec1.6", lab, "eps/Eg", f3(a["eps_over_Eg"]), f3(b["eps_over_Eg"])))
a, b = J2["Ge_decomp"], J3["Ge_decomp"]
for q in ("VR", "VP", "Cov2", "F", "F_ren", "rbar"):
    if f4(a[q]) != f4(b[q]): chg.append(("sec1.6", "Ge", q, f4(a[q]), f4(b[q])))
if f3(a["eps_over_Eg"]) != f3(b["eps_over_Eg"]): chg.append(("sec1.6", "Ge", "eps/Eg", f3(a["eps_over_Eg"]), f3(b["eps_over_Eg"])))
for p2, p3 in zip(J2["rk_slopes"], J3["rk_slopes"]):
    if f3(p2["eps"]) != f3(p3["eps"]): chg.append(("sec1.7", (p2["A"], p2["Eg"]), "eps", f3(p2["eps"]), f3(p3["eps"])))
    if f4(p2["F"]) != f4(p3["F"]): chg.append(("sec1.7", (p2["A"], p2["Eg"]), "F", f4(p2["F"]), f4(p3["F"])))
K2 = {(p["A"], p["Eg"]): p for p in J2["rk_slopes"]}; K3 = {(p["A"], p["Eg"]): p for p in J3["rk_slopes"]}
for K, tag in ((K2, "v2"), (K3, "v3")):
    print(tag, "secants: deps/dA %.4f dF/dA %.5f deps/dEg %.3f dF/dEg %.4f" % ((K[(7.0, 1.124)]["eps"] - K[(3.0, 1.124)]["eps"]) / 4,
          (K[(7.0, 1.124)]["F"] - K[(3.0, 1.124)]["F"]) / 4, (K[(5.2, 1.2)]["eps"] - K[(5.2, 1.0)]["eps"]) / 0.2, (K[(5.2, 1.2)]["F"] - K[(5.2, 1.0)]["F"]) / 0.2))
for c in chg: print(*c)
out["printed_changes"] = chg
json.dump(out, open(os.path.join(HERE, "data", "delta_v2_v3.json"), "w"), indent=1, default=float)

# ---- derived quantities quoted in the errata (R&K deviations, scan F range, k2 exponent)
print("== derived")
for tag, J_ in (("v2", J2), ("v3", J3)):
    rk = J_["rk_slopes"]; K = {(p["A"], p["Eg"]): p for p in rk}
    de = [p["eps"] / p["eps_RK"] - 1 for p in rk]; dF = [p["F"] / p["F_RK"] - 1 for p in rk]
    sl = [((K[(7.0, 1.124)]["eps"] - K[(3.0, 1.124)]["eps"]) / 4) / 0.084 - 1, ((K[(7.0, 1.124)]["F"] - K[(3.0, 1.124)]["F"]) / 4) / 0.0015 - 1,
          ((K[(5.2, 1.2)]["eps"] - K[(5.2, 1.0)]["eps"]) / 0.2) / 1.7 - 1, ((K[(5.2, 1.2)]["F"] - K[(5.2, 1.0)]["F"]) / 0.2) / -0.028 - 1]
    print(tag, "RK point dev eps", [f"{100*x:+.2f}" for x in de], "F", [f"{100*x:+.2f}" for x in dF], "slopes", [f"{100*x:+.1f}" for x in sl],
          "dF/dEg terms", K[(5.2, 1.2)]["F"], K[(5.2, 1.0)]["F"])
for tag, S_ in (("v2", S2), ("v3", S3)):
    Fs = [r["F"] for r in S_["rows"]]; pe = S_["p_eps"]
    print(tag, "scan F range", min(Fs), max(Fs), "k2 exponent 1-(3+g)b", 1 - (3 + pe[2]) * pe[3], "rounded", 1 - (3 + round(pe[2], 3)) * round(pe[3], 4),
          "k2(Si)", pe[1] * ((J2 if tag == 'v2' else J3)["variants"]["V0"]["A"] * 0.063 ** pe[2]) ** pe[3] * 1.164 ** (1 - (3 + pe[2]) * pe[3]))

# ---- markdown rows for the replacement tables (sec. 3 table and sec. 2 model columns), v3 values, v2 formats
def sig(x, n=2):
    from math import log10, floor
    d = n - 1 - int(floor(log10(abs(x)))); d = max(d, 0); return f"{x:.{d}f}"
print("== md sec3")
for k, b in J3["predictions"].items():
    lam = b["V0"]["lam"]; lam_s = f"{lam:.0f}" if lam > 100 else (f"{lam:.3g}" if lam >= 1 else sig(lam, 2))
    print(f"| {k} | {b['Eg']} | {lam_s} | {b['V0']['w']:.4f} | {b['eps']:.2f} ({b['eps_lo']:.2f}–{b['eps_hi']:.2f}) | {b['eps']/b['Eg']:.2f} | {b['F']:.3f} ({b['F_lo']:.3f}–{b['F_hi']:.3f}) |")
print("== md sec2 model columns")
for blk in ("validation", "validation_ext", "validation_lit"):
    for k, b in J3[blk].items():
        print(f"| {k} | {b['V0']['eps']:.2f} ({b['V1']['eps']:.2f}, {b['V3']['eps']:.2f}) | {100*b['resid']:+.1f}% | {b['V0']['F']:.3f} |")
print("GaAs", f"{J3['unverified']['GaAs']['eps']:.2f}", f"{100*(4.2/J3['unverified']['GaAs']['eps']-1):+.1f}%", f"{J3['unverified']['GaAs']['F']:.3f}")
