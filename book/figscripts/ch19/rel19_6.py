"""Delayed release of stored energy (Sect. 19.6): release window and verdicts, worked example 19.6 (we:19-sumrule),
Fig. 19.5 (fig:19-release) and the low-energy-excess numbers of Sect. 19.6.
Log: rel19_6.log.  Run: python rel19_6.py > rel19_6.log  (seconds).

Inputs and sources
  Attempt rate Gamma_0 = 1e13 s^-1 and observation time 1 yr: the frozen bound of Sect. 16.8 / App. E.22.
  Two-parabola tunneling exponent lambda = (d/2)(2 M V)^(1/2) (App. E.22; Phillips/Jackle convention, Sect. 16.7).
    Si: M = 26.16 GeV (Sect. 7.4), V = 0.1 eV, d = 1.5 A (App. E.22, an estimate); a quartic barrier multiplies lambda by 4/3.
    Al: M = 26.98 u; V = 0.1 eV, d = 1.4 A (estimate, chosen to illustrate a path at the edge of the window).
  Energy-gap law (weak coupling): A(eps) w_p = e^{-S} S^p / p!, p = eps/w_p, with S = 1, w_p = 60 meV, eps = 1 eV
    (illustrative values, App. E.22 / Sect. 19.6); p! = Gamma(p + 1).
  Silicon defect energies (Sect. 7.4, Holmstrom et al. Table III): close Frenkel pair 6.8-7.5 eV, bond defect 2.6-3.0 eV,
    vacancy 3.4-3.9 eV, interstitial 4.7-5.8 eV.  WE 19.6 takes 7.0 eV and 2.8 eV inside these ranges.
  WE 19.6 exponents lambda_C0 = 24.0, lambda_CB = 22.5, lambda_B0 = 25.0: ILLUSTRATIVE (no computed path exists, App. E.22).
  Phonon collection f_ph = 0.25: "phonons are collected with O(25%) efficiency" (Anthony-Petersen et al., arXiv:2208.02790,
    Sect. II).  Low-energy-excess bins 3-38 and 38-85 eV in energy absorbed by the sensor (same paper, Fig. 2, Sect. II A).
  Two-level-system family: Sect. 16.8, eq:16.8-heat and its spectrum (P/4t)[tanh(E/2T_lo) - tanh(E/2T_hi)], T_hi = T_frz = 4.8 K,
    T_lo = 10 mK (we:16-heat).
  Recrystallization energy of amorphous silicon pockets ~0.1 eV per atom: an estimate (App. E.23).
  Largest energy an electron of 10 eV gives a silicon nucleus: 4 m_e E/M (elastic, M >> m_e).
  Ln Gamma for the Frenkel-pair family of Fig. 19.5b: lambda uniform in [20, 30], ILLUSTRATIVE, around the two-parabola estimates.
"""
import os
import numpy as np
from scipy.special import gammaln
from scipy.linalg import expm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch19")
HBARC = 1973.269804  # eV A
AMU = 931.49410242e6
YEAR = 3.15576e7
KB = 8.617333e-5
G0 = 1e13

# ---------------- release window ----------------
L = np.log(G0 * YEAR)
print("ln(Gamma_0 t_obs) = ln(%.3e) = %.2f ; strong coupling: lambda <= %.2f" % (G0 * YEAR, L, L / 2))
lam_si = (1.5 / 2 / HBARC) * np.sqrt(2 * 26.16e9 * 0.1)
print("Si close pair two-parabola lambda = %.2f ; quartic x4/3 = %.1f ; needs %.1f %% lower" % (lam_si, 4 / 3 * lam_si, 100 * (1 - L / 2 / lam_si)))
lam_al = (1.4 / 2 / HBARC) * np.sqrt(2 * 26.98 * AMU * 0.1)
print("Al dumbbell (V 0.1 eV, d 1.4 A) lambda = %.2f ; needs %.1f %% lower" % (lam_al, 100 * (1 - L / 2 / lam_al)))
S, wp, eps = 1.0, 0.060, 1.0
p = eps / wp
lnA = -S + p * np.log(S) - gammaln(p + 1)
print("energy-gap law: p = %.2f, ln(1/(A w_p)) = %.1f -> lambda <= %.1f ; A w_p = %.2e, extra lambda = %.1f"
      % (p, -lnA, (L + lnA) / 2, np.exp(lnA), -lnA / 2))
