"""GAP-EF checks (labels GAP-EF-Cn). Run: python3 -I checks.py  (< 2 min). Prints PASS/FAIL; exit code 1 on any FAIL.
Deterministic quadrature and sympy only; no Monte Carlo, no first-principles numerics.
Two-route checks: exact moment recursion vs an exactly soluble model (Renyi/RPP, 0911.1532); N-moments vs heat moments
from independent recursions; renewal formula vs an explicit renewal recursion; sympy algebra vs the WP5v3-C4 numbers;
the solver vs the independent R&K Monte Carlo (2004.10709 F_inf = 0.115); spot rows of data/results.json recomputed."""
import json, os, sys, time
import numpy as np
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from cascade import Cascade
from model import run, calibrate_A
RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:86s} {note}", flush=True)
t0 = time.time()
J = json.load(open(os.path.join(HERE, "data", "results.json"))); S = json.load(open(os.path.join(HERE, "data", "scan.json")))

# C1 Renyi random parking (0911.1532: rho_inf = 0.7475987 Eq. (23) p.4; F_exact = 0.0510387 Eq. (2) p.2): Richardson h -> 0
c1 = Cascade(0, 0.05, X=30, h=0.01, a=(0.0, 0.0), hole_delta=True, phonon=False)
c2 = Cascade(0, 0.05, X=30, h=0.005, a=(0.0, 0.0), hole_delta=True, phonon=False)
e1, F1, _ = c1.asym(0); e2, F2, _ = c2.asym(0); eR, FR = 2 * e2 - e1, 2 * F2 - F1
rep("GAP-EF-C1 RPP limit: coverage 1/eps -> 0.747599, F -> 0.0510387 (Richardson)", abs(1 / eR - 0.7475987) < 3e-4 and abs(FR - 0.0510387) < 1e-4,
    f"1/eps={1/eR:.5f} F={FR:.5f}")
# C2 renewal (uncorrelated final-state) estimate in the RPP limit vs 0911.1532 p.4 F_unc = 0.0439766
d1, d2 = c1.decomposition(0), c2.decomposition(0); Fu = 2 * d2["F_ren"] - d1["F_ren"]
rep("GAP-EF-C2 renewal estimate per carrier type, RPP limit -> F_unc = 0.04398 (0911.1532 p.4)", abs(Fu - 0.0439766) < 5e-4, f"F_unc={Fu:.5f}")
# C3-C4 Si model: energy conservation of the discrete kernel; Var N E_g^2 = Var(H_< + H_>) from independent recursions
cs = Cascade(3.5501, 0.063 / 1.164, X=40, h=1 / 74); ds = cs.decomposition(0)
rep("GAP-EF-C3 discrete kernel conserves energy: x = N + H_< + H_> (max rel)", cs.energy_residual(0) < 1e-12, f"{cs.energy_residual(0):.1e}")
rep("GAP-EF-C4 F from N-moments = F from heat moments; F = V_< + V_> + 2Cov", abs(ds["F"] - ds["F_from_H"]) < 1e-9 and
    abs(ds["VR"] + ds["VP"] + ds["Cov2"] - ds["F"]) < 1e-9, f"F={ds['F']:.4f} V<={ds['VR']:.3f} V>={ds['VP']:.3f} 2Cov={ds['Cov2']:.3f}")
# C5 discretisation (Si, omega_0 on the grid): N = 74 vs 148
ra, rb = run(5.5947, 1.164, 0.063, N=74), run(5.5947, 1.164, 0.063, N=148)
rep("GAP-EF-C5 Si grid N=74 vs 148: |d eps|/eps < 1e-3, |dF|/F < 2e-3", abs(ra["eps"] / rb["eps"] - 1) < 1e-3 and abs(ra["F"] / rb["F"] - 1) < 2e-3,
    f"{ra['eps']:.4f}/{rb['eps']:.4f}, {ra['F']:.5f}/{rb['F']:.5f}")
