#!/usr/bin/env python3
"""R12 / WP7-B2-v2 checks (v1 checks kept; C3, C4a, C15, C16 corrected; C21-C28 new)
R10 / WP7-B2 checks (sympy, exact where possible; small numpy pieces only for random-matrix sanity checks).

Run:  python3 checks.py      (all checks must print PASS; total runtime << 2 min)
Labels WP7B2v2-Cn are cited in returns/R12/WP7-B2-v2.md.
Units: hbar = c = k_B = 1, Heaviside-Lorentz e^2 = 4 pi alpha (CONVENTIONS sec. 1).
"""
import sympy as sp
import numpy as np

RESULTS = []


def check(label, cond, note=""):
    ok = bool(cond)
    RESULTS.append((label, ok))
    print(f"{label:10s} {'PASS' if ok else 'FAIL'}  {note}")


# ---------------------------------------------------------------------------------------------
# C1  A4: WP0-v3 (3.5) with the one-phonon S equals 2308.06314 Eq. (2) with Eq. (16) (self-energy form)
#     -Im[2 w_nu/(w^2 - w_nu^2 + i w g)] integrates to pi over w>0 for every g>0 (so -> pi delta(w - w_nu))
w, wn, g, y, F2, Om = sp.symbols('omega omega_nu gamma y F2 Omega', positive=True)
lor = sp.simplify(-sp.im(2*wn/(w**2 - wn**2 + sp.I*w*g)))
lor = sp.simplify(2*wn*w*g/((w**2 - wn**2)**2 + w**2*g**2))
import mpmath as _mp
val = []
for gg in (1e-2, 1e-3, 1e-4):
    fl = sp.lambdify(w, lor.subs({wn: 1, g: gg}), 'mpmath')
    val.append((gg, _mp.quad(fl, [0, 0.5, 1 - 20*gg, 1, 1 + 20*gg, 2, _mp.inf])))
check("C1a", all(abs(v - _mp.pi) < 2*gg for gg, v in val), "int_0^inf -Im[2w_nu/(w^2-w_nu^2+iwg)] dw -> pi as g->0 (error < 2g)")
# Gamma_URF = (y^2/2w) S,  S = (2pi/Omega)|F.T|^2 delta ;  Gamma_2308 = -(1/w) Im Pi,  Pi = (y^2/Omega)|F.T|^2 * 2w_nu/(...)
G_urf = y**2/(2*w)*(2*sp.pi/Om)*F2           # coefficient of delta(w - w_nu)
G_src = (1/w)*(y**2/Om)*F2*sp.pi             # -Im[...] -> pi delta
check("C1b", sp.simplify(G_urf - G_src) == 0, "(y^2/2w)S_OO = -(1/w)Im Pi_phiphi (2308.06314 Eqs. (2),(16))")

# ---------------------------------------------------------------------------------------------
# C2  coupling-to-mass rule for the k->0 optical vertex of a diatomic crystal
c1, c2, M1, M2 = sp.symbols('c1 c2 M1 M2', positive=True)
Mt = M1 + M2
e1, e2 = sp.sqrt(M2/Mt), -sp.sqrt(M1/Mt)            # optical eigenvector at Q=0 (orthogonal to sqrt(M) acoustic)
vert = c1*e1/sp.sqrt(M1) + c2*e2/sp.sqrt(M2)
check("C2a", sp.simplify(sp.sqrt(M1)*e1 + sp.sqrt(M2)*e2) == 0, "optical mode orthogonal to the mass-weighted translation")
check("C2b", sp.simplify(vert - (c1/M1 - c2/M2)*sp.sqrt(M1*M2/Mt)) == 0, "vertex = (c1/M1 - c2/M2) sqrt(M1 M2/M_cell)")
lam = sp.symbols('lambda', positive=True)
check("C2c", sp.simplify(vert.subs({c1: lam*M1, c2: lam*M2})) == 0, "c_k proportional to M_k -> zero single-phonon absorption")

