"""GAP-EF-v2 checks (labels GAP-EF-v2-Cn). Run: python3 -I checks.py  (< 2 min). Prints PASS/FAIL; exit code 1 on any FAIL.
Deterministic quadrature, sympy and exact enumeration only; no Monte Carlo, no first-principles numerics.
v2 (returns/R16/GAP-EF-v2.md) absorbs REF-GAP-EF-A K1-K14 and REF-GAP-EF-B items 1-9:
  C2 target is the corrected 0911.1532 value F_unc = 0.0443977 (the printed 0.0439766 is a typo), tolerance 1e-5 (K9);
  C4 is split: C4a N route = heat route; C4b Cov(H_<, H_>) by an independent deposit D = H_< - H_> (K10);
  C7b no longer has a 5% pass band: it checks the quoted 2.6 sigma and the weak A-dependence (K6);
  C8 compares with R&K's MC at its ~2% scatter and with the four slopes of R&K Eqs. (12)-(13) (REF-A R3, REF-B 2.3);
  C11 checks the 36-39% overstatement (K8); C13 declares the validation convention (K3);
  C16b shows thinning fails for energy-dependent capture (K2); C19-C26 are new (see the return, sec. 7).
ERRATA (returns/R16/GAP-EF-v2-errata.md, answering referees/R16/VER-GAP-EF-v2.md V-1...V-14):
  C1 targets Renyi's constant 0.74759792 computed here (0911.1532 Eq. (23) prints 0.7475987, a 7th-digit misprint), tol 3e-6;
  C2 no longer uses a hard-coded target: F_unc is evaluated independently (mpmath, Renyi gap law) and the dropped-digit misprint is checked;
  C5, C8, C10, C15 tolerances tightened to just above the quoted values; C8 adds dF/dE_g (V-12);
  C13 recomputes the statistics from the measured values typed from sec. 2 and checks the text-quoted numbers (no json-vs-json);
  C23 rewritten (V-2): (EF8) exact on every grid once the O(h^2) threshold artefact is booked; Richardson row 5e-4 / 1e-8;
  C25 adds k2(Si) = 1.87 eV (V-13) and the in-domain minimum; C26-C29 are new (errata sec. 3, 4)."""
import json, os, sys, time, itertools
import numpy as np
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from cascade import Cascade
from model import run, grid
RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:92s} {note}", flush=True)
t0 = time.time()
J = json.load(open(os.path.join(HERE, "data", "results.json"))); S = json.load(open(os.path.join(HERE, "data", "scan.json")))
REN = ("N", "R", "P", "H", "R2", "C", "Re", "Rh", "R2e", "R2h", "Ce", "Ch")

# C1 Renyi random parking (0911.1532: rho_inf = 0.7475987 Eq. (23) p.4; F_exact = 0.0510387 Eq. (2) p.2): Richardson h -> 0
c1 = Cascade(0, 0.05, X=30, h=0.01, a=(0.0, 0.0), hole_delta=True, phonon=False, sets=REN)
c2 = Cascade(0, 0.05, X=30, h=0.005, a=(0.0, 0.0), hole_delta=True, phonon=False, sets=REN)
e1, F1, _ = c1.asym(0); e2, F2, _ = c2.asym(0); eR, FR = 2 * e2 - e1, 2 * F2 - F1
# Independent Renyi values (mpmath; jammed gap density G(g) = 2 int_0^inf t exp(-g t - 2 Ein(t)) dt, 0 <= g <= 1, inner g-integrals analytic)
import mpmath as mp
mp.mp.dps = 30
Ein = lambda t: mp.euler + mp.log(t) + mp.e1(t)
_gk = (lambda t: (1 - mp.exp(-t)) / t, lambda t: (1 - mp.exp(-t) * (1 + t)) / t ** 2, lambda t: (2 - mp.exp(-t) * (t * t + 2 * t + 2)) / t ** 3)
gm = [mp.quad(lambda t: 2 * t * mp.exp(-2 * Ein(t)) * _gk[k](t), [0, 1, 10, 100, mp.inf]) for k in range(3)]
rho_inf = float(mp.quad(lambda t: mp.exp(-2 * Ein(t)), [0, 1, 10, 100, mp.inf]))
g1_, g2_ = gm[1] / gm[0], gm[2] / gm[0]; Func_true = float((g2_ - g1_ ** 2) / (1 + g1_) ** 2)
rep("GAP-EF-v2-C1 RPP limit: 1/eps -> Renyi 0.74759792 (mpmath; 0911.1532 prints 0.7475987), F -> 0.0510387 (Richardson)",
    abs(rho_inf - 0.7475979203) < 1e-9 and abs(float(gm[0]) - rho_inf) < 1e-12 and abs(float(gm[0] + gm[1]) - 1) < 1e-12
    and abs(1 / eR - rho_inf) < 3e-6 and abs(FR - 0.0510387) < 5e-6,
    f"rho={rho_inf:.8f} 1/eps={1/eR:.7f} F={FR:.7f}")
