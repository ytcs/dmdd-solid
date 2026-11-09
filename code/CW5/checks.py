"""R16 / CW5 closure checks, revised for returns/R16/CW5-errata.md (sympy + numpy + scipy; target < 2 min).
Cited in returns/R16/CW5.md as CW5-Cn and in CW5-errata.md as CW5-Cn (revised) and ERR-CW5-Cn (new).
No first-principles numerics.  WP5-AUD's FOM function is COPIED from code/WP5-AUD/checks.py (lines 116-125), not imported,
because that file runs its own checks on import.  Literature records are read from literature/papers-CW5/ and literature/papers-ERR-CW5/.

Errata revision (ERR-CW5):
 * tolerances: every quoted number is checked to half a unit of its last quoted digit (TOL(x) below); Monte Carlo checks use
   4 standard errors computed from the sample, not a fixed slack;
 * circular checks removed: old C6b (compared n0/(1+Cn0 t) with itself) -> ODE integration of r_g = (E_pairs + E_X)/(N E_g);
   old C8b (restated its own algebra) -> numerical Born limit on the 1D chain + spin counting; C18 is labelled BOOKKEEPING;
 * C3 now samples X^oth_ER < 0 (the verifier's counterexample) and checks the sharpened bound;
 * new checks ERR-CW5-C1 ... C9 for each correction of the errata.
"""
import math, os, time
import numpy as np, sympy as sp
from scipy.linalg import eigh_tridiagonal, expm
from scipy.special import gammaln
from scipy.integrate import quad, solve_ivp
T0 = time.time(); RES = []
TL = [time.time()]
def rep(name, ok, note=""):
    dt = time.time() - TL[-1]; TL.append(time.time()); note = (note + f"; {dt:.1f}s") if note else f"{dt:.1f}s"
    RES.append(bool(ok)); print(("PASS " if ok else "FAIL ") + name + (f"  [{note}]" if note else ""))
def TOL(v, quoted):
    """|v - quoted| <= half a unit of the last digit of the quoted string (rounding-consistent check)."""
    s = quoted.split('e')[0]; dec = len(s.split('.')[1]) if '.' in s else 0
    scale = 10**int(quoted.split('e')[1]) if 'e' in quoted else 1
    return abs(v - float(quoted)) <= 0.5*10**(-dec)*scale*(1 + 1e-9)

# ---------------------------------------------------------------- C1 (LE-22, D-1): exact zero-field Y_H shift from unrelaxed gap energy
yy, G = 0.102, 1.17/3.75
ratio = (1 - yy*G)/(1 - G); first = (1 - yy)*G
G38 = 1.17/3.8; ratio38 = (1 - yy*3.75/3.8*G38)/(1 - G38)
rep("CW5-C1 D-1: Y_H(r_g=1)/Y_H(r_g=0) = (1-yG)/(1-G) = 1.407 vs first-order 0.280; 1.400 with the source eps = 3.8 eV",
    TOL(ratio, "1.407") and TOL(first, "0.280") and TOL(ratio38, "1.400"), f"{ratio:.5f}, {first:.5f}, {ratio38:.5f}")
Rn, Re_, d = sp.symbols('r_n r_e delta'); y_, G_ = sp.symbols('y G', positive=True); rr = sp.Symbol('r')
YH = (1 - d)*(1 - y_*G_*Rn)/(1 - G_*Re_)
rep("CW5-C1b exact Y_H with separate r_g^NR, r_g^ER: = 1 - delta_coll at r_g = 0; first-order term (1-y)G r_g at r_n = r_e = r",
    sp.simplify(YH.subs({Rn: 0, Re_: 0}) - (1 - d)) == 0 and
    sp.simplify(sp.series(YH.subs({d: 0, Rn: rr, Re_: rr}), G_, 0, 2).removeO() - (1 + (1 - y_)*G_*rr)) == 0)

# ---------------------------------------------------------------- C2 (LE-22, D-7): WP8-R HV figure of merit, eps convention and <q>
eps_si = 3.75
def fom(ER, Vb, C, da, yy, sigE=2.65, F_ER=0.15, F_NR=1.0, q=1.0):          # copied verbatim from code/WP5-AUD/checks.py
    gg = q*Vb/eps_si
    Etot = ER*(1 + yy*gg); E_er = Etot/(1 + gg)
    n_nr, n_er = yy*ER/eps_si, E_er/eps_si
    dO = C*(gg/(1 + gg) - yy*gg/(1 + yy*gg)); sn = sigE/Etot
    s_nr = math.sqrt(sn**2 + da**2 + (C*q*Vb*math.sqrt(F_NR*n_nr)/Etot)**2)
    s_er = math.sqrt(sn**2 + da**2 + (C*q*Vb*math.sqrt(F_ER*n_er)/Etot)**2)
    return dO/math.sqrt(0.5*(s_nr**2 + s_er**2))
def S(ER, Y, FER, FNR, q, src=False):   # src=True: source definition <n_eh> = Y E_r / 3.8 (2303.02196 Eq. (1)) -> Y_eff = Y*3.75/3.8
    return fom(ER, 100, 1.0, 0.0, Y*(eps_si/3.8 if src else 1.0), 1e-9, FER, FNR, q)
