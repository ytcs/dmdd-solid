"""Numerical checks of the derivations and numbers quoted in Appendix D.12, D.13, D.14 and D.15.

Run: python check_D_b.py   (asserts every check; prints the quoted numbers)
Units: natural units, energies in eV unless a model is dimensionless.
Constants: CODATA 2018 (alpha, m_e, Bohr radius); natural-abundance M = 28.0855 u for the kappa_BO values of Sect. 5.1
and for the D.13 text (Sects. 5.3, C.6).
"""
import itertools
import numpy as np
from scipy import integrate
import sympy as sp

rng = np.random.default_rng(7)

# ---------------------------------------------------------------- D.12
# Exact diagonalization of four spin-orbitals (two occupied, two empty, each pair degenerate) with complex
# orbitals on a grid and an unscreened two-body interaction of strength lam. The resonant (Tamm-Dancoff)
# problem with Hartree-Fock energies and kernel K^x - K^d (spin-orbitals, W -> v_C) must agree with the exact
# singly excited energies to O(lam^2). Kernel definitions as eq:D.12-kernels:
#   K^x_{mn,m'n'} = v_{m n', n m'},  K^d_{mn,m'n'} = v_{m n', m' n},  v_{ab,cd} = <ab|v|cd> (physicists').
M, nso = 40, 4
X = rng.normal(size=(M, nso)) + 1j * rng.normal(size=(M, nso))
phi, _ = np.linalg.qr(X)
xg = np.linspace(-1, 1, M)
vker = 1 / np.sqrt((xg[:, None] - xg[None, :]) ** 2 + 0.3)   # real, symmetric model interaction
h = np.diag([0.0, 0.0, 1.0, 1.0]).astype(complex)            # degenerate occupied and empty pairs
occ, vir = [0, 1], [2, 3]


def V4(lam):
    A = np.einsum('xa,xc->acx', phi.conj(), phi)
    return lam * np.einsum('acx,xy,bdy->abcd', A, vker, A)


def jw_ops(n):
    I2, Z, a = np.eye(2), np.diag([1.0, -1.0]), np.array([[0.0, 1.0], [0.0, 0.0]])
    ops = []
    for p in range(n):
        m = np.array([[1.0]])
        for q in range(n):
            m = np.kron(m, Z if q < p else (a if q == p else I2))
        ops.append(m)
    return ops


c = jw_ops(nso)
cd = [o.conj().T for o in c]
Nop = sum(cd[p] @ c[p] for p in range(nso))
sector = np.where(np.isclose(np.diag(Nop).real, 2))[0]


def exact(lam):
    v = V4(lam)
    H = sum(h[p, q] * cd[p] @ c[q] for p in range(nso) for q in range(nso))
    for a, b, cc, d in itertools.product(range(nso), repeat=4):
        H = H + 0.5 * v[a, b, cc, d] * cd[a] @ cd[b] @ c[d] @ c[cc]
    E = np.linalg.eigvalsh(H[np.ix_(sector, sector)])
    return E[1:5] - E[0]


def tda(lam, sign=1, swap=False):
    v = V4(lam)
    F = h.copy()
    for p in range(nso):
        for q in range(nso):
            F[p, q] += sum(v[p, j, q, j] - v[p, j, j, q] for j in occ)
    T = [(a, i) for a in vir for i in occ]          # transition (n=i -> m=a)
    A = np.zeros((4, 4), complex)
    for I, (a, i) in enumerate(T):
        for J, (b, j) in enumerate(T):
            A[I, J] = F[a, b] * (i == j) - F[j, i] * (a == b)
            Kx = v[a, j, i, b]
            Kd = v[a, i, b, j] if swap else v[a, j, b, i]
            A[I, J] += Kx - sign * Kd
    return np.sort(np.linalg.eigvals(A).real)


for label, kw, expect in [('correct', {}, 4.0), ('K^d sign reversed', dict(sign=-1), 2.0),
                          ('hole indices exchanged', dict(swap=True), 2.0)]:
    errs = [np.max(np.abs(exact(l) - tda(l, **kw))) for l in (0.02, 0.01, 0.005)]
    ratios = [errs[i] / errs[i + 1] for i in range(2)]
    print(f"D.12 {label}: errors {errs[0]:.2e}, {errs[1]:.2e}, {errs[2]:.2e}; ratios {ratios[0]:.2f}, {ratios[1]:.2f}")
    assert all(abs(r - expect) < 0.05 for r in ratios)

