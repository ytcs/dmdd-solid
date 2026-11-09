"""Limit Check 15.2a (lim:15.2a, fig:15-limit-edge), Table 15.1 (tab:15-edge) and Worked example 15.2 (we:15-edge).

Loss function of aluminum at the pair-breaking edge, divided by the normal-state Lindhard loss function, along the
kinematic edge q = omega/v_max (the smallest momentum transfer that can deposit omega), as a function of y = omega/Delta_BCS.

Inputs (book values): v_max = 2.650e-3 (794.5 km/s, Sect. 1.2); v_F = 6.753e-3 and E_F = 11.65 eV, the free-electron
gas with m* = m_e of al_constants.py; Delta_BCS = 0.18 meV (Sect. 7.2).
On the edge w = omega/(q v_F) = v_max/v_F = 0.3924 for every y (fraktur w in the book), and Q = q v_F/Delta = y/w.

Curves (edge15.py; App. D.39):
  literature form = loss function of the bare BCS dielectric function, Gan et al. 2609.06423 Eqs. (8)-(9), evaluated
    in closed form: direct bare bubble (Eq. 15.1-Rcons without the ladder) and the resummed form Eq. (15.2-LBCS) with the
    Kramers-Kronig shift integrated to infinity (KK-inf) and cut at omega' = q v_F (cut);
  normal-state screening, Gan et al. Eq. (10): L = g_I L_nor;
  first-order form of Sect. 15.1: g_I L_nor [1 - 2 (Delta/q v_F) s_BCS];
  fuller result: conserving response (pair-phase ladder of Eq. 7.2-Rc, Coulomb screening), clean, T = 0;
  markers: conserving response with Born impurity scattering, mean free path 1 um and 30 nm (normal state at the same
    scattering rate), read from impurity.csv (a T = 0 calculation with the impurity ladder in both the bubble and the
    pair channel; rate 1/tau = v_F/l_e with v_F = 6.8e-3 in the l_e labels; computed at v_max/v_F = 0.390, which
    differs from the book's 0.392 by 0.6 % (the clean column changes by at most 0.004, logged below); with the book's
    v_F the labels 1.007 um and 30.1 nm become 1.000 um and 29.9 nm).
Shaded: L_bare/L_cons >= 0.9 (validity of the literature form).  The normal-state screening g_I L_nor is shown in
Limit Check 15.1a and is not repeated here.
Outputs: tex/figures/ch15/limit15_2a.pdf; figscripts/ch15/limit15_2a.log.
"""
import os
import sys
import csv
import warnings
import numpy as np
from scipy import optimize, integrate
import matplotlib
import matplotlib.ticker
matplotlib.use("Agg")
import matplotlib.pyplot as plt

