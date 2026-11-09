"""DC-41 checks.  Run: python checks.py  (stdout -> data/checks_stdout.txt).  Each check prints PASS/FAIL with its numbers; C10 needs data/table_grid.csv and data/table_2d.csv."""
import csv, os, sys
import numpy as np, sympy as sp
import bcs1d as b, bubbles2d as d, kk
H = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(H, "data")
res = []
def chk(name, ok, info=""):
    res.append(bool(ok)); print(("PASS " if ok else "FAIL ") + name + " | " + str(info), flush=True)

# C1 algebra (sympy): spinors -> coherence factors; identities behind the closed form; q = 0 per-k Goldstone cancellation with Pi23 = -Pi32 carried
a_, c_ = sp.symbols('a c', positive=True)              # xi = sinh a, xi' = sinh c  (Delta = 1): E = cosh a; half-angle spinors
E_, Ep = sp.cosh(a_), sp.cosh(c_); xi, xp = sp.sinh(a_), sp.sinh(c_)
num = lambda e: [abs(complex(e.subs({a_: A, c_: C}).evalf())) for A, C in ((0.3, 1.1), (-0.7, 0.4), (1.9, -0.2))]
u = lambda x, E: sp.sqrt((1 + x / E) / 2); v = lambda x, E: sp.sqrt((1 - x / E) / 2)
U, V, Up, Vp = u(xi, E_), v(xi, E_), u(xp, Ep), v(xp, Ep)
M3 = -(Up * V + Vp * U); M2 = -sp.I * (Up * U + Vp * V)
W = E_ + Ep; s_ = xp - xi
idn = {"|M3|^2 = (1/2)[1-(xx'-1)/EE']": M3 ** 2 - (1 - (xi * xp - 1) / (E_ * Ep)) / 2,
       "|M2|^2 = (1/2)[1+(xx'+1)/EE']": (M2 * sp.conjugate(M2)) - (1 + (xi * xp + 1) / (E_ * Ep)) / 2,
       "M3* M2 = i W/(2EE')": sp.conjugate(M3) * M2 - sp.I * W / (2 * E_ * Ep),
       "EE'+xx'+1 = (W^2-s^2)/2": E_ * Ep + xi * xp + 1 - (W ** 2 - s_ ** 2) / 2,
       "EE'-xx'-1 = 2 s^2/(W^2-s^2)": E_ * Ep - xi * xp - 1 - 2 * s_ ** 2 / (W ** 2 - s_ ** 2)}
mx = max(max(num(e)) for e in idn.values())
I_, om, Dl = sp.symbols('I omega Delta', positive=True)
gold = sp.simplify(-4 * Dl ** 2 * I_ + ((sp.I * (-2 * Dl * om * I_)) * (-(sp.I * (-2 * Dl * om * I_)))) / (om ** 2 * I_))
chk("C1 spinor/coherence identities (5, numeric at 3 sympy points) and K2 q = 0: R = Pi33 + Pi32 Pi23/D = 0", mx < 1e-12 and gold == 0, "max dev %.1e; symbolic R = %s" % (mx, gold))
# identity g(s) = Int dxi W/(EE'(W^2 - s^2)) = 1/Delta^2 and dxi W/(EE') = 2 dA, numerically, all s
gs = []
for s in (0.0, 0.3, 2.0, 20.0, 300.0):
    from scipy import integrate
    fn = lambda eta: (lambda E1, E2: (E1 + E2) / (E1 * E2 * ((E1 + E2) ** 2 - s * s)))(np.sqrt((eta - s / 2) ** 2 + 1), np.sqrt((eta + s / 2) ** 2 + 1))
    gs.append(2 * sum(integrate.quad(fn, a, c, limit=800)[0] for a, c in ((0, s / 2), (s / 2, s / 2 + 10), (s / 2 + 10, np.inf)) if c > a))
chk("C1b g(s) = 1 for all s (static compressibility unchanged at every angle)", np.max(np.abs(np.array(gs) - 1)) < 1e-6, gs)

# C2 g_I: WP4 [4.2] closed form, the u-form derived here, WP4 values
vals = {2.5: 1.418, 4: 1.211, 5: 1.151, 10: 1.050, 100: 1.001}
e1 = max(abs(float(b.gI(y)) - g) for y, g in vals.items()); e2 = max(abs(float(b.gI(y)) - b.gI_int(y)) for y in (2.05, 2.5, 5, 10, 50))
chk("C2 g_I closed form = WP4 values (3 dp) = u-integral", e1 < 6e-4 and e2 < 1e-9 and abs(b.gI(2.0000001) - np.pi / 2) < 1e-5, "%.1e %.1e" % (e1, e2))

