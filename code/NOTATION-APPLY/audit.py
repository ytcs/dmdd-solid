"""NOTATION-APPLY consistency audit (sympy). Each check prints PASS/FAIL."""
import sympy as sp
res = []
def rep(tag, ok, note=""):
    res.append((tag, bool(ok))); print(f"{'PASS' if ok else 'FAIL'}  {tag}  {note}")

q, w, m, mu, v0, vmin, rho, rhoT, sig, F, Sb, al, Om, N, Vv, c = sp.symbols(
    'q omega m_chi mu v0 v_min rho_chi rho_T sigbar F Sbar alpha Omega N V c', positive=True)
e2 = 4*sp.pi*al
# A1: isotropic velocity integral = eta/(2q). Shell distribution f = delta(v-v0)/(4 pi v0^2).
ct = sp.symbols('ct', real=True)
G = sp.integrate(2*sp.pi*v0**2/(4*sp.pi*v0**2)*sp.DiracDelta(w - q*v0*ct + q**2/(2*m)), (ct, -1, 1))
G = sp.simplify(G.subs({w: q*v0/3}))  # a point inside the kinematic range
# both G and eta carry the same step Theta(v0 - v_min); compare the coefficients
G = G.replace(sp.Heaviside, lambda *a: 1)
eta = 1/v0
rep("A1 int d3v f delta(omega-omega_q) = eta(v_min)/(2q)  [WP0 9.1, REF-A; D1 eta/q wrong]",
    sp.simplify(G - eta/(2*q)) == 0, f"G={G}")
# A2: rate prefactor
dR = (rho/(m*rhoT))*(sp.pi*sig*F**2/mu**2)*(4*sp.pi*q**2/(2*sp.pi)**3)*(eta/(2*q))*Sb
rep("A2 dR/domega dq = rho sig/(4 pi m rhoT mu^2) q F^2 eta S  [WP0 9.2 = WP6 1.4]",
    sp.simplify(dR - rho*sig/(4*sp.pi*m*rhoT*mu**2)*q*F**2*eta*Sb) == 0)
dR_D1 = (rho/(m*rhoT))*(sp.pi*sig*F**2/mu**2)*(4*sp.pi*q**2/(2*sp.pi)**3)*(eta/q)*Sb
rep("A2b D1 printed 1/(2pi) prefactor is 2x the correct one", sp.simplify(dR_D1/dR) == 2)
# WP6 (1.4): rho/(4 pi^2 m rhoT) * q * A0 eta with A0 = pi sig F^2 S/mu^2
rep("A2c WP6 (1.4) A0-form equals WP0 (9.2)",
    sp.simplify(rho/(4*sp.pi**2*m*rhoT)*q*(sp.pi*sig*F**2*Sb/mu**2)*eta - dR/1) == 0)
# A3: Hochberg S.9 with S = 2 q^2 W/e^2, |V|^2 arbitrary
Wl, V2 = sp.symbols('W V2', positive=True)
lhs = (rho/(m*rhoT))*V2*(4*sp.pi*q**2/(2*sp.pi)**3)*(eta/(2*q))*(2*q**2*Wl/e2)
rhs = rho/(2*sp.pi**2*e2*rhoT*m)*q**3*V2*Wl*eta
rep("A3 Hochberg 2101.08263 (S.9) = WP0 (3.4)+(9.1)+FDT", sp.simplify(lhs-rhs) == 0)
# A4: S <-> L factor
rep("A4 2q^2/e^2 = q^2/(2 pi alpha)  [KKL eq 6]", sp.simplify(2*q**2/e2 - q**2/(2*sp.pi*al)) == 0)
# A5: f_crys dictionary vs 1509.01598 eq 17 (per target mass: divide by N_cell * rho_T Omega)
me, f2 = sp.symbols('m_e f2', positive=True)
essig = (rho/m)*(1/(rhoT*Om))*sig*al*me**2/mu**2*(1/q**2)*eta*F**2*f2   # dR/domega dq
fsol = sp.solve(sp.Eq(essig, dR), f2)[0]
rep("A5 |f_crys|^2 = Omega q^3 S/(4 pi alpha m_e^2)  [WP1 E12 = WP6 1.5]",
    sp.simplify(fsol - Om*q**3*Sb/(4*sp.pi*al*me**2)) == 0)
fsol_D1 = sp.solve(sp.Eq(essig, dR_D1), f2)[0]
rep("A5b D1's 'Omega q^3 S/(2 pi alpha m_e^2)' follows only from eta/q (factor 2)",
    sp.simplify(fsol_D1 - Om*q**3*Sb/(2*sp.pi*al*me**2)) == 0)
