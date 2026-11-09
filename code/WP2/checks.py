#!/usr/bin/env python3
"""WP2 (R5) identity checks. Theory support only: no simulations, all checks < 1 min.

C1  single-oscillator LO pole: Im[-1/eps] = (pi wL/2)(1/eps_inf - 1/eps_0) delta(w - wL)          (WP2 eq 4.3)
C2  multi-mode Sherman-Morrison: residues of -1/eps(w) at the LO zeros = |p.e_lambda^NA|^2/(eps_inf^2 2 w_lambda) (WP2 eq 4.2)
C3  Einstein incoherent: f-sum saturated by the all-n Poisson series; 1-phonon without DW also saturates it   (WP2 eq 3.4)
C4  compound-Poisson (Panjer) identity  w S(w) = int dw' w' mu(w') S(w - w')  for a 2-line DOS, to O(x^4)   (WP2 eq 3.5)
C5  exact cumulants of a 1D anharmonic oscillator S(q,w): k1 = q^2/2M, k2 = q^2<p^2>/M^2,
    k3 = q^2<V''>/(2M^2), k4 = q^2<V'^2>/M^2 + q^4(<p^4>-3<p^2>^2)/M^4                                  (WP2 eq 6.1)
C6  second-derivative identity <d2V> = d2E0 + 2 sum_n |<n|dV|0>|^2/(En-E0)  (G/X split of k3)             (WP2 eq 6.2)
C7  cubic group O: number of A1 copies in l = 0..8  -> lowest anisotropic harmonic is l = 4                 (WP2 eq 8.2)
C8  free-recoil limit of WP0 (3.4) reproduces hep-ph/0608035 eq (5)                                         (WP2 eq 5.3)
C9  1D monatomic chain (N sites): BZ-average over q of the coherent 2-phonon weight = incoherent weight     (WP2 eq 2.3)
"""
import numpy as np
import sympy as sp

ok = {}

# ---------- C1 ----------
w, wT, wL, einf = sp.symbols('omega omega_T omega_L epsilon_inf', positive=True)
eps = einf * (wL**2 - w**2) / (wT**2 - w**2)
# residue of -1/eps in w^2 at w^2 = wL^2 gives Im part pi*Res*delta(w^2-wL^2) = pi*Res/(2wL) delta(w-wL)
s = sp.symbols('s')  # s = w^2
m1 = sp.simplify(-1 / eps.subs(w**2, s))
m1 = sp.simplify(-1 / (einf * (wL**2 - s) / (wT**2 - s)))
res = sp.limit((s - wL**2) * m1, s, wL**2)        # -1/eps ~ res/(s - wL^2) ; Im[1/(wL^2 - s - i0)] = pi delta
weight = sp.simplify(-res * sp.pi / (2 * wL))      # coefficient of delta(w - wL)
eps0 = einf * wL**2 / wT**2                        # LST
target = sp.pi * wL / 2 * (1 / einf - 1 / eps0)
ok['C1'] = sp.simplify(weight - target) == 0

# ---------- C2 ----------
rng = np.random.default_rng(1)
n = 6
A = rng.normal(size=(n, n)); DA = A @ A.T + n * np.eye(n)        # analytic dynamical matrix (mass-weighted), PD
p = rng.normal(size=n)                                           # mode-charge vector  (q.Z*_k)/sqrt(M_k)
c, einf_n = 0.7, 3.0                                             # c = e^2/Omega
DNA = DA + (c / einf_n) * np.outer(p, p)
lam, U = np.linalg.eigh(DNA)
wTs, UT = np.linalg.eigh(DA)
def minv_eps(z):  # -1/eps(z), z = w^2 (complex)
    e = einf_n + c * sum((p @ UT[:, i])**2 / (wTs[i] - z) for i in range(n))
    return -1.0 / e
# residue at each LO zero z = lam_k : compare with  (c/einf^2)|p.U_k|^2
resid = []
for k in range(n):
    h = 1e-6 * lam[k]
    r = 0.5 * (minv_eps(lam[k] + h) * h + minv_eps(lam[k] - h) * (-h))  # ~ Res of -1/eps in z
    resid.append(abs(-r - (c / einf_n**2) * (p @ U[:, k])**2) / ((c / einf_n**2) * (p @ U[:, k])**2 + 1e-30))
