"""WP1-v3 identity and number checks (R8 revision; copy of code/WP1-v2/checks.py with the R7 referee fixes and new checks).
Sympy only, exact arithmetic; numbers are evalf of closed forms or polynomial roots (no simulation, no numpy/scipy).
Run:  python3 -I checks.py        Labels WP1v3-Cn (CONVENTIONS sec. 14). Notation: NOTATION v4.
Changed vs v2: C7b/C7c (q_c with the plasmon dispersion, REF-B H), C9 (threshold = min over q, REF-A A9 / REF-B G; the v2
check only solved the pinned formula), C10 (full space group with the nonsymmorphic phases; v2's C10 used point operations only
and could not see the Si (2-00) Umklapp, REF-A A8). New: C1c (PT reality), C2d (Pauli spin-curl coefficient), C3c-d (beyond-RPA
condition), C6c-e (O8 bounds and ratios), C7d (Cappellini numbers), C8b-c (p-state weight, edge continuity), C9a-g, C10c-e."""
import sympy as sp, itertools
from sympy import I, Rational as Q, Matrix, eye, sqrt, pi, exp, cos, sin, symbols, simplify, zeta

RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:86s} {note}")
def is0(e):
    if isinstance(e, sp.MatrixBase): return all(is0(x) for x in e)
    return sp.simplify(sp.expand_complex(sp.sympify(e))) == 0
def dag(M): return M.conjugate().T
def cm(a, b): return Q(a) + I*Q(b)
N3 = lambda e: sp.N(e, 3)

# ------------------------------------------------ C1: continuity and Catena's responses (§2.1, L3)
x, q, m = symbols('x q m', positive=True)
f = sp.Function('f')(x)
p_ = lambda g: -I*sp.diff(g, x)
n_ = lambda g: exp(I*q*x)*g
T_ = lambda g: p_(p_(g))/(2*m)
j_ = lambda g: (p_(n_(g)) + n_(p_(g)))/(2*m)
rep("WP1v3-C1a [T_e, n_e(q)] = q.j_e(q), j_e = 1/2{p/m_e, e^{iqx}} (no (q^2/2m)n term)", is0(T_(n_(f)) - n_(T_(f)) - q*j_(f)))
fvec = lambda g: n_(I*sp.diff(g, x))/m                       # 2105.02233 Eq. (11) vector overlap
rep("WP1v3-C1b q.f_vec = -(q.j_e - (q^2/2m_e) n_e)  =>  W2-bar, W4-bar fixed by W1-bar (local H)",
    is0(q*fvec(f) + q*j_(f) - q**2/(2*m)*n_(f)))
# C1c: PT (TR + inversion) => F_ab(z) = F_ab(z*)^*  => S_ab real (Im W2-bar = W5-bar = 0) for ANY H, local or not.
z = symbols('z'); xs = [Q(-3, 2), Q(-1, 2), Q(1, 2), Q(3, 2)]; qq_ = Q(7, 5)
e1, e2_, t1, s1, w1 = Q(1, 3), Q(-2, 5), Q(1), Q(3, 4), Q(1, 7)
Hpt = Matrix([[e1, -t1, w1, 0], [-t1, e2_, -s1, w1], [w1, -s1, e2_, -t1], [0, w1, -t1, e1]])   # real, P-symmetric (w1: 2nd neighbour, a "nonlocal" term)
Nop = sp.diag(*[exp(I*qq_*xx) for xx in xs])
Dm = Matrix([[0, 1, 0, 0], [-1, 0, 1, 0], [0, -1, 0, 1], [0, 0, -1, 0]])/2
Pop = -I*Dm; Jop = (Pop*Nop + Nop*Pop)/2
psi0 = Matrix([1, 2, 2, 1])                                   # PT-invariant reference: psi(-x)^* = psi(x)
def F(H, A, B, zz): return (dag(psi0)*dag(A)*(zz*eye(4) - H).inv()*B*psi0)[0]
def ptdefect(H, A, B):
    zs = Q(1, 2) + I*Q(1, 3)
    return sp.nsimplify(sp.expand_complex(F(H, A, B, zs) - sp.conjugate(F(H, A, B, sp.conjugate(zs)))))
okPT = all(is0(ptdefect(Hpt, A, B)) for A, B in [(Nop, Jop), (Jop, Jop), (Nop, Nop)])
Hbroken = Hpt + sp.diag(Q(1, 2), 0, 0, 0)                      # T kept, inversion broken (GaAs-like)
rep("WP1v3-C1c PT-symmetric H (incl. nonlocal hop): F_ab(z)=F_ab(z*)^* for (n,j),(j,j): S_ab real; fails if P broken",
    okPT and not is0(ptdefect(Hbroken, Nop, Jop)))

