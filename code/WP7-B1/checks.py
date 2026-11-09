#!/usr/bin/env python3
"""R10 / WP7-B1 checks (sympy exact where possible; mpmath/scipy quadrature for C6a, C9b, C10).
Run: python3 checks.py   (target < 2 min). Every check prints PASS/FAIL; exit code 1 on any FAIL.
Labels are cited in returns/R10/WP7-B1.md as WP7B1-Cn."""
import sys
import numpy as np
import sympy as sp
import mpmath as mp
from scipy import integrate

RES = []


def rec(label, ok, note=""):
    RES.append((label, bool(ok)))
    print(f"{label:6s} {'PASS' if ok else 'FAIL'}  {note}")


# ---------------------------------------------------------------- C1 (E5)
# C1a: exciton (Davydov) mixing is unitary => sum_lambda |sum_kappa c*_{kappa lambda} a_kappa|^2 = sum_kappa |a_kappa|^2
th, al, be, ph = sp.symbols('theta alpha beta phi', real=True)
a1, a2, b1, b2 = sp.symbols('a1 a2 b1 b2', real=True)
A = sp.cos(th) * sp.exp(sp.I * al)
B = sp.sin(th) * sp.exp(sp.I * be)
U = sp.Matrix([[A, B], [-sp.conjugate(B) * sp.exp(sp.I * ph), sp.conjugate(A) * sp.exp(sp.I * ph)]])
x = sp.Matrix([a1 + sp.I * b1, a2 + sp.I * b2])
tot = sum(sp.Abs(sum(sp.conjugate(U[k, l]) * x[k] for k in range(2))) ** 2 for l in range(2))
diff = sp.simplify(sp.expand(sp.expand_complex(tot - (a1**2 + b1**2 + a2**2 + b2**2))))
rec("C1a", diff == 0, "Frenkel: incoherent molecule sum = coherent exciton sum (bins >> Davydov splitting)")
rng = np.random.default_rng(1)
Z = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
Q4, _ = np.linalg.qr(Z)
av = rng.normal(size=4) + 1j * rng.normal(size=4)
rec("C1a'", abs(np.sum(np.abs(Q4.conj().T @ av) ** 2) - np.sum(np.abs(av) ** 2)) < 1e-12, "4 molecules/cell (t-stilbene)")
# C1b: prefactors of 1912.02822 Eq.(19) and 2103.08601 Eq.(8) from WP0-v3 (3.3) with S = 2*pi*n_mol*sum|f|^2 delta
pref19 = sp.pi * 2 * sp.pi / ((2 * sp.pi) ** 3 * 2)          # |V|^2 = pi sigma/mu^2 ; 2 pi delta ; eta/(2q)
pref8 = sp.pi * 2 * sp.pi / (2 * sp.pi) ** 3
rec("C1b", sp.simplify(pref19 - 1 / (8 * sp.pi)) == 0 and sp.simplify(pref8 - 1 / (4 * sp.pi)) == 0,
    "1/(8 pi) [1912.02822 (19)], d^3q/(4 pi) [2103.08601 (8)]")
# isotropic velocity kernel: int d^3v g(v) delta(DE + q^2/2m - q.v) = (1/2q) int 4 pi v dv g Theta = eta/(2q)
v, q, c, vm = sp.symbols('v q c v_m', positive=True)
inner = sp.integrate(sp.DiracDelta(q * v * c - q * vm), (c, -1, 1))   # vm < v assumed
rec("C1c", sp.simplify(inner.subs(vm, v / 2) - 1 / (q * v)) == 0, "angular delta -> 1/(qv): G = eta/(2q)")

