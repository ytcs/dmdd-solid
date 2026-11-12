"""Figs. 4.3 and 4.4 of Sect. 4.3 (causality and sum rules), and every number quoted in Sect. 4.3, its Worked examples
4.5-4.7 and Appendix D.6.  Natural units hbar = c = k_B = 1 unless stated.

Outputs: tex/figures/ch04/fig4_3.pdf  (a) the contour behind the Kramers-Kronig relations; (b) Kramers-Kronig
                                          reconstruction of Re R for the damped oscillator of Worked example 4.1.
         tex/figures/ch04/fig4_3b.pdf (a) cumulative Thomas-Reiche-Kuhn sum of hydrogen 1s; (b) cumulative oscillator
                                          strength of silicon per atom from the Henke tables.

Inputs and their sources
  Constants (CODATA 2018): m_e = 510998.95 eV, alpha = 1/137.035999, hbar c = 197.3269804 eV nm,
     Rydberg energy I_H = alpha^2 m_e / 2 = 13.6057 eV, atomic mass unit 931.49410 MeV.
  Silicon valence density n_e = 2.00e23 cm^-3 (App. A.2 of the book; 8 electrons per 40.05 A^3 cell); all 14 electrons
     per atom: 3.5 times that.  Si atomic mass 28.0855 u.
  Measured electronic dielectric constant of Si: eps_inf = 11.7 (book convention).
  Band gap E_g = 1.17 eV, the low-temperature gap (book convention, Sect. 1.3).
  Hartree-Fock total energy of the Si atom E_HF = -288.854 hartree (Roothaan-Hartree-Fock tables of Bunge, Barrientos
     and Bunge, At. Data Nucl. Data Tables 53, 113 (1993)); virial theorem <T> = -E for a Coulomb Hamiltonian.
  Hydrogen (I below = E_B = 13.6 eV of the text) oscillator strengths (Bethe and Salpeter, Quantum Mechanics of One- and Two-Electron Atoms, Sect. 61, closed
     forms evaluated here):  f_{1s->np} = 2^8 n^5 (n-1)^(2n-4) / (3 (n+1)^(2n+4));
     continuum, per unit photon energy w (w > I):  df/dw = (2^7 / 3 I) (I/w)^4 exp(-4 eta arccot eta) / (1 - exp(-2 pi eta)),
     eta = (I/(w - I))^(1/2).  [Equivalent to the photoionization cross-section sigma = (2 pi^2 alpha/m_e) df/dw with
     sigma_threshold = 6.30e-18 cm^2, checked below.]
  Hydrogen 2p form factor at q0 = alpha m_e (Sect. 2.2 closed form): |f_{1s->2p}|^2 = 72 (q a0)^2 / (9/4 + q^2 a0^2)^6.
  Henke, Gullikson and Davis, At. Data Nucl. Data Tables 54, 181 (1993), tables as distributed by CXRO
     (https://henke.lbl.gov/optical_constants/sf/si.nff):
     columns E (eV), f1, f2.  Tables' convention: f2(E) = (pi/2) E df/dE, so df/dE = 2 f2 / (pi E) per atom.
     Used from 30 eV (lower bound chosen for this book; the 1993 paper covers 50 eV - 30 keV and the distributed file
     starts at 10 eV) to 30 keV; the region above 30 keV is a power-law extrapolation of the last decade.
  Edge energies of Si, read off as the steps of f2 in the same tables: L2,3 rise between 99.6 and 100.9 eV (taken as 99.8 eV),
     K between 1838 and 1840 eV (taken as 1839 eV).
Modelling choices
  KK reconstruction: damped oscillator V R = 2 lam^2 w0 / (w^2 + i G w - w0^2), G = 0.2 w0 (as Fig. 4.1b), PV integral
  by scipy quad with Cauchy weight, upper limit 4000 w0 (tail below 1e-6).
  Figure contour: schematic positions only (pole at z = 0.6 + 0.35 i, indentation radius 0.12, semicircle radius 2).
"""
import os
import numpy as np
from scipy import integrate
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(BOOK, "tex", "figures", "ch04")
os.makedirs(OUT, exist_ok=True)

