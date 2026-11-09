"""DC-67 checks (CW7 C5-C8 on the new two-table solver, the commensurate-grid and Gaussian-match pitfalls, the old-vs-new Si numbers, independent MC of the full N distribution).
Run: python checks.py > data/checks_stdout.txt.  Reads data/library_summary.csv, data/conv_h.csv (from conv.py).  All imports from this directory's copies."""
import csv, json, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, "src_copies")]
import casc2
import build_library as BL
from cascade import Cascade
from model import run, lagrange, nodes
from cascade_gf import CascadeGF, moments_fast, pmf_from_gf, commensurate_h
import mc as MC
res = []; OUT = {}
def chk(name, ok, info=""):
    res.append(bool(ok)); print(("PASS " if ok else "FAIL ") + name + " | " + str(info), flush=True)
def sl(x, y, lo):
    s = x > lo; return np.polyfit(x[s], y[s], 1)[0]

# ---- C5: p.g.f. solver = moment recursion (two-table, asymmetric DOS, theta 3/2, a = 1), sum P, P >= 0
o = []
for lab, kw in (("Si V0 W", dict(lam=3.5431, N=74, w=4 / 74, W=12 / 1.164, a=.5, theta=1.0)), ("V1 W", dict(lam=3.4988, N=74, w=4 / 74, W=12 / 1.164, a=.5, theta=1.5)) if False else ("V1 even", dict(lam=3.4988, N=74, w=4 / 74, W=12 / 1.164, a=.5, theta=1.5)),
                ("V3", dict(lam=.45, N=74, w=4 / 74, W=None, a=1.0, theta=1.0)), ("narrow", dict(lam=.04, N=98, w=2 / 98, W=1.0, a=.5, theta=1.0))):
    x, G = casc2.solve_gf(kw["lam"], kw["w"], 14.0, kw["N"], 32, a=kw["a"], W=kw["W"], theta=kw["theta"])
    c = Cascade(kw["lam"], kw["w"], X=14.0, h=1 / kw["N"], a=(kw["a"], kw["a"]), W=(None, kw["W"]), theta=(kw["theta"],) * 2, sets=("N",))
    m, s = c.res["N"]; n = np.arange(32); e = 0; e2 = 0; se = 0; mn = 0
    for t in (0, 1):
        P = casc2.pmf(G[t]); sel = x <= (kw["W"] or 1e9) if t == 1 else x < 99
        e = max(e, np.abs(P @ n - m[t])[sel].max()); e2 = max(e2, np.abs(P @ (n * n) - s[t])[sel].max()); se = max(se, np.abs(P.sum(1) - 1).max()); mn = min(mn, P.min())
    o.append((lab, "%.1e %.1e %.1e %.1e" % (e, e2, se, mn)))
    ok_ = e < 1e-9 and e2 < 1e-9 and se < 1e-12 and mn > -1e-13
    chk("C5 %s: G'(1), G''(1) = cascade.py moments to 1e-9; sum P = 1; P >= 0" % lab, ok_, o[-1])

# ---- equals the CW7 symmetric solver
Nz = 32; zs = np.exp(2j * np.pi * np.arange(Nz) / Nz)
gf = CascadeGF(X=8.0, h=0.002, a=0.5, lam=3.55, w=0.054, theta=1.5, zs=zs); Gc = gf.solve_gf()
x, G = casc2.solve_gf(3.55, 0.054, 8.0, 500, Nz, a=.5, W=None, theta=1.5)
dP = np.abs(pmf_from_gf(Gc[-1], zs) - casc2.pmf(G[0][-1])).max()
chk("C5b casc2 (W = None) = CW7 cascade_gf (fixed) at x = 8, theta 3/2, h = 0.002", dP < 1e-12, dP)

# ---- commensurate-grid guard
def raises(f):
    try: f(); return False
    except ValueError: return True
chk("G1 guard raises on h = 0.02, w = 0.054; on theta 3/2, N = 79", raises(lambda: casc2.check_grid(0.02, 0.054, 1.0)) and raises(lambda: casc2.check_grid(1 / 79, 4 / 79, 1.5)))

# ---- C6: lam -> 0, Richardson O(h) (GAP-EF-v2 sec. 1.6)
ce = []
for h in (0.02, 0.01):
    x, m, s = moments_fast(X=40.0, h=h, a=0.5, lam=0.0, w=0.054)
    sm = sl(x, m, 20); ce.append((1 / sm, sl(x, s - m ** 2, 20) / sm))