ok['C2'] = max(resid) < 1e-4

# ---------- C3 ----------
x, w0 = sp.symbols('x omega_0', positive=True)
nn = sp.symbols('n', integer=True, nonnegative=True)
fsum = sp.summation(nn * w0 * sp.exp(-x) * x**nn / sp.factorial(nn), (nn, 0, sp.oo))
ok['C3a'] = sp.simplify(fsum - x * w0) == 0                       # = q^2/2M since x w0 = q^2/2M
ok['C3b'] = sp.simplify(w0 * x - x * w0) == 0                     # 1-phonon, no DW: w0 * (x) exactly (trivial identity)

# ---------- C4 ----------
# DOS = two lines at w1, w2 with weights a1, a2 (mu(w') = x*(a1 delta(w'-w1)/w1 + a2 delta(w'-w2)/w2) ),
# S(w) = e^{-2W} sum_{j,k} c_{jk} delta(w - j w1 - k w2). Check the identity coefficient-wise.
w1, w2, a1, a2 = sp.symbols('omega_1 omega_2 a_1 a_2', positive=True)
m1c, m2c = x * a1 / w1, x * a2 / w2                               # line strengths of mu
def coef(j, k):  # compound Poisson coefficient of delta(w - j w1 - k w2) (e^{-2W} dropped)
    return m1c**j * m2c**k / (sp.factorial(j) * sp.factorial(k))
good = True
for j in range(0, 4):
    for k in range(0, 4):
        if j + k == 0:
            continue
        lhs = (j * w1 + k * w2) * coef(j, k)
        rhs = (w1 * m1c * coef(j - 1, k) if j > 0 else 0) + (w2 * m2c * coef(j, k - 1) if k > 0 else 0)
        good &= sp.simplify(lhs - rhs) == 0
ok['C4'] = good

# ---------- C5 ----------
M, W0, lam3, lam4, q = 1.0, 1.0, 0.04, 0.004, 1.7
Nb = 160
a = np.diag(np.sqrt(np.arange(1, Nb)), 1)
X = (a + a.T) / np.sqrt(2 * M * W0); P = 1j * np.sqrt(M * W0 / 2) * (a.T - a)
y = np.sqrt(2 * M * W0) * X
V = 0.5 * M * W0**2 * X @ X + lam3 * W0 * np.linalg.matrix_power(y, 3) + lam4 * W0 * np.linalg.matrix_power(y, 4)
H = P @ P / (2 * M) + V
E, Ev = np.linalg.eigh(H)
g = Ev[:, 0]
# exp(iqX) in the eigenbasis
xe, xv = np.linalg.eigh(X)
eiqx = xv @ np.diag(np.exp(1j * q * xe)) @ xv.conj().T
amp = Ev.conj().T @ eiqx @ g
keep = slice(0, 70)                                                 # well-converged low states
wts = np.abs(amp[keep])**2; om = E[keep] - E[0]
Z = wts.sum()
mom = [np.sum(wts * om**k) / Z for k in range(5)]
k1 = mom[1]; k2 = mom[2] - mom[1]**2
k3 = mom[3] - 3 * mom[2] * mom[1] + 2 * mom[1]**3
k4 = mom[4] - 4 * mom[3] * mom[1] - 3 * mom[2]**2 + 12 * mom[2] * mom[1]**2 - 6 * mom[1]**4
ex = lambda O: np.real(g.conj() @ O @ g)
Vp = M * W0**2 * X + 3 * lam3 * W0 * np.sqrt(2 * M * W0) * (y @ y) + 4 * lam4 * W0 * np.sqrt(2 * M * W0) * np.linalg.matrix_power(y, 3)
Vpp = M * W0**2 * np.eye(Nb) + 6 * lam3 * W0 * (2 * M * W0) * y + 12 * lam4 * W0 * (2 * M * W0) * (y @ y)
p2, p4 = ex(P @ P), ex(np.linalg.matrix_power(P, 4))
pred = [q**2 / (2 * M), q**2 * p2 / M**2, q**2 * ex(Vpp) / (2 * M**2),
        q**2 * ex(Vp @ Vp) / M**2 + q**4 * (p4 - 3 * p2**2) / M**4]
