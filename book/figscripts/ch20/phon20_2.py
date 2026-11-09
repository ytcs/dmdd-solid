"""Shared model and every number of Sect. 20.2 (athermal phonons in the substrate) that is not printed by the figure
scripts.  Log: phon20_2.log.  Run: python phon20_2.py > phon20_2.log  (about a minute).
Used by fig20_2.py, limit20_2a.py and limit20_2b.py.

Inputs (sources):
  [LEM]  Leman, arXiv:1109.1193, Table I (p.16): Si B = 2.43e-42 s^3, A = 7.41e-56 s^4, c_L = 9000, c_T = 5400 m/s,
         nu_D = 15 THz; Ge B = 3.67e-41 s^3, A = 6.43e-55 s^4, c_L = 5310, c_T = 3250 m/s, nu_D = 8.64 THz.
  [HER]  Hernandez et al., arXiv:2408.04732, Table 3 (A, 1e-55 s^4: Si 1.15 calc, 0.741 lit; Ge 6.8 calc, 16.5 lit (Tamura);
         Al2O3 12.7 calc, 1.88 lit), Table 4 (Gamma_md: Si 2.02e-4, Ge 5.88e-4, Al2O3 1.25e-5; B, 1e-42 s^3: Si 2.33 calc,
         2.42 lit, 2.42-2.56 measured for different polarizations; Ge 35.4 calc, 36.7 lit; Al2O3 0.025 calc, 0.04 meas),
         Table 5 (LDOS share at 1 THz: Al2O3 0.137; max acoustic frequency Al2O3 8.41 THz), Eq. (4).
  [HP]   Hertel and Pyle, arXiv:1109.4343, p.2: Ge A = 1.61e-55 s^4 (credited there to Msall and Wolfe 1997).
  [KEL]  Kelsey et al., arXiv:2302.05998, Sect. 2.2.2 (p.4): equilibrium branch mix (isotope mode mixing) Si 53.1/37.6/9.3 %,
         Ge 53.5/36.7/9.8 % (slow T / fast T / L); only L down-conversion is implemented (T decay negligible).
  [ISO]  Natural isotopes: Si from figscripts/ch11/iso11.py (Meija 2016 abundances, AME2020 masses); Ge abundances
         70/72/73/74/76 = 20.57/27.45/7.75/36.50/7.73 % (Meija et al., Pure Appl. Chem. 88, 293 (2016), Table 1) and AME2020
         masses 69.92424875, 71.922075826, 72.923458956, 73.921177761, 75.921402726 u (Wang et al. 2021).
  [C18]  Si elastic constants C11, C12, C44 = 165.6, 63.9, 79.5 GPa, rho_T = 2.33 g/cm^3 (App. C.18, room temperature);
         a = 5.431 A, Omega_at = a^3/8 (Sect. 3.1).
  [BOOK] omega_opt = 64.1 meV (Si, measured, Sect. 5.1), 37.6 meV (Ge, Chap. 18); eps_eh = 3.75 eV (Si, Sect. 18.4),
         2.96 eV (Ge, [LEM] Table I); optical-phonon lifetime 3.66 ps (Si, WE 5.9); partition time 10-100 ps (Sect. 19.1);
         Si effective masses m_par = 0.916, m_perp = 0.19 m_e (Sect. 3.3) -> density-of-states mass per valley 0.32 m_e.
  [DEV]  Ren et al., arXiv:2012.12430, p.4: 1 cm x 1 cm x 0.4 cm Si chip, top face instrumented.
Model of the cascade (MODELLING CHOICES, stated in the text and the captions):
  isotropic continuum; isotope mixing keeps the branch populations at the equilibrium mix, so a phonon of frequency f
  decays at the mean rate f_LA A f^5 (f_LA = L share of [KEL]); each decay gives two daughters with energy fractions x and
  1 - x, x drawn from Beta(3,3) (symmetric, self-similar kernel); no surfaces, no absorption, T = 0 (spontaneous decay).
  Energy spectra u(ln f, t) on a uniform ln f grid (step DLN), evolved exactly with the matrix exponential of the
  discretized fragmentation operator (scipy.linalg.expm, scaling and squaring).  Energy is conserved to round-off.
"""
import os
import sys
import numpy as np
from scipy.special import betainc
from scipy.linalg import expm
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))

