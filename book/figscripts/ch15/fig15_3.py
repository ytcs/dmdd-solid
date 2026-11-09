"""Fig. 15.3 (fig:15-absorption): absorption of a uniform field by aluminum at T = 0, through the current (panel a, dark
photon) and through the spin current (panel b, axion-like particle), and the numbers of Sect. 15.4.3.

Panel (a): sigma_1 in eV against omega from 0.3 to 300 meV:
  Holstein, normal metal (Allen):  sigma_1^N = (omega_p^2/omega^2) gamma_H, Debye a2F_tr;
  Holstein, superconductor:         Eq. 15.4-holstein, case-I factor;
  impurity-assisted, normal metal:  Drude sigma_N = omega_p^2 gamma_rel/(omega^2 + gamma_rel^2), gamma_rel = v_F/l_e;
  impurity-assisted, superconductor (Mattis-Bardeen, dirty limit): sigma_N g_II(omega/Delta).
Panel (b): spin-current conductivity sigma^J (normalized so that sigma^J = sigma_1 for independent electrons without
spin-orbit coupling in the normal state, Eq. 10.7-alp):
  clean superconductor, direct pair breaking (Eq. 15.4-sJ) times the quasiparticle factor 1/(1 + lambda_ep) = 1/1.43
  (lambda_ep = 0.43 of Sect. 6.4), the form the text of Sect. 15.4 quotes;
  impurity-assisted, superconductor (dirty limit): sigma_N g_I(omega/Delta);  and its normal-metal value sigma_N;
  Holstein, normal metal (reference; the phonon-assisted spin-current part of the superconductor is not evaluated).
Inputs and modelling choices (abs15.py): Delta_BCS = 0.18 meV; omega_p = 12.29 eV (computed intraband value);
lambda_tr = 0.39, omega_D = 37 meV (Debye a2F_tr); v_F = 6.753e-3 (al_constants.py); l_e = 50 nm, the film of Sect. 15.3 (gamma_rel = 26.65 meV,
free-electron omega_p for its Drude conductivity; dirty limit gamma_rel >> Delta).  Interband absorption (above about 0.5 eV) is not included.
Run: python fig15_3.py   (a few seconds)
"""
import os
import numpy as np
from scipy.optimize import brentq
from scipy import integrate
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import abs15 as A

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch15", "fig15_3.pdf")
D = A.DELTA
GR = A.tau_inv(50e-9)
sdc = A.WP_FREE**2 / GR
rho_uohmcm = 1 / (sdc / A.HBAR_EVS * 8.8541878128e-12) * 1e8
print("gamma_rel = v_F/l_e for l_e = 50 nm: %.2f meV = %.0f Delta; free-electron omega_p = %.2f eV; sigma_dc = omega_p^2/gamma_rel = %.3g eV, resistivity %.3f micro-ohm cm" % (GR * 1e3, GR / D, A.WP_FREE, sdc, rho_uohmcm))

ws = np.geomspace(0.3e-3, 0.3, 600)
sN = np.array([A.sigma_holstein(w, coh="N") for w in ws])
sS = np.array([A.sigma_holstein(w, coh="I") for w in ws])
dN = np.array([A.sigma_N_imp(w, GR) for w in ws])
dS = np.array([A.sigma_MB(w, GR) for w in ws])
LAM_EP = 0.43                     # lambda_ep of aluminum from the specific heat (Sect. 6.4)
QPF = 1 / (1 + LAM_EP)            # quasiparticle factor on the direct term (0.70)
jdir = QPF * A.sigmaJ_direct(ws)  # plotted in panel (b)
jimp = np.array([A.sigmaJ_imp(w, GR) for w in ws])

