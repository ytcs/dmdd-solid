"""Sect. 17.2 (absorption across channels): Fig. 17.2 (fig:17-abs-coverage), Worked example 17.2 (we:17-handover) and
every number printed in Sect. 17.2.  Log: abs17_2.log.  Run: python abs17_2.py > abs17_2.log  (about a minute).

Nothing here is new physics: each curve re-evaluates a rate that an earlier section derived, with that section's inputs,
by importing that section's script.  Natural units, Heaviside-Lorentz e^2 = 4 pi alpha; rho_chi = 0.3 GeV/cm^3;
reach = coupling for 3 events in 1 kg yr without background.

Curves and their sources (book section, equation, script):
  Two-level systems of thermal SiO2 (Sect. 16.7, eq:16.7-dp; tls16_7.py): R = (rho_chi/rho_T) zeta^2 tan(d0) tanh(m/2T)/eps_r,
      tan d0 = 3.0e-4 (O'Connell et al. 2008, Table I), eps_r = 3.9 (assumed value of Sect. 16.7), rho_T = 2.2 g/cm^3, T = 10 mK.
      Drawn up to the crossing with the vibrational absorption of the glass, 0.4636 meV (limit16_7d.log).
  Vibrational (Ioffe-Regel) absorption of g-SiO2 (Sect. 16.7, Limit Check 16.7d; limit16_7d.py, reimplemented with its
      constants: A = 4000 cm^-2, B = 0.3, Theta_D = 330 K, eps_1 = 3.9), drawn from 0.4636 meV to omega_IR = 35 cm^-1.
  Clean aluminum, phonon-assisted (Holstein) conductivity with the Debye transport function (Sect. 15.4, eq:15.4-holstein;
      abs15.py: Delta = 0.18 meV, omega_p = 12.29 eV, lambda_tr = 0.39, omega_D = 37 meV), dark photon through the clean
      condensate loss function, ALP through eq:10.7-alp with the same sigma_1 (the published route, dashed).
  Clean aluminum, direct spin-current pair breaking (Sect. 15.4, eq:15.4-sJ; abs15.sigmaJ_direct) times the quasiparticle
      factor 1/(1 + lambda_ep) = 1/1.43 that Sect. 15.4 quotes, ALP; drawn up to its crossing with the phonon-assisted sigma_1, 10.9 meV.
  Si:P donors at 1e15 cm^-3 (Sect. 16.5; we16_5.log, central-cell model CC0.10): 2p0 line at 34.11 meV, zeta = 2.33e-16
      (width 4.22 ueV); continuum at 50 meV, zeta = 4.85e-15.  Quoted from that log, not recomputed.
  ZrTe5 with the background in the total epsilon (Sect. 16.1; dirac16.py): per-polarization loss function along the principal
      axes, unpolarized average, rho_T = 6.135 g/cm^3, the parameters of dirac16.ZRTE5 (v_i, Lambda_i, eps_bg,ii, g = 2) with
      the half-gap Delta_D = 11.8 meV with the measured-structure row (v, Lambda of 1910.02091 Table 1, Lt = 0.191 eV; the
      central row of Sect. 16.1) and 15.6 meV with the relaxed-cell ISIF7 row (Lt = 0.180 eV).  Modelling choice: the
      other parameters are kept at the ISIF7 row for both half-gaps.
  GaAs and sapphire single-phonon lines (Sect. 11.8, Fig. 11.8; abs11_8.py): damped factorized dielectric functions, GaAs widths
      1 % of each frequency, sapphire 77 K widths; electron-coupled scalar in GaAs through eq:11.8-Rscalar with Z* = 2.11,
      eps_inf = 10.88 (residue d = -1.21e-3 per u), <v^2>^(1/2) = 379 km/s.
  Silicon electrons (Sect. 10.7; abs10_7.py): measured 300 K optical constants (Franta et al. 2017) below 40 eV, Henke tables above,
      untransferred; drawn from the excitonic edge of cold silicon, 1.1728 eV.  Near the edge the cold excitonic model of
      Sect. 13.8 (fig13_8.py, Eq. 13.8-edge, TA + TO branches with weights 5.5 : 4.0, E_x^b = 14.7 meV, scale fitted to the
      300 K data on 1.18-1.30 eV as there) is drawn dotted up to 1.30 eV.  Scalar: the kinetic-row model spectrum of
      si_scalar10_7.npz (empirical pseudopotential, smoothed over 0.25 eV as in Fig. 10.6).
  YIG Kittel line (Sect. 14.3, eq:14.3-peak, Worked example 14.3): rho_T Omega = 2951.8 u, s_net = 10, lambda_S = 1, assumed
      Gamma_M = 1e-5 omega (Mitridate et al., Sect. V B), <v_perp^2> = v0^2 + vE^2 = 1.327e-6 (z perpendicular to v_E).
      ALP: the peak rate as the line is tuned, 9.49 ueV (sphere saturation) to 1.158 meV (10 T).
      Dark photon (through B' = i p x e A', Sect. 14.3): g_aee^2 <v_perp^2> -> e^2 zeta^2 <|(v x e)_perp|^2>, with the
      polarization e isotropic and independent of v: <|(v x e)_perp|^2> = (<v^2> + <v_z^2>)/3, <v^2> = 3 v0^2/2 + vE^2,
      <v_z^2> = v0^2/2 (truncation neglected, as for <v_perp^2> in Sect. 14.3); vacuum zeta.
  MnF2 AFMR line at the measured 1.1 meV (Sect. 14.3): 2.6e-2 s^-1 kg^-1 at g_aee = 1e-13 (quoted from the text of Sect. 14.3).
Coherent against counting readout (Sect. 17.2-coherent): thermal occupation n_B(m) = 1/(e^{m/T} - 1) of the readout mode;
  quantum-limited linear readout noise n_B + 1 quanta per mode (Lamoreaux et al., arXiv:1306.3591, Eq. (9)); counting noise from
  the variance of thermal counts, N_th + N_th^2/N_coh (Sect. 14.6), N_th = n_B N_coh; N_coh = t_int Delta_omega_eq/(2 pi) with
  Delta_omega_eq = 2.67 m v0^2 (Sect. 14.6); background-free counting when N_th < 0.05 (Lamoreaux et al., Eq. (20)), with
  3 signal quanta (their Eq. (19)); linear readout at the weak-signal threshold t = 2.71 of Sect. 14.6, t = N_sig^2/(N_coh (n_B+1)^2).
Handover GaAs -> Si (WE 17.2): equal rate per kg needs L_GaAs/rho_GaAs = L_Si/rho_Si, with L = eps_2/|eps|^2 ~ n alpha (hbar c/omega)/n^4
  below a gap (eps_2 << eps_1); GaAs n at 22 C from the Skauli dispersion formula (book/sources/12.6/gaas_skauli.yml), Si n from
  Franta 300 K; rho_GaAs = 5.361 (Sect. 11.8), rho_Si = 2.33 g/cm^3.
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
np.seterr(over="ignore")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "..", "..")
FIG = os.path.join(BOOK, "tex", "figures", "ch17")
os.makedirs(FIG, exist_ok=True)
for sub in ("ch16", "ch15", "ch11", "ch10"):
    sys.path.insert(0, os.path.join(HERE, "..", sub))

import rate10_2 as R10   # noqa: E402
import abs10_7 as SI     # noqa: E402
import abs11_8 as GA     # noqa: E402
import abs15 as AL       # noqa: E402
import tls16_7 as TL     # noqa: E402
import dirac16 as DI     # noqa: E402

NEV = 3.0
E2 = 4 * np.pi * R10.ALPHA
ME = R10.ME
KELVIN = 8.617333e-5
HBAR_EVS = 6.582119569e-16


def reach(R):
    """Coupling for NEV events in 1 kg yr from a rate per unit squared coupling [1/(kg yr)]."""
    R = np.asarray(R, float)
    return np.where(R > 0, np.sqrt(NEV / np.where(R > 0, R, 1.0)), np.nan)


out = print
out("=== Sect. 17.2: absorption across channels ===")

# ---------------------------------------------------------------------------------------------- TLS and glass
T_MK = 0.010 * KELVIN
PRE_TL = TL.RHO_CHI / TL.RHO_T * TL.KG * TL.YEAR
m_tls = np.geomspace(1e-9, 0.4636e-3, 400)
R_tls = PRE_TL * TL.TAND_THERMAL / TL.EPS_R * np.tanh(m_tls / (2 * T_MK))
CM1 = 1.239841984e-4
A_IR, B_IR, WD_IR, WIR = 4000.0, 0.3, 330.0 * 0.6950348, 35.0


def L_ir(wt):
    a = (A_IR + B_IR * wt**2) * 3 * wt**2 / WD_IR**3
    e2 = np.sqrt(TL.EPS_R) * a / (2 * np.pi * wt)
    return e2 / (TL.EPS_R**2 + e2**2)


m_ir = np.geomspace(0.4636e-3, WIR * CM1, 100)
R_ir = PRE_TL * L_ir(m_ir / CM1)
m6 = 6 * 4.135667696e-6
out("TLS (thermal SiO2, tan d0 = 3.0e-4, eps_r 3.9, 10 mK): R/zeta^2 at 6 GHz = %.3e, zeta = %.3g; at 1 ueV: zeta = %.3g; "
    "at 0.1 ueV: tanh factor %.3f, zeta = %.3g" % (
        PRE_TL * TL.TAND_THERMAL / TL.EPS_R * np.tanh(m6 / 2 / T_MK),
        reach(PRE_TL * TL.TAND_THERMAL / TL.EPS_R * np.tanh(m6 / 2 / T_MK)),
        reach(PRE_TL * TL.TAND_THERMAL / TL.EPS_R * np.tanh(1e-6 / 2 / T_MK)),
        np.tanh(1e-7 / 2 / T_MK), reach(PRE_TL * TL.TAND_THERMAL / TL.EPS_R * np.tanh(1e-7 / 2 / T_MK))))
out("glass vibrational: zeta at 0.4636 meV = %.3g, at 1.24 meV = %.3g, at omega_IR = %.3f meV: %.3g" % (
    reach(R_ir[0]), reach(PRE_TL * L_ir(10.0)), WIR * CM1 * 1e3, reach(R_ir[-1])))

# ---------------------------------------------------------------------------------------------- aluminum
m_al = np.geomspace(2 * AL.DELTA * 1.03, 30e-3, 160)
s1S = np.array([AL.sigma_holstein(w) for w in m_al])
R_al_dp = np.array([AL.rate_darkphoton(w, s) for w, s in zip(m_al, s1S)])
R_al_alpS = np.array([AL.rate_alp(w, s) for w, s in zip(m_al, s1S)])
QPF_AL = 1 / 1.43                 # quasiparticle factor 1/(1 + lambda_ep), lambda_ep = 0.43 (Sects. 6.4, 15.4)
sJ_al = lambda w: QPF_AL * AL.sigmaJ_direct(w)  # noqa: E731
m_alJ = np.geomspace(2 * AL.DELTA * (1 + 1e-4), 10.9e-3, 300)   # above 10.9 meV the phonon-assisted part dominates (Sect. 15.4)
R_al_alpJ = AL.rate_alp(m_alJ, sJ_al(m_alJ))
i1 = np.argmin(abs(m_al - 1e-3))
out("Al clean, dark photon (Holstein): zeta at %.3f meV = %.3g (WE 15.4: 1.5e-9); best over 0.37-30 meV: %.3g at %.2f meV" % (
    m_al[i1] * 1e3, reach(R_al_dp[i1]), np.nanmin(reach(R_al_dp)), m_al[np.nanargmin(reach(R_al_dp))] * 1e3))
w072 = 4 * AL.DELTA
out("Al clean, ALP at 0.72 meV: spin current g = %.3g (15.4: 6.1e-13; bare form %.3g); phonon-assisted sigma_1 route g = %.3g (15.4: 5.6e-9)" % (
    reach(AL.rate_alp(w072, sJ_al(w072))), reach(AL.rate_alp(w072, AL.sigmaJ_direct(w072))), reach(AL.rate_alp(w072, AL.sigma_holstein(w072)))))
out("Al clean, ALP spin current: g at 10 meV = %.3g, at 100 meV = %.3g" % (
    reach(AL.rate_alp(10e-3, sJ_al(10e-3))), reach(AL.rate_alp(0.1, sJ_al(0.1)))))
# condensate screening: eps_1 at 1 meV and the bound L <= 1/(2|eps_1|)
eps1_al = 1 - AL.WP**2 / 1e-3**2
out("Al at 1 meV: eps_1 = %.3g, bound 1/(2|eps_1|) = %.3g" % (eps1_al, 1 / (2 * abs(eps1_al))))

# ---------------------------------------------------------------------------------------------- donors (quoted)
SIP_LINE = (34.11e-3, 2.33e-16)
SIP_CONT = (50e-3, 4.85e-15)
out("Si:P 1e15 cm^-3 (we16_5.log, CC0.10): 2p0 line %.2f meV zeta = %.3g; continuum 50 meV zeta = %.3g" % (
    SIP_LINE[0] * 1e3, SIP_LINE[1], SIP_CONT[1]))

# ---------------------------------------------------------------------------------------------- ZrTe5
ZP = DI.ZRTE5                      # relaxed-cell row (ISIF7) of 1910.02091: Delta_D = 15.6 meV, Lt = 0.180 eV
# measured-structure row of 1910.02091 Table 1 (as Sect. 16.1, zrte5_16.py): v = (1.1, 0.45, 1.0)e-3,
# Lambda_i = (0.23, 0.215, 0.1) 1/A, Lt = min_i v_i Lambda_i = 0.191 eV, Delta_D = 11.8 meV (central value of Sect. 16.1)
ZM = dict(ZP, v=np.array([1.1e-3, 4.5e-4, 1.0e-3]), Lam=np.array([0.23, 0.215, 0.1]), D=11.8e-3)
ZM["Lt"] = float(np.min(ZM["Lam"] * DI.HBARC * ZM["v"]))
Z = ZM
rhoZ = ZP["rho_src"] * DI.GCM3
zr = {}
for D, Z in ((11.8e-3, ZM), (15.6e-3, ZP)):
    Bt = DI.Btab(D, Z["Lt"])
    ma = np.geomspace(2 * D * 1.0005, 2 * Z["Lt"] * 0.999, 300)
    Lp = DI.abs_L_pol(ma, Z, Bt)
    zb = DI.zeta_lim(Lp.mean(axis=1), rhoZ)
    zs = DI.zeta_lim((Lp * Z["ebg"]).mean(axis=1), rhoZ)
    zr[D] = (ma, zb)
    j = np.argmin(abs(ma - 0.1))
    out("ZrTe5 Delta_D = %.1f meV: onset 2 Delta = %.1f meV, top 2 Lt = %.0f meV; zeta at 100 meV = %.3g (total eps), %.3g "
        "(published rule); best %.3g at %.0f meV; total/published %.2f-%.2f" % (
            D * 1e3, 2 * D * 1e3, 2 * Z["Lt"] * 1e3, zb[j], zs[j], np.nanmin(zb), ma[np.nanargmin(zb)] * 1e3,
            np.nanmin(zb / zs), np.nanmax(zb / zs)))
out("ZrTe5 rows: measured structure Lt = %.4f eV (cone end 2 Lt = %.3f eV); relaxed cell Lt = %.4f eV" % (ZM["Lt"], 2 * ZM["Lt"], ZP["Lt"]))
out("ZrTe5 eps_bg,ii = %s: bound 1/(2 eps_bg) = %.4f, %.4f, %.4f" % (Z["ebg"], *(1 / (2 * Z["ebg"]))))

# ---------------------------------------------------------------------------------------------- GaAs, sapphire
w_g = np.linspace(30e-3, 45e-3, 20001)
L_g = GA.loss(w_g, *GA.GAAS_ARGS)
R_g = GA.events_per_kgyr(L_g, GA.RHO_GAAS)
w_s = np.linspace(45e-3, 130e-3, 40001)
L_s = GA.loss_saph(w_s)
R_s = GA.events_per_kgyr(L_s, GA.RHO_SAPH)
v2, _ = GA.v2_mean()
v2n = v2 / GA.P.C_KMS**2
dG = GA.d_site(GA.ZS, GA.EPSINF)
R_gsc = GA.events_per_kgyr(L_g, GA.RHO_GAAS, v2n / E2 * (GA.EPSINF * GA.MU * dG / GA.ZS) ** 2)
out("GaAs dark photon: L peak %.3f at %.2f meV, zeta = %.3g; sapphire L peak %.3f at %.2f meV, zeta = %.3g" % (
    L_g.max(), w_g[np.argmax(L_g)] * 1e3, reach(R_g.max()), L_s.max(), w_s[np.argmax(L_s)] * 1e3, reach(R_s.max())))
out("GaAs electron scalar (residue d = %.3e per u): g = %.3g at the line center" % (dG, reach(R_gsc.max())))
out("GaAs: 1/(2 eps_inf) = %.4f ; L at the TO line %.2f meV = %.3g" % (
    1 / (2 * GA.EPSINF), GA.WT * 1e3, GA.loss(np.array([GA.WT]), *GA.GAAS_ARGS)[0]))

# ---------------------------------------------------------------------------------------------- silicon
EDGE_X = 1.1728
m_si = np.geomspace(EDGE_X, 1e4, 3000)
rs = SI.rates(m_si)
PRE_SI = SI.per_kg_yr(R10.RHO_CHI / R10.RHO_T)
out("Si: rho_chi/rho_T per kg yr = %.4e" % PRE_SI)
for m0 in (3.0, 10.0, 16.4, 100.0, 1000.0):
    r0 = SI.rates(np.array([m0]))
    out("Si at %6.1f eV: L = %.4g, |eps|^2 = %.4g, dark photon zeta = %.3g, ALP g = %.3g" % (
        m0, r0["L"][0], abs(r0["eps"][0]) ** 2, reach(r0["dp"][0]), reach(r0["alp"][0])))
k = np.argmin(reach(rs["dp"]) + (m_si > 40) * 1e9)
out("Si best dark-photon reach below 40 eV: zeta = %.3g at %.2f eV" % (reach(rs["dp"][k]), m_si[k]))
kk = np.argmin(reach(rs["alp"]))
out("Si best ALP reach (whole range to 10 keV): g = %.3g at %.1f eV" % (reach(rs["alp"][kk]), m_si[kk]))

# cold excitonic edge of Sect. 13.8 (copied from fig13_8.py)
kB = 86.17e-6
WPH = {"TA": 212 * kB, "TO": 670 * kB}
CPH = {"TA": 5.5, "TO": 4.0}
EB = 14.7e-3


def Eg(T):
    return 1.1692 - 4.9e-4 * T**2 / (T + 655.0)


def nB(w, T):
    if T <= 0:
        return 0.0
    return 1.0 / np.expm1(w / (kB * T))


def fermi(E):
    xi = np.sqrt(EB / E)
    return 2 * np.pi * xi / (-np.expm1(-2 * np.pi * xi))


def cont(x):
    if x <= 0:
        return 0.0
    f = lambda t: (np.sin(t) * np.cos(t)) ** 2 * 2 * x**2 * fermi(x * np.sin(t) ** 2)  # noqa: E731
    return 8 / np.pi * quad(f, 1e-12, np.pi / 2, limit=200)[0]


def lines(x, nmax=400):
    n = np.arange(1, nmax + 1)
    arg = x + EB / n**2
    return 32 * EB**1.5 * np.sum(np.where(arg > 0, np.sqrt(np.maximum(arg, 0)), 0) / n**3)


def alpha_x(w, T):
    tot = 0.0
    for nu in ("TA", "TO"):
        n = nB(WPH[nu], T)
        tot += CPH[nu] * ((n + 1) * (lines(w - Eg(T) - WPH[nu]) + cont(w - Eg(T) - WPH[nu]))
                          + (n * (lines(w - Eg(T) + WPH[nu]) + cont(w - Eg(T) + WPH[nu])) if n > 0 else 0.0))
    return tot


wf, ef = SI.franta()
nf = np.sqrt(ef).real
af = 2 * wf * np.sqrt(ef).imag / 1.973269804e-5      # absorption coefficient, cm^-1
fit = (wf >= 1.18) & (wf <= 1.30)
A_X = np.exp(np.mean(np.log(af[fit] / np.array([alpha_x(w, 300.0) for w in wf[fit]]))))
out("cold excitonic edge (Sect. 13.8): fitted scale A = %.1f cm^-1 eV^-2 (13.8: 42.4)" % A_X)
HC = 1.973269804e-5


def L_from_alpha(alpha_cm, w, n):
    e2 = n * alpha_cm * HC / w
    return e2 / (n**4)          # eps_2 << eps_1 = n^2 below the gap


m_cold = np.linspace(EDGE_X + 1e-5, 1.30, 300)
n_si_c = np.interp(m_cold, wf, nf)
a_cold = np.array([A_X * alpha_x(w, 0.0) for w in m_cold])
R_si_cold = PRE_SI * L_from_alpha(a_cold, m_cold, n_si_c)
R_si_cold_alp = R_si_cold * 3 * m_cold**2 / (4 * ME**2 * E2) * n_si_c**4   # ALP: sigma_1, no 1/|eps|^2
j12 = np.argmin(abs(m_cold - 1.2))
out("cold Si at 1.200 eV: alpha = %.3g cm^-1 (13.8: 2.95), zeta = %.3g (13.8: 2.13e-14); 300 K data zeta = %.3g" % (
    a_cold[j12], reach(R_si_cold[j12]), reach(SI.rates(np.array([1.2]))["dp"][0])))

# ---------------------------------------------------------------------------------------------- scalar, Si model
d = np.load(os.path.join(HERE, "..", "ch10", "si_scalar10_7.npz"))
ws, Stt = d["omega"], d["S_TT"]
Sts = np.convolve(Stt, np.ones(5) / 5, mode="same")
sel = (ws > 3.2) & (ws < 40.0)
msc = ws[sel]
R_si_sc = SI.per_kg_yr(R10.RHO_CHI / (R10.RHO_T * msc) * Sts[sel] / (2 * msc * ME**2))
k10 = np.argmin(abs(msc - 10.0))
out("Si scalar model (kinetic row): g at 10 eV = %.3g; best %.3g at %.1f eV" % (
    reach(R_si_sc[k10]), np.nanmin(reach(R_si_sc)), msc[np.nanargmin(reach(R_si_sc))]))

# ---------------------------------------------------------------------------------------------- magnets
U = 931.494e6
C_KMS = 299792.458
v0, vE = 238.0 / C_KMS, 250.5 / C_KMS
vperp2 = v0**2 + vE**2
v2tot = 1.5 * v0**2 + vE**2
vz2 = 0.5 * v0**2
vxe = (v2tot + vz2) / 3
KG_EV = 5.60958860e35
YR_S = 3.15576e7


def yig_peak(m, g2, vfac):
    gm = 1e-5 * m
    return R10.RHO_CHI * g2 * vfac * 1.0 * 10 / (ME**2 * 2951.8 * U * gm) * KG_EV / HBAR_EVS * YR_S


R_yig10 = yig_peak(10e-6, 1e-26, vperp2)
out("YIG Kittel line at 10 ueV, g_aee = 1e-13: %.3e per kg yr (%.3f per s per kg; WE 14.3: 3.63); g(3 events) = %.3g" % (
    R_yig10, R_yig10 / YR_S, 1e-13 * np.sqrt(NEV / R_yig10)))
m_yig = np.geomspace(9.49e-6, 1.158e-3, 100)
R_yig_alp = yig_peak(m_yig, 1.0, vperp2)
frac = np.pi / 2 * 1e-5
out("YIG: <v_perp^2> = %.4g, <v^2> = %.4g, <v_z^2> = %.4g, <|(v x e)_perp|^2> = %.4g; dark/ALP factor e^2 x ratio = %.4f" % (
    vperp2, v2tot, vz2, vxe, E2 * vxe / vperp2))
R_yig_dp10 = yig_peak(10e-6, E2, vxe)
out("YIG dark photon (vacuum zeta) at 10 ueV: R/zeta^2 = %.3e, zeta = %.3g; TLS film at 10 ueV zeta = %.3g" % (
    R_yig_dp10, reach(R_yig_dp10), reach(PRE_TL * TL.TAND_THERMAL / TL.EPS_R * np.tanh(10e-6 / 2 / T_MK))))
out("YIG ALP at 1.158 meV (10 T): g = %.3g" % reach(yig_peak(1.158e-3, 1.0, vperp2)))
out("tuned line averaged over one e-fold of mass: fraction (pi/2) Gamma_M/m = %.3g; YIG at 10 ueV averaged g = %.3g" % (
    frac, reach(frac * yig_peak(10e-6, 1.0, vperp2))))
R_mnf2 = 2.6e-2 * YR_S / 1e-26
out("MnF2 AFMR at 1.1 meV: R/g^2 = %.3e, g(3 events) = %.3g; e-fold averaged g = %.3g" % (
    R_mnf2, reach(R_mnf2), reach(frac * R_mnf2)))

# ---------------------------------------------------------------------------------------------- ALP in a static field
TESLA = 5.788e-5 * 2 * ME / np.sqrt(E2)          # eV^2 per tesla (as abs10_7.py)
for nm, mm, zz in (("Si plasmon", 16.45, reach(rs["dp"][k])), ("sapphire top line", w_s[np.argmax(L_s)], reach(R_s.max())),
                   ("GaAs line", GA.WL, reach(R_g.max()))):
    out("ALP in B0 = 10 T as a dark photon zeta = g B0/m: %s at %.4g eV: g_agg = %.3g GeV^-1" % (nm, mm, zz * mm / (10 * TESLA) * 1e9))
# ---------------------------------------------------------------------------------------------- loss-function bound
out("bound L <= 1/(2|eps_1|), attained at eps_2 = |eps_1|: Si below gap (eps_1 = 11.7) %.4f; a-SiO2 (3.9) %.4f" % (
    1 / (2 * 11.7), 1 / (2 * 3.9)))

# ---------------------------------------------------------------------------------------------- WE 17.2: handover GaAs -> Si
skc = [4.372514, 5.466742, 0.4431307, 0.02429960, 0.8746453, 1.957522, 36.9166]


def n_gaas(w):
    lam = 1.239841984 / w
    n2 = 1 + skc[0] + sum(skc[i] * lam**2 / (lam**2 - skc[i + 1] ** 2) for i in (1, 3, 5))
    return np.sqrt(n2)


X0 = Eg(0) + WPH["TA"] - EB
out("1s TA replica threshold E_g(0) + w_TA - E_x^b = %.6f eV" % X0)
wx = 1.175
nG, nS = n_gaas(wx), np.interp(wx, wf, nf)
fac = (nG / nS) ** 3 * GA.RHO_GAAS / 2.33
out("\nWE 17.2: n_GaAs(%.3f eV, 22 C) = %.4f; n_Si(300 K) = %.4f; alpha_GaAs needed for equal rate per kg = %.3f alpha_Si" % (
    wx, nG, nS, fac))
# square-root onset of the 1s TA replica: alpha = A C_TA 32 E_b^1.5 sqrt(w - 1.1728)
coef = A_X * CPH["TA"] * 32 * EB**1.5
out("1s TA replica onset: alpha_Si = %.3f cm^-1 x sqrt((w - %.6f eV)/eV)" % (coef, X0))
for dd in (0.1e-3, 1e-3, 5e-3, 10e-3):
    out("  %.1f meV above: alpha_Si model = %.4g cm^-1 (onset form %.4g), zeta = %.3g" % (
        dd * 1e3, A_X * alpha_x(X0 + dd, 0.0), coef * np.sqrt(dd),
        reach(PRE_SI * L_from_alpha(A_X * alpha_x(X0 + dd, 0.0), X0 + dd, nS))))
for aG in (1e-3, 1e-2, 0.1, 1.0, 10.0):
    f = lambda w: A_X * alpha_x(w, 0.0) - aG / fac  # noqa: E731
    wc = brentq(f, X0 + 1e-13, 1.30, xtol=1e-14)
    out("  GaAs alpha = %6.3f cm^-1: handover at %.6f eV, %.3g meV above the 1s threshold" % (aG, wc, (wc - X0) * 1e3))
# GaAs one-phonon line far above it: damped model values
for w0 in (0.1, 0.3, 1.0, 1.1728):
    e = GA.eps_fact(np.array([w0]), *GA.GAAS_ARGS)[0]
    out("  GaAs factorized model at %.4f eV: eps_2 = %.3g (asymptote eps_inf (gL - gT)/w = %.3g), alpha = %.3g cm^-1" % (
        w0, e.imag, GA.EPSINF * (1e-2 * GA.WL - 1e-2 * GA.WT) / w0, 2 * w0 * np.sqrt(e).imag / HC))
# Lorentz oscillator with equal widths (gamma = 1% omega_T): tail eps_2 = (eps0 - eps_inf) wT^2 gamma w/((wT^2-w^2)^2 + gamma^2 w^2)
gam = 1e-2 * GA.WT
for w0 in (0.1, 0.3, 1.1728):
    e2L = (GA.EPS0 - GA.EPSINF) * GA.WT**2 * gam * w0 / ((GA.WT**2 - w0**2) ** 2 + gam**2 * w0**2)
    out("  Lorentz oscillator (equal widths) at %.4f eV: eps_2 = %.3g, alpha = %.3g cm^-1" % (
        w0, e2L, e2L * w0 / (n_gaas(min(w0, 1.27)) * HC)))
out("GaAs gap 1.52 eV (low temperature, Sect. 3.3)")

# ---------------------------------------------------------------------------------------------- coherent vs counting
out("\n--- coherent (linear) readout against counting ---")
V0 = 238.0 / C_KMS


def ncoh(m, t):
    dw = 2.67 * m * V0**2 / HBAR_EVS          # rad/s
    return t * dw / (2 * np.pi)


for x in (0.25, 1.0, 2.0, 4.0, 10.0):
    nb = 1 / np.expm1(x)
    out("m/T = %5.2f: n_B = %.4g; counting/linear SNR ratio sqrt((n_B+1)/n_B) = e^(m/2T) = %.4g; in coupling %.4g" % (
        x, nb, np.sqrt((nb + 1) / nb), np.exp(x / 4)))
for T in (0.010, 0.100):
    for t, tl in ((3600.0, "1 h"), (86400.0, "1 day")):
        f = lambda m: (1 / np.expm1(m / (T * KELVIN))) * ncoh(m, t) - 0.05  # noqa: E731
        mbf = brentq(f, 1e-8, 1e-3, xtol=1e-14)
        out("T = %3.0f mK, t_int = %s: background-free counting (N_th < 0.05) above m = %.3g ueV (%.2f GHz), m/T = %.2f, "
            "N_coh = %.3g" % (T * 1e3, tl, mbf * 1e6, mbf / 4.135667696e-6, mbf / (T * KELVIN), ncoh(mbf, t)))
for m, T, t in ((10e-6, 0.010, 86400.0), (24.81e-6, 0.010, 86400.0), (1e-9, 4.2, 3600.0), (1e-9, 0.010, 3600.0),
                (1e-6, 0.010, 86400.0)):
    nb = 1 / np.expm1(m / (T * KELVIN))
    Nc = ncoh(m, t)
    Nlin = np.sqrt(2.71 * Nc) * (nb + 1)
    Nth = nb * Nc
    if Nth < 0.05:
        Ncnt = 3.0
    else:
        Ncnt = np.sqrt(2.71 * (Nth + Nth**2 / Nc))
    out("m = %.3g eV, T = %.3g K, t = %.0f s: n_B = %.3g, N_coh = %.3g, N_th = %.3g; threshold signal quanta: linear %.3g, "
        "counting %.3g; ratio %.3g (coupling %.3g)" % (m, T, t, nb, Nc, Nth, Nlin, Ncnt, Nlin / Ncnt, np.sqrt(Nlin / Ncnt)))
out("10 mK = %.3f ueV; 4.2 K = %.1f ueV; 1 neV = %.1f kHz" % (0.010 * KELVIN * 1e6, 4.2 * KELVIN * 1e6, 1e-9 / 4.135667696e-15 / 1e3))

# ---------------------------------------------------------------------------------------------- figure
plt.rcParams.update({"font.size": 8.5, "font.family": "serif", "mathtext.fontset": "cm"})
fig, axs = plt.subplots(3, 1, figsize=(6.4, 6.3), sharex=True)
TSH = T_MK
for ax in axs:
    ax.axvspan(1e-10, TSH, color="0.90", lw=0)
    ax.set_xscale("log")
    ax.set_yscale("log")
ax = axs[0]
ax.plot(m_tls, reach(R_tls), color="C1", lw=1.3)
ax.text(2e-6, 1.2e-14, "two-level systems (SiO$_2$, 10 mK)", color="C1", fontsize=7)
ax.plot(m_ir, reach(R_ir), color="C1", lw=1.3, ls="--")
ax.plot(m_al, reach(R_al_dp), color="C7", lw=1.2)
ax.text(1.3e-3, 1e-9, "Al (clean)", color="C7", fontsize=7)
ax.plot([SIP_LINE[0]], [SIP_LINE[1]], "v", color="C4", ms=4)
ax.plot([SIP_CONT[0]], [SIP_CONT[1]], "^", color="C4", ms=4)
ax.text(5e-3, 2.5e-16, "Si:P", color="C4", fontsize=7)
for D, ls in ((11.8e-3, "-"), (15.6e-3, ":")):
    ax.plot(zr[D][0], zr[D][1], color="C2", lw=1.2, ls=ls)
ax.text(1.0e-1, 3e-14, r"ZrTe$_5$", color="C2", fontsize=7)
ax.plot(w_g, reach(R_g), color="k", lw=1.0)
ax.text(8e-3, 3e-17, "GaAs", color="k", fontsize=7)
ax.plot(w_s, reach(R_s), color="C0", lw=1.0)
ax.text(1.5e-1, 6e-18, r"Al$_2$O$_3$", color="C0", fontsize=7)
ax.plot(m_si, reach(rs["dp"]), color="C3", lw=1.3)
ax.plot(m_cold, reach(R_si_cold), color="C3", lw=1.0, ls=":")
ax.text(3e1, 3e-17, "Si electrons", color="C3", fontsize=7)
ax.plot([10e-6], [reach(R_yig_dp10)], "D", color="C5", ms=3.5)
ax.text(1.4e-5, 4e-17, "YIG line", color="C5", fontsize=7)
ax.set_ylim(3e-18, 1e-8)
ax.set_ylabel(r"$\zeta$")
ax.text(0.01, 0.92, "(a) dark photon", transform=ax.transAxes)
ax = axs[1]
ax.plot(m_yig, reach(R_yig_alp), color="C5", lw=1.2, ls="--")
ax.text(1.2e-5, 3e-18, "YIG line (peak)", color="C5", fontsize=7)
ax.plot([1.1e-3], [reach(R_mnf2)], "D", color="C5", ms=3.5)
ax.text(1.4e-3, 1.0e-16, r"MnF$_2$", color="C5", fontsize=7)
ax.plot(m_alJ, reach(R_al_alpJ), color="C7", lw=1.3)
ax.plot(m_al, reach(R_al_alpS), color="C7", lw=1.0, ls="--")
ax.text(2.5e-3, 6e-14, "Al spin current", color="C7", fontsize=7)
ax.text(1.5e-3, 3e-8, "Al phonon-assisted", color="C7", fontsize=7)
ax.plot(m_si, reach(rs["alp"]), color="C3", lw=1.3)
ax.plot(m_cold, reach(R_si_cold_alp), color="C3", lw=1.0, ls=":")
ax.text(3e0, 5e-10, "Si electrons", color="C3", fontsize=7)
ax.set_ylim(1e-18, 1e-6)
ax.set_ylabel(r"$g_{aee}$")
ax.text(0.01, 0.92, "(b) axion-like particle, electron coupling", transform=ax.transAxes)
ax = axs[2]
ax.plot(w_g, reach(R_gsc), color="k", lw=1.0)
ax.text(6e-3, 1e-13, "GaAs", color="k", fontsize=7)
ax.plot(msc, reach(R_si_sc), color="C3", lw=1.2)
ax.text(1.5e0, 4e-14, "Si electrons (model)", color="C3", fontsize=7)
ax.set_ylim(1e-16, 1e-11)
ax.set_ylabel(r"$g_{\phi ee}$")
ax.text(0.01, 0.92, "(c) scalar, electron coupling", transform=ax.transAxes)
ax.set_xlim(1e-9, 1e4)
ax.set_xlabel(r"$m_\phi$ (eV)")
for ax in axs:
    ax.text(1.3e-9, ax.get_ylim()[0] * 2, r"$m_\phi < T$", fontsize=7, color="0.4")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig17_2.pdf"))
out("wrote fig17_2.pdf")
