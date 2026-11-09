"""WP6-v3 identity checks (R8 revision of returns/R6/WP6-v2.md after REF-WP6-A/B). Labels WP6v3-Cn; C1-C15 keep their v2 numbers
(C5b, C8c, C10a,b, C11 repaired per REF-WP6-B G / REF-WP6-A F), C16-C33 are new. Original v2 docstring follows.
WP6-v2 identity checks (R6 revision of returns/R5/WP6.md). Sympy only (mpmath via evalf for closed forms);
no simulations, no numpy/scipy. Run:  python3 -I checks.py   Prints PASS/FAIL per check. Labels WP6v2-Cn (CONVENTIONS sec. 14).
Each check names the WP6-v2 equation it supports. Notation: NOTATION v4 (v_T, v_par, delta_v, N_esc, A^(0), A^(2), p_on, k_tail ...).
v1 -> v2 label map: C1-C3 -> C1-C3; C4a (numerical quadrature) -> C4a (exact Leibniz proof); C4b -> C4b; C4 sensitivities -> C4c;
C5a -> C5a; C5b (numerical fit) -> C5b (exact Beta-function integral); new C5c (tail lens); C6 -> C6; C7 -> C7; C8 (brentq) -> C8
(closed form via Lambert W); C9 -> C9; C10a,b -> C10a-d; C11 -> C11; C12 (quadrature) -> C12 (exact); new C13 (tau string), C14."""
import re
import sympy as sp
from sympy import Rational as Q, pi, sqrt, exp, erf, oo

RES = []
def rep(name, ok, note=""):
    RES.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name:86s} {note}")
def is0(e):
    if isinstance(e, sp.MatrixBase): return all(is0(x) for x in e)
    return sp.simplify(e) == 0

# ------------------------------------------------ C1-C3: conventions dictionary (1.6), per-target / per-cell (WP6-D1)
q, w, Om, al, me, Sb, V = sp.symbols('q omega Omega alpha m_e Sbar V', positive=True)
f2 = Om*q**3*Sb/(4*pi*al*me**2)                           # |f_crys|^2 of (1.6)
urf = w*V/(4*pi)*q*Sb                                     # (9.2) x rho_T V, integrand per d ln omega, common factors stripped
ess = (V/Om)*al*me**2*(w/q**2)*f2                         # 1509.01598 Eq. (17), N_cell = V/Omega, d ln q = dq/q
rep("WP6v3-C1  |f_crys|^2 = Omega q^3 Sbar/(4 pi alpha m_e^2) <=> 1509.01598 Eq.(17) = WP0-v2 (9.2)", is0(urf - ess))
L = sp.symbols('L', positive=True)
rep("WP6v3-C2  ELF form (S = 2q^2 L/e^2, T=0) gives 2101.08275 Eq.(16)", is0(f2.subs(Sb, 2*q**2/(4*pi*al)*L) - q**5*Om*L/(8*pi**2*al**2*me**2)))
E, sg, rho, m, mu, F, eta, fc = sp.symbols('E sigma rho m mu F eta f_c', positive=True)
b3 = rho/m*sg/(8*mu**2)*q*F**2*(8*al*me**2*E/q**3)*fc*eta
e17 = rho/m*sg*al*me**2/mu**2*(1/q)*(E/q)*eta*F**2*fc
rep("WP6v3-C3a 2311.04957 Eqs.(3)-(4) = 1509.01598 Eq.(17)/N_cell (per cell, WP6-D1)", is0(b3 - e17))
rep("WP6v3-C3b |f_res|^2 = (8 alpha m_e^2 omega/q^3)|f_crys|^2 = 2 Omega omega Sbar/pi  (1.6)", is0(8*al*me**2*w/q**3*f2 - 2*Om*w*Sb/pi))

# ------------------------------------------------ C4: SHM eta (1509.01598 Eqs. (66)-(68)), edge (3.2), sensitivities
u, v, v0, ve, vE, c = sp.symbols('u v v_0 v_esc v_E c', positive=True)
Nesc = v0**3*pi*(sqrt(pi)*erf(ve/v0) - 2*ve/v0*exp(-(ve/v0)**2))
etaA = v0**2*pi/(2*vE*Nesc)*(-4*exp(-ve**2/v0**2)*vE + sqrt(pi)*v0*(erf((u + vE)/v0) - erf((u - vE)/v0)))
etaB = v0**2*pi/(2*vE*Nesc)*(-2*exp(-ve**2/v0**2)*(ve - u + vE) + sqrt(pi)*v0*(erf(ve/v0) - erf((u - vE)/v0)))
# radial density g(v) = Int dOmega v^2 f_chi / v over the escape sphere (lab frame, Gaussian boosted by v_E):
#   eta(u) = Int_u^{v_max} g(v) dv,  g = (2 pi v/N_esc) Int_{-1}^{c_max} dc exp(-(v^2 + v_E^2 + 2 v v_E c)/v0^2)
def gfun(cmax):
    return 2*pi*v/Nesc*sp.integrate(exp(-(v**2 + vE**2 + 2*v*vE*c)/v0**2), (c, -1, cmax))
gA = gfun(1)                                              # v < v_esc - v_E: full sphere
gB = gfun((ve**2 - v**2 - vE**2)/(2*v*vE))                # v_esc - v_E < v < v_esc + v_E: cut by the escape sphere
okA = is0(sp.diff(etaA, u) + gA.subs(v, u))
okB = is0(sp.diff(etaB, u) + gB.subs(v, u))
okc = is0((etaA - etaB).subs(u, ve - vE)) and is0(etaB.subs(u, ve + vE))
rep("WP6v3-C4a SHM closed form: d eta/du = -g(u) on both branches, continuous, eta(v_max) = 0 (exact)", okA and okB and okc)
d, a = sp.symbols('delta_v a', positive=True)
eta2 = etaB.subs({ve: a*v0}).subs(u, a*v0 + vE - d)
ser = sp.series(eta2, d, 0, 3).removeO()
rep("WP6v3-C4b edge (3.2): eta = pi v_esc e^{-v_esc^2/v0^2} delta_v^2/(v_E N_esc) + O(delta_v^3)",
    is0(ser - (pi*a*v0*exp(-a**2)*d**2/(vE*Nesc.subs(ve, a*v0)))))
ser3 = sp.series(eta2, d, 0, 4).removeO()
r3 = sp.simplify(ser3.coeff(d, 3)/ser3.coeff(d, 2))
dX = 3*a*v0/(2*a**2 - 1)                                  # crossover delta_v,x = 3 v_esc v0^2/(2 v_esc^2 - v0^2)
rep("WP6v3-C4d next order: eta ~ delta_v^2 [1 + delta_v/delta_vx], delta_vx = 3 v_esc v0^2/(2v_esc^2 - v0^2) = 173 km/s",
    is0(r3 - 1/dX) and abs(float(dX.subs({a: Q(544, 238), v0: 238})) - 172.7) < 0.1)
ref = {v0: 238, ve: 544, vE: Q(501, 2)}                   # 2105.00599, v_E^ref = |v_sun| = 250.5 km/s
lnB = sp.log(etaB)
sens = {um: [float(sp.N(sp.diff(lnB, s).subs(ref).subs(u, um))) for s in (v0, ve, vE)] for um in (500, 600, 700, 760)}
for um, sv in sens.items():
    print(f"      v_min={um}: dln eta/dv0={sv[0]:.4f}, /dv_esc={sv[1]:.4f}, /dv_E={sv[2]:.4f} per km/s")
