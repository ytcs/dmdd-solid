"""Fig. 12.4 (Sect. 12.4): the three regimes of the Migdal effect in silicon against the momentum transfer q.
Output: tex/figures/ch12/fig12_4.pdf. Prints every number of Sect. 12.4 that rests on this model (log: fig12_4.log).

Model (leading entry eq:12.1-Skk, diagonal G = G', the form of Berghaus et al. 2210.06490 Eq. (3.8)):
    d2P/domega_l domega_e = 4 alpha int d^3p/(2pi)^3 Z_ion(p)^2 (v_N.p)^2 L(p, omega_e) / (omega_e^4 p^2) s(|q - p|, omega_l),
with s the incoherent T = 0 response of one Si nucleus (unit weight, zero-phonon line included). In the incoherent
harmonic model the n-phonon weight of s(Q, .) is the Poisson weight e^{-2W(Q)} (2W(Q))^n / n!, 2W(Q) = Q^2 <u_x^2>
(Sect. 11.3). The fraction of Migdal events with n phonons is therefore the Poisson weight averaged over the momentum p
the electrons take, with the weight of the integrand above:
    w(p, c) dp dc  ~  c^2 Z_ion(p)^2 g(p) p^2 dp dc ,   g(p) = int_{omega >= E_g} dw L(p, w) / w^4 ,
c = cos(q, p). The mean lattice energy is <|q - p|^2>/2M (first moment of s, Sect. 11.3).
Inputs (reused): L(p, omega) with local fields and Z_ion(p) from mig12.py (Knapen-Kozaczuk-Lin tables, Sect. 12.3;
scissor gap 1.11 eV, p <= 22.5 keV, omega <= 89 eV); 2W(Q), <omega>, M from ../ch11/imp11.py (PBE DOS, Sect. 5.2).
Regime boundaries: e^{-2W(q)} = 1/2 (zero-phonon line holds half of the lattice weight at the kick q); the impulse onset
x_R = E_R/<omega> = 4, q = 92.5 keV (Sect. 11.4). Top axis: the lightest dark matter that reaches q, m_chi = q/(2 v_max),
v_max = 794.5 km/s (Sect. 1.2).
Coherence of the zero-phonon line (printed, not plotted): in the exact harmonic lattice factor the zero-phonon part is
the Bragg term, so p = q - G with G a reciprocal-lattice vector; per nucleus the zero-phonon Migdal probability is
    P_0^coh = (1/Omega_p) sum_G (|S_G|^2/2) F(q - G) e^{-2W(G)} ,  F(p) = 4 alpha v_N^2 c^2 Z_ion(p)^2 g(p),
against the incoherent P_0^inc = int d^3p/(2pi)^3 F(p) e^{-2W(|q - p|)} (diamond structure factor |S_G|^2 = |1 + e^{iG.tau}|^2,
tau = (a/4)(1,1,1), a = 5.431 A; Omega_p = a^3/4). Both are averaged over the direction of q.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mig12 as G  # noqa: E402
import imp11 as IMP  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch12")
M = G.M
VMAX = IMP.VMAX
HBARC = 1973.269804           # eV A
A_SI = 5.431                  # A

# electronic weight g(p) on the momentum grid, and Z_ion^2
sel = G.OM >= G.EG
W = G.OM[sel]
K = G.KG[1:]
Z2 = G.ZG[1:]**2
LK = G.LF_G[sel][:, 1:]
gk = np.trapezoid(LK / W[:, None]**4, W, axis=0)          # g(p), eV^-3 (per unit of L)
wk = K**2 * Z2 * gk                                         # radial weight
CN, CW = np.polynomial.legendre.leggauss(48)
CW = CW / 2
WEIGHT = wk[:, None] * (CN**2 * CW)[None, :]               # [p, c]
WEIGHT = WEIGHT * np.gradient(K)[:, None]
WEIGHT /= WEIGHT.sum()

ux2 = IMP.two_w(1.0)            # 2W(Q) = ux2 * Q^2


def regime(q):
    """Phonon-number fractions n = 0..5 and n >= 6 of Migdal events, mean lattice energy, at kick q (eV)."""
    Q2 = q**2 + K[:, None]**2 - 2 * q * K[:, None] * CN[None, :]
    tw = ux2 * Q2
    from scipy.stats import poisson
    fr = [np.sum(WEIGHT * poisson.pmf(n, tw)) for n in range(6)]
    fr.append(1 - sum(fr))
    mean_wl = np.sum(WEIGHT * Q2) / (2 * M)
    return np.array(fr), mean_wl


qs = np.geomspace(1e3, 300e3, 140)
FR = np.array([regime(q)[0] for q in qs])
MW = np.array([regime(q)[1] for q in qs])
ZP_soft = np.exp(-IMP.two_w(qs))
p2 = np.sum(WEIGHT * K[:, None]**2)
q_half = np.sqrt(np.log(2) / ux2)
q_onset = G.Q_ONSET

print("Electronic weight of the leading entry: <p^2>^(1/2) = %.2f keV, median p = %.2f keV"
      % (np.sqrt(p2) / 1e3, np.interp(0.5, np.cumsum(WEIGHT.sum(axis=1)), K) / 1e3))
print("Regime boundaries: e^-2W(q) = 1/2 at q = %.1f keV (m_chi = %.2f MeV); impulse onset q = %.1f keV (m_chi = %.2f MeV)"
      % (q_half / 1e3, q_half / (2 * VMAX) / 1e6, q_onset / 1e3, q_onset / (2 * VMAX) / 1e6))
for q in [2e3, 5e3, 10e3, 20e3, 33.2e3, 50e3, 92.5e3, 150e3]:
    fr, mw = regime(q)
    print("  q = %6.1f keV (m_chi >= %5.2f MeV): E_R = %7.3f meV, e^-2W(q) = %.4f; Migdal events: zero-phonon %.4f, "
          "one %.4f, two %.4f, >=3 %.4f; mean omega_l = %.3f meV = %.2f E_R; <|q-p|^2>/q^2 = %.3f"
          % (q / 1e3, q / (2 * VMAX) / 1e6, q**2 / 2 / M * 1e3, np.exp(-IMP.two_w(q)), fr[0], fr[1], fr[2],
             fr[3:].sum(), mw * 1e3, mw / (q**2 / 2 / M), mw * 2 * M / q**2))

# ---- coherence of the zero-phonon line --------------------------------------------------------------------------
b = 2 * np.pi / A_SI * HBARC                     # 2 pi / a in eV
Omega_p = A_SI**3 / 4 / HBARC**3                 # eV^-3
nmax = 27
hkl = np.array([(h, k, l) for h in range(-nmax, nmax + 1) for k in range(-nmax, nmax + 1) for l in range(-nmax, nmax + 1)
                if (h % 2 == k % 2 == l % 2)])
Gv = hkl * b
Gm = np.linalg.norm(Gv, axis=1)
phase = np.pi / 2 * hkl.sum(axis=1)              # G.tau with tau = (a/4)(1,1,1)
S2 = np.abs(1 + np.exp(1j * phase))**2
keep = (S2 > 1e-9) & (Gm < 62e3)
Gm, S2 = Gm[keep], S2[keep]
Fg = np.interp  # alias


def F_of(p, c):
    """c^2 Z_ion^2 g(p), zero above the table edge (22.5 keV)."""
    z2g = np.interp(p, K, Z2 * gk, left=(Z2 * gk)[0], right=0.0)
    return c**2 * z2g


xs, xw = np.polynomial.legendre.leggauss(64)
xw = xw / 2


def coh_ratio(q):
    tot = 0.0
    for g, s2 in zip(Gm, S2):
        if g == 0:
            tot += (s2 / 2) * F_of(q, 1.0)
            continue
        p = np.sqrt(q**2 + g**2 - 2 * q * g * xs)
        c = (q - g * xs) / p
        tot += (s2 / 2) * np.exp(-ux2 * g**2) * np.sum(xw * F_of(p, c))
    coh = tot / Omega_p
    # incoherent: int d^3p/(2pi)^3 F e^{-2W(|q-p|)}
    pp = np.linspace(1.0, K[-1], 2000)
    PP, CC = np.meshgrid(pp, xs, indexing="ij")
    Q2 = q**2 + PP**2 - 2 * q * PP * CC
    inc = np.trapezoid(np.sum(xw[None, :] * F_of(PP, CC) * np.exp(-ux2 * Q2), axis=1) * pp**2, pp) * 2 / (2 * np.pi)**2
    return coh / inc


print("Zero-phonon Migdal line, coherent (Bragg) sum over G / incoherent integral, averaged over the direction of q:")
for q in [2e3, 3e3, 5e3, 7.5e3, 10e3, 15e3, 20e3, 30e3]:
    print("  q = %5.1f keV (%.2f q_BZ): %.3f" % (q / 1e3, q / G.QBZ, coh_ratio(q)))

# ---- figure -------------------------------------------------------------------------------------------------------
fig, (ax, ax2) = plt.subplots(2, 1, figsize=(5.0, 4.6), sharex=True, gridspec_kw=dict(height_ratios=(3, 1.6), hspace=0.08))
cols = ["#2b6ca3", "#5aa0d0", "#9cc9e8", "#f2c46d", "#e8914a", "#c8553d", "#7a2e2e"]
labs = ["zero-phonon", "1 phonon", "2", "3", "4", "5", r"$\geq 6$"]
ax.stackplot(qs / 1e3, FR.T, colors=cols, labels=labs, alpha=0.95)
ax.plot(qs / 1e3, ZP_soft, color="k", lw=0.9, ls="--", label=r"$\mathrm{e}^{-2W(q)}$ (lattice at $q$)")
for x in (q_half, q_onset):
    ax.axvline(x / 1e3, color="k", lw=0.6, ls=":")
ax.text(4.5, 0.5, "zero-phonon\nMigdal", ha="center", va="center", color="w", fontsize=8)
ax.text(np.sqrt(q_half * q_onset) / 1e3, 0.93, "multiphonon", ha="center", fontsize=8)
ax.text(170, 0.93, "impulse", ha="center", fontsize=8, color="w")
ax.set_xscale("log")
ax.set_xlim(1, 300)
ax.set_ylim(0, 1)
ax.set_ylabel("fraction of Migdal events")
ax.legend(fontsize=6, loc="lower left", ncol=2, framealpha=0.9)
sec = ax.secondary_xaxis("top", functions=(lambda x: x * 1e3 / (2 * VMAX) / 1e6, lambda m: m * 1e6 * 2 * VMAX / 1e3))
sec.set_xlabel(r"lightest $m_\chi$ that reaches $q$ (MeV)", fontsize=8)
sec.tick_params(labelsize=7)

ER = qs**2 / (2 * M)
ax2.loglog(qs / 1e3, MW * 1e3, color="C3", lw=1.2, label=r"mean $\omega_l$ of a Migdal event")
ax2.loglog(qs / 1e3, ER * 1e3, color="k", lw=0.9, ls="--", label=r"$E_R = q^2/2M$")
ax2.axhline(p2 / (2 * M) * 1e3, color="0.5", lw=0.7, ls="-.", label=r"$\langle p^2\rangle/2M$")
for x in (q_half, q_onset):
    ax2.axvline(x / 1e3, color="k", lw=0.6, ls=":")
ax2.set_xlabel(r"momentum transfer $q$ (keV)")
ax2.set_ylabel(r"$\omega_l$ (meV)")
ax2.legend(fontsize=6, loc="upper left")
ax2.set_ylim(1e-2, 2e3)
fig.subplots_adjust(left=0.13, right=0.97, top=0.89, bottom=0.11)
fig.savefig(os.path.join(OUT, "fig12_4.pdf"))
print("wrote", os.path.join(OUT, "fig12_4.pdf"))
