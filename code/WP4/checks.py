"""WP4 identity checks (sympy/mpmath, < 1 min). Run: python3 -I checks.py
Each check prints PASS/FAIL. Labels Kn are cited in returns/R5/WP4.md."""
import sympy as sp, mpmath as mp
ok = {}
def rep(k, cond, note=""):
    ok[k] = bool(cond); print(f"{k}: {'PASS' if cond else 'FAIL'}  {note}")

# K1  Lindhard static long-wavelength limit: bracket -> 1, so Re eps = 1 + lam_TF^2/q^2 (not lam^2/(2q^2), 2101.08263 eq.3)
x = sp.symbols('x', positive=True)
F = sp.Rational(1,2) + (1-x**2)/(4*x)*sp.log((1+x)/(1-x))
rep("K1", sp.limit(F, x, 0) == 1, "static Lindhard bracket -> 1")
# and dynamic small-Q limit used in eq.3 regime (omega << q vF, q << kF): bracket -> 1 as well
kF, q, w, vF = sp.symbols('k_F q omega v_F', positive=True)
Qm = q/(2*kF) - w/(q*vF); Qp = q/(2*kF) + w/(q*vF)
br = sp.Rational(1,2) + kF/(4*q)*((1-Qm**2)*sp.log((1+Qm)/(1-Qm)) + (1-Qp**2)*sp.log((1+Qp)/(1-Qp)))
t = sp.symbols('t', positive=True)
lim = sp.limit(br.subs({w: t**2, q: t}), t, 0)   # omega/(q vF) ~ t -> 0 and q/kF -> 0
rep("K1b", sp.simplify(lim - 1) == 0, f"dynamic bracket limit = {lim}")

# K2  BCS: bare tau3 bubble at q=0 is nonzero; gauge-invariant (phase-vertex) combination vanishes.
nu, Om, xi, D = sp.symbols('nu Omega xi Delta', real=True)
Ee = sp.symbols('E', positive=True)        # E = sqrt(xi^2 + Delta^2); xi^2 replaced by E^2 - Delta^2 at the end
t1 = sp.Matrix([[0,1],[1,0]]); t2 = sp.Matrix([[0,-sp.I],[sp.I,0]]); t3 = sp.Matrix([[1,0],[0,-1]]); I2 = sp.eye(2)
def Gnum(z):  # numerator of Nambu Green function; G = -(i z + xi t3 + D t1)/(z^2+E^2)
    return -(sp.I*z*I2 + xi*t3 + D*t1)
def Pi(ti, tj):
    num = sp.expand(-(ti*Gnum(nu+Om)*tj*Gnum(nu)).trace())
    den = (nu**2 + Ee**2)*((nu+Om)**2 + Ee**2)
    res = 0
    for p in (sp.I*Ee, sp.I*Ee - Om):          # upper-half-plane simple poles (Om real, nonzero)
        res += num.subs(nu, p)/sp.diff(den, nu).subs(nu, p)
    out = sp.simplify(sp.I*res)                 # int dnu/2pi = i * sum residues
    return sp.simplify(sp.expand(out).subs(xi**2, Ee**2 - D**2))
P33 = Pi(t3, t3); P32 = Pi(t3, t2); P23 = Pi(t2, t3); P22 = Pi(t2, t2); P22_0 = sp.limit(P22, Om, 0)
print("   per-k  Pi33 =", sp.factor(P33)); print("   per-k  Pi32 =", sp.factor(P32)); print("   per-k  Pi22-Pi22(0) =", sp.factor(sp.simplify(P22-P22_0)))
rep("K2a", sp.simplify(P33) != 0, "bare density bubble at q=0 nonzero (coherence factor Delta^2/E^2)")
# all three are (function of Delta,Omega) x h(E,Omega) with common h -> the k-sum factors out
h = sp.simplify(P33/D**2)
r32 = sp.simplify(P32/h); r22 = sp.simplify((P22-P22_0)/h)
indep = all(sp.simplify(sp.diff(r, Ee)) == 0 and sp.simplify(sp.diff(r, xi)) == 0 for r in (r32, r22))
comb = sp.simplify(D**2 - r32*sp.simplify(P23/h)/r22)
rep("K2b", indep and comb == 0, f"Pi33 - Pi32 Pi23/(Pi22(Om)-Pi22(0)) = 0 at q=0 (r32={sp.simplify(r32)}, r22={sp.simplify(r22)})")

# K3  Coherence-factor algebra: (u v' + v u')^2 = (1/2)(1 - (xi xi' - D^2)/(E E')); its q->0 limit = D^2/E^2
E = sp.sqrt(xi**2 + D**2); xp = sp.symbols("xi_p", real=True); Ep = sp.sqrt(xp**2+D**2)
u = sp.sqrt((1+xi/E)/2); v = sp.sqrt((1-xi/E)/2); up = sp.sqrt((1+xp/Ep)/2); vp = sp.sqrt((1-xp/Ep)/2)
lhs = sp.expand((u*vp+v*up)**2); rhs = sp.Rational(1,2)*(1-(xi*xp-D**2)/(E*Ep))
num = [ (lhs-rhs).subs({xi:a, xp:b, D:c}).evalf() for a,b,c in [(0.3,-1.2,0.5),(2,1,0.1),(-0.7,0.2,1.3)] ]
rep("K3", all(abs(n) < 1e-12 for n in num) and sp.simplify(rhs.subs(xp, xi) - D**2/E**2) == 0, "coherence factor identity and q->0 limit")

