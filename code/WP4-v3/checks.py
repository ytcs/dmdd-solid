"""WP4-v3 identity checks (R8 revision of returns/R6/WP4-v2.md after the R7 referee reports REF-WP4-A/B).
Sympy only (exact algebra; Integral.evalf for 1-D quadratures; evalf of closed-form 2x2 matrix functions). No numerical simulation.
Run:  python3 -I checks.py     Prints PASS/FAIL per check. Labels WP4v3-Kn (CONVENTIONS sec. 14); K1-K21 keep their v2 meaning
(K11 rebuilt: REF-B called its ratio test tautological; K15/K16/K17/K21 extended); K22-K32 are new (R8); K33-K34 added in the R9 clean-up (mpmath, sympy's numerical backend,
for exact diagonalisation of small model matrices and 1-D quadratures).
Notation: NOTATION v4 (Delta_BCS, g_I -> frak g_I, eps_bg, Lambda_D, L, v_C, ...). No numerical simulation."""
import sympy as sp
from sympy import Rational as R, pi, sqrt, I

RES = []
def rep(k, cond, note=""):
    RES.append(bool(cond)); print(f"{'PASS' if cond else 'FAIL'}  WP4v3-{k:5s} {note}")

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

# ---- K11 Mermin limits, now DERIVED from [4.3] (REF-WP4-B: the v2 ratio test only checked the quoted asymptotes)        [4.3]-[4.4]
#      Hypothesis q << k_F (small-q Lindhard bracket f(z) = (eps_Lin(q,z)-1)/(eps_Lin(q,0)-1) = 1 - (z/u) atanh(u/z), u = q v_F, z = w + i gamma_rel)
wp, gr, kTF, l = sp.symbols('omega_p gamma_rel k_TF ell', positive=True)
zz_, uu = sp.Symbol('z'), sp.Symbol('u', positive=True); cc = sp.symbols('c', positive=True)
fL = 1 - zz_/uu*sp.atanh(uu/zz_)
ok_ser = sp.simplify(sp.series(fL, uu, 0, 6).removeO() - (-uu**2/(3*zz_**2) - uu**4/(5*zz_**4))) == 0     # |z| >> u (diffusive side)
zM = w + I*gr
def epsM1(f, K): return zM*K*f/(w + I*gr*f)                     # [4.3] minus 1 with eps_Lin(z) - 1 = K f, eps_Lin(0) - 1 = K
Ddiff = vF**2/(3*gr)                                             # = v_F l/3 with l = v_F/gamma_rel
Ed = epsM1((-uu**2/(3*zz_**2)).subs({uu: t*vF, zz_: zM}), kTF**2/t**2).subs(w, cc*t**2)   # q = t, w = c t^2 (w ~ D q^2)
ok_diff = sp.simplify(sp.limit(sp.simplify(Ed*t**2), t, 0) - kTF**2*Ddiff/(Ddiff - I*cc)) == 0   # -> 1 + k_TF^2 D/(D q^2 - i w)
zn = R(1, 100) + R(2, 100)*I                                     # retarded branch, |z| << u (u = 1): f = 1 + i pi z/(2u) - z^2/u^2 + O(z^3)
ok_br = abs((1 - zn/2*sp.log((zn + 1)/(zn - 1))).evalf(30) - (1 + I*pi*zn/2 - zn**2).evalf(30)) < 1e-6
fb = 1 + I*pi*zM/(2*uu) - zM**2/uu**2
gb = sp.simplify(zM*fb/(w + I*gr*fb))                            # eps_Mer - 1 = K g; L = Im g/(K|g|^2) + O(1/K^2)  (k_TF >> q)
Lb = sp.simplify(sp.im(sp.expand_complex(gb))/sp.expand_complex(gb*sp.conjugate(gb)))
ok_ball = sp.limit(Lb*uu*2/(pi*w), uu, sp.oo) == 1              # L_ball = pi w q/(2 k_TF^2 v_F), up to O(1/(q l))
eps_d = 1 + kTF**2*Ddiff/(Ddiff*q**2 - I*w)
lim11 = sp.limit(sp.simplify(sp.im(-1/eps_d).subs(kTF, 1/t)*(1/t)**2*Ddiff/w), t, 0)   # L_diff = w/(k_TF^2 D), any w/(D q^2)
Ldiff = w/(kTF**2*Ddiff); Lball = pi*w*q/(2*kTF**2*vF)
ok_dr = sp.simplify(Ldiff - w*gr/wp**2).subs(wp, kTF*vF/sqrt(3)) == 0      # = Drude (k_TF^2 = 3 w_p^2/v_F^2)
rep("K11", ok_ser and ok_diff and ok_br and ok_ball and sp.simplify(lim11 - 1) == 0 and ok_dr and sp.simplify(Lball/Ldiff - pi*q*(vF/gr)/6) == 0,
    "[4.3] -> diffusive 1 + k_TF^2 D/(Dq^2 - iw) and ballistic L = pi w q/(2 k_TF^2 v_F) (q << k_F, k_TF); ratio pi q l/6 derived")

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
rep("K12", sp.simplify(odd - target) == 0, "odd part of sum_ab D_ab S_ab (= tr[D^T S]) = + q^2 Re(c5* c8) gamma_OA/(m_e (4 m_chi m_e)^2); Gamma_R - Gamma_L = 2x this")

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
rep("K15", abs(Pint - 1) < 1e-12, f"int P(E1|omega) dE1 = {float(Pint):.12f}; eta_pb = Delta_BCS N_qp/omega (= 2Delta/omega for omega < 4Delta, K27)")

