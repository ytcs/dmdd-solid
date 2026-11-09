"""ZrTe5 with the background dielectric constant in the total epsilon (Sect. 16.1; Fig. 16.1 data).

Inputs: Geilhufe et al., arXiv:1910.02091, Table 1 row ISIF7 and Table 2 (dirac16.ZRTE5): v = (1.1, 0.44, 0.91)e-3,
Lambda_i = (0.23, 0.216, 0.1) 1/A, eps_bg,ii = (308.4, 20.75, 126.1), g = 2; energy cutoff Lt = min_i v_i Lambda_i
= 0.180 eV (their Eq. (2.21)).  Central parameter set (book): the whole experimental-structure (NR) row of their
Table 1, v = (1.1, 0.45, 1.0)e-3, Lambda_i = (0.23, 0.215, 0.1) 1/A (Lt = 0.191 eV), Delta_D = 11.8 meV (text below
Table 1: gap 23.6 meV <-> Delta = 11.8 meV), with the Table 2 tensor.  Computed range: the ISIF7 row (Delta = 15.6 meV,
the row they implement, with its own velocities and cutoff) and 17.5 meV (their Ref. [21] row; evaluated here with the
NR velocities and cutoff).  The 'Exp. [52]' row (11.75 meV) is measured, not computed.  The recomputation of the
published curves uses their implemented ISIF7 row.  Off-diagonal entries of their Table 2 (|kappa_ij| <= 1.2) are
dropped (modelling choice).  The DFPT tensor is used as the background; the Dirac term inside it is 3-8 % (Sect. 7.3 WE).
Scattering: light mediator, F_DM = (alpha m_e/q)^2, 3 events in 1 kg yr, book halo (rate10_2.py); the loss function is
averaged over the directions of q (24 x 24 Gauss-Legendre octant), i.e. the rate averaged over crystal orientations.
Rules: 'book' = total eps (q.eps_bg.q + eps_D); 'src' = the per-component rule of 1910.02091 Eq. (3.14) (with q_x^2 v_x^2);
'lead' = Im eps_D/(q.eps_bg.q)^2; 'iso' = the isotropic model of Sect. 7.3 WE (geometric-mean v, harmonic-mean eps_bg)
with the total eps.  rho_T = 6.089 g/cm^3 (measured, as quoted in 1910.02091 Fig. 3(d)); the ratios do not depend on it.
Absorption: per polarization along the principal axes, unpolarized average, rho_T = 6.135 g/cm^3 for the comparison with
the published curve (the value used there), rho_chi = 0.3 GeV/cm^3.
Kinematic thresholds by root-finding on m (brentq) with the inner maximization over q by bounded minimization.
Published curves: digitized from the vector figures of the arXiv sources (data/*.csv).
Halo dependence: the published curves state no halo constants; the published-rule recomputation is repeated with
(v0, v_E, v_esc) = (220, 232, 600) and (220, 232, 544) km/s, and the published/total-eps ratio with the same halos.
Run: python zrte5_16.py > zrte5_16.log   (about four minutes); writes zrte5_16.npz.
"""
import os
import numpy as np
from scipy.optimize import brentq, minimize_scalar
import dirac16 as d
from scipy.special import erf

np.seterr(divide="ignore", invalid="ignore")   # zero rate just above the kinematic threshold

HERE = os.path.dirname(os.path.abspath(__file__))
ZP = d.ZRTE5                        # implemented ISIF7 row of 1910.02091 (Delta_D = 15.6 meV), published curves
Z = dict(ZP, v=np.array([1.1e-3, 4.5e-4, 1.0e-3]), Lam=np.array([0.23, 0.215, 0.1]), D=11.8e-3)   # NR row (central)
Z["Lt"] = float(np.min(Z["Lam"] * d.HBARC * Z["v"]))
v, ebg, g, D, Lt = Z["v"], Z["ebg"], Z["g"], Z["D"], Z["Lt"]
DP = ZP["D"]
vg = np.prod(v) ** (1 / 3)
eh = d.harmonic(ebg)
print("ZrTe5 central (NR row): v = %s, Delta_D = %.1f meV, Lt = %.4f eV, eps_bg = %s, g = %d ; ISIF7 row: v = %s, Delta = %.1f meV, Lt = %.4f eV"
      % (v, D * 1e3, Lt, ebg, g, ZP["v"], DP * 1e3, ZP["Lt"]))
