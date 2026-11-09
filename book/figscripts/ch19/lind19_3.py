"""Lindhard quenching of silicon recoils (Sect. 19.3): Fig. 19.3 (fig:19-yields), Limit Check 19.3a (lim:19.3a,
fig:19-limit-lindhard) and every Lindhard number printed in Sect. 19.3.
Log: lind19_3.log.  Run: python lind19_3.py > lind19_3.log  (under a minute).

Model (Sect. 19.3, eq:19.3-simple): Lindhard's simplified integral equation for the mean energy given to atomic motion,
in reduced units,
    k_L eps^(1/2) nu'(eps) = int_0^eps dx f(x)/x^2 [nu(eps - x^2/eps) + nu(x^2/eps) - nu(eps)],   nu -> eps as eps -> 0,
(the form of Lindhard et al. 1963 as written by Sarkis et al., arXiv:2001.06503 Eq. (5), with x = t^(1/2)).
y_L = 1 - nu/eps.  Lindhard's parametrization: y_L = k g/(1 + k g), g = 3 eps^0.15 + 0.7 eps^0.6 + eps
(2001.06503 Eq. (7); Sorensen arXiv:1412.3028 Eqs. (5)-(7)).

Inputs and their sources
  Z = 14, A = 28.0855 (silicon; atomic mass as in the PDG atomic-properties table).
  k_L = 0.133 Z^(2/3) A^(-1/2) (2001.06503 Eq. (4); 1412.3028 Eq. (4)).
  Screening length a_L = 0.8853 a_0/(sqrt(2) Z^(1/3)), reduced energy eps = a_L E/(2 Z^2 e^2) for equal masses
     (1412.3028 Eq. (2) and Sect. II A); compared with c_L = 11.5 Z^(-7/3) keV^-1 (2001.06503 Sect. II).
  a_0 = 0.529177 A, e^2 = 14.39965 eV A (Gaussian; CODATA 2018).
  f(x): MODELLING CHOICE.  Thomas-Fermi screening function phi (solved here from phi'' = phi^(3/2)/sqrt(r), phi(0) = 1,
     phi(inf) = 0, by shooting on the initial slope), deflection in the impulse (small-angle) approximation,
     theta(beta) = -(1/eps) dI/dbeta, I(beta) = int_0^inf phi(r)/r dz, r = sqrt(beta^2 + z^2), lengths in a_L,
     t^(1/2) = eps*theta/2 = -(1/2) dI/dbeta, and f(x) = 2 x^2 beta |dbeta/dx| from d sigma = 2 pi a^2 beta d beta
     = pi a^2 f(x) dx/x^2.  Unscreened check: phi = 1 gives f = 1/(2x) (Rutherford).
  Silicon yield data: Albakry et al. (SuperCDMS), arXiv:2303.02196 Table II (total uncertainties).
  Power-law fit of the same paper: Y = 0.302 (E_R/10 keV)^0.261 (text below its Fig. 3).
  Constant-binding ansatz: 2001.06503 Eq. (13), nu = nu_L(eps) + C0 eps^(1/2) + C1 + u, eps = eps_R - u, with Table 3
     (Si): C0 = 9.1e-3, C1 = 3.33e-5, U = 0.15 keV, u = c_L U; yield (eps + u - nu)/(eps + u) (Eq. (2)); k = Lindhard's.
  Binary threshold E_R,th = 352 eV (Sect. 19.2).
Numerics: forward integration on a log grid in eps (1e-9 .. 30, 6000 points), trapezoid in the implicit right end,
the right-end term affine in nu'(eps_i) and solved exactly; x-integral on a geometric grid (400 points) in x/eps from
1e-6 to 1 plus the small-x piece f(x)(1 - nu')/eps integrated analytically from the grid.  Convergence checked by halving
both grids (printed).
"""
import os
import numpy as np
from scipy.integrate import solve_ivp, quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "..", "tex", "figures", "ch19"))
os.makedirs(OUT, exist_ok=True)

