"""Table 18.1 (tab:18-pairs) and the silicon numbers of Sect. 18.4: the energy-only random-k cascade for Si, Ge and GaAs.
Run: python table18_4.py > table18_4.log  (about one minute).  Writes table18_4.json (A_AB) for limit18_4c.py and the theta_ii = 3/2 value of Sect. 18.4.

Inputs (each with its source):
  Si calibration datum: eps_eh = 3.749 +- 0.001 eV and F_eh = 0.119 +- 0.002 at 123 K, 5.9 keV (Rodrigues et al.,
     arXiv:2004.11499, abstract and Sect. 5).  Gap at 123 K: 1.160 eV from Ramanathan and Kurinsky's Eq. (11) (arXiv:2004.10709),
     as in App. E.13.  omega_AB = 63 meV and hole band width B_h = 12 eV (arXiv:2004.10709, Sect. II B and II A), as in App. E.13.
     A_AB = 5.703 eV^3 is fitted to the pair energy alone, in the continuum limit (si_cascade18.py, the one silicon set of
     Chap. 18); F_eh is then a model output.
  Every model value is the continuum limit: steps E_g/N and E_g/(2N), extrapolated in h^(3/2) (si_cascade18.casc_cont).
  Ge: gap at 77 K from Wei, Wang and Mei's Eq. (7), arXiv:1602.08005: E_g(T) = 0.7437 - 4.774e-4 T^2/(T + 235) eV;
     optical phonon 37.6 meV (Table 5.x of Sect. 5.3, tab:5-phonons); measured eps = 2.96 eV at 77 K and F = 0.06-0.13
     (Mei et al., arXiv:1909.05806, Sect. 4.3, quoting earlier experiments).  Low-temperature gap 0.744 eV (tab:3-materials).
  GaAs: gap 1.42 eV at 300 K and 1.52 eV at low temperature (tab:3-materials); LO phonon 36.35 meV (Strauch and Dorner, as in
     Sect. 5.5); measured eps about 4.2 eV at room temperature (Bertuccio and Maiocchi 2002, as quoted by Nielsen and Fischetti,
     arXiv:2610.16949, Fig. 1).  No measured F.
  Ge and GaAs: no hole-band cutoff (B_h = None); X = 60 E_g where lambda = A/E_g^3 > 5 (slow approach to the asymptote), else 40.
"""
import json
import os
import time
import numpy as np
import casc18_4 as C
from si_cascade18 import A_AB, EG_SI, OM_SI, BH_SI, EPS_MEAS, DEPS_MEAS, F_MEAS, DF_MEAS, casc_cont, calibrate

HERE = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

EPS_SI, DEPS_SI = EPS_MEAS, DEPS_MEAS
F_SI, DF_SI = F_MEAS, DF_MEAS
EG_SI_123 = EG_SI

A = A_AB
si = casc_cont(A, EG_SI_123, OM_SI, Bh=BH_SI, X=40.0)
print("calibration (si_cascade18.log): A_AB = %.3f eV^3 gives eps_eh(Si, 123 K) = %.4f eV in the continuum" % (A, si["eps"]))
print("Si (123 K): lambda = %.3f, w = %.4f, eps/E_g = %.4f, F_eh = %.5f" % (si["lam"], si["w"], si["eps_over_Eg"], si["F"]))
print("  measured F = 0.119 +- 0.002: model below by %.2f sigma; ratio meas/model - 1 = %+.2f %%" % ((F_SI - si["F"]) / DF_SI, 100 * (F_SI / si["F"] - 1)))
print("  Lowe-Sareen 0.118 +- 0.004 at 123 K (as quoted by Rodrigues et al.): %.2f sigma above the model" % ((0.118 - si["F"]) / 0.004))
print("  identity eps = E_g + residual + phonon heat per pair: %.4f + %.4f + %.4f = %.4f eV" % (EG_SI_123, si["Rpair"], si["Ppair"], EG_SI_123 + si["Rpair"] + si["Ppair"]))
print("  mean terminal residual per carrier E_f = %.4f eV = %.4f E_g; phonons per pair above threshold r = %.2f" % (si["Rpair"] / 2, si["Rpair"] / 2 / EG_SI_123, si["Ppair"] / OM_SI))
# grid check: the two grids of the extrapolation against the continuum
g1, g2 = si["grid"]
print("  grids E_g/%d and E_g/%d against the continuum: eps %+.3f %% and %+.3f %%, F %+.3f %% and %+.3f %%" %
      (g1["N"], g2["N"], 100 * (g1["eps"] / si["eps"] - 1), 100 * (g2["eps"] / si["eps"] - 1), 100 * (g1["F"] / si["F"] - 1),
       100 * (g2["F"] / si["F"] - 1)))
# sensitivity to the constant (secants at E_g = 1.160 eV)
for s_ in (1.1, 0.9):
    r = casc_cont(s_ * A, EG_SI_123, OM_SI, Bh=BH_SI, X=40.0, sets=("N",))
    print("  A_AB x %.1f: eps %+.2f %%, F %+.2f %%; secant slopes d eps/dA = %.4f eV^-2, dF/dA = %.5f eV^-3" %
          (s_, 100 * (r["eps"] / si["eps"] - 1), 100 * (r["F"] / si["F"] - 1), (r["eps"] - si["eps"]) / ((s_ - 1) * A),
           (r["F"] - si["F"]) / ((s_ - 1) * A)))