for eps7 in [7.0]:
    p7 = eps7 / wp
    print("  for eps = %.1f eV (Frenkel pair), ln(1/(A w_p)) = %.0f" % (eps7, S - p7 * np.log(S) + gammaln(p7 + 1)))

# ---------------- worked example: three-state chain ----------------
E = {"C": 7.0, "B": 2.8, "0": 0.0}
lam = {("C", "0"): 24.0, ("C", "B"): 22.5, ("B", "0"): 25.0}
rate = {k: G0 * np.exp(-2 * v) for k, v in lam.items()}
for k, v in rate.items():
    print("rate %s->%s: lambda %.1f, Gamma = %.3e s^-1, 1/Gamma = %.3g d" % (k[0], k[1], lam[k], v, 1 / v / 86400))
gC = rate[("C", "0")] + rate[("C", "B")]
bB = rate[("C", "B")] / gC
print("branching C->B = %.4f, C->0 = %.4f ; 1/(total out of C) = %.1f d" % (bB, 1 - bB, 1 / gC / 86400))
Q = np.array([[-gC, rate[("C", "B")], rate[("C", "0")]],
              [0.0, -rate[("B", "0")], rate[("B", "0")]],
              [0.0, 0.0, 0.0]])  # rows: from C, B, 0 ; generator for row vector p
Ev = np.array([E["C"], E["B"], E["0"]])
for t in [1 * YEAR, 10 * YEAR, 100 * YEAR]:
    pt = np.array([1.0, 0.0, 0.0]) @ expm(Q * t)
    # expected hop counts N_ij = Gamma_ij int_0^t p_i dt (analytic integrals of the two-exponential solution)
    gB = rate[("B", "0")]
    intC = (1 - np.exp(-gC * t)) / gC
    cB = rate[("C", "B")] / (gB - gC)
    intB = cB * ((1 - np.exp(-gC * t)) / gC - (1 - np.exp(-gB * t)) / gB)
    nCB = rate[("C", "B")] * intC
    nC0 = rate[("C", "0")] * intC
    nB0 = gB * intB
    released = nCB * (E["C"] - E["B"]) + nC0 * E["C"] + nB0 * E["B"]
    Est = pt @ Ev
    print("t = %5.0f yr: p_C %.4f p_B %.4f p_0 %.4f ; E_st(t) = %.3f eV ; hops C->B %.4f C->0 %.4f B->0 %.4f ; <N_hop> %.4f ;"
          " released %.3f eV ; E_st - E_st(t) = %.3f eV"
          % (t / YEAR, pt[0], pt[1], pt[2], Est, nCB, nC0, nB0, nCB + nC0 + nB0, released, E["C"] - Est))
    if t == YEAR:
        print("    mean release per hop E_st^rel/<N_hop> = %.3f eV" % (released / (nCB + nC0 + nB0)))
fph = 0.25
for name, e in [("C->0", 7.0), ("C->B", 4.2), ("B->0", 2.8)]:
    print("collected energy of hop %s at f_ph = %.2f: %.2f eV" % (name, fph, fph * e))
print("close-pair range collected: %.2f-%.2f eV" % (fph * 6.8, fph * 7.5))

# ---------------- low-energy excess numbers ----------------
for Eev in [3.0, 38.0, 85.0]:
    Er = Eev / fph
    print("event of %.0f eV absorbed needs %.0f eV released at f_ph = %.2f: %.0f close pairs at 7 eV, %.0f atoms of pocket at 0.1 eV"
          % (Eev, Er, fph, Er / 7.0, Er / 0.1))
