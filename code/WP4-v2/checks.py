"""WP4-v2 identity checks (R6 revision of returns/R5/WP4.md). Sympy only (exact algebra; Integral.evalf for 1-D quadratures).
Run:  python3 -I checks.py     Prints PASS/FAIL per check. Labels WP4v2-Kn (CONVENTIONS sec. 14); K1-K10 keep their v1 meaning.
Notation: NOTATION v4 (Delta_BCS, g_I -> frak g_I, eps_bg, Lambda_D, L, v_C, ...). No numerical simulation."""
import sympy as sp
from sympy import Rational as R, pi, sqrt, I

RES = []
def rep(k, cond, note=""):
    RES.append(bool(cond)); print(f"{'PASS' if cond else 'FAIL'}  WP4v2-{k:5s} {note}")

# ---- K1 Lindhard: static bracket -> 1 => Re eps = 1 + k_TF^2/q^2 (2101.08263 Eq. (3) prints k_TF^2/(2q^2))   [4.2 step 6]
x = sp.symbols('x', positive=True)
F = R(1, 2) + (1 - x**2)/(4*x)*sp.log((1 + x)/(1 - x))
rep("K1", sp.limit(F, x, 0) == 1, "static Lindhard bracket -> 1")
kF, q, w, vF = sp.symbols('k_F q omega v_F', positive=True)
Qm = q/(2*kF) - w/(q*vF); Qp = q/(2*kF) + w/(q*vF)
br = R(1, 2) + kF/(4*q)*((1 - Qm**2)*sp.log((1 + Qm)/(1 - Qm)) + (1 - Qp**2)*sp.log((1 + Qp)/(1 - Qp)))
t = sp.symbols('t', positive=True)
rep("K1b", sp.simplify(sp.limit(br.subs({w: t**2, q: t}), t, 0) - 1) == 0, "dynamic bracket -> 1 for omega << q v_F, q << k_F")

# ---- K2 BCS, q = 0: bare tau3 bubble != 0; GRPA (phase-vertex) combination == 0                                   [4.1]
nu, Om, xi, D = sp.symbols('nu Omega xi Delta', real=True)
Ee = sp.symbols('E', positive=True)
t1 = sp.Matrix([[0, 1], [1, 0]]); t2 = sp.Matrix([[0, -I], [I, 0]]); t3 = sp.Matrix([[1, 0], [0, -1]]); I2 = sp.eye(2)
def Gnum(z): return -(I*z*I2 + xi*t3 + D*t1)          # Nambu G^N numerator; G^N = Gnum/(z^2+E^2)
def Pi(ti, tj):
    num = sp.expand(-(ti*Gnum(nu + Om)*tj*Gnum(nu)).trace())
    den = (nu**2 + Ee**2)*((nu + Om)**2 + Ee**2)
    res = sum(num.subs(nu, p)/sp.diff(den, nu).subs(nu, p) for p in (I*Ee, I*Ee - Om))
    return sp.simplify(sp.expand(sp.simplify(I*res)).subs(xi**2, Ee**2 - D**2))
P33 = Pi(t3, t3); P32 = Pi(t3, t2); P23 = Pi(t2, t3); P22 = Pi(t2, t2); P22_0 = sp.limit(P22, Om, 0)
rep("K2a", sp.simplify(P33) != 0, f"bare Pi^N_33(q=0) per k = {sp.factor(P33)}")
h = sp.simplify(P33/D**2); r32 = sp.simplify(P32/h); r22 = sp.simplify((P22 - P22_0)/h)
indep = all(sp.simplify(sp.diff(r, Ee)) == 0 for r in (r32, r22))
rep("K2b", indep and sp.simplify(D**2 - r32*sp.simplify(P23/h)/r22) == 0, "Pi33 - Pi32 Pi23/(Pi22 - Pi22(0)) == 0 after k-sum")

# ---- K3 coherence factor (u v' + v u')^2 = (1/2)(1 - (xi xi' - D^2)/(E E')), exact; q -> 0 limit D^2/E^2           [4.1]
xp = sp.symbols('xi_p', real=True); Dp = sp.symbols('Delta_p', positive=True)
E = sqrt(xi**2 + Dp**2); Ep = sqrt(xp**2 + Dp**2)
u2, v2, uv = (1 + xi/E)/2, (1 - xi/E)/2, Dp/(2*E); up2, vp2, upvp = (1 + xp/Ep)/2, (1 - xp/Ep)/2, Dp/(2*Ep)
lhs = u2*vp2 + v2*up2 + 2*uv*upvp
rhs = R(1, 2)*(1 - (xi*xp - Dp**2)/(E*Ep))
rep("K3", sp.simplify(lhs - rhs) == 0 and sp.simplify(rhs.subs(xp, xi) - Dp**2/E**2) == 0, "coherence identity (uv = Delta/2E) and q->0 limit")

