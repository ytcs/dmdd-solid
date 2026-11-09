"""WP1 identity and number checks (theory support only; no simulation). Run: python3 checks.py  (< 30 s)
Each check prints PASS/FAIL or the number quoted in returns/R5/WP1.md."""
import itertools, math
import numpy as np
import sympy as sp

ok = lambda c, name: print(("PASS " if c else "FAIL ") + name)

# ---------- C1: continuity with j = 1/2{p/m, e^{iqx}}  (WP0 defect D1) ----------
x, q, m = sp.symbols('x q m', real=True, positive=True)
f = sp.Function('f')(x)
p = lambda g: -sp.I * sp.diff(g, x)
n = lambda g: sp.exp(sp.I * q * x) * g
T = lambda g: p(p(g)) / (2 * m)
j = lambda g: (p(n(g)) + n(p(g))) / (2 * m)
lhs = sp.simplify(T(n(f)) - n(T(f)))            # [T, n] f
ok(sp.simplify(lhs - q * j(f)) == 0, "C1 [T,n]=q.j exactly (no extra q^2/2m n term)")
# Catena overlap f_vec = <e^{iqx} (i d/dx)/m> = -(j - q n/2m): q.f_vec = -(dE - q^2/2m) f
fvec = lambda g: n(sp.I * sp.diff(g, x)) / m
ok(sp.simplify(q * fvec(f) + q * j(f) - q**2 / (2 * m) * n(f)) == 0,
   "C1b q.f_vec = -(q.j - q^2/2m n)  => W2=-(dE-q^2/2m)W1/m, W4=(dE-q^2/2m)^2 W1/m^2")

# ---------- C2: relativistic f-sum: only p^4 (mass-velocity) contributes ----------
px, py, pz, qx, qy, qz = sp.symbols('px py pz qx qy qz', real=True)
P = sp.Matrix([px, py, pz]); Q = sp.Matrix([qx, qy, qz])
p2 = lambda v: (v.T * v)[0]
dd = sp.expand(p2(P + Q)**2 + p2(P - Q)**2 - 2 * p2(P)**2)   # <[n+,[p^4,n]]> kernel
ok(sp.simplify(dd - 2 * (2 * p2(P) * p2(Q) + p2(Q)**2 + 4 * (P.T * Q)[0]**2)) == 0, "C2 p^4 double commutator")
# linear-in-p operators (SOC sigma.(gradV x p)) : A(p+q)+A(p-q)-2A(p) = 0 for A linear
a1, a2, a3 = sp.symbols('a1:4')
A = lambda v: a1 * v[0] + a2 * v[1] + a3 * v[2]
ok(sp.expand(A(P + Q) + A(P - Q) - 2 * A(P)) == 0, "C2b SOC/linear-in-p terms give zero f-sum shift")
# isotropic average: -(1/8m^3)*dd / (q^2/m) -> -(5/6) p^2/m^2 = -(5/3) T/m
th = sp.symbols('th'); pp, qq = sp.symbols('pp qq', positive=True)
avg = sp.integrate((2 * (2 * pp**2 * qq**2 + qq**4 + 4 * pp**2 * qq**2 * sp.cos(th)**2)) * sp.sin(th), (th, 0, sp.pi)) / 2
rel = sp.limit(sp.simplify(-avg / (8 * m**3) / (qq**2 / m)), qq, 0)
ok(sp.simplify(rel + sp.Rational(5, 6) * pp**2 / m**2) == 0, "C2c delta_rel = -(5/6)<p^2>/m^2 = -(5/3)<T>/m (q->0)")
for Z, nm in [(14, 'Si 1s'), (32, 'Ge 1s')]:
    print(f"   (Z alpha)^2 {nm} = {(Z/137.036)**2:.4f}")
print(f"   Ge 3d SO split/binding = {0.58/29.5:.3f};  all-electron f-sum shift Si,Ge ~ "
      f"{-5/3*289*27.211/14/511e3:.4f}, {-5/3*2075*27.211/32/511e3:.4f}")