me = 510998.95            # eV
alpha = 1 / 137.035999
hbarc_cm = 197.3269804e-7  # eV cm
IH = alpha**2 * me / 2     # eV
e2 = 4 * np.pi * alpha
u = 931.49410e6            # eV


def close(a, b, rtol=5e-3, name=""):
    assert abs(a - b) <= rtol * abs(b), f"{name}: {a} vs {b}"
    print(f"  {name:55s} {a:.6g}   (quoted {b})")


print("== plasma frequencies and the f-sum (Sect. 4.3)")
n_val = 2.00e23 * hbarc_cm**3           # eV^3
n_all = 3.5 * n_val
wp = np.sqrt(e2 * n_val / me)
wp_all = np.sqrt(e2 * n_all / me)
close(wp, 16.6, name="omega_p, valence (eV)")
close(wp_all, 31.1, name="omega_p, all 14 electrons (eV)")
close(np.pi / 2 * wp**2, 433, name="(pi/2) omega_p^2 (eV^2), App. E.6 value")

print("== Kramers-Kronig + f-sum: mean energy of S at q -> 0 (Sect. 4.3)")
eps_inf = 11.7
Ebar = wp / np.sqrt(1 - 1 / eps_inf)
close(1 - 1 / eps_inf, 0.915, name="1 - 1/eps_inf")
close(Ebar, 17.4, name="E_bar = omega_p / sqrt(1 - 1/eps_inf) (eV)")

print("== relativistic (mass-velocity) correction (Sect. 4.3, App. D.6)")
Ha = 2 * IH
T_tot = 288.854 * Ha
Kbar = T_tot / 14
close(T_tot, 7860, name="total kinetic energy of the Si atom (eV)")
close(Kbar, 561, name="Kbar per electron (eV)")
close(5 / 3 * Kbar / me, 1.83e-3, name="(5/3) Kbar/m_e")
close(14 * 5 / 3 * Kbar / me, 0.026, rtol=2e-2, name="electrons per atom removed")
K1s = 14**2 * IH
close(K1s, 2670, rtol=2e-3, name="hydrogenic 1s kinetic energy Z^2 I (eV)")
close(5 / 3 * K1s / me, 8.7e-3, rtol=5e-3, name="(5/3) K_1s / m_e")
for q, val in [(10e3, 9.6e-5), (53e3, 2.7e-3)]:
    close(q**2 / (4 * me**2), val, rtol=1e-2, name=f"q^2/4m^2 at q = {q/1e3:.0f} keV")
# symbolic check of the double commutator of p^4 (one particle, isotropic average)
import sympy as sp
px, py, pz, qz = sp.symbols("p_x p_y p_z q", real=True)
p2 = px**2 + py**2 + pz**2
dc = sp.expand((px**2 + py**2 + (pz + qz)**2)**2 + (px**2 + py**2 + (pz - qz)**2)**2 - 2 * p2**2)
assert sp.simplify(dc - (4 * p2 * qz**2 + 8 * pz**2 * qz**2 + 2 * qz**4)) == 0
print("  (p+q)^4 + (p-q)^4 - 2p^4 = 4p^2q^2 + 8(p.q)^2 + 2q^4   verified")
# p^2 terms: -(1/8m^3)[4 + 8/3] p^2 q^2 = -(5/6) p^2 q^2 / m^3 ;  relative to q^2/m: -(5/3) (p^2/2m)/m
assert sp.Rational(1, 8) * (4 + sp.Rational(8, 3)) == sp.Rational(5, 6)

print("== nuclear share of the charge f-sum (Sect. 4.3)")
M_Si = 28.0855 * u
close(14 * me / M_Si, 2.73e-4, rtol=2e-3, name="Z^2 n_k m_e / (n_e M_k), Si all-electron")

