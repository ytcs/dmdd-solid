"""Fig. 4.6 of Sect. 4.5 (the homogeneous electron gas), the two limit-box plots of Sect. 4.5, and every number quoted
in Sect. 4.5 and its Worked example 4.10.  Natural units hbar = c = k_B = 1, Heaviside-Lorentz charge e^2 = 4 pi alpha.

Outputs (tex/figures/ch04/):
  fig4_6.pdf         (a) loss function L(q, w) of the electron gas at the silicon valence density (r_s = 2.0) in the
                     random-phase approximation, with the particle-hole continuum, the plasmon line and the line
                     w = q v_max; (b) L(q, w) at q = 0.3 k_F: Lindhard, Mermin and the naive substitution.
  limit4_tf.pdf      static Lindhard screening against Thomas-Fermi.
  limit4_plasmon.pdf RPA plasmon dispersion against the quadratic formula and its q^4 correction.

Inputs and their sources
  Constants (CODATA 2018): m_e = 510998.95 eV, alpha = 1/137.035999, hbar c = 1973.269804 eV A.
  Silicon valence density n_e = 2.00e23 cm^-3 (App. A.2 of the book); k_F, E_F, v_F, N_F recomputed from it
     (eq:2.5-fermi; book values 3.57 keV, 12.5 eV, 7.0e-3, 9.2e7 eV^2); omega_p = 16.6 eV (Sect. 4.3);
     k_TF = 4.12 keV (Sect. 4.4); r_s = 2.0 (Sect. 2.3).  v_max = 2.65e-3 (Chap. 1).
  Lindhard function: eq:D.8-Rz (complex z), eq:D.8-Re and eq:D.8-Im (real omega) of App. D.8.
  Mermin function: eq:D.9-R of App. D.9.
  Silicon optical data (Worked example 4.10): Franta et al., Appl. Surf. Sci. 421, 405 (2017), file Franta-300K.yml of
     the refractiveindex.info database (CC0), as in fig4_5.py.
Modelling choices
  The undamped RPA plasmon below q_c is a delta function; panel (a) draws it as a line, not as a colour.
  Panel (b) uses gamma_rel = 1.0 eV = 0.06 omega_p for the Mermin function and the naive substitution (an illustrative
     value, of the size fitted to the plasmon of a simple metal); it is named in the caption.
  Worked example 4.10: the Drude (Mermin at q -> 0) loss function with gamma_rel = 3.66 eV, the full width at half
     maximum of the tabulated silicon loss peak (computed in fig4_5.py and again here).
"""
import os
import numpy as np
from scipy import integrate, optimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

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
    print(f"  {name:62s} {a:.6g}   (quoted {b})")


print("Silicon valence electron gas")
ne = 2.00e23 * hbarc_cm**3
kF = (3 * np.pi**2 * ne) ** (1 / 3)
EF = kF**2 / (2 * me)
vF = kF / me
NF = me * kF / (2 * np.pi**2)
wp = np.sqrt(e2 * ne / me)
kTF = np.sqrt(2 * e2 * NF)
a0 = 1 / (alpha * me)
rs = (3 / (4 * np.pi * ne)) ** (1 / 3) / a0
vmax = 2.65e-3
q0 = alpha * me
close(kF / 1e3, 3.57, 2e-3, "k_F [keV]")
close(EF, 12.5, 3e-3, "E_F [eV]")
close(vF, 7.0e-3, 3e-3, "v_F")
close(wp, 16.6, 3e-3, "omega_p [eV]")
close(rs, 2.0, 3e-3, "r_s")
close(kTF / 1e3, 4.12, 3e-3, "k_TF [keV]")
close(wp / EF, 1.33, 3e-3, "omega_p / E_F")
close(kTF**2 / kF**2, 0.663 * rs, 2e-3, "k_TF^2/k_F^2 = 0.663 r_s")
close((4 / np.pi) * (4 / (9 * np.pi)) ** (1 / 3), 0.663, 1e-3, "(4/pi)(4/9pi)^(1/3)")
close(vmax / vF, 0.379, 3e-3, "v_max / v_F")