# C3  GaAs electron-scalar coupling at the observable LO residue (vertex Z_k - Z*_k/eps_inf, C21); source structure Z - Q/eps_inf (Q = +-3)
MGa, MAs = sp.Rational(6972, 100), sp.Rational(7492, 100)
einf, Zs = sp.Rational(109, 10), sp.Rational(21, 10)
def dLO(zst, eps):
    return (31 - zst/eps)/MGa - (33 + zst/eps)/MAs
d_urf = dLO(Zs, einf); d_src = dLO(3, einf)
d_prop_rig = sp.Rational(28)/MGa - sp.Rational(36)/MAs
ratio = sp.N((d_urf/d_src)**2)
sens = sp.N(abs(dLO(Zs*sp.Rational(11, 10), einf) - d_urf)/abs(d_urf))
check("C3", abs(float(d_urf) + 0.00117) < 2e-5 and abs(float(d_src) + 0.00346) < 2e-5 and 0.10 < float(ratio) < 0.12 and 0.4 < float(sens) < 0.5,
      f"d_LO URF {float(d_urf):.5f}, source-structure {float(d_src):.5f}, rate ratio {float(ratio):.3f}; +10% in Z*/eps_inf moves d by {float(sens):.0%}")

# C4  isotope-disorder broadband channel for B-L in natural Si
iso = [(28, sp.Rational(279769, 10000), sp.Rational(92223, 100000)), (29, sp.Rational(289765, 10000), sp.Rational(4685, 100000)),
       (30, sp.Rational(299738, 10000), sp.Rational(3092, 100000))]
Z = 14
xs_ = [x for _, _, x in iso]; Ms_ = [M for _, M, _ in iso]; gs_ = [sp.Rational(A - Z)/M for A, M, _ in iso]
gbar = sum(x*(A - Z) for A, M, x in iso)/sum(x*M for A, M, x in iso)          # v_bar = sum v / sum M (mass-weighted)
Mbar = sum(x*M for x, M in zip(xs_, Ms_))/sum(xs_)
wvar = sum(x*M*(g_ - gbar)**2 for x, M, g_ in zip(xs_, Ms_, gs_))/sum(xs_)
rel = wvar/(Mbar*gbar**2)
check("C4a", abs(float(rel) - 1.88e-4) < 0.02e-4, f"sum x M (gamma-gamma_bar)^2/(M_bar gamma_bar^2) = {float(rel):.3e} (B-L, nat. Si, mass-weighted)")
# random-mass chain: every non-zero mode is orthogonal to sqrt(M_I) (so the mean coupling gamma_bar M_I drops out exactly)
rng = np.random.default_rng(1)
Nn = 40
Ms = rng.choice([28.0, 29.0, 30.0], size=Nn, p=[0.9223, 0.0468, 0.0309])
K = np.zeros((Nn, Nn))
for i in range(Nn):
    j = (i + 1) % Nn
    K[i, i] += 1; K[j, j] += 1; K[i, j] -= 1; K[j, i] -= 1
D = K/np.sqrt(np.outer(Ms, Ms))
wv, ev = np.linalg.eigh(D)
proj = np.abs(np.sqrt(Ms) @ ev[:, 1:]).max()
check("C4b", proj < 1e-10, f"max_lambda |sum_I sqrt(M_I) e_I,lambda| = {proj:.1e} (periodic random-mass chain)")

# ---------------------------------------------------------------------------------------------
# C5  S5: URF (3.5) with the incoherent spin channel reproduces 2411.10542 Eq. (31)
gp, ma, rho, xi_D, mcell, rhoT = sp.symbols('g_p m_a rho_a XiD m_cell rho_T', positive=True)
# y^2 = (2 g_p m_a)^2 ; S = (2pi/Omega) * sum_k x lam^2 J(J+1) w D/(2M) = (2pi/Omega) * (w/2) * XiD  (XiD = sum_j xi_j D_j)
S5 = (2*sp.pi/Om)*(ma/2)*xi_D
Gam = (2*gp*ma)**2/(2*ma)*S5
R_urf = rho*Gam/(rhoT*ma)
R_src = 2*sp.pi*rho*ma/mcell*gp**2*xi_D
check("C5", sp.simplify(R_urf.subs(rhoT, mcell/Om) - R_src) == 0, "rho Gamma_abs/(rho_T m_a) = 2411.10542 Eq. (31)")

