"""Fig. 14.1 (fig:14-nio-rate): one-magnon rate of NiO against the dark-matter mass for a spin-dependent contact
interaction O_4 = S_chi.S_e (heavy mediator), with the numbers quoted in Sect. 14.1.

Rate (eq:8.2-spectrum with D_ab = |c_4|^2 delta_ab/4 and the one-magnon response eq:14.1-Safm; isotropic halo kernel
of eq:A.8-eta, i.e. averaged over crystal orientations relative to the dark-matter wind; T = 0):
  R(omega_th) = rho_chi/(m_chi rho_T) * pi |c_4|^2 |S|/(2 Omega) * int d^3q/(2pi)^3 |F(q)|^2 w_q eta(v_min)/(2q)
                 * Theta(omega^M_q - omega_th),
  v_min = omega^M_q/q + q/(2 m_chi), w_q = |S|(A_q - B_q)/omega^M_q (eq:D.38-weight), Omega = a^3/4 per Ni ion.
  Reference cross-section of the free electron with the same operator (TZZ 1905.13744 Eq. (11) at F_DM = 1):
  sigma_e = mu_chie^2 <|V|^2>/pi with the spin average <|c_4 S_chi.S_e|^2> = 3|c_4|^2/16, so
  |c_4|^2 = 16 pi sigma_e/(3 mu_chie^2).  Plotted: events per kg-year at sigma_e = 1e-40 cm^2.
Modelling choices (named in the caption): Heisenberg J1, J2 of Hutchings-Samuelsen, no anisotropy and no rhombohedral
  distortion (gapless), |S| = 1, Ni2+ <j0> form factor (magnon14.py); orientation-averaged kernel; thresholds 5, 20,
  50 meV.  Sensitivity runs: (i) F = 1 (the setting of the literature formula); (ii) an easy-axis single-ion term K
  added to A_k, K chosen so that the zone-centre gap is 4.54 meV, the zone-centre magnon energy of NiO from far-infrared
  absorption used by dos Santos et al., PRB 113, 024427 (2026), Sect. III, threshold 5 meV.
Halo and constants as figscripts/ch10/rate10_2.py: v0 = 238, v_esc = 544, v_E = 250.5 km/s; rho_chi = 0.3 GeV/cm^3;
  eta in the closed form of App. D.1.  NiO density rho_T = 4 M_NiO/a^3 with M_NiO = 58.693 + 15.999 u (IUPAC
  standard atomic weights), a = 4.17 A: 6.84 g/cm^3.
Grid: q log-spaced (2000 points, 1 eV to 60 keV) x 2000 Fibonacci directions; convergence checked by halving both.
Outputs: tex/figures/ch14/fig14_1.pdf; figscripts/ch14/fig14_1.log (all numbers).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import erf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import magnon14 as m

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch14", "fig14_1.pdf")
LOG = open(os.path.join(HERE, "fig14_1.log"), "w")


def out(s):
    print(s)
    LOG.write(s + "\n")


ME = 510998.95
HBARC = 1973.269804           # eV A
CKM = 299792.458
EV_S, KG_EV, YR_S, CM = 1.519267e15, 5.609589e35, 3.15576e7, 5.067731e4
U_G = 1.66053907e-24
V0, VESC, VE = 238.0, 544.0, 250.5
VMAX = (VESC + VE) / CKM
RHO_CHI = 0.3e9 / CM**3
M_NIO = 58.693 + 15.999
RHO_G = 4 * M_NIO * U_G / (m.A_NIO * 1e-8)**3
RHO_T = RHO_G * 1e-3 * KG_EV / CM**3
OMEGA = m.A_NIO**3 / 4 / HBARC**3          # eV^-3 per Ni ion
SIG = 1e-40 * CM**2
_Z = VESC / V0
_NESC = np.pi**1.5 * V0**3 * (erf(_Z) - 2 / np.sqrt(np.pi) * _Z * np.exp(-_Z**2))


def eta(vmin):
    u = np.maximum(np.asarray(vmin) * CKM, 0.0)
    k = np.pi * V0**2 / (VE * _NESC)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + VE) / V0) - erf((u - VE) / V0)) - 2 * VE * np.exp(-_Z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(_Z) - erf((u - VE) / V0)) - (VESC + VE - u) * np.exp(-_Z**2))
    return np.where(u < VESC - VE, b1, np.where(u < VESC + VE, b2, 0.0)) * CKM


def fib(n):
    i = np.arange(n) + 0.5
    th = np.arccos(1 - 2 * i / n)
    ph = np.pi * (1 + 5**0.5) * i
    return np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], -1)


def tables(nq, nd, kani=0.0):
    q = np.geomspace(1.0, 6e4, nq)                      # eV
    lnq = np.log(q)
    dlnq = np.gradient(lnq)
    dirs = fib(nd)
    om = np.empty((nq, nd))
    w = np.empty((nq, nd))
    for i, qq in enumerate(q):
        kv = dirs * (qq / HBARC)                          # A^-1
        a, b = m.ab_nio(kv, kani=kani)
        om[i] = m.omega(a, b)                             # meV
        w[i] = m.weight(a, b)
    f2 = m.fmag_ni2(q / HBARC)**2
    return q, dlnq, om, w, f2


def rate(mchi, wth, tab, use_f=True):
    q, dlnq, om, w, f2 = tab
    mu = mchi * ME / (mchi + ME)
    c4sq = 16 * np.pi * SIG / (3 * mu**2)
    pref = RHO_CHI / (mchi * RHO_T) * np.pi * c4sq * m.S_NIO / (2 * OMEGA)
    vmin = (om * 1e-3) / q[:, None] + q[:, None] / (2 * mchi)
    integrand = w * eta(vmin) * (om >= wth)
    ang = integrand.mean(1) * (f2 if use_f else 1.0)
    # int d^3q/(2pi)^3 X/(2q) = (1/4pi^2) int q dq <X>_dir = (1/4pi^2) int q^2 dlnq <X>
    val = pref / (4 * np.pi**2) * np.sum(q**2 * ang * dlnq)
    return val * EV_S * KG_EV * YR_S


out(f"rho_T(NiO) = {RHO_G:.3f} g/cm^3; Omega per Ni = {m.A_NIO**3/4:.3f} A^3; v_max = {VMAX:.4e}")
out(f"Brown <j0> coefficients match periodictable: {m.check_brown()}")
for qa in (0.5, 1.0, 1.305, 2.0, 2.7, 4.0):
    out(f"  F^mag(Ni2+) at q = {qa} A^-1 ({qa*HBARC/1e3:.2f} keV): {m.fmag_ni2(qa):.3f}; |F|^2 = {m.fmag_ni2(qa)**2:.3f}")

masses = np.geomspace(5e3, 1e7, 60)
tab = tables(2000, 2000)
tab_c = tables(1000, 1000)
# gap model: K with |S| sqrt((A0+K)^2 - A0^2) = Delta
A0 = 6 * (m.J1 + m.J2)                 # A_0 = J_AB(0)
DELTA = 4.54
K = -A0 + np.sqrt(A0**2 + (DELTA / m.S_NIO)**2)
out(f"easy-axis K = {K:.4f} meV for a zone-centre gap of {DELTA} meV (A_0 = 6(J1 + J2) = {A0:.2f} meV)")
kk = np.array([[0, 0, 0], m.Q_AF])
aa, bb = m.ab_nio(kk, kani=K)
out(f"  check: omega(Gamma) = {m.omega(aa, bb)[0]:.3f} meV, omega(Q_AF) = {m.omega(aa, bb)[1]:.3f} meV")
tab_g = tables(2000, 2000, kani=K)

curves = {}
for wth in (5.0, 20.0, 50.0):
    curves[wth] = np.array([rate(mm, wth, tab) for mm in masses])
curves["nof"] = np.array([rate(mm, 5.0, tab, use_f=False) for mm in masses])
curves["gap"] = np.array([rate(mm, 5.0, tab_g) for mm in masses])

out("\nRate R (events / kg / yr) at sigma_e = 1e-40 cm^2, heavy mediator, O_4:")
for mm in (1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7):
    r5 = rate(mm, 5.0, tab)
    r5c = rate(mm, 5.0, tab_c)
    out(f"  m = {mm/1e3:8.0f} keV: wth=5 meV {r5:.3e} (coarse grid {r5c:.3e}, ratio {r5c/r5 if r5 else 0:.3f});"
        f" 20 meV {rate(mm, 20.0, tab):.3e}; 50 meV {rate(mm, 50.0, tab):.3e};"
        f" F=1 {rate(mm, 5.0, tab, use_f=False):.3e}; gap model {rate(mm, 5.0, tab_g):.3e}")
for wth in (5.0, 20.0, 50.0):
    r = curves[wth]
    nz = masses[r > 0]
    out(f"  lightest mass with nonzero rate on the mass grid, wth = {wth} meV: {nz[0]/1e3:.1f} keV;"
        f" kinematic estimate wth/(2 c (v_max - c)) with c = 1.39e-4: {wth*1e-3/(2*1.39e-4*(VMAX-1.39e-4))/1e3:.1f} keV")
i1 = np.argmin(abs(masses - 1e6))
out(f"  F^mag suppression at 1 MeV (5 meV): {curves[5.0][i1]/curves['nof'][i1]:.3f}")
out(f"  gap model / gapless at 5 meV: 30 keV {rate(3e4, 5.0, tab_g)/rate(3e4, 5.0, tab):.3f},"
    f" 100 keV {rate(1e5, 5.0, tab_g)/rate(1e5, 5.0, tab):.3f}, 1 MeV {rate(1e6, 5.0, tab_g)/rate(1e6, 5.0, tab):.3f}")

# large-mass check: incoherent scattering off ionic spins with the one-magnon weight |S|(1 + 2 Delta S) per ion,
# R_inc = (rho_chi/m)(1/(rho_T Omega)) <v> sigma_e (m/mu)^2 (4/3)|S|(1 + 2 Delta S), F = 1, <v> = 2 int u eta(u) du
DS = 0.0785   # Delta S of NiO, we14_1.log
uu = np.linspace(0, VMAX, 20001)
vmean = 2 * np.trapezoid(uu * eta(uu), uu)
out(f"\nmean laboratory speed <v> = {vmean:.4e} = {vmean*CKM:.1f} km/s")
for mm in (3e6, 1e7):
    mu = mm * ME / (mm + ME)
    rinc = RHO_CHI / mm / (RHO_T * OMEGA) * vmean * SIG * (mm / mu)**2 * (4 / 3) * m.S_NIO * (1 + 2 * DS)
    rinc *= EV_S * KG_EV * YR_S
    rf = rate(mm, 5.0, tab, use_f=False)
    out(f"  m = {mm/1e6:.0f} MeV: F = 1 rate {rf:.4e}, incoherent-spin estimate {rinc:.4e}, ratio {rf/rinc:.3f}")

# share of the rate from |q| < |Q_AF|/2 (near Gamma) at selected masses
q, dlnq, om, w, f2 = tab
for mm in (1e5, 1e6):
    mu = mm * ME / (mm + ME)
    vmin = (om * 1e-3) / q[:, None] + q[:, None] / (2 * mm)
    ang = (w * eta(vmin) * (om >= 5.0)).mean(1) * f2
    tot = np.sum(q**2 * ang * dlnq)
    qa = q / HBARC
    near = np.sum((q**2 * ang * dlnq)[qa < 0.5 * np.linalg.norm(m.Q_AF)])
    out(f"  m = {mm/1e3:.0f} keV: share of the 5 meV rate from |q| < |Q_AF|/2 = {near/tot:.3f}")

plt.rcParams.update({"font.size": 8.5})
fig, ax = plt.subplots(figsize=(4.6, 3.3))
col = {5.0: "C0", 20.0: "C1", 50.0: "C2"}
for wth in (5.0, 20.0, 50.0):
    ax.loglog(masses / 1e6, np.where(curves[wth] > 0, curves[wth], np.nan), color=col[wth],
              label=rf"$\omega_{{\mathrm{{th}}}} = {wth:.0f}$ meV")
ax.loglog(masses / 1e6, np.where(curves["nof"] > 0, curves["nof"], np.nan), color="C0", ls=":",
          label=r"5 meV, $F^{\mathrm{mag}} = 1$")
ax.loglog(masses / 1e6, np.where(curves["gap"] > 0, curves["gap"], np.nan), color="C0", ls="--",
          label="5 meV, gap 4.54 meV")
qaf = np.linalg.norm(m.Q_AF) * HBARC
ax.axvline(qaf / (2 * VMAX) / 1e6, color="0.5", lw=0.6, ls="-.")
ax.text(qaf / (2 * VMAX) / 1e6 / 1.1, 2e-2, r"$2m_\chi v_{\mathrm{max}} = |\mathbf{Q}_{\mathrm{AF}}|$", fontsize=7,
        color="0.3", ha="right")
ax.set_xlabel(r"$m_\chi$ (MeV)")
ax.set_ylabel(r"$\mathcal{R}$ (events kg$^{-1}$ yr$^{-1}$)")
ax.set_xlim(5e-3, 10)
ax.set_ylim(1e-2, 1e4)
ax.legend(fontsize=7, frameon=False, loc="lower right")
fig.tight_layout()
fig.savefig(OUT)
out(f"wrote {OUT}")
LOG.close()