print("isotropic model: v_D = %.4e (geometric mean), eps_bg = %.2f (harmonic mean), alpha~ = %.3f, Lambda_D = Lt/v_D = %.1f eV"
      % (vg, eh, d.ALPHA / (eh * vg), Lt / vg))
print("per-axis eps_bg^2 = %.3g, %.3g, %.3g ; (eps_xx/eps_yy)^2 = %.1f" % (*(ebg**2), (ebg[0] / ebg[1]) ** 2))


# --- kinematic threshold: half-gap against a misread full gap -------------------------------------------------------
def mthr(Dh, vv):
    def gap(m):
        f = lambda q: -(q * d.VMAX - q**2 / (2 * m) - np.sqrt((vv * q) ** 2 + 4 * Dh**2))  # noqa: E731
        r = minimize_scalar(f, bounds=(1e-3, 2 * m * d.VMAX), method="bounded", options=dict(xatol=1e-10))
        return -r.fun
    return brentq(gap, 1e3, 1e6, xtol=1e-6)


for Dh, vv, lab in [(11.75e-3, v, "11.75 meV (measured Exp. row; NR velocities)"), (D, v, "half-gap 11.8 meV (NR row)"),
                    (DP, ZP["v"], "half-gap 15.6 meV (ISIF7 row)"), (17.5e-3, v, "17.5 meV (Ref. [21]; NR velocities)"),
                    (2 * D, v, "gap 23.6 meV read as Delta (NR velocities)")]:
    vgg = np.prod(vv) ** (1 / 3)
    print("threshold mass, isotropic v_D = %.3e, Delta = %s: %.2f keV (flat-band limit 4 Delta/v_max^2 = %.2f keV)"
          % (vgg, lab, mthr(Dh, vgg) / 1e3, 4 * Dh / d.VMAX**2 / 1e3))
    print("  along x, y, z: %.2f, %.2f, %.2f keV" % tuple(mthr(Dh, vv[i]) / 1e3 for i in range(3)))

# --- loss-function tables on a fixed (omega, q) grid -----------------------------------------------------------------
nw, nq = 240, 420
iso = dict(v=np.full(3, vg), ebg=np.full(3, eh), g=g)


def grid(Dh, M):
    Wg = 2 * Dh + (2 * M["Lt"] - 2 * Dh) * np.linspace(0, 1, nw) ** 2
    Wg[0] = 2 * Dh * (1 + 1e-6)
    Qg = np.geomspace(2 * Dh / d.VMAX * 0.99, 2 * M["Lt"] / min(M["v"]), nq)
    return Wg, Qg


def tables(Dh, rules, M=Z):
    Bt = d.Btab(Dh, M["Lt"])
    Wg, Qg = grid(Dh, M)
    out = {}
    for rule in rules:
        mat, r = {"book": (M, "book"), "src": (M, "src"), "lead": (M, "lead"), "iso": (iso, "book"),
                  "iso_src": (iso, "src")}[rule]
        out[rule] = np.array([d.L_aniso_avg(Qg, w, mat, Bt, r) for w in Wg])
    return Wg, Qg, out, Bt


W, Q, tabs, Bt = tables(D, ("book", "src", "lead", "iso", "iso_src"))
# isotropic check: the iso source rule is eps_bg^2 times the iso book rule at every point
mask = tabs["iso"] > 0
print("iso check: max |L_src/L - eps_bg^2|/eps_bg^2 = %.1e" % np.max(np.abs(tabs["iso_src"][mask] / tabs["iso"][mask] / eh**2 - 1)))
WP, QP, tabsP, BtP = tables(DP, ("book", "src"), ZP)
D175 = 17.5e-3
W175, Q175, tabs175, _ = tables(D175, ("book",))


