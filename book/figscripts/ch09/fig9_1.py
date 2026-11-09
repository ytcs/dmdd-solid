"""Fig. 9.1 and the computed entries of Table 9.2 / Sect. 9.2 (the kinematic map).

Output: tex/figures/ch09/fig9_1.pdf and figscripts/ch09/fig9_1.log (every number printed in Sect. 9.2 that no
other section prints is written to the log; numbers quoted from home sections are listed there too, marked
"quoted", so that the figure can be checked against them).

Kinematics (Sect. 1.3, eq:1.3-region): a particle of mass m at speed v deposits at most q v - q^2/(2m) at momentum
transfer q. A channel whose lowest final state above threshold at momentum q has energy E_ch(q) is reachable iff
m >= q^2 / [2 (q v_max - E_ch(q))] for some q with q v_max > E_ch(q). Its minimum mass is the minimum over q.
  flat onset   E_ch = E0                 -> m = 2 E0 / v^2 at q = 2 E0 / v                       (eq:1.3-mmin)
  linear       E_ch = c q, q >= w_th/c   -> m = w_th / [2 c (v - c)] at q = w_th / c           (eq:11.1-edge)
  Dirac pairs  E_ch = sqrt(u^2 q^2 + E0^2), E0 = 2 Delta_D (eq:7.3-edge)                     -> numerical minimum
  free nucleus E = q^2/2M                -> E_R^max = 2 mu^2 v^2 / M (eq:1.3-ERmax), solved for m
  absorption   m_phi = omega (q = m_phi v ~ 1e-3 m_phi; Sect. 1.4, 8.2)
Halo exponent (envelope theorem): d ln m_min / d ln v_max = - q* v / (q* v - E_ch(q*)), with q* the minimizing
momentum, valid when q* is an interior minimum or sits on a v-independent constraint (q* = w_th / c).

Inputs (book values; sections cited):
  v_max = 544 + 250.5 = 794.5 km/s (tab:1-shm, eq:1.2-vmax)
  Si: E_g(0) = 1.1692 eV (Ramanathan Eq. 11; sec:3.3), k_c = 1.94 keV (eq:3.3-kc, we:3-kc), c_LA,max = 9.35 km/s [111]
      (we:5-debye, sec:11.1), c_TA[100] = 5.84 km/s (we:5-debye), rate-weighted 8.956 km/s (we:11-cbar), optical phonon
      64.1 meV (tab:17-endo, sec:5.2), a = 5.431020511 A (CODATA), M = 26.162 GeV (natural Si, sec:11.4),
      <omega> = 40.9 meV, impulse onset x_R = E_R/<omega> = 4 (sec:11.4)
  Ge: E_g = 0.744 eV, |Gamma L| = 1.90 keV (sec:3.3, we:3-mmin), c_LA,max = 5.598 km/s (sec:17.1, a = 5.658 A), 3d centroid 29.4 eV
      (doublet 29.2/29.8; sec:10.6), M = 72.63 u x 0.931494 GeV/u = 67.65 GeV, impulse onset 21.3 MeV (sec:17.1, estimate)
  GaAs: E_g = 1.52 eV (tab:3-materials), L valleys 1.815 eV at |Gamma L| = 1.90 keV (sec:13.1), omega_L = 36.35 meV (we:5-lst)
  Al: 2 Delta = 0.36 meV (we:7-al); fastest longitudinal speed along [111], c_L = [(C11 + 2 C12 + 4 C44)/(3 rho)]^(1/2),
      from the 0 K constants C11, C12, C44 = 114.3, 61.9, 31.6 GPa and the 0 K density 2.73 g/cm^3 (sec:20.3), as the
      Si, Ge and GaAs edges use the fastest direction (eq:11.1-edge); the Voigt speeds 6.63 / 3.30 km/s of sec:20.3 are
      logged for comparison
  ZrTe5: Delta_D = 11.8 meV (half of the computed 23.6 meV gap, measured-structure row), principal velocities
      1.1e-3, 4.5e-4, 1.0e-3 (sec:16.1, Geilhufe et al. 2020 Table 1); isotropic v_D = geometric mean
  NiO: c_M = 1.36e-4 (fastest J1-J2 magnon speed, sec:14.1), omega_th = 5 meV; measured zone-centre magnon 4.54 meV
  Si 2p: binding 99.4 eV below the valence-band maximum (sec:3.5) plus E_g = 1.17 eV; least momentum E/v_max (sec:3.5, 10.6)
  Si phonon-assisted onset (sec:13.1, quoted): q* = 2E/v_max = 883-894 eV leaves the phonon k_c - q* = 1057 eV, where
      omega_TA = 14.79-14.87 meV; a phonon supplying all of k_c (absorption, light) costs 18.27 meV
"""
import os
import numpy as np
from scipy.optimize import minimize_scalar, brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch09", "fig9_1.pdf")
LOG = os.path.join(HERE, "fig9_1.log")
lines = []


