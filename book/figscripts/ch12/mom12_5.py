"""Sect. 12.5: Migdal moments of Si and Ge (Table 12.1), the probability bounds and Worked example 12.5.
Run: python mom12_5.py  (< 1 min).  Natural units, eV.

Moments per nucleus, at leading order in the boost (eq:12.5-moments):
    P = q^2 I_4/M^2,  E1 = int w dP = q^2 I_3/M^2 = E_R dM/M,  E2 = q^2 I_2/M^2,  E3 = q^2 I_1/M^2,
so every moment is E_R times a material constant; the drag mass is dM = M E1/E_R = 2 I_3.
Valence: the soft-limit loss-function spectrum of Sect. 12.3 (eq:12.3-soft),
    dP/dw = 4 alpha v_N^2 int d^3p/(2pi)^3 Z_ion(p)^2 Lbar(p, w)/(3 w^4),   v_N^2 = 2 E_R/M,
    hence dM_val = (8 alpha/3) int d^3p/(2pi)^3 Z_ion(p)^2 int dw Lbar(p, w)/w^3.
  Si: Knapen-Kozaczuk-Lin GPAW tables (../ch10/si_elf_binned.npz; 'lf' = RPA with local fields, 'rpa' without),
      Z_ion(p) of Sect. 12.3 (mig12.py), table threshold 1.11 eV (scissor).
  Ge: the same authors' Ge tables (ge_elf_binned.npz, from ge_elf_reduce.py; 3d in the frozen core), Z_ion(p) = 32 - f_core(p)
      with the 28 core electrons: 2s..3d from the all-electron PBE atom of Sect. 3.5 (../ch03/ld1/ge_r1.wfc), 1s hydrogenic
      with Z - 5/16 (the 1s is not in that file; its form factor is 1.97-2.00 below 22.5 keV).  Threshold 0.744 eV.
  Momentum window of the tables: 0.4-22.5 keV (below the first bin held constant, as in mig12.py); energies <= 89 (Si), 81 (Ge) eV.
Cores: Cox, Dolan, McCabe and Quiney (arXiv:2208.12222) dipole tables per orbital (atom12_2.cox_dipole), rescaled by
  (q_e/q_ref)^2, omega_e = E_B + E_e with the measured binding energies of Sect. 3.5 (Si 2p 99.55, 2s 149.7, 1s 1839 eV;
  Ge 3d 29.4, 3p 122.2, 3s 180.1, 2p 1227, 2s 1414.6 eV; from ../ch10/core10_6.py).
Bounds (eq:12.5-bound): P <= E1/E_th (support above E_th), P >= E1^2/E2 (Cauchy-Schwarz).
"""
import os
import sys
import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
import mig12 as G          # noqa: E402
import atom12_2 as A       # noqa: E402

ALPHA, ME, AU = G.ALPHA, G.ME, G.AU
MASS = {"Si": G.M, "Ge": 67.654e9}
ETH = {"Si": 1.11, "Ge": 0.744}
ECORE = {"Si": {"2p": 99.55, "2s": 149.7, "1s": 1839.0},
         "Ge": {"3d": 29.4, "3p": (4 * 120.8 + 2 * 124.9) / 6, "3s": 180.1, "2p": (4 * 1217.0 + 2 * 1248.1) / 6,
                "2s": 1414.6}}


def ge_tables():
    d = np.load(os.path.join(HERE, "ge_elf_binned.npz"))
    return d["omega"], d["q"], {k: np.maximum(d[k], 0.0) for k in ("lf", "rpa", "ip")}


def ge_fcore(k):
    path = os.path.join(HERE, "..", "ch03", "ld1", "ge_r1.wfc")
    heads = open(path).readline().split()[2:]
    d = np.loadtxt(path)
    rr = d[:, 0]
    occ = {"3D": 10, "3P": 6, "3S": 2, "2P": 6, "2S": 2}
    k = np.atleast_1d(np.asarray(k, float))
    kr = np.outer(k / AU, rr)
    out = np.zeros_like(k)
    for h, n in occ.items():
        u2 = d[:, heads.index(h) + 1]**2
        out += n * np.trapezoid(u2[None, :] * spherical_jn(0, kr), rr, axis=1) / np.trapezoid(u2, rr)
    z1 = 32 - 5 / 16
    x = k / AU / (2 * z1)
    out += 2 / (1 + x**2)**2
    return out