def eta_halo(vmin, v0, vE, vesc):
    """eta of the truncated boosted Maxwellian (same form as rate10_2.eta) for other halo constants (km/s)."""
    ck = d.R.CKM
    u = np.maximum(np.asarray(vmin) * ck, 0.0)
    z = vesc / v0
    nesc = np.pi**1.5 * v0**3 * (erf(z) - 2 / np.sqrt(np.pi) * z * np.exp(-z**2))
    k = np.pi * v0**2 / (vE * nesc)
    b1 = k * (np.sqrt(np.pi) * v0 / 2 * (erf((u + vE) / v0) - erf((u - vE) / v0)) - 2 * vE * np.exp(-z**2))
    b2 = k * (np.sqrt(np.pi) * v0 / 2 * (erf(z) - erf((u - vE) / v0)) - (vesc + vE - u) * np.exp(-z**2))
    return np.where(u < vesc - vE, b1, np.where(u < vesc + vE, b2, 0.0)) * ck


def rate(m, tab, rhoT, Wg=None, Qg=None, halo=None):
    """events per kg yr per cm^2 (rate per unit sigma_e)."""
    Wg = W if Wg is None else Wg
    Qg = Q if Qg is None else Qg
    Wm, Qm = np.meshgrid(Wg, Qg, indexing="ij")
    vm = Wm / Qm + Qm / (2 * m)
    et = d.R.eta(vm) if halo is None else eta_halo(vm, *halo)
    integ = Qm**3 * et * (d.Q0 / Qm) ** 4 * tab
    dR = np.trapezoid(integ, Qg, axis=1)
    return np.trapezoid(dR, Wg) * d.prefactor(m, rhoT) * d.KGYR * d.SIG1


rho = Z["rho_exp"] * d.GCM3
m_th = mthr(D, min(v))
masses = np.geomspace(m_th * 1.0005, 1e6, 60)
lim = {k: np.array([d.sigma_lim(rate(m, tabs[k], rho)) for m in masses]) for k in ("book", "src", "lead", "iso")}
print("\nscattering reach (3 events, 1 kg yr, light mediator, orientation average, rho_T = 6.089 g/cm^3):")
for mt in (20e3, 50e3, 100e3, 300e3, 1e6):
    j = np.argmin(np.abs(masses - mt))
    print("  m = %6.1f keV: total eps %.3e ; published rule %.3e ; ratio %.0f ; leading/total rate %.3f ; isotropic model %.3e (iso/aniso %.2f)"
          % (masses[j] / 1e3, lim["book"][j], lim["src"][j], lim["book"][j] / lim["src"][j],
             lim["book"][j] / lim["lead"][j], lim["iso"][j], lim["iso"][j] / lim["book"][j]))
sel = masses >= 20e3
rat = lim["book"] / lim["src"]
print("  ratio of reaches (= N_src/N_book) for 20 keV-1 MeV: %.0f to %.0f ; isotropised eps_bg^2 = %.0f"
      % (rat[sel].min(), rat[sel].max(), eh**2))
jb = np.argmin(lim["book"])
print("  best total-eps reach %.2e cm^2 at %.0f keV" % (lim["book"][jb], masses[jb] / 1e3))
r100 = rate(1e5, tabs["book"], rho)
print("  rate at m = 100 keV and sigma_e = 1e-38 cm^2: %.2f per kg yr" % (r100 * 1e-38))