print("== Worked example 4.5: hydrogen TRK")
def f_np(n):
    n = np.asarray(n, dtype=float)
    return np.exp(np.log(2**8 / 3) + 5 * np.log(n) + (2 * n - 4) * np.log(n - 1) - (2 * n + 4) * np.log(n + 1))

f2p = 2**8 * 2**5 / (3 * 3**8)
close(f2p, 0.4162, rtol=1e-4, name="f_1s->2p")
for n, v in [(3, 0.0791), (4, 0.0290), (5, 0.01394)]:
    close(f_np(n), v, rtol=2e-3, name=f"f_1s->{n}p")
ns = np.arange(2, 200001)
fd = f_np(ns).sum() + (2**8 / 3) * np.exp(-4) / (2 * 200001**2)   # tail ~ (256/3) e^-4 / n^3
close(fd, 0.5650, rtol=2e-4, name="discrete sum")
close(f_np(np.arange(2, 5)).sum(), 0.5243, rtol=2e-4, name="2p + 3p + 4p")


def dfdw(w):
    """oscillator-strength density per unit energy (1/eV) for w > I."""
    eta = np.sqrt(IH / (w - IH))
    return (2**7 / (3 * IH)) * (IH / w)**4 * np.exp(-4 * eta * np.arctan(1 / eta)) / (-np.expm1(-2 * np.pi * eta))


def fc_between(a, b):
    """continuum strength between photon energies a*I and b*I (b may be np.inf)."""
    return integrate.quad(lambda x: IH * dfdw(IH * x), a, b, limit=400)[0]


fc = fc_between(1.0 + 1e-12, 50) + fc_between(50, np.inf)
close(fc, 0.4350, rtol=2e-4, name="continuum")
close(fd + fc, 1.0, rtol=2e-4, name="TRK total")
close(IH * dfdw(IH * (1 + 1e-9)), 128 / 3 * np.exp(-4), rtol=1e-4, name="df/d(w/I) at threshold")
close(128 / 3 * np.exp(-4), 0.7815, rtol=1e-4, name="(128/3) e^-4")
sig_th = 2 * np.pi**2 * alpha / me * dfdw(IH * (1 + 1e-9)) * hbarc_cm**2
close(sig_th, 6.30e-18, rtol=2e-3, name="threshold photoionization cross-section (cm^2)")
for b, v in [(2, 0.316), (5, 0.416)]:
    close(fc_between(1 + 1e-12, b), v, rtol=3e-3, name=f"continuum strength below {b} I")
close(fc_between(10, np.inf), 0.0042, rtol=1e-2, name="continuum strength above 10 I")
# finite q: share of the first moment carried by 2p at q0 = alpha m_e (q0 a0 = 1)
f2p_q0 = 72 * 1.0 / (9 / 4 + 1.0)**6
close(f2p_q0, 0.0611, rtol=2e-3, name="|f_2p(q0)|^2")
close(f2p_q0 * 0.75 * IH / IH, 0.0458, rtol=2e-3, name="2p share of q0^2/2m at q0 (omega_2p = 3/4 I)")
close(alpha**2 * me / 2, 13.6057, rtol=1e-5, name="q0^2/2m_e = I (eV)")

print("== Worked example 4.6: free electron gas, direct integration")
kF = 1.0; m = 1.0
nF = kF**3 / (3 * np.pi**2)
def S0(q, w):
    a = abs(m * w / q - q / 2); b = np.sqrt(max(kF**2 - 2 * m * w, 0.0))
    kmin = max(a, b)
    return (m / (2 * np.pi * q)) * (kF**2 - kmin**2) if (kmin < kF and w > 0) else 0.0