# ---- numbers of Sect. 15.4.3 (spin current) --------------------------------------------------------------------------
xc = brentq(lambda w: float(A.sigmaJ_direct(w)) - A.sigma_holstein(w, coh="N"), 3e-3, 37e-3)
print("bare direct spin-current pair breaking equals the normal-metal Holstein sigma_1 at omega = %.1f meV" % (xc * 1e3))
xq = brentq(lambda w: QPF * float(A.sigmaJ_direct(w)) - A.sigma_holstein(w, coh="N"), 3e-3, 37e-3)
print("with the factor 1/(1 + %.2f) = %.3f (plotted): crossing at omega = %.1f meV" % (LAM_EP, QPF, xq * 1e3))
for w in (0.4e-3, 0.72e-3, 1e-3, 2e-3, 5e-3, 10e-3):
    print("  omega = %.2f meV: sigma^J_dir = %.3g eV, sigma^J_imp(50 nm) = %.3g eV, Holstein sigma_1^N = %.3g eV, sigma_1^S = %.3g eV, ratio dir/S = %.3g"
          % (w * 1e3, A.sigmaJ_direct(w), A.sigmaJ_imp(w, GR), A.sigma_holstein(w, coh="N"), A.sigma_holstein(w),
             A.sigmaJ_direct(w) / max(A.sigma_holstein(w), 1e-300)))
# share of the weight (pi/2) omega_p^2 below a given omega: int_{2D}^{w} = (pi/2) omega_p^2 tanh(arccosh(w/2D))
for w in (0.4e-3, 0.72e-3, 1e-3, 3.6e-3):
    t = np.arccosh(w / (2 * D))
    print("  fraction of the spin Drude weight below %.2f meV: %.3f" % (w * 1e3, np.tanh(t)))
for w in (0.72e-3, 1e-3):
    Rj = A.rate_alp(w, float(A.sigmaJ_direct(w)))
    Rh = A.rate_alp(w, A.sigma_holstein(w))
    print("  ALP at m = %.2f meV: direct %.3g g^2 /kg/yr -> g_aee(3 events/kg yr) = %.2g; with sigma_1^S in Eq. 10.7-alp %.3g g^2 -> %.2g"
          % (w * 1e3, Rj, np.sqrt(3 / Rj), Rh, np.sqrt(3 / Rh)))
    print("     at g_aee = 1e-13: %.3g events/kg/yr (direct)" % (Rj * 1e-26))
    for lam in (0.43,):   # lambda_ep of aluminum from the specific heat (Sect. 6.4)
        print("     if the direct term carried a quasiparticle factor 1/(1 + %.2f): g_aee x %.3f = %.2g" % (lam, np.sqrt(1 + lam), np.sqrt(3 / Rj) * np.sqrt(1 + lam)))
# impurity version: weight check (pi/2) omega_p^2 of the Drude Lorentzian, and case-I sum over omega > 2 Delta
tot_imp = integrate.quad(lambda w: A.sigmaJ_imp(w, GR), 2 * D, 50, limit=500, points=[3 * D, 10 * D, GR])[0]
tot_N = integrate.quad(lambda w: A.sigma_N_imp(w, GR), 0, 50, limit=500, points=[GR])[0]
print("dirty limit: int sigma^J_imp domega (omega > 2 Delta) / int sigma_N domega (omega > 0) = %.4f (0 to 50 eV)" % (tot_imp / tot_N))
# exact identity int_2^inf (g_I(y) - 1) dy = 2: the weight above 2 Delta replaces the weight below exactly for flat sigma_N
I1 = integrate.quad(lambda y: float(A.gI(y)) - 1, 2, 1e3, limit=1000)[0]
I2 = integrate.quad(lambda y: float(A.gI(y)) - 1, 1e3, 1e7, limit=1000)[0]
print("int_2^inf (g_I - 1) dy = %.8f (+ tail beyond 1e7: (2 ln 2Y + 1)/Y = %.1e)" % (I1 + I2, (2 * np.log(2e7) + 1) / 1e7))
for top in (50.0, 500.0):
    a = integrate.quad(lambda w: A.sigmaJ_imp(w, GR), 2 * D, top, limit=800, points=[3 * D, 10 * D, GR])[0]
    b_ = integrate.quad(lambda w: A.sigma_N_imp(w, GR), 0, top, limit=800, points=[GR])[0]
    print("  Drude sigma_N, cutoff %.0f eV: ratio = %.5f" % (top, a / b_))