# Algebra of eq:D.12-Lsol: [F(z - D) - K]^{-1} = (z - D - F K)^{-1} F for F = diag(+-1).
nr = 3
D = np.diag(rng.uniform(1, 2, 2 * nr))
Fm = np.diag([1.0] * nr + [-1.0] * nr)
Kr = rng.normal(size=(2 * nr, 2 * nr)); Kr = 0.1 * (Kr + Kr.T)
z = 0.3 + 0.7j
lhs = np.linalg.inv(Fm @ (z * np.eye(2 * nr) - D) - Kr)
rhs = np.linalg.inv(z * np.eye(2 * nr) - D - Fm @ Kr) @ Fm
assert np.allclose(lhs, rhs)
# Rank-one head separation (eq:D.12-epsmac): L^-1 = Lbar^-1 - g v rho rho^dag  =>  R00 = Rbar/(1 - v Rbar).
L0 = np.diag(1 / (z - np.diag(D)))
rho = rng.normal(size=2 * nr) + 1j * rng.normal(size=2 * nr)
Kbar = Kr
vq = 0.37
Lbar = np.linalg.inv(np.linalg.inv(L0) - Kbar)
Lfull = np.linalg.inv(np.linalg.inv(L0) - Kbar - vq * np.outer(rho, rho.conj()))
Rbar = rho.conj() @ Lbar @ rho
Rfull = rho.conj() @ Lfull @ rho
assert np.isclose(Rfull, Rbar / (1 - vq * Rbar))
assert np.isclose(1 + vq * Rfull, 1 / (1 - vq * Rbar))
# Independent-particle optical limit of eq:D.12-eps2: pi g e^2/(V q^2) |q.v/w|^2 = 8 pi^2 alpha/(Omega w^2) |qhat.v|^2/N.
alpha = 1 / 137.035999084
e2 = 4 * np.pi * alpha
assert np.isclose(np.pi * 2 * e2, 8 * np.pi**2 * alpha)
print("D.12 algebra (L solution, head separation, optical prefactor): ok")

# ---------------------------------------------------------------- D.13
m_e = 510998.950          # eV
M_Si = 28.0855 * 931.49410242e6   # eV, natural silicon
a0_A = 0.529177210903     # Angstrom
Eh = alpha**2 * m_e       # 27.211 eV
ratio = m_e / M_Si
kBO = ratio ** 0.25
print(f"D.13 M/m_e = {M_Si/m_e:.4g}; kappa_BO = {kBO:.4f}, ^2 = {kBO**2:.3e}, ^3 = {kBO**3:.3e}; "
      f"alpha^2 m_e = {Eh:.2f} eV; kappa a0 = {kBO*a0_A:.4f} A; kappa^2 alpha^2 m_e = {kBO**2*Eh:.3f} eV")
# D.13 text: natural-abundance silicon, M = 28.0855 u (as in Sect. 5.3); the kappa_BO values
# above are those of Sect. 5.1 for the same mass.
M_nat = 28.0855 * 931.49410242e6   # eV
print(f"D.13 natural Si: M = {M_nat/1e9:.4f} GeV, M/m_e = {M_nat/m_e:.4g}, sqrt(M/m_e) = {(M_nat/m_e)**0.5:.1f}")
assert abs(M_nat / 1e9 - 26.16) < 0.005
assert abs(M_nat / m_e - 5.12e4) < 0.005e4
assert abs((M_nat / m_e) ** 0.5 - 226) < 0.5
assert abs(kBO - 0.0665) < 5e-5 and abs(kBO**2 - 4.42e-3) < 5e-6 and abs(kBO**3 - 2.94e-4) < 5e-7
assert abs(kBO * a0_A - 0.035) < 5e-4 and abs(kBO**2 * Eh - 0.12) < 5e-3
# Solvable electron + nucleus model: low root of m M w^4 - [m(k+K) + M k] w^2 + k K = 0.
r, K, k = sp.symbols('r K k', positive=True)
a_, b_, c_ = r, r * (k + K) + k, k * K       # M = 1
w2 = (b_ - sp.sqrt(b_**2 - 4 * a_ * c_)) / (2 * a_)
series = sp.expand(sp.series(w2 / K, r, 0, 3).removeO())
assert sp.simplify(series - (1 - r + (1 - K / k) * r**2)) == 0
for rr, quoted in ((1e-2, 5.0e-5), (1e-3, 5.0e-7), (1e-4, 5.0e-9)):
    kk, KK = 1.0, 0.5
    aa, bb, cc_ = rr, rr * (kk + KK) + kk, kk * KK
    w2n = (bb - np.sqrt(bb * bb - 4 * aa * cc_)) / (2 * aa)
    dev = w2n / KK - (1 - rr)
    print(f"D.13 model m/M = {rr:g}: relative deviation from (K/M)(1 - m/M) = {dev:.2e}")
    assert abs(dev / quoted - 1) < 0.02
