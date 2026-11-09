"""Recoil discrimination with phonon readout (Sect. 20.5): high-voltage ceiling, primary route, gap-energy channel,
low-bias Luke route.  Every number printed in Sect. 20.5.4-20.5.5, worked example we:20-ceiling and Fig. 20.5
(fig:20-ceiling).  Run:  python disc20_5.py > disc20_5.log   (a few seconds).
Output: tex/figures/ch20/fig20_5.pdf

Inputs (book values and sources)
  eps_eh = 3.75 eV (book silicon pair energy, Sect. 18.4); the measured nuclear-recoil yields are defined with the
           source's eps_src = 3.8 eV, <n_eh> = Y E_r / 3.8 eV (Albakry et al. 2303.02196 Eq. (1)), so a nuclear recoil
           of energy E_R makes Y E_R / eps_src pairs on average.
  F_eh   = 0.119 (measured silicon Fano factor of electron recoils, Sect. 18.4).
  Measured silicon nuclear-recoil yield Y and pair-number Fano factor F_NR, 1 sigma (2303.02196 Table II):
           0.10 keV: Y 0.102 +0.034 -0.030, F 0.9 +0.7 -0.4
           0.22 keV: Y 0.108 +0.009 -0.010, F 0.5 +0.2 -0.1
           0.46 keV: Y 0.136 +0.009 -0.008, F 1.8 +0.6 -0.5
           0.89 keV: Y 0.127 +0.031 -0.015, F 3.7 +0.8 -0.9
           Between rows: linear interpolation in log E_R of the central values and of each band edge
           (MODELLING CHOICE; no measurement lies between 0.22 and 0.46 keV).
  Collection: detected fraction f_det = 0.873 (the 12.7 % trapping probability of the detector model of 2303.02196,
           p. 3) or 1.  Two limits for the spread of the induced charge (Sect. 20.1):
             binomial  (a trapped carrier induces nothing): F_eff = f_det F + 1 - f_det  (measured-charge Fano factor)
             Ramo mean (every pair induces f_det):          F_eff = f_det F
  Bias 100 V (2303.02196), g_Luke = eV_bias/eps_eh = 26.67.
  Primary route: Si optical phonon 64.1 meV (Sect. 5.1).
  Low-bias route: baseline sigma_ph = 2.65 eV (Ren et al. 2012.12430, abstract: 0 V resolution of a 1 x 1 x 0.4 cm^3
           Si chip).

High-voltage ceiling (derived in Sect. 20.5.5).  At equal total phonon energy E_ph, an electron recoil of energy
E_ER = E_R (1 + f g Y')/(1 + f g) and a nuclear recoil of energy E_R (Y' = Y eps_eh/eps_src) differ in detected pair
number by Delta N = f (E_R/eps_eh)(1 - Y')/(1 + f g).  With an ideal readout of the Luke share (contrast 1, no
baseline or position noise) the separation is
   S_HV = Delta N / sqrt( (F_eff^NR <N_NR> + F_eff^ER <N_ER>)/2 ),
   <N_NR> = f Y' E_R/eps_eh,  <N_ER> = f (E_R/eps_eh)(1 + f g Y')/(1 + f g).
"""
import os
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch20")
os.makedirs(FIG, exist_ok=True)

EPS, EPS_SRC, F_ER, EG = 3.75, 3.8, 0.119, 1.17
ROWS = {100: (0.102, 0.034, 0.030, 0.9, 0.7, 0.4), 220: (0.108, 0.009, 0.010, 0.5, 0.2, 0.1),
        460: (0.136, 0.009, 0.008, 1.8, 0.6, 0.5), 890: (0.127, 0.031, 0.015, 3.7, 0.8, 0.9)}
EKEYS = np.array(sorted(ROWS))


def S_hv(ER, Y, FNR, f=0.873, V=100.0, model="binomial", FER=F_ER, eps_src=EPS_SRC):
    g = V / EPS
    yp = Y * EPS / eps_src
    nR = ER / EPS
    dN = f * nR * (1 - yp) / (1 + f * g)
    Nn = f * yp * nR
    Ne = f * nR * (1 + f * g * yp) / (1 + f * g)
    if model == "binomial":
        Fn, Fe = f * FNR + 1 - f, f * FER + 1 - f
    else:
        Fn, Fe = f * FNR, f * FER
    return dN / np.sqrt(0.5 * (Fn * Nn + Fe * Ne))