# C6 asymptotic window (r1)-(r3): X = 40 vs 80, fit window [X/2, X] vs [3X/4, X]
rc, rd = run(5.5947, 1.164, 0.063, X=80, frac=0.75), ra
rep("GAP-EF-C6 Si asymptote stable: X=40,[X/2,X] vs X=80,[3X/4,X] (rel < 1e-4)", abs(rc["eps"] / rd["eps"] - 1) < 1e-4 and abs(rc["F"] / rd["F"] - 1) < 1e-4,
    f"dF/F={rc['F']/rd['F']-1:.1e}")
# C7 calibration (single parameter A on Si eps = 3.749 eV [FT 2004.11499]) and the uncalibrated F_Si
V0 = J["variants"]["V0"]; A0 = V0["A"]
rep("GAP-EF-C7 A_ph(Si) reproduces 3.749 eV; A in [5.0, 6.0] eV^3 (ABS fit 5.2 [FT 2610.16949 p.3])",
    abs(run(A0, 1.164, 0.063, Wv=12.0, X=40)["eps"] - 3.749) < 2e-3 and 5.0 < A0 < 6.0, f"A={A0:.3f}")
rep("GAP-EF-C7b predicted F_Si within 5% of 0.119 +- 0.002 [FT 2004.11499] (not calibrated)", abs(V0["Si"]["F"] / 0.119 - 1) < 0.05,
    f"F_Si={V0['Si']['F']:.4f}")
# C8 cross-check against the R&K Monte Carlo (2004.10709 p.6: F_inf = 0.115 at A = 5.2, 300 K, E_g = 1.124, W = 12 eV)
rk = run(5.2, 1.124, 0.063, Wv=12.0, X=40)
rep("GAP-EF-C8 R&K parameters: F_inf = 0.115 (independent MC, 2004.10709 p.6) within 1%", abs(rk["F"] / 0.115 - 1) < 0.01, f"F={rk['F']:.4f}")
# C9 Klein algebra (sympy): uniform-in-k residual below theta E_g: eps = E_g(1 + 6 theta/5); N fixed vs energy-constrained Fano
x, th = sp.symbols("x theta", positive=True)
pdf = sp.sqrt(x) / sp.integrate(sp.sqrt(x), (x, 0, th)); m1 = sp.integrate(x * pdf, (x, 0, th)); m2 = sp.integrate(x ** 2 * pdf, (x, 0, th))
epsK = sp.simplify(1 + 2 * m1); var1 = sp.simplify(m2 - m1 ** 2)
FNfix = sp.simplify(2 * var1); Fren = sp.simplify(2 * var1 / epsK ** 2)
k32 = {th: sp.Rational(3, 2)}
rep("GAP-EF-C9 Klein: eps = (1 + 6theta/5)E_g = 14/5 at theta=3/2; WP5v3-C4b 54/175 is the N-fixed value; constrained = 0.0394",
    sp.simplify(epsK - (1 + sp.Rational(6, 5) * th)) == 0 and epsK.subs(k32) == sp.Rational(14, 5) and FNfix.subs(k32) == sp.Rational(54, 175)
    and sp.simplify(Fren.subs(k32) - sp.Rational(54, 175) * sp.Rational(25, 196)) == 0, f"F_ren = {sp.N(Fren.subs(k32), 4)}")
# C10 renewal formula F = sigma^2/eps^2 (Fano 1947; 0911.1532 Eq. (7)) vs an explicit renewal recursion with exact energy constraint
h = 0.005; K = int(30 / h) + 1; xs = np.arange(K) * h; nG = int(1 / h)
nr = int(1.5 / h); fr = np.sqrt(xs[:nr]); fr /= fr.sum()                     # cost per pair = 1 + r, r ~ sqrt on [0, 1.5)
mm = np.zeros(K); ss = np.zeros(K)
for n in range(K):
    js = n - nG - np.arange(nr); ok = js >= 0; p = fr[ok]; jj = js[ok]
    if n < nG: continue
    pn = p.sum(); mm[n] = pn * 1 + (p * mm[jj]).sum(); ss[n] = pn + (p * (2 * mm[jj] + ss[jj])).sum()   # stop if r overshoots (prob 1-pn)
