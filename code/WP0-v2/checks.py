"""WP0-v2 identity checks (R6 revision). Sympy only, exact arithmetic; no numerics beyond evalf of exact numbers.
Run:  python3 -I checks.py      Prints PASS/FAIL per check. Labels are WP0v2-Cn (CONVENTIONS sec. 14).
Each check names the WP0-v2 equation it supports. Notation: NOTATION v4 (v_C, R, R~, eps, S, L, ...)."""
import sympy as sp
from sympy import I, Rational as Q, Matrix, eye, zeros, simplify, sqrt, pi, exp, oo

RESULTS = []
def rep(name, ok, note=""):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name:78s} {note}")
def is0(expr):
    if isinstance(expr, sp.MatrixBase):
        return all(is0(e) for e in expr)
    expr = sp.sympify(expr)
    if expr.has(sp.Derivative, sp.Subs) or expr.atoms(sp.core.function.AppliedUndef):
        return sp.simplify(expr) == 0
    return sp.simplify(sp.expand_complex(expr)) == 0
def cm(a, b): return Q(a) + I*Q(b)
def dag(M): return M.conjugate().T

# ---------------------------------------------------------------- C1: species-space Coulomb resummation (5.1)-(5.5)
z = Matrix([-1, 2, 3])                     # charge numbers z_e = -1, Z_kappa
v = Q(7, 10)                               # v_C(q) for one q (no LFE)
A = Matrix([[cm(1, 2), cm(0, 1), cm(-1, 0)], [cm(2, -1), cm(1, 1), cm(0, 3)], [cm(1, 0), cm(-2, 1), cm(1, -1)]])
Rt = -Q(3, 10)*A*dag(A) + Q(1, 10)*I*eye(3)                 # proper response R~ (complex, generic)
Vsp = v*z*z.T
R = (eye(3) - Rt*Vsp).inv()*Rt                                # R = R~ + R~ Z^T v Z R
eps = 1 - v*(z.T*Rt*z)[0]
Rsm = Rt + v*(Rt*z)*(z.T*Rt)/eps                              # Sherman-Morrison (rank one)
rep("WP0v2-C1a Dyson == Sherman-Morrison, species basis (5.3), no LFE", is0(R - Rsm))
rep("WP0v2-C1b charge channel z.R.z == ((eps^-1) - 1)/v_C  (5.4, ELF form)", is0((z.T*R*z)[0] - (1/eps - 1)/v))
Rt2 = zeros(3, 3); Rt2[0, 0] = cm(-2, 0)/5 + I/20             # clamped nuclei: R~_ek = R~_kk = 0
R2 = (eye(3) - Rt2*Vsp).inv()*Rt2; e2 = 1 - v*Rt2[0, 0]
rep("WP0v2-C1c clamped nuclei: R_ee == (1/eps_e - 1)/v_C  (5.5)(i)", is0(R2[0, 0] - (1/e2 - 1)/v))

# ---------------------------------------------------------------- C2: local fields, arbitrary operators (5.3)
vG = sp.diag(Q(1, 2), Q(1, 5))
B = lambda s: Matrix(2, 2, [cm(*t) for t in s])
Rcc = B([(1, 1), (0, 2), (-1, 1), (2, 0)]); Rac = B([(0, 1), (1, 0), (1, -1), (0, -2)])
Rcb = B([(2, 1), (1, 1), (0, 1), (-1, 0)]); Rab = B([(1, 0), (3, 1), (0, 0), (1, 2)])
epsM = eye(2) - vG*Rcc
full = Rab + Rac*epsM.inv()*vG*Rcb
big = Matrix(sp.BlockMatrix([[Rab, Rac], [Rcb, Rcc]])); Vb = zeros(4, 4); Vb[2:, 2:] = vG
Rbig = (eye(4) - big*Vb).inv()*big
rep("WP0v2-C2  R_ab = R~_ab + R~_ac eps^-1 v_C R~_cb (LFE) == super-space Dyson (5.3)", is0(Rbig[:2, :2] - full))