H_EV = 4.135667696e-15        # eV s (h)
MEV_PER_THZ = H_EV * 1e12 * 1e3   # 4.1357 meV per THz

MAT = {
    "Si": dict(B=2.43e-42, A=7.41e-56, A_range=(7.41e-56, 1.15e-55), xL=0.093, fD=15.0e12, cL=9000.0, cT=5400.0),
    "Ge": dict(B=3.67e-41, A=1.61e-55, A_range=(1.61e-55, 16.5e-55), xL=0.098, fD=8.64e12, cL=5310.0, cT=3250.0),
}


def vbar(m):
    """rms group speed of the equilibrium mix in the isotropic model, <v^2> = sum c^-1 / sum c^-3 (DOS weights c^-3)."""
    c = np.array([m["cL"], m["cT"], m["cT"]])
    return np.sqrt(np.sum(1 / c) / np.sum(c**-3.0))


def fstar(t, m, A=None):
    A = m["A"] if A is None else A
    return (m["xL"] * A * t) ** (-0.2)


def n_mix(t, m):
    """number of isotope scatterings by time t along the scaling trajectory f_*(t'): 5 B (f_LA A)^(-4/5) t^(1/5)."""
    return 5 * m["B"] * (m["xL"] * m["A"]) ** (-0.8) * t**0.2


def r_rms(t, m):
    """3D rms displacement, <r^2> = 6 int D dt', D = <v^2>/(3 B f_*^4): (10/9) v^2 (f_LA A)^(4/5) t^(9/5) / B."""
    return np.sqrt(10 / 9 * vbar(m) ** 2 * (m["xL"] * m["A"]) ** 0.8 * t**1.8 / m["B"])


# ----------------------------------------------------------------- cascade on a ln f grid
DLN = 0.01


def grid(fmin=0.02e12, fmax=20.0e12, dln=DLN):
    n = int(np.round(np.log(fmax / fmin) / dln)) + 1
    lnf = np.log(fmin) + dln * np.arange(n)
    return np.exp(lnf), dln


def kernel_weights(dln, a=3.0):
    """Energy share p_k of the daughters landing k bins below the parent (k = 0, 1, ...), Beta(a,a) fractions.
    Daughter energy density in x is 2 x b(x); its integral over x in (e^{-(k+1/2) dln}, e^{-(k-1/2) dln}) is p_k.
    Since 2 x b(x) for Beta(a,a) is 2 * [a/(2a)] * Beta(a+1, a) density = Beta(a+1,a) density, p_k is a Beta(a+1,a) cdf difference."""
    kmax = int(12 / dln)
    edges = np.exp(-(np.arange(kmax + 1) - 0.5) * dln)
    edges[0] = 1.0
    cdf = betainc(a + 1, a, edges)
    p = cdf[:-1] - cdf[1:]
    return p


def operator(f, dln, m, A=None):
    """Dense generator G with du/dt = G u for the energy per bin u_i."""
    A = m["A"] if A is None else A
    n = len(f)
    r = m["xL"] * A * f**5
    p = kernel_weights(dln)
    G = np.zeros((n, n))
    for j in range(n):
        kk = np.arange(min(len(p), j + 1))
        G[j - kk, j] += r[j] * p[kk]          # energy deposited at lower bins (k = 0 is the same bin)
        G[j, j] -= r[j]
        # energy carried below the grid floor stays booked in bin 0 (negligible above 1 ps for the grids used)
        lost = 1.0 - p[kk].sum()
        G[0, j] += r[j] * lost
    return G


_CACHE = {}


def propagator(G, t):
    """exp(G t), scaling and squaring (scipy.linalg.expm); cached by (id(G), t)."""
    key = (id(G), float(t))
    if key not in _CACHE:
        if len(_CACHE) > 8:
            _CACHE.clear()
        _CACHE[key] = expm(G * t)
    return _CACHE[key]


def evolve1(u0, G, t):
    return propagator(G, t) @ u0


def evolve(u0, G, times):
    """u(t) for the list of times (s), exact matrix exponential."""
    return np.array([evolve1(u0, G, t) for t in np.asarray(times, float)])


def line(f, f0):
    u = np.zeros_like(f)
    u[np.argmin(np.abs(np.log(f / f0)))] = 1.0
    return u