Z, A = 14, 28.0855
A0, E2G = 0.529177, 14.39965
kL = 0.133 * Z**(2 / 3) / np.sqrt(A)
aL = 0.8853 * A0 / (np.sqrt(2) * Z**(1 / 3))
cL = aL / (2 * Z**2 * E2G) * 1e3          # keV^-1
Zz = 12**0.23 + 14**0.23
print(f"ZBL-convention reduced energy (Z1 = 12, Z2 = 14; 2209.04503): C = 16.2616/(Z Z1 Z2) = {16.2616/(Zz*12*14):.5f} keV^-1, "
      f"ratio to Lindhard's {16.2616/(Zz*12*14)/(0.8853*A0/(np.sqrt(2)*Z**(1/3))/(2*Z**2*E2G)*1e3):.4f}")
print(f"k_L = {kL:.4f};  a_L = {aL:.5f} A;  eps/E = {cL:.5f} keV^-1  (11.5 Z^-7/3 = {11.5*Z**(-7/3):.5f} keV^-1)")

# ---------------- Thomas-Fermi screening function by shooting
def tf_shoot(B, xmax=40.0):
    x0 = 1e-6
    y0 = [1 + B * x0 + 4 / 3 * x0**1.5, B + 2 * x0**0.5]
    def rhs(x, y):
        return [y[1], max(y[0], 0.0)**1.5 / np.sqrt(x)]
    ev1 = lambda x, y: y[0]; ev1.terminal = True
    ev2 = lambda x, y: y[1]; ev2.terminal = True
    s = solve_ivp(rhs, (x0, xmax), y0, rtol=1e-12, atol=1e-14, events=(ev1, ev2), dense_output=True)
    return s

lo, hi = -1.60, -1.57
for _ in range(60):
    mid = 0.5 * (lo + hi)
    s = tf_shoot(mid)
    if s.t_events[0].size:      # phi crossed zero: slope too negative
        lo = mid
    else:
        hi = mid
B = 0.5 * (lo + hi)
s = tf_shoot(B)
xm = s.t[-1] * 0.6
print(f"Thomas-Fermi initial slope phi'(0) = {B:.8f}; solution used to r = {xm:.1f} a_L, then phi ~ (r_m/r)^3 phi(r_m)")
phim = s.sol(xm)[0]
def phi(r):
    r = np.asarray(r, float)
    out = np.empty_like(r)
    m = r <= xm
    if m.any():
        out[m] = s.sol(np.maximum(r[m], 1e-6))[0]
    out[~m] = phim * (xm / r[~m])**3
    return out
def dphi(r):
    r = np.asarray(r, float)
    out = np.empty_like(r)
    m = r <= xm
    if m.any():
        out[m] = s.sol(np.maximum(r[m], 1e-6))[1]
    out[~m] = -3 * phim * xm**3 / r[~m]**4
    return out
print(f"phi(1) = {phi(np.array([1.0]))[0]:.5f}, phi(5) = {phi(np.array([5.0]))[0]:.6f}")

# ---------------- impulse deflection and f(x)
u = np.linspace(0, 12, 6001)
def dIdb(beta):
    r = beta * np.cosh(u)                 # z = beta sinh u, dz = beta cosh u du
    integrand = (beta / r) * (dphi(r) / r - phi(r) / r**2) * beta * np.cosh(u)
    return np.trapezoid(integrand, u)
betas = np.geomspace(1e-4, 60, 900)
xs = np.array([-0.5 * dIdb(b) for b in betas])
lb, lx = np.log(betas), np.log(xs)
dlx = np.gradient(lx, lb)
fx = 2 * xs**2 * betas / (xs * np.abs(dlx) / betas)   # |dx/dbeta| = x |dlnx/dlnbeta| / beta
o = np.argsort(xs)
X, F = xs[o], fx[o]
print("f(x) checks: x f(x) at x = 10, 100 (Rutherford: 0.5):",
      [round(float(np.interp(v, X, F)) * v, 4) for v in (10.0, 100.0)])
XC = 2e-3      # below this reduced transfer, continue f as the power law of its local slope at XC (modelling choice)
def f_tf(x):
    x = np.asarray(x, float)
    out = np.exp(np.interp(np.log(x), np.log(X), np.log(F)))
    big = x > X[-1]
    out[big] = 0.5 / x[big]
    return out
SLOPE = float(np.log(f_tf(np.array([XC * 1.05]))[0] / f_tf(np.array([XC / 1.05]))[0]) / np.log(1.05**2))
FC = float(f_tf(np.array([XC]))[0])
M_EXP = (1 - SLOPE) / 2
print(f"local slope of f at x = {XC}: dln f/dln x = {SLOPE:.4f} (m = {M_EXP:.4f}); "
      f"TF-impulse slope at x = 1e-5: {np.log(f_tf(np.array([1.05e-5]))[0]/f_tf(np.array([1e-5/1.05]))[0])/np.log(1.05**2):.4f}")