def setup(el):
    if el == "Si":
        om, qt = G.OM, G.QT
        tabs = {"lf": G.LF, "rpa": G.RPA}
        zfun = G.z_ion
    else:
        om, qt, tabs = ge_tables()
        zfun = lambda k: 32.0 - ge_fcore(k)  # noqa: E731
    kg = np.concatenate([np.linspace(0, qt[0], 25)[:-1], qt])
    out = {}
    for key, tab in tabs.items():
        out[key] = np.array([np.interp(kg, qt, tab[i]) for i in range(len(om))])
    return om, kg, out, zfun(kg)


def spectrum(el, resp="lf", zfix=None, kmin=0.0, kmax=np.inf):
    """w, dP/dw per unit E_R (eV^-2), on the table energies above threshold."""
    om, kg, tabs, zg = setup(el)
    z2 = (np.full_like(kg, zfix) if zfix else zg)**2
    m = (kg >= kmin) & (kg <= kmax)
    integ = np.trapezoid(kg[m]**2 * z2[m] * tabs[resp][:, m], kg[m], axis=1)
    keep = om >= ETH[el]
    w = om[keep]
    y = 4 * ALPHA * (2 / MASS[el]) * integ[keep] / (6 * np.pi**2 * w**4)
    return w, y


def moments(w, y):
    return [np.trapezoid(w**k * y, w) for k in range(4)]


def cores(el, ER):
    """Per shell: P and E1 at recoil energy ER from the Cox dipole tables."""
    tab = A.cox_dipole(el)
    s = (A.q_e(el, ER) / A.QE_REF)**2
    res = {}
    for orb, (Ee, dp) in tab.items():
        if orb not in ECORE[el]:
            continue
        w = Ee + ECORE[el][orb]
        P = s * np.trapezoid(dp, Ee)
        E1 = s * np.trapezoid(w * dp, Ee)
        res[orb] = (P, E1)
    return res