# ---- K4 frak g_I, frak g_II (T = 0, omega << v_F q): quadrature vs closed forms; g_II = Mattis-Bardeen;
#      NEW closed form g_I(y_BCS) = (1 + 2/y_BCS) E(k) - 4/(y_BCS+2) K(k), k = (y_BCS-2)/(y_BCS+2)                                       [4.2]
th = sp.symbols('theta')
def gq(y, sgn):
    a = y/2 - 1; e = y/2 - a*sp.cos(th)
    return sp.Integral((e*(y - e) + sgn)/sqrt((e + 1)*(y - e + 1)), (th, 0, pi)).evalf(18)/y
def gI_cf(y): k = (y - 2)/(y + 2); return (1 + 2/y)*sp.elliptic_e(k**2) - 4/(y + 2)*sp.elliptic_k(k**2)
def MB(y):    k = (y - 2)/(y + 2); return (1 + 2/y)*sp.elliptic_e(k**2) - 4/y*sp.elliptic_k(k**2)
ok4 = True
for y in (R(20001, 10000), R(5, 2), 4, 5, 10, 100):
    a, b, c, d = gq(y, 1), gI_cf(y).evalf(18), gq(y, -1), MB(y).evalf(18)
    ok4 &= abs(a - b) < 1e-12 and abs(c - d) < 1e-12
    print(f"        y_BCS = {float(y):8.4f}   g_I = {float(a):.5f}  (closed {float(b):.5f})   g_II = {float(c):.5f}  (MB {float(d):.5f})")
ys = sp.symbols('y', positive=True)
lim2 = sp.limit(gI_cf(ys), ys, 2, '+')
rep("K4", ok4 and sp.simplify(lim2 - pi/2) == 0, f"quadrature == closed forms to 1e-12; g_I(2+) = {lim2} exactly; g_II == MB")

# ---- K5 massless isotropic Dirac cone, spin 2: Im delta eps_D = e^2/(12 pi v_F)                                   [5.1]
e2, thh, ve = sp.symbols('e2 theta v', positive=True)
ang = sp.integrate(sp.sin(thh)**3*2*pi, (thh, 0, pi))
ImEps = e2/q**2*pi*2/(2*pi)**3*q**2/4*ang/(2*ve)
rep("K5", sp.simplify(ImEps - e2/(12*pi*ve)) == 0, f"Im delta eps_D = {sp.simplify(ImEps)} (g_deg = 2, Delta_D = 0)")

# ---- K6 magnon normalisation -> 1905.13744 Eq. (12) prefactor                                                     [2.1]
S_, Om_ = sp.symbols('S Omega_c', positive=True)
rep("K6", sp.simplify((2*pi/Om_)*(S_/2)/(2*pi)**3 - (S_/Om_)/(8*pi**2)) == 0, "(2pi/Omega)(|S|/2)/(2pi)^3 = (|S|/Omega)/(8 pi^2)")

# ---- K7 Pauli-blocked kinematics e_- = (omega - E_q)^2/(4 E_q) (1512.04533 Eq. (13) lacks the 4)                   [4.3(b)]
m = sp.symbols('m', positive=True); pmin = m*w/q - q/2; Eq_ = q**2/(2*m)
rep("K7", sp.simplify(pmin**2/(2*m) - (w - Eq_)**2/(4*Eq_)) == 0, "e_- = (omega - E_q)^2/(4E_q)")

# ---- K8 URF golden rule -> 2609.06423 Eq. (9) prefactor                                                           [4.3(e)]
al, vv = sp.symbols('alpha v', positive=True)
urf = 2*pi*q**2/(q*vv)/(2*pi)**3*2*q**2/(4*pi*al)
rep("K8", sp.simplify(urf - q**3/(2*pi)**3/(al*vv)) == 0, "int d^3q delta -> 2pi q dq/v; S = (2q^2/e^2)L")

# ---- K9 exothermic shell Jacobian int q^2 dq delta(...) = m_chi q*                                                 [7.1]
Dx, w0, mc = sp.symbols('Delta_x omega_0 m_chi', positive=True)
arg = Dx - q**2/(2*mc) - w0
root = [r for r in sp.solve(arg, q) if r.is_positive is not False][0]
jac = (q**2/sp.Abs(sp.diff(arg, q))).subs(q, root)
rep("K9", sp.simplify(jac - mc*sqrt(2*mc*(Dx - w0))) == 0, "Jacobian = m_chi q*")