# ---------------------------------------------------------------- C3: FDT and positivity (4.1), (4.4)
w, eta, beta = sp.symbols('omega eta beta', positive=True)
En = [0, Q(1, 2), Q(3, 2)]                                    # many-body levels (exact)
Zp = sum(exp(-beta*e) for e in En); p = [exp(-beta*e)/Zp for e in En]
Oa = Matrix([[cm(0, 0), cm(1, 1), cm(2, 0)], [cm(1, -1), cm(0, 1), cm(1, 0)], [cm(0, 2), cm(1, 1), cm(-1, 0)]])
Ob = Matrix([[cm(1, 0), cm(0, 1), cm(1, 1)], [cm(2, 0), cm(0, 0), cm(0, -1)], [cm(1, 0), cm(1, 2), cm(0, 1)]])
def Rret(Ad, Bm):   # R_{a b} = sum (p_i - p_f) (O_a^dag)_{if} (O_b)_{fi} / (w - (E_f - E_i) + i eta)
    return sum((p[i]-p[f])*Ad[i, f]*Bm[f, i]/(w - (En[f]-En[i]) + I*eta) for i in range(3) for f in range(3))
lhs = I*(Rret(dag(Oa), Ob) - sp.conjugate(Rret(dag(Ob), Oa)))
rhs = sum(2*pi*(p[i]-p[f])*dag(Oa)[i, f]*Ob[f, i]*(eta/pi)/((w-En[f]+En[i])**2+eta**2) for i in range(3) for f in range(3))
rep("WP0v2-C3a i(R_ab - R_ba^*) == 2pi sum (p_i - p_f) O^dag_if O_fi delta_eta  (4.1)",
    sp.simplify(sp.expand_complex(lhs - rhs).subs({w: Q(7, 10), eta: Q(1, 10), beta: Q(2)})) == 0)
# detailed-balance step on the delta support: (p_i - p_f) = p_i (1 - e^{-beta w}) at w = E_f - E_i
rep("WP0v2-C3b (p_i - p_f) == (1 - e^{-beta omega}) p_i on shell (all i,f)",
    all(sp.simplify((p[i]-p[f]) - p[i]*(1-exp(-beta*(En[f]-En[i])))) == 0 for i in range(3) for f in range(3)))
# positivity: S restricted to one transition bin is a Gram matrix
c1, c2 = sp.symbols('c1 c2')
Sbin = Matrix([[sp.conjugate(Oa[1, 0])*Oa[1, 0], sp.conjugate(Oa[1, 0])*Ob[1, 0]],
               [sp.conjugate(Ob[1, 0])*Oa[1, 0], sp.conjugate(Ob[1, 0])*Ob[1, 0]]])
rep("WP0v2-C3c S_ab Hermitian PSD (trace >= 0, det >= 0)  (4.4)",
    is0(Sbin - dag(Sbin)) and sp.simplify(Sbin.trace()) >= 0 and sp.simplify(Sbin.det()) >= 0)