# published scattering curves
p10 = np.loadtxt(os.path.join(HERE, "data", "pub_scat_ZrTe5_th.csv"), delimiter=",")
p10 = p10[np.argsort(p10[:, 0])]
# recomputation of the published curve with the implemented row (Delta_D = 15.6 meV)
m_thP = mthr(DP, min(ZP["v"]))
massesP = np.geomspace(m_thP * 1.0005, 1e6, 60)
HALOS = [None, (220.0, 232.0, 600.0), (220.0, 232.0, 544.0)]
HLAB = ["book halo (238, 250.5, 544)", "halo (v0, v_E, v_esc) = (220, 232, 600)", "halo (220, 232, 544)"]
limP = {}
for hl, lab in zip(HALOS, HLAB):
    limP[lab] = {k: np.array([d.sigma_lim(rate(m, tabsP[k], rho, WP, QP, hl)) for m in massesP]) for k in ("book", "src")}
    srcI = np.interp(p10[:, 0] * 1e3, massesP, limP[lab]["src"] * Z["rho_exp"] / Z["rho_src"])
    rr = srcI / p10[:, 1]
    for lo in (20, 50):
        s = p10[:, 0] >= lo
        print("  published-rule recomputation (Delta_D = 15.6 meV, %s) / published 1910.02091 ZrTe5 th. curve, m >= %d keV: %.2f to %.2f"
              % (lab, lo, rr[s].min(), rr[s].max()))
    ratP = limP[lab]["book"] / limP[lab]["src"]
    selP = massesP >= 20e3
    print("    published/total-eps rate ratio, Delta_D = 15.6 meV, %s, 20 keV-1 MeV: %.0f to %.0f" % (lab, ratP[selP].min(), ratP[selP].max()))
for hl, lab in zip(HALOS[1:], HLAB[1:]):
    lb = np.array([d.sigma_lim(rate(m, tabs["book"], rho, W, Q, hl)) for m in masses])
    ls = np.array([d.sigma_lim(rate(m, tabs["src"], rho, W, Q, hl)) for m in masses])
    print("  published/total-eps rate ratio, Delta_D = 11.8 meV, %s, 20 keV-1 MeV: %.0f to %.0f" % (lab, (lb / ls)[sel].min(), (lb / ls)[sel].max()))
# half-gap range of the computed rows: total-eps reach at Delta_D = 15.6 and 17.5 meV
for Dh, vmin_ax, Wg, Qg, tb in [(DP, min(ZP["v"]), WP, QP, tabsP["book"]), (D175, min(v), W175, Q175, tabs175["book"])]:
    mm = np.geomspace(mthr(Dh, vmin_ax) * 1.0005, 1e6, 60)
    lb = np.array([d.sigma_lim(rate(m, tb, rho, Wg, Qg)) for m in mm])
    j = np.argmin(lb)
    print("  total-eps reach with Delta_D = %.1f meV: best %.2e cm^2 at %.0f keV ; at 100 keV %.2e ; at 1 MeV %.2e"
          % (Dh * 1e3, lb[j], mm[j] / 1e3, np.interp(1e5, mm, lb), lb[-1]))
p08 = np.loadtxt(os.path.join(HERE, "data", "pub_h_Zr_th.csv"), delimiter=",")

# --- absorption -------------------------------------------------------------------------------------------------------
maP = np.geomspace(2 * DP * 1.0005, 2 * ZP["Lt"] * 0.999, 300)
LpP = d.abs_L_pol(maP, ZP, BtP)
zsP = d.zeta_lim((LpP * ebg).mean(axis=1), Z["rho_src"] * d.GCM3)
pa = np.loadtxt(os.path.join(HERE, "data", "pub_abs_ZrTe5_th.csv"), delimiter=",")
pa = pa[(pa[:, 1] < 1e-14) & (pa[:, 0] > 2 * DP * 1.3) & (pa[:, 0] < 2 * ZP["Lt"] * 0.98)]
ra = np.interp(pa[:, 0], maP, zsP) / pa[:, 1]
print("\nabsorption: published-rule recomputation (Delta_D = 15.6 meV) / published 1910.02091 ZrTe5 th. curve: %.4f to %.4f (%d points)" % (ra.min(), ra.max(), len(ra)))
ma = np.geomspace(2 * D * 1.0005, 2 * Lt * 0.999, 300)
Lp = d.abs_L_pol(ma, Z, Bt)                 # (n, 3)
Lbook = Lp.mean(axis=1)
Lsrc = (Lp * ebg).mean(axis=1)
zb = d.zeta_lim(Lbook, Z["rho_src"] * d.GCM3)
zs = d.zeta_lim(Lsrc, Z["rho_src"] * d.GCM3)
print("absorption with the central Delta_D = 11.8 meV below:")
fz = zb / zs
print("zeta reach factor total/published: %.3f to %.3f over %.0f-%.0f meV ; per axis sqrt(eps_bg,ii) = %.2f, %.2f, %.2f"
      % (fz.min(), fz.max(), ma[0] * 1e3, ma[-1] * 1e3, *np.sqrt(ebg)))