def log(s):
    print(s)
    lines.append(s)


C_KMS = 299792.458
V_ESC, V_E = 544.0, 250.5
V_MAX = (V_ESC + V_E) / C_KMS
KEV, MEV, GEV = 1e3, 1e6, 1e9
HBARC = 1973.2698  # eV A
C11_AL, C12_AL, C44_AL, RHO_AL0 = 114.3e9, 61.9e9, 31.6e9, 2730.0   # Pa, kg/m^3 (sec:20.3; 0 K)
C_AL111 = np.sqrt((C11_AL + 2 * C12_AL + 4 * C44_AL) / (3 * RHO_AL0)) / 1e3   # km/s, fastest LA, [111]


def kms(c):
    return c / C_KMS


def m_flat(E0, v=V_MAX):
    return 2 * E0 / v**2


def m_lin(wth, c, v=V_MAX):
    return wth / (2 * c * (v - c))


def m_at_q(q, E, v=V_MAX):
    """mass that deposits E at exactly momentum q (eq:1.3-region inverted)"""
    return q**2 / (2 * (q * v - E))


def m_dirac(E0, u, v=V_MAX):
    """minimum over q of q^2 / [2 (q v - sqrt(u^2 q^2 + E0^2))]; returns (m, q*)"""
    if u >= v:
        return np.inf, np.nan
    qlo = E0 / np.sqrt(v**2 - u**2) * (1 + 1e-12)
    f = lambda lq: np.log(m_at_q(np.exp(lq), np.sqrt(u**2 * np.exp(lq)**2 + E0**2), v))
    # dense grid then bounded refinement (Ch15 lesson: no coarse-grid minima)
    lq = np.linspace(np.log(qlo) + 1e-9, np.log(qlo) + 6, 20001)
    vals = np.array([f(x) for x in lq])
    i = int(np.argmin(vals))
    res = minimize_scalar(f, bounds=(lq[max(i - 2, 0)], lq[min(i + 2, len(lq) - 1)]), method="bounded",
                          options={"xatol": 1e-12})
    return float(np.exp(res.fun)), float(np.exp(res.x))


def kappa_num(fun, v=V_MAX, h=1e-5):
    return -(np.log(fun(v * (1 + h))) - np.log(fun(v * (1 - h)))) / (np.log(1 + h) - np.log(1 - h))


def m_free(E, M, v=V_MAX):
    """lightest m whose largest free recoil 2 mu^2 v^2 / M equals E (eq:1.3-ERmax)"""
    mu = np.sqrt(M * E / 2) / v
    return mu * M / (M - mu)


log("Sect. 9.2 kinematic map; v_max = %.4f km/s = %.6e; v_max^2 = %.4e" % (V_ESC + V_E, V_MAX, V_MAX**2))
log("factor between scattering floor and absorption line 2/v_max^2 = %.4e (%.3f decades)" % (2 / V_MAX**2, np.log10(2 / V_MAX**2)))

