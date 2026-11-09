"""WP0-v3 identity checks (R8 revision; v2 checks C1-C14 kept, C10g and C12 labels fixed, C14d-e and C15-C22 new). Sympy only, exact arithmetic; no numerics beyond evalf of exact numbers.
Run:  python3 -I checks.py      Prints PASS/FAIL per check. Labels are WP0v3-Cn (CONVENTIONS sec. 14).
Each check names the WP0-v3 equation it supports. Notation: NOTATION v4 (v_C, R, R~, eps, S, L, ...)."""
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
rep("WP0v3-C1a Dyson == Sherman-Morrison, species basis (5.3), no LFE", is0(R - Rsm))
rep("WP0v3-C1b charge channel z.R.z == ((eps^-1) - 1)/v_C  (5.4, ELF form)", is0((z.T*R*z)[0] - (1/eps - 1)/v))
Rt2 = zeros(3, 3); Rt2[0, 0] = cm(-2, 0)/5 + I/20             # clamped nuclei: R~_ek = R~_kk = 0
R2 = (eye(3) - Rt2*Vsp).inv()*Rt2; e2 = 1 - v*Rt2[0, 0]
rep("WP0v3-C1c clamped nuclei: R_ee == (1/eps_e - 1)/v_C  (5.5)(i)", is0(R2[0, 0] - (1/e2 - 1)/v))

# ---------------------------------------------------------------- C2: local fields, arbitrary operators (5.3)
vG = sp.diag(Q(1, 2), Q(1, 5))
B = lambda s: Matrix(2, 2, [cm(*t) for t in s])
Rcc = B([(1, 1), (0, 2), (-1, 1), (2, 0)]); Rac = B([(0, 1), (1, 0), (1, -1), (0, -2)])
Rcb = B([(2, 1), (1, 1), (0, 1), (-1, 0)]); Rab = B([(1, 0), (3, 1), (0, 0), (1, 2)])
epsM = eye(2) - vG*Rcc
full = Rab + Rac*epsM.inv()*vG*Rcb
big = Matrix(sp.BlockMatrix([[Rab, Rac], [Rcb, Rcc]])); Vb = zeros(4, 4); Vb[2:, 2:] = vG
Rbig = (eye(4) - big*Vb).inv()*big
rep("WP0v3-C2  R_ab = R~_ab + R~_ac eps^-1 v_C R~_cb (LFE) == super-space Dyson (5.3)", is0(Rbig[:2, :2] - full))

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
rep("WP0v3-C3a i(R_ab - R_ba^*) == 2pi sum (p_i - p_f) O^dag_if O_fi delta_eta  (4.1)",
    sp.simplify(sp.expand_complex(lhs - rhs).subs({w: Q(7, 10), eta: Q(1, 10), beta: Q(2)})) == 0)
# detailed-balance step on the delta support: (p_i - p_f) = p_i (1 - e^{-beta w}) at w = E_f - E_i
rep("WP0v3-C3b (p_i - p_f) == (1 - e^{-beta omega}) p_i on shell (all i,f)",
    all(sp.simplify((p[i]-p[f]) - p[i]*(1-exp(-beta*(En[f]-En[i])))) == 0 for i in range(3) for f in range(3)))
# positivity: S restricted to one transition bin is a Gram matrix
c1, c2 = sp.symbols('c1 c2')
Sbin = Matrix([[sp.conjugate(Oa[1, 0])*Oa[1, 0], sp.conjugate(Oa[1, 0])*Ob[1, 0]],
               [sp.conjugate(Ob[1, 0])*Oa[1, 0], sp.conjugate(Ob[1, 0])*Ob[1, 0]]])
rep("WP0v3-C3c S_ab Hermitian PSD (trace >= 0, det >= 0)  (4.4)",
    is0(Sbin - dag(Sbin)) and sp.simplify(Sbin.trace()) >= 0 and sp.simplify(Sbin.det()) >= 0)

# ---------------------------------------------------------------- C4: moments and commutators (4.5)-(4.8)
x, X, q, m, Mn = sp.symbols('x X q m M', positive=True)
f = sp.Function('f')(x, X); Vf = sp.Function('V')(x - X)
def Hop(g): return -sp.diff(g, x, 2)/(2*m) - sp.diff(g, X, 2)/(2*Mn) + Vf*g
ne = lambda g: exp(I*q*x)*g; neD = lambda g: exp(-I*q*x)*g
nN = lambda g: exp(I*q*X)*g; nND = lambda g: exp(-I*q*X)*g
comm = lambda A_, B_: (lambda g: A_(B_(g)) - B_(A_(g)))
rep("WP0v3-C4a [n_e^dag,[H,n_e]] == q^2/m_e  (4.6)", is0(comm(neD, comm(Hop, ne))(f) - q**2/m*f))
rep("WP0v3-C4b mixed [n_e^dag,[H,n_kappa]] == 0  (4.6c)", is0(comm(neD, comm(Hop, nN))(f)))
rep("WP0v3-C4c [n_k^dag,[H,n_k]] == q^2/M_kappa  (4.6b)", is0(comm(nND, comm(Hop, nN))(f) - q**2/Mn*f))
s_ = sp.Symbol('s')
m3 = sp.expand(comm(comm(neD, Hop), comm(Hop, comm(Hop, nN)))(f))
target = -(q**2/(m*Mn))*exp(I*q*(X - x))*sp.diff(sp.Function('V')(s_), s_, 2).subs(s_, x - X)*f
rep("WP0v3-C4d mixed 3rd moment == -(q^2/m_e M) e^{iq(X-x)} V''  (4.7)", is0(m3 - target))
# continuity (WP1-D1): [T_e, n_e(q)] = q.j_e(q) exactly, j = (1/2){p/m, e^{iqx}}, p = -i d/dx
g1 = sp.Function('g')(x)
T = lambda h: -sp.diff(h, x, 2)/(2*m); pop = lambda h: -I*sp.diff(h, x)
j = lambda h: (pop(exp(I*q*x)*h) + exp(I*q*x)*pop(h))/(2*m)
rep("WP0v3-C4e [T_e, n_e(q)] == q.j_e(q) exactly (no (q^2/2m)n term)  (4.6),(5.3)",
    is0(T(exp(I*q*x)*g1) - exp(I*q*x)*T(g1) - q*j(g1)))