def interp(ER, k, nsig=1.0):
    """central and band edges at ER (log-linear between rows); k = 0 (Y) or 1 (F)."""
    x = np.log(EKEYS)
    c = np.array([ROWS[e][3 * k] for e in EKEYS])
    hi = c + nsig * np.array([ROWS[e][3 * k + 1] for e in EKEYS])
    lo = np.maximum(c - nsig * np.array([ROWS[e][3 * k + 2] for e in EKEYS]), 1e-3)
    xe = np.log(ER)
    return np.interp(xe, x, c), np.interp(xe, x, lo), np.interp(xe, x, hi)


def envelope(ER, nsig=1.0):
    Yc, Yl, Yh = interp(ER, 0, nsig)
    Fc, Fl, Fh = interp(ER, 1, nsig)
    vals = [S_hv(ER, y, F, f, model=m) for y in (Yl, Yh) for F in (Fl, Fh) for f in (0.873, 1.0)
            for m in ("binomial", "ramo")]
    return S_hv(ER, Yc, Fc), min(vals), max(vals)


print("High-voltage (100 V) ceiling, ideal Luke-share readout, central values, binomial collection f_det = 0.873:")
for E in EKEYS:
    Y, _, _, F, _, _ = ROWS[E]
    print(f"  E_R = {E:4d} eV: S = {S_hv(E, Y, F):.3f}  (Ramo mean {S_hv(E, Y, F, model='ramo'):.3f}; "
          f"f_det = 1: {S_hv(E, Y, F, f=1.0):.3f}; zero bias {S_hv(E, Y, F, V=1e-9):.3f})")
print("1-sigma envelopes (corners of Y, F_NR; f_det 0.873 or 1; both collection limits):")
for E in (100, 150, 220, 300, 460):
    c, lo, hi = envelope(E)
    c2, lo2, hi2 = envelope(E, 2.0)
    print(f"  E_R = {E:4d} eV: central {c:.3f}, 1 sigma [{lo:.3f}, {hi:.3f}], 2 sigma [{lo2:.3f}, {hi2:.3f}]")
EG_ = np.geomspace(100, 890, 2001)
for nsig in (1.0, 2.0):
    up = np.array([envelope(e, nsig)[2] for e in EG_])
    above = EG_[up > 2.0]
    i = np.argmax(up)
    txt = (f"exceeds 2 on {above.min():.0f}-{above.max():.0f} eV" if above.size else "stays below 2")
    print(f"upper {nsig:.0f}-sigma envelope, 100-890 eV: maximum {up[i]:.3f} at {EG_[i]:.0f} eV; {txt}")
    if above.size:
        # contiguous pieces
        brk = np.where(np.diff(np.flatnonzero(up > 2.0)) > 1)[0]
        print(f"   pieces: {len(brk) + 1}; " + ", ".join(f"{EG_[np.flatnonzero(up > 2.0)][a]:.0f}" for a in [0] + list(brk + 1)))
cen = np.array([envelope(e)[0] for e in EG_])
print(f"central curve, 100-890 eV: maximum {cen.max():.3f} at {EG_[np.argmax(cen)]:.0f} eV")

# worked example at 220 eV
E, Y, F = 220, 0.108, 0.5
g = 100 / EPS; f = 0.873; yp = Y * EPS / EPS_SRC; nR = E / EPS
print("\nWorked example, E_R = 220 eV, 100 V:")
print(f"  g_Luke = {g:.3f}; f g = {f*g:.3f}; Y' = Y eps_eh/eps_src = {yp:.4f}; E_R/eps_eh = {nR:.3f}")
Nn = f * yp * nR; Ne = f * nR * (1 + f * g * yp) / (1 + f * g); dN = f * nR * (1 - yp) / (1 + f * g)
Eph = E * (1 + f * g * yp); Eer = Eph / (1 + f * g)
print(f"  E_ph = {Eph:.1f} eV; electron recoil of equal E_ph: {Eer:.2f} eV")
print(f"  <N_NR> = {Nn:.3f}, <N_ER> = {Ne:.3f}, Delta N = {dN:.3f}")
Fn, Fe = f * F + 1 - f, f * F_ER + 1 - f
print(f"  F_eff: NR {Fn:.4f}, ER {Fe:.4f}; variances {Fn*Nn:.3f}, {Fe*Ne:.3f}; S = {dN/np.sqrt(0.5*(Fn*Nn+Fe*Ne)):.3f}")
print(f"  Ramo-mean limit: S = {S_hv(E, Y, F, model='ramo'):.3f}; f_det = 1: {S_hv(E, Y, F, f=1.0):.3f}")
corner = S_hv(E, Y - 0.010, F - 0.1, model="ramo")
print(f"  most favourable 1-sigma corner (Y 0.098, F_NR 0.4, Ramo mean, f 0.873): S = {corner:.3f}; with f = 1: "
      f"{S_hv(E, Y - 0.010, F - 0.1, f=1.0, model='ramo'):.3f}")