def lg(w):
    return np.log((w + 1) / (w - 1))


def R0z(q, z):
    """eq:D.8-Rz, any z with Im z > 0 (principal branch of the logarithm)."""
    nup = z / (q * vF) + q / (2 * kF)
    num = z / (q * vF) - q / (2 * kF)
    return -2 * NF * (0.5 + kF / (4 * q) * ((1 - nup**2) * lg(nup) - (1 - num**2) * lg(num)))


def R0(q, w):
    """eq:D.8-Re and eq:D.8-Im, real w > 0."""
    nup = w / (q * vF) + q / (2 * kF)
    num = w / (q * vF) - q / (2 * kF)
    lr = lambda x: np.log(np.abs((x + 1) / (x - 1)))
    re = -2 * NF * (0.5 + kF / (4 * q) * ((1 - nup**2) * lr(nup) - (1 - num**2) * lr(num)))
    im = -np.pi * kF * NF / (2 * q) * ((1 - num**2) * (np.abs(num) < 1) - (1 - nup**2) * (np.abs(nup) < 1))
    return re + 1j * im


def epsL(q, w):
    return 1 - e2 / q**2 * R0(q, w)


def Lloss(eps):
    return np.imag(-1 / eps)


wplus = lambda q: q * vF + q * q / (2 * me)

# consistency of the real-axis form with the complex form just above the axis
for qq, ww in [(0.5 * kF, 5.0), (1.5 * kF, 30.0), (0.3 * kF, 20.0)]:
    a, b = R0(qq, ww), R0z(qq, ww + 1e-7j)
    assert abs(a - b) < 1e-6 * abs(a), (a, b)
# Im R0 = -S0/2 (eq:4.2-gas) at two points
for qq, ww in [(0.5 * kF, 2.0), (1.5 * kF, 40.0)]:
    nu = abs(me * ww / qq - qq / 2)
    kmin = max(nu, np.sqrt(max(kF**2 - 2 * me * ww, 0)))
    S0 = me / (2 * np.pi * qq) * (kF**2 - kmin**2) if kmin < kF else 0
    close(-2 * R0(qq, ww).imag, S0, 1e-9, f"S0 = -2 Im R0 at q/kF = {qq/kF:.1f}")

print("Static screening (Limit: Thomas-Fermi)")
FL = lambda y: 0.5 + (1 - y * y) / (4 * y) * np.log(np.abs((1 + y) / (1 - y)))
for x in [0.1, 0.7, 1.9]:
    q = x * kF
    close(epsL(q, 1e-9).real, 1 + kTF**2 / q**2 * FL(q / (2 * kF)), 1e-7, f"eps_Lin(q,0) = 1 + kTF^2 F_L/q^2, q/kF={x}")
close(epsL(q0, 1e-9).real, 2.10, 3e-3, "eps_Lin(q0, 0)")
close(1 + kTF**2 / q0**2, 2.22, 3e-3, "eps_TF(q0)")
close(epsL(q0, 1e-9).real ** 2, 4.41, 3e-3, "eps_Lin(q0,0)^2")
close(epsL(kF, 1e-9).real, 2.21, 3e-3, "eps_Lin(k_F, 0)")
close(1 + kTF**2 / kF**2, 2.33, 3e-3, "eps_TF(k_F)")
# where F_L is within 2 and 10 percent of one
y2 = optimize.brentq(lambda y: FL(y) - 0.98, 1e-3, 0.99)
y10 = optimize.brentq(lambda y: FL(y) - 0.90, 1e-3, 0.99)
close(2 * y2, 0.49, 1e-2, "q/k_F where F_L = 0.98")
close(2 * y10, 1.06, 1e-2, "q/k_F where F_L = 0.90")
close(FL(1 - 1e-12), 0.5, 1e-6, "F_L(1)")