# C2 renewal (uncorrelated final-state) estimate in the RPP limit: corrected F_unc = 0.0443977 (0911.1532 p.4 prints 0.0439766, a typo:
#    its own F_nnp = F_unc + dF_nnp = 0.05208 with dF_nnp = 0.007685 needs 0.044398; REF-A b.1). Tolerance 1e-5. Lower bound: F_unc < F_exact.
d1, d2 = c1.decomposition(0), c2.decomposition(0); Fu = 2 * d2["F_ren"] - d1["F_ren"]
#    Errata V-1: the misprint is a dropped digit: "0.04439766" with one "4" deleted is the printed "0.0439766".
drop = {"0.04439766"[:i] + "0.04439766"[i + 1:] for i in range(2, 10)}
rep("GAP-EF-v2-C2 RPP renewal estimate = independent F_unc (mpmath 0.04439766) to 5e-6; printed 0.0439766 = dropped digit; F_nnp consistent",
    abs(Func_true - 0.0443976648) < 1e-9 and abs(Fu - Func_true) < 5e-6 and Fu < FR and "0.0439766" in drop
    and abs(Func_true + 0.007685 - 0.05208) < 5e-6 and abs(0.0439766 + 0.007685 - 0.05208) > 3e-4,
    f"F_unc(solver)={Fu:.7f} F_unc(mpmath)={Func_true:.8f}")
# C3-C4 Si model (B_h = infinity here; the calibration uses B_h = 12 eV, effect <= 1e-4, REF-B R4)
cs = Cascade(3.5501, 0.063 / 1.164, X=40, h=1 / 74, sets=("N", "R", "P", "H", "D")); xs_ = cs.x; sel = xs_ >= 20
A_ = np.vstack([1 + xs_[sel], np.ones(sel.sum())]).T; sl = lambda y: np.linalg.lstsq(A_, y[sel], rcond=None)[0][0]
eps_s = 1 / sl(cs.res["N"][0][0]); vN, vR, vP, vH, vD = (sl(cs.var(k)) * eps_s for k in ("N", "R", "P", "H", "D"))
rep("GAP-EF-v2-C3 discrete kernel conserves energy: x = N + H_< + H_> (max rel)", cs.energy_residual(0) < 1e-12, f"{cs.energy_residual(0):.1e}")
rep("GAP-EF-v2-C4a F from N-moments = F from heat moments (independent recursions)", abs(vN - vH) < 1e-9, f"F={vN:.4f}")
C2d = 0.5 * (vH - vD); C2r = vH - vR - vP
rep("GAP-EF-v2-C4b 2Cov(H_<,H_>) from the D = H_< - H_> recursion equals the remainder Var H - V_< - V_> (two routes)",
    abs(C2d - C2r) < 1e-9 and C2d < 0, f"V<={vR:.3f} V>={vP:.3f} 2Cov={C2d:.4f}")
# C5 discretisation: Si N = 74 vs 148; diamond N = 67 vs 134 (REF-B 2.7)
ra, rb = run(5.5947, 1.164, 0.063, N=74), run(5.5947, 1.164, 0.063, N=148)
rcA, rcB = run(5.5947, 5.47, 0.163, X=25, N=67), run(5.5947, 5.47, 0.163, X=25, N=134)
rep("GAP-EF-v2-C5 grid doubling: Si |d eps|/eps < 6e-4, |dF|/F < 1e-3; C |d eps|/eps < 1.5e-3 (text: 0.05%, 0.05%, 0.12%)",
    abs(ra["eps"] / rb["eps"] - 1) < 6e-4 and abs(ra["F"] / rb["F"] - 1) < 1e-3 and abs(rcA["eps"] / rcB["eps"] - 1) < 1.5e-3,
    f"Si {ra['eps']/rb['eps']-1:.1e}/{ra['F']/rb['F']-1:.1e}; C {rcA['eps']/rcB['eps']-1:.1e}")
# C6 asymptotic window (r1)-(r3): X = 40 vs 80, fit window [X/2, X] vs [3X/4, X]
rc = run(5.5947, 1.164, 0.063, X=80, frac=0.75)
rep("GAP-EF-v2-C6 Si asymptote stable: X=40,[X/2,X] vs X=80,[3X/4,X] (rel < 1e-4)", abs(rc["eps"] / ra["eps"] - 1) < 1e-4 and abs(rc["F"] / ra["F"] - 1) < 1e-4,
    f"dF/F={rc['F']/ra['F']-1:.1e}")
# C7 calibration (single parameter A on Si eps = 3.749 eV [FT 2004.11499])
V0 = J["variants"]["V0"]; A0 = V0["A"]
rep("GAP-EF-v2-C7 A_ph(Si) reproduces 3.749 eV; A in [5.0, 6.0] eV^3 (ABS fit 5.2 [FT 2610.16949 p.3])",
    abs(run(A0, 1.164, 0.063, Wv=12.0, X=40)["eps"] - 3.749) < 2e-3 and 5.0 < A0 < 6.0, f"A={A0:.3f}")
# C7b F_Si is untuned but is NOT an independent test: quoted deviation 2.6 sigma; +-10% in A moves F by < 1%; equals R&K's 0.115 within 2%
FSi = V0["Si"]["F"]; nsig = (0.119 - FSi) / 0.002; dFrel = 0.5 * (J["Si_F_pm10A"][1] - J["Si_F_pm10A"][0]) / FSi   # per +10% in A
rep("GAP-EF-v2-C7b F_Si = 0.114: 2.6 sigma below 0.119 +- 0.002; |dF/F| < 1% per 10% in A; |F/0.115 - 1| < 2%",
    2.5 < nsig < 2.7 and abs(dFrel) < 0.01 and abs(FSi / 0.115 - 1) < 0.02, f"F={FSi:.4f}, {nsig:.2f} sigma, dF/F per 10% A={dFrel:+.4f}")