def tv(u1, u2):
    return 0.5 * np.sum(np.abs(u1 / u1.sum() - u2 / u2.sum()))


def birth_spike(f, ftop):
    """Thermal-spike birth (MODEL): energy density in f proportional to f^3 (Debye modes x energy) below ftop,
    stored per ln f bin as f^4."""
    u = np.where(f < ftop, f**4, 0.0)
    return u / u.sum()


def birth_top_line(f, ftop):
    """Near-top birth (MODEL): Gaussian at 0.95 ftop with width 0.05 ftop (energy per ln f bin)."""
    u = np.exp(-0.5 * ((f - 0.95 * ftop) / (0.05 * ftop)) ** 2)
    return u / u.sum()


def birth_er_si(f, soft=0.0171):
    """Electron-recoil birth in Si (MODEL): optical phonons decayed into LA (42 meV) + TA (22 meV) pairs, energy shares
    42/64 and 22/64 (the dominant channel of Sect. 5.7), each a Gaussian of 10 % relative width (MODELLING CHOICE), plus a soft fraction f_s spread uniformly in energy over
    0.2-6 meV (acoustic emission of carriers below the optical energy).  Energy per ln f bin."""
    E = f * MEV_PER_THZ / 1e12
    g = lambda E0: np.exp(-0.5 * ((E - E0) / (0.1 * E0)) ** 2) * E      # Gaussian in E (10 % width), per ln E bin
    u = (1 - soft) * (42 / 64) * g(42.0) / g(42.0).sum() + (1 - soft) * (22 / 64) * g(22.0) / g(22.0).sum()
    s = np.where((E > 0.2) & (E < 6.0), E, 0.0)     # uniform in E -> per ln E bin proportional to E
    u += soft * s / s.sum()
    return u / u.sum()


def tau_lines(f, G, fl, fh, t, nl=6):
    """sup over pairs of line births in [fl, fh] of the TV distance at time t (lines on a uniform grid in ln f)."""
    lines = np.exp(np.linspace(np.log(fl), np.log(fh), nl))
    U = [evolve1(line(f, x), G, t) for x in lines]
    return max(tv(U[i], U[j]) for i in range(nl) for j in range(i + 1, nl))


def crossing(fun, lo, hi, level=1e-3):
    """time where fun(t) = level, found by brentq in ln t."""
    return np.exp(brentq(lambda lt: np.log(fun(np.exp(lt))) - np.log(level), np.log(lo), np.log(hi), xtol=1e-4))


def gmd(x, M):
    x = np.asarray(x, float) / np.sum(x)
    Mb = np.sum(x * M)
    return np.sum(x * (M - Mb) ** 2) / Mb**2, Mb


def christoffel_cm3(C11, C12, C44, rho, n=96):
    """Sphere average of (1/3) sum_nu c_nu^-3 for a cubic crystal (Gauss-Legendre in cos theta x uniform phi)."""
    xg, wg = np.polynomial.legendre.leggauss(n)
    phis = (np.arange(2 * n) + 0.5) * np.pi / n
    s = 0.0
    wsum = 0.0
    for x, w in zip(xg, wg):
        st = np.sqrt(1 - x * x)
        for ph in phis:
            q = np.array([st * np.cos(ph), st * np.sin(ph), x])
            Mm = np.empty((3, 3))
            for i in range(3):
                for k in range(3):
                    if i == k:
                        Mm[i, k] = C11 * q[i] ** 2 + C44 * (1 - q[i] ** 2)
                    else:
                        Mm[i, k] = (C12 + C44) * q[i] * q[k]
            ev = np.linalg.eigvalsh(Mm) / rho
            s += w * np.sum(ev**-1.5) / 3
            wsum += w
    return s / wsum