print(f"  same corner, binomial (trapped carriers induce nothing), f 0.873: S = {S_hv(E, Y - 0.010, F - 0.1):.3f}; "
      f"f = 1: {S_hv(E, Y - 0.010, F - 0.1, f=1.0):.3f}")
fs = brentq(lambda x: S_hv(E, Y, x, model="ramo") - 2.0, 1e-4, 3.0)
fsb = brentq(lambda x: S_hv(E, Y, x) - 2.0, -0.5, 3.0) if S_hv(E, Y, -0.5) > 2 else float("nan")
print(f"  F_NR at which S = 2 (central Y, Ramo mean): {fs:.3f}; binomial: {fsb:.3f} (negative or nan = unreachable)")
print(f"  with the book's eps for the yield too (Y' = Y): S = {S_hv(E, Y, F, eps_src=EPS):.3f}")
print(f"  S at 300 eV central: {envelope(300)[0]:.3f}; at 1 V (g = {1/EPS:.3f}): {S_hv(E, Y, F, V=1.0):.3f}")
# large-gain form
print(f"  bias dependence at 220 eV (binomial): " + ", ".join(f"{V:g} V {S_hv(E, Y, F, V=V):.3f}" for V in (0, 4, 10, 30, 100, 300)))

# ------------------------------------------------------------------ primary route
wop = 0.0641
fsoft = wop / EPS
print(f"\nPrimary route: soft fraction of an electron recoil f_s = omega_opt/eps_eh = {fsoft:.4f}")
for Y in (0.102, 0.136):
    ds = (1 - Y) * fsoft
    print(f"  Y = {Y}: Delta_soft = (1 - Y) f_s = {ds:.4f}; position spread that caps S < 2 for any contrast: {ds/2:.4f}")

# ------------------------------------------------------------------ gap-energy channel
G = EG / EPS
print(f"\nGap channel: E_g/eps_eh = {G:.4f}")
for Y in (0.102, 0.108):
    print(f"  Y = {Y}: equal release, nothing released by t1: Delta O_b = (1 - Y) E_g/eps = {(1-Y)*G:.4f}")
xf = brentq(lambda x: np.exp(-x) - 0.102 / (1 + x), 0.1, 20)
print(f"  NR annihilation 1/(1 + t/t_rel) vs ER exponential exp(-t/t_rel): Delta O_b changes sign at t1 = {xf:.3f} t_rel "
      f"(root of exp(-x)(1 + x) = Y_q at Y_q = 0.102)")

# ------------------------------------------------------------------ low-bias Luke route
print("\nLow-bias route: Delta phi_L = g(1 - Y)/[(1 + g)(1 + Y g)], maximum (1 - sqrt Y)/(1 + sqrt Y) at g = Y^-1/2")
for Y in (0.102,):
    print(f"  Y = {Y}: g_opt = {Y**-0.5:.3f} (V = {Y**-0.5*EPS:.2f} V at full collection), "
          f"max Delta phi_L = {(1-np.sqrt(Y))/(1+np.sqrt(Y)):.4f}")


def S_low(w, V, ER=100.0, Y=0.102, FNR=0.9, f=0.873, spos=0.05, sph=2.65):
    """Low-bias route at equal recoil energy E_R: observable O = a_prim + varpi_O phi_Luke (varpi_gap = 0); each
    recoil's spread is sigma_pos^2 + (sigma_ph/E_ph)^2 + (varpi_O e V/E_ph)^2 F_eff <N_det>, at its own E_ph
    (MODELLING CHOICE, stated in the text); binomial F_eff with F_eh = 0.119 (ER) and F_NR (NR); Y' = Y eps_eh/eps_src."""
    g = V / EPS; yp = Y * EPS / EPS_SRC; nR = ER / EPS
    En = ER * (1 + f * g * yp); Ee = ER * (1 + f * g)
    Nn = f * yp * nR; Ne = f * nR
    dO = w * f * g * (1 - yp) / ((1 + f * g) * (1 + f * g * yp))
    Fn, Fe = f * FNR + 1 - f, f * F_ER + 1 - f
    vn = spos**2 + (sph / En) ** 2 + (w * V / En) ** 2 * Fn * Nn
    ve = spos**2 + (sph / Ee) ** 2 + (w * V / Ee) ** 2 * Fe * Ne
    return dO / np.sqrt(0.5 * (vn + ve))