c0 = 2 * ce[1][0] - ce[0][0]; F0 = 2 * ce[1][1] - ce[0][1]
chk("C6 lam -> 0: eps/E_g Richardson 1.585, F 0.081 (CW7-C6)", abs(c0 - 1.585) < 6e-4 and abs(ce[1][1] - 0.081) < 6e-4, (round(c0, 4), round(F0, 4), round(ce[1][1], 4)))

# ---- C7 and the "+1.3%": CW7 Si case lam 3.55, w 0.054, theta 1, X 40 (symmetric DOS, no W_v)
tab = []
for h, st in ((0.02, False), (0.01, False), (0.002, True), (0.001, True)):
    x, m, s = moments_fast(X=40.0, h=h, a=0.5, lam=3.55, w=0.054, strict=st)
    sm = sl(x, m, 20); tab.append(dict(h=h, w_eff=max(1, round(.054 / h)) * h, eps_over_Eg=1 / sm, F=sl(x, s - m ** 2, 20) / sm))
    print("   ", tab[-1], flush=True)
OUT["C7"] = tab
bias = tab[0]["eps_over_Eg"] / tab[2]["eps_over_Eg"] - 1
chk("C7 CW7 case: h = 0.02 eps/E_g 3.2610, F 0.1147; h = 0.002 eps/E_g 3.2185, F 0.1139; bias +1.3%", abs(tab[0]["eps_over_Eg"] - 3.2610) < 2e-3 and abs(tab[2]["eps_over_Eg"] - 3.2185) < 2e-3 and abs(tab[2]["F"] - .1139) < 2e-4 and abs(bias - .0132) < .002, "bias %+.3f%%" % (100 * bias))
# the same on the two-table GAP-EF physics: v3 production, grounding run
A0 = BL.A["V0"]; r = run(A0, 1.164, 0.063, Wv=12.0, X=40.0)
chk("V3 grounding: model.run copy at A = 5.5878: eps 3.749, F 0.11384", abs(r["eps"] - 3.749) < 2e-4 and abs(r["F"] - .11384) < 2e-5, (r["eps"], r["F"], r["N"]))
OUT["v3_Si"] = dict(eps=r["eps"], F=r["F"], N=r["N"])

# ---- C8: seeds
x, G = casc2.solve_gf(3.5431, 4 / 74, 12.0, 74, 32, W=12 / 1.164)
Pe, Ph = casc2.pmf(G[0]), casc2.pmf(G[1]); n = np.arange(32); o = 0; p0 = 0
for ie, ih in ((300, 150), (740, 40), (10, 20), (500, 500)):
    P = casc2.compose(Pe[ie], Ph[ih]); nn = np.arange(P.size)
    o = max(o, abs(P @ nn - (1 + Pe[ie] @ n + Ph[ih] @ n))); p0 = max(p0, abs(P[0]))
Pb = casc2.compose(Pe[10], Ph[20])
chk("C8 <N|L> = 1 + m(x_e) + m(x_h); P(0|L) = 0; P = delta_{N,1} below threshold", o < 1e-11 and p0 == 0 and abs(Pb[1] - 1) < 1e-13, "%.1e" % o)

# ---- N_z doubling (aliasing), X dependence of tables
o = []
for mat in ("Si", "Ge", "InSb", "LiF"):
    M = BL.materials()[mat]; cfg = dict(BL.configs(M))["m1"]
    r1 = BL.solve_cfg(M, cfg, Nz=32); r2 = BL.solve_cfg(M, cfg, Nz=64)
    o.append((mat, float(np.abs(r1["Pe"] - r2["Pe"][:, :32]).max()), r1["X"]))
chk("Nz doubling 32 -> 64: max|dP| < 1e-10", max(a[1] for a in o) < 1e-10, o)

# ---- omega_0 interpolation: 2 / 3 / 5 nodes at fixed N; exact commensurate Si (w = 21/388)
M = BL.materials(); o = []
for mat in ("Si", "3C-SiC", "CsI"):
    m = M[mat]; cfg = dict(BL.configs(m))["m1"]; w = m["om"] / m["Eg"]
    N = BL.grid(w, nwmin=1)[0]; c = int(round(w * N)); X = 12.0
    cand = sorted(range(max(1, c - 5), c + 6), key=lambda k: (abs(k - w * N), k))
    P = {k: BL.solve_cfg(m, cfg, N=N, X=X, Nz=32, ks=sorted(cand[:k]))["Pe"] for k in (2, 3, 5)}
    o.append((mat, N, c, "%.2e" % np.abs(P[3] - P[5]).max(), "%.2e" % np.abs(P[2] - P[5]).max(), "%.2e" % P[3].min()))