okS = abs(sens[600][0] - 0.0180) < 5e-4 and abs(sens[600][2] - 0.0125) < 5e-4 and abs(sens[760][1] - 0.0469) < 5e-4 and abs(sens[760][2] - 0.0601) < 5e-4
emptyA = (ref[vE] + ref[v0]) > (ref[ve] - ref[vE])
rep("WP6v3-C4c sensitivities at v_E^ref (3.2); v1 regime-A interval v_E+v0 < v_min < v_esc-v_E is empty", okS and emptyA,
    f"(v_E+v0 = {float(ref[vE]+ref[v0])} > v_esc - v_E = {float(ref[ve]-ref[vE])})")

# ------------------------------------------------ C5: near-threshold rate (3.3)-(3.4)
x, Dl, cc = sp.symbols('x Delta c', positive=True)
I5 = sp.integrate((Dl - cc*x**2)**2, (x, -sqrt(Dl/cc), sqrt(Dl/cc)))
rep("WP6v3-C5a Int (D - c x^2)^2 dx = (16/15) D^{5/2} c^{-1/2}", is0(I5 - Q(16, 15)*Dl**Q(5, 2)/sqrt(cc)))
y = sp.symbols('y', positive=True)
ok5 = True
for k in (0, 1, 2):
    Ik = sp.integrate(sp.expand((Dl - cc*x**2)**(2 + k)), (x, -sqrt(Dl/cc), sqrt(Dl/cc)))
    ok5 &= sp.simplify(Ik/(Dl**(Q(5, 2) + k)/sqrt(cc))).is_number                # q integral ~ delta^{5/2+k}
    for p in (0, 1, 2, 3, 4, 5, Q(3, 2), Q(5, 2)):
        Iw = sp.integrate(y**p*(Dl - y)**(Q(5, 2) + k), (y, 0, Dl))
        ok5 &= sp.gammasimp(sp.expand_func(Iw/(Dl**(p + k + Q(7, 2))*sp.beta(p + 1, Q(7, 2) + k)))) == 1   # exact (v3: no numeric tolerance, REF-B G)
rep("WP6v3-C5b R ~ delta_v0^{7/2 + k_tail + p_on} exactly, gammasimp (k_tail = 0,1,2; p_on = 0-5, 3/2, 5/2; WP3-v3 final 3, 4, 3/2, 5/2)", ok5)
rho_, t_, vmx, k_ = sp.symbols('varrho t v_max k', positive=True)
aa = 1/(2*ve) - 1/(2*vmx)
lens = sp.integrate(2*pi*rho_*(d - aa*rho_**2)**(k_ + 1)/(k_ + 1), (rho_, 0, sqrt(d/aa)))
okL = is0(sp.simplify(lens - pi*d**(k_ + 2)/(aa*(k_ + 1)*(k_ + 2))))
eta_k0 = (lens.subs(k_, 0)/vmx*exp(-ve**2/v0**2)/Nesc).subs(vmx, ve + vE)
rep("WP6v3-C5c tail lens: eta ~ pi delta_v^{2+k_tail}/(a(k+1)(k+2)); k=0 reproduces C4b", okL and is0(eta_k0 - pi*ve*exp(-ve**2/v0**2)*d**2/(vE*Nesc)))

# ------------------------------------------------ C6: v_E^ref, annual mean and range (CONVENTIONS sec. 8)
tt = sp.symbols('t', real=True)
vsun = sp.Matrix([Q(111, 10), 238 + Q(122, 10), Q(73, 10)])
e1 = sp.Matrix([Q(9941, 10000), Q(1088, 10000), Q(42, 10000)]); e2 = sp.Matrix([Q(-504, 10000), Q(4946, 10000), Q(-8677, 10000)])
vEt = vsun + Q(298, 10)*(e1*sp.cos(tt) + e2*sp.sin(tt))
mod2 = sp.expand(vEt.dot(vEt))
mean = sp.N(sp.Integral(sqrt(mod2), (tt, 0, 2*pi)).evalf(12)/(2*pi))
crit = [sp.nsolve(sp.diff(mod2, tt), tt, g0) for g0 in (0.5, 2.0, 3.5, 5.0)]
ext = sorted(set(round(float(sqrt(mod2.subs(tt, cr))), 2) for cr in crit))
vsref = float(sp.N(sqrt(vsun.dot(vsun))))
print(f"      |v_sun| = {vsref:.2f}; <|v_E(t)|> = {float(mean):.2f}; extremes {ext}; v_max range [{544+ext[0]:.1f}, {544+ext[-1]:.1f}]")
rep("WP6v3-C6 |v_sun| = 250.5 (v_E^ref), annual mean 252.1, |v_E(t)| in [237.4, 266.4], v_max in [781, 810]",
    abs(vsref - 250.5) < 0.1 and abs(float(mean) - 252.1) < 0.05 and abs(ext[0] - 237.35) < 0.05 and abs(ext[-1] - 266.45) < 0.05)

# ------------------------------------------------ C7: m_min = 2 E_th/v_max^2 (3.1)
cl = Q(299792458, 1000)
def mmin(Eth, vmax): return float(2*Eth*(cl/vmax)**2/10**6)
tab = {"Si 1.12 eV, 794.5": mmin(Q(112, 100), Q(1589, 2)), "Si 1.12 eV, 840": mmin(Q(112, 100), 840),
       "Si 1.2 eV, 776 (2311.04957)": mmin(Q(6, 5), 776), "Ge 0.67 eV, 794.5": mmin(Q(67, 100), Q(1589, 2)),
       "Si 1.12 eV, 781.4": mmin(Q(112, 100), 544 + Q(ext[0]).limit_denominator(100)), "Si 1.12 eV, 810.4": mmin(Q(112, 100), 544 + Q(ext[-1]).limit_denominator(100))}
tab.update({"Si E_g(0) 1.170 eV, 794.5": mmin(Q(117, 100), Q(1589, 2)), "PAER edge 1.188 eV, 794.5": mmin(Q(1188, 1000), Q(1589, 2)),
            "Ge E_g(0) 0.744 eV, 794.5": mmin(Q(744, 1000), Q(1589, 2)), "Si 1.170 eV, 810.4": mmin(Q(117, 100), 544 + Q(ext[-1]).limit_denominator(100)),
            "Si 1.170 eV, 781.4": mmin(Q(117, 100), 544 + Q(ext[0]).limit_denominator(100))})
for kk, vv in tab.items(): print(f"      m_min[{kk}] = {vv:.3f} MeV")
rep("WP6v3-C7b campaign default E_g(T_op): Si 1.170 eV -> 0.333 (annual 0.320-0.344), v2 E_g+omega_TA(K) 1.188 eV -> 0.338 (withdrawn as PAER edge), Ge 0.744 eV -> 0.212 MeV",
    abs(tab["Si E_g(0) 1.170 eV, 794.5"] - 0.333) < 5e-4 and abs(tab["PAER edge 1.188 eV, 794.5"] - 0.338) < 5e-4 and abs(tab["Ge E_g(0) 0.744 eV, 794.5"] - 0.212) < 5e-4
    and abs(tab["Si 1.170 eV, 810.4"] - 0.320) < 1e-3 and abs(tab["Si 1.170 eV, 781.4"] - 0.345) < 1e-3)