share = (Lp / Lp.sum(axis=1, keepdims=True))
j = np.argmin(np.abs(ma - 0.1))
print("at 100 meV: polarization shares of the total-eps rate x,y,z = %.3f, %.3f, %.3f ; zeta reach %.2e (total eps), %.2e (published rule)"
      % (*share[j], zb[j], zs[j]))
jm = np.argmin(zb)
print("best total-eps absorption reach zeta = %.2e at %.0f meV" % (zb[jm], ma[jm] * 1e3))

np.savez(os.path.join(HERE, "zrte5_16.npz"), masses=masses, book=lim["book"], src=lim["src"], lead=lim["lead"],
         iso=lim["iso"], p10=p10, p08=p08, ebg08=d.EBG_1708, ma=ma, zb=zb, zs=zs, pa=pa,
         massesP=massesP, srcP=limP[HLAB[0]]["src"], srcP_halo=limP[HLAB[1]]["src"], maP=maP, zsP=zsP)

# --- excitonic (Sommerfeld) region near the edge, isotropic model ------------------------------------------------------
# Nonrelativistic Sommerfeld factor of the pair, S = x/(1 - e^-x) with x = pi alpha~/b, b = (1 - 4 Delta^2/s)^(1/2)
# the speed of each carrier in the pair frame in units of v_D (Sect. 16.1 validity).  Binding energy Delta alpha~^2/4.
at = d.ALPHA / (eh * vg)
xs = brentq(lambda x: x / (1 - np.exp(-x)) - 1.5, 0.1, 5)
bS = np.pi * at / xs
print("\nisotropic alpha~ = %.3f: exciton binding Delta alpha~^2/4 = %.3f meV ; S = 1.5 at b = %.3f, i.e. sqrt(s) < %.3f x 2 Delta"
      % (at, D * at**2 / 4 * 1e3, bS, 1 / np.sqrt(1 - bS**2)))
s_cut = 4 * D**2 / (1 - bS**2)
for mt in (2e4, 1e5, 1e6):
    def Lcut(q, w, cut):
        e = d.epsD_iso(q, w, vg, g, Bt)
        s = w**2 - (vg * q) ** 2
        num = np.where((s < s_cut) == cut, e.imag, 0.0)
        return num / np.abs(eh + e) ** 2
    tot = d.scatter_rate(mt, lambda q, w: Lcut(q, w, True), 2 * D * (1 + 1e-6), 2 * Lt, 2 * Lt / vg, rho) \
        + d.scatter_rate(mt, lambda q, w: Lcut(q, w, False), 2 * D * (1 + 1e-6), 2 * Lt, 2 * Lt / vg, rho)
    near = d.scatter_rate(mt, lambda q, w: Lcut(q, w, True), 2 * D * (1 + 1e-6), 2 * Lt, 2 * Lt / vg, rho)
    print("  m = %5.0f keV: fraction of the isotropic-model rate with S > 1.5 (sqrt(s) below the cut): %.2f" % (mt / 1e3, near / tot))

# expansion parameter of the one-loop response at long wavelength (Sect. 7.3): g alpha~ ln(Lt/max(Delta, v q)), q -> 0
for Dh, M in ((D, Z), (DP, ZP)):
    vgM = np.prod(M["v"]) ** (1 / 3)
    atM = d.ALPHA / (eh * vgM)
    print("expansion parameter g alpha~ ln(Lt/Delta_D) at Delta_D = %.1f meV (own row, Lt = %.3f eV): %.2f (g alpha~ = %.3f)"
          % (Dh * 1e3, M["Lt"], g * atM * np.log(M["Lt"] / Dh), g * atM))
