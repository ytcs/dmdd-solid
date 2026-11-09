"""Fig. 4.1: poles of the retarded response function in the complex frequency plane (Sect. 4.1), and every number
quoted in Worked examples 4.1 and 4.2. Output: tex/figures/ch04/fig4_1.pdf. Natural units; frequencies in units of the
oscillator frequency omega0 (panel b) or of the level spacing (two-level numbers).

Models (all defined in Sect. 4.1; no external data enter):
  Damped harmonic oscillator (Worked example 4.1). O = lambda (d + d^dagger), lambda^2 = 1/(2 M omega0); classical
  equation of motion M (x'' + Gamma_w x' + omega0^2 x) = -phi_ext(t) with the e^{-i omega t} convention of App. A.3, so
      V R(omega) = 1 / [M (omega^2 + i Gamma_w omega - omega0^2)] = 2 lambda^2 omega0 / (omega^2 + i Gamma_w omega - omega0^2).
  Poles: omega = -i Gamma_w/2 +- sqrt(omega0^2 - Gamma_w^2/4); on the circle |omega| = omega0 for Gamma_w < 2 omega0,
  on the negative imaginary axis for Gamma_w > 2 omega0. Panel (a) marks Gamma_w/omega0 = 0.2, 1, 1.6, 2, 3 (a display
  choice). Panel (b) plots omega0 V R / lambda^2 on the real axis for Gamma_w = 0.2 omega0 (a display choice).
  Finite system (panel a, crosses): Lehmann poles at +-(E_f - E_i) - i0, drawn at an illustrative set of transition
  energies 0.35, 0.55, 0.8, 1.25, 1.6 (in units of omega0) a small distance below the axis (the -i0 is drawn as 0.04).
  Two-level system (Worked example 4.2): p0 - p1 = tanh(Delta/2T); V R(0) = -2 tanh(Delta/2T) |O_10|^2 / Delta.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- Worked example 4.1: oscillator --------------------------------------------------------------------------------
def VR_osc(w, gam, w0=1.0, lam2=1.0):
    """V R(omega) of the damped oscillator, in units lam2 = lambda^2."""
    return 2 * lam2 * w0 / (w**2 + 1j * gam * w - w0**2)

# undamped, from the commutator: lambda^2 [1/(w - w0 + i0) - 1/(w + w0 + i0)], checked off resonance
w = np.array([0.3, 0.7, 1.4, 2.5])
lehmann = 1 / (w - 1.0) - 1 / (w + 1.0)
assert np.allclose(lehmann, VR_osc(w, 0.0).real)
# Lehmann with thermal weights (n_B + 1) and n_B gives the same at any T
for nB in [0.0, 0.109, 3.0]:
    first = (nB + 1) / (w - 1.0) + nB / (w + 1.0)
    second = (nB + 1) / (w + 1.0) + nB / (w - 1.0)
    assert np.allclose(first - second, lehmann)
# static limit and second-order energy: V R(0) = -2 lambda^2/omega0; E2 = (1/2) V R(0) phi^2 = -lambda^2 phi^2/omega0
assert np.isclose(VR_osc(0.0, 0.0).real, -2.0)
# large omega: V R -> 2 lambda^2 omega0 / omega^2 (the double commutator <[O,[H,O]]> = 2 lambda^2 omega0)
assert np.isclose(VR_osc(1e4, 0.0).real * 1e8, 2.0, rtol=1e-6)
# damped: -Im V R at omega0 equals 2 lambda^2/Gamma_w; for Gamma_w = 0.2 omega0 that is 10 lambda^2/omega0
gam_b = 0.2
peak = -VR_osc(1.0, gam_b).imag
assert np.isclose(peak, 2 / gam_b)
print(f"WE 4.1: V R(0) = -2 lambda^2/omega0; -Im V R(omega0) = {peak:.1f} lambda^2/omega0 at Gamma_w = 0.2 omega0")
# poles in the lower half plane for every Gamma_w > 0
def poles(gam, w0=1.0):
    disc = np.sqrt(complex(w0**2 - gam**2 / 4))
    return np.array([-1j * gam / 2 + disc, -1j * gam / 2 - disc])
for g in [1e-3, 0.2, 1.0, 1.6, 2.0, 3.0]:
    p = poles(g)
    assert np.all(p.imag < 0)
    # they are zeros of the denominator
    assert np.allclose(p**2 + 1j * g * p - 1.0, 0.0)
    if g < 2:
        assert np.allclose(np.abs(p), 1.0)
print("poles at Gamma_w = 3 omega0:", np.round(poles(3.0), 3))
# check analyticity numerically: R(z) from the time integral, z in the upper half plane
t = np.linspace(0, 400, 400001)
gam_t = 0.2
w1 = np.sqrt(1 - gam_t**2 / 4)
VRt = -np.exp(-gam_t * t / 2) * np.sin(w1 * t) / w1 * 2   # 2 lambda^2 omega0 * (-(1/M) G(t)) with lambda^2 = 1/(2M)
for z in [0.5 + 0.1j, 1.0 + 0.05j, 2.0 + 0.3j]:
    integral = np.trapezoid(np.exp(1j * z * t) * VRt, t)
    assert np.isclose(integral, VR_osc(z, gam_t), rtol=1e-4), (z, integral, VR_osc(z, gam_t))

# ---- Worked example 4.2: two-level system --------------------------------------------------------------------------
Delta = 1.0
T = 0.5
p0 = 1 / (1 + np.exp(-Delta / T)); p1 = 1 - p0
assert np.isclose(p0 - p1, np.tanh(Delta / (2 * T)))
VR0 = -2 * (p0 - p1) / Delta
print(f"WE 4.2: p0 = {p0:.3f}, p1 = {p1:.3f}, p0 - p1 = {p0 - p1:.3f}, V R(0) = {VR0:.3f} |O10|^2/Delta at T = Delta/2")
assert abs(p0 - 0.881) < 5e-4 and abs(p1 - 0.119) < 5e-4 and abs((p0 - p1) - 0.762) < 5e-4
assert abs(VR0 + 1.523) < 5e-4
# Curie limit: T >> Delta, V R(0) -> -|O10|^2/T
for T in [10.0, 100.0]:
    VR0T = -2 * np.tanh(Delta / (2 * T)) / Delta
    assert np.isclose(VR0T, -1 / T, rtol=1e-2)
# Lehmann form of the two-level response equals the closed form
wv = np.array([0.2, 0.7, 1.5, 3.0])
leh = p0 / (wv - 1) + p1 / (wv + 1) - p0 / (wv + 1) - p1 / (wv - 1)
assert np.allclose(leh, 2 * (p0 - p1) / (wv**2 - 1))

# ---- figure --------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.7), gridspec_kw={"width_ratios": [1.15, 1]})

ax1.axhspan(0, 1.3, color="C0", alpha=0.10, lw=0)
ax1.text(-1.95, 0.45, r"analytic: $\mathrm{Im}\,\omega > 0$", fontsize=8, color="C0")
ax1.axhline(0, color="k", lw=0.6); ax1.axvline(0, color="k", lw=0.4, ls=":")
E = np.array([0.35, 0.55, 0.8, 1.25, 1.6])
ax1.plot(np.r_[E, -E], -0.04 * np.ones(2 * len(E)), "x", color="C3", ms=5, mew=1.1,
         label=r"finite system, $\pm(E_f - E_i) - \mathrm{i}0$")
th = np.linspace(np.pi, 2 * np.pi, 200)
ax1.plot(np.cos(th), np.sin(th), color="0.6", lw=0.8)
ax1.plot([0, 0], [-1, -2.75], color="0.6", lw=0.8)
for g, mk in zip([0.2, 1.0, 1.6, 2.0, 3.0], ["o", "s", "^", "D", "v"]):
    p = poles(g)
    ax1.plot(p.real, p.imag, mk, color="C1", ms=4, mfc="white", mew=1.0)
    lab = rf"$\mathit{{\Gamma}}_{{\mathrm{{w}}}} = {g:g}\,\omega_0$"
    x, y = p[0].real, p[0].imag
    if g < 0.5:
        ax1.annotate(lab, (-x, y), (-x - 0.85, y - 0.30), fontsize=7, color="C1")
    elif g < 2:
        ax1.annotate(lab, (x, y), (x + 0.12, y - 0.05), fontsize=7, color="C1")
    elif g == 2.0:
        ax1.annotate(lab, (0, -1), (0.12, -1.05), fontsize=7, color="C1")
    else:
        ax1.annotate(lab, (0, p.imag.min()), (-1.15, p.imag.min() - 0.02), fontsize=7, color="C1")
ax1.set_xlim(-2.0, 2.0); ax1.set_ylim(-2.8, 1.3)
ax1.set_xlabel(r"$\mathrm{Re}\,\omega/\omega_0$"); ax1.set_ylabel(r"$\mathrm{Im}\,\omega/\omega_0$")
ax1.set_title("(a) poles", fontsize=9)
ax1.legend(fontsize=7, loc="upper right", frameon=False, handletextpad=0.2, borderaxespad=0.2)

wr = np.linspace(0, 2.5, 2001)
vr = VR_osc(wr, gam_b)
ax2.axhline(0, color="k", lw=0.5)
ax2.plot(wr, vr.real, color="C0", label=r"$\mathrm{Re}$")
ax2.plot(wr, -vr.imag, color="C3", label=r"$-\mathrm{Im}$")
ax2.axvline(1.0, color="0.6", lw=0.6, ls=":")
ax2.set_xlim(0, 2.5); ax2.set_ylim(-6, 11)
ax2.set_xlabel(r"$\omega/\omega_0$"); ax2.set_ylabel(r"$\omega_0 \mathscr{V} R/\lambda_{\mathrm{osc}}^2$")
ax2.set_title(r"(b) $\mathit{\Gamma}_{\mathrm{w}} = 0.2\,\omega_0$", fontsize=9)
ax2.legend(fontsize=7, loc="upper right", frameon=False)

fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch04", "fig4_1.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