# ---------------------------------------------------------------------------------------------
# C6  S2: one-sublattice FM, axion wind; URF = 2005.10256 Eq. (27) (gamma->0) = 2001.10666 golden-rule limit of Eq. (35)
gae, me, Sj, lS, vperp, f = sp.symbols('g_aee m_e S_j lambda_S v_perp f', positive=True)
k_perp = ma*vperp
S_ks = (2*sp.pi/Om)*lS**2*Sj/2*k_perp**2               # coefficient of delta(w - w_K) in S_{k.s,k.s}
Gam6 = gae**2/(2*ma*me**2)*S_ks
R6 = rho*Gam6/((mcell/Om)*ma)
fj2 = gae**2*lS**2*rho/(2*me**2)*vperp**2               # |f_j . r_j|^2 of 2005.10256 Table 1 (r=(1,i,0))
R6_src = (sp.pi/mcell)*Sj*fj2                           # 2w * w_nu g/((w^2-w_nu^2)^2+w^2 g^2) -> pi delta
check("C6a", sp.simplify(R6 - R6_src) == 0, "URF magnon absorption = 2005.10256 Eq. (27), g_j=2, one sublattice")
Ncell = sp.symbols('N', positive=True)
V2 = Sj*Ncell*rho*vperp**2/f**2                          # |V|^2 of 2001.10666 Eq. (27) with m_a^2 a0^2 = 2 rho
Gam_tot_src = sp.pi/2*V2                                 # 2 pi |V/2|^2 delta (sin -> amplitude V/2i)
Gam_tot_urf = (R6*Ncell*mcell).subs({gae/me: 1/f, lS: 1}).subs(gae, me/f)
check("C6b", sp.simplify(Gam_tot_urf - Gam_tot_src) == 0, "total rate = 2001.10666 Eqs. (25)-(27),(35) in the golden-rule limit")

# C7  Larmor theorem: isotropic exchange + uniform Zeeman -> S^-_tot creates weight only at w_L, total 2<S^z_tot>
def spin_ops(s):
    m = [s - i for i in range(int(2*s) + 1)]
    n = len(m)
    Sz = sp.diag(*m)
    Sp = sp.zeros(n)
    for i in range(1, n):
        mm = m[i]
        Sp[i - 1, i] = sp.sqrt(s*(s + 1) - mm*(mm + 1))
    return Sz, Sp, Sp.T
def kron(*ms):
    out = ms[0]
    for mm in ms[1:]:
        out = sp.kronecker_product(out, mm)
    return out
sA, sB = sp.Integer(1), sp.Rational(1, 2)
SzA, SpA, SmA = spin_ops(sA); SzB, SpB, SmB = spin_ops(sB)
IA, IB = sp.eye(3), sp.eye(2)
J, wL = sp.Integer(3), sp.Rational(1, 7)
SA_dot_SB = kron(SzA, SzB) + (kron(SpA, SmB) + kron(SmA, SpB))/2
Sz_tot = kron(SzA, IB) + kron(IA, SzB)
Sm_tot = kron(SmA, IB) + kron(IA, SmB)
H = J*SA_dot_SB - wL*Sz_tot          # ferrimagnet (AF coupling, S_A=1, S_B=1/2); field favours +S^z
Hn = np.array(H.evalf(), dtype=float)
E, U = np.linalg.eigh(Hn)
g0 = U[:, 0]
Smn = np.array(Sm_tot.evalf(), dtype=float)
amps = (U.T @ Smn @ g0)**2
weights = {round(E[i] - E[0], 10): 0.0 for i in range(len(E))}
for i in range(len(E)):
    weights[round(E[i] - E[0], 10)] += amps[i]
nonzero = {k: v for k, v in weights.items() if v > 1e-12}
Szg = float(g0 @ np.array(Sz_tot.evalf(), dtype=float) @ g0)
check("C7", len(nonzero) == 1 and abs(list(nonzero)[0] - float(wL)) < 1e-10 and abs(sum(nonzero.values()) - 2*Szg) < 1e-10,
      f"S^-_tot weight only at w_Lar={float(wL):.4f}; total {sum(nonzero.values()):.4f} = 2<S^z>={2*Szg:.4f} (ferrimagnet 1, 1/2)")

