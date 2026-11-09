#!/usr/bin/env python3
"""WP2-v2 (R6) identity checks. Sympy only, exact arithmetic wherever an identity is tested; no simulations.
Labels WP2v2-Cn are cited in returns/R6/WP2-v2.md.

C1   one polar branch: Im[-1/eps] = (pi w_L/2)(1/eps_inf - 1/eps_0) delta(w - w_L)                       (4.3)
C2   Sherman-Morrison, exact rational 3-mode model: -1/eps(z) = -1/eps_inf + (c/eps_inf^2) p^T (D_NA - z)^-1 p  (4.2)
C3   f-sum: (a) Poisson series saturates it; (b) per-phonon-order fraction e^{-x}x^{n-1}/(n-1)! at ANY T
     (two-line DOS with absorption lines, detailed balance); (c) n_B(-x) + 1 = -n_B(x)                     (3.1), (3.4)
C4   compound-Poisson (Panjer) identity, two-line DOS, coefficient-wise                                    (3.5)
C5   exact cumulants k1..k4 of S_self for an anharmonic (cubic + quartic) oscillator with exact ground state
     psi = e^{-W}; equality certified by an exact integration-by-parts polynomial Q (Q' - 2W'Q = difference) (5.1)
C6   second-derivative identity <d2V> = d2E0 + 2 sum |<n|dV|0>|^2/(En-E0) (implicit differentiation, exact);
     Migdal moments: first = q^2 dM/(2M^2) (WP3 J3), third = (q^2/2M^2)(<d2V> - d2E0)                      (5.2)
C7   cubic group O: A1 multiplicities l = 0..8 -> first anisotropic harmonic l = 4                         (8.2)
C8   free-recoil limit of WP0-v2 (3.4) reproduces hep-ph/0608035 Eq. (5)                                   (5.3)
C9   BZ average of coherent 2-phonon weight = incoherent weight (1D chain, symbolic weights)               (2.4)
C10  numbers quoted in the return (x_R = 1 momenta, endpoint masses at v_max = 794.5 km/s, q_BZ, 2W, ...)
C11  contact identities for F4: (a) Newton-3 (q.grad_R)^2 U = (q.grad_r)^2 U; (b) Gauss flux of grad(1/4 pi r) = -1;
     (c) cubic average of a rank-2 tensor = tr/3; (d) 1D operator algebra: e-N third-moment double commutator is
     multiplicative = e^{iq(X-x)} q^2 U''/(m M) (WP0-v2 (4.7)); its potential part equals -(M/m) x the kappa-kappa
     potential part at contact                                                                              (5.2')
C12  M-type nuisance does not preserve the linear constraints (6.1) between theta = 0 and 1               (6.1)
C13  phase-convention map: v1 e^{iG.r}*prod e^(x) = e^{iq.r}*prod e^(R) (CONVENTIONS 5)                     (2.2)
"""
import sympy as sp

ok = {}
I = sp.I

# ---------- C1 ----------
w, wT, wL, einf, s = sp.symbols('omega omega_T omega_L epsilon_inf s', positive=True)
m1 = -1 / (einf * (wL**2 - s) / (wT**2 - s))
res = sp.limit((s - wL**2) * m1, s, wL**2)
weight = sp.simplify(-res * sp.pi / (2 * wL))
eps0 = einf * wL**2 / wT**2
ok['C1'] = sp.simplify(weight - sp.pi * wL / 2 * (1 / einf - 1 / eps0)) == 0

# ---------- C2 ----------
z = sp.symbols('z')
DA = sp.Matrix([[5, 1, sp.Rational(1, 2)], [1, 4, -1], [sp.Rational(1, 2), -1, 6]])
p = sp.Matrix([1, -2, sp.Rational(3, 2)])
c, ei = sp.Rational(7, 10), sp.Integer(3)
Id = sp.eye(3)
epsz = ei + c * (p.T * (DA - z * Id).inv() * p)[0]
DNA = DA + (c / ei) * p * p.T
rhs = -1 / ei + (c / ei**2) * (p.T * (DNA - z * Id).inv() * p)[0]
ok['C2'] = sp.simplify(sp.together(-1 / epsz - rhs)) == 0

