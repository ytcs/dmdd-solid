"""Fig. 15.2 and the numbers of Sect. 15.3 (films and disorder). Output: tex/figures/ch15/fig15_2.pdf.
Every number printed in Sect. 15.3 is printed here (log: film15.log, written by `python film15.py > film15.log`).

Model (modelling choices, also named in the caption and the text):
  Normal-state aluminum as the free electron gas of al_constants.py (one set book-wide): m* = m_e, a = 4.05 A,
  k_F = 1.749 A^-1, v_F = k_F/m_e = 6.753e-3, omega_p = 15.78 eV, k_TF = 4.05 keV; k_TF^2 = 3 omega_p^2 / v_F^2
  holds exactly, as in the gas of Sect. 4.5.  T = 0, Heaviside-Lorentz natural units, e^2 = 4 pi alpha.
  Lindhard R0(q, z) of eq:4.5-lindhard, at complex z with Im z > 0, principal-branch logarithm (mpmath, 40 digits).
  Mermin eq:4.5-mermin; naive substitution eps_Lin(q, omega + i gamma); Drude 1 - omega_p^2/[omega(omega + i gamma)].
  Film: mean free path l_e = 50 nm, taken equal to the thickness d = 50 nm (illustrative choice: a film whose surfaces
  scatter diffusely), gamma_rel = v_F / l_e, D_diff = v_F l_e / 3.
  Energy of Fig. 15.2(a) and of the worked example: omega = 5 Delta_BCS with the bulk gap Delta_BCS = 0.18 meV
  (Sect. 7.2), q_min = omega / v_max, v_max = 2.650e-3 (Sect. 1.3).
Small-q form (q << k_F, used in panel (b) and checked against the full Lindhard):
  R0(q, z)/R0(q, 0) = f_L(nu) = 1 - (nu/2) l(nu), nu = z/(q v_F), l(w) = ln[(w+1)/(w-1)].
Quoted inputs (not computed here):
  WSi: Zhang et al., arXiv:1607.07854, Table I (5 nm films): R_s = 326-417 Ohm, D_e = 0.70-0.75 cm^2/s,
       N_0 = 2.6e47-4.1e47 m^-3 J^-1, xi(0) = 7.0-7.4 nm, T_c = 3.83-4.08 K.
       QROCODILE, arXiv:2412.16279: 2 nm W45Si55 layer, T_c = 1.73 K (p. 3); supplement: E_F = 7 eV,
       omega_p ~ 10.8 eV, Lindhard with plasmon width Gamma = 0.1 E_F (Eq. (S.1) and text).
  Al plasmon width 0.863 eV, omega_p 14.9 eV: Hochberg et al., arXiv:2101.08263, Fig. S1 caption (Froehlich fit).
  Dirty-edge ratios L_BCS / (g_I L_nor(Gamma)) on the kinematic edge q = omega/v_max (Born impurities, T = 0, v_F = 6.8e-3,
       Delta = 0.18 meV; validated table of the deferred-computation record, quoted with its l_e scope).
"""
import os
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import special

mp.mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch15", "fig15_2.pdf")

ALPHA = 1 / 137.035999084
E2 = 4 * np.pi * ALPHA
ME = 510998.95          # eV
HBARC_NM = 197.3269804  # eV nm
HBAR_EVS = 6.582119569e-16
EPS0 = 8.8541878128e-12
QE = 1.602176634e-19
C = 2.99792458e8

# ---------------- aluminum gas ----------------
import sys
sys.path.insert(0, HERE)
import al_constants as alc
KF = alc.KF                  # eV  (1.749 A^-1)
VF = alc.VF
MSTAR = ME
NF2 = MSTAR * KF / np.pi**2   # 2 N_F, both spins, eV^2
KTF2 = E2 * NF2
KTF = np.sqrt(KTF2)
NE = KF**3 / (3 * np.pi**2)
WP = np.sqrt(E2 * NE / MSTAR)
VMAX = 2.650e-3
DELTA = 0.18e-3
DW = 1.764 * 1.73 * 8.617333e-5   # WSi gap from T_c = 1.73 K (QROCODILE)
LE_NM = 50.0
LE = LE_NM / HBARC_NM          # eV^-1
DFILM = LE
GAM = VF / LE
DDIFF = VF * LE / 3