rep("WP0v3-C4e' v1 form [T,n] = q.j + (q^2/2m) n is wrong (residual != 0)",
    not is0(T(exp(I*q*x)*g1) - exp(I*q*x)*T(g1) - q*j(g1) - q**2/(2*m)*exp(I*q*x)*g1))
# Ward identity for the mass density: [H, rho_M(q)] = q.g(q), two particles, interaction V(x - X)
Pop = lambda h: -I*sp.diff(h, X)
rhoM = lambda h: m*exp(I*q*x)*h + Mn*exp(I*q*X)*h
gmom = lambda h: (pop(exp(I*q*x)*h) + exp(I*q*x)*pop(h))/2 + (Pop(exp(I*q*X)*h) + exp(I*q*X)*Pop(h))/2
rep("WP0v3-C4f [H, rho_M(q)] == q.g(q) (translation Ward identity)  (4.8)", is0(comm(Hop, rhoM)(f) - q*gmom(f)))
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
rep("WP0v3-C4g mass-velocity: <[n^dag,[H_mv,n]]> == -(q^2/m)[(5/3)<T>/m + q^2/4m^2]  (4.6')",
    is0(avg_iso - (-(qq**2/m)*(Q(5, 3)*Tmean/m + qq**2/(4*m**2)))))
a_v = Matrix(sp.symbols('a1 a2 a3'))
Fso = lambda P: (a_v.T*P)[0]                                 # SOC / any term linear in p at fixed r
rep("WP0v3-C4h SOC (linear in p) and Darwin (multiplicative) add 0 to the f-sum  (4.6')",
    is0(sp.expand(Fso(pv + qv) + Fso(pv - qv) - 2*Fso(pv))))
ZaGe = (Q(32)/sp.Float('137.035999', 15))**2
rep("WP0v3-C4i Ge 1s (Z alpha)^2 = 0.055 (v1 quoted 0.27)  (1.2)", abs(float(ZaGe) - 0.0545) < 5e-4, f"value={float(ZaGe):.4f}")

# ---------------------------------------------------------------- C5: Hoelder bound L17 (9.6) on an exact positive measure
amps = [Q(3), Q(20), Q(5), Q(1, 2)]; ws = [Q(12), Q(17), Q(60), Q(150)]   # L = sum a_i delta(w - w_i), a_i > 0
K = lambda n: sum(a*wi**n for a, wi in zip(amps, ws))
wp2 = K(1)/(pi/2); onem = K(-1)/(pi/2)
worst = max(sp.N(K(nn) - (pi/2)*wp2**((1 + nn)/2)*onem**((1 - nn)/2), 40) for nn in [Q(k, 8) for k in range(-8, 9)])
rep("WP0v3-C5  K_n <= (pi/2) w_p^{n+1} (1 - 1/eps(q,0))^{(1-n)/2}, -1<=n<=1  (9.6)", worst <= sp.Float('1e-30'), f"max excess={sp.N(worst,5)}")

# ---------------------------------------------------------------- C6: dark-photon absorption algebra (L9b)
mm, e1, e2_ = sp.symbols('m e1 e2', positive=True); epsc = e1 + I*e2_; Pi = mm**2*(1 - epsc)
G = -sp.im(sp.simplify(mm**2*Pi/(mm**2 - Pi)))/mm
rep("WP0v3-C6  -Im[m^2 Pi/(m^2 - Pi)]/m == m Im(-1/eps)  (2.9), L9b", is0(G - mm*sp.im(-1/epsc)))

# ---------------------------------------------------------------- C7: projected pair-channel truncation (5.7') and its limits
Dl = [Q(3, 2), Q(2), Q(5, 2)]; aM = [cm(1, 1), cm(-1, 2), cm(0, 1)]; bR = [cm(1, 0), cm(2, -1), cm(1, 1)]
vv, ww, et = Q(9, 10), Q(21, 10), Q(1, 20)
gg = [1/(ww - d + I*et) for d in Dl]
RMM = sum(abs(a)**2*g for a, g in zip(aM, gg)); RMr = sum(sp.conjugate(a)*b*g for a, b, g in zip(aM, bR, gg))
RrM = sum(sp.conjugate(b)*a*g for a, b, g in zip(aM, bR, gg)); Rrr = sum(abs(b)**2*g for b, g in zip(bR, gg))
epsP = 1 - vv*Rrr
lhs7 = sp.im(sp.expand_complex(RMM + RMr*vv*RrM/epsP))
rhs7 = sum(abs(sp.expand_complex(a + b*vv*RrM/epsP))**2*sp.im(g) for a, b, g in zip(aM, bR, gg))
rep("WP0v3-C7a projected pair channel: Im[R_MM + R_Mr v R_rM/eps] == sum|M~|^2 Im g  (5.7')", is0(sp.expand_complex(lhs7 - rhs7)))
a2 = [Q(3, 10)*b for b in bR]                                  # coherent-potential limit M = U rho
RMM2 = sum(abs(a)**2*g for a, g in zip(a2, gg)); RMr2 = sum(sp.conjugate(a)*b*g for a, b, g in zip(a2, bR, gg))
RrM2 = sum(sp.conjugate(b)*a*g for a, b, g in zip(a2, bR, gg))
Mt2 = [sp.expand_complex(a + b*vv*RrM2/epsP) for a, b in zip(a2, bR)]
rep("WP0v3-C7b M = U rho  ->  M~ = M/eps(P, omega_f) per pair (X2 coherent-potential limit)",
    all(is0(sp.expand_complex(mt - a/epsP)) for mt, a in zip(Mt2, a2)))

# ---------------------------------------------------------------- C8: hyperfine contact term (1.2), WP4-D1
ge, mB, gI, mN = sp.symbols('g_e mu_B g_I mu_N', positive=True)
mu_e_per_s = -ge*mB                                            # mu_e = -g_e mu_B s ; B_contact = (2/3) mu_I delta (HL, mu_0 = 1)
coef_s = -mu_e_per_s*Q(2, 3)*gI*mN                             # H = -mu_e . B  -> coefficient of s.I delta
rep("WP0v3-C8  H_FC = +(2/3) g_e mu_B g_I mu_N s.I delta = +(1/3)(...) sigma.I delta; v1 is 2x  (1.2)",
    is0(coef_s - Q(2, 3)*ge*mB*gI*mN) and is0(coef_s/2 - Q(1, 3)*ge*mB*gI*mN) and is0((Q(2, 3)*ge*mB*gI*mN)/(coef_s/2) - 2))