if __name__ == "__main__":
    print("Table 12.1, valence (soft-limit spectrum of the crystal tables), per unit recoil energy E_R:")
    rows = {}
    for el in ["Si", "Ge"]:
        M = MASS[el]
        for resp, zfix in [("lf", None), ("rpa", None), ("lf", 4.0)]:
            w, y = spectrum(el, resp, zfix)
            P, E1, E2, E3 = moments(w, y)
            dM = M * E1 / ME
            lab = f"{el} {resp}{' Z=4' if zfix else ' Z_ion(p)'}"
            rows[lab] = (P, E1, E2, E3, dM)
            print(f"  {lab:16s}: P/E_R = {P:.3e} /eV, E1/E_R = {E1:.3e}, dM_val = {dM:5.1f} m_e, "
                  f"<w> = {E1/P:.2f} eV, E2/E_R = {E2:.3e} eV, E3/E_R (table window) = {E3:.3e} eV^2; "
                  f"bounds: E1/E_th = {E1/ETH[el]:.3e} (P/bound {P/(E1/ETH[el]):.3f}), E1^2/E2 = {E1**2/E2:.3e} "
                  f"(P/lower {P/(E1**2/E2):.2f}); diagonal BO correction along q: {E2/4:.3e} eV")
        # where the first moment lives (local fields, Z_ion)
        w, y = spectrum(el)
        E1 = np.trapezoid(w * y, w)
        for kc in [2.25e3, 5e3, 10e3]:
            w2, y2 = spectrum(el, kmin=kc)
            print(f"   {el}: share of E1 from p > {kc/1e3:.2f} keV: {np.trapezoid(w2*y2, w2)/E1:.3f}")
        for wc in [2.0, 3.0, 5.0, 10.0]:
            m = w <= wc
            print(f"   {el}: share of E1 from w <= {wc} eV: {np.trapezoid((w*y)[m], w[m])/E1:.3f}; of P: "
                  f"{np.trapezoid(y[m], w[m])/np.trapezoid(y, w):.3f}")
        # top of the table: bound on the missing first moment above w_top. Per p, int_{w_top}^inf L/w^3 dw
        # <= w_top^-4 int_{w_top}^inf w L dw = w_top^-4 [(pi/2) w_p,val^2 - int_0^{w_top} w L dw] (valence f-sum);
        # w_p,val = 16.6 eV (Si, Sect. 10.2); Ge: 15.6 eV (4 electrons, a = 5.658 A).
        om, kg, tabs, zg = setup(el)
        wp = 16.6 if el == "Si" else 15.6
        held = np.trapezoid(om[:, None] * tabs["lf"], om, axis=0)
        miss = np.maximum(np.pi / 2 * wp**2 - held, 0.0) / om[-1]**4
        E1miss = 4 * ALPHA * (2 / MASS[el]) * np.trapezoid(kg**2 * zg**2 * miss, kg) / (6 * np.pi**2)
        print(f"   {el}: E1 above the table top ({om[-1]:.1f} eV) <= {E1miss/E1:.3f} of E1 (p <= 22.5 keV)")
    # Ge threshold sensitivity: weight of the table between its first nonzero row and 0.744 eV
    om, kg, tabs, zg = setup("Ge")
    integ = np.trapezoid(kg**2 * zg**2 * tabs["lf"], kg, axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        y = 4 * ALPHA * (2 / MASS["Ge"]) * integ / (6 * np.pi**2 * om**4)
    for wth in [0.744, 0.6, 0.4]:
        m = om >= wth
        print(f"   Ge threshold {wth} eV: P/E_R = {np.trapezoid(y[m], om[m]):.3e}, E1/E_R = {np.trapezoid((om*y)[m], om[m]):.3e}")
    # on-site curvature against the contact term (Si): Phi_on = M <omega^2> (harmonic, cubic site), DOS of Sect. 11.4
    sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
    import imp11 as IMP  # noqa: E402
    w2 = np.sum(IMP.G * IMP.WG**2) * IMP.DW
    phi = MASS["Si"] * w2
    contact = 14 * 4 * np.pi * ALPHA * 1765 * AU**3 / 3
    print(f"Si: <omega^2>^1/2 = {np.sqrt(w2)*1e3:.1f} meV, Phi_on = M<omega^2> = {phi:.3e} eV^3, Z e^2 n/3 = {contact:.3e} eV^3, "
          f"ratio {phi/contact:.2e}; P_Mig = 1e-3 at E_R = {1e-3/rows['Si lf Z_ion(p)'][0]:.1f} eV (valence, table)")
    print("Cores (free atom, Cox et al. dipole tables), per unit E_R; drag share dM_s = M E1_s/E_R:")
    CORE_DM = {}
    for el in ["Si", "Ge"]:
        ER = 500.0
        c = cores(el, ER)
        tot = 0.0
        for orb, (P, E1) in c.items():
            dM = MASS[el] * E1 / ER / ME
            tot += dM
            print(f"  {el} {orb}: P/E_R = {P/ER:.3e} /eV, dM_s = {dM:.2f} m_e, bound E1/E_B = {E1/ECORE[el][orb]/ER:.3e} /eV "
                  f"(P/bound {P/(E1/ECORE[el][orb]):.3f})")
        print(f"  {el} cores in the table: dM = {tot:.2f} m_e")
        CORE_DM[el] = tot
    print("Worked example 12.5: silicon at E_R = 500 eV")
    ER = 500.0
    M = MASS["Si"]
    w, y = spectrum("Si")
    P, E1, E2, E3 = [ER * x for x in moments(w, y)]
    print(f"  valence: P = {P:.3e}, E1 = {E1:.4f} eV, upper bound E1/1.11 = {E1/1.11:.3e}, lower bound E1^2/E2 = {E1**2/E2:.3e}")
    c = cores("Si", ER)
    Pc = sum(v[0] for v in c.values())
    Bc = sum(v[1] / ECORE["Si"][k] for k, v in c.items())
    print(f"  cores: P = {Pc:.3e}, shell bounds sum = {Bc:.3e}")
    dMcore = CORE_DM["Si"]
    dMon = dMcore + rows["Si lf Z_ion(p)"][4]
    for dMtot, lab in [(14, "atomic 14 m_e"), (dMon, f"{dMcore:.2f} m_e core + crystal valence")]:
        print(f"  single-threshold bound with {lab}: E_R dM/(M E_g) = {ER*dMtot*ME/M/1.17:.3e} (E_g = 1.17 eV)")
    print(f"  dM/M: atomic {14*ME/M:.3e}; core+valence ({dMon:.2f} m_e) {dMon*ME/M:.3e}; E1 = E_R dM/M = {ER*dMon*ME/M:.4f} eV;"
          f" off-site sum 14 - {dMon:.2f} = {14 - dMon:.2f} m_e; mass shift M(1 + {dMon*ME/M:.2e})")