# ---------- C3: static RPA+LFE: 0 < (eps^-1)_00 <= 1  (WP0 O5) ----------
rng = np.random.default_rng(1); good = True
for _ in range(2000):
    N = rng.integers(2, 12); B = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    R0 = -(B @ B.conj().T) * rng.uniform(0.01, 5)          # static KS response: Hermitian NSD
    v = np.diag(rng.uniform(0.1, 10, N))
    eps = np.eye(N) - v @ R0; ei = np.linalg.inv(eps)[0, 0]
    good &= (ei.real > 0) and (ei.real <= 1 + 1e-12) and abs(ei.imag) < 1e-9
ok(good, "C3 RPA+LFE static: 0 < (eps^-1)_00 <= 1, i.e. eps_M(q,0) >= 1 (2000 random NSD R0)")
# dynamic: Im R = B ImR0 B^dag with B = 1 + R v  (amplitude weights of WP0 7.2)
N = 6; B = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N)); H = B @ B.conj().T
R0 = -H + 1j * (-(lambda C: C @ C.conj().T)(rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N))))
R0 = (R0 + R0.T) / 2                                       # TR+inversion: complex symmetric
v = np.diag(rng.uniform(0.5, 3, N)); R = np.linalg.solve(np.eye(N) - R0 @ v, R0)
Bm = np.eye(N) + R @ v
lhs = (R - R.conj().T) / 2j; rhs = Bm @ ((R0 - R0.conj().T) / 2j) @ Bm.conj().T
ok(np.allclose(lhs, rhs), "C3b anti-Hermitian part: Im R = (1+Rv) Im R0 (1+Rv)^dag")
epsinv = np.eye(N) + v @ R
ok(np.allclose(Bm[0, :], epsinv[:, 0]), "C3c weight (1+Rv)_{0G} = (eps^-1)_{G0} when R symmetric (Si/Ge)")

# ---------- C4: plasmon pole weight (small-q Lindhard/RPA expansion) ----------
w, wp, vF, k = sp.symbols('w w_p v_F k', positive=True)
eps1 = 1 - wp**2 / w**2 - sp.Rational(3, 5) * wp**2 * k**2 * vF**2 / w**4
wpl = sp.sqrt(wp**2 + sp.Rational(3, 5) * k**2 * vF**2)          # zero to O(k^2)
frac = sp.series(sp.simplify((2 * wpl / (wp**2 * sp.diff(eps1, w))).subs(w, wpl)), k, 0, 3).removeO()
print("   C4 plasmon share of f-sum  F(k) =", sp.simplify(frac))
# Si HEG numbers
a0 = 0.529177; aSi = 5.431; ne = 32 / aSi**3                        # per A^3
rs = (3 / (4 * math.pi * ne))**(1 / 3) / a0; kF = (3 * math.pi**2 * ne)**(1 / 3)
hc = 1973.27; me = 510999.0
wp_ = math.sqrt(4 * math.pi * ne * 14.3996)  # e^2 = 14.3996 eV A ; omega_p = sqrt(4 pi n e^2 hbar^2 / m)
wp_ = math.sqrt(4 * math.pi * ne * 14.3996 * hc**2 / me)
vF_ = kF * hc / me
qc = (-vF_ + math.sqrt(vF_**2 + 4 * wp_ / (2 * me))) / (2 / (2 * me))  # wp = q vF + q^2/2m
print(f"   Si HEG: r_s={rs:.2f}, k_F={kF:.2f} 1/A = {kF*hc/1e3:.2f} keV, w_p={wp_:.1f} eV, v_F={vF_:.2e}, "
      f"q_c(Landau onset)={qc/1e3:.2f} keV, w_p/v_F={wp_/vF_/1e3:.2f} keV, 2pi/a={2*math.pi/aSi*hc/1e3:.2f} keV")