# ---- K16 Al kinematics: q xi_coh >= 2 v_F/(pi v_max), Delta/(v_F q) <= v_max/(2 v_F); q_min = 2 Delta/v_max in eV (v2: "keV")  [4.3], WP5 R5
vmax = R(7945, 10)/299792.458; vFAl = R(68, 10000); DAl = R(17, 100000)                   # Delta_BCS(Al) = 0.17 meV, in eV
qminAl = 2*DAl/vmax; xiAl = vFAl/(pi*DAl)                                                   # eV; eV^-1
rep("K16", abs(float(2*vFAl/(pi*vmax)) - 1.63) < 0.01 and abs(float(vmax/(2*vFAl)) - 0.195) < 0.002 and abs(float(qminAl) - 0.128) < 0.002
    and abs(float(qminAl*xiAl) - 1.63) < 0.01,
    f"q xi_coh >= {float(2*vFAl/(pi*vmax)):.2f}; Delta/(v_F q) <= {float(vmax/(2*vFAl)):.3f}; q_min = {float(qminAl):.3f} eV (not keV), xi_coh = {float(xiAl):.1f}/eV")

# ---- K17 Dirac charge renormalisation, both cutoff schemes (REF-WP4-A V4):
#      (a) e^{-5/6}-redefined cutoff [v2]: Re delta eps_D/eps_bg = (alpha~/6pi) ln(4 Lambda_D^2 v_F^2/s)
#      (b) 1708.08929 Eq. (2.6) literal: + int x(1-x) ln[1/(x(1-x))] = 5/18, i.e. (alpha~/6pi)[ln(...) + 5/3]
xx = sp.symbols('xx', positive=True); alpha = 1/R('137.036')
at = alpha*2/(40*R(4, 10000))
lg = sp.log((2*R(4, 10000)*200/R(1, 100))**2)                    # Lambda_D = 200 eV, v_F = 4e-4, sqrt(s) = 10 meV
re = at/(6*pi)*lg; re_b = at/(6*pi)*(lg + R(5, 3))
I518 = sp.integrate(xx*(1 - xx)*sp.log(1/(xx*(1 - xx))), (xx, 0, 1))
rep("K17", sp.integrate(xx*(1 - xx), (xx, 0, 1)) == R(1, 6) and sp.simplify(I518 - R(5, 18)) == 0 and abs(float(at) - 0.912) < 0.002
    and abs(float(re) - 0.268) < 0.003 and abs(float(re_b) - 0.349) < 0.003 and abs(float(1/(1 + re_b)**2) - 0.55) < 0.01,
    f"alpha~ = {float(at):.3f}; Re delta eps/eps_bg = {float(re):.3f} (a) / {float(re_b):.3f} (b); rate factor {float(1/(1 + re)**2):.2f} / {float(1/(1 + re_b)**2):.2f}")

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