# C8 R&K (2004.10709 p.6: F_inf = 0.115 at A = 5.2, E_g = 1.124, W = 12 eV; MC scatter ~2%) and its Eqs. (12)-(13) slopes
rk = run(5.2, 1.124, 0.063, Wv=12.0, X=40); K = {(p["A"], p["Eg"]): p for p in J["rk_slopes"]}
assert abs(K[(5.2, 1.124)]["F"] - rk["F"]) < 1e-9
deA = (K[(7.0, 1.124)]["eps"] - K[(3.0, 1.124)]["eps"]) / 4; dFA = (K[(7.0, 1.124)]["F"] - K[(3.0, 1.124)]["F"]) / 4
deE = (K[(5.2, 1.2)]["eps"] - K[(5.2, 1.0)]["eps"]) / 0.2; dFE = (K[(5.2, 1.2)]["F"] - K[(5.2, 1.0)]["F"]) / 0.2
okp = all(abs(p["eps_RK"] - (1.7 * p["Eg"] + 0.084 * p["A"] + 1.3)) < 1e-9 and abs(p["F_RK"] - (-0.028 * p["Eg"] + 0.0015 * p["A"] + 0.14)) < 1e-9
          for p in J["rk_slopes"])   # the plane values are R&K Eqs. (12)-(13), re-evaluated here
rep("GAP-EF-v2-C8 R&K: F_inf 0.115 within 2%; four slopes (incl. dF/dE_g, errata V-12) within 8%; points <= 1.2% (eps), <= 2.5% (F)",
    okp and abs(rk["F"] / 0.115 - 1) < 0.02 and abs(deA / 0.084 - 1) < 0.08 and abs(dFA / 0.0015 - 1) < 0.08 and abs(deE / 1.7 - 1) < 0.08
    and abs(dFE / -0.028 - 1) < 0.08
    and all(abs(p["eps"] / p["eps_RK"] - 1) < 0.012 and abs(p["F"] / p["F_RK"] - 1) < 0.025 for p in J["rk_slopes"]),
    f"F={rk['F']:.4f}; {deA:.4f}/0.084, {dFA:.5f}/0.0015, {deE:.3f}/1.7, {dFE:.4f}/-0.028")
# C9 Klein algebra (sympy): uniform-in-k residual below theta E_g: eps = E_g(1 + 6 theta/5); N fixed vs energy-constrained Fano
x, th = sp.symbols("x theta", positive=True)
pdf = sp.sqrt(x) / sp.integrate(sp.sqrt(x), (x, 0, th)); m1 = sp.integrate(x * pdf, (x, 0, th)); m2 = sp.integrate(x ** 2 * pdf, (x, 0, th))
epsK = sp.simplify(1 + 2 * m1); var1 = sp.simplify(m2 - m1 ** 2)
FNfix = sp.simplify(2 * var1); Fren = sp.simplify(2 * var1 / epsK ** 2)
k32 = {th: sp.Rational(3, 2)}
rep("GAP-EF-v2-C9 Klein: eps = (1 + 6theta/5)E_g = 14/5 at theta=3/2; 54/175 is the N-fixed value; constrained 27/686 = 0.0394",
    sp.simplify(epsK - (1 + sp.Rational(6, 5) * th)) == 0 and epsK.subs(k32) == sp.Rational(14, 5) and FNfix.subs(k32) == sp.Rational(54, 175)
    and sp.simplify(Fren.subs(k32) - sp.Rational(27, 686)) == 0, f"F_ren = {sp.N(Fren.subs(k32), 4)}")
# C10 renewal formula F = sigma^2/eps^2 (iid per-pair costs; 0911.1532 Eq. (7)) vs an explicit renewal recursion with exact energy constraint
TOL10 = 1e-3   # errata: tightened from 2% (observed 2.4e-4)
h = 0.005; Kk = int(30 / h) + 1; xs = np.arange(Kk) * h; nG = int(1 / h)
nr = int(1.5 / h); fr = np.sqrt(xs[:nr]); fr /= fr.sum()
mm = np.zeros(Kk); ss = np.zeros(Kk)
for n in range(Kk):
    js = n - nG - np.arange(nr); ok = js >= 0; p = fr[ok]; jj = js[ok]
    if n < nG: continue
    pn = p.sum(); mm[n] = pn * 1 + (p * mm[jj]).sum(); ss[n] = pn + (p * (2 * mm[jj] + ss[jj])).sum()
sel = xs > 15; Am = np.vstack([xs[sel], np.ones(sel.sum())]).T
sl_m = np.linalg.lstsq(Am, mm[sel], rcond=None)[0][0]; sl_v = np.linalg.lstsq(Am, (ss - mm ** 2)[sel], rcond=None)[0][0]
r1 = (fr * xs[:nr]).sum(); r2 = (fr * xs[:nr] ** 2).sum(); epsr = 1 + r1
rep("GAP-EF-v2-C10 renewal: Var N/<N> -> sigma_h^2/eps^2 (to 1e-3) with exact energy constraint (not sigma_h^2/E_g^2)",
    abs(sl_v / sl_m / ((r2 - r1 ** 2) / epsr ** 2) - 1) < TOL10 and abs(1 / sl_m / epsr - 1) < 2e-3, f"F={sl_v/sl_m:.5f} vs {(r2-r1**2)/epsr**2:.5f} ({sl_v/sl_m/((r2-r1**2)/epsr**2)-1:+.1e}); eps {1/sl_m/epsr-1:+.1e}")
