"""Shared inputs and every number of Sect. 11.8 (absorption on phonons and acoustic modes). Run directly to print them.

Sources of every input:
  Halo [B]: Baxter et al., EPJC 81, 907 (2021), arXiv:2105.00599, Table 1 (v0 = 238, v_esc = 544, |v_E| = 250.5 km/s,
      rho_chi = 0.3 GeV/cm^3), hard-truncated boosted Maxwellian; eta(v_min) from phon11.py (App. D.1 closed form).
      Speed distribution f_sp(v) = v |d eta/dv| (eta = int_{v_min} f_sp/v dv), so F_phi(omega) = f_sp/(m v) = |eta'(v)|/m.
  GaAs, measured (Sect. 5.5, WE 5.6, Sect. 11.2; pol11_2.py): omega_T = 33.62, omega_L = 36.35 meV (Strauch and Dorner 1990);
      eps_inf = 10.88, eps_0 = 12.9 (Lockwood et al. 2005); Z* = 2.11 from the splitting (WE 5.6); a = 5.638 A,
      Omega = a^3/4 = 44.80 A^3, rho_T = 5.361 g/cm^3; standard atomic weights Ga 69.723, As 74.9216 u; Z_Ga = 31, Z_As = 33.
  GaAs, PBE (Sect. 5.5, fig5_4_epsk.sh): Z* = 2.094, eps_inf = 13.70 (28^3 k grid).
  GaAs, App. E.17 inputs: Z* = 2.16, eps_inf = 10.9 (used there for d = -1.33e-3; reproduced below).
  Rigid-ion structure of Mitridate et al., arXiv:2308.06314 v1, Eqs. (40)-(41) and the text after Eq. (44): electron numbers
      N_Ga,e = 28, N_As,e = 36 (ionic charges Q = +3, -3), electronic mixing term with eps_inf: site coupling Z - Q/eps_inf.
  Phonon widths: GaAs gamma_nu = 1e-2 omega_nu (the modelling choice of 2308.06314, Sect. III A, "we use gamma_nu = 1e-2 omega_nu").
      Sapphire: Griffin et al., arXiv:1807.10291 v1, Table II (77 K fits; e-ray widths adopted from the o-ray, as the table says),
      eps_inf = 3.2 and rho_T = 3.98 g/cm^3 (Table I); polarization average 2/3 o + 1/3 e (their Eq. (40)).
  Isotopes of Ga (WE 8.6 numbers, AME2020 / IUPAC): A/M = 1.001072 (Ga, natural) and 1.001046 per u (As).
Constants: e^2 = 4 pi alpha (Heaviside-Lorentz); 1 u = 931.494 MeV; 1 kg = 5.60959e35 eV; 1 yr = 3.15576e7 s.
"""
import numpy as np
import phon11 as P
import pol11_2 as Q

E2 = 4 * np.pi * P.ALPHA
U = 931.494e6                       # eV per u
ANG = P.ANG                         # 1 A in eV^-1
KGYR = P.KG * P.YEAR                # (eV of 1 kg) x (eV^-1 of 1 yr)
CM_MEV = 0.1239841984

# ---------------------------------------------------------------- GaAs
M_GA, M_AS = 69.723, 74.9216
Z_GA, Z_AS = 31, 33
MU = M_GA * M_AS / (M_GA + M_AS)    # u
WT, WL = 33.62e-3, 36.35e-3         # eV
EPSINF, EPS0 = 10.88, 12.9
ZS = 2.11
A_GAAS = 5.638
OMEGA = A_GAAS**3 / 4 * ANG**3      # eV^-3
RHO_GAAS = 5.361                    # g/cm^3
G_PER_EV = 1.78266192e-33


def rho_eV4(rho_g_cm3):
    return rho_g_cm3 / G_PER_EV * (P.HBARC_EV_CM)**3


def d_site(zs, epsinf, q_ion=None):
    """Mass-weighted difference d = v_Ga/M_Ga - v_As/M_As (e per u) of the electron-row site couplings
    v = Z - Z*/eps_inf (Z*_Ga = +zs, Z*_As = -zs); with q_ion, the rigid-ion structure Z - Q/eps_inf."""
    c = zs if q_ion is None else q_ion
    return (Z_GA - c / epsinf) / M_GA - (Z_AS + c / epsinf) / M_AS