# ---------------------------------------------------------------- C9: f-sum normalisation (CONVENTIONS sec. 6; WP6-W1)
ne_, e_, w0 = sp.symbols('nbar_e e omega_0', positive=True)
wp2s = e_**2*ne_/m
# T = 0, L = (pi/2) w_p^2 delta(w - w0)/w0 (saturates (9.5)); S = (2q^2/e^2) L for w > 0, 0 for w < 0
intS = (2*q**2/e_**2)*sp.integrate(w*(pi/2)*wp2s*sp.DiracDelta(w - w0)/w0, (w, 0, oo))
rep("WP0v3-C9a int_R dw w S == pi nbar_e q^2/m_e (from (9.5) and S = 2q^2 L/e^2)", is0(intS - pi*ne_*q**2/m))
rep("WP0v3-C9b same from (4.5) with S[O^dag] = S: (2/2pi) int w S = nbar q^2/m", is0(2*intS/(2*pi) - ne_*q**2/m))
rep("WP0v3-C9c v1 (8.2) normalisation 2pi nbar q^2/m is 2x too large", is0(2*pi*ne_*q**2/m/intS - 2))

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
rep("WP0v3-C10a R - R^dag = (1+Rv)(R0-R0^dag)(1+vR^dag) = (1+R^dag v)(R0-R0^dag)(1+vR)  (7.2)",
    is0(sp.simplify(f1 - antiH(Rf))) and is0(sp.simplify(f2 - antiH(Rf))))
wout = [(eye(2) + Vd*Rf)[G, 0] for G in range(2)]             # retarded (eps^-1)_{G0} = delta + v_C R_{G0} (WP0 (3.2) order)
win = [(eye(2) + Vd*dag(Rf))[G, 0] for G in range(2)]         # advanced: delta + v_C R^*_{0G}
pair = lambda wl, r: abs(sp.expand_complex(sum(wl[G]*r[G] for G in range(2))))**2
out_tot = sum(sp.im(g)*pair(wout, r) for r, g in zip(rho, gf)); in_tot = sum(sp.im(g)*pair(win, r) for r, g in zip(rho, gf))
rep("WP0v3-C10b out-state (retarded eps^-1_{G0}) pair weights sum to exact Im R_00, any target", is0(sp.simplify(out_tot - exact)))
rep("WP0v3-C10c in-state (advanced) weights also sum to Im R_00 (labelling convention)", is0(sp.simplify(in_tot - exact)))
rep("WP0v3-C10d pair-resolved out vs in differ when absorptive (difference != 0)",
    not is0(sp.simplify(sp.im(gf[0])*(pair(wout, rho[0]) - pair(win, rho[0])))))
# coincide pair by pair when R is Hermitian at (q, w) (no open pairs, e.g. the PAER window): take real g
gH = [Q(1, 3), Q(-1, 5), Q(2, 7)]; R0H = R0of(rho, gH); RH = (eye(2) - R0H*Vd).inv()*R0H
rep("WP0v3-C10e out == in pair by pair when R is Hermitian (window)",
    all(is0(sp.simplify((eye(2) + Vd*RH)[G, 0] - (eye(2) + Vd*dag(RH))[G, 0])) for G in range(2)))
w1lit = [(eye(2) + Rf*Vd)[0, G] for G in range(2)]             # WP1 [E2] as printed: (1+Rv)_{0G} rho(q+G)
lit_tot = sum(sp.im(g)*pair(w1lit, r) for r, g in zip(rho, gf))
rep("WP0v3-C10f WP1 [E2] as printed misses Im R_00 when S0 is not symmetric (flag; diff != 0)", not is0(sp.simplify(lit_tot - exact)))
rho_s = [Matrix([Q(1), Q(2)]), Matrix([Q(-1), Q(3)]), Matrix([Q(2), Q(1)])]   # real vertices: S0, R0 symmetric (TR + inversion)
R0s = R0of(rho_s, gf); Rs = (eye(2) - R0s*Vd).inv()*R0s
lit_s = sum(sp.im(g)*pair([(eye(2) + Rs*Vd)[0, G] for G in range(2)], r) for r, g in zip(rho_s, gf))
out_s = sum(sp.im(g)*pair([(eye(2) + Vd*Rs)[G, 0] for G in range(2)], r) for r, g in zip(rho_s, gf))
# R7 REF-WP0-B V11: v2's label claimed "pair by pair" but only totals were compared. Now tested pair by pair.
wl_s = [(eye(2) + Rs*Vd)[0, G] for G in range(2)]; wo_s = [(eye(2) + Vd*Rs)[G, 0] for G in range(2)]
rep("WP0v3-C10g with TR + inversion (symmetric R0, S0) WP1 [E2] == out-state, pair by pair AND in total (label fixed)",
    is0(sp.simplify(lit_s - sp.simplify(antiH(Rs)[0, 0]))) and is0(sp.simplify(lit_s - out_s))
    and all(is0(sp.simplify(pair(wl_s, r) - pair(wo_s, r))) for r in rho_s))

# ---------------------------------------------------------------- C11: isotropic velocity kernel (9.1)-(9.2)
vs, us, xx = sp.symbols('v u x', positive=True)
ker = sp.integrate(sp.DiracDelta(vs*xx - us)/2, (xx, -1, 1))
rep("WP0v3-C11a <delta(q^.v - u)>_q^ == Theta(v - u)/(2v)  -> G = eta(v_min)/(2q)  (9.1)",
    is0(sp.simplify(ker.subs({vs: 3, us: 1}) - Q(1, 6))) and is0(ker.subs({vs: 1, us: 3})))
