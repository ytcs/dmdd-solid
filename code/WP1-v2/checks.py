"""WP1-v2 identity and number checks (R6 revision of returns/R5/WP1.md). Sympy only, exact arithmetic;
numbers are evalf of closed forms (no simulation, no numpy/scipy). Run:  python3 -I checks.py
Labels WP1v2-Cn (CONVENTIONS sec. 14). Notation: NOTATION v4 (v_C, R, R~, R0, eps, S, L, rho_cv, ...)."""
import sympy as sp
from sympy import I, Rational as Q, Matrix, eye, sqrt, pi, exp, cos, sin, symbols, simplify, zeta

RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:84s} {note}")
def is0(e):
    if isinstance(e, sp.MatrixBase): return all(is0(x) for x in e)
    return sp.simplify(sp.expand_complex(sp.sympify(e))) == 0
def dag(M): return M.conjugate().T
def cm(a, b): return Q(a) + I*Q(b)

# ------------------------------------------------ C1: continuity [T_e, n_e(q)] = q.j_e(q) exactly  (§2.1, WP0-v2 (4.6))
x, q, m = symbols('x q m', positive=True)
f = sp.Function('f')(x)
p_ = lambda g: -I*sp.diff(g, x)
n_ = lambda g: exp(I*q*x)*g
T_ = lambda g: p_(p_(g))/(2*m)
j_ = lambda g: (p_(n_(g)) + n_(p_(g)))/(2*m)
rep("WP1v2-C1a [T_e, n_e(q)] = q.j_e(q), j_e = 1/2{p/m_e, e^{iqx}} (no (q^2/2m)n term)", is0(T_(n_(f)) - n_(T_(f)) - q*j_(f)))
fvec = lambda g: n_(I*sp.diff(g, x))/m                       # 2105.02233 Eq. (11) vector overlap
rep("WP1v2-C1b q.f_vec = -(q.j_e - (q^2/2m_e) n_e)  =>  W2-bar, W4-bar fixed by W1-bar (L3 (a))",
    is0(q*fvec(f) + q*j_(f) - q**2/(2*m)*n_(f)))

# ------------------------------------------------ C2: relativistic f-sum [E11]: only mass-velocity contributes
px, py, pz, qx, qy, qz, a1, a2, a3 = symbols('px py pz qx qy qz a1 a2 a3', real=True)
P = Matrix([px, py, pz]); Qv = Matrix([qx, qy, qz]); p2 = lambda v: (v.T*v)[0]
dd = sp.expand(p2(P + Qv)**2 + p2(P - Qv)**2 - 2*p2(P)**2)   # <[n^dag,[p^4,n]]> kernel
rep("WP1v2-C2a p^4 double-commutator kernel = 2(2p^2q^2 + q^4 + 4(p.q)^2)",
    is0(dd - 2*(2*p2(P)*p2(Qv) + p2(Qv)**2 + 4*(P.T*Qv)[0]**2)))
A = lambda v: a1*v[0] + a2*v[1] + a3*v[2]
rep("WP1v2-C2b terms linear in p (SOC) and multiplicative (Darwin) give zero double commutator",
    sp.expand(A(P + Qv) + A(P - Qv) - 2*A(P)) == 0)
th = symbols('th'); pp, qq = symbols('pp qq', positive=True)
avg = sp.integrate(2*(2*pp**2*qq**2 + qq**4 + 4*pp**2*qq**2*cos(th)**2)*sin(th), (th, 0, pi))/2
shift = sp.expand(-avg/(8*m**3)/(qq**2/m))                    # relative shift of M^1_ee
rep("WP1v2-C2c delta_rel = -(5/3)<T>/m_e - q^2/(4m_e^2)  (<T> = <p^2>/2m_e)",
    is0(shift - (-Q(5, 3)*(pp**2/(2*m))/m - qq**2/(4*m**2))))
al = 1/Q(137036, 1000); me = 510999                            # eV
Ha = Q(272114, 10000)
print(f"   (Z alpha)^2: Si 1s {sp.N((14*al)**2, 3)}, Ge 1s {sp.N((32*al)**2, 3)};  Ge 1s alone (5/6)(Z alpha)^2 = "
      f"{sp.N(Q(5, 6)*(32*al)**2, 3)};  Ge 3d SO/binding = {sp.N(Q(58, 100)/Q(295, 10), 2)}")
print(f"   all-electron shift (<T> = -E_tot: Si 289 Ha/14 e, Ge 2075 Ha/32 e): Si {sp.N(-Q(5, 3)*289*Ha/14/me, 3)}, "
      f"Ge {sp.N(-Q(5, 3)*2075*Ha/32/me, 3)}")