a = S(300, 0.098, 0.119, 0.4, 0.873); b = S(300, 0.098, 0.119, 0.4, 0.873, True); c = S(300, 0.098, 0.119, 0.4, 1.0)
e1 = S(300, 0.12, 0.15, 0.15, 1.0); e2 = S(300, 0.12, 0.15, 0.15, 1.0, True); f2 = S(220, 0.088, 0.119, 0.3, 0.873, True)
def Fstar(q, src=False):
    lo, hi = 0.01, 3.0
    for _ in range(60):
        m = 0.5*(lo + hi); (lo, hi) = (m, hi) if S(300, 0.098, 0.119, m, q, src) > 2 else (lo, m)
    return 0.5*(lo + hi)
fs = [Fstar(q) for q in (1.0, 0.873, 0.8)]; fs_src = [Fstar(q, True) for q in (1.0, 0.873, 0.8)]
rep("CW5-C2 D-7: 1sigma corner 1.9986 (eps 3.75) -> 2.014 (source eps 3.8) > 2; 1.763 at <q> = 1; energy-matched C7c' 1.993/2.008; "
    "220 eV joint 2sigma corner 2.015; F_NR* = 0.275/0.399/0.498 (eps 3.75) and 0.28/0.41/0.51 (eps 3.8) at <q> = 1/0.873/0.8",
    TOL(a, "1.9986") and TOL(b, "2.014") and TOL(c, "1.763") and TOL(e1, "1.993") and TOL(e2, "2.008") and TOL(f2, "2.015")
    and all(TOL(x, t) for x, t in zip(fs, ("0.275", "0.399", "0.498"))) and all(TOL(x, t) for x, t in zip(fs_src, ("0.28", "0.41", "0.51"))),
    f"{a:.5f} {b:.5f} {c:.5f} {e1:.5f} {e2:.5f} {f2:.5f} F*={[round(x,4) for x in fs]} F*_src={[round(x,4) for x in fs_src]}")
# ERR-CW5-C1 (VER row 8): the 1sigma corners at the two measured points below 300 eV (2303.02196 Table II as quoted in WP5-AUD §3.3)
c220 = S(220, 0.098, 0.119, 0.4, 0.873, True)                                   # Y = 0.108 - 0.010, F_NR = 0.5 - 0.1
scan220 = [S(220, Y, 0.119, 0.4, 0.873, True) for Y in (0.085, 0.10)]
c100 = S(100, 0.072, 0.119, 0.5, 0.873, True)                                   # Y = 0.102 - 0.030, F_NR = 0.9 - 0.4
corners = [S(E, Y, 0.119, F, 0.873, True) for E, Ys, Fs in ((220, (0.098, 0.117), (0.4, 0.7)), (100, (0.072, 0.136), (0.5, 1.6)))
           for Y in Ys for F in Fs]
rep("ERR-CW5-C1 OC-7 support: 1sigma corner at 220 eV = 1.72 (Y in [0.085, 0.10], F_NR 0.4: 1.70-1.87, VER V6); at 100 eV = 1.27; "
    "all 1sigma corners at 100 and 220 eV < 2 (eps 3.8, <q> 0.873, F_ER 0.119)",
    TOL(c220, "1.72") and TOL(scan220[1], "1.70") and TOL(scan220[0], "1.87") and TOL(c100, "1.27") and max(corners) < 2,
    f"220: {c220:.4f}, scan {scan220[1]:.4f}-{scan220[0]:.4f}; 100: {c100:.4f}; max corner {max(corners):.4f}")

# ---------------------------------------------------------------- C3 (LE-22, L38): closed-form bound, now with X^oth_ER of either sign
g, r, yv, e, X, x, dl = sp.symbols('g r y e X x delta', real=True)
kap = (1 + r*g*yv)/(1 + r*g)
SER = 1 - X + r*g; dNR = e + kap*X + x; SNR = (1 - dl)*(1 - dNR) + r*g*yv
eta = (1 + g)*SNR/SER - g*yv
f = sp.simplify((1 - e - eta)*SER)
f0 = sp.simplify(f.subs({x: 0, dl: 0}))
ok_split = sp.simplify(f - f0 - (1 + g)*(dl*(1 - e - kap*X) + x*(1 - dl))) == 0          # exact: f = f0 + (1+g)[delta(1-e-kX) + x(1-delta)]
okl = sp.simplify(sp.diff(f0, e, 2)) == 0
oke0 = sp.simplify(f0.subs(e, 0) - g*(r - 1)*(1 - yv)*(1 - X/(1 + r*g))) == 0
oke1 = sp.simplify(f0.subs(e, 1 - yv) - (1 - yv)*X*(1 + g)/(1 + r*g)) == 0
okr1 = sp.simplify(f0.subs(r, 1) - X*e) == 0                                               # VER §1.1: f0|_{r=1} = X e exactly
f0l = sp.lambdify((g, r, yv, X, e), f0); fl = sp.lambdify((g, r, yv, X, e, x, dl), f); SERl = sp.lambdify((g, r, X), SER)
cex = (f0l(1.047, 1.1, 0.3, -0.01, 0.06), f0l(1.047, 1.1, 0.3, -0.01, 0.69))               # VER counterexample
rng = np.random.default_rng(1); worst_pos = 1.0; worst_sharp = 1.0
for _ in range(20000):
    gv, rv, yv_ = rng.uniform(0.1, 30), rng.uniform(1, 3), rng.uniform(0, 1)
    Xv = rng.uniform(-0.2, 1.0); ev = rng.uniform(0, 1 - yv_)
    kv = (1 + rv*gv*yv_)/(1 + rv*gv); xmax = max(0.0, 1 - ev - kv*Xv)                      # domain d'_NR <= 1
    xv, dv = rng.uniform(0, xmax), rng.uniform(0, 1)
    fv = float(fl(gv, rv, yv_, Xv, ev, xv, dv)); Sv = float(SERl(gv, rv, Xv))
    corr = ev*max(-Xv, 0.0)*(1 + gv)/(1 + rv*gv)                                           # sharpened: f >= -e X^-(1+g)/(1+rg)
    worst_sharp = min(worst_sharp, (fv + corr)/Sv)
    if Xv >= 0: worst_pos = min(worst_pos, fv/Sv)