# ---------- C3 ----------
x, w0 = sp.symbols('x omega_0', positive=True)
nn = sp.symbols('n', integer=True, nonnegative=True)
fsum = sp.summation(nn * w0 * sp.exp(-x) * x**nn / sp.factorial(nn), (nn, 0, sp.oo))
ok['C3a'] = sp.simplify(fsum - x * w0) == 0
# (b) two phonon lines w1, w2 with DOS weights d1, d2; mu has emission lines at +w (weight (n+1)d/w) and
#     absorption lines at -w (weight n d/w); q^2/2M = 1.  Moment generating function F(t) = int mu e^{w t}.
w1, w2, d1, d2, beta, t = sp.symbols('omega_1 omega_2 d_1 d_2 beta t', positive=True)
nB = lambda e: 1 / (sp.exp(beta * e) - 1)
lines = [(w1, (nB(w1) + 1) * d1 / w1), (-w1, nB(w1) * d1 / w1), (w2, (nB(w2) + 1) * d2 / w2), (-w2, nB(w2) * d2 / w2)]
F = sum(m * sp.exp(e * t) for e, m in lines)
twoW = F.subs(t, 0)
first = sp.diff(F, t).subs(t, 0)
ok['C3b_fsum'] = sp.simplify(first - (d1 + d2)) == 0            # = q^2/2M when d1 + d2 = 1 (normalised DOS)
good = True
for n in range(1, 5):
    mom1_n = sp.diff(F**n, t).subs(t, 0)                        # int w mu^{*n}
    good &= sp.simplify(mom1_n - n * first * twoW**(n - 1)) == 0
ok['C3b_order'] = good
xx = sp.symbols('xx', positive=True)
ok['C3c'] = sp.simplify(nB(-xx) + 1 + nB(xx)) == 0

# ---------- C4 ----------
a1, a2 = sp.symbols('a_1 a_2', positive=True)
m1c, m2c = x * a1 / w1, x * a2 / w2
coef = lambda j, k: m1c**j * m2c**k / (sp.factorial(j) * sp.factorial(k))
good = True
for j in range(4):
    for k in range(4):
        if j + k == 0:
            continue
        lhs = (j * w1 + k * w2) * coef(j, k)
        rhs4 = (w1 * m1c * coef(j - 1, k) if j else 0) + (w2 * m2c * coef(j, k - 1) if k else 0)
        good &= sp.simplify(lhs - rhs4) == 0
ok['C4'] = good

# ---------- C5 ----------
X, q, M = sp.symbols('x q M', positive=True)
Wsup = sp.Rational(1, 2) * X**2 + sp.Rational(1, 5) * X**3 + sp.Rational(1, 7) * X**4   # psi = e^{-W}, E = 0
psi = sp.exp(-Wsup)
Vp = (sp.diff(Wsup, X)**2 - sp.diff(Wsup, X, 2)) / (2 * M)                               # H psi = 0
Hop = lambda g: -sp.diff(g, X, 2) / (2 * M) + Vp * g
Lop = lambda g: Hop(g) + q**2 / (2 * M) * g - I * q / M * sp.diff(g, X)              # e^{-iqx}(H-E)e^{iqx}
# moments m_k*Norm = int psi L^k psi ; integrand/psi^2:
Lk, mom = psi, {}
for k in range(1, 5):
    Lk = sp.expand(Lop(Lk))
    mom[k] = sp.expand(sp.simplify(Lk / psi))                                           # psi*L^k psi / psi^2
p2 = sp.expand(sp.simplify(-sp.diff(psi, X, 2) / psi))                                 # <p^2> density
p4 = sp.expand(sp.simplify(sp.diff(psi, X, 4) / psi))
Vpp = sp.diff(Vp, X, 2); V1 = sp.diff(Vp, X)
k1 = q**2 / (2 * M)
# predicted raw moments, written linearly in expectations (the 3<p^2>^2 of k4 cancels against 3 k2^2):
pred = {1: k1,
        2: q**2 * p2 / M**2 + k1**2,
        3: q**2 * Vpp / (2 * M**2) + 3 * (q**2 * p2 / M**2) * k1 + k1**3,
        4: q**2 * V1**2 / M**2 + q**4 * p4 / M**4 + 4 * (q**2 * Vpp / (2 * M**2)) * k1
           + 6 * (q**2 * p2 / M**2) * k1**2 + k1**4}