rel = [abs(c_ - p_) / abs(p_) for c_, p_ in zip([k1, k2, k3, k4], pred)]
ok['C5'] = max(rel) < 2e-3 and abs(Z - 1) < 1e-6

# ---------- C6 ----------
B = rng.normal(size=(4, 4)); B = B + B.T
C = rng.normal(size=(4, 4)); C = C + C.T
A0 = np.diag([0.0, 3.0, 4.5, 7.0])
def E0(R):
    return np.linalg.eigvalsh(A0 + R * B + 0.5 * R**2 * C)[0]
h = 1e-4
d2E = (E0(h) - 2 * E0(0) + E0(-h)) / h**2
e, v = np.linalg.eigh(A0)
dV, d2V = B, C
lhs = v[:, 0] @ d2V @ v[:, 0]
rhs = d2E + 2 * sum((v[:, k] @ dV @ v[:, 0])**2 / (e[k] - e[0]) for k in range(1, 4))
ok['C6'] = abs(lhs - rhs) < 1e-5

# ---------- C7 ----------
# characters of SO(3) irrep l restricted to O (24 elements): classes E(1), C3(8), C2 face(3), C4(6), C2 edge(6)
def chi(l, th):
    return sp.Integer(2 * l + 1) if th == 0 else sp.sin((l + sp.Rational(1, 2)) * th) / sp.sin(th / 2)
classes = [(1, 0), (8, 2 * sp.pi / 3), (3, sp.pi), (6, sp.pi / 2), (6, sp.pi)]
nA1 = [sp.nsimplify(sum(m * chi(l, th) for m, th in classes) / 24) for l in range(9)]
ok['C7'] = nA1 == [1, 0, 0, 0, 1, 0, 1, 0, 1]       # O: invariants at l=0,4,6,8 (xyz is A2 of O; odd l excluded anyway by S(q)=S(-q))

# ---------- C8 ----------
rho, mchi, rhoT, sig_p, mup, MN, A_, F2, eta, nN = sp.symbols('rho_chi m_chi rho_T sigma_p mu_p M_N A F2 eta n_N', positive=True)
qq, om_ = sp.symbols('q omega', positive=True)
V2 = sp.pi * sig_p / mup**2                                        # |V_p|^2  (WP0 2.3 normalisation, nucleon)
# dR/dw = rho/(m rhoT) * int 4pi q^2 dq/(2pi)^3 * V2 * [2 pi n_N A^2 F2 delta(w - q^2/2M)] * eta/(2q)
integrand_q = 4 * sp.pi * qq**2 / (2 * sp.pi)**3 * V2 * 2 * sp.pi * nN * A_**2 * F2 * eta / (2 * qq)
# int dq q * delta(w - q^2/2M) -> M  ;  so replace q*delta by M:
dRdw = rho / (mchi * rhoT) * sp.simplify(integrand_q / qq) * MN
dRdw = dRdw.subs(rhoT, nN * MN)
muN = sp.symbols('mu_N', positive=True)
sigN = sig_p * A_**2 * muN**2 / mup**2
target = rho * sigN * F2 * eta / (2 * mchi * muN**2)                # hep-ph/0608035 eq (5)
ok['C8'] = sp.simplify(dRdw - target) == 0

# ---------- C9 ----------
N = 12
ks = 2 * np.pi * np.arange(1, N) / N                               # exclude k=0 translation
wk = 2 * np.abs(np.sin(ks / 2))
# coherent 2-phonon weight at lattice momentum Q (mod 2pi): sum over k1,k2 with k1+k2 = Q  of 1/(w1 w2) * N/N^2
def coh2(Qi):
    tot = 0.0
    for i1, k1 in enumerate(ks):
        for i2, k2 in enumerate(ks):
            if (np.arange(1, N)[i1] + np.arange(1, N)[i2] - Qi) % N == 0:
                tot += 1.0 / (wk[i1] * wk[i2])
    return tot * N / N**2
inc2 = (np.sum(1 / wk) / N)**2
avg = np.mean([coh2(Qi) for Qi in range(N)])
ok['C9'] = abs(avg - inc2) < 1e-12

for k_, v_ in ok.items():
    print(f"{k_}: {'PASS' if v_ else 'FAIL'}")
print("C5 relative errors k1..k4:", ["%.1e" % r for r in rel])
print("C7 A1 multiplicities l=0..8:", nA1)