rho_chi, mchi, rhoT, sig, mu, eta_, F = sp.symbols('rho_chi m_chi rho_T sigma_e mu_chie eta F', positive=True)
lhs11 = (rho_chi/(mchi*rhoT))*(pi*sig*F**2/mu**2)*q**2/(2*pi**2)*eta_/(2*q)
rhs11 = rho_chi*sig/(4*pi*mchi*rhoT*mu**2)*q*F**2*eta_
rep("WP0v3-C11b (9.2) prefactor rho_chi sigma_e/(4 pi m_chi rho_T mu^2) int q dq F^2 eta S", is0(lhs11 - rhs11))

# ---------------------------------------------------------------- C12: soft acoustic limit (4.9) = X1 (X1)
# scalar projections: QD = Q^.D^n.e^, Qv = Q^.v^g_n, ep = e^.p_nn, c = c_nu; sign s = +1 emission, -1 absorption
QDc, QDv, Qvc, Qvv, epc, epv, eq_, c = sp.symbols('QDc QDv Qvc Qvv epc epv eq c', real=True)
for sgn in (1, -1):
    lab = eq_ - epc + epv + (QDc + Qvc*epc)/(Qvc + sgn*c) - (QDv + Qvv*epv)/(Qvv + sgn*c)   # (X1'), Xi = D + v (x) p
    x1 = eq_ + (QDc - sgn*c*epc)/(Qvc + sgn*c) - (QDv - sgn*c*epv)/(Qvv + sgn*c)          # (X1)
    v1lab = eq_ + (QDc + Qvc*epc)/(Qvc + sgn*c) - (QDv + Qvv*epv)/(Qvv + sgn*c)          # v1 (4.9), Xi read as lab slope
    rep(f"WP0v3-C12a{'+' if sgn>0 else '-'} [algebra only; content D in X1] lab form (X1') == comoving form (X1), sign {'emission' if sgn>0 else 'absorption'}", is0(sp.together(lab - x1)))
    rep(f"WP0v3-C12b{'+' if sgn>0 else '-'} v1 (4.9) - X1 == e^.(p_cc - p_vv): equal only at band extrema", is0(sp.together(v1lab - x1 - (epc - epv))))
Ncell, Mc, wQ = sp.symbols('N M_cell omega_Q', positive=True)
rep("WP0v3-C12c ell_Q: v1 (N inside) == X1/D1 (N outside)/sqrt(N)", is0((2*Mc*wQ*Ncell)**Q(-1, 2) - (2*Mc*wQ)**Q(-1, 2)/sqrt(Ncell)))

# ---------------------------------------------------------------- C13: Dyson-convention lemma pieces (Theorem D (iv'), O4 (O4.4))
xv, Gm = sp.symbols('x Gamma', positive=True)
xr = sp.Symbol('xr', real=True)
fpG = sp.integrate((exp(-xr**2) - 1)/xr**2, (xr, -oo, oo))
rep("WP0v3-C13a <fp(1/x^2), e^{-x^2}> == -2 sqrt(pi) < 0 (X+ not PSD outside window)", is0(fpG + 2*sqrt(pi)))
rep("WP0v3-C13b int Gamma/(x^2 + Gamma^2/4) dx == 2 pi (delta weight to X0 under DC)",
    is0(sp.integrate(Gm/(xr**2 + Gm**2/4), (xr, -oo, oo)) - 2*pi))

# ---------------------------------------------------------------- C14: WP6 nuisance types and reporting (8.1), (8.3)
dl, cc, th, r_, S0 = sp.symbols('delta c theta r S', positive=True)
prof = 2*(1 - sqrt(1 - cc*dl**2))/(cc*dl**2)
rep("WP0v3-C14a profile: sigma_up ratio = 1 + 2.71 delta^2/4 (2.71 = chi^2_1 90% quantile, never bare c) + O(delta^4)  (O(delta^2))", is0(sp.series(prof, dl, 0, 4).removeO() - (1 + cc*dl**2/4)))
rep("WP0v3-C14b envelope: 1/(1 - delta) = 1 + delta + O(delta^2)  (O(delta))", is0(sp.series(1/(1 - dl), dl, 0, 2).removeO() - (1 + dl)))
Mtype = S0*(1 + r_)**th
rep("WP0v3-C14c M type agrees with additive S + theta Delta at first order in theta and r", is0(sp.series(sp.diff(Mtype, th).subs(th, 0), r_, 0, 2).removeO() - S0*r_))


# C14 continued (R7: REF-WP6-A F, REF-WP6-B F6): like-for-like profile vs envelope at delta = 1/2; the v2 "x1.8" mixed types
d5 = Q(1, 2); c90 = Q(271, 100)
lin_prof = 2*(1 - sqrt(1 - c90*d5**2))/(c90*d5**2)                       # linear nuisance, profiled
kd = sp.log(1 + d5); Wl = sqrt(1 + c90*kd**2) - 1                       # log-normal (M type), explicit root of w^2 + 2w - 2.71k^2 = 0
ln_prof = 2*Wl*exp(Wl)/(c90*kd**2)
rM, rL, rMix = (1 + d5)/ln_prof, (1/(1 - d5))/lin_prof, (1/(1 - d5))/ln_prof
rep("WP0v3-C14d like-for-like envelope/profile at delta=0.5: M type 1.35, linear 1.57; v2's x1.8 = linear/log-normal (mixed)",
    abs(float(rM) - 1.35) < 5e-3 and abs(float(rL) - 1.57) < 5e-3 and abs(float(rMix) - 1.80) < 5e-3
    and is0(sp.expand(Wl**2 + 2*Wl - c90*kd**2)),
    f"M={float(rM):.3f} lin={float(rL):.3f} mixed={float(rMix):.3f}")
rep("WP0v3-C14e linear profile has no solution for delta > 2.71^(-1/2) = 0.607", abs(float(1/sqrt(c90)) - 0.6075) < 1e-3)

# ---------------------------------------------------------------- C15: rate index order (3.3)-(3.4), (7.3) (REF-WP0-A V2)
# finite-level target, two operators, DM amplitudes V_a: golden-rule sum |<f| sum_a V_a O_a |i>|^2 == sum_ab D_ab S_ab, D_ab = V_a^* V_b
Va = [cm(1, 2), cm(-1, 1)]
OA = [Matrix([[0, cm(1, 1), cm(0, 2)], [cm(2, 0), 0, cm(1, -1)], [cm(0, 1), cm(1, 0), 0]]),
      Matrix([[0, cm(0, 1), cm(1, 0)], [cm(1, 1), 0, cm(2, 1)], [cm(-1, 0), cm(0, -2), 0]])]