# C8  Polder/Kittel ellipticity: H = (wx X^2 + wy P^2)/2 ; |<1|X|0>|^2 = sqrt(wy/wx)/2, mode frequency sqrt(wx wy)
wx, wy = sp.symbols('omega_x omega_y', positive=True)
# canonical rescaling X = (wy/wx)^(1/4) x, P = (wx/wy)^(1/4) p turns H into sqrt(wx wy)(x^2+p^2)/2
X01sq = (wy/wx)**sp.Rational(1, 2)*sp.Rational(1, 2)
P01sq = (wx/wy)**sp.Rational(1, 2)*sp.Rational(1, 2)
wK = sp.sqrt(wx*wy)
check("C8a", sp.simplify(wx*X01sq*2 - wK) == 0 and sp.simplify(wy*P01sq*2 - wK) == 0, "Kittel w_K = sqrt(w_x w_y); x-drive weight sqrt(w_y/w_x)")
check("C8b", sp.simplify((X01sq + P01sq) - (wx + wy)/(2*wK)) == 0, "transverse-isotropic average = A/w_K = (w_x+w_y)/(2 w_K) >= 1")

# ---------------------------------------------------------------------------------------------
# C9  S6: chi'' (2504.02927 Eq. (8), s_e = sigma) = 2(1 - e^{-beta w}) S_{s s} (campaign); Eq. (17) = URF; Eq. (26) inversion
beta, Sss = sp.symbols('beta S_ss', positive=True)
R_camp, Rconj = sp.symbols('R Rc')   # campaign retarded R_{ss}, and R_{ss}^*
# chi_sigma = -4 R (Kubo sign, sigma = 2 s); chi'' = -i(chi - chi^dag)/2 ; FDT: (1-e^{-bw}) S = i(R - R^*)
chi = -4*R_camp; chic = -4*Rconj
chi2 = -sp.I*(chi - chic)/2
check("C9a", sp.simplify(chi2 - 2*sp.I*(R_camp - Rconj)) == 0, "chi'' = 2 i (R - R*) = 2 (1 - e^{-beta w}) S_ss")
vv = sp.symbols('v', positive=True)
G_src = gae**2*ma*vv**2*(2*Sss)          # Eq. (17) with chi'' = 2 S (T = 0), g_ae dimensionful; v^i v^j -> v^2 (diag)
G_urf = (1/(2*ma))*(2*gae)**2*(ma*vv)**2*Sss   # H = -g grad a . sigma = -2 g grad a . s
check("C9b", sp.simplify(G_src - G_urf) == 0, "2504.02927 Eq. (17) = (y^2/2w) k k S_ss")
gn, e_, Nf, Omc = sp.symbols('gamma_n e N_f Omega_c', positive=True)
Sn_from_S = gn**2*e_**4*Omc/(4*me**2*(2*sp.pi)**3*Nf)*Sss
Sn_eq26 = (1/Nf)*gn**2*e_**4/(8*me**2)*Omc/(2*sp.pi)**3*(2*Sss)
check("C9c", sp.simplify(Sn_from_S - Sn_eq26) == 0, "S_n = gamma_n^2 e^4 Omega_c P_T S/(4 m_e^2 (2pi)^3 N_f)")

# ---------------------------------------------------------------------------------------------
# C10 chiral phonons: Zhang-Niu L_z is conserved by the harmonic H only if D commutes with the on-site rotation generator
# H = p.p/2 + u.D.u/2 (mass-weighted), L_z = u^T J p ; [H, L_z] = i( p^T J p - u^T D J u )-type term -> zero iff [D, J] = 0
def comm_vanishes(Dm, Jm):
    return (Dm*Jm - Jm*Dm) == sp.zeros(*Dm.shape)