rep("CW5-C3 (revised) L38: f = f0 + (1+g)[delta(1-e-kappa X) + x(1-delta)] exactly; f0 linear in e, f0(0) = g(r-1)(1-y)(1-X/(1+rg)), "
    "f0(1-y) = (1-y)X(1+g)/(1+rg), f0|_{r=1} = X e; bound exact for X >= 0; VER counterexample (X = -0.01) f0 = +0.067 -> -0.0055; "
    "sharpened bound 1 - e - eta >= -e X^-(1+g)/[(1+rg)S_ER] holds on 20000 points with X in [-0.2, 1]",
    ok_split and okl and oke0 and oke1 and okr1 and TOL(cex[0], "0.067") and TOL(cex[1], "-0.0055") and worst_pos >= -1e-12
    and worst_sharp >= -1e-12, f"cex {cex[0]:.4f}/{cex[1]:.5f}; min over X>=0 {worst_pos:.2e}; min sharpened {worst_sharp:.2e}")

# ---------------------------------------------------------------- C4 (LE-133): defecton diffusion D_T ∝ T^-9 (exponent only)
k, q1, q2, J, a_, w = sp.symbols('k q1 q2 J a omega', real=True)
eps = lambda kk: -2*J*sp.cos(kk*a_)
d1 = eps(k + q1) - eps(k); d2 = eps(k - q2) - eps(k); wp = w + eps(k) - eps(k + q1 - q2)       # on-shell outgoing energy
br = 1/(w - d1) - 1/(wp + d2)
lead = sp.series(br.subs(J, sp.Symbol('t')*J), sp.Symbol('t'), 0, 2).removeO().subs(sp.Symbol('t'), 1)
second_diff = eps(k + q1) + eps(k - q2) - eps(k) - eps(k + q1 - q2)
ok_cancel = sp.simplify(lead - second_diff/w**2) == 0
sd_small = sp.series(second_diff.subs({q1: sp.Symbol('s')*q1, q2: sp.Symbol('s')*q2}), sp.Symbol('s'), 0, 3).removeO()
ok_q2 = sp.simplify(sd_small - (2*J*a_**2*sp.cos(k*a_)*sp.Symbol('s')**2*q1*q2)) == 0
I = lambda T: quad(lambda om: om**8/(math.exp(om/T) - 1.0), 0, 60*T, epsabs=0, epsrel=1e-12)[0]
p9 = math.log(I(2.0)/I(1.0), 2)
rep("CW5-C4 LE-133: linear-coupling two-phonon amplitude cancels to the second difference of eps(k) (= +2Ja^2 cos(ka) q q' + ...); "
    "transport rate ∝ T^9 (=> exponent of D_T is -9; prefactor not checked)", ok_cancel and ok_q2 and abs(p9 - 9) < 1e-9,
    f"log2 ratio = {p9:.10f}")

# ---------------------------------------------------------------- C5 (LE-143): renewal toys and the many-to-one (tagged-unit) representation
h = 0.004; Eg = np.arange(0, 30, h); fx = Eg*np.exp(-Eg)          # gamma(2,1): mu = 2, sigma^2 = 2
m = np.zeros_like(Eg)
for i in range(len(Eg)):
    m[i] = 1.0 + (h*np.dot(m[i-1::-1], fx[1:i+1]) if i > 0 else 0.0)
lim = m[-1] - Eg[-1]/2.0
dd = 1.0; Es = np.array([10.25, 10.75]); md = np.floor(Es/dd) + 1; per = md - Es/dd
rng = np.random.default_rng(7); xs = 6.0; n = 40000; samp = np.empty(n)
for jj in range(n):
    y = xs; s = 0.0
    while y >= 1.0:
        s += 1.0/y; y *= math.sqrt(rng.random())                     # size-biased fraction, density 2v on [0,1]
    samp[jj] = xs*s
mc, se = samp.mean(), samp.std(ddof=1)/math.sqrt(n)
rep("CW5-C5 LE-143 (toys only; not evidence for the branching limit): (a) non-lattice renewal limit (s^2+mu^2)/(2mu^2) = 0.75 "
    "(O(h) quadrature); (b) lattice loss leaves 1-{E/d}; (c) tagged-unit formula reproduces N_ev = 2x - 1 = 11 within 4 SE",
    abs(lim - 0.75) < 2e-3 and abs(per[0] - 0.75) < 1e-12 and abs(per[1] - 0.25) < 1e-12 and abs(mc - 11.0) < 4*se,
    f"lim {lim:.5f}; MC {mc:.4f} ± {se:.4f}")
# ERR-CW5-C2 (VER row 12, (r4')): lineage with a summable O(a/x) kernel perturbation (killing prob a/x per event) still has a limit of
# h(x) = E[sum_j 1/x_j]; Cauchy differences decay like 1/x.  Log-grid trapezoid solution of h(x) = 1/x + (1 - a/x) ∫ 2v h(vx) dv.
def hsolve(aK, ymax=14.0, dy=0.002):
    ys = np.arange(0, ymax + dy/2, dy); hh = np.zeros_like(ys); ker = 2*np.exp(2*(-ys))*dy      # ker[j]: weight at u = -j dy
    ker[0] *= 0.5
    for i in range(len(ys)):
        surv = 1 - min(1.0, aK*np.exp(-ys[i]))
        kk = ker[:i+1].copy(); kk[-1] *= (0.5 if i > 0 else 1.0)                        # trapezoid ends
        acc = np.dot(kk[1:], hh[i-1::-1][:i]) if i > 0 else 0.0
        hh[i] = (np.exp(-ys[i]) + surv*acc)/(1 - surv*kk[0])
    return ys, hh
