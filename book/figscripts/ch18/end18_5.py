"""Section 18.5 (the end of the cascade): every number printed in s18-5.tex and Fig. 18.4.

Run:  python end18_5.py > end18_5.log
Output: tex/figures/ch18/fig18_4.pdf

Sources of inputs (book values first):
  Eg(Si) = 1.17 eV, Eg(Ge) = 0.744 eV at low T          -- tab:3-materials (Sect. 3.3)
  eps_eh(Si) = 3.749 +- 0.001 eV, F = 0.119 +- 0.002    -- measured, Rodrigues et al. 2004.11499 (as in App. E.13 table)
  F_eh(Si) cascade model                                 -- continuum value of the one silicon set (si_cascade18.py)
  E_x^b(Si) = 14.7 meV, a_x = 4.2 nm                      -- Sect. 4.9 (Shaklee-Nahory 1970)
  E_x^b(Ge) = 2.5 and 5 meV, indirect ground state      -- absorption: Zwerdling et al., PRB 114, 80 (1959), 2.5 +- 0.4 meV;
                                                            Macfarlane et al., PR 108, 1377 (1957), 5 meV (both abstracts)
  D0X localization (dissociation into X + D0) ~ 5 meV     -- Lo et al. 1411.1324 p.2
  P donor ground state 45.59 meV below E_c                -- Sect. 7.4 (Vinh et al., measured)
  static dielectric constant of Si at liquid-He T: 11.4   -- Sect. 7.4 (fit of the 2p+- lines)
  slopes d eps/d Eg of the calibrated cascade (Si, Ge)   -- table18_4.json (secants at fixed A_AB, continuum)
  Ge eps_eh at low-T gap, cascade model                  -- table18_4.json (tab:18-pairs)
  D0X (bound exciton) Auger lifetime 200-300 ns            -- Lo et al. 1411.1324 p.2, quoting Schmid 1977
  e^2/(4 pi eps0) = 1.439964 eV nm; k_B = 8.617333e-5 eV/K (CODATA)
Rates of the kinetic model (Fig. 18.4) other than the bound-exciton Auger rate are ILLUSTRATIVE:
no formation, trapping, binding or free-exciton decay rate of silicon is measured at 50 mK.
"""
import os
import sys
import json
import numpy as np
from scipy.linalg import expm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch18")
os.makedirs(OUT, exist_ok=True)

KE2 = 1.439964          # e^2/(4 pi eps0) in eV nm
KB = 8.617333e-5        # eV/K
EG_SI, EG_GE = 1.17, 0.744
EPS_EH = 3.75           # eV, rounded measured 3.749
F_MEAS, F_MEAS_ERR = 0.119, 0.002
sys.path.insert(0, HERE)
from si_cascade18 import casc_cont, A_AB
F_MODEL = casc_cont(A_AB, sets=("N",))["F"]
EXB_SI, AX_SI = 0.0147, 4.2   # eV, nm
EXB_GE_LIST = (0.0025, 0.005)   # eV, the two absorption values
E_LOC = 0.005           # eV, D0X localization energy (Lo et al.)
E_P = 0.04559           # eV
EPS_STAT = 11.4
_J = json.load(open(os.path.join(HERE, "table18_4.json")))
SLOPE, SLOPE_GE = _J["deps_dEg_Si"], _J["deps_dEg_Ge"]
EPS_GE = _J["eps_Ge_lowT"]
print(f"inputs: F_eh(model) = {F_MODEL:.5f}; d eps/d Eg = {SLOPE:.3f} (Si), {SLOPE_GE:.3f} (Ge); eps_eh(Ge, low T) = {EPS_GE:.3f} eV")


def section(title):
    print("\n== " + title)