# C11 lam -> 0: Klein's uniform population (1 + 6theta/5) overstates the exact c0 by 39% (theta = 1) and 36% (theta = 3/2)
T1 = J["table1"]; c0 = {1.0: T1["lam0_th1"]["eps"], 1.5: T1["lam0_th15"]["eps"]}
L0a = Cascade(0.0, 0.05, X=30, h=0.01, theta=(1.0, 1.0), phonon=False, sets=("N", "R", "P", "C"))
L0b = Cascade(0.0, 0.05, X=30, h=0.005, theta=(1.0, 1.0), phonon=False, sets=("N", "R", "P", "C"))
ea, eb = L0a.asym(0)[0], L0b.asym(0)[0]
o1, o15 = 2.2 / c0[1.0] - 1, 2.8 / c0[1.5] - 1
rep("GAP-EF-v2-C11 (K2) overstates c0: 2.2/c0(1) - 1 in [0.38, 0.40], 2.8/c0(3/2) - 1 in [0.35, 0.37]; json c0(1) recomputed",
    0.38 < o1 < 0.40 and 0.35 < o15 < 0.37 and abs(2 * eb - ea - c0[1.0]) < 1e-9, f"c0 = {c0[1.0]:.4f}, {c0[1.5]:.4f}; +{100*o1:.1f}%, +{100*o15:.1f}%")
# C12 spot rows of results.json recomputed (validation C, 4H-SiC; prediction Al2O3, its W_v variant; CsI on the fixed grid)
from predict import R
spot = [(J["validation"]["C"]["V0"], dict(A=A0, Eg=5.47, om0=0.163)), (J["validation"]["4H-SiC"]["V0"], dict(A=A0, Eg=3.26, om0=0.120)),
        (J["predictions"]["Al2O3"]["V0"], dict(A=A0, Eg=8.8, om0=0.104)), (J["predictions"]["Al2O3"]["Wv"], dict(A=A0, Eg=8.8, om0=0.104, Wv=8.8))]
ok = True
for row, kw in spot:
    r = R(**kw); ok &= abs(r["eps"] - row["eps"]) < 1e-9 and abs(r["F"] - row["F"]) < 1e-9
rep("GAP-EF-v2-C12 spot rows of data/results.json reproduced (C, 4H-SiC, Al2O3, Al2O3 W_v = E_g)", ok)
# C13 validation statistics (errata: non-circular). Measured values typed from the return's sec. 2 table, model V0 from the solver
#     (C12 reproduces spot rows). Convention: primary = named measurements, GaN at EBIC 9.59 eV; extended = + beta-Ga2O3 (EBIC + MC 15.6);
#     all = extended + EF-LIT rows (Al2O3 27 vendor value, CaWO4 29.8 model value); no-GaN variant. Checked against the text-quoted numbers.
MEAS = {"Ge": 2.96, "C": 12.95, "4H-SiC": 7.83, "6H-SiC": 6.7, "3C-SiC": 6.90, "GaN": 9.59, "SiO2": 18.0}
MEXT, MLIT = {"b-Ga2O3": 15.6}, {"Al2O3": 27.0, "CaWO4": 29.8}
assert set(MEAS) == set(J["validation"]) and set(MEXT) == set(J["validation_ext"]) and set(MLIT) == set(J["validation_lit"])
res_ = lambda M, blk: [M[k] / J[blk][k]["V0"]["eps"] - 1 for k in M]
prim = res_(MEAS, "validation"); ext = prim + res_(MEXT, "validation_ext"); allr = ext + res_(MLIT, "validation_lit")
nog = [r_ for k, r_ in zip(MEAS, prim) if k != "GaN"]
rms = lambda a: float(np.sqrt(np.mean(np.square(a)))); pc = lambda v: round(100 * v, 1)
q13 = dict(pmin=-6.5, pmax=24.6, pmean=8.2, prms=12.3, nmean=5.5, nrms=8.7, nmax=13.9, emean=14.2, erms=23.0, emax=56.1, arms=63.4, amax=178.8)
got = dict(pmin=pc(min(prim)), pmax=pc(max(prim)), pmean=pc(np.mean(prim)), prms=pc(rms(prim)), nmean=pc(np.mean(nog)), nrms=pc(rms(nog)),
           nmax=pc(max(nog)), emean=pc(np.mean(ext)), erms=pc(rms(ext)), emax=pc(max(ext)), arms=pc(rms(allr)), amax=pc(max(allr)))
rep("GAP-EF-v2-C13 validation statistics from typed sec. 2 measurements = text-quoted values (primary, no-GaN, extended, all)",
    got == q13, f"prim {got['pmean']}/{got['prms']}%; noGaN {got['nmean']}/{got['nrms']}%; ext {got['emean']}/{got['erms']}%; all rms {got['arms']}%")