def R0(q, z, kf=KF, vf=VF, nf2=NF2):
    q = mp.mpf(q)
    z = mp.mpc(z)
    nu = z / (q * vf)
    yp = q / (2 * kf)

    def ell(w):
        return mp.log((w + 1) / (w - 1))
    nup, num = nu + yp, nu - yp
    br = mp.mpf(1) / 2 + (kf / (4 * q)) * ((1 - nup**2) * ell(nup) - (1 - num**2) * ell(num))
    return -nf2 * br


def eps_lin(q, z, **kw):
    return 1 - (E2 / mp.mpf(q)**2) * R0(q, z, **kw)


def eps_static(q, **kw):
    return mp.re(eps_lin(q, mp.mpc(0, 1e-30), **kw))


def eps_mermin(q, w, g, **kw):
    z = mp.mpc(w, g)
    el = eps_lin(q, z, **kw)
    es = eps_static(q, **kw)
    a = mp.mpc(0, g) / w
    return 1 + (1 + a) * (el - 1) / (1 + a * (el - 1) / (es - 1))


def loss(e):
    return float(mp.im(-1 / e))


def eps_drude(w, g, wp=WP):
    return 1 - wp**2 / (w * (w + 1j * g))


def fL(nu):
    nu = mp.mpc(nu)
    return 1 - nu / 2 * mp.log((nu + 1) / (nu - 1))


def ratio_small_q(x, w_over_g):
    """L_Mermin / L_Drude for q << k_F, k_TF >> q, as a function of x = q l_e and omega/gamma (units gamma = 1)."""
    g = mp.mpf(1)
    w = mp.mpf(w_over_g)
    qv = x  # q v_F in units of gamma, since q l_e = q v_F / gamma
    nu = mp.mpc(w, g) / qv
    f = fL(nu)
    # eps - 1 = (k^2/q^2) (w + i g) f / (w + i g f); drop the 1 (k_TF >> q); overall k^2/q^2 cancels in the ratio below
    em = mp.mpc(w, g) * f / (w + mp.mpc(0, 1) * g * f)
    # L = Im(-1/eps) with eps = (k^2/q^2) em -> L = (q^2/k^2) Im(-1/em); Drude L = w g / wp^2 = w/(k^2 D) = 3 w g/(k^2 v^2)
    # ratio = (q^2) Im(-1/em) / (3 w g / v^2) = (qv)^2 Im(-1/em) / (3 w g)
    return float((qv**2) * mp.im(-1 / em) / (3 * w * g))


def ratio_naive_small_q(x, w_over_g):
    g = mp.mpf(1)
    w = mp.mpf(w_over_g)
    qv = x
    nu = mp.mpc(w, g) / qv
    f = fL(nu)
    return float((qv**2) * mp.im(-1 / f) / (3 * w * g))


def gI(y):
    k = (y - 2) / (y + 2)
    return (1 + 2 / y) * special.ellipe(k**2) - 4 * special.ellipk(k**2) / (y + 2)


print("=== Aluminum free-electron gas ===")
print(f"k_F = {KF:.1f} eV = {KF/1000:.3f} keV, v_F = {VF}, m*/m_e = {MSTAR/ME:.4f}")
print(f"k_TF = {KTF:.0f} eV, omega_p = {WP:.2f} eV, k_TF^2 = {KTF2:.4e} eV^2")
print(f"check k_TF^2 v_F^2/3 = omega_p^2: {KTF2*VF**2/3:.4f} vs {WP**2:.4f}")
print(f"v_max/v_F = {VMAX/VF:.4f}")
xi = VF / (np.pi * DELTA)
print(f"coherence length v_F/(pi Delta) = {xi*HBARC_NM:.0f} nm (Delta = 0.18 meV)")