# ---------------------------------------------------------------- C2 (E8, 1D Luttinger)
vF, V, qq, w, g2, g4, N = sp.symbols('v_F V q omega g2 g4 N', positive=True)
gL = sp.sqrt((2 * sp.pi * vF + g4 - g2) / (2 * sp.pi * vF + g4 + g2))
vL = sp.sqrt((vF + g4 / (2 * sp.pi)) ** 2 - (g2 / (2 * sp.pi)) ** 2)
rec("C2a", sp.simplify((gL * vL).subs({g2: V, g4: V}) - vF) == 0,
    "2607.15338 Eq.(3): g v = v_F when g2 = g4 (density-density) <=> f-sum")
# 1D RPA with linear bubble, N channels: R0 = N vF q^2/(pi (w^2 - vF^2 q^2)); pole and residue
R0 = N * vF * qq**2 / (sp.pi * (w**2 - vF**2 * qq**2))
den = sp.together(1 - V * R0)
pole = sp.solve(sp.numer(den), w)
wpl = [p for p in pole if p.is_positive is not False][0]
gc = 1 / sp.sqrt(1 + N * V / (sp.pi * vF))
rec("C2b", sp.simplify(wpl - vF * qq / gc) == 0, "1D RPA plasmon v_c = v_F/g_c, g_c = (1+N V/(pi v_F))^(-1/2)")
R = sp.simplify(R0 / den)
resid = sp.simplify(sp.limit((w - wpl) * R, w, wpl))
# retarded: 1/(w - wpl + i0) -> -i pi delta, so Im R = -pi resid delta and S = -2 Im R = 2 pi resid delta
weight = sp.simplify(2 * sp.pi * resid)
rec("C2c", sp.simplify(weight - N * gc * qq) == 0, "S = N g_c |q| delta(w - v_c q) = 2607.15338 Eq.(4) (N=1)")
rec("C2d", sp.simplify(weight * wpl - N * vF * qq**2) == 0, "f-sum: int w S = N v_F q^2 = pi n q^2/m (Galilean, n=N k_F/pi)")

# ---------------------------------------------------------------- C3 (E8, demon / acoustic plasmon)
k, Om, qa = sp.symbols('k Omega q', positive=True)
eps = 1 + k**2 / qa**2 - Om**2 / w**2
wa = Om * qa / sp.sqrt(qa**2 + k**2)
rec("C3a", sp.simplify(eps.subs(w, wa)) == 0, "acoustic zero of eps")
L_weight = sp.pi / sp.diff(eps, w).subs(w, wa)        # L = pi delta(w - wa)/eps'
f_share = sp.simplify(wa * L_weight / (sp.pi * Om**2 / 2))
rec("C3b", sp.simplify(f_share - (qa**2 / (qa**2 + k**2)) ** 2) == 0, "f-sum share of acoustic mode = (q^2/(q^2+k_TF^2))^2")

# ---------------------------------------------------------------- C4 (E9)
mp.mp.dps = 30
qv, qz, Lv = mp.mpf('0.7'), mp.mpf('0.4'), mp.mpf('2.3')
lhs = mp.nsum(lambda n: 1 / (qv**2 + (qz + 2 * mp.pi * n / Lv) ** 2), [-mp.inf, mp.inf]) / Lv
rhs = mp.sinh(qv * Lv) / (2 * qv * (mp.cosh(qv * Lv) - mp.cos(qz * Lv)))
rec("C4a", abs(lhs - rhs) < mp.mpf('1e-20'), "layered-sheet Coulomb sum = (1/2q) sinh/(cosh - cos)")
Qs, Qz, Ls = sp.symbols('q q_z L', positive=True)
VL = sp.sinh(Qs * Ls) / (2 * Qs * (sp.cosh(Qs * Ls) - sp.cos(Qz * Ls)))
t = sp.symbols('t', positive=True)
small = sp.series(VL.subs({Qs: t * Qs, Qz: t * Qz}), t, 0, 0).removeO()
rec("C4b", sp.simplify(small * t**2 - 1 / (Ls * (Qs**2 + Qz**2))) == 0, "qL -> 0: 3D Coulomb with n_3D = n_2D/L")
rec("C4b'", sp.limit(VL * 2 * Qs, Ls, sp.oo) == 1, "L -> oo: isolated sheet e^2/(2q)")
e1, e2, f, s = sp.symbols('epsilon_1 epsilon_2 f s')
epar = f * e1 + (1 - f) * e2
eperp = 1 / (f / e1 + (1 - f) / e2)
emt_inv = 1 / (epar * s + eperp * (1 - s))     # s = k_parallel^2/k^2 (their k_z)
lp16 = ((1 - f) * e1 + f * e2) / (e1 * e2 + (1 - f) * f * (e1 - e2) ** 2 * s)
rec("C4c", sp.simplify(emt_inv - lp16) == 0, "2110.01587 Eq.(16) = exact uniaxial EMT (any d/L, kL << 1)")