# Diagonal BO correction of the model: <d psi0/dX|d psi0/dX>/(2M) = m w_e/(4M) for a translated oscillator.
me_, we = 1.0, 1.3
xs = np.linspace(-12, 12, 20001)
psi = (me_ * we / np.pi) ** 0.25 * np.exp(-me_ * we * xs**2 / 2)
dpsi = np.gradient(psi, xs)
assert np.isclose(np.trapezoid(dpsi**2, xs), me_ * we / 2, rtol=1e-6)
print("D.13 algebra (series, diagonal correction): ok")

# ---------------------------------------------------------------- D.14
# (a) Eliminating the field equals adding the nonanalytic term, anisotropic random model.
nat = 3
Ms = rng.uniform(1, 3, nat)
Z = rng.normal(size=(nat, 3, 3)); Z -= Z.mean(axis=0)          # charge neutrality eq:D.14-neutral
eps_inf = np.eye(3) + 0.5 * (lambda A: A @ A.T)(rng.normal(size=(3, 3)))
Om = 2.0
e = np.sqrt(e2)
Cr = rng.normal(size=(3 * nat, 3 * nat)); Can = Cr @ Cr.T
# impose the acoustic sum rule: sum_k' C_kk' = 0 (rows and columns)
P = np.kron(np.eye(nat) - np.ones((nat, nat)) / nat, np.eye(3))
Can = P @ Can @ P
Qh = rng.normal(size=3); Qh /= np.linalg.norm(Qh)
ZQ = np.concatenate([Z[kk] @ Qh for kk in range(nat)])         # (Z_k . Qhat)^alpha stacked
Cna = e2 / Om * np.outer(ZQ, ZQ) / (Qh @ eps_inf @ Qh)
Mh = np.repeat(Ms, 3) ** -0.5
Dtot = Mh[:, None] * (Can + Cna) * Mh[None, :]
w2L = np.linalg.eigvalsh(Dtot)
for w2v in w2L:
    # bordered system in (u, E_par): (C - w2 M) u - e Z.Qhat E = 0 ;  (e/Om) u.Z.Qhat + Qeps Q E = 0
    Bm = np.zeros((3 * nat + 1, 3 * nat + 1))
    Bm[:3 * nat, :3 * nat] = Can - w2v * np.diag(np.repeat(Ms, 3))
    Bm[:3 * nat, -1] = -e * ZQ
    Bm[-1, :3 * nat] = e / Om * ZQ
    Bm[-1, -1] = Qh @ eps_inf @ Qh
    sv = np.linalg.svd(Bm, compute_uv=False)
    assert sv[-1] / sv[0] < 1e-10
print("D.14 field elimination = nonanalytic term: ok")
# (b) Generalized LST, cubic-like scalar model along one direction with three polar modes (4 atoms).
nat = 4
Ms = rng.uniform(1, 3, nat)
Zs = rng.normal(size=nat); Zs -= Zs.mean()
einf = 3.3
Cr = rng.normal(size=(nat, nat)); C1 = Cr @ Cr.T
Pp = np.eye(nat) - np.ones((nat, nat)) / nat
C1 = Pp @ C1 @ Pp
Mh = Ms ** -0.5
Dan = Mh[:, None] * C1 * Mh[None, :]
wT2, ev = np.linalg.eigh(Dan)
Dl = Mh[:, None] * (C1 + e2 / Om * np.outer(Zs, Zs) / einf) * Mh[None, :]
wL2 = np.linalg.eigvalsh(Dl)
zt = ev.T @ (Zs * Mh)                       # mode charges z_nu
pol = np.abs(wT2) > 1e-9                    # drop the acoustic zero mode
eps0 = einf + e2 / Om * np.sum(zt[pol] ** 2 / wT2[pol])
lst = np.prod(wL2[np.abs(wL2) > 1e-9]) / np.prod(wT2[pol])
print(f"D.14 generalized LST: eps0/einf = {eps0/einf:.12f}, prod wL^2/wT^2 = {lst:.12f}")
assert np.isclose(eps0 / einf, lst, rtol=1e-12)
# zeros of eps(w) at the LO frequencies
for w2v in wL2[np.abs(wL2) > 1e-9]:
    epsw = einf + e2 / Om * np.sum(zt[pol] ** 2 / (wT2[pol] - w2v))
    assert abs(epsw) < 1e-8
