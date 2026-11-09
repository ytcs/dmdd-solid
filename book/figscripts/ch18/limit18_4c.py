"""Limit Check 18.4c (lim:18.4c, fig:18-limit-c), the validated range, the material predictions and Worked example 18.4.
Run: python limit18_4c.py > limit18_4c.log  (several minutes on three cores).  A_AB = 5.703 eV^3 from si_cascade18.py.
Every cascade value is the continuum limit (steps E_g/N and E_g/(2N), extrapolated in h^(3/2); si_cascade18.casc_cont), except
for the crystals whose phonon step needs N > 200 (NaI, CsI, NaCl, NaF, CaF2: w < 0.005, outside the validated range), solved on one grid.

(1) Scan of the cascade (casc18_4.py; theta_ii = 1, a = 1/2, no hole cutoff, A_AB of the silicon calibration) over
    lambda = A_AB/E_g^3 in [0.003, 100] (10 log-spaced values) and w = omega_AB/E_g in {0.01, 0.02, 0.035, 0.05, 0.075, 0.1};
    X = 25 E_g (60 E_g for lambda > 5).  Fitted:  eps/E_g = c0 + c1 (lambda w^gamma)^beta  (least squares in the relative error).
    With lambda = A/E_g^3 this reads  eps = c0 E_g + k2,  k2 = c1 (A omega^gamma)^beta E_g^{1 - (3 + gamma) beta}.
(2) Validation against measured pair energies (inputs and measurements with sources):
    Ge     E_g(77 K) 0.7346 eV (arXiv:1602.08005 Eq. (7)), omega 37.6 meV (tab:5-phonons); eps 2.96 eV (arXiv:1909.05806 Sect. 4.3)
    C      E_g 5.47 eV, omega_O 161 meV (Griffin et al., arXiv:1910.10716, Table I); eps = inverse-variance mean of 13.1 +- 0.2,
           13.25 +- 0.50, 13.05 +- 0.20, 12.82 +- 0.13 eV (Nielsen and Fischetti, arXiv:2311.05011, Sect. III)
    4H-SiC E_g 3.26 eV, omega_LO 120.0 meV (Griffin et al., arXiv:2008.08560, Table I); eps 7.83 +- 0.02 eV (Gsponer et al.,
           arXiv:2311.03902)
    6H-SiC E_g 3.02 eV, omega_LO 120.0 meV (arXiv:2008.08560 Table I); eps 6.7 eV (ibid., Table I, quoting its Ref. 34)
    3C-SiC E_g 2.39 eV, omega_LO 120.5 meV (arXiv:2008.08560 Table I); eps 6.90 eV (arXiv:2610.16949 Table II, quoting Makarov)
    GaN    E_g 3.43 eV, omega_O 88.9 meV (arXiv:1910.10716 Table I); eps 9.59 eV, electron-beam induced current (arXiv:2308.03893
           Sect. IV, quoting its Ref. 100)
    SiO2   E_g 9.2 eV, omega_O 149 meV (arXiv:1910.10716 Table I); eps 18.0 eV (arXiv:2610.16949 Table II, quoting Ausman and McLean)
    Residual = model/measured - 1 (the one convention of Chap. 18).  Validated range: lambda and w spanned by these materials and silicon.
(3) Predictions for the 24 crystals of Griffin et al. Table I (E_g, highest optical phonon omega_O), the inputs of Chap. 17; for
    Si, Ge, GaAs the book values of Table 18.1 are used instead.
(4) Worked example 18.4: GaAs at the low-temperature gap 1.52 eV and omega_LO = 36.35 meV.
Plot: eps_eh against E_g; validity region shaded = E_g range of the measured set (0.73 - 9.2 eV).
"""
import json
import os
import time
from multiprocessing import Pool
import numpy as np
from scipy.optimize import least_squares
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import casc18_4 as C
from si_cascade18 import A_AB, casc_cont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch18")
os.makedirs(OUT, exist_ok=True)
A = A_AB


def job(args):
    lam, w = args
    X = 60.0 if lam > 5 else 25.0
    r = casc_cont(lam, 1.0, w, Bh=None, X=X, sets=("N",))
    return lam, w, r["eps_over_Eg"], r["F"]