for q in [0.1, 0.5, 1.0, 1.9, 2.5, 4.0]:
    wp_ = q * kF / m + q**2 / (2 * m)
    w1 = q * kF / m - q**2 / (2 * m)
    pts = [w1] if q < 2 * kF else None
    I1 = integrate.quad(lambda w: w * S0(q, w), 0, wp_, points=pts, limit=400)[0]
    close(I1, np.pi * nF * q**2 / m, rtol=1e-6, name=f"int w S0 / (pi n q^2/m) at q/kF = {q}")
q = 0.5
w1 = q * kF / m - q**2 / (2 * m)
lin = integrate.quad(lambda w: w * S0(q, w), 0, w1)[0]
close(lin / (np.pi * nF * q**2 / m), (1 - q / (2 * kF))**3, rtol=1e-6, name="share of first moment in the linear region = (1 - q/2kF)^3")
close((1 - 0.25)**3, 0.42, rtol=1e-2, name="(3/4)^3 at q = kF/2")
# mean energy (q^2/2m) / S_st with S_st -> 3q/4kF: (2/3) q v_F
qs = 1e-3
Sst = 3 * qs / (4 * kF) - qs**3 / (16 * kF**3)
close((qs**2 / (2 * m)) / Sst, (2 / 3) * qs * kF / m, rtol=1e-5, name="mean energy at small q / (q v_F)")
# gap bound S_st <= q^2 / (2 m E_g) against the free-gas 3q/4kF at the Si valence density
kF_si = (3 * np.pi**2 * n_val)**(1 / 3)
close(kF_si, 3.57e3, rtol=2e-3, name="k_F of the Si valence density (eV)")
qx = 3 * me * 1.17 / (2 * kF_si)
close(qx, 251, rtol=1e-2, name="q where 3q/4kF = q^2/(2 m E_g) (eV)")
close((100.0**2 / (2 * me * 1.17)) / (3 * 100.0 / (4 * kF_si)), 0.40, rtol=2e-2, name="gap bound / free gas at q = 100 eV")

print("== Worked example 4.7: silicon from the Henke tables")
d = np.loadtxt(os.path.join(BOOK, "figscripts", "data", "4.3", "si_henke.nff"), skiprows=1)
E, f2 = d[:, 0], d[:, 2]
sel = E >= 30.0
E, f2 = E[sel], f2[sel]
g = 2 / np.pi * f2 / E
cum = np.concatenate([[0.0], np.cumsum(0.5 * (g[1:] + g[:-1]) * np.diff(E))])
def upto(x):
    return np.interp(x, E, cum)
# power-law tail beyond 30 keV, fitted to the last decade of g
hi = E >= 3e3
slope = np.polyfit(np.log(E[hi]), np.log(g[hi]), 1)[0]
tail = g[-1] * E[-1] / (-slope - 1)
close(tail, 0.007, rtol=0.15, name="extrapolated strength above 30 keV")
above30 = cum[-1] + tail
close(above30, 10.42, rtol=2e-3, name="strength above 30 eV")
close(14 - above30, 3.58, rtol=3e-3, name="TRK 14 minus strength above 30 eV")
close(14 - 14 * 5 / 3 * Kbar / me - above30, 3.55, rtol=3e-3, name="same with the mass-velocity reduction")
Lb, Kb = 99.8, 1839.0
r_low = upto(Lb - 0.05)
close(r_low, 0.35, rtol=2e-2, name="strength 30 eV - L edge")
close(14 - above30 + r_low, 3.93, rtol=3e-3, name="strength below the L edge (inferred)")
r_L = upto(Kb - 0.5) - upto(Lb - 0.05)
close(r_L, 8.46, rtol=2e-3, name="strength between L and K edges")
r_K = cum[-1] - upto(Kb - 0.5) + tail
close(r_K, 1.61, rtol=3e-3, name="strength above the K edge")
close((upto(1000) - upto(Lb - 0.05)) / r_L, 0.97, rtol=5e-3, name="share of the L region collected by 1 keV")
close((upto(5000) - upto(Kb - 0.5)) / r_K, 0.84, rtol=1e-2, name="share of the K region collected by 5 keV")
close((upto(10000) - upto(Kb - 0.5)) / r_K, 0.96, rtol=5e-3, name="share of the K region collected by 10 keV")
close(10e3**2 / (2 * me), 97.8, rtol=2e-3, name="free recoil at q = 10 keV (eV)")

