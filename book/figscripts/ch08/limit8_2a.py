"""Limit Check 8.2a (validity of the first Born approximation) of Sect. 8.2: map and the numbers quoted with it.

Output: tex/figures/ch08/limit8_2a.pdf; every number goes to limit8_2a.log (stdout).
Natural units hbar = c = 1, energies in eV.

Physics.  Yukawa potential between the dark matter and one target particle, V(r) = -/+ (g/4 pi) e^{-m_V r}/r with
g = y_chi y_e (electron) or A y_chi y_N (coherent nucleus), reduced mass mu, relative momentum p = mu v.
  first Born amplitude f_1(q) = mu g / [2 pi (q^2 + m_V^2)],  |f(0)| = mu g/(2 pi m_V^2)  (Sect. 2.2)
  (1) zero energy: the scattering length is a = a_1 (1 + |f(0)| m_V/2 + ...) for attraction, so the cross section is
      sigma = sigma_Born (1 +/- |f(0)| m_V)  [computed below by integrating the zero-energy radial equation].
  (2) p >> m_V: partial waves (variable-phase method) at small coupling give the order-g^3 correction to the total and
      the differential cross section.  It stays below the Sommerfeld parameter g/(4 pi v) = mu g/(4 pi p) and falls
      as m_V/p -> 0 (pure Coulomb: Born modulus exact).  The parameter is set by the relative momentum p, not by q.
  Estimate used for the map (exact at p -> 0, twice the Sommerfeld parameter at p >> m_V):
      delta_Born = |f(0)| m_V * m_V/(m_V + p) = mu g / [2 pi (m_V + p)].
  The calibration below compares delta_Born with the computed correction to the total and the differential cross
  section (q <= 2p): within 30 % of the largest computed value for p <= m_V, above it for p >= 3 m_V.
  Perturbative couplings, g <= 4 pi (electron) or g/A <= 4 pi (nucleus), give delta_Born <= 2 mu A/(m_V + p): a 10 %
  correction then needs m_V + p <= 20 mu A (A = 1 for electrons); above this the plot is hatched.
Couplings: reference cross sections of the book, sigma_e-bar = 1e-37 cm^2 (Chaps. 1, 10) and sigma_p = 1e-40 cm^2
  (Sect. 11.9), with the form factor normalized at q_0 = alpha m_e (eq:1.4-yukawa-sigma; Sect. 11.1):
      g_e = sqrt(pi sigma_e) (m_V^2 + q_0^2)/mu_chie,   g_N = A sqrt(pi sigma_p) (m_V^2 + q_0^2)/mu_chip.
  Then delta_Born = sqrt(pi sigma)(m_V^2 + q_0^2)/[2 pi (m_V + p)] x (1 for electrons; A mu_chiN/mu_chip for nuclei):
  the dark-matter mass enters only through p.  v = 1e-3 (as Sect. 2.2); the speed of a bound electron only raises p,
  so the electron estimate is conservative.  Silicon: A = 28, M = 28.0855 u (natural silicon).
Plot: contours of the cross section at which delta_Born = 0.1, sigma_10 = sigma_ref (0.1/delta_ref)^2, over m_chi and m_V;
  dashed m_V = p = mu v; dotted m_V = q_0; gray: the 10 % point needs y_chi y > 4 pi.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.special import spherical_jn, spherical_yn
from numpy.polynomial.legendre import leggauss, legval

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch08")
alpha = 1 / 137.035999
me = 510998.95
mp = 938272.09e3
mu_u = 931494.10e3
hbarc_cm = 197.3269804e-7            # eV cm
q0 = alpha * me
A, MSi = 28, 28.0855 * mu_u
v = 1e-3

# ---------- (1) zero-energy coefficient ----------
def scatt_length(lam):
    """u'' = -lam e^{-r}/r u (units m_V = 1); a = r - u/u' at large r. lam = 2 mu (g/4pi)/m_V = |f(0)| m_V."""
    s = solve_ivp(lambda r, y: [y[1], -lam * np.exp(-r) / r * y[0]], [1e-8, 60], [1e-8, 1.0], rtol=1e-12, atol=1e-16)
    return 60 - s.y[0, -1] / s.y[1, -1]