# Ramanathan-Kurinsky Eqs. (12)-(13) at 123 K (A = 5.2 in their units), as App. E.13
print("  R&K planes at E_g = 1.160 eV, A = 5.2: eps = %.3f eV, F = %.4f" % (1.7 * 1.160 + 0.084 * 5.2 + 1.3, -0.028 * 1.160 + 0.0015 * 5.2 + 0.14))
siT = casc_cont(A, 1.17, OM_SI, Bh=BH_SI, X=40.0)
print("Si (low T, E_g = 1.17 eV): eps = %.3f eV, F = %.4f" % (siT["eps"], siT["F"]))

def eg_ge(T):
    return 0.7437 - 4.774e-4 * T ** 2 / (T + 235.0)

rows = {}
for name, Eg, om, note in (("Ge 77 K", eg_ge(77.0), 0.0376, "eps meas 2.96 eV"), ("Ge low T", 0.744, 0.0376, ""),
                           ("GaAs 300 K", 1.42, 0.03635, "eps meas ~4.2 eV"), ("GaAs low T", 1.52, 0.03635, "")):
    lam = A / Eg ** 3
    X = 60.0 if lam > 5 else 40.0
    r = casc_cont(A, Eg, om, Bh=None, X=X)
    rows[name] = r
    print("%-11s E_g = %.4f eV, omega = %.2f meV: lambda = %.3f, w = %.4f, eps = %.4f eV (eps/E_g = %.3f), F = %.4f, "
          "E_f/E_g = %.3f  %s" % (name, Eg, 1e3 * om, lam, om / Eg, r["eps"], r["eps_over_Eg"], r["F"], r["Rpair"] / 2 / Eg, note))
ge = rows["Ge 77 K"]
print("Ge: meas/model - 1 = %+.1f %% (model/meas - 1 = %+.1f %%);  F model %.3f against 0.06-0.13 (F at 0.106 from Mei et al.'s own model: %+.0f %%)" % (100 * (2.96 / ge["eps"] - 1), 100 * (ge["eps"] / 2.96 - 1), ge["F"], 100 * (ge["F"] / 0.106 - 1)))
ga = rows["GaAs 300 K"]
print("GaAs: meas/model - 1 = %+.1f %% (model/meas - 1 = %+.1f %%; measured about 4.2 eV at room temperature)" %
      (100 * (4.2 / ga["eps"] - 1), 100 * (ga["eps"] / 4.2 - 1)))
# structural variants, each recalibrated to the silicon pair energy: threshold 3/2 E_g; density of states x^1 (a = 1)
AV = {}
for lab, kw, lo, hi in (("theta_ii = 3/2", dict(theta=1.5, N=74), 5.4, 5.9), ("rho ~ x (a = 1)", dict(a=1.0), 0.6, 0.8)):
    Av = calibrate(EPS_SI, lo=lo, hi=hi, **kw)
    AV[lab] = Av
    rv = casc_cont(Av, EG_SI_123, OM_SI, Bh=BH_SI, X=40.0, **kw)
    print("variant %-15s: A = %.4f (units eV^(3 + 2(a - 1/2)) ), eps = %.4f eV, F = %.4f (%+.1f %% from the base model)" % (lab, Av, rv["eps"], rv["F"], 100 * (rv["F"] / si["F"] - 1)))
# slopes d eps/d E_g of the calibrated cascade at fixed A_AB and omega (secants +- 0.05 eV, continuum)
sl = {}
for name, Eg0, om, Bh in (("Si", 1.17, OM_SI, BH_SI), ("Ge", 0.744, 0.0376, None)):
    X = 60.0 if A / Eg0 ** 3 > 5 else 40.0
    up = casc_cont(A, Eg0 + 0.05, om, Bh=Bh, X=X, sets=("N",))["eps"]
    dn = casc_cont(A, Eg0 - 0.05, om, Bh=Bh, X=X, sets=("N",))["eps"]
    sl[name] = (up - dn) / 0.1
    print("d eps/d E_g at fixed A_AB, %s (E_g = %.3f eV +- 0.05): %.3f" % (name, Eg0, sl[name]))
nB = 1.0 / np.expm1(0.0376 / (8.617333e-5 * 77.0))
print("Bose occupation of the 37.6 meV Ge phonon at 77 K: %.4f; of the 63 meV Si phonon at 123 K: %.2e" % (nB, 1.0 / np.expm1(0.063 / (8.617333e-5 * 123.0))))
json.dump(dict(A_AB=A, Eg_Si_123=EG_SI_123, om_Si=OM_SI, F_Si=si["F"], lam_Si=si["lam"], w_Si=si["w"],
               A_theta32=AV["theta_ii = 3/2"], eps_Si_lowT=siT["eps"], eps_Ge_lowT=rows["Ge low T"]["eps"],
               eps_GaAs_lowT=rows["GaAs low T"]["eps"], deps_dEg_Si=sl["Si"], deps_dEg_Ge=sl["Ge"]),
          open(os.path.join(HERE, "table18_4.json"), "w"), indent=1)
print("done in %.0f s" % (time.time() - t0))