# ---------------- flat onsets
log("\n# Flat onsets, m = 2 E0 / v_max^2")
flat = {
    "Si gap E_g(0)=1.1692 eV (floor)": 1.1692,
    "Ge gap 0.744 eV (floor)": 0.744,
    "GaAs gap 1.52 eV (floor)": 1.52,
    "GaAs L valleys 1.815 eV (floor)": 1.815,
    "Ge 3d 29.2+0.744 eV": 29.2 + 0.744,
    "Ge 3d 29.8+0.744 eV": 29.8 + 0.744,
    "ZrTe5 2 Delta_D = 23.6 meV": 0.0236,
    "Al 2 Delta = 0.36 meV": 0.36e-3,
    "GaAs omega_L = 36.35 meV": 0.03635,
    "Si optical 64.1 meV": 0.0641,
    "NiO zone-centre magnon 4.54 meV (gap, flat limit)": 4.54e-3,
    "omega_th = 1 meV (free target / gapless gas)": 1e-3,
}
for k, E in flat.items():
    m = m_flat(E)
    log("  %-48s m = %.5g eV = %.4g keV = %.4g MeV, q* = 2E/v = %.4g eV" % (k, m, m / KEV, m / MEV, 2 * E / V_MAX))

# ---------------- brackets of an offset minimum (indirect gap)
log("\n# Offset minimum: mass that deposits the gap at exactly the valley momentum (upper end of the bracket)")
for name, kc, E in [("Si k_c = 1.94 keV, 1.1692 eV", 1940.0, 1.1692), ("Ge |GL| = 1.898 keV, 0.744 eV (as sec:3.3)", 1898.0, 0.744),
                    ("GaAs L |GL| = 1.90 keV, 1.815 eV", 1900.0, 1.815)]:
    m = m_at_q(kc, E)
    kap = kc * V_MAX / (kc * V_MAX - E)
    log("  %-36s m = %.4f MeV ; q v/(q v - E) there = %.3f" % (name, m / MEV, kap))

# ---------------- linear gapless branches
log("\n# Linear branches, m = w_th / [2 c (v_max - c)]")
lin = [("Si LA [111] 9.35 km/s", kms(9.35), 1e-3), ("Si TA [100] 5.84 km/s", kms(5.84), 1e-3),
       ("Si rate-weighted 8.956 km/s", kms(8.956), 1e-3), ("Ge LA max 5.60 km/s", kms(5.598), 1e-3),
       ("Al LA [111] %.3f km/s (0 K constants, 0 K density)" % C_AL111, kms(C_AL111), 1e-3),
       ("Al LA 6.63 km/s (Voigt, sec:20.3; comparison)", kms(6.63), 1e-3), ("Al TA 3.30 km/s", kms(3.30), 1e-3),
       ("NiO magnon c_M = 1.36e-4", 1.36e-4, 5e-3), ("NiO magnon c_M = 1.36e-4 at 1 meV", 1.36e-4, 1e-3)]
for name, c, wth in lin:
    m = m_lin(wth, c)
    log("  %-36s w_th = %.3g eV: m = %.4g keV ; q* = w_th/c = %.4g eV ; ratio to floor 2w/v^2 = %.3f ; v/4c = %.3f ; kappa = v/(v-c) = %.5f"
        % (name, wth, m / KEV, wth / c, m / m_flat(wth), V_MAX / (4 * c), V_MAX / (V_MAX - c)))

# ---------------- Dirac pairs, ZrTe5
log("\n# Dirac pair continuum, E_ch = sqrt(u^2 q^2 + (2 Delta_D)^2), Delta_D = 11.8 meV")
DD = 0.0118
vels = {"x (1.1e-3)": 1.1e-3, "y (4.5e-4)": 4.5e-4, "z (1.0e-3)": 1.0e-3}
u_iso = (1.1e-3 * 4.5e-4 * 1.0e-3) ** (1 / 3)
vels["isotropic, geometric mean %.4e" % u_iso] = u_iso
for k, u in vels.items():
    m, qs = m_dirac(2 * DD, u)
    E = np.sqrt(u**2 * qs**2 + (2 * DD)**2)
    kap_formula = qs * V_MAX / (qs * V_MAX - E)
    kap = kappa_num(lambda v: m_dirac(2 * DD, u, v)[0])
    log("  axis %-34s u/v_max = %.3f : m = %.4g keV (floor 4 Delta/v^2 = %.4g keV, ratio %.3f) ; q* = %.4g eV ; kappa = %.4f (formula %.4f)"
        % (k, u / V_MAX, m / KEV, m_flat(2 * DD) / KEV, m / m_flat(2 * DD), qs, kap, kap_formula))
log("  quoted (sec:16.1): isotropic 8.0 keV; principal axes 9.6, 7.1, 9.0 keV")
log("  narrow-gap III-V cone v_D = 1.8 v_max (sec:7.3): u >= v_max -> no scattering at any mass: %s" % (m_dirac(1.0, 1.8 * V_MAX)[0]))