ys0, h0 = hsolve(0.0); ysA, hA = hsolve(0.5)
xg = np.exp(ys0); ok_a0 = np.max(np.abs(h0[xg > 2] - (2 - 1/xg[xg > 2]))) < 1e-4
dA = hA - h0                                                          # perturbation part; grid error of the common kernel cancels
pts = [int(round(math.log(2.0**kq)/0.002)) for kq in (8, 10, 12, 14, 16)]
dif = [abs(dA[pts[i+1]] - dA[pts[i]]) for i in range(len(pts) - 1)]
rep("ERR-CW5-C2 (r4') mechanism: with killing a/x (a = 0.5) the tagged-unit sum h(x) converges; |Δh(4x) - Δh(x)| shrinks ~ x^-1 for x = 2^8...2^16 (Δh = h_a - h_0) "
    "(a = 0 reproduces 2 - 1/x)", ok_a0 and all(dif[i+1] < 0.35*dif[i] for i in range(len(dif) - 1)) and dif[-1] < 5e-5,
    f"h(2^20) = {hA[pts[-1]]:.5f}; h_a - h_0 diffs {['%.1e' % v for v in dif]}")

# ---------------------------------------------------------------- C6 (LE-141, GAP-LEE): zero-field gap-energy release, linear kinetics
kFX, kFT, kXB, kXh, kBh, eta_l, eta_B = 1/2e-9, 1/50e-9, 1/30e-9, 1/1e-6, 1/300e-9, 0.02, 0.01   # illustrative rates [E], not data
M = np.array([[-(kFX + kFT), 0, 0], [kFX, -(kXB + kXh), 0], [0, kXB, -kBh]])           # states F (free pair), X, BX; lower triangular
def rg(t): return float(np.ones(3) @ expm(M*t) @ np.array([1.0, 0, 0]))
bT = kFT/(kFX + kFT)
occ_int = -np.linalg.solve(M, np.array([1.0, 0, 0]))
heat = kXh*(1 - eta_l)*occ_int[1] + kBh*(1 - eta_B)*occ_int[2]; light = kXh*eta_l*occ_int[1] + kBh*eta_B*occ_int[2]; trap = kFT*occ_int[0]
light_an = (1 - bT)*(kXh*eta_l + kXB*eta_B)/(kXh + kXB)
lam, V = np.linalg.eig(M); wk = (np.ones(3) @ V)*np.linalg.solve(V, np.array([1.0, 0, 0]))
rep("CW5-C6 (revised) LE-141: r_g = Σ w_k e^{-γ_k t}, Σ w_k = 1, γ_k = diagonal of the lower-triangular M; split heat + light + trap = 1, "
    "trap = b_trap, light = (1-b_trap)(k_X↓η_X + Σk_XB η_B)/(k_X↓ + Σk_XB) (BX light fraction η_B as a parameter); some w_k < 0",
    rg(1e-3) < 1e-12 and abs(rg(0) - 1) < 1e-12 and abs(light - light_an) < 1e-12 and abs(heat + light + trap - 1) < 1e-12
    and abs(trap - bT) < 1e-12 and abs(wk.sum() - 1) < 1e-10 and wk.real.min() < 0
    and np.allclose(sorted(-lam.real), sorted(-np.diag(M))),
    f"w_k = {['%.3f' % v for v in wk.real]}; heat {heat:.4f}, light {light:.4f}, trap {trap:.4f}")
# ERR-CW5-C3 (VER row 17): degenerate rates give t e^{-γt} (M not diagonalisable); sequential transfer without loss gives a negative weight
tt_, aa, bb = sp.symbols('t a b', positive=True)
Mab = sp.Matrix([[-aa, 0], [aa, -bb]]); r2 = sp.simplify((sp.ones(1, 2)*(Mab*tt_).exp()*sp.Matrix([1, 0]))[0])
Maa = sp.Matrix([[-aa, 0], [aa, -aa]]); r2d = sp.simplify((sp.ones(1, 2)*(Maa*tt_).exp()*sp.Matrix([1, 0]))[0])
rep("ERR-CW5-C3 Theorem CW5-G hypotheses: F->X (rate a, no loss) -> decay b gives r_g = [a e^{-bt} - b e^{-at}]/(a - b) (weight -b/(a-b) < 0 "
    "for a > b); a = b gives (1 + a t) e^{-at}",
    sp.simplify(r2 - (aa*sp.exp(-bb*tt_) - bb*sp.exp(-aa*tt_))/(aa - bb)) == 0 and sp.simplify(r2d - (1 + aa*tt_)*sp.exp(-aa*tt_)) == 0)
# CW5-C6b (REPLACED; old version was circular): integrate r_g = n_F + n_X (gap energy in E_pairs + E_X), not n_F
def ivp(fun, y0, ts):
    return solve_ivp(fun, (0, ts[-1]), y0, t_eval=ts, rtol=1e-11, atol=1e-14, method='LSODA').y