# C4d: Rytov transfer matrix for a periodic stack of local dielectrics and its k -> 0 limit (= EMT mode condition)
kk2, d1, d2, eA, eB, tq = sp.symbols('k d_1 d_2 epsilon_A epsilon_B t', positive=True)
Mlay = lambda e_, d_: sp.Matrix([[sp.cosh(kk2 * d_), sp.sinh(kk2 * d_) / (e_ * kk2)], [e_ * kk2 * sp.sinh(kk2 * d_), sp.cosh(kk2 * d_)]])
half_tr = sp.simplify((Mlay(eB, d2) * Mlay(eA, d1)).trace() / 2)
rytov = sp.cosh(kk2 * d1) * sp.cosh(kk2 * d2) + (eA / eB + eB / eA) * sp.sinh(kk2 * d1) * sp.sinh(kk2 * d2) / 2
ok4d = sp.simplify(sp.expand((half_tr - rytov).rewrite(sp.exp))) == 0
ff = d1 / (d1 + d2)
ratio_emt = (ff * eA + (1 - ff) * eB) * (ff / eA + (1 - ff) / eB) * (d1 + d2) ** 2
ser = sp.series(rytov.subs(kk2, tq * kk2), tq, 0, 3).removeO()
coef = sp.simplify(sp.expand(ser - 1).coeff(tq, 2) * 2 / kk2**2)       # cos(q a) ~ 1 - q^2 a^2/2 => q^2 a^2 = -k^2 coef
ok4d &= sp.simplify(coef - ratio_emt) == 0
rec("C4d", ok4d, "Rytov: (1/2)tr M_B M_A = cosh cosh + (eA/eB+eB/eA)/2 sinh sinh; k->0 gives eps_par k^2 + eps_perp q_perp^2 = 0")

# ---------------------------------------------------------------- C5 (E10, dielectric sphere)
l, ei, eo, Rr, Acoef, Bcoef = sp.symbols('l epsilon_in epsilon_out R A B', positive=True)
sol = sp.solve([sp.Eq(Acoef * Rr**l, Rr**l + Bcoef * Rr**(-l - 1)),
                sp.Eq(ei * l * Acoef * Rr**(l - 1), eo * (l * Rr**(l - 1) - (l + 1) * Bcoef * Rr**(-l - 2)))],
               [Acoef, Bcoef], dict=True)[0]
rec("C5", sp.simplify(sol[Acoef] - (2 * l + 1) * eo / (l * ei + (l + 1) * eo)) == 0,
    "QD multipole local-field factor (2l+1)eps_out/(l eps_in + (l+1) eps_out)")

# ---------------------------------------------------------------- C6 (E12, 2D Dirac sheet)
def imchi0_num(qn, wn, vn=1.0, gdeg=4):
    Om_ = wn / vn

    def integrand(thv):
        cth = np.cos(thv)
        kk = (Om_**2 - qn**2) / (2 * (Om_ + qn * cth))
        kq = np.sqrt(kk**2 + qn**2 + 2 * kk * qn * cth)
        dsdk = 1 + (kk + qn * cth) / kq
        cosphi = (kk + qn * cth) / kq
        return kk * 0.5 * (1 - cosphi) / (vn * dsdk)
    val, _ = integrate.quad(integrand, 0, 2 * np.pi, limit=200)
    return -np.pi * gdeg * val / (2 * np.pi) ** 2


