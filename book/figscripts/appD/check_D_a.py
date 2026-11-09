"""Numerical checks of the closed forms and numbers quoted in Appendix D.4, D.5, D.8 and D.9.

Run: python check_D_a.py   (asserts every check; prints the quoted numbers)
Units: natural units, energies in eV. Constants: CODATA 2018 (alpha, m_e, hbar*c).
Silicon valence density n_e = 2.00e23 cm^-3 (four valence electrons per atom; App. A.2 of the book).
"""
import numpy as np
from scipy import integrate

alpha = 1 / 137.035999084
m_e = 510998.950          # eV
hbarc_cm = 1.973269804e-5  # eV cm
Ry = alpha**2 * m_e / 2    # 13.6057 eV
a0 = 1 / (alpha * m_e)     # eV^-1

# ---------- silicon valence electron gas (D.4, D.5) ----------
n_e = 2.00e23 * hbarc_cm**3            # eV^3
kF = (3 * np.pi**2 * n_e) ** (1 / 3)   # eV
EF = kF**2 / (2 * m_e)
vF = kF / m_e
rs = (3 / (4 * np.pi * n_e)) ** (1 / 3) / a0
print(f"kF = {kF/1e3:.3f} keV, EF = {EF:.2f} eV, vF = {vF:.2e}, rs = {rs:.3f}")
assert abs(kF / 1e3 - 3.57) < 0.005 and abs(EF - 12.5) < 0.05

e2 = 4 * np.pi * alpha                 # Heaviside-Lorentz

def FL(y):
    y = np.asarray(y, float)
    return 0.5 + (1 - y**2) / (4 * y) * np.log(np.abs((1 + y) / (1 - y)))

# exchange self-energy Sigma_x(k) = -int d^3p/(2pi)^3 e^2/|k-p|^2, p < kF  (D.4)
def sigma_x_num(k):
    f = lambda p: -(e2 / (4 * np.pi**2)) / k * p * np.log(abs((k + p) / (k - p)))
    val, _ = integrate.quad(f, 0, kF, points=[k] if k < kF else None, limit=200)
    return val
for x in [0.1, 0.5, 0.9, 1.0 + 1e-9, 1.5, 3.0]:
    k = x * kF
    closed = -(e2 * kF / (2 * np.pi**2)) * FL(x)
    assert abs(sigma_x_num(k) / closed - 1) < 1e-6, (x, sigma_x_num(k), closed)
# mean of F over the Fermi sphere = 3/4
avgF, _ = integrate.quad(lambda x: 3 * x**2 * FL(x), 0, 1, points=[1.0])
assert abs(avgF - 0.75) < 1e-8
Ex = -3 * alpha * kF / (4 * np.pi)           # exchange energy per electron
print(f"E_x/N = {Ex:.3f} eV = {Ex/Ry:.4f} Ry; -0.916/rs Ry = {-0.9163/rs*Ry:.3f} eV")
assert abs(Ex / Ry * rs + 0.91633) < 1e-4
width_shift = alpha * kF / np.pi           # e^2 kF/(4 pi^2) = Sigma_x(kF) - Sigma_x(0)
print(f"HF widening of the occupied band = {width_shift:.2f} eV; HF band width = {EF+width_shift:.1f} eV")
vx_KS = -e2 * kF / (4 * np.pi**2)          # LDA exchange potential (4/3) eps_x = Sigma_x(kF)
assert abs(vx_KS - (4 / 3) * Ex) < 1e-9 and abs(vx_KS + width_shift) < 1e-9
print(f"v_x(LDA) = Sigma_x(kF) = {vx_KS:.2f} eV, Slater 3/2 of it = {1.5*vx_KS:.2f} eV, Sigma_x(0) = {2*vx_KS:.2f} eV")
# HF group velocity diverges logarithmically at kF: dF/dx -> (1/2) ln|1-x| + const
sl = [(FL(1 - d) - FL(1 - 2 * d)) / d for d in [1e-3, 1e-5, 1e-7]]
assert abs((sl[1] - sl[0]) - 0.5 * np.log(1e-2)) < 0.05 and abs((sl[2] - sl[1]) - 0.5 * np.log(1e-2)) < 0.05

# ---------- Lindhard function at T = 0 (D.8); units m = kF = 1 ----------
def Ianti(w):
    return w + 0.5 * (1 - w**2) * np.log((w + 1) / (w - 1))
# antiderivative check: I(w) = int_0^1 kappa ln((w+kappa)/(w-kappa)) dkappa, complex w in UHP
for w in [0.3 + 0.2j, 2.0 + 0.01j, -0.7 + 0.5j, 5 + 1j]:
    re, _ = integrate.quad(lambda t: (t * np.log((w + t) / (w - t))).real, 0, 1)
    im, _ = integrate.quad(lambda t: (t * np.log((w + t) / (w - t))).imag, 0, 1)
    assert abs(re + 1j * im - Ianti(w)) < 1e-8, w

NF = 1 / (2 * np.pi**2)   # one spin, m = kF = 1
def R0(q, z):
    """closed form, complex z in the upper half plane (z = omega/ (units E with m=kF=1))"""
    nu = z / q
    y = q / 2
    return (1 / (2 * np.pi**2 * q)) * (Ianti(nu - y) - Ianti(nu + y))

def R0_direct(q, z):
    def f(u, k, part):
        D = k * q * u + q**2 / 2
        val = (2 * 2 * np.pi / (2 * np.pi) ** 3) * k**2 * (1 / (z - D) - 1 / (z + D))
        return val.real if part == 0 else val.imag
    re, _ = integrate.dblquad(lambda u, k: f(u, k, 0), 0, 1, -1, 1)
    im, _ = integrate.dblquad(lambda u, k: f(u, k, 1), 0, 1, -1, 1)
    return re + 1j * im