# ------------------------------------------------ C3: static stability [E3]: 0 < (eps^-1)_00(q,0) <= 1 at RPA+LFE
lam = symbols('lam', nonpositive=True)
y = lam/(1 - lam)
u = symbols('u', nonnegative=True)                            # lam = -u <= 0
rep("WP1v2-C3a lam <= 0  =>  lam/(1-lam) = -u/(1+u) in (-1, 0]  (eigenvalues of v^1/2 R v^1/2 = X(1-X)^-1)",
    is0(y.subs(lam, -u) + u/(1 + u)) and is0(y.subs(lam, -u) + 1 - 1/(1 + u)))
samples = [Matrix([[cm(1, 0), cm(2, 1), cm(0, -1)], [cm(1, 1), cm(-1, 2), cm(3, 0)], [cm(0, 2), cm(1, -1), cm(2, 2)]]),
           Matrix([[cm(5, 0), cm(0, 0), cm(1, 1)], [cm(0, 3), cm(1, 0), cm(0, 0)], [cm(2, 0), cm(-1, 1), cm(0, 1)]]),
           Matrix([[cm(1, 0), cm(1, 0), cm(1, 0)], [cm(1, 0), cm(1, 0), cm(1, 0)], [cm(0, 0), cm(0, 1), cm(0, 0)]])]
okC3 = True
for k, B in enumerate(samples):
    for scale, vd in [(Q(1, 10), [Q(10), Q(1), Q(1, 3)]), (Q(7), [Q(1, 2), Q(4), Q(9)])]:
        R0s = -scale*B*dag(B)                                    # static KS response: Hermitian NSD
        V = sp.diag(*vd); epsinv00 = sp.nsimplify((eye(3) - V*R0s).inv()[0, 0])
        okC3 &= is0(sp.im(epsinv00)) and (0 < sp.re(epsinv00) <= 1)
rep("WP1v2-C3b exact NSD R0 examples (complex, LFE 3x3): 0 < (eps^-1)_00 <= 1, Im = 0", okC3)

# ------------------------------------------------ C4: pair-resolved external weight [E2] (F1, CC with WP0-v2 §10)
vg = [Q(1), Q(2, 5)]; Vd = sp.diag(*vg)                       # v_C(q+G), G in {0, G1}
def R0of(rhos, gs):                                           # R0_{GG'} = sum_pairs rho_G^* rho_G' g_pair  (WP0 (3.2) order)
    return sum((r.conjugate()*r.T*g for r, g in zip(rhos, gs)), sp.zeros(2))
rho = [Matrix([cm(1, 0), cm(1, 2)]), Matrix([cm(0, 1), cm(2, -1)]), Matrix([cm(1, 1), cm(-1, 0)])]   # GaAs-like (complex)
gf = [cm(1, -2), cm(-1, -1), cm(2, -3)]                       # Im g < 0: open (absorptive) pairs, omega > 0
R0 = R0of(rho, gf); R = (eye(2) - R0*Vd).inv()*R0
antiH = lambda M: (M - dag(M))/(2*I)
rep("WP1v2-C4a R - R^dag = (1+Rv)(R0-R0^dag)(1+vR^dag) = (1+R^dag v)(R0-R0^dag)(1+vR)",
    is0((eye(2) + R*Vd)*(R0 - dag(R0))*(eye(2) + Vd*dag(R)) - (R - dag(R))) and
    is0((eye(2) + dag(R)*Vd)*(R0 - dag(R0))*(eye(2) + Vd*R) - (R - dag(R))))
exact = antiH(R)[0, 0]
pair = lambda w, r: sp.Abs(sum(w[G]*r[G] for G in range(2)))**2
wout = [(eye(2) + Vd*R)[G, 0] for G in range(2)]             # (eps^-1)_{G0} = delta + v_C(q+G) R_{G0}, retarded
win = [sp.conjugate((eye(2) + R*Vd)[0, G]) for G in range(2)] # [(1+Rv)_{0G}]^*  (in-state, conjugated)
wv1 = [(eye(2) + R*Vd)[0, G] for G in range(2)]               # v1 [E2] as printed
tot = lambda w: sum(sp.im(g)*pair(w, r) for r, g in zip(rho, gf))
rep("WP1v2-C4b [E2] out-state weight (eps^-1)_{G0} rho(q+G): pairs sum to Im R_00, no inversion", is0(tot(wout) - exact))
rep("WP1v2-C4c in-state weight [(1+Rv)_{0G}]^* rho(q+G): pairs also sum to Im R_00", is0(tot(win) - exact))
rep("WP1v2-C4d v1 [E2] as printed, (1+Rv)_{0G} rho, misses Im R_00 without inversion (F1 accepted)",
    not is0(tot(wv1) - exact))