rep("WP6v3-C7a labelled comparisons m_min: 0.319 (Si), 0.285 (840 km/s; EXCEED-DM 0.28 at 1.11 eV), 0.358, 0.191 (Ge); annual 0.307-0.330",
    abs(tab["Si 1.12 eV, 794.5"] - 0.319) < 5e-4 and abs(mmin(Q(111, 100), 840) - 0.283) < 2e-3 and abs(tab["Si 1.2 eV, 776 (2311.04957)"] - 0.358) < 5e-4
    and abs(tab["Ge 0.67 eV, 794.5"] - 0.191) < 5e-4 and abs(tab["Si 1.12 eV, 810.4"] - 0.307) < 1e-3 and abs(tab["Si 1.12 eV, 781.4"] - 0.330) < 1e-3)

# ------------------------------------------------ C8: profile vs envelope (6.2); -2lnL = 2 s mu(theta) + theta^2, q = 2.71
dl, s, th, kq = sp.symbols('delta s theta kappa_q', positive=True)
c90 = Q(271, 100)
s_lin = (1 - sqrt(1 - c90*dl**2))/dl**2                  # linear mu = 1 + theta delta: theta_hat = -s delta
thl = -s*dl
okl = is0(sp.diff(2*s*(1 + th*dl) + th**2, th).subs(th, thl)) and is0((2*s*(1 + thl*dl) + thl**2 - c90).subs(s, s_lin))
prof = s_lin/(c90/2)
okl &= is0(sp.series(prof, dl, 0, 4).removeO() - (1 + c90*dl**2/4))
rep("WP6v3-C8a linear nuisance: ratio 2(1 - sqrt(1 - c d^2))/(c d^2) = 1 + c d^2/4 + O(d^4)  (O(delta^2))", okl)
Wl = -1 + sqrt(1 + c90*kq**2)                              # log-normal mu = e^{theta k}, k = ln(1+delta): Lambert-W solution
s_ln = Wl*exp(Wl)/kq**2
thn = -Wl/kq
okn = is0(sp.diff(2*s*exp(th*kq) + th**2, th).subs({s: s_ln, th: thn})) and is0((2*s_ln*exp(thn*kq) + thn**2) - c90)
rat = {d0: float(sp.N((s_ln/(c90/2)).subs(kq, sp.log(1 + d0)))) for d0 in (Q(1, 10), Q(3, 10), Q(1, 2))}
print("      log-normal ratios:", {float(k0): round(v1, 3) for k0, v1 in rat.items()}, " envelope 1/(1-d):", [round(1/(1 - float(d0)), 3) for d0 in rat])
okn &= abs(rat[Q(1, 10)] - 1.006) < 1e-3 and abs(rat[Q(3, 10)] - 1.047) < 1e-3 and abs(rat[Q(1, 2)] - 1.112) < 1e-3
rep("WP6v3-C8b log-normal (M-type) exact via the quadratic root w_delta: 1.006, 1.047, 1.112 at delta = 0.1, 0.3, 0.5", okn)
okc8 = abs(Q(3, 2)/rat[Q(1, 2)] - 1.349) < 2e-3 and abs(2/float(prof.subs(dl, Q(1, 2))) - 1.567) < 2e-3      # like for like (REF-A F, REF-B F6)
okc8 &= abs(1.5/rat[Q(1, 2)] - 1.80) > 0.4                                                             # v2 x1.8 = 2.0/1.112 mixes types: withdrawn
okc8 &= sp.solve(1 - c90*dl**2, dl) == [1/sqrt(c90)] and abs(float(1/sqrt(c90)) - 0.607) < 1e-3       # linear profile: no limit for delta > 0.607
wq = sp.symbols('w', positive=True)
okc8 &= is0((wq**2 + 2*wq - c90*kq**2).subs(wq, Wl))                                                     # w_delta is a quadratic root (not Lambert W)
ser_ln = sp.series((s_ln/(c90/2)).subs(kq, sp.log(1 + dl)), dl, 0, 4).removeO()
okc8 &= is0(ser_ln.coeff(dl, 2) - c90/4) and not is0(ser_ln.coeff(dl, 3))
print(f"      like-for-like at delta=0.5: M {1.5/rat[Q(1, 2)]:.3f}, linear {2/float(prof.subs(dl, Q(1, 2))):.3f}; log-normal series {sp.nsimplify(ser_ln)}")
rep("WP6v3-C8c envelope/profile like for like at delta=0.5: x1.35 (M), x1.57 (linear); linear no limit for delta>0.607; w_delta quadratic root; O(delta^3) term", okc8)

# ------------------------------------------------ C9: impulse tail obeys the f-sum (5.2), WP0-v2 (4.6)
pz, s0, nsh = sp.symbols('p_z s_0 nbar_sh', positive=True)
J = exp(-pz**2/(2*s0**2))/sqrt(2*pi*s0**2)
mom = sp.integrate((q**2/(2*me) + q*pz/me)*2*pi*nsh*(me/q)*J*(q/me), (pz, -oo, oo))
rep("WP6v3-C9  S_IA = 2 pi nbar_sh (m_e/q) J(p_z): Int_R w S_IA dw = pi nbar_sh q^2/m_e", is0(mom - pi*nsh*q**2/me))

# ------------------------------------------------ C10: Radon / transverse averages (1.3)-(1.4)
ct, vm, ph = sp.symbols('c_t v_m phi', real=True)
vv_, ss_ = sp.symbols('v s', positive=True)
okA10 = okB10 = True
for uu in (ss_, -ss_):                                    # general v > 0, u of either sign (exothermic DM: v_min < 0, REF-B A1)
    a0 = Q(1, 2)*sp.integrate(sp.DiracDelta(vv_*ct - uu), (ct, -1, 1))
    a2 = Q(1, 2)*sp.integrate((vv_**2 - vv_**2*ct**2)*sp.DiracDelta(vv_*ct - uu), (ct, -1, 1))
    for vs0, s0_ in ((3, 1), (1, 3), (2, Q(1, 2))):
        th_ = 1 if vs0 > s0_ else 0
        okA10 &= is0(a0.subs({vv_: vs0, ss_: s0_}) - Q(th_, 2*vs0))
        okB10 &= is0(a2.subs({vv_: vs0, ss_: s0_}) - (vs0**2 - s0_**2)*Q(th_, 2*vs0))
    okA10 &= is0(sp.simplify(a0.rewrite(sp.Heaviside)) - (sp.Heaviside(1 - uu/vv_) - sp.Heaviside(-1 - uu/vv_))/(2*vv_))
rep("WP6v3-C10a <delta(q^.v - u)>_q^ = Theta(v - |u|)/(2v), symbolic v, u of both signs (v3: |v_min|)", okA10)
rep("WP6v3-C10b <|v_T|^2 delta(q^.v - u)>_q^ = (v^2 - u^2)Theta(v - |u|)/(2v), both signs of u", okB10)
vT = sp.symbols('v_T', positive=True)
vvec = sp.Matrix([vT*sp.cos(ph), vT*sp.sin(ph), 0])     # q^ = z
Tav = (vvec*vvec.T).applyfunc(lambda e: sp.integrate(e, (ph, 0, 2*pi))/(2*pi))
PT = sp.diag(1, 1, 0)
d2, d2p = sp.symbols('d_2 d_2p')
D2 = d2*sp.eye(3) + d2p*sp.diag(0, 0, 1)
okT = is0(Tav - vT**2*PT/2)
okT &= is0(sum(D2.multiply_elementwise(Tav)) - d2*vT**2)            # D^(2)_cd v_T^c v_T^d -> d_2 |v_T|^2
okT &= is0(Q(1, 2)*sum(PT.multiply_elementwise(D2)) - d2)           # (1/2) tr_T D^(2) = d_2
okT &= all(is0(sp.integrate(e, (ph, 0, 2*pi))) for e in vvec)
rep("WP6v3-C10c <v_T v_T>_az = |v_T|^2 P_T/2; A^(2) = (1/2)tr_T D^(2) = d_2; <v_T>_az = 0 (n = 1 drops)", okT)