print("    REJECTED node interpolation of P, for the record: (material, N, n_w, 3v5 nodes, 2v5 nodes, min P)", o)
m = M["Si"]; cfg = dict(BL.configs(m))["m1"]
lam = cfg["A"] / m["Eg"] ** 3; w = m["om"] / m["Eg"]; W = 12 / 1.164
xs_ = np.arange(1, 81) * .25
tabx = lambda r_: np.stack([np.interp(xs_, r_["x"], r_["Pe"][:, n]) for n in range(32)], 1)
ri = tabx(BL.solve_cfg(m, cfg, N=388, X=20.0, Nz=32, ks=[21]))      # exact commensurate, no mixture
rf = tabx(BL.solve_cfg(m, cfg, N=370, X=20.0, Nz=32))               # convex read, w N = 20.03
rj = tabx(BL.solve_cfg(m, cfg, N=74, X=20.0, Nz=32))
OUT["Si_exact_vs_frac370"] = float(np.abs(ri - rf).max()); OUT["Si_exact_vs_prod74"] = float(np.abs(ri - rj).max())
chk("W2 convex read = exact-commensurate Si (w = 21/388): N 370 vs 388 < 1e-3; production N 74 vs 388 reported", OUT["Si_exact_vs_frac370"] < 1e-3, (OUT["Si_exact_vs_frac370"], OUT["Si_exact_vs_prod74"]))

# ---- Gaussian match beyond X (CW7-errata 1.4: changes P by < 1e-6)
r = BL.solve_cfg(m, cfg, N=74, X=40.0, Nz=32); x = r["x"]; e, F, b = BL.asym(x, r["Pe"]); n = np.arange(32)
gp = []
for xx in (10., 15., 20., 30., 40.):
    i = int(round(xx * 74)); P = r["Pe"][i]; mu = 1 + (1 + xx) / e + 0; mean = (1 + xx) / e + b; var = F * (1 + xx) / e
    # discretised Gaussian in N_tot = 1 + N_sub
    from scipy.stats import norm
    Pg = norm.cdf((n + 1 + .5 - mean) / np.sqrt(var)) - norm.cdf((n + 1 - .5 - mean) / np.sqrt(var))
    mean_true = 1 + P @ n; var_true = P @ (n * n) - (P @ n) ** 2
    Pg2 = norm.cdf((n + 1 + .5 - mean_true) / np.sqrt(var_true)) - norm.cdf((n + 1 - .5 - mean_true) / np.sqrt(var_true))
    gp.append((xx, "%.2e" % np.abs(P - Pg).max(), "%.2e" % np.abs(P - Pg2).max()))
OUT["gauss"] = gp
print("    (x, max|P - G| with asymptotic (eps,F,b), with exact mean and variance)", gp)
chk("X1 Gaussian match at x = 20-40 within 1e-6 (CW7-errata 1.4 criterion)", all(float(a[1]) < 1e-6 for a in gp[2:]), gp)

# ---- seed dependence of b_N
xs = (10., 20.); o = []
r = BL.solve_cfg(m, cfg, N=74, X=21.0, Nz=32); Pe = r["Pe"]; Ph = r["Ph"]; n = np.arange(32)
for om in (10., 20.):
    one = 1 + Pe[int(round((om - 1) * 74))] @ n
    sym = 1 + Pe[int(round((om - 1) / 2 * 74))] @ n + Ph[int(round((om - 1) / 2 * 74))] @ n
    o.append((om, round(one, 4), round(sym, 4), round(one - sym, 4)))
OUT["seed_bN"] = o
print("    seed dependence, Si: (omega/E_g, <N> one-sided, <N> symmetric, difference)", o)

# ---- reproduces GAP-EF-v3 rows
R3 = BL.R3; rows = list(csv.DictReader(open(os.path.join(HERE, "data", "library_summary.csv"))))
de = dF = 0; cnt = 0; worst = None
for r in rows:
    if r["cfg"] not in ("m1", "V1", "V3"): continue
    v = {"m1": "V0", "V1": "V1", "V3": "V3"}[r["cfg"]]; mat = r["material"]
    src = R3["variants"][v]["Si"] if mat == "Si" else (R3["predictions"].get(mat) or {}).get(v) or (R3["validation"].get(mat) or {}).get(v)
    if src is None: print("    no v3 row", mat, v); continue
    a = abs(float(r["eps_eV"]) / src["eps"] - 1); c = abs(float(r["F"]) / src["F"] - 1); cnt += 1
    if a > de: worst = (mat, v, float(r["eps_eV"]), src["eps"])
    de = max(de, a); dF = max(dF, c)