pi_ = [Q(1, 2), Q(1, 3), Q(1, 6)]                                        # any stationary (diagonal) state
gold = sum(pi_[i]*abs(sp.expand_complex(sum(Va[a]*OA[a][f, i] for a in range(2))))**2 for i in range(3) for f in range(3))
Dm = Matrix(2, 2, lambda a, b: sp.conjugate(Va[a])*Va[b])
Sm = Matrix(2, 2, lambda a, b: sum(pi_[i]*sp.conjugate(OA[a][f, i])*OA[b][f, i] for i in range(3) for f in range(3)))
sumab = sum(Dm[a, b]*Sm[a, b] for a in range(2) for b in range(2))
rep("WP0v3-C15a golden rule == sum_ab D_ab S_ab == tr[D^T S]  (3.3)", is0(sp.expand_complex(gold - sumab)) and is0(sp.expand_complex(sumab - (Dm.T*Sm).trace())))
rep("WP0v3-C15b tr[D S] != tr[D^T S] when Im D and Im S are both nonzero (v2 (3.4),(7.3) index order wrong)",
    not is0(sp.expand_complex((Dm*Sm).trace() - (Dm.T*Sm).trace())))
Dh = Matrix([[2, cm(1, 1)], [cm(1, -1), 3]]); Sh = Matrix([[2, cm(1, 2)], [cm(1, -2), 4]])   # REF-A S4-type example
rep("WP0v3-C15c tr[D S] - tr[D^T S] == -2 tr[D_I S_I] (antisymmetric imaginary parts)",
    is0(sp.expand_complex((Dh*Sh).trace() - (Dh.T*Sh).trace() + 2*(Dh.applyfunc(sp.im)*Sh.applyfunc(sp.im)).trace())))

# ---------------------------------------------------------------- C16: moment normalisation (4.5), (4.7) (REF-WP0-B V4, REF-WP0-A V7)
Hl = [0, Q(1), Q(5, 2), Q(4)]; pr = [Q(4, 10), Q(3, 10), Q(2, 10), Q(1, 10)]   # stationary diagonal state, nondegenerate levels
Hm = sp.diag(*Hl)
Pa = Matrix(4, 4, lambda i, j: cm((i + 2*j) % 3 - 1, (2*i + j) % 4 - 1))
Pb = Matrix(4, 4, lambda i, j: cm((3*i + j) % 4 - 2, (i*j) % 3 - 1))
ex = lambda X: sum(pr[i]*X[i, i] for i in range(4))
Cm = lambda A_, B_: A_*B_ - B_*A_
def mom(k, A_, B_):  # int (dw/2pi) w^k S_AB[O] with V = 1: sum p_i (A^dag)_{if} B_{fi} w_fi^k
    return sum(pr[i]*dag(A_)[i, f]*B_[f, i]*(Hl[f] - Hl[i])**k for i in range(4) for f in range(4))
def momD(k, A_, B_):  # same with both operators daggered: S_AB[O^dag] means O_A -> O_A^dag, O_B -> O_B^dag
    return mom(k, dag(A_), dag(B_))
M1c = ex(Cm(dag(Pa), Cm(Hm, Pb)))
rep("WP0v3-C16a (4.5) corrected: <[Oa^dag,[H,Ob]]> == int w (S_ab[O] + S_ba[O^dag])", is0(sp.expand_complex(M1c - mom(1, Pa, Pb) - momD(1, Pb, Pa))))
rep("WP0v3-C16b v2 (4.5) as written (S_ab[O] + S_ab[O^dag]) fails off-diagonal", not is0(sp.expand_complex(M1c - mom(1, Pa, Pb) - momD(1, Pa, Pb))))
rep("WP0v3-C16c ... and holds on the diagonal (a = b)", is0(sp.expand_complex(ex(Cm(dag(Pa), Cm(Hm, Pa))) - mom(1, Pa, Pa) - momD(1, Pa, Pa))))
M3c = ex(Cm(Cm(dag(Pa), Hm), Cm(Hm, Cm(Hm, Pb))))
rep("WP0v3-C16d (4.7) normalisation: <[[Oa^dag,H],[H,[H,Ob]]]> == int w^3 (S_ab[O] + S_ba[O^dag])", is0(sp.expand_complex(M3c - mom(3, Pa, Pb) - momD(3, Pb, Pa))))

# ---------------------------------------------------------------- C17: R^infinity and the gauge identity (4.2) (REF-WP0-A V5, REF-WP0-B V3a)
qg = Q(3, 2)
Nn = Matrix(4, 4, lambda i, j: 0 if i == j else cm((i + j) % 3, (i - j) % 2))          # density, no diagonal (q != 0)
JL = Matrix(4, 4, lambda f, i: (Hl[f] - Hl[i])*Nn[f, i]/qg)                              # <f|q.j|i> = w_fi <f|n|i>  (4.6)
def Rlehm(A_, B_, z):
    return sum((pr[i] - pr[f])*dag(A_)[i, f]*B_[f, i]/(z - (Hl[f] - Hl[i])) for i in range(4) for f in range(4) if f != i)
zz = sp.Symbol('z')
rep("WP0v3-C17a Lehmann R_{jL jL}(w) -> 0 as w -> oo: R^inf = 0 for currents too", sp.limit(Rlehm(JL, JL, zz), zz, oo) == 0)
M1n = ex(Cm(dag(Nn), Cm(Hm, Nn)))
rep("WP0v3-C17b R_{jL jL}(q,0) == -M1/q^2 (spectral R alone; physical kernel R + n/m vanishes)", is0(sp.expand_complex(Rlehm(JL, JL, 0) + M1n/qg**2)))

