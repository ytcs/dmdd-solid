"""Limit Check 20.2b (lim:20.2b, fig:20-limit-iso): the Rayleigh (Tamura) isotope rate against the Born rate with the full
phonon density of states of silicon.  Log: limit20_2b.log.  Run: python limit20_2b.py > limit20_2b.log  (about two minutes).

Born rate of a phonon of frequency omega off random mass defects (derived in Sect. 20.2; equals the width of Sect. 11.6):
    Gamma_iso(omega) = (pi/6) g_md omega^2 g_ph,kappa(omega),    g_ph,kappa normalized to 3 modes per site,
exact at second order in the mass defects for any mode of silicon (cubic site symmetry).  Its long-wavelength limit is
    Gamma_iso = g_md Omega_at <c^-3> omega^4 / (4 pi) = B_iso (E_ath/h)^4,  B_iso = 4 pi^3 g_md Omega_at <c^-3>
(Hernandez et al., arXiv:2408.04732, Eq. (4); eq:E.12-iso), with <c^-3> the sphere average of (1/3) sum_nu c_nu^-3.
The ratio of the two is g_ph,kappa(omega)/g_Debye(omega), independent of g_md.
DOS: the PBE force constants of Sect. 5.2 (figscripts/ch05/si_ifc.py, Fourier interpolation of the 6^3 DFPT constants), integrated
over the Brillouin zone in spherical coordinates about Gamma: Gauss-Legendre in cos(theta) (NT points) x uniform phi (2 NT), each
ray from Q = 0 to the zone boundary (fcc zone: reciprocal vectors <111> and <200> in 2pi/a), NQ midpoint steps in |Q|, weight
Q^2 dQ dOmega; frequencies histogrammed in 0.1-meV bins.  This samples the region near Gamma finely, so that g/g_Debye is
reliable down to 1 meV (the cached matdyn DOS of 5.2 is not, below about 3 meV).  The Debye reference uses the PBE sound speeds
(slopes at Q = 0.01 x 2pi/a along each ray), so that the ratio isolates the dispersion; the PBE <c^-3> is printed against the
measured-tensor value of phon20_2.py.  MODELLING CHOICE: 0.1-meV bins with a 3-bin running mean for the plotted ratio; the
10 % crossing is found by brentq on the linear interpolant of the unsmoothed 0.1-meV ratio after a 5-bin running mean.
Leading correction: g/g_Debye - 1 = a (E/E_D)^2, a fitted by least squares on 2-6 meV (E_D = 55.6 meV, Sect. 5.2).
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc as S  # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch20")
HBAR = 6.582119569e-16      # eV s
A = 5.431e-10               # m
E_D = 55.6                  # meV, Debye energy of Sect. 5.2

NT, NQ = 32, 800
xg, wg = np.polynomial.legendre.leggauss(NT)
phis = (np.arange(2 * NT) + 0.5) * np.pi / NT
dphi = np.pi / NT
G = np.array([(i, j, k) for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)] +
             [(2, 0, 0), (-2, 0, 0), (0, 2, 0), (0, -2, 0), (0, 0, 2), (0, 0, -2)], float)

bins = np.arange(0.0, 64.5, 0.1)
hist = np.zeros(len(bins) - 1)
cinv3 = []
qs = 0.01
for x, w in zip(xg, wg):
    st = np.sqrt(1 - x * x)
    for ph in phis:
        n = np.array([st * np.cos(ph), st * np.sin(ph), x])
        ng = G @ n
        qb = np.min((G**2).sum(1)[ng > 1e-12] / (2 * ng[ng > 1e-12]))
        dq = qb / NQ
        q = (np.arange(NQ) + 0.5) * dq
        om, _ = S.phonons(np.outer(q, n))
        wt = w * dphi * q**2 * dq
        for nu in range(6):
            hist += np.histogram(om[:, nu], bins=bins, weights=wt)[0]
        o0, _ = S.phonons(qs * n[None, :])
        c = o0[0, :3] * 1e-3 / HBAR / (qs * 2 * np.pi / A)      # m/s
        cinv3.append((w, np.mean(c**-3.0)))
# normalization: (V_cell/(2pi)^3) d^3Q, Q in 2pi/a: V_cell (2pi/a)^3/(2pi)^3 = a^3/4 / a^3 = 1/4 per (2pi/a)^3
gcell = hist * 0.25 / np.diff(bins)          # modes per meV per cell (6 in total)
Ec = 0.5 * (bins[1:] + bins[:-1])
print(f"total modes per cell = {np.sum(gcell*np.diff(bins)):.4f} (6 expected)")
wsum = sum(w for w, _ in cinv3)
cm3_pbe = sum(w * v for w, v in cinv3) / wsum
print(f"PBE <c^-3> = {cm3_pbe:.4e} s^3/m^3 (1/<c^-3> = {1/cm3_pbe:.4e}); measured tensor (phon20_2.log): 4.9031e-12")
print(f"PBE/measured <c^-3> = {cm3_pbe/4.9031e-12:.3f}")
# Debye DOS per cell in modes per meV: V_cell omega^2 3<c^-3>/(2 pi^2), omega in rad/s, per meV: d omega/dE = 1e-3/HBAR
Vc = A**3 / 4
om = Ec * 1e-3 / HBAR
gD = Vc * om**2 * 3 * cm3_pbe / (2 * np.pi**2) * (1e-3 / HBAR)
ratio = gcell / gD


def smooth(y, k):
    return np.convolve(y, np.ones(k) / k, mode="same")


r5 = smooth(ratio, 5)
for e in [1, 2, 3, 4.136, 5, 6, 8, 10, 12, 15, 17, 20, 25]:
    i = np.argmin(np.abs(Ec - e))
    print(f"E = {e:6.2f} meV: g/g_Debye = {ratio[i]:.4f} (5-bin mean {r5[i]:.4f})")
mfit = (Ec > 2) & (Ec < 6)
X = (Ec[mfit] / E_D) ** 2
a = np.sum(X * (ratio[mfit] - 1)) / np.sum(X * X)
print(f"leading correction fit on 2-6 meV: g/g_Debye - 1 = {a:.2f} (E/E_D)^2")
f = lambda e: np.interp(e, Ec, r5) - 1.10
e10 = brentq(f, 3.0, 14.0)
print(f"10 % crossing of the Rayleigh law: E_ath = {e10:.2f} meV = {e10/4.135667696:.2f} THz = {e10/E_D:.3f} E_D")
print(f"  (leading-correction estimate: (0.1/a)^(1/2) E_D = {np.sqrt(0.1/a)*E_D:.2f} meV)")
f20 = lambda e: np.interp(e, Ec, r5) - 1.0 - 0.0
ipk = np.argmax(np.where(Ec < 30, r5, 0))
print(f"maximum of the ratio below 30 meV: {r5[ipk]:.2f} at {Ec[ipk]:.1f} meV (transverse van Hove peak)")
# absolute rate at 1 THz from the DOS with g_md and measured B (WE cross-check)
gmd = 2.0070e-4
i1 = np.argmin(np.abs(Ec - 4.135667696))
om1 = 2 * np.pi * 1e12
g_site = r5[i1] * gD[i1] / 2 / (1e-3 / HBAR)   # per site per (rad/s)
print(f"Born rate with PBE DOS at 1 THz: (pi/6) g_md omega^2 g_site = {np.pi/6*gmd*om1**2*g_site:.3e} 1/s")

fig, ax = plt.subplots(figsize=(4.6, 3.1))
m = Ec <= 30
ax.axvspan(0, e10, color="0.88", lw=0)
ax.plot(Ec[m], smooth(ratio, 3)[m], color="#c0392b", lw=1.3, label="Born rate, PBE density of states")
ax.axhline(1.0, color="#2c6fbb", ls="--", lw=1.2, label=r"Rayleigh law $B_{\mathrm{iso}}(E_{\mathrm{ath}}/h)^4$")
ee = np.linspace(0, 14, 100)
ax.plot(ee, 1 + a * (ee / E_D) ** 2, color="k", ls=":", lw=1.1, label=r"$1 + %.1f\,(E_{\mathrm{ath}}/\omega_{\mathrm{D}})^2$" % a)
ax.set_xlim(0, 30)
ax.set_ylim(0.8, 3.2)
ax.set_xlabel(r"$E_{\mathrm{ath}}$ (meV)")
ax.set_ylabel(r"$\mathit{\Gamma}_{\mathrm{iso}}$ / Rayleigh law")
sec = ax.secondary_xaxis("top", functions=(lambda e: e / 4.135667696, lambda f: f * 4.135667696))
sec.set_xlabel(r"$E_{\mathrm{ath}}/h$ (THz)")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit20_2b.pdf"))
print("wrote limit20_2b.pdf")