Wp = sp.diff(Wsup, X)
def certify(D):
    """find polynomial Q with Q' - 2W'Q = D, i.e. int e^{-2W} D = 0 exactly"""
    D = sp.expand(D)
    if D == 0:
        return True
    deg = sp.Poly(D, X).degree() - 3
    if deg < 0:
        return False
    cs = sp.symbols('c0:%d' % (deg + 1))
    Q = sum(ci * X**i for i, ci in enumerate(cs))
    eqs = sp.Poly(sp.expand(sp.diff(Q, X) - 2 * Wp * Q - D), X).all_coeffs()
    sol = sp.solve(eqs, cs, dict=True)
    return len(sol) == 1
ok['C5'] = all(certify(mom[k] - pred[k]) for k in range(1, 5))

# ---------- C6 ----------
R, E = sp.symbols('R E')
A0 = sp.diag(0, 3, sp.Rational(9, 2), 7)
B = sp.Matrix([[0, 1, -2, 1], [1, 1, 0, 3], [-2, 0, -1, 1], [1, 3, 1, 2]])
C = sp.Matrix([[2, -1, 0, 1], [-1, 0, 2, 0], [0, 2, 1, -1], [1, 0, -1, 3]])
Fc = (A0 + R * B + R**2 * C / 2 - E * sp.eye(4)).det()
FR, FE = sp.diff(Fc, R), sp.diff(Fc, E)
at = {R: 0, E: 0}
E1 = -(FR / FE).subs(at)
E2 = -((sp.diff(Fc, R, 2) + 2 * sp.diff(Fc, R, E) * E1 + sp.diff(Fc, E, 2) * E1**2) / FE).subs(at)
gaps = [A0[k, k] - A0[0, 0] for k in range(1, 4)]
sumB = sum(B[k, 0]**2 / gaps[k - 1] for k in range(1, 4))
ok['C6a'] = sp.simplify(C[0, 0] - (E2 + 2 * sumB)) == 0 and E1 == B[0, 0]
qq = sp.symbols('q', positive=True)
amp2 = [(qq / M)**2 * B[k, 0]**2 / gaps[k - 1]**4 for k in range(1, 4)]           # |Migdal amplitude|^2
dM = 2 * sum(B[k, 0]**2 / gaps[k - 1]**3 for k in range(1, 4))
mig1 = sum(a * g for a, g in zip(amp2, gaps)); mig3 = sum(a * g**3 for a, g in zip(amp2, gaps))
ok['C6b'] = sp.simplify(mig1 - qq**2 * dM / (2 * M**2)) == 0 and \
            sp.simplify(mig3 - qq**2 / (2 * M**2) * (C[0, 0] - E2)) == 0

# ---------- C7 ----------
def chi(l, th):
    return sp.Integer(2 * l + 1) if th == 0 else sp.sin((l + sp.Rational(1, 2)) * th) / sp.sin(th / 2)
classes = [(1, 0), (8, 2 * sp.pi / 3), (3, sp.pi), (6, sp.pi / 2), (6, sp.pi)]
nA1 = [sp.nsimplify(sum(m * chi(l, th) for m, th in classes) / 24) for l in range(9)]
ok['C7'] = nA1 == [1, 0, 0, 0, 1, 0, 1, 0, 1]

# ---------- C8 ----------
rho, mchi, rhoT, sig_p, mup, MN, A_, F2, eta, nN, muN = sp.symbols(
    'rho_chi m_chi rho_T sigma_p mu_p M_N A F2 eta n_N mu_N', positive=True)
V2 = sp.pi * sig_p / mup**2
integrand_q = 4 * sp.pi * qq**2 / (2 * sp.pi)**3 * V2 * 2 * sp.pi * nN * A_**2 * F2 * eta / (2 * qq)
dRdw = (rho / (mchi * rhoT) * sp.simplify(integrand_q / qq) * MN).subs(rhoT, nN * MN)  # int dq q delta(w-q^2/2M) = M
sigN = sig_p * A_**2 * muN**2 / mup**2
ok['C8'] = sp.simplify(dRdw - rho * sigN * F2 * eta / (2 * mchi * muN**2)) == 0

# ---------- C9 ----------
Nc = 7
f = sp.symbols('f1:%d' % Nc)                                  # weights 1/omega_k for k = 1..N-1 (k = 0 excluded)
def coh2(Qi):
    return sum(f[i - 1] * f[j - 1] for i in range(1, Nc) for j in range(1, Nc) if (i + j - Qi) % Nc == 0) * Nc / Nc**2
