"""Limit Check 14.5a (lim:14.5a, Sect. 14.5): chiral phonons (panel a) and the metastable line of a single-molecule magnet
(panel b). Output tex/figures/ch14/limit14_5a.pdf, log limit14_5a.log.  Run: python limit14_5a.py  (about two minutes).

Panel (a), chiral phonons in GaAs (point group -43m, no inversion, time reversal kept).
  Phonons: the PBE force constants of Sect. 5.5 through gaas_ifc14.py (acoustic branches equal to the matdyn dispersion of
  Fig. 5.4 to 1e-3 meV). Angular momentum L^ph_{Q nu} = -i sum_kappa e*_{kappa nu}(Q) x e_{kappa nu}(Q), units of hbar
  (Romao et al. 2301.07617 Eq. (6); Matas et al. 2511.20461 Eq. (11)).
  Literature formula: the probability that an event ends as a detectable chiral phonon is taken as the average of |L^ph| over the
  lowest band, every mode equally likely (2511.20461 Sect. III: kappa = <||J_1||>/hbar, quoted 0.07 for GaAs from a published
  dynamical matrix; 2301.07617 Sect. VII: 0.15 for InF3(bpy)). Here: the same average on a shifted 20^3 grid of the first zone.
  Fuller result: the final-state-resolved one-phonon response, eq:11.1-S1 with the angular momentum of each created mode,
  for a heavy-mediator coupling to nucleon number (A_kappa = 69.723, 74.922, the mass numbers to the accuracy needed), T = 0,
  Debye-Waller factor set to 1 (W < 0.03 for q < 10 keV with <u_x^2> = 1.9e-3 A^2 of Sect. 11.7), crystal orientation averaged:
  per d^3q the halo kernel is eta(v_min)/(2q) (App. A.8), v_min = omega/q + q/(2 m_chi), standard halo of App. A.8 (aniso11.py).
  The q sum runs over q = Q + G (Q on the 20^3 grid, all G), |q| <= 2 m_chi v_max, phonon energies above 0.5 meV.
  Plotted against m_chi: rate-weighted <|L^ph|> of the created lowest-band phonons and of all created phonons.
  Dotted: masses where the lowest band takes less than 1 % of the one-phonon rate.
  Shaded: masses where the rate-weighted value for the lowest band is within 10 % of the band average (contiguous window from
  the heaviest mass; below about 0.8 MeV the lowest band takes less than 1 % of the rate and its sampled average is noisy).
  Control: silicon (inversion and time reversal) gives |L^ph| < 1e-12 on the same grid (si_ifc.py of Sect. 5.2).

Panel (b), the metastable line of Mn12-acetate (S = 10).
  Spin Hamiltonian H = -D S_z^2 + B40 O40 - omega_Lar S_z (2601.01043 Eq. (3) for the axial term; the field term as in Sect. 14.3),
  D = 0.454 cm^-1, B40 = -2.0e-5 cm^-1 (Edwards et al., cond-mat/0302052, Fig. 2 caption; their D = -0.454 in the sign convention
  H = D S_z^2), O40 = 35 m^4 - 30 S(S+1) m^2 + 25 m^2 - 6 S(S+1) + 3 S^2 (S+1)^2.  MODELLING CHOICE: B0 = 1 T (the field of
  2601.01043 Sect. IV) and g = 2, so omega_Lar = 0.1158 meV.
  Literature formula: the molecule sits in the metastable state m = -S (2601.01043 Fig. 4(b)); the S+ line m = -S -> -S+1 then has the
  full weight 2S at omega_meta = E(-S+1) - E(-S).
  Fuller result: thermal populations p_m inside the metastable well (levels m = -S ... up to the barrier top), net absorption
  (p_m - p_{m+1}) [S(S+1) - m(m+1)] on every in-well S+ line. Plotted against omega_meta/T: the net weight of the line at omega_meta,
  over 2S, and the net weight summed over all in-well lines, over 2S (= 2|<S_z>|_well / 2S, the sum rule of the spin algebra).
  Shaded: omega_meta/T where the metastable line keeps 90 % of 2S.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import gaas_ifc14 as G                 # noqa: E402
from aniso11 import upsilon, VESC, VE, C_KMS   # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch14")
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(HERE, "limit14_5a.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


# ---------------------------------------------------------------- panel (a)
B = np.array([[-1, -1, 1], [1, 1, 1], [-1, 1, -1]], float)       # fcc reciprocal vectors, 2 pi/a
NQ = 20
g = (np.array([(i, j, k) for i in range(NQ) for j in range(NQ) for k in range(NQ)], float) + 0.5) / NQ
Qc = g @ B
w, ev = G.phonons(Qc)
L = G.ang_mom(ev)
aL = np.linalg.norm(L, axis=2)                       # (Q, nu)
out(f"(a) GaAs, shifted {NQ}^3 grid: band-averaged <|L^ph|> by band (lowest first): " + ", ".join(f"{x:.3f}" for x in aL.mean(0)))
out(f"    lowest band: <|L^ph|> = {aL[:, 0].mean():.4f}; fraction of its modes with |L^ph| > 0.4: {(aL[:, 0] > 0.4).mean():.3f};"
    f" max |L^ph| = {aL.max():.3f}")
for N10, sh in ((10, 0.0), (10, 0.5)):
    gg = (np.array([(i, j, k) for i in range(N10) for j in range(N10) for k in range(N10)], float) + sh) / N10
    qq = gg @ B
    qq = qq[np.linalg.norm(qq, axis=1) > 1e-9]
    _, e2 = G.phonons(qq)
    out(f"    check {N10}^3 grid, shift {sh}: lowest-band <|L^ph|> = {np.linalg.norm(G.ang_mom(e2), axis=2)[:, 0].mean():.4f}")
out("    quoted for GaAs (2511.20461, published dynamical matrix, 10^3 grid): 0.07")
# time reversal: L(-Q) = -L(Q)
_, em = G.phonons(-Qc[:50])
Lm = G.ang_mom(em)
gap = np.minimum(np.abs(np.diff(w[:50], axis=1, prepend=-1e3)), np.abs(np.diff(w[:50], axis=1, append=1e3)))
out(f"    time reversal check: max|L(Q) + L(-Q)| over modes of 50 grid points separated by > 0.05 meV from their neighbours: "
    f"{np.max(np.abs(L[:50] + Lm)[gap > 0.05]):.1e}")
# silicon control
try:
    from si_ifc import phonons as si_ph
    _, es = si_ph(Qc[:300])
    es = es.reshape(es.shape[0], 2, 3, 6)
    Ls = np.real(-1j * np.cross(np.conj(es), es, axis=2).sum(axis=1))
    out(f"    silicon control (inversion and time reversal), 300 points: max |L^ph| = {np.abs(Ls).max():.1e}")
except Exception as exc:     # pragma: no cover
    out("    silicon control skipped:", exc)

# one-phonon rates
A_KAP = np.array([69.723, 74.9216])
MASSU = np.array([69.723, 74.9216])
QUNIT_KEV = 2 * np.pi / G.A_ANG * 1.973269804           # keV per (2 pi/a)
out(f"    2 pi/a = {QUNIT_KEV:.3f} keV (static PBE a = {G.A_ANG:.4f} A)")
vstar_grid = np.linspace(0, VESC + VE + 1, 4000)
eta_grid = upsilon(0, vstar_grid)                       # (km/s)^-1, eta(v_min)
eta = lambda v: np.interp(v, vstar_grid, eta_grid, right=0.0)
vmax = (VESC + VE) / C_KMS
evr = ev.reshape(len(Qc), 2, 3, 6)                     # (Q, kappa, alpha, nu)
masses = np.logspace(np.log10(0.1), np.log10(5.0), 20)  # MeV
res = []
for m in masses:
    qmax = 2 * m * 1e3 * vmax / QUNIT_KEV                # 2 pi/a
    nmax = int(np.ceil(qmax)) + 2
    Gs = np.array([(i, j, k) for i in range(-nmax, nmax + 1) for j in range(-nmax, nmax + 1) for k in range(-nmax, nmax + 1)],
                  float) @ B
    Gs = Gs[np.linalg.norm(Gs, axis=1) <= qmax + 1.8]
    num_all = num_ta = den_all = den_ta = 0.0
    for Gv in Gs:
        q = Qc + Gv
        qn = np.linalg.norm(q, axis=1)
        sel = (qn <= qmax) & (qn > 1e-9)
        if not sel.any():
            continue
        qs, qns = q[sel], qn[sel]
        ph = np.exp(2j * np.pi * qs @ G.TAU.T)          # (n, kappa)
        qe = np.einsum("na,nkav->nkv", qs, np.conj(evr[sel]))
        F = np.einsum("k,nk,nkv->nv", A_KAP / np.sqrt(MASSU), ph, qe) * (2 * np.pi)
        om = w[sel]                                      # meV
        qkev = qns * QUNIT_KEV
        vst = (om * 1e-3 / (qkev[:, None] * 1e3) + qkev[:, None] * 1e3 / (2 * m * 1e6)) * C_KMS
        wt = np.abs(F)**2 / (2 * np.maximum(om, 1e-9)) * eta(vst) / qns[:, None]
        wt[om < 0.5] = 0.0
        num_all += np.sum(wt * aL[sel]); den_all += np.sum(wt)
        num_ta += np.sum(wt[:, 0] * aL[sel][:, 0]); den_ta += np.sum(wt[:, 0])
    if den_all > 0:
        res.append((m, num_all / den_all, num_ta / den_ta if den_ta > 0 else np.nan, den_ta / den_all))
res = np.array(res)
band_avg = aL[:, 0].mean()
for r in res:
    out(f"    m = {r[0]:7.3f} MeV: rate-weighted <|L|> all = {r[1]:.4f}, lowest band = {r[2]:.4f}, "
        f"lowest-band share of the one-phonon rate = {r[3]:.3f}")
ok = np.abs(res[:, 2] / band_avg - 1) <= 0.1
# contiguous window from the heaviest mass down (isolated grid points where the lowest band carries < 1 % of the rate are noise)
k0 = len(ok) - 1
while k0 > 0 and ok[k0 - 1]:
    k0 -= 1
ok = np.zeros_like(ok); ok[k0:] = True
if ok.any():
    out(f"    lowest band within 10 % of the band average for m_chi in [{res[ok,0].min():.3f}, {res[ok,0].max():.3f}] MeV "
        f"(grid points {np.sum(ok)})")
else:
    out("    lowest band never within 10 % of the band average on this mass grid")

# ---------------------------------------------------------------- panel (b)
CM = 0.123984198      # meV per cm^-1
KB = 0.08617333262    # meV/K
MUB = 0.05788381806   # meV/T
S = 10
Dz, B40 = 0.454 * CM, -2.0e-5 * CM
wL = 2 * MUB * 1.0
ms = np.arange(-S, S + 1)
O40 = 35 * ms**4 - 30 * S * (S + 1) * ms**2 + 25 * ms**2 - 6 * S * (S + 1) + 3 * S**2 * (S + 1)**2
E = -Dz * ms**2 + B40 * O40 - wL * ms
E0 = -Dz * ms**2 - wL * ms
iS = 0
wmeta = E[1] - E[0]
out(f"(b) Mn12-acetate, S = 10, D = {Dz:.5f} meV, B40 = {B40:.3e} meV, B0 = 1 T, g = 2 (omega_Lar = {wL:.4f} meV)")
out(f"    D(2S-1) = {Dz*(2*S-1):.4f} meV; with B40: E(-9)-E(-10) at B0 = 0 is {(E[1]+wL*ms[1])-(E[0]+wL*ms[0]):.4f} meV")
out(f"    metastable line omega_meta = {wmeta:.4f} meV = {wmeta/KB:.2f} K (axial term only: {E0[1]-E0[0]:.4f} meV)")
itop = np.argmax(E[:S + 1])                # top of the barrier on the m <= 0 side
out(f"    barrier top at m = {ms[itop]}, height above m = -S: {E[itop]-E[0]:.3f} meV = {(E[itop]-E[0])/KB:.1f} K")
well = slice(0, itop + 1)
x = np.logspace(np.log10(0.3), np.log10(30), 400)
yline, ytot = [], []
for xv in x:
    T = wmeta / xv
    p = np.exp(-(E[well] - E[0]) / T)
    p /= p.sum()
    mm = ms[well]
    me2 = S * (S + 1) - mm * (mm + 1)
    pn = np.append(p[1:], 0.0)
    net = (p - pn) * me2
    yline.append(net[0] / (2 * S))
    ytot.append(net.sum() / (2 * S))
yline, ytot = np.array(yline), np.array(ytot)
xok = x[yline >= 0.9].min()
out(f"    metastable line keeps >= 90 % of 2S for omega_meta/T >= {xok:.2f}, i.e. T <= {wmeta/xok/KB:.2f} K for Mn12-acetate")
for TK in (0.5, 1.0, 2.0, 4.0, 8.0):
    xv = wmeta / (KB * TK)
    out(f"    T = {TK} K: omega_meta/T = {xv:.2f}, line weight/2S = {np.interp(xv, x, yline):.4f}, "
        f"all in-well lines/2S = {np.interp(xv, x, ytot):.4f}")
out(f"    neighbouring in-well line (m = -S+1 -> -S+2) at {E[2]-E[1]:.4f} meV, {wmeta-(E[2]-E[1]):.4f} meV below omega_meta")

# ---------------------------------------------------------------- figure
fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.1))
ax = axs[0]
if ok.any():
    ax.axvspan(res[ok, 0].min(), res[ok, 0].max(), color="0.88", lw=0, zorder=0)
ax.axhline(band_avg, color="k", lw=1.0, label=r"band average, lowest band")
big = res[:, 3] >= 0.01
kb = len(big) - 1
while kb > 0 and big[kb - 1]:
    kb -= 1
big[:kb] = False
out(f"    lowest band takes >= 1 % of the one-phonon rate for m_chi >= {res[kb, 0]:.3f} MeV")
ax.semilogx(res[:, 0], res[:, 2], color="C3", lw=0.8, ls=":")
ax.semilogx(res[big, 0], res[big, 2], color="C3", lw=1.3, label="created, lowest band")
ax.semilogx(res[:, 0], res[:, 1], color="C0", lw=1.3, ls="--", label="created, all branches")
ax.set_xlim(0.1, 5)
ax.set_xticks([0.1, 0.3, 1, 3]); ax.set_xticklabels(["0.1", "0.3", "1", "3"]); ax.minorticks_off()
ax.set_ylim(0, 0.42)
ax.set_xlabel(r"$m_\chi$ (MeV)")
ax.set_ylabel(r"$\langle|\mathbf{L}^{\mathrm{ph}}|\rangle$")
ax.set_title("(a) chiral phonons in GaAs", fontsize=8)
ax.legend(fontsize=7, frameon=False, loc="upper left")

ax = axs[1]
ax.axvspan(xok, 30, color="0.88", lw=0, zorder=0)
ax.axhline(1, color="k", lw=1.0, label=r"all molecules in $m = -|\mathbf{S}|$")
ax.semilogx(x, yline, color="C3", lw=1.3, label=r"line at $\omega_{\mathrm{meta}}$")
ax.semilogx(x, ytot, color="C0", lw=1.3, ls="--", label="all lines of the well")
for TK, mk in ((1.0, "o"), (4.0, "^")):
    xv = wmeta / (KB * TK)
    ax.plot([xv], [np.interp(xv, x, yline)], mk, color="k", ms=4, mfc="w", label=f"Mn$_{{12}}$-acetate, {TK:.0f} K")
ax.set_xlim(0.3, 30)
ax.set_ylim(0, 1.1)
ax.set_xlabel(r"$\omega_{\mathrm{meta}}/T$")
ax.set_ylabel(r"net weight $/\,2|\mathbf{S}|$")
ax.set_title("(b) metastable line of a molecular magnet", fontsize=8)
ax.legend(fontsize=7, frameon=False, loc="lower right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit14_5a.pdf"))
out("wrote", os.path.join(FIG, "limit14_5a.pdf"))
LOG.close()
