"""Sect. 16.5: the hydrogenic donor form factor of Du et al. (arXiv:2212.04504v1, Eq. (12)), the misprint in its
bracket, and the oscillator-strength content of its continuum.  Prints every number of the text, the F row and the
footnote-free misprint sentence.  Natural units; energies in eV, lengths in Angstrom, hbar c = 1973.2698 eV A.

Source formulas (read from the arXiv v1 full text, sources/16.5/2212.04504.html.txt):
  Eq. (10)  W(q, w) = (2 pi)^2 alpha n_D /(q^2 |eps|^2) sum_k delta(E_k - E_i - w) |<k| e^{-i q.r} |i>|^2;
  Eq. (12)  W = (E_eff/E_0)^2 [2^10 pi^2 alpha m* n_D a*^4 / (3 |eps|^2)]
              (3 q~ + k~^2 + 1) exp[-(2/k~) atan(2k~/(q~^2 - k~^2 + 1))] / {[(q~+k~)^2+1]^3 [(q~-k~)^2+1]^3 [1 - e^{-2pi/k~}]},
            q~ = q a*, k~ = sqrt(2 m* (w - E_I)) a*;  the hydrogenic bracket has 3 q~^2 (checked below);
  parameters (their Sect. IV and App. VII.2): E_I = 45 meV, m* = 0.3 m_e, a* = 23 a.u., E_eff/E_0 = 2.2, n_D = 1e18 cm^-3;
  Eq. (32)  dR/dw = rho_chi /((2 pi)^3 alpha rho_T m_chi) int dq q^3 eta(v_min) |V(q)|^2 W(q, w).
  The atan is the branch in [0, pi] (atan2(2k~, q~^2 - k~^2 + 1)), as the continuity of the generalized oscillator
  strength requires.
Checks: (i) the bracket with 3 q~^2 equals the partial-wave sum over Coulomb waves of the hydrogen continuum
  (mpmath.coulombf; same normalization as figscripts/ch02/limit2_ionization.py) to 1e-4, the printed one does not;
  (ii) at q -> 0 and with a* = 1/sqrt(2 m* E_I), W is the hydrogen dipole continuum of Sect. 4.3 (Bethe-Salpeter Sect. 61)
  times 4 pi^2 alpha n_D/(2 m* w |eps|^2).
Halo for the rate ratio: standard halo of tab:1-shm (v0 = 238, v_esc = 544, v_E = 250.5 km/s), eta of App. D.1 (same
  function as figscripts/ch02/limit2_ionization.py).  The ratio does not depend on rho_chi, n_D, eps or E_eff/E_0.
"""
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from scipy.special import erf, spherical_jn

HBARC, ALPHA, ME = 1973.2698, 1 / 137.035999, 510998.95
A0 = 0.529177
C_KMS = 299792.458
V0, VESC, VE = 238.0, 544.0, 250.5
ZE = VESC / V0
NESC = np.pi**1.5 * V0**3 * (erf(ZE) - 2 / np.sqrt(np.pi) * ZE * np.exp(-ZE**2))
VMAX = (VESC + VE) / C_KMS

EI, MS, AST = 0.045, 0.3 * ME, 23 * A0          # eV, eV, Angstrom (Du et al.)


def eta(u):
    k = np.pi * V0**2 / (VE * NESC)
    u = np.maximum(u, 0.0)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + VE) / V0) - erf((u - VE) / V0)) - 2 * VE * np.exp(-ZE**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(ZE) - erf((u - VE) / V0)) - (VESC + VE - u) * np.exp(-ZE**2))
    return np.where(u < VESC - VE, b1, np.where(u < VESC + VE, b2, 0.0))


def bracket(qt, kt, printed=False):
    num = (3 * qt if printed else 3 * qt**2) + kt**2 + 1
    th = np.arctan2(2 * kt, qt**2 - kt**2 + 1)
    return num * np.exp(-2 / kt * th) / (((qt + kt)**2 + 1)**3 * ((qt - kt)**2 + 1)**3 * (1 - np.exp(-2 * np.pi / kt)))


def gos_partial(p, q):
    """Hydrogen (a = 1, E in Ry) 1s -> continuum generalized oscillator strength per unit energy, from the partial-wave
    sum: dF/dE = (E/q^2) * (p/(4 pi^2)) ... normalized below against the q->0 dipole limit."""
    def integ(L):
        def g(r):
            if r == 0:
                return 0.0
            rad = float(mp.coulombf(L, -1.0 / p, p * r)) / (p * r)
            return r * r * rad * spherical_jn(L, q * r) * 2 * np.exp(-r)
        return quad(g, 0, 80, limit=600)[0]
    return sum((2 * L + 1) * integ(L)**2 for L in range(int(8 + 3 * (p + q))))


print("Check (i): bracket against the Coulomb partial-wave sum (hydrogen units, a = 1, E in Ry).  The generalized oscillator")
print("  strength per unit energy from the sum is (2 k/pi) sum_L (2L+1) I_L^2 (the |f_ion|^2 of Sect. 2.2 over 2k^2); the closed")
print("  form is (2^8/3) q^2 x bracket.  Ratio closed form / sum:")
for qt, kt in [(0.3, 0.5), (1.0, 0.5), (2.0, 1.0), (0.5, 1.5), (3.0, 2.0)]:
    pw = 2 * kt / np.pi * gos_partial(kt, qt)
    c, p_ = (2**8 / 3) * qt**2 * bracket(qt, kt), (2**8 / 3) * qt**2 * bracket(qt, kt, True)
    print(f"  q~ = {qt:3.1f}, k~ = {kt:3.1f}: corrected {c/pw:.5f}, printed {p_/pw:.4f}")