print("Plasmon")


def wpl(q):
    return optimize.brentq(lambda w: epsL(q, w).real, wplus(q) * (1 + 1e-10), 10 * wp, xtol=1e-12)


qc = optimize.brentq(lambda q: epsL(q, wplus(q) * (1 + 1e-12)).real, 0.1 * kF, 1.5 * kF, xtol=1e-9)
close(qc / kF, 0.730, 2e-3, "q_c / k_F")
close(qc / 1e3, 2.60, 3e-3, "q_c [keV]")
close(wplus(qc), 24.8, 3e-3, "omega_pl(q_c) = omega_+(q_c) [eV]")
close(wplus(qc) / EF, 1.99, 3e-3, "omega_pl(q_c) / E_F")
close(wp / vF / kF, 0.666, 2e-3, "estimate omega_p/v_F in k_F")
close(wp / vF / 1e3, 2.38, 3e-3, "estimate omega_p/v_F [keV]")
quad = lambda q: np.sqrt(wp**2 + 0.6 * vF**2 * q**2)
quart = lambda q: np.sqrt(wp**2 + 0.6 * vF**2 * q**2 + (1 / (4 * me**2) + 12 / 175 * vF**4 / wp**2) * q**4)
close(12 / 175, 3 / 7 - 9 / 25, 1e-12, "12/175 = 3/7 - 9/25")
for x in [0.1, 0.3]:
    q = x * kF
    print(f"    q/kF={x}: exact {wpl(q):.5f}, quadratic {quad(q):.5f}, with q^4 {quart(q):.5f}")
close(abs(quad(0.1 * kF) / wpl(0.1 * kF) - 1), 4.6e-5, 2e-2, "quadratic error at 0.1 k_F")
close(abs(quart(0.3 * kF) / wpl(0.3 * kF) - 1), 3.3e-4, 5e-2, "quartic error at 0.3 k_F")
# validity of the quadratic formula: 1 percent
x1 = optimize.brentq(lambda x: wpl(x * kF) / quad(x * kF) - 1.01, 0.1, 0.72)
close(x1, 0.39, 1e-2, "q/k_F where quadratic is 1 percent low")
alpha_pl = 0.3 * vF**2 * me / wp          # omega_pl = omega_p + alpha_pl q^2/m_e
close(alpha_pl, 0.6 * EF / wp, 1e-12, "alpha_pl = (3/5) E_F/omega_p")
close(alpha_pl, 0.45, 5e-3, "dispersion coefficient alpha_pl")


def dE1(q, w):
    h = 1e-6 * w
    return (epsL(q, w + h).real - epsL(q, w - h).real) / (2 * h)


close(dE1(0.02 * kF, wpl(0.02 * kF)), 2 / wp, 3e-3, "d eps_1/d omega at q -> 0 = 2/omega_p")
# f-sum: plasmon weight + continuum, and perfect-screening (inverse moment) at several q
fsums = {}
for x in [0.1, 0.5]:
    q = x * kF
    w0 = wpl(q)
    plas = np.pi * w0 / dE1(q, w0)
    cont = integrate.quad(lambda w: w * Lloss(epsL(q, w)), 1e-9, wplus(q), limit=400)[0]
    inv = integrate.quad(lambda w: Lloss(epsL(q, w)) / w, 1e-9, wplus(q), limit=400)[0] + np.pi / (w0 * dE1(q, w0))
    fsums[x] = plas / (np.pi / 2 * wp**2)
    close((plas + cont) / (np.pi / 2 * wp**2), 1.0, 1e-5, f"RPA f-sum at q/kF = {x}")
    close(2 / np.pi * inv, 1 - 1 / epsL(q, 1e-9).real, 1e-5, f"RPA inverse moment = 1 - 1/eps(q,0), q/kF = {x}")
    pinv = 2 / np.pi * np.pi / (w0 * dE1(q, w0))
    print(f"    q/kF={x}: plasmon share of f-sum {fsums[x]:.4f}, of inverse moment {pinv:.4f}")