# ------------------------------------------------ C11: invariant harmonics (1.5)
def chi(l, phi):
    return sp.Integer(2*l + 1) if phi == 0 else sp.nsimplify(sp.sin((l + Q(1, 2))*phi)/sp.sin(phi/2))
def n_inv(l, improper_sign):     # O (24 rotations) or T_d (rotations E,8C3,3C2 + improper 6S4,6sigma_d = i x (C4, C2'))
    rot = chi(l, 0) + 8*chi(l, 2*pi/3) + 3*chi(l, pi)
    imp = 6*chi(l, pi/2) + 6*chi(l, pi)
    return sp.simplify((rot + improper_sign*imp)/24)
Oh = {l: n_inv(l, 1) for l in range(0, 13, 2)}
Td_odd = {l: n_inv(l, -1) for l in range(1, 14, 2)}     # T_d: improper elements carry (-1)^l
TR_odd = {l: sp.simplify((n_inv(l, -1) + n_inv(l, -1)*(-1)**l)/2) for l in range(1, 14, 2)}  # add -1 (TR: S(q)=S(-q)) -> projector (1+(-1)^l)/2
print(f"      O_h even-l A1g counts: {Oh}; T_d odd-l A1 counts: {Td_odd}; with TR: {TR_odd}")
rep("WP6v3-C11 O_h: l = 0,4,6,8,10 once, 12 twice, none at 2; T_d odd l = 3,7,9,11,13 present; TR removes ALL odd l (REF-A A3)",
    Oh == {0: 1, 2: 0, 4: 1, 6: 1, 8: 1, 10: 1, 12: 2} and Td_odd == {1: 0, 3: 1, 5: 0, 7: 1, 9: 1, 11: 1, 13: 1} and all(x == 0 for x in TR_odd.values()))

# ------------------------------------------------ C12: xi = 2 Int_u^oo u' eta(u') du' for any f_chi (1.3)
gg = sp.Function('g')
vmax_ = sp.symbols('v_max', positive=True)
xi = sp.Integral(gg(v)*(v**2 - u**2), (v, u, vmax_))
et = sp.Integral(gg(v), (v, u, vmax_))
rep("WP6v3-C12 d xi/du = -2u eta (Leibniz, any radial density g), xi(v_max) = 0  => xi = 2 Int u' eta",
    is0(sp.diff(xi, u).doit() + 2*u*et.doit()) and xi.subs(u, vmax_).doit() == 0)

# ------------------------------------------------ C13: tau string (CONVENTIONS sec. 11; CORRECTIONS sec. 12; WP0-v2 F9)
tau = "nB=0|ng=0|nA=0|X=RPA+LFE|nT=0|K=-|Mg=-|nD=-"; meta = "T=130K;ref=normal;scr=ext,LFE;conv=window"
keys = [kv.split('=')[0] for kv in tau.split('|')]
okt = keys == ['nB', 'ng', 'nA', 'X', 'nT', 'K', 'Mg', 'nD'] and re.fullmatch(r"\d+", dict(kv.split('=') for kv in tau.split('|'))['nT']) is not None
okt &= [kv.split('=')[0] for kv in meta.split(';')] == ['T', 'ref', 'scr', 'conv'] and 'K' not in tau.split('nT=')[1].split('|')[0]
v1tau = "nB0|ng0|nA0|X=RPA+LFE|nT=130K|K=-|M=-|nD=-"
okt &= re.fullmatch(r"\d+", v1tau.split('nT=')[1].split('|')[0]) is None
rep("WP6v3-C13 tau string: 8 slots in CONVENTIONS order, nT an integer order, T in metadata; v1 string rejected", okt)

# ------------------------------------------------ C14: step basis (4.1): eta~ = sum_j h_j Theta(v_j - u) => xi~
hs = sp.symbols('h1:4', positive=True); vs_ = sp.symbols('v1:4', positive=True); up = sp.symbols('u_p', positive=True)
ok14 = True
for uu in (Q(1, 2), Q(3, 2), Q(5, 2)):
    vals = {vs_[0]: 1, vs_[1]: 2, vs_[2]: 3}
    eta_s = sum(h*sp.Heaviside(vj - up) for h, vj in zip(hs, vs_))
    lhs = 2*sp.integrate((up*eta_s).subs(vals), (up, uu, 4))
    rhs = sum(h*(vj**2 - uu**2)*sp.Heaviside(vj - uu) for h, vj in zip(hs, vs_)).subs(vals)
    ok14 &= is0(lhs - rhs)
rep("WP6v3-C14 step basis: xi~ = sum_j eta~_j (v_j^2 - u^2) Theta(v_j - u)  (4.1)", ok14)

# ------------------------------------------------ C15: constrained anharmonic nuisance (5.1'), WP2-v2 (6.1), (6.1')
yb = [Q(-2), Q(-1), Q(0), Q(1), Q(3)]                      # bins in y_R = omega - E_R
St = [Q(1, 10), Q(3, 10), Q(4, 10), Q(2, 10), Q(1, 20)]    # S^tau >= 0
Xp = [Q(1, 50), Q(-3, 100), Q(1, 25), Q(-1, 20), Q(1, 40)] # arbitrary shape template Delta'_A
mom = lambda F, a: sum(f*yy**a for f, yy in zip(F, yb))
Mm = sp.Matrix(3, 3, lambda a, b: mom(St, a + b)); cvec = Mm.solve(sp.Matrix([mom(Xp, a) for a in range(3)]))
PiX = [x - st*sum(cvec[b]*yy**b for b in range(3)) for x, st, yy in zip(Xp, St, yb)]
thA = sp.symbols('theta_A', real=True)
DA = [Q(1, 100), Q(-2, 100), Q(1, 100), Q(0), Q(0)]        # a central increment with moments 0,1 = 0 (toy)
DA = [d_ - st*sum(c_*yy**b for b, c_ in enumerate(Mm.solve(sp.Matrix([mom([Q(1,100),Q(-2,100),Q(1,100),0,0], a) for a in range(2)] + [0])))) for d_, st, yy in zip(DA, St, yb)]
S_th = [st + d_ + thA*px for st, d_, px in zip(St, DA, PiX)]
ok15 = all(is0(mom(PiX, a)) for a in range(3)) and all(is0(sp.diff(mom(S_th, a), thA)) for a in range(3))
rep("WP6v3-C15a projection Pi_mom kills moments 0,1,2: constraints (6.1) hold for every theta_A  (5.1')", ok15)
aa2 = Q(3, 10)
viol = (1 + aa2)**Q(1, 2) + (1 - aa2)**Q(1, 2) - 2
rep("WP6v3-C15b M type: two-bin zeroth moment (1+a)^th + (1-a)^th - 2 != 0 at th = 1/2, = 0 at th = 0, 1; O(th(1-th)a^2)",
    float(viol) < 0 and all(is0((1 + aa2)**t0 + (1 - aa2)**t0 - 2) for t0 in (0, 1))
    and abs(float(viol) - float(-Q(1, 2)*Q(1, 2)*aa2**2/2*2)) < 2e-3)