# ---------------------------------------------------------------- C18: Breit orbit-orbit term in the f-sum (1.2), (4.6') (REF-WP0-A V4)
x1, x2 = sp.symbols('x1 x2', real=True)
ff = sp.Function('f')(x1, x2); Kf = sp.Function('K')(x1 - x2)
p1 = lambda h: -I*sp.diff(h, x1); p2 = lambda h: -I*sp.diff(h, x2)
Hoo = lambda h: (p1(Kf*p2(h)) + p2(Kf*p1(h)))/2                                          # Hermitian p1 K(r12) p2
n12 = lambda h: (exp(I*q*x1) + exp(I*q*x2))*h; n12D = lambda h: (exp(-I*q*x1) + exp(-I*q*x2))*h
dc = comm(n12D, comm(Hoo, n12))(ff)
rep("WP0v3-C18a [n^dag,[p1 K p2,n]] == 2 q^2 K(r12) cos(q r12) (multiplicative)",
    sp.simplify(sp.expand(sp.simplify(dc - 2*q**2*Kf*sp.cos(q*(x1 - x2))*ff)).rewrite(sp.exp)) == 0)
th_ = sp.Symbol('theta')
rep("WP0v3-C18b angular average <1 + (q^.r^)^2> = 4/3", is0(sp.integrate((1 + sp.cos(th_)**2)*sp.sin(th_), (th_, 0, pi))/2 - Q(4, 3)))
kk, mu_r = sp.symbols('k mu', positive=True); cc_ = sp.Symbol('cc', real=True)
xr_ = sp.Symbol('xr', positive=True)
ang = sp.simplify(sp.integrate(2*pi*cc_**2*sp.cos(xr_*cc_), (cc_, -1, 1)))               # odd (sine) part integrates to 0
# FT[(k^.r^)^2/r](k) = k^-2 int_0^oo x ang(x) dx (Abel-regularised): x ang = 4pi[sin x + (2x cos x - 2 sin x)/x^2]
rep("WP0v3-C18c0 angular integral: x*ang(x) == 4pi[sin x + (2x cos x - 2 sin x)/x^2]",
    is0(sp.simplify(xr_*ang - 4*pi*(sp.sin(xr_) + (2*xr_*sp.cos(xr_) - 2*sp.sin(xr_))/xr_**2))))
abel = sp.limit(sp.integrate(sp.sin(xr_)*exp(-mu_r*xr_), (xr_, 0, oo)), mu_r, 0)
rest = sp.integrate((2*xr_*sp.cos(xr_) - 2*sp.sin(xr_))/xr_**2, (xr_, 0, oo))
ft_rr = 4*pi*(abel + rest)/kk**2
rep("WP0v3-C18c FT[(1 + r^r^)/r] is transverse: q^.FT.q^ = 4pi/q^2 + FT[(q^.r^)^2/r] = 0 (uniform Hartree part of H_oo gives 0)",
    is0(sp.simplify(4*pi/kk**2 + ft_rr)), f"FT[(k.r)^2/r]={sp.simplify(ft_rr)}")
Tk = sp.Symbol('T', positive=True)
dmv_ = -Q(5, 3)*Tk/m; doo_ = -Q(4, 3)*(Tk/3)/m                                           # Thomas-Fermi E_ee/N_e = <T>/3
rep("WP0v3-C18d delta_oo/delta_mv = 4/15 = 0.27 (Thomas-Fermi E_ee = T/3) [E]", is0(doo_/dmv_ - Q(4, 15)))

# ---------------------------------------------------------------- C19: (4.7) q -> 0 limit; REF-A vs REF-B order of limits
qx, qy, qz = sp.symbols('q_x q_y q_z', real=True); qv3 = Matrix([qx, qy, qz]); q2 = qx**2 + qy**2 + qz**2
summand = lambda Gv: ((qv3.T*(qv3 - Gv))[0])**2/((qv3 - Gv).T*(qv3 - Gv))[0]           # (q.(q-G))^2/|q-G|^2
rep("WP0v3-C19a G = 0 term of -Ze^2 sum_G n_G (q.(q-G))^2/|q-G|^2 is exactly -Ze^2 nbar_e q^2 at every q (non-analytic, survives q->0)",
    is0(sp.simplify(summand(Matrix([0, 0, 0])) - q2)))
import itertools
stars = {'100': [Matrix(v) for v in set(itertools.permutations([1, 0, 0])) | set(itertools.permutations([-1, 0, 0]))],
         '111': [Matrix([a, b, c]) for a in (1, -1) for b in (1, -1) for c in (1, -1)],
         '110': [Matrix(v) for v in {p for s1 in (1, -1) for s2 in (1, -1) for p in itertools.permutations([s1, s2, 0])}]}
eps_ = sp.Symbol('epsilon', positive=True)
ok = True
for nm, st in stars.items():
    lead = sum(sp.series(summand(G).subs({qx: eps_*qx, qy: eps_*qy, qz: eps_*qz}), eps_, 0, 3).removeO() for G in st)
    ok &= is0(sp.expand(lead - eps_**2*len(st)*q2/3))
rep("WP0v3-C19b cubic stars <100>,<110>,<111>: sum_star (q.G)^2/G^2 = |star| q^2/3 at O(q^2)", ok)
yv, xv_ = sp.symbols('y x', positive=True)
cc2 = sp.Symbol('c2', real=True)
angP2 = sp.simplify(sp.integrate(exp(-I*xv_*cc2)*sp.legendre(2, cc2), (cc2, -1, 1)))
j2 = (3/xv_**3 - 1/xv_)*sp.sin(xv_) - 3*sp.cos(xv_)/xv_**2
rep("WP0v3-C19c int_{-1}^{1} e^{-ixc} P2(c) dc == -2 j2(x)", is0(sp.simplify(sp.expand_complex(angP2 + 2*j2))))
Ij2 = sp.integrate(j2/xv_, (xv_, 0, oo))
rep("WP0v3-C19d int_0^oo j2(x)/x dx == 1/3", is0(sp.simplify(Ij2 - Q(1, 3))), f"value={Ij2}")
Zs, alp, nb, nR = sp.symbols('Z alpha nbar n_R', positive=True)
e2 = 4*pi*alp
# uniform part: (q.grad)^2 (Z alpha/y) = Z alpha q^2 2 P2/y^3 - (q^2/3) Z e^2 delta^3 ; traceless piece integrated with nbar e^{-iq.y}
unif_traceless = 2*Zs*alp*q**2*nb*2*pi*(-2)*Ij2                                          # int y^2 dy/y^3 * angular, x = q y
rep("WP0v3-C19e uniform background, traceless (l=2) part: -(2/3) q^2 Z e^2 nbar  (thermodynamic limit first)",
    is0(sp.simplify(unif_traceless + Q(2, 3)*q**2*Zs*e2*nb)))