def job_mat(args):
    name, Eg, om = args
    lam = A / Eg ** 3
    X = 60.0 if lam > 5 else 25.0
    if C.grid(om / Eg) <= 200:
        r = casc_cont(A, Eg, om, Bh=None, X=X, sets=("N",))
    else:   # phonon step below 0.005 E_g (NaI, CsI, NaCl, NaF, CaF2): one grid, step ~ omega_AB; continuum extrapolation too slow here
        r = C.run(A, Eg, om, X=X, sets=("N",))
    return name, Eg, om, r["eps"], r["F"]


MEAS = {"Ge": (0.7346, 0.0376, 2.96), "C": (5.47, 0.161, None), "4H-SiC": (3.26, 0.1200, 7.83), "6H-SiC": (3.02, 0.1200, 6.7),
        "3C-SiC": (2.39, 0.1205, 6.90), "GaN": (3.43, 0.0889, 9.59), "SiO2": (9.2, 0.149, 18.0)}
cv = np.array([13.1, 13.25, 13.05, 12.82])
cs = np.array([0.2, 0.5, 0.2, 0.13])
wmean = np.sum(cv / cs ** 2) / np.sum(1 / cs ** 2)
MEAS["C"] = (5.47, 0.161, wmean)

GRIFFIN = [("NaI", 5.8, 0.0200), ("CsI", 6.14, 0.0100), ("CaWO4", 5.2, 0.106), ("Al2O3", 8.8, 0.104), ("diamond", 5.47, 0.161),
           ("SiO2", 9.2, 0.149), ("PbTe", 0.19, 0.0135), ("InSb", 0.24, 0.0215), ("AlN", 6.20, 0.109), ("CaF2", 11.81, 0.0556),
           ("GaN", 3.43, 0.0889), ("GaSb", 0.720, 0.0273), ("LiF", 14.2, 0.0772), ("MgF2", 12.4, 0.0737), ("MgO", 7.83, 0.0826),
           ("NaCl", 8.75, 0.0306), ("NaF", 11.5, 0.0499), ("PbS", 0.29, 0.0269), ("PbSe", 0.17, 0.0171), ("ZnO", 3.3, 0.0634),
           ("ZnS", 3.80, 0.0410), ("Si", 1.17, 0.063), ("Ge", 0.744, 0.0376), ("GaAs", 1.52, 0.03635)]

