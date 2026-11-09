"""Shared inputs for Sect. 11.6 (nuclear-spin and isotope couplings): host Green function of silicon, single mass defects
(Lifshitz), the isotope-disorder absorption of a B - L vector, the electromagnetic (two-phonon) comparison and the nuclear-spin
weights. Used by limit11_6a.py, limit11_6b.py and fig11_6.py. Run directly to print every number of Sect. 11.6 (iso11.log).

Sources of every input:
  [DOS]  PBE (DFPT) phonon density of states of Sect. 5.2, figscripts/ch05/fig5_2_data.npz (matdyn, 0.25 cm^-1 bins, total DOS
         normalized to 6 modes per two-atom cell; omega_max = 513.75 cm^-1 = 63.7 meV). On the two equivalent sites of silicon the
         site-projected DOS is g_ph,kappa = total/2 (normalized to three) and D(omega) = g_ph,kappa/3 is normalized to one.
  [MEI]  Meija et al., Pure Appl. Chem. 88, 293 (2016): natural Si abundances 92.223, 4.685, 3.092 % (28Si, 29Si, 30Si).
  [AME]  Wang et al., Chin. Phys. C 45, 030003 (2021) (AME2020): atomic masses 27.97692653, 28.97649466, 29.973770137 u.
  [KLOS] Klos et al., PRD 88, 083516 (2013), Table III: 29Si <S_n> = 0.156, <S_p> = 0.016, J_nuc = 1/2 (as Sect. 8.1).
  [IKE]  Ikezawa and Ishigame, J. Phys. Soc. Jpn. 50, 3734 (1981), measured two-phonon absorption of Si at 293 K, as plotted in
         Deinzer and Strauch, PRB 69, 045205 (2004), Fig. 3 (diamonds). Points read from that figure (rendered at 600 dpi; reading
         uncertainty about 0.05 cm^-1 plus 10 %): alpha(403 cm^-1 = 50.0 meV) = 0.55 cm^-1; the in-band table ALPHA_293 below.
  eps_1 = 11.7 for Si below the electronic gap (Sects. 4.4, 4.6), n_r = sqrt(11.7) = 3.42.
  Lattice constant a = 5.431 A (Sect. 3.1): Omega_at = a^3/8 = 20.02 A^3.  e^2 = 4 pi alpha.  1 u = 931.494 MeV.
Model (stated in the text and the captions): harmonic lattice with the force constants of the mean-mass crystal; isotopes differ only
in mass; host on-site Green function
  G_h(omega) = (1/3) sum over modes |e_kappa|^2 / (Mbar (omega_n^2 - omega^2 - i0)),
  Mbar G_h = PV int D(w') dw' / (w'^2 - omega^2) + i pi D(omega) / (2 omega)       (D normalized to one),
real part by a principal-value quadrature with the singularity subtracted. Single defect of mass M_i = Mbar (1 - delta_i):
  G_i = G_h / (1 + delta_i Mbar omega^2 G_h),   g_i(omega)/g_ph,kappa(omega) = (1 - delta_i) Im[G_i]/Im[G_h]          (Lifshitz)
and to first order in delta_i, 1 + delta_i h(omega) with h = -1 - 2 Mbar omega^2 Re G_h.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
D52 = os.path.join(HERE, "..", "ch05", "fig5_2_data.npz")

CM = 1.239841984e-4            # eV per cm^-1
ALPHA = 1 / 137.035999
E2 = 4 * np.pi * ALPHA
U_EV = 931.494e6
HBARC_EV_A = 1973.269804
A_SI = 5.431
OMEGA_AT = A_SI**3 / 8 / HBARC_EV_A**3        # eV^-3
EPS1 = 11.7
NR = np.sqrt(EPS1)

# isotopes of natural silicon [MEI], [AME]; neutron numbers N = A - 14
ISO = {"28Si": (0.92223, 27.97692653, 14), "29Si": (0.04685, 28.97649466, 15), "30Si": (0.03092, 29.973770137, 16)}
X = np.array([v[0] for v in ISO.values()]); X = X / X.sum()
MI = np.array([v[1] for v in ISO.values()])
NI = np.array([v[2] for v in ISO.values()], float)
AI = NI + 14
MBAR = np.sum(X * MI)                         # u, abundance-weighted mean mass
DELTA = (MBAR - MI) / MBAR                    # mass defects referenced to Mbar

# measured 293 K absorption read from Deinzer-Strauch Fig. 3 [IKE] (cm^-1, cm^-1)
ALPHA_293 = np.array([[126, 0.30], [158, 0.40], [197, 0.45], [237, 0.45], [284, 0.47], [324, 0.47], [363, 0.49],
                      [403, 0.55], [446, 0.70], [474, 0.90], [493, 1.20], [513, 1.50]])


def dos():
    """omega (eV), D(omega) (eV^-1, normalized to one per site and direction) from the cached PBE DOS."""
    d = np.load(D52)["dos"]
    w = d[:, 0] * CM
    g = d[:, 1] / CM                           # states per eV per cell (total, 6 modes)
    D = g / 6.0
    D /= np.sum(0.5 * (D[1:] + D[:-1]) * np.diff(w))
    return w, D


W, D = dos()
WMAX = W[np.nonzero(D)[0][-1]]


def mG(om):
    """Mbar * G_h(omega) in eV^-2 for omega > 0 (array), principal value with the singularity subtracted."""
    om = np.atleast_1d(om).astype(float)
    out = np.empty(om.size, complex)
    dw = np.diff(W)
    for k, o in enumerate(om):
        Do = np.interp(o, W, D, left=0.0, right=0.0)
        # PV int D(w)/(w^2 - o^2) dw = int [D(w) - Do]/(w^2 - o^2) dw + Do * PV int_0^wmax dw/(w^2 - o^2)
        den = W**2 - o**2
        f = np.where(np.abs(den) > 1e-14, (D - Do) / np.where(np.abs(den) > 1e-14, den, 1.0), 0.0)
        # at w = o the integrand tends to D'(o)/(2o): use neighbours (finite); trapezoid
        re = np.sum(0.5 * (f[1:] + f[:-1]) * dw)
        if Do > 0:
            wm = W[-1]
            re += Do * np.log(abs((wm - o) / (wm + o))) / (2 * o)
        out[k] = re + 1j * np.pi * Do / (2 * o)
    return out


def ldos_ratio(om, delta):
    """g_i/g_ph,kappa = D_i/D for a single defect of mass Mbar(1 - delta) (exact, Lifshitz); in-band omega only."""
    g = mG(om)
    gi = g / (1 + delta * om**2 * g)
    return (1 - delta) * gi.imag / g.imag


def h_first(om):
    """h(omega) = -1 - 2 Mbar omega^2 Re G_h (first-order coefficient of D_i/D in delta)."""
    return -1 - 2 * om**2 * mG(om).real


def local_mode(delta):
    """Frequency (eV) above the band where 1 + delta Mbar omega^2 Re G_h = 0 (light defect, delta > 0), and its weight."""
    if delta <= 0:
        return None
    om = np.linspace(WMAX * 1.0001, 3 * WMAX, 4000)
    f = 1 + delta * om**2 * mG(om).real
    s = np.where(np.sign(f[1:]) != np.sign(f[:-1]))[0]
    if len(s) == 0:
        return None
    o = om[s[0]]
    # weight of the pole in D_i: (1 - delta) * |1/ d/d(omega^2)[(1 + delta om^2 G)/G] | * ... computed numerically below
    eps = 1e-6
    def F(x):
        gg = mG(np.array([x]))[0].real
        return (1 + delta * x**2 * gg) / gg
    dF = (F(o + eps) - F(o - eps)) / (2 * eps)
    # D_i(omega) = (2 omega M_i / pi) Im G_i  ->  pole of G_i = 1/F: weight in omega is (2 o M_i/pi) * pi / |dF/domega| / Mbar
    wgt = (1 - delta) * 2 * o / abs(dF)
    return o, wgt


def bl_weights():
    """B - L charge per mass b_i = N_i/M_i (u^-1), mass-weighted mean, sigma_b^2 = sum x_i (M_i/Mbar)(b_i - bbar)^2."""
    b = NI / MI
    bbar = np.sum(X * NI) / np.sum(X * MI)
    s2 = np.sum(X * MI / MBAR * (b - bbar)**2)
    dmean = np.sum(X * MI * (b - bbar)**2 * DELTA) / np.sum(X * MI * (b - bbar)**2)
    return b, bbar, s2, dmean


def gamma_iso(om, exact=True):
    """Gamma_iso / g^2 in eV (per absorbed quantum), Eq. (11.6-Giso); exact single-defect LDOS per isotope if exact."""
    b, bbar, s2, _ = bl_weights()
    Dh = np.interp(om, W, D, left=0.0, right=0.0)
    if not exact:
        return np.pi * MBAR / U_EV * s2 * Dh / (2 * OMEGA_AT)
    tot = 0.0
    for x, m, bi, dl in zip(X, MI, b, DELTA):
        tot = tot + x * m / U_EV * (bi - bbar)**2 * Dh * ldos_ratio(om, dl)
    return np.pi * tot / (2 * OMEGA_AT)


def gamma_em(om_ev, alpha_cm):
    """Gamma_EM / g^2 = omega Im(-1/eps)/e^2 from a measured absorption coefficient (eps_2 = alpha n_r c / omega)."""
    # omega/c in cm^-1 = omega / (hbar c) with hbar c = 1.97327e-5 eV cm
    k = om_ev / 1.973269804e-5
    eps2 = alpha_cm * NR / k
    iml = eps2 / (EPS1**2 + eps2**2)
    return om_ev * iml / E2, eps2, iml


if __name__ == "__main__":
    print(f"PBE DOS: omega_max = {WMAX*1e3:.2f} meV; norm = {np.sum(0.5*(D[1:]+D[:-1])*np.diff(W)):.4f}")
    print(f"Mbar = {MBAR:.4f} u; delta_i = {DELTA}; mass variance g_md = {np.sum(X*(MI-MBAR)**2)/MBAR**2:.3e}")
    b, bbar, s2, dmean = bl_weights()
    print(f"B-L per mass b_i = {b} u^-1; bbar = {bbar:.5f}; sigma_b^2/bbar^2 = {s2/bbar**2:.4e}; <delta>_b = {dmean:.4f}")
    bb = AI / MI; bbbar = np.sum(X * AI) / np.sum(X * MI)
    print(f"baryon number per mass A_i/M_i = {bb}; weighted variance / mean^2 = {np.sum(X*MI/MBAR*(bb-bbbar)**2)/bbbar**2:.3e}")
    om = 0.050
    Do = np.interp(om, W, D)
    print(f"D(50 meV) = {Do:.2f} eV^-1 per site and direction; g_ph,kappa = {3*Do:.2f}")
    g = mG(np.array([om]))[0]
    print(f"Mbar G_h(50 meV) = {g.real:.2f} + {g.imag:.2f} i eV^-2; Mbar w^2 G_h = {om**2*g.real:.3f} + {om**2*g.imag:.3f} i")
    h = h_first(np.array([om]))[0]
    print(f"h(50 meV) = {h:.3f}; first-order correction <delta>_b h = {dmean*h:+.4f}")
    for name, dl in zip(ISO, DELTA):
        print(f"  {name}: delta = {dl:+.5f}; D_i/D(50 meV) exact = {ldos_ratio(np.array([om]), dl)[0]:.5f}; first order = {1+dl*h:.5f}")
    gi_ex = gamma_iso(np.array([om]))[0]; gi_0 = gamma_iso(np.array([om]), exact=False)[0]
    print(f"Gamma_iso/g^2 (50 meV): host DOS {gi_0:.4e} eV, exact single-defect {gi_ex:.4e} eV (ratio {gi_ex/gi_0:.4f})")
    ge, eps2, iml = gamma_em(om, 0.55)
    print(f"alpha_293(50 meV) = 0.55 cm^-1 -> eps2 = {eps2:.3e}, Im(-1/eps) = {iml:.3e}, Gamma_EM/g^2 = {ge:.4e} eV")
    print(f"ratio Gamma_iso/Gamma_EM at 50 meV, 293 K data: host {gi_0/ge:.3e}, exact {gi_ex/ge:.3e}")
    for a in (0.50, 0.60):
        print(f"   alpha = {a}: ratio host {gi_0/gamma_em(om, a)[0]:.3e}")
    # ratio across the band
    for row in ALPHA_293:
        o = row[0] * CM
        if o < WMAX:
            print(f"   omega = {o*1e3:5.1f} meV: D = {np.interp(o, W, D):6.2f} /eV, ratio (host DOS) = {gamma_iso(np.array([o]), exact=False)[0]/gamma_em(o, row[1])[0]:.3e}")
    # 76 meV comparison (610 cm^-1), above the band
    print(f"610 cm^-1 = {610*CM*1e3:.1f} meV, alpha 9.5: Im(-1/eps) = {gamma_em(610*CM, 9.5)[2]:.3e}")
    # Lifshitz checks
    om_b = np.linspace(0.0005, WMAX * 0.9999, 3000)
    for dl in (DELTA[2], -0.5, 0.3, 0.6):
        r = ldos_ratio(om_b, dl)
        Dh = np.interp(om_b, W, D)
        norm = np.sum(0.5 * (r[1:] * Dh[1:] + r[:-1] * Dh[:-1]) * np.diff(om_b))
        lm = local_mode(dl)
        lmtxt = "" if lm is None else f"; local mode {lm[0]*1e3:.2f} meV, weight {lm[1]:.4f}, total {norm + lm[1]:.4f}"
        print(f"  delta = {dl:+.4f}: in-band weight of D_i = {norm:.4f}{lmtxt}")
    # critical light defect for a local mode: 1 + delta Mbar wmax^2 Re G(wmax) = 0
    gm = mG(np.array([WMAX * 1.0005]))[0].real * (WMAX * 1.0005)**2
    print(f"Mbar w^2 Re G_h just above the band = {gm:.3f}; local mode for delta > {-1/gm:.3f}")
    # spin weights, 29Si (Sect. 8.1)
    Sn, Sp, J = 0.156, 0.016, 0.5
    print(f"29Si: c_a/g_ann (neutron only) = {Sn/J:.3f}; x c^2 J(J+1) = {X[1]*(Sn/J)**2*J*(J+1):.4e}")
    r29 = ldos_ratio(np.array([0.020, 0.030, 0.040, 0.050, 0.058, 0.062]), DELTA[1])
    print(f"29Si D_29/D at 20,30,40,50,58,62 meV: {np.round(r29, 4)}")
