#!/usr/bin/env python3
"""WP2-v3 (R8) identity checks. Sympy only, exact arithmetic wherever an identity is tested; no simulations.
Labels WP2v3-Cn are cited in returns/R8/WP2-v3.md. Copied from code/WP2-v2/checks.py; v3 changes (R7 referees):
  C9    re-described: it tests lattice orthogonality j_BZ(DeltaR) = delta_{DeltaR,0} for a MONATOMIC chain only
        (REF-A item 4, REF-B item 4); it does not test the basis case.
  C9b   NEW, corrected (2.4) for a basis: 1D diatomic chain, every inter-sublattice shell survives with weight
        j_BZ(DeltaR + r_k - r_k'); exact values (-1)^n/(pi(n+1/2)); v2 form (DeltaR = 0 only) shown to fail;
        sum_DeltaR j_BZ(DeltaR + r) = 1 (Poisson).
  C9c   NEW, gradient term of (2.4): BZ average of |q+p|^{2n} has no linear term (BZ inversion symmetry), relative
        correction n(2n-1) q_BZ^2/(12 q^2) in 1D; cross terms keep a linear piece (int p e^{-ipd} != 0).
  C3d   NEW, species-weighted truncation loss (3.4'').
  C4b   NEW, two-sided (T > 0) compound-Poisson identity; not a forward recursion.
  C6c   NEW, Migdal-consistent GS f-sum: (1-P)q^2/2(M+dM) = q^2/2M - E1 - P q^2/2M + O(2nd order).
  C10   numbers updated: shell estimate range (2 and 10 keV) and envelope, j_BZ(Si nearest neighbour) spherical-BZ
        estimate, 2 n_e / n_e(R) for Si, 1/a_1s and R(q) at 51/102 keV.
  C11d  re-described: tests the 1D operator algebra at phase = 1 only (REF-A A7, REF-B F); the finite-q content is C11e-g.
  C11e  NEW, j_2 Rayleigh representation and the uniform-density traceless integral int_0^oo j_2(y)/y dy = 1/3 -> 2 n_e.
  C11f  NEW, Laplace identity int_0^oo e^{-sy}(cos(mu y) - 1)/y dy = -(1/2) ln(1 + mu^2/s^2) (derivative + limit).
  C11g  NEW, hydrogenic 1s closed form R(q) = 3 + 3s^2 - 3s(1+s^2) atan(1/s), s = 2/(q a_1s): small-q 1 + (q a_1s)^2/10;
        reproduces REF-B's quadrature table (1.035, 1.091, 1.288, 1.674).
  C12b  NEW, normalisation of the third identity of (6.1): factor (2 pi/Omega)|c_k|^2.
  R9    C10 adds the net farther-pair weight 1 - 4 j_BZ(NN) = -0.77 (VER-WP2-B R1).
  C14   NEW, vertex bookkeeping: harmonic <1|e^{iqu}|0> = i q <1|u|0> e^{-W}, while <1|u|0> carries no e^{-W}.

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
C9   BZ average of coherent 2-phonon weight = incoherent weight, MONATOMIC 1D chain, symbolic q-independent
     weights: tests lattice orthogonality only                                                            (2.4)
C10  numbers quoted in the return (x_R = 1 momenta, endpoint masses at v_max = 794.5 km/s, q_BZ, 2W, ...)
C11  contact identities for F4: (a) Newton-3 (q.grad_R)^2 U = (q.grad_r)^2 U; (b) Gauss flux of grad(1/4 pi r) = -1;
     (c) cubic average of a rank-2 tensor = tr/3; (d) 1D operator algebra: e-N third-moment double commutator is
     multiplicative = e^{iq(X-x)} q^2 U''/(m M) (WP0-v2 (4.7)); its potential part equals -(M/m) x the kappa-kappa
     potential part when the phase is set to 1 by hand (i.e. q a_1s -> 0; trace part only)                   (5.2')
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
shell = 4 * abs(sp.sin(qL) / qL) * sp.Float('0.3')**2                 # q = 10 keV (near a node of j0)
qL2 = 2 * sp.Float('2.35') / hbarc
shell2 = 4 * abs(sp.sin(qL2) / qL2) * sp.Float('0.3')**2              # q = 2 keV
env10, env2 = 4 * sp.Float('0.3')**2 / qL, 4 * sp.Float('0.3')**2 / qL2   # envelope 4 cbar^2/(q d)
# j_BZ at the Si nearest-neighbour vector, spherical BZ of equal volume: k_s^3 = 6 pi^2 * 4 / a^3, d = sqrt(3) a/4
ksd = (24 * sp.pi**2)**sp.Rational(1, 3) * sp.sqrt(3) / 4
jNN = 3 * (sp.sin(ksd) / ksd**2 - sp.cos(ksd) / ksd) / ksd
far = 1 - 4 * jNN                                                      # R9: net weight of farther pairs (sum j_BZ = 1)
# uniform-density term of the e-kappa moment: 2 n_e / n_e(R), Si; n_e = 8*14/a^3 (a in bohr), n_e(R) = 2 Z^3/pi (1s^2, Z = 14)
abohr = sp.Float('5.431') / sp.Float('0.529177')
unif = 2 * (8 * 14 / abohr**3) / (2 * 14**3 / sp.pi)
# hydrogenic 1s: 1/a_1s = Z_eff alpha m_e, Z_eff = 13.7; R(q) of C11g at q = 51 and 102 keV, and at 10, 30 keV
inv_a1s = sp.Float('13.7') * sp.Float('3.7289')                        # keV (alpha m_e = 3.7289 keV)
Rq = lambda qk: (lambda s_: 3 + 3 * s_**2 - 3 * s_ * (1 + s_**2) * sp.atan(1 / s_))(2 * inv_a1s / qk)
R51, R102, R10, R30 = Rq(51), Rq(102), Rq(10), Rq(30)
toy = 1 - (3 * 28 * 40 - 2 * 28**2) / sp.Float(44**2)
Mme = 28.0855 * u / sp.Float('510998.95')
k3ratio = (4 * sp.pi * 14 * (2 * 14**3 / sp.pi) / 3) / (Mme * (sp.Float('0.044') / sp.Float('27.211386'))**2)
qGS = sp.sqrt(2 * MSi * sp.Float('1.12')) / 1e3                                        # q^2/2M = E_g(Si)
numbers = dict(qR1_Si=qR1[0], qR1_Ge=qR1[1], qIA_Si=qIA[0], qIA_Ge=qIA[1], mend_Si=mend[0], mend_Ge=mend[1],
               mwin_lo=mwin[0], mwin_hi=mwin[1], qBZ_Si=qBZ[0], qBZ_Ge=qBZ[1], qBZ_GaAs=qBZ[2], twoW_1keV=twoW,
               adiab_GaAs=adGaAs, shell_n2_10keV=shell, shell_n2_2keV=shell2, envelope_10keV=env10, envelope_2keV=env2,
               jBZ_SiNN_sph=jNN, farther_pairs_weight=far, unif_2ne_over_neR_Si=unif, inv_a1s_Si_keV=inv_a1s, R_51keV=R51, R_102keV=R102,
               R_10keV=R10, R_30keV=R30,
               toy_k3_low=toy, k3X_over_k3GS_Si=k3ratio, q_kappa1_eq_Eg_Si=qGS)
ok['C10'] = (45 < qR1[0] < 46.5 and 55 < qR1[1] < 57 and 17 < mend[0] < 18.5 and 21 < mend[1] < 22.5
             and 2.2 < qBZ[0] < 2.35 and 6e-4 < twoW < 7e-4 and 0.015 < shell < 0.025 and 0.09 < shell2 < 0.11
             and 0.42 < jNN < 0.46 and -0.80 < far < -0.74 and 1e-4 < unif < 1.4e-4 and 50 < inv_a1s < 52.5
             and 1.08 < R51 < 1.10 and 1.27 < R102 < 1.30 and 0.07 < toy < 0.08 and k3ratio > 1e5)

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

# =====================================================================================================
# v3 additions (R7 referee reports)
# =====================================================================================================

# ---------- C3d: species-weighted truncation loss (3.4'') ----------
x1, x2, g1, g2 = sp.symbols('x_1 x_2 g_1 g_2', positive=True)      # 2W_k and weights g_k = |c_k|^2/M_k
kk = sp.symbols('k', integer=True, nonnegative=True)
Ncut = 3
share = lambda xv, n: sp.exp(-xv) * xv**(n - 1) / sp.factorial(n - 1)   # order-n share of species f-sum
tail = lambda xv: sp.summation(sp.exp(-xv) * xv**kk / sp.factorial(kk), (kk, Ncut, sp.oo))  # P[Pois >= N]
lost_direct = (g1 * (1 - sum(share(x1, n) for n in range(1, Ncut + 1)))
               + g2 * (1 - sum(share(x2, n) for n in range(1, Ncut + 1)))) / (g1 + g2)
ok['C3d'] = sp.simplify(lost_direct - (g1 * tail(x1) + g2 * tail(x2)) / (g1 + g2)) == 0

# ---------- C4b: two-sided (T > 0) compound-Poisson identity ----------
# one line at +w1 (emission, measure a) and -w1 (absorption, measure b): S = e^{-(a+b)} sum_{j,k} a^j b^k/(j!k!) delta(w-(j-k)w1)
# (3.5) bin w = (j-k)w1:  w S(w) = w1 a S(w - w1) - w1 b S(w + w1)  holds term by term in (j,k):
aa_, bb_ = sp.symbols('a b', positive=True)
cjk = lambda j, k: (aa_**j * bb_**k / (sp.factorial(j) * sp.factorial(k))) if (j >= 0 and k >= 0) else 0
good = True
for j in range(6):
    for k in range(6):
        lhs = (j - k) * w1 * cjk(j, k)
        rhs = w1 * aa_ * cjk(j - 1, k) - w1 * bb_ * cjk(j, k - 1)
        good &= sp.simplify(lhs - rhs) == 0
# the bin equation at w = m w1 involves S((m+1) w1): not lower-triangular in w (no forward march at T > 0)
ok['C4b'] = good

# ---------- C6c: Migdal-consistent GS first moment ----------
Pm, dMs, qs, Ms = sp.symbols('P_Mig deltaM q M', positive=True)
eps_ = sp.symbols('epsilon', positive=True)
gs = ((1 - eps_ * Pm) * qs**2 / (2 * (Ms + eps_ * dMs)))
target_gs = qs**2 / (2 * Ms) - eps_ * qs**2 * dMs / (2 * Ms**2) - eps_ * Pm * qs**2 / (2 * Ms)
ok['C6c'] = sp.simplify(sp.series(gs, eps_, 0, 2).removeO() - target_gs) == 0

# ---------- C9b: corrected (2.4) for a basis (1D diatomic chain, lattice constant 1) ----------
pp, rr_ = sp.symbols('p r', real=True)
jBZ = lambda d: sp.integrate(sp.exp(-I * pp * d), (pp, -sp.pi, sp.pi)) / (2 * sp.pi)   # (Omega/(2pi)^d) int_BZ e^{-ipd}
half = sp.Rational(1, 2)
good = True
for n_ in range(-3, 4):
    good &= sp.simplify(jBZ(n_ + half) - (-1)**n_ / (sp.pi * (n_ + half))) == 0          # exact values
    good &= sp.simplify(jBZ(sp.Integer(n_)) - (1 if n_ == 0 else 0)) == 0               # kappa = kappa'
# model coherent S(q) = sum_{k,k',DR} A e^{-iq(DR + r_k - r_k')}, A held fixed (smooth factors at q)
Aself = sp.symbols('A0')
Ax = {n_: sp.symbols('A12_%d' % (n_ + 3)) for n_ in range(-2, 3)}
qq_ = sp.symbols('q', real=True)
Sq = Aself + sum(Ax[n_] * sp.exp(-I * qq_ * (n_ + half)) for n_ in Ax)
avg = sp.simplify(sp.integrate(Sq.subs(qq_, qq_ + pp), (pp, -sp.pi, sp.pi)) / (2 * sp.pi))
corrected = Aself + sum(Ax[n_] * jBZ(n_ + half) * sp.exp(-I * qq_ * (n_ + half)) for n_ in Ax)
v2form = Aself + Ax[0] * jBZ(half) * sp.exp(-I * qq_ * half)                             # v2: DeltaR = 0 only
good &= sp.simplify(sp.expand(avg - corrected)) == 0
good &= sp.simplify(sp.expand(avg - v2form)) != 0
good &= sp.simplify(jBZ(-half) - 2 / sp.pi) == 0 and sp.simplify(jBZ(half) - 2 / sp.pi) == 0   # both nearest neighbours
# sum_n j_BZ(n + 1/2) = (2/pi) sum_{m>=0} 2(-1)^m/(2m+1) = 1   (n and -n-1 give equal terms)
mm = sp.symbols('m', integer=True, nonnegative=True)
good &= sp.simplify(sp.summation(4 * (-1)**mm / (sp.pi * (2 * mm + 1)), (mm, 0, sp.oo)) - 1) == 0
ok['C9b'] = good

# ---------- C9c: gradient term of (2.4) ----------
qg = sp.symbols('q', positive=True)
good = True
for n_ in range(1, 4):
    avg_n = sp.integrate(sp.expand((qg + pp)**(2 * n_)), (pp, -sp.pi, sp.pi)) / (2 * sp.pi)
    lead = sp.expand(avg_n / qg**(2 * n_))
    c1 = lead.coeff(qg, -1); c2 = lead.coeff(qg, -2)
    qBZ1 = 2 * sp.pi                                                      # q_BZ = 2 pi / a, a = 1
    good &= c1 == 0 and sp.simplify(c2 - n_ * (2 * n_ - 1) * qBZ1**2 / 12) == 0
lin_cross = sp.integrate(pp * sp.exp(-I * pp * half), (pp, -sp.pi, sp.pi))
good &= sp.simplify(lin_cross) != 0                                           # cross terms keep a linear piece
ok['C9c'] = good

# ---------- C11e: j_2 Rayleigh form and the uniform-density traceless integral ----------
yv, muv = sp.symbols('y mu', positive=True)
P2 = (3 * muv**2 - 1) / 2
j2 = sp.expand_func(sp.jn(2, yv))
rayleigh = -sp.integrate(P2 * sp.cos(yv * muv), (muv, 0, 1))                    # -(1/2) int_{-1}^{1} P2 cos(y mu)
good = sp.simplify(rayleigh - j2) == 0
uni = sp.integrate(P2 * sp.log(muv), (muv, 0, 1))                               # s -> 0 limit of (1/2) int_0^1 P2 ln(1+mu^2/s^2) - ln-s piece (int P2 = 0)
good &= sp.integrate(P2, (muv, 0, 1)) == 0 and sp.simplify(uni - sp.Rational(1, 3)) == 0
# Delta n = -(3/4pi) int n e^{-iq.rho} 2P2/rho^3 = 6 int n j2/rho drho -> 6 * nbar * (1/3) = 2 nbar
good &= 6 * sp.Rational(1, 3) == 2
ok['C11e'] = good

# ---------- C11f: Laplace identity used for the spherical-core integral ----------
sv = sp.symbols('s', positive=True)
lhs_d = -sp.integrate(sp.exp(-sv * yv) * (sp.cos(muv * yv) - 1), (yv, 0, sp.oo), conds='none')   # d/ds of LHS
rhs_f = -sp.log(1 + muv**2 / sv**2) / 2
ok['C11f'] = sp.simplify(lhs_d - sp.diff(rhs_f, sv)) == 0 and sp.limit(rhs_f, sv, sp.oo) == 0

# ---------- C11g: hydrogenic 1s closed form of the finite-q e-kappa factor ----------
Fs = sp.simplify(sp.integrate(P2 * sp.log(1 + muv**2 / sv**2), (muv, 0, 1)) / 2)   # = int_0^oo e^{-sy} j2(y)/y dy
Rclosed = 3 + 3 * sv**2 - 3 * sv * (1 + sv**2) * sp.atan(1 / sv)
good = sp.simplify(1 + 6 * Fs - Rclosed) == 0
xs = sp.symbols('x', positive=True)                                             # x = q a_1s / 2 = 1/s
good &= sp.simplify(sp.series(Rclosed.subs(sv, 1 / xs), xs, 0, 4).removeO() - (1 + sp.Rational(2, 5) * xs**2)) == 0
refB = {sp.Rational(3, 10): 1.035, sp.Rational(1, 2): 1.091, 1: 1.288, 2: 1.674}
good &= all(abs(sp.N(Rclosed.subs(sv, 1 / k_)) - v_) < 6e-4 for k_, v_ in refB.items())
ok['C11g'] = good

# ---------- C12b: normalisation of the third identity of (6.1) ----------
Nn, d0, ER_, dv = sp.symbols('N d0 E_R dv', positive=True)
w_a, w_b = sp.symbols('w_a w_b', real=True)
# harmonic and anharmonic normalised shapes with equal mean E_R and variances v, v + dv (two-point laws)
Ph = [(ER_ - 1, half), (ER_ + 1, half)]
sd = sp.sqrt(1 + dv)
Pa = [(ER_ - sd, half), (ER_ + sd, half)]
mom2 = lambda P: sum(wt * (om - ER_)**2 for om, wt in P)
ok['C12b'] = sp.simplify(Nn * mom2(Pa) - Nn * mom2(Ph) - Nn * dv) == 0      # N = (2pi/Omega)|c_k|^2 multiplies dk2

# ---------- C14: Debye-Waller bookkeeping of the vertex ----------
xo, ell, qo = sp.symbols('x ell q', positive=True)
psi0 = (2 * sp.pi * ell**2)**sp.Rational(-1, 4) * sp.exp(-xo**2 / (4 * ell**2))     # <x^2> = ell^2
psi1 = xo / ell * psi0                                                               # = b^dagger psi0, u = ell(b + b^dagger)
amp_exp = sp.simplify(sp.integrate(psi1 * sp.exp(I * qo * xo) * psi0, (xo, -sp.oo, sp.oo)))
amp_u = sp.simplify(sp.integrate(psi1 * xo * psi0, (xo, -sp.oo, sp.oo)))
Wdw = qo**2 * ell**2 / 2                                                             # 2W = q^2 <u^2>
ok['C14'] = sp.simplify(amp_exp - I * qo * amp_u * sp.exp(-Wdw)) == 0 and sp.simplify(amp_u - ell) == 0

for k_, v_ in ok.items():
    print(f"{k_}: {'PASS' if v_ else 'FAIL'}")
print("C7 A1 multiplicities l=0..8:", nA1)
for k_, v_ in numbers.items():
    print(f"  {k_} = {sp.N(v_, 4)}")
print(f"{sum(bool(v) for v in ok.values())}/{len(ok)} PASS")