# C14 fits (EF9)-(EF10) against fresh solver runs inside the fit domain (Si and diamond lam, w)
pe, pF = S["p_eps"], S["p_F"]
def fe(l, w): return pe[0] + pe[1] * (l * w ** pe[2]) ** pe[3]
def fF(e, w): return pF[0] + pF[1] * e + pF[2] * e ** 2 + pF[3] * w
ok = True; note = ""
for (Aa, Eg, om) in ((A0, 1.164, 0.063), (A0, 5.47, 0.163)):
    r = run(Aa, Eg, om, X=25.0, Nmax=300, nwmin=1)
    ok &= abs(fe(r["lam"], r["w"]) / r["eps_over_Eg"] - 1) < max(0.006, S["eps_fit_maxrel"]) and abs(fF(r["eps_over_Eg"], r["w"]) / r["F"] - 1) < max(0.025, S["F_fit_maxrel"])
    note += f"{fe(r['lam'], r['w'])/r['eps_over_Eg']-1:+.4f}/{fF(r['eps_over_Eg'], r['w'])/r['F']-1:+.4f} "
rep("GAP-EF-v2-C14 closed-form fits (EF9)-(EF10) within their stated max residual", ok, note)
# C15 effective-gap sensitivity d eps/d E_g at fixed A_ph, omega_0: solver finite difference vs (EF11) from the fit
d = 0.01; ep = run(A0, 1.164 + d, 0.063, X=25.0)["eps"]; em = run(A0, 1.164 - d, 0.063, X=25.0)["eps"]
lam, w = A0 / 1.164 ** 3, 0.063 / 1.164; u = (lam * w ** pe[2]) ** pe[3]
fd = (ep - em) / (2 * d); an = pe[0] + pe[1] * u * (1 - 3 * pe[3] - pe[2] * pe[3])
rep("GAP-EF-v2-C15 d eps/dE_g (Si): FD 1.777 vs (EF11) 1.695 as quoted (+-0.005), i.e. (EF11) is 4.6% low", abs(fd - 1.777) < 0.005 and abs(an - 1.695) < 0.005,
    f"FD={fd:.3f} EF11={an:.3f} ({an/fd-1:+.3f})")
# C16 binomial thinning, constant f (sympy): F' = (1 - f)F + f, eps' = eps/(1 - f)
n, f, Fv, mu = sp.symbols("n f F mu", positive=True)
mean_t = (1 - f) * mu; var_t = (1 - f) ** 2 * Fv * mu + f * (1 - f) * mu
rep("GAP-EF-v2-C16 prompt capture, f the same for every carrier: F' = (1-f)F + f", sp.simplify(var_t / mean_t - ((1 - f) * Fv + f)) == 0)
# C16b f depending on the terminal state: exact enumeration of a toy cascade whose residual state s correlates with N.
#      General law Var N' = E sum f_i(1 - f_i) + Var(sum (1 - f_i)) holds; (EF12) with the mean f fails.
fs = {0: 0.05, 1: 0.5}; law = {(1, (0,)): 0.2, (1, (1,)): 0.2, (2, (0, 0)): 0.35, (2, (1, 1)): 0.05, (2, (0, 1)): 0.2}
EN = sum(p * n_ for (n_, _), p in law.items()); VN = sum(p * n_ ** 2 for (n_, _), p in law.items()) - EN ** 2
m1_, m2_ = 0.0, 0.0
for (n_, st), p in law.items():
    for keep in itertools.product((0, 1), repeat=n_):
        q = p
        for s_, k_ in zip(st, keep): q *= (1 - fs[s_]) if k_ else fs[s_]
        m1_ += q * sum(keep); m2_ += q * sum(keep) ** 2
VNp = m2_ - m1_ ** 2
gen = sum(p * sum(fs[s_] * (1 - fs[s_]) for s_ in st) for (n_, st), p in law.items())
ES = sum(p * sum(1 - fs[s_] for s_ in st) for (n_, st), p in law.items()); VS = sum(p * sum(1 - fs[s_] for s_ in st) ** 2 for (n_, st), p in law.items()) - ES ** 2
fbar = 1 - m1_ / EN; ef12 = (1 - fbar) ** 2 * VN + fbar * (1 - fbar) * EN
rep("GAP-EF-v2-C16b state-dependent capture: general Var N' law exact; (EF12) with mean f is off (needs energy-independent f)",
    abs(VNp - (gen + VS)) < 1e-12 and abs(VNp / ef12 - 1) > 0.05, f"Var N'={VNp:.4f}, general={gen+VS:.4f}, (EF12)={ef12:.4f}")
# C17 hydrogenic (Wannier) exciton estimates [E]: E_x^b = 13.606 mu*/eps_r^2 eV (eps_r [UNVERIFIED], CSV masses [DB])
Ry = 13.605693; ex = lambda me, mh, er: Ry * (me * mh / (me + mh)) / er ** 2
vals = {"GaN": ex(0.19, 1.647, 9.5), "ZnO": ex(0.22, 2.34, 8.1), "4H-SiC": ex(0.47, 1.353, 9.8)}
rep("GAP-EF-v2-C17 hydrogenic E_x^b [E]: GaN 26, ZnO 42, 4H-SiC 49 meV (+-1 meV)",
    all(abs(1e3 * vals[k] - v) < 1 for k, v in (("GaN", 26), ("ZnO", 42), ("4H-SiC", 49))), " ".join(f"{k} {1e3*v:.0f} meV" for k, v in vals.items()))
