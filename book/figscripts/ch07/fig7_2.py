"""Fig. 7.2 (BCS quasiparticle density of states and the pair-creation spectra of the density and the spin density) and
every number quoted in Sect. 7.2 and its worked example on aluminum.  Natural units hbar = c = k_B = 1.

Output: tex/figures/ch07/fig7_2.pdf
  (a) N_s(E)/(2 N_F) = E/(E^2 - Delta^2)^{1/2} (eq:D.20-dos), with the aluminum energy scale on the top axis.
  (b) Bare pair-creation spectrum at T = 0 divided by its normal-state value, for the density (case I) and the z component
      of the spin density (case II), eq:7.2-pairspec:
        P_{I,II}(omega) = (1/omega) int_Delta^{omega-Delta} dE [E(omega-E) +- Delta^2] / ([E^2-Delta^2][(omega-E)^2-Delta^2])^{1/2}.
      Modelling assumptions (named in the caption and the text): bare quasiparticle bubble, linearized band near the Fermi
      surface, q << k_F and v_F q >= omega (then xi and xi' = xi + v_F q cos(theta) are independent and uniformly
      distributed), constant N_F, T = 0.  The case-II curve is checked against the Mattis-Bardeen T = 0 closed form
      (1 + 2Delta/omega) E(k) - (4 Delta/omega) K(k), k = (omega - 2Delta)/(omega + 2Delta) (complete elliptic integrals
      of modulus k).

Inputs and their sources
  Constants (CODATA 2018): hbar c = 1973.269804 eV A, k_B = 8.617333e-5 eV/K, c = 299792.458 km/s.
  v_max = 794.5 km/s = 2.650e-3 (Sect. 1.2/1.3).
  Aluminum:
    T_c = 1.18 K and Delta_BCS(0) = 0.18 meV, measured (Savrasov and Savrasov, PRB 54, 16487 (1996), Table III,
      rows Tc^exp and Delta_0^exp).
    lambda_ep = 0.44, omega_log = 270 K (same reference, Tables II and III; as in Sect. 6.4 and App. E.9).
    mu*_C = 0.12, the value that reproduces T_c in the Eliashberg solution (App. E.9, same reference Table III).
    omega_D stand-in: the largest phonon energy, 40 meV (Sect. 6.4 model; App. E.9 quotes 40.5 meV from Savrasov Sect. III).
      MODELLING CHOICE: the BCS cutoff omega_D is set to 40 meV; the alternative omega_log = 270 K is also printed.
    v_F = 2.0e6 m/s, the free-electron value with k_F = 1.75 A^-1 (Sect. 6.4).
    Film value 2 Delta_BCS = 0.6 meV used in dark-matter projections (Sect. 1.5; Hochberg et al. 1512.04533), a convention.
"""
import os
import numpy as np
from scipy import integrate, optimize, special
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(BOOK, "tex", "figures", "ch07")
os.makedirs(OUT, exist_ok=True)

hbarc_A = 1973.269804      # eV A
kB = 8.617333e-5           # eV/K
c_kms = 299792.458
vmax = 794.5 / c_kms


def close(a, b, rtol=5e-3, name=""):
    assert abs(a - b) <= rtol * abs(b), f"{name}: {a} vs {b}"
    print(f"  {name:66s} {a:.6g}   (quoted {b})")


# ------------------------------------------------------------------ weak-coupling constants (App. D.20)
print("Weak-coupling constants")
gE = np.euler_gamma
close(np.pi * np.exp(-gE), 1.764, 2e-4, "Delta(0)/T_c = pi e^-gamma_E")
close(2 * np.exp(gE) / np.pi, 1.134, 2e-4, "T_c prefactor 2 e^gamma_E / pi")


def gap_T0(NV, wD):
    return wD / np.sinh(1 / NV)


