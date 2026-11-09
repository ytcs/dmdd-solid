"""Fig. 6.8 (fig:6-edge) and the numbers of Worked example 6.5 (we:6-siedge): the Hall-Bardeen-Blatt edge of silicon.

Model (eq:6.5-edge, derived in App. D.18, eq:D.18-edge): for each phonon branch nu that assists the transition,
    alpha_abs(omega) = sum_nu A_nu [ n_nu (omega - Eg + w_nu)^2 Theta(...) + (n_nu + 1)(omega - Eg - w_nu)^2 Theta(...) ],
free electron-hole pairs (no exciton), parabolic bands, matrix elements constant across the edge.

Inputs and their sources:
  Eg = 1.17 eV       low-temperature indirect gap of Si, as used in Sect. 3.3 (Ramanathan; Table 3.1 of the book).
  w_TA = k_B * 212 K, w_TO = k_B * 670 K  phonon energies from the absorption-edge fine structure of Macfarlane, McLean,
                     Quarrington and Roberts, Phys. Rev. 111, 1245 (1958) (theta = 212 K and 670 K; branch assignment TA, TO
                     as in Yu and Cardona, Fundamentals of Semiconductors, Chap. 6).
  k_B = 86.17 ueV/K  (Sect. 2.5).
  Neutron values at X for comparison (Sect. 5.2): TA 4.49 THz, TO 13.90 THz; 1 THz = 4.13567 meV.
  Flatness of the branches between 0.85 X (= k_c, Sect. 3.3) and X, from the PBE dispersion of Sect. 5.2
  (figscripts/ch05/fig5_2_data.npz, path index 51 = 0.85 X, 60 = X): TA 137.77 / 137.62 cm^-1 (ratio 1.001),
  TO 463.08 / 461.92 cm^-1 (ratio 1.0025); recomputed below.
  E_x^b = 14.7 meV   exciton binding of Si, Shaklee and Nahory, PRL 24, 942 (1970) (Sect. 4.9): the measured kinks are
                     exciton thresholds, E_x^b below the free-pair ones.

Modelling choices (named in the caption): A_TO = A_TA (equal coefficients; the figure shows the shape,
not the measured ratio of the two branches); the gap is held at 1.17 eV at every temperature, so that the
figure isolates the occupation factors (the shift of the gap with T is the subject of Sect. 6.3); free pairs only.
Run: python fig6_8.py   (numpy, matplotlib; a few seconds)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch06", "fig6_8.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

kB = 86.17e-6          # eV/K
THz = 4.13567e-3       # eV per THz
Eg = 1.17
wTA, wTO = 212 * kB, 670 * kB
Exb = 14.7e-3

# --- flatness of the branches between k_c = 0.85 X and X (PBE, Sect. 5.2) ---
d = np.load(os.path.join(HERE, "..", "ch05", "fig5_2_data.npz"))
q, f = d["q"], d["f"]
assert abs(q[51, 2] - 0.85) < 1e-6 and abs(q[60, 2] - 1.0) < 1e-6
rTA, rTO = f[51, 0] / f[60, 0], f[51, 5] / f[60, 5]
print(f"PBE 0.85X/X: TA {f[51,0]:.2f}/{f[60,0]:.2f} cm-1 ratio {rTA:.4f}; TO {f[51,5]:.2f}/{f[60,5]:.2f} ratio {rTO:.4f}")

print(f"w_TA = {wTA*1e3:.2f} meV (neutron X: {4.49*THz*1e3:.2f}), w_TO = {wTO*1e3:.2f} meV (neutron X: {13.90*THz*1e3:.2f})")
thr = {"Eg-wTO": Eg - wTO, "Eg-wTA": Eg - wTA, "Eg+wTA": Eg + wTA, "Eg+wTO": Eg + wTO}
for k, v in thr.items():
    print(f"threshold {k}: {v:.4f} eV  (exciton replica {v - Exb:.4f} eV)")


def nB(w, T):
    if T <= 0:
        return 0.0
    x = w / (kB * T)
    return 0.0 if x > 700 else 1.0 / np.expm1(x)


for T in (300.0, 77.0, 20.0, 0.010):
    nTA, nTO = nB(wTA, T), nB(wTO, T)
    print(f"T = {T:g} K (kT = {kB*T*1e3:.3f} meV): n_TA = {nTA:.3e}, n_TO = {nTO:.3e}; "
          f"slope ratio abs/em TA sqrt(n/(n+1)) = {np.sqrt(nTA/(nTA+1)):.3e}, TO = {np.sqrt(nTO/(nTO+1)):.3e}; "
          f"e^(-w/2T): TA {np.exp(-wTA/(2*kB*T)) if T > 1 else 0:.3e}")
    # detailed balance check: n/(n+1) = exp(-w/T)
    if T > 1:
        assert abs(nTA / (nTA + 1) - np.exp(-wTA / (kB * T))) < 1e-12
        assert abs(nTO / (nTO + 1) - np.exp(-wTO / (kB * T))) < 1e-12
x10 = wTA / (kB * 0.010)
print(f"10 mK: w_TA/T = {x10:.3e}, n_TA = exp(-{x10:.0f})")

# slopes of sqrt(alpha) per component, in units of sqrt(A): emission sqrt(n+1), absorption sqrt(n)
for T in (300.0, 77.0):
    for name, w in (("TA", wTA), ("TO", wTO)):
        n = nB(w, T)
        print(f"T={T:g} K {name}: slope abs sqrt(n) = {np.sqrt(n):.3f}, slope em sqrt(n+1) = {np.sqrt(n+1):.3f} (units sqrt(A))")
# 2T*ln(slope ratio) recovers w (thermometer)
n = nB(wTA, 300.0)
print("thermometer check: w_TA from slope ratio at 300 K =", -2 * kB * 300 * np.log(np.sqrt(n / (n + 1))) * 1e3, "meV")


def alpha(om, T, A=(1.0, 1.0)):
    out = np.zeros_like(om)
    comps = []
    for Anu, w in zip(A, (wTA, wTO)):
        n = nB(w, T)
        ca = Anu * n * np.clip(om - Eg + w, 0, None) ** 2
        ce = Anu * (n + 1) * np.clip(om - Eg - w, 0, None) ** 2
        comps += [ca, ce]
        out += ca + ce
    return out, comps


om = np.linspace(1.08, 1.26, 1801)
plt.rcParams.update({"font.size": 8, "font.family": "serif", "mathtext.fontset": "cm"})
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.7))
cols = {300.0: "#c4661f", 150.0: "#7a5ea8", 77.0: "#2a6fb0"}
ax = axs[0]
for T, c in cols.items():
    a, _ = alpha(om, T)
    ax.plot(om, np.sqrt(a) * 1e3, color=c, lw=1.2, label=f"{T:g} K")
for k, v in thr.items():
    ax.axvline(v, color="0.6", lw=0.6, ls=":")
ax.axvline(Eg, color="0.3", lw=0.6, ls="--")
ax.text(Eg + 0.0015, 150, r"$E_{\mathrm{g}}$", fontsize=7, color="0.3")
ax.set_xlabel(r"photon energy $\omega$ (eV)")
ax.set_ylabel(r"$\sqrt{\alpha_{\mathrm{abs}}/A}$ (meV)")
ax.set_xlim(om[0], om[-1]); ax.set_ylim(0, 170)
ax.legend(frameon=False, fontsize=7, loc="upper left", bbox_to_anchor=(0.0, 0.88))
ax.set_title("(a) sum of all components", fontsize=8)
labs = [r"$-\omega_{\mathrm{TO}}$", r"$-\omega_{\mathrm{TA}}$", r"$+\omega_{\mathrm{TA}}$", r"$+\omega_{\mathrm{TO}}$"]
for (k, v), lab in zip(thr.items(), labs):
    ax.text(v + 0.0015, 163, lab, fontsize=6, ha="left", va="center", color="0.35")

ax = axs[1]
T = 300.0
a, comps = alpha(om, T)
names = [r"TA, absorption ($\propto n$)", r"TA, emission ($\propto n+1$)", r"TO, absorption", r"TO, emission"]
styles = [("#2a6fb0", "--"), ("#2a6fb0", "-"), ("#c4661f", "--"), ("#c4661f", "-")]
for cmp, nm, (c, ls) in zip(comps, names, styles):
    ax.plot(om, np.sqrt(cmp) * 1e3, color=c, ls=ls, lw=1.0, label=nm)
ax.plot(om, np.sqrt(a) * 1e3, color="k", lw=1.4, label="sum")
ax.set_xlabel(r"photon energy $\omega$ (eV)")
ax.set_xlim(om[0], om[-1]); ax.set_ylim(0, 170)
ax.legend(frameon=False, fontsize=6, loc="upper left")
ax.set_title(r"(b) components at 300 K", fontsize=8)
fig.tight_layout()
fig.savefig(OUT)
print("wrote", OUT)
