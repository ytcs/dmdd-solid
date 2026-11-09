"""DC-41 production: tables on the WP4 [4.2] grid y in [2, 50], Q = q v_F/Delta in [y v_F/v_max, 10^3] (v_max/v_F = 0.39, CW4 sec. 8).  Writes data/table_grid.csv, data/edge_table.csv,
data/threshold.csv, data/scaling.csv, data/al_corrections.csv, data/summary.json.  L ratios are formed from Im and the KK Re (q << k_TF: eps = -(k_TF^2/q^2) P)."""
import csv, json, os, time
import numpy as np
import bcs1d as b, kk
H = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(H, "data")
R = 0.39
YS = [2.02, 2.05, 2.1, 2.2, 2.35, 2.5, 2.75, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 40, 50]
QG = list(np.round(np.geomspace(5.0, 1000.0, 25), 3))
EDGE5 = [2.2, 2.5, 3, 5, 10]
CW4 = {2.2: (4.01, 1.42, 0.33, 0.40), 2.5: (2.82, 0.88, 0.45, 0.54), 3: (2.03, 0.53, 0.58, 0.66), 5: (1.05, 0.16, 0.80, 0.86), 10: (0.50, 0.04, 0.94, 0.96)}

def Lof(P):
    return -P.imag / (P.real ** 2 + P.imag ** 2)

def row(y, Q, S):
    p, g = b.Pg(y, Q)
    p2, g2 = b.Pg(y, Q, n=24, refine=2)
    nr = b.pnor(y, Q)
    gi = float(b.gI(y))
    kb, kg = S.kk(y, "bare"), S.kk(y, "grpa")
    Pb, Pgk = complex(kb, p.imag), complex(kg, g.imag)
    v = g.imag / p.imag - 1
    v2 = g2.imag / p2.imag - 1
    Ln = Lof(nr)
    sb, sg = Q * (-p.real + nr.real), Q * (-g.real + nr.real)     # direct Re: Q multiplies the 1e-6 KK quadrature offset; KK enters L and the KK check
    return dict(y=y, Q=Q, x=y / Q, g_I=gi, Im_bare_over_nor=p.imag / nr.imag, Im_grpa_over_nor=g.imag / nr.imag, v_GRPA=v, dv_doubling=abs(v - v2),
                ReP_nor=nr.real, ReP_bare=p.real, ReP_grpa=g.real, KKerr_bare=kb - p.real, KKerr_grpa=kg - g.real,
                s_eff_bare=sb, s_eff_grpa=sg, L_bare_over_gLnor=Lof(Pb) / (gi * Ln), L_grpa_over_gLnor=Lof(Pgk) / (gi * Ln), L_grpa_over_Lnor=Lof(Pgk) / Ln, L_bare_over_Lnor=Lof(Pb) / Ln)