SLOPE_LOCAL = SLOPE
SLOPE, M_EXP = 1 / 3, 1 / 3     # main choice: continue with f ~ x^(1/3); alternative: the local slope SLOPE_LOCAL
TAIL = "power"
def f_of_x(x):
    x = np.asarray(x, float)
    out = f_tf(x)
    if TAIL == "power":
        sm = x < XC
        out[sm] = FC * (x[sm] / XC)**SLOPE
    return out
print("f(x) at x = 1e-3, 1e-2, 0.1, 1:", [f"{float(f_of_x(np.array([v]))[0]):.4f}" for v in (1e-3, 1e-2, 0.1, 1.0)])
xx_ = np.geomspace(1e-3, 10, 20001)
ff_ = f_tf(xx_)
print(f"f(x) maximum: {ff_.max():.4f} at x = {xx_[ff_.argmax()]:.3f}")
ee_ = np.geomspace(0.03, 3, 400)
sn_ = np.array([np.trapezoid(f_tf(np.geomspace(1e-8, e_, 4000)), np.geomspace(1e-8, e_, 4000)) / e_ for e_ in ee_])
print(f"s_n maximum: {sn_.max():.4f} at eps = {ee_[sn_.argmax()]:.3f}")
for e in (0.01, 0.1, 0.3, 1.0, 3.0):
    sn = quad(lambda x: float(f_of_x(np.array([x]))[0]), 0, e, limit=200)[0] / e
    print(f"  reduced nuclear stopping s_n({e}) = {sn:.4f}")

# ---------------- forward solution of the integral equation
def solve(k, NE=6000, NX=400, emin=1e-9, emax=30.0):
    eps = np.geomspace(emin, emax, NE)
    nu = np.empty(NE); dnu = np.empty(NE)
    lam_eff = FC / XC**SLOPE
    Jm = quad(lambda s_: s_**(-1 - M_EXP) * (1 - (1 - s_)**(0.5 + 2 * M_EXP) - s_**(0.5 + 2 * M_EXP)), 0, 1)[0]
    Ca = 2 * k / (lam_eff * Jm) if TAIL == "power" else 0.0
    pa = 0.5 + 2 * M_EXP
    nu[0], dnu[0] = eps[0] - Ca * eps[0]**pa, 1 - pa * Ca * eps[0]**(pa - 1)
    sgrid = np.geomspace(1e-6, 1.0, NX)
    for i in range(1, NE):
        e, ep = eps[i], eps[i - 1]
        x = e * sgrid
        fw = f_of_x(x) / x**2
        a1 = x**2 / e                     # argument of nu for the struck atom
        a2 = e - a1                       # argument for the scattered projectile
        r_prev = nu[:i] / eps[:i]
        def nu_known(a):
            a = np.asarray(a)
            res = np.where(a <= eps[0], a - Ca * np.abs(a)**pa,
                           a * np.interp(np.log(np.maximum(a, eps[0])), np.log(eps[:i]), r_prev))
            return res
        def rhs(dn):
            nui = nu[i - 1] + 0.5 * (e - ep) * (dnu[i - 1] + dn)
            v1 = nu_known(np.minimum(a1, ep))
            v1 = np.where(a1 > ep, nui - dn * (e - a1), v1)
            v2 = nu_known(np.minimum(a2, ep))
            v2 = np.where(a2 > ep, nui - dn * (e - a2), v2)
            br = v1 + v2 - nui
            I = np.trapezoid(fw * br, x)
            # x < x_0 piece: bracket ~ (x^2/eps)(1 - nu')
            I += (1 - dn) / e * F_small(x[0])
            return I, nui
        R0, _ = rhs(0.0)
        R1, _ = rhs(1.0)
        Bc = R1 - R0
        dn = R0 / (k * np.sqrt(e) - Bc)
        dnu[i] = dn
        nu[i] = nu[i - 1] + 0.5 * (e - ep) * (dnu[i - 1] + dn)
    return eps, nu

def F_small(x0):
    xx = np.geomspace(x0 * 1e-6, x0, 50)
    return np.trapezoid(f_of_x(xx), xx)