print("(1) zero energy, attractive Yukawa, lam = |f(0)| m_V:")
for lam in [1e-3, 1e-2, 0.1]:
    a = -scatt_length(lam)
    print(f"  lam = {lam:.0e}: a m_V = {a:.6e}; (a/a_1 - 1)/lam = {(a/lam - 1)/lam:.4f}; sigma/sigma_Born - 1 = {(a/lam)**2 - 1:.4e}")

# ---------- (2) partial waves at small coupling ----------
tg, wg = leggauss(600)

def Ql(l, z):
    c = np.zeros(l + 1); c[l] = 1
    return 0.5 * np.sum(wg * legval(tg, c) / (z - tg))

def phase(l, k, lam, R=40.0):
    U = lambda r: -lam * np.exp(-r) / r     # attractive, units m_V = 1
    def f(r, d):
        x = k * r
        j, n = x * spherical_jn(l, x), -x * spherical_yn(l, x)
        return [-(U(r) / k) * (np.cos(d[0]) * j + np.sin(d[0]) * n) ** 2]
    r0 = max(1e-8, 0.05 * l / k)
    return solve_ivp(f, [r0, R], [0.0], rtol=1e-11, atol=1e-16, max_step=min(0.5 / k, 1.0)).y[0, -1]

print("(2) partial waves, attractive, lam = 1e-3; corrections in units of lam = |f(0)| m_V and of g/(4 pi v) = lam m_V/2p;")
print("    delta_Born/lam = 1/(1 + p/m_V)")
lam = 1e-3
calib = []
for kap in [0.1, 0.3, 1.0, 3.0, 10.0]:
    L = int(8 * kap + 15); ls = np.arange(L)
    d = np.array([phase(l, kap, lam) for l in ls])
    dB = np.array([(lam / (2 * kap)) * Ql(l, 1 + 1 / (2 * kap**2)) for l in ls])
    tot = 2 * np.sum((2 * ls + 1) * dB * (d - dB)) / np.sum((2 * ls + 1) * dB**2)
    est = 1 / (1 + kap)
    row = [kap, tot / lam]
    out = f"  p/m_V = {kap:5.1f}: total {tot/lam:.4f} lam ({tot/lam*2*kap:.3f} Sommerfeld)"
    for qq in sorted({min(1.0, 1.999 * kap), kap, 1.999 * kap}):
        ct = 1 - qq**2 / (2 * kap**2)
        P = np.array([legval(ct, np.eye(L)[l]) for l in ls])
        df = np.sum((2 * ls + 1) * (np.exp(1j * d) * np.sin(d) - dB) * P) / kap
        rel = 2 * df.real / (lam / (qq**2 + 1)) / lam
        row.append(rel)
        out += f"; q/m_V = {qq:5.2f}: {rel:.4f} lam ({rel*2*kap:.3f} Sommerfeld)"
    out += f"; estimate {est:.4f} lam; max computed/estimate = {max(row[1:])/est:.3f}"
    calib.append(row)
    print(out)

# ---------- benchmark of the text ----------
s39 = 3.0e-39 / hbarc_cm**2
print(f"heavy dark photon (m_V = 30 MeV, sigma_e = 3.0e-39 cm^2): |f(0)| m_V = sqrt(pi sigma)(m_V^2+q0^2)/(2 pi m_V) = "
      f"{np.sqrt(np.pi*s39)*(30e6**2+q0**2)/(2*np.pi*30e6):.2e}")

# ---------- map ----------
def red(a, b):
    return a * b / (a + b)

sig_e = 1e-37 / hbarc_cm**2
sig_p = 1e-40 / hbarc_cm**2
mchi = np.logspace(3, 9, 241)
mV = np.logspace(0, 10, 241)
MC, MV = np.meshgrid(mchi, mV)

def delta_e(mc, mv, sig):
    p = red(mc, me) * v
    return np.sqrt(np.pi * sig) * (mv**2 + q0**2) / (2 * np.pi * (mv + p))