# ------------------------------------------------ C2: relativistic f-sum [E11]; FW spin-curl coefficient (§5.2)
px, py, pz, qx, qy, qz, a1, a2, a3 = symbols('px py pz qx qy qz a1 a2 a3', real=True)
P = Matrix([px, py, pz]); Qv = Matrix([qx, qy, qz]); p2 = lambda v: (v.T*v)[0]
dd = sp.expand(p2(P + Qv)**2 + p2(P - Qv)**2 - 2*p2(P)**2)
rep("WP1v3-C2a p^4 double-commutator kernel = 2(2p^2q^2 + q^4 + 4(p.q)^2)",
    is0(dd - 2*(2*p2(P)*p2(Qv) + p2(Qv)**2 + 4*(P.T*Qv)[0]**2)))
A = lambda v: a1*v[0] + a2*v[1] + a3*v[2]
rep("WP1v3-C2b terms linear in p (SOC) and multiplicative (Darwin) give zero double commutator",
    sp.expand(A(P + Qv) + A(P - Qv) - 2*A(P)) == 0)
th = symbols('th'); pp, qq = symbols('pp qq', positive=True)
avg = sp.integrate(2*(2*pp**2*qq**2 + qq**4 + 4*pp**2*qq**2*cos(th)**2)*sin(th), (th, 0, pi))/2
shift = sp.expand(-avg/(8*m**3)/(qq**2/m))
rep("WP1v3-C2c delta_rel = -(5/3)<T>/m_e - q^2/(4m_e^2)  (<T> = <p^2>/2m_e)",
    is0(shift - (-Q(5, 3)*(pp**2/(2*m))/m - qq**2/(4*m**2))))
sig = [Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])]
pv = Matrix(symbols('p1:4', real=True)); ppv = Matrix(symbols('pp1:4', real=True)); qv_ = ppv - pv
sdot = lambda a: sum((a[k]*sig[k] for k in range(3)), sp.zeros(2))
okG = True
for i in range(3):
    lhs = (sdot(ppv)*sig[i] + sig[i]*sdot(pv))/(2*m)              # NR limit of u'^dag gamma^0 gamma^i u (Pauli spinors)
    qxs = [qv_[(i+1) % 3]*sig[(i+2) % 3] - qv_[(i+2) % 3]*sig[(i+1) % 3]][0]   # (q x sigma)_i
    rhs = (pv[i] + ppv[i])/(2*m)*eye(2) - (I/m)*(qxs/2)           # (p+p')/2m - (i/m)(q x s), s = sigma/2
    okG &= is0(sp.expand(lhs - rhs))
rep("WP1v3-C2d NR vector current: (p+p')/2m_e - (i/m_e) q x s_e (spin-curl coefficient 1/m_e with s = sigma/2)", okG)
al = 1/Q(137036, 1000); me = 510999; Ha = Q(272114, 10000)
print(f"   (Z alpha)^2: Si 1s {N3((14*al)**2)}, Ge 1s {N3((32*al)**2)};  Ge 3d SO/binding = {sp.N(Q(58, 100)/Q(295, 10), 2)} (bound);"
      f"  all-electron shift: Si {N3(-Q(5, 3)*289*Ha/14/me)}, Ge {N3(-Q(5, 3)*2075*Ha/32/me)}")

# ------------------------------------------------ C3: static stability [E3] (RPA) and the beyond-RPA condition (§1.4)
lam = symbols('lam', nonpositive=True); y = lam/(1 - lam); u = symbols('u', nonnegative=True)
rep("WP1v3-C3a lam <= 0  =>  lam/(1-lam) = -u/(1+u) in (-1, 0]  (eigenvalues of v^1/2 R v^1/2 = X(1-X)^-1)",
    is0(y.subs(lam, -u) + u/(1 + u)) and is0(y.subs(lam, -u) + 1 - 1/(1 + u)))
samples = [Matrix([[cm(1, 0), cm(2, 1), cm(0, -1)], [cm(1, 1), cm(-1, 2), cm(3, 0)], [cm(0, 2), cm(1, -1), cm(2, 2)]]),
           Matrix([[cm(5, 0), cm(0, 0), cm(1, 1)], [cm(0, 3), cm(1, 0), cm(0, 0)], [cm(2, 0), cm(-1, 1), cm(0, 1)]]),
           Matrix([[cm(1, 0), cm(1, 0), cm(1, 0)], [cm(1, 0), cm(1, 0), cm(1, 0)], [cm(0, 0), cm(0, 1), cm(0, 0)]])]
okC3 = True
for B in samples:
    for scale, vd in [(Q(1, 10), [Q(10), Q(1), Q(1, 3)]), (Q(7), [Q(1, 2), Q(4), Q(9)])]:
        R0s = -scale*B*dag(B); V = sp.diag(*vd); ei = sp.nsimplify((eye(3) - V*R0s).inv()[0, 0])
        okC3 &= is0(sp.im(ei)) and (0 < sp.re(ei) <= 1)
rep("WP1v3-C3b exact NSD R0 examples (complex, LFE 3x3): 0 < (eps^-1)_00 <= 1, Im = 0", okC3)
a_, b_, c_ = Q(1), Q(2), Q(3)                                 # R0 = -a, f_xc = -b, v_C = c (1x1)
Rt = -a_/(1 - b_*a_); einv = 1/(1 - c_*Rt)
rep("WP1v3-C3c counterexample: 1 - f_Hxc R0 = 2 > 0 (full R stable) yet (eps^-1) = -1/2 < 0: v2 condition insufficient",
    (1 - (c_ - b_)*(-a_)) > 0 and einv == Q(-1, 2))