# ---- K21 ZrTe5 background anisotropy (eps_bg,xx/eps_bg,yy)^2: clamped-ion (187.5, 9.8, 90.9) [1708.08929]; DFT (308.4, 20.75) [1910.02091]
r21a = (R(1875, 10)/R(98, 10))**2; r21b = (R(3084, 10)/R(2075, 100))**2
rep("K21", abs(r21a - 366) < 1 and abs(r21b - 221) < 1, f"(eps_xx/eps_yy)^2 = {float(r21a):.0f} (1708 table) / {float(r21b):.0f} (1910 values); rate larger for q || y")

# ======================== R8 additions (K22-K31) ========================
# ---- K22 L16 scattering, eps_bg^2 [5.3]: golden rule with bare vertex, sum_f |f|^2 delta ∝ (q^2/e^2) Im eps_tot = Im delta eps_D.
#      Source (1708.08929 Eqs. (3.7),(3.11); 1910.02091 Eqs. (2.7),(3.14)): times |F_med|^2 = 1/|eps_r|^2, eps_r = eps/eps_bg.
#      URF (WP0-v2 (5.3)/(5.4)): Im eps/|eps|^2.  Ratio = eps_bg^2 for ANY complex delta eps_D; anisotropic: eps_bg -> qhat.eps_bg.qhat
eb = sp.symbols('epsilon_bg', positive=True); dr, di = sp.symbols('d_r d_i', real=True)
dD = dr + I*di; epst = eb + dD; epsr = epst/eb
R_src = di/sp.expand_complex(epsr*sp.conjugate(epsr)); R_urf = di/sp.expand_complex(epst*sp.conjugate(epst))
ex1, ex2, ex3, qh1, qh2, qh3 = sp.symbols('e_xx e_yy e_zz qh1 qh2 qh3', positive=True)
eq = ex1*qh1**2 + ex2*qh2**2 + ex3*qh3**2                       # qhat.eps_bg.qhat (principal axes)
ratio_aniso = sp.simplify((di/sp.expand_complex((1 + dD/eq)*sp.conjugate(1 + dD/eq)))/(di/sp.expand_complex((eq + dD)*sp.conjugate(eq + dD))))
rep("K22", sp.simplify(R_src/R_urf - eb**2) == 0 and sp.simplify(ratio_aniso - eq**2) == 0,
    "Rate_src/Rate_URF = eps_bg^2 exactly (any delta eps_D); anisotropic (qhat.eps_bg.qhat)^2; = 1600 at eps_bg = 40")

# ---- K23 the corrected explanation [5.3]: absorbing the '1' into Lambda'_D is an identity common to both theories.
#      Re eps_r = 1 + A ln(X^2/s), A = alpha~/(6 pi) = e^2 g/(24 pi^2 eps_bg v_F)  =>  = A ln(X'^2/s), X' = X e^{1/(2A)}, 1/(2A) = 3pi/alpha~.
#      1/|eps_r|^2 = (1/A^2)/|L'|^2 (explicit eps_bg^2 in the source rate), 1/|eps|^2 = 1/((eps_bg A)^2 |L'|^2) with eps_bg A eps_bg-free.
al_, gd, vf_, X, s_s, Lp = sp.symbols('alpha g_deg v_F X s Lambda_p', positive=True)
e2_ = 4*pi*al_; A_ = e2_*gd/(24*pi**2*eb*vf_); atl = al_*gd/(eb*vf_)
id1 = sp.simplify(A_ - atl/(6*pi)) == 0 and sp.simplify(1/(2*A_) - 3*pi/atl) == 0 and sp.simplify(1/(2*A_) - 12*pi**2*eb*vf_/(e2_*gd)) == 0
Xp = X*sp.exp(1/(2*A_))
id2 = sp.simplify(sp.expand_log(1 + A_*sp.log(X**2/s_s) - A_*sp.log(Xp**2/s_s), force=True)) == 0
pref_src = 1/A_**2; pref_urf = 1/(eb*A_)**2
id3 = sp.simplify(pref_src/2 - 288*pi**4*eb**2*vf_**2/(e2_**2*gd**2)) == 0 and sp.diff(pref_urf, eb) == 0 and sp.simplify(pref_src/pref_urf - eb**2) == 0
rep("K23", id1 and id2 and id3, "Lambda'_D = Lambda_D exp(3pi/alpha~) common to both; 1708 (3.14) prefactor 288pi^4 k^2 v_F^2/(e^4 g^2) = (1/2)/A^2 is the omitted eps_bg^2")