Jz1 = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
Jz = sp.diag(Jz1, Jz1)                         # two atoms, rotation of displacement vectors only
a_, b_, c_, d_ = sp.symbols('a b c d', positive=True)
D_iso = sp.Matrix(6, 6, lambda i, j: (a_ if i == j else 0) + (-b_ if abs(i - j) == 3 else 0))
D_aniso = D_iso.copy(); D_aniso[0, 0] += c_; D_aniso[3, 3] += c_; D_aniso[0, 4] = D_aniso[4, 0] = d_
check("C10", comm_vanishes(D_iso, Jz) and not comm_vanishes(D_aniso, Jz),
      "[D,J]=0 (isotropic springs) conserves phonon L_z; generic crystal D does not (no conservation law for decay)")

# ---------------------------------------------------------------------------------------------
# C11 X10: exact acceleration identity [H,[H,X]] = (dV/dX)/M on a test function; URF -> 2312.10566 Eq. (17)
Xs, xs, Mn, mel = sp.symbols('X x M m', positive=True)
Vf = sp.Function('V')(Xs, xs)
psi = sp.Function('psi')(Xs, xs)
def Hop(fn):
    return -sp.diff(fn, Xs, 2)/(2*Mn) - sp.diff(fn, xs, 2)/(2*mel) + Vf*fn
def comm_HX(fn):
    return Hop(Xs*fn) - Xs*Hop(fn)
lhs = Hop(comm_HX(psi)) - comm_HX(Hop(psi))
check("C11a", sp.simplify(sp.expand(lhs - sp.diff(Vf, Xs)*psi/Mn)) == 0, "[H,[H,X]] psi = (dV/dX/M) psi exactly (any V)")
# rate: Gamma = y^2 gamma^2 m_e^2 k^2 Im(-1/eps)/(e^2 w); dilute: Im(-1/eps) ~ n_at sigma_gamma / w ; per atom, gamma = g/m_p
gphi, mp, kk, sig, nat, al = sp.symbols('g_phi m_p k sigma_gamma n_at alpha', positive=True)
Gam11 = gphi**2*(1/mp)**2*me**2*kk**2*(nat*sig/w)/(4*sp.pi*al*w)
src17 = gphi**2*(me/mp)**2*(kk/w)*sig/(4*sp.pi*al)*(kk/w)   # sigma_phi * v, v = k/w
check("C11b", sp.simplify(Gam11/nat - src17) == 0, "URF (B2.8.2) per atom = 2312.10566 Eq. (17) x v")

# ---------------------------------------------------------------------------------------------
# C12 sec. 10(iii): optical potential U0 = 2 pi b n0/m_chi vs E_kin = m v^2/2 at the 2512.16451 benchmark
hbarc = sp.Rational(197327, 10**10)        # eV cm
m_chi, v_, n0 = sp.Integer(20), sp.Rational(1, 1000), sp.Rational(269, 100)*10**24   # eV, c, cm^-3
sig_b = sp.Rational(4, 1)*sp.Rational(1, 10**38)                                       # cm^2
b = sp.sqrt(sig_b/(4*sp.pi))
U0 = 2*sp.pi*b*n0*hbarc**2/m_chi
Ek = m_chi*v_**2/2
ratio12 = sp.N(U0/Ek)
kcm = m_chi*v_/hbarc
sig_crit = sp.N(4*sp.pi*(kcm**2/(4*sp.pi*n0))**2)
check("C12", abs(float(ratio12) - 1.85) < 0.05 and abs(float(sig_crit) - 1.17e-38) < 0.05e-38,
      f"U0/E_kin = {float(ratio12):.2f} at 4e-38 cm^2, 20 eV; Born needs sigma << {float(sig_crit):.2e} cm^2")