# ---------------- free nuclear recoil
log("\n# Free nucleus, E_R^max = 2 mu^2 v^2 / M")
M_SI = 26.162 * GEV
M_GE = 72.63 * 0.931494 * GEV
ER_imp = 4 * 0.0409
m_si = m_free(ER_imp, M_SI)
log("  Si impulse onset E_R = 4 x 40.9 meV = %.4f eV -> m = %.4f MeV ; q = 2 mu v = %.2f keV (quoted 17.5 MeV, 92.5 keV)"
    % (ER_imp, m_si / MEV, 2 * (m_si * M_SI / (m_si + M_SI)) * V_MAX / KEV))
mu = 21.3 * MEV * M_GE / (21.3 * MEV + M_GE)
ER_ge = 2 * mu**2 * V_MAX**2 / M_GE
log("  Ge impulse onset 21.3 MeV (quoted, estimate) -> E_R^max = %.4f eV (M = %.4g GeV)" % (ER_ge, M_GE / GEV))
log("  Si free recoil reaching E_g = 1.17 eV (reduced mass): m = %.2f MeV ; E_g(0) = 1.1692 eV: %.2f MeV ; 1.11 eV: %.2f MeV (sec:1.3)"
    % (m_free(1.17, M_SI) / MEV, m_free(1.1692, M_SI) / MEV, m_free(1.11, M_SI) / MEV))
kap_free = kappa_num(lambda v: m_free(0.1, M_SI, v))
log("  kappa for a free Si nucleus at 0.1 eV = %.4f" % kap_free)

# ---------------- halo dependence
log("\n# Halo dependence of the edges")
for dv in (+25.0, -25.0):
    v = (V_ESC + dv + V_E) / C_KMS
    log("  v_esc %+g km/s: v_max %+.3f %% ; flat edge %+.2f %% ; Si acoustic %+.2f %% ; ZrTe5 iso %+.2f %% ; free Si nucleus %+.2f %%"
        % (dv, 100 * (v / V_MAX - 1), 100 * (m_flat(1, v) / m_flat(1) - 1), 100 * (m_lin(1e-3, kms(9.35), v) / m_lin(1e-3, kms(9.35)) - 1),
           100 * (m_dirac(2 * DD, u_iso, v)[0] / m_dirac(2 * DD, u_iso)[0] - 1), 100 * (m_free(0.1, M_SI, v) / m_free(0.1, M_SI) - 1)))
for name, vm in (("June 544 + 266.4 = 810.4 km/s", 810.4), ("December 544 + 237.4 = 781.4 km/s", 781.4)):  # Earth speeds of fig:1-eta
    v = vm / C_KMS
    log("  %s: flat %+.2f %% ; Si acoustic %+.2f %%" % (name, 100 * (m_flat(1, v) / m_flat(1) - 1),
                                                      100 * (m_lin(1e-3, kms(9.35), v) / m_lin(1e-3, kms(9.35)) - 1)))

# ---------------- worked example 9.2
log("\n# Worked example 9.2: Si acoustic edge at 1 meV")
c = kms(9.35)
a_si = 5.431020511
two_pi_a = 2 * np.pi * HBARC / a_si
log("  c = %.5e ; q* = %.3f eV ; v_max - c = %.5e ; m = %.4f keV ; floor %.2f eV ; ratio %.3f"
    % (c, 1e-3 / c, V_MAX - c, m_lin(1e-3, c) / KEV, m_flat(1e-3), m_lin(1e-3, c) / m_flat(1e-3)))
log("  2 pi/a = %.4f keV ; q*/(2 pi/a) = %.4f" % (two_pi_a / KEV, (1e-3 / c) / two_pi_a))
m6 = m_lin(1e-3, c)
log("  at m = m_ac: largest deposit (1/2) m v^2 = %.3f meV at q = m v = %.3f eV ; phonon there c q = %.3f meV"
    % (0.5 * m6 * V_MAX**2 * 1e3, m6 * V_MAX, c * m6 * V_MAX * 1e3))