# ---------------------------------------------------------------- C4: moments and commutators (4.5)-(4.8)
x, X, q, m, Mn = sp.symbols('x X q m M', positive=True)
f = sp.Function('f')(x, X); Vf = sp.Function('V')(x - X)
def Hop(g): return -sp.diff(g, x, 2)/(2*m) - sp.diff(g, X, 2)/(2*Mn) + Vf*g
ne = lambda g: exp(I*q*x)*g; neD = lambda g: exp(-I*q*x)*g
nN = lambda g: exp(I*q*X)*g; nND = lambda g: exp(-I*q*X)*g
comm = lambda A_, B_: (lambda g: A_(B_(g)) - B_(A_(g)))
rep("WP0v2-C4a [n_e^dag,[H,n_e]] == q^2/m_e  (4.6)", is0(comm(neD, comm(Hop, ne))(f) - q**2/m*f))
rep("WP0v2-C4b mixed [n_e^dag,[H,n_kappa]] == 0  (4.6c)", is0(comm(neD, comm(Hop, nN))(f)))
rep("WP0v2-C4c [n_k^dag,[H,n_k]] == q^2/M_kappa  (4.6b)", is0(comm(nND, comm(Hop, nN))(f) - q**2/Mn*f))
s_ = sp.Symbol('s')
m3 = sp.expand(comm(comm(neD, Hop), comm(Hop, comm(Hop, nN)))(f))
target = -(q**2/(m*Mn))*exp(I*q*(X - x))*sp.diff(sp.Function('V')(s_), s_, 2).subs(s_, x - X)*f
rep("WP0v2-C4d mixed 3rd moment == -(q^2/m_e M) e^{iq(X-x)} V''  (4.7)", is0(m3 - target))
# continuity (WP1-D1): [T_e, n_e(q)] = q.j_e(q) exactly, j = (1/2){p/m, e^{iqx}}, p = -i d/dx
g1 = sp.Function('g')(x)
T = lambda h: -sp.diff(h, x, 2)/(2*m); pop = lambda h: -I*sp.diff(h, x)
j = lambda h: (pop(exp(I*q*x)*h) + exp(I*q*x)*pop(h))/(2*m)
rep("WP0v2-C4e [T_e, n_e(q)] == q.j_e(q) exactly (no (q^2/2m)n term)  (4.6),(5.3)",
    is0(T(exp(I*q*x)*g1) - exp(I*q*x)*T(g1) - q*j(g1)))
rep("WP0v2-C4e' v1 form [T,n] = q.j + (q^2/2m) n is wrong (residual != 0)",
    not is0(T(exp(I*q*x)*g1) - exp(I*q*x)*T(g1) - q*j(g1) - q**2/(2*m)*exp(I*q*x)*g1))
# Ward identity for the mass density: [H, rho_M(q)] = q.g(q), two particles, interaction V(x - X)
Pop = lambda h: -I*sp.diff(h, X)
rhoM = lambda h: m*exp(I*q*x)*h + Mn*exp(I*q*X)*h
gmom = lambda h: (pop(exp(I*q*x)*h) + exp(I*q*x)*pop(h))/2 + (Pop(exp(I*q*X)*h) + exp(I*q*X)*Pop(h))/2
rep("WP0v2-C4f [H, rho_M(q)] == q.g(q) (translation Ward identity)  (4.8)", is0(comm(Hop, rhoM)(f) - q*gmom(f)))
# relativistic f-sum (WP1 [E11]): for H = F(p), [n^dag,[H,n]] = F(p+q) + F(p-q) - 2F(p)
px, py, pz, qq = sp.symbols('p_x p_y p_z q', real=True)
pv = Matrix([px, py, pz]); qv = Matrix([0, 0, qq])
Fmv = lambda P: -((P.T*P)[0])**2/(8*m**3)
dmv = sp.expand(Fmv(pv + qv) + Fmv(pv - qv) - 2*Fmv(pv))
P2 = sp.Symbol('P2', positive=True)                            # isotropic average: <p_i p_j> = delta_ij P2/3
poly = sp.Poly(dmv, px, py, pz)
def mono_avg(mon):
    if any(e % 2 for e in mon): return 0
    k = sum(mon)
    if k == 0: return 1
    if k == 2: return P2/3
    raise ValueError("degree > 2 survives")
avg_iso = sp.expand(sum(cf*mono_avg(mon) for mon, cf in poly.terms()))
Tmean = P2/(2*m)
rep("WP0v2-C4g mass-velocity: <[n^dag,[H_mv,n]]> == -(q^2/m)[(5/3)<T>/m + q^2/4m^2]  (4.6')",
    is0(avg_iso - (-(qq**2/m)*(Q(5, 3)*Tmean/m + qq**2/(4*m**2)))))
a_v = Matrix(sp.symbols('a1 a2 a3'))
Fso = lambda P: (a_v.T*P)[0]                                 # SOC / any term linear in p at fixed r
rep("WP0v2-C4h SOC (linear in p) and Darwin (multiplicative) add 0 to the f-sum  (4.6')",
    is0(sp.expand(Fso(pv + qv) + Fso(pv - qv) - 2*Fso(pv))))