okC3d = True
for B in samples[:2]:
    R0s = -Q(1, 4)*B*dag(B); fxc = -Q(1, 50)*Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 2]])
    Mpos = (-R0s).inv() + fxc                                  # condition (-R0)^-1 + f_xc > 0 (Sylvester minors)
    pos = all(sp.re(sp.nsimplify(Mpos[:k, :k].det())) > 0 for k in (1, 2, 3))
    Rt3 = (eye(3) - R0s*fxc).inv()*R0s; V = sp.diag(Q(3), Q(1), Q(1, 2))
    ei = sp.nsimplify((eye(3) - V*Rt3).inv()[0, 0])
    okC3d &= pos and is0(sp.im(ei)) and (0 < sp.re(ei) <= 1)
rep("WP1v3-C3d (-R0)^-1 + f_xc > 0 (proper R~ NSD) => 0 < (eps^-1)_00 <= 1 with LFE and attractive f_xc", okC3d)

# ------------------------------------------------ C4: pair-resolved external weight [E2] (F1)
vg = [Q(1), Q(2, 5)]; Vd = sp.diag(*vg)
def R0of(rhos, gs): return sum((r.conjugate()*r.T*g for r, g in zip(rhos, gs)), sp.zeros(2))
rho = [Matrix([cm(1, 0), cm(1, 2)]), Matrix([cm(0, 1), cm(2, -1)]), Matrix([cm(1, 1), cm(-1, 0)])]
gf = [cm(1, -2), cm(-1, -1), cm(2, -3)]
R0 = R0of(rho, gf); R = (eye(2) - R0*Vd).inv()*R0
antiH = lambda M: (M - dag(M))/(2*I)
rep("WP1v3-C4a R - R^dag = (1+Rv)(R0-R0^dag)(1+vR^dag) = (1+R^dag v)(R0-R0^dag)(1+vR)",
    is0((eye(2) + R*Vd)*(R0 - dag(R0))*(eye(2) + Vd*dag(R)) - (R - dag(R))) and
    is0((eye(2) + dag(R)*Vd)*(R0 - dag(R0))*(eye(2) + Vd*R) - (R - dag(R))))
exact = antiH(R)[0, 0]
pair = lambda w, r: sp.Abs(sum(w[G]*r[G] for G in range(2)))**2
wout = [(eye(2) + Vd*R)[G, 0] for G in range(2)]
win = [sp.conjugate((eye(2) + R*Vd)[0, G]) for G in range(2)]
wv1 = [(eye(2) + R*Vd)[0, G] for G in range(2)]
tot = lambda w: sum(sp.im(g)*pair(w, r) for r, g in zip(rho, gf))
rep("WP1v3-C4b [E2] out-state weight (eps^-1)_{G0} rho(q+G): pairs sum to Im R_00, no inversion", is0(tot(wout) - exact))
rep("WP1v3-C4c in-state weight [(1+Rv)_{0G}]^* rho(q+G): pairs also sum to Im R_00", is0(tot(win) - exact))
rep("WP1v3-C4d v1 [E2] as printed, (1+Rv)_{0G} rho, misses Im R_00 without inversion (F1 accepted)", not is0(tot(wv1) - exact))
rho_s = [Matrix([Q(1), Q(2)]), Matrix([Q(-1), Q(3)]), Matrix([Q(2), Q(1)])]
R0s = R0of(rho_s, gf); Rs = (eye(2) - R0s*Vd).inv()*R0s
w1s = [(eye(2) + Rs*Vd)[0, G] for G in range(2)]; wos = [(eye(2) + Vd*Rs)[G, 0] for G in range(2)]
rep("WP1v3-C4e TR + inversion (symmetric R): (1+Rv)_{0G} = (eps^-1)_{G0}; v1 form = out-state pair by pair",
    all(is0(w1s[G] - wos[G]) for G in range(2)))

# ------------------------------------------------ C5: exciton matrix element [E7]; spin factor [E6]
A1, A2 = cm(1, 1)/2, cm(1, -1)/2; r1, r2 = cm(1, 2), cm(0, 1)
amp_true = sqrt(2)*(sp.conjugate(A1)*r1 + sp.conjugate(A2)*r2)
rep("WP1v3-C5a |<lambda|n|0>|^2 = 2|sum A^* rho|^2 differs from v1's 2|sum A rho|^2 for complex A, rho",
    not is0(sp.Abs(amp_true)**2 - 2*sp.Abs(A1*r1 + A2*r2)**2))
spin_ratio = [[sp.trace((sig[a]/2)*(sig[b]/2))/sp.trace(eye(2)) for b in range(3)] for a in range(3)]
rep("WP1v3-C5b spin channel [E6]: tr(s^a s^b)/tr(1) = delta_ab/4 (S_ss = S_nn^IP/4); DM j=1/2: tr(S^aS^b)/2 = delta/4",
    all(is0(spin_ratio[a][b] - (Q(1, 4) if a == b else 0)) for a in range(3) for b in range(3)))