warnings.simplefilter("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edge15 as e

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch15", "limit15_2a.pdf")
LOG = open(os.path.join(HERE, "limit15_2a.log"), "w")


def out(s):
    print(s)
    LOG.write(s + "\n")


import al_constants as alc
VMAX, VF, DELTA, EF, ME = alc.VMAX, alc.VF, alc.DELTA, alc.EF, alc.ME
NU = VMAX / VF
out(f"v_max/v_F = {NU:.4f}")
out(f"Re Lindhard bracket at nu: 1 - (nu/2)ln((1+nu)/(1-nu)) = {e.ref_lin(NU):.4f}; r_eps = (pi/2)nu/bracket = "
    f"{0.5*np.pi*NU/e.ref_lin(NU):.4f}; 1/bracket = {1/e.ref_lin(NU):.3f}")

# ---------------------------------------------------------------- checks
out("\nChecks")
for y in (2.2, 3.0, 5.0, 10.0):
    out(f"  g_I closed form vs Eq. 7.2-pairspec integral, y = {y}: {e.g_I(np.array([y]))[0]:.12f} vs {e.g_I_integral(y):.12f}")
out(f"  s_BCS(y -> 0) (static screening unchanged): s_BCS(1e-3) = {e.s_BCS(1e-3):.1e}")
for y, Q in ((2.2, 2.2 / NU), (3.0, 3.0 / NU), (10.0, 10.0 / NU), (3.0, 3.2)):
    o = e.responses(y, Q)
    out(f"  Im P33/Im P_nor - g_I at (y, Q) = ({y}, {Q:.3f}), omega < q v_F: {o['ImRatio'] - o['g']:.1e}")
for Q in (0.01, 0.1):
    o = e.responses(2.5, Q)
    out(f"  conservation, Q = {Q}, y = 2.5: P_cons = {o['Pc'].real:.4e}, Q^2/(3y^2) = {Q*Q/(3*6.25):.4e}; "
        f"bare P33 = {o['P33'].real:.4f}")
o = e.responses(50.0, 50.0 / NU)
out(f"  normal limit y = 50: L_cons/L_nor = {o['Lcons_nor']:.5f}, g_I = {o['g']:.5f}")
o = e.responses(0.01, 5.0)
out(f"  static limit y = 0.01, Q = 5: P_cons = {o['Pc'].real:.5f} (epsilon = 1 + k_TF^2/q^2 needs -1)")


# L-level sum rule: (2/pi) int dy Im(1/P)/y over y > 2 equals 4/5 if no weight below 2 Delta
def sumrule(Q, which):
    f = lambda y: (1 / e.responses(y, Q)[which]).imag / y
    a, _ = integrate.quad(f, 2.0, 2.0 + 1e-6, limit=50)
    b, _ = integrate.quad(f, 2.0 + 1e-6, 4 * Q, limit=400)
    c, _ = integrate.quad(f, 4 * Q, 400 * Q, limit=400)
    return 2 / np.pi * (a + b + c)


for Q in (5.0, 12.0):
    o = e.responses(1000.0, Q)
    out(f"  large-omega constant of 2N_F/R_cons - 3(omega/qv_F)^2 at y = 1000, Q = {Q}: {(1/o['Pc']).real - 3e6/Q/Q:.4f} (-9/5 = -1.8)")
fnor = lambda y, Q: (1 / e.P_nor(y / Q)).imag / y
for Q in (5.0, 12.0):
    a, _ = integrate.quad(lambda y: fnor(y, Q), 0.0, Q, limit=400)
    out(f"  same integral for the normal metal from y = 0 at Q = {Q}: {2/np.pi*a:.4f}")
for Q in (5.0, 12.0):
    out(f"  L sum rule (2/pi) int_2 dy Im(1/P_cons)/y at Q = {Q}: {sumrule(Q, 'Pc'):.4f} (normal metal: 0.8)")

# ---------------------------------------------------------------- Table 15.1
out("\nTable 15.1 (edge q = omega/v_max)")
ys = (2.05, 2.2, 2.5, 3.0, 5.0, 10.0)
tab = {}
for y in ys:
    Q = y / NU
    o = e.responses(y, Q)
    a = e.resummed(y, Q)
    b = e.resummed(y, Q, ycut=Q)
    t = dict(Q=Q, g=o["g"], s=a["s"], scut=b["s"], d=a["d"], first=a["first"], kk=a["ratio"], cut=b["ratio"],
             bare=o["Lbare_nor"] / o["g"], cons=o["Lcons_nor"] / o["g"], consL=o["Lcons_nor"], v=o["v"],
             absr=o["absratio"], dq=1 / Q)
    tab[y] = t
    out(f"  y = {y:5.2f}: Q = {Q:6.2f}, Delta/qv_F = {1/Q:.4f}, g_I = {t['g']:.3f}, s_BCS = {t['s']:.2f} (cut {t['scut']:.2f}), "
        f"delta_s = {t['d']:.3f}, first-order 2(Delta/qv_F)s = {t['first']:.3f}")
    out(f"            L/(g_I L_nor): resummed KK-inf {t['kk']:.3f}, cut {t['cut']:.3f}, bare direct {t['bare']:.3f} "
        f"(direct/KK-inf - 1 = {t['bare']/t['kk']-1:+.3f}); conserving {t['cons']:.3f}; L_cons/L_nor = {t['consL']:.3f}; "
        f"vertex fraction v = {t['v']:.3f}; |eps_cons|/|eps_nor| = {t['absr']:.3f}")

for y in (3.0, 5.0, 10.0):
    o = e.responses(y, y / NU)
    out(f"  bare |eps|^2/|eps_nor|^2 on the edge at y = {y}: {abs(o['P33'])**2/abs(o['Pn'])**2:.3f}")

# Anderson-Bogoliubov zero of <(omega^2 - s^2) F> below 2 Delta (pole of R_cons, zero of L)
out("Anderson-Bogoliubov pole of R_cons below 2 Delta, at the edge momentum of y = 2.2, 2.5, 3:")
for y in (2.2, 2.5, 3.0):
    Q = y / NU
    g = lambda w: e._avg(lambda s_, yy: (yy * yy - s_ * s_) * e.tsuneto((yy * yy - s_ * s_) / 4), w, Q).real
    wab = optimize.brentq(g, 0.5, 2 - 1e-12)
    out(f"  Q = {Q:.2f}: omega_AB/Delta = {wab:.4f} (2 - omega_AB/Delta = {2 - wab:.4f}); Q/sqrt(3) = {Q/np.sqrt(3):.2f}")

out("Share of the Anderson-Bogoliubov pole in the shift Re(P_cons - P_nor) on the edge (pole term 2 r y_AB/(y^2 - y_AB^2),"
    " r the residue of the ladder at y_AB at the same Q):")
for y in (2.2, 2.5, 3.0, 5.0):
    Q = y / NU
    Dfun = lambda w: e._avg(lambda s_, yy: (yy * yy - s_ * s_) * e.tsuneto((yy * yy - s_ * s_) / 4), w, Q).real
    if Q / np.sqrt(3) > 2 and Dfun(2 - 1e-9) * Dfun(0.5) > 0:
        o = e.responses(y, Q)
        out(f"  y = {y}: Q = {Q:.2f}, no zero of the ladder denominator below 2 Delta; pole share 0; total shift "
            f"{(o['Pc'] - o['Pn']).real:.3f}")
        continue
    wab = optimize.brentq(Dfun, 0.5, 2 - 1e-12)
    h = 1e-6
    dD = (Dfun(wab + h) - Dfun(wab - h)) / (2 * h)
    Fab = e._avg(lambda s_, yy: e.tsuneto((yy * yy - s_ * s_) / 4), wab, Q).real
    r = -wab * wab * Fab**2 / dD
    o = e.responses(y, Q)
    tot = (o["Pc"] - o["Pn"]).real
    pole = 2 * r * wab / (y * y - wab * wab)
    out(f"  y = {y}: Q = {Q:.2f}, y_AB = {wab:.4f}, pole term {pole:.3f} of total {tot:.3f} (share {pole/tot:.2f})")
out("Real part of the conserving dielectric function relative to the normal one on the edge, 1 + delta = Re P_cons/Re P_nor:")
for y in (2.05, 2.2, 2.5, 3.0):
    o = e.responses(y, y / NU)
    out(f"  y = {y}: 1 + delta = {o['Pc'].real/o['Pn'].real:+.3f}")
out("Bare over conserving on the edge (direct bare; resummed KK-inf):")
for y in ys:
    t = tab[y]
    out(f"  y = {y}: {t['bare']/t['cons']:.3f}; {t['kk']/t['cons']:.3f}")

# first-order expansion fails: 2(Delta/q v_F) s_BCS = 0.3
f1 = lambda y: 2 * NU / y * e.s_BCS(y) - 0.3
f2 = lambda y: 2 * NU / y * e.s_BCS(y, ycut=y / NU) - 0.3
ym = optimize.brentq(f1, 3.0, 5.0)
ymc = optimize.brentq(f2, 2.3, 5.0)
out(f"\nFirst-order term 2(Delta/qv_F)s_BCS = 0.3 at y = {ym:.2f} (KK-inf), {ymc:.2f} (cut)")
# log-log interpolation of the tabulated KK-inf column between y = 3 and 5
l3, l5 = tab[3.0]["first"], tab[5.0]["first"]
yi = 3 * (5 / 3) ** (np.log(0.3 / l3) / np.log(l5 / l3))
out(f"  log-log interpolation between y = 3 ({l3:.3f}) and 5 ({l5:.3f}): y = {yi:.2f}")

# validity of the literature form: |L_bare/L_cons - 1| <= 0.1
fv = lambda y: (lambda o: o["Lbare_nor"] / o["Lcons_nor"] - 0.9)(e.responses(y, y / NU))
yv = optimize.brentq(fv, 5.0, 20.0)
out(f"Bare within 10 % of conserving for y >= {yv:.2f} on the edge")
# normal-screening form g_I L_nor within 10 % of conserving
fn = lambda y: (lambda o: o["Lcons_nor"] / o["g"] - 0.9)(e.responses(y, y / NU))
yn = optimize.brentq(fn, 2.05, 2.5)
out(f"g_I L_nor within 10 % of conserving (clean) for y >= {yn:.3f}; max of L_cons/(g_I L_nor) on y in [2.5, 20]:")
yy = np.linspace(2.5, 20, 176)
cc = np.array([e.responses(y, y / NU)["Lcons_nor"] / e.g_I(np.array([y]))[0] for y in yy])
out(f"  {cc.max():.3f} at y = {yy[cc.argmax()]:.1f}")
yx = optimize.brentq(lambda y: e.responses(y, y / NU)["Lcons_nor"] / e.g_I(np.array([y]))[0] - 1, 2.3, 3.0)
out(f"  L_cons rises above g_I L_nor at y = {yx:.3f} on the edge")

# away from the edge: q = 2, 8 times the edge value
out("\nAway from the edge (conserving, clean): L/(g_I L_nor) and v")
for y in (2.2, 3.0, 5.0, 10.0):
    for m in (2, 8):
        o = e.responses(y, m * y / NU)
        out(f"  y = {y}, q = {m} x edge: L/(g_I L_nor) = {o['Lcons_nor']/o['g']:.3f}, bare {o['Lbare_nor']/o['g']:.3f}, v = {o['v']:.4f}")

# threshold
out("\nThreshold behaviour on the edge Q = 2/nu")
Q0 = 2 / NU
for dy in (1e-6, 1e-4, 1e-3, 1e-2, 0.03, 0.1):
    o = e.responses(2 + dy, Q0)
    out(f"  y - 2 = {dy:.0e}: L_cons/L_nor = {o['Lcons_nor']:.3f}, L_bare/L_nor = {o['Lbare_nor']:.3f}, g_I = {o['g']:.4f}")
out(f"  y - 2 = 0.03 corresponds to {0.03*DELTA*1e6:.1f} micro-eV")
for dy in (1e-4, 1e-2, 0.1):
    o = e.responses(2 + dy, Q0)
    out(f"  conserving Im eps/Im eps_nor at y - 2 = {dy:.0e}: {o['Pc'].imag/o['Pn'].imag:.3f} (bare {o['ImRatio']:.3f})")
yy2 = np.linspace(2.3, 4.0, 69)
cl = np.array([e.responses(y, y / NU)["Lcons_nor"] for y in yy2])
out(f"  maximum of L_cons/L_nor on the edge: {cl.max():.3f} at y = {yy2[cl.argmax()]:.2f}")
out("Size of the vertex term in the response, |R_cons - R_bare|/|R_bare| x (q v_F/Delta)^2 at y = 3:")
for Q in (3.0 / NU, 20.0, 100.0, 1000.0):
    o = e.responses(3.0, Q)
    out(f"  Q = {Q:.2f}: {abs(o['Pc'] - o['P33'])/abs(o['P33'])*Q*Q:.1f}")

# Worked example 15.2 at y = 3
out("\nWorked example 15.2 (y = 3)")
y = 3.0
w = y * DELTA
q = w / VMAX
out(f"  omega = 3 Delta = {w*1e3:.2f} meV; edge q = omega/v_max = {q:.4f} eV; 1/q = {197.327e-9/q*1e6:.2f} micro-m;"
    f" q v_F = {q*VF*1e3:.3f} meV = {q*VF/DELTA:.2f} Delta; Delta/q v_F = {DELTA/(q*VF):.4f}")
t = tab[3.0]
out(f"  g_I(3) = {t['g']:.4f}; s_BCS(3) = {t['s']:.3f}; delta_s = (Delta/qv_F) s/bracket = {t['d']:.4f};"
    f" r_eps = {0.5*np.pi*NU/e.ref_lin(NU):.4f}")
r = 0.5 * np.pi * NU / e.ref_lin(NU)
num = 1 + r * r
den = (1 + t["d"]) ** 2 + t["g"] ** 2 * r * r
out(f"  numerator 1 + r^2 = {num:.4f}; (1 + delta)^2 = {(1+t['d'])**2:.4f}; g^2 r^2 = {t['g']**2*r*r:.4f}; ratio = {num/den:.4f}")
out(f"  first order 1 - 2(Delta/qv_F)s_BCS = {1 - t['first']:.3f}")
out(f"  the two first-order terms of the resummed form: 2 delta_s = {2*t['d']:.3f}; (g_I^2 - 1) r^2 = {(t['g']**2 - 1)*r*r:.3f}")
out(f"  bare L/L_nor = g_I x {t['kk']:.3f} = {t['g']*t['kk']:.3f}; conserving L/L_nor = {t['consL']:.3f}")
kF = np.sqrt(2 * ME * EF)
kTF2 = 4 / 137.036 / np.pi * ME * kF
out(f"  dropped '1' of epsilon: q^2/k_TF^2 = {q*q/kTF2:.1e} (k_TF = {np.sqrt(kTF2):.0f} eV from E_F)")
o = e.responses(3.0, 3.0 / NU)
out(f"  conserving Im/Im_nor = g_I (1 + v) = {t['g']*(1+o['v']):.4f}; Re P_cons/Re P_nor = {o['Pc'].real/o['Pn'].real:.4f}"
    f" (bare {o['P33'].real/o['Pn'].real:.4f})")

# ---------------------------------------------------------------- impurity columns
imp = {}
with open(os.path.join(HERE, "impurity.csv")) as fh:
    for row in csv.DictReader(fh):
        imp[(float(row["Gam"]), float(row["y"]))] = (float(row["l_nm"]), float(row["L_over_gLnor"]))
out("\nConserving response with impurities, L/(g_I L_nor(same rate)) on the edge (v_max/v_F = 0.39)")
gams = sorted(set(k[0] for k in imp))
for G in gams:
    if G < 0.03:
        continue
    l = imp[(G, 2.2)][0]
    row = "  ".join(f"y={y}: {imp[(G, y)][1]:.3f}" for y in (2.05, 2.2, 2.5, 3.0, 5.0, 10.0))
    out(f"  l_e = {l/1e3:9.2f} um (Gamma = 1/(2 tau Delta) = {G}): {row}")
for y in (3.0, 5.0, 10.0):
    vals = [imp[(G, y)][1] for G in gams if G >= 0.03]
    out(f"  spread at y = {y} over l_e = 30 nm ... 100 um: {min(vals):.3f} to {max(vals):.3f}")
out("Clean column at v_max/v_F = 0.390 (impurity data) against the book's x: " + "  ".join(
    f"y={y}: {imp[(0.037, y)][1] - tab[y]['cons']:+.4f}" for y in (2.05, 2.2, 2.5, 3.0, 5.0, 10.0)))
out("\nExclusion criterion (the energies removed from the signal region near the edge): keep y where the conserving value"
    " L_cons/(g_I L_nor(same rate)) on the edge varies by at most 10 % (max/min <= 1.1) over l_e = 30 nm ... 100 um:")
keep = []
for y in (2.05, 2.2, 2.5, 3.0, 5.0, 10.0):
    vals = [imp[(G, y)][1] for G in gams if G >= 0.03]
    ok = max(vals) / min(vals) <= 1.1
    keep.append(ok)
    out(f"  y = {y}: max/min = {max(vals)/min(vals):.3f} -> {'kept' if ok else 'excluded'}")
ycut = [y for y, k in zip((2.05, 2.2, 2.5, 3.0, 5.0, 10.0), keep) if k][0]
out(f"  smallest computed y with the criterion met at it and above: y = {ycut} (the boundary lies between 2.5 and 3);"
    f" exclusion y < {ycut}")

# ---------------------------------------------------------------- figure
yg = np.unique(np.concatenate([2 + np.logspace(-3, 0, 40), np.linspace(3, 30, 60)]))
bare, cons, kk, cut, gI, fo = [], [], [], [], [], []
for y in yg:
    Q = y / NU
    o = e.responses(y, Q)
    a = e.resummed(y, Q)
    b = e.resummed(y, Q, ycut=Q)
    bare.append(o["Lbare_nor"]); cons.append(o["Lcons_nor"])
    kk.append(a["ratio"] * a["g"]); cut.append(b["ratio"] * b["g"]); gI.append(a["g"])
    fo.append(a["g"] * (1 - a["first"]))
bare, cons, kk, cut, gI, fo = map(np.array, (bare, cons, kk, cut, gI, fo))

plt.rcParams.update({"font.size": 8.5})
fig, ax = plt.subplots(figsize=(4.8, 4.0))
ax.axvspan(yv, 30, color="0.9", lw=0)
ax.text(yv * 1.04, 0.08, "bare within 10%\nof conserving", fontsize=7, color="0.35")
ax.plot(yg, cons, color="k", lw=1.6, label="conserving response (clean)")
ax.plot(yg, bare, color="C3", lw=1.2, label="bare BCS dielectric function")
ax.plot(yg[::3], kk[::3], "o", color="C3", ms=2.2, label=r"resummed form, Kramers--Kronig to $\infty$")
ax.plot(yg, cut, color="C3", lw=0.9, ls="--", label=r"resummed form, cut at $\omega' = qv_{\mathrm{F}}$")
m = fo > 0
ax.plot(yg[m], fo[m], color="C2", lw=1.0, ls="-.", label="first order in $\\Delta_{\\mathrm{BCS}}/qv_{\\mathrm{F}}$")
ylist = (2.05, 2.2, 2.5, 3.0, 5.0, 10.0)
for G, mk, lab in ((3.7, "s", r"conserving, $\mathfrak{l}_e = 1\,\mu$m"), (124.0, "^", r"conserving, $\mathfrak{l}_e = 30$ nm")):
    vals = [imp[(G, y)][1] * e.g_I(np.array([y]))[0] for y in ylist]
    ax.plot(ylist, vals, mk, mfc="none", mec="k", ms=4, mew=0.8, label=lab)
ax.axhline(1, color="0.6", lw=0.5)
ax.set_xscale("log")
ax.set_xlim(2, 30)
ax.set_ylim(0, 1.7)
ax.set_xticks([2, 3, 5, 10, 20, 30])
ax.set_xticklabels(["2", "3", "5", "10", "20", "30"])
ax.set_xlabel(r"$y = \omega/\Delta_{\mathrm{BCS}}$ (on the kinematic edge $q = \omega/v_{\mathrm{max}}$)")
ax.set_ylabel(r"$L/L^{\mathrm{nor}}$")
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.legend(fontsize=6.2, loc="upper center", bbox_to_anchor=(0.45, -0.17), frameon=False, ncol=2)
fig.tight_layout()
fig.savefig(OUT)
out(f"\nwrote {os.path.relpath(OUT, HERE)}")
LOG.close()