def bare_and_born(zs, epsinf):
    bare = Z_GA / M_GA - Z_AS / M_AS
    born = zs / epsinf * (1 / M_GA + 1 / M_AS)
    return bare, born


# ---------------------------------------------------------------- halo
VGRID = np.linspace(1.0, 794.4, 20000)          # km/s


def fsp_over_v_kms():
    """f_sp(v)/v = -d eta/dv in (km/s)^-2."""
    eta = P.eta_kms(VGRID)
    return VGRID, -np.gradient(eta, VGRID)


def v2_mean():
    v, g = fsp_over_v_kms()
    fsp = g * v
    norm = np.trapezoid(fsp, v)
    return np.trapezoid(fsp * v**2, v) / norm, norm


def Q_dm_eff():
    """Effective quality factor of the field line, (pi/2) m F_phi(omega) = (pi/2) f_sp(v)/v in natural units."""
    v, g = fsp_over_v_kms()
    return np.pi / 2 * g * P.C_KMS**2, v


# ---------------------------------------------------------------- loss functions (factorized, damped)
def eps_fact(w, wL, wT, gL, gT, epsinf):
    w = np.asarray(w, complex)
    out = epsinf * np.ones_like(w)
    for a, b, c, d in zip(np.atleast_1d(wL), np.atleast_1d(wT), np.atleast_1d(gL), np.atleast_1d(gT)):
        out *= (a**2 - w**2 - 1j * w * c) / (b**2 - w**2 - 1j * w * d)
    return out


def loss(w, *args):
    return np.imag(-1 / eps_fact(w, *args))


GAAS_ARGS = (WL, WT, 1e-2 * WL, 1e-2 * WT, EPSINF)
SO = dict(wL=np.array([906.6, 629.5, 481.7, 387.6]) * CM_MEV * 1e-3, gL=np.array([16, 4.4, 1.4, 1.4]) * CM_MEV * 1e-3,
          wT=np.array([633.6, 569.0, 439.1, 385.0]) * CM_MEV * 1e-3, gT=np.array([3.8, 3.2, 1.5, 1.4]) * CM_MEV * 1e-3)
SE = dict(wL=np.array([881.1, 510.9]) * CM_MEV * 1e-3, gL=np.array([16, 1.4]) * CM_MEV * 1e-3,
          wT=np.array([582.4, 397.5]) * CM_MEV * 1e-3, gT=np.array([3.2, 1.5]) * CM_MEV * 1e-3)
SAPH_EPSINF, RHO_SAPH = 3.2, 3.98


def loss_saph(w):
    lo = loss(w, SO['wL'], SO['wT'], SO['gL'], SO['gT'], SAPH_EPSINF)
    le = loss(w, SE['wL'], SE['wT'], SE['gL'], SE['gT'], SAPH_EPSINF)
    return 2 / 3 * lo + 1 / 3 * le


def events_per_kgyr(L, rho_T_gcm3, coupling2=1.0):
    """R = (rho_chi/rho_T) coupling^2 L, times one kg-yr."""
    return P.RHO_CHI / rho_eV4(rho_T_gcm3) * coupling2 * L * KGYR