close(fsums[0.5], 0.957, 1e-3, "plasmon share of f-sum at 0.5 k_F")
close(fsums[0.1], 1.000, 1e-4, "plasmon share of f-sum at 0.1 k_F")
for x in [1.0, 2.5]:
    q = x * kF
    tot = integrate.quad(lambda w: w * Lloss(epsL(q, w)), 1e-9, wplus(q), limit=800)[0]
    close(tot / (np.pi / 2 * wp**2), 1.0, 1e-5, f"RPA f-sum (continuum only) at q/kF = {x}")
close(1 - 1 / epsL(0.1 * kF, 1e-9).real, 0.9925, 2e-4, "1 - 1/eps(0.1 kF, 0)")
# static structure factor carried by the plasmon at small q
q = 0.1 * kF
close(q * q / (2 * me * wp), 7.5e-3, 1e-2, "S^st = q^2/(2 m omega_p) at 0.1 k_F")
close(3 * q / (4 * kF), 0.075, 1e-9, "free-gas S^st = 3q/4k_F at 0.1 k_F")

print("Dark-matter kinematics")
close(wp / vmax / 1e3, 6.27, 3e-3, "q at which q v_max = omega_p [keV]")
close(wp / vmax / kF, 1.76, 3e-3, "same in k_F")
wq0 = q0 * vmax
eq0 = epsL(q0, wq0)
close(wq0, 9.88, 3e-3, "q0 v_max [eV]")
close(abs(eq0) ** 2, 3.96, 3e-3, "|eps_Lin(q0, q0 v_max)|^2")
close(wplus(q0), 39.7, 3e-3, "omega_+(q0) [eV]")
close(Lloss(eq0), 0.183, 3e-3, "L_Lin(q0, q0 v_max)")
qa = 0.05 * kF
wa = 0.05 * qa * vF
close(Lloss(epsL(qa, wa)), e2 * me**2 * qa * wa / (2 * np.pi * kTF**4), 1e-2, "corner L = e^2 m^2 q w/(2 pi kTF^4), q=0.05kF")

print("Mermin function")


def RMer(q, w, g):
    Rg = R0z(q, w + 1j * g)
    Rs = R0(q, 1e-12 * EF).real
    return (1 + 1j * g / w) * Rg / (1 + (1j * g / w) * Rg / Rs)


epsM = lambda q, w, g: 1 - e2 / q**2 * RMer(q, w, g)
epsN = lambda q, w, g: 1 - e2 / q**2 * R0z(q, w + 1j * g)
g = 1.0
for x in [0.3, 1.2]:
    q = x * kF
    fM = integrate.quad(lambda w: w * Lloss(epsM(q, w, g)), 1e-6, 400, limit=2000, points=[wpl(q) if x < 0.73 else wplus(q)])[0]
    fN = integrate.quad(lambda w: w * Lloss(epsN(q, w, g)), 1e-6, 400, limit=2000, points=[wpl(q) if x < 0.73 else wplus(q)])[0]
    # analytic tail beyond 400 eV: L -> wp^2 g / w^3 (Mermin) and 2 wp^2 g / w^3 (naive) at large w
    fM += wp**2 * g / 400
    fN += 2 * wp**2 * g / 400
    close(fM / (np.pi / 2 * wp**2), 1.0, 2e-4, f"Mermin f-sum at q/kF = {x}")
    close(fN / (np.pi / 2 * wp**2), 1.0, 2e-4, f"naive-substitution f-sum at q/kF = {x}")