# ------------------------------------------------ C6: on-shell cancellation [E4], transverse response [E5], O8 bounds (L3 (c))
vx, vy, vz, mchi, Ww, e2, beta = symbols('v_x v_y v_z m_chi omega e2 beta', real=True)
qvec = Matrix([0, 0, q]); vvec = Matrix([vx, vy, vz])
omq = (qvec.T*vvec)[0] - q**2/(2*mchi); vchi = vvec - qvec/(2*mchi)
rep("WP1v3-C6a q^.v_chi = omega_q/q on shell: longitudinal (v_chi,L n - j_L) -> 0; only v_T, j_T survive",
    is0(vchi[2] - omq/q) and is0(Matrix([vchi[0], vchi[1]]) - Matrix([vx, vy])))
ImR = symbols('ImR', real=True)
rep("WP1v3-C6b [E5] S_{jTjT,lambda} = (2 w^2/e^2) Im eps_{T,lambda}/(1 - e^{-beta w}) per polarisation",
    is0(-2*ImR/(1 - exp(-beta*Ww)) - 2*Ww**2/e2*(-e2*ImR/Ww**2)/(1 - exp(-beta*Ww))))
Aa, Bb, cc, rr = symbols('A B c r', positive=True)
rep("WP1v3-C6c PSD: A - 2Re c + B >= (sqrt A - sqrt B)^2 if |c|^2 <= AB; (sqrt r - 1)^2 >= 1 iff r >= 4",
    is0((Aa + Bb - 2*sqrt(Aa*Bb)) - (sqrt(Aa) - sqrt(Bb))**2) and sp.solve(sp.Eq((sqrt(rr) - 1)**2, 1), rr) == [4])
ImT, ImL, absL, w_ = symbols('ImT ImL absL w', positive=True)
ratio = (2*(2*w_**2/e2)*ImT)/(vx**2*(2*q**2/e2)*ImL/absL**2)
rep("WP1v3-C6d in-medium O8 ratio tr S_jTjT/(|v_T|^2 S_nn) = 2(w/q)^2 |eps_L|^2 (Im eps_T/Im eps_L)/|v_T|^2 (REF-B C)",
    is0(ratio - 2*(w_/q)**2*absL**2*(ImT/ImL)/vx**2))
kF_me = Q(698, 100000)                                         # Si valence HEG v_F = k_F/m_e
r_lo, r_hi = Q(2, 5)*kF_me**2/Q(1, 10**6), Q(2, 5)*kF_me**2/Q(7, 10**7)
rep("WP1v3-C6e IP zeroth-moment ratio <p_T^2>/(m_e^2|v_T|^2) = (2/5)v_F^2/|v_T|^2 in [20, 30] for |v_T|^2 = (0.7-1)e-6",
    19 < r_lo < 21 and 27 < r_hi < 29, f"= {N3(r_lo)} .. {N3(r_hi)}")

# ------------------------------------------------ C7: Si HEG, plasmon [E9], Landau onset with dispersion, Cappellini
w, wp, vF, k = symbols('w w_p v_F k', positive=True)
eps1 = 1 - wp**2/w**2 - Q(3, 5)*wp**2*k**2*vF**2/w**4
wpl = sqrt(wp**2 + Q(3, 5)*k**2*vF**2)
Fk = sp.series(sp.simplify((2*wpl/(wp**2*sp.diff(eps1, w))).subs(w, wpl)), k, 0, 4).removeO()
rep("WP1v3-C7a plasmon pole share of the f-sum w_pl(q) = 1 + O(q^4)  [E9]", is0(Fk - 1))
a0 = Q(529177, 10**6); aSi = Q(5431, 1000); aGe = Q(5658, 1000); hc = Q(197327, 100)
ne = 32/aSi**3; rs = sp.N(((3/(4*pi*ne))**Q(1, 3))/a0, 4); kF = (3*pi**2*ne)**Q(1, 3)
wp_ = sqrt(4*pi*ne*Q(143996, 10000)*hc**2/me); vF_ = kF*hc/me
vmax = Q(7945, 10)/Q(299792458, 1000)
qq0 = symbols('qq0', positive=True)
qc_old = max(sp.Poly(sp.expand((qq0*vF_ + qq0**2/(2*me))**2 - wp_**2), qq0).nroots(n=15), key=lambda r: sp.re(r) if r.is_real else -1)
qc_new = max(r for r in sp.Poly(sp.expand((qq0*vF_ + qq0**2/(2*me))**2 - wp_**2 - Q(3, 5)*qq0**2*vF_**2), qq0).nroots(n=15) if r.is_real)
print(f"   Si HEG: r_s={rs}, k_F={N3(kF*hc/1000)} keV, w_p={N3(wp_)} eV, v_F={N3(vF_)}, 2pi/a={N3(2*pi/aSi*hc/1000)} keV, "
      f"w_p/v_max={N3(wp_/vmax/1000)} keV; Landau onset: with w_p {N3(qc_old/1000)} keV (v2), with w_pl(q) {N3(qc_new/1000)} keV")