# ---- K10 two-magnon: FM V^B = 0; AFM u^2 - v^2 = 1 with |u v| = O(1) (S-independent)                             [2.4]
kk = sp.symbols('kk', real=True); gam = sp.cos(kk)
uk2 = (1/sqrt(1 - gam**2) + 1)/2; vk2 = (1/sqrt(1 - gam**2) - 1)/2
rep("K10", sp.simplify(uk2 - vk2 - 1) == 0 and sp.simplify(uk2*vk2 - gam**2/(4*(1 - gam**2))) == 0, "u^2 - v^2 = 1, u^2 v^2 = gamma^2/(4(1-gamma^2))")

# ---- K11 Mermin limits: diffusive == Drude, ballistic/diffusive = pi q l/6                                        [4.4]
wp, gr, kTF, l = sp.symbols('omega_p gamma_rel k_TF ell', positive=True)
Ddiff = vF*l/3
Ldiff = w/(kTF**2*Ddiff); Ldrude = w*gr/wp**2
Lball = pi*w*q/(2*kTF**2*vF)
ok11 = sp.simplify(Ldiff.subs(l, vF/gr) - Ldrude.subs(wp, kTF*vF/sqrt(3))) == 0 and sp.simplify(Lball/Ldiff - pi*q*l/6) == 0
eps_d = 1 + kTF**2*Ddiff/(Ddiff*q**2 - I*w)                 # full diffusive form: L -> w/(k_TF^2 D) for k_TF^2 >> q^2, w/D
Lfull = sp.im(-1/eps_d)
lim11 = sp.limit(sp.simplify(Lfull.subs(kTF, 1/t)*(1/t)**2*Ddiff/w), t, 0)
rep("K11", ok11 and sp.simplify(lim11 - 1) == 0, "L_diff = L_Drude (k_TF^2 = 3 w_p^2/v_F^2, l = v_F/gamma_rel); ratio pi q l/6; valid for any w/(D q^2)")

# ---- K12 chiral interference [3.3]: D_ab from c5, c8 vertices (WP0-v2 (2.2) matching), contracted with S^A
c5, c8 = sp.symbols('c5 c8'); qv = sp.symbols('q1:4', real=True); me, mx, gOA = sp.symbols('m_e m_chi gamma_OA', positive=True)
Sx = [sp.Matrix([[0, 1], [1, 0]])/2, sp.Matrix([[0, -I], [I, 0]])/2, sp.Matrix([[1, 0], [0, -1]])/2]
Nn = 1/(4*mx*me); eps3 = sp.LeviCivita
V = [sum((-I*eps3(a, b, d)*Sx[a]*qv[b]/me for a in range(3) for b in range(3)), sp.zeros(2))*c5*Nn - Sx[d]*c8*Nn for d in range(3)]
Dm = [[R(1, 2)*(V[d].H*V[e]).trace() for e in range(3)] for d in range(3)]
SA = [[I*sum(eps3(d, e, c)*qv[c] for c in range(3))*gOA for e in range(3)] for d in range(3)]   # S = S^S + i S^A, S^A = eps q gamma_OA
odd = sp.simplify(sp.expand(sum(Dm[d][e]*SA[d][e] for d in range(3) for e in range(3))))
q2 = sum(c**2 for c in qv)
target = q2*gOA*(c5*sp.conjugate(c8) + c8*sp.conjugate(c5))/2/(me*(4*mx*me)**2)
rep("K12", sp.simplify(odd - target) == 0, "odd part of tr[D S] = + q^2 Re(c5* c8) gamma_OA/(m_e (4 m_chi m_e)^2); Gamma_R - Gamma_L = 2x this (v1: -1/2x)")

# ---- K13 exothermic rate prefactor [7.2]: (1/(2pi)^3)(2pi/Omega) 4pi m q* = m q*/(pi Omega)
Omc, qs = sp.symbols('Omega q_star', positive=True)
rep("K13", sp.simplify((2*pi/Omc)/(2*pi)**3*4*pi*mc*qs - mc*qs/(pi*Omc)) == 0, "Gamma_chi^(nu) = m_chi q*/(pi Omega) <D |calE|^2>")

# ---- K14 spectral budget [1.3]: 4 J m_e a^2 with J = 10 meV, a = 4 A (hbar c = 1973.27 eV A)
J, me_eV, a = R(1, 100), 510999, 4/R('1973.27')
val = 4*J*me_eV*a**2
rep("K14", abs(float(val) - 0.084) < 0.002, f"4 J m_e a^2 = {float(val):.4f} (v1 quoted 2%: missing factor 4)")

# ---- K15 QP-generation spectrum [4.6] is normalised: int dE1 P(E1|omega) = 1 (Delta = 1, y_BCS = 5)
e1 = sp.symbols('e1'); y5 = 5
a5 = R(y5, 2) - 1; e = R(y5, 2) - a5*sp.cos(th)
Pint = sp.Integral((e*(y5 - e) + 1)/sqrt((e + 1)*(y5 - e + 1)), (th, 0, pi)).evalf(18)/(y5*gI_cf(sp.Integer(y5)).evalf(18))
rep("K15", abs(Pint - 1) < 1e-12, f"int P(E1|omega) dE1 = {float(Pint):.12f}; eta_pb = Delta_BCS N_qp/omega (= 2Delta/omega for omega < 3Delta)")