# C18 every cited arXiv ID has an API record (literature/papers-GAP-EF or papers-GAP-EF-v2)
lits = [os.path.join(HERE, "..", "..", "literature", dd) for dd in ("papers-GAP-EF", "papers-GAP-EF-v2")]
ids = ["2610.16949", "0911.1532", "2311.03902", "1602.08005", "2202.03924", "2311.05011", "2004.11499", "2305.09005", "1909.05806",
       "2411.12320", "2308.03893", "1901.07569", "2004.10709", "2008.08560", "1910.10716", "1902.02687"]
okl = True
for i in ids:
    found = False
    for lit in lits:
        try:
            pp = json.load(open(os.path.join(lit, f"arxiv-{i}.json")))["papers"]; found |= bool(pp) and pp[0]["id"].startswith(i)
        except Exception:
            pass
    okl &= found
rep("GAP-EF-v2-C18 arXiv IDs verified against the API (arxiv-*.json present, IDs match)", okl, f"{len(ids)} IDs")
# C19 the renewal (final-state) estimate is BELOW F in every computed case (K1): ratio range as quoted [0.12, 0.88]
cases = {"RPP": T1["RPP"], "lam0 th=1": T1["lam0_th1"], "lam0 th=3/2": T1["lam0_th15"], "Si V0": V0["Si"], "Si V1": J["variants"]["V1"]["Si"],
         "Si V3": J["variants"]["V3"]["Si"], "Ge": J["Ge_decomp"]}
rat = {k: v["F_ren"] / v["F"] for k, v in cases.items()}
rep("GAP-EF-v2-C19 F_ren < F_eh in all computed cases; F_ren/F in [0.12, 0.88]", all(0.12 < r < 0.88 for r in rat.values()),
    " ".join(f"{k}:{r:.2f}" for k, r in rat.items()))
# C20 grid fix (REF-B 2.7): every validation and prediction row has |w_eff/w - 1| < 1%; CsI ran on N >= 600; grid() raises outside tol
rows = [r_[v] for blk in ("validation", "validation_ext", "validation_lit", "predictions") for r_ in J[blk].values() for v in ("V0", "V1", "V3")]
werr = max(abs(r_["w_eff"] / r_["w"] - 1) for r_ in rows)
try:
    grid(0.00163, Nmax=300, tol=1e-6); raised = False
except ValueError:
    raised = True
rep("GAP-EF-v2-C20 omega_0 on the grid for every row (max |w_eff/w - 1| < 1%); CsI N >= 600; grid() fails loudly",
    werr < 0.01 and J["predictions"]["CsI"]["V0"]["N"] >= 600 and raised, f"max err {100*werr:.2f}%, CsI N={J['predictions']['CsI']['V0']['N']}")
# C21 (EF13) against WP5-v4 (W4'): H_eff = omega - N_eh E_g is unchanged by excitons (N_eh = N_e^f + N_X); the bare heat is
#     H = H_eff + N_X E_x^b, Var H = Var H_eff + E_x^b^2 Var N_X + 2 E_x^b Cov(H_eff, N_X)  (exact enumeration, toy joint law)
Exb = 0.3; jl = {(2.0, 0): 0.3, (2.5, 1): 0.25, (3.0, 1): 0.25, (2.2, 2): 0.2}   # (H_eff, N_X): probability
E_ = lambda g: sum(p * g(a, b) for (a, b), p in jl.items())
VHe = E_(lambda a, b: a * a) - E_(lambda a, b: a) ** 2; VNX = E_(lambda a, b: b * b) - E_(lambda a, b: b) ** 2
CHN = E_(lambda a, b: a * b) - E_(lambda a, b: a) * E_(lambda a, b: b)
VHb = E_(lambda a, b: (a + Exb * b) ** 2) - E_(lambda a, b: a + Exb * b) ** 2
rep("GAP-EF-v2-C21 (EF13): bare heat H = H_eff + N_X E_x^b; variance identity exact; mean shift +<N_X>E_x^b", abs(VHb - (VHe + Exb ** 2 * VNX + 2 * Exb * CHN)) < 1e-12
    and abs(E_(lambda a, b: a + Exb * b) - E_(lambda a, b: a) - Exb * E_(lambda a, b: b)) < 1e-12)
# C22 4H-SiC: the 2005 limit F <= 0.04 lies below every F computed for this model class (minimum over all computed cases >= 0.051)
allF = [v["F"] for v in cases.values()] + [r_["F"] for r_ in rows] + [r_["Wv"]["F"] for r_ in J["predictions"].values() if "Wv" in r_]
F4H = [J["validation"]["4H-SiC"][v]["F"] for v in ("V0", "V1", "V3")]
rep("GAP-EF-v2-C22 4H-SiC: model F (V0, V1, V3) > 0.04; min F over all computed cases >= 0.051 (RPP)", min(F4H) > 0.04 and min(allF) >= 0.0510,
    f"4H F = {', '.join(f'{x:.3f}' for x in F4H)}; min F = {min(allF):.4f}")