log("  phonon emitted at the edge carries q* = 2 m (v_max - c), i.e. backscatter: 2 m (v-c) = %.3f eV" % (2 * m6 * (V_MAX - c)))
for th in (0.1e-3, 10e-3):
    log("  w_th = %.2g meV: Si edge %.4g keV" % (th * 1e3, m_lin(th, c) / KEV))

open(LOG, "w").write("\n".join(lines) + "\n")

# linearized halo shifts printed in the text
dlv = 25.0 / (V_ESC + V_E)
log("\n# Linearized shifts for v_esc +-25 km/s (delta ln v_max = %.4f): flat %.2f %%, Si acoustic %.2f %%, ZrTe5 iso %.2f %%, free nucleus %.2f %%"
    % (dlv, 200 * dlv, 100 * V_MAX / (V_MAX - kms(9.35)) * dlv,
       100 * kappa_num(lambda v: m_dirac(2 * DD, u_iso, v)[0]) * dlv, 100 * kap_free * dlv))
E2P = 99.4 + 1.17
log("\n# Si 2p: E0 = 99.4 + 1.17 = %.2f eV ; least momentum E0/v_max = %.2f keV ; floor 2 E0/v_max^2 = 2 (E0/v_max)/v_max = %.2f MeV" % (E2P, E2P / V_MAX / KEV, m_flat(E2P) / MEV))
msi = m_lin(1e-3, kms(9.35))
mzr = m_dirac(2 * DD, 4.5e-4)[0]
log("\n# Equivalent Si acoustic thresholds: GaAs LO edge 10.35 keV <-> %.2f meV ; ZrTe5 slow axis %.3f keV <-> %.3f meV ; NiO 7.31 keV <-> %.2f meV ; Al pairs 0.1025 keV / Si acoustic 1 meV = 1/%.1f"
    % (m_flat(0.03635) / msi, mzr / KEV, mzr / msi, m_lin(5e-3, 1.36e-4) / msi, msi / m_flat(0.36e-3)))
mg, qg = m_dirac(4.54e-3, 1.36e-4)
log("# NiO gapped magnon, E = (c_M^2 q^2 + (4.54 meV)^2)^(1/2): edge %.4f keV (flat value %.4f keV, ratio %.4f)" % (mg / KEV, m_flat(4.54e-3) / KEV, mg / m_flat(4.54e-3)))
log("# NiO c_M / c_LA,max(Si) = %.2f" % (1.36e-4 / kms(9.35)))
log("# Floor at 1 meV (random-site couplings, sec:11.6; two magnons, sec:14.2): %.4f keV ; Si acoustic / floor = %.1f ; NiO one magnon at 1 meV / floor = %.2f"
    % (m_flat(1e-3) / KEV, msi / m_flat(1e-3), m_lin(1e-3, 1.36e-4) / m_flat(1e-3)))
log("# Al [111] speed from the 0 K constants and density: %.3f km/s ; edge at 1 meV %.4f keV" % (C_AL111, m_lin(1e-3, kms(C_AL111)) / KEV))
for Eb in (1.1692, 1.17):
    log("# Si phonon-assisted onset: q* = 2 E/v_max at E = %.4f eV: %.0f eV ; k_c - q* = %.0f eV (sec:13.1 quotes 1057 eV and 14.79-14.87 meV TA; 18.27 meV for all of k_c)" % (Eb, 2 * Eb / V_MAX, 1940 - 2 * Eb / V_MAX))
open(LOG, "w").write("\n".join(lines) + "\n")

# ================= figure =================
import matplotlib.gridspec as gridspec
FS = 7
fig = plt.figure(figsize=(5.0, 5.9))
gs = gridspec.GridSpec(2, 1, height_ratios=[3.9, 1.7], hspace=0.30, left=0.13, right=0.88, top=0.985, bottom=0.075)
ax = fig.add_subplot(gs[0])
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(1e-7, 2e2); ax.set_ylim(1e-7, 1e10)


def rot(x1, x2, f):
    p1 = ax.transData.transform((x1, f(x1))); p2 = ax.transData.transform((x2, f(x2)))
    return np.degrees(np.arctan2(p2[1] - p1[1], p2[0] - p1[0]))