L = sp.symbols('L', positive=True)
rep("A5c ELF form Omega q^5 L/(8 pi^2 alpha^2 m_e^2)  [2101.08275 eq 16]",
    sp.simplify(fsol.subs(Sb, 2*q**2*L/e2) - Om*q**5*L/(8*sp.pi**2*al**2*me**2)) == 0)
# A6: eps2^PA normalisations. avg = N^-2 sum_{kQ}|M_D1|^2.
avg = sp.symbols('avg', positive=True)
D1 = 8*sp.pi**2*al/(Om*q**2)*avg
D2 = 2*sp.pi*e2/(q**2*N*Om)*(N**2*avg/N)    # sum_kQ |M_D2|^2 = N^2 avg / N
rep("A6 D1 (4) = D2 (2.2) with M_D2 = M_D1/sqrt(N), V = N Omega", sp.simplify(D1-D2) == 0)
SPA = 4*sp.pi/Om*avg
rep("A6b D1 (2)/WP3 (W.4c) S^PA=(4pi/Omega)<<|M|^2>> -> eps2=(e^2/2q^2)S = D1 (4) = X2 (2.3) via L",
    sp.simplify(e2/(2*q**2)*SPA - D1) == 0)
# A7: optical prefactor. EPW eq 63: 2*pi e^2/(eps0 Omega omega^2) with e^2/eps0 -> 4 pi alpha (SI->HL)
rep("A7 EPW 2302.08085 eq 63 prefactor -> 8 pi^2 alpha/(Omega omega^2)",
    sp.simplify(2*sp.pi*(4*sp.pi*al)/(Om*w**2) - 8*sp.pi**2*al/(Om*w**2)) == 0)
nr, cc = sp.symbols('n_r c_light', positive=True)
alpha_abs = 2*(4*sp.pi**2*al)/(w*cc*nr)/Om*avg      # Noffsinger eq 1, Gaussian e^2 = alpha
rep("A7b Noffsinger eq 1: eps2 = n_r c alpha_abs/omega = 8 pi^2 alpha/(Omega omega^2)<<.>>",
    sp.simplify(nr*cc*alpha_abs/w - 8*sp.pi**2*al/(Om*w**2)*avg) == 0)
# A8: on-shell equality of the first denominator, D1 vs D2
ec, ev, em, wQ = sp.symbols('e_c e_v e_m omega_Q', real=True)
for s in (1, -1):
    w_os = ec - ev + s*wQ
    assert sp.simplify((w_os - em + ev) - (ec - em + s*wQ)) == 0
rep("A8 D2 first denominator (omega-e_m+e_v) = D1 (e_c'-e_m +- omega_Q) on shell, both signs", True)
# A9: X1 identity (D + v P)/(v +- c) = P + (D -+ c P)/(v +- c)
Dd, vv, P = sp.symbols('D v P', real=True)
ok = all(sp.simplify((Dd+vv*P)/(vv+s*c) - (P + (Dd - s*c*P)/(vv+s*c))) == 0 for s in (1, -1))
rep("A9 X1 (X1') -> (X1) with Xi = D + v (x) P", ok)
# A10: X2 coherent-potential limit and K5
U, chi0, chi0f, vC, rr = sp.symbols('U chi0 chi0f v_C rho')
Mt = U*rr + rr*(vC/(1 - vC*chi0))*(U*chi0)        # M + rho W T with T = U chi0, W = v/eps
rep("A10 X2: M_tilde = M/eps(P,omega_f) when M = U rho (coherent potential) [= WP0 5.6 M~rho]",
    sp.simplify(Mt - U*rr/(1 - vC*chi0)) == 0)
eps = lambda x: 1 - vC*x
rep("A10b X2 K5: eps(w)eps(wf)[chi(w)-chi(wf)] = chi0(w)-chi0(wf)",
    sp.simplify(eps(chi0)*eps(chi0f)*(chi0/eps(chi0) - chi0f/eps(chi0f)) - (chi0 - chi0f)) == 0)
# A11: WP6 xi = 2 int u eta  (radial f)
u, vv2 = sp.symbols('u vv', positive=True)
f = sp.Function('f')
eta_u = sp.Integral(4*sp.pi*vv2**2*f(vv2)/vv2, (vv2, u, sp.oo))
xi_u = sp.Integral(4*sp.pi*vv2**2*f(vv2)*(vv2**2-u**2)/vv2, (vv2, u, sp.oo))
rep("A11 WP6 (1.3) d xi/du = -2 u eta(u)", sp.simplify(sp.diff(xi_u, u).doit() + 2*u*eta_u.doit()) == 0)
# A12: f-sum normalisation with free recoil S = (2pi/V) N delta(omega - q^2/2M) at T=0
n, Mm = sp.symbols('n M', positive=True)
first = 2*sp.pi*n*(q**2/(2*Mm))   # int omega S d omega
rep("A12 int_-inf^inf omega S = pi n q^2/M (WP6 W1); WP0 (8.2) '2 pi n q^2/m' is 2x",
    sp.simplify(first - sp.pi*n*q**2/Mm) == 0 and sp.simplify(2*sp.pi*n*q**2/Mm/first) == 2)