rho_s = [Matrix([Q(1), Q(2)]), Matrix([Q(-1), Q(3)]), Matrix([Q(2), Q(1)])]        # real vertices: TR + inversion
R0s = R0of(rho_s, gf); Rs = (eye(2) - R0s*Vd).inv()*R0s
w1s = [(eye(2) + Rs*Vd)[0, G] for G in range(2)]; wos = [(eye(2) + Vd*Rs)[G, 0] for G in range(2)]
rep("WP1v2-C4e TR + inversion (symmetric R): (1+Rv)_{0G} = (eps^-1)_{G0}; v1 form = out-state pair by pair",
    all(is0(w1s[G] - wos[G]) for G in range(2)))

# ------------------------------------------------ C5: exciton matrix element <lambda|n_q|0> = sqrt2 sum A^* rho  ([E7])
A1, A2 = cm(1, 1)/2, cm(1, -1)/2; r1, r2 = cm(1, 2), cm(0, 1)  # two-pair envelope, complex
amp_true = sqrt(2)*(sp.conjugate(A1)*r1 + sp.conjugate(A2)*r2)  # |lambda> = sum A |cvk, singlet>
rep("WP1v2-C5a |<lambda|n|0>|^2 = 2|sum A^* rho|^2 differs from v1's 2|sum A rho|^2 for complex A, rho",
    not is0(sp.Abs(amp_true)**2 - 2*sp.Abs(A1*r1 + A2*r2)**2))
sig = [Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])]
spin_ratio = [[sp.trace((sig[a]/2)*(sig[b]/2)) / sp.trace(eye(2)) for b in range(3)] for a in range(3)]
rep("WP1v2-C5b spin channel [E6]: tr(s^a s^b)/tr(1) = delta_ab/4 (S_ss = S_nn^IP/4); DM j=1/2: tr(S^aS^b)/2 = delta/4",
    all(is0(spin_ratio[a][b] - (Q(1, 4) if a == b else 0)) for a in range(3) for b in range(3)))

# ------------------------------------------------ C6: on-shell longitudinal cancellation [E4] and transverse response [E5]
vx, vy, vz, mchi, Ww, e2, beta, nn, ImEpsT = symbols('v_x v_y v_z m_chi omega e2 beta n ImEpsT', real=True)
qvec = Matrix([0, 0, q]); vvec = Matrix([vx, vy, vz])
omq = (qvec.T*vvec)[0] - q**2/(2*mchi)                       # (2.1) with Delta_chi = 0
vchi = vvec - qvec/(2*mchi)
rep("WP1v2-C6a q^.v_chi = omega_q/q on shell: longitudinal (v_chi,L n - j_L) -> 0; only v_T, j_T survive",
    is0(vchi[2] - omq/q) and is0(Matrix([vchi[0], vchi[1]]) - Matrix([vx, vy])))
ImR = symbols('ImR', real=True)
ImEps = -e2*ImR/Ww**2                                         # eps_T = 1 - Pi^gamma_T/w^2, Pi = e^2(R + n/m)
S_from_R = -2*ImR/(1 - exp(-beta*Ww))
rep("WP1v2-C6b [E5] S_{jTjT} = (2 w^2/e^2) Im eps_T/(1 - e^{-beta w}) per polarisation",
    is0(S_from_R - 2*Ww**2/e2*ImEps/(1 - exp(-beta*Ww))))