avg = sum(coh2(Qi) for Qi in range(Nc)) / Nc
ok['C9'] = sp.expand(avg - (sum(f) / Nc)**2) == 0

# ---------- C10 (numbers) ----------
u = sp.Float('931.494e6')                                     # eV per atomic mass unit
MSi, MGe = 28.0855 * u, 72.630 * u
wSi, wGe = sp.Float('0.040'), sp.Float('0.023')               # mean phonon energies [E], eV
kms = sp.Float(1) / 299792.458
vmax = (544 + sp.Float('250.5')) * kms                        # CONVENTIONS 8
qR1 = [sp.sqrt(2 * Mm * ww) / 1e3 for Mm, ww in ((MSi, wSi), (MGe, wGe))]          # keV
qIA = [2 * v for v in qR1]
mend = [qv * 1e3 / (2 * vmax) / 1e6 for qv in qIA]                                     # MeV, q_max = 2 m v_max
mwin = [10e3 / (2 * vmax) / 1e6, 100e3 / (2 * vmax) / 1e6]
hbarc = sp.Float('1.973269804')                               # keV*Angstrom
qBZ = [2 * sp.pi * hbarc / a for a in (5.431, 5.658, 5.653)]
twoW = (1 / hbarc)**2 * sp.Float('0.0025')                    # q = 1 keV, <u_x^2> = 0.0025 A^2
adGaAs = (sp.Float('0.036') / sp.Float('1.5'))**2
qL = 10 * sp.Float('2.35') / hbarc
shell = 4 * abs(sp.sin(qL) / qL) * sp.Float('0.3')**2
toy = 1 - (3 * 28 * 40 - 2 * 28**2) / sp.Float(44**2)
Mme = 28.0855 * u / sp.Float('510998.95')
k3ratio = (4 * sp.pi * 14 * (2 * 14**3 / sp.pi) / 3) / (Mme * (sp.Float('0.044') / sp.Float('27.211386'))**2)
qGS = sp.sqrt(2 * MSi * sp.Float('1.12')) / 1e3                                        # q^2/2M = E_g(Si)
numbers = dict(qR1_Si=qR1[0], qR1_Ge=qR1[1], qIA_Si=qIA[0], qIA_Ge=qIA[1], mend_Si=mend[0], mend_Ge=mend[1],
               mwin_lo=mwin[0], mwin_hi=mwin[1], qBZ_Si=qBZ[0], qBZ_Ge=qBZ[1], qBZ_GaAs=qBZ[2], twoW_1keV=twoW,
               adiab_GaAs=adGaAs, shell_n2=shell, toy_k3_low=toy, k3X_over_k3GS_Si=k3ratio, q_kappa1_eq_Eg_Si=qGS)
ok['C10'] = (45 < qR1[0] < 46.5 and 55 < qR1[1] < 57 and 17 < mend[0] < 18.5 and 21 < mend[1] < 22.5
             and 2.2 < qBZ[0] < 2.35 and 6e-4 < twoW < 7e-4 and shell < 0.03 and 0.07 < toy < 0.08 and k3ratio > 1e5)

# ---------- C11 ----------
r1, r2, r3, R1, R2, R3, Z, e = sp.symbols('r1 r2 r3 R1 R2 R3 Z e', real=True)
q1, q2, q3 = sp.symbols('q1 q2 q3', real=True)
dist = sp.sqrt((r1 - R1)**2 + (r2 - R2)**2 + (r3 - R3)**2)
U = Z * e**2 / (4 * sp.pi * dist)
qgrad = lambda g, v: q1 * sp.diff(g, v[0]) + q2 * sp.diff(g, v[1]) + q3 * sp.diff(g, v[2])
rv, Rv = (r1, r2, r3), (R1, R2, R3)
ok['C11a'] = sp.simplify(qgrad(qgrad(U, Rv), Rv) - qgrad(qgrad(U, rv), rv)) == 0
rr, th, ph = sp.symbols('rr theta phi', positive=True)
flux = sp.integrate(sp.integrate(sp.diff(1 / (4 * sp.pi * rr), rr) * rr**2 * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi))
ok['C11b'] = sp.simplify(flux + 1) == 0
Tm = sp.Matrix(3, 3, lambda i, j: sp.Symbol('T%d%d' % (min(i, j), max(i, j))))
gens = [sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]]), sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])]
group = {sp.ImmutableMatrix(sp.eye(3))}
while True:
    new = {sp.ImmutableMatrix(g * h) for g in group for h in gens} | group
    if new == group:
        break
    group = new