rep("A12b D2 §3: int_0^inf omega S d omega/2pi = n q^2/2m", sp.simplify(first/(2*sp.pi) - n*q**2/(2*Mm)) == 0)
# A13: [p^2/2m, e^{iqx}] = q j with j = (p e + e p)/2m  (1D, acting on psi)
x = sp.symbols('x', real=True); psi = sp.Function('psi')(x); me1 = sp.symbols('m', positive=True)
p = lambda g: -sp.I*sp.diff(g, x)
E = sp.exp(sp.I*q*x)
lhs = (p(p(E*psi)) - E*p(p(psi)))/(2*me1)
j = (p(E*psi) + E*p(psi))/(2*me1)
rep("A13 [T,n_q] = q.j exactly (WP1 D1); WP0 extra (q^2/2m)n term is wrong", sp.simplify(lhs - q*j) == 0,
    f"residual of WP0 form: {sp.simplify(lhs - q*j - q**2/(2*me1)*E*psi) != 0}")
# A14: Fano thinning
eta_d, Ff, nn = sp.symbols('eta_det F n', positive=True)
var = eta_d**2*Ff*nn + eta_d*(1-eta_d)*nn; mean = eta_d*nn
rep("A14 WP5: F_meas = eta F + 1 - eta", sp.simplify(var/mean - (eta_d*Ff + 1 - eta_d)) == 0)
# A15: WP4 exothermic Jacobian and [7.2] prefactor
qs = sp.symbols('q_star', positive=True); ff = sp.symbols('Fnu2', positive=True)
Gam = (4*sp.pi*qs**2/(2*sp.pi)**3)*(2*sp.pi/Om)*ff*(m/qs)   # int q^2 dq delta(...) = m q*  -> q*^2 * (m/q*)
rep("A15 WP4 [7.2]: Gamma_nu = m q*/(pi Omega) <D|F|^2>", sp.simplify(Gam - m*qs*ff/(sp.pi*Om)) == 0)
# A16: sigma_e anchor
c1 = sp.symbols('c1', positive=True)
Vn = c1/(4*m*me)
rep("A16 WP0 (2.3): sigbar_e = mu^2|c1|^2/(16 pi m^2 m_e^2) = (mu^2/pi)|V|^2",
    sp.simplify(mu**2*c1**2/(16*sp.pi*m**2*me**2) - mu**2/sp.pi*Vn**2) == 0)
# A17: numbers
ckms = 299792.458
vsun = (11.1**2 + (238+12.2)**2 + 7.3**2)**0.5
print(f"      |v_lsr+v_pec| = {vsun:.2f} km/s ; v_esc + |v_sun| = {544+vsun:.1f} km/s")
mmin = lambda E, vm: 2*E/(vm/ckms)**2/1e6
print(f"      m_min(1.12 eV, 794) = {mmin(1.12,794):.3f} MeV ; m_min(1.170+0.018, 794) = {mmin(1.188,794):.3f} MeV ;"
      f" annual band v_max 781..810 -> {mmin(1.12,810):.3f}..{mmin(1.12,781):.3f} MeV")
qx, Ex = 1940.0, 1.170-0.0147
mx = qx**2/(2*(qx*794/ckms - Ex))/1e6
print(f"      WP1 Si zero-phonon exciton threshold (q=1.94 keV, E_x=1.155 eV) = {mx:.3f} MeV")
rep("A17 numbers: |v_sun|=250.5; m_min 0.319/0.339 MeV; WP1 exciton 0.473 MeV",
    abs(vsun-250.5) < 0.1 and abs(mmin(1.12,794)-0.319) < 2e-3 and abs(mmin(1.188,794)-0.339) < 2e-3 and abs(mx-0.473) < 3e-3)
# A18: hyperfine (2/3) s.I = (1/3) sigma.I
sI = sp.symbols('sI'); rep("A18 WP4 D1: (2/3) s.I = (1/3) sigma.I (WP0 (2/3) sigma.I is 2x)",
    sp.simplify(sp.Rational(2,3)*sI - sp.Rational(1,3)*(2*sI)) == 0)
print(f"\n{sum(o for _,o in res)}/{len(res)} PASS")