ts = np.array([1.0, 10.0, 100.0])
Y1 = ivp(lambda t, y: [-y[0]**2, y[0]**2 - 1e-3*y[1]], [1.0, 0.0], ts); rg_slow = Y1[0] + Y1[1]   # C_X n0 = 1, k_X↓ = 1e-3 /t0
Y2 = ivp(lambda t, y: [-y[0]**2, y[0]**2 - 1e3*y[1]], [1.0, 0.0], ts); rg_fast = Y2[0] + Y2[1]    # k_X↓ = 1e3 /t0 >> C_X n
kk_, gg_ = 0.05, 1.0                                                                               # annihilation + linear loss
Y3 = ivp(lambda t, y: [-kk_*y[0] - gg_*y[0]**2], [1.0], ts)[0]
an3 = np.exp(-kk_*ts)/(1 + (gg_/kk_)*(1 - np.exp(-kk_*ts)))
Y4 = ivp(lambda t, y: [-y[0]**3], [1.0], ts)[0]                                                    # Auger, C_A n0^2 = 1
rep("CW5-C6b (replaced) row 18: bimolecular FORMATION with slow X loss keeps r_g = 0.9997/0.992/0.909 at t/t0 = 1/10/100 (VER V3) while "
    "n_F = 1/(1+t/t0); with k_X↓ >> C_X n, r_g -> 1/(1+t/t0); X-X annihilation + linear loss: r_g = e^{-kt}/[1 + (γn0/k)(1-e^{-kt})]; "
    "Auger: (1 + 2t/t0)^{-1/2}",
    all(TOL(v, s) for v, s in zip(rg_slow, ("0.9997", "0.992", "0.909"))) and np.max(np.abs(Y1[0] - 1/(1 + ts))) < 1e-8
    and np.max(np.abs(rg_fast - 1/(1 + ts))/(1/(1 + ts))) < 2e-3 and np.max(np.abs(Y3 - an3)) < 1e-8
    and np.max(np.abs(Y4 - (1 + 2*ts)**-0.5)) < 1e-8,
    f"r_g(slow) {rg_slow.round(5)}; r_g(fast)/(1/(1+t)) - 1 = {(rg_fast*(1 + ts) - 1).round(5)}")
# ERR-CW5-C4 (row 18, geometry): first order in γ with Gaussian profiles; s = r0^2 + 4 D t
gm_, Nn, lam_, D_, r0_, t_, rho_ = sp.symbols('gamma N lambda D r0 t rho', positive=True)
s_ = r0_**2 + 4*D_*t_
int3 = sp.integrate((Nn*sp.exp(-rho_**2/s_)/(sp.pi*s_)**sp.Rational(3, 2))**2*4*sp.pi*rho_**2, (rho_, 0, sp.oo))
int2 = sp.integrate((lam_*sp.exp(-rho_**2/s_)/(sp.pi*s_))**2*2*sp.pi*rho_, (rho_, 0, sp.oo))
ok3 = sp.simplify(int3 - Nn**2/(2*sp.sqrt(2)*(sp.pi*s_)**sp.Rational(3, 2))) == 0
ok2 = sp.simplify(int2 - lam_**2/(2*sp.pi*s_)) == 0
tint3 = sp.integrate(1/(2*sp.sqrt(2)*(sp.pi*s_)**sp.Rational(3, 2)), (t_, 0, sp.oo))
ok3b = sp.simplify(tint3 - 1/(4*sp.sqrt(2)*sp.pi**sp.Rational(3, 2)*D_*r0_)) == 0
lam_t = lam_/(1 + gm_*lam_/(8*sp.pi*D_)*sp.log(1 + 4*D_*t_/r0_**2))                         # cylinder: logarithmic
ok2b = sp.simplify(sp.diff(lam_t, t_) + gm_*lam_t**2/(2*sp.pi*s_)) == 0
rep("ERR-CW5-C4 diffusing tracks, bimolecular loss dn/dt = -γn^2: 3D Gaussian cloud ∫n^2 dV = N^2/(2√2 (πs)^{3/2}), loss saturates: "
    "1/N_∞ - 1/N0 = γ/(4√2 π^{3/2} D r0); cylinder ∫n^2 dA = λ^2/(2πs), λ(t) = λ0/[1 + (γλ0/8πD) ln(1 + 4Dt/r0^2)]",
    ok3 and ok2 and ok3b and ok2b)

# ---------------------------------------------------------------- C7 (LE-23): signed seed weights; clipping biases; second moment, not variance
K = np.array([0.55, 0.50, -0.05]); fv = np.array([1.0, 3.0, 10.0]); exact = K @ fv
R = np.abs(K).sum()/K.sum(); p = np.abs(K)/np.abs(K).sum()
rng = np.random.default_rng(3); idx = rng.choice(3, size=400000, p=p)
zz = np.sign(K[idx])*np.abs(K).sum()*fv[idx]; est, se7 = zz.mean(), zz.std(ddof=1)/math.sqrt(len(zz))
Kc = np.clip(K, 0, None); clip = (Kc/Kc.sum()*K.sum()) @ fv
m2_signed = (p*(np.abs(K).sum()*fv)**2).sum()/K.sum()**2; m2_abs = (p*fv**2).sum()                 # normalised by ΣK and Σ|K|
var_signed1 = R**2 - 1.0; var_abs1 = 0.0                                                            # f ≡ 1
rep("CW5-C7 (revised) LE-23: signed estimator unbiased (within 4 SE); clip-and-renormalise biased (+0.95, +26%); second-moment factor "
    "is exactly (Σ|K|/ΣK)^2 = 1.21; variance is NOT bounded by it: f ≡ 1 gives 0 (|K|-law) vs R^2 - 1 = 0.21 (signed)",
    abs(est - exact) < 4*se7 and abs(clip - exact) > 0.4 and abs(m2_signed/m2_abs - R**2) < 1e-12 and TOL(R**2, "1.21")
    and TOL(var_signed1, "0.21") and var_abs1 == 0.0, f"exact {exact:.3f}, signed {est:.4f} ± {se7:.4f}, clipped {clip:.3f}")