# ---- K24 dark-photon absorption, eps_bg (not eps_bg^2) [5.5]: kappa_eff^2 = kappa_mix^2 m^4/|m^2 - Pi|^2, Gamma = -kappa_eff^2 Im Pi/omega,
#      omega = m_phi, k -> 0: Pi = m^2 (1 - eps) (total charge) vs source Pi = m^2 (1 - eps_r)  =>  Gamma_src/Gamma_URF = eps_bg
km, mph = sp.symbols('kappa_mix m_phi', positive=True); ar, ai = sp.symbols('a_r a_i', real=True)
er_ = ar + I*ai
def Gam(eps_):
    Pi = mph**2*(1 - eps_); den = sp.expand_complex((mph**2 - Pi)*sp.conjugate(mph**2 - Pi))
    return sp.simplify(km**2*mph**4/den*(-sp.im(sp.expand_complex(Pi)))/mph)
G_true, G_src = Gam(eb*er_), Gam(er_)
ok24 = sp.simplify(G_src/G_true - eb) == 0 and sp.simplify(G_true - km**2*mph*sp.im(sp.expand_complex(-1/(eb*er_)))) == 0
rep("K24", ok24, "Gamma_abs,src/Gamma_abs,URF = eps_bg (per principal polarisation: eps_bg,ii); URF = kappa_mix^2 m Im(-1/eps) (WP0-v2 L9b)")

# ---- K25 2609.06423 Eqs. (4),(7)-(8): time-ordered == retarded for omega > 0 (full complex Pi, not only Im); differ only at omega < 0
eta = sp.symbols('eta', positive=True); Omg, xr = sp.symbols('Omega_p x', real=True)
dTR = 1/(w + Omg - I*eta) - 1/(w + Omg + I*eta)                 # second-pole term, time-ordered minus retarded
ok25a = sp.limit(dTR.subs(Omg, 1), eta, 0) == 0                 # omega > 0, Omega > 0: no pole, identical
ok25b = sp.integrate(sp.simplify(dTR.subs(w, xr - Omg)), (xr, -sp.oo, sp.oo)) == 2*pi*I   # = 2 pi i delta(omega + Omega): weight at omega < 0 only
rep("K25", ok25a and ok25b, "Pi^T(omega) = Pi^R(omega) for omega > 0 at T = 0; difference 2 pi i delta(omega + E + E') lives at omega < 0")