def Tc_of(NV, wD):
    f = lambda T: integrate.quad(lambda x: np.tanh(x / (2 * T)) / x, 0, wD, limit=400)[0] - 1 / NV
    return optimize.brentq(f, 1e-9 * wD, wD)


NV, wD = 0.2, 1.0
close(gap_T0(NV, wD) / Tc_of(NV, wD), 1.764, 1e-3, "numerical Delta(0)/T_c at N_F V_BCS = 0.2")

# ------------------------------------------------------------------ aluminum
print("Aluminum")
Tc = 1.18                    # K, measured
Delta_meas = 0.18e-3         # eV, measured
Tc_eV = Tc * kB
close(Tc_eV * 1e3, 0.1017, 1e-3, "T_c in meV")
Delta = np.pi * np.exp(-gE) * Tc_eV
close(Delta * 1e3, 0.179, 3e-3, "Delta_BCS = 1.764 T_c (meV)")
close(2 * Delta * 1e3, 0.36, 5e-3, "2 Delta_BCS (meV)")
close(2 * Delta_meas / Tc_eV, 3.54, 3e-3, "measured 2 Delta/T_c")
close(2 * np.pi * np.exp(-gE), 3.53, 2e-3, "BCS 2 Delta/T_c")
mmin = 2 * (2 * Delta) / vmax**2
close(mmin, 102.0, 5e-3, "m_min = 2(2 Delta)/v_max^2 (eV), weak-coupling gap")
close(2 * (2 * Delta_meas) / vmax**2, 102.5, 5e-3, "m_min with the measured 2 Delta = 0.36 meV (eV)")
close(2 * 0.6e-3 / vmax**2, 171.0, 5e-3, "m_min with the film convention 2 Delta = 0.6 meV (eV)")
qthr = 2 * (2 * Delta) / vmax          # momentum transfer at the threshold mass, q = m v_max = 2 omega / v_max
close(qthr, 0.271, 5e-3, "q at the threshold mass, 2(2 Delta)/v_max (eV)")
close(hbarc_A / qthr * 1e-4, 0.73, 1e-2, "1/q at threshold (micrometer)")
vF = 2.0e3 / c_kms                     # 2.0e6 m/s
close(vF, 6.67e-3, 3e-3, "v_F (units of c)")
close(vF * qthr / Delta, 10.1, 1e-2, "v_F q/Delta at the threshold mass")
close(vF * (2 * Delta / vmax) / Delta, 5.0, 1e-2, "v_F q/Delta at omega = 2 Delta, q = omega/v_max (lowest q)")
close(vmax / (2 * vF), 0.20, 2e-2, "bound Delta/(v_F q) <= v_max/(2 v_F)")
xi0 = vF / (np.pi * Delta)             # eV^-1
close(xi0 * hbarc_A * 1e-4, 2.3, 2e-2, "pair size v_F/(pi Delta), free-electron v_F (micrometer)")
close(qthr * xi0, 3.2, 2e-2, "q xi_0 at the threshold mass")

lam, mustar = 0.44, 0.12
wDal = 40e-3                           # eV, cutoff stand-in (largest phonon energy)
wlog = 270 * kB
close(wlog * 1e3, 23.3, 3e-3, "omega_log = 270 K in meV")
NV_al = 1 / np.arcsinh(wDal / Delta)
close(NV_al, 0.164, 5e-3, "N_F V_BCS that gives Delta = 0.179 meV with omega_D = 40 meV")
close(1 / np.arcsinh(wlog / Delta), 0.18, 1e-2, "same with omega_D = omega_log")
for name, x, quoted in [("lambda", lam, 54), ("lambda/(1+lambda)", lam / (1 + lam), 20),
                        ("(lambda-mu*)/(1+lambda)", (lam - mustar) / (1 + lam), 5.8)]:
    TcK = 2 * np.exp(gE) / np.pi * wDal * np.exp(-1 / x) / kB
    print(f"    N_F V_BCS = {name:24s} = {x:.4f}: T_c = {TcK:.3g} K")
    close(TcK, quoted, 2e-2, f"T_c(BCS, omega_D = 40 meV) with N_F V = {name}")