print("\n=== 50 nm film ===")
print(f"l_e = {LE_NM} nm = {LE:.4f} eV^-1; 1/l_e = {1/LE:.3f} eV")
print(f"gamma_rel = v_F/l_e = {GAM*1e3:.2f} meV; D_diff = v_F l_e/3 = {DDIFF:.4e} eV^-1 = {DDIFF*HBARC_NM*1e-9*C*1e4:.1f} cm^2/s")
print(f"k_F l_e = {KF*LE:.0f}; l_e/xi = {LE_NM/(xi*HBARC_NM):.4f}")
KF_M = KF / 1973.269804 * 1e10   # k_F in m^-1
rho_l = 3 * np.pi**2 * HBAR_EVS * QE / (QE**2 * KF_M**2)   # Ohm m^2, free-electron rho*l = 3 pi^2 hbar/(e^2 k_F^2)
print(f"free-electron rho*l_e = {rho_l:.3e} Ohm m^2 (k_F = {KF/1973.269804:.4f} A^-1)")
rho = rho_l / (LE_NM * 1e-9)
print(f"rho for l_e = 50 nm: {rho:.3e} Ohm m = {rho*1e8:.3f} microOhm cm")
mq = (1 / DFILM) / (2 * VMAX)
print(f"q = 1/d = {1/DFILM:.3f} eV reached by m_chi >= q/(2 v_max) = {mq:.0f} eV")


print("\n=== Table: disorder parameters ===")
qe_al = 2 * DELTA / VMAX
print(f"Al: pair-breaking edge q = 2 Delta/v_max = {qe_al:.4f} eV; q l_e = {qe_al*LE:.4f}; at q = 1 keV q l_e = {1000*LE:.0f}")

print("\n=== Worked example: omega = 5 Delta, q = q_min ===")
w = 5 * DELTA
q = w / VMAX
print(f"omega = {w*1e3:.3f} meV, q_min = omega/v_max = {q:.4f} eV")
print(f"q l_e = {q*LE:.4f}; q d = {q*DFILM:.4f}; q v_F = {q*VF*1e3:.4f} meV; D q^2 = {DDIFF*q**2*1e3:.4f} meV")
nu = complex(w, GAM) / (q * VF)
print(f"D q^2/Delta = {DDIFF*q**2/DELTA:.3f}")
print(f"nu_gamma = (omega + i gamma)/(q v_F) = {nu.real:.3f} + {nu.imag:.3f} i")
f = complex(fL(nu))
print(f"f_L(nu_gamma) = {f.real:.5e} + {f.imag:.5e} i ;  -1/(3 nu^2) = {(-1/(3*nu**2)).real:.5e} + {(-1/(3*nu**2)).imag:.5e} i")
em = eps_mermin(q, w, GAM)
el = eps_lin(q, mp.mpc(w, 1e-30))
en = eps_lin(q, mp.mpc(w, GAM))
ed = eps_drude(w, GAM)
diffpole = 1 + KTF2 * DDIFF / (DDIFF * q**2 - 1j * w)
print(f"eps_Mermin = {complex(em):.4e}")
print(f"diffusion-pole form 1 + k_TF^2 D/(D q^2 - i omega) = {diffpole:.4e}")
print(f"eps_Drude = {ed:.4e}")
print(f"eps_naive = {complex(en):.4e}")
print(f"eps_Lindhard (clean) = {complex(el):.4e}; static k_TF^2/q^2 = {KTF2/q**2:.4e}")
LM, LL, LN, LD = loss(em), loss(el), loss(en), float(np.imag(-1 / ed))
print(f"L_Mermin = {LM:.4e}; L_Drude = {LD:.4e}; omega gamma/omega_p^2 = {w*GAM/WP**2:.4e}; omega/(k_TF^2 D) = {w/(KTF2*DDIFF):.4e}")
print(f"L_Lindhard = {LL:.4e}; pi omega q/(2 k_TF^2 v_F) = {np.pi*w*q/(2*KTF2*VF):.4e}")
print(f"L_naive = {LN:.4e}; |eps_Mer|/|eps_naive| = {float(abs(em)/abs(en)):.1f}; Im eps_Mer/Im eps_naive = {float(mp.im(em)/mp.im(en)):.0f}")
print(f"ratios: Mermin/Lindhard = {LM/LL:.3f} (6/(pi q l_e) = {6/(np.pi*q*LE):.3f}); naive/Mermin = {LN/LM:.4f}; Mermin/Drude = {LM/LD:.5f}")
Lrho = EPS0 * (w / HBAR_EVS) * rho
print(f"eps0 omega rho = {Lrho:.4e} (L from the resistivity alone)")
y = 5.0
print(f"g_I(5) = {gI(5.0):.4f}; g_I(3) = {gI(3.0):.4f}; g_I(2.2) = {gI(2.2):.4f}")
dirty = {"30 nm": {2.2: 0.187, 2.5: 0.569, 3: 1.008, 5: 1.091}, "100 nm": {2.2: 0.246, 2.5: 0.633, 3: 1.025, 5: 1.082},
         "300 nm": {2.2: 0.375, 2.5: 0.733, 3: 1.027, 5: 1.066}, "1 um": {2.2: 0.600, 2.5: 0.854, 3: 1.021, 5: 1.057},
         "clean": {2.2: 0.866, 2.5: 0.998, 3: 1.068, 5: 1.066}}