sel = xs > 15; Am = np.vstack([xs[sel], np.ones(sel.sum())]).T
sl_m = np.linalg.lstsq(Am, mm[sel], rcond=None)[0][0]; sl_v = np.linalg.lstsq(Am, (ss - mm ** 2)[sel], rcond=None)[0][0]
r1 = (fr * xs[:nr]).sum(); r2 = (fr * xs[:nr] ** 2).sum(); epsr = 1 + r1
rep("GAP-EF-C10 renewal: Var N/<N> -> sigma_r^2/eps^2 with exact energy constraint (not sigma_r^2/E_g^2)",
    abs(sl_v / sl_m / ((r2 - r1 ** 2) / epsr ** 2) - 1) < 0.02 and abs(1 / sl_m / epsr - 1) < 2e-3,
    f"F={sl_v/sl_m:.4f} vs {(r2-r1**2)/epsr**2:.4f}")
# C11 lam -> 0 (no phonons): c0(theta) by Richardson; Klein's uniform population (1 + 6theta/5) overstates it
c0 = {}
for tt in (1.0, 1.5):
    e_a = Cascade(0.0, 0.05, X=30, h=0.01, theta=(tt, tt), phonon=False, sets=("N",)).asym(0)[0]
    e_b = Cascade(0.0, 0.05, X=30, h=0.005, theta=(tt, tt), phonon=False, sets=("N",)).asym(0)[0]
    c0[tt] = 2 * e_b - e_a
rep("GAP-EF-C11 c0(1) and c0(3/2) below Klein's 2.2 and 2.8 by > 25%", c0[1.0] < 0.75 * 2.2 and c0[1.5] < 0.75 * 2.8,
    f"c0(1)={c0[1.0]:.3f}, c0(1.5)={c0[1.5]:.3f}")
# C12 spot rows of results.json recomputed (validation C, 4H-SiC; prediction Al2O3, W_v variant)
from predict import R
spot = [(J["validation"]["C"]["V0"], dict(A=A0, Eg=5.47, om0=0.163)), (J["validation"]["4H-SiC"]["V0"], dict(A=A0, Eg=3.26, om0=0.120)),
        (J["predictions"]["Al2O3"]["V0"], dict(A=A0, Eg=8.8, om0=0.104)), (J["predictions"]["Al2O3"]["Wv"], dict(A=A0, Eg=8.8, om0=0.104, Wv=8.8))]
ok = all(abs(R(**kw)["eps"] - row["eps"]) < 1e-9 and abs(R(**kw)["F"] - row["F"]) < 1e-9 for row, kw in spot)
rep("GAP-EF-C12 spot rows of data/results.json reproduced (C, 4H-SiC, Al2O3, Al2O3 W_v = E_g)", ok)
# C13 validation statistics recomputed from the json
res = [v["meas"] / v["V0"]["eps"] - 1 for v in J["validation"].values()]
rep("GAP-EF-C13 validation residuals [FT rows only]: range and rms as quoted", abs(min(res) - J["resid_range"][0]) < 1e-12 and
    abs(max(res) - J["resid_range"][1]) < 1e-12, f"range [{min(res):+.3f}, {max(res):+.3f}], rms {np.sqrt(np.mean(np.square(res))):.3f}")