ok6 = True
for (qn, wn) in [(0.3, 1.0), (1.0, 1.7), (0.05, 0.4)]:
    num = imchi0_num(qn, wn)
    ana = -(4 / 16) * qn**2 / np.sqrt(wn**2 - qn**2)
    ok6 &= abs(num / ana - 1) < 1e-7
rec("C6a", ok6, "undoped graphene Im chi0 = -(g/16) q^2/sqrt(w^2 - v^2 q^2)")
z, sig, qp = sp.symbols('z sigma q', positive=True)
Aamp = sp.symbols('A')
solA = sp.solve(sp.Eq(e1 * qp * Aamp + e2 * qp * Aamp, sig), Aamp)[0]
rec("C6b", sp.simplify(solA - sig / (qp * (e1 + e2))) == 0, "sheet on substrate: V_2D = e^2/(q(eps_1+eps_2))")
n2, me, eb, e2c = sp.symbols('n_2D m e_b e2', positive=True)
w2d = sp.solve(sp.Eq(eb - (e2c / (2 * qp)) * n2 * qp**2 / (me * w**2), 0), w)
rec("C6c", any(sp.simplify(r**2 - e2c * n2 * qp / (2 * me * eb)) == 0 for r in w2d), "2D plasmon w^2 = e^2 n q/(2 m eps_bar)")

# ---------------------------------------------------------------- C7 (X6, 2011.13352 Eq.(11) prefactor from (W.5))
rho, mchi, sig_n, mu, Aat, Zion, alpha, Om_c, M, NT = sp.symbols('rho m_chi sigma mu A Z alpha Omega M N_T', positive=True)
# R = N_T rho/m int d^3v f/v * (|V|^2/(2 pi)) int q dq int dw dP/dw ; |V|^2 = A^2 pi sigma/mu^2 ;
# dP/dw = 4 alpha Z^2 q^2 F/(3 M^2 w^4 Omega)
pref_urf = NT * rho / mchi * (Aat**2 * sp.pi * sig_n / mu**2) / (2 * sp.pi) * 4 * alpha * Zion**2 / (3 * M**2 * Om_c)
pref_src = rho / mchi * 2 * Aat**2 * sig_n * Zion**2 * alpha * NT / (3 * mu**2 * Om_c * M**2)
rec("C7", sp.simplify(pref_urf - pref_src) == 0, "2011.13352 Eq.(11) = WP3 (W.5) T0-T5(imp), valence Z_ion, LFE kept")

# ---------------------------------------------------------------- C8 (X8, hydrogenic bound-state Migdal)
r, cc, kk_ = sp.symbols('r c k', positive=True)
psi1s = sp.exp(-r) / sp.sqrt(sp.pi)
psi2p_ang = r * sp.exp(-r / 2) / (4 * sp.sqrt(2 * sp.pi))      # times cos(theta)
ang = sp.integrate(cc * sp.exp(sp.I * kk_ * r * cc), (cc, -1, 1))
amp = 2 * sp.pi * sp.integrate(sp.simplify(r**2 * psi2p_ang * psi1s * ang), (r, 0, sp.oo))
P = sp.simplify(sp.Abs(sp.simplify(amp)) ** 2)
P_closed = sp.Rational(2**15, 3**10) * kk_**2 / (1 + sp.Rational(4, 9) * kk_**2) ** 6
rec("C8", sp.simplify(P - P_closed) == 0, "P(1s->2p0) = (2^15/3^10) q_e^2 a^2/(1 + 4 q_e^2 a^2/9)^6; dipole limit (2^15/3^10) q_e^2")