def yL(eps, k=kL):
    g = 3 * eps**0.15 + 0.7 * eps**0.6 + eps
    return k * g / (1 + k * g)

eps, nu = solve(kL)
ynum = 1 - nu / eps
lam_main = FC / XC**(1 / 3)
J13 = quad(lambda s_: s_**(-4 / 3) * (1 - (1 - s_)**(7 / 6) - s_**(7 / 6)), 0, 1)[0]
print(f"main continuation f = lambda x^(1/3) below x = {XC}: lambda = {lam_main:.4f}; J(1/3) = {J13:.4f}; "
      f"small-eps law y = (2 k/(lambda J)) eps^(1/6) = {2/(lam_main*J13):.3f} k eps^(1/6); check against the solution at eps = 1e-8: "
      f"{2*kL/(lam_main*J13)*1e-8**(1/6):.5f}")
eps2, nu2 = solve(kL, NE=3000, NX=200)
ynum2 = 1 - nu2 / eps2
def ynum_at(e, E=eps, Y=ynum):
    return np.interp(np.log(e), np.log(E), Y)
print(f"  solution at eps = 1e-8, 1e-6: {ynum_at(1e-8):.5f}, {ynum_at(1e-6):.5f}; asymptotic law: {2*kL/(lam_main*J13)*1e-8**(1/6):.5f}, {2*kL/(lam_main*J13)*1e-6**(1/6):.5f}")
print("\nNumerical solution of Lindhard's equation (k_L = %.4f) against his parametrization:" % kL)
print("  eps      E_R/keV   y_num    y_num(half grids)  y_L(param)  y_L/y_num")
for e in (1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 3.0, 10.0):
    print(f"  {e:7.1e}  {e/cL:8.4f}  {ynum_at(e):.4f}   {ynum_at(e, eps2, ynum2):.4f}            {yL(e):.4f}      {yL(e)/ynum_at(e):.4f}")

SLOPE, M_EXP = SLOPE_LOCAL, (1 - SLOPE_LOCAL) / 2
eps4, nu4 = solve(kL)
yalt = 1 - nu4 / eps4
SLOPE, M_EXP = 1 / 3, 1 / 3
print("  alternative continuation with the local slope %.4f below x = %.0e:" % (SLOPE_LOCAL, XC))
for ER_ in (1.0, 4.0):
    e_ = cL * ER_
    print(f"    E_R = {ER_} keV: y_alt = {ynum_at(e_, eps4, yalt):.4f}, y_main = {ynum_at(e_):.4f}, ratio {ynum_at(e_, eps4, yalt)/ynum_at(e_):.4f}")
for e in (1e-3, 1e-2, 0.1, 1.0, 10.0):
    print(f"    eps = {e:7.1e}: y_alt = {ynum_at(e, eps4, yalt):.4f}, y_main = {ynum_at(e):.4f}, y_L/y_alt = {yL(e)/ynum_at(e, eps4, yalt):.4f}")
# exponent scan of the continuation (sensitivity, not an uncertainty band): f = FC (x/XC)^a below XC
print("  exponent scan of the continuation below x = %.0e (y at E_R = 1 keV relative to the x^(1/3) continuation):" % XC)
for a_ in (0.30, 1 / 3, SLOPE_LOCAL, 0.40, 0.45):
    SLOPE, M_EXP = a_, (1 - a_) / 2
    eps5, nu5 = solve(kL, NE=3000, NX=250)
    y5 = 1 - nu5 / eps5
    SLOPE, M_EXP = 1 / 3, 1 / 3
    print(f"    a = {a_:.4f}: y(1 keV) = {ynum_at(cL*1.0, eps5, y5):.4f} ({100*(ynum_at(cL*1.0, eps5, y5)/ynum_at(cL*1.0) - 1):+.1f} %), "
          f"y(4 keV) = {ynum_at(cL*4.0, eps5, y5):.4f} ({100*(ynum_at(cL*4.0, eps5, y5)/ynum_at(cL*4.0) - 1):+.1f} %); "
          f"small-eps law y ~ eps^(1/2 - a) = eps^{0.5 - a_:.3f}")
print("  Thomas-Fermi tail: phi_TF ~ 144/r^3 at large r, V ~ r^-4, so f ~ x^(1/2) (m = 1/4) as x -> 0: then the nuclear and "
      "electronic stopping both scale as eps^(1/2) and y tends to a nonzero constant (exponent 1/2 - a = 0)")