# ------------------------------------------------ C7: Si HEG and plasmon [E9]
w, wp, vF, k = symbols('w w_p v_F k', positive=True)
eps1 = 1 - wp**2/w**2 - Q(3, 5)*wp**2*k**2*vF**2/w**4
wpl = sqrt(wp**2 + Q(3, 5)*k**2*vF**2)
Fk = sp.series(sp.simplify((2*wpl/(wp**2*sp.diff(eps1, w))).subs(w, wpl)), k, 0, 4).removeO()
rep("WP1v2-C7a plasmon pole share of the f-sum w_pl(q) = 1 + O(q^4)  [E9], (9.5) normalisation", is0(Fk - 1))
a0 = Q(529177, 10**6); aSi = Q(5431, 1000); hc = Q(197327, 100)   # A, A, eV A
ne = 32/aSi**3; rs = sp.N(((3/(4*pi*ne))**Q(1, 3))/a0, 4); kF = (3*pi**2*ne)**Q(1, 3)
wp_ = sqrt(4*pi*ne*Q(143996, 10000)*hc**2/me); vF_ = kF*hc/me
qc = sp.N((-vF_ + sqrt(vF_**2 + 2*wp_/me))*me, 6)                  # w_p = q v_F + q^2/2m_e
vmax = Q(7945, 10)/Q(299792458, 1000)                              # v_max = 794.5 km/s (CONVENTIONS §8)
print(f"   Si HEG: r_s={rs}, k_F={sp.N(kF*hc/1000, 3)} keV, w_p={sp.N(wp_, 3)} eV, v_F={sp.N(vF_, 3)}, q_c={sp.N(qc/1000, 3)} keV, "
      f"w_p/v_F={sp.N(wp_/vF_/1000, 3)} keV, 2pi/a={sp.N(2*pi/aSi*hc/1000, 3)} keV, w_p/v_max={sp.N(wp_/vmax/1000, 3)} keV")
rep("WP1v2-C7b w_p/v_max > q_c: no bulk plasmon for halo DM", sp.N(wp_/vmax) > qc)

# ------------------------------------------------ C8: Elliott/Wannier [E8]
D, Eb, ax = symbols('D E_b a_x', positive=True)
bound = zeta(3)/(pi*ax**3)                                        # sum_n 1/(pi a^3 n^3)
mu2 = 1/(ax**2*Eb)                                                # 2 mu_x = 1/(a_x^2 E_b)
cont = sp.integrate(mu2**Q(3, 2)*sqrt(D)/(4*pi**2), (D, 0, D))
sol = sp.solve(sp.Eq(cont.subs(D, D*Eb), bound), D)[0]
rep("WP1v2-C8a bound weight = free-continuum weight within (6 pi zeta(3))^{2/3} E_b of the edge",
    is0(sol - (6*pi*zeta(3))**Q(2, 3)), f"= {sp.N(sol, 3)} E_b")
SF = lambda xx: (2*pi/sqrt(xx))/(1 - exp(-2*pi/sqrt(xx)))
print("   Sommerfeld S_F at (w-E_min)/E_x^b = 1, 10, 30, 100, 1.5eV/14.7meV:",
      [float(sp.N(SF(t), 3)) for t in [1, 10, 30, 100, Q(1500, 147)*10]])

# ------------------------------------------------ C9: kinematic thresholds (§3.4), v_max = 794.5 km/s
def mmin(frac, a, Ex):
    qv = sqrt(sum(sp.nsimplify(c)**2 for c in frac))*2*pi/a*hc
    return sp.N(qv/1000, 3), sp.N(qv**2/(2*(qv*vmax - Ex))/10**6, 3)
for lab, frac, a, Ex in [("Si G=0 (q||Delta, forbidden)", [Q(85, 100), 0, 0], aSi, Q(1170, 1000) - Q(147, 10000)),
                         ("Si G=(-1,1,1) (allowed)", [Q(85, 100) - 1, 1, 1], aSi, Q(1170, 1000) - Q(147, 10000)),
                         ("Ge G=0 (q||Lambda, allowed)", [Q(1, 2)]*3, Q(5658, 1000), Q(744, 1000) - Q(415, 100000))]:
    qk, mm = mmin(frac, a, Ex); print(f"   C9 {lab}: |q| = {qk} keV, m_chi,min = {mm} MeV")
rep("WP1v2-C9 threshold formula m_chi >= q^2/[2(q v_max - E_x)] from omega_q >= E_x (2.1)",
    is0(sp.solve(sp.Eq(q*symbols('V') - q**2/(2*mchi), symbols('E_x')), mchi)[0]
        - q**2/(2*(q*symbols('V') - symbols('E_x')))))

# ------------------------------------------------ C10: point-group selection rules at the extrema (§3.2 (c))
X, Y, Z = symbols('X Y Z')
def projA1(fun, ops): return sp.simplify(sum(fun.subs({X: o[0], Y: o[1], Z: o[2]}, simultaneous=True) for o in ops)/len(ops))
C4v_x = [(X, Y, Z), (X, -Z, Y), (X, -Y, -Z), (X, Z, -Y), (X, -Y, Z), (X, Y, -Z), (X, Z, Y), (X, -Z, -Y)]
G25p = [Y*Z, Z*X, X*Y]
rep("WP1v2-C10a Si: Gamma25' has no Delta1 (A1 of C4v[100]) part: rho_cv(Gamma25'->Delta1, q||[100]) = 0",
    all(projA1(g, C4v_x) == 0 for g in G25p))