# ======================================================= v3 additions (R7 referee items) ===================================================
# ------------------------------------------------ C16: exact finite-shift halo factors (3.2), (V4) (REF-A B2, REF-B B)
def ratio(um, s, dv):
    dd = dict(ref); dd[s] = ref[s] + dv
    return float(sp.N((etaB.subs(dd)/etaB.subs(ref)).subs(u, um), 15))
F = {(um, nm): ratio(um, s, dv) for um in (600, 760) for nm, s, dv in
     (("esc+", ve, 25), ("esc-", ve, -25), ("E+15", vE, 15), ("E-15", vE, -15), ("Emax", vE, Q(26645, 100) - Q(501, 2)),
      ("Emin", vE, Q(23735, 100) - Q(501, 2)), ("v0+", v0, 6), ("v0-", v0, -6))}
print("      exact eta ratios:", {k: round(x, 3) for k, x in F.items()})
ok16 = abs(F[(760, "esc+")] - 2.261) < 2e-3 and abs(F[(760, "esc-")] - 0.100) < 1e-3 and abs(F[(760, "E+15")] - 2.131) < 2e-3
ok16 &= abs(F[(760, "E-15")] - 0.310) < 1e-3 and abs(F[(760, "Emax")] - 2.218) < 2e-3 and abs(F[(760, "Emin")] - 0.373) < 1e-3
ok16 &= abs(F[(600, "Emax")] - 1.215) < 1e-3 and abs(F[(600, "Emin")] - 0.845) < 1e-3 and abs(F[(600, "v0+")] - 1.109) < 1e-3 and abs(F[(600, "v0-")] - 0.893) < 1e-3
ok16 &= abs(float(sp.exp(Q(117, 100))) - 3.22) < 0.01 and not (abs(F[(760, "esc+")] - 3.22) < 0.5)              # v2's e^{1.17} is wrong
dl760 = float(sp.N(sp.diff(lnB, ve).subs(ref).subs(u, 760)))
ok16 &= abs(dl760 - 0.0469) < 2e-4 and abs(2/34.5 - 0.0580) < 1e-4 and abs(-2*544/238**2 + 0.0192) < 1e-4      # gap 0.058 -> 0.047 is mainly -2v_esc/v0^2
rep("WP6v3-C16 exact asymmetric factors at 760: v_esc+-25 x2.26/x0.100; annual x2.22/x0.373; dln eta/dv_esc gap from -2v_esc/v0^2", ok16)

# ------------------------------------------------ C17: (3.5) sizes (REF-A B3, REF-B B)
lnv = {ve_: float(sp.log(Q(ve_*2 + 501, 2)/Q(1589, 2))) for ve_ in (503, 528, 600)}
ok17 = abs(lnv[528] + 0.0203) < 3e-4 and abs(lnv[503] + 0.0530) < 3e-4 and abs(lnv[600] - 0.0681) < 3e-4 and abs(float(Q(1701, 1589) - 1) - 0.0705) < 3e-4
ok17 &= abs(float(sp.log(Q(12, 10)/Q(117, 100))) - 0.0253) < 3e-4 and abs(float(sp.log(Q(12, 10)/Q(112, 100))) - 0.0690) < 3e-4
rep("WP6v3-C17 delta ln v_max: 528 -2.0%, 503 -5.3%, 600 +6.8% (+7.0% fractional); step E_th offset 2.5% vs 1.170 eV (6.9% vs 1.12)", ok17,
    f"{ {k: round(x, 4) for k, x in lnv.items()} }")

# ------------------------------------------------ C18: general edge m_min = min_q q^2/[2(q v_max - E_th(q))] (3.1') (REF-A D1, REF-B E1; WP1-v3 [E13])
qq, mm, vmax0, E0, cp, w0, Kq = sp.symbols('q m v_m E_0 c_p omega_0 K', positive=True)
mq = qq**2/(2*(qq*vmax0 - E0))
q0 = sp.solve(sp.diff(mq, qq), qq); ok18 = is0(mq.subs(qq, 2*E0/vmax0) - 2*E0/vmax0**2) and 2*E0/vmax0 in q0     # constant E_th -> (3.1)
A_ = E0 + cp*Kq                                                           # linear local dispersion E_th(q) = E_0 + c_p (K - q): exact 2A/(v + c_p)^2
mlin = sp.simplify(sp.Min(*[mq.subs(E0, A_ - cp*qq).subs(qq, r_) for r_ in sp.solve(sp.diff(mq.subs(E0, A_ - cp*qq), qq), qq) if r_ != 0]))
ok18 &= is0(sp.simplify(mlin - 2*A_/(vmax0 + cp)**2))
cl_ = Q(299792458, 1000); vm_ = Q(1589, 2)/cl_; Eg_ = Q(117, 100); Ex_ = Eg_ - Q(147, 10000)
hbarc_eVA = Q(1973269804, 1000000)                                         # hbar c = 1973.27 eV Angstrom
cTA = Q(5840, 299792458)                                                   # Si TA [100] sound speed / c
Kpk = Q(983, 1000)*hbarc_eVA                                               # |K_pk| = 0.983 A^-1 in eV
m_floor = 2*Eg_/vm_**2/10**6; m_xfloor = 2*Ex_/vm_**2/10**6
m_lin = 2*(Eg_ + cTA*Kpk)/(vm_ + cTA)**2/10**6                           # REF-A construction (linear TA): upper bound
qopt = sp.sqrt(2*m_lin*10**6*(Eg_ + cTA*Kpk))                              # optimum |q| (eV) for the linear model
Qstar = (Kpk - qopt)/hbarc_eVA                                             # |Q*| (A^-1) at the optimum
wTA = Q(135, 10000)                                                        # omega_TA(0.53 A^-1) ~ 13.5 meV [E, measured dispersion]
m_pa = 2*(Eg_ + wTA)/vm_**2/10**6; m_px = 2*(Ex_ + wTA)/vm_**2/10**6
m_x0 = Kpk**2/(2*(Kpk*vm_ - Eg_))/10**6                                    # zero-phonon at |q| = |K| (edge shell / X0): 0.474
# first-order invariance of m under a local slope c': d m/d c' = 0 at c' = 0 when A = E + omega_0 + c' q_0, q_0 = sqrt(2 m A)
cpp, om0 = sp.symbols('cpp om0', positive=True)
Aq = Eg_ + om0; q0_ = 2*Aq/vm_                              # optimum q_0 = sqrt(2 m A) = 2A/v at c' = 0
mexp = 2*(Aq + cpp*q0_)/(vm_ + cpp)**2
ok18 &= is0(sp.diff(mexp, cpp).subs(cpp, 0))
vals18 = [float(x) for x in (m_floor, m_xfloor, m_lin, m_pa, m_px, m_x0, Qstar)]
print("      m_min [MeV]: floor E_g %.4f, floor E_x %.4f, linear-TA (REF-A) %.4f, PAER cont. %.4f, PAER exciton replica %.4f, ZPL at |K| %.4f; |Q*| = %.3f A^-1" % tuple(vals18))
ok18 &= abs(vals18[0] - 0.3332) < 3e-4 and abs(vals18[1] - 0.3290) < 3e-4 and abs(vals18[2] - 0.3389) < 3e-4 and abs(vals18[3] - 0.3370) < 3e-4
ok18 &= abs(vals18[4] - 0.3328) < 3e-4 and abs(vals18[5] - 0.474) < 1e-3 and 0.45 < vals18[6] < 0.60 and vals18[6] > 0.33          # Q* > Q_w = 0.33 A^-1: in window
EgG = Q(744, 1000); ExG = Q(211, 1000)*10**6*vm_**2/2; wG = Q(75, 10000)
mG = [float(2*EgG/vm_**2/10**6), float(2*(EgG + wG)/vm_**2/10**6), float(2*(ExG + wG)/vm_**2/10**6)]
ok18 &= abs(mG[0] - 0.2119) < 3e-4 and abs(mG[1] - 0.2140) < 3e-4 and 0.2125 < mG[2] < 0.2140
# halo-gap degeneracy broken by a q-dependent onset: d ln m/d ln lambda (E -> lambda^2 E, v -> lambda v) = 2 E'(q0)/v at first order
lam = sp.symbols('lambda', positive=True)
ok18 &= is0(sp.diff(2*lam**2*A_/(lam*vmax0 + lam*cp)**2, lam).subs(lam, 1))   # linear model: exact degeneracy if c_p also scales
print(f"      Ge: floor {mG[0]:.4f}, PAER continuum {mG[1]:.4f}, PAER exciton {mG[2]:.4f} MeV")
rep("WP6v3-C18 edge = min_q q^2/[2(q v_max - E_th(q))]: constant E_th -> 2E/v^2; linear 2A/(v+c)^2; tangency (slope enters at second order: dm/dc' = 0); Si/Ge edge numbers", ok18)

