"""Fig. 2.5: (a) real and imaginary parts of a regularized energy denominator 1/(x + i Gamma_w/2) (Sect. 2.4);
(b) Worked example 2.6: two-photon absorption in a three-level system, rate against the frequency of beam 1.
Output: tex/figures/ch02/fig2_5.pdf. Natural units, energies in eV; 1 eV = 1.519267e15 s^-1 (hbar = 6.582119569e-16 eV s).

No external data. Every number is a model choice of the worked example, stated here and in the text:
  E_MG   = 1.50 eV   energy of the intermediate level m above the ground level a
  E_BAND = 3.20 eV   bottom of the flat band of final states b (one photon of either beam, and two photons of beam 1
                     for omega_1 < 1.60 eV, cannot reach it)
  OM2    = 1.90 eV   frequency of beam 2 (fixed); its detuning from a->m is delta_2 = OM2 - E_MG = 0.40 eV
  O_MG   = 1e-4 eV   matrix element <m|O|a> of either beam (the same operator O for both beams)
  G_ION  = 1e-4 eV   2 pi |<b|O|m>|^2 D_b: the rate at which beam 2 empties a real level m into the band (beam 1
                     cannot: E_MG + omega_1 < E_BAND)
  G_W    = 1e-3 eV   total width Gamma_w of m (beam-induced emptying plus all other decay)
  SIG_L  = 0.010 eV  rms spectral width of a broadband beam 1 (Gaussian), for the delta + finite-part check
Model (Sect. 2.4, WE 2.6): T_b = <b|O|m><m|O|a> D(omega_1), D = 1/(delta_1 + i G_W/2) + 1/(delta_2 + i G_W/2),
delta_j = omega_j - E_MG; rate Gamma_2ph = G_ION |O_MG|^2 |D|^2 (flat band, golden rule summed over b).
Regularization of the resonant ordering only matters for delta_1; G_W in the beam-2-first denominator is kept
for symmetry and changes nothing at the quoted digits.
"""
import os
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

EV_TO_INV_S = 1 / 6.582119569e-16      # 1 eV in s^-1
E_MG, E_BAND, OM2 = 1.50, 3.20, 1.90
O_MG, G_ION, G_W, SIG_L = 1e-4, 1e-4, 1e-3, 0.010
D2 = OM2 - E_MG


def D(d1, both=True):
    out = 1 / (d1 + 1j * G_W / 2)
    if both:
        out = out + 1 / (D2 + 1j * G_W / 2)
    return out


def rate(d1, both=True):
    return G_ION * O_MG**2 * np.abs(D(d1, both))**2


# --- kinematics of the model --------------------------------------------------------------------
assert OM2 < E_BAND and 1.6 < E_BAND and 2 * 1.6 <= E_BAND   # one photon closed; two photons of beam 1 closed below 1.60 eV
assert E_MG + OM2 >= E_BAND                                     # beam 2 empties a real level m into the band
print(f"final energy at omega_1 = 1.50 eV: {1.50 + OM2:.2f} eV (band bottom {E_BAND} eV)")
print(f"perturbative check |O_mg|/(G_w/2) = {O_MG / (G_W / 2):.2f}")

# --- off resonance -----------------------------------------------------------------------------
for w1 in [1.20]:
    d1 = w1 - E_MG
    r_both, r_one = rate(d1), rate(d1, both=False)
    print(f"omega_1 = {w1} eV: delta_1 = {d1:+.2f} eV, |D|^2 = {abs(D(d1))**2:.4f} eV^-2 "
          f"(beam-1-first only: {abs(D(d1, False))**2:.3f}), ratio {r_one / r_both:.1f}")
    print(f"   rate = {r_both:.3e} eV = {r_both * EV_TO_INV_S:.3e} s^-1")
d_zero = -D2
print(f"interference zero at omega_1 = {E_MG + d_zero:.2f} eV; |D|^2 there = {abs(D(d_zero))**2:.2e} eV^-2")

# --- on resonance ------------------------------------------------------------------------------
r0 = rate(0.0)
casc = (4 * O_MG**2 / G_W) * (G_ION / G_W)
print(f"on resonance: |D|^2 = {abs(D(0.0))**2:.4e} eV^-2, rate = {r0:.4e} eV = {r0 * EV_TO_INV_S:.3e} s^-1")
print(f"   cascade (4|O|^2/G_w) * (G_ion/G_w) = {casc:.4e} eV; ratio rate/cascade = {r0 / casc:.6f}")
print(f"   first-order rate into m on resonance 4|O|^2/G_w = {4 * O_MG**2 / G_W:.2e} eV; branching {G_ION / G_W:.2f}")
print(f"   on/off-resonance ratio = {r0 / rate(1.20 - E_MG):.3e}")


# --- broadband beam 1: delta part + finite part ------------------------------------------------
def gauss(x, c):
    return np.exp(-(x - c)**2 / (2 * SIG_L**2)) / (np.sqrt(2 * np.pi) * SIG_L)


def fp_inv_x2(c):
    """Hadamard finite part of int g(x)/x^2 dx = int_0^inf [g(x) + g(-x) - 2 g(0)]/x^2 dx."""
    f = lambda x: (gauss(x, c) + gauss(-x, c) - 2 * gauss(0, c)) / x**2 if x > 1e-9 else (
        (gauss(1e-4, c) + gauss(-1e-4, c) - 2 * gauss(0, c)) / 1e-8)
    a = quad(f, 0, 20 * SIG_L + abs(c), limit=400, points=[abs(c)])[0]
    b = -2 * gauss(0, c) / (20 * SIG_L + abs(c))           # tail of -2 g(0)/x^2 beyond the cutoff (g itself negligible)
    return a + b