if __name__ == "__main__":
    v2, norm = v2_mean()
    print(f"halo: norm f_sp = {norm:.4f}; <v^2> = {v2:.0f} (km/s)^2, v_rms = {np.sqrt(v2):.1f} km/s = {np.sqrt(v2)/P.C_KMS:.4e}")
    q, v = Q_dm_eff()
    i = np.argmax(q)
    print(f"Q_DM^eff max = {q[i]:.3e} at v = {v[i]:.0f} km/s")
    print("Z/M: Ga %.5f As %.5f diff %.5f" % (Z_GA / M_GA, Z_AS / M_AS, Z_GA / M_GA - Z_AS / M_AS))
    print("1/M_Ga + 1/M_As = %.6f; mu_red = %.3f u" % (1 / M_GA + 1 / M_AS, MU))
    print("Z*/eps_inf at exact cancellation: %.5f" % ((Z_GA / M_GA - Z_AS / M_AS) / (1 / M_GA + 1 / M_AS)))
    rows = [("measured (2.11, 10.88)", ZS, EPSINF), ("E.17 (2.16, 10.9)", 2.16, 10.9), ("PBE (2.094, 13.70)", 2.094, 13.70)]
    d_rig = d_site(ZS, EPSINF, q_ion=3.0)
    for nm, zs, ei in rows:
        d = d_site(zs, ei)
        b, bo = bare_and_born(zs, ei)
        print(f"{nm}: Z*/eps = {zs/ei:.5f}; v_Ga = {Z_GA - zs/ei:.4f}, v_As = {Z_AS + zs/ei:.4f}; bare {b:.5f} born {bo:.5f} "
              f"d = {d:.4e}; dln|d|/dln(Z*/eps) = {bo/abs(d):.2f}; (d_rig/d)^2 = {(d_site(zs, ei, 3.0)/d)**2:.2f}")
    print(f"rigid ion (Q=3, eps 10.88): v_Ga = {Z_GA-3/EPSINF:.4f} v_As = {Z_AS+3/EPSINF:.4f}  d = {d_rig:.4e}")
    d = d_site(ZS, EPSINF)
    for f in (0.99, 1.01, 1.1):
        dd = d_site(ZS * f, EPSINF)
        print(f"  Z*/eps x {f}: d = {dd:.4e} ({dd/d-1:+.3f}); rate x {(dd/d)**2:.3f}")
    # range of the overstatement over Z* in [2.09, 2.16] with eps 10.88-10.9
    for zs in (2.09, 2.11, 2.16):
        print(f"  Z* = {zs}: (d_rig/d)^2 = {(d_site(zs, EPSINF, 3.0)/d_site(zs, EPSINF))**2:.2f}")
    # vertex ratio to the charge vertex
    r = EPSINF * MU * d / ZS
    print(f"eps_inf mu d / Z* = {r:.4f}; squared {r**2:.4f}; rigid {EPSINF*MU*d_rig/ZS:.4f}")
    # nucleon scalar (WE 8.6)
    dN = 1.001072 - 1.001046
    print(f"nucleon: d_N = {dN:.2e} per u; a_N = mu d_N = {MU*dN:.2e}; eps mu dN/Z* = {EPSINF*MU*dN/ZS:.2e}")
    # one-branch loss weight and peak
    w = 1 / EPSINF - 1 / EPS0
    wpol = 1 / EPSINF * (1 - WT**2 / WL**2)
    print(f"1/eps_inf - 1/eps_0 = {w:.5f}; LST-consistent (splitting) weight = {wpol:.5f}")
    ww = np.linspace(30e-3, 40e-3, 200001)
    Lg = loss(ww, *GAAS_ARGS)
    print(f"GaAs L peak (gamma = 1e-2 omega) = {Lg.max():.3f} at {ww[np.argmax(Lg)]*1e3:.3f} meV; int L dw = {np.trapezoid(Lg, ww)*1e3:.4f} meV"
          f" [(pi/2) wL w = {np.pi/2*WL*wpol*1e3:.4f} meV]")
    # dark photon reach at the peak
    Rpk = events_per_kgyr(Lg.max(), RHO_GAAS)
    print(f"GaAs dark photon: events/kg-yr/zeta^2 at peak = {Rpk:.3e}; zeta(3 events) = {np.sqrt(3/Rpk):.2e}")
    ws = np.linspace(40e-3, 130e-3, 400001)
    Ls = loss_saph(ws)
    Rs = events_per_kgyr(Ls.max(), RHO_SAPH)
    print(f"sapphire: L_avg peak = {Ls.max():.3f} at {ws[np.argmax(Ls)]*1e3:.2f} meV; zeta(3 events) = {np.sqrt(3/Rs):.2e}")
    # electron scalar in GaAs at the peak: R = (rho/rho_T) g^2 <v^2>/e^2 (eps mu d/Z*)^2 L
    v2n = v2 / P.C_KMS**2
    for nm, dd in (("residue", d), ("rigid", d_rig)):
        Re = events_per_kgyr(Lg.max(), RHO_GAAS, v2n / E2 * (EPSINF * MU * dd / ZS)**2)
        print(f"electron scalar {nm}: events/kg-yr/g^2 at peak = {Re:.3e}; g(3 events) = {np.sqrt(3/Re):.2e}")
    # photon-like check of 2308.06314 Eq. (43): g ~ kappa e / v with v = 230 km/s
    print(f"photon-like conversion g/zeta = e/v: v=230 km/s -> {np.sqrt(E2)/(230/P.C_KMS):.3e}; v_rms -> {np.sqrt(E2/v2n):.3e}")