# ------------------------------------------------ C19: contact geometry of the edge (3.3'): smooth p+k+7/2, corner p+k+4, 3-D isolated line 7/2+k, sphere 5/2+k
ee, xx, sc, nn = sp.symbols('epsilon x s n', positive=True)
ok19 = True
for n_ in (2, 3, Q(7, 2), 5):
    sm = sp.integrate((ee - sc*xx**2)**n_, (xx, -sp.sqrt(ee/sc), sp.sqrt(ee/sc)))
    co = 2*sp.integrate((ee - sc*xx)**n_, (xx, 0, ee/sc))
    ok19 &= not sp.simplify(sm/ee**(n_ + Q(1, 2))).has(ee) and not sp.simplify(co/ee**(n_ + 1)).has(ee)
rr = sp.symbols('r', positive=True)
for k0 in (0, 1, 2):
    iso3 = 4*pi*sp.integrate(rr**2*(ee - rr**2)**(2 + k0), (rr, 0, sp.sqrt(ee)))          # isolated 3-D maximum of G(q): bound line, S-bar step
    ok19 &= not sp.simplify(iso3/ee**(Q(7, 2) + k0)).has(ee)
    sph = sp.integrate((ee - xx**2)**(2 + k0), (xx, -sp.sqrt(ee), sp.sqrt(ee)))            # line with isotropic dispersion: maximum on a sphere
    ok19 &= not sp.simplify(sph/ee**(Q(5, 2) + k0)).has(ee)
rep("WP6v3-C19 smooth contact eps^{n+1/2} (n = p+k+3), corner eps^{n+1}; bound line: isolated 3-D eps^{7/2+k}, isotropic sphere eps^{5/2+k}", ok19)

# ------------------------------------------------ C20: validity window of the power law (3.3) (REF-B E3)
dd_ = sp.symbols('delta', positive=True)
Eth_ = mm*(vmax0 - dd_)**2/2; wmax_ = mm*vmax0**2/2
ok20 = is0(sp.series((wmax_ - Eth_)/Eth_, dd_, 0, 2).removeO() - 2*dd_/vmax0)
mrel = sp.series(((vmax0/(vmax0 - dd_))**2 - 1), dd_, 0, 2).removeO()     # m/m_min - 1 at fixed E_th
ok20 &= is0(mrel - 2*dd_/vmax0)
win = [float(Q(w_, 1000)/(2*Q(1188, 1000))) for w_ in (10, 60)]           # delta_v0/v_max for omega range 10-60 meV
ok20 &= abs(win[0] - 0.0042) < 2e-4 and abs(win[1] - 0.0253) < 2e-4
rep("WP6v3-C20 omega_max - E_th = E_th 2 delta_v0/v_max; Delta m/m = 2 delta_v0/v_max; 10-60 meV -> delta_v0/v_max 0.4-2.5%, Delta m/m ~1-5%", ok20)

# ------------------------------------------------ C21: halo-independent bound needs a non-decreasing step column (4.2) (REF-A C1, REF-B D1)
Acol = [Q(1), Q(3), Q(2), Q(4)]                                            # A_i(v_j) >= 0 but NOT monotone (dip at j = 3)
h = 1; u0j = 1                                                             # constraint eta~(u_0 = v_1..) : sum_{j >= u0j} nu_j = h
best = min(Acol[j] for j in range(u0j, 4))
ok21 = best < Acol[u0j]                                                    # a step at v_3 gives a smaller rate than the step at u_0: v2 argument fails
A0f, A2f, vmn = sp.symbols('A0 A2 v_min', nonnegative=True); vv2 = sp.symbols('v', positive=True)
dcol = sp.diff((A0f + A2f*(vv2**2 - vmn**2))*sp.Heaviside(vv2 - vmn), vv2)
ok21 &= is0(sp.simplify(dcol.subs(sp.DiracDelta(vv2 - vmn), 0) - 2*A2f*vv2*sp.Heaviside(vv2 - vmn)))   # derivative = A0 delta + 2 v A2 Theta >= 0
nb = sp.symbols('N_b', positive=True)
ok21 &= is0(nb*(Q(1, 10)/nb) - Q(1, 10))                                   # Bonferroni: N_b bins at 1 - 0.1/N_b -> union failure <= 0.1
rep("WP6v3-C21 A_ij >= 0 with a non-monotone column breaks the single-step bound; A0, A2 >= 0 => column non-decreasing; Bonferroni CL", ok21)

# ------------------------------------------------ C22: M type on matrices (5.1) (REF-B F1): elementwise power not PSD; PSD geodesic is
St_ = sp.Matrix([[1, Q(1, 10)], [Q(1, 10), 1]]); Sp_ = sp.Matrix([[2, Q(14, 10)], [Q(14, 10), 1]])
ok22 = all(ev > 0 for ev in St_.eigenvals()) and all(ev > 0 for ev in Sp_.eigenvals())
Mel = lambda t: sp.Matrix(2, 2, lambda a, b: St_[a, b]*(Sp_[a, b]/St_[a, b])**t)
ok22 &= Mel(2).det() < 0 and Mel(0) == St_ and Mel(1) == Sp_              # elementwise M-type leaves the PSD cone at theta = 2
Pm, Dm = St_.diagonalize(normalize=True); Sh = Pm*sp.sqrt(Dm)*Pm.T; Shi = Sh.inv()
Cm = sp.simplify(Shi*Sp_*Shi); Pc, Dc = Cm.diagonalize(normalize=True)
geo = lambda t: sp.simplify(Sh*Pc*sp.diag(*[Dc[i, i]**t for i in range(2)])*Pc.T*Sh)
ok22 &= is0(geo(0) - St_) and is0(geo(1) - Sp_)
for t0 in (-2, -1, Q(1, 2), 2, 3):
    ok22 &= all(float(sp.N(e)) > 0 for e in geo(t0).eigenvals())
