"""Sect. 19.2 (electronic excitation by the recoil): every number of the section and Fig. 19.2.
Run: python yield19_2.py > yield19_2.log   (about 5 s).  Output: tex/figures/ch19/fig19_2.pdf.

Natural units hbar = c = 1 unless a name says otherwise; energies in eV, momenta in eV or 1/Angstrom as named.

1. Binary electron-hole threshold (eq:19.2-transfer, eq:19.2-Eth).  A slow ion of speed v_N meets a valence electron of
   speed v_e; in the ion frame the electron reflects elastically, so the largest energy it gains is 2 m_e v_N (v_N + v_e).
   With v_e <= v_F (free gas of the four valence electrons per atom, n = 32/a^3 in the cubic cell of eight atoms) a pair
   (cost E_g) needs 2 m_e v_N (v_N + v_F) >= E_g.  Leading order in v_N/v_F: v_th = E_g/(2 m_e v_F),
   E_R,th = M v_th^2/2 = (M/m_e) E_g^2/(16 E_F).  Full root: v_N = [-v_F + (v_F^2 + 2 E_g/m_e)^(1/2)]/2.
   Inputs (book values): Si a = 5.431 A (CODATA, Sect. 3.1), E_g = 1.17 eV (low T, Sect. 3.3), M = 28.0855 u;
   Ge a = 5.658 A (Sect. 3.3), E_g = 0.744 eV (low T, Sect. 3.3), M = 72.630 u.  u = 931.494 MeV, m_e = 510.999 keV,
   hbar c = 1973.2698 eV A (CODATA 2022).
2. Massey parameter xi_M = E_g l / v_N with l = 1 A (the definition of App. E.23), and the Born parameter Z alpha / v_F.
3. Soft threshold: the fraction of valence electrons whose speed admits a gain >= E_g, f(p > p_min), with
   p_min(E_R) = E_g/(2 v_N) - m_e v_N (from 2 m_e v_N (v_N + p/m_e) >= E_g).  Free gas: 1 - (p_min/k_F)^3 for p_min < k_F.
   Crystal model: valence momentum density of the local empirical pseudopotential of Sect. 3.3 (../ch03/epm.py,
   Cohen-Bergstresser form factors, a = 5.43 A of their fit), n(p) = 2 sum_{n<=4, k} |c_nk(G)|^2 delta(p - k - G) on a
   10^3 Monkhorst-Pack grid of the primitive reciprocal cell.  The model's pseudo-orbitals lack the oscillations of the true
   valence orbitals inside the cores, which add weight at large p; the basis reaches |k + G| = 5.3 1/A, so f is reported
   only for p_min <= 4.8 1/A (E_R >= 50 eV).
4. Migdal part of the measured yield.  Soft-limit Migdal spectrum dP/domega_e of Sect. 12.3 (../ch12/mig12.py: loss
   function with local fields, Z_ion(p), tables to 89 eV with their 1.11 eV gap), proportional to v_N^2 = 2E_R/M.
   Mean pair number of a pair seeded at omega_e from the silicon cascade of Chap. 18 (../ch18/casc18_4.py with the
   parameter set of ../ch18/si_cascade18.py: E_g = 1.160 eV, omega_AB = 63 meV, B_h = 12 eV, A_AB = 5.703 eV^3,
   theta_ii = 1), nbar(omega) = 1 + <m_e(x1) + m_h(x2)>, x1 + x2 = omega - E_g, for two splits: uniform in x1 and
   one-sided (electron takes all).  Yield convention of the measurement (Albakry et al., arXiv:2303.02196, Eq. (1)):
   Y = <n_eh> epsilon / E_r with epsilon = 3.8 eV.  So Delta Y_Mig = (3.8 eV / E_R) int domega_e (dP/domega_e) nbar.
5. Measured silicon yields and Fano factors: Albakry et al., arXiv:2303.02196, Table II (E_r = 0.10, 0.22, 0.46, 0.89,
   2.33, 3.91 keV); their power-law fit Y = 0.302 (E_r/10 keV)^0.261 (text below Table II).  Germanium: Kavner and
   Jovanovic, arXiv:2405.10405, abstract and Table IV: 63.8 +- 8.4 eV_ee at 254.1 eV_nr, quenching factor 25.1 +- 3.3 %
   (77 K), Lindhard 14.3 % with kappa = 0.157.
6. Lindhard yield, eq:16.6-lindhard: y_L = k g/(1 + k g), g = 3 e^0.15 + 0.7 e^0.6 + e, e = 11.5 (E_R/keV) Z^(-7/3),
   k_L = 0.133 Z^(2/3) A^(-1/2) (= 0.1458 for Si; Albakry et al. draw k = 0.146).
7. Electronic-energy spread from the measured Fano factor: for a conversion at constant epsilon, the law of total variance
   gives F_NR = F_eh + Var(E_el)/(epsilon <E_el>), <E_el> = Y E_R; with F_eh = 0.119 (measured, Sect. 18.4).
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")   # small batched eigenproblems (epm.py) run fastest single-threaded
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch19")
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
sys.path.insert(0, os.path.join(HERE, "..", "ch12"))
sys.path.insert(0, os.path.join(HERE, "..", "ch18"))

U = 931.494e6            # eV
ME = 510.999e3           # eV
HBARC = 1973.2698        # eV A
ALPHA = 1 / 137.035999
C_MS = 2.99792458e8      # m/s

MAT = {"Si": dict(a=5.431, Eg=1.17, A=28.0855, Z=14),
       "Ge": dict(a=5.658, Eg=0.744, A=72.630, Z=32)}

DATA = [  # E_r [keV], Y, +, -, F, +, -   (2303.02196 Table II)
    (0.10, 0.102, 0.034, 0.030, 0.9, 0.7, 0.4),
    (0.22, 0.108, 0.009, 0.010, 0.5, 0.2, 0.1),
    (0.46, 0.136, 0.009, 0.008, 1.8, 0.6, 0.5),
    (0.89, 0.127, 0.031, 0.015, 3.7, 0.8, 0.9),
    (2.33, 0.173, 0.044, 0.019, 7.7, 3.2, 2.2),
    (3.91, 0.236, 0.055, 0.009, 8.4, 2.4, 1.9),
]
EPS_Y = 3.8              # eV, the measurement's pair energy
F_EH = 0.119


def free_gas(m):
    a, Eg, M = m["a"], m["Eg"], m["A"] * U
    n = 32.0 / a ** 3                                  # valence electrons per A^3
    kF = (3 * np.pi ** 2 * n) ** (1 / 3)               # 1/A
    pF = kF * HBARC                                    # eV
    vF = pF / ME
    EF = pF ** 2 / (2 * ME)
    v0 = Eg / (2 * ME * vF)
    E0 = 0.5 * M * v0 ** 2
    v1 = 0.5 * (-vF + np.sqrt(vF ** 2 + 2 * Eg / ME))
    E1 = 0.5 * M * v1 ** 2
    return dict(n=n, kF=kF, vF=vF, EF=EF, vth=v0, Eth=E0, Eth_full=E1, M=M)


def vN(ER, M):
    return np.sqrt(2 * ER / M)


def pmin(ER, M, Eg):
    v = vN(ER, M)
    return (Eg / (2 * v) - ME * v) / HBARC             # 1/A


def lindhard(ER, Z, A, k=None):
    k = 0.133 * Z ** (2 / 3) / np.sqrt(A) if k is None else k
    e = 11.5 * (ER / 1e3) * Z ** (-7 / 3)
    g = 3 * e ** 0.15 + 0.7 * e ** 0.6 + e
    return k * g / (1 + k * g), k


def epm_momentum(nk=10):
    from epm import EPM
    E = EPM("Si")
    a = E.a
    b = np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], float)
    f = (np.arange(nk) + 0.5) / nk
    ks = np.array([i * b[0] + j * b[1] + l * b[2] for i in f for j in f for l in f])
    P, W = [], []
    for s in range(0, len(ks), 100):
        kk = ks[s:s + 100]
        _, v = E.bands(kk, nb=4, vectors=True)
        for i, k in enumerate(kk):
            p = np.linalg.norm(k + E.G, axis=1) * 2 * np.pi / a
            w = (np.abs(v[i]) ** 2).sum(axis=1)       # four bands, sum of |c|^2 over bands
            P.append(p)
            W.append(w)
    P, W = np.concatenate(P), np.concatenate(W)
    W = W / W.sum()
    gmax = np.sqrt(E.ecut) * 2 * np.pi / a
    return P, W, a, gmax


def frac_above(P, W, p0):
    return W[P > p0].sum()


def cascade_nbar(omegas, split):
    import casc18_4 as C
    import si_cascade18 as S
    Eg, om, Bh, A = S.EG_SI, S.OM_SI, S.BH_SI, S.A_AB
    w = om / Eg
    N = C.grid(w)
    h = 1.0 / N
    X = float(np.ceil(omegas.max() / Eg)) + 1.0
    c = C.Cascade(A / Eg ** 3, round(w * N) / N, X=X, h=h, a=0.5, Bh=Bh / Eg, theta=1.0, sets=("N",))
    m_e, m_h = c.res["N"][0]
    x = c.x
    out = np.zeros_like(omegas)
    for i, o in enumerate(omegas):
        xt = (o - Eg) / Eg
        if xt < 0:
            continue
        if split == "one":
            out[i] = 1 + np.interp(xt, x, m_e)
        else:
            y = np.linspace(0, xt, 401)
            out[i] = 1 + np.trapezoid(np.interp(y, x, m_e) + np.interp(xt - y, x, m_h), y) / max(xt, 1e-12) \
                if xt > 0 else 1.0
    return out, N, Eg


def main():
    os.makedirs(FIG, exist_ok=True)
    print("== 1. Binary threshold ==")
    fg = {}
    for name, m in MAT.items():
        r = free_gas(m)
        fg[name] = r
        print(f"{name}: a = {m['a']} A, n = {r['n']:.5f} A^-3, k_F = {r['kF']:.4f} A^-1, E_F = {r['EF']:.3f} eV, "
              f"v_F = {r['vF']:.4e} = {r['vF']*C_MS:.4e} m/s, M/m_e = {r['M']/ME:.0f}")
        print(f"   E_g = {m['Eg']} eV: v_th = {r['vth']:.4e} = {r['vth']*C_MS/1e3:.2f} km/s, "
              f"E_R,th (v_N << v_F) = {r['Eth']:.1f} eV = {r['Eth']/m['Eg']:.0f} E_g; keeping v_N^2: {r['Eth_full']:.1f} eV "
              f"({100*(r['Eth_full']/r['Eth']-1):+.1f} %)")
        print(f"   check (M/m_e) E_g^2/(16 E_F) = {r['M']/ME*m['Eg']**2/(16*r['EF']):.1f} eV; "
              f"E_g/(16 E_F) = {m['Eg']/(16*r['EF']):.5f}")
    si = fg["Si"]
    Msi = si["M"]
    for ER in (20.0, 100.0, 352.0, 1000.0):
        v = vN(ER, Msi)
        print(f"Si E_R = {ER:6.0f} eV: v_N = {v:.4e} = {v*C_MS/1e3:.1f} km/s = v_F/{si['vF']/v:.0f}; "
              f"max gain 2 m_e v_N (v_N + v_F) = {2*ME*v*(v+si['vF']):.3f} eV")
    # lightest dark-matter mass for a given maximal recoil, E_R,max = 2 mu^2 v_max^2 / M (eq:1.3-ERmax), v_max = 2.650e-3
    vmax = 2.650e-3
    for ER in (100.0, si["Eth"]):
        m = brentq(lambda mc: 2 * (mc * Msi / (mc + Msi)) ** 2 * vmax ** 2 / Msi - ER, 1e6, 1e11)
        print(f"Si: E_R,max = {ER:.1f} eV needs m_chi >= {m/1e9:.3f} GeV (v_max = {vmax})")
    # WE 19.2 intermediate numbers
    print("WE 19.2: E_F = %.3f eV, M = %.4e eV, E_g^2/16E_F = %.5f eV, M/m_e = %.1f" %
          (si["EF"], Msi, 1.17 ** 2 / (16 * si["EF"]), Msi / ME))

    print("\n== 2. Massey and Born parameters ==")
    ell = 1.0
    for ER in (20.0, 100.0, 352.0, 1000.0):
        v = vN(ER, Msi)
        xi = 1.17 * ell / (v * HBARC)
        print(f"Si E_R = {ER:6.0f} eV: xi_M = E_g l / v_N = {xi:.2f} (l = 1 A), exp(-xi) = {np.exp(-xi):.2e}")
    for name, m in MAT.items():
        print(f"{name}: Z alpha / v_F = {m['Z']*ALPHA/fg[name]['vF']:.1f}")

    print("\n== 3. Soft threshold: fraction of valence electrons fast enough ==")
    P, W, aE, gmax = epm_momentum()
    kF_epm = (3 * np.pi ** 2 * 32 / aE ** 3) ** (1 / 3)
    print(f"EPM Si (a = {aE} A): basis reaches |k+G| = {gmax:.2f} A^-1; k_F (a = {aE}) = {kF_epm:.4f} A^-1")
    print(f"  fraction of valence momentum density beyond k_F: {frac_above(P, W, kF_epm):.4f}; beyond 1.5 k_F: "
          f"{frac_above(P, W, 1.5*kF_epm):.4f}; beyond 2 k_F: {frac_above(P, W, 2*kF_epm):.5f}")
    ERs = np.geomspace(50, 1000, 200)
    f_free, f_epm = [], []
    for ER in ERs:
        p0 = pmin(ER, Msi, 1.17)
        f_free.append(max(0.0, 1 - (p0 / si["kF"]) ** 3))
        f_epm.append(frac_above(P, W, p0))
    f_free, f_epm = np.array(f_free), np.array(f_epm)
    for ER in (50.0, 100.0, 200.0, 300.0, 352.0, 500.0, 1000.0):
        p0 = pmin(ER, Msi, 1.17)
        ff = max(0.0, 1 - (p0 / si["kF"]) ** 3)
        print(f"  E_R = {ER:6.0f} eV: p_min = {p0:.3f} A^-1 = {p0/si['kF']:.3f} k_F; free gas {ff:.4f}; "
              f"EPM {frac_above(P, W, p0):.5f}")

    print("\n== 4. Migdal part of the measured yield ==")
    import mig12 as G
    om = G.OM
    for split in ("uniform", "one"):
        nb, Nc, EgC = cascade_nbar(om, split)
        if split == "uniform":
            nb_u = nb
        else:
            nb_o = nb
    print(f"cascade grid E_g/{Nc}, E_g = {EgC} eV")
    for o in (2.0, 3.0, 4.0, 6.0, 10.0, 20.0):
        i = np.argmin(np.abs(om - o))
        print(f"  omega_e = {om[i]:.2f} eV: nbar = {nb_u[i]:.3f} (uniform split), {nb_o[i]:.3f} (one-sided); "
              f"omega/3.749 = {om[i]/3.749:.3f}")
    for ER in (100.0, 220.0, 460.0):
        d = G.dP_domega(ER)
        sel = om >= G.EG
        Pm = np.trapezoid(d[sel], om[sel])
        wm = np.trapezoid(om[sel] * d[sel], om[sel]) / Pm
        nmu = np.trapezoid(nb_u[sel] * d[sel], om[sel])
        nmo = np.trapezoid(nb_o[sel] * d[sel], om[sel])
        dYu, dYo = EPS_Y * nmu / ER, EPS_Y * nmo / ER
        Yd = [r for r in DATA if abs(r[0] * 1e3 - ER) < 1][0][1]
        print(f"  E_R = {ER:.0f} eV: P_Mig = {Pm:.4e}, mean omega_e = {wm:.2f} eV, pairs per Migdal event "
              f"{nmu/Pm:.3f} (uniform) / {nmo/Pm:.3f} (one-sided); Delta Y_Mig = {dYu:.3e} / {dYo:.3e}; "
              f"measured Y = {Yd}; ratio Y/DeltaY = {Yd/dYu:.0f} / {Yd/dYo:.0f}; share {100*dYu/Yd:.2f} % / {100*dYo/Yd:.2f} %")
    dY_mig = EPS_Y * np.trapezoid(nb_u[om >= G.EG] * G.dP_domega(100.0)[om >= G.EG], om[om >= G.EG]) / 100.0

    print("\n== 5./6. Data against the Lindhard yield ==")
    for r in DATA:
        yl, k = lindhard(r[0] * 1e3, 14, 28.0855)
        npair = r[1] * r[0] * 1e3 / EPS_Y
        print(f"  Si {r[0]:.2f} keV: Y = {r[1]} (+{r[2]} -{r[3]}), <n_eh> = {npair:.2f}, Lindhard (k_L = {k:.4f}) "
              f"{yl:.3f}, ratio data/Lindhard {r[1]/yl:.2f}; power law {0.302*(r[0]/10)**0.261:.3f}")
    yl146, _ = lindhard(100.0, 14, 28.0855, k=0.146)
    print(f"  Si 100 eV with k = 0.146: {yl146:.3f}")
    ylge, kge = lindhard(254.1, 32, 72.630, k=0.157)
    print(f"  Ge 254.1 eV: Lindhard (k = 0.157) {ylge:.3f}; with k_L of eq:16.6-lindhard: "
          f"{lindhard(254.1, 32, 72.630)[0]:.3f} (k_L = {lindhard(254.1, 32, 72.630)[1]:.4f}); measured 0.251 +- 0.033")

    print("\n== 7. Spread of the electronic energy from F_NR ==")
    for r in DATA:
        Eel = r[1] * r[0] * 1e3
        var = (r[4] - F_EH) * EPS_Y * Eel
        print(f"  {r[0]:.2f} keV: <E_el> = {Eel:.1f} eV, Var(E_el) = {var:.0f} eV^2, sigma = {np.sqrt(max(var,0)):.1f} eV "
              f"= {100*np.sqrt(max(var,0))/Eel:.0f} % of the mean")

    # ---- figure ----
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.0))
    E = np.array([r[0] for r in DATA]) * 1e3
    Y = np.array([r[1] for r in DATA])
    yerr = np.array([[r[3] for r in DATA], [r[2] for r in DATA]])
    Eg = np.geomspace(50, 5000, 300)
    a1.plot(Eg, lindhard(Eg, 14, 28.0855)[0], color="0.45", ls="--", lw=1.0, label=r"Lindhard, $k_L = 0.146$")
    a1.plot(Eg, 0.302 * (Eg / 1e4) ** 0.261, color="C0", lw=0.8, ls=":", label="power-law fit")
    a1.errorbar(E, Y, yerr=yerr, fmt="o", ms=3.5, color="C0", capsize=2, lw=0.9, label="Si data")
    a1.axhline(dY_mig, color="C3", lw=1.0, label=r"Migdal part $\Delta Y_q$")
    a1.axvline(si["Eth"], color="k", lw=0.8)
    a1.axvspan(si["Eth_full"], si["Eth"], color="0.85", lw=0)
    a1.text(si["Eth"] * 1.08, 1.6e-4, r"$E_{R,\mathrm{th}}$", fontsize=8)
    a1.set_xscale("log")
    a1.set_yscale("log")
    a1.set_xlim(50, 5000)
    a1.set_ylim(1e-4, 0.6)
    a1.set_xlabel(r"$E_R$ (eV)")
    a1.set_ylabel(r"$Y_q$")
    a1.legend(fontsize=7.2, loc="center right", bbox_to_anchor=(1.0, 0.45), frameon=False)
    a1.text(0.03, 0.95, "(a)", transform=a1.transAxes, fontsize=9, va="top")

    a2.plot(ERs, np.where(f_free > 0, f_free, np.nan), color="k", lw=1.0, label="free electron gas")
    a2.plot(ERs, f_epm, color="C1", lw=1.2, label="pseudopotential crystal")
    a2.axvline(si["Eth"], color="k", lw=0.8)
    a2.set_xscale("log")
    a2.set_yscale("log")
    a2.set_xlim(50, 1000)
    a2.set_xticks([50, 100, 200, 500, 1000])
    a2.set_xticks([], minor=True)
    a2.xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
    a2.set_ylim(1e-6, 1.2)
    a2.set_xlabel(r"$E_R$ (eV)")
    a2.set_ylabel(r"fraction of valence electrons")
    a2.legend(fontsize=7.2, loc="lower left", bbox_to_anchor=(0.04, 0.02), frameon=False)
    a2.text(0.03, 0.95, "(b)", transform=a2.transAxes, fontsize=9, va="top")
    fig.tight_layout()
    out = os.path.join(FIG, "fig19_2.pdf")
    fig.savefig(out)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