# Gaussian check of the finite part: fp int e^{-x^2/2s^2}/(sqrt(2 pi) s x^2) dx = -1/s^2
assert abs(fp_inv_x2(0.0) * SIG_L**2 + 1) < 1e-6, fp_inv_x2(0.0) * SIG_L**2

for c in [0.0, 0.030]:
    lo, hi = c - 12 * SIG_L, c + 12 * SIG_L
    exact_res = quad(lambda x: gauss(x, c) / (x**2 + G_W**2 / 4), lo, hi, points=[0.0], limit=800)[0]
    exact_tot = quad(lambda x: gauss(x, c) * abs(D(x))**2, lo, hi, points=[0.0], limit=800)[0]
    delta_part = 2 * np.pi / G_W * gauss(0, c)
    fp_part = fp_inv_x2(c)
    # cross term between the two orderings, 2 PV int g(x)/x dx / delta_2 (Cauchy weight; zero for c = 0 by symmetry)
    cross = 2 / D2 * quad(lambda x: gauss(x, c), lo, hi, weight="cauchy", wvar=0.0)[0]
    nonres = 1 / D2**2
    approx_tot = delta_part + fp_part + cross + nonres
    print(f"broadband beam 1 centered at delta_c = {c * 1e3:.0f} meV, rms {SIG_L * 1e3:.0f} meV (all in eV^-2):")
    print(f"   delta part {delta_part:.4e}, finite part {fp_part:.4e} ({fp_part / delta_part:+.4f} of delta part), "
          f"cross PV {cross:.3e}, non-resonant {nonres:.3f}")
    print(f"   resonant ordering: exact {exact_res:.5e}, delta + fp {delta_part + fp_part:.5e}, "
          f"rel. diff {(delta_part + fp_part) / exact_res - 1:+.2e}; delta alone {delta_part / exact_res - 1:+.2e}")
    print(f"   total: exact {exact_tot:.5e}, approx {approx_tot:.5e}, rel. diff {approx_tot / exact_tot - 1:+.2e}")
    print(f"   expected O(G_w) remainder -pi G_w g''(0)/4 relative: "
          f"{-np.pi * G_W / 4 * ((c**2 - SIG_L**2) / SIG_L**4) * gauss(0, c) / exact_res:+.2e}")

# --- App. D.3: pole correction for the flat continuum of WE 2.1 (Gamma/E_w = 0.01) --------------------------------
GAM_OVER_EW = 0.01
Rp = 2 * GAM_OVER_EW / np.pi                     # R'(0) = 2 Gamma/(pi E_w)
surv = np.exp(-1 / (1 - Rp)) / (1 - Rp)**2       # Z^2 exp(-Gamma t/(1 - R')) at Gamma t = 1
print(f"D.3: R'(0) = {Rp:.4f}; survival at Gamma t = 1 exceeds e^-1 by {surv - np.exp(-1):.4f}, "
      f"{(surv - np.exp(-1)) / (1 - np.exp(-1)) * 100:.2f}% of the depletion")

# ---- figure ---------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.6))

x = np.linspace(-6, 6, 1201)           # x in units of Gamma_w
z = 1 / (x + 0.5j)                     # (Gamma_w) / (x + i Gamma_w/2) with Gamma_w = 1
ax1.axhline(0, color="0.6", lw=0.5); ax1.axvline(0, color="0.6", lw=0.5)
ax1.plot(x, z.real, color="C0", label=r"real part")
ax1.plot(x, z.imag, color="C3", label=r"imaginary part")
xp = x[x > 0.15]; xn = x[x < -0.15]
# italic Γ_w (width) via \mathit{Γ}: matplotlib mathtext lacks \varGamma
ax1.plot(xp, 1 / xp, color="k", ls="--", lw=0.8, label=r"$\mathit{Γ}_{\mathrm{w}}/x$")
ax1.plot(xn, 1 / xn, color="k", ls="--", lw=0.8)
ax1.set_xlim(-6, 6); ax1.set_ylim(-2.15, 1.3)
ax1.set_xlabel(r"$x/\mathit{Γ}_{\mathrm{w}}$")
ax1.set_ylabel(r"$\mathit{Γ}_{\mathrm{w}}/(x + \mathrm{i}\mathit{Γ}_{\mathrm{w}}/2)$")
ax1.set_title("(a)", fontsize=9)
ax1.legend(fontsize=7, loc="upper left", frameon=False)   # lower right ran into the imaginary part near x = 0

w1 = np.linspace(1.00, 1.80, 8001)
w1 = np.union1d(w1, E_MG + np.linspace(-0.01, 0.01, 2001))
ax2.semilogy(w1, rate(w1 - E_MG) * EV_TO_INV_S, color="C0", label="both orderings")
ax2.semilogy(w1, rate(w1 - E_MG, both=False) * EV_TO_INV_S, color="C1", ls="--", lw=0.9,
             label="beam 1 absorbed first only")
ax2.axvline(E_MG, color="0.6", lw=0.5, ls=":")
ax2.set_xlim(1.0, 1.8); ax2.set_ylim(1e0, 1e11)
ax2.set_xlabel(r"frequency of beam 1, $\omega_1$ (eV)")
ax2.set_ylabel(r"two-photon rate (s$^{-1}$)")
ax2.set_title("(b)", fontsize=9)
ax2.legend(fontsize=7, loc="upper left", frameon=False)
fig.tight_layout()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch02", "fig2_5.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