# ---------------------------------------------------------------------------------------------
# C13 squared-coupling misprints: 2601.01043 Eq. (12) vs (13); 2308.06314 Eq. (48) vs (49)
kap, gag, B0 = sp.symbols('kappa g_agg B_0', positive=True)
g_sol = sp.solve(sp.Eq((gag*B0/ma)**2, kap**2), gag)
check("C13a", g_sol == [kap*ma/B0], "squared form of 2601.01043 Eq. (12) gives its Eq. (13) g ~ eps m/B0 (linear form would not)")
num49 = sp.N(2*sp.sqrt(4*sp.pi/137.036)*1e-16*511e3/0.1)   # g_aee from (1/4)(g/e)^2 (w/m_e)^2 = kappa^2, w = 100 meV
check("C13b", 1e-10 < float(num49) < 1e-9, f"squared 2308.06314 Eq. (48) -> g_aee = {float(num49):.1e} ~ Eq. (49) 1e-9 (linear: ~1e-25)")
nr, e1r, e2r = sp.symbols('n_r eps1 eps2', positive=True)
R_urf13 = kap**2*w*e2r/(e1r**2 + e2r**2)       # kappa^2 w Im(-1/eps)
R_src13 = kap**2*w*e2r/nr                      # kappa^2 alpha, alpha = w eps2 / n_r
check("C13c", sp.simplify(R_urf13/R_src13 - nr/(e1r**2 + e2r**2)) == 0, "R_URF/R_(alpha, eps=1) = n_r/|eps|^2")

# ---------------------------------------------------------------------------------------------
# C14 random-coupling broadband theorem: <|sum_I c_I . e_I|^2>_c = sum_I sigma_I^2 |e_I|^2/3 for isotropic, independent c_I
cs = sp.symbols('s1:3', positive=True)
ex = sp.symbols('e1:7')
# <c_I^a c_J^b> = delta_IJ delta_ab s_I^2/3
avg = sum(cs[I]**2/3*sum(ex[3*I + a]**2 for a in range(3)) for I in range(2))
# explicit average via second moments
expr = 0
for I in range(2):
    for J in range(2):
        for a in range(3):
            for bb in range(3):
                mom = (cs[I]**2/3 if (I == J and a == bb) else 0)
                expr += mom*ex[3*I + a]*ex[3*J + bb]
check("C14", sp.simplify(expr - avg) == 0, "configurational average -> self (incoherent) term with sigma_I^2 D_I")

# C15 X10 correction n_r/|eps|^2 = 1 + (3/2) w_p^2/w^2 + ... ; Si at 1 keV with 12 e/atom bound below w (w_p ~ 28.8 eV)
dd = sp.symbols('delta', positive=True)
ser = sp.series(sp.sqrt(1 - dd)/(1 - dd)**2, dd, 0, 2).removeO()
wp12 = sp.Rational(166, 10)*sp.sqrt(3)
corr = sp.N(sp.Rational(3, 2)*(wp12/1000)**2)
check("C15", sp.simplify(ser - (1 + sp.Rational(3, 2)*dd)) == 0 and 1.1e-3 < float(corr) < 1.35e-3,
      f"n_r/|eps|^2 = 1 + (3/2)w_p^2/w^2; +{float(corr):.2e} at 1 keV in Si (12 e/atom)")

# C16 SMM: H = -D S_z^2 - w_Z S_z ; line S -> S-1 at D(2S-1) + w_Z with |<S-1|S^-|S>|^2 = 2S
Dz, wZ = sp.symbols('D omega_Z', positive=True)
Sbig = sp.Integer(10)
E_m = lambda m: -Dz*m**2 - wZ*m
check("C16", sp.simplify(E_m(Sbig - 1) - E_m(Sbig) - (Dz*(2*Sbig - 1) + wZ)) == 0 and
      sp.simplify(E_m(-Sbig + 1) - E_m(-Sbig) - (Dz*(2*Sbig - 1) - wZ)) == 0 and
      sp.simplify(Sbig*(Sbig + 1) - (-Sbig)*(-Sbig + 1) - 2*Sbig) == 0,
      "SMM: S^- line D(2S-1)+w_Z from m=S; S^+ line D(2S-1)-w_Z from metastable m=-S; both weight 2S")

# C17 1705.03016 Eq. (6): zero-point momentum spread of H in LiH vs alpha m_e
MH, wH = sp.Float(938.8e6), sp.Float(0.1)      # eV
dp = sp.sqrt(MH*wH/2)
qmin = sp.sqrt(2*MH*9)
check("C17", 6.5e3 < float(dp) < 7.2e3 and float(dp/qmin) < 0.06,
      f"Delta p = sqrt(M w/2) = {float(dp)/1e3:.1f} keV (vs alpha m_e = 3.7 keV); Delta p/q_min = {float(dp/qmin):.3f}")