rep("WP1v3-C7b Landau onset with the [E9] dispersion q_c in [2.2, 2.3] keV (REF-B H; v2's 1.88 used constant w_p)",
    2200 < qc_new < 2300 and 1850 < qc_old < 1900)
rep("WP1v3-C7c w_p/v_max > q_c (either definition): no bulk plasmon for halo DM", sp.N(wp_/vmax) > qc_new)
epsinf, kTF, alC = Q(113, 10), Q(4130), Q(1563, 1000)
capp = lambda qq_e: 1 + 1/(1/(epsinf - 1) + alC*(qq_e/kTF)**2 + qq_e**4/(4*me**2*Q(166, 10)**2))
i2, iam = 1/capp(Q(2000))**2, 1/capp(al*me)**2
rep("WP1v3-C7d Cappellini static 1/eps^2 = 0.117 (q = 2 keV), 0.451 (q = alpha m_e) (pointwise, REF-B K)",
    abs(sp.N(i2) - Q(117, 1000)) < Q(1, 1000) and abs(sp.N(iam) - Q(451, 1000)) < Q(1, 1000), f"{N3(i2)}, {N3(iam)}")

# ------------------------------------------------ C8: Elliott/Wannier [E8] (allowed and second class)
D, Eb, ax = symbols('D E_b a_x', positive=True)
bound = zeta(3)/(pi*ax**3); mu2 = 1/(ax**2*Eb)
cont = sp.integrate(mu2**Q(3, 2)*sqrt(D)/(4*pi**2), (D, 0, D))
sol = sp.solve(sp.Eq(cont.subs(D, D*Eb), bound), D)[0]
rep("WP1v3-C8a bound weight = free-continuum weight within (6 pi zeta(3))^{2/3} E_b of the edge",
    is0(sol - (6*pi*zeta(3))**Q(2, 3)), f"= {N3(sol)} E_b")
from sympy.physics.hydrogen import R_nl
rr_ = symbols('rr', positive=True); okp = True
for nH in [2, 3, 4, 5]:
    cnl = sp.limit(R_nl(nH, 1, rr_, 1)/rr_, rr_, 0)              # R_n1 ~ c r, a_x = 1
    okp &= is0(cnl**2*Q(3)/(4*pi) - (nH**2 - 1)/(3*pi*nH**5))  # sum_m |d_z psi_n1m(0)|^2 (only m = 0)
rep("WP1v3-C8b second class: sum_m |b.grad psi_n1m(0)|^2 = |b|^2 (n_H^2-1)/(3 pi a_x^5 n_H^5) (v2 printed 3x this)", okp)
nH, eps_ = symbols('n_H epsilon', positive=True)
dens_s = (1/(pi*ax**3*nH**3))*nH**3/(2*Eb)                     # line weight x lines per unit energy (n_H -> oo)
cont_s = sp.limit((mu2**Q(3, 2)*sqrt(eps_)/(4*pi**2))*2*pi*sqrt(Eb/eps_), eps_, 0)
dens_p = ((nH**2 - 1)/(3*pi*ax**5*nH**5))*nH**3/(2*Eb)
cont_p = sp.limit((mu2*eps_/3)*(mu2**Q(3, 2)*sqrt(eps_)/(4*pi**2))*2*pi*sqrt(Eb/eps_)*(1 + Eb/eps_), eps_, 0)
rep("WP1v3-C8c edge continuity: bound-line density = continuum at E_min+ for s (|rho|^2) and p (|b|^2 k^2/3, S_F(1+zeta^2))",
    is0(dens_s - cont_s) and is0(sp.limit(dens_p, nH, sp.oo) - cont_p))
SF = lambda xx: (2*pi/sqrt(xx))/(1 - exp(-2*pi/sqrt(xx)))
print("   Sommerfeld S_F at (w-E_min)/E_x^b = 1, 10, 30, 100:", [float(N3(SF(t))) for t in [1, 10, 30, 100]])

# ------------------------------------------------ C9: zero-phonon thresholds = min over q (§3.4, IF-6)
Qs, V, Ex, M, Q0 = symbols('Q V E_x M Q_0', positive=True)
g = Qs**2/(2*(Qs*V - Ex))
rep("WP1v3-C9a flat E: dg/dQ = Q(QV - 2E_x)/[2(QV - E_x)^2] > 0 at the extremum when Q V > 2E_x (pinned value not minimal)",
    is0(sp.diff(g, Qs) - Qs*(Qs*V - 2*Ex)/(2*(Qs*V - Ex)**2)))
gd = Qs**2/(2*(Qs*V - Ex - (Q0 - Qs)**2/(2*M)))
Qstar = (2*M*Ex + Q0**2)/(M*V + Q0)
rep("WP1v3-C9b parabolic E(Q) = E_x + (Q_0-Q)^2/2M: dg/dQ = 0 at Q* = (2M E_x + Q_0^2)/(M V + Q_0) (linear condition)",
    is0(sp.numer(sp.together(sp.diff(gd, Qs))).subs(Qs, Qstar)))