print(f"  optimum gain g = f_det g_Luke = Y'^-1/2 = {(0.102*EPS/EPS_SRC)**-0.5:.3f} (with Y: {0.102**-0.5:.3f}); bias at "
      f"f_det = 0.873: {0.102**-0.5*EPS/0.873:.2f} V (with Y), {(0.102*EPS/EPS_SRC)**-0.5*EPS/0.873:.2f} V (with Y')")
VV = np.geomspace(1e-3, 300, 800)
for spos in (0.02, 0.05, 0.10):
    smax = lambda w: max(S_low(w, V, spos=spos) for V in VV)
    try:
        wmin = brentq(lambda w: smax(w) - 2.0, 1e-3, 1.0, xtol=1e-4)
        Vb = VV[np.argmax([S_low(wmin, V, spos=spos) for V in VV])]
        print(f"  sigma_pos = {spos:.2f}: varpi_O,min = {wmin:.3f} (best bias {Vb:.1f} V)")
    except ValueError:
        print(f"  sigma_pos = {spos:.2f}: S < 2 for every varpi_O <= 1 (max {smax(1.0):.3f})")
sl = [S_low(1.0, V, spos=0.0, sph=0.0) for V in VV]
print(f"  ceiling of the route (varpi_O = 1, no baseline, no position spread) at 100 eV: max {max(sl):.3f} at "
      f"V = {VV[int(np.argmax(sl))]:.3g} V (bias grid 1e-3-300 V); zero-bias charge-and-heat value {S_hv(100, 0.102, 0.9, V=1e-9):.3f}")
from scipy.stats import norm
print(f"meaning of S_sep (equal Gaussians, cut at the midpoint): S = 2 -> acceptance = rejection = {norm.cdf(1.0):.3f}; "
      f"leakage 1e-3 at the midpoint cut needs S = {2*norm.ppf(1-1e-3):.2f}")

# ------------------------------------------------------------------ figure
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.8, 3.2))
EE = np.geomspace(100, 890, 200)
env = np.array([envelope(e) for e in EE])
env2 = np.array([envelope(e, 2.0) for e in EE])
ax.fill_between(EE, env2[:, 1], env2[:, 2], color="C0", alpha=0.12, lw=0, label=r"$2\sigma$ inputs")
ax.fill_between(EE, env[:, 1], env[:, 2], color="C0", alpha=0.30, lw=0, label=r"$1\sigma$ inputs")
ax.plot(EE, env[:, 0], color="C0", lw=1.4, label="central")
ax.plot(EE, [S_hv(e, interp(e, 0)[0], interp(e, 1)[0], V=1e-9) for e in EE], color="k", lw=1.0, ls="--",
        label="zero bias, same readout")
ax.axhline(2.0, color="C3", lw=0.9)
ax.axvspan(100, 300, color="0.95", lw=0, zorder=0)
for e in EKEYS:
    ax.axvline(e, color="0.5", lw=0.5, ls=":")
ax.set_xscale("log")
ax.set_xlim(100, 890)
ax.set_yscale("log")
ax.set_ylim(0.3, 30)
ax.set_yticks([0.5, 1, 2, 5, 10, 20]); ax.set_yticklabels(["0.5", "1", "2", "5", "10", "20"])
ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_xticks([100, 200, 300, 500, 890]); ax.set_xticklabels(["100", "200", "300", "500", "890"])
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_xlabel(r"recoil energy $E_R$ (eV)")
ax.set_ylabel(r"separation $\mathcal{S}_{\mathrm{HV}}$ at 100 V")
ax.legend(fontsize=6.5, frameon=False, loc="center right", bbox_to_anchor=(1.0, 0.62))
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig20_5.pdf"))
print("\nwrote fig20_5.pdf")