# C18 D5 factorisation: R_1 = R_CM + (m2/M) r  and  m2/M = mu12/m1
m1_, m2_ = sp.symbols('m1 m2', positive=True)
check("C18", sp.simplify(m2_/(m1_ + m2_) - (m1_*m2_/(m1_ + m2_))/m1_) == 0, "e^{iq.R1} = e^{iq.R_CM} e^{i(mu12/m1) q.r}")

# C19 S5 spin-average identity behind 2411.10542 Eq. (27): sum_a <J^a J^a> = J(J+1), <J^a J^b> = delta J(J+1)/3
Jq = sp.Rational(3, 2)
SzJ, SpJ, SmJ = spin_ops(Jq)
Jx = (SpJ + SmJ)/2; Jy = (SpJ - SmJ)/(2*sp.I)
tr = lambda M_: sp.simplify(M_.trace()/(2*Jq + 1))
check("C19", tr(Jx*Jx) == Jq*(Jq + 1)/3 and tr(Jx*Jy) == 0 and tr(SzJ*SzJ) == Jq*(Jq + 1)/3,
      "unpolarised nuclear spin: <J^a J^b> = delta_ab J(J+1)/3")

# C20 (B2.7.1): two-phonon creation amplitude of u x P at one site, u = sum e(b + b^dag)/sqrt(2 M w), P = M du/dt
B1, B2, Mq, w1, w2 = sp.symbols('B1 B2 M_q w1 w2', positive=True)
ev1 = sp.Matrix(sp.symbols('a1:4')); ev2 = sp.Matrix(sp.symbols('c1:4'))
u_cr = ev1*B1/sp.sqrt(2*Mq*w1) + ev2*B2/sp.sqrt(2*Mq*w2)
P_cr = sp.I*sp.sqrt(Mq*w1/2)*ev1*B1 + sp.I*sp.sqrt(Mq*w2/2)*ev2*B2
uxP = u_cr.cross(P_cr)
coef = sp.Matrix([sp.expand(uxP[i]).coeff(B1).coeff(B2) for i in range(3)])
target = sp.I/2*(sp.sqrt(w2/w1) - sp.sqrt(w1/w2))*ev1.cross(ev2)
check("C20", sp.simplify(coef - target) == sp.zeros(3, 1), "<12|u x P|0> = (i/2)[sqrt(w2/w1) - sqrt(w1/w2)] e1 x e2 (zero one-phonon term)")

# C21 LO residue of the full R (WP0 (3.6)/(5.3)) in a one-mode model: vertex a + b(1 - 1/eps_inf)
a_, b_, v_, chi_, w2, wT2 = sp.symbols('a b v chi w2 wT2', real=True)
Pp = 1/(w2 - wT2)
Rt_OO = a_**2*Pp + chi_; Rt_Oc = a_*b_*Pp - chi_; Rt_cc = b_**2*Pp + chi_
eps_w = 1 - v_*Rt_cc
epsinf = 1 - v_*chi_
wLO2 = sp.solve(sp.Eq(eps_w, 0), w2)[0]
res = sp.simplify((v_*Rt_Oc**2/sp.diff(eps_w, w2)).subs(w2, wLO2))
check("C21", sp.simplify(res - (a_ + b_*(1 - 1/epsinf))**2) == 0, "Res_LO R_OO = [a + b(1 - 1/eps_inf)]^2 -> electron row Z - Z*/eps_inf")
# C22 Debye random medium: FT of exp(-r/xi) = 8 pi xi^3/(1+q^2 xi^2)^2  (2512.16451 Eq. (12))
r_, q_, xi_ = sp.symbols('r q xi', positive=True)
ft = sp.integrate(4*sp.pi*r_**2*sp.sin(q_*r_)/(q_*r_)*sp.exp(-r_/xi_), (r_, 0, sp.oo))
R_, n0_, dn2 = sp.symbols('R n0 dn2', positive=True)
F2 = dn2*ft*(4*sp.pi*R_**3/3)/(n0_*4*sp.pi*R_**3/3)**2
check("C22", sp.simplify(ft - 8*sp.pi*xi_**3/(1 + q_**2*xi_**2)**2) == 0 and
      sp.simplify(F2 - dn2/n0_**2*6*xi_**3/(R_**3*(1 + q_**2*xi_**2)**2)) == 0, "2512.16451 Eq. (12) re-derived (bulk limit)")