total_A = -Zs*e2*(nb*q**2 + q**2*(nR - nb)/3)                                             # G=0 exact + G!=0 star average
rep("WP0v3-C19f sum: M3 kernel -> -(q^2/3) Z e^2 [n_e(R) + 2 nbar_e]  (REF-A form)", is0(sp.expand(total_A + q**2*Zs*e2*(nR + 2*nb)/3)))
rep("WP0v3-C19g ... = contact (-(q^2/3)Ze^2 n_e(R)) + uniform traceless (C19e): decomposition consistent",
    is0(sp.expand(total_A - (-(q**2/3)*Zs*e2*nR + unif_traceless.subs(Ij2, Q(1, 3))))))
# independent route: RPA two-plasma high-frequency expansion; RPA has an uncorrelated pair density, n_e(R) -> nbar_e
wv = sp.Symbol('w', positive=True); ne0, nk0 = sp.symbols('n_e n_k', positive=True)
Rt_sp = sp.diag(ne0*q**2/(m*wv**2), nk0*q**2/(Mn*wv**2)); zsp = Matrix([-1, Zs]); vq = e2/q**2
R_sp = (eye(2) - Rt_sp*zsp*zsp.T*vq).inv()*Rt_sp
c4 = sp.limit(sp.simplify(R_sp[0, 1]*wv**4), wv, oo)
rep("WP0v3-C19h RPA: w^-4 coefficient of R_ek = -Z e^2 n_e n_k q^2/(m M) == REF-A form at n_e(R) = nbar_e; REF-B form is 3x smaller",
    is0(sp.simplify(c4 + Zs*e2*ne0*nk0*q**2/(m*Mn))) and is0(sp.simplify(c4/(-q**2*Zs*e2*nk0*(ne0 + 2*ne0)/(3*m*Mn)) - 1))
    and not is0(sp.simplify(c4 - (-q**2*Zs*e2*nk0*ne0/(3*m*Mn)))))
rep("WP0v3-C19i opposite order (q -> 0 first, spherical sample): angular int of P2 = 0, traceless uniform part vanishes (REF-B form)",
    is0(sp.integrate(sp.legendre(2, cc2), (cc2, -1, 1))))
# next order: O(q^3) term is odd in G; cancels at centrosymmetric sites, survives at T_d sites as i q_x q_y q_z
o3 = lambda G: sp.series(summand(G).subs({qx: eps_*qx, qy: eps_*qy, qz: eps_*qz}), eps_, 0, 4).removeO().coeff(eps_, 3)
etaG = lambda G: G[0]*G[1]*G[2]                                                          # T_d sign pattern on <111> (Im n_G odd)
cen = sp.expand(sum(o3(G) for G in stars['111'])); td = sp.expand(sum(etaG(G)*o3(G) for G in stars['111']))
rep("WP0v3-C19j O(q^3): zero for an inversion-symmetric star; at a T_d site prop. to q_x q_y q_z (nonzero)",
    is0(cen) and is0(sp.simplify(td/(qx*qy*qz)).diff(qx)) and not is0(td), f"T_d term={sp.factor(td)}")

# R9 (VER-WP0-B N1): a star with |G| << q acts like G = 0 (weight 1, not 1/3): (4.7'')
Gs = sp.Symbol('G_s', positive=True)
far = sp.limit(summand(Matrix([0, 0, Gs])).subs({qx: 0, qy: 0}) / qz**2, Gs, 0)
rep("WP0v3-C19k (4.7''): for |G| << q the star term (q.(q-G))^2/(q^2|q-G|^2) -> 1 (G=0-like); range of (4.7') is q << G_min", is0(far - 1))

# ---------------------------------------------------------------- C20: L17 (iii) electron channel with relaxed lattice (REF-A V18, REF-B V15)
av, bv = sp.symbols('a b', positive=True)
v0 = sp.Symbol('v', positive=True); Re_, Rk_ = -av/v0, -bv/(v0*Zs**2)                     # a = -v R~_e, b = -v Z^2 R~_k (static, two-fluid)
Rt0 = sp.diag(Re_, Rk_); R0f = (eye(2) - Rt0*zsp*zsp.T*v0).inv()*Rt0
epse_inv = sp.simplify(1 + v0*R0f[0, 0]); epsc_inv = sp.simplify(1 + v0*(zsp.T*R0f*zsp)[0])
rep("WP0v3-C20a two-fluid: eps_e^-1(0) = (1 + b - a b)/(1 + a + b), eps_c^-1 = 1/(1 + a + b)",
    is0(sp.simplify(epse_inv - (1 + bv - av*bv)/(1 + av + bv))) and is0(sp.simplify(epsc_inv - 1/(1 + av + bv))))
rep("WP0v3-C20b 1 - eps_e^-1 = a(1+b)/(1+a+b) > 1 iff a b > 1 + b", is0(sp.simplify(1 - epse_inv - av*(1 + bv)/(1 + av + bv)))
    and is0(sp.simplify((1 - epse_inv - 1)*(1 + av + bv) - (av*bv - 1 - bv))))
gaas = (1 - epse_inv).subs({av: Q(99, 10), bv: 2}); si_ = (1 - epse_inv).subs({av: Q(107, 10), bv: Q(1, 2)})
# R9 (VER-WP0-A N2): the Si figure (10.7, 0.5) -> 1.32 is dropped (R~_ek = 0 model does not describe non-polar Si)
rep("WP0v3-C20c GaAs-like (a=9.9,b=2): eps_e^-1 = -1.30, 1-eps_e^-1 = 2.30 (Si figure dropped, R9)",
    abs(float(epse_inv.subs({av: Q(99, 10), bv: 2})) + 1.30) < 5e-3 and abs(float(gaas) - 2.30) < 5e-3)
rep("WP0v3-C20d (ii) relaxed eps_e(0) = eps_0/(1 + b - ab) with eps_0 = 1+a+b: neither eps_inf nor eps_0",
    is0(sp.simplify(1/epse_inv - (1 + av + bv)/(1 + bv - av*bv))))