TAIL = "tf"
eps3, nu3 = solve(kL)
TAIL = "power"
ytf = 1 - nu3 / eps3
print("  sensitivity: Thomas-Fermi impulse f kept below x = %.0e (no power-law continuation), start y = 0 at eps = 1e-9:" % XC)
for e in (1e-3, 1e-2, 0.1, 1.0):
    print(f"    eps = {e:7.1e} (E_R = {e/cL*1e3:7.0f} eV): y = {ynum_at(e, eps3, ytf):.4f}  against {ynum_at(e):.4f} with the continuation")
print(f"  asymptotic small-eps law of the continued equation: y = C eps^(2m - 1/2), 2m - 1/2 = {2*M_EXP-0.5:.4f}")

# where does the parametrization deviate by 5 %, 10 %?  (fine grid, root by interpolation on the dense solution)
eg = np.geomspace(1e-5, 10, 20000)
rat = yL(eg) / ynum_at(eg)
for lev in (1.05, 1.10, 1.20):
    idx = np.where(np.abs(rat - 1) > lev - 1)[0]
    if idx.size:
        j = idx.max()
        print(f"  |y_L/y_num - 1| > {lev-1:.2f} for eps < {eg[j]:.3e} (E_R < {eg[j]/cL*1e3:.0f} eV)")
print(f"  max |y_L/y_num - 1| for eps >= 0.1: {np.max(np.abs(rat[eg >= 0.1] - 1)):.4f}")

# ---------------- data
data = np.array([  # E_R [keV], Y, +err, -err  (2303.02196 Table II)
    [0.10, 0.102, 0.034, 0.030],
    [0.22, 0.108, 0.009, 0.010],
    [0.46, 0.136, 0.009, 0.008],
    [0.89, 0.127, 0.031, 0.015],
    [2.33, 0.173, 0.044, 0.019],
    [3.91, 0.236, 0.055, 0.009]])
def ansatz(ER):
    """2001.06503 Eq. (13) with Table 3 (Si)."""
    C0, C1, U = 9.1e-3, 3.33e-5, 0.15
    uu = cL * U
    eR = cL * np.asarray(ER, float)
    e = eR - uu
    out = np.full_like(eR, np.nan)
    m = e > 0
    nuL = e[m] / (1 + kL * (3 * e[m]**0.15 + 0.7 * e[m]**0.6 + e[m]))
    nub = nuL + C0 * np.sqrt(e[m]) + C1 + uu
    out[m] = (e[m] + uu - nub) / (e[m] + uu)
    out[out < 0] = np.nan
    return out
def powlaw(ER):
    return 0.302 * (np.asarray(ER) / 10.0)**0.261

print("\nAt the energies of the silicon data (2303.02196 Table II):")
print("  E_R/keV   eps       Y_meas (+/-)          y_L(param)  y_num   meas/y_L   ansatz(U=0.15 keV)  power law")
for ER, Y, ep, em in data:
    e = cL * ER
    an = ansatz(np.array([ER]))[0]
    print(f"  {ER:5.2f}   {e:.5f}  {Y:.3f} (+{ep:.3f}/-{em:.3f})   {yL(e):.4f}     {ynum_at(e):.4f}  {Y/yL(e):.3f}      {an:.4f}             {powlaw(ER):.4f}")
for ER in (0.01, 0.03, 0.05, 0.352, 1.0, 4.0, 10.0):
    e = cL * ER
    print(f"  E_R = {ER*1e3:6.0f} eV: eps = {e:.3e}, y_L = {yL(e):.4f}, y_num = {ynum_at(e):.4f}, ansatz = {ansatz(np.array([ER]))[0]:.4f}")
# cutoff of the ansatz on a fine grid
Eg = np.linspace(0.2, 0.5, 300001)
an = ansatz(Eg)
ok = np.where(np.isfinite(an))[0][0]
print(f"  constant-binding ansatz: yield reaches zero at E_R = {Eg[ok]*1e3:.1f} eV (2U = 300 eV)")
print(f"  k = 0.161 (2001.06503 Table 4): y_L at 1 keV = {yL(cL*1.0, 0.161):.4f}; at 10 keV = {yL(cL*10, 0.161):.4f}")
print(f"  power-law fit through Lindhard at 10 keV: y_L(10 keV) = {yL(cL*10):.4f} (paper: 0.302)")