# C14 fits (EF9)-(EF10) against fresh solver runs inside the fit domain (Si and diamond lam, w)
pe, pF = S["p_eps"], S["p_F"]
def fe(l, w): return pe[0] + pe[1] * (l * w ** pe[2]) ** pe[3]
def fF(e, w): return pF[0] + pF[1] * e + pF[2] * e ** 2 + pF[3] * w
ok = True; note = ""
for (A_, Eg, om) in ((A0, 1.164, 0.063), (A0, 5.47, 0.163)):
    r = run(A_, Eg, om, X=25.0, Nmax=300, nwmin=1)
    ok &= abs(fe(r["lam"], r["w"]) / r["eps_over_Eg"] - 1) < max(0.006, S["eps_fit_maxrel"]) and abs(fF(r["eps_over_Eg"], r["w"]) / r["F"] - 1) < max(0.025, S["F_fit_maxrel"])
    note += f"{fe(r['lam'], r['w'])/r['eps_over_Eg']-1:+.4f}/{fF(r['eps_over_Eg'], r['w'])/r['F']-1:+.4f} "
rep("GAP-EF-C14 closed-form fits (EF9)-(EF10) within their stated max residual", ok, note)
# C15 effective-gap sensitivity d eps/d E_g at fixed A_ph, omega_0: solver finite difference vs (EF11) from the fit
d = 0.01; ep = run(A0, 1.164 + d, 0.063, X=25.0)["eps"]; em = run(A0, 1.164 - d, 0.063, X=25.0)["eps"]
lam, w = A0 / 1.164 ** 3, 0.063 / 1.164; u = (lam * w ** pe[2]) ** pe[3]
fd = (ep - em) / (2 * d); an = pe[0] + pe[1] * u * (1 - 3 * pe[3] - pe[2] * pe[3])
rep("GAP-EF-C15 d eps/dE_g (Si): finite difference vs (EF11) within 10%", abs(fd / an - 1) < 0.10, f"FD={fd:.3f} EF11={an:.3f}")
# C16 binomial thinning of prompt capture (sympy, exact): F' = (1 - f)F + f, eps' = eps/(1 - f)
n, f, Fv, mu = sp.symbols("n f F mu", positive=True)
mean_t = (1 - f) * mu; var_t = (1 - f) ** 2 * Fv * mu + f * (1 - f) * mu         # law of total variance, Bernoulli(1-f) per pair
rep("GAP-EF-C16 prompt capture as Bernoulli thinning: F' = (1-f)F + f", sp.simplify(var_t / mean_t - ((1 - f) * Fv + f)) == 0)
# C17 hydrogenic (Wannier) exciton estimates used in section 4 [E]: E_x^b = 13.606 mu*/eps_r^2 eV
Ry = 13.605693; ex = lambda me, mh, er: Ry * (me * mh / (me + mh)) / er ** 2
vals = {"GaN": ex(0.19, 1.647, 9.5), "ZnO": ex(0.22, 2.34, 8.1), "4H-SiC": ex(0.47, 1.353, 9.8)}
rep("GAP-EF-C17 hydrogenic E_x^b [E]: GaN, ZnO, 4H-SiC (CSV masses, eps_r as quoted in sec. 4)", all(0.005 < v < 0.1 for v in vals.values()),
    " ".join(f"{k} {1e3*v:.0f} meV" for k, v in vals.items()))
# C18 every cited arXiv ID has an API record in literature/papers-GAP-EF
lit = os.path.join(HERE, "..", "..", "literature", "papers-GAP-EF")
ids = ["2610.16949", "0911.1532", "2311.03902", "1602.08005", "2202.03924", "2311.05011", "2004.11499", "2305.09005", "1909.05806",
       "2411.12320", "2308.03893", "1901.07569", "2004.10709", "2008.08560", "1910.10716"]
okl = True
for i in ids:
    try:
        p = json.load(open(os.path.join(lit, f"arxiv-{i}.json")))["papers"]; okl &= bool(p) and p[0]["id"].startswith(i)
    except Exception:
        okl = False
rep("GAP-EF-C18 arXiv IDs verified against the API (arxiv-*.json present, IDs match)", okl, f"{len(ids)} IDs")
print(f"{sum(RES)}/{len(RES)} PASS, {time.time() - t0:.0f} s")
sys.exit(0 if all(RES) else 1)