print("quoted dirty-edge ratios L_BCS/(g_I L_nor):", dirty)
for k in ("30 nm", "100 nm"):
    print(f"  at y = 5, {k}: L_BCS/L_nor = g_I(5) x {dirty[k][5]} = {gI(5.0)*dirty[k][5]:.3f}")
print(f"  y = 2.2: L_BCS/L_nor = g_I x ratio: clean {gI(2.2)*0.866:.3f}, 1 um {gI(2.2)*0.600:.3f}, 30 nm {gI(2.2)*0.187:.3f}")
print(f"  y = 2.2 corresponds to omega = {2.2*DELTA*1e3:.3f} meV; y = 3 to {3*DELTA*1e3:.3f} meV")


print("\n=== Dirty local limit: Mattis-Bardeen loss-function ratio (T = 0) ===")
# sigma_1/sigma_n: case-II (Mattis-Bardeen) closed form; sigma_2/sigma_n: T = 0 integral
#   sigma_2/sigma_n = (1/y) int_{max(1-y,-1)}^{1} dE (E^2 + 1 + yE)/sqrt((1-E^2)((E+y)^2-1))   (units Delta = 1)
# checked against the Kramers-Kronig transform of sigma_1 with the missing weight (pi^2/2) Delta sigma_n at omega = 0.
from scipy import integrate


def mb1(y):
    if y <= 2:
        return 0.0
    k = (y - 2) / (y + 2)
    return (1 + 2 / y) * special.ellipe(k**2) - (4 / y) * special.ellipk(k**2)


def mb2(y):
    lo, hi = max(1 - y, -1.0), 1.0

    def f(t):
        E = lo + (hi - lo) * (1 - np.cos(t)) / 2
        return (E * E + 1 + y * E) / np.sqrt((1 - E * E) * ((E + y)**2 - 1)) * (hi - lo) * np.sin(t) / 2
    return integrate.quad(f, 0, np.pi, limit=400)[0] / y


Wmiss = integrate.quad(lambda x: 1 - mb1(x), 0, 2)[0] + integrate.quad(lambda x: 1 - mb1(x), 2, 1e3, limit=500)[0] \
    + integrate.quad(lambda x: 1 - mb1(x), 1e3, 1e6, limit=500)[0]
print(f"missing weight int (1 - sigma_1/sigma_n) d(omega)/Delta = {Wmiss:.4f}; pi^2/2 = {np.pi**2/2:.4f}")


def mb2_kk(y):
    I = integrate.quad(lambda x: mb1(x) - 1, 0, 1e5, weight="cauchy", wvar=y, limit=2000)[0]
    J = integrate.quad(lambda x: (mb1(x) - 1) / (x + y), 0, 1e5, limit=2000)[0]
    return np.pi / y - 2 * y / np.pi * (I - J) / (2 * y)


