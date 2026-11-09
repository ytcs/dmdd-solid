"""Phonon transmission into sensor films (Sect. 20.3): every number printed in Sect. 20.3, worked example
we:20-escape, and the solver used by fig20_3.py and limit20_3a.py.  Log: amm20_3.log.
Run: python amm20_3.py > amm20_3.log   (a few seconds).

Media (book constants, App. C.18):
  Si: C11, C12, C44 = 165.6, 63.9, 79.5 GPa, rho = 2.33 g/cm^3 (C.18, from Martinez et al. 1805.02495 Table I).
  Al (primary, 0 K): C11, C12, C44 = 114.3, 61.9, 31.6 GPa (Kamm & Alers extrapolated to 0 K, as tabulated by
      Malica & Dal Corso, arXiv:2109.13551 Table 2, row "Expt."), rho = 2.70 g/cm^3 (density used for the impedances
      and rates).  Voigt speeds c_L = 6.63, c_T = 3.30 km/s.  (Ch. 15's 6.47/3.40 km/s are the [100] speeds
      sqrt(C11/rho), sqrt(C44/rho) at rho = 2.73; they are not isotropic averages and are not used here.)
  Al (sensitivity, room temperature): C11, C12, C44 = 106.8, 60.7, 28.2 GPa, rho = 2.70 (C.18, Kittel);
      Voigt speeds 6.41/3.11 km/s.
  MODELLING CHOICE: each crystal is replaced by an isotropic medium with the Voigt averages
      mu = (C11 - C12 + 3 C44)/5,  B = (C11 + 2 C12)/3,  lambda = B - 2 mu/3.
  For Si this gives lambda = 52.4, mu = 68.0 GPa, the isotropic tensor of C.18 and of 1805.02495 Table I
  (c_L = 9.00, c_T = 5.40 km/s).  For 0 K Al c_L = 6.63, c_T = 3.30 km/s; for room-temperature Al 6.41/3.11 km/s.
  Sensitivity variants (text only): Si with its [100] speeds (8.43/5.84 km/s) and its [111] speeds (9.35/5.09 km/s),
  App. C.18 eq:C.18-cubic; Al with the room-temperature C.18 constants (above); Al 0 K at rho = 2.73.

Physics (derived in Sect. 20.3):
  Welded plane interface z = 0, medium 1 (z < 0), medium 2 (z > 0).  Plane waves exp[i w (p x + s z - t)], slowness
  p = sin(theta)/c conserved; s = sqrt(1/c^2 - p^2), or i sqrt(p^2 - 1/c^2) (evanescent).
  Unit polarizations: P: c_L (p, s_z); SV: c_T (s_z, -p)  (x, z components; s_z signed).
  Continuity of u_x, u_z, sigma_zz = lambda div u + 2 mu d_z u_z, sigma_xz = mu (d_z u_x + d_x u_z): 4x4 system.
  Energy coefficient of an outgoing propagating wave j: rho_j c_j^2 Re(s_j) |A_j|^2 / (rho_inc c_inc^2 s_inc).
  SH decouples: r = (Z1 - Z2)/(Z1 + Z2), Z = mu s_T, t_SH = 1 - |r|^2.
  Flux-weighted angle average <t> = int_0^{pi/2} t(theta) 2 sin(theta) cos(theta) d theta.
  Mode average for an isotropic population: weights c_nu^{-2} (L, SV, SH):
      tbar_12 = [c_L^-2 <t_P> + c_T^-2 (<t_SV> + <t_SH>)] / n_1,   n_1 = c_L^-2 + 2 c_T^-2  (fraktur n of the text).
  Reciprocity: n_1 tbar_12 = n_2 tbar_21.  DMM: t_12 = n_2/(n_1 + n_2).
  Film: v_s = n_f / sum_nu c_nu^-3 (density-of-states-weighted mean speed); t_l = 4 d_f/(v_s tbar_esc).
  Absorption per entry, isotropized film (diffuse at every pass):
      P_abs = (1 - S)/(1 - (1 - tbar_esc) S),  S = 2 E_3(2 d_f / l_f)   (E_3 exponential integral).
  Specular variant (fixed angle, t_esc -> tbar_esc), flux averaged:
      P_abs^spec = < (1 - e^{-a})/(1 - (1 - tbar_esc) e^{-a}) >,  a = 2 d_f/(l_f cos theta).
  Lumped form of App. E.12 (Kelsey et al. 2302.05998 Eq. (17)): P_lump = 1 - exp(-4 d_f/l_f).
  Reading of the fitted Si->Al coefficient T_fit = 0.30-0.55 (1805.02495 abstract and Sect. V; 60 nm Al on 380 um Si,
  specular G4CMP fit with no propagation in Al): T_fit = tbar_SiAl * P_abs -> P_abs -> l_f/d_f by inverting S.
  Pair-breaking time near 2 Delta: t0 ~ tau_0^phi = 0.26 ns for Al (Kaplan et al. 1976, as quoted by
  Guruswamy et al. 1401.1937 p. 2).
  Interlayer (text only): normal-incidence L transmission Si | layer h | Al by the 2x2 transfer matrix of a layer
  with impedance Z3 and speed c3: amorphous SiO2, rho = 2.2 g/cm^3, rho c_LA^2 = 7.40e10 Pa (Sect. 16.7 values).
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import expn
from scipy.optimize import brentq


class Medium:
    def __init__(self, name, rho, lam=None, mu=None, cL=None, cT=None):
        """rho in kg/m^3, moduli in Pa, speeds in m/s; give (lam, mu) or (cL, cT)."""
        self.name, self.rho = name, rho
        if cL is None:
            cL = np.sqrt((lam + 2 * mu) / rho)
            cT = np.sqrt(mu / rho)
        self.cL, self.cT = cL, cT
        self.mu = rho * cT**2
        self.lam = rho * cL**2 - 2 * self.mu

    @property
    def n(self):  # interface-weighted phonon density, s^2/m^2
        return self.cL**-2 + 2 * self.cT**-2

    @property
    def vs(self):  # density-of-states-weighted mean speed
        return self.n / (self.cL**-3 + 2 * self.cT**-3)


def voigt(name, rho_gcc, C11, C12, C44):
    mu = (C11 - C12 + 3 * C44) / 5 * 1e9
    B = (C11 + 2 * C12) / 3 * 1e9
    return Medium(name, rho_gcc * 1e3, lam=B - 2 * mu / 3, mu=mu)


def vslow(p, c):
    q = 1.0 / c**2 - p**2
    return np.sqrt(q + 0j) if q >= 0 else 1j * np.sqrt(-q)


def _col(m, kind, p, sign):
    """[u_x, u_z, sigma_zz/(i w), sigma_xz/(i w)] of a unit-amplitude wave; sign = +1 (+z) or -1 (-z)."""
    if kind == "P":
        s = sign * vslow(p, m.cL)
        dx, dz = m.cL * p, m.cL * s
    else:
        s = sign * vslow(p, m.cT)
        dx, dz = m.cT * s, -m.cT * p
    szz = m.lam * (p * dx + s * dz) + 2 * m.mu * s * dz
    sxz = m.mu * (s * dx + p * dz)
    return np.array([dx, dz, szz, sxz], dtype=complex)


def psv(m1, m2, inc, theta):
    """Energy coefficients (R_P, R_SV, T_P, T_SV) for a P or SV wave incident from m1 at angle theta."""
    cinc = m1.cL if inc == "P" else m1.cT
    p = np.sin(theta) / cinc
    M = np.column_stack([_col(m1, "P", p, -1), _col(m1, "S", p, -1),
                         -_col(m2, "P", p, +1), -_col(m2, "S", p, +1)])
    rhs = -_col(m1, inc, p, +1)
    A = np.linalg.solve(M, rhs)
    sinc = np.cos(theta) / cinc
    out = []
    for amp, m, c in zip(A, (m1, m1, m2, m2), (m1.cL, m1.cT, m2.cL, m2.cT)):
        s = vslow(p, c).real
        out.append(m.rho * c**2 * s * abs(amp) ** 2 / (m1.rho * cinc**2 * sinc))
    return np.array(out)


def sh(m1, m2, theta):
    p = np.sin(theta) / m1.cT
    Z1 = m1.mu * vslow(p, m1.cT)
    Z2 = m2.mu * vslow(p, m2.cT)
    r = (Z1 - Z2) / (Z1 + Z2)
    return 1.0 - abs(r) ** 2


def t_mode(m1, m2, mode, theta):
    """Total transmitted energy fraction (all modes in m2) for incident mode P, SV or SH."""
    if mode == "SH":
        return sh(m1, m2, theta)
    c = psv(m1, m2, mode, theta)
    return c[2] + c[3]


def crit_angles(m1, m2, mode):
    cinc = m1.cL if mode == "P" else m1.cT
    out = []
    for c in (m1.cL, m1.cT, m2.cL, m2.cT):
        if c > cinc:
            out.append(np.arcsin(cinc / c))
    return sorted(set(out))


def flux_avg(f, pts):
    pts = [x for x in pts if 0 < x < np.pi / 2]
    val, err = quad(lambda th: f(th) * 2 * np.sin(th) * np.cos(th), 0, np.pi / 2,
                    points=pts or None, limit=400, epsabs=1e-12, epsrel=1e-11)
    return val


def averages(m1, m2):
    avg = {}
    for mode in ("P", "SV", "SH"):
        avg[mode] = flux_avg(lambda th: t_mode(m1, m2, mode, th), crit_angles(m1, m2, mode))
    tbar = (m1.cL**-2 * avg["P"] + m1.cT**-2 * (avg["SV"] + avg["SH"])) / m1.n
    return avg, tbar


def dmm(m1, m2):
    return m2.n / (m1.n + m2.n)


def S_diffuse(b):
    return 2 * expn(3, b)


def pabs_diffuse(b, tesc):
    S = S_diffuse(b)
    return (1 - S) / (1 - (1 - tesc) * S)


def pabs_specular(b, tesc):
    f = lambda th: (1 - np.exp(-b / np.cos(th))) / (1 - (1 - tesc) * np.exp(-b / np.cos(th)))
    return flux_avg(lambda th: f(th) if np.cos(th) > 1e-12 else 1.0, [])


def invert_b(P, tesc, kind="diffuse"):
    fun = (lambda b: pabs_diffuse(b, tesc) - P) if kind == "diffuse" else (lambda b: pabs_specular(b, tesc) - P)
    return brentq(fun, 1e-8, 50.0, xtol=1e-14)


def layer_t(Z1, Z2, Z3, c3, h, f):
    """Normal-incidence energy transmission Z1 | layer (Z3, c3, thickness h) | Z2 at frequency f (Hz)."""
    k = 2 * np.pi * f / c3
    # transfer matrix of the layer for (velocity, stress) amplitudes
    Mm = np.array([[np.cos(k * h), 1j * np.sin(k * h) / Z3], [1j * Z3 * np.sin(k * h), np.cos(k * h)]])
    # incident + reflected in 1, transmitted in 2 (velocity-stress formulation, sign convention stress = -Z v)
    t_amp = 2 / (Mm[0, 0] + Mm[0, 1] * Z2 + (Mm[1, 0] + Mm[1, 1] * Z2) / Z1)
    return (Z2 / Z1) * abs(t_amp) ** 2 * 1.0


SI = voigt("Si", 2.33, 165.6, 63.9, 79.5)
AL = voigt("Al", 2.70, 114.3, 61.9, 31.6)          # primary: 0 K constants
AL_RT = voigt("AlRT", 2.70, 106.8, 60.7, 28.2)     # sensitivity: room temperature (C.18)


def main():
    print("== Isotropic media (Voigt averages; Si C.18, Al 0 K primary, Al room T sensitivity) ==")
    for m in (SI, AL, AL_RT):
        print(f"{m.name}: rho = {m.rho:.0f} kg/m3, lambda = {m.lam/1e9:.2f} GPa, mu = {m.mu/1e9:.2f} GPa, "
              f"c_L = {m.cL/1e3:.3f} km/s, c_T = {m.cT/1e3:.3f} km/s, Z_L = rho c_L = {m.rho*m.cL/1e6:.2f}e6 kg/m2/s, "
              f"n = c_L^-2 + 2c_T^-2 = {m.n*1e6:.4f} (km/s)^-2, v_s = {m.vs/1e3:.3f} km/s, "
              f"L share of n = {m.cL**-2/m.n:.4f}")
    print(f"n_Si/n_Al = {SI.n/AL.n:.4f}")
    print(f"anisotropy ratios 2C44/(C11-C12): Si {2*79.5/(165.6-63.9):.3f}, Al 0 K {2*31.6/(114.3-61.9):.3f}, "
          f"Al room T {2*28.2/(106.8-60.7):.3f}")
    print(f"Al: sum c^-2 = {AL.n*1e6:.4f} (km/s)^-2, sum c^-3 = {(AL.cL**-3 + 2*AL.cT**-3)*1e9:.4f} (km/s)^-3; "
          f"T share of Al flux = {2*AL.cT**-2/AL.n:.4f}; n_Al/n_Si = {AL.n/SI.n:.3f}")

    print("\n== Critical angles (deg) ==")
    deg = np.degrees
    print(f"Al L -> Si L: {deg(np.arcsin(AL.cL/SI.cL)):.2f}; Al T -> Si L: {deg(np.arcsin(AL.cT/SI.cL)):.2f}; "
          f"Al T -> Si T: {deg(np.arcsin(AL.cT/SI.cT)):.2f}; Al T -> Al L (reflected): {deg(np.arcsin(AL.cT/AL.cL)):.2f}")
    print(f"Si T -> Al L: {deg(np.arcsin(SI.cT/AL.cL)):.2f}; Si T -> Si L (reflected): {deg(np.arcsin(SI.cT/SI.cL)):.2f}")

    print("\n== Normal incidence ==")
    for (a, b) in ((SI, AL), (AL, SI)):
        print(f"{a.name}->{b.name}: t_P(0) = {t_mode(a, b, 'P', 0.0):.4f} (impedance law "
              f"{4*a.rho*a.cL*b.rho*b.cL/(a.rho*a.cL+b.rho*b.cL)**2:.4f}), t_SV(0) = {t_mode(a, b, 'SV', 0.0):.4f}, "
              f"t_SH(0) = {t_mode(a, b, 'SH', 0.0):.4f}")

    print("\n== Flux conservation and mode conversion (max over 2000 angles, 0-89.9 deg) ==")
    ths = np.linspace(0, np.radians(89.9), 2000)
    for (a, b) in ((SI, AL), (AL, SI)):
        for mode in ("P", "SV"):
            dev = max(abs(psv(a, b, mode, th).sum() - 1) for th in ths)
            print(f"{a.name}->{b.name} {mode}: max |sum - 1| = {dev:.1e}")
    # conversion for Si->Al P incidence
    conv = np.array([psv(SI, AL, "P", th)[3] + psv(SI, AL, "P", th)[1] for th in ths])
    print(f"Si->Al incident P: largest converted (SV) flux {conv.max():.4f} at {deg(ths[conv.argmax()]):.1f} deg")
    tsv = np.array([psv(SI, AL, "P", th)[3] for th in ths])
    print(f"Si->Al incident P: largest transmitted SV flux {tsv.max():.4f} at {deg(ths[tsv.argmax()]):.1f} deg; "
          f"at 30 deg {psv(SI, AL, 'P', np.radians(30))[3]:.4f}")
    from scipy.optimize import brentq as _bq
    print("Si->Al incident L, total transmitted: " + ", ".join(
        f"{d} deg {t_mode(SI, AL, 'P', np.radians(d)):.4f}" for d in (0, 30, 45, 60, 70, 75, 80, 85)))
    print(f"Si->Al incident L falls below 0.9 at {deg(_bq(lambda th: t_mode(SI, AL, 'P', th) - 0.9, np.radians(60), np.radians(89.9))):.2f} deg")
    thLL = np.arcsin(AL.cL / SI.cL)
    print(f"Al->Si incident L just beyond the L->L critical angle {deg(thLL):.2f} deg (+0.01): "
          f"{t_mode(AL, SI, 'P', thLL + np.radians(0.01)):.4f}")
    for th_d in (10, 20, 30, 45, 60):
        c = psv(SI, AL, "P", np.radians(th_d))
        print(f"  Si->Al P at {th_d} deg: R_P {c[0]:.4f} R_SV {c[1]:.4f} T_P {c[2]:.4f} T_SV {c[3]:.4f}")
    for th_d in (10, 20, 30, 40, 45):
        c = psv(AL, SI, "P", np.radians(th_d))
        print(f"  Al->Si P at {th_d} deg: R_P {c[0]:.4f} R_SV {c[1]:.4f} T_P {c[2]:.4f} T_SV {c[3]:.4f}")

    print("\n== Angle and mode averages ==")
    res = {}
    for (a, b) in ((SI, AL), (AL, SI)):
        avg, tbar = averages(a, b)
        res[(a.name, b.name)] = (avg, tbar)
        print(f"{a.name}->{b.name}: <t_P> = {avg['P']:.4f}, <t_SV> = {avg['SV']:.4f}, <t_SH> = {avg['SH']:.4f}, "
              f"tbar = {tbar:.4f}, DMM = {dmm(a, b):.4f}")
    tSA = res[("Si", "Al")][1]
    tAS = res[("Al", "Si")][1]
    print(f"Reciprocity: n_Si tbar_SiAl = {SI.n*tSA*1e6:.6f}, n_Al tbar_AlSi = {AL.n*tAS*1e6:.6f} (km/s)^-2, "
          f"relative difference {abs(SI.n*tSA/(AL.n*tAS)-1):.1e}")
    print(f"tbar_AlSi / t_P(0) = {tAS/t_mode(AL, SI, 'P', 0.0):.4f}; tbar_SiAl/tbar_AlSi = {tSA/tAS:.3f}")
    # Al->Si: trapped transverse flux
    thc = np.arcsin(AL.cT / SI.cT)
    trapT = 1 - (AL.cT / SI.cT) ** 2
    wT = 2 * AL.cT**-2 / AL.n
    print(f"Al T beyond {deg(thc):.2f} deg: share of T flux {trapT:.4f}, of all film flux {trapT*wT:.4f} "
          f"(T weight {wT:.4f})")
    thcR = np.arcsin(AL_RT.cT / SI.cT)
    print(f"  room-T Al: T critical angle {deg(thcR):.2f} deg, trapped share of film flux "
          f"{(1-(AL_RT.cT/SI.cT)**2)*2*AL_RT.cT**-2/AL_RT.n:.4f}")
    # L/T flux contrast at the Si->Al interface
    avg = res[("Si", "Al")][0]
    LT = avg["P"] / ((avg["SV"] + avg["SH"]) / 2)
    print(f"Si->Al L/T flux contrast <t_P>/<t_T> = {LT:.3f}; normal incidence {t_mode(SI, AL, 'P', 0)/t_mode(SI, AL, 'SH', 0):.3f}")

    print("\n== Sensitivity: anisotropy bracket of Si and the Al constants (0 K primary, room T, 0 K at rho 2.73) ==")
    variants = {
        "Si Voigt": SI,
        "Si [100] speeds": Medium("Si100", SI.rho, cL=8430.0, cT=5840.0),
        "Si [111] speeds": Medium("Si111", SI.rho, cL=9350.0, cT=5090.0),
    }
    al73 = voigt("Al0K273", 2.73, 114.3, 61.9, 31.6)
    # Hill average (mean of Voigt and Reuss shear moduli; the bulk modulus is the same for cubic crystals)
    C11, C12, C44 = 114.3, 61.9, 31.6
    GV = (C11 - C12 + 3 * C44) / 5
    GR = 5 * (C11 - C12) * C44 / (4 * C44 + 3 * (C11 - C12))
    GH = 0.5 * (GV + GR)
    Bk = (C11 + 2 * C12) / 3
    alH = Medium("AlHill", 2700.0, lam=(Bk - 2 * GH / 3) * 1e9, mu=GH * 1e9)
    _, tH = averages(alH, SI)
    print(f"Al 0 K Hill average: G_V = {GV:.2f}, G_R = {GR:.2f}, G_H = {GH:.2f} GPa; c_L = {alH.cL/1e3:.3f}, c_T = {alH.cT/1e3:.3f} km/s; "
          f"tbar_esc = {tH:.4f}, t_l(60 nm) = {4*60e-9/(alH.vs*tH)*1e9:.4f} ns")
    print(f"Al room T: c_L = {AL_RT.cL/1e3:.3f}, c_T = {AL_RT.cT/1e3:.3f} km/s, v_s = {AL_RT.vs/1e3:.3f} km/s")
    print(f"Al 0 K at rho 2.73: c_L = {al73.cL/1e3:.3f}, c_T = {al73.cT/1e3:.3f} km/s, v_s = {al73.vs/1e3:.3f} km/s")
    for k, s in variants.items():
        for al, aname in ((AL, "Al 0 K"), (AL_RT, "Al room T"), (al73, "Al 0 K 2.73")):
            if k != "Si Voigt" and aname == "Al 0 K 2.73":
                continue
            _, t12 = averages(s, al)
            _, t21 = averages(al, s)
            print(f"{k:16s} / {aname}: tbar_SiAl = {t12:.4f}, tbar_esc = tbar_AlSi = {t21:.4f}, DMM_esc = {dmm(al, s):.4f}")
            print(f"{'':16s}   t_l(60 nm) = {4*60e-9/(al.vs*t21)*1e9:.4f} ns")

    print("\n== Film escape (worked example, d_f = 60 nm) ==")
    d = 60e-9
    tdmm = dmm(AL, SI)
    for lab, te in (("AMM", tAS), ("DMM", tdmm)):
        tl = 4 * d / (AL.vs * te)
        print(f"{lab}: tbar_esc = {te:.4f}, t_l = 4 d_f/(v_s tbar_esc) = {tl*1e9:.4f} ns")
    print(f"t_l(DMM)/t_l(AMM) = {tAS/tdmm:.4f}")
    t0 = 0.26e-9
    tlA = 4 * d / (AL.vs * tAS)
    print(f"t0 = 0.26 ns (near 2 Delta): t_l/t0 (AMM) = {tlA/t0:.3f}, (DMM) = {4*d/(AL.vs*tdmm)/t0:.3f}")
    print(f"l_f = v_s t0 = {AL.vs*t0*1e6:.3f} um, d_f/l_f = {d/(AL.vs*t0):.4f}")
    b0 = 2 * d / (AL.vs * t0)
    print(f"  P_abs (diffuse, AMM esc) at l_f = v_s t0: {pabs_diffuse(b0, tAS):.4f}; rate form t_l/(t_l+t0) = {tlA/(tlA+t0):.4f}")
    print(f"  lumped form at l_f = v_s t0: {1-np.exp(-2*b0):.4f}; ratio P_abs(AMM)/lumped = {pabs_diffuse(b0, tAS)/(1-np.exp(-2*b0)):.3f}"
          f" (thin-film limit 1/tbar_esc = {1/tAS:.3f})")
    print("  room-temperature Al (sensitivity):")
    _, tASr = averages(AL_RT, SI)
    for lab, te in (("AMM", tASr), ("DMM", dmm(AL_RT, SI))):
        tl = 4 * d / (AL_RT.vs * te)
        print(f"    {lab}: tbar_esc = {te:.4f}, t_l = {tl*1e9:.4f} ns, t_l/t0 = {tl/t0:.3f}")
    print(f"    room T thin-limit factor 1/tbar_esc = {1/tASr:.3f}; t_l(0 K)/t_l(room T) - 1 = {tASr*AL_RT.vs/(tAS*AL.vs)-1:+.4f}; "
          f"tbar_esc(0 K)/tbar_esc(room T) - 1 = {tAS/tASr-1:+.4f}; t_l(room T)/t_l(0 K) - 1 = {tAS*AL.vs/(tASr*AL_RT.vs)-1:+.4f}")

    print("\n== Lumped form against the multiple-pass absorption ==")
    for x in (0.01, 0.03, 0.06, 0.1, 0.2, 0.5, 1.0):
        b = 2 * x
        pl = 1 - np.exp(-4 * x)
        p1 = pabs_diffuse(b, 1.0)
        pA = pabs_diffuse(b, tAS)
        pS = pabs_specular(b, tAS)
        print(f"d/l = {x:5.2f}: lumped {pl:.4f}, t_esc=1 exact {p1:.4f} (lumped/exact - 1 = {pl/p1-1:+.4f}), "
              f"AMM esc diffuse {pA:.4f}, specular {pS:.4f}, lumped/AMM {pl/pA:.4f}")
    # where the lumped form is within 10% of the t_esc = 1 exact form
    g = lambda x: (1 - np.exp(-4 * x)) / pabs_diffuse(2 * x, 1.0) - 1.10
    x10 = brentq(g, 1e-4, 0.2)
    x10b = brentq(g, 0.235, 5.0)
    print(f"lumped within 10% of the exact t_esc = 1 form for d/l < {x10:.4f} and again for d/l > {x10b:.3f}")
    xg = np.logspace(-4, 1, 4001)
    rr = (1 - np.exp(-4 * xg)) / pabs_diffuse(2 * xg, 1.0) - 1
    print(f"lumped above the exact t_esc = 1 form everywhere on 1e-4..10: min excess {rr.min():.2e}; "
          f"max excess {rr.max():.4f} at d/l = {xg[rr.argmax()]:.3f}")
    # thin-film limit ratio = tbar_esc
    print(f"thin limit P_abs -> 4 d/(l tbar_esc): ratio lumped/AMM at d/l=1e-4: "
          f"{(1-np.exp(-4e-4))/pabs_diffuse(2e-4, tAS):.4f} (tbar_esc = {tAS:.4f})")

    print("\n== Reading of the fitted Si->Al coefficient 0.30-0.55 (60 nm Al) ==")
    for lab, tin, tesc in (("AMM", tSA, tAS), ("DMM", dmm(SI, AL), tdmm)):
        for T in (0.30, 0.55):
            P = T / tin
            bd = invert_b(P, tesc, "diffuse")
            bs = invert_b(P, tesc, "specular")
            lfd = 2 / bd
            print(f"{lab} pair ({tin:.4f}, {tesc:.4f}), T_fit = {T:.2f}: P_abs = {P:.4f}; "
                  f"l_f/d_f = {lfd:.3f} (diffuse) / {2/bs:.3f} (specular); l_f = {lfd*60:.0f} nm / {2/bs*60:.0f} nm; "
                  f"t_pb = l_f/v_s = {lfd*d/AL.vs*1e9:.4f} ns / {2/bs*d/AL.vs*1e9:.4f} ns; "
                  f"t_l/t_pb (from l) = {4/(lfd*tesc):.3f}")
    print(f"Naive reciprocity reading tbar_esc = (n_Si/n_Al) * T_fit: {SI.n/AL.n*0.30:.3f}-{SI.n/AL.n*0.55:.3f}")
    _, tSAr = averages(SI, AL_RT)
    _, tASr = averages(AL_RT, SI)
    for lab, tin, tesc in (("AMM room T", tSAr, tASr), ("DMM room T", dmm(SI, AL_RT), dmm(AL_RT, SI))):
        out = []
        for T in (0.30, 0.55):
            P = T / tin
            out.append(f"T_fit {T:.2f}: l_f/d_f = {2/invert_b(P, tesc, 'diffuse'):.2f} (diffuse) / {2/invert_b(P, tesc, 'specular'):.2f} (specular)")
        print(f"{lab}: " + "; ".join(out))

    print("\n== Interlayer at normal incidence (amorphous SiO2, rho 2.2 g/cm3, rho c^2 = 7.40e10 Pa) ==")
    c3 = np.sqrt(7.40e10 / 2200.0)
    Z1, Z2, Z3 = SI.rho * SI.cL, AL.rho * AL.cL, 2200.0 * c3
    print(f"c_LA(SiO2) = {c3/1e3:.3f} km/s, Z3 = {Z3/1e6:.2f}e6; Z_Si = {Z1/1e6:.2f}e6, Z_Al = {Z2/1e6:.2f}e6")
    print(f"check h = 0: {layer_t(Z1, Z2, Z3, c3, 0.0, 1e12):.4f}")
    for h in (1e-9, 2e-9):
        row = ", ".join(f"{f/1e12:.1f} THz {layer_t(Z1, Z2, Z3, c3, h, f):.4f}" for f in (0.3e12, 0.8e12, 1.5e12, 2.5e12))
        print(f"h = {h*1e9:.0f} nm: {row}")
    fmin = c3 / (4 * 2e-9)
    print(f"quarter-wave frequency of a 2 nm layer: {fmin/1e12:.2f} THz, t there {layer_t(Z1, Z2, Z3, c3, 2e-9, fmin):.4f}")
    print(f"Wavelengths at 0.8 THz in Al: L {AL.cL/0.8e12*1e9:.2f} nm, T {AL.cT/0.8e12*1e9:.2f} nm; "
          f"frequency where lambda_L(Al) = 60 nm: {AL.cL/60e-9/1e12:.3f} THz")


if __name__ == "__main__":
    main()
