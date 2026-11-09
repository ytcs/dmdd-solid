"""Bethe stopping from the loss function (Sect. 19.3): Limit Check 19.3b (lim:19.3b, fig:19-limit-bethe), Worked example 19.3
(we:19-lnI) and every stopping number printed in Sect. 19.3.
Log: bethe19_3.log.  Run: python bethe19_3.py > bethe19_3.log  (about two minutes).
Natural units, Heaviside-Lorentz (e^2 = 4 pi alpha); energies and momenta in eV; hbar c = 1973.27 eV A.

(1) Dielectric stopping, eq:4.4-dEdx:  -dE/dx = (2 Z1^2 alpha/(pi v^2)) int dq/q int_0^{qv} dw w L(q, w), T = 0.
    Bethe limit, eq:19.3-bethe:          -dE/dx = (4 pi Z1^2 alpha^2 n_e/(m_e v^2)) ln(2 m_e v^2 / I),
    ln I = (2/(pi w_p^2)) int dw w L(0, w) ln w   (eq:19.3-lnI).
(2) Model loss function for the limit check: the electron gas at the valence density of silicon, n_e = 32/a^3, a = 5.431 A
    (k_F = 1.8085 A^-1, v_F = 6.98e-3, w_p = 16.6 eV as in Sect. 4.4), Mermin dielectric function (Sect. 4.5) with relaxation
    rate gamma = 0.1 w_p (MODELLING CHOICE, named in the caption; Mermin keeps the f-sum for any gamma).  Lindhard function at
    complex frequency in the closed form of Sect. 4.5/App. D.8 continued to Im w > 0 on the principal branch.
(3) Silicon mean excitation energy from data: Franta et al. 2017 optical constants (4 meV-40 eV) and Henke et al. 1993
    scattering factors (40 eV-30 keV), spliced at 40 eV exactly as figscripts/ch10/abs10_7.py (imported).  Reference:
    I = 173.0 eV and hbar w_p = 31.05 eV for silicon (PDG, Atomic and Nuclear Properties of Materials, 2024).
(4) Worked example 19.3: valence single oscillator of Worked example 4.9 at q -> 0: w_p = 16.6 eV, E_bar = 17.4 eV,
    Gamma_w = 3.66 eV.
Silicon recoil speeds v = sqrt(2 E_R/M), M = 28.0855 u = 2.6162e10 eV.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
OUT = os.path.abspath(os.path.join(HERE, "..", "..", "tex", "figures", "ch19"))
os.makedirs(OUT, exist_ok=True)

ALPHA = 1 / 137.035999
ME = 510998.95
HBARC = 1973.2698          # eV A
a_si = 5.431
n_e = 32 / a_si**3 * HBARC**3                  # eV^3
kF = (3 * np.pi**2 * n_e)**(1 / 3)
vF = kF / ME
wp = np.sqrt(4 * np.pi * ALPHA * n_e / ME)
kTF2 = 3 * wp**2 / vF**2
MSI = 28.0855 * 931.49410e6
print(f"valence electron gas: n_e = {n_e/HBARC**3:.5f} A^-3, k_F = {kF/HBARC:.4f} A^-1 = {kF:.1f} eV, v_F = {vF:.4e}, "
      f"w_p = {wp:.3f} eV")
print(f"Born parameter Z1 alpha/v_F for Z1 = 14: {14*ALPHA/vF:.2f}")
for ER in (100.0, 352.0, 1000.0, 10000.0):
    v = np.sqrt(2 * ER / MSI)
    print(f"  Si recoil E_R = {ER:6.0f} eV: v = {v:.4e} = {v/vF:.4f} v_F; Z1 alpha/v = {14*ALPHA/v:.0f}")


def eps_lind(q, w):
    """RPA (Lindhard) dielectric function of the electron gas at complex w (Im w > 0), T = 0."""
    z = q / (2 * kF)
    u = w / (q * vF)
    zm, zp = z - u, z + u
    br = 0.5 + (1 / (8 * z)) * ((1 - zm**2) * np.log((zm + 1) / (zm - 1)) + (1 - zp**2) * np.log((zp + 1) / (zp - 1)))
    return 1 + kTF2 / q**2 * br


GAM = 0.1 * wp


def eps_mermin(q, w):
    w = np.asarray(w, complex)
    el = eps_lind(q, w + 1j * GAM)
    e0 = eps_lind(q, 1e-9j * np.ones_like(w))
    return 1 + (1 + 1j * GAM / w) * (el - 1) / (1 + (1j * GAM / w) * (el - 1) / (e0 - 1))


def loss(q, w):
    return np.imag(-1 / eps_mermin(q, w))


# f-sum check at a few q
for q in (0.2 * kF, kF, 3 * kF):
    w = np.concatenate([np.linspace(1e-4, 4 * wp, 8000), np.geomspace(4 * wp, 200 * (q**2 / (2 * ME) + q * vF + wp), 6000)[1:]])
    fs = np.trapezoid(w * loss(q, w), w) / (np.pi / 2 * wp**2)
    print(f"  f-sum of the Mermin loss function at q = {q/kF:.1f} k_F: {fs:.4f} of (pi/2) w_p^2")

# mean excitation energy of the model at q -> 0 (Drude form of Mermin at q = 0)
w = np.concatenate([np.linspace(1e-4, 10 * wp, 200000), np.geomspace(10 * wp, 1e7, 200000)[1:]])
L0 = wp**2 * GAM * w / ((w**2 - wp**2)**2 + GAM**2 * w**2)
fs0 = np.trapezoid(w * L0, w) / (np.pi / 2 * wp**2)
lnI_gas = np.trapezoid(w * L0 * np.log(w), w) / (np.pi / 2 * wp**2)
I_gas = np.exp(lnI_gas)
print(f"model at q -> 0: f-sum fraction {fs0:.5f}; I = {I_gas:.3f} eV (w_p = {wp:.3f} eV; ratio {I_gas/wp:.4f})")


def stopping(v, Z1=1.0, nq=500):
    """-dE/dx in eV/A for a heavy projectile of speed v (eq:4.4-dEdx) with the Mermin loss function."""
    qmin = 1e-3 * wp / v
    qmax = 2 * ME * (v + vF) * 3 + 20 * kF
    qs = np.geomspace(qmin, qmax, nq)
    inner = np.empty(nq)
    for j, q in enumerate(qs):
        wmax = q * v
        if wmax <= 3 * wp:
            w = np.linspace(1e-6 * wmax, wmax, 2500)
        else:
            w = np.concatenate([np.linspace(1e-6, 3 * wp, 2500), np.geomspace(3 * wp, wmax, 1500)[1:]])
        inner[j] = np.trapezoid(w * loss(q, w), w)
    val = 2 * Z1**2 * ALPHA / (np.pi * v**2) * np.trapezoid(inner / qs, qs)   # eV^2
    return val / HBARC


def bethe(v, I, Z1=1.0):
    return 4 * np.pi * Z1**2 * ALPHA**2 * n_e / (ME * v**2) * np.log(2 * ME * v**2 / I) / HBARC


vs = vF * np.geomspace(0.02, 30, 46)
S = np.array([stopping(v) for v in vs])
Bt = bethe(vs, I_gas)
print("\nZ1 = 1 stopping in the valence electron gas (eV/A):")
print("  v/v_F    full      Bethe(I_model)   full/Bethe   friction coefficient (full)/v")
for v, s_, b in zip(vs, S, Bt):
    print(f"  {v/vF:7.3f}  {s_:.4e}  {b: .4e}      {s_/b if b > 0 else float('nan'):8.4f}     {s_/v:.4e}")
# where the full result is within 10 % and 5 % of Bethe (fine interpolation in log v)
lv = np.log(vs)
rat = np.where(Bt > 0, S / np.where(Bt > 0, Bt, 1), np.nan)
fine = np.geomspace(vs[0], vs[-1], 20000)
rf = np.interp(np.log(fine), lv, np.nan_to_num(rat, nan=10.0))
for lev in (0.10, 0.05):
    bad = np.where(np.abs(rf - 1) > lev)[0]
    vlim = fine[bad.max() + 1] if bad.size and bad.max() + 1 < fine.size else np.nan
    print(f"  full/Bethe within {lev*100:.0f} % for v > {vlim/vF:.2f} v_F (v > {vlim:.3e})")
# Bethe logarithm turns negative
v0 = np.sqrt(I_gas / (2 * ME))
print(f"  Bethe logarithm vanishes at v = sqrt(I/2m_e) = {v0:.3e} = {v0/vF:.3f} v_F")
# low-speed friction
fr = S[:4] / vs[:4]
print(f"  low-speed friction coefficient -dE/dx / v (Z1 = 1): {fr[0]:.3f}, {fr[1]:.3f}, {fr[2]:.3f}, {fr[3]:.3f} eV/A at v/v_F = "
      f"{vs[0]/vF:.3f}, {vs[1]/vF:.3f}, {vs[2]/vF:.3f}, {vs[3]/vF:.3f}")
v1 = np.sqrt(2 * 1000.0 / MSI)
s1 = np.exp(np.interp(np.log(v1), lv, np.log(S)))
print(f"  at the speed of a 1 keV Si recoil: Z1 = 1 stopping {s1:.4f} eV/A; Z1^2 = 196 times: {196*s1:.2f} eV/A "
      f"(Lindhard k_L value 2.77 eV/A, lind19_3.log)")

# ---------------- silicon mean excitation energy from data
import abs10_7 as D
wd = np.concatenate([np.geomspace(0.01, 40, 6000), np.geomspace(40, 30000, 12000)[1:]])
ed = D.eps_si(wd)
Ld = ed.imag / np.abs(ed)**2
wp_tot = np.sqrt(4 * np.pi * ALPHA * 14 * n_e / 4 / ME)
fsum = np.trapezoid(wd * Ld, wd)
print(f"\nsilicon, all 14 electrons: w_p = {wp_tot:.2f} eV (PDG 31.05 eV); (pi/2) w_p^2 = {np.pi/2*wp_tot**2:.1f} eV^2")
print(f"  data f-sum to 30 keV: {fsum:.1f} eV^2 = {fsum/(np.pi/2*wp_tot**2):.4f} of (pi/2) w_p^2")
lnI_data = np.trapezoid(wd * Ld * np.log(wd), wd) / fsum
print(f"  I from the data, normalized to their own f-sum: {np.exp(lnI_data):.1f} eV (PDG: 173.0 eV)")
print(f"  relative to the adopted 173.0 eV: {100*(np.exp(lnI_data)/173.0 - 1):+.1f} %; rescaling L to the exact f-sum leaves I unchanged")
# a normalization S != int w L makes S^-1 int w L ln w depend on the energy unit; not used (shown for eV and keV)
for unit, lab in ((1.0, "eV"), (1e3, "keV")):
    lnr = np.trapezoid(wd * Ld * np.log(wd / unit), wd) / (np.pi / 2 * wp_tot**2)
    print(f"  (unit-dependent variant, not used: exact-f-sum normalization with omega in {lab}: I = {np.exp(lnr)*unit:.1f} eV)")
bands = [(0.01, 90.0, "valence (below the L edge)"), (90.0, 1830.0, "L shell region"), (1830.0, 30000.0, "K shell region")]
print("  decomposition: band, weight w_j (share of the data f-sum), log-mean energy exp<ln w>_j, contribution w_j ln w_j")
tot = 0
for a, b, name in bands:
    m = (wd >= a) & (wd < b)
    wj = np.trapezoid(wd[m] * Ld[m], wd[m]) / fsum
    lj = np.trapezoid(wd[m] * Ld[m] * np.log(wd[m]), wd[m]) / np.trapezoid(wd[m] * Ld[m], wd[m])
    tot += wj * lj
    print(f"    {name:28s} w = {wj:.4f} (electrons {14*wj*fsum/(np.pi/2*wp_tot**2):.2f}), exp<ln w> = {np.exp(lj):8.1f} eV, w ln w = {wj*lj:.4f}")
print(f"    sum = {tot:.4f} = ln({np.exp(tot):.1f} eV)")
m = wd < 40
print(f"  data below 40 eV: f-sum {np.trapezoid(wd[m]*Ld[m], wd[m]):.1f} eV^2 against (pi/2)(16.6)^2 = {np.pi/2*16.6**2:.1f} eV^2 (valence)")

# ---------------- Worked example 19.3: valence oscillator
wpv, Eb, Gw = 16.6, 17.4, 3.66
w = np.concatenate([np.linspace(1e-5, 200, 400000), np.geomspace(200, 1e8, 400000)[1:]])
Lv = wpv**2 * Gw * w / ((w**2 - Eb**2)**2 + Gw**2 * w**2)
fv = np.trapezoid(w * Lv, w) / (np.pi / 2 * wpv**2)
lnIv = np.trapezoid(w * Lv * np.log(w), w) / (np.pi / 2 * wpv**2)
print(f"\nWE 19.3 valence oscillator: f-sum fraction {fv:.5f}; ln I_val = {lnIv:.4f}, I_val = {np.exp(lnIv):.3f} eV against E_bar = {Eb} eV")
# undamped limit and first correction: numerically for smaller damping
for g in (0.5, 1.0, 2.0, 3.66, 7.32):
    Lg = wpv**2 * g * w / ((w**2 - Eb**2)**2 + g**2 * w**2)
    print(f"   Gamma_w = {g:5.2f} eV: I_val = {np.exp(np.trapezoid(w*Lg*np.log(w), w)/(np.pi/2*wpv**2)):.3f} eV; "
          f"(I/E_bar)^2 - 1 = {(np.exp(np.trapezoid(w*Lg*np.log(w), w)/(np.pi/2*wpv**2))/Eb)**2 - 1:.4e}; "
          f"-(Gamma/2E)^2 = {-(g/(2*Eb))**2:.4e}")
# share of each frequency range of the valence model in ln I
for a, b in ((0, 10), (10, 30), (30, 100), (100, 1e8)):
    m = (w >= a) & (w < b)
    print(f"   valence model: weight in {a}-{b:g} eV: {np.trapezoid(w[m]*Lv[m], w[m])/(np.pi/2*wpv**2):.4f}")
# Bethe stopping of a 1 MeV proton and a 10 keV Si recoil with I = 173 eV (all electrons)
ne_tot = 14 * n_e / 4
for name, Z1, M, E in (("1 MeV proton", 1, 938.272e6, 1e6), ("10 keV Si recoil", 14, MSI, 1e4)):
    v = np.sqrt(2 * E / M)
    arg = 2 * ME * v**2 / 173.0
    print(f"  {name}: v = {v:.4e}, 2 m_e v^2 = {2*ME*v**2:.2f} eV, 2 m_e v^2/I = {arg:.3e}, Z1 alpha/v = {Z1*ALPHA/v:.2f}")

# ---------------- Limit Check 19.3b figure
fig, ax = plt.subplots(figsize=(6.0, 3.7))
x = vs / vF
ok = np.abs(rf - 1) <= 0.10
xf = fine / vF
if ok.any():
    first = np.where(ok & (xf > 1))[0][0]
    ax.axvspan(xf[first], x[-1], color="0.88", lw=0)
ax.axvspan(np.sqrt(2 * 100 / MSI) / vF, np.sqrt(2 * 1e4 / MSI) / vF, color="C1", alpha=0.18, lw=0)
ax.text(np.sqrt(2 * 100 / MSI) / vF * 1.05, 15, "Si recoils\n0.1–10 keV", fontsize=7.5, color="C1")
ax.plot(x, S, color="k", lw=1.6, label=r"dielectric stopping, electron gas (Mermin)")
pos = Bt > 0
ax.plot(x[pos], Bt[pos], color="C0", lw=1.3, ls="--", label=r"Bethe, $\ln(2m_ev^2/\bar I)$")
ax.plot(x[:30], fr[0] * vs[:30], color="C3", lw=1.0, ls=":", label="friction $\\propto v$")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(x[0], x[-1])
ax.set_ylim(0.1, 40)
ax.set_xlabel(r"projectile speed $v/v_{\mathrm{F}}$")
ax.set_ylabel(r"$-\mathrm{d}E/\mathrm{d}x$ for $Z_1 = 1$ (eV/Å)")
sec = ax.secondary_xaxis("top", functions=(lambda t: 14 * ALPHA / (np.maximum(t, 1e-12) * vF), lambda b: 14 * ALPHA / (np.maximum(b, 1e-12) * vF)))
sec.set_xlabel(r"Born parameter $Z_1\alpha/v$ for $Z_1 = 14$", fontsize=8)
ax.legend(fontsize=7.5, loc="lower right", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit19_3b.pdf"))
print("\nwrote limit19_3b.pdf")