print("== Kramers-Kronig reconstruction of the damped oscillator (Fig. 4.3b)")
lam2, w0, G = 1.0, 1.0, 0.2
R = lambda w: 2 * lam2 * w0 / (w**2 + 1j * G * w - w0**2)
def ReR_KK(w):
    # (2/pi) PV int_0^inf w' Im R(w') / (w'^2 - w^2)  =  (2/pi) PV int [w' Im R / (w' + w)] / (w' - w)
    f = lambda x: x * R(x).imag / (x + w)
    if w > 0:
        a = integrate.quad(f, 0, 50, weight="cauchy", wvar=w, limit=400)[0]
    else:
        a = integrate.quad(lambda x: f(x) / (x - w), 0, 50, limit=400)[0]
    b = integrate.quad(lambda x: f(x) / (x - w), 50, 4000, limit=400)[0]
    return 2 / np.pi * (a + b)
wk = np.linspace(0.0, 3.0, 61)
kk = np.array([ReR_KK(w) for w in wk])
err = np.max(np.abs(kk - R(wk).real))
assert err < 2e-4, err
print(f"  max |Re R_KK - Re R| on [0, 3] w0: {err:.1e}")
close(ReR_KK(0.0), -2.0, rtol=1e-4, name="static value from KK (units lam^2/w0)")
mom = integrate.quad(lambda x: x * (-R(x).imag), 0, 50, limit=400)[0] + integrate.quad(lambda x: x * (-R(x).imag), 50, np.inf, limit=400)[0]
close(mom, np.pi * lam2 * w0, rtol=1e-4, name="int_0^inf w (-Im VR) = pi lam^2 w0")

# ---------------------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.7), gridspec_kw={"width_ratios": [1.1, 1]})
# (a) contour
Rb, z0, r_ind = 2.0, 0.6 + 0.35j, 0.12
ax1.axhline(0, color="0.6", lw=0.6); ax1.axvline(0, color="0.6", lw=0.6)
ax1.fill_between([-2.3, 2.3], 0, 2.3, color="C0", alpha=0.08, lw=0)
th = np.linspace(0, np.pi, 200)
ax1.plot(Rb * np.cos(th), Rb * np.sin(th), color="C0", lw=1.2)
ax1.plot([-Rb, Rb], [0.0, 0.0], color="C0", lw=1.6)
for x0, x1 in [(-0.9, -0.7), (0.9, 1.1)]:
    ax1.annotate("", (x1, 0), (x0, 0), arrowprops=dict(arrowstyle="-|>", color="C0", lw=1.0))