mch = symbols('m_chi', positive=True)
rep("WP1v3-C9c m_chi >= Q^2/[2(QV - E)]  <=>  E/Q + Q/(2 m_chi) <= V (REF-WP6-A edge form)",
    is0(sp.solve(sp.Eq(Ex/Qs + Qs/(2*mch), V), mch)[0] - g))
vm = vmax; qBZ = lambda a: 2*pi/a*hc
ExSi, ExGe = Q(1170, 1000) - Q(147, 10000), Q(744, 1000) - Q(415, 100000)
mlSi, mlGe = Q(916, 1000), Q(159, 100)                          # CB longitudinal masses [UNVERIFIED inputs]
hhSi100 = 1/(Q(4285, 1000) - 2*Q(339, 1000)); hhGe111 = 1/(Q(1338, 100) - 2*Q(569, 100))   # Luttinger hh masses [UNVERIFIED]
MSi, MGe = (mlSi + hhSi100)*me, (mlGe + hhGe111)*me
def thr(Q0v, Exv, Mv, qmin=None):
    Qst = (2*Mv*Exv + Q0v**2)/(Mv*vm + Q0v)
    if qmin is not None and Qst < qmin: Qst = qmin
    D_ = Qst*vm - Exv - (Q0v - Qst)**2/(2*Mv)
    return Qst, Qst**2/(2*D_), (Q0v - Qst)**2/(2*Mv)
pin = lambda Q0v, Exv: Q0v**2/(2*(Q0v*vm - Exv))
Q0Si, Q0Ge = Q(85, 100)*qBZ(aSi), sqrt(3)/2*qBZ(aGe)
Q0U200, Q0U111, QX = Q(115, 100)*qBZ(aSi), sqrt(Q(15, 100)**2 + 2)*qBZ(aSi), qBZ(aSi)
rows = [("Si G=0 (2nd class on axis)", Q0Si, ExSi, MSi, None), ("Si G=(-2,0,0) on-axis Umklapp (allowed), q >= q_X", Q0U200, ExSi, MSi, QX),
        ("Si G=(-1,1,1) (allowed)", Q0U111, ExSi, MSi, None), ("Ge L, G=0 (allowed)", Q0Ge, ExGe, MGe, None),
        ("Ge L, G=0, M/2 (sensitivity)", Q0Ge, ExGe, MGe/2, None), ("Si G=0, M/2 (sensitivity)", Q0Si, ExSi, MSi/2, None)]
out = {}
for lab, Q0v, Exv, Mv, qmn in rows:
    Qst, mt, Ek = thr(Q0v, Exv, Mv, qmn); out[lab] = sp.N(mt/10**6)
    print(f"   C9 {lab:52s}: |Q0| = {N3(Q0v/1000)} keV, pinned {N3(pin(Q0v, Exv)/10**6)} MeV -> min_q {N3(mt/10**6)} MeV "
          f"at |q| = {N3(Qst/1000)} keV (pair offset {N3(Ek)} eV, dq/q_BZ = {N3((Q0v - Qst)/qBZ(aSi if 'Si' in lab else aGe))})")
floorSi, floorGe = 2*ExSi/vm**2/10**6, 2*ExGe/vm**2/10**6
print(f"   C9 floors 2E_x/v_max^2: Si {N3(floorSi)} MeV, Ge {N3(floorGe)} MeV;  M_Si = {N3(MSi/me)} m_e, M_Ge = {N3(MGe/me)} m_e")
rep("WP1v3-C9d pinned values reproduce v2 (0.472 / 0.594 (2-00) / 0.708 / 0.420 MeV)",
    [round(float(sp.N(pin(a, b)/10**6)), 3) for a, b in [(Q0Si, ExSi), (Q0U200, ExSi), (Q0U111, ExSi), (Q0Ge, ExGe)]] == [0.472, 0.594, 0.708, 0.42])
rep("WP1v3-C9e min_q (parabolic [E]): Si 2nd class ~0.42, Si allowed ~0.54, Ge L ~0.32 MeV; all above the floors",
    abs(out[rows[0][0]] - 0.42) < 0.01 and abs(out[rows[1][0]] - 0.54) < 0.01 and abs(out[rows[3][0]] - 0.32) < 0.01
    and out[rows[3][0]] > floorGe and out[rows[0][0]] > floorSi)
EdirGe, mcG = Q(889, 1000) - Q(14, 10000), Q(38, 1000)          # Ge direct exciton; Gamma CB mass [UNVERIFIED inputs]
MG = (mcG + hhGe111)*me
QG, mG, EkG = thr(0, EdirGe, MG)
print(f"   C9 Ge Gamma (direct, M = {N3(MG/me)} m_e, heaviest hh): max_q(qv - q^2/2M) = M v^2/2 = {N3(MG*vm**2/2)} eV vs E = {N3(EdirGe)} eV;"
      f" min_q m = {N3(mG/10**6)} MeV at q = {N3(QG/1000)} keV (flat-band bound 2E/v^2 = {N3(2*EdirGe/vm**2/10**6)} MeV)")