avgT = sum((g * Tm * g.T for g in group), sp.zeros(3)) / len(group)
ok['C11c'] = len(group) == 24 and sp.simplify(avgT - Tm.trace() / 3 * sp.eye(3)) == sp.zeros(3)
# (d) 1D: H = p^2/2m + P^2/2M - U(x - X)
xe, XN, me, MM, qd = sp.symbols('x X m M q', positive=True)
fu, Uf = sp.Function('f'), sp.Function('U')
g0 = fu(xe, XN)
Hd = lambda g: -sp.diff(g, xe, 2) / (2 * me) - sp.diff(g, XN, 2) / (2 * MM) - Uf(xe - XN) * g
mul = lambda h: (lambda g: h * g)
comm = lambda A, Bo: (lambda g: A(Bo(g)) - Bo(A(g)))
ne_d, nN, nN_d = mul(sp.exp(-I * qd * xe)), mul(sp.exp(I * qd * XN)), mul(sp.exp(-I * qd * XN))
Ceκ = sp.simplify(comm(comm(ne_d, Hd), comm(Hd, comm(Hd, nN)))(g0) / g0)
Uxx = sp.diff(Uf(xe - XN), xe, 2)
target = sp.exp(I * qd * (XN - xe)) * qd**2 * Uxx / (me * MM)
ok['C11d_eN'] = sp.simplify(sp.expand(Ceκ - target)) == 0
Cκκ = sp.expand(sp.simplify(comm(comm(nN_d, Hd), comm(Hd, comm(Hd, nN)))(g0) / g0))
U2 = sp.Subs(sp.Derivative(Uf(sp.Symbol('_xi_1')), (sp.Symbol('_xi_1'), 2)), sp.Symbol('_xi_1'), xe - XN)
pot_kk = sp.simplify(sum(tm for tm in Cκκ.as_ordered_terms() if tm.has(sp.Derivative) and tm.has(Uf)
                         and not tm.has(I)))     # Hermitian U'' part; the i q^3 U' part is anti-Hermitian
# contact: phase -> 1; compare the U'' parts
ok['C11d_ratio'] = sp.simplify(pot_kk / target.subs(sp.exp(I * qd * (XN - xe)), 1) + me / MM) == 0

# ---------- C12 ----------
aa, thv = sp.symbols('a theta', positive=True)
tot = (1 + aa)**thv + (1 - aa)**thv                           # S = (1,1), Delta = (a,-a): int Delta = 0
ok['C12'] = tot.subs(thv, 0) == 2 and sp.simplify(tot.subs(thv, 1)) == 2 and \
            sp.N((tot.subs({thv: sp.Rational(1, 2), aa: sp.Rational(1, 2)}))) < 2

# ---------- C13 ----------
Q1, Q2, G, rk, qv = sp.symbols('Q1 Q2 G r_k q', real=True)
s1, s2 = 1, -1                                                # one emission, one absorption
ex1, ex2 = sp.symbols('ex1 ex2')                              # x-convention polarisation components
# e^(R)(Q) = e^(x)(Q) e^{iQ r}; emission uses e*, absorption uses e
eR = lambda ex, Qv: ex * sp.exp(I * Qv * rk)
v1 = sp.exp(I * G * rk) * sp.conjugate(ex1) * ex2             # v1: e^{iG r} e^(x)*(Q1) e^(x)(Q2)
v2 = sp.exp(I * qv * rk) * sp.conjugate(eR(ex1, Q1)) * eR(ex2, Q2)
ok['C13'] = sp.simplify((v2 - v1).subs(qv, s1 * Q1 + s2 * Q2 + G)) == 0

for k_, v_ in ok.items():
    print(f"{k_}: {'PASS' if v_ else 'FAIL'}")
print("C7 A1 multiplicities l=0..8:", nA1)
for k_, v_ in numbers.items():
    print(f"  {k_} = {sp.N(v_, 4)}")
print(f"{sum(bool(v) for v in ok.values())}/{len(ok)} PASS")