def main():
    t0 = time.time(); rows = []
    Sp = {}
    def spec(Q):
        if Q not in Sp: Sp[Q] = kk.Spec(Q)
        return Sp[Q]
    for Q in QG:
        for y in YS:
            if Q >= y / R: rows.append(row(y, Q, spec(Q)))
    print("grid", len(rows), time.time() - t0, flush=True)
    edge = []
    for y in sorted(set(YS + EDGE5)):
        Q = y / R; S = kk.Spec(Q); r = row(y, Q, S)
        r["s_BCS_inf"] = b.s_bcs(y); r["s_BCS_cut"] = b.s_bcs(y, Y=Q)
        rr = np.pi / 2 * R / (1 - R / 2 * np.log((1 + R) / (1 - R))); ReL = 1 - R / 2 * np.log((1 + R) / (1 - R)); gi = r["g_I"]
        for lab, s in (("inf", r["s_BCS_inf"]), ("cut", r["s_BCS_cut"])):
            d = R * s / y / ReL
            r["eq81_" + lab] = (1 + rr ** 2) / ((1 + d) ** 2 + gi ** 2 * rr ** 2)
        r["w_AB"] = S.wab; r["Z_AB"] = S.Z; r["ABfrac_fsum"] = np.pi * S.Z * S.wab / (np.pi * Q * Q / 6)
        edge.append(r); rows.append({k: r[k] for k in rows[0]})
    print("edge", time.time() - t0, flush=True)
    rows.sort(key=lambda r: (r["y"], r["Q"]))
    with open(os.path.join(D, "table_grid.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader()
        for r in rows: w.writerow({k: ("%.7g" % v) for k, v in r.items()})
    with open(os.path.join(D, "edge_table.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(edge[0])); w.writeheader()
        for r in edge: w.writerow({k: ("%.7g" % v) for k, v in r.items()})
    # threshold approach y -> 2+
    th = []
    for Q in (5.2, 12.8, 100.0, 1000.0):
        for k in range(1, 11):
            y = 2 + 10.0 ** -k
            p, g = b.Pg(y, Q); nr = b.pnor(y, Q); gi = float(b.gI(y))
            th.append(dict(Q=Q, y_minus_2=10.0 ** -k, g_I=gi, ReP_bare=p.real, ImP_bare=p.imag, ReP_grpa=g.real, ImP_grpa=g.imag, L_bare_over_Lnor=Lof(p) / Lof(nr), L_grpa_over_Lnor=Lof(g) / Lof(nr)))
    with open(os.path.join(D, "threshold.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(th[0])); w.writeheader()
        for r in th: w.writerow({k: ("%.7g" % v) for k, v in r.items()})
    # scaling of the vertex with Q: magnitude ratio |P~ - P33|/|P33| and Im fraction v, vs 1/Q^2 and 1/(Q ln Q)
    sc = []
    for y in (2.2, 3, 5, 10, 30):
        for Q in (y / R, 30, 100, 300, 1000, 3000, 10000):
            if Q < y / R: continue
            p, g = b.Pg(y, Q)
            C, F, KF = b.avgs(y, Q)
            sc.append(dict(y=y, Q=Q, v=g.imag / p.imag - 1, mag=abs(g - p) / abs(p), v_QlnQ=(g.imag / p.imag - 1) * Q * np.log(Q), mag_Q2=abs(g - p) / abs(p) * Q * Q, KF_re=KF.real, KF_im=KF.imag))
    with open(os.path.join(D, "scaling.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(sc[0])); w.writeheader()
        for r in sc: w.writerow({k: ("%.7g" % v) for k, v in r.items()})
    # Al corrections dropped by the quasiclassical table: q^2/2m shift of s; the "1" of eps (q << k_TF).  Delta 0.18 meV [E, CONVENTIONS row 33], E_F 11.7 eV, v_F 6.8e-3 (WP4 sec. 4.3)
    Dl, EF, vF = 0.18e-3, 11.7, 6.8e-3
    me = 0.51099895e6; kF = np.sqrt(2 * me * EF); kTF = np.sqrt(4 * me * kF / (np.pi * 137.036))
    al = []
    for y, Q in ((2.2, 2.2 / R), (3, 3 / R), (10, 10 / R), (5, 100.0), (50, 50 / R), (5, 1000.0), (50, 1000.0)):
        dq = Q * Q * Dl / (4 * EF)
        p0, g0 = b.Pg(y, Q); p1, g1 = b.Pg(y, Q, dq=dq)
        q = Q * Dl / vF
        pref = (kTF / q) ** 2
        e_with = 1 - pref * g0; e_wo = -pref * g0
        al.append(dict(y=y, Q=Q, q_eV=q, omega_meV=y * Dl * 1e3, dq_over_Delta=dq, rel_dP_grpa=abs(g1 - g0) / abs(g0), rel_dL_grpa=abs(Lof(g1) / Lof(g0) - 1), rel_dL_eps1=abs(Lof(-e_with) * 1 / (Lof(-e_wo)) - 1)))
    with open(os.path.join(D, "al_corrections.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(al[0])); w.writeheader()
        for r in al: w.writerow({k: ("%.7g" % v) for k, v in r.items()})
    dm = np.array([[r["v_GRPA"], r["dv_doubling"], abs(r["KKerr_grpa"]), abs(r["KKerr_bare"]), r["L_grpa_over_gLnor"], r["L_bare_over_gLnor"], r["y"], r["Q"]] for r in rows])
    S = dict(n_rows=len(rows), v_max=float(dm[:, 0].max()), v_min=float(dm[:, 0].min()), dv_doubling_max=float(dm[:, 1].max()), KKerr_grpa_max=float(dm[:, 2].max()), KKerr_bare_max=float(dm[:, 3].max()),
             L_grpa_ratio_range=[float(dm[:, 4].min()), float(dm[:, 4].max())], L_bare_ratio_range=[float(dm[:, 5].min()), float(dm[:, 5].max())], kTF_eV=kTF, kF_eV=kF, runtime_s=time.time() - t0)
    json.dump(S, open(os.path.join(D, "summary.json"), "w"), indent=1)
    print(S)
    for r in edge:
        if r["y"] in EDGE5: print({k: round(float(r[k]), 4) for k in ("y", "Q", "g_I", "v_GRPA", "s_BCS_inf", "s_BCS_cut", "s_eff_bare", "s_eff_grpa", "eq81_inf", "eq81_cut", "L_bare_over_gLnor", "L_grpa_over_gLnor", "w_AB", "ABfrac_fsum")})

if __name__ == "__main__":
    main()