# static limits
q = 0.3 * kF
close(epsM(q, 1e-7, g).real, epsL(q, 1e-9).real, 1e-4, "eps_Mer(q, omega -> 0) = eps_Lin(q, 0)")
print(f"    naive substitution at omega -> 0, q = 0.3 k_F: {epsN(q, 1e-7, g).real:.3f} vs Lindhard {epsL(q, 1e-9).real:.3f}")
# q -> 0: Drude
qs = 0.01 * kF
for ww in [5.0, 10.0, 16.0]:
    d = 1 - wp**2 / (ww * (ww + 1j * g))
    assert abs(epsM(qs, ww, g) - d) < 2e-3 * abs(d), (ww, epsM(qs, ww, g), d)
print("  Mermin at q = 0.01 k_F equals Drude to 2e-3")
# low-frequency tails at q -> 0, omega << omega_p
ww = 1.0
LD = Lloss(1 - wp**2 / (ww * (ww + 1j * g)))
LN = Lloss(1 - wp**2 / (ww + 1j * g) ** 2)
close(LD, g * ww / wp**2, 2e-2, "Drude tail gamma omega/omega_p^2")
close(LN / LD, 2.0, 2e-2, "naive/Drude tail ratio at q -> 0")

print("Worked example 4.10: silicon data")
rows = []
for line in open(os.path.join(BOOK, "figscripts", "data", "4.4", "si_franta_300K.yml")):
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
Ld = e2d / np.abs(eps) ** 2
il = np.argmax(Ld)
close(w[il], 16.4, 3e-3, "loss peak [eV]")
close(Ld[il], 4.5, 1e-2, "loss peak height")
iz = np.where((e1[:-1] < 0) & (e1[1:] > 0))[0][0]
wz = w[iz] + (w[iz + 1] - w[iz]) * (-e1[iz]) / (e1[iz + 1] - e1[iz])
close(wz, 16.3, 3e-3, "eps_1 zero [eV]")
close(1 - wz / wp, 0.018, 3e-2, "omega_p above the eps_1 zero (fraction)")
slope = (np.interp(wz + 0.05, w, e1) - np.interp(wz - 0.05, w, e1)) / 0.1
close(slope, 0.128, 5e-3, "d eps_1/d omega of data at the zero [1/eV]")
close(2 * wp**2 / wz**3, 0.127, 5e-3, "free-gas slope 2 omega_p^2/omega^3 there [1/eV]")
e2z = np.interp(wz, w, e2d)
close(e2z, 0.22, 2e-2, "eps_2 at the zero")
close(2 * e2z / slope, 3.5, 1e-2, "Lorentzian FWHM 2 eps_2/slope [eV]")
half = w[Ld > Ld[il] / 2]
close(half.max() - half.min(), 3.66, 3e-3, "measured FWHM [eV]")
m = w <= wz
fs = lambda mm: np.trapezoid((w * e2d)[mm], w[mm]) / (np.pi / 2 * wp**2)
close(fs(m), 0.87, 1e-2, "valence f-sum fraction below the zero")
close(fs((w > wz)), 0.094, 2e-2, "fraction between the zero and 40 eV")
rms = np.sqrt(np.trapezoid((w**3 * e2d)[m], w[m]) / np.trapezoid((w * e2d)[m], w[m]))
close(rms, 6.5, 1e-2, "rms energy of the weight below the zero [eV]")
gS = 3.66
LDr = lambda x: wp**2 * gS * x / ((x * x - wp**2) ** 2 + gS**2 * x * x)
close(LDr(wp), wp / gS, 1e-12, "Drude peak omega_p/gamma")
close(wp / gS, 4.54, 3e-3, "Drude peak height")
close(LDr(3.0), 0.042, 2e-2, "Drude L(3 eV)")
close(LDr(3.0) / np.interp(3.0, w, Ld), 14, 3e-2, "Drude / data at 3 eV")
close(np.interp(3.0, w, Ld), 3.1e-3, 1e-2, "data L(3 eV)")