# ---- K26 [3.2] density channel: omega^2 S_nn = q_a q_b S_{j^a j^b} (continuity); q-linear odd part of S_jj -> odd S_nn is O(q^3)
qs3 = sp.symbols('p1:4', real=True); Om2 = sp.symbols('omega_s', positive=True)
A2 = [[sp.Symbol(f'A{a}{b}') for b in range(3)] for a in range(3)]
B3 = [[[sp.Symbol(f'B{a}{b}{c}') for c in range(3)] for b in range(3)] for a in range(3)]
C4 = [[[[sp.Symbol(f'C{a}{b}{c}{d}') for d in range(3)] for c in range(3)] for b in range(3)] for a in range(3)]
def Sjj(a, b, p): return A2[a][b] + sum(B3[a][b][c]*p[c] for c in range(3)) + sum(C4[a][b][c][d]*p[c]*p[d] for c in range(3) for d in range(3))
def Snn(p): return sp.expand(sum(p[a]*p[b]*Sjj(a, b, p) for a in range(3) for b in range(3))/Om2**2)
odd = sp.expand((Snn(qs3) - Snn([-x for x in qs3]))/2)
tt = sp.symbols('tt', positive=True)
deg = sp.Poly(sp.expand(odd.subs({qs3[i]: tt*qs3[i] for i in range(3)})), tt)
cub = sp.expand(sum(qs3[a]*qs3[b]*qs3[c]*B3[a][b][c] for a in range(3) for b in range(3) for c in range(3))/Om2**2)
rep("K26", min(m[0] for m in deg.monoms()) == 3 and sp.simplify(odd - cub) == 0,
    "S_nn(q) - S_nn(-q) = 2 q_a q_b q_c b^NR_abc/omega^2 + O(q^5): density odd part O(q^3), even part O(q^2)")

# ---- K27 N_qp = 2 up to omega < 4 Delta_BCS [4.6]: largest prompt QP E1 <= omega - Delta; a pair-breaking phonon needs E1 - Delta >= 2 Delta
Dl = sp.symbols('Delta', positive=True)
sol27 = sp.solve_univariate_inequality((w - Dl) - Dl >= 2*Dl, w, relational=False)
rep("K27", sol27 == sp.Interval(4*Dl, sp.oo), f"third QP possible only for omega in {sol27}: N_qp = 2, eta_pb = 2 Delta/omega for omega < 4 Delta (v2: 3 Delta)")

# ---- K28 Al: Q_+ < 1 <=> omega < q v_F - q^2/2m_e; with omega <= q v_max: q < 2 k_F (1 - v_max/v_F); m_chi threshold (q_max = 2 m_chi v_max)
meV_ = 510999; kFAl = meV_*vFAl
Qp_ = q/(2*kF) + w/(q*vF)
ok28a = sp.simplify((Qp_ - 1).subs(kF, m*vF)*q*vF - (w - (q*vF - q**2/(2*m)))) == 0
qQ = 2*kFAl*(1 - vmax/vFAl); mQ = qQ/(2*vmax)
rep("K28", ok28a and abs(float(qQ) - 4240) < 20 and abs(float(mQ)/1e6 - 0.80) < 0.01,
    f"[4.2] hypothesis Q_+ < 1 guaranteed for q < {float(qQ)/1e3:.2f} keV; fails somewhere for m_chi > {float(mQ)/1e6:.2f} MeV")

# ---- K29 exothermic example validity [7.2]: v* = sqrt(2|Delta_chi|/m_chi) (omega_nu << |Delta_chi|)
def vstar(mchi, Dchi): return sqrt(2*Dchi/mchi)
v1, v50 = vstar(10**6, 1), vstar(10**6, 50)
rep("K29", abs(float(v1) - 1.414e-3) < 1e-5 and abs(float(vmax/v1) - 1.87) < 0.01 and abs(float(vmax/v50) - 0.265) < 0.003
    and abs(float(sqrt(2*10**6*50))/1e3 - 10.0) < 0.01,
    f"(1 MeV, 1 eV): v_max/v* = {float(vmax/v1):.2f} (outside validity); (1 MeV, 50 eV): v_max/v* = {float(vmax/v50):.3f}, q* = 10 keV")

# ---- K30 Theorem D-g (a) cross terms [8]: bin function f_D(x) = g(x/D)/D; ||f_D(w-H) - f_D(w-H_d)|| <= c_g ||H - H_d||/D^2,
#      c_g = (1/2pi) int |s| |g^(s)| ds (Duhamel/Fourier bound); Gaussian g: c_g = 1/pi. f_D(w - H_d) is sector-diagonal: no cross terms.
sv = sp.symbols('s_v', real=True)
cg = sp.integrate(sp.Abs(sv)*sp.exp(-sv**2/2), (sv, -sp.oo, sp.oo))/(2*pi)
def fD(x, Dw): return sp.exp(-x**2/(2*Dw**2))/(sqrt(2*pi)*Dw)
def matf(Hm, wv, Dw):
    P, Dg = Hm.diagonalize(normalize=True)
    return P*sp.diag(*[fD(wv - Dg[i, i], Dw) for i in range(Hm.shape[0])])*P.H