ZaGe = (Q(32)/sp.Float('137.035999', 15))**2
rep("WP0v2-C4i Ge 1s (Z alpha)^2 = 0.055 (v1 quoted 0.27)  (1.2)", abs(float(ZaGe) - 0.0545) < 5e-4, f"value={float(ZaGe):.4f}")

# ---------------------------------------------------------------- C5: Hoelder bound L17 (9.6) on an exact positive measure
amps = [Q(3), Q(20), Q(5), Q(1, 2)]; ws = [Q(12), Q(17), Q(60), Q(150)]   # L = sum a_i delta(w - w_i), a_i > 0
K = lambda n: sum(a*wi**n for a, wi in zip(amps, ws))
wp2 = K(1)/(pi/2); onem = K(-1)/(pi/2)
worst = max(sp.N(K(nn) - (pi/2)*wp2**((1 + nn)/2)*onem**((1 - nn)/2), 40) for nn in [Q(k, 8) for k in range(-8, 9)])
rep("WP0v2-C5  K_n <= (pi/2) w_p^{n+1} (1 - 1/eps(q,0))^{(1-n)/2}, -1<=n<=1  (9.6)", worst <= sp.Float('1e-30'), f"max excess={sp.N(worst,5)}")

# ---------------------------------------------------------------- C6: dark-photon absorption algebra (L9b)
mm, e1, e2_ = sp.symbols('m e1 e2', positive=True); epsc = e1 + I*e2_; Pi = mm**2*(1 - epsc)
G = -sp.im(sp.simplify(mm**2*Pi/(mm**2 - Pi)))/mm
rep("WP0v2-C6  -Im[m^2 Pi/(m^2 - Pi)]/m == m Im(-1/eps)  (2.9), L9b", is0(G - mm*sp.im(-1/epsc)))

# ---------------------------------------------------------------- C7: projected pair-channel truncation (5.7') and its limits
Dl = [Q(3, 2), Q(2), Q(5, 2)]; aM = [cm(1, 1), cm(-1, 2), cm(0, 1)]; bR = [cm(1, 0), cm(2, -1), cm(1, 1)]
vv, ww, et = Q(9, 10), Q(21, 10), Q(1, 20)
gg = [1/(ww - d + I*et) for d in Dl]
RMM = sum(abs(a)**2*g for a, g in zip(aM, gg)); RMr = sum(sp.conjugate(a)*b*g for a, b, g in zip(aM, bR, gg))
RrM = sum(sp.conjugate(b)*a*g for a, b, g in zip(aM, bR, gg)); Rrr = sum(abs(b)**2*g for b, g in zip(bR, gg))
epsP = 1 - vv*Rrr
lhs7 = sp.im(sp.expand_complex(RMM + RMr*vv*RrM/epsP))
rhs7 = sum(abs(sp.expand_complex(a + b*vv*RrM/epsP))**2*sp.im(g) for a, b, g in zip(aM, bR, gg))
rep("WP0v2-C7a projected pair channel: Im[R_MM + R_Mr v R_rM/eps] == sum|M~|^2 Im g  (5.7')", is0(sp.expand_complex(lhs7 - rhs7)))
a2 = [Q(3, 10)*b for b in bR]                                  # coherent-potential limit M = U rho
RMM2 = sum(abs(a)**2*g for a, g in zip(a2, gg)); RMr2 = sum(sp.conjugate(a)*b*g for a, b, g in zip(a2, bR, gg))
RrM2 = sum(sp.conjugate(b)*a*g for a, b, g in zip(a2, bR, gg))
Mt2 = [sp.expand_complex(a + b*vv*RrM2/epsP) for a, b in zip(a2, bR)]
rep("WP0v2-C7b M = U rho  ->  M~ = M/eps(P, omega_f) per pair (X2 coherent-potential limit)",
    all(is0(sp.expand_complex(mt - a/epsP)) for mt, a in zip(Mt2, a2)))