# C3 ladder off: bare bubble (2609.06423 Eq. (7), 2-D spinor) ; Im P33/Im P^nor = g_I(y) exactly while y^2 - 4 <= Q^2; s_eff -> s_BCS(y) as Q -> inf
pts = [(2.2, 5.64), (3, 7.7), (5, 12.8), (10, 25.6), (5, 100.0), (30, 300.0), (50, 1000.0)]
dv = []
for y, Q in pts:
    p = b.P33(y, Q); dv.append(abs(p.imag / b.pnor(y, Q).imag / float(b.gI(y)) - 1))
B = d.bubbles(5.0, 12.8, nmu=12, n=20)
d2 = abs(B["P33"].imag / b.pnor(5.0, 12.8).imag / float(b.gI(5.0)) - 1)
# first run used 1e-7: the residual 1e-8..1e-6 does not fall under refinement (inverse-sqrt endpoint panel, floor ~ sqrt(2^-44 L)); the physics test is Q independence
qi = abs(b.P33(5, 12.8).imag * 12.8 - b.P33(5, 100.0).imag * 100.0)
chk("C3a Im eps^bare = g_I Im eps^nor, no O(Delta^2/q^2 v_F^2) term for y^2-4 <= Q^2: 1-D < 2e-6 (quadrature floor); Q Im P33 identical at Q = 12.8, 100; 2-D at (5,12.8)", max(dv) < 2e-6 and qi < 1e-12 and d2 < 1e-4, "%.1e %.1e %.1e" % (max(dv), qi, d2))
ss = []
for y in (2.2, 3, 5, 10):
    Q = 3e4
    ss.append((y, Q * (-b.P33(y, Q, n=24, refine=2).real + b.pnor(y, Q).real), b.s_bcs(y)))
chk("C3b bare s_eff(y, Q = 3e4) -> s_BCS(y) (WP4 K32, KK to infinity), 1%", all(abs(a / c - 1) < 0.01 for _, a, c in ss), ss)
# C3c CW4 sec. 8 table reproduced by the copied K2 functions
tab = {2.2: (4.01, 0.33, 0.40), 2.5: (2.82, 0.45, 0.54), 3: (2.03, 0.58, 0.66), 5: (1.05, 0.80, 0.86), 10: (0.50, 0.94, 0.96)}
R = 0.39; ReL = 1 - R / 2 * np.log((1 + R) / (1 - R)); rr = np.pi / 2 * R / ReL; ok = True; o = []
for y, (s0, k0, c0) in tab.items():
    s = b.s_bcs(y); sc = b.s_bcs(y, Y=y / R); gi = float(b.gI(y))
    f = lambda z: (1 + rr ** 2) / ((1 + R * z / y / ReL) ** 2 + gi ** 2 * rr ** 2)
    ok &= abs(s - s0) < 0.006 and abs(f(s) - k0) < 0.006 and abs(f(sc) - c0) < 0.006; o.append((y, round(s, 3), round(f(s), 3), round(f(sc), 3)))
chk("C3c CW4 sec. 8 table to +-0.006 (this code = CW4 K2)", ok, o)

# C4 Goldstone: R~ -> 0 at q -> 0 for every omega; 2-D with Pi22(0,0) at the same cutoff; negative control with a shifted cutoff
o = []; ok = True
for y in (2.5, 5, 20):
    for Q in (1e-2, 1e-1):
        p, g = b.Pg(y, Q); v = g.imag / p.imag - 1; o.append((y, Q, abs(g / p), v, g.real * y * y / (Q * Q / 3))); ok &= abs(g / p) < 3 * Q * Q and abs(v + 1) < 1e-3
B = d.bubbles(3.0, 0.01, nmu=6, n=20); g2 = d.grpa(B)
Bbad = dict(B); Bbad["D"] = B["D"] + 0.005                 # Pi22(0,0) from a cutoff 1% off: (1/2)(2 ln 1.01)/2 ~ 0.005 in D/2N
gbad = d.grpa(Bbad)
chk("C4a Goldstone: |P~/P33| -> O(Q^2), v_GRPA -> -1; P~ -> Q^2/(3 y^2)", ok, o)
# first run demanded > 0.1, a wrong estimate: a shift d of D leaves the spurious constant d/|D| (|D| = 2.47 here), which is what the control must show
pred = 0.005 / abs(B["D"])
chk("C4b 2-D same cutoff cancels; negative control (1% cutoff mismatch) leaves the predicted spurious constant d/|D|, >= 100x the same-cutoff value", abs(g2 / B["P33"]) < 1e-3 and abs(abs(gbad / B["P33"]) / pred - 1) < 0.01 and abs(gbad / g2) > 100, "same %.2e, mismatched %.5f, predicted %.5f" % (abs(g2 / B["P33"]), abs(gbad / B["P33"]), pred))