ok30 = sp.simplify(cg - 1/pi) == 0
worst = 0
for (a1, hh, Dw, wv) in [(1, R(1, 20), R(3, 10), R(1, 2)), (R(1, 2), R(1, 10), R(1, 5), R(1, 4)), (2, R(1, 100), R(1, 2), 1)]:
    Hd = sp.diag(0, a1); Hf = Hd + hh*sp.Matrix([[0, 1], [1, 0]])
    Dmat = (matf(Hf, wv, Dw) - matf(Hd, wv, Dw)).evalf(30)
    nrm = max(abs(ev) for ev in Dmat.eigenvals().keys())
    bound = (cg*hh/Dw**2).evalf(30)
    worst = max(worst, float(nrm/bound)); ok30 &= nrm <= bound
rep("K30", ok30, f"c_g = {cg} (Gaussian bin); 2x2 tests: ||cross|| / bound <= {worst:.3f}; relative cross terms O(h_off/Delta_omega_bin)")

# ---- K31 WSi (2412.16279 per both referees' FT reading): E_F = 7 eV, Gamma = 0.1 E_F; k_F, k_TF = (4 alpha m_e k_F/pi)^{1/2}, l = v_F/Gamma
EF_W = 7; kFW = sqrt(2*meV_*EF_W); kTFW = sqrt(4*alpha*meV_*kFW/pi); vFW = kFW/meV_; lW = vFW/(R(7, 10))   # eV^-1
hc = R('1973.27')                                                # eV Angstrom
rep("K31", abs(float(kFW) - 2675) < 10 and abs(float(kTFW) - 3560) < 30 and abs(float(lW*hc)/10 - 1.47) < 0.02
    and abs(float(1000*lW) - 7.5) < 0.1 and abs(float(pi*R(3, 2)/6) - 0.785) < 0.001,
    f"k_F = {float(kFW)/1e3:.2f} keV, k_TF = {float(kTFW)/1e3:.2f} keV (q = 1-5 keV not << either); l = {float(lW*hc)/10:.2f} nm, q l = {float(1000*lW):.1f}-{float(5000*lW):.0f}")

# ---- K32 Re eps^BCS in the DM region (A-V6 / REF-A sec. 2.3: v2's "Re eps^BCS = Re eps^nor [1 + O(Delta^2/v_F^2 q^2)]" was asserted) [4.2']
#      KK of delta Im eps = Im eps^nor [g_I(y) Theta(y-2) - 1], Im eps^nor = (pi/2)(k_TF^2/q^2) omega/(q v_F):
#      delta Re eps/Re eps^nor = (Delta/(q v_F)) h(y),  h(y) = P int_0^oo dy' y'^2 G(y')/(y'^2 - y^2),  G = g_I Theta(y'-2) - 1.
#      (i) sum rule h(0) = int_0^oo G dy = 0, i.e. int_2^oo (g_I - 1) dy = 2; tail from g_I - 1 = (2 ln 2y - 1)/y^2 + ...; (ii) h(5.01) ~ 1.05
yv = sp.symbols('y_v', positive=True); Yc = 10**5
segs = [2, R(5, 2), 3, 5, 10, 30, 100, 1000, 10**4, Yc]
Ssum = sum(sp.Integral(gI_cf(yv) - 1, (yv, a_, b_)).evalf(20) for a_, b_ in zip(segs[:-1], segs[1:]))
tail = ((2*sp.log(2*Yc) + 1)/Yc).evalf(20)
asym = ((gI_cf(sp.Integer(Yc)) - 1)*Yc**2 - (2*sp.log(2*Yc) - 1)).evalf(20)
y0 = R(501, 100); G0 = (gI_cf(y0) - 1).evalf(25)
hexpr = (yv**2*(gI_cf(yv) - 1) - y0**2*G0)/(yv**2 - y0**2)           # subtracted PV form (P int dy'/(y'^2 - y^2) = 0)
segs2 = [2, R(5, 2), 3, 4, R(9, 2), R(49, 10), R(52, 10), 6, 10, 30, 100, 1000, 10**4, Yc]
h5 = (sp.Integral((-yv**2 - y0**2*G0)/(yv**2 - y0**2), (yv, 0, 2)).evalf(15) + sum(sp.Integral(hexpr, (yv, a_, b_)).evalf(15)
      for a_, b_ in zip(segs2[:-1], segs2[1:])) + tail - y0**2*G0/Yc)