import warnings
warnings.filterwarnings("ignore")
print(f"KK check at y = 3: sigma_2/sigma_n integral {mb2(3.0):.4f}, Kramers-Kronig {mb2_kk(3.0):.4f}")
for yy in [2.05, 2.2, 2.5, 3.0, 5.0, 10.0]:
    a1, a2 = mb1(yy), mb2(yy)
    print(f"y = {yy}: sigma_1/sigma_n = {a1:.4f}, sigma_2/sigma_n = {a2:.4f}, L_s/L_n = sigma_1/(sigma_1^2 + sigma_2^2) = "
          f"{a1/(a1*a1+a2*a2):.4f}; g_I = {gI(yy):.4f}")
print(f"sigma_2/sigma_n at y = 2: {mb2(2.0000001):.4f}")
print("Mattis-Bardeen L_s/L_n divided by g_I (the normalization of tab:15-edge): " + "  ".join(
    f"y={yy}: {mb1(yy)/(mb1(yy)**2+mb2(yy)**2)/gI(yy):.3f}" for yy in (2.05, 2.2, 2.5, 3.0, 5.0, 10.0)))
print("Born-impurity edge values times g_I (L_BCS/L_nor) at y = 2.2:",
      {k: round(gI(2.2) * v[2.2], 3) for k, v in dirty.items()})
print("same at y = 2.5:", {k: round(gI(2.5) * v[2.5], 3) for k, v in dirty.items()})
print("same at y = 3:", {k: round(gI(3.0) * v[3], 3) for k, v in dirty.items()})


print("\n=== Worked example, superconducting step and WSi normal-state loss at its edge ===")
print(f"L_s(y = 5) = MB ratio x L_Mermin = {mb1(5.0)/(mb1(5.0)**2+mb2(5.0)**2):.4f} x {LM:.4e} = {mb1(5.0)/(mb1(5.0)**2+mb2(5.0)**2)*LM:.4e}")
qy22 = 2.2 * DELTA / VMAX
print(f"Al film at y = 2.2 on the edge: q = {qy22:.4f} eV, D q^2 = {DDIFF*qy22**2*1e3:.4f} meV = {DDIFF*qy22**2/DELTA:.3f} Delta")
D30 = VF * (30.0 / HBARC_NM) / 3
print(f"l_e = 30 nm at y = 2.2 on the edge: D q^2 = {D30*qy22**2/DELTA:.3f} Delta; q l_e = {qy22*30.0/HBARC_NM:.4f}")
mbt = {y_: mb1(y_)/(mb1(y_)**2+mb2(y_)**2)/gI(y_) for y_ in (2.2, 3.0, 5.0, 10.0)}
print("spread at y = 5 over clean, 1 um, 30 nm (tab:15-edge) and the local limit, units of tab:15-edge: "
      f"{min(1.067, 1.057, 1.091, mbt[5.0]):.3f} - {max(1.067, 1.057, 1.091, mbt[5.0]):.3f}; clean/local at y = 2.2: {0.867/mbt[2.2]:.2f}")
for rW in (1.63e-6, 2.09e-6):
    print(f"WSi rho = {rW*1e8:.0f} microOhm cm: L = eps0 omega rho at omega = 2 Delta = {2*DW*1e3:.3f} meV: "
          f"{EPS0*(2*DW/HBAR_EVS)*rW:.3e}; rho/rho(Al film) = {rW/rho:.0f}")


# Values of tab:15-edge (Sect. 15.2), conserving response in units of g_I L_nor, quoted for the comparison in 15.3
tab = {2.2: (0.867, 0.600, 0.187), 3.0: (1.069, 1.021, 1.008), 5.0: (1.067, 1.057, 1.091)}
for yy, (c, u1, n30) in tab.items():
    print(f"tab:15-edge y = {yy}: L_s/L_n clean {gI(yy)*c:.3f}, 1 um {gI(yy)*u1:.3f}, 30 nm {gI(yy)*n30:.3f}")