# ---------------------------------------------------------------- figure 4.6
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.85), gridspec_kw={"width_ratios": [1.15, 1]})
xq = np.linspace(0.01, 2.6, 520)
yw = np.linspace(0.005, 6.0, 600)
X, Y = np.meshgrid(xq, yw)
Lmap = Lloss(epsL(X * kF, Y * EF))
Lmap = np.where(Lmap > 1e-4, Lmap, np.nan)
pc = ax1.pcolormesh(X, Y, Lmap, norm=LogNorm(1e-3, 3), cmap="Blues", shading="auto", rasterized=True)
cb = fig.colorbar(pc, ax=ax1, pad=0.17, fraction=0.06)   # room for the eV axis on the right of panel (a)
cb.set_label(r"$L(q,\omega)$", fontsize=8)
cb.ax.tick_params(labelsize=7)
ax1.plot(xq, (xq * kF * vF + (xq * kF) ** 2 / (2 * me)) / EF, color="0.25", lw=0.7)
xm = xq[xq > 2]
ax1.plot(xm, ((xm * kF) ** 2 / (2 * me) - xm * kF * vF) / EF, color="0.25", lw=0.7)
xp = np.linspace(0.02, qc / kF * (1 - 1e-4), 120)
ax1.plot(xp, [wpl(x * kF) / EF for x in xp], color="C3", lw=1.6)
ax1.plot([qc / kF], [wplus(qc) / EF], "o", color="C3", ms=3.5)
ax1.text(qc / kF - 0.06, wplus(qc) / EF + 0.1, r"$q_{\mathrm{c}}$", color="C3", fontsize=8, ha="right")   # on white, outside the continuum
ax1.plot(xq, xq * kF * vmax / EF, color="C1", lw=1.0, ls="--")
ax1.text(1.1, 1.38, r"$\omega = qv_{\mathrm{max}}$", color="C1", fontsize=7.5, rotation=17)
ax1.text(0.03, 1.75, r"$\omega_{\mathrm{pl}}(q)$", color="C3", fontsize=8)
ax1.text(1.28, 4.6, r"$\omega_+$", color="0.2", fontsize=8, ha="right")   # outside the continuum, off the edge line
ax1.text(2.38, 0.12, r"$\omega_-$", color="0.2", fontsize=8)
ax1.set_xlim(0, 2.6)
ax1.set_ylim(0, 6)
ax1.set_xlabel(r"$q/k_{\mathrm{F}}$")
ax1.set_ylabel(r"$\omega/E_{\mathrm{F}}$")
ax1.text(0.03, 0.95, "(a)", transform=ax1.transAxes, va="top")
sec = ax1.secondary_yaxis("right", functions=(lambda y: y * EF, lambda y: y / EF))
sec.set_ticks([0, 20, 40, 60])
sec.tick_params(labelsize=7, pad=1)
sec.set_ylabel(r"$\omega$ (eV)", fontsize=7, labelpad=1)

qb = 0.3 * kF
ws = np.linspace(0.02, 30, 3000)
LL = Lloss(epsL(qb, ws))
LL[ws > wplus(qb)] = np.nan
ax2.semilogy(ws, LL, color="0.55", lw=2.4, label="Lindhard")
ax2.semilogy(ws, Lloss(epsM(qb, ws, g)), color="C0", lw=1.1, label="Mermin", zorder=3)   # gamma_rel = 1 eV is given in the caption
ax2.semilogy(ws, Lloss(epsN(qb, ws, g)), color="C1", lw=1.0, ls="--", label=r"$\omega \to \omega + \mathrm{i}\gamma_{\mathrm{rel}}$")
w0b = wpl(qb)
ax2.annotate("", xy=(w0b, 30), xytext=(w0b, 1e-4), arrowprops=dict(arrowstyle="->", color="0.2", lw=1.0))
ax2.text(w0b + 0.6, 6, r"$\omega_{\mathrm{pl}}$", fontsize=8)
ax2.axvline(wplus(qb), color="0.6", lw=0.6, ls=":")
ax2.text(wplus(qb) + 0.3, 2e-4, r"$\omega_+$", fontsize=8, color="0.35")
ax2.set_xlim(0, 30)
ax2.set_ylim(1e-4, 40)
ax2.set_xlabel(r"$\omega$ (eV)")
ax2.set_ylabel(r"$L(q,\omega)$ at $q = 0.3\,k_{\mathrm{F}}$")
ax2.legend(fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.93), handlelength=1.4,
           borderaxespad=0.3)   # short handles keep the legend left of the plasmon arrow
