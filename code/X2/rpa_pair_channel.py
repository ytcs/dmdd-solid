"""R3/X2 sympy algebra checks (exact rationals, < 10 s).

Finite 'crystal' with a conserved integer momentum label: sector 0 = {v0, c0}, sector 1 = {v1, c1}.
X raises the label by one (analogue of e^{iq.r}); the pair channel of a Q=0 phonon is the same channel X.
TDH (= RPA) with a separable Hartree kernel  dV = lam (X Tr(X^+ drho) + X^+ Tr(X drho)).
Density-matrix perturbation theory:  r_ab = F_ab (f_b - f_a)/(w - E_ab),
second order  (w_f - E_ab) s_ab = ([F1,r2] + [F2,r1])_ab + dV2_ab (f_b - f_a).
The on-shell residue N~_cv (c = c1, v = v0) is the transition amplitude (Pauli theorem built in).

Checks
 K1  rigid structure: [X, A] = c X with A anti-Hermitian, g = [A, H0]  (exact rigid translation analogue)
 K2  general X2 formula  N~ = N[phi/eps(w)] + X_cv W(w_f) T   equals brute-force self-consistent TDH
 K3  lab TDH == frame TDH for the induced density at w1+w2 (frame: X -> X(1+cu), extra -i udot A);
     the e^{iq.u} part is c u phi [chi(w_f) - chi(w)] (REF-A form, screened at w_f); remainder = Delta-v part
 K4  rigid triangle vanishes as w2 -> 0 (rigid cancellation); a generic (non-commutator) g gives
     an O(1) triangle, hence an unsuppressed pair-channel field.
 K5  scalar identity eps(w) eps(wf) [chi(w) - chi(wf)] = chi0(w) - chi0(wf)
"""
import sympy as sp

I = sp.I
w1, w2, lam, phi, u = sp.symbols('omega1 omega2 lambda phi u')
E = [sp.Rational(-1), sp.Rational(2), sp.Rational(-1, 2), sp.Rational(5, 2)]   # v0 c0 v1 c1
f = [1, 0, 1, 0]
n = 4
H0 = sp.diag(*E)
Xb = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])  # orthogonal
X = sp.zeros(4, 4); X[2:4, 0:2] = Xb
gam = sp.Rational(2, 7)
S0 = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 3)], [sp.Rational(1, 3), -sp.Rational(1, 4)]])
S1 = Xb * S0 * Xb.T - gam * sp.eye(2)
A = sp.zeros(4, 4); A[0:2, 0:2] = I * S0; A[2:4, 2:4] = I * S1
c = I * gam
assert sp.simplify(X * A - A * X - c * X) == sp.zeros(4, 4)          # K1
assert sp.simplify(A + A.H) == sp.zeros(4, 4)
g = A * H0 - H0 * A                                                  # rigid e-ph vertex, g_nn = 0


def R(F, w):
    return sp.Matrix(n, n, lambda a, b: F[a, b] * (f[b] - f[a]) / (w - E[a] + E[b]))


def chi0(w):
    return sp.simplify((X.T * R(X, w)).trace())


def tdh_lab(gvert, wf):
    e1 = 1 - lam * chi0(w1); ef = 1 - lam * chi0(wf)
    F1 = phi / e1 * X
    r1 = R(F1, w1); r2 = R(u * gvert, w2)
    N = F1 * r2 - r2 * F1 + u * gvert * r1 - r1 * u * gvert
    s0 = sp.Matrix(n, n, lambda a, b: N[a, b] / (wf - E[a] + E[b]))
    T = (X.T * s0).trace()
    return N, T, e1, ef


cv = (3, 0)
Ecv = E[3] - E[0]
wf = w1 + w2
# K2: brute-force self-consistent second-order TDH (solve for the unknown induced <X^+>_2 = y)
N, T, e1, ef = tdh_lab(g, wf)
y = sp.symbols('y')
s_full = sp.Matrix(n, n, lambda a, b: (N[a, b] + lam * X[a, b] * y * (f[b] - f[a])) / (wf - E[a] + E[b]))
ysol = sp.solve(sp.Eq(y, (X.T * s_full).trace()), y)[0]
brute = N[cv] + lam * X[cv] * ysol
formula = N[cv] + X[cv] * (lam / ef) * T
print('K2 brute - formula =', sp.simplify(brute - formula))

# K3: frame computation at the level of the induced density <X^+>_2(w_f) (valid at every w1, w2;
# a finite model has discrete pairs, so on-shell residues are degenerate: the pair channel moves the pole).
# lab:   <X^+>_2 = T/eps_f                        (T from the X2 formula, KS triangle with phi/eps(w1))
# frame: <X^+>_2^fr = [chi0_f phi c u + T']/eps_f,  T' = KS triangle of (phi X/eps(w1), B = -w2 u A)
# relation: <X^+>_lab(w_f) = <X^+>_fr(w_f) - c u <X^+>_1(w1),  <X^+>_1 = chi0(w1) phi/eps(w1)
B = -w2 * u * A
F1 = phi / e1 * X
r1 = R(F1, w1); rB = R(B, w2)
Np = F1 * rB - rB * F1 + B * r1 - r1 * B
s0p = sp.Matrix(n, n, lambda a, b: Np[a, b] / (wf - E[a] + E[b]))
Tp = (X.T * s0p).trace()
lab = T / ef
fr = (chi0(wf) * phi * c * u + Tp) / ef - c * u * chi0(w1) * phi / e1
print('K3 lab - frame =', sp.simplify(sp.together(lab - fr)))
# e^{iq.u} part of the full response: c u phi [chi(w_f) - chi(w1)], chi = chi0/eps  (REF-A form)
conv = c * u * phi * (chi0(wf) / ef - chi0(w1) / e1)
rest = sp.simplify(sp.together(lab - conv))
print('K3 remainder (intraband/Delta-v part) = Tp/eps_f ?', sp.simplify(sp.together(rest - Tp / ef)))
# the remainder vanishes linearly as w2 -> 0 (adiabatic): leading order
print('K3 remainder at w2=0:', sp.simplify((Tp / ef).subs(w2, 0)))

# K4: generic (non-commutator) g with intraband elements: KS triangle T is O(1) as w2 -> 0,
# so the pair-channel field W T is not suppressed (no rigid cancellation).
Gg = sp.Matrix([[0, sp.Rational(1, 2), 0, 0], [sp.Rational(1, 2), sp.Rational(1, 3), 0, 0],
                [0, 0, -sp.Rational(1, 5), sp.Rational(2, 3)], [0, 0, sp.Rational(2, 3), sp.Rational(1, 4)]])
Ng, Tg, _, efg = tdh_lab(Gg, wf)
Tg0 = sp.simplify((Tg * e1 / phi / u).subs(w2, 0))
print('K4 generic g: KS triangle per unit screened phi at w2=0:', Tg0, '  (rigid g gives 0 there:',
      sp.simplify((T * e1 / phi / u).subs(w2, 0)), ')')

# K5
x0, x0f, v = sp.symbols('chi0 chi0f v')
ee, eef = 1 - v * x0, 1 - v * x0f
print('K5 =', sp.simplify(ee * eef * (x0 / ee - x0f / eef) - (x0 - x0f)))