for q, z in [(0.5, 0.3 + 0.2j), (1.2, 1.0 + 0.3j), (3.0, 4.0 + 0.5j), (0.2, 0.05 + 0.1j)]:
    assert abs(R0(q, z) / R0_direct(q, z) - 1) < 1e-6, (q, z)
# the printed form of Eq. (D.8-Rz): -2 N_F {1/2 + (kF/4q)[(1-nu+^2) l(nu+) - (1-nu-^2) l(nu-)]}
def R0_printed(q, z):
    nu = z / q; y = q / 2
    l = lambda w: np.log((w + 1) / (w - 1))
    npl, nmi = nu + y, nu - y
    return -2 * NF * (0.5 + (1 / (4 * q)) * ((1 - npl**2) * l(npl) - (1 - nmi**2) * l(nmi)))
for q, z in [(0.5, 0.3 + 0.2j), (1.2, 1.0 + 1e-9j), (3.0, 4.0 + 0.5j), (0.2, 0.15 + 1e-9j)]:
    assert abs(R0_printed(q, z) - R0(q, z)) < 1e-10 * max(1, abs(R0(q, z))), (q, z)
# static limit
for q in [0.1, 1.0, 1.9, 2.0 + 1e-9, 3.0]:
    assert abs(R0(q, 0 + 1e-12j).real + 2 * NF * FL(q / 2)) < 1e-9
# imaginary part on the real axis = -S0/2 of the book's Eq. (4.2-gas)
def S0(q, w):
    kmin = max(abs(w / q - q / 2), np.sqrt(max(1 - 2 * w, 0)))
    return (1 / (2 * np.pi * q)) * (1 - kmin**2) if kmin < 1 else 0.0
for q in [0.3, 1.0, 1.7, 2.5]:
    for w in np.linspace(0.01, q + q**2 / 2 + 0.3, 13):
        assert abs(R0(q, w + 1e-12j).imag + S0(q, w) / 2) < 1e-9, (q, w)
# large-frequency expansion and f-sum
n = 1 / (3 * np.pi**2)
for q in [0.1, 0.3]:
    w = 20 * q
    lead = n * q**2 / w**2
    corr = (0.6 * q**2 + (q**2 / 2) ** 2) / w**2
    r = R0(q, w + 1e-12j).real / lead
    assert abs(r - 1 - corr) < 3 * corr**2 + 1e-12, (q, r, corr)
for q in [0.4, 1.0, 2.5]:
    top = q + q**2 / 2
    val, _ = integrate.quad(lambda w: w * R0(q, w + 1e-13j).imag, 0, top, limit=200,
                            points=[max(q - q**2 / 2, 1e-9)] if q < 2 else None)
    assert abs(val / (-np.pi * n * q**2 / 2) - 1) < 1e-6, (q, val)

# ---------- Mermin (D.9) ----------
def Rmer(q, w, g):
    r1 = R0(q, w + 1j * g)
    r0 = R0(q, 0 + 1e-14j).real
    return (1 + 1j * g / w) * r1 / (1 + (1j * g / w) * r1 / r0)
g = 0.05
# the printed epsilon form, Eq. (D.9-eps), equals 1 - v_C R^Mer (v_C = e^2/q^2, here with e^2 = 1)
for q, w in [(0.3, 0.2), (1.0, 0.7), (1.5, 2.0)]:
    vC = 1 / q**2
    eL = lambda z: 1 - vC * R0(q, z)
    epsM = 1 + (1 + 1j * g / w) * (eL(w + 1j * g) - 1) / (1 + (1j * g / w) * (eL(w + 1j * g) - 1) / (eL(1e-14j) - 1))
    assert abs(epsM - (1 - vC * Rmer(q, w, g))) < 1e-10, (q, w)
for q in [0.3, 1.0]:
    assert abs(Rmer(q, 1e-7, g) - R0(q, 1e-14j).real) < 1e-5            # static limit
    assert abs(R0(q, 1j * g).real - R0(q, 1e-14j).real) > 1e-3          # bare substitution misses it
# q -> 0: Drude n q^2/(m w (w + i g))
q = 1e-3
for w in [0.05, 0.2]:
    drude = n * q**2 / (w * (w + 1j * g))
    assert abs(Rmer(q, w, g) / drude - 1) < 1e-3, w
# perfect screening: q^2 R(q, 0) -> finite for Mermin (eps ~ 1 + kTF^2/q^2), -> 0 for bare substitution
for q in [1e-2, 1e-3]:
    assert abs(Rmer(q, 1e-9, g).real + 2 * NF) < 1e-3
    assert abs(R0(q, 1j * g).real) < 2 * n * q**2 / g**2
# f-sum on both: int_0^inf w Im R dw = -pi n q^2 / 2 (m = 1); integrate in pieces out to w = 16384
edges = [1e-9, 0.5, 1, 2, 4, 8, 16, 64, 256, 1024, 4096, 16384]
import warnings
warnings.filterwarnings("ignore", category=integrate.IntegrationWarning)
for q in [0.5, 1.5]:
    for fun in (lambda w: Rmer(q, w, g), lambda w: R0(q, w + 1j * g)):
        val = sum(integrate.quad(lambda w: w * fun(w).imag, a, b, limit=500)[0]
                  for a, b in zip(edges[:-1], edges[1:]))
        assert abs(val / (-np.pi * n * q**2 / 2) - 1) < 1e-4, (q, val)
print("all D.4/D.5/D.8/D.9 checks passed")