rep("WP6v3-C22 elementwise M on S_ab: det < 0 at theta = 2 (not PSD); PSD geodesic S^1/2 (S^-1/2 S' S^-1/2)^theta S^1/2 PSD for all theta", ok22)

# ------------------------------------------------ C23: A type: S + a Delta PSD for all a > 0 iff Delta PSD (REF-B F2)
Dn = sp.Matrix([[Q(1, 2), 0], [0, -Q(1, 10)]])                            # not PSD (outside-window DC piece)
ok23 = (St_ + 20*Dn).det() < 0 and (St_ + Q(1, 2)*Dn).det() > 0
Dp = sp.Matrix([[Q(1, 2), Q(1, 5)], [Q(1, 5), Q(1, 5)]])
ok23 &= all(ev >= 0 for ev in Dp.eigenvals()) and all((St_ + a_*Dp).det() > 0 for a_ in (Q(1, 100), 1, 100, 10**6))
rep("WP6v3-C23 A type: non-PSD Delta leaves the cone at large a (log-normal a unbounded); PSD Delta stays", ok23)

# ------------------------------------------------ C24: exponentially tilted anharmonic nuisance (5.1'') (REF-A E): exact constraints, PSD, = (5.1') at first order
yb4 = [Q(-2), Q(-1), Q(0), Q(1), Q(3)]
Sc = [Q(1, 10), Q(3, 10), Q(4, 10), Q(2, 10), Q(1, 20)]                    # S_c = S^tau + Delta^tau_A (central), > 0 on the grid
psi = [Q(1, 5), Q(-1, 10), Q(1, 10), Q(-1, 4), Q(1, 2)]                   # log-shape psi (v3-R9: psi = ln(1 + Delta'_A/S_c), C30); S_c psi plays Delta'_A at first order
nrm = sp.symbols('n_c', positive=True)                                     # (2 pi/Omega)|c_kappa|^2 (WP2-v3 IF-4)
sig = Q(1, 5)
thA_, thD_ = sp.symbols('theta_A theta_delta', real=True)
l0, l1, l2 = sp.symbols('lambda0:3', real=True)
phi_ = lambda yy: [1, yy, yy**2]
mom4 = lambda Fv, a: sum(f*yy**a for f, yy in zip(Fv, yb4))
T = [mom4(Sc, 0), mom4(Sc, 1), mom4(Sc, 2) + thD_*nrm*sig]                  # targets: moments of S_c, third shifted by theta_delta x normalised sigma
Sth = [s_*sp.exp(thA_*p_ + l0 + l1*yy + l2*yy**2) for s_, p_, yy in zip(Sc, psi, yb4)]
G = [mom4(Sth, a) - T[a] for a in range(3)]
lam_ = [l0, l1, l2]
Jl = sp.Matrix(3, 3, lambda a, b: sp.diff(G[a], lam_[b])).subs({l0: 0, l1: 0, l2: 0, thA_: 0, thD_: 0})
Jt = sp.Matrix(3, 2, lambda a, b: sp.diff(G[a], (thA_, thD_)[b])).subs({l0: 0, l1: 0, l2: 0, thA_: 0, thD_: 0})
dlam = -Jl.inv()*Jt                                                        # implicit-function derivative at theta = 0 (exact)
dS_A = [s_*(p_ + sum(dlam[b, 0]*phi_(yy)[b] for b in range(3))) for s_, p_, yy in zip(Sc, psi, yb4)]
Xp4 = [s_*p_ for s_, p_ in zip(Sc, psi)]
Mm4 = sp.Matrix(3, 3, lambda a, b: mom4(Sc, a + b)); cv4 = Mm4.solve(sp.Matrix([mom4(Xp4, a) for a in range(3)]))
Pi4 = [x - s_*sum(cv4[b]*yy**b for b in range(3)) for x, s_, yy in zip(Xp4, Sc, yb4)]
ok24 = all(is0(a_ - b_) for a_, b_ in zip(dS_A, Pi4))                      # first order in theta_A = Pi_mom[Delta'_A] (v2 form)
dS_D = [s_*sum(dlam[b, 1]*phi_(yy)[b] for b in range(3)) for s_, yy in zip(Sc, yb4)]
ok24 &= is0(mom4(dS_D, 0)) and is0(mom4(dS_D, 1)) and is0(mom4(dS_D, 2) - nrm*sig)   # = S_c P_delta with the WP2-v3 normalisation
sol = sp.nsolve([g.subs({thA_: 2, thD_: -4, nrm: 1}) for g in G], lam_, [0, 0, 0], prec=40)   # a large excursion (2 sigma, -4 sigma)
Snum = [e.subs({thA_: 2, l0: sol[0], l1: sol[1], l2: sol[2]}) for e in Sth]
ok24 &= all(float(x) > 0 for x in Snum) and all(abs(float(mom4(Snum, a) - T[a].subs({thD_: -4, nrm: 1}))) < 1e-30 for a in range(3))
lin_neg = [s_ + (-4)*x for s_, x in zip(Sc, [s_*sum(dlam[b, 1].subs(nrm, 1)*phi_(yy)[b] for b in range(3)) for s_, yy in zip(Sc, yb4)])]
ok24 &= any(float(x) < 0 for x in lin_neg)                                 # the affine (5.1') form at theta_delta = -4 is negative somewhere
rep("WP6v3-C24 tilted nuisance: exact moments + PSD at (theta_A, theta_delta) = (2, -4) where the affine form fails; first order = Pi_mom (5.1')", ok24)

# ------------------------------------------------ C25: prior encodings (REF-B F3; WP3-v3 IF-10)
med = lambda lo, hi: sp.sqrt(lo*hi); wid = lambda lo, hi: sp.log(hi/lo)/2
p25 = {"ladder [1.3, 2.0]": (float(med(Q(13, 10), 2)), float(wid(Q(13, 10), 2))), "PAER [0.4, 1.8]": (float(med(Q(2, 5), Q(9, 5))), float(wid(Q(2, 5), Q(9, 5)))),
       "v2 [0.5, 1.2]": (float(med(Q(1, 2), Q(6, 5))), float(wid(Q(1, 2), Q(6, 5))))}
print("      (median, sigma_ln):", {k: (round(a_, 3), round(b_, 3)) for k, (a_, b_) in p25.items()})
ok25 = abs(p25["ladder [1.3, 2.0]"][0] - 1.612) < 1e-3 and abs(p25["ladder [1.3, 2.0]"][1] - 0.215) < 1e-3
ok25 &= abs(p25["PAER [0.4, 1.8]"][0] - 0.849) < 1e-3 and abs(p25["PAER [0.4, 1.8]"][1] - 0.752) < 1e-3 and abs(p25["v2 [0.5, 1.2]"][0] - 0.775) < 1e-3
rep("WP6v3-C25 log-symmetric encodings: ladder median 1.61, sigma 0.22; PAER [0.4,1.8] median 0.85, sigma 0.75; v2 [0.5,1.2] median 0.77 (not 1)", ok25)