# ---------------------------------------------------------------- C8: hyperfine contact term (1.2), WP4-D1
ge, mB, gI, mN = sp.symbols('g_e mu_B g_I mu_N', positive=True)
mu_e_per_s = -ge*mB                                            # mu_e = -g_e mu_B s ; B_contact = (2/3) mu_I delta (HL, mu_0 = 1)
coef_s = -mu_e_per_s*Q(2, 3)*gI*mN                             # H = -mu_e . B  -> coefficient of s.I delta
rep("WP0v2-C8  H_FC = +(2/3) g_e mu_B g_I mu_N s.I delta = +(1/3)(...) sigma.I delta; v1 is 2x  (1.2)",
    is0(coef_s - Q(2, 3)*ge*mB*gI*mN) and is0(coef_s/2 - Q(1, 3)*ge*mB*gI*mN) and is0((Q(2, 3)*ge*mB*gI*mN)/(coef_s/2) - 2))

# ---------------------------------------------------------------- C9: f-sum normalisation (CONVENTIONS sec. 6; WP6-W1)
ne_, e_, w0 = sp.symbols('nbar_e e omega_0', positive=True)
wp2s = e_**2*ne_/m
# T = 0, L = (pi/2) w_p^2 delta(w - w0)/w0 (saturates (9.5)); S = (2q^2/e^2) L for w > 0, 0 for w < 0
intS = (2*q**2/e_**2)*sp.integrate(w*(pi/2)*wp2s*sp.DiracDelta(w - w0)/w0, (w, 0, oo))
rep("WP0v2-C9a int_R dw w S == pi nbar_e q^2/m_e (from (9.5) and S = 2q^2 L/e^2)", is0(intS - pi*ne_*q**2/m))
rep("WP0v2-C9b same from (4.5) with S[O^dag] = S: (2/2pi) int w S = nbar q^2/m", is0(2*intS/(2*pi) - ne_*q**2/m))
rep("WP0v2-C9c v1 (8.2) normalisation 2pi nbar q^2/m is 2x too large", is0(2*pi*ne_*q**2/m/intS - 2))

# ---------------------------------------------------------------- C10: external local-field weight, pair-resolved (7.2), contested WP1-D6
vg = [Q(1), Q(1, 3)]                                           # v_C(q+G), G in {0, G1}
Vd = sp.diag(*vg)
rho = [Matrix([cm(1, 0), cm(1, 2)]), Matrix([cm(0, 1), cm(2, -1)]), Matrix([cm(1, 1), cm(-1, 0)])]  # rho_f(G), GaAs-like (complex)
gf = [cm(1, -1)/3, cm(-1, -2)/5, cm(2, -1)/7]                 # Im g_f < 0 (retarded); absorptive at (q, w)
def R0of(rh, gfl): return sum(((r.conjugate()*r.T)*g for r, g in zip(rh, gfl)), zeros(2, 2))   # R0_GG' = sum rho*_G rho_G' g
R0 = R0of(rho, gf); Rf = (eye(2) - R0*Vd).inv()*R0                 # RPA: R = R0 + R0 v R
antiH = lambda M_: (M_ - dag(M_))/(2*I)
exact = sp.simplify(antiH(Rf)[0, 0])
f1 = (eye(2) + Rf*Vd)*antiH(R0)*(eye(2) + Vd*dag(Rf)); f2 = (eye(2) + dag(Rf)*Vd)*antiH(R0)*(eye(2) + Vd*Rf)
rep("WP0v2-C10a R - R^dag = (1+Rv)(R0-R0^dag)(1+vR^dag) = (1+R^dag v)(R0-R0^dag)(1+vR)  (7.2)",
    is0(sp.simplify(f1 - antiH(Rf))) and is0(sp.simplify(f2 - antiH(Rf))))