def delta_N(mc, mv, sig):
    muN, mup = red(mc, MSi), red(mc, mp)
    p = muN * v
    return A * muN / mup * np.sqrt(np.pi * sig) * (mv**2 + q0**2) / (2 * np.pi * (mv + p))

De, DN = delta_e(MC, MV, sig_e), delta_N(MC, MV, sig_p)
S10e = 1e-37 * (0.1 / De) ** 2
S10N = 1e-40 * (0.1 / DN) ** 2
print(f"map: m_chi 1 keV - 1 GeV, m_V 1 eV - 10 GeV, v = {v}")
print(f"  electrons, sigma_e = 1e-37 cm^2: max delta_Born = {De.max():.2e}; min sigma_e(10 %) = {S10e.min():.2e} cm^2 at "
      f"m_chi = {MC.flat[S10e.argmin()]:.3g} eV, m_V = {MV.flat[S10e.argmin()]:.3g} eV")
print(f"  nuclei (Si), sigma_p = 1e-40 cm^2: max delta_Born = {DN.max():.2e}; min sigma_p(10 %) = {S10N.min():.2e} cm^2 at "
      f"m_chi = {MC.flat[S10N.argmin()]:.3g} eV, m_V = {MV.flat[S10N.argmin()]:.3g} eV")
for mc in [1e3, 1e6, 1e8, 1e9]:
    for mv in [1.0, red(mc, me) * v, q0, 1e6, 1e9]:
        de = delta_e(mc, mv, sig_e); dn = delta_N(mc, mv, sig_p)
        print(f"  m_chi = {mc:.0e}, m_V = {mv:.3g}: delta_e = {de:.2e} (sigma_e,10% = {1e-37*(0.1/de)**2:.1e}); "
              f"delta_N = {dn:.2e} (sigma_p,10% = {1e-40*(0.1/dn)**2:.1e})")
# heavy-mediator asymptote, mu-independent for electrons
print(f"  heavy (m_V >> q_0, p): delta_e = sqrt(pi sigma_e) m_V/2pi = {np.sqrt(np.pi*sig_e)/(2*np.pi):.2e} m_V/eV; "
      f"10 % at m_V = {0.2*np.pi/np.sqrt(np.pi*sig_e):.2e} eV")
cN = A * red(1e9, MSi) / red(1e9, mp) * np.sqrt(np.pi * sig_p) / (2 * np.pi)
print(f"  heavy, Si nuclei, m_chi = 1 GeV: delta_N = A (mu_N/mu_p) sqrt(pi sigma_p) m_V/2pi = {cN:.2e} m_V/eV at sigma_p = 1e-40; "
      f"at the perturbative edge m_V = 539 GeV: delta_N = {cN*5.39e11:.2e}, sigma_p(10 %) = {1e-40*(0.1/(cN*5.39e11))**2:.1e} cm^2")
gmax = np.sqrt(np.pi * sig_e) * (1e10**2 + q0**2) / red(1e9, me)
print(f"  y_chi y_e at m_V = 10 GeV, m_chi = 1 GeV, sigma_e = 1e-37: {gmax:.2f} (4 pi = {4*np.pi:.2f})")
# light limit m_V -> 0: Coulomb-type, sigma_e at which g/(4 pi v) = 0.05 (delta_Born = 0.1)
for mc in [1e3, 1e9]:
    p = red(mc, me) * v
    print(f"  light limit, m_chi = {mc:.0e} eV: delta_e = sqrt(pi sigma_e) q0^2/(2 pi p) = {np.sqrt(np.pi*sig_e)*q0**2/(2*np.pi*p):.2e}")

print(f"  perturbative edge of the 10 % point (g = 4 pi, resp. g/A = 4 pi): m_V = 20 mu A - p; electrons at m_chi = 1 GeV: "
      f"{(20*red(1e9, me) - red(1e9, me)*v)/1e6:.2f} MeV, at 1 keV: {(20*red(1e3, me) - red(1e3, me)*v)/1e3:.2f} keV; "
      f"Si nuclei at 1 GeV: {(20*A*red(1e9, MSi) - red(1e9, MSi)*v)/1e9:.0f} GeV")