ax2.text(0.03, 0.97, "(b)", transform=ax2.transAxes, va="top")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_6.pdf"), dpi=300)
plt.close(fig)

# ---------------------------------------------------------------- limit: Thomas-Fermi
fig, ax = plt.subplots(figsize=(4.6, 2.5))
xs = np.linspace(0.005, 3.0, 1200)
ax.axvspan(0, 2 * y2, color="0.88", lw=0)
ax.plot(xs, FL(xs / 2), color="C0", lw=1.4, label=r"Lindhard, $F_{\mathrm{L}}(q/2k_{\mathrm{F}})$")
ax.axhline(1, color="0.2", lw=1.0, ls="--", label="Thomas\u2013Fermi")
ax.plot(xs[xs < 1.6], 1 - (xs[xs < 1.6] / 2) ** 2 / 3, color="C1", lw=1.0, ls=":", label=r"$1 - q^2/12k_{\mathrm{F}}^2$")
ax.axvline(2, color="0.6", lw=0.6, ls=":")
ax.text(2.04, 0.85, r"$2k_{\mathrm{F}}$", fontsize=8, color="0.35")
ax.set_xlim(0, 3)
ax.set_ylim(0, 1.1)
ax.set_xlabel(r"$q/k_{\mathrm{F}}$")
ax.set_ylabel(r"$[\varepsilon(q,0) - 1]\,q^2/k_{\mathrm{TF}}^2$")
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
sx = ax.secondary_xaxis("top", functions=(lambda x: x * kF / 1e3, lambda x: x * 1e3 / kF))
sx.set_xlabel(r"$q$ (keV), silicon valence density", fontsize=8)
sx.tick_params(labelsize=7)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit4_tf.pdf"))
plt.close(fig)

# ---------------------------------------------------------------- limit: plasmon dispersion
fig, ax = plt.subplots(figsize=(4.6, 2.6))
xs = np.linspace(0.02, qc / kF * (1 - 1e-4), 200)
ex = np.array([wpl(x * kF) for x in xs])
ax.axvspan(0, x1, color="0.88", lw=0)
ax.plot(xs, ex / wp, color="C3", lw=1.5, label="RPA, root of $\\varepsilon_1 = 0$")
xx = np.linspace(0, 0.95, 200)
ax.plot(xx, quad(xx * kF) / wp, color="0.2", lw=1.0, ls="--", label=r"$(\omega_p^2 + \frac{3}{5}v_{\mathrm{F}}^2q^2)^{1/2}$")
ax.plot(xx, quart(xx * kF) / wp, color="C0", lw=1.0, ls=":", label=r"with the $q^4$ term")
ax.plot(xx, wplus(xx * kF) / wp, color="0.5", lw=0.8, label=r"continuum edge $\omega_+$")
ax.plot([qc / kF], [wplus(qc) / wp], "o", color="C3", ms=3.5)
ax.text(qc / kF + 0.02, wplus(qc) / wp - 0.12, r"$q_{\mathrm{c}}$", color="C3", fontsize=8)
ax.set_xlim(0, 0.95)
ax.set_ylim(0.95, 1.8)
ax.set_xlabel(r"$q/k_{\mathrm{F}}$")
ax.set_ylabel(r"$\omega_{\mathrm{pl}}/\omega_p$")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit4_plasmon.pdf"))
plt.close(fig)
print("figures written")
