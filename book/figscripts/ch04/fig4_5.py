"""Fig. 4.5 of Sect. 4.4 (screening and the dielectric function), and every number quoted in Sect. 4.4, its Worked
examples 4.8 and 4.9 and Appendix D.7.  Natural units hbar = c = k_B = 1, Heaviside-Lorentz charge e^2 = 4 pi alpha.

Output: tex/figures/ch04/fig4_5.pdf  (a) eps_1 and eps_2 of silicon at q -> 0, 300 K; (b) loss function L of silicon
        at q -> 0 (log scale) with the single damped oscillator of Worked example 4.9.

Inputs and their sources
  Constants (CODATA 2018): m_e = 510998.95 eV, alpha = 1/137.035999, hbar c = 1973.269804 eV A.
  Silicon valence density n_e = 2.00e23 cm^-3 (App. A.2 of the book); omega_p = 16.6 eV (Sect. 4.3);
     k_F = 3.57 keV, N_F = 9.2e7 eV^2 per spin (Sect. 2.5, recomputed here from n_e).
  Measured electronic dielectric constant eps_inf = 11.7 (book value).  Gap marker 1.12 eV, the room-temperature value, to match the 300 K data (the low-temperature gap is 1.17 eV).
  Optical constants n, k of float-zone crystalline silicon at 300 K from 4 meV to 40 eV: D. Franta, A. Dubroka, C. Wang,
     A. Giglia, J. Vohanka, P. Franta and I. Ohlidal, Appl. Surf. Sci. 421, 405 (2017), doi:10.1016/j.apsusc.2017.02.021.
     This is a Kramers-Kronig-consistent dispersion model fitted to ellipsometric and spectrophotometric measurements,
     tabulated by the authors; file Franta-300K.yml of the refractiveindex.info database (CC0), downloaded 2026-11-02,
     copy in book/sources/4.4/si_franta_300K.yml.  Columns: wavelength (um), n, k.  eps = (n + i k)^2.
     The data are optical (transverse) at q -> 0; L = eps_2/|eps|^2 uses eps^T = eps at q -> 0 (Sect. 4.4).
Modelling choices
  Worked example 4.9: eps^{-1}(q, w) = 1 + w_p^2/(w^2 - w_q^2 + i g w), w_q^2 = w_L^2 + (q^2/2m_e)^2,
     w_L^2 = w_p^2 eps_inf/(eps_inf - 1) (so that eps(q -> 0, 0) = eps_inf), damping g = 3.66 eV = full width at half
     maximum of the tabulated L (computed below).  The free-recoil term (q^2/2m_e)^2 is the modelling choice that makes
     the oscillator move to the free recoil at large q; it closes the q integral of the stopping power.
  Appendix D.7 checks: random complex 7x7 proper response with the q -> 0 structure of an insulator (head ~ q^2,
     wings ~ q), q = 1e-3 in units of the shortest G; v_C(|q+G|) on a cubic-like set of G.
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

me = 510998.95
alpha = 1 / 137.035999
e2 = 4 * np.pi * alpha
hbarc_A = 1973.269804       # eV A
hbarc_cm = 197.3269804e-7   # eV cm


def close(a, b, rtol=5e-3, name=""):
    assert abs(a - b) <= rtol * abs(b), f"{name}: {a} vs {b}"
    print(f"  {name:58s} {a:.6g}   (quoted {b})")


print("Silicon valence electron gas")
ne = 2.00e23 * hbarc_cm**3          # eV^3
kF = (3 * np.pi**2 * ne) ** (1 / 3)
NF = me * kF / (2 * np.pi**2)
vF = kF / me
wp = np.sqrt(e2 * ne / me)
close(kF / 1e3, 3.57, 2e-3, "k_F [keV]")
close(NF, 9.2e7, 1e-2, "N_F [eV^2]")
close(wp, 16.6, 3e-3, "omega_p [eV]")
close(np.pi / 2 * wp**2, 433, 3e-3, "(pi/2) omega_p^2 [eV^2]")

print("Thomas-Fermi (Worked example 4.8)")
kTF2 = 2 * e2 * NF
close(kTF2, 4 * alpha * me * kF / np.pi, 1e-9, "k_TF^2 = 4 alpha m_e k_F/pi")
close(kTF2, 3 * wp**2 / vF**2, 1e-9, "k_TF^2 = 3 omega_p^2/v_F^2")
kTF = np.sqrt(kTF2)
close(kTF / 1e3, 4.12, 3e-3, "k_TF [keV]")
close(hbarc_A / kTF, 0.48, 5e-3, "1/k_TF [A]")
close(kTF / kF, 1.15, 5e-3, "k_TF/k_F")
q0 = alpha * me
close(1 + kTF2 / q0**2, 2.22, 5e-3, "eps_TF(q0 = alpha m_e)")
close((1 + kTF2 / q0**2) ** 2, 4.9, 1e-2, "|eps_TF(q0)|^2")
eps_inf = 11.7
qx = kTF / np.sqrt(eps_inf - 1)
close(qx / 1e3, 1.26, 5e-3, "q where 1 + k_TF^2/q^2 = eps_inf [keV]")
close(hbarc_A / qx, 1.57, 5e-3, "1/q there [A]")

print("Mean excitation energy from the two moments (moved from Sect. 4.3)")
Ebar = wp / np.sqrt(1 - 1 / eps_inf)
close(np.sqrt(1 - 1 / eps_inf), 0.956, 1e-3, "(1 - 1/eps_inf)^(1/2)")
close(Ebar, 17.4, 3e-3, "E_bar [eV]")

print("Tabulated optical constants of Si at 300 K")
rows = []
for line in open(os.path.join(BOOK, "sources", "4.4", "si_franta_300K.yml")):
    p = line.split()
    if len(p) == 3:
        try:
            rows.append([float(x) for x in p])
        except ValueError:
            pass
lam, n, k = np.array(rows).T
w = 1.239841984 / lam
o = np.argsort(w)
w, n, k = w[o], n[o], k[o]
eps = (n + 1j * k) ** 2
e1, e2d = eps.real, eps.imag
L = e2d / np.abs(eps) ** 2
close(w.max(), 40.0, 1e-3, "upper end of table [eV]")
close(e1[0], 11.7, 2e-3, "eps_1 at 4 meV")
jm = np.argmax(e2d)
close(w[jm], 4.24, 3e-3, "main eps_2 peak [eV]")
m = (w > 2.5) & (w < 3.8)
close(w[m][np.argmax(e2d[m])], 3.42, 3e-3, "lower eps_2 peak [eV]")
iz = np.where((e1[:-1] < 0) & (e1[1:] > 0))[0][0]
close(w[iz], 16.3, 3e-3, "eps_1 crosses zero upward [eV]")
il = np.argmax(L)
close(w[il], 16.4, 3e-3, "loss peak [eV]")
close(L[il], 4.5, 1e-2, "loss peak height")
half = w[L > L[il] / 2]
fwhm = half.max() - half.min()
close(fwhm, 3.66, 3e-3, "loss FWHM [eV]")
close(np.trapezoid(w * e2d, w) / (np.pi / 2 * wp**2), 0.96, 5e-3, "int_0^40 w eps_2 / (pi/2)w_p^2")
close(np.trapezoid(w * L, w) / (np.pi / 2 * wp**2), 0.925, 5e-3, "int_0^40 w L / (pi/2)w_p^2")
kk = 2 / np.pi * np.trapezoid(e2d / w, w)
close(kk / (e1[0] - 1), 0.998, 1e-3, "(2/pi) int eps_2/w / (eps_1(0) - 1)")
inv = 2 / np.pi * np.trapezoid(L / w, w)
close(inv / (1 - 1 / e1[0]), 0.978, 1e-3, "(2/pi) int L/w / (1 - 1/eps_1(0))")
close(np.interp(3.0, w, L), 3.1e-3, 1e-2, "L(3 eV)")

print("Worked example 4.9: single damped oscillator")
g = 3.66
wL = wp * np.sqrt(eps_inf / (eps_inf - 1))
wg = wp / np.sqrt(eps_inf - 1)
close(wL, Ebar, 1e-12, "omega_L = E_bar")
close(wg, 5.08, 3e-3, "omega_g [eV]")


def Lmod(q, x):
    wq2 = wL**2 + (q * q / 2 / me) ** 2
    return wp**2 * g * x / ((x * x - wq2) ** 2 + g * g * x * x)


for qq in [0.0, 3.0e3, 2.0e4]:
    fs = integrate.quad(lambda x: x * Lmod(qq, x), 0, np.inf, limit=500)[0]
    close(fs, np.pi / 2 * wp**2, 1e-6, f"f-sum of model L at q = {qq:g} eV")
    wq2 = wL**2 + (qq * qq / 2 / me) ** 2
    iv = integrate.quad(lambda x: Lmod(qq, x) / x, 0, np.inf, limit=500)[0]
    close(iv, np.pi / 2 * wp**2 / wq2, 1e-6, f"inverse moment of model L at q = {qq:g} eV")
close(1 + wp**2 / wg**2, eps_inf, 1e-12, "eps(0) of the oscillator")
close(Lmod(0, wL), wp**2 / (g * wL), 1e-12, "model peak w_p^2/(g w_L)")
close(wp**2 / (g * wL), 4.34, 3e-3, "model peak height")
close(Lmod(0, 3.0), 0.035, 1e-2, "model L(3 eV)")
close(Lmod(0, 3.0) / np.interp(3.0, w, L), 11, 3e-2, "model/data at 3 eV")
close(np.sqrt(2 * me * wL) / 1e3, 4.2, 5e-3, "q where w_q/q is smallest [keV]")
close(np.sqrt(wL / me), 5.8e-3, 1e-2, "min of w_q/q (speed)")
xint = integrate.quad(lambda x: x * x / (1 + x**4) ** 2, 0, np.inf)[0]
close(xint, np.pi / (8 * np.sqrt(2)), 1e-9, "int x^2/(1+x^4)^2")


def stopping(v):
    f = lambda q: integrate.quad(lambda x: x * Lmod(q, x), 0, q * v, limit=200)[0] / q
    I = integrate.quad(f, 0, 2.0e5, limit=400, points=[1e3, 4e3, 1e4])[0]
    return 2 * alpha / (np.pi * v * v) * I / hbarc_A        # eV/A for Z_1 = 1


slow = lambda v: alpha * g * v * wp**2 * me**1.5 / (6 * wL**2.5) / hbarc_A
close(slow(1e-3), 0.181, 3e-3, "slow-particle formula, v = 1e-3 [eV/A]")
close(stopping(1e-3), 0.186, 3e-3, "full integral, v = 1e-3 [eV/A]")
close(stopping(1e-4) / slow(1e-4), 1.0003, 1e-3, "full/slow at v = 1e-4")
close(stopping(2.65e-3) / slow(2.65e-3), 1.22, 5e-3, "full/slow at v = v_max")

print("Appendix D.7: matrix identities")
rng = np.random.default_rng(7)
Gs = np.array([[0, 0, 0], [1, 1, 1], [-1, -1, -1], [1, -1, 1], [-1, 1, -1], [2, 0, 0], [-2, 0, 0]], float)
qv = np.array([1e-3, 0.4e-3, 0.2e-3])
kv = Gs + qv
vC = 1 / np.sum(kv**2, axis=1)              # e^2/|q+G|^2 with e^2 = 1
N = len(Gs)
A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
Rt = -(A @ A.conj().T) / N - 0.3j * np.eye(N)          # generic complex proper response
qq = np.sqrt(qv @ qv)
scale = np.ones(N); scale[0] = qq                        # head ~ q^2, wings ~ q
Rt = scale[:, None] * Rt * scale[None, :]
V = np.diag(vC)
I = np.eye(N)
eps_m = I - V @ Rt
R = np.linalg.solve(I - Rt @ V, Rt)                      # R = Rt + Rt v R
close(np.abs(R - (Rt + Rt @ V @ R)).max() + 1, 1, 1e-10, "Dyson residual (+1)")
einv = np.linalg.inv(eps_m)
close(np.abs(einv - (I + V @ R)).max() + 1, 1, 1e-10, "eps^-1 = 1 + v R (+1)")
head = 1 / einv[0, 0]
schur = eps_m[0, 0] - eps_m[0, 1:] @ np.linalg.solve(eps_m[1:, 1:], eps_m[1:, 0])
close(abs(head - schur) + 1, 1, 1e-10, "1/(eps^-1)_00 = Schur complement (+1)")
Vbar = V.copy(); Vbar[0, 0] = 0
Rbar = np.linalg.solve(I - Rt @ Vbar, Rt)
close(abs(head - (1 - vC[0] * Rbar[0, 0])) + 1, 1, 1e-10, "eps_mac = 1 - v_0 Rbar_00 (+1)")
Vh = np.diag(np.sqrt(vC))
eps_s = I - Vh @ Rt @ Vh
close(np.abs(np.diag(np.linalg.inv(eps_s)) - np.diag(einv)).max() + 1, 1, 1e-10, "same diagonal of inverse (+1)")
print(f"  |eps_0G| ~ {np.abs(eps_m[0,1]):.3g} (grows as 1/q), |eps_G0| ~ {np.abs(eps_m[1,0]):.3g} (falls as q), "
      f"head eps_00 = {eps_m[0,0]:.4g}, eps_mac = {head:.4g}")

# ---------------------------------------------------------------- figure
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.7))
ax1.plot(w, e1, color="C0", lw=1.2, label=r"$\varepsilon_1$")
ax1.plot(w, e2d, color="C1", lw=1.2, label=r"$\varepsilon_2$")
ax1.axhline(0, color="0.6", lw=0.6)
ax1.axhline(eps_inf, color="0.5", lw=0.7, ls=":")
ax1.text(17, eps_inf + 2, r"$\varepsilon_\infty = 11.7$", fontsize=7.5, color="0.35")
ax1.set_xlim(0, 25); ax1.set_ylim(-25, 50)
ax1.set_xlabel(r"$\omega$ [eV]"); ax1.legend(fontsize=7.5, frameon=False, loc="upper right")
ax1.set_title(r"(a) dielectric function, $q \to 0$", fontsize=9)

ws = np.linspace(0.05, 40, 2000)
ax2.semilogy(w, L, color="C2", lw=1.3, label="silicon, 300 K")
ax2.semilogy(ws, Lmod(0, ws), color="0.3", lw=1.0, ls="--", label="single oscillator")
ax2.axvline(1.12, color="0.6", lw=0.6, ls=":")
ax2.text(1.5, 2.0, r"$E_{\mathrm{g}}$", fontsize=7.5, color="0.35")
ax2.set_xlim(0, 40); ax2.set_ylim(1e-4, 10)
ax2.set_xlabel(r"$\omega$ [eV]")
ax2.legend(fontsize=7.5, frameon=False, loc="lower right")
ax2.set_title(r"(b) loss function $L$, $q \to 0$", fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_5.pdf"))
print("wrote fig4_5.pdf")