rep("K32", abs(float(Ssum + tail - 2)) < 1e-6 and abs(float(asym)) < 1e-6 and abs(float(h5) - 1.05) < 0.01,
    f"int_0^oo G dy = {float(Ssum + tail - 2):.1e} (h(0) = 0); h(5) = {float(h5):.3f}: delta L/L = -2 (Delta/q v_F) h = -{float(2*vmax/vFAl*h5/y0):.2f} at the Al edge (KK to oo; cutoff spread in K34)")

# ======================== R9 clean-up additions (K33-K34) ========================
import mpmath as mp            # sympy's numerical backend (lambdify target); exact model matrices, no simulation
mp.mp.dps = 30
# ---- K33 restated (G5') / [8.1'] (VER-WP4-A N1, VER-WP4-B N2): state-restricted Duhamel bound and the size of h_off.
#      (i) golden rule: Gamma = 2 pi |V|^2 rho, sum_f |V_f|^2 = |V|^2 rho W_c  =>  h_off = ||H_off phi|| = sqrt(Gamma W_c/(2 pi)) >> Gamma.
#      (ii) star model (level phi + N continuum levels over W_c, coupling V): ||(f(w-H) - f(w-H_d)) phi|| <= c_g h_off/Delta^2 with
#           h_off = sup_s ||H_off e^{-iH_d s} phi|| = sqrt(N) V (phi is an H_d eigenstate), exact diagonalisation.
#      (iii) extensivity: M independent copies (free fermions): many-body ||H_off|| = sum of positive one-body eigenvalues = M sqrt(N) V,
#           while ||H_off phi|| for one particle stays sqrt(N) V: the operator-norm (G5) of v3 is vacuous in bulk.
Vs, rho, Wc = sp.symbols('V rho W_c', positive=True)
Gs = 2*pi*Vs**2*rho
ok33a = sp.simplify(sp.sqrt(Vs**2*rho*Wc) - sp.sqrt(Gs*Wc/(2*pi))) == 0
def star(N, W, V, Dw, wv):
    d = mp.mpf(W)/N; E = [-mp.mpf(W)/2 + d*(j + mp.mpf(1)/2) for j in range(N)]
    Hd = mp.zeros(N + 1, N + 1)
    for j in range(N): Hd[j + 1, j + 1] = E[j]
    Hf = Hd.copy()
    for j in range(N): Hf[0, j + 1] = V; Hf[j + 1, 0] = V
    def fm(H):
        ev, Q = mp.eigsy(H)
        return Q*mp.diag([mp.exp(-(wv - e)**2/(2*Dw**2))/(mp.sqrt(2*mp.pi)*Dw) for e in ev])*Q.T
    ph = mp.zeros(N + 1, 1); ph[0] = 1
    df = (fm(Hf) - fm(Hd))*ph
    nrm = mp.sqrt(sum(df[i]**2 for i in range(N + 1)))
    hoff = mp.sqrt(N)*V; Gam = 2*mp.pi*V**2/d
    return nrm, hoff/(mp.pi*Dw**2), hoff, mp.sqrt(Gam*W/(2*mp.pi)), Gam
