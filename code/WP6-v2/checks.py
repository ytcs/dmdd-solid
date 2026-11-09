"""WP6-v2 identity checks (R6 revision of returns/R5/WP6.md). Sympy only (mpmath via evalf for closed forms);
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
rep("WP6v2-C1  |f_crys|^2 = Omega q^3 Sbar/(4 pi alpha m_e^2) <=> 1509.01598 Eq.(17) = WP0-v2 (9.2)", is0(urf - ess))
L = sp.symbols('L', positive=True)
rep("WP6v2-C2  ELF form (S = 2q^2 L/e^2, T=0) gives 2101.08275 Eq.(16)", is0(f2.subs(Sb, 2*q**2/(4*pi*al)*L) - q**5*Om*L/(8*pi**2*al**2*me**2)))
E, sg, rho, m, mu, F, eta, fc = sp.symbols('E sigma rho m mu F eta f_c', positive=True)
b3 = rho/m*sg/(8*mu**2)*q*F**2*(8*al*me**2*E/q**3)*fc*eta
e17 = rho/m*sg*al*me**2/mu**2*(1/q)*(E/q)*eta*F**2*fc
rep("WP6v2-C3a 2311.04957 Eqs.(3)-(4) = 1509.01598 Eq.(17)/N_cell (per cell, WP6-D1)", is0(b3 - e17))
rep("WP6v2-C3b |f_res|^2 = (8 alpha m_e^2 omega/q^3)|f_crys|^2 = 2 Omega omega Sbar/pi  (1.6)", is0(8*al*me**2*w/q**3*f2 - 2*Om*w*Sb/pi))

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
rep("WP6v2-C4a SHM closed form: d eta/du = -g(u) on both branches, continuous, eta(v_max) = 0 (exact)", okA and okB and okc)
d, a = sp.symbols('delta_v a', positive=True)
eta2 = etaB.subs({ve: a*v0}).subs(u, a*v0 + vE - d)
ser = sp.series(eta2, d, 0, 3).removeO()
rep("WP6v2-C4b edge (3.2): eta = pi v_esc e^{-v_esc^2/v0^2} delta_v^2/(v_E N_esc) + O(delta_v^3)",
    is0(ser - (pi*a*v0*exp(-a**2)*d**2/(vE*Nesc.subs(ve, a*v0)))))
ser3 = sp.series(eta2, d, 0, 4).removeO()
r3 = sp.simplify(ser3.coeff(d, 3)/ser3.coeff(d, 2))
dX = 3*a*v0/(2*a**2 - 1)                                  # crossover delta_v,x = 3 v_esc v0^2/(2 v_esc^2 - v0^2)
rep("WP6v2-C4d next order: eta ~ delta_v^2 [1 + delta_v/delta_vx], delta_vx = 3 v_esc v0^2/(2v_esc^2 - v0^2) = 173 km/s",
    is0(r3 - 1/dX) and abs(float(dX.subs({a: Q(544, 238), v0: 238})) - 172.7) < 0.1)
ref = {v0: 238, ve: 544, vE: Q(501, 2)}                   # 2105.00599, v_E^ref = |v_sun| = 250.5 km/s
lnB = sp.log(etaB)
sens = {um: [float(sp.N(sp.diff(lnB, s).subs(ref).subs(u, um))) for s in (v0, ve, vE)] for um in (500, 600, 700, 760)}
for um, sv in sens.items():
    print(f"      v_min={um}: dln eta/dv0={sv[0]:.4f}, /dv_esc={sv[1]:.4f}, /dv_E={sv[2]:.4f} per km/s")
okS = abs(sens[600][0] - 0.0180) < 5e-4 and abs(sens[600][2] - 0.0125) < 5e-4 and abs(sens[760][1] - 0.0469) < 5e-4 and abs(sens[760][2] - 0.0601) < 5e-4
emptyA = (ref[vE] + ref[v0]) > (ref[ve] - ref[vE])
rep("WP6v2-C4c sensitivities at v_E^ref (3.2); v1 regime-A interval v_E+v0 < v_min < v_esc-v_E is empty", okS and emptyA,
    f"(v_E+v0 = {float(ref[vE]+ref[v0])} > v_esc - v_E = {float(ref[ve]-ref[vE])})")

# ------------------------------------------------ C5: near-threshold rate (3.3)-(3.4)
x, Dl, cc = sp.symbols('x Delta c', positive=True)
I5 = sp.integrate((Dl - cc*x**2)**2, (x, -sqrt(Dl/cc), sqrt(Dl/cc)))
rep("WP6v2-C5a Int (D - c x^2)^2 dx = (16/15) D^{5/2} c^{-1/2}", is0(I5 - Q(16, 15)*Dl**Q(5, 2)/sqrt(cc)))
y = sp.symbols('y', positive=True)
ok5 = True
for k in (0, 1, 2):
    Ik = sp.integrate(sp.expand((Dl - cc*x**2)**(2 + k)), (x, -sqrt(Dl/cc), sqrt(Dl/cc)))
    ok5 &= sp.simplify(Ik/(Dl**(Q(5, 2) + k)/sqrt(cc))).is_number                # q integral ~ delta^{5/2+k}
    for p in (0, 1, 2, 3, 4, 5, Q(3, 2), Q(5, 2)):
        Iw = sp.integrate(y**p*(Dl - y)**(Q(5, 2) + k), (y, 0, Dl))
        dd5 = sp.expand_func(Iw - Dl**(p + k + Q(7, 2))*sp.beta(p + 1, Q(7, 2) + k)); ok5 &= is0(dd5) or abs(sp.N(dd5.subs(Dl, 2), 30)) < 1e-25  # sympy leaves catalan(n/2) forms unsimplified  # omega integral adds p_on + 1
rep("WP6v2-C5b R ~ delta_v0^{7/2 + k_tail + p_on} exactly (k_tail = 0,1,2; p_on = 0-5, 3/2, 5/2 incl. WP3-v2 PAER (A1))", ok5)
rho_, t_, vmx, k_ = sp.symbols('varrho t v_max k', positive=True)
aa = 1/(2*ve) - 1/(2*vmx)
lens = sp.integrate(2*pi*rho_*(d - aa*rho_**2)**(k_ + 1)/(k_ + 1), (rho_, 0, sqrt(d/aa)))
okL = is0(sp.simplify(lens - pi*d**(k_ + 2)/(aa*(k_ + 1)*(k_ + 2))))
eta_k0 = (lens.subs(k_, 0)/vmx*exp(-ve**2/v0**2)/Nesc).subs(vmx, ve + vE)
rep("WP6v2-C5c tail lens: eta ~ pi delta_v^{2+k_tail}/(a(k+1)(k+2)); k=0 reproduces C4b", okL and is0(eta_k0 - pi*ve*exp(-ve**2/v0**2)*d**2/(vE*Nesc)))

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
rep("WP6v2-C6 |v_sun| = 250.5 (v_E^ref), annual mean 252.1, |v_E(t)| in [237.4, 266.4], v_max in [781, 810]",
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
rep("WP6v2-C7b campaign default E_g(T_op): Si 1.170 eV -> 0.333 (annual 0.320-0.344), PAER edge 1.188 eV -> 0.338, Ge 0.744 eV -> 0.212 MeV",
    abs(tab["Si E_g(0) 1.170 eV, 794.5"] - 0.333) < 5e-4 and abs(tab["PAER edge 1.188 eV, 794.5"] - 0.338) < 5e-4 and abs(tab["Ge E_g(0) 0.744 eV, 794.5"] - 0.212) < 5e-4
    and abs(tab["Si 1.170 eV, 810.4"] - 0.320) < 1e-3 and abs(tab["Si 1.170 eV, 781.4"] - 0.345) < 1e-3)
rep("WP6v2-C7a labelled comparisons m_min: 0.319 (Si), 0.285 (840 km/s; EXCEED-DM 0.28 at 1.11 eV), 0.358, 0.191 (Ge); annual 0.307-0.330",
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
rep("WP6v2-C8a linear nuisance: ratio 2(1 - sqrt(1 - c d^2))/(c d^2) = 1 + c d^2/4 + O(d^4)  (O(delta^2))", okl)
Wl = -1 + sqrt(1 + c90*kq**2)                              # log-normal mu = e^{theta k}, k = ln(1+delta): Lambert-W solution
s_ln = Wl*exp(Wl)/kq**2
thn = -Wl/kq
okn = is0(sp.diff(2*s*exp(th*kq) + th**2, th).subs({s: s_ln, th: thn})) and is0((2*s_ln*exp(thn*kq) + thn**2) - c90)
rat = {d0: float(sp.N((s_ln/(c90/2)).subs(kq, sp.log(1 + d0)))) for d0 in (Q(1, 10), Q(3, 10), Q(1, 2))}
print("      log-normal ratios:", {float(k0): round(v1, 3) for k0, v1 in rat.items()}, " envelope 1/(1-d):", [round(1/(1 - float(d0)), 3) for d0 in rat])
okn &= abs(rat[Q(1, 10)] - 1.006) < 1e-3 and abs(rat[Q(3, 10)] - 1.047) < 1e-3 and abs(rat[Q(1, 2)] - 1.112) < 1e-3
rep("WP6v2-C8b log-normal (M-type) exact via Lambert W: 1.006, 1.047, 1.112 at delta = 0.1, 0.3, 0.5", okn)
rep("WP6v2-C8c envelope/log-normal at delta = 0.5 = 1.80; linear profile at 0.5 = 1.28",
    abs(2/rat[Q(1, 2)] - 1.80) < 0.01 and abs(float(prof.subs(dl, Q(1, 2))) - 1.276) < 2e-3)

# ------------------------------------------------ C9: impulse tail obeys the f-sum (5.2), WP0-v2 (4.6)
pz, s0, nsh = sp.symbols('p_z s_0 nbar_sh', positive=True)
J = exp(-pz**2/(2*s0**2))/sqrt(2*pi*s0**2)
mom = sp.integrate((q**2/(2*me) + q*pz/me)*2*pi*nsh*(me/q)*J*(q/me), (pz, -oo, oo))
rep("WP6v2-C9  S_IA = 2 pi nbar_sh (m_e/q) J(p_z): Int_R w S_IA dw = pi nbar_sh q^2/m_e", is0(mom - pi*nsh*q**2/me))

# ------------------------------------------------ C10: Radon / transverse averages (1.3)-(1.4)
ct, vm, ph = sp.symbols('c_t v_m phi', real=True)
avg0 = Q(1, 2)*sp.integrate(sp.DiracDelta(3*ct - 1), (ct, -1, 1))
rep("WP6v2-C10a <delta(q^.v - u)>_q^ = Theta(v-u)/(2v)  (v=3, u=1)", is0(avg0 - Q(1, 6)))
avg2 = Q(1, 2)*sp.integrate((9 - 9*ct**2)*sp.DiracDelta(3*ct - 1), (ct, -1, 1))
rep("WP6v2-C10b <|v_T|^2 delta(q^.v - u)>_q^ = (v^2 - u^2)Theta(v-u)/(2v)  (v=3, u=1)", is0(avg2 - Q(8, 6)))
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
rep("WP6v2-C10c <v_T v_T>_az = |v_T|^2 P_T/2; A^(2) = (1/2)tr_T D^(2) = d_2; <v_T>_az = 0 (n = 1 drops)", okT)

# ------------------------------------------------ C11: invariant harmonics (1.5)
def chi(l, phi):
    return sp.Integer(2*l + 1) if phi == 0 else sp.nsimplify(sp.sin((l + Q(1, 2))*phi)/sp.sin(phi/2))
def n_inv(l, improper_sign):     # O (24 rotations) or T_d (rotations E,8C3,3C2 + improper 6S4,6sigma_d = i x (C4, C2'))
    rot = chi(l, 0) + 8*chi(l, 2*pi/3) + 3*chi(l, pi)
    imp = 6*chi(l, pi/2) + 6*chi(l, pi)
    return sp.simplify((rot + improper_sign*imp)/24)
Oh = {l: n_inv(l, 1) for l in range(0, 13, 2)}
Td_odd3 = n_inv(3, -1)
print(f"      O_h even-l A1g counts: {Oh}; T_d l=3 A1 count: {Td_odd3}")
rep("WP6v2-C11 O_h: l = 0,4,6,8,10 once, 12 twice (7 coefficients), none at l=2; T_d l=3 invariant removed by TR",
    Oh == {0: 1, 2: 0, 4: 1, 6: 1, 8: 1, 10: 1, 12: 2} and Td_odd3 == 1)

# ------------------------------------------------ C12: xi = 2 Int_u^oo u' eta(u') du' for any f_chi (1.3)
gg = sp.Function('g')
vmax_ = sp.symbols('v_max', positive=True)
xi = sp.Integral(gg(v)*(v**2 - u**2), (v, u, vmax_))
et = sp.Integral(gg(v), (v, u, vmax_))
rep("WP6v2-C12 d xi/du = -2u eta (Leibniz, any radial density g), xi(v_max) = 0  => xi = 2 Int u' eta",
    is0(sp.diff(xi, u).doit() + 2*u*et.doit()) and xi.subs(u, vmax_).doit() == 0)

# ------------------------------------------------ C13: tau string (CONVENTIONS sec. 11; CORRECTIONS sec. 12; WP0-v2 F9)
tau = "nB=0|ng=0|nA=0|X=RPA+LFE|nT=0|K=-|Mg=-|nD=-"; meta = "T=130K;ref=normal;scr=ext,LFE;conv=window"
keys = [kv.split('=')[0] for kv in tau.split('|')]
okt = keys == ['nB', 'ng', 'nA', 'X', 'nT', 'K', 'Mg', 'nD'] and re.fullmatch(r"\d+", dict(kv.split('=') for kv in tau.split('|'))['nT']) is not None
okt &= [kv.split('=')[0] for kv in meta.split(';')] == ['T', 'ref', 'scr', 'conv'] and 'K' not in tau.split('nT=')[1].split('|')[0]
v1tau = "nB0|ng0|nA0|X=RPA+LFE|nT=130K|K=-|M=-|nD=-"
okt &= re.fullmatch(r"\d+", v1tau.split('nT=')[1].split('|')[0]) is None
rep("WP6v2-C13 tau string: 8 slots in CONVENTIONS order, nT an integer order, T in metadata; v1 string rejected", okt)

# ------------------------------------------------ C14: step basis (4.1): eta~ = sum_j h_j Theta(v_j - u) => xi~
hs = sp.symbols('h1:4', positive=True); vs_ = sp.symbols('v1:4', positive=True); up = sp.symbols('u_p', positive=True)
ok14 = True
for uu in (Q(1, 2), Q(3, 2), Q(5, 2)):
    vals = {vs_[0]: 1, vs_[1]: 2, vs_[2]: 3}
    eta_s = sum(h*sp.Heaviside(vj - up) for h, vj in zip(hs, vs_))
    lhs = 2*sp.integrate((up*eta_s).subs(vals), (up, uu, 4))
    rhs = sum(h*(vj**2 - uu**2)*sp.Heaviside(vj - uu) for h, vj in zip(hs, vs_)).subs(vals)
    ok14 &= is0(lhs - rhs)
rep("WP6v2-C14 step basis: xi~ = sum_j eta~_j (v_j^2 - u^2) Theta(v_j - u)  (4.1)", ok14)

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
rep("WP6v2-C15a projection Pi_mom kills moments 0,1,2: constraints (6.1) hold for every theta_A  (5.1')", ok15)
aa2 = Q(3, 10)
viol = (1 + aa2)**Q(1, 2) + (1 - aa2)**Q(1, 2) - 2
rep("WP6v2-C15b M type: two-bin zeroth moment (1+a)^th + (1-a)^th - 2 != 0 at th = 1/2, = 0 at th = 0, 1; O(th(1-th)a^2)",
    float(viol) < 0 and all(is0((1 + aa2)**t0 + (1 - aa2)**t0 - 2) for t0 in (0, 1))
    and abs(float(viol) - float(-Q(1, 2)*Q(1, 2)*aa2**2/2*2)) < 2e-3)

print(f"\n{sum(RES)}/{len(RES)} checks PASS")