me = 0.51099895e6
print("max transfer from a 10 eV electron to Si: 4 m_e E/M = %.2e eV" % (4 * me * 10 / 26.16e9))

# ---------------- Fig. 19.5 ----------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.8))
# (a) collected-energy spectra per release, per unit ln E, each family normalized to one release
Thi, Tlo = 4.8 * KB, 0.010 * KB
Eg = np.logspace(-7, 3, 4000)
s_tls = Eg * 0.5 * (np.tanh(Eg / 2 / Tlo) - np.tanh(Eg / 2 / Thi))  # per unit ln(Delta), unnormalized
lnE = np.log(Eg)
s_tls /= np.trapezoid(s_tls, lnE)
Ec_tls = fph * Eg
mean_tls = np.trapezoid(Eg * s_tls, lnE)
print("two-level family: mean quantum %.3e eV = %.2f T_frz ; collected %.2e eV" % (mean_tls, mean_tls / Thi, fph * mean_tls))
a1.axvspan(3, 38, color="0.85", lw=0)
a1.axvspan(38, 85, color="0.93", lw=0)
a1.plot(Ec_tls, s_tls / s_tls.max(), "b-", lw=1.4, label="two-level systems")
# Frenkel pairs: E_conf uniform 6.8-7.5 eV, plotted per unit ln E
Ef = np.linspace(6.8, 7.5, 50)
yf = Ef / Ef.max()
a1.plot(fph * Ef, yf, "r-", lw=1.4, label="close Frenkel pairs")
a1.vlines([fph * 6.8, fph * 7.5], 0, yf[[0, -1]], colors="r", lw=1.4)
a1.set_xscale("log")
a1.set_xlim(1e-6, 2e2)
a1.set_ylim(0, 1.25)
a1.set_xlabel(r"collected energy per release (eV)")
a1.set_ylabel(r"releases per unit $\ln E$ (peak 1)")
a1.text(16, 1.08, "excess\nbins", fontsize=7, ha="center")
a1.legend(loc="upper left", fontsize=7, frameon=False)
a1.set_title("(a)", fontsize=9, loc="left")
# (b) fraction of a Frenkel-pair family released by time t, lambda uniform in [20, 30], strong coupling
t = np.logspace(2, 15, 800)
lams = np.linspace(20, 30, 4001)
frac = np.array([np.trapezoid(1 - np.exp(-G0 * np.exp(-2 * lams) * tt), lams) / 10 for tt in t])
f1 = np.trapezoid(1 - np.exp(-G0 * np.exp(-2 * lams) * YEAR), lams) / 10
print("Fig 19.5b: fraction released within 1 yr = %.3f (window estimate (23.6 - 20)/10 = %.3f)" % (f1, (L / 2 - 20) / 10))
print("Fig 19.5b: 1/t window from %.2e s (%.1f h) to %.2e s (%.0f yr); rate per unit ln t inside = %.3f"
      % (np.exp(40) / G0, np.exp(40) / G0 / 3600, np.exp(60) / G0, np.exp(60) / G0 / YEAR, 1 / 20))
a2.semilogx(t / YEAR, frac, "r-", lw=1.4, label=r"$\lambda_{\mathrm{tun}}$ uniform in [20, 30]")
a2.axvline(1.0, color="0.4", lw=0.7, ls="--")
a2.text(1.3, 0.85, "1 yr", fontsize=7)
a2.set_xlabel(r"time after the recoil (yr)")
a2.set_ylabel("fraction of pairs recombined")
a2.set_ylim(0, 1.02)
a2.set_xlim(t[0] / YEAR, t[-1] / YEAR)
a2.legend(loc="lower right", fontsize=7, frameon=False)
a2.set_title("(b)", fontsize=9, loc="left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig19_5.pdf"))
print("wrote fig19_5.pdf")