# ---------------------------------------------------------------- C9 (A2)
Wv, wD, lam, Wp = sp.symbols('omega omega_D lambda Omega', positive=True)
Acoef2 = 2 * lam / wD**4                                     # alpha^2F_tr = A Omega^4 below omega_D, lambda_tr = 2 int a2F/Omega
lo = sp.simplify(2 * sp.pi / Wv * sp.integrate((Wv - Wp) * Acoef2 * Wp**4, (Wp, 0, Wv)))
hi = sp.simplify(2 * sp.pi / Wv * sp.integrate((Wv - Wp) * Acoef2 * Wp**4, (Wp, 0, wD)))
rec("C9a", sp.simplify(lo - sp.Rational(2, 15) * sp.pi * lam * Wv**5 / wD**4) == 0 and
    sp.simplify(hi - sp.Rational(4, 5) * sp.pi * lam * wD * (1 - sp.Rational(5, 6) * wD / Wv)) == 0,
    "Allen 1/tau(w) with Debye a2F = 1604.06800 Eq.(16) (both branches)")
mp.mp.dps = 20
ok9 = True
for Dl in [mp.mpf('0.1'), mp.mpf('0.3'), mp.mpf('0.45')]:
    x_ = mp.mpf(1)
    b = 2 * Dl / x_
    fI = lambda E: (E * (x_ - E) + Dl**2) / (mp.sqrt(E**2 - Dl**2) * mp.sqrt((x_ - E) ** 2 - Dl**2))
    fII = lambda E: (E * (x_ - E) - Dl**2) / (mp.sqrt(E**2 - Dl**2) * mp.sqrt((x_ - E) ** 2 - Dl**2))
    II = mp.quad(fI, [Dl, x_ / 2, x_ - Dl])
    III = mp.quad(fII, [Dl, x_ / 2, x_ - Dl])
    m1 = 1 - b**2
    ok9 &= abs(II - x_ * mp.ellipe(m1)) < 1e-10
    ok9 &= abs(III - x_ * (mp.ellipe(m1) - b**2 * mp.ellipk(m1))) < 1e-10
    y = 2 / b
    kmod = (y - 2) / (y + 2)
    gI = (1 + 2 / y) * mp.ellipe(kmod**2) - 4 * mp.ellipk(kmod**2) / (y + 2)
    ok9 &= abs(gI - mp.ellipe(m1)) < 1e-12
rec("C9b", ok9, "case-I pair integral = x E(sqrt(1-4D^2/x^2)) = x g_I (WP4 [4.2]) = 1604.06800 Eq.(17); MB = E - b^2 K")

# ---------------------------------------------------------------- C10 (A6, 2212.04504 Eq.(12) q-shape)
mp.mp.dps = 15
kf = mp.mpf(1)
eta_c = -1 / kf


def Tq(qn, lmax=14):
    tot_ = mp.mpf(0)
    for ll in range(lmax + 1):
        fint = lambda rr: rr**2 * (mp.coulombf(ll, eta_c, kf * rr) / (kf * rr)) * mp.sqrt(mp.pi / (2 * qn * rr)) * \
            mp.besselj(ll + mp.mpf(1) / 2, qn * rr) * mp.exp(-rr)
        Il = mp.quad(fint, [0, 2, 6, 15, 40])
        tot_ += (2 * ll + 1) * Il**2
    return tot_


def Gform(qn, corr=True):
    pre = (3 * qn**2 if corr else 3 * qn) + kf**2 + 1
    return qn**2 * pre * mp.exp(-(2 / kf) * mp.atan2(2 * kf, qn**2 - kf**2 + 1)) / \
        (((qn + kf) ** 2 + 1) ** 3 * ((qn - kf) ** 2 + 1) ** 3)


q1, q2 = mp.mpf('0.5'), mp.mpf('2')
ratio_num = Tq(q1) / Tq(q2)
r_corr = Gform(q1) / Gform(q2)
r_mis = Gform(q1, False) / Gform(q2, False)
rec("C10", abs(ratio_num / r_corr - 1) < 1e-6 and abs(ratio_num / r_mis - 1) > 0.05,
    f"hydrogenic 1s->continuum: (3q^2+k^2+1) correct; printed '3q' off by x{float(r_mis/ratio_num):.3f} at q=0.5,2")