# C5 sum rules, AB pole, positivity, KK check, tail
o = []; okf = okb = okc = okp = okk = True
for Q in (0.3, 1.0, 3.0, 5.64, 12.8, 50.0, 300.0, 1000.0):
    S = kk.Spec(Q); fg, cg = S.sums("grpa"); fb, cb = S.sums("bare")
    S2 = kk.Spec(Q, fac=1e4)
    kerr = 0.0; tail = 0.0
    for y in (2.2, 3.0, 5.0, 10.0, 50.0):
        p, g = b.Pg(y, Q); kerr = max(kerr, abs(S.kk(y) - g.real) / max(abs(g), 1e-3)); tail = max(tail, abs(S.kk(y) - S2.kk(y)) / abs(g))
    o.append((Q, round(fg, 7), round(cg, 7), round(fb, 4), round(cb, 7), S.wab, round(S.Z, 6), "%.1e" % kerr, "%.1e" % tail, "%.1e" % (S.I["grpa"].max())))
    okf &= abs(fg - 1) < 1e-4; okc &= abs(cg - 1) < 1e-4; okp &= S.I["grpa"].max() <= 1e-15; okk &= kerr < 1e-3 and tail < 1e-3
    if Q <= 12.8: okb &= fb > 1.5
print("   columns: Q, f-sum GRPA, compress GRPA, f-sum bare (cut at 10^3 Q), compress bare, w_AB, Z, KK rel err, KK tail 10^3 vs 10^4 Q, max Im P~"); [print("  ", r) for r in o]
chk("C5a f-sum: GRPA + AB pole = 1 to 1e-4", okf); chk("C5b compressibility rule GRPA = 1 to 1e-4", okc)
chk("C5c bare bubble fails the f-sum at Q <= 12.8 (WP4-K2 discriminator)", okb); chk("C5d -Im P~ >= 0 (positivity)", okp); chk("C5e KK = direct Re < 1e-3; KK tail < 1e-3", okk)
S = kk.Spec(5.0, fac=1e4); w = S.w; i = np.argmin(abs(w - 3e3)); j = np.argmin(abs(w - 3e2))
pg, pb = np.log(S.I["grpa"][i] / S.I["grpa"][j]) / np.log(w[i] / w[j]), np.log(S.I["bare"][i] / S.I["bare"][j]) / np.log(w[i] / w[j])
chk("C5f tails above q v_F: bare ~ w^-2, GRPA ~ w^-6: suppression (Q/w)^4 (WP4 sec. 4.2 states (Q/w)^2)", abs(pg + 6) < 0.05 and abs(pb + 2) < 0.05, "%.3f %.3f" % (pg, pb))

# C6 normal limit y >> 1
o = []; ok = True
for y, Q in ((50, 1000.0), (50, 128.2), (30, 1000.0), (200, 1000.0), (1000, 1e4)):
    p, g = b.Pg(y, Q); nr = b.pnor(y, Q)
    L = lambda P: -P.imag / abs(P) ** 2
    o.append((y, Q, round(float(b.gI(y)), 5), round(g.imag / nr.imag, 5), "%.1e" % (g.imag / p.imag - 1), round(L(g) / L(nr), 5), round(L(p) / L(nr), 5)))
    ok &= abs(g.imag / nr.imag - 1) < 0.01 and abs(L(g) / L(nr) - 1) < 0.02
chk("C6 y >> 1: Im ratio -> g_I -> 1, v -> 0, L^BCS -> L^nor", ok, o)

# C7 (8.1) identity with the computed s_eff and g_I(1 + v)
y, Q = 3.0, 7.692307; p, g = b.Pg(y, Q); nr = b.pnor(y, Q); r = nr.imag / nr.real
G = g.imag / nr.imag; dl = (g.real - nr.real) / nr.real
a = G * (1 + r * r) / ((1 + dl) ** 2 + G * G * r * r); L = lambda P: -P.imag / abs(P) ** 2
chk("C7 (8.1) with g_I -> g_I(1 + v), delta from s_eff = direct L ratio", abs(a / (L(g) / L(nr)) - 1) < 1e-12, a)

# C8 convergence of the closed-form path and the 2-D table
rows = list(csv.DictReader(open(os.path.join(D, "table_grid.csv"))))
m = max(float(r["dv_doubling"]) for r in rows)
chk("C8 v_GRPA 1-D path, node and panel doubling, max on 460 points < 1e-3", m < 1e-3, m)
if os.path.exists(os.path.join(D, "table_2d.csv")):
    t = list(csv.DictReader(open(os.path.join(D, "table_2d.csv"))))
    full = len(t) == len(rows)
    m1, m2, m3 = (max(float(r[k]) for r in t if r[k]) for k in ("dv_doubling", "dv_2d_1d", "dPg_2d_1d"))
    print("   doubled rows:", sum(1 for r in t if r["dv_doubling"]))
    chk("C9 spec 2-D quadrature on the table: doubling < 1e-3 and 2-D = closed form", full and m1 < 1e-3 and m2 < 1e-3, "rows %d/%d; dv doubling %.2e; |v_2D - v_1D| %.2e; |P~_2D - P~_1D| %.2e" % (len(t), len(rows), m1, m2, m3))
print("%d/%d PASS" % (sum(res), len(res)))