qg = symbols('q_g', positive=True); mL = thr(Q0Ge, ExGe, MGe)[1]
Mreq = qg**2/(2*(qg*vm - qg**2/(2*mL) - EdirGe))               # Gamma-pair mass needed to open below the Ge L onset
qreq = [r for r in sp.solve(sp.diff(Mreq, qg), qg) if r.is_real and r > 0][0]
print(f"   C9 Ge Gamma undercuts the L onset ({N3(mL/10**6)} MeV) only if the Gamma-pair mass is >= {N3(Mreq.subs(qg, qreq)/me)} m_e at q = {N3(qreq/1000)} keV")
rep("WP1v3-C9f Ge Gamma channel: flat bound 0.253 MeV is not an onset; parabolic bands give > 2 MeV; undercut needs M >= 2 m_e",
    abs(sp.N(2*EdirGe/vm**2/10**6) - 0.253) < 0.002 and sp.N(mG/10**6) > 2 and sp.N(Mreq.subs(qg, qreq)/me) > 2)
# C9g: forbidden-class ZPL vs PAER, pointwise ratio R(eps) [E] (§3.7): R = (l_b/a_x)^2 (eps+E_b)/(3E_b) S_F(eps) sqrt(eps/eps_PA)/eta_PA
Ebs, axs = Q(147, 10000), Q(49, 1)                               # Si: E_x^b, a_x = 4.9 nm (Angstrom)
def Rpt(epsv, lb, eta, off=Q(19, 100)):
    zz = sqrt(Ebs/epsv); SFv = 2*pi*zz/(1 - exp(-2*pi*zz))
    return (lb/axs)**2*(epsv + Ebs)/(3*Ebs)*SFv*sqrt(epsv/(off + epsv))/eta
grid = [(e_, [N3(Rpt(e_, lb, eta)) for lb, eta in [(1, Q(1, 100)), (2, Q(1, 300)), (3, Q(1, 1000))]]) for e_ in [Q(1, 1000), Ebs, Q(1, 10), Q(5, 10)]]
for e_, vals in grid: print(f"   C9g R(eps_ex = {N3(e_)} eV) for (l_b, eta_PA) = (1 A, 1e-2), (2 A, 3e-3), (3 A, 1e-3): {vals}")
Rlo, Rhi = Rpt(Q(1, 10), 1, Q(1, 100)), Rpt(Q(1, 10), 3, Q(1, 1000))
rep("WP1v3-C9g forbidden ZPL / PAER at eps_ex = 0.1 eV spans O(0.1)..O(10^2) [E]: PAER not guaranteed to lead", Rlo < 1 < Rhi, f"{N3(Rlo)}..{N3(Rhi)}")

# ------------------------------------------------ C10: selection rules with the nonsymmorphic phases (§3.2 (c))
mats = []
for perm in itertools.permutations(range(3)):
    for sgn in itertools.product([1, -1], repeat=3):
        Mm = sp.zeros(3)
        for i in range(3): Mm[i, perm[i]] = sgn[i]
        mats.append(Mm)
tet = [Matrix(v) for v in [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]]
inTd = lambda Mm: all(any((Mm*v - w_).norm() == 0 for w_ in tet) for v in tet)
tau = Matrix([1, 1, 1])/4                                       # atom origin; {R|tau} for R in O_h \ T_d (units a_lat)
X_, Y_, Z_ = symbols('X Y Z'); Xv = Matrix([X_, Y_, Z_]); G25 = [Y_*Z_, Z_*X_, X_*Y_]
def chiT2g(Mm):
    r_ = Mm.inv()*Xv; tr = 0
    for i, fb in enumerate(G25):
        gfun = sp.expand(fb.subs({X_: r_[0], Y_: r_[1], Z_: r_[2]}, simultaneous=True))
        tr += sp.Poly(gfun, X_, Y_, Z_).coeff_monomial(G25[i])
    return tr
def mult(qdir, kdir, G):            # multiplicity of the trivial rep in e^{-iG.t} x Gamma25' x (A1 final state) over {g: Rq=q, Rk=k}
    ops = [Mm for Mm in mats if (Mm*qdir - qdir).norm() == 0 and (Mm*kdir - kdir).norm() == 0]
    s = sum(chiT2g(Mm)*exp(-2*pi*I*(G.T*(sp.zeros(3, 1) if inTd(Mm) else tau))[0]) for Mm in ops)
    return sp.nsimplify(s/len(ops)), len(ops)