# ---- K16 Al kinematics: q xi_coh >= 2 v_F/(pi v_max), Delta/(v_F q) <= v_max/(2 v_F)                                [4.3], WP5 R5
vmax = R(7945, 10)/299792.458; vFAl = R(68, 10000)
rep("K16", abs(float(2*vFAl/(pi*vmax)) - 1.63) < 0.01 and abs(float(vmax/(2*vFAl)) - 0.195) < 0.002,
    f"q xi_coh >= {float(2*vFAl/(pi*vmax)):.2f}; Delta/(v_F q) <= {float(vmax/(2*vFAl)):.3f}")

# ---- K17 Dirac charge renormalisation: int_0^1 x(1-x) = 1/6 -> Re delta eps_D/eps_bg = (alpha~/6pi) ln(4 Lambda_D^2 v_F^2/s)
xx = sp.symbols('xx'); alpha = 1/R('137.036')
at = alpha*2/(40*R(4, 10000))
re = at/(6*pi)*sp.log((2*R(4, 10000)*200/R(1, 100))**2)          # Lambda_D = 200 eV, sqrt(s) = 10 meV
rep("K17", sp.integrate(xx*(1 - xx), (xx, 0, 1)) == R(1, 6) and abs(float(at) - 0.912) < 0.002 and abs(float(re) - 0.268) < 0.003,
    f"alpha~ = {float(at):.3f}; Re delta eps/eps_bg = {float(re):.3f}; rate factor 1/(1+re)^2 = {float(1/(1 + re)**2):.2f}")

# ---- K18 kinematic numbers with v_max = 794.5 km/s (CONVENTIONS sec. 8)
EbP, EZPL = R(456, 10000), R(1945, 1000)
mminP = 2*EbP/vmax**2; qminP = EbP/vmax; mNV = 2*EZPL/vmax**2; qNV = EZPL/vmax
rep("K18", abs(float(mminP) - 1.30e4) < 100 and abs(float(qminP) - 17.2) < 0.2 and abs(float(mNV) - 5.54e5) < 5e3 and abs(float(qNV) - 734) < 3,
    f"Si:P m_min = {float(mminP)/1e3:.1f} keV, q_min = {float(qminP):.1f} eV; NV m_min = {float(mNV)/1e6:.3f} MeV, q_min = {float(qNV):.0f} eV")

# ---- K19 hyperfine contact (WP4-D1, applied in WP0-v2 (1.2)): -mu_e.B, mu_e = -g_e mu_B s, B = (2/3) g_I mu_N I delta
ge, muB, gI, muN = sp.symbols('g_e mu_B g_I mu_N', real=True); s_, Ivec = sp.symbols('s I', real=True)
H = -(-ge*muB*s_)*(R(2, 3)*gI*muN*Ivec)
rep("K19", sp.simplify(H - R(2, 3)*ge*muB*gI*muN*s_*Ivec) == 0 and sp.simplify(H.subs(s_, sp.Symbol('sigma')/2) - R(1, 3)*ge*muB*gI*muN*sp.Symbol('sigma')*Ivec) == 0,
    "H_FC = +(2/3) g_e mu_B g_I mu_N s.I = +(1/3)(...) sigma.I")

# ---- K20 one-phonon phase with CONVENTIONS sec. 5 eigenvectors: e^{i(Q+G).(R+r)} e^{-iQ.R} = e^{iq.r} (G.R in 2piZ)  [7.2]
Gs, Rs, Qs, rs, nint = sp.symbols('G R Q r n', real=True)
ph = sp.exp(I*(Qs + Gs)*(Rs + rs))*sp.exp(-I*Qs*Rs)
rep("K20", sp.simplify(sp.expand(ph/sp.exp(I*Gs*Rs)) - sp.exp(I*(Qs + Gs)*rs)) == 0, "phase = e^{iG.R} e^{i q.r_kappa} -> e^{i q.r_kappa} (e^{iG.R} = 1), not e^{i G.r_kappa}")

# ---- K21 ZrTe5 background anisotropy (eps_bg,xx/eps_bg,yy)^2 with clamped-ion (187.5, 9.8, 90.9)
rep("K21", abs((R(1875, 10)/R(98, 10))**2 - 366) < 1, f"(eps_xx/eps_yy)^2 = {float((R(1875, 10)/R(98, 10))**2):.0f}")

print(f"{sum(RES)}/{len(RES)} PASS" + ("  ALL PASS" if all(RES) else "  SOME FAIL"))
