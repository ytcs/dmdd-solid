"""The screening correction of the silicon rate estimate (Sect. 13.9), rebuilt from the pieces that Sect. 13.4 derives,
and the spread of the cold absorption data that the estimate is normalized to (Sects. 13.8, 13.9).  Log: interim13.log.

WHAT IS BEING SIZED
  The estimate of Sect. 13.9 writes the screened phonon-assisted loss function at finite q as
      L_est(q, w) = eps2_opt(w) * F(q) / eps1_model(q, w)^2 ,
  with eps2_opt(w) a MEASURED cold optical edge (q -> 0), F(q) a computed form factor of the zero-phonon vertex, and
  eps1_model a model dielectric function.  The measured eps2 already contains, at q -> 0, the screening effects of the
  amplitude (Sect. 13.4): the local-field wings of the vertex and the pair channel.  It does NOT contain the external
  factor (photon absorption measures eps2, with no 1/|eps|^2); that factor is calibrated at q -> 0 only because
  eps1_model is pinned to the measured eps1(omega).  The true loss function
  (eq:13.4-Lscr) is
      L(q, w) = eps2_PA(q, w) / eps1_0(q, w)^2 ,   eps2_PA ~ |M[rho_LF] + pair term|^2 .
  Write the vertex with local fields as M[rho](1 + w(q)) and the amplitude with the pair channel as M[rho_LF](1 + r(q)).
  Then, apart from the form-factor item (F(q) against the true independent-particle fall-off, budgeted separately),
      L / L_est = K_ext(q, w) * K_wing(q) * K_pair(q) ,
      K_ext  = [eps1_model(q, w) / eps1_0(q, w)]^2         (external macroscopic factor; contains the macroscopic local fields)
      K_wing = |1 + w(q)|^2 / |1 + w(0)|^2                   (local-field wings of the vertex beyond the calibration)
      K_pair = |1 + r(q)|^2 / |1 + r(0)|^2                   (pair channel beyond the calibration)
  The product is the "screening correction relative to the optical calibration".  It replaces the factor [0.4, 1.8]
  whose inputs (pair channel within +-50 %, unsigned local fields within +-20 %) Sect. 13.4 contradicts.

INPUTS (each with its source)
  I1. RPA dielectric function of silicon with and without local fields, Knapen, Kozaczuk and Lin, arXiv:2101.08275,
      Sect. III B (GPAW), files of the DarkELF package (arXiv:2104.12786), cached in eps13_4.npz (see we13_4.py).  Each mesh
      momentum is one vector q + G, so each mesh point is one direction; ranges are quoted over mesh points.
  I2. Measured eps1 of silicon at 1.20 eV: n_r = 3.565, eps1 = 12.706 (Franta et al. 2017, 300 K; fig13_8.log, WE 13.8).
  I3. The estimate's model eps1 (Cappellini et al., PRB 47, 9892 (1993), the form used by the estimate):
         eps1_model(q, w) = 1 + 1 / [1/(eps0(w) - 1) + alpha_C (q/k_TF)^2 + q^4/(4 w_p^2)]   (atomic units, q in 1/bohr),
         eps0(w) = n(w)^2, n(w) = 3.55 + 0.37 (w - 1.17 eV), alpha_C = 1.563, k_TF = 1.104 1/bohr, w_p = 0.610 Ha.
      At q -> 0 it equals the measured eps1(w); at finite q it is not calibrated by any measurement.
  I4. Window of Sect. 13.6: |q| from the onset momentum 0.90 keV to the window end 1.33 keV (parabolic) on the valley axis;
      omega from the onset 1.184 eV to the window edge 1.47 eV at 1 keV (WE 13.3, fig13_6.log).
  I5. Pair momentum pinned at k_c = 1.94 keV (Sect. 13.4); mesh points 1.87-2.03 keV of I1.  omega_f = omega - omega_TA:
      omega_TA(Q*) = 14.8 meV at finite q (WE 13.1), omega_TA(k_c) = 18.27 meV at q -> 0 (Sect. 6.5).
  I6. Cold absorption of silicon, two datasets:
      S: fit of Stanford et al. to their data at 0.5, 5, 77, 295 K, arXiv:2010.15844 Eqs. (4)-(7), evaluated at 0.5 K:
         alpha = sum_nu C_nu c0 (w - E_g1 - w_nu)^2, c0 = 325 eV^-2 cm^-1, E_g1 = 1.134 eV, C_TA = 5.5, C_TO = 4.0,
         w_TA = 18.27, w_TO = 57.73 meV (as fig13_8.py; lowest measured photon energy 1.205 eV).
      M: Macfarlane et al. 1958, 20 K, as digitized for the estimate: (alpha hbar w)^(1/2) = 0.65 + 78 (w - 1.212 eV)
         (eV/cm)^(1/2) above 1.212 eV, a linear ramp from 1.160 eV below (the form in the estimate's rate code).
      n_r(w) = 3.55 + 0.37 (w - 1.17 eV) converts alpha to eps2 = n_r alpha hbar c / w.
  I7. Rate model of the estimate (Sect. 13.9): S(q, w) = q^2 L_est / (2 pi alpha); F(q) and the angular quantiles of
      E_min(q) from the PBE bands (tables of the estimate, rate_in.json); off-shell window delta_w = 0.3 eV; halo of
      Table 1.1 (v0 = 238, v_esc = 544, v_E = 250.5 km/s); rho_chi = 0.3 GeV/cm^3; 1 kg yr, three events, every event
      with at least one electron.  Rerun here with both datasets of I6 (reproduces the published central values with M).
  I8. Zero-phonon to phonon-assisted ratios of Sect. 13.9 (0.020, 0.16, 0.34 at 14.7, 50, 100 meV above the first edge;
      the mass table 0.023, 0.24/0.56, 1.19/2.14, 2.64/3.85 at 0.41-0.44 MeV, fig13_9.py) were computed with dataset M at
      omega = E_0 + eps, E_0 = 1.3546 eV.  Changing the dataset multiplies each ratio by alpha_M/alpha_S at that omega.

ASSUMPTIONS (each stated; the log prints the consequence)
  A1. The true eps1_0 at the window momenta lies between the RPA value with local fields (I1) and that value scaled by the
      RPA deficit at q -> 0 and the same omega (measured / RPA with local fields), i.e. the deficit at finite q is neither
      negative nor larger than at q -> 0.  The deficit is the electron-hole attraction missing from the RPA kernel.
  A2. The local-field wings change |vertex|^2 at each momentum by no more than the macroscopic local fields change
      1/eps1^2 there (head -> macroscopic, from I1), with either sign, independently at q and at q -> 0.
  A3. The pair channel: in BOTH solvable limits of Sect. 13.4 (source ~ applied potential; rigid translation) K_pair is
      computed below.  Between the limits the pair ratio r(q) is not derived; if r(q) and r(0) are only assumed to lie
      between the limits, independently, K_pair spans [(1/eps_pair)^2, (1/eps_pair)^-2] (printed, not adopted).
  A4. Combination: the sized factors are combined as a product of independent ranges (envelope, not quadrature).

Run: python interim13.py   (numpy; about 1 min).  Output: interim13.log.
"""
import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LOGF = open(os.path.join(HERE, "interim13.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOGF.write(s + "\n")


HBARC = 1973.269804           # eV A
BOHR = 0.529177               # A
d = np.load(os.path.join(HERE, "eps13_4.npz"))
OM, KQ = d["omega"], d["q"]
E1N, E1L = d["e1n"], d["e1l"]


def at(e, j, w):
    return float(np.interp(w, OM, e[:, j]))


def eps_model(q_eV, w):
    """Cappellini et al. model as used by the estimate (I3)."""
    n = 3.55 + 0.37 * (w - 1.17)
    e0 = n * n
    qb = q_eV / HBARC * BOHR
    return 1.0 + 1.0 / (1.0 / (e0 - 1.0) + 1.563 * (qb / 1.104) ** 2 + qb ** 4 / (4 * 0.610 ** 2))


out("=" * 100)
out("A. SCREENING CORRECTION RELATIVE TO THE OPTICAL CALIBRATION (Sects. 13.4, 13.9)")
out("=" * 100)
EPS_MEAS = 12.706             # I2, eps1 at 1.20 eV
W0 = 1.20
e_n0, e_l0 = at(E1N, 0, W0), at(E1L, 0, W0)
s0 = EPS_MEAS / e_l0
out("q -> 0, omega = %.2f eV: RPA eps1 head %.3f, macroscopic %.3f; measured %.3f; deficit factor (A1) s0 = %.3f"
    % (W0, e_n0, e_l0, EPS_MEAS, s0))
out("   macroscopic local-field change of 1/eps1^2 at q -> 0: (head/mac)^2 = %.3f" % ((e_n0 / e_l0) ** 2))
out("   model eps1 at q -> 0: %.3f (pinned to the measured eps1(omega) by construction)" % eps_model(1e-6, W0))

js = np.where((KQ >= 900.0) & (KQ <= 1330.0))[0]
out("\nwindow momenta (I4): mesh points |q| = %s eV" % ", ".join("%.0f" % KQ[j] for j in js))
kext_lo, kext_hi, lf_max = [], [], []
for w in (1.184, 1.20, 1.47):
    for j in js:
        q = KQ[j]
        a, b, m = at(E1N, j, w), at(E1L, j, w), eps_model(q, w)
        klo, khi = (m / (s0 * b)) ** 2, (m / b) ** 2
        kext_lo.append(klo); kext_hi.append(khi); lf_max.append((a / b) ** 2)
        out("  omega %.3f, |q| %4.0f: eps1 head %.3f mac %.3f model %.3f | (head/mac)^2 %.3f | K_ext = (model/eps0)^2 in [%.3f, %.3f]"
            % (w, q, a, b, m, (a / b) ** 2, klo, khi))
jk = np.where((KQ >= 900.0) & (KQ <= 1100.0))[0]
out("  at |q| = 1 keV (mesh %s), omega 1.20 eV: model eps1 %s; RPA mac %s; head %s"
    % (", ".join("%.0f" % KQ[j] for j in jk), " ".join("%.2f" % eps_model(KQ[j], W0) for j in jk),
       " ".join("%.2f" % at(E1L, j, W0) for j in jk), " ".join("%.2f" % at(E1N, j, W0) for j in jk)))
k1lo = min((eps_model(KQ[j], W0) / (s0 * at(E1L, j, W0))) ** 2 for j in jk)
k1hi = max((eps_model(KQ[j], W0) / at(E1L, j, W0)) ** 2 for j in jk)
out("  K_ext at 1 keV, 1.20 eV: [%.2f, %.2f]" % (k1lo, k1hi))
KE_LO, KE_HI = min(kext_lo), max(kext_hi)
out("K_ext over the window (A1): [%.2f, %.2f]   (the macroscopic local fields, +25 to +31 %% at 1 keV, are inside it)"
    % (KE_LO, KE_HI))

# A2: local-field wings
LF_Q = max(lf_max) - 1.0
LF_0 = (e_n0 / e_l0) ** 2 - 1.0
KW_LO, KW_HI = (1 - LF_Q) / (1 + LF_0), (1 + LF_Q) / (1 - LF_0)
out("\nK_wing (A2): |delta_wing(q)| <= %.3f (largest head->mac change of 1/eps1^2 over the window), "
    "|delta_wing(0)| <= %.3f  ->  K_wing in [%.2f, %.2f]" % (LF_Q, LF_0, KW_LO, KW_HI))

# A3: pair channel
jp = np.where((KQ >= 1850.0) & (KQ <= 2050.0))[0]
out("\npair channel at the pinned momentum (I5): mesh %s eV" % ", ".join("%.0f" % KQ[j] for j in jp))
wta_q, wta_0 = 0.0148, 0.01827
devs = []
for w in (1.184, 1.20, 1.30, 1.47):
    for e, lab in ((E1N, "head"), (E1L, "mac")):
        for j in jp:
            r_q = at(e, j, w - wta_q)
            r_0 = at(e, j, w - wta_0)
            kp = (r_0 / r_q) ** 2           # [1/eps(w_f,q)]^2 / [1/eps(w_f,0)]^2
            devs.append(abs(kp - 1))
out("  applied-potential limit: K_pair = [eps1(k_c, w - w_TA(k_c)) / eps1(k_c, w - w_TA(Q*))]^2; "
    "largest |K_pair - 1| over omega 1.184-1.47 eV and the mesh: %.1e" % max(devs))
ep_lo = min(min(at(E1N, j, W0), at(E1L, j, W0)) for j in jp)
ep_hi = max(max(at(E1N, j, W0), at(E1L, j, W0)) for j in jp)
out("  (the factor itself, 1/eps1(k_c)^2 = %.3f-%.3f, is the same at q and at q -> 0 and is absorbed by the calibration)"
    % (1 / ep_hi ** 2, 1 / ep_lo ** 2))
out("  rigid-translation limit: pair channel changes the rate by <= 2e-3 at each momentum (we13_4.log) -> |K_pair - 1| <= 4e-3")
out("  between the limits (A3, not adopted): |1+r|^2 in [1/eps1^2, 1] over the mesh (max eps1 = %.2f) -> K_pair in [%.3f, %.1f]"
    % (ep_hi, 1 / ep_hi ** 2, ep_hi ** 2))
out("  pinning holds exactly at the onset only: above it the pair momenta spread by ~0.2 keV around k_c, where eps1(k_c)")
for e, lab in ((E1N, "head"), (E1L, "mac")):
    jj = np.where((KQ >= 1600.0) & (KQ <= 2150.0))[0]
    out("    %s eps1(1.18 eV) at |q| = %s eV: %s" % (lab, " ".join("%.0f" % KQ[j] for j in jj),
                                                      " ".join("%.2f" % at(e, j, 1.18) for j in jj)))
out("  -> 1/eps1^2 varies pair by pair; it cancels between q and q -> 0 only as far as the final-pair distributions match:"
    " an unsized residual of K_pair")

S_LO, S_HI = KE_LO * KW_LO, KE_HI * KW_HI
out("\nRESULT (A4): sized screening correction K_ext * K_wing in [%.2f, %.2f]; geometric centre %.2f;"
    % (S_LO, S_HI, np.sqrt(S_LO * S_HI)))
out("  K_pair = 1 to 4e-3 in both solvable limits; between them unsized (an open nuisance, not part of the range).")
out("  Old factor [0.4, 1.8] (pair +-0.5, LF +-0.2, omega +-2 %%): 0.98*0.8*0.5 = %.3f, 1.02*1.2*1.5 = %.3f"
    % (0.98 * 0.8 * 0.5, 1.02 * 1.2 * 1.5))

# ------------------------------------------------------------------------------------------------ B. data spread
out("\n" + "=" * 100)
out("B. COLD ABSORPTION DATA: STANFORD ET AL. (0.5 K FIT) AGAINST MACFARLANE ET AL. (20 K) (Sects. 13.8, 13.9)")
out("=" * 100)
HBARC_CM = 1.97327e-5
W_TA, W_TO = 0.01827, 0.05773


def alpha_S(w):
    w = np.asarray(w, float)
    return (5.5 * 325.0 * np.maximum(w - 1.134 - W_TA, 0) ** 2 + 4.0 * 325.0 * np.maximum(w - 1.134 - W_TO, 0) ** 2)


def alpha_M(w):
    w = np.asarray(w, float)
    y = np.where(w > 1.212, 0.65 + 78 * (w - 1.212), np.clip(0.65 * (w - 1.160) / 0.052, 0, None))
    return y ** 2 / w


def n_ref(w):
    return 3.55 + 0.37 * (w - 1.17)


for w in (1.20, 1.21, 1.25, 1.30, 1.3546 + 0.0147, 1.37, 1.40, 1.3546 + 0.05, 1.3546 + 0.066, 1.3546 + 0.10,
          1.3546 + 0.115, 1.3546 + 0.161):
    aS, aM = float(alpha_S(w)), float(alpha_M(w))
    out("  omega %.4f eV: alpha_S %.3g, alpha_M %.3g cm^-1; S/M = %.3f; eps2_S %.3e, eps2_M %.3e"
        % (w, aS, aM, aS / aM if aM > 0 else np.inf, n_ref(w) * aS * HBARC_CM / w, n_ref(w) * aM * HBARC_CM / w))
out("  ratio rescaling for the zero-phonon/phonon-assisted ratios of I8 (multiply by alpha_M/alpha_S):")
for eps, rr in ((0.0147, 0.020), (0.05, 0.16), (0.10, 0.34)):
    w = 1.3546 + eps
    out("    %.1f meV above the first edge: %.3f -> %.3f (factor %.3f)" % (eps * 1e3, rr, rr * alpha_M(w) / alpha_S(w),
                                                                        alpha_M(w) / alpha_S(w)))
for m, eps, rc, rl in ((0.41, 0.015, 0.023, 0.023), (0.42, 0.066, 0.24, 0.56), (0.43, 0.115, 1.19, 2.14),
                       (0.44, 0.161, 2.64, 3.85)):
    f = float(alpha_M(1.3546 + eps) / alpha_S(1.3546 + eps))
    out("    %.2f MeV (eps %.3f eV): factor %.3f; ratios %.3g/%.3g -> %.3g/%.3g" % (m, eps, f, rc, rl, rc * f, rl * f))

# rate model of the estimate, rerun with both datasets
RIN = "/home/user/dmdd-solid/code/COMP-PAER/out/rate_in.json"
D = json.load(open(RIN))
qF, Fc = np.array(D["qF"]), np.array(D["F"])
qE, Edirs = np.array(D["qE"]), np.array(D["Emin_dirs"])
Esort = np.sort(Edirs, axis=1)
C = 299792.458


def make_eta(v0=238., vesc=544., vE=250.5, n=4000):
    v = np.linspace(0, (vesc + vE), n)[1:]
    c = np.linspace(-1, 1, 801)
    V, CC = np.meshgrid(v, c, indexing="ij")
    wgt = np.exp(-(V ** 2 + vE ** 2 + 2 * V * vE * CC) / v0 ** 2) * ((V ** 2 + vE ** 2 + 2 * V * vE * CC) < vesc ** 2)
    Fv = 2 * np.pi * V[:, 0] ** 2 * np.trapezoid(wgt, c, axis=1)
    Fv /= np.trapezoid(Fv, v)
    integ = Fv / v
    cum = np.concatenate([[0], np.cumsum(0.5 * (integ[1:] + integ[:-1]) * np.diff(v))])
    eta_tab = (cum[-1] - cum) * C
    return (lambda u: np.interp(u, v / C, eta_tab, right=0.0)), (vesc + vE) / C


eta, vmax = make_eta()
ALPHA = 1 / 137.035999
ME = 510998.95
A2EV = 1973.27
rho_chi = 0.3e9 * HBARC_CM ** 3
rho_T = 2.329 * 5.60959e32 * HBARC_CM ** 3
CM2 = 1 / HBARC_CM ** 2
KGYR = 5.60959e35 * 3.15576e7 / 6.58212e-16


def fwin(qA, w, d0=0.3):
    i = min(max(np.searchsorted(qE, qA), 1), len(qE) - 1)
    t = (qA - qE[i - 1]) / (qE[i] - qE[i - 1])
    Em = (1 - t) * Esort[i - 1] + t * Esort[i]
    return np.mean(w <= Em - d0)


def rate(m, alpha_fn, light=False, d0=0.3):
    mu = m * ME / (m + ME)
    wgrid = np.arange(1.161, 1.62, 0.004)
    qA = np.linspace(0.05, 2.4, 240)
    q = qA * A2EV
    Ftab = np.interp(qA, qF, Fc)
    FDM2 = (ALPHA * ME / q) ** 4 if light else 1.0
    dR = []
    for w in wgrid:
        vmin = w / q + q / (2 * m)
        e2 = n_ref(w) * float(alpha_fn(w)) * HBARC_CM / w
        S = np.array([(a * A2EV) ** 2 * e2 * f / eps_model(a * A2EV, w) ** 2 * fwin(a, w, d0) / (2 * np.pi * ALPHA)
                      if vm < vmax else 0.0 for a, f, vm in zip(qA, Ftab, vmin)])
        dR.append(rho_chi / (4 * np.pi * m * rho_T * mu ** 2) * np.trapezoid(q * FDM2 * eta(vmin) * S, q))
    return np.trapezoid(np.array(dR), wgrid) * KGYR * CM2


out("\nrate model of the estimate (I7), three events in 1 kg yr; sigma_e in cm^2:")
out("  (published central values with dataset M: heavy 3.07e-29 at 0.36, 6.95e-32 at 0.40; light 1.27e-31, 3.93e-34)")
res = {}
for m in (0.36, 0.38, 0.40, 0.42, 0.43):
    row = []
    for light in (False, True):
        RM = rate(m * 1e6, alpha_M, light)
        RS = rate(m * 1e6, alpha_S, light)
        row.append((3 / RM, 3 / RS, RS / RM))
    res[m] = row
    out("  %.2f MeV: heavy sigma_M %.2e, sigma_S %.2e (rate S/M %.2f) | light sigma_M %.2e, sigma_S %.2e (rate S/M %.2f)"
        % (m, row[0][0], row[0][1], row[0][2], row[1][0], row[1][1], row[1][2]))

ms = np.arange(0.360, 0.3851, 0.005)
sS = np.array([3 / rate(m * 1e6, alpha_S) for m in ms])
sM = np.array([3 / rate(m * 1e6, alpha_M) for m in ms])
mS = np.interp(30.0, -np.log10(sS), ms)
mM = np.interp(30.0, -np.log10(sM), ms)
out("  heavy mediator: sigma = 1e-30 cm^2 reached at %.4f MeV (S), %.4f MeV (M); first zero-phonon edge 0.405 MeV:"
    " top %.3f (S), %.3f (M) MeV of the phonon-assisted-only band" % (mS, mM, 0.405 - mS, 0.405 - mM))
out("  fall of sigma (heavy) from 0.36 to 0.40 MeV: x%.0f (S, %.2f orders), x%.0f (M, %.2f orders)"
    % (res[0.36][0][1] / res[0.40][0][1], np.log10(res[0.36][0][1] / res[0.40][0][1]),
       res[0.36][0][0] / res[0.40][0][0], np.log10(res[0.36][0][0] / res[0.40][0][0])))
for m in (0.40, 0.42):
    for lab, fn in (("S", alpha_S), ("M", alpha_M)):
        a, b = rate(m * 1e6, fn), rate(m * 1e6, fn, d0=0.0)
        out("  %.2f MeV, dataset %s: share of the rate in the margin below the zero-phonon edge (delta_w 0.3 -> 0): %.0f %%"
            % (m, lab, 100 * (1 - a / b)))

# F1: how much of the 0.36 MeV rate rests on the extrapolation of the 0.5 K fit below its lowest diode energy
W_DIODE = 1.206        # eV, Stanford et al. lowest photon energy (1028 nm)
cutS = lambda w: alpha_S(w) * (np.asarray(w) >= W_DIODE)
mixSM = lambda w: np.where(np.asarray(w) >= W_DIODE, alpha_S(w), alpha_M(w))
clampS = lambda w: alpha_S(w) * (np.asarray(w) >= 1.1728)
for m in (0.36, 0.38, 0.40):
    rS = rate(m * 1e6, alpha_S)
    out("  %.2f MeV: share of the 0.5 K-fit rate from omega < %.3f eV (extrapolation of the fit): %.0f %%"
        % (m, W_DIODE, 100 * (1 - rate(m * 1e6, cutS) / rS)))
out("  0.36 MeV heavy variants: fit above 1.206 eV and 20 K curve below: sigma %.1e; fit clamped at the cold edge 1.1728 eV:"
    " sigma %.1e; fit's TA threshold E_g1 + w_TA = %.4f eV, %.0f meV below the cold excitonic edge 1.1728 eV"
    % (3 / rate(0.36e6, mixSM), 3 / rate(0.36e6, clampS), 1.134 + W_TA, 1e3 * (1.1728 - 1.134 - W_TA)))
out("  (the 20 K curve below 1.212 eV is the estimate's linear ramp from 1.160 eV, not data)")
out("  0.36 MeV reach band (heavy): %.1e to %.1e cm^2; light %.1e to %.1e cm^2"
    % (res[0.36][0][1], res[0.36][0][0], res[0.36][1][1], res[0.36][1][0]))

# ------------------------------------------------------------------------------------------------ C. budget
out("\n" + "=" * 100)
out("C. ERROR BUDGET OF THE RATE ESTIMATE (Sect. 13.9), sized items in quadrature of logs")
out("=" * 100)
f_ff = 3.0
f_scr = np.sqrt(S_HI / S_LO)
f_thr = 1.5
dsp = [res[m][0][2] for m in (0.38, 0.40, 0.42, 0.43)]
f_dat = max(max(dsp), 1 / min(dsp))
out("  form factor x%.1f; screening (half-range of [%.2f, %.2f]) x%.2f; data spread S/M at 0.38-0.43 MeV %s -> x%.2f; "
    "threshold shift with Q* x%.1f" % (f_ff, S_LO, S_HI, f_scr, " ".join("%.2f" % x for x in dsp), f_dat, f_thr))
comb = np.exp(np.sqrt(np.log(f_ff) ** 2 + np.log(f_scr) ** 2 + np.log(f_dat) ** 2 + np.log(f_thr) ** 2))
f36 = max(res[0.36][0][2], 1 / res[0.36][0][2])
c36 = np.exp(np.sqrt(np.log(f_ff) ** 2 + np.log(f_scr) ** 2 + np.log(f36) ** 2 + np.log(f_thr) ** 2))
out("  at 0.36 MeV the data spread is x%.2f and the combined uncertainty x%.1f" % (f36, c36))
out("  combined: x%.2f at 0.38-0.43 MeV (old budget with x2 screening, 25 %% data: x%.2f)"
    % (comb, np.exp(np.sqrt(np.log(3) ** 2 + np.log(2) ** 2 + np.log(1.25) ** 2 + np.log(1.5) ** 2))))
LOGF.close()
