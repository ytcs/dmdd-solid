"""Fig. 2.6: upward and downward transitions of a thermal two-level system (Sect. 2.5), and every number quoted in
Sect. 2.5 (two-level weights, Worked example 2.7 on the thermal oscillator, free Fermi gas of silicon's valence electrons).
Output: tex/figures/ch02/fig2_6.pdf. Natural units hbar = c = k_B = 1; energies in eV.

Model of the figure: two levels |0>, |1> with splitting Delta (Delta_tl in the text and labels), an operator O with |<1|O|0>| = |<0|O|1>| (e.g. Hermitian),
Gibbs weights p0 = 1/(1 + e^{-Delta/T}), p1 = e^{-Delta/T}/(1 + e^{-Delta/T}). The transition sum is
S_O(omega) = |O_10|^2 [p0 delta(omega - Delta) + p1 delta(omega + Delta)]. Panel (a) draws the two delta weights as stems at
T = Delta/2 (a display choice). Panel (b) draws p0 and p1 against T/Delta, with their ratio e^{-Delta/T}.

Inputs and their sources:
  k_B = 8.617333262e-5 eV/K                         (CODATA 2018, exact SI definitions)
  m_e = 0.51099895e6 eV                             (CODATA 2018)
  hbar c = 1.973269804e-5 eV cm                     (CODATA 2018), so 1 cm^-1 = 1.973269804e-5 eV
  c = 299792.458 km/s
  n_e(Si valence) = 2.00e23 cm^-3                   (App. A.2 of the book: 4 valence electrons per atom, a = 5.431 A)
  q0 = alpha m_e = 3.73 keV                         (Sect. 1.3 of the book, eq:1.3-q0); alpha = 1/137.035999
  v_max = 2.650e-3                                  (Sect. 1.2 of the book, eq:1.2-vmax, 794.5 km/s)
  omega0 = 64 meV, silicon optical phonon at Gamma  (15.5 THz from neutron data, Nilsson and Nelin, PRB 6, 3777 (1972);
                                                    App. A.1 of the book: 15.5 THz = 64.1 meV; Raman 520 cm^-1 = 64.5 meV)
  omega0 = 1 meV, an acoustic phonon                (illustrative choice of Worked example 2.7)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

KB = 8.617333262e-5          # eV/K
ME = 0.51099895e6            # eV
HBARC_CM = 1.973269804e-5    # eV cm
C_KMS = 299792.458
ALPHA = 1 / 137.035999084


def nB(x, T):
    """Bose function n_B(x) = 1/(e^{x/T} - 1)."""
    return 1.0 / np.expm1(x / T)


# ---- two-level weights quoted in the text --------------------------------------------------------------------------
for r in (0.5, 1.0):
    p0 = 1 / (1 + np.exp(-1 / r)); p1 = 1 - p0
    print(f"two-level, T = {r} Delta: p0 = {p0:.3f}, p1 = {p1:.3f}, ratio p1/p0 = {p1/p0:.4f}")

# ---- Worked example 2.7: thermal oscillator --------------------------------------------------------------------------
print("\nWorked example 2.7: n_B, loss/gain ratio e^{omega0/T} = (n+1)/n, total weight 2n+1")
for w0, TK in ((0.064, 300.0), (0.064, 4.0), (0.001, 1.0), (0.001, 0.02), (0.001, 20.0)):
    T = KB * TK
    b = w0 / T
    n = nB(w0, T)
    # log10 of n_B for tiny values
    log10n = -b / np.log(10) if b > 50 else np.log10(n)
    print(f"omega0 = {w0*1e3:.0f} meV, T = {TK:g} K: T = {T*1e3:.4g} meV, beta*omega0 = {b:.4g}, "
          f"n_B = 10^{log10n:.4g} = {n:.4g}, (n+1)/n = e^(beta w0) = 10^{b/np.log(10):.4g}, 2n+1 = {2*n+1:.4g}")
    assert np.isclose((n + 1) / n, np.exp(b)) if b < 50 else True

# check the detailed-balance identity numerically for a truncated oscillator (Gibbs sum over 400 levels)
T = KB * 300.0; w0 = 0.064
lev = np.arange(400); p = np.exp(-lev * w0 / T); p /= p.sum()
up = np.sum(p * (lev + 1)); down = np.sum(p[1:] * lev[1:])
assert np.isclose(up / down, np.exp(w0 / T)) and np.isclose(down, nB(w0, T))
assert np.isclose(up - down, 1.0)          # first moment / omega0 = 1, temperature independent
print(f"check (300 K, 64 meV): sum p_n (n+1) = {up:.6f}, sum p_n n = {down:.6f}, difference = {up-down:.6f}")

# ---- free Fermi gas: silicon valence density ------------------------------------------------------------------------
ne = 2.00e23 * HBARC_CM**3                  # eV^3
kF = (3 * np.pi**2 * ne) ** (1 / 3)         # eV
EF = kF**2 / (2 * ME)
vF = kF / ME
NF = ME * kF / (2 * np.pi**2)               # eV^2, per spin and volume
q0 = ALPHA * ME
print(f"\nFermi gas, n_e = 2.00e23 cm^-3 = {ne:.4g} eV^3")
print(f"k_F = {kF:.4g} eV = {kF/q0:.3f} q0;  E_F = {EF:.4g} eV;  v_F = {vF:.4g} = {vF*C_KMS:.4g} km/s = {vF/2.650e-3:.3f} v_max")
print(f"N_F = {NF:.4g} eV^2 per spin; 2 N_F E_F / n_e = {2*NF*EF/ne:.4f} (must be 3/2)")
print(f"T/E_F at 300 K: {KB*300/EF:.3g}; at 10 mK: {KB*0.01/EF:.3g}")
assert np.isclose(2 * NF * EF / ne, 1.5)
assert np.isclose(kF**3 / (3 * np.pi**2), ne)


def unblocked(x):
    """Fraction of the Fermi sphere whose electrons can take momentum q = x k_F (target state outside the sphere)."""
    x = np.asarray(x, float)
    return np.where(x < 2, 0.75 * x - x**3 / 16, 1.0)


# Monte Carlo check of the closed form
rng = np.random.default_rng(1)
pts = rng.uniform(-1, 1, (400000, 3)); pts = pts[np.sum(pts**2, 1) < 1]
for x in (0.1, 0.5, 1.0, 1.9):
    mc = np.mean(np.sum((pts + np.array([x, 0, 0]))**2, 1) > 1)
    assert abs(mc - unblocked(x)) < 3e-3, (x, mc)
    print(f"unblocked fraction at q = {x} k_F: {float(unblocked(x)):.4f} (Monte Carlo {mc:.4f})")
print(f"q = 0.1 q0 = {0.1*q0:.4g} eV = {0.1*q0/kF:.4f} k_F -> unblocked {float(unblocked(0.1*q0/kF)):.4f}")

# ---- figure ---------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.5), gridspec_kw={"width_ratios": [1, 1.25]})

r = 0.5
p0 = 1 / (1 + np.exp(-1 / r)); p1 = 1 - p0
ax1.axhline(0, color="0.5", lw=0.6)
ax1.vlines([1], 0, [p0], color="C0", lw=2.2)
ax1.vlines([-1], 0, [p1], color="C3", lw=2.2)
ax1.plot([1], [p0], "o", color="C0", ms=4); ax1.plot([-1], [p1], "o", color="C3", ms=4)
ax1.annotate(f"upward\n$p_0 = {p0:.3f}$", (1, p0), (1.12, 0.62), fontsize=8, color="C0")
ax1.annotate(f"downward\n$p_1 = {p1:.3f}$", (-1, p1), (-1.85, 0.30), fontsize=8, color="C3")
ax1.set_xlim(-2, 2); ax1.set_ylim(0, 1.05)
ax1.set_xticks([-1, 0, 1]); ax1.set_xticklabels([r"$-\Delta_{\mathrm{tl}}$", "0", r"$\Delta_{\mathrm{tl}}$"])
ax1.set_xlabel(r"energy given to the system, $\omega$")
ax1.set_ylabel(r"weight of $\delta$ in $\mathcal{S}_O(\omega)/|O_{10}|^2$")
ax1.set_title(r"(a) $T = \Delta_{\mathrm{tl}}/2$", fontsize=9)

t = np.linspace(0.02, 3, 400)
P0 = 1 / (1 + np.exp(-1 / t)); P1 = 1 - P0
ax2.plot(t, P0, color="C0", label=r"upward, $p_0$ ($\omega = +\Delta_{\mathrm{tl}}$)")
ax2.plot(t, P1, color="C3", label=r"downward, $p_1$ ($\omega = -\Delta_{\mathrm{tl}}$)")
ax2.plot(t, np.exp(-1 / t), color="k", ls="--", lw=1, label=r"ratio $p_1/p_0 = \mathrm{e}^{-\Delta_{\mathrm{tl}}/T}$")
ax2.axhline(0.5, color="0.6", lw=0.6, ls=":")
ax2.set_xlim(0, 3); ax2.set_ylim(0, 1.45)
ax2.set_xlabel(r"temperature $T/\Delta_{\mathrm{tl}}$")
ax2.set_ylabel("weight"); ax2.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax2.set_title("(b)", fontsize=9)
ax2.legend(fontsize=7, loc="upper right", frameon=False)
fig.tight_layout()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch02", "fig2_6.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