# C23 general: [H, L] = (i/2) u^T [J, D] u for H = p.p/2 + u.D.u/2, L = u^T J p (J antisymmetric)
n3 = 3
us = sp.Matrix(sp.symbols('u0:3')); ps = sp.Matrix(sp.symbols('p0:3'))
Dm = sp.Matrix(n3, n3, lambda i, j: sp.Symbol(f'D{min(i,j)}{max(i,j)}'))
Jm = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
# canonical commutator via Poisson bracket x i (exact for quadratic forms): [A,B] = i {A,B}
H_ = (ps.T*ps)[0]/2 + (us.T*Dm*us)[0]/2
L_ = (us.T*Jm*ps)[0]
pb = sum(sp.diff(H_, us[k])*sp.diff(L_, ps[k]) - sp.diff(H_, ps[k])*sp.diff(L_, us[k]) for k in range(n3))
check("C23", sp.expand(sp.I*pb - sp.I/2*(us.T*(Jm*Dm - Dm*Jm)*us)[0]) == 0, "[H,L] = (i/2) u^T [J,D] u (zero iff [J,D]=0)")
# C24 GaAs-free check of the Ni2+ neutron bracket (quenched 3d: lambda_S = 1): [1/(g/2)]^2 at g = 2.2
check("C24", abs(float((1/(sp.Rational(22, 10)/2))**2) - 0.826) < 0.002, "Ni2+-like bracket [lambda_S/(g/2)]^2 = 0.83")
# C25 DW at q = 0.1 eV: 2W ~ q^2 <u^2>, <u^2> ~ 5e-3 A^2
qA = 0.1/1973.27     # A^-1
check("C25", 1e-12 < qA**2*5e-3 < 1e-10, f"2W(q=0.1 eV) ~ {qA**2*5e-3:.1e} (negligible)")
# C26 V_opt/E_kin at v = 1.2e-3 (scales as v^-2)
check("C26", abs(float(ratio12)*(1/1.2)**2 - 1.29) < 0.03, f"V_opt/E_kin(v=1.2e-3) = {float(ratio12)/1.44:.2f}")
# C27 isotope (B-L) vs EM-like (two-phonon ELF) broadband absorption in Si, order of magnitude
u_eV = 931.494e6
sig_w = float(wvar)/u_eV                                  # sum x M (gamma - gamma_bar)^2 in eV^-1 (gamma in 1/u -> 1/eV ... )
sig_w = float(wvar)*(1/u_eV)                              # wvar has units u*(1/u)^2 = 1/u
e2 = 4*np.pi/137.036
Om_at = 20.02*(1/1973.27)**3                              # Si atomic volume 20.02 A^3 in eV^-3
Dw, wq, ImL = 20.0, 0.05, 5.0e-6                          # D(50 meV) eV^-1; Im(-1/eps) at 50 meV, 293 K (Deinzer & Strauch 2004, alpha ~0.55/cm)
ratio27 = np.pi*e2*sig_w*Dw/(2*Om_at*wq*ImL)
check("C27", 4e3 < ratio27 < 9e3, f"Gamma_iso/Gamma_EM ~ {ratio27:.0f} at 50 meV, 293 K (D=20/eV, Im(-1/eps)=5e-6) [E]")
# C28 LO-vertex near cancellation: Z/M for Ga and As
check("C28", abs(31/69.72 - 33/74.92) < 0.005, f"Z/M: Ga {31/69.72:.4f}, As {33/74.92:.4f} (near-cancellation)")

n_pass = sum(ok for _, ok in RESULTS)
print(f"\n{n_pass}/{len(RESULTS)} PASS")
if n_pass != len(RESULTS):
    raise SystemExit(1)