# C23 (errata V-2, rebuttal R2) (EF8) eps/E_g = 1 + 2 rbar_c + <H_>>/n. At lam = 0 the grid point x = E_g has Phi(0) = 0, so p = 0 and
#     cascade.py l.74 takes the phonon branch (one step h) even with phonon=False: a spurious <H_>> that is O(h^2) per carrier (deposit h x
#     hit probability O(h)). (i) Per grid, (EF8) with that term booked is exact (1e-12). (ii) Pc(0.01)/Pc(0.005) in [3.8, 4.2] (O(h^2)).
#     (iii) Richardson for an O(h) scheme maps c h^2 to -c h^2/2 (sympy), so the extrapolated row inherits -Pc(0.01)/2 (within 5%).
#     (iv) json Richardson rows: |eps - 1 - 2 rbar| < 5e-4 (theta = 1; observed 1.8e-4) and < 1e-8 (theta = 3/2: no artefact, nth > nG).
def _slopes(c, frac=0.5):
    sel = c.x >= frac * c.x[-1]; om = 1.0 + c.x[sel]; A = np.vstack([om, np.ones_like(om)]).T
    sl = lambda y: np.linalg.lstsq(A, y[sel], rcond=None)[0][0]
    mN, mR, mP, mC = (sl(c.res[k][0][0]) for k in ("N", "R", "P", "C"))
    return dict(eps=1 / mN, rbar=mR / mC, Pc=mP / mC, cpp=mC / mN, VP=sl(c.var("P")) / mN)
ga, gb = _slopes(L0a), _slopes(L0b)
hh, cc = sp.symbols("h c", positive=True); rich = sp.simplify(2 * (cc * (hh / 2) ** 2) - cc * hh ** 2)
exact_grid = all(abs(g["eps"] - 1 - 2 * (g["rbar"] + g["Pc"])) < 1e-12 and abs(g["cpp"] - 2) < 1e-9 for g in (ga, gb))
ratio = ga["Pc"] / gb["Pc"]; PcR = 2 * gb["Pc"] - ga["Pc"]
ok = (exact_grid and 3.8 < ratio < 4.2 and sp.simplify(rich + cc * hh ** 2 / 2) == 0 and abs(PcR / (-ga["Pc"] / 2) - 1) < 0.05
      and abs(T1["lam0_th1"]["eps"] - 1 - 2 * T1["lam0_th1"]["rbar"]) < 5e-4 and abs(T1["lam0_th15"]["eps"] - 1 - 2 * T1["lam0_th15"]["rbar"]) < 1e-8
      and all(abs(T1[k]["carriers_per_pair"] - 2) < 1e-9 for k in ("lam0_th1", "lam0_th15")))
rep("GAP-EF-v2-C23 (EF8) exact per grid with the O(h^2) threshold artefact booked; Richardson rows 5e-4 (th=1), 1e-8 (th=3/2)", ok,
    f"Pc={ga['Pc']:.2e},{gb['Pc']:.2e} (x{ratio:.2f}); Rich Pc={PcR:.2e}; th=1 defect {T1['lam0_th1']['eps']-1-2*T1['lam0_th1']['rbar']:.1e}")
# C24 fit-edge bias of scan.py (X = 25): lam = 100, w = 0.05, X = 25 vs X = 60; quoted ~1% in F, 0.2-0.3% in eps
r25, r60 = run(100.0, 1.0, 0.05, X=25.0, Nmax=300, nwmin=1), run(100.0, 1.0, 0.05, X=60.0, Nmax=300, nwmin=1)
bF, be = r25["F"] / r60["F"] - 1, r25["eps"] / r60["eps"] - 1
rep("GAP-EF-v2-C24 scan fit-edge bias at lam = 100: |dF/F| < 1.5%, |d eps/eps| < 0.4% (inside the 2.3% / 0.52% fit budgets)",
    abs(bF) < 0.015 and abs(be) < 0.004, f"dF/F={bF:+.4f} deps/eps={be:+.4f}")
# C25 k2 = c1 (A omega_0^g)^b E_g^(1-(3+g)b) over the prediction rows' (E_g, omega_0): range 1.2-2.5 eV
#     (REF-B 2.5 quoted 1.2-2.3, REF-A 1.2-2.6; the E_g^0.05 factor lifts SiO2 and C to 2.5). Inside the (EF9) domain: 1.5-2.5 eV
k2 = [pe[1] * (A0 * r_["om0"] ** pe[2]) ** pe[3] * r_["Eg"] ** (1 - (3 + pe[2]) * pe[3]) for r_ in J["predictions"].values()]
k2f = lambda Eg, om: pe[1] * (A0 * om ** pe[2]) ** pe[3] * Eg ** (1 - (3 + pe[2]) * pe[3])
ind = [k2f(r_["Eg"], r_["om0"]) for r_ in J["predictions"].values() if 0.01 <= r_["om0"] / r_["Eg"] <= 0.1 and 0.003 <= A0 / r_["Eg"] ** 3 <= 100]
rep("GAP-EF-v2-C25 k2 spans 1.20-2.53 eV over the survivors (1.50-2.53 in the fit domain); k2(Si) = 1.87 eV (errata V-13)",
    abs(min(k2) - 1.196) < 0.005 and abs(max(k2) - 2.534) < 0.005 and abs(min(ind) - 1.505) < 0.005 and abs(k2f(1.164, 0.063) - 1.871) < 0.002,
    f"k2 in [{min(k2):.3f}, {max(k2):.3f}], in-domain min {min(ind):.3f}, Si {k2f(1.164, 0.063):.3f} eV")