chk("R1 library eps, F (convex read, new code) = GAP-EF-v3 results.json on every row and V0/V1/V3 within 1e-3 (v3's own discretisation <= 0.19%); v3 interpolates eps, F over nodes, so not bitwise", de < 1e-3 and dF < 1e-3 and cnt >= 88, "rows %d max deps %.2e dF %.2e %s" % (cnt, de, dF, worst))
sp_ = max(float(r["sumP_err"]) for r in rows); pm = min(float(r["Pmin"]) for r in rows); nz = all(r["Nz_rule_ok"] == "True" for r in rows)
chk("L1 every library row: |sum P - 1| < 1e-12; Nz >= Nbar + 8 sigma", sp_ < 1e-12 and nz, "rows %d max %.1e; min P after interpolation %.2e" % (len(rows), sp_, pm))
chk("L2 min P >= -1e-13 (a p.g.f. mixture: round-off only)", pm > -1e-13, pm)

# ---- h convergence (conv.py)
if os.path.exists(os.path.join(HERE, "data", "conv_h.csv")):
    c = list(csv.DictReader(open(os.path.join(HERE, "data", "conv_h.csv"))))
    print("    conv_h rows", len(c), "max|dP| N vs 2N at equal x: median %.2e max %.2e (%s); observed order on 4N rows median %.2f" % (np.median([float(r["dP_N_2N"]) for r in c]), max(float(r["dP_N_2N"]) for r in c), max(c, key=lambda r: float(r["dP_N_2N"]))["material"], np.nanmedian([float(r["p_obs"]) for r in c])))

# ---- MC of the full distribution: Si, Ge, C at x0 = 5, 10, 20; solver continuum from N, 2N at order 3/2
Mh = 1000000; mcout = {}; zmax = 0; okh = True
for mat, (Eg, om, Wv, Xm) in MC.CASES.items():
    lam = A0 / Eg ** 3; w = om / Eg; W = None if Wv is None else Wv / Eg
    mm = M[mat]; cfg = dict(BL.configs(mm))["m1"]; N = BL.grid(w, nwmin=1)[0]
    r1 = BL.solve_cfg(mm, cfg, N=N, X=20.0, Nz=32); r2 = BL.solve_cfg(mm, cfg, N=2 * N, X=20.0, Nz=32)
    for x0 in (5.0, 10.0, 20.0):
        i1, i2 = int(round(x0 * N)), int(round(x0 * 2 * N))
        Pc = r2["Pe"][i2] + (r2["Pe"][i2] - r1["Pe"][i1]) / (2 ** 1.5 - 1)
        c = np.concatenate([MC.cascade_mc(lam, w, x0, 200000, W=W, seed=7000 + 100 * j + int(x0) + 11 * len(mat)) for j in range(Mh // 200000)]).astype(int)
        hst = np.bincount(c, minlength=32)[:32] / Mh
        sel = Pc * Mh > 25
        se = np.sqrt(np.maximum(Pc, 1e-12) * (1 - Pc) / Mh)
        z = (hst - Pc)[sel] / se[sel]
        chi2 = float((z ** 2).sum()); dof = int(sel.sum())
        mcout["%s_%g" % (mat, x0)] = dict(chi2=chi2, dof=dof, zmax=float(np.abs(z).max()), maxdP=float(np.abs(hst - Pc).max()), P=[round(float(v), 6) for v in Pc[:16]], Pmc=[round(float(v), 6) for v in hst[:16]])
        print("    MC", mat, x0, "chi2/dof %.1f/%d zmax %.2f max|dP| %.1e" % (chi2, dof, np.abs(z).max(), np.abs(hst - Pc).max()), flush=True)
        zmax = max(zmax, np.abs(z).max()); okh &= chi2 < dof + 4 * np.sqrt(2 * dof) + 8
OUT["mc"] = mcout
chk("MC1 independent event-by-event MC of the N histogram (true omega_0, 1e6 histories) = solver continuum, chi2 test", okh, "zmax %.2f" % zmax)
json.dump(OUT, open(os.path.join(HERE, "data", "checks_out.json"), "w"), indent=0, default=float)
print("%d/%d PASS" % (sum(res), len(res)))
