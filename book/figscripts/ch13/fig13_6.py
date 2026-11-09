"""Fig. 13.6 (fig:13-offshell) and every number of Sect. 13.6 outside its worked example (log: fig13_6.log).

Panel (a): the (|q|, omega) plane of silicon for q along [100], the valley axis. Curves:
  E_min(q): the cached first-principles grid of Fig. 3.6 (figscripts/ch03/qe_si_pbe.npz: QE 7.6, PBE, SG15, 60 Ry,
            a = 5.431 A, 48^3 grid, no spin-orbit coupling), conduction bands shifted rigidly so that the indirect gap
            equals the measured E_g(0) = 1.17 eV (scissor 0.613 eV, as in Figs. 3.6 and 13.2). Linear interpolation
            between the grid momenta (step 2pi/24a = 95 eV). Because the scissor is fixed to the measured low-temperature
            gap, the edge carries the measured zero-point renormalization of the gap, taken rigid in k (Sect. 13.7).
  E_min(q) - delta_w with the margin delta_w = 0.3 eV;
  E_min^PA(q) = E_g + omega_TA(k_c - q), eq:13.1-EPA, with the book's PBE force constants (figscripts/ch05/si_ifc.py);
            for q beyond the valley the nearest valley is k_c, and beyond |G_200| - k_c = 2.63 keV its Umklapp image;
  the largest energy deposited, q v_max - q^2 / 2 m_chi, for 0.35 and 0.42 MeV.
  Shaded: the off-shell window (between E_min^PA and E_min - delta_w), the margin band (E_min - delta_w to E_min),
  and the open zero-phonon continuum above E_min (Dyson convention of Sect. 8.6).
Panel (b): the controlling ratios against the margin delta_w: omega_max / delta_w (top of the phonon band, the zone-center
optical phonon 64.1 meV, Sect. 6.2), |ZPR_gap| / delta_w (silicon gap, 56.2 meV computed fixed-volume to 73 meV, the
electron-phonon part implied by experiment, Sect. 6.3), Gamma_pair / delta_w (estimate below), E_x^b / delta_w
(14.7 meV, Sect. 4.9); right axis: the largest |q| < k_c along [100] at which the window is not empty.

Pair width estimate (a model estimate, labelled as such in the text): T = 0, spontaneous emission only, deformation-
potential rates with the DFPT constants of Li, Graziosi and Neophytou (2104.08998, Table III) in the form of their
Eq. (10),  1/tau = pi D^2 Z_f / (2 rho omega) * g(E - omega),  with g the density of states of the final valley counting
both spin orientations, g(E) = (2 m_d)^{3/2} E^{1/2} / (2 pi^2 hbar^3) (the reading in which Eq. (10) is the golden
rule for spin-conserving emission; reading g as per spin would halve every optical/intervalley rate below).
  electrons: g-type LO 3.86 eV/A at 61.06 meV (Z_f = 1), f-type LA 1.83 eV/A at 46.67 meV (Z_f = 4), f-type TO
  3.55 eV/A at 56.40 meV (Z_f = 4); m_d = 0.322 m_e (Sect. 6.5); plus intravalley acoustic emission, eq:6.3-cherenkov
  with the constants of Sect. 6.3 (Xi_LA = 4.75 eV, Xi_TA = 3.23 eV, c = 8.43, 5.84 km/s, m* = 0.322 m_e).
  holes: optical deformation potential 10.45 eV/A at 62.08 meV (Z_f = 1), DOS mass m_dv = 0.50 m_e (Sect. 3.3).
The pair at the zero-phonon edge E_min(q) shares the kinetic energy E_min(q) - E_g in proportion to the masses along
the valley axis, electron m_par / (m_par + m_hh) = 0.768, hole 0.232 (parabolic partition, Sect. 3.3, m_par = 0.916,
m_hh[100] = 0.277), and Gamma_pair = Gamma_e + Gamma_h (electron and hole decay independently).
rho_Si = 2329 kg/m^3; Omega = a^3/4; M_cell = 2 x 28.0855 u.
Soft-acoustic bound: on the energy shell inside the window, |Q| >= delta_w / (v^g_max + c_nu); v^g_max is the largest
conduction-band slope on the symmetry lines of Fig. 3.6 (bands 5-8 of the cached path).
Run: python fig13_6.py (about 10 s). Output: tex/figures/ch13/fig13_6.pdf and fig13_6.log.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc                                   # noqa: E402

LOG = open(os.path.join(HERE, "fig13_6.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


HBARC = 1973.269804           # eV A
ME = 510998.95                # eV
U = 931.49410242e6            # eV
VMAX = 794.5 / 299792.458
EG = 1.17
A = 5.431
G1 = 2 * np.pi * HBARC / A    # 2283 eV
KC = 0.85 * G1                # 1.94 keV
KC2 = 2 * G1 - KC             # Umklapp image of the opposite valley along [100], 2.63 keV
MEH = (0.916 + 0.277) * ME    # pair mass along the axis
DW = 0.3                      # eV, margin
WMAX = 0.0641                 # eV, top of the phonon band (zone-center optical, Sect. 6.2)
ZPR = (0.0562, 0.073)         # eV, |gap ZPR|: computed fixed volume ... e-ph part implied by experiment (Sect. 6.3)
EXB = 0.0147                  # eV

# ---------------- E_min(q) along [100] ---------------------------------------------------------------------------
d = np.load(os.path.join(HERE, "..", "ch03", "qe_si_pbe.npz"))
SCIS = 0.613
qg, Eg_grid = d["q[100]"], d["E[100]"] + SCIS
q = np.linspace(0.0, 4000.0, 4001)
Emin = np.interp(q, qg, Eg_grid)
Epar = EG + np.minimum((q - KC) ** 2, (q - KC2) ** 2) / (2 * MEH)


def Qstar(qq):
    """Phonon wavevector (2pi/a) to the nearest valley along [100]."""
    return np.where(qq < 0.5 * (KC + KC2), np.abs(KC - qq), np.abs(qq - KC2)) / G1


QS = Qstar(q)
w, _ = si_ifc.phonons(np.column_stack([QS, 0 * QS, 0 * QS]))
wTA = np.clip(w[:, 0], 0, None) / 1e3
EPA = EG + wTA
out("E_min grid at q = 0.5, 1.0, 1.33 keV: %s eV (parabola %s)" % (
    np.round(np.interp([500, 1000, 1330], q, Emin), 3), np.round(np.interp([500, 1000, 1330], q, Epar), 3)))


def window_edge(Emin_curve, dw, side="low"):
    """Largest |q| < k_c (side low) or smallest |q| > k_c2 (side high) at which E_PA <= E_min - dw."""
    ok = EPA <= Emin_curve - dw
    if side == "low":
        sel = np.where(ok & (q < KC))[0]
        return q[sel.max()] if len(sel) else np.nan
    sel = np.where(ok & (q > KC2))[0]
    return q[sel.min()] if len(sel) else np.nan


for dw in (0.1, 0.2, 0.3, 0.4, 0.5):
    out("delta_w = %.1f eV: window along [100] for |q| <= %.0f eV (grid E_min), %.0f eV (parabola); reopens beyond "
        "%.0f eV (grid), %.0f (parabola)" % (dw, window_edge(Emin, dw), window_edge(Epar, dw),
                                            window_edge(Emin, dw, "high"), window_edge(Epar, dw, "high")))
# 13.3's closed form with a linear branch c = 5.0 km/s
cTA = 5.0e3 / 299792458.0
Qb = MEH * cTA + np.sqrt((MEH * cTA) ** 2 + 2 * MEH * DW)
out("13.3 closed form |Q*| >= M c + (M^2 c^2 + 2 M delta_w)^1/2 = %.0f eV = %.3f 1/A -> |q| <= %.0f eV"
    % (Qb, Qb / HBARC, KC - Qb))
jq = np.argmin(np.abs(q - 1000))
out("at |q| = 1.0 keV: E_PA = %.4f eV, E_min - delta_w = %.4f eV (grid), %.4f (parabola); window width %.3f eV (grid)"
    % (EPA[jq], Emin[jq] - DW, Epar[jq] - DW, Emin[jq] - DW - EPA[jq]))

# ---------------- ratios at delta_w = 0.3 eV --------------------------------------------------------------------
wTA_on = np.interp(896.0, q, wTA)
out("ratios at delta_w = 0.3 eV: omega_max/delta_w = %.3f; omega_TA(Q*) at the onset (%.1f meV)/delta_w = %.3f; "
    "|ZPR|/delta_w = %.2f-%.2f; E_x^b/delta_w = %.3f" % (WMAX / DW, wTA_on * 1e3, wTA_on / DW, ZPR[0] / DW,
                                                        ZPR[1] / DW, EXB / DW))
for dw in (0.1, 0.5):
    out("ratios at delta_w = %.1f eV: omega_max/delta_w = %.3f; |ZPR|/delta_w = %.2f-%.2f; E_x^b/delta_w = %.3f"
        % (dw, WMAX / dw, ZPR[0] / dw, ZPR[1] / dw, EXB / dw))

# ---------------- pair widths (model estimate) -------------------------------------------------------------------
HBAR = 1.054571817e-34
EV = 1.602176634e-19
MEKG = 9.1093837015e-31
RHO = 2329.0


def dos_both(E_eV, md):
    """Density of states per unit volume and energy, both spins, one valley (J^-1 m^-3)."""
    E = np.clip(E_eV, 0, None) * EV
    return (2 * md * MEKG) ** 1.5 * np.sqrt(E) / (2 * np.pi ** 2 * HBAR ** 3)


def rate_opt(E_eV, D_eVA, w_meV, Z, md):
    D = D_eVA * EV / 1e-10
    om = w_meV * 1e-3 * EV / HBAR
    return np.pi * D ** 2 * Z / (2 * RHO * om) * dos_both(np.asarray(E_eV) - w_meV * 1e-3, md)


def gamma_e(E):
    r = (rate_opt(E, 3.86, 61.06, 1, 0.322) + rate_opt(E, 1.83, 46.67, 4, 0.322)
         + rate_opt(E, 3.55, 56.40, 4, 0.322))
    return HBAR * r / EV                                  # eV


def gamma_ac(E):
    """eq:6.3-cherenkov, LA + one TA, spherical valley m* = 0.322, natural units (eV, A)."""
    Om = A ** 3 / 4
    Mc = 2 * 28.0855 * U
    ms = 0.322 * ME
    tot = 0.0
    for Xi, cms in ((4.75, 8.43e3), (3.23, 5.84e3)):
        c = cms / 299792458.0
        k = np.sqrt(2 * ms * E)                            # eV
        Qm = np.clip(2 * (k - ms * c), 0, None)
        G = Om / HBARC ** 3 * Xi ** 2 * ms * Qm ** 3 / (12 * np.pi * Mc * c * k)
        tot = tot + G
    return tot


def gamma_h(E):
    return HBAR * rate_opt(E, 10.45, 62.08, 1, 0.50) / EV


out("check eq:6.3-cherenkov at 10 meV: %.2f micro-eV (Sect. 6.3: 12.3)" % (gamma_ac(0.010) * 1e6))
FE = 0.916 / (0.916 + 0.277)
for qq in (500.0, 1000.0, 1330.0):
    Ek = np.interp(qq, q, Emin) - EG
    Ee, Eh = FE * Ek, (1 - FE) * Ek
    ge, ga, gh = gamma_e(Ee), gamma_ac(Ee), gamma_h(Eh)
    gp = ge + ga + gh
    out("|q| = %.2f keV: E_min - E_g = %.3f eV -> electron %.3f eV (intervalley %.1f meV, acoustic %.2f meV), "
        "hole %.3f eV (optical %.1f meV); Gamma_pair = %.1f meV, Gamma/delta_w = %.3f"
        % (qq / 1e3, Ek, Ee, ge * 1e3, ga * 1e3, Eh, gh * 1e3, gp * 1e3, gp / DW))
# the pair at the window edge sits higher by up to delta_w: width at E_min + 0.3 eV (upper end of the resonant shell)
for qq in (1000.0,):
    Ek = np.interp(qq, q, Emin) - EG + DW
    gp = gamma_e(FE * Ek) + gamma_ac(FE * Ek) + gamma_h((1 - FE) * Ek)
    out("|q| = 1.0 keV, pair %.2f eV above E_min: Gamma_pair = %.1f meV" % (DW, gp * 1e3))
GAM_RANGE = []
for qq in np.linspace(400, 1400, 11):
    Ek = np.interp(qq, q, Emin) - EG
    GAM_RANGE.append(gamma_e(FE * Ek) + gamma_ac(FE * Ek) + gamma_h((1 - FE) * Ek))
GLO, GHI = min(GAM_RANGE), max(GAM_RANGE)
out("Gamma_pair at E_min(q) for 0.4 <= |q| <= 1.4 keV: %.1f to %.1f meV" % (GLO * 1e3, GHI * 1e3))

# ---------------- soft-acoustic bound inside the window ------------------------------------------------------------
xp, bands = d["xp"], d["bands"]
dx = np.diff(xp) * A / (2 * np.pi)                         # A^-1 per path step
vmax = 0.0
for n in range(4, 8):
    dv = np.abs(np.diff(bands[:, n])) / np.where(dx > 1e-9, dx, np.nan)
    vmax = max(vmax, np.nanmax(dv))
out("largest conduction-band slope on the path: %.1f eV A = %.2e m/s" % (vmax, vmax / HBARC * 299792458.0))
for dw in (0.1, 0.3):
    out("  |Q| >= delta_w/(v^g_max + c) = %.3f 1/A at delta_w = %.1f eV" % (dw / (vmax + 0.0329), dw))
for name, m, cms in (("TA, transverse mass 0.191", 0.191, 5.84e3), ("LA, longitudinal mass 0.916", 0.916, 8.43e3)):
    mc = m * ME * cms / 299792458.0
    out("  soft-limit scale near the valley, %s: m* c_nu = %.2f eV = %.1e 1/A" % (name, mc, mc / HBARC))
# deformation against recoil (E.17: D/c ~ 300 keV)
for D, cms in ((9.85, 8.43e3), (8.84, 8.43e3)):
    out("  D/c_nu = %.0f keV for D = %.2f eV, c = %.2f km/s" % (D / (cms / 299792458.0) / 1e3, D, cms / 1e3))

# ---------------- figure ----------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.8, 3.3), gridspec_kw={"wspace": 0.42, "width_ratios": [1.25, 1]})
qk = q / 1e3
top = 2.4
ok = EPA <= Emin - DW
ax.fill_between(qk, EPA, Emin - DW, where=ok, color="#9ad19a", alpha=0.6, lw=0, label="off-shell window")
ax.fill_between(qk, np.maximum(Emin - DW, EPA), Emin, where=Emin > EPA, color="#f2c48d", alpha=0.6, lw=0,
                label=r"margin $\delta_{\mathrm{w}}$")
ax.fill_between(qk, Emin, top, color="0.85", lw=0, label="zero-phonon pairs real")
ax.plot(qk, Emin, color="k", lw=1.1)
ax.plot(qk, Emin - DW, color="k", lw=0.8, ls="--")
ax.plot(qk, EPA, color="C3", lw=1.1)
ax.plot(qk, Epar, color="0.45", lw=0.6, ls=":")
for m, ls in ((0.35e6, "-."), (0.42e6, (0, (1, 1)))):
    qq = np.linspace(1, 4000, 800)
    ax.plot(qq / 1e3, qq * VMAX - qq ** 2 / (2 * m), color="C0", lw=0.8, ls=ls)
    jm = np.argmax(qq * VMAX - qq ** 2 / (2 * m))
    # labels in the green area with thin leaders, clear of the edges and of each other
    xt, yt = (0.18, 1.47) if m == 0.42e6 else (0.08, 1.32)
    ax.annotate("%.2f MeV" % (m / 1e6), xy=(qq[jm] / 1e3, qq[jm] * VMAX - qq[jm] ** 2 / (2 * m)), xytext=(xt, yt),
                fontsize=6.5, va="center", ha="left", color="C0",
                arrowprops=dict(arrowstyle="-", lw=0.5, color="C0", shrinkA=1, shrinkB=1))
qe = window_edge(Emin, DW)
ax.axvline(qe / 1e3, color="0.4", lw=0.5)
ax.text(qe / 1e3 + 0.03, 2.0, "%.2f keV" % (qe / 1e3), fontsize=6.5, color="0.3", va="top")
left = qk < 1.9                               # left branch of the edge, for the label leaders
xa = np.interp(1.82, (Emin[left])[::-1], (qk[left])[::-1])
xb = np.interp(1.60, (Emin[left] - DW)[::-1], (qk[left])[::-1])
ax.annotate(r"$E_{\mathrm{min}}(\mathbf{q})$", xy=(xa, 1.82), xytext=(0.03, 1.88), fontsize=7, va="center",
            arrowprops=dict(arrowstyle="-", lw=0.5, color="k", shrinkA=1, shrinkB=0))
ax.annotate(r"$E_{\mathrm{min}} - \delta_{\mathrm{w}}$", xy=(xb, 1.60), xytext=(0.03, 1.64), fontsize=7, va="center",
            arrowprops=dict(arrowstyle="-", lw=0.5, color="k", shrinkA=1, shrinkB=0))
ax.text(0.03, 1.198, r"$E_{\mathrm{g}} + \omega_{\mathrm{TA}}$", fontsize=7, color="C3", ha="left", va="bottom")
ax.set_xlim(0, 3.6); ax.set_ylim(1.12, top)
ax.set_xlabel(r"$|\mathbf{q}|$ along [100] (keV)"); ax.set_ylabel(r"$\omega$ (eV)")
ax.legend(loc="upper right", fontsize=6.5, frameon=True, framealpha=0.9, handlelength=1.2)
ax.text(0.02, 0.97, "(a)", transform=ax.transAxes, va="top")

dws = np.linspace(0.05, 0.8, 76)
bx.plot(dws, WMAX / dws, color="k", lw=1.0, ls=(0, (4, 2)), zorder=5, label=r"$\omega_{\max}/\delta_{\mathrm{w}}$")
bx.fill_between(dws, ZPR[0] / dws, ZPR[1] / dws, color="C1", alpha=0.35, lw=0,
                label=r"$|\mathrm{ZPR}|/\delta_{\mathrm{w}}$")
bx.fill_between(dws, GLO / dws, GHI / dws, color="C2", alpha=0.5, lw=0, label=r"$\mathit{\Gamma}_{\mathrm{pair}}/\delta_{\mathrm{w}}$")
bx.plot(dws, EXB / dws, color="C4", lw=0.8, ls="--", label=r"$E_x^{\mathrm{b}}/\delta_{\mathrm{w}}$")
bx.axvline(DW, color="0.4", lw=0.6)
bx.set_yscale("log"); bx.set_ylim(5e-3, 2)
bx.set_xlim(0.05, 0.8)
bx.set_xlabel(r"margin $\delta_{\mathrm{w}}$ (eV)"); bx.set_ylabel("ratio")
bx.legend(loc="upper right", fontsize=6.5, frameon=False, handlelength=1.4)
cx = bx.twinx()
qmax = np.array([window_edge(Emin, x) for x in dws])
cx.plot(dws, qmax / 1e3, color="C3", lw=1.0)
cx.set_ylabel(r"largest window $|\mathbf{q}|$ (keV)", color="C3")
cx.tick_params(axis="y", colors="C3")
cx.set_ylim(0.6, 1.9)
bx.text(0.03, 0.92, "(b)", transform=bx.transAxes)
outp = os.path.join(HERE, "..", "..", "tex", "figures", "ch13", "fig13_6.pdf")
fig.savefig(outp, bbox_inches="tight")
out("wrote", os.path.normpath(outp))
LOG.close()