print("\n=== Sheet screening of the 50 nm film at q_min (film in vacuum) ===")
qd = q * DFILM
es = 1 + (qd / 2) * (em - 1)
print(f"q d = {qd:.4f}; (q d/2)|eps - 1| = {float(abs(qd/2*(em-1))):.3e}")
print(f"|eps/eps_sheet|^2 = {float(abs(em/es))**2:.1f}; (2/(q d))^2 = {(2/qd)**2:.1f}")
print(f"1/q = {HBARC_NM/q:.0f} nm")
kd = qd
ecm = complex(em)
coth = 1 / np.tanh(kd / 2)
Rlp = (1 / ecm) * (2 - kd * coth + ecm * (2 * ecm - 4 - kd)) / (coth + ecm)   # k R of Lasenby-Prabhu Eq. (19)
ratio_slab = (Rlp.imag / kd) / np.imag(-1 / ecm)
print(f"exact slab in vacuum (Lasenby and Prabhu arXiv:2110.01587 Eq. (19), k normal to the layer... in their axes k || z"
      f" in the plane): Im(R)/d over Im(-1/eps) = {ratio_slab:.1f}; leading order (2/(q d))^2 = {(2/qd)**2:.1f};"
      f" ratio exact/leading = {ratio_slab/(2/qd)**2:.3f}")
q1k = 1000.0
print(f"at q = 1 keV: q d = {q1k*DFILM:.1f}")

print("\n=== Universal ratio L_Mermin/L_Drude (q << k_F, k_TF >> q) ===")
wg = w / GAM
print(f"omega/gamma used = {wg:.4f}")
for x in [0.01, 0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 30.0, 100.0]:
    r = ratio_small_q(x, wg)
    r0 = ratio_small_q(x, 1e-4)
    rn = ratio_naive_small_q(x, wg)
    print(f"x = q l_e = {x:7.2f}: L_Mer/L_D = {r:.4f} (omega/gamma=1e-4: {r0:.4f}); pi x/6 = {np.pi*x/6:.4f}; "
          f"ratio/(pi x/6) = {r/(np.pi*x/6):.4f}; naive/Drude = {rn:.4f}")
xs = np.logspace(-3, 3, 241)
rs = np.array([ratio_small_q(x, wg) for x in xs])
rn = np.array([ratio_naive_small_q(x, wg) for x in xs])
dif_ok = xs[np.abs(rs - 1) <= 0.1]
bal_ok = xs[np.abs(rs / (np.pi * xs / 6) - 1) <= 0.1]
print(f"within 10% of 1 (diffusive): x <= {dif_ok.max():.3f} (grid)")
print(f"within 10% of pi x/6 (ballistic): x >= {bal_ok.min():.2f} (grid)")
from scipy.optimize import brentq
xd = brentq(lambda x: ratio_small_q(x, wg) - 1.1, 0.1, 3.0, xtol=1e-6)
xb = brentq(lambda x: ratio_small_q(x, wg) / (np.pi * x / 6) - 1.1, 2.0, 50.0, xtol=1e-6)
print(f"root-finder: L_Mer/L_D = 1.1 at q l_e = {xd:.3f}; L_Mer/(pi q l_e/6 L_D) = 1.1 at q l_e = {xb:.2f}")
# cross-check small-q form against the full Lindhard at the worked-example point
xq = q * LE
print(f"cross-check at x = {xq:.4f}: small-q ratio {ratio_small_q(xq, wg):.5f} vs full {LM/LD:.5f}")

print("\n=== Amorphous WSi ===")
EFW = 7.0
KFW = np.sqrt(2 * ME * EFW)
VFW = KFW / ME
print(f"free electron at E_F = 7 eV: k_F = {KFW:.1f} eV = {KFW/HBARC_NM*1e0:.2f} nm^-1 (k_F = {KFW/HBARC_NM:.2f} /nm), "
      f"v_F = {VFW:.4e} = {VFW*C:.3e} m/s, 2pi/k_F = {2*np.pi*HBARC_NM/KFW:.3f} nm")