if __name__ == "__main__":
    t0 = time.time()
    print("A_AB = %.3f eV^3 (continuum silicon calibration, si_cascade18.log); inverse-variance mean for diamond: %.3f eV (plain %.3f)"
          % (A, wmean, cv.mean()))
    lams = 10 ** np.linspace(np.log10(0.003), 2.0, 10)
    ws = [0.01, 0.02, 0.035, 0.05, 0.075, 0.1]
    tasks = [(l, w) for l in lams for w in ws]
    mats = [(n, e, o) for n, e, o in GRIFFIN] + [(n + " (meas)", v[0], v[1]) for n, v in MEAS.items()]
    cache = os.path.join(HERE, "limit18_4c_scan.json")
    if os.path.exists(cache):
        scan = [tuple(v) for v in json.load(open(cache))]
        print("scan read from limit18_4c_scan.json (written by an earlier run of this script)")
    else:
        with Pool(3) as pool:
            scan = pool.map(job, tasks)
        json.dump([list(map(float, v)) for v in scan], open(cache, "w"))
    with Pool(3) as pool:
        mres = pool.map(job_mat, mats)
    print("scan and materials done in %.0f s" % (time.time() - t0))
    lam_a = np.array([s[0] for s in scan]); w_a = np.array([s[1] for s in scan]); e_a = np.array([s[2] for s in scan])
    F_a = np.array([s[3] for s in scan])

    def model(p, l, w):
        return p[0] + p[1] * (l * w ** p[2]) ** p[3]
    fit = least_squares(lambda p: model(p, lam_a, w_a) / e_a - 1, [1.6, 2.3, 0.96, 0.24])
    c0, c1, g, b = fit.x
    rel = model(fit.x, lam_a, w_a) / e_a - 1
    print("fit eps/E_g = %.4f + %.4f (lambda w^%.4f)^%.4f : max |rel| %.2f %%, rms %.2f %% over %d points"
          % (c0, c1, g, b, 100 * np.abs(rel).max(), 100 * np.sqrt(np.mean(rel ** 2)), len(rel)))
    print("  eps/E_g range of the scan %.3f - %.3f; F range %.4f - %.4f" % (e_a.min(), e_a.max(), F_a.min(), F_a.max()))
    ex = 1 - (3 + g) * b
    print("  k2 = %.3f (A omega^%.3f)^%.4f E_g^%.4f  (A in eV^3, energies in eV)" % (c1, g, b, ex))
    k2 = lambda Eg, om: c1 * (A * om ** g) ** b * Eg ** ex
    print("  k2(Si: E_g 1.17 eV, 63 meV) = %.3f eV; k2(E_g 1.16, 63 meV) = %.3f eV" % (k2(1.17, 0.063), k2(1.16, 0.063)))

    def dom(Eg, om):
        lam, w = A / Eg ** 3, om / Eg
        return 0.003 <= lam <= 100 and 0.01 <= w <= 0.1

    print("\nvalidation (residual = model / measured - 1):")
    resid = []
    mm = {r[0]: r for r in mres}
    lv, wv = [A / 1.160 ** 3], [0.063 / 1.160]
    for n, (Eg, om, em) in MEAS.items():
        r = mm[n + " (meas)"]
        res = r[3] / em - 1
        resid.append(res)
        lv.append(A / Eg ** 3); wv.append(om / Eg)
        lin = c0 * Eg + k2(Eg, om)
        print("  %-7s E_g %.3f omega %.4f lambda %.4f w %.4f: model %.3f eV (linear law %.3f), measured %.3f eV, residual %+.1f %%, F %.4f"
              % (n, Eg, om, A / Eg ** 3, om / Eg, r[3], lin, em, 100 * res, r[4]))
    resid = np.array(resid)
    print("  range %+.1f %% to %+.1f %%, mean %+.1f %%, rms %.1f %% (7 materials)"
          % (100 * resid.min(), 100 * resid.max(), 100 * resid.mean(), 100 * np.sqrt(np.mean(resid ** 2))))
    rr = np.array([round(100 * v, 1) for v in resid])
    print("  from the rounded residuals as tabulated: mean %+.1f %%, rms %.1f %%" % (rr.mean(), np.sqrt(np.mean(rr ** 2))))
    # full-band Monte Carlo of Nielsen and Fischetti for silicon, 3.1 eV (arXiv:2610.16949, Sect. III), against the 123 K value
    # 3.749 eV and the room-temperature value of about 3.6 eV that the source compares with
    print("  full-band silicon pair energy 3.1 eV: model/measured - 1 = %+.1f %% against 3.749 eV, %+.1f %% against 3.6 eV"
          % (100 * (3.1 / 3.749 - 1), 100 * (3.1 / 3.6 - 1)))
    for n, fb in (("3C-SiC", 6.6), ("4H-SiC", 7.3), ("GaN", 8.9), ("C", 12.87), ("SiO2", 16.7)):
        em = MEAS[n][2]
        print("  full band %-6s %.2f eV: model/measured - 1 = %+.1f %% (cascade %+.1f %%)" % (n, fb, 100 * (fb / em - 1),
                                                                                         100 * (mm[n + " (meas)"][3] / em - 1)))
    print("validated range: lambda %.4f - %.2f, w %.4f - %.4f, E_g 0.73 - 9.2 eV" % (min(lv), max(lv), min(wv), max(wv)))
    LMIN, LMAX, WMIN, WMAX = min(lv), max(lv), min(wv), max(wv)

    def valid(Eg, om):
        lam, w = A / Eg ** 3, om / Eg
        return LMIN * 0.999 <= lam <= LMAX * 1.001 and WMIN * 0.999 <= w <= WMAX * 1.001

    print("\npredictions (Griffin et al. Table I inputs; Si, Ge, GaAs at the book low-temperature values):")
    print("  material  E_g    omega   lambda    w       eps(eV)  eps/E_g  F      linear law  k2    fit domain  validated range")
    k2s_in, k2s_all = [], []
    for n, Eg, om, e, F in mres:
        if "(meas)" in n:
            continue
        lam, w = A / Eg ** 3, om / Eg
        kk = k2(Eg, om)
        k2s_all.append(kk)
        if dom(Eg, om):
            k2s_in.append(kk)
        print("  %-8s %6.3f  %.4f  %8.4g  %.4f  %7.3f  %6.3f  %.4f  %7.3f   %5.2f  %-5s       %s"
              % (n, Eg, om, lam, w, e, e / Eg, F, c0 * Eg + kk, kk, dom(Eg, om), valid(Eg, om)))
    print("k2 over the 24 crystals: %.2f - %.2f eV; inside the fit domain: %.2f - %.2f eV" % (min(k2s_all), max(k2s_all), min(k2s_in), max(k2s_in)))

    # Worked example 18.4: GaAs
    Eg, om = 1.52, 0.03635
    lam, w = A / Eg ** 3, om / Eg
    u = (lam * w ** g) ** b
    print("\nWE 18.4 GaAs (E_g 1.52 eV, omega_LO 36.35 meV): lambda = %.4f, w = %.5f, w^gamma = %.5f, lambda w^gamma = %.5f, (.)^beta = %.4f"
          % (lam, w, w ** g, lam * w ** g, u))
    print("  eps/E_g = %.4f + %.4f x %.4f = %.4f; eps = %.3f eV; k2 = %.3f eV; 1.61 E_g = %.3f eV" % (c0, c1, u, c0 + c1 * u, (c0 + c1 * u) * Eg, k2(Eg, om), c0 * Eg))
    print("  cascade itself: %.3f eV (Table 18.1); empirical 1.54 E_g + 1.89 = %.3f eV; Klein 2.8 E_g + 0.5 = %.3f eV" % (mm["GaAs"][3], 1.54 * Eg + 1.89, 2.8 * Eg + 0.5))
    Eg3 = 1.42
    print("  at 300 K (E_g 1.42 eV): linear law %.3f eV against about 4.2 eV measured" % (c0 * Eg3 + k2(Eg3, om)))
    print("  Klein at 1.52 eV with r_K omega_K = 0.5 eV: %.2f eV; empirical at 1.42 eV: %.3f" % (2.8 * 1.52 + 0.5, 1.54 * 1.42 + 1.89))

    # plot
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    ax.axvspan(0.73, 9.2, color="0.9", lw=0)
    Eg_l = np.logspace(np.log10(0.12), np.log10(20), 200)
    ax.fill_between(Eg_l, c0 * Eg_l + min(k2s_in), c0 * Eg_l + max(k2s_in), color="C0", alpha=0.15, lw=0)
    ax.plot(Eg_l, c0 * Eg_l + k2(1.17, 0.063) * (Eg_l / 1.17) ** 0, color="C0", lw=1.2, label=r"$1.61E_{\mathrm{g}} + k_2$, $k_2$ = %.2f eV (band: in-domain $k_2$)" % k2(1.17, 0.063))
    ax.plot(Eg_l, 1.54 * Eg_l + 1.89, color="k", lw=1.0, ls="--", label=r"$1.54E_{\mathrm{g}} + 1.89$ eV (fit to data)")
    first = [True, True]
    for n, Eg, om, e, F in mres:
        if "(meas)" in n:
            continue
        inside = dom(Eg, om)
        ax.plot([Eg], [e], "o" if inside else "x", ms=4, color="C0" if inside else "C3", mfc="C0" if inside else "none",
                label=("cascade, inside fit domain" if inside and first[0] else ("cascade, outside" if (not inside and first[1]) else None)))
        if inside:
            first[0] = False
        else:
            first[1] = False
    fm = True
    for n, (Eg, om, em) in list(MEAS.items()) + [("Si", (1.160, 0.063, 3.749))]:
        ax.plot([Eg], [em], "s", ms=5, mfc="none", color="C2", label="measured" if fm else None)
        fm = False
    for n, Eg, om, e, F in mres:
        if n in ("LiF", "CsI", "PbSe", "Ge", "Si", "GaAs", "NaF", "Al2O3", "diamond"):
            # CaWO4 and diamond sit close together: label them to the left, one above and one below
            off, ha = {"CaWO4": ((-4, -9), "right"), "diamond": ((-4, 4), "right")}.get(n, ((4, -9), "left"))
            ax.annotate(n.replace("2", "$_2$").replace("4", "$_4$").replace("3", "$_3$"), (Eg, e), xytext=off, textcoords="offset points", fontsize=6.5, color="0.25", ha=ha)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(0.12, 20); ax.set_ylim(1, 40)
    ax.set_xlabel(r"gap $E_{\mathrm{g}}$ (eV)")
    ax.set_ylabel(r"$\varepsilon_{\mathrm{eh}}$ (eV)")
    ax.legend(fontsize=7, loc="upper left", frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "limit18_4c.pdf"))
    print("wrote limit18_4c.pdf; total %.0f s" % (time.time() - t0))