# electronic stopping implied by k_L for Si in Si
n_at = 8 / 5.431**3
for ER in (0.1, 1.0, 10.0):
    e = cL * ER
    Se = kL * np.sqrt(e)                                  # d eps / d rho
    dEdx = Se / (cL * 1e-3) * np.pi * aL**2 * n_at        # eV/A
    print(f"  electronic stopping of a Si ion in Si from k_L at E_R = {ER} keV: {dEdx:.3f} eV/A")

# ---------------- Fig. 19.3: yields against data
E = np.geomspace(0.03, 30, 600)
fig, ax = plt.subplots(figsize=(6.0, 3.8))
ax.plot(E, yL(cL * E), color="k", lw=1.5, label=r"Lindhard, $k_L = 0.146$")
ax.plot(E, yL(cL * E, 0.161), color="k", lw=1.0, ls=":", label=r"Lindhard, $k_L = 0.161$")
ax.plot(E, ansatz(E), color="C3", lw=1.3, ls="--", label=r"constant binding, $U = 0.15$ keV")
ax.plot(E, powlaw(E), color="C0", lw=1.0, ls="-.", label=r"power law of Ref. (measured fit)")
ax.errorbar(data[:, 0], data[:, 1], yerr=[data[:, 3], data[:, 2]], fmt="o", ms=4, color="C0", capsize=2,
            label="silicon data, 0.1–3.9 keV")
ax.axvline(0.352, color="0.5", lw=0.7, ls=(0, (2, 2)))
ax.text(0.37, 0.37, r"$E_{R,\mathrm{th}}$", fontsize=8, color="0.3")
ax.set_xscale("log")
ax.set_xlim(0.03, 30)
ax.set_ylim(0, 0.4)
ax.set_xlabel(r"recoil energy $E_R$ (keV)")
ax.set_ylabel(r"ionization yield $Y_q$")
h, l = ax.get_legend_handles_labels()
l[3] = "power-law fit to the data"
ax.legend(h, l, fontsize=7.5, loc="lower right", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig19_3.pdf"))
plt.close(fig)

# ---------------- Limit Check 19.3a: ratios against E_R
E = np.geomspace(0.01, 100, 800)
fig, ax = plt.subplots(figsize=(6.0, 3.6))
valid = E >= 0.1 / cL
ax.axvspan(0.1 / cL, 100, color="0.88", lw=0)
r1 = yL(cL * E) / ynum_at(cL * E)
r2 = yL(cL * E) / ynum_at(cL * E, eps4, yalt)
ax.fill_between(E, np.minimum(r1, r2), np.maximum(r1, r2), color="0.6", alpha=0.5, lw=0)
ax.plot(E, r1, color="k", lw=1.5, label="formula / solution of its integral equation")
dr = data[:, 1] / yL(cL * data[:, 0])
ax.errorbar(data[:, 0], dr, yerr=[data[:, 3] / yL(cL * data[:, 0]), data[:, 2] / yL(cL * data[:, 0])],
            fmt="o", ms=4, color="C0", capsize=2, label="silicon data / formula")
ax.plot(E, ansatz(E) / yL(cL * E), color="C3", lw=1.2, ls="--", label=r"constant binding $U$ / formula")
ax.axhline(1, color="0.4", lw=0.6)
ax.axvline(0.352, color="0.5", lw=0.7, ls=(0, (2, 2)))
ax.text(0.33, 0.13, r"$E_{R,\mathrm{th}}$", fontsize=8, color="0.3", ha="right")
ax.text(9, 1.62, r"$\epsilon_L \geq 0.1$", fontsize=8, color="0.3")
ax.set_xscale("log")
ax.set_xlim(0.01, 100)
ax.set_ylim(0, 1.8)
ax.set_xlabel(r"recoil energy $E_R$ (keV)")
ax.set_ylabel("ratio")
sec = ax.secondary_xaxis("top", functions=(lambda x: cL * x, lambda e: e / cL))
sec.set_xlabel(r"reduced energy $\epsilon_L$", fontsize=8)
ax.legend(fontsize=7.5, loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit19_3a.pdf"))
plt.close(fig)
print("\nwrote fig19_3.pdf, limit19_3a.pdf")