w = np.logspace(-7, 2.4, 400)
ax.plot(w, w, color="k", lw=1.3)
ax.plot(w, m_flat(w), color="k", lw=1.0, ls="--")
r1 = rot(1e-6, 1e-5, lambda x: x)
ax.text(3e-7, 3e-7 * 6, r"absorption, $m_\phi = \omega$", rotation=r1, fontsize=FS, va="bottom", rotation_mode="anchor")
ax.text(3e-7, m_flat(3e-7) * 6, r"flat onset, $2\omega_{\mathrm{th}}/v_{\mathrm{max}}^2$", rotation=r1, fontsize=FS,
        va="bottom", rotation_mode="anchor")
wl = np.logspace(-4, -2, 50)
for cc, col in ((9.35, "C0"), (C_AL111, "C2"), (5.598, "C1")):
    ax.plot(wl, m_lin(wl, kms(cc)), color=col, lw=1.0)
ax.text(1.1e-4, m_lin(1.1e-4, kms(5.598)) * 5, "acoustic phonons", fontsize=FS - 0.5, rotation=r1, rotation_mode="anchor")
wm = np.logspace(-3, np.log10(0.03), 50)
ax.plot(wm, m_lin(wm, 1.36e-4), color="C4", lw=1.0)
wn = np.logspace(-2, 2.4, 200)
ax.plot(wn, m_free(wn, M_SI), color="0.35", lw=1.0, ls="-.")
ax.plot(wn, m_free(wn, M_GE), color="0.35", lw=1.0, ls=":")
r2 = rot(1.0, 10.0, lambda x: m_free(x, M_SI))
ax.text(0.012, m_free(0.012, M_GE) * 3.0, "free nucleus (Si, Ge)", fontsize=FS - 0.5, color="0.3", rotation=r2, rotation_mode="anchor")


def pt(a, x, y, col, filled=True, mk="o", ms=4.0):
    a.plot([x], [y], marker=mk, ms=ms, color=col, mfc=col if filled else "white", mew=1.0, ls="none", zorder=5)


def lab(a, x, y, s, col="k", ha="left", va="center"):
    a.text(x, y, s, color=col, fontsize=FS - 0.8, ha=ha, va=va)


# scattering edges, panel (a)
pt(ax, 0.36e-3, m_flat(0.36e-3), "C2"); lab(ax, 0.55e-3, m_flat(0.36e-3), "Al, pairs", "C2")
pt(ax, 1e-3, m_lin(1e-3, kms(9.35)), "C0"); pt(ax, 1e-3, m_lin(1e-3, kms(C_AL111)), "C2"); pt(ax, 1e-3, m_lin(1e-3, kms(5.598)), "C1")
pt(ax, 5e-3, m_lin(5e-3, 1.36e-4), "C4"); lab(ax, 0.033, 5.5e4, "NiO magnon", "C4", va="bottom")
pt(ax, 0.0236, 8.0e3, "C5", mk="D")
ax.plot([0.0236] * 2, [7.1e3, 9.6e3], color="C5", lw=2.0)
lab(ax, 0.02, 3.5e3, "ZrTe$_5$", "C5", ha="right", va="top")
pt(ax, 0.03635, m_flat(0.03635), "C3", mk="s"); lab(ax, 0.033, 3.5e3, "GaAs LO", "C3", va="top")
pt(ax, 0.0641, m_flat(0.0641), "C0", filled=False)
lab(ax, 0.09, 1.2e4, "Si optical", "C0", va="top")
# electronic and core edges (detail in panel b)
for x, y, col, mk in ((1.1692, 0.3332e6, "C0", "o"), (0.744, 0.2119e6, "C1", "o"), (1.52, 0.433e6, "C3", "s")):
    pt(ax, x, y, col, mk=mk)
lab(ax, 2.3, 1.6e5, "Ge, Si, GaAs\npairs (b)", "0.2", ha="left", va="center")
pt(ax, 29.944, 8.6e6, "C1", mk="v"); lab(ax, 40.0, 4.0e6, "Ge $3d$", "C1", va="top")
pt(ax, ER_imp, m_si, "0.3", mk="*", ms=6); lab(ax, 0.035, 5e6, "Si impulse onset", "0.3", ha="left", va="top")
pt(ax, ER_ge, 21.3e6, "0.3", filled=False, mk="*", ms=6)
# absorption edges on m = omega
for x, col, mk in ((0.36e-3, "C2", "o"), (1.1e-3, "C4", "o"), (0.0236, "C5", "D"), (0.03635, "C3", "s"),
                   (0.744, "C1", "o"), (1.1728, "C0", "o"), (1.52, "C3", "s")):
    pt(ax, x, x, col, mk=mk)
