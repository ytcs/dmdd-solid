"""Numbers of Sect. 14.4 (spin responses from neutron data) and of Worked example 14.4 (we:14-paramagnet).
Log: we14_4.log.  Run: python we14_4.py (instant).

Cited inputs (printed with their source so that every number of the section is in a log):
  Berlin, Millar, Trickle, Zhou, arXiv:2504.02927 (v2), Sect. III B and App. C/D:
    incident neutron energy of the YIG dataset E_i = 120 meV; maximum magnon energy of YIG about 110 meV; energy resolution
    5 meV at zero energy transfer (data below 5 meV removed); detectors up to 60 deg from the beam, none below about 3 deg;
    edge of the first Brillouin zone q_1BZ = 987 eV; data-driven sensitivity close to the Heisenberg-model result near
    m_chi ~ 1 MeV and falling rapidly below about 200 keV; Fe3+ form factor suppresses the rate by an order of magnitude
    for q >~ 10 keV; phonon production by the nuclear coupling suppressed by q^2/(m_N omega) = (q/30 keV)^2 for
    m_N ~ 50 GeV, omega ~ 20 meV (their App. C).
  Book values: v_max = v_esc + v_E = 794.5 km/s (NOTATION, Sect. 1.2); m_n = 939.565 MeV (CODATA); (gamma_n r_cl)^2 =
    0.2906 b (App. C.19, gamma_n = -1.913, r_cl = 2.818 fm).

Worked example 14.4 (two-angle inversion; model numbers, no data):
  Uniaxial (spin-space) form S = S_par m m + S_perp (1 - m m) (+ antisymmetric part, which drops out of every symmetric
  contraction).  Unpolarized data measure P(c) = P_T:S = S_par (1 - c^2) + S_perp (1 + c^2), c = q.m.
  Two angles c1, c2:  S_par  = [P1 (1 + c2^2) - P2 (1 + c1^2)] / [2 (c2^2 - c1^2)],
                      S_perp = [P2 (1 - c1^2) - P1 (1 - c2^2)] / [2 (c2^2 - c1^2)].
  Longitudinal element at a dark-matter direction c': L(c') = S_par c'^2 + S_perp (1 - c'^2).
  Isotropic paramagnet: S_par = S_perp = S0 (units S0 = 1), so P = 2 at every c; each P measured with a 5 % statistical
  error (illustrative choice), errors independent and Gaussian.  Rotations: c2 = 1 (90 deg between the two field or
  crystal settings relative to q) and c2 = sin 30 deg = 0.5; c1 = 0 in both.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "we14_4.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


C_KMS = 299792.458
VMAX = 794.5 / C_KMS
MN = 939.565e6          # eV
EI = 0.120              # eV, 2504.02927 Sect. III B
Q1BZ = 987.0            # eV, 2504.02927 Sect. III B

out("== Cited inputs (2504.02927 v2 Sect. III B, App. C)")
out("E_i = 120 meV; YIG maximum magnon energy about 110 meV; resolution 5 meV at zero transfer; detectors to 60 deg;")
out("q_1BZ = 987 eV; agreement with the Heisenberg-model result near 1 MeV; rapid fall below about 200 keV;")
out("YIG sample at T < ~10 K (their App. B 2)")
out("Fe3+ form factor: order-of-magnitude suppression for q >~ 10 keV; phonon factor (q/30 keV)^2 for m_N ~ 50 GeV, omega ~ 20 meV")
out(f"Book: v_max = 794.5 km/s = {VMAX:.4e}")

out("\n== C_sn at q -> 0 for J multiplets, [lambda_S/(g_J/2)]^2 with lambda_S = g_J - 1 (tab:14-lande, Hund's rules)")
from fractions import Fraction as Fr
for ion, gJ in (("Gd3+", Fr(2)), ("Er3+", Fr(6, 5)), ("Sm3+", Fr(2, 7))):
    lam = gJ - 1
    out(f"{ion}: g_J = {gJ}, lambda_S = {lam}, C_sn(0) = {(lam/(gJ/2))**2}")

out("\n== Kinematics of the neutron probe")
pn = np.sqrt(2 * MN * EI)
out(f"neutron momentum at E_i = 120 meV: p_n = {pn:.0f} eV = {pn/1e3:.1f} keV; largest momentum transfer (backscattering) {2*pn/1e3:.1f} keV")
m_eq = pn / VMAX
out(f"dark-matter mass whose largest momentum, m v_max, equals p_n: {m_eq/1e6:.2f} MeV; its largest momentum transfer 2 m v_max = {2*pn/1e3:.1f} keV")
out(f"kinetic energy of that dark-matter particle at v_max: {0.5*m_eq*VMAX**2:.1f} eV (against 0.120 eV for the neutron)")
m_bz = Q1BZ / (2 * VMAX)
out(f"mass whose largest momentum transfer 2 m v_max equals q_1BZ = 987 eV: {m_bz/1e3:.0f} keV")
HBARC_EV_A = 1973.269804
for aY in (12.56, 12.375):
    out(f"bcc YIG, a = {aY} A: 2 pi/a (Gamma to the zone corner H) = {2*np.pi/aY*HBARC_EV_A:.0f} eV;"
        f" inscribed radius pi sqrt2/a (Gamma to N) = {np.pi*np.sqrt(2)/aY*HBARC_EV_A:.0f} eV;"
        f" every q inside the first zone for m < (pi sqrt2/a)/(2 v_max) = {np.pi*np.sqrt(2)/aY*HBARC_EV_A/(2*VMAX)/1e3:.0f} keV")
out("  (q_1BZ = 987 eV of 2504.02927 is 2 pi/a for their a = 12.56 A; the book's a = 12.375 A, DATA-ADDENDA)")
out(f"phonon factor (q/30 keV)^2 at q = 5, 10, 15 keV: {(5/30)**2:.3f}, {(10/30)**2:.3f}, {(15/30)**2:.3f}")

out("\n== Worked example 14.4: two-angle inversion, isotropic paramagnet (S0 = 1)")
rel = 0.05


def invert(c1, c2, P1, P2):
    d = 2 * (c2**2 - c1**2)
    spar = (P1 * (1 + c2**2) - P2 * (1 + c1**2)) / d
    sper = (P2 * (1 - c1**2) - P1 * (1 - c2**2)) / d
    return spar, sper


def errors(c1, c2, sP1, sP2, cp):
    d = 2 * (c2**2 - c1**2)
    # linear coefficients of S_par, S_perp in (P1, P2)
    a_par = np.array([(1 + c2**2) / d, -(1 + c1**2) / d])
    a_per = np.array([-(1 - c2**2) / d, (1 - c1**2) / d])
    a_L = cp**2 * a_par + (1 - cp**2) * a_per
    s = np.array([sP1, sP2])
    f = lambda a: np.sqrt(np.sum((a * s)**2))
    return f(a_par), f(a_per), f(a_L), a_L


S0 = 1.0
for c2 in (1.0, 0.5):
    c1 = 0.0
    P1 = S0 * (1 - c1**2) + S0 * (1 + c1**2)
    P2 = S0 * (1 - c2**2) + S0 * (1 + c2**2)
    sp, so = invert(c1, c2, P1, P2)
    out(f"c1 = {c1}, c2 = {c2}: P1 = {P1:.3f}, P2 = {P2:.3f} (units S0); determinant 2(c2^2 - c1^2) = {2*(c2**2-c1**2):.3f}")
    out(f"   inverted S_par = {sp:.3f}, S_perp = {so:.3f}")
    sP = rel * 2 * S0
    for cp2 in (1.0, 0.5, 1 / 3, 0.0):
        cp = np.sqrt(cp2)
        e_par, e_per, e_L, aL = errors(c1, c2, sP, sP, cp)
        L = sp * cp2 + so * (1 - cp2)
        out(f"   c'^2 = {cp2:.3f}: L = {L:.3f} +- {e_L:.3f} (coefficients on P1, P2: {aL[0]:+.3f}, {aL[1]:+.3f}); "
            f"sigma(S_par) = {e_par:.3f}, sigma(S_perp) = {e_per:.3f}")
    out(f"   isotropy test P2 - P1 = {P2-P1:.3f} +- {np.sqrt(2)*sP:.3f}; equals (c2^2 - c1^2)(S_perp - S_par)")
out(f"one-angle isotropic shortcut L = P/2: L = {2*S0/2:.3f} +- {rel*2*S0/2:.3f} (5 %), valid only if S_par = S_perp")

# illustration: Berlin's collinear relation (S_par = 0 assumed) applied to a magnet with S_par/S_perp = r
out("\n== Collinear one-angle relation (S_par = 0 assumed, 2504.02927 Eqs. (36)-(37)) against a uniaxial response")
for r in (0.073,):
    for c in (0.0, 0.5, 1.0):
        P = r * (1 - c**2) + (1 + c**2)      # S_perp = 1
        for cp2 in (1.0, 0.0):
            Ltrue = r * cp2 + (1 - cp2)
            Lest = (1 - cp2) * P / (1 + c**2)
            out(f"   r = {r}, measured at c = {c}: L(c'^2={cp2:.0f}) true {Ltrue:.3f}, from S_par = 0: {Lest:.3f}")
LOG.close()

LOG = open(os.path.join(HERE, "we14_4.log"), "a")
out("\n== Shifted-wavevector route (localized moments, one magnetic ion per primitive cell): S_ab(k+G) = |F|^2 S^lat_ab(k)")
# Each G gives the transverse trace Tr S^lat - n.S^lat.n with n = (k+G)/|k+G|, linear in the 6 components of the
# symmetric part of S^lat.  Rank of that linear map for the directions of k + G, k small, G the shortest fcc vectors
# of the NiO chemical lattice (units 2 pi/a): (111)-type and (200)-type.
def row(n):
    n = n / np.linalg.norm(n)
    # components (xx, yy, zz, xy, xz, yz) of a symmetric tensor; Tr S - n.S.n
    return np.array([1 - n[0]**2, 1 - n[1]**2, 1 - n[2]**2, -2*n[0]*n[1], -2*n[0]*n[2], -2*n[1]*n[2]])
k = np.array([0.05, 0.02, 0.01])
Gs = [np.array(g, float) for g in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1), (2, 0, 0), (0, 2, 0), (0, 0, 2)]]
for nG in (3, 4, 6, 7):
    M = np.array([row(k + G) for G in Gs[:nG]])
    out(f"  {nG} shifted wavevectors: rank of the map to the 6 symmetric components = {np.linalg.matrix_rank(M)}")
rng = np.random.default_rng(0)
A = rng.normal(size=(3, 3)); Strue = A @ A.T
v = np.array([Strue[0, 0], Strue[1, 1], Strue[2, 2], Strue[0, 1], Strue[0, 2], Strue[1, 2]])
M = np.array([row(k + G) for G in Gs])
sol = np.linalg.lstsq(M, M @ v, rcond=None)[0]
out(f"  reconstruction of a random positive tensor from 7 transverse traces: max error {np.max(np.abs(sol - v)):.1e}")
LOG.close()