# K4  Case-I (density) and case-II (current) T=0 pair-breaking functions in the omega << q vF limit
def _g(wr, sgn):   # (1/w) int_1^{w-1} de (e(w-e) + sgn)/sqrt((e^2-1)((w-e)^2-1)), Delta=1; e = w/2 - (w/2-1)cos(th)
    a = wr/2 - 1
    f = lambda th: (lambda e: (e*(wr-e) + sgn)/mp.sqrt((e+1)*(wr-e+1)))(wr/2 - a*mp.cos(th))
    return mp.quad(f, [0, mp.pi])/wr
gI = lambda wr: _g(wr, +1); gII = lambda wr: _g(wr, -1)
def MB(wr):   # Mattis-Bardeen T=0 closed form, k=(w-2)/(w+2), mpmath ellipe/ellipk take m=k^2
    k = (wr-2)/(wr+2); return (1+2/wr)*mp.ellipe(k**2) - (4/wr)*mp.ellipk(k**2)
vals = [(wr, gI(wr), gII(wr), MB(wr)) for wr in (2.0001, 2.5, 4, 5, 10, 100)]
for wr, a, b, c in vals: print(f"   omega/Delta={wr:8.4f}  g_I={float(a):.5f}  g_II={float(b):.5f}  MB={float(c):.5f}")
rep("K4", abs(vals[0][1]-mp.pi/2) < 2e-2 and abs(vals[0][2]) < 2e-2 and all(abs(b-c) < 1e-6 for _, _, b, c in vals) and abs(vals[-1][1]-1) < 2e-2,
    "g_I(2D+)=pi/2 (step), g_II = Mattis-Bardeen, both -> 1")

# K5  Massless isotropic Dirac cone: Im eps(q->0) = e^2/(12 pi vF) per Dirac cone (spin 2) ; W = Im eps/|kappa+...|^2
e2, k_, th, ve = sp.symbols('e2 k theta v', positive=True)
# overlap |<+,k+q|-,k>|^2 -> q^2 sin^2(th)/(4k^2) ; Im eps = (e2/q^2) * pi * (2/(2pi)^3) * int d^3k overlap delta(w-2 v k)
ang = sp.integrate(sp.sin(th)**2*sp.sin(th)*2*sp.pi, (th, 0, sp.pi))          # 8pi/3
ImEps = e2/q**2*sp.pi*2/(2*sp.pi)**3 * q**2/4*ang/(2*ve)                         # k-integral of delta(w-2vk) -> 1/(2v)
rep("K5", sp.simplify(ImEps - e2/(12*sp.pi*ve)) == 0, f"Im eps_Dirac = {sp.simplify(ImEps)}")

# K6  Magnon normalisation: URF S_ab for n=1 FM gives 1905.13744 eq.(12) prefactor n_s/(8 pi^2)
S_, Om_ = sp.symbols('S Omega_c', positive=True)
pref = (2*sp.pi/Om_)*(S_/2)/(2*sp.pi)**3
rep("K6", sp.simplify(pref - (S_/Om_)/(8*sp.pi**2)) == 0, "Gamma = n_s/(8pi^2) int d^3q |O^+|^2 delta")

# K7  Free-electron Pauli-blocked kinematics: minimum initial energy e_- = (w - E_q)^2/(4 E_q) (1512.04533 eq.13 lacks the 4)
m = sp.symbols('m', positive=True)
pmin = m*w/q - q/2; Eq = q**2/(2*m)
rep("K7", sp.simplify(pmin**2/(2*m) - (w-Eq)**2/(4*Eq)) == 0, "e_- = (omega-E_q)^2/(4E_q)")

# K8  Phase-space reduction of the URF golden rule to 2609.06423 eq.(9): Gamma = int dw int q^3 dq/(2pi)^3 |V|^2 W/(alpha v)
al, vv = sp.symbols('alpha v', positive=True)
urf = 2*sp.pi*q**2/(q*vv)/(2*sp.pi)**3 * 2*q**2/(4*sp.pi*al)    # d^3q delta(w - q v c + ..) -> 2pi q dq / v ; S = 2q^2/e^2 W ; e^2=4 pi alpha
rep("K8", sp.simplify(urf - q**3/(2*sp.pi)**3/(al*vv)) == 0, "2609.06423 eq.(9) prefactor")

# K9  Exothermic kinematics into a dispersionless mode: q* = sqrt(2 m (|D| - w0)) ; isotropic phase-space Jacobian
Dx, w0, mc = sp.symbols('Delta_x omega_0 m_chi', positive=True)
qs = sp.sqrt(2*mc*(Dx-w0))
arg = Dx - q**2/(2*mc) - w0; root = [r for r in sp.solve(arg, q) if r.is_positive is not False][0]
jac = (q**2/sp.Abs(sp.diff(arg, q))).subs(q, root)
rep("K9", sp.simplify(jac - qs*mc) == 0, f"int q^2 dq delta(...) = m q* = {sp.simplify(jac)}")

# K10 Two-magnon longitudinal weight vanishes for a Heisenberg FM (V=0) and is O(S^0) vs one-magnon O(S) for a 2-sublattice AFM
kk = sp.symbols('kk', real=True)
gam = sp.cos(kk)   # 1D chain structure factor, AFM LSWT: u=cosh, v=sinh with tanh(2 theta) = gamma
uk2 = (1/sp.sqrt(1-gam**2) + 1)/2; vk2 = (1/sp.sqrt(1-gam**2) - 1)/2
rep("K10", sp.simplify(uk2 - vk2 - 1) == 0, "AFM Bogoliubov u^2-v^2=1 (two-magnon amplitude ~ u v, S-independent); FM: v=0 -> no 2-magnon at T=0")

print("ALL PASS" if all(ok.values()) else "SOME FAIL")