# ---------------------------------------------------------------- 1. capture ledger, worked example 18.5
section("Worked example 18.5: one captured electron in ten pairs (Si)")
N0 = 10
omega = N0 * EPS_EH
Enp0 = omega - N0 * EG_SI
Enp1 = omega - (N0 - 1) * EG_SI
print(f"omega = {omega:.2f} eV ; E_np before = {Enp0:.2f} eV ; after = {Enp1:.2f} eV ; rise = {Enp1 - Enp0:.2f} eV (= Eg)")
print(f"phonons at capture on P (Ec - Ej) = {E_P*1e3:.1f} meV ; held by trapped electron + unpaired hole = {EG_SI - E_P:.3f} eV")
print(f"energy per counted pair {omega/(N0-1):.3f} eV vs {omega/N0:.3f} eV : +{100*(N0/(N0-1)-1):.1f} %")
f = 0.1
nbar1 = (1 - f) * N0
F1 = (1 - f) * F_MEAS + f
var0 = F_MEAS * N0
var1 = F1 * nbar1
print(f"binomial capture f = {f}: <N'> = {nbar1:.1f}, eps' = {EPS_EH/(1-f):.3f} eV, F' = {F1:.4f}")
print(f"Var N: {var0:.3f} -> {var1:.3f} ; sigma {np.sqrt(var0):.3f} -> {np.sqrt(var1):.3f}")
print(f"  split of Var N': thinned cascade (1-f)^2 Var N = {(1-f)**2*var0:.4f}, binomial f(1-f)<N> = {f*(1-f)*N0:.4f}")
# check against direct binomial thinning of a distribution with mean 10, variance 1.19 (two-point mixture)
rng = np.random.default_rng(1)
# distribution on {9,10,11} with mean 10 and variance 1.19 is impossible (max var 1 for p only on 9,11 ... ) -> use {8..12}
vals = np.arange(8, 13)
# choose symmetric weights w(8)=w(12)=a, w(9)=w(11)=b, w(10)=1-2a-2b with 8a+2b = 1.19 ; take a = 0.05
a = 0.05
b = (var0 - 8 * a) / 2
w = np.array([a, b, 1 - 2 * a - 2 * b, b, a])
assert np.all(w >= 0)
Ns = rng.choice(vals, size=2_000_000, p=w)
Np = rng.binomial(Ns, 1 - f)
print(f"Monte Carlo thinning check: mean {Np.mean():.4f}, F' = {Np.var()/Np.mean():.4f} (formula {F1:.4f})")

section("Bernoulli loss that would raise F from the cascade value to the measured one")
p = (F_MEAS - F_MODEL) / (1 - F_MODEL)
plo = (F_MEAS - F_MEAS_ERR - F_MODEL) / (1 - F_MODEL)
phi = (F_MEAS + F_MEAS_ERR - F_MODEL) / (1 - F_MODEL)
print(f"p = {p:.4f} ({100*p:.2f} %), range for 0.119 +- 0.002: {100*plo:.2f} - {100*phi:.2f} %")
print(f"dF_meas/dp = 1 - F = {1 - F_MEAS:.3f}")
print(f"eps_eh rises by 1/(1-p) - 1 = {100*(1/(1-p)-1):.2f} %")

# ---------------------------------------------------------------- 2. excitons: heat estimator, impact excitation
section("Excitons: heat-based Fano factor if every pair binds; mean heat shift")
for name, exb, eg in (("Si", EXB_SI, EG_SI),) + tuple(("Ge %.1f meV" % (1e3 * e), e, EG_GE) for e in EXB_GE_LIST):
    x = exb / eg
    fac = (1 - x) ** 2
    print(f"{name}: E_x^b/Eg = {x:.5f} ; F_heat/F_eh = (1-x)^2 = {fac:.5f} ({100*(fac-1):+.2f} %)")
print(f"Si mean heat shift per pair E_x^b/eps_eh = {100*EXB_SI/EPS_EH:.3f} % of omega")
print(f"impact excitation: |d eps| <= slope*E_x^b = {SLOPE*EXB_SI*1e3:.1f} meV (Si) = {100*SLOPE*EXB_SI/EPS_EH:.2f} % ; "
      + " ; ".join(f"Ge ({1e3*e:.1f} meV) {SLOPE_GE*e*1e3:.1f} meV = {100*SLOPE_GE*e/EPS_GE:.2f} %" for e in EXB_GE_LIST))
print(f"r_gap overstates the held energy by at most (E_x^b + E_loc)/Eg = {100*(EXB_SI+E_LOC)/EG_SI:.2f} % (Si; E_x^b alone "
      f"{100*EXB_SI/EG_SI:.2f} %)")