NEW = KFW**3 / (3 * np.pi**2)
WPW = np.sqrt(E2 * NEW / ME)
print(f"free-electron omega_p = {WPW:.2f} eV")
dos_free = ME * KFW / np.pi**2  # eV^2, both spins
conv = (1 / (HBARC_NM * 1e-9))**3 / QE   # eV^2 -> m^-3 J^-1
print(f"free-electron 2N_F = {dos_free*conv:.3e} m^-3 J^-1; measured 2.6e47-4.1e47 -> ratio {2.6e47/(dos_free*conv):.2f}-{4.1e47/(dos_free*conv):.2f}")
for D in (0.70, 0.75):
    l = 3 * D * 1e-4 / (VFW * C)
    print(f"D = {D} cm^2/s: l_e = 3D/v_F = {l*1e9:.3f} nm, k_F l_e = {KFW*l*1e9/HBARC_NM:.2f}, gamma = v_F/l = "
          f"{VFW*HBARC_NM/(l*1e9):.2f} eV, 1/l_e = {HBARC_NM/(l*1e9)/1000:.2f} keV")
for Rs in (326.0, 417.0):
    rhoW = Rs * 5e-9
    g = EPS0 * (WPW / HBAR_EVS)**2 * rhoW * HBAR_EVS   # eV
    l = VFW * HBARC_NM / g
    print(f"R_s = {Rs} Ohm, d = 5 nm: rho = {rhoW*1e8:.0f} microOhm cm; gamma = eps0 omega_p^2 rho = {g:.2f} eV; "
          f"l_e = v_F/gamma = {l:.3f} nm; k_F l_e = 2E_F/gamma = {2*EFW/g:.2f}")
print(f"QROCODILE Gamma = 0.1 E_F = {0.1*EFW:.1f} eV")
print(f"Al plasmon width 0.863 eV over gamma_rel of the 50 nm film: {0.863/GAM:.1f}; 30 nm conserving (0.187) over the local limit at y = 2.2: {0.187/(mb1(2.2)/(mb1(2.2)**2+mb2(2.2)**2)/gI(2.2)):.2f}")
# Zhang et al. Table I rows (x, B in mT, R_s in Ohm, D in cm^2/s, tabulated N_0 in m^-3 J^-1); Einstein relation
# sigma = e^2 N D with rho = R_s d, d = 5 nm, gives N = 1/(e^2 R_s d D)
rows = [(0.75, 410, 0.71, 2.7e47), (0.75, 417, 0.70, 2.6e47), (0.80, 340, 0.71, 3.2e47), (0.80, 357, 0.70, 3.1e47),
        (0.85, 326, 0.73, 4.1e47), (0.85, 350, 0.75, 3.8e47)]
Ns = []
for xw, Rs, Dz, N0 in rows:
    N = 1 / (QE**2 * Rs * 5e-9 * Dz * 1e-4)
    Ns.append(N)
    print(f"Zhang x = {xw}, R_s = {Rs} Ohm, D = {Dz}: Einstein 1/(e^2 rho D) = {N:.2e} m^-3 J^-1 (tabulated {N0:.1e})")
print(f"Einstein-relation range {min(Ns):.2e} - {max(Ns):.2e}; over the free gas {min(Ns)/(dos_free*conv):.2f} - {max(Ns)/(dos_free*conv):.2f};"
      f" bound from rho >= 163 uOhm cm and D >= 0.70: {1/(QE**2*1.63e-6*0.70e-4):.2e}")
DW = 1.764 * 1.73 * 8.617333e-5
print(f"Delta = 1.764 T_c (T_c = 1.73 K) = {DW*1e3:.3f} meV; edge q = 2 Delta/v_max = {2*DW/VMAX:.3f} eV")
lW = 3 * 0.70e-4 / (VFW * C) * 1e9
print(f"q l_e at the edge (l_e = {lW:.3f} nm): {2*DW/VMAX*lW/HBARC_NM:.2e}")
for qk in (1.0, 5.0):
    print(f"q = {qk} keV: q l_e = {qk*1000*lW/HBARC_NM:.2f}, q/k_F = {qk*1000/KFW:.2f}")