close(lam / (1 + lam), 0.31, 2e-2, "lambda/(1+lambda)")
close((lam - mustar) / (1 + lam), 0.22, 2e-2, "(lambda - mu*)/(1+lambda)")
# exponential sensitivity: dlnT_c/d(NV) = 1/NV^2 ; 25 % change of NV around 0.164-0.22
close(np.exp(1 / NV_al - 1 / ((lam - mustar) / (1 + lam))), 4.9, 3e-2, "factor between T_c(0.222) and T_c(0.164)")
# thermal quasiparticles at 10 mK
close(Delta / (0.010 * kB), 208, 3e-3, "Delta/T at 10 mK")
# Cooper binding with N_F V = 0.164
Eb = 2 * wDal * np.exp(-2 / NV_al)
print(f"    Cooper binding 2 omega_D exp(-2/N_F V) = {Eb*1e6:.3g} micro-eV vs 2 Delta = {2*Delta*1e6:.0f} micro-eV")
close(Eb * 1e6, 0.4, 0.1, "Cooper binding (micro-eV)")
close(2 * Delta / Eb, 900, 0.05, "2 Delta / Cooper binding")

# ------------------------------------------------------------------ f-sum violation of the bare bubble (App. D.21)
print("f-sum violation of the bare bubble: q dependence (Delta = 1, shell omega_D/Delta = 223)")
wDr = wDal / Delta
D0 = 8 * np.arcsinh(wDr)               # [8 pi Delta^2 / V_BCS] / (pi N_F Delta^2)


def Dq(x):
    """Spurious first moment / (pi N_F Delta^2) at v_F q = x Delta: linearized band, gap inside the shell only."""
    xis = np.concatenate([np.linspace(-wDr - x - 2, -60, 3000), np.linspace(-60, 60, 60001),
                          np.linspace(60, wDr + x + 2, 3000)])
    mus = np.linspace(-1, 1, 801)
    XI, MU = np.meshgrid(xis, mus, indexing="ij")
    XP = XI + x * MU
    D1 = (abs(XI) < wDr) * 1.0
    D2 = (abs(XP) < wDr) * 1.0
    E, Ep = np.hypot(XI, D1), np.hypot(XP, D2)
    sc = (E + Ep) * (1 - (XI * XP - D1 * D2) / (E * Ep))
    nm = 2 * abs(XP - XI) * (XI * XP < 0)
    return np.trapezoid(np.trapezoid(sc - nm, mus, axis=1) / 2, xis)


for x in [0.1, 1.0, 5.0, 20.0]:
    r = Dq(x) / D0
    print(f"    v_F q = {x:5.1f} Delta: spurious moment / (8 pi Delta^2/V_BCS) = {r:.4f}")
    assert abs(r - 1) < 2e-3
print("    (the spurious first moment is independent of q to 0.2 % for v_F q <= 20 Delta)")
close(np.sqrt(12 / NV_al), 8.6, 1e-2, "v_F q/Delta where 12 (Delta/v_F q)^2/(N_F V) = 1")

# ------------------------------------------------------------------ pair-creation spectra (eq:7.2-pairspec)


def P(w, sign):
    """Ratio of the bare pair-creation spectrum to its normal-state value; Delta = 1; sign +1 case I, -1 case II."""
    if w <= 2:
        return 0.0
    L = w - 2

    def f(phi):
        s = np.sin(phi)**2
        E, Ep = 1 + L * s, 1 + L * (1 - s)
        return 2 * (E * Ep + sign) / np.sqrt((E + 1) * (Ep + 1))
    return integrate.quad(f, 0, np.pi / 2, limit=200)[0] / w