# (c) Frohlich limit of eq:D.14-gL for a cubic diatomic, eq:D.14-frohlich.
M1, M2, Zst, ei, Omc, wT = 1.7, 2.9, 1.3, 2.2, 1.9, 0.8
mu = M1 * M2 / (M1 + M2); Mc = M1 + M2
wL = np.sqrt(wT**2 + e2 * Zst**2 / (Omc * ei * mu))
e0 = ei * wL**2 / wT**2
Qm = 0.013
s = Zst * Qm * (np.sqrt(M2 / Mc) / np.sqrt(M1) + np.sqrt(M1 / Mc) / np.sqrt(M2))
g_full = e2 / Omc * s / (np.sqrt(2 * wL) * ei * Qm**2)
g_fro = np.sqrt(e2 * wL / (2 * Omc) * (1 / ei - 1 / e0)) / Qm
assert np.isclose(s, Zst * Qm / np.sqrt(mu)) and np.isclose(g_full, g_fro)
print("D.14 Frohlich limit: ok")
# (d) Hermiticity eq:A.6-herm of eq:D.14-gL with complex polarization vectors (e(-Q) = e(Q)^*) and real Z*, eps.
Zr = rng.normal(size=(2, 3, 3)); Zr -= Zr.mean(axis=0)
ev2 = rng.normal(size=(2, 3)) + 1j * rng.normal(size=(2, 3)); ev2 /= np.linalg.norm(ev2)
Qv = 0.02 * rng.normal(size=3); Ms2 = np.array([1.2, 2.3]); wq = 0.5; epsr = eps_inf
rho_mn = 0.3 - 0.4j


def gL(evec, Q, rho):
    num = sum((evec[kk] @ Zr[kk] @ Q) / np.sqrt(2 * Ms2[kk] * wq) for kk in range(2))
    return 1j * e2 / Om * num / (Q @ epsr @ Q) * rho


assert np.isclose(np.conj(gL(ev2, Qv, rho_mn)), gL(ev2.conj(), -Qv, np.conj(rho_mn)))
print("D.14 Hermiticity of g^L: ok")
# (e) polariton estimate: sqrt(eps0)*30 meV vs zone 2 pi/a, a ~ 5.6 A
hbarc_eVA = 1973.269804
print(f"D.14 polariton scale {np.sqrt(13)*0.030:.3f} eV vs 2pi/a = {2*np.pi/5.65*hbarc_eVA:.0f} eV: "
      f"ratio {np.sqrt(13)*0.030/(2*np.pi/5.65*hbarc_eVA):.1e}")

# ---------------------------------------------------------------- D.15
# Bloch identity for one mode in a truncated Fock space, complex non-Hermitian A, and the moments.
nmax, w0, beta = 120, 1.0, 0.7
dop = np.diag(np.sqrt(np.arange(1, nmax)), 1)
Hm = w0 * (np.diag(np.arange(nmax)) + 0.5)
rhoT = np.diag(np.exp(-beta * np.diag(Hm))); rhoT /= np.trace(rhoT)
nB = 1 / np.expm1(beta * w0)
from scipy.linalg import expm
for eta1, eta2 in ((0.3 + 0.2j, -0.5 + 0.1j), (0.8j, 0.8j), (0.4, 0.4)):
    A = eta1 * dop + eta2 * dop.conj().T
    lhs = np.trace(rhoT @ expm(A))
    rhs = np.exp(eta1 * eta2 * (2 * nB + 1) / 2)
    assert abs(lhs - rhs) < 1e-10, (lhs, rhs)
print("D.15 Bloch identity (truncated Fock space): ok")
# Debye model: closed form vs direct integral, high-T expansion, value at T = omega_D.
f = lambda x: x / np.expm1(x)


def bracket(t):           # t = T/omega_D
    return 1 + 4 * t**2 * integrate.quad(f, 1e-14, 1 / t)[0]


def direct(t):            # (4/9) * omega_D * M * <u^2> from the coth integral, omega_D = M = 1
    return (4 / 9) * integrate.quad(lambda w: 9 * w**2 * (1 / np.tanh(w / (2 * t))) / (2 * w), 1e-14, 1)[0]


for t in (0.05, 0.3, 1.0, 3.0):
    assert np.isclose(bracket(t), direct(t), rtol=1e-9)
print(f"D.15 Debye bracket at T = omega_D: {bracket(1.0):.3f}")
assert abs(bracket(1.0) - 4.11) < 0.005
for t in (5.0, 10.0, 20.0):
    exact_hiT = bracket(t) * 3 / 4          # 2W in units q^2/(M omega_D)
    approx = 3 * t * (1 + 1 / (36 * t**2))
    assert abs(exact_hiT / approx - 1) < 2 / t**4
print("D.15 Debye closed form and high-T expansion: ok")
print("all checks passed")