# ---------------------------------------------------------------- C8 (LE-127): Anderson orthogonality exponent, 1D semi-infinite chain
def occ(N, V):
    dg = np.zeros(N); dg[0] = V; w_, v_ = eigh_tridiagonal(dg, -np.ones(N - 1)); return v_[:, :N//2]
def expo(V1, V2, Ns=(100, 200, 400, 800)):
    L = [np.linalg.slogdet(occ(N, V1).T @ occ(N, V2))[1] for N in Ns]; return -np.polyfit(np.log(Ns), L, 1)[0]
ok8 = True; notes = []
for V1, V2 in [(0.0, 1.0), (0.5, 2.0)]:
    sl = expo(V1, V2); th = ((np.arctan(V2) - np.arctan(V1))/np.pi)**2/2
    ok8 &= abs(sl - th)/th < 0.04; notes.append(f"{sl:.4f}/{th:.4f}")
rep("CW5-C8 LE-127: |<Psi_L|Psi_R>| ∝ N^{-(dδ/π)^2/2} per spinless channel (δ = -arctan V at E_F), fit within 4% (finite-N)",
    ok8, "; ".join(notes))
# CW5-C8b (REPLACED; old version restated its own algebra): Born limit tested on the chain.  End-site DOS at E_F: ρ_σ = 1/π (hopping 1).
# ±v contact coupling: δ̃ = 2πρ_σ v in Born; α_ohm = Σ_σ (overlap exponent) = 2·expo; Born prediction 4(ρ_σ v)^2 = 4K.
vB = 0.15; alpha_chain = 2*expo(-vB, vB); K_sig = (vB/math.pi)**2; alpha_exact = 2*((2*math.atan(vB))/math.pi)**2/2
rhoS, VO = sp.symbols('rho_sigma VOmega', positive=True)
K_both = (2*rhoS*VO)**2; alpha_sym = sp.Rational(1, 2)/sp.pi**2*2*(2*sp.pi*rhoS*VO)**2
rep("CW5-C8b (replaced) LE-127 Born limit on the chain: α_ohm(fit, v = ±0.15) = 4K_σ to O(v^2) and = exact-phase value to 4%; "
    "spin counting: α = 4K with per-spin n0, α = K_both (factor 1, not 2) with a both-spin n0",
    abs(alpha_chain - alpha_exact)/alpha_exact < 0.04 and abs(alpha_exact/(4*K_sig) - 1) < 0.02
    and sp.simplify(alpha_sym - 4*(rhoS*VO)**2) == 0 and sp.simplify(alpha_sym/K_both - 1) == 0,
    f"α fit {alpha_chain:.5f}, exact-phase {alpha_exact:.5f}, 4K_σ {4*K_sig:.5f}")

# ---------------------------------------------------------------- C9 (LE-129): mK window, weak vs strong coupling; percentages (row 23)
lnGt = math.log(1e13*3.156e7); lam_max_strong = lnGt/2
pp = 1.0/0.06; S_ = 1.0; lnA = -(-S_ + pp*math.log(S_) - gammaln(pp + 1))
lam_max_weak = (lnGt - lnA)/2
hbar, amu, eV, A = 1.054571817e-34, 1.66053907e-27, 1.602176634e-19, 1e-10
lamP = lambda V, d, Mamu: (d*A/2)*math.sqrt(2*Mamu*amu*V*eV)/hbar
Vd2 = (lam_max_strong*hbar*2)**2/(2*28.0855*amu*eV)/A**2*1e3
rep("CW5-C9 (revised) LE-129: ln(Γ_att t_obs) = 47.2 -> λ_max = 23.6 (strong); ln[1/ω A] = 33.6 -> 6.8 (weak); V d^2 = 166 meV Å^2; "
    "Si λ_P = 27.5 -> needs >= 14.2% reduction; Al λ_P = 25 -> >= 5.6% (not 6%)",
    TOL(lnGt, "47.2") and TOL(lam_max_strong, "23.6") and TOL(lnA, "33.6") and TOL(lam_max_weak, "6.8") and TOL(Vd2, "166")
    and TOL(lamP(0.1, 1.5, 28.0855), "27.5") and TOL(1 - lam_max_strong/27.5, "0.142") and TOL(1 - lam_max_strong/25, "0.056"),
    f"{lam_max_strong:.3f}, {lnA:.3f}, {lam_max_weak:.3f}, {Vd2:.2f}, {lamP(0.1,1.5,28.0855):.3f}, "
    f"{1-lam_max_strong/27.5:.4f}, {1-lam_max_strong/25:.4f}")

# ---------------------------------------------------------------- C10 (LE-138): R1 size through the GAP-EF closed form (EF9)
c0, c1, gm, be = 1.613, 2.327, 0.964, 0.2395; eS = 3.221; u = (eS - c0)/c1
sens = c1*be*u/eS; sens_v = be*(eS - c0)/eS; dZ = sens*math.log(1/0.8)
rep("CW5-C10 LE-138: d ln ε_eh / d ln λ_ph = 0.1196 (= β(ε/E_g - c0)/(ε/E_g), VER row 15); Z_qp = 0.8 gives ≈ 2.7% (Z part, a value, not a bound)",
    TOL(sens, "0.1196") and abs(sens - sens_v) < 1e-12 and TOL(dZ, "0.027"), f"{sens:.5f}, {dZ:.5f}")

# ---------------------------------------------------------------- C11 (LE-146): Auger loss in a diffusing cylindrical Gaussian track
CA, lamL, Da, r0 = 4e-31*1e-12, 1e7*1e2, 1e-3, 5e-9
def fA_num():
    s0 = r0**2
    ring = lambda s_: quad(lambda rr: (lamL/(math.pi*s_))**3*math.exp(-3*rr**2/s_)*2*math.pi*rr, 0, 20*math.sqrt(s_))[0]
    ratio_ = ring(s0)/(lamL**3/(3*math.pi**2*s0**2))
    return ratio_*CA/lamL*quad(lambda u: (lamL**3/(3*math.pi**2*(s0*u)**2)), 1, np.inf)[0]*s0/(4*Da)
fA_an = CA*lamL**2/(3*math.pi**2*4*Da*r0**2)
rep("CW5-C11 LE-146: f_A = C_A λ^2/(12 π^2 D_a r0^2) (first order in C_A, ambipolar diffusion, no field)", abs(fA_num()/fA_an - 1) < 1e-8,
    f"f_A = {fA_an:.3e} for the illustrative inputs")

# ---------------------------------------------------------------- C12 (LE-147): T = 0 displaced oscillator: quanta in the reaction mode are Poisson
Nf = 60; Sx = 2.5; al = math.sqrt(Sx); ad = np.diag(np.sqrt(np.arange(1, Nf)), 1); Dm = expm(al*(ad.T - ad))
pn = np.abs(Dm[:, 0])**2; pois = np.array([math.exp(-Sx)*Sx**nn/math.factorial(nn) for nn in range(Nf)])
rep("CW5-C12 LE-147: |<n|D(√S)|0>|^2 = e^{-S} S^n/n! (athermal probability = Poisson tail Σ_{n ≥ E_bar/ω_R})",
    np.max(np.abs(pn[:30] - pois[:30])) < 1e-12)

# ---------------------------------------------------------------- C13 (LE-145): 1/t law, ln sum rule, critical branching sizes
Gmin, Gmax = 1e-9, 1e3; ts13 = np.array([1e2, 1e4]); rate = lambda t: (1 - np.exp(-Gmax*t) - (1 - np.exp(-Gmin*t)))/t
Ecum = quad(lambda lt: math.exp(lt)*rate(math.exp(lt)), math.log(1e2), math.log(1e4), epsabs=0, epsrel=1e-12)[0]
lb = lambda s_, b_: -b_*s_ + (s_ - 1)*math.log(b_*s_) - gammaln(s_ + 1)
tail = (lb(1e4, 1.0) - lb(1e3, 1.0))/math.log(10)
rep("CW5-C13 LE-145: flat ln-barrier density -> rate ∝ 1/t (to O(Γ_min t)) and released energy ∝ ln(t2/t1); critical Borel sizes P(s) ∝ s^-3/2 "
    "(in releases s, not in energy)",
    abs(rate(ts13[0])*ts13[0]/(rate(ts13[1])*ts13[1]) - 1) < 2e-5 and abs(Ecum - math.log(100)) < 2e-5 and abs(tail + 1.5) < 1e-4,
    f"tail slope {tail:.6f}")

# ---------------------------------------------------------------- C14 (LE-131): maximum entropy at fixed mean on E >= 0 is exponential
Eb = np.linspace(0, 40, 4001); dE = Eb[1] - Eb[0]; mean = 3.0
expo_ = np.exp(-Eb/mean); expo_ /= expo_.sum()*dE
alt = Eb**1*np.exp(-2*Eb/mean); alt /= alt.sum()*dE
H = lambda pv: -np.sum(pv[pv > 0]*np.log(pv[pv > 0]))*dE
rep("CW5-C14 LE-131: exponential (E_slope = mean) has larger entropy than a gamma(2) law of equal mean",
    abs(np.trapezoid(Eb*expo_, Eb) - mean) < 2e-2 and abs(np.trapezoid(Eb*alt, Eb) - mean) < 2e-2 and H(expo_) > H(alt))

# ---------------------------------------------------------------- C15 (LE-136, LE-130): tanh factor, P̄p^2, density conversion
kB, h_ = 1.380649e-23, 6.62607015e-34
th = math.tanh(h_*6e9/(2*kB*0.1)); th25 = math.tanh(h_*6e9/(2*kB*0.025))
e0, Debye = 8.8541878128e-12, 3.33564e-30
Pp2 = lambda tand, er: 3*er*e0*tand/math.pi
Pbar = lambda tand, er, pD: Pp2(tand, er)/(pD*Debye)**2/(1/eV)/1e6
conv = 1/(1e-12*h_*1e9/eV)                                              # 1 /(µm^3 GHz) -> eV^-1 cm^-3
sig_lo, sig_hi = 0.4/0.003*conv, 0.5/0.002*conv                        # 0.4-0.5 /(GHz µm^2) over 2-3 nm (1705.01108 p. 13)
rep("CW5-C15 (revised) LE-136/130: tanh = 0.894 (6 GHz, 100 mK), 0.99998 (25 mK; CW5 wrote 0.99999); P̄(5e-3, ε_r 3.9) = 2.37e21 (1 D) - 6.6e19 (6 D); "
    "10^2/(µm^3 GHz) = 2.42e19; 0.4-0.5/(GHz µm^2) over 2-3 nm = (3.2-6.0)e19 /(eV cm^3)",
    TOL(th, "0.894") and TOL(th25, "0.99998") and TOL(Pbar(5e-3, 3.9, 1), "2.37e21") and TOL(Pbar(5e-3, 3.9, 6), "6.6e19")
    and TOL(1e2*conv, "2.42e19") and TOL(sig_lo, "3.2e19") and TOL(sig_hi, "6.0e19"),
    f"P̄ {Pbar(5e-3,3.9,1):.3e}/{Pbar(5e-3,3.9,6):.3e}; σ {sig_lo:.3e}-{sig_hi:.3e}")

# ---------------------------------------------------------------- C16 (LE-139): relaxation-time memory weight w = Γ_E/(Γ_E + Γ_k)
GE, Gk = 1.0, 4.0; rng = np.random.default_rng(11); tE = rng.exponential(1/GE, 400000); tk = rng.exponential(1/Gk, 400000)
wmc = np.mean(tk > tE); se16 = math.sqrt(wmc*(1 - wmc)/len(tE))
rep("CW5-C16 LE-139: P(no randomising event before the next energy-changing event) = Γ_E/(Γ_E+Γ_k) within 4 SE (given (H-BGK))",
    abs(wmc - GE/(GE + Gk)) < 4*se16, f"{wmc:.4f} ± {se16:.4f} vs {GE/(GE+Gk):.4f}")

# ---------------------------------------------------------------- C17 (LE-22 B-2): N_eh cap; trajectory count (row 5)
Nm = 0.127*890/3.8; sd = math.sqrt(3.7*Nm); cap = Nm + 6*sd
kurt_err = lambda nn, kex: math.sqrt(2/(nn - 1) + kex/nn)
nmin = next(nn for nn in range(10, 10**5) if kurt_err(nn, 2) <= 0.06)
rep("CW5-C17 (revised) B-2: <N_eh>(0.89 keV) = 29.7, σ = 10.5, cap 92.7; error 6.3% / 8.95% at n = 500 (κ_ex = 0/2; CW5 rounded to 9.0%); "
    "6% at κ_ex = 2 needs n >= 1112 (1100: 6.03%, 1111: 6.0017%)",
    TOL(Nm, "29.7") and TOL(sd, "10.5") and TOL(cap, "92.7") and TOL(kurt_err(500, 0), "0.063") and TOL(kurt_err(500, 2), "0.0895")
    and nmin == 1112 and TOL(kurt_err(1100, 2), "0.0603") and TOL(kurt_err(1111, 2), "0.060017"),
    f"nmin {nmin}; {kurt_err(1100,2):.5f}, {kurt_err(1111,2):.6f}")

# ---------------------------------------------------------------- ERR-CW5-C5 (VER rows 2, 24, 15, LE-149): small numbers used in the errata text
Ge_field = 4.0/2.54                                                   # ±2 V across a 25.4 mm crystal [E: thickness not in 1805.09942]
td = (2.54/1e6*1e6, 2.54/1e5*1e6)                                     # µs at v_d = 1e6, 1e5 cm/s [E]
n_traj = lambda dP, pP=0.5, zz_=2.0: math.ceil(2*pP*(1 - pP)*(zz_/dP)**2)   # two independent arms, 2-sigma resolution of ΔP
rep("ERR-CW5-C5 Ge field ≈ 1.6 V/cm (4 V / 2.54 cm); t_drift ≈ 2.5-25 µs for v_d = 10^6-10^5 cm/s; LE-149 n_traj = 2p(1-p)(z/ΔP)^2 "
    "= 2.0e4 per arm for ΔP = 0.01 at p = 0.5 (2σ); 1.4% (Si E_x^b/E_g = 14.7/1170 meV = 1.26%)",
    TOL(Ge_field, "1.6") and TOL(td[0], "2.5") and TOL(td[1], "25") and n_traj(0.01) == 20000 and TOL(14.7/1170, "0.0126"),
    f"{Ge_field:.3f} V/cm; {td[0]:.2f}-{td[1]:.1f} µs; n {n_traj(0.01)}")

# ---------------------------------------------------------------- C18: BOOKKEEPING (not a physics check): literature records present
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../literature/papers-CW5")
want = {"0802.2404": "Microwave Dielectric Loss", "cond-mat_0507622": "Decoherence in Josephson Qubits", "1805.09942": "Energy Loss Due to Defect Formation",
        "2009.03804": "Nanomechanical damping", "1705.01108": "Towards understanding two-level-systems", "cond-mat_0310283": "Quantum Diffusion"}
ok18 = True
for kk, tt in want.items():
    fn = os.path.join(base, f"arxiv-{kk}.xml")
    txt = open(fn).read() if os.path.exists(fn) else ""
    ok18 &= (tt in txt) and (kk.replace("_", "/") in txt)
base2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../literature/papers-ERR-CW5")
dois = {"works-kesten1974.json": "10.1214/aop/1176996654", "works-alsmeyer1994.json": "10.1016/0304-4149(94)90146-5"}
for fn, doi in dois.items():
    pth = os.path.join(base2, fn); ok18 &= os.path.exists(pth) and doi in open(pth).read()
ok18 &= not any(fn.endswith(".pdf") for fn in os.listdir(base2))
rep("CW5-C18 BOOKKEEPING: six arXiv records (CW5) and two Crossref records (Kesten 1974, Alsmeyer 1994; ERR-CW5) present; no PDF kept", ok18)

print(f"\n{sum(RES)}/{len(RES)} PASS in {time.time() - T0:.1f} s")