flat = lambda w: 1.0
a = integrate.quad(lambda w: float(A.gI(w / D)), 2 * D, 50, limit=800, points=[3 * D, 10 * D])[0]
print("  flat sigma_N, cutoff 50 eV: ratio = %.6f (deficit from the Drude shape and the cutoff, not the coherence factor)" % (a / 50))
# 50 nm film, ALP at 4 Delta: the published sigma_1 mapping on the film's own Mattis-Bardeen sigma_1, against the spin channel
w = 0.72e-3
for lab, s1 in (("Mattis-Bardeen sigma_1 = sigma_n g_II", A.sigma_MB(w, GR)), ("spin channel sigma_n g_I", A.sigmaJ_imp(w, GR))):
    R = A.rate_alp(w, s1)
    print("  50 nm film, ALP at 0.72 meV with %s = %.3g eV: g_aee(3 events/kg yr) = %.2g" % (lab, s1, np.sqrt(3 / R)))
print("film at 1 meV: Mattis-Bardeen %.3g eV against Holstein %.3g eV (ratio %.2g)"
      % (A.sigma_MB(1e-3, GR), A.sigma_holstein(1e-3), A.sigma_MB(1e-3, GR) / A.sigma_holstein(1e-3)))
for w in (0.1, 0.3):
    print("omega = %.0f meV: Holstein %.3g eV, impurity (50 nm) %.3g eV, ratio impurity/Holstein %.2f" % (w * 1e3, A.sigma_holstein(w), A.sigma_N_imp(w, GR), A.sigma_N_imp(w, GR) / A.sigma_holstein(w)))
rmin = min(A.sigma_N_imp(w, GR) / A.sigma_holstein(w) for w in np.geomspace(1e-3, 0.3, 400))
print("smallest ratio impurity (50 nm)/Holstein between 1 and 300 meV: %.2f" % rmin)

# ---- figure ------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, axs = plt.subplots(1, 2, figsize=(6.6, 3.0), sharey=True)
wm = ws * 1e3
ax = axs[0]
ax.plot(wm, sN, color="k", lw=1.0, ls="--", label="phonon, normal")
ax.plot(wm, sS, color="k", lw=1.4, label="phonon, superconductor")
ax.plot(wm, dN, color="tab:blue", lw=1.0, ls="--", label="impurity, normal")
ax.plot(wm, dS, color="tab:blue", lw=1.4, label="impurity, superconductor")
ax.set_ylabel(r"conductivity (eV)")
ax.set_title(r"(a) current: $\sigma_1$", fontsize=9)
ax = axs[1]
ax.plot(wm, jdir, color="tab:red", lw=1.4, label="direct, clean superconductor")
ax.plot(wm, jimp, color="tab:blue", lw=1.4, label="impurity, superconductor")
ax.plot(wm, dN, color="tab:blue", lw=1.0, ls="--", label="impurity, normal")
ax.plot(wm, sN, color="k", lw=1.0, ls="--", label="phonon, normal")
ax.set_title(r"(b) spin current: $\sigma_1^{\mathcal{J}}$", fontsize=9)
for ax in axs:
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.3, 300)
    ax.set_ylim(1e-6, 1e8)
    ax.axvline(2 * D * 1e3, color="0.5", lw=0.6, ls=":")
    ax.axvline(A.WD * 1e3, color="0.5", lw=0.6, ls="-.", ymax=1.0 if ax is axs[0] else 0.72)
    ax.set_xlabel(r"$\omega$ (meV)")
lg = axs[0].legend(fontsize=6.5, loc="lower right", frameon=True, framealpha=1.0, facecolor="white", edgecolor="none")
lg.set_zorder(5)
axs[1].legend(fontsize=6.5, loc="upper right", frameon=False)
axs[0].text(2 * D * 1e3 * 1.08, 2e6, r"$2\Delta_{\mathrm{BCS}}$", fontsize=7, color="0.3")
axs[0].text(A.WD * 1e3 * 1.08, 2e6, r"$\omega_{\mathrm{D}}$", fontsize=7, color="0.3")
fig.tight_layout()
fig.savefig(OUT)
print("wrote", OUT)