ax1.annotate("", (-1.42, 1.42), (-1.30, 1.53), arrowprops=dict(arrowstyle="-|>", color="C0", lw=1.0))
ax1.plot(z0.real, z0.imag, "x", color="C3", ms=6, mew=1.4)
ax1.text(z0.real + 0.1, z0.imag + 0.08, r"$z$", color="C3")
# singularities of R below the axis: a cut (crosses) and a resonance pole
xs = np.linspace(-1.7, 1.7, 15)
ax1.plot(xs, -0.06 + 0 * xs, "+", color="C1", ms=4, mew=0.9)
ax1.plot([1.2, -1.2], [-0.55, -0.55], "o", mfc="none", color="C1", ms=5)
ax1.text(-1.95, -0.95, r"singularities of $R$: $\mathrm{Im}\,\omega' < 0$", fontsize=7.5, color="C1")
ax1.text(-1.95, 1.95, r"$|\omega'| = \Omega_{\mathrm{arc}}$", fontsize=8, color="C0")
ax1.text(1.25, 0.12, r"real $\omega'$", fontsize=8)
ax1.set_xlim(-2.3, 2.3); ax1.set_ylim(-1.15, 2.3); ax1.set_aspect("equal")
ax1.set_xticks([]); ax1.set_yticks([])
ax1.set_title("(a) Kramers--Kronig contour".replace("--", "\u2013"), fontsize=9)
# (b) KK reconstruction
wf = np.linspace(0, 3, 601)
ax2.plot(wf, -R(wf).imag, color="C1", lw=1.2, label=r"$-\mathrm{Im}\,VR$ (input)")
ax2.plot(wf, R(wf).real, color="C0", lw=1.2, label=r"$\mathrm{Re}\,VR$ (exact)")
ax2.plot(wk[::3], kk[::3], "o", color="C0", ms=3, mfc="none", label="Kramers\u2013Kronig from " + r"$\mathrm{Im}$")
ax2.axhline(0, color="0.6", lw=0.6)
ax2.set_xlabel(r"$\omega/\omega_0$"); ax2.set_ylabel(r"units of $\lambda_{\mathrm{osc}}^2/\omega_0$")
ax2.set_xlim(0, 3); ax2.set_ylim(-6, 10.5)
ax2.legend(fontsize=7, frameon=False, loc="upper right")
ax2.set_title(r"(b) damped oscillator, $\varGamma_{\mathrm{w}} = 0.2\,\omega_0$".replace(r"\varGamma", r"\mathit{\Gamma}"), fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_3.pdf"))
plt.close(fig)

# ---------------------------------------------------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.7))
# (a) hydrogen: cumulative TRK sum against photon energy in units of I
xd = 1 - 1 / np.arange(2, 400)**2
cd = np.cumsum(f_np(np.arange(2, 400)))
xc = np.logspace(np.log10(1 + 1e-6), np.log10(1e3), 400)
cc = fd + np.array([fc_between(1 + 1e-12, x) for x in xc])
ax1.step(np.concatenate([[0.7], xd]), np.concatenate([[0], cd]), where="post", color="C0", lw=1.1, label="discrete $np$")
ax1.plot(xc, cc, color="C1", lw=1.4, label="with continuum")
ax1.axhline(1, color="0.5", lw=0.7, ls="--")
ax1.axvline(1, color="0.6", lw=0.6, ls=":")
ax1.set_xscale("log"); ax1.set_xlim(0.7, 1e3); ax1.set_ylim(0, 1.05)
ax1.set_xlabel(r"$\omega / E_B$"); ax1.set_ylabel(r"$\sum f^{\mathrm{osc}}$ below $\omega$")
ax1.text(1.3, 0.47, "0.565", fontsize=7.5, color="C0")
ax1.legend(fontsize=7, frameon=False, loc="lower right")
ax1.set_title("(a) hydrogen 1s", fontsize=9)
# (b) silicon: cumulative oscillator strength per atom from 30 eV, offset by the inferred strength below 30 eV
off = 14 - above30
ax2.plot(E, off + cum, color="C0", lw=1.2)
ax2.plot([10, 30], [off, off], color="C0", lw=1.2, ls=":")
for x, lab, yl in [(Lb, "L", 0.6), (Kb, "K", 0.6)]:
    ax2.axvline(x, color="0.6", lw=0.6, ls=":")
    ax2.text(x * 1.06, yl, lab, fontsize=7.5)
for y in [4, 12, 14]:
    ax2.axhline(y, color="0.5", lw=0.6, ls="--")
ax2.set_xscale("log"); ax2.set_xlim(10, 3e4); ax2.set_ylim(0, 14.8)
ax2.set_xlabel(r"$\omega$ (eV)"); ax2.set_ylabel(r"$\sum f^{\mathrm{osc}}$ per atom below $\omega$")
ax2.set_title("(b) silicon", fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_3b.pdf"))
plt.close(fig)
print("wrote fig4_3.pdf, fig4_3b.pdf")