if __name__ == "__main__":
    print("=== Sect. 20.2 numbers (phon20_2.py) ===")
    print(f"h = {H_EV:.6e} eV s; 1 THz = {MEV_PER_THZ:.4f} meV")
    # ---------------- isotopes and B_iso
    import iso11 as I
    g_si, Mb_si = gmd(I.X, I.MI)
    print(f"Si: Mbar = {Mb_si:.4f} u, abundances {I.X}, g_md = {g_si:.4e} ([HER] Table 4: 2.02e-4)")
    for nm, x, Mi in zip(I.ISO.keys(), I.X, I.MI):
        print(f"   {nm}: x = {x:.5f}, M = {Mi:.6f} u, (M - Mbar)/Mbar = {(Mi-Mb_si)/Mb_si:+.5f}, x*(dM/M)^2 = {x*((Mi-Mb_si)/Mb_si)**2:.3e}")
    xge = np.array([0.2057, 0.2745, 0.0775, 0.3650, 0.0773])
    Mge = np.array([69.92424875, 71.922075826, 72.923458956, 73.921177761, 75.921402726])
    g_ge, Mb_ge = gmd(xge, Mge)
    print(f"Ge: Mbar = {Mb_ge:.4f} u, g_md = {g_ge:.4e} ([HER] Table 4: 5.88e-4)")
    rho = 2330.0
    cm3 = christoffel_cm3(165.6e9, 63.9e9, 79.5e9, rho)
    print(f"Si <c^-3> (sphere average, C18 tensor) = {cm3:.4e} s^3/m^3; 1/<c^-3> = {1/cm3:.4e} m^3/s^3 ([HER]: 2.13e11)")
    cm3_iso = (1 / 9000.0**3 + 2 / 5400.0**3) / 3
    print(f"Si <c^-3> isotropic code speeds 9.0/5.4 km/s = {cm3_iso:.4e}; 1/ = {1/cm3_iso:.4e}")
    Om = (5.431e-10) ** 3 / 8
    print(f"Si Omega_at = {Om*1e30:.3f} A^3")
    for lab, c in [("C18 tensor", cm3), ("code speeds", cm3_iso)]:
        B = 4 * np.pi**3 * g_si * Om * c
        print(f"  B_iso({lab}) = 4 pi^3 g_md Omega_at <c^-3> = {B:.4e} s^3; Gamma_iso(1 THz) = {B*1e48:.3e} 1/s")
    B_si = 4 * np.pi**3 * g_si * Om * cm3
    # WE 20.2: natural Si at 1 THz
    f1 = 1e12
    G1 = B_si * f1**4
    v = vbar(MAT["Si"])
    print(f"WE 20.2: Gamma_iso(1 THz) = {G1:.4e} 1/s, lifetime {1/G1*1e9:.1f} ns; with [LEM] B: {2.43e-42*1e48:.3e}; [HER] meas 2.42-2.56 -> {2.42e6:.2e}-{2.56e6:.2e}")
    print(f"   omega at 1 THz = {2*np.pi*f1:.4e} 1/s; Gamma/omega = {G1/(2*np.pi*f1):.2e}")
    print(f"   v_rms (isotropic code speeds, DOS weights) = {v:.0f} m/s; mean free path v/Gamma = {v/G1*1e3:.2f} mm; with c_T 5400: {5400/G1*1e3:.2f} mm")
    lam = 5400 / f1
    print(f"   wavelength (T, 5.4 km/s) = {lam*1e9:.2f} nm; mfp/wavelength = {5400/G1/lam:.2e}")
    print(f"   E_ath(1 THz) = {MEV_PER_THZ:.3f} meV")
    # isotope relative width at 50 meV in 11.6: 2.5e-4 (check scaling only)
    # ---------------- rates, mixing vs decay
    for name, m in MAT.items():
        print(f"--- {name}: B = {m['B']:.3e}, A = {m['A']:.3e} (range {m['A_range']}), f_LA = {m['xL']}, f_D = {m['fD']/1e12} THz, v_rms = {vbar(m):.0f} m/s")
        print(f"   B/A (isotope = L-decay frequency) = {m['B']/m['A']/1e12:.1f} THz;  Gamma_iso/Gamma_anh,L at 10 THz = {m['B']/(m['A']*1e13):.2f}")
        t0 = 1 / (m["xL"] * m["A"] * m["fD"] ** 5)
        print(f"   initial decay time 1/(f_LA A f_D^5) = {t0*1e9:.3f} ns; 1/(A f_D^5) (L phonon) = {1/(m['A']*m['fD']**5)*1e12:.1f} ps")
        for t in [1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4]:
            fs = fstar(t, m)
            print(f"   t = {t:.0e} s: f_* = {fs/1e12:.2f} THz = {fs/1e12*MEV_PER_THZ:.2f} meV; N_mix = {n_mix(t, m):.0f}; r_rms = {r_rms(t, m)*1e6:.1f} um")
        for A in m["A_range"]:
            print(f"   f_*(100 ns) with A = {A:.3e}: {fstar(1e-7, m, A)/1e12:.2f} THz")
    # near-face shell of the 4-mm device, one instrumented face
    d = 4e-3
    for t in [1e-8, 1e-7, 1e-6, 3e-6]:
        print(f"Si near-face shell r_rms/d at {t:.0e} s: {r_rms(t, MAT['Si'])/d*100:.2f} % of the 4-mm chip")
    # athermal locality at 10.9 THz (45 meV)
    m = MAT["Si"]
    f = 45e-3 / H_EV
    tau = 1 / (m["xL"] * m["A"] * f**5)
    Gi = m["B"] * f**4
    L = np.sqrt(2 * vbar(m) ** 2 * tau / Gi)
    print(f"Si phonon at 45 meV = {f/1e12:.2f} THz: decay time of the mixed population {tau*1e9:.2f} ns; diffusion length sqrt(6 D tau) = {L*1e6:.2f} um")
    tst = 1 / (m["xL"] * m["A"] * f**5)
    print(f"   rms distance along the scaling trajectory (the law of the text) at t = {tst*1e9:.2f} ns, when E_* = 45 meV: "
          f"{r_rms(tst, m)*1e6:.2f} um (used in the text; the fixed-energy value above is not)")
    # prompt phonons of a 100 eV electron recoil (E_g/eps_eh = 1.17/3.75 = 0.312, Sects. 19.5, 18.4) and their occupation
    Eh = 100 * (1 - 1.17 / 3.75)
    nph = Eh / 0.030
    nat = 8 / (5.431e-8) ** 3                       # atoms per cm^3
    Vs = 4 / 3 * np.pi * (1e-4) ** 3                # 1 um sphere, cm^3
    print(f"100 eV ER: prompt phonons {Eh:.1f} eV, gap energy {100-Eh:.1f} eV; ~{nph:.0f} phonons at 30 meV;"
          f" modes in a 1-um sphere = 3 x {nat*Vs:.2e} atoms = {3*nat*Vs:.2e}; occupation ~ {nph/(3*nat*Vs):.1e}")
    print(f"thermal energy at 10 mK = {8.617333e-5*0.01*1e6:.3f} ueV")
    # soft fraction
    for nm, wo, eps in [("Si", 64.1e-3, 3.75), ("Ge", 37.6e-3, 2.96)]:
        print(f"{nm}: soft fraction f_s = omega_opt/eps_eh = {wo/eps*100:.2f} %")
    me = 0.511e6
    mdos = (0.916 * 0.19**2) ** (1 / 3)
    for Ec in [0.010, 0.030, 0.032, 0.064]:
        k = np.sqrt(2 * mdos * me * Ec)
        w = 2 * (9000 / 2.998e8) * k
        print(f"Si electron (m_dos = {mdos:.3f}) at {Ec*1e3:.0f} meV: max LA phonon 2 c_L k = {w*1e3:.2f} meV = {w/H_EV/1e12:.2f} THz")
    print(f"Si optical lifetime 3.66 ps -> fraction left at 10 ps: {np.exp(-10/3.66):.3f}; at 100 ps: {np.exp(-100/3.66):.1e}")
    # ---------------- sapphire
    for Bs, lab in [(0.025e-42, "calc"), (0.04e-42, "meas")]:
        for As in [1.88e-55, 12.7e-55]:
            print(f"Al2O3 B = {Bs:.3e} ({lab}), A = {As:.2e}: B/A = {Bs/As/1e12:.3f} THz")
        for fT in [1e12, 2e12, 5e12]:
            print(f"   B f^4 x 1 us at {fT/1e12:.0f} THz = {Bs*fT**4*1e-6:.3f}")
    for As in [1.88e-55, 12.7e-55]:
        fa = 8.41e12
        print(f"Al2O3 L decay at 8.41 THz (A = {As:.2e}): {1/(As*fa**5)*1e9:.3f} ns; at 2 THz {1/(As*2e12**5)*1e6:.2f} us")
    print(f"Ge vs Si B ratio {MAT['Ge']['B']/MAT['Si']['B']:.1f}; Ge g_md/Si g_md = {g_ge/g_si:.2f}")