# printed/correct at k~ = 1 for q~ in 0.5..2 (the C10-type comparison)
r = [bracket(q, 1.0, True) / bracket(q, 1.0) for q in (0.5, 1.0, 2.0)]
print(f"  printed/correct bracket at k~ = 1: q~ = 0.5: {r[0]:.3f}, 1: {r[1]:.3f}, 2: {r[2]:.3f}")

# check (ii): q -> 0 limit against the Sect. 4.3 dipole continuum, consistent hydrogenic parameters
print("\nCheck (ii): q -> 0 limit with a* = 1/sqrt(2 m* E_I) against 4 pi^2 alpha n/(2 m* w) df/dw (Sect. 4.3):")
a_cons = HBARC / np.sqrt(2 * MS * EI)
pref = 2**10 * np.pi**2 * ALPHA * MS * (a_cons / HBARC)**4 / 3          # eV^-3 ... times n_D (eV^3) -> 1/eV? (per n)
for w in (0.05, 0.07, 0.12):
    kt = np.sqrt(2 * MS * (w - EI)) * a_cons / HBARC
    Wdu = pref * bracket(1e-6, kt)
    xi = np.sqrt(EI / (w - EI))
    dfdw = 2**7 / (3 * EI) * (EI / w)**4 * np.exp(-4 * xi * np.arctan(1 / xi)) / (1 - np.exp(-2 * np.pi * xi))
    Wbs = 4 * np.pi**2 * ALPHA / (2 * MS * w) * dfdw
    print(f"  w = {w*1e3:5.1f} meV: Eq. (12) / Bethe-Salpeter = {Wdu/Wbs:.6f}")

# oscillator-strength content of the published continuum
print("\nTRK content of the continuum of Eq. (12) at q = 0, in units of the f-sum (pi/2) omega_pD^2/eps^2 of one electron")
print(f"  of mass m* per donor (Du et al.: E_I = 45 meV, m* = 0.3 m_e, a* = 23 a.u. = {AST:.2f} A)")
EA = HBARC**2 / (2 * MS * AST**2)
print(f"  hydrogenic binding implied by m* and a*: 1/(2 m* a*^2) = {EA*1e3:.1f} meV; (E_I/that)^2 = {(EI/EA)**2:.3f}")
for a_use, lab in ((a_cons, f"consistent a* = {a_cons:.2f} A"), (AST, "Du et al. a* = 23 a.u.")):
    pref = 2**10 * np.pi**2 * ALPHA * MS * (a_use / HBARC)**4 / 3
    f = lambda w: w * pref * bracket(1e-7, np.sqrt(2 * MS * (w - EI)) * a_use / HBARC)
    integ = quad(f, EI, EI * 400, limit=400, points=[EI * 1.01, EI * 2, EI * 10])[0]
    fsum = np.pi / 2 * 4 * np.pi * ALPHA / MS
    print(f"  {lab}: continuum share {integ/fsum:.3f}; times (E_eff/E_0)^2 = 2.2^2 = 4.84: {4.84*integ/fsum:.3f}")
    print(f"     in units of m_e: f_cont = {integ/fsum*ME/MS:.3f}, with 4.84: {4.84*integ/fsum*ME/MS:.3f}")
fsi = (2 / 0.191 + 1 / 0.916) / 3
print(f"  f-sum of one donor electron in the silicon valleys, cubic average m_e(2/m_perp + 1/m_par)/3 = {fsi:.3f}")

# ratio of the scattering rate with the printed and the corrected bracket
print("\nScattering rate with the printed bracket over the corrected one (Du et al. parameters, eps held fixed,")
print("  standard halo of tab:1-shm, v_max = 794.5 km/s):")


def rate(m, printed, light):
    wmax = m * VMAX**2 / 2
    if wmax <= EI:
        return 0.0
    ws = EI + (wmax - EI) * (1 - np.cos(np.linspace(0, np.pi / 2, 160)))
    tot = []
    for w in ws[1:]:
        disc = np.sqrt(max(VMAX**2 - 2 * w / m, 0.0))
        qlo, qhi = m * (VMAX - disc), m * (VMAX + disc)
        qs = np.geomspace(qlo, qhi, 400)
        vmin = (w / qs + qs / (2 * m)) * C_KMS
        kt = np.sqrt(2 * MS * (w - EI)) * AST / HBARC
        W = bracket(qs * AST / HBARC, kt, printed)
        V2 = qs**-4 if light else 1.0
        tot.append(np.trapezoid(qs**3 * eta(vmin) * V2 * W, qs))
    return np.trapezoid(tot, ws[1:])


for light in (False, True):
    out = []
    for m in (0.02e6, 0.1e6, 1e6, 10e6):
        out.append(rate(m, True, light) / rate(m, False, light))
    print(f"  {'light' if light else 'heavy'} mediator, m_chi = 0.02, 0.1, 1, 10 MeV: " + ", ".join(f"{x:.2f}" for x in out))
print(f"  threshold mass 2 E_I/v_max^2 = {2*EI/VMAX**2/1e3:.1f} keV")