pert_e = MV + red(MC, me) * v <= 20 * red(MC, me)
pert_N = MV + red(MC, MSi) * v <= 20 * A * red(MC, MSi)
print(f"  inside the perturbative region: min sigma_e(10 %) = {S10e[pert_e].min():.2e} cm^2 at m_chi = {MC[pert_e][S10e[pert_e].argmin()]:.3g} eV, "
      f"m_V = {MV[pert_e][S10e[pert_e].argmin()]:.3g} eV; min sigma_p(10 %) = {S10N[pert_N].min():.2e} cm^2 at "
      f"m_chi = {MC[pert_N][S10N[pert_N].argmin()]:.3g} eV, m_V = {MV[pert_N][S10N[pert_N].argmin()]:.3g} eV")

# ---------- figure ----------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, axs = plt.subplots(1, 2, figsize=(6.2, 2.8), sharey=True)
for ax, S, lab, ref in [(axs[0], S10e, r"electrons: $\bar\sigma_e$ [cm$^2$] at 10 %", -37),
                        (axs[1], S10N, r"silicon nuclei: $\sigma_p$ [cm$^2$] at 10 %", -40)]:
    Z = np.log10(S)
    pline = (red(mchi, me) if ref == -37 else red(mchi, MSi)) * v
    mueff = red(mchi, me) if ref == -37 else A * red(mchi, MSi)
    edge = 20 * mueff - pline
    Z = np.where(MV <= np.interp(MC, mchi, edge), Z, np.nan)
    lv = np.arange(-36, -15, 2)
    cs = ax.contour(MC / 1e6, MV / 1e6, Z, levels=lv, colors="C0", linewidths=0.8, linestyles="solid")
    man = [(2.5e-3, 4e-6), (0.03, 1e-5), (0.3, 3e-6), (30, 2.5e-2), (30, 4e-3), (30, 0.7), (300, 6), (30, 7e-2)] if ref == -37 else \
        [(300, 4e3), (300, 400), (0.3, 120), (300, 10), (0.01, 0.3), (300, 1.2), (300, 0.15), (300, 2e-3), (1.5, 1e-4), (6, 1e-5), (0.03, 1.2e-5)]
    lbl = ax.clabel(cs, levels=lv, fmt=lambda x: r"$10^{%d}$" % x, fontsize=7, inline=False, manual=man)
    for t in lbl:
        t.set_bbox(dict(facecolor="white", edgecolor="none", pad=0.4))
        if ref == -37 and t.get_text() == r"$10^{-24}$":       # hugs the gray boundary: set it just below its contour
            x0, y0 = t.get_position()
            t.set_position((x0, y0 / 2.0))
    ax.plot(mchi / 1e6, pline / 1e6, color="C3", lw=1.0, ls=(0, (4, 2)))
    ax.axhline(q0 / 1e6, color="0.4", lw=0.6, ls=":")
    ax.fill_between(mchi / 1e6, edge / 1e6, 1e4, color="0.88", lw=0, zorder=3)
    ax.plot(mchi / 1e6, edge / 1e6, color="0.3", lw=0.7, zorder=4)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(1e-3, 1e3); ax.set_ylim(1e-6, 1e4)
    ax.set_xlabel(r"$m_\chi$ [MeV]")
    ax.set_title(lab, fontsize=8)
axs[0].set_ylabel(r"$m_V$ [MeV]")
for ax in axs:
    ax.text(1.5e-3, 3e-3, r"$q_0$", color="0.3", fontsize=7)
axs[0].text(30, 1.0e-4, r"$m_V = p_{\mathrm{rel}}$", color="C3", fontsize=7)
# the dashed line m_V = p_rel is labeled in the left panel only: in the right panel every spot along it is crossed by contours
axs[0].text(1.5e-3, 1.5e2, r"$y_\chi y_e > 4\pi$", color="0.2", fontsize=7, zorder=5)
axs[1].text(1.5e-3, 1.5e2, r"$y_\chi y_N > 4\pi$", color="0.2", fontsize=7, zorder=5)
fig.tight_layout()
os.makedirs(OUT, exist_ok=True)
fig.savefig(os.path.join(OUT, "limit8_2a.pdf"))
print("wrote limit8_2a.pdf")