# ---------------------------------------------------------------- C11 (I3, exothermic shell)
mm, vv, Dd, Fc = sp.symbols('m v D F', positive=True)
qp_ = mm * vv + sp.sqrt(mm**2 * vv**2 + 2 * mm * Dd)
qm_ = -mm * vv + sp.sqrt(mm**2 * vv**2 + 2 * mm * Dd)
shell = sp.simplify(2 * sp.pi * Fc / vv * (qp_**2 - qm_**2) / 2)
rec("C11", sp.simplify(shell - 4 * sp.pi * mm * Fc * sp.sqrt(2 * mm * Dd + mm**2 * vv**2)) == 0,
    "int d^3q delta(w-|D|-q.v+q^2/2m) F = 4 pi m F sqrt(q*^2 + m^2 v^2): halo-independent to O(v^2/v*^2)")

# ---------------------------------------------------------------- C12 (I5, relativistic DM vertex)
I2 = sp.eye(2)
sx, sy, sz = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
g0 = sp.diag(1, 1, -1, -1)
gs = [sp.Matrix(sp.BlockMatrix([[sp.zeros(2), si], [-si, sp.zeros(2)]])) for si in (sx, sy, sz)]
E1, E2, mD = sp.symbols('E E_p m', positive=True)
p1 = sp.symbols('p1:4', real=True)
p2 = sp.symbols('pp1:4', real=True)
slash = lambda E_, p_: E_ * g0 - sum((p_[i] * gs[i] for i in range(3)), sp.zeros(4))
T = sp.simplify(((slash(E2, p2) + mD * sp.eye(4)) * g0 * (slash(E1, p1) + mD * sp.eye(4)) * g0).trace() / 2)
dot = sum(p1[i] * p2[i] for i in range(3))
Qsq = sum((p1[i] - p2[i]) ** 2 for i in range(3))
target = (E1 + E2) ** 2 - Qsq
diffT = sp.simplify(sp.expand(T - target + (E1**2 - mD**2 - sum(pi_**2 for pi_ in p1))
                              + (E2**2 - mD**2 - sum(pi_**2 for pi_ in p2))))   # mass-shell terms vanish
rec("C12a", diffT == 0, "(1/2)Tr[(p'+m)g0(p+m)g0] = (2E-w)^2 - Q^2 on shell (2401.11971 Eq.(5) numerator)")
Ev, wv, Qv = sp.symbols('E w Q', positive=True)
ratio5 = ((2 * Ev - wv) ** 2 - Qv**2) / (4 * Ev * (Ev - wv))
rec("C12b", sp.limit(ratio5.subs({Ev: mD, wv: 0, Qv: 0}), mD, 1) == 1, "NR limit of the relativistic factor = 1")

# C12c: conserved currents, vector mediator: longitudinal part of J_chi.J_e = J0 rho (1 - w^2/Q^2) (Coulomb gauge)
J0, rh, mV = sp.symbols('J0 rho m_V')
amp_full = (J0 * rh - (wv / Qv * J0) * (wv / Qv * rh)) / (Qv**2 - wv**2 + mV**2)
amp_src = J0 * rh / (Qv**2 - wv**2 + mV**2)
rec("C12c", sp.simplify((amp_full / amp_src) - (1 - wv**2 / Qv**2)) == 0 and
    sp.simplify(amp_full.subs(mV, 0) - J0 * rh / Qv**2) == 0,
    "density row carries (1 - w^2/Q^2); massless mediator: exactly Coulomb 1/Q^2 (2401.11971 Eq.(5) lacks it)")

nf = sum(1 for _, o in RES if not o)
print(f"\n{len(RES) - nf}/{len(RES)} PASS")
sys.exit(1 if nf else 0)
