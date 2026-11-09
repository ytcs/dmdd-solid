"""Fig. 13.9 (fig:13-window-rates) and the mass exponent of Sect. 13.9 (log: fig13_9.log).

Panel (a): ratio of the zero-phonon to the phonon-assisted electron-recoil rate of silicon across the window, against the
dark-matter mass. These are ESTIMATES, plotted as such; nothing in this panel is computed by this script.
  Phonon-assisted side: the measured 20 K indirect absorption of silicon (Macfarlane et al. 1958) as the optical limit,
     times a computed form factor of the zero-phonon density vertex for the fall-off at finite q, screened by eps_1(q, omega)
     and restricted to the off-shell window (delta_w = 0.3 eV, Sect. 13.6). Known to a factor of ten either way.
     With the 0.5 K fit of Stanford et al. (the primary cold edge of Sect. 13.9) the ratios below change by 0.97-1.05
     (the two datasets agree within 5 % above 1.37 eV; interim13.log), so the plotted values are kept.
  Zero-phonon side: a Wannier-Mott continuum (Sect. 10.5) at each of the 24 equivalent off-axis minima of the first edge
     (6 valleys x 2 mirror planes x the two signs of the tilt), with vertices computed from PBE plane-wave states with
     spin-orbit coupling (Sect. 13.9): out-of-plane gradients 1.57 A (q, pair relaxed) and 0.32 A (k); the second
     (mirror-even) heavy hole with g_perp = 2.21 A, assigned entirely to that band (an upper estimate); SOC lift 1.3e-4.
  Both channels carry the same external 1/eps_1(q, omega)^2 at the same (q, omega), so the ratio is that of the proper eps_2.
  At fixed mass each channel is evaluated at the largest excess energy above the first edge that the mass reaches,
     0.015, 0.066, 0.115, 0.161 eV at 0.41, 0.42, 0.43, 0.44 MeV (an upper estimate of the integrated ratio).
  Values (ratio, first-hole + second-hole + SOC terms), for the second-hole edge at 0.4197 MeV (central) and 0.4150 MeV:
     0.41: 0.023 / 0.023;  0.42: 0.24 / 0.56;  0.43: 1.19 / 2.14;  0.44: 2.64 / 3.85.
  Allowed (-2,0,0) class at its X-face opening (0.50 MeV): 2.4 (lowest conduction band) to 7.0 (two lowest), 1 meV above
     the edge; 10-11 at 0.05 (2 pi/a) inside the class, reached from 0.508 MeV.
  Edges (computed): phonon-assisted onset 0.3332 (exciton replica) / 0.3374 MeV (free pair); first zero-phonon edge
     0.402-0.405 (1s) / 0.405-0.408 MeV (continuum, best 0.407, PBE + SOC, measured lattice constant); second heavy hole
     0.415-0.420 MeV; allowed (-2,0,0) line opens at 0.50 MeV.
  Criteria of the text: ratio 1 ("central" end of the phonon-assisted lead, 0.424-0.428 MeV) and ratio 1/3 (zero-phonon equal
     to the phonon-assisted rate at the low end of its band, 0.418-0.421 MeV), by linear interpolation of the table above.

Panel (b): model check of the mass exponent derived in Sect. 13.9 (eq:13.9-medge). For a direction-averaged loss function
  L(q, omega) = C x^p, x = omega - E_th(|q|), the rate of eq:10.2-rate near the onset mass m0 behaves as (m - m0)^(p + 7/2).
  Model: E_th(q) = E_g + omega_TA(k_c - q) on the valley axis [100] (free pair; the exciton replica lowers E_g by E_x^b),
  with the TA branch of the book's PBE force constants (figscripts/ch05/si_ifc.py, Sect. 5.2) on a spline through 400 points;
  E_g = 1.17 eV, k_c = 0.85 (2 pi/a), a = 5.431 A (Sect. 3.3), E_x^b = 14.7 meV (Sect. 4.9);
  eta(v_min) of the standard halo (Table 1.1: v0 = 238, v_esc = 544, v_E = 250.5 km/s) on its second branch, written as the
  integral of Sect. 1.3 above eq:1.3-edge (exact, free of the cancellation in the closed form near v_max);
  q^3 F_DM^2 with F_DM = 1 (heavy mediator); p = 3 (free-pair transverse acoustic edge) and p = 3/2 (exciton replica), Sect. 13.3.
  Plotted: the local exponent d ln R / d ln(m - m0) from finite differences on a logarithmic grid of m - m0.
Run: python fig13_9.py  (numpy, scipy, matplotlib; about 1 min). Output: tex/figures/ch13/fig13_9.pdf and fig13_9.log.
"""
import os
import sys
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar, brentq
from scipy.special import erf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch13", "fig13_9.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
LOG = open(os.path.join(HERE, "fig13_9.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


HBARC = 1973.269804          # eV A
CKM = 299792.458
A_SI = 5.431
G1 = 2 * np.pi * HBARC / A_SI
KC = 0.85 * G1
EG = 1.17
EXB = 0.0147
V0, VESC, VE = 238.0, 544.0, 250.5
VMAX = (VESC + VE) / CKM
_Z = VESC / V0
_NESC = np.pi ** 1.5 * V0 ** 3 * (erf(_Z) - 2 / np.sqrt(np.pi) * _Z * np.exp(-_Z ** 2))

# ---------------------------------------------------------------- TA branch along [100]
Qf = np.linspace(0.0, 1.0, 401)                       # units of 2 pi/a
w, _ = si_ifc.phonons(np.c_[Qf, 0 * Qf, 0 * Qf])
wTA = w[:, 0] * 1e-3                                   # eV, lowest branch
TA = CubicSpline(Qf * G1, wTA)
out("TA along [100]: omega(0.46 X) = %.2f meV, omega(X) = %.2f meV" % (TA(0.46 * G1) * 1e3, TA(G1) * 1e3))


def eta_edge(delta):
    """eta at v_min = v_max - delta (delta in km/s, second branch), in units of 1/c (Sect. 1.3, integral above eq:1.3-edge)."""
    pref = np.pi * V0 ** 2 / (VE * _NESC) * np.exp(-VESC ** 2 / V0 ** 2)
    f = lambda s: np.expm1((2 * VESC * s - s * s) / V0 ** 2)
    val, _ = quad(f, 0.0, delta, epsabs=0, epsrel=1e-12)
    return pref * val * CKM


def Eth(q, gap):
    return gap + TA(KC - q)


def F(q, m, gap):
    return q * VMAX - q * q / (2 * m) - Eth(q, gap)


def onset(gap):
    """Onset mass on the axis: smallest m with max_q F >= 0."""
    def fmax(m):
        r = minimize_scalar(lambda q: -F(q, m, gap), bounds=(0.3 * KC, 0.75 * KC), method="bounded",
                            options={"xatol": 1e-6})
        return -r.fun
    return brentq(fmax, 3.0e5, 3.6e5, xtol=1e-9, rtol=1e-15)


GL_X, GL_W = np.polynomial.legendre.leggauss(64)


def rate(m, gap, p):
    """Model rate (arbitrary units): int dq q^3 int_0^F dx eta(v_min) x^p, v_min = v_max - (F - x)/q."""
    r = minimize_scalar(lambda q: -F(q, m, gap), bounds=(0.3 * KC, 0.75 * KC), method="bounded", options={"xatol": 1e-7})
    qs, f0 = r.x, -r.fun
    if f0 <= 0:
        return 0.0
    h = np.sqrt(2 * m * f0)
    lo = brentq(lambda q: F(q, m, gap), qs - 3 * h, qs, xtol=1e-9)
    hi = brentq(lambda q: F(q, m, gap), qs, qs + 3 * h, xtol=1e-9)
    tot = 0.0
    for xq, wq in zip(GL_X, GL_W):
        # substitution q = c + d sin(theta) removes the square-root ends
        th = 0.5 * np.pi * xq
        c, d = 0.5 * (lo + hi), 0.5 * (hi - lo)
        q = c + d * np.sin(th)
        jac = d * np.cos(th) * 0.5 * np.pi
        fq = F(q, m, gap)
        if fq <= 0:
            continue
        xs = 0.5 * fq * (GL_X + 1)
        inner = 0.0
        for xx, wx in zip(xs, GL_W):
            delta = (fq - xx) / q * CKM          # km/s
            inner += wx * eta_edge(delta) * xx ** p
        inner *= 0.5 * fq
        tot += wq * jac * q ** 3 * inner
    return tot


res = {}
for name, gap, p in ((r"free pair, $p_{\mathrm{on}} = 3$", EG, 3.0), (r"exciton replica, $p_{\mathrm{on}} = 3/2$", EG - EXB, 1.5)):
    m0 = onset(gap)
    dm = np.geomspace(1e-6, 1e-2, 25) * 1e6         # eV
    R = np.array([rate(m0 + d, gap, p) for d in dm])
    loc = np.gradient(np.log(R), np.log(dm))
    res[name] = (dm, loc, p)
    out("%s: onset m0 = %.5f MeV" % (name, m0 / 1e6))
    for d, l in zip(dm[::3], loc[::3]):
        out("   m - m0 = %.1e MeV   F0 = %.3f meV   local exponent %.3f (p + 7/2 = %.2f)"
            % (d / 1e6, 0.5 * VMAX ** 2 * d * 1e3, l, p + 3.5))

out("F0 = v_max^2 (m - m0)/2 per 0.001 MeV: %.2f meV; m - m0 at F0 = 1.3 meV: %.1e MeV"
    % (0.5 * VMAX ** 2 * 1e3 * 1e3, 2 * 1.3e-3 / VMAX ** 2 / 1e6))
out("onset error 0.0004 MeV at 0.005 MeV above the onset, exponent 6.5-7: factor %.2f-%.2f"
    % ((1 - 0.08) ** 6.5, (1 - 0.08) ** 7))

# ---------------------------------------------------------------- panel (a) data (estimates; see docstring)
m_tab = np.array([0.41, 0.42, 0.43, 0.44])
r_cen = np.array([0.023, 0.24, 1.19, 2.64])
r_low = np.array([0.023, 0.56, 2.14, 3.85])
for target in (1.0, 1 / 3):
    mc = np.interp(np.log(target), np.log(r_cen), m_tab)
    ml = np.interp(np.log(target), np.log(r_low), m_tab)
    out("ratio %.2f reached at %.3f (central edge) / %.3f MeV (low edge), log-linear" % (target, mc, ml))
for target in (1.0, 1 / 3):
    mc = np.interp(target, r_cen, m_tab)
    ml = np.interp(target, r_low, m_tab)
    out("ratio %.2f reached at %.3f (central edge) / %.3f MeV (low edge), linear" % (target, mc, ml))

plt.rcParams.update({"font.size": 8, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.6, 2.9), gridspec_kw={"wspace": 0.36, "width_ratios": [1.35, 1]})

ax.axvspan(0.3332, 0.405, color="#9ad19a", alpha=0.45, lw=0)
ax.axvspan(0.405, 0.408, color="0.55", alpha=0.6, lw=0)
ax.axvspan(0.415, 0.420, color="0.75", alpha=0.6, lw=0)
ax.axvspan(0.43, 0.51, color="#f2c48d", alpha=0.35, lw=0)
ax.axvline(0.3374, color="C3", lw=0.8)
ax.axvline(0.3332, color="C3", lw=0.8, ls="--")
ax.axvline(0.50, color="C0", lw=0.8, ls="-.")
ax.fill_between(m_tab, r_cen / 10, r_low * 10, color="C0", alpha=0.12, lw=0)
ax.fill_between(m_tab, r_cen, r_low, color="C0", alpha=0.45, lw=0)
ax.plot(m_tab, r_cen, "o-", color="C0", ms=3, lw=1.0)
ax.plot(m_tab, r_low, "s--", color="C0", ms=3, lw=0.8)
ax.errorbar([0.50], [np.sqrt(2.4 * 7.0)], yerr=[[np.sqrt(2.4 * 7.0) - 2.4], [7.0 - np.sqrt(2.4 * 7.0)]], fmt="D",
            color="C0", ms=3, capsize=2, lw=0.8)
ax.annotate("", xy=(0.512, 60), xytext=(0.512, 10), arrowprops=dict(arrowstyle="->", color="C0", lw=0.8))
ax.plot([0.508, 0.516], [10, 10], color="C0", lw=1.0)
ax.axhline(1.0, color="k", lw=0.6)
ax.axhline(1 / 3, color="k", lw=0.6, ls=":")
ax.set_yscale("log")
ax.set_xlim(0.33, 0.53)
ax.set_ylim(1e-3, 3e2)
ax.set_xlabel(r"$m_\chi$ (MeV)")
ax.set_ylabel(r"$\mathcal{R}^{\mathrm{ZP}}/\mathcal{R}^{\mathrm{PA}}$ (estimate)")
ax.text(0.369, 2e-3, "phonon-assisted\nonly", ha="center", va="bottom", fontsize=6.5, color="#2e7d32")
ax.text(0.47, 1.5e2, "two-channel\nband", ha="center", va="top", fontsize=6.5, color="#a0522d")
ax.text(0.4065, 1.5e2, "first\nedge", ha="right", va="top", fontsize=6.5, color="0.3", rotation=90)
ax.text(0.4175, 1.5e2, "second\nhole", ha="left", va="top", fontsize=6.5, color="0.3", rotation=90)
ax.text(0.497, 2e-3, r"allowed $(\bar 2 00)$ opens", ha="right", va="bottom", fontsize=6.5, color="C0", rotation=90)
ax.text(0.338, 1.5e2, "onset", ha="left", va="top", fontsize=6.5, color="C3", rotation=90)
ax.text(0.442, 0.25, "ratio 1/3", fontsize=6.5, va="top")
ax.set_title("(a)", loc="left", fontsize=8)

for name, (dm, loc, p) in res.items():
    col = "C3" if p == 3.0 else "C1"
    bx.semilogx(dm / 1e6, loc, color=col, lw=1.2, label=name.replace(", ", ",\n", 1))
    bx.axhline(p + 3.5, color=col, lw=0.6, ls=":")
bx.axvline(2 * 1.3e-3 / VMAX ** 2 / 1e6, color="0.5", lw=0.6, ls="--")
bx.set_xlabel(r"$m_\chi - m_{\mathrm{min}}^{\mathrm{PA}}$ (MeV)")
bx.set_ylabel(r"$\mathrm{d}\ln\mathcal{R}/\mathrm{d}\ln(m_\chi - m_{\mathrm{min}}^{\mathrm{PA}})$")
bx.set_ylim(4.5, 7.0)
bx.legend(fontsize=6.5, loc="center left", frameon=False)
bx.set_title("(b)", loc="left", fontsize=8)

fig.subplots_adjust(left=0.105, right=0.98, bottom=0.16, top=0.92)
fig.savefig(OUT)
out("wrote", OUT)