wout = [(eye(2) + Vd*Rf)[G, 0] for G in range(2)]             # retarded (eps^-1)_{G0} = delta + v_C R_{G0} (WP0 (3.2) order)
win = [(eye(2) + Vd*dag(Rf))[G, 0] for G in range(2)]         # advanced: delta + v_C R^*_{0G}
pair = lambda wl, r: abs(sp.expand_complex(sum(wl[G]*r[G] for G in range(2))))**2
out_tot = sum(sp.im(g)*pair(wout, r) for r, g in zip(rho, gf)); in_tot = sum(sp.im(g)*pair(win, r) for r, g in zip(rho, gf))
rep("WP0v2-C10b out-state (retarded eps^-1_{G0}) pair weights sum to exact Im R_00, any target", is0(sp.simplify(out_tot - exact)))
rep("WP0v2-C10c in-state (advanced) weights also sum to Im R_00 (labelling convention)", is0(sp.simplify(in_tot - exact)))
rep("WP0v2-C10d pair-resolved out vs in differ when absorptive (difference != 0)",
    not is0(sp.simplify(sp.im(gf[0])*(pair(wout, rho[0]) - pair(win, rho[0])))))
# coincide pair by pair when R is Hermitian at (q, w) (no open pairs, e.g. the PAER window): take real g
gH = [Q(1, 3), Q(-1, 5), Q(2, 7)]; R0H = R0of(rho, gH); RH = (eye(2) - R0H*Vd).inv()*R0H
rep("WP0v2-C10e out == in pair by pair when R is Hermitian (window)",
    all(is0(sp.simplify((eye(2) + Vd*RH)[G, 0] - (eye(2) + Vd*dag(RH))[G, 0])) for G in range(2)))
w1lit = [(eye(2) + Rf*Vd)[0, G] for G in range(2)]             # WP1 [E2] as printed: (1+Rv)_{0G} rho(q+G)
lit_tot = sum(sp.im(g)*pair(w1lit, r) for r, g in zip(rho, gf))
rep("WP0v2-C10f WP1 [E2] as printed misses Im R_00 when S0 is not symmetric (flag; diff != 0)", not is0(sp.simplify(lit_tot - exact)))
rho_s = [Matrix([Q(1), Q(2)]), Matrix([Q(-1), Q(3)]), Matrix([Q(2), Q(1)])]   # real vertices: S0, R0 symmetric (TR + inversion)
R0s = R0of(rho_s, gf); Rs = (eye(2) - R0s*Vd).inv()*R0s
lit_s = sum(sp.im(g)*pair([(eye(2) + Rs*Vd)[0, G] for G in range(2)], r) for r, g in zip(rho_s, gf))
out_s = sum(sp.im(g)*pair([(eye(2) + Vd*Rs)[G, 0] for G in range(2)], r) for r, g in zip(rho_s, gf))
rep("WP0v2-C10g with TR + inversion (symmetric R0, S0) WP1 [E2] == out-state, pair by pair and in total",
    is0(sp.simplify(lit_s - sp.simplify(antiH(Rs)[0, 0]))) and is0(sp.simplify(lit_s - out_s)))

# ---------------------------------------------------------------- C11: isotropic velocity kernel (9.1)-(9.2)
vs, us, xx = sp.symbols('v u x', positive=True)
ker = sp.integrate(sp.DiracDelta(vs*xx - us)/2, (xx, -1, 1))
rep("WP0v2-C11a <delta(q^.v - u)>_q^ == Theta(v - u)/(2v)  -> G = eta(v_min)/(2q)  (9.1)",
    is0(sp.simplify(ker.subs({vs: 3, us: 1}) - Q(1, 6))) and is0(ker.subs({vs: 1, us: 3})))
rho_chi, mchi, rhoT, sig, mu, eta_, F = sp.symbols('rho_chi m_chi rho_T sigma_e mu_chie eta F', positive=True)
lhs11 = (rho_chi/(mchi*rhoT))*(pi*sig*F**2/mu**2)*q**2/(2*pi**2)*eta_/(2*q)
rhs11 = rho_chi*sig/(4*pi*mchi*rhoT*mu**2)*q*F**2*eta_
rep("WP0v2-C11b (9.2) prefactor rho_chi sigma_e/(4 pi m_chi rho_T mu^2) int q dq F^2 eta S", is0(lhs11 - rhs11))