ok33b, worst33, rat = True, 0, []
for args in [(8, 4, mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('0.3')), (16, 4, mp.mpf('0.07'), mp.mpf('0.5'), 0), (24, 6, mp.mpf('0.05'), 1, mp.mpf('0.5'))]:
    nrm, bnd, hoff, gr_, Gam = star(*args)
    ok33b &= nrm <= bnd and abs(hoff - gr_) < 1e-20; worst33 = max(worst33, float(nrm/bnd)); rat.append(float(hoff/Gam))
Ms, Nst, Vst = 3, 6, mp.mpf('0.1')
hone = mp.zeros(Nst + 1, Nst + 1)
for j in range(Nst): hone[0, j + 1] = Vst; hone[j + 1, 0] = Vst
evs = list(mp.eigsy(hone)[0])*Ms                                   # M decoupled copies: one-body spectrum repeated
opnorm_MB = sum(e for e in evs if e > 0)                           # many-body ground/top-state norm of a quadratic H_off
ok33c = abs(opnorm_MB - Ms*mp.sqrt(Nst)*Vst) < 1e-20
rep("K33", ok33a and ok33b and ok33c,
    f"h_off = sqrt(Gamma W_c/2pi) (h_off/Gamma = {', '.join(f'{r:.1f}' for r in rat)} in the tests); state-restricted bound holds (max ratio {worst33:.2f}); "
    f"many-body ||H_off|| = M sqrt(N) V (extensive), ||H_off phi|| = sqrt(N) V")

# ---- K34 [4.2'] validity domain (VER-WP4-B N1, VER-WP4-A N2): |dL/L| = 2 (v_max/v_F) s_BCS(y)/y at the Al edge q = omega/v_max,
#      with the KK integral to infinity and with a sharp cutoff at Y = q v_F/Delta = y v_F/v_max (Im eps^nor linear only for omega' < q v_F)
yv4 = sp.symbols('y4', positive=True); k4 = (yv4 - 2)/(yv4 + 2)
gI_m = sp.lambdify(yv4, (1 + 2/yv4)*sp.elliptic_e(k4**2) - 4/(yv4 + 2)*sp.elliptic_k(k4**2), 'mpmath')
def Gm(y): return mp.mpf(-1) if y < 2 else gI_m(y) - 1
def s_cut(y0, Y):
    y0 = mp.mpf(y0); G0 = Gm(y0); Y = mp.mpf(Y)
    pts = sorted(set([mp.mpf(0), mp.mpf(2), y0] + [mp.mpf(p) for p in (3, 5, 10, 30, 100, 1000) if abs(p - y0) > 1e-9 and p < Y])) + [Y]
    return mp.quad(lambda t: (t**2*Gm(t) - y0**2*G0)/(t**2 - y0**2), pts) + y0**2*G0*mp.log((Y - y0)/(Y + y0))/(2*y0)
vr = mp.mpf(vmax)/mp.mpf(vFAl)
tab = {}
for y0 in (mp.mpf('2.2'), mp.mpf('2.5'), mp.mpf(3), mp.mpf('5.01'), mp.mpf(10)):
    sinf = s_cut(y0, 10**4) + (2*mp.log(2*10**4) + 1)/10**4
    tab[float(y0)] = (float(2*vr*sinf/y0), float(2*vr*s_cut(y0, y0/vr)/y0))
ok34 = (abs(tab[2.2][0] - 1.42) < 0.01 and abs(tab[2.5][0] - 0.88) < 0.01 and abs(tab[3.0][0] - 0.53) < 0.01
        and abs(tab[5.01][0] - 0.163) < 0.002 and 0.06 < tab[5.01][1] < 0.09 and all(v[0] > 0 for v in tab.values()))
rep("K34", ok34, "edge |dL/L| (KK to oo / cut at q v_F): " + "; ".join(f"y={k:g}: {v[0]:.2f}/{v[1]:.2f}" for k, v in tab.items())
    + "; s_BCS > 0 => L lowered; [4.2'] fails for y <~ 3.5 at the edge")

print(f"{sum(RES)}/{len(RES)} PASS" + ("  ALL PASS" if all(RES) else "  SOME FAIL"))