vmax = (544 + 250) / 299792.458
print(f"   halo q needed for w_p: q >= w_p/v_max = {wp_/vmax/1e3:.1f} keV  (> q_c: no bulk plasmon from halo DM)")

# ---------- C5: Elliott/Sommerfeld numbers ----------
x8 = (6 * math.pi * float(sp.zeta(3)))**(2 / 3)
print(f"   C5 bound-exciton weight = free continuum weight within {x8:.2f} E_b of the edge")
for E in [1, 10, 30, 100]:
    s = 2 * math.pi / math.sqrt(E); print(f"   Sommerfeld factor at (w-E_min)={E:>3} E_b : {s/(1-math.exp(-s)):.2f}")

# ---------- C6: indirect-exciton kinematic thresholds ----------
def mmin(qvec_frac, a, Ex):
    qv = np.linalg.norm(qvec_frac) * 2 * math.pi / a * hc         # eV
    return qv, qv**2 / (2 * (qv * vmax - Ex)) if qv * vmax > Ex else float('inf')
for lab, qf, a, Ex in [("Si G=0   (forbidden, q||Delta)", [0.85, 0, 0], 5.431, 1.170 - 0.0147),
                       ("Si G=111 (allowed)", [0.85 - 1, 1, 1], 5.431, 1.170 - 0.0147),
                       ("Ge G=0   (allowed, q||Lambda)", [0.5, 0.5, 0.5], 5.658, 0.744 - 0.00415)]:
    qv, mm = mmin(np.array(qf), a, Ex)
    print(f"   C6 {lab}: |q|={qv/1e3:.2f} keV, m_chi,min={mm/1e6:.3f} MeV")

# ---------- C7: point-group selection rules at the band extrema ----------
X, Y, Zc = sp.symbols('X Y Z')
def proj_A1(fun, ops):
    return sp.simplify(sum(fun.subs({X: o[0], Y: o[1], Zc: o[2]}, simultaneous=True) for o in ops) / len(ops))
C4v_x = [(X, Y, Zc), (X, -Zc, Y), (X, -Y, -Zc), (X, Zc, -Y), (X, -Y, Zc), (X, Y, -Zc), (X, Zc, Y), (X, -Zc, -Y)]
G25p = [Y * Zc, Zc * X, X * Y]                                     # Gamma_25' (T2g-like) basis
ok(all(proj_A1(g, C4v_x) == 0 for g in G25p), "C7 Si: Gamma25' has no A1 (Delta1) part under C4v(x): rho_cv(Gamma->Delta1,q||[100])=0")
C3v = [(X, Y, Zc), (Y, Zc, X), (Zc, X, Y), (Y, X, Zc), (X, Zc, Y), (Zc, Y, X)]
ok(any(proj_A1(g, C3v) != 0 for g in G25p), "C7b Ge: Gamma25' contains A1 (Lambda1) under C3v[111]: Gamma->L1 allowed")

# ---------- C8: cubic symmetry kills l=1,2 multipoles of an Oh-invariant ELF ----------
ops = []
for perm in itertools.permutations(range(3)):
    for s in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3)); [M.__setitem__((i, perm[i]), s[i]) for i in range(3)]; ops.append(M)
from scipy.special import sph_harm_y
def gavg(l, mm, vec):
    vals = []
    for M in ops:
        u = M @ vec; th_ = math.acos(u[2]); ph_ = math.atan2(u[1], u[0])
        vals.append(sph_harm_y(l, mm, th_, ph_))
    return np.mean(vals)
vecs = rng.normal(size=(20, 3)); vecs /= np.linalg.norm(vecs, axis=1)[:, None]
mx = {l: max(abs(gavg(l, mm, v)) for v in vecs for mm in range(-l, l + 1)) for l in [1, 2, 3, 4]}
ok(mx[1] < 1e-12 and mx[2] < 1e-12 and mx[3] < 1e-12 and mx[4] > 1e-3,
   f"C8 Oh: no invariant for l=1,2,3; l=4 present (max |avg| = {mx[4]:.3f})")