ex = Matrix([1, 0, 0]); e111 = Matrix([1, 1, 1])
mSi0, nops = mult(ex, ex, sp.zeros(3, 1)); mU200, _ = mult(ex, ex, Matrix([-2, 0, 0]))
mU111, n111 = mult(Matrix([-Q(15, 100), 1, 1]), ex, Matrix([-1, 1, 1]))
mGe0, _ = mult(e111, e111, sp.zeros(3, 1)); mGeU, _ = mult(e111, e111, Matrix([-1, -1, -1]))
rep("WP1v3-C10a Si G=0, q||[100], full C4v with tau phases: Delta1 multiplicity 0 (forbidden; phases cancel at G=0)", mSi0 == 0 and nops == 8)
rep("WP1v3-C10b Ge G=0 and G=(-1,-1,-1), q||[111] (C3v, all pure): Lambda1/L1 multiplicity 1 (allowed)", mGe0 == 1 and mGeU == 1)
rep("WP1v3-C10c Si G=(-2,0,0), q = (-1.15,0,0) 2pi/a: e^{-iG.tau} = -1 on C4, sigma_v -> multiplicity 1 (ALLOWED, REF-A)", mU200 == 1)
rep("WP1v3-C10d Si G=(-1,1,1), q off-axis (group {E, sigma_yz}): allowed", mU111 >= 1 and n111 == 2, f"mult {mU111}")
phase_flip = [sp.nsimplify(exp(-2*pi*I*(Matrix([2, 0, 0]).T*tau)[0]))]
rep("WP1v3-C10e relabelling k -> k+(200) multiplies tau-elements by -1: Delta1 <-> Delta2' (X-point band sticking)", phase_flip == [-1])

# ------------------------------------------------ C11: multipoles of S in cubic crystals (§6.1)
chi = lambda l, ang: sp.simplify(sum(exp(I*mm*ang) for mm in range(-l, l + 1)).rewrite(cos))
def n_inv_O(l):  return sp.nsimplify((chi(l, 0) + 8*chi(l, 2*pi/3) + 3*chi(l, pi) + 6*chi(l, pi/2) + 6*chi(l, pi))/24)
def n_inv_Oh(l): return sp.nsimplify(n_inv_O(l)*(1 + (-1)**l)/2)
def n_inv_Td(l): return sp.nsimplify((chi(l, 0) + 8*chi(l, 2*pi/3) + 3*chi(l, pi) + (-1)**l*(6*chi(l, pi/2) + 6*chi(l, pi)))/24)
Oh = [n_inv_Oh(l) for l in range(9)]; Td = [n_inv_Td(l) for l in range(9)]
Td_TR = [Td[l] if l % 2 == 0 else 0 for l in range(9)]
rep("WP1v3-C11a O_h (Si, Ge) invariant harmonics l=0..8: [1,0,0,0,1,0,1,0,1]", Oh == [1, 0, 0, 0, 1, 0, 1, 0, 1], str(Oh))
rep("WP1v3-C11b T_d (GaAs): l=3 invariant (xyz) exists; removed by TR; l=2 absent", Td[3] == 1 and Td[2] == 0 and
    Td_TR == [1, 0, 0, 0, 1, 0, 1, 0, 1], str(Td))

# ------------------------------------------------ C12: rate dictionaries [E12], L2, L11
Om, S_, eps2, alpha, mel, mu, rhoT, rhoc, mc, sig_e, eta_, F2, E_ = symbols(
    'Omega S eps2 alpha m_e mu rho_T rho_chi m_chi sigma_e eta F2 E', positive=True)
e2v = 4*pi*alpha; fcr = Om*q**3*S_/(4*pi*alpha*mel**2)
rep("WP1v3-C12a [E12] Omega q^3 S/(4 pi alpha m_e^2) = Omega q^5 eps2/(8 pi^2 alpha^2 m_e^2) with S = 2q^2 eps2/e^2",
    is0(fcr.subs(S_, 2*q**2*eps2/e2v) - Om*q**5*eps2/(8*pi**2*alpha**2*mel**2)))
integrand17 = (rhoc/mc)*(1/(rhoT*Om))*sig_e*alpha*(mel**2/mu**2)*(1/q)*(E_/q)*eta_*F2*fcr/E_
integrand92 = rhoc*sig_e/(4*pi*mc*rhoT*mu**2)*q*eta_*F2*S_
rep("WP1v3-C12b 1509.01598 Eq. (17) with [E12] = WP0-v2 (9.2) integrand (spin 2, eta/2q)", is0(integrand17 - integrand92))
rep("WP1v3-C12c L2: 2q^2/e^2 = q^2/(2 pi alpha)  (2101.08275 Eq. (6))", is0(2*q**2/e2v - q**2/(2*pi*alpha)))
echi, Lf = symbols('e_chi L', positive=True)
lhs = (1/(2*pi)**3)*(echi**2*e2v/q**4)*(2*q**2/e2v)*Lf
rep("WP1v3-C12d L11: |V|^2 = e_chi^2 e^2/q^4 gives (alpha_chi/pi^2) d^3q L/q^2, alpha_chi = e_chi^2/4pi (2002.06937 Eq. (13))",
    is0(lhs - (echi**2/(4*pi))/pi**2*Lf/q**2))
lr = sp.log(Q(5000)/Q(166))/sp.log(Q(1900)/Q(166))
rep("WP1v3-C12e 2002.06937 Eq. (14) log measure: ln(5 keV/q_min)/ln(1.9 keV/q_min) ~ 1.4 at v = 0.1 (not (5/1.9)^2 = 6.9)",
    abs(sp.N(lr) - Q(14, 10)) < Q(5, 100), f"= {N3(lr)}")

print(f"\n{sum(RES)}/{len(RES)} PASS")