# C26 (errata V-3) (EF12) ledger: with N_eh = N_e^f + N_X, a captured electron lowers N_eh by 1, so H_eff = omega - N_eh E_g - E_st - E_esc rises by
#     exactly E_g; WP7-E-v3 (E1-pr) books it as (E_c - E_j) to H, (E_j - mu_F) to E_trap^pr, (mu_F - E_v) to E_pairs^unp (sympy)
Ec, Ev, Ej, muF, om_, Ne, Nh, NX, Hh, Etr = sp.symbols("E_c E_v E_j mu_F omega N_e N_h N_X H E_tr", real=True)
Eg_ = Ec - Ev
Heff = lambda ne, nx: om_ - (ne + nx) * Eg_
rhs = lambda ne, nh, H, Et: H + Et + (nh - ne) * (muF - Ev)         # H + E_trap^pr + E_pairs^unp (E_es = E_X^b = W_bias = 0)
dL = sp.simplify(Heff(Ne - 1, NX) - Heff(Ne, NX)); dR = sp.simplify(rhs(Ne - 1, Nh, Hh + (Ec - Ej), Etr + (Ej - muF)) - rhs(Ne, Nh, Hh, Etr))
rep("GAP-EF-v2-C26 (EF12) ledger: H_eff rises by exactly E_g per captured electron, split H / E_trap^pr / E_pairs^unp (any E_j, mu_F)",
    sp.simplify(dL - Eg_) == 0 and sp.simplify(dR - Eg_) == 0, f"dH_eff = {dL}")
# C27 (errata V-7) beta-Ga2O3 at the Gamma-point maximum LO frequency 764.26 cm^-1 [FT 1902.02687 Table I p.8] = 94.76 meV instead of the
#     zone-edge maximum 784.92 cm^-1 = 97.32 meV: the convention mix moves the model by < 0.3% and the +56% residual by < 0.5 points
cm2meV = 0.12398419843
rG = run(A0, 4.8, 764.26 * cm2meV * 1e-3); e0 = J["validation_ext"]["b-Ga2O3"]["V0"]["eps"]
rep("GAP-EF-v2-C27 beta-Ga2O3 with omega_0 = Gamma-LO max (94.76 meV): |d eps|/eps < 0.3%, residual change < 0.5 points",
    abs(764.26 * cm2meV - 94.76) < 0.01 and abs(784.92 * cm2meV - 97.32) < 0.01 and abs(rG["eps"] / e0 - 1) < 3e-3 and abs(15.6 / rG["eps"] - 15.6 / e0) < 5e-3,
    f"eps {rG['eps']:.3f} vs {e0:.3f} eV; residual {100*(15.6/rG['eps']-1):+.1f}% vs {100*(15.6/e0-1):+.1f}%")
# C28 (rebuttal R3) 10 meV kernel bins: the off-grid fraction |10 round(w/10) - w|/w on [10, 20] meV peaks at 1/3 (w = 15), not 50%;
#     over the survivors the worst rows are PbTe 26% and PbSe 17%; CsI and NaI (10.0, 20.0 meV) are on the grid
wv = sp.symbols("w", positive=True)
mx = max(sp.maximum((wv - 10) / wv, wv, sp.Interval(10, 15)), sp.maximum((20 - wv) / wv, wv, sp.Interval(15, 20)))
offg = {k: abs(10 * max(1, round(1e3 * r_["om0"] / 10)) - 1e3 * r_["om0"]) / (1e3 * r_["om0"]) for k, r_ in J["predictions"].items()}
worst = sorted(offg, key=offg.get)[-2:]
rep("GAP-EF-v2-C28 10 meV bins: max off-grid fraction on [10, 20] meV = 1/3; survivors' worst PbTe 26%, PbSe 17%; CsI, NaI < 3%",
    mx == sp.Rational(1, 3) and worst == ["PbSe", "PbTe"] and abs(offg["PbTe"] - 0.26) < 0.01 and offg["CsI"] < 0.03 and offg["NaI"] < 0.03,
    f"max={mx}; PbTe {offg['PbTe']:.2f}, PbSe {offg['PbSe']:.2f}, CsI {offg['CsI']:.3f}, NaI {offg['NaI']:.3f}")
# C29 (errata V-4) ab initio vs model residuals (meas/calc - 1) per material, as typed from sec. 2 / sec. 5: ab initio is worse for SiO2 and 4H-SiC
ai = {"C": (12.95, 12.87), "3C-SiC": (6.90, 6.6), "GaN": (9.59, 8.9), "b-Ga2O3": (15.6, 11.24), "4H-SiC": (7.83, 7.3), "SiO2": (18.0, 16.7)}
mod = {k: (MEAS.get(k) or MEXT.get(k)) / (J["validation"].get(k) or J["validation_ext"].get(k))["V0"]["eps"] - 1 for k in ai}
worse = sorted(k for k in ai if abs(ai[k][0] / ai[k][1] - 1) > abs(mod[k]))
rep("GAP-EF-v2-C29 ab initio residual larger than the model's exactly for {4H-SiC, SiO2} (SiO2 +7.8% vs +3.4%)",
    worse == ["4H-SiC", "SiO2"] and pc(ai["SiO2"][0] / ai["SiO2"][1] - 1) == 7.8 and pc(mod["SiO2"]) == 3.4,
    " ".join(f"{k} {100*(a/b-1):+.1f}/{100*mod[k]:+.1f}" for k, (a, b) in ai.items()))

print(f"{sum(RES)}/{len(RES)} PASS, {time.time() - t0:.0f} s")
sys.exit(0 if all(RES) else 1)