# ---------------------------------------------------------------- 3. Coulomb scales at 50 mK
section("Coulomb and field scales in Si (eps = 11.4)")
T = 0.050
kT = KB * T
ke = KE2 / EPS_STAT               # eV nm
rO = ke / kT                      # nm
print(f"kT(50 mK) = {kT*1e6:.3f} micro-eV ; Onsager radius r_O = {rO/1e3:.1f} micrometer")
print(f"E_x^b/kT = {EXB_SI/kT:.0f}")
for Efield_vcm in (4.0, 100.0):
    E_vm = Efield_vcm * 100.0
    rf = np.sqrt(ke * 1e-9 / E_vm)          # m ; ke*1e-9 in V m
    print(f"field-balance radius at {Efield_vcm:g} V/cm: {rf*1e6:.3f} micrometer")
fi = EXB_SI / (AX_SI * 1e-7)              # V/cm
print(f"exciton field-ionization scale E_x^b/(e a_x) = {fi:.3g} V/cm")
for E in (0.1, 0.35, 0.94, 1.755):
    rC = ke / E                    # nm
    sig = np.pi * (rC * 1e-7) ** 2  # cm^2
    print(f"carrier at {E:.3f} eV: r_C = {rC:.3f} nm, pi r_C^2 = {sig:.2e} cm^2, "
          f"capture length at 1e12 cm^-3 = {1/(1e12*sig):.3g} cm, at 1e18 = {1e4/(1e18*sig):.3g} micrometer")
dPF = 2 * np.sqrt(ke * 1e-9 * 1e4)        # V, at 100 V/cm = 1e4 V/m
print(f"Poole-Frenkel lowering at 100 V/cm = {dPF*1e3:.2f} meV")
print(f"thermal emission exponent, P donor, 50 mK: E/kT = {E_P/kT:.4g} ; with PF lowering {(E_P-dPF)/kT:.4g}")

# ---------------------------------------------------------------- 4. linear pair kinetics (Fig. 18.4)
section("Linear kinetics of one pair at 50 mK (illustrative rates)")
# states: F (free pair), X (free exciton), B (bound exciton, one species); sinks: T (trapped), L (light), H (heat)
G_FX = 1.0e9        # s^-1  formation of a free exciton from a cold geminate pair          [illustrative]
b_trap_in = 0.05    #       target trapped fraction -> G_FT                                 [illustrative]
G_FT = G_FX * b_trap_in / (1 - b_trap_in)
G_X = 1.0e5         # s^-1  free-exciton decay (radiative + nonradiative)                   [illustrative]
eta_X = 0.1         #       luminescent fraction of free-exciton decay                      [illustrative]
G_XB = 1.0e6        # s^-1  binding to neutral impurities, sigma v n_j                      [illustrative]
G_B = 1 / 250e-9    # s^-1  bound-exciton Auger decay; 250 ns inside the quoted 200-300 ns  [Lo et al.]
eta_B = 0.0         #       Auger decay: no light                                          [assumption]
M = np.array([[-(G_FX + G_FT), 0, 0],
              [G_FX, -(G_X + G_XB), 0],
              [0, G_XB, -G_B]])
p0 = np.array([1.0, 0, 0])
gam = -np.diag(M)
print(f"rates (1/s): G_FX={G_FX:.3g} G_FT={G_FT:.3g} G_X={G_X:.3g} eta_X={eta_X} G_XB={G_XB:.3g} G_B={G_B:.3g}")
print("decay constants gamma_k (1/s):", ", ".join(f"{g:.4g}" for g in gam))
print("time constants (s):", ", ".join(f"{1/g:.3g}" for g in gam))
# weights of r(t) = 1^T exp(Mt) p0 = sum_k w_k exp(-gamma_k t)
evals, V = np.linalg.eig(M)
c = np.linalg.solve(V, p0)
wk = np.ones(3) @ V * c
order = np.argsort(-evals.real)
for i in order:
    print(f"  gamma = {-evals[i].real:.4g} /s : weight w = {wk[i].real:+.4f}")
print(f"  sum of weights = {wk.real.sum():.6f}")
# asymptotic split, formula vs integration of outgoing fluxes (-M^-1 p0)
tau = -np.linalg.solve(M, p0)           # time integrals of p_F, p_X, p_B
trap = G_FT * tau[0]
light = G_X * eta_X * tau[1] + G_B * eta_B * tau[2]
heat = G_X * (1 - eta_X) * tau[1] + G_B * (1 - eta_B) * tau[2]
b = G_FT / (G_FX + G_FT)
light_f = (1 - b) * (G_X * eta_X + G_XB * eta_B) / (G_X + G_XB)
print(f"split by flux integrals: trapped {trap:.5f}, light {light:.5f}, heat {heat:.5f}, sum {trap+light+heat:.12f}")
print(f"split by formula: trapped {b:.5f}, light {light_f:.5f}, heat {1-b-light_f:.5f}")
assert abs(trap - b) < 1e-12 and abs(light - light_f) < 1e-12