# ---------------------------------------------------------------- C21: J-row transversality needs [H, s_i] = 0 (REF-WP0-B V1)
sx = Matrix([[0, 1], [1, 0]])/2; sy = Matrix([[0, -I], [I, 0]])/2; sz = Matrix([[1, 0], [0, -1]])/2
Bz = sp.Symbol('B_z', positive=True)
rep("WP0v3-C21 Zeeman (or contact s.I, or SOC) term does not commute with s^x: q_a J^{ab} != [H, s^b(q)] unless SU(2)",
    not is0(Cm(Bz*sz, sx)) and is0(Cm(sx*sx + sy*sy + sz*sz, sx)))

# ---------------------------------------------------------------- C22: nonreciprocity order of S_ee (4.3) (REF-WP0-B V3b)
d1, d2, Q1, Q2 = sp.symbols('d1 d2 Q1 Q2')                                                # complex dipole and quadrupole matrix elements
qs = sp.Symbol('q', real=True)
rho_p = I*qs*d1 - qs**2*Q1/2; rho_m = -I*qs*d1 - qs**2*Q1/2                              # <f|e^{+-iq.r}|i>, f != i, to O(q^2)
diffNR = sp.expand(rho_p*sp.conjugate(rho_p) - rho_m*sp.conjugate(rho_m))
rep("WP0v3-C22 |n_fi(q)|^2 - |n_fi(-q)|^2 starts at O(q^3) for densities (no O(q) term)",
    is0(diffNR.coeff(qs, 1)) and is0(diffNR.coeff(qs, 2)) and not is0(diffNR.coeff(qs, 3)))

# ---------------------------------------------------------------- C23: nuisance types (8.1)-(8.2) = WP6-v3 (5.1)-(5.3) (AUDIT-2 B1)
S0m = Matrix([[1, Q(1, 10)], [Q(1, 10), 1]]); S1m = Matrix([[1, Q(9, 10)], [Q(9, 10), 1]])     # both PSD
elem = Matrix(2, 2, lambda a, b: S0m[a, b]*(S1m[a, b]/S0m[a, b])**2)                                # elementwise M at theta = 2
def psd2(M_): return sp.simplify(M_[0, 0]) >= 0 and sp.simplify(M_.det()) >= 0
U2 = Matrix([[1, 1], [1, -1]])/sqrt(2)                                                  # common eigenbasis (both matrices commute here)
d0 = [S0m[0, 0] + S0m[0, 1], S0m[0, 0] - S0m[0, 1]]; S0h = U2*sp.diag(*[sqrt(d) for d in d0])*U2.T; S0mh = S0h.inv()
Cg = sp.simplify(S0mh*S1m*S0mh); dc = [sp.simplify((U2.T*Cg*U2)[i, i]) for i in range(2)]
geo = lambda t: sp.simplify(S0h*(U2*sp.diag(*[d**t for d in dc])*U2.T)*S0h)
rep("WP0v3-C23a elementwise M on S_ab leaves the PSD cone at theta=2; PSD geodesic (commuting example) is PSD at theta=2 and hits S^tau, S^tau+e at 0, 1",
    psd2(S0m) and psd2(S1m) and not psd2(elem) and psd2(geo(2))
    and is0(sp.simplify(geo(0) - S0m)) and is0(sp.simplify(geo(1) - S1m)))
Dpsd = Matrix([[1, 0], [0, 0]]); Dnon = Matrix([[0, 1], [1, 0]]); aa = sp.Symbol('a', positive=True)
rep("WP0v3-C23b type A: S + a Delta PSD for all a>0 iff Delta PSD (counterexample with indefinite Delta)",
    is0(sp.simplify((S0m + aa*Dpsd).det() - (S0m.det() + aa*S0m[1, 1]))) and sp.simplify((S0m + 5*Dnon).det()) < 0)
lo, hi = Q(4, 10), Q(18, 10)
rep("WP0v3-C23c PAER interim [0.4, 1.8] log-symmetric: median 0.85, sigma_ln 0.75 (68%)",
    abs(float(sqrt(lo*hi)) - 0.85) < 5e-3 and abs(float(sp.log(hi/lo)/2) - 0.75) < 5e-3)

# ---------------------------------------------------------------- C24: L17 beyond RPA, WP1-v3 (1.4') (AUDIT-2 B2)
# proper R~ = (1 - R0 f)^-1 R0 is negative definite iff (-R0)^-1 + f_xc > 0 (R0 NSD invertible, f real symmetric)
R0x = -Matrix([[2, Q(1, 2)], [Q(1, 2), 1]]); fx = lambda t: Matrix([[t, 0], [0, t]])
Rt_of = lambda t: (eye(2) - R0x*fx(t)).inv()*R0x
def negdef(M_): Ms = (M_ + M_.T)/2; return sp.simplify(Ms[0, 0]) < 0 and sp.simplify(Ms.det()) > 0
def cond(t): C_ = (-R0x).inv() + fx(t); return sp.simplify(C_[0, 0]) > 0 and sp.simplify(C_.det()) > 0
rep("WP0v3-C24 (1.4'): R~ NSD <=> (-R0)^-1 + f_xc > 0 (tested on both sides of the instability)",
    all(negdef(Rt_of(t)) == cond(t) for t in [Q(-1, 10), Q(-1, 2), Q(-3, 4)]) and cond(Q(-1, 10)) and not cond(Q(-3, 4)))

# ---------------------------------------------------------------- C25: Migdal/multiphonon first-moment bookkeeping (AUDIT-2 B3)
Pm_s, dM, qq_ = sp.symbols('P_Mig deltaM q', positive=True)
E1 = qq_**2*dM/(2*Mn**2)
gs = (1 - Pm_s)*qq_**2/(2*(Mn + dM)); xs = E1 + Pm_s*qq_**2/(2*Mn)
tot = sp.series((gs + xs).subs({dM: eps_*dM, Pm_s: eps_*Pm_s}), eps_, 0, 2).removeO()
rep("WP0v3-C25 (1-P_Mig) S^GS with M+dM plus X moment (E1 + P_Mig q^2/2M) = q^2/2M through first order (WP5-v3 3.1)",
    is0(sp.expand(tot - qq_**2/(2*Mn))))

print(f"\n{sum(RESULTS)}/{len(RESULTS)} PASS")
