"""Sect. 16.3, semiconducting nanotubes: checks of the one-dimensional massive-Dirac bubble and of the cylindrical-shell
Coulomb kernel, and the numbers quoted in the text.  No figure.

(1) Interband bubble of h = v k sigma_x + Delta sigma_z per unit length, T = 0, undoped (derived in Sect. 16.3):
      -Im R_1D(q, w) = 2 g v q^2 Delta^2 / [s^{3/2} (s - 4 Delta^2)^{1/2}],  s = w^2 - v^2 q^2 > 4 Delta^2,
    checked against direct integration -Im R = (g/2) int dk |<+,k+q|-,k>|^2 delta(w - e_k - e_{k+q}).
(2) Weight: int ds of 2 Delta^2/[s^{3/2}(s - 4 Delta^2)^{1/2}] = 1 (metallic limit g v q^2 delta(s)).
(3) Kernel of a charged cylindrical shell of radius r_t (Heaviside-Lorentz, e^2 = 4 pi alpha): V_1D = 2 alpha I0(q r_t) K0(q r_t);
    checked against the direct ring average of the 1D transform 2 alpha K0(q rho), rho = 2 r_t |sin(phi/2)|, and its limits
    (small q r_t: 2 alpha [ln(2/(q r_t)) - gamma_E]; large: alpha/(q r_t), the sheet kernel 2 pi alpha/q per circumference).
(4) Graphene Dirac velocity v_D = 3 t a_cc/2 with t = 2.8 eV, a_cc = 1.42 Angstrom (Castro Neto et al., arXiv:0709.1163,
    text after Eq. (5), Eq. (7) and text after it), against v_max = 2.650e-3 (eq:A.8-ref); zone-folding half-gap
    Delta_1 = v_D/(3 r_t) for a semiconducting tube.
(5) q -> 0 limit used for absorption: -Im R_1D/q^2 -> 2 g v Delta^2/(w^3 (w^2 - 4 Delta^2)^{1/2}).
Run: python nt16_3.py  (seconds)
"""
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
from scipy.special import i0, k0, k0 as K0

ALPHA = 1 / 137.035999
HBARC_EVA = 1973.269804           # eV Angstrom


def ek(k, v, D):
    return np.sqrt(v * v * k * k + D * D)


def overlap2(k, kp, v, D):
    """|<+,kp|-,k>|^2 for h = v k sx + D sz."""
    e1, e2 = ek(k, v, D), ek(kp, v, D)
    return 0.5 * (1 - (v * v * k * kp + D * D) / (e1 * e2))


def imR_direct(q, w, v, D, g=4):
    f = lambda k: ek(k, v, D) + ek(k + q, v, D) - w  # noqa: E731
    k0_ = -q / 2
    if f(k0_) >= 0:
        return 0.0
    out = 0.0
    for a, b in ((k0_, k0_ + 1e3 * (w / v + q)), (k0_ - 1e3 * (w / v + q), k0_)):
        r = brentq(f, a, b) if f(a) * f(b) < 0 else None
        if r is None:
            continue
        dfdk = v * v * r / ek(r, v, D) + v * v * (r + q) / ek(r + q, v, D)
        out += overlap2(r, r + q, v, D) / abs(dfdk)
    return 0.5 * g * out


def imR_formula(q, w, v, D, g=4):
    s = w * w - v * v * q * q
    if s <= 4 * D * D:
        return 0.0
    return 2 * g * v * q * q * D * D / (s**1.5 * np.sqrt(s - 4 * D * D))


v, D = 3.0e-3, 0.4
print("(1) -Im R_1D, direct integration vs closed form (v = 3e-3, Delta = 0.4 eV, g = 4):")
for q, w in ((10.0, 0.81), (100.0, 0.9), (300.0, 1.5), (100.0, 3.0), (1000.0, 5.0)):
    a, b = imR_direct(q, w, v, D), imR_formula(q, w, v, D)
    print(f"   q = {q:6.0f} eV, w = {w:4.2f} eV: direct {a:.6e}, formula {b:.6e}, rel. diff {abs(a-b)/b:.1e}")

val, err = quad(lambda t: 2 * D**2 * 4 * D**2 / ((4 * D**2 * t) ** 1.5 * np.sqrt(4 * D**2 * (t - 1))), 1, np.inf, limit=400)
print(f"(2) weight int ds 2 Delta^2/[s^1.5 (s - 4 Delta^2)^0.5] = {val:.8f}")

print("(3) cylindrical-shell kernel / (2 alpha): I0 K0 vs ring average of K0(q rho):")
for x in (0.01, 0.1, 1.0, 10.0):
    ring, _ = quad(lambda ph: K0(x * 2 * abs(np.sin(ph / 2))), 0, 2 * np.pi, limit=400, points=[np.pi])
    ring /= 2 * np.pi
    small = np.log(2 / x) - np.euler_gamma
    print(f"   q r_t = {x:5.2f}: I0 K0 = {i0(x)*k0(x):.6f}, ring average = {ring:.6f}, small-x form {small:.6f},"
          f" large-x form 1/(2x) = {1/(2*x):.6f}")

a_cc, t = 1.42, 2.8
vD_eVA = 1.5 * t * a_cc
vD = vD_eVA / HBARC_EVA
vmax = (544 + 250.5) / 299792.458
print(f"(4) v_D = 3 t a_cc/2 = {vD_eVA:.2f} eV Angstrom = {vD:.3e} (c = 1) = {vD*2.99792458e8:.3e} m/s;"
      f" v_max = {vmax:.4e}; v_D/v_max = {vD/vmax:.3f}")
for d_nm in (0.8, 1.0, 1.5):
    rt = d_nm * 10 / 2
    D1 = vD_eVA / (3 * rt)
    print(f"    tube diameter {d_nm} nm: Delta_1 = v_D/(3 r_t) = {D1:.3f} eV, gap 2 Delta_1 = {2*D1:.3f} eV;"
          f" Delta_2 = {2*D1:.3f} eV")

w = 1.0
for q in (1e-2, 1e-1, 1.0):
    print(f"(5) q = {q:5.2f} eV: -Im R/q^2 = {imR_formula(q, w, v, D)/q**2:.6e}, limit {2*4*v*D**2/(w**3*np.sqrt(w*w-4*D*D)):.6e}")

# (6) reach of the subband edges: at the edge q_par = 0, so q = q_perp >= 2 Delta_n/v_max and q_perp r_t >= 2 n v_D/(3 v_max),
#     independent of the radius; |F_perp|^2 = J0(q_perp r_t)^2 there; lightest mass m = 2 (2 Delta_n)/v_max^2.
from scipy.special import j0
for n in (1, 2):
    x = 2 * n * vD / (3 * vmax)
    print(f"(6) subband {n}: q_perp r_t at the edge >= {x:.3f}, J0^2 = {j0(x)**2:.3f}")
for d_nm in (1.0,):
    D1 = vD_eVA / (3 * d_nm * 5)
    print(f"    d = {d_nm} nm: lightest mass reaching 2 Delta_1 = 4 Delta_1/v_max^2 = {4*D1/vmax**2/1e3:.0f} keV;"
          f" 2 Delta_2: {8*D1/vmax**2/1e3:.0f} keV")