t = np.logspace(-11, -4, 600)
P = np.array([expm(M * ti) @ p0 for ti in t])
rgap = P.sum(axis=1)
# cumulative sinks
cumT = G_FT * np.array([(-np.linalg.solve(M, (np.eye(3) - expm(M * ti)) @ p0))[0] for ti in t])
for tt in (1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4):
    Pt = expm(M * tt) @ p0
    print(f"t = {tt:.0e} s: p_F={Pt[0]:.4f} p_X={Pt[1]:.4f} p_B={Pt[2]:.4f} r_gap={Pt.sum():.4f}")
from scipy.optimize import brentq, minimize_scalar
pB = lambda lt: (expm(M * 10**lt) @ p0)[2]
res = minimize_scalar(lambda lt: -pB(lt), bounds=(-8, -5), method="bounded", options={"xatol": 1e-8})
print(f"bound-exciton population peaks at t = {10**res.x:.3g} s with p_B = {pB(res.x):.4f} (bounded minimizer)")
rg = lambda lt, lev: (expm(M * 10**lt) @ p0).sum() - lev
def sinks(tt):
    q = -np.linalg.solve(M, (np.eye(3) - expm(M * tt)) @ p0)   # time integrals up to tt
    tr = G_FT * q[0]
    li = G_X * eta_X * q[1] + G_B * eta_B * q[2]
    rgv = (expm(M * tt) @ p0).sum()
    return rgv, tr, li, 1 - rgv - tr - li
for lev in (0.5, 0.1, 0.01):
    tl = 10**brentq(rg, -9, -3, args=(lev,), xtol=1e-12)
    rgv, tr, li, ph = sinks(tl)
    print(f"r_gap = {lev} at t = {tl:.4g} s (root-finder); there trapped {tr:.4f}, light {li:.4f}, phonons {ph:.4f}")
rgv, tr, li, ph = sinks(1e-6)
print(f"at 1 us: still held {rgv:.4f}, trapped {tr:.4f}, light {li:.4f}, phonons {ph:.4f}; a heat window closing at 1 us misses "
      f"{rgv:.3f} (held) + {tr + li:.3f} (trapped or radiated) = {rgv + tr + li:.3f}")

# ---------------------------------------------------------------- figure
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, axs = plt.subplots(1, 2, figsize=(6.3, 2.8), sharex=True)
ax = axs[0]
ax.loglog(t, P[:, 0], color="C0", label="free pair $p_F$")
ax.loglog(t, P[:, 1], color="C1", label="free exciton $p_X$")
ax.loglog(t, P[:, 2], color="C2", label="bound exciton $p_B$")
ax.loglog(t, cumT, color="C3", ls="--", label="trapped (cumulative)")
ax.set_ylim(1e-4, 1.5)
ax.set_xlim(1e-11, 1e-4)
ax.set_xlabel("time after the cascade (s)")
ax.set_ylabel("occupation per pair")
ax.legend(fontsize=7, loc="lower left", frameon=False)
ax.text(0.96, 0.95, "(a)", transform=ax.transAxes, va="top", ha="right")
ax = axs[1]
ax.semilogx(t, rgap, color="k", label=r"gap energy still held, $r_{\rm gap}$")
cumL = np.array([eta_X * G_X * (-np.linalg.solve(M, (np.eye(3) - expm(M * ti)) @ p0))[1] for ti in t])
ax.semilogx(t, cumL, color="C4", ls=":", label="escaped as light")
ax.semilogx(t, 1 - rgap - cumT - cumL, color="C5", ls="-.", label="returned as phonons")
ax.semilogx(t, cumT, color="C3", ls="--", label="trapped")
ax.set_ylim(-0.02, 1.02)
ax.set_xlabel("time after the cascade (s)")
ax.set_ylabel("fraction of the gap energy")
ax.legend(fontsize=7, loc="center left", frameon=False)
ax.text(0.96, 0.84, "(b)", transform=ax.transAxes, va="top", ha="right")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig18_4.pdf"))
print("\nwrote", os.path.join(OUT, "fig18_4.pdf"))