# ---------------------------------------------------------------- C12: soft acoustic limit (4.9) = X1 (X1)
# scalar projections: QD = Q^.D^n.e^, Qv = Q^.v^g_n, ep = e^.p_nn, c = c_nu; sign s = +1 emission, -1 absorption
QDc, QDv, Qvc, Qvv, epc, epv, eq_, c = sp.symbols('QDc QDv Qvc Qvv epc epv eq c', real=True)
for sgn in (1, -1):
    lab = eq_ - epc + epv + (QDc + Qvc*epc)/(Qvc + sgn*c) - (QDv + Qvv*epv)/(Qvv + sgn*c)   # (X1'), Xi = D + v (x) p
    x1 = eq_ + (QDc - sgn*c*epc)/(Qvc + sgn*c) - (QDv - sgn*c*epv)/(Qvv + sgn*c)          # (X1)
    v1lab = eq_ + (QDc + Qvc*epc)/(Qvc + sgn*c) - (QDv + Qvv*epv)/(Qvv + sgn*c)          # v1 (4.9), Xi read as lab slope
    rep(f"WP0v2-C12a{'+' if sgn>0 else '-'} lab form (X1') == comoving form (X1), sign {'emission' if sgn>0 else 'absorption'}", is0(sp.together(lab - x1)))
    rep(f"WP0v2-C12b{'+' if sgn>0 else '-'} v1 (4.9) - X1 == e^.(p_cc - p_vv): equal only at band extrema", is0(sp.together(v1lab - x1 - (epc - epv))))
Ncell, Mc, wQ = sp.symbols('N M_cell omega_Q', positive=True)
rep("WP0v2-C12c ell_Q: v1 (N inside) == X1/D1 (N outside)/sqrt(N)", is0((2*Mc*wQ*Ncell)**Q(-1, 2) - (2*Mc*wQ)**Q(-1, 2)/sqrt(Ncell)))

# ---------------------------------------------------------------- C13: Dyson-convention lemma pieces (Theorem D (iv'), O4 (O4.4))
xv, Gm = sp.symbols('x Gamma', positive=True)
xr = sp.Symbol('xr', real=True)
fpG = sp.integrate((exp(-xr**2) - 1)/xr**2, (xr, -oo, oo))
rep("WP0v2-C13a <fp(1/x^2), e^{-x^2}> == -2 sqrt(pi) < 0 (X+ not PSD outside window)", is0(fpG + 2*sqrt(pi)))
rep("WP0v2-C13b int Gamma/(x^2 + Gamma^2/4) dx == 2 pi (delta weight to X0 under DC)",
    is0(sp.integrate(Gm/(xr**2 + Gm**2/4), (xr, -oo, oo)) - 2*pi))

# ---------------------------------------------------------------- C14: WP6 nuisance types and reporting (8.1), (8.3)
dl, cc, th, r_, S0 = sp.symbols('delta c theta r S', positive=True)
prof = 2*(1 - sqrt(1 - cc*dl**2))/(cc*dl**2)
rep("WP0v2-C14a profile: sigma_up ratio = 1 + 2.71 delta^2/4 (2.71 = chi^2_1 90% quantile, never bare c) + O(delta^4)  (O(delta^2))", is0(sp.series(prof, dl, 0, 4).removeO() - (1 + cc*dl**2/4)))
rep("WP0v2-C14b envelope: 1/(1 - delta) = 1 + delta + O(delta^2)  (O(delta))", is0(sp.series(1/(1 - dl), dl, 0, 2).removeO() - (1 + dl)))
Mtype = S0*(1 + r_)**th
rep("WP0v2-C14c M type agrees with additive S + theta Delta at first order in theta and r", is0(sp.series(sp.diff(Mtype, th).subs(th, 0), r_, 0, 2).removeO() - S0*r_))

print(f"\n{sum(RESULTS)}/{len(RESULTS)} PASS")