# ------------------------------------------------ C26: orientation average vs component-wise average of a tensor S_cd (REF-A A2)
th1, ph1 = sp.symbols('vartheta varphi', real=True)
sL, sT = sp.symbols('s_L s_T', positive=True)
qh = sp.Matrix([sp.sin(th1)*sp.cos(ph1), sp.sin(th1)*sp.sin(ph1), sp.cos(th1)])
Scd = sL*qh*qh.T + sT*(sp.eye(3) - qh*qh.T)
comp = Scd.applyfunc(lambda e: sp.integrate(sp.integrate(e*sp.sin(th1), (ph1, 0, 2*pi)), (th1, 0, pi))/(4*pi))
ok26 = is0(comp - (sL + 2*sT)/3*sp.eye(3))                                 # component-wise: q^-independent, mixes L and T
trT_comp = sum((sp.diag(1, 1, 0)).multiply_elementwise(comp)); trT_orient = 2*sT  # transverse trace at q^ = z
ok26 &= not is0(trT_comp - trT_orient)
rep("WP6v3-C26 component-wise q^ average of S_cd = (s_L+2s_T)/3 delta: transverse trace != 2 s_T; orientation average keeps L/T", ok26)

# ------------------------------------------------ C27: daily average keeps the zonal projection along the Earth axis (REF-B A3(ii))
al_, be_, ph2 = sp.symbols('alpha beta phi2', real=True)
nax = sp.Matrix([sp.sin(al_), 0, sp.cos(al_)])
e1_ = sp.Matrix([sp.cos(al_), 0, -sp.sin(al_)]); e2_ = sp.Matrix([0, 1, 0])
wdir = sp.cos(be_)*nax + sp.sin(be_)*(sp.cos(ph2)*e1_ + sp.sin(ph2)*e2_)   # wind direction in the crystal frame over a sidereal day
mean = lambda f: sp.simplify(sp.integrate(sp.expand(f), (ph2, 0, 2*pi))/(2*pi))
ok27 = is0(mean(wdir[2]) - sp.cos(be_)*nax[2])                            # l = 1: P_1(cos beta) n_z, nonzero
K4 = lambda w: w[0]**4 + w[1]**4 + w[2]**4 - Q(3, 5)
P4 = lambda x: (35*x**4 - 30*x**2 + 3)/8
ok27 &= is0(sp.simplify(mean(K4(wdir)) - P4(sp.cos(be_))*K4(nax)))         # l = 4 cubic invariant: P_4(cos beta) K_4(n^)
X3 = lambda w: w[0]*w[1]*w[2]
ok27 &= is0(sp.simplify(mean(X3(wdir)) - sp.Rational(1, 2)*sp.cos(be_)*(5*sp.cos(be_)**2 - 3)*X3(nax)))   # l = 3 (T_d xyz): P_3 x xyz(n^)
rep("WP6v3-C27 sidereal-day mean of Y_l(w(t)) = P_l(cos beta) Y_l(n^): l = 1, 3 (xyz), 4 (cubic K4) survive the daily average", ok27)

# ------------------------------------------------ C28: odd-l invariants of cubic groups (REF-A A3, REF-B A3(i); WP4-v3 I4)
def n_T(l):  # T (12 rotations)
    return sp.simplify((chi(l, 0) + 8*chi(l, 2*pi/3) + 3*chi(l, pi))/12)
odd = range(1, 14, 2)
cnt = {"T": {l: n_T(l) for l in odd}, "O": {l: n_inv(l, 1) for l in odd}, "T_d": {l: n_inv(l, -1) for l in odd}}
print("      odd-l invariant counts:", cnt)
ok28 = all(cnt[g][1] == 0 for g in cnt) and cnt["T"][3] == 1 and cnt["T_d"][3] == 1 and cnt["O"][3] == 0 and min(l for l in odd if cnt["O"][l] > 0) == 9
rep("WP6v3-C28 no l = 1 invariant in any cubic group; lowest odd l: 3 (T, T_d), 9 (O); with -1 in G_eff none (C11)", ok28)

# ------------------------------------------------ C29: zero-count bin trials: profiling cost bookkeeping (4.4) (REF-B F)
Nb, Nv, Nq, Nw, NL = 10, 100, 300, 2500, 10
ok29 = Nb*Nv*Nq*Nw*NL == 75*10**8 and Nb*Nq*Nw*NL == 75*10**6
csum = lambda vals, vj, vmins: sum(a_ for a_, vm in zip(vals, vmins) if vm < vj)
vals_ = [Q(3), Q(1), Q(2), Q(5)]; vmins_ = [Q(7), Q(2), Q(5), Q(9)]
srt = sorted(zip(vmins_, vals_)); pref = [sum(x[1] for x in srt[:i + 1]) for i in range(4)]
ok29 &= all(csum(vals_, vj, vmins_) == (pref[max(i for i in range(4) if srt[i][0] < vj)] if any(s_[0] < vj for s_ in srt) else 0) for vj in (3, 6, 8, 10))
rep("WP6v3-C29 A_i(v_j) = prefix sum over v_min-sorted cells (removes N_v): 7.5e9 -> 7.5e7 per evaluation", ok29)


# ------------------------------------------------ C30: R9 type-T fixes (VER-WP6-A N1, N2 = VER-WP6-B NEW-2)
Dpr = [Q(3, 100), Q(-1, 10), Q(1, 10), Q(-3, 20), Q(1, 10)]                 # template Delta'_A > -S_c
psiL = [sp.log(1 + d_/s_) for d_, s_ in zip(Dpr, Sc)]
ok30 = all(is0(s_*sp.exp(p_) - (s_ + d_)) for s_, p_, d_ in zip(Sc, psiL, Dpr))          # theta_A = 1 (lambda = 0) gives S_c + Delta'_A exactly
ok30 &= not all(is0(s_*sp.exp(d_/s_) - (s_ + d_)) for s_, d_ in zip(Sc, Dpr))             # v3's psi = Delta'/S_c does not
ya, yb_, T0s, T1s, T2s = sp.symbols('y_a y_b T_0 T_1 T_2', real=True)
ybar = T1s/T0s
ok30 &= is0(T0s*((yb_ - ybar)*(ybar - ya) - (T2s/T0s - ybar**2)) - ((ya + yb_)*T1s - ya*yb_*T0s - T2s))   # endpoint (upper variance) bound identity
lo, hi = min(yb4), max(yb4)
for td in (-4, 0, 3):                                                       # targets used / tested on the grid: inside both bounds
    t0, t1, t2 = [x.subs({thD_: td, nrm: 1}) for x in T]
    ok30 &= (t2*t0 - t1**2 > 0) and ((lo + hi)*t1 - lo*hi*t0 - t2 > 0)
tmax = sp.solve((lo + hi)*T[1] - lo*hi*T[0] - T[2].subs(nrm, 1), thD_)[0]   # theta_delta above which no tilt exists on this grid
ok30 &= float(tmax) > 3
print(f"      upper theta_delta bound on the toy grid: {float(tmax):.2f}")
rep("WP6v3-C30 psi = ln(1 + Delta'/S_c): theta_A = 1 reproduces the template; moment cone needs Var < (y_max - ybar)(ybar - y_min): theta_delta bounded above", ok30)

print(f"\n{sum(RES)}/{len(RES)} checks PASS")