print("Pair-creation spectra")
close(P(2 + 1e-9, +1), np.pi / 2, 1e-6, "case I at threshold = pi/2")
close(P(2 + 1e-6, -1) + 1, 1.0, 1e-5, "case II at threshold = 0 (printed +1)")
for w in [2.5, 3.0, 4.0, 6.0, 10.0]:
    k = (w - 2) / (w + 2)
    mb = (1 + 2 / w) * special.ellipe(k**2) - (4 / w) * special.ellipk(k**2)
    assert abs(P(w, -1) - mb) < 1e-8, (w, P(w, -1), mb)
print("  case II = Mattis-Bardeen T = 0 closed form to 1e-8 at omega/Delta = 2.5, 3, 4, 6, 10")
for w in [3.0, 4.0, 10.0, 20.0]:
    print(f"    omega/Delta = {w:4.1f}: case I {P(w, +1):.4f}, case II {P(w, -1):.4f}")
close(P(4.0, +1), 1.21, 1e-2, "case I at omega = 4 Delta")
close(P(4.0, -1), 0.67, 1e-2, "case II at omega = 4 Delta")

# ------------------------------------------------------------------ figure
plt.rcParams.update({"font.size": 9, "axes.labelsize": 9, "legend.fontsize": 7.5, "pdf.fonttype": 42})
blue, orange, gray = "#2f6db5", "#d9822b", "0.55"

fig, ax = plt.subplots(1, 2, figsize=(6.3, 2.7))
a = ax[0]
E = np.linspace(1.0005, 4, 1500)
a.axvspan(0, 1, color="0.9", lw=0)
a.plot(E, E / np.sqrt(E**2 - 1), color=blue, lw=1.5, label="superconductor")
a.plot([0, 4], [1, 1], color=gray, lw=1.0, ls="--", label="normal metal")
a.plot([1, 1], [0, 4], color=blue, lw=0.6, ls=":")
a.set_xlim(0, 4)
a.set_ylim(0, 4)
a.set_xlabel(r"$E/\Delta_{\mathrm{BCS}}$")
a.set_ylabel(r"$\mathcal{N}_{\mathrm{s}}(E)/2\mathcal{N}_{\mathrm{F}}$")
a.text(0.5, 3.0, "gap", ha="center", fontsize=8, color="0.35")
a.legend(loc="upper right", frameon=False)
top = a.secondary_xaxis("top", functions=(lambda x: x * Delta * 1e3, lambda y: y / (Delta * 1e3)))
top.set_xlabel("$E$ in aluminum (meV)", fontsize=8)
top.tick_params(labelsize=7.5)
a.text(-0.2, 1.17, "(a)", transform=a.transAxes, fontsize=9)

b = ax[1]
w = np.linspace(0, 10, 1001)
PI = np.array([P(x, +1) for x in w])
PII = np.array([P(x, -1) for x in w])
b.plot(w[w > 2], PI[w > 2], color=blue, lw=1.5, label=r"density $n_e$ (case I)")
b.plot([2, 2], [0, np.pi / 2], color=blue, lw=0.8, ls=":")
b.plot(w[w > 2], PII[w > 2], color=orange, lw=1.5, label=r"spin density $s^z_e$ (case II)")
b.plot(w[w <= 2], 0 * w[w <= 2], color="k", lw=1.2)
b.plot([0, 10], [1, 1], color=gray, lw=1.0, ls="--", label="normal metal")
b.annotate(r"$\pi/2$", xy=(1.95, np.pi / 2), xytext=(0.5, 1.75), fontsize=8, color=blue,
           arrowprops=dict(arrowstyle="->", color=blue, lw=0.7))
b.set_xlim(0, 10)
b.set_ylim(0, 2)
b.set_xlabel(r"$\omega/\Delta_{\mathrm{BCS}}$")
b.set_ylabel("pair creation / normal metal")
b.legend(loc="upper right", frameon=False)
b.text(-0.2, 1.17, "(b)", transform=b.transAxes, fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig7_2.pdf"))
print("wrote", os.path.join(OUT, "fig7_2.pdf"))