C3v = [(X, Y, Z), (Y, Z, X), (Z, X, Y), (Y, X, Z), (X, Z, Y), (Z, Y, X)]
rep("WP1v2-C10b Ge: Gamma25' contains Lambda1 (A1 of C3v[111]): Gamma25'->L1 allowed", any(projA1(g, C3v) != 0 for g in G25p))

# ------------------------------------------------ C11: multipoles of S in cubic crystals (§6.1): group characters
t = symbols('t')
chi = lambda l, ang: sp.simplify(sum(exp(I*mm*ang) for mm in range(-l, l + 1)).rewrite(cos))
def n_inv_O(l):  return sp.nsimplify((chi(l, 0) + 8*chi(l, 2*pi/3) + 3*chi(l, pi) + 6*chi(l, pi/2) + 6*chi(l, pi))/24)
def n_inv_Oh(l): return sp.nsimplify(n_inv_O(l)*(1 + (-1)**l)/2)
def n_inv_Td(l): return sp.nsimplify((chi(l, 0) + 8*chi(l, 2*pi/3) + 3*chi(l, pi) + (-1)**l*(6*chi(l, pi/2) + 6*chi(l, pi)))/24)
Oh = [n_inv_Oh(l) for l in range(9)]; Td = [n_inv_Td(l) for l in range(9)]
Td_TR = [Td[l] if l % 2 == 0 else 0 for l in range(9)]            # TR: S(q) = S(-q) kills odd l
rep("WP1v2-C11a O_h (Si, Ge) invariant harmonics l=0..8: [1,0,0,0,1,0,1,0,1]", Oh == [1, 0, 0, 0, 1, 0, 1, 0, 1], str(Oh))
rep("WP1v2-C11b T_d (GaAs): l=3 invariant (xyz) exists; removed by TR; l=2 absent", Td[3] == 1 and Td[2] == 0 and
    Td_TR == [1, 0, 0, 0, 1, 0, 1, 0, 1], str(Td))

# ------------------------------------------------ C12: rate dictionaries [E12], L2, L11
Om, S_, eps2, alpha, mel, mu, rhoT, rhoc, mc, sig_e, eta_, F2, E_ = symbols(
    'Omega S eps2 alpha m_e mu rho_T rho_chi m_chi sigma_e eta F2 E', positive=True)
e2v = 4*pi*alpha
fcr = Om*q**3*S_/(4*pi*alpha*mel**2)
rep("WP1v2-C12a [E12] Omega q^3 S/(4 pi alpha m_e^2) = Omega q^5 eps2/(8 pi^2 alpha^2 m_e^2) with S = 2q^2 eps2/e^2",
    is0(fcr.subs(S_, 2*q**2*eps2/e2v) - Om*q**5*eps2/(8*pi**2*alpha**2*mel**2)))
# 1509.01598 Eq. (17), per target -> per unit mass (N_cell/M_T = 1/(rho_T Omega)), d/dlnE -> d/domega
integrand17 = (rhoc/mc)*(1/(rhoT*Om))*sig_e*alpha*(mel**2/mu**2)*(1/q)*(E_/q)*eta_*F2*fcr/E_
integrand92 = rhoc*sig_e/(4*pi*mc*rhoT*mu**2)*q*eta_*F2*S_
rep("WP1v2-C12b 1509.01598 Eq. (17) with [E12] = WP0-v2 (9.2) integrand (spin 2, eta/2q)", is0(integrand17 - integrand92))
rep("WP1v2-C12c L2: 2q^2/e^2 = q^2/(2 pi alpha)  (2101.08275 Eq. (6))", is0(2*q**2/e2v - q**2/(2*pi*alpha)))
echi, Lf = symbols('e_chi L', positive=True)
lhs = (1/(2*pi)**3)*(echi**2*e2v/q**4)*(2*q**2/e2v)*Lf         # d^3q/(2pi)^3 |V|^2 S, T = 0
rep("WP1v2-C12d L11: |V|^2 = e_chi^2 e^2/q^4 gives (alpha_chi/pi^2) d^3q L/q^2, alpha_chi = e_chi^2/4pi (2002.06937 Eq. (13))",
    is0(lhs - (echi**2/(4*pi))/pi**2*Lf/q**2))

print(f"\n{sum(RES)}/{len(RES)} PASS")