print(f"l_e/xi(0) = {lW/7.0:.3f} (xi(0) = 7.0 nm)")
xiW = VFW / (np.pi * DW) * HBARC_NM
print(f"clean v_F/(pi Delta) for WSi with Delta = {DW*1e3:.3f} meV: {xiW:.0f} nm")

# ---------------- figure ----------------
plt.rcParams.update({"font.size": 9, "axes.labelsize": 9, "legend.fontsize": 7.5, "pdf.fonttype": 42})
fig, (a, b) = plt.subplots(1, 2, figsize=(7.0, 2.9))
qs = np.logspace(np.log10(0.05), np.log10(6000), 160)
Lm = np.array([loss(eps_mermin(x, w, GAM)) for x in qs])
Lm1 = np.array([loss(eps_mermin(x, w, VF / (1000 / HBARC_NM))) for x in qs])
Ll = np.array([loss(eps_lin(x, mp.mpc(w, 1e-30))) for x in qs])
Ln = np.array([loss(eps_lin(x, mp.mpc(w, GAM))) for x in qs])
blue, red, grey = "#1f4e9c", "#c0392b", "0.45"
Ll_plot = np.where(Ll > 0, Ll, np.nan)
a.loglog(qs, Ll_plot, color="k", lw=1.3, label="bulk, clean (Lindhard)")
a.loglog(qs, Lm, color=blue, lw=1.3, label=r"film, $\mathfrak{l}_e = 50$ nm (Mermin)")
a.loglog(qs, Lm1, color=blue, lw=1.0, ls="--", label=r"$\mathfrak{l}_e = 1\ \mu$m (Mermin)")
a.axhline(w * GAM / WP**2, color=grey, lw=0.8, ls="-.")
a.text(2e2, w * GAM / WP**2 * 1.35, "Drude, 50 nm", fontsize=7, color=grey)
a.axvspan(qs[0], q, color="0.88", lw=0)
a.text(0.055, 1.2e-6, "kinematically\nforbidden", fontsize=6.5, color="0.35")
a.axvline(1 / LE, color=grey, lw=0.7, ls=(0, (2, 2)))
a.text(1 / LE * 1.15, 1.5e-10, r"$q\mathfrak{l}_e = qd = 1$", fontsize=7, color=grey, rotation=90, va="bottom")
a.set_xlabel(r"$q$ (eV)")
a.set_ylabel(r"$L(q,\omega)$")
a.set_xlim(qs[0], qs[-1])
a.set_ylim(1e-10, 1e-5)
a.legend(loc="lower right", frameon=False, fontsize=6.5)
a.text(-0.2, 1.05, "(a)", transform=a.transAxes, fontsize=9)
b.loglog(xs, rs, color=blue, lw=1.3, label="Mermin / Drude")
b.loglog(xs, np.pi * xs / 6, color="k", lw=0.8, ls="--", label=r"$\pi q\mathfrak{l}_e/6$")
b.axhline(1, color="k", lw=0.8, ls="-.")
b.axvspan(xs[0], dif_ok.max(), color="#dbe6f5", lw=0)
b.axvspan(bal_ok.min(), xs[-1], color="#f3e3d3", lw=0)
b.text(2e-3, 0.3, "diffusive", fontsize=7)
b.text(1.5e1, 0.15, "ballistic", fontsize=7)
b.set_xlabel(r"$q\mathfrak{l}_e$")
b.set_ylabel(r"$L/L_{\mathrm{Drude}}$")
b.set_xlim(1e-3, 1e3)
b.set_ylim(0.1, 300)
b.legend(loc="upper left", frameon=False, fontsize=6.5)
b.text(-0.2, 1.05, "(b)", transform=b.transAxes, fontsize=9)
fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT)
print(f"\nwrote {os.path.relpath(OUT, HERE)}")