lab(ax, 0.36e-3, 0.36e-3 / 12, "Al", "C2", ha="center", va="top")
lab(ax, 1.1e-3 * 1.5, 1.1e-3 / 1.3, "MnF$_2$", "C4", va="top")
lab(ax, 0.03, 0.03 / 15, "ZrTe$_5$, GaAs LO", "0.3", ha="center", va="top")
lab(ax, 1.0, 1.0 / 15, "Ge, Si, GaAs", "0.3", ha="center", va="top")
ax.plot([2e-6, 1e-3], [2e-6, 1e-3], color="C4", lw=3.5, alpha=0.35, solid_capstyle="butt")
lab(ax, 2e-6 * 1.8, 2e-6 / 8, "magnets in a field", "C4", va="top")
ax.set_xlabel(r"threshold or deposited energy $\omega_{\mathrm{th}}$ (eV)", fontsize=FS + 1)
ax.set_ylabel(r"lightest mass (eV)", fontsize=FS + 1)
sec = ax.secondary_yaxis("right")
sec.set_yticks([1e3, 1e6, 1e9]); sec.set_yticklabels(["keV", "MeV", "GeV"]); sec.tick_params(labelsize=FS)
ax.tick_params(labelsize=FS)
ax.grid(True, which="major", color="0.92", lw=0.5)
ax.text(0.02, 0.98, "(a)", transform=ax.transAxes, fontsize=FS + 1, va="top")

# panel (b): electron-hole pairs, linear axes
bx = fig.add_subplot(gs[1])
E = np.linspace(0.6, 2.0, 50)
bx.plot(E, m_flat(E) / MEV, color="k", lw=1.0, ls="--")
# brackets: floor to the mass that deposits the gap exactly at the valley (thin vertical line)
for x, y0, y1, col in ((1.1692, 0.333, 0.474, "C0"), (0.744, 0.212, 0.420, "C1"), (1.815, 0.517, 0.560, "C3")):
    bx.plot([x, x], [y0, y1], color=col, lw=0.8, alpha=0.6)
    bx.plot([x - 0.015, x + 0.015], [y1, y1], color=col, lw=0.8, alpha=0.6)
pt(bx, 1.1692, 0.3332, "C0"); pt(bx, 1.1692, 0.3374, "C0")
bx.plot([1.1692] * 2, [0.405, 0.408], color="C0", lw=3.0); pt(bx, 1.1692, 0.4065, "C0", mk="^")
lab(bx, 1.20, 0.336, "phonon-assisted onset", "C0")
lab(bx, 1.20, 0.4065, "zero-phonon edge", "C0")
lab(bx, 1.20, 0.474, "Si", "C0")
bx.plot([0.744] * 2, [0.2119, 0.2141], color="C1", lw=3.0); pt(bx, 0.744, 0.213, "C1")
pt(bx, 0.744, 0.32, "C1", filled=False, mk="^")
lab(bx, 0.775, 0.32, "zero-phonon estimate", "C1")
lab(bx, 0.775, 0.42, "Ge", "C1")
bx.plot([1.52] * 2, [0.433, 0.436], color="C3", lw=3.0); pt(bx, 1.52, 0.4345, "C3", mk="s")
bx.plot([1.815] * 2, [0.517, 0.560], color="C3", lw=3.0)
lab(bx, 1.55, 0.405, "GaAs", "C3", va="top")
lab(bx, 1.79, 0.538, "L valleys", "C3", ha="right")
bx.set_xlim(0.6, 2.05); bx.set_ylim(0.15, 0.62)
bx.set_xlabel(r"pair energy at the edge (eV)", fontsize=FS + 1)
bx.set_ylabel(r"lightest mass (MeV)", fontsize=FS + 1)
bx.tick_params(labelsize=FS)
bx.text(0.02, 0.95, "(b)", transform=bx.transAxes, fontsize=FS + 1, va="top")
fig.savefig(OUT)
print("wrote", OUT)
