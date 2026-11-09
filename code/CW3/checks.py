#!/usr/bin/env python3
"""R16 / CW3 closure checks (numpy + sympy + scipy; < 1 min). Cited in returns/R16/CW3.md as CW3-Cn
and in returns/R16/CW3-errata.md (ERR-CW3) as CW3-Cn (new or changed checks are marked [ERR]).
ERR-CW3 changes: tolerances tightened to ~3-10x the observed error; vacuous C6c and C11 replaced by real checks;
new or rewritten checks C1d, C2d-g, C3d-e, C5c, C6c, C9e, C10b, C11a-b, C12a-d, C13a-c, C14 for the VER-CW3 corrections.
Run: python3 -I code/CW3/checks.py   (exit status 0 iff all PASS)."""
import numpy as np, sympy as sp, sys
from scipy.integrate import quad

RES = []
def check(name, ok, info=""):
    RES.append((name, bool(ok))); print(f"{'PASS' if ok else 'FAIL'}  {name}  {info}")

rng = np.random.default_rng(7)

# ---------------------------------------------------------------------------------------------
# C1 (LE-77): O(1) prefactor of the Fano term. Wide-band Fano model, one X0 level (energy 0), phonon
# branches nu with widths G_nu, one non-phonon branch x (width Gx, no off-shell amplitude).
# Exact branch weight W_b = int dw G_b |t_b + (rho + Ups)/(w + i G/2)|^2 - G_b |t_b|^2 * window,
# Ups = -i sum_b G_b t_b / 2, t_b = off-shell amplitude per unit coupling (O4 lambda_f / a^off).
# Claim: W_b / sum W = (G_b/G)(1 + cbar - c_b),  c_b = G Im(rho* t_b)/|rho|^2 (dimensionless, Gamma^tot),
# cbar = sum_b G_b c_b / G, to O(G^2 |t|^2).  WP5-v4 form (extra 2*pi) fails.
def fano_branch_weights(G_b, t_b, rho, L=2000.0):
    G = G_b.sum(); Ups = -0.5j * np.sum(G_b * t_b); rp = rho + Ups
    A = np.arctan(2 * L / G)           # exact window integrals: int 1/(w^2+G^2/4) = 4A/G, int 1/(w+iG/2) = -2iA
    return G_b * (np.abs(rp)**2 * 4 * A / G + 2 * np.real(np.conj(t_b) * rp * (-2j * A)))
G_b = np.array([0.010, 0.006, 0.004]); t_b = np.array([0.6*np.exp(0.9j), -0.4, 0.3j, 0.0])[:3]
G_b = np.append(G_b, 0.005); t_b = np.append(t_b, 0.0)       # last branch = non-phonon x, a^off_x = 0
rho = 1.0
W = fano_branch_weights(G_b, t_b, rho); K_exact = W / W.sum()
G = G_b.sum(); c = G * np.imag(np.conj(rho) * t_b) / abs(rho)**2; cbar = np.sum(G_b * c) / G
K_ours = (G_b / G) * (1 + cbar - c)
K_wp5 = (G_b / G) * (1 + 2*np.pi*(cbar - c))
err_ours = np.max(np.abs(K_exact - K_ours)); err_wp5 = np.max(np.abs(K_exact - K_wp5))
check("C1a Fano kernel K_b = (G_b/G)(1+cbar-c_b), prefactor 1 (not 2pi)", err_ours < 3e-5 and err_wp5 > 300*err_ours,
      f"|dK| ours {err_ours:.1e}, WP5 2pi-form {err_wp5:.1e}")
check("C1b non-phonon branch shifted by G_x cbar (sum over phonon branches of F != 0 when G_x > 0)",
      abs(K_exact[-1] - G_b[-1]/G) > 1e-4 and abs(K_exact[-1] - K_ours[-1]) < 3e-5,
      f"K_x - G_x/G = {K_exact[-1]-G_b[-1]/G:.2e}")
# scaling: residual is O(G^2): halve all widths -> error / 4
W2 = fano_branch_weights(G_b/2, t_b, rho); K2 = W2/W2.sum(); c2 = (G/2)*np.imag(np.conj(rho)*t_b)/abs(rho)**2
K2o = (G_b/G)*(1 + np.sum(G_b/2*c2)/(G/2) - c2)
check("C1c residual scales as G^2", 3.8 < err_ours/np.max(np.abs(K2-K2o)) < 4.2,
      f"ratio {err_ours/np.max(np.abs(K2-K2o)):.2f}")
# [ERR] C1d (VER-CW3 V1): the self-energy of the off-shell amplitude on a flat continuum is
# Ups = sum_f g_f^2 a_f/(w - E_f + i0) -> -(i/2) sum_b G_b a_b (complex a: "Im Ups = -1/2 sum G a" is wrong).
hE = 2e-3; Ef = np.arange(-40.0, 40.0 + hE/2, hE); eta = 0.05
Ups_num = sum(Gb_*hE/(2*np.pi)*tb_*np.sum(1.0/(0.0 - Ef + 1j*eta)) for Gb_, tb_ in zip(G_b, t_b))
Ups_ref = -0.5j*np.sum(G_b*t_b)
check("C1d [ERR] Ups = -(i/2) sum G_b a_b on a flat continuum (not Im Ups = -1/2 sum G a)",
      abs(Ups_num - Ups_ref) < 3e-3*abs(Ups_ref) and abs(1j*Ups_ref.imag - (-0.5j*np.sum(G_b*t_b))) > 1e-4,   # 'Im Ups' form drops the Re(a) part of a complex a
      f"|num-ref|/|ref| = {abs(Ups_num-Ups_ref)/abs(Ups_ref):.1e}")

# ---------------------------------------------------------------------------------------------
# C2 (LE-75): F = 0 for PT-symmetric targets WITH SOC. Single-particle Theta = i s_y K (Theta^2 = -1);
# pair (electron x hole) space: U = (i s_y) (x) (i s_y), Theta_pair^2 = +1. Degenerate X0 manifold D (dim 4),
# per branch 4 final states. Theta-even data: rho = U rho*, g_nu = U g_nu* U^dag, t_nu = U t_nu*.
# Fano observable = part of the branch weight odd in t (wide band, matrix widths, exact window integrals).
sy = np.array([[0, -1j], [1j, 0]]); U = np.kron(1j*sy, 1j*sy)
def theta_even_vec(v): return 0.5*(v + U @ v.conj())
def theta_even_mat(M): return 0.5*(M + U @ M.conj() @ U.conj().T)
def branch_odd(rho, gs, ts, Et=None, w0=0.0, L=4000.0, n=400001):
    # [ERR] Et = O(g^2) level-shift matrix on D (VER-CW3 V2); G = (w - Et + i Gam/2)^{-1} via the (non-normal) eigen-
    # decomposition of H_eff = Et - i Gam/2. Window centred at w0. Et = None reproduces the CW3 C2 code (Et = 0).
    w = np.linspace(w0-L, w0+L, n); dw = w[1]-w[0]
    Gam = sum(2*np.pi * g.conj().T @ g for g in gs)            # matrix width on D (density of final states = 1)
    Ups = -1j*np.pi*sum(g.conj().T @ t for g, t in zip(gs, ts))
    Et = np.zeros_like(Gam) if Et is None else Et
    lam, R = np.linalg.eig(Et - 0.5j*Gam); Ri = np.linalg.inv(R)
    out = []
    for g, t in zip(gs, ts):
        def W(sign):
            x = Ri @ (rho + sign*Ups)
            # A(w) = sign t + g R diag(1/(w - lam)) R^-1 (rho + Ups) ; integrate |A|^2 - |t|^2 on the grid
            Gv = 1.0/(w[:, None] - lam[None, :])
            A = sign*t[None, :] + (Gv * x[None, :]) @ (g @ R).T
            return np.sum(np.abs(A)**2 - np.abs(t)**2) * dw
        out.append(0.5*(W(+1) - W(-1)))
    return np.array(out)
def rnd(*s): return rng.normal(size=s) + 1j*rng.normal(size=s)
rho = theta_even_vec(rnd(4)); gs = [0.05*theta_even_mat(rnd(4, 4)) for _ in range(2)]
ts = [0.5*theta_even_vec(rnd(4)) for _ in range(2)]
odd_pt = branch_odd(rho, gs, ts)
elem_im = max(abs(np.imag(np.conj(rho) * (g.conj().T @ t))).max() for g, t in zip(gs, ts))
rho_g = rnd(4); gs_g = [0.05*rnd(4, 4) for _ in range(2)]; ts_g = [0.5*rnd(4) for _ in range(2)]
odd_gen = branch_odd(rho_g, gs_g, ts_g)
check("C2a PT + SOC (pair Theta^2=+1), Et = 0: Fano (t-odd) branch weight vanishes", np.max(np.abs(odd_pt)) < 1e-10*np.max(np.abs(odd_gen)),
      f"PT {np.max(np.abs(odd_pt)):.1e} vs generic {np.max(np.abs(odd_gen)):.1e}")
check("C2b element-wise Im(rho* a) != 0 in the Kramers product basis (only a Theta-real basis is real)", elem_im > 1e-3,
      f"max elementwise {elem_im:.2e}")
# Theta-real basis exists: eigenvectors of the antiunitary; build real basis and verify rho real there
cands = [theta_even_vec(e) for e in np.eye(4)] + [theta_even_vec(1j*e) for e in np.eye(4)]
B = []
for vv_ in cands:                                   # Gram-Schmidt: <x|y> is real for Theta-even x, y, so it preserves Theta-evenness
    for b_ in B: vv_ = vv_ - (b_.conj() @ vv_) * b_
    if np.linalg.norm(vv_) > 1e-8: B.append(vv_/np.linalg.norm(vv_))
B = np.column_stack(B[:4])
check("C2c Theta-real pair basis: rho, g, t all real", np.max(np.abs(np.imag(B.conj().T @ rho))) < 1e-12 and
      max(np.max(np.abs(np.imag(B.conj().T @ g @ B))) for g in gs) < 1e-12)
# [ERR] C2d-f (VER-CW3 V2, hypothesis (P5)): a real symmetric but NON-scalar level-shift matrix Et on D (Theta-real basis)
# gives a per-branch Fano weight != 0 (branch sum ~ 0); Et = s*1 (scalar, P5) keeps it 0; for splittings >> Gamma it decays ~ 1/s.
Dsh = np.diag([1.0, -1.0, 0.5, -0.3]); gen = np.max(np.abs(odd_gen))
odd_s = {s_: branch_odd(rho, gs, ts, Et=B @ (s_*Dsh) @ B.conj().T) for s_ in (0.2, 5.0, 20.0)}
odd_sc = branch_odd(rho, gs, ts, Et=0.3*np.eye(4), w0=0.3)
check("C2d [ERR] non-scalar real Et (s = 0.2 ~ Gamma): per-branch Fano weight != 0, branch sum ~ 0 (P5 needed)",
      np.min(np.abs(odd_s[0.2])) > 1e-2*gen and abs(odd_s[0.2].sum()) < 1e-3*np.max(np.abs(odd_s[0.2])),
      f"per branch {odd_s[0.2][0]:+.2e}, {odd_s[0.2][1]:+.2e}; sum {odd_s[0.2].sum():.1e}; generic {gen:.2e}")
check("C2e [ERR] scalar Et = s*1 (P5): Fano weight vanishes", np.max(np.abs(odd_sc)) < 1e-10*gen, f"{np.max(np.abs(odd_sc)):.1e}")
r5, r20 = np.max(np.abs(odd_s[5.0])), np.max(np.abs(odd_s[20.0]))
check("C2f [ERR] splitting >> Gamma: Fano weight -> 0 as Gamma/splitting (levels become non-degenerate seeds)",
      r20 < r5 < np.max(np.abs(odd_s[0.2])) and 2.5 < r5/r20 < 5.5, f"s = 5: {r5:.2e}, s = 20: {r20:.2e}, ratio {r5/r20:.2f}")
# [ERR] C2g (ERR-CW3 R2): commuting case closed form. int conj(g_i) g_j dw, g_j = 1/(w - e_j + i gam_j/2), equals
# 2 pi i/(e_i - e_j + i(gam_i+gam_j)/2) = (4 pi/(gam_i+gam_j))/(1 - i eta), eta = 2(e_i-e_j)/(gam_i+gam_j); Im part antisymmetric, ~ eta/(1+eta^2).
wS, eI, eJ = sp.symbols('w e_i e_j', real=True); gI, gJ = sp.symbols('gamma_i gamma_j', positive=True)
integ = sp.conjugate(1/(wS - eI + sp.I*gI/2))*(1/(wS - eJ + sp.I*gJ/2))
pole = eI + sp.I*gI/2
resid = sp.simplify(2*sp.pi*sp.I*sp.cancel(sp.expand_complex(integ)*(wS - pole)).subs(wS, pole))   # upper half plane; integrand ~ 1/w^2
etaS = 2*(eI - eJ)/(gI + gJ); Xij = (4*sp.pi/(gI + gJ))/(1 - sp.I*etaS)
vals = {eI: 0.3, eJ: -0.1, gI: 0.2, gJ: 0.5}
fnum = sp.lambdify(wS, sp.expand_complex(integ.subs(vals)))
num_chk = quad(lambda t: fnum(t).real, -np.inf, np.inf, limit=400)[0] + 1j*quad(lambda t: fnum(t).imag, -np.inf, np.inf, limit=400)[0]
ImX = sp.simplify(sp.im(sp.expand_complex(Xij)))
lim_inf = sp.limit(ImX*eI, eI, sp.oo)
check("C2g [ERR] closed form X_ij = (4pi/(g_i+g_j))/(1 - i eta_ij); Im X antisymmetric, 0 at eta = 0, ~ 1/eta at large eta",
      sp.simplify(resid - Xij) == 0 and abs(num_chk - complex(Xij.subs(vals))) < 1e-7
      and sp.simplify(ImX + ImX.subs({eI: eJ, eJ: eI, gI: gJ, gJ: gI}, simultaneous=True)) == 0 and sp.simplify(ImX.subs(eI, eJ)) == 0
      and lim_inf.is_finite and lim_inf != 0, f"Im X = {ImX}")

# ---------------------------------------------------------------------------------------------
# C3 (LE-90): 2501.05504 prefactor 32 and M_n.
z, x, y, L0, r, M, w, rho_, e_, eps0, kap, rV, mV, gam, th = sp.symbols(
    'z x y L0 r_n M_n omega_n rho e_pt epsilon0 kappa rho_V m_V gamma theta', positive=True)
n = sp.Integer(1)
U_n = sp.cos(n*sp.pi*z/L0)*sp.exp(-(x**2+y**2)/(2*r**2))/sp.sqrt(M*w)
norm = sp.integrate(sp.integrate(sp.integrate(U_n**2, (z, 0, L0)), (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo))
Mn = sp.solve(sp.Eq(norm, 1/(2*rho_*w)), M)[0]
check("C3a M_n = rho pi r_n^2 L0 from int U_n^2 = 1/(2 rho omega_n)", sp.simplify(Mn - rho_*sp.pi*r**2*L0) == 0, str(Mn))
I = sp.integrate(sp.integrate(sp.integrate(sp.diff(U_n, z), (z, 0, L0)), (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo))
A = kap*sp.sqrt(2*rV)*e_/eps0
H0sq = (A*sp.cos(th)/2)**2 * I**2
lor = (2*gam*w**2/sp.pi)/((mV**2-w**2)**2 + w**2*gam**2)   # delta(m-w) -> relativistic Lorentzian
Ps = 2*sp.pi*mV*H0sq*lor
Ps = sp.simplify(Ps.subs(r**2, M/(rho_*sp.pi*L0)))
src = 32*kap**2*rV/rho_**2*e_**2/eps0**2*M/L0**2*mV**2*gam*sp.cos(th)**2/((mV**2-w**2)**2+(w*gam)**2)
check("C3b P_s = 32 kappa^2 ... (Eq. 7) at m_V omega_n -> m_V^2 (odd n)", sp.simplify((Ps/src).subs(w, mV)) == 1,
      f"ratio = {sp.simplify(Ps/src)}")
I2 = sp.integrate(sp.diff(sp.cos(2*sp.pi*z/L0), z), (z, 0, L0))
check("C3c even-n modes do not couple (int d_z cos(2 pi z/L0) = 0)", I2 == 0)
# [ERR] C3d (VER-CW3 V15): |<n|dH0|0>|^2 = 8 kappa^2 rho_V e^2 cos^2 M_n/(eps0^2 rho^2 L0^2 omega_n)  (CW3 4.5 printed 4)
H0sq_s = sp.simplify(H0sq.subs(r**2, M/(rho_*sp.pi*L0)))
check("C3d [ERR] |<n|dH0|0>|^2 prefactor is 8 (not 4); 32 = 2pi x 8 x 2/pi",
      sp.simplify(H0sq_s - 8*kap**2*rV*e_**2*sp.cos(th)**2*M/(eps0**2*rho_**2*L0**2*w)) == 0 and 2*sp.pi*8*2/sp.pi == 32, str(H0sq_s))
# [ERR] C3e (VER-CW3 V15): Eq. (7)'s m_V^2 numerator is the exact steady-state power of a velocity-damped mode
# x'' + gam x' + w^2 x = (F/M) cos(m t); its integral over m equals the golden rule 2 pi m |F/2|^2 |x_10|^2, |x_10|^2 = 1/(2 M w).
F_, Mo, mm = sp.symbols('F M_o m', positive=True)
Xamp = (F_/Mo)/(w**2 - mm**2 + sp.I*gam*mm)
Pcl = sp.simplify(sp.re(sp.expand_complex(F_/2*sp.I*mm*Xamp)))
gnum = 1e-3; Pf = sp.lambdify(mm, Pcl.subs({F_: 1, Mo: 1, w: 1, gam: gnum}))
Pint = quad(Pf, 0.9, 1.1, points=[1.0], limit=400)[0] + quad(Pf, 0, 0.9)[0] + quad(Pf, 1.1, 50)[0]
check("C3e [ERR] damped-oscillator power = F^2 gam m^2/(2M((w^2-m^2)^2+gam^2 m^2)) (Eq. (7) form); integral = golden rule pi F^2/(4M)",
      sp.simplify(Pcl - F_**2*gam*mm**2/(2*Mo*((w**2-mm**2)**2 + gam**2*mm**2))) == 0 and abs(Pint/(np.pi/4) - 1) < 2e-3,
      f"int P dm/(pi F^2/4M) = {Pint/(np.pi/4):.5f}")

# ---------------------------------------------------------------------------------------------
# C4, C5 (LE-94): exact tree-level dark Compton (V or ALP at rest + e at rest -> gamma + e).
I2m = np.eye(2); Z2 = np.zeros((2, 2)); sxm = np.array([[0, 1], [1, 0]], complex); szm = np.diag([1., -1]).astype(complex)
g0 = np.block([[I2m, Z2], [Z2, -I2m]]).astype(complex); GG = [g0] + [np.block([[Z2, s], [-s, Z2]]) for s in (sxm, sy, szm)]
met = np.diag([1, -1, -1, -1.]); g5 = 1j*GG[0]@GG[1]@GG[2]@GG[3]
def sl(p): return sum(met[m, m]*p[m]*GG[m] for m in range(4))
def spinors(p, m):
    out = []
    for chi in (np.array([1, 0]), np.array([0, 1])):
        sp_ = sum(p[1+i]*[sxm, sy, szm][i] for i in range(3))
        out.append(np.sqrt(p[0]+m)*np.concatenate([chi, sp_@chi/(p[0]+m)]))
    return out
def sigv(mb, kind, me=1.0):
    s = (mb+me)**2; wp = (s-me**2)/(2*np.sqrt(s)); k = np.array([mb, 0, 0, 0.]); p = np.array([me, 0, 0, 0.])
    us = spinors(p, me); tot = 0; cnt = 0
    for ct in (-0.7, 0.1, 0.8):
        nv = np.array([np.sqrt(1-ct**2), 0, ct]); kp = np.concatenate([[wp], wp*nv]); pp = k+p-kp; ups = spinors(pp, me)
        a = np.cross(nv, [0.3, 0.5, 0.8]); a /= np.linalg.norm(a); b = np.cross(nv, a)
        P1 = k+p; P2 = p-kp; d1 = P1@met@P1-me**2; d2 = P2@met@P2-me**2
        verts = [sl(np.concatenate([[0], e])) for e in np.eye(3)] if kind == 'V' else [g5]
        for Vv in verts:
            for e in (a, b):
                eg = sl(np.concatenate([[0], e]))
                O = eg@(sl(P1)+me*np.eye(4))@Vv/d1 + Vv@(sl(P2)+me*np.eye(4))@eg/d2
                tot += sum(abs(u2.conj()@g0@O@u1)**2 for u1 in us for u2 in ups)
        cnt += 1
    M2 = tot/cnt/len(verts)/2
    return M2*wp/(4*np.pi*np.sqrt(s))/(2*mb*2*me)      # e = coupling = 1 (HL), m_e = 1
xs = (1e-3, 0.1, 1.0, 3.0)
rV_ = [sigv(xx, 'V')/((xx+2)*(xx**2+2*xx+2)/(24*np.pi*(xx+1)**3)) for xx in xs]
check("C4a dark photon: exact tree QED = 2109.08168 Eq. (2) at all x", np.allclose(rV_, 1, atol=1e-10), str(np.round(rV_, 12)))
X = sp.symbols('x'); wpX = X*(X+2)/(2*(X+1))       # omega'/m_e for V at rest
T4 = (wpX/X)/(1+wpX)                                # (T.4)/(n kappa^2 sigma_Th)
EX = (X+2)*(X**2+2*X+2)/(4*(X+1)**3)                # Eq.(2)/(n kappa^2 sigma_Th)
dser = sp.series(EX - T4, X, 0, 4).removeO()
wnr = -1 + sp.sqrt(1 + 2*X); T4nr = (wnr/X)/(1 + wnr)  # (T.4) with NR recoil omega' + omega'^2/2m = m_V
c3 = [sp.series(f, X, 0, 4).removeO().coeff(X, 3) for f in (EX, T4, T4nr)]
check("C4c x^3 coefficients: exact -15/4, (T.4) exact recoil -17/4, (T.4) NR recoil -35/8",
      c3 == [sp.Rational(-15, 4), sp.Rational(-17, 4), sp.Rational(-35, 8)] and
      all(sp.series(f, X, 0, 3).removeO() == sp.series(EX, X, 0, 3).removeO() for f in (T4, T4nr)), str(c3))
check("C4b (T.4) = exact through O(x^2); first difference at O(x^3)",
      sp.simplify(dser.coeff(X, 0)) == 0 and dser.coeff(X, 1) == 0 and dser.coeff(X, 2) == 0 and dser.coeff(X, 3) != 0,
      f"exact - T4 = {sp.nsimplify(dser)}")
rA = [sigv(xx, 'A')/(xx*xx*(xx+2)/(16*np.pi*(xx+1)**3)) for xx in xs]
check("C5a ALP: exact tree QED sigma v = e^2 g^2 m_a^2 (m_a+2m_e)/(16 pi m_e^2 (m_a+m_e)^3)", np.allclose(rA, 1, atol=1e-10),
      str(np.round(rA, 12)))
r3 = [((xx+2)**2/(xx+1)**4)/((xx+2)/(xx+1)**3) for xx in xs]
check("C5b 2109.08168 Eq. (3) exceeds the exact result by (m_a+2m_e)/(m_a+m_e) (factor 2 at m_a << m_e)",
      np.allclose(r3, [(xx+2)/(xx+1) for xx in xs]), str(np.round(r3, 4)))
# route 2: the source's own |M|^2 (App. Eq. (16), ALP; Eq. (9), vector) vs exact: same 1/4 offset, so (16) integrated like (9)->(12) gives (CW3.5)
def M2ex(mb, kind, me=1.0):
    s_ = (mb+me)**2; wp_ = (s_-me**2)/(2*np.sqrt(s_)); return sigv(mb, kind)*(4*np.pi*np.sqrt(s_))*(2*mb*2*me)/wp_
off = []
for xx in (0.1, 1.0, 3.0):
    s_ = (xx+1)**2; wp_ = (s_-1)/(2*np.sqrt(s_)); w_ = xx; D9 = 2*w_+xx**2; D16 = xx**2+2*w_
    b9 = (2+xx**2)/wp_**2+4*wp_/D9+4*(2+xx**2)*(1+2*w_+xx**2)/D9**2+(xx**4+4*(w_**2-xx**2)-8*(w_+1))/(wp_*D9)
    b16 = xx**2/wp_**2+(xx**4-4*xx**2+4*w_**2)/(wp_*D16)+4*xx**2/D16**2+(4*wp_-8*w_)/D16
    off.append((M2ex(xx, 'V')/(b9/6), M2ex(xx, 'A')/(b16/4)))
check("C5d source Eq. (9) and Eq. (16) carry the same normalisation offset (x4) relative to exact |M|^2",
      np.allclose(np.array(off), 4.0, atol=1e-9), str(np.round(np.array(off), 9).tolist()))
# NR seagull -(e g/(2 m^2)) (d_t a) sigma.A : sigma v = c^2 omega'/(2 pi m_a), c = e g m_a/(2 m^2)
xa = 1e-3; c_ = xa/2; nr = c_**2*(xa*(xa+2)/(2*(xa+1)))/(2*np.pi*xa)
check("C5c NR seagull reproduces the exact ALP rate as m_a -> 0: ratio = (1 + m_a/m_e)^2 exactly", abs(nr/sigv(xa, 'A') - (1 + xa)**2) < 1e-9,
      f"{nr/sigv(xa,'A'):.8f}")

# ---------------------------------------------------------------------------------------------
# C6 (LE-95): Bethe from (S.1); prefactor and the log constant (oscillator model, exact k-split).
Zk, al, v, me_, ne, k0, wn, fn = sp.symbols('Z alpha v m_e n_e k_0 omega_n f_n', positive=True)
wp2 = 4*sp.pi*al*ne/me_
pref = (2*Zk**2*al/(sp.pi*v**2))*(sp.pi/2)*wp2
check("C6a (2Z^2 alpha/pi v^2)(pi/2)omega_p^2 = 4 pi Z^2 alpha^2 n_e/(m_e v^2)", sp.simplify(pref - 4*sp.pi*Zk**2*al**2*ne/(me_*v**2)) == 0)
logsum = sp.log(k0*v/wn) + sp.log(2*me_*v/k0)
check("C6b k_0 drops out: ln(k0 v/omega) + ln(2 m v/k0) = ln(2 m v^2/omega)", sp.simplify(sp.expand_log(logsum - sp.log(2*me_*v**2/wn), force=True)) == 0)
# [ERR] C6c (VER-CW3 V20; the CW3 version was a hard-coded True): PDG bracket (1/2)ln(2 m b^2 g^2 W_max/I^2) - b^2,
# W_max = 2 m b^2 g^2 (heavy projectile), minus ln(2 m v^2/I): the ln g^2 = b^2 + ... cancels -b^2, remainder O(v^4) (= b^4/2).
bet, Ii = sp.symbols('beta I', positive=True); gam2 = 1/(1 - bet**2); Wm = 2*me_*bet**2*gam2
brk = sp.Rational(1, 2)*sp.log(2*me_*bet**2*gam2*Wm/Ii**2) - bet**2
rem = sp.series(sp.expand_log(brk - sp.log(2*me_*bet**2/Ii), force=True), bet, 0, 6).removeO()
check("C6c [ERR] PDG Eq. (34.5) bracket -> ln(2 m v^2/I) + v^4/2 + ... (NR); the '- v^2' of CW3 4.10 is wrong",
      sp.simplify(rem.coeff(bet, 2)) == 0 and sp.simplify(rem.coeff(bet, 4) - sp.Rational(1, 2)) == 0 and sp.simplify(rem.coeff(bet, 0)) == 0,
      f"bracket - ln(2mv^2/I) = {sp.simplify(rem)} + O(v^6)")

# ---------------------------------------------------------------------------------------------
# C7 (LE-87): massive nu~ kinematics: omega^F = omega_WP0 + k^2/(2 m_chi) - k^2/(2 m_nu), k = m_chi v - q (exact at NR order)
mc, d, vv, qq, cth = sp.symbols('m_chi Delta v q c', real=True)
mn = mc + d; k2 = mc**2*vv**2 - 2*mc*qq*vv*cth + qq**2
omF = (mc + mc*vv**2/2) - (mn + k2/(2*mn)); om0 = qq*vv*cth - qq**2/(2*mc) - d
check("C7 omega^F - omega(2.1) = k^2/2m_chi - k^2/2m_nu (= (Delta/m_nu) k^2/2m_chi)",
      sp.simplify(omF - om0 - (k2/(2*mc) - k2/(2*mn))) == 0 and sp.simplify(k2/(2*mc) - k2/(2*mn) - d/mn*k2/(2*mc)) == 0)

# ---------------------------------------------------------------------------------------------
# C8 (LE-79): O_2 matching. Plane waves k -> k' = k+q: v_s = (k+k')/2m; (v_chi - v_s)^2 = v_chi^2 - 2 v_chi.v_s + v_s^2,
# and <k'|K|k> = (k+k')^2/(4m^2) = k.k'/m^2 + q^2/(4m^2); {p,{p,e^{iqx}}}/4m^2 has that matrix element (1D check).
kk, qv, m, vc = sp.symbols('k q m v_chi', real=True)
kp_ = kk + qv
lhs = (vc - (kk+kp_)/(2*m))**2; rhs = vc**2 - 2*vc*(kk+kp_)/(2*m) + (kk+kp_)**2/(4*m**2)
mat = (kp_*kp_ + kp_*kk + kp_*kk + kk*kk)/(4*m**2)      # <k'| p p e + p e p + p e p + e p p |k>/4m^2
check("C8 O_2 -> v_chi^2 n - 2 v_chi.j + K_s; K_s = {p,{p,e^{iqr}}}/(4m^2) = k.k'/m^2 + q^2/4m^2",
      sp.simplify(lhs - rhs) == 0 and sp.simplify(mat - (kk+kp_)**2/(4*m**2)) == 0
      and sp.simplify((kk+kp_)**2/(4*m**2) - (kk*kp_/m**2 + qv**2/(4*m**2))) == 0)

# ---------------------------------------------------------------------------------------------
# C9 (LE-83): relaxed electron channel. (a) two-fluid toy: static step = above-phonon step + Lehmann LO term
ae, ai0, wT, om = sp.symbols('a_e a_i0 omega_T omega', positive=True)
vR = lambda ai: -ae + ae**2/(1 + ae + ai)
ai_w = ai0*wT**2/(wT**2 - om**2)
step0 = sp.simplify(-vR(ai0)); stepinf = sp.simplify(-vR(0))
check("C9a step(0) - step(above phonons) = a_e^2 (1/eps_inf - 1/eps_0) >= 0",
      sp.simplify(step0 - stepinf - ae**2*(1/(1+ae) - 1/(1+ae+ai0))) == 0)
check("C9b GaAs-like two-fluid: 1 - eps_e^-1 = 2.30", abs(float(step0.subs({ae: 9.9, ai0: 2.0})) - 2.30) < 0.01,
      f"{float(step0.subs({ae: 9.9, ai0: 2.0})):.3f}")
# LO pole of R_ee(omega): residue consistent with Lehmann sum (static - high-freq = 2 w/omega_LO)
wL2 = wT**2*(1+ae+ai0)/(1+ae)
Rw = vR(ai_w); res = sp.limit(sp.simplify(Rw*(om**2 - wL2)), om, sp.sqrt(wL2))
check("C9c Lehmann: vR(0) - vR(inf) = -res/omega_LO^2 (single LO pole)", sp.simplify(vR(ai0) - vR(0) + res/wL2) == 0)
# (b) acoustic GS term: Omega_P,e^2/(c_L q)^2 for Si, GaAs (all-electron n_e, rho_T)
hbarc = 1.97327e-5  # eV cm
def OmP2(ne_cm3, rho_gcm3):
    n = ne_cm3*hbarc**3; r_ = rho_gcm3*5.6096e32*hbarc**3
    return 4*np.pi/137.036*n**2/r_
for name, ne_, rh, cL in (("Si", 14*4.994e22, 2.329, 8433.0), ("GaAs", 64*2.213e22, 5.317, 4730.0)):
    O2 = OmP2(ne_, rh); cq = cL/2.998e8*1e3   # omega_LA(q = 1 keV) in eV
    print(f"      {name}: Omega_P,e = {np.sqrt(O2):.3f} eV; acoustic step at q = 1 keV: {O2/cq**2:.0f}; q* = Omega/c = {np.sqrt(O2)/(cL/2.998e8)/1e3:.1f} keV")
check("C9d Si q -> 0 formula evaluated at q = 1 keV: Omega_P,e^2/(c_L q)^2 = 333 (an [E] extrapolation, VER-CW3 V6)",
      330 < OmP2(14*4.994e22, 2.329)/(8433/2.998e8*1e3)**2 < 336 and abs(np.sqrt(OmP2(14*4.994e22, 2.329)) - 0.513) < 1e-3)
# [ERR] C9e (VER-CW3 V6): the q -> 0 limit is exact only asymptotically. Monatomic-chain toy (one acoustic branch,
# omega = 2 sqrt(K/M)|sin(qa/2)|, Z^(e) = const): G_GS/[Omega^2/(c_L q)^2] = (qa/2)^2/sin^2(qa/2) = 1 + O(q^2), pi^2/4 at the zone edge;
# in a real solid Z^(e)(q) also falls off, so the sign of the deviation is not fixed -> [D] only as q -> 0, [E] at q ~ q_BZ.
ua = sp.symbols('u', positive=True); ratio_ch = ua**2/sp.sin(ua)**2
check("C9e [ERR] linear-dispersion form exact only as q -> 0: ratio 1 + (qa)^2/12 + ..., pi^2/4 at q = pi/a",
      sp.limit(ratio_ch, ua, 0) == 1 and sp.series(ratio_ch, ua, 0, 3).removeO().coeff(ua, 2) == sp.Rational(1, 3)
      and sp.simplify(ratio_ch.subs(ua, sp.pi/2) - sp.pi**2/4) == 0)

# ---------------------------------------------------------------------------------------------
# C10 (LE-89): Rabi frequency of H = (w_L/2) s_z - d E s_x cos(w_L t) is Omega_a = dE (= per-level shift, half-splitting);
# small-angle M_perp/M_0 = Omega_a t at resonance -> 1306.6089 Eq. (1) amplitude (np mu E* eps_S d_n t) with d_n eps_S E* = dE.
wL, dE, T = 50.0, 0.01, 30.0
from scipy.integrate import solve_ivp
def rhs(t, y):
    psi = y[:2] + 1j*y[2:]
    H = 0.5*wL*np.diag([1, -1]) - dE*np.cos(wL*t)*np.array([[0, 1], [1, 0]])
    d = -1j*H@psi; return np.concatenate([d.real, d.imag])
sol = solve_ivp(rhs, (0, T), [0, 1, 0, 0], rtol=1e-10, atol=1e-12, max_step=0.01)   # start in the lower level
psi = sol.y[:2, -1] + 1j*sol.y[2:, -1]
mperp = 2*abs(np.conj(psi[0])*psi[1])
check("C10 transverse magnetisation grows as M0 * (dE) t (Rabi = dE, not dE/2 or 2dE)", abs(mperp/np.sin(dE*T) - 1) < 5e-4,
      f"M_perp/sin(dE t) = {mperp/np.sin(dE*T):.4f}")
# u factor (2101.01241 S22-S23): in-phase steady state averaged over a symmetric inhomogeneous line; quadrature -> 0
T2, Gam = 16.7, 2*np.pi*78.0   # ms, rad/ms (78 kHz full width)
D = np.linspace(-3*Gam, 3*Gam, 200001); h = np.where(abs(D) < Gam/2, 1/Gam, 0)
Lr = 1/(1 + (D*T2)**2); Li = D*T2/(1 + (D*T2)**2)
u = np.trapezoid(Lr*h, D); uq = np.trapezoid(Li*h, D)
u_exact = (2/(Gam*T2))*np.arctan(Gam*T2/2)            # closed form for a box line (-> pi/(Gamma T2), S24)
check("C10b u = int L h (box line) = (2/(Gamma T2)) arctan(Gamma T2/2) ~ pi/(Gamma T2); quadrature cancels; within S25 3.8(3)e-4",
      abs(u/u_exact - 1) < 1e-6 and abs(uq) < 1e-9 and abs(u_exact/(np.pi/(Gam*T2)) - 1) < 2e-4 and abs(u - 3.8e-4) < 0.3e-4,
      f"u = {u:.4e}")

# ---------------------------------------------------------------------------------------------
# [ERR] C11 (LE-77 owed corrections 1-2; the CW3 C11 was arithmetic only): on random kernels with phonon branches nu and a
# non-phonon branch x (c_x = 0), (a) |dP| <= (G_ph/G) max_nu|c_nu| * spread(P_b) always holds and is nearly saturated,
# (b) 2 max|c| <= 1 => all K_b >= 0, and K_b < 0 occurs for some kernels with 2 max|c| > 1 (the condition is not vacuous).
rr = np.random.default_rng(11); worst = 0.0; viol = 0; neg_found = False
for _ in range(20000):
    nb = rr.integers(2, 6); Gb_ = rr.uniform(0.1, 1.0, nb + 1); Gb_[-1] *= rr.uniform(0, 2)     # last = x branch
    cmax = rr.uniform(0, 1.2); cb_ = np.append(rr.uniform(-cmax, cmax, nb), 0.0); Pb_ = rr.uniform(0, 1, nb + 1)
    Gt = Gb_.sum(); cbar_ = np.sum(Gb_*cb_)/Gt; Kb_ = (Gb_/Gt)*(1 + cbar_ - cb_)
    dP = np.sum((Kb_ - Gb_/Gt)*Pb_); bnd = (Gb_[:-1].sum()/Gt)*np.max(np.abs(cb_[:-1]))*(Pb_.max() - Pb_.min())
    if bnd > 0: worst = max(worst, abs(dP)/bnd)
    if 2*np.max(np.abs(cb_)) <= 1 and np.min(Kb_) < -1e-14: viol += 1
    if 2*np.max(np.abs(cb_)) > 1 and np.min(Kb_) < 0: neg_found = True
check("C11a [ERR] (W15) bound |dP| <= (G_ph/G) max|c^F| spread holds on 2e4 random kernels incl. x branch", worst <= 1 + 1e-12 and worst > 0.5,
      f"max |dP|/bound = {worst:.3f}")
check("C11b [ERR] 2 max|c^F| <= 1 => K_b >= 0 (no violation); K_b < 0 reachable when 2 max|c^F| > 1", viol == 0 and neg_found)

# ---------------------------------------------------------------------------------------------
# [ERR] C12 (VER-CW3 V9, LE-82): with U_qp = 1 the bare sea is not an H eigenstate, so H_off|nk> contains the disconnected
# c+_nk H_off|FS>, whose norm^2 is extensive. Exact Fock-space toy: 1D ring of N cells, bands v (filled), c (empty), one phonon
# branch, X = N^-1/2 sum g_mn(k,Q) c+_{m,k+Q} c_{nk} b+_{-Q} (the emission half of H_ep; phonon vacuum, one application).
def fock_toy(N, gfun):
    g = np.array([[[[gfun(m, n, k, Q, N) for Q in range(N)] for k in range(N)] for n in range(2)] for m in range(2)])
    fidx = lambda b, k: 2*(k % N) + b
    def apply_X(state):
        out = {}
        for (fb, pb), amp in state.items():
            for k in range(N):
                for Q in range(1, N):
                    for n_ in range(2):
                        j = fidx(n_, k)
                        if not (fb >> j) & 1: continue
                        s1 = (-1)**bin(fb & ((1 << j) - 1)).count('1'); f1 = fb & ~(1 << j)
                        for m_ in range(2):
                            i = fidx(m_, k + Q)
                            if (f1 >> i) & 1: continue
                            s2 = (-1)**bin(f1 & ((1 << i) - 1)).count('1'); qb = (-Q) % N
                            key = (f1 | (1 << i), pb | (1 << qb))
                            out[key] = out.get(key, 0) + amp*s1*s2*g[m_, n_, k, Q]/np.sqrt(N)
        return out
    FS = sum(1 << fidx(0, k) for k in range(N)); j0 = fidx(1, 0)
    sgn = (-1)**bin(FS & ((1 << j0) - 1)).count('1')
    nFS = sum(abs(a)**2 for a in apply_X({(FS, 0): 1.0}).values())
    nSrc = sum(abs(a)**2 for a in apply_X({(FS | (1 << j0), 0): sgn}).values())
    conn = sum(abs(g[1, 1, 0, Q])**2 for Q in range(1, N))/N                 # source electron -> (c, Q): orthogonal component
    blocked = sum(abs(g[1, 0, (-Q) % N, Q])**2 for Q in range(1, N))/N       # sea (v, -Q) -> (c, 0): Pauli-blocked by the source
    fm0 = sum(abs(g[m_, 1, 0, Q])**2 for m_ in range(2) for Q in range(1, N))/N   # Fan-Migdal zeroth moment (all m), T = 0
    fsform = sum(abs(g[1, 0, k, Q])**2 for k in range(N) for Q in range(1, N))/N
    return nFS, fsform, nSrc, conn, blocked, fm0
rq = np.random.default_rng(3); Gr = rq.normal(size=(2, 2, 8, 8)) + 1j*rq.normal(size=(2, 2, 8, 8))
res_r = [fock_toy(N, lambda m, n, k, Q, N_: Gr[m, n, k, Q]) for N in (3, 4, 5)]
check("C12a [ERR] ||H_off|nk>||^2 = ||H_off|FS>||^2 + conn - blocked exactly (Fock toy, N = 3,4,5)",
      all(abs(r_[0] - r_[1]) < 1e-12 and abs(r_[2] - (r_[0] + r_[3] - r_[4])) < 1e-12 for r_ in res_r))
smooth = lambda m, n, k, Q, N_: (0.7 + 0.3j*m - 0.2*n)*np.sin(np.pi*Q/N_)*(1 + 0.3*np.cos(2*np.pi*k/N_))
res_s = {N: fock_toy(N, smooth) for N in (4, 8, 16)}
check("C12b [ERR] disconnected part extensive (||H_off|FS>||^2 ~ N), connected part intensive (U_qp = 1)",
      1.9 < res_s[8][0]/res_s[4][0] < 2.3 and 1.9 < res_s[16][0]/res_s[8][0] < 2.1 and abs(res_s[16][3]/res_s[8][3] - 1) < 0.05,
      f"||H_off FS||^2: {res_s[4][0]:.2f}, {res_s[8][0]:.2f}, {res_s[16][0]:.2f}; conn: {res_s[8][3]:.3f}, {res_s[16][3]:.3f}")
check("C12c [ERR] the subtracted 'linked' norm conn - blocked is sign-indefinite (not a norm); conn <= FM zeroth moment",
      min(r_[3] - r_[4] for r_ in res_r) < 0 < max(r_[3] - r_[4] for r_ in res_r) and all(r_[3] <= r_[5] + 1e-15 for r_ in res_r),
      str([round(r_[3] - r_[4], 3) for r_ in res_r]))
# C12d: dressed-vacuum lemma. If |i> is an H eigenstate inside Ran Q_0 (a rank-3 sector projector that contains |i> but is not
# |i><i|; three sectors), then H_off|i> = 0 exactly, while H_off itself is not small; for bare sectors not containing |i>, H_off|i> != 0.
Hm = rq.normal(size=(8, 8)); Hm2 = Hm + Hm.T
ev2, V2 = np.linalg.eigh(Hm2); vac = V2[:, 0]
Wr = np.linalg.qr(np.column_stack([vac, rq.normal(size=(8, 7))]))[0]          # sector 0 = span(vac, two random vectors)
Ps = [Wr[:, :3] @ Wr[:, :3].T, Wr[:, 3:5] @ Wr[:, 3:5].T, Wr[:, 5:] @ Wr[:, 5:].T]
Hd_v = sum(P_ @ Hm2 @ P_ for P_ in Ps)
Pb = [np.diag([1., 1, 1, 0, 0, 0, 0, 0]), np.diag([0., 0, 0, 1, 1, 0, 0, 0]), np.diag([0., 0, 0, 0, 0, 1, 1, 1])]
Hd_b = sum(P_ @ Hm2 @ P_ for P_ in Pb)
check("C12d [ERR] lemma: |i> in Ran Q_0 (rank 3) and H|i> = E|i> => H_off|i> = 0 with H_off != 0; bare sectors give H_off|i> != 0",
      np.linalg.norm(Ps[0] @ vac - vac) < 1e-12 and np.linalg.norm(Hd_v - Hm2) > 1.0 and np.linalg.norm((Hm2 - Hd_v) @ vac) < 1e-12
      and np.linalg.norm((Hm2 - Hd_b) @ vac) > 1e-2,
      f"||H_off|| = {np.linalg.norm(Hd_v - Hm2):.2f}; ||H_off vac|| dressed {np.linalg.norm((Hm2 - Hd_v) @ vac):.1e}, bare {np.linalg.norm((Hm2 - Hd_b) @ vac):.2f}")

# ---------------------------------------------------------------------------------------------
# [ERR] C13 (VER-CW3 V10, LE-82 (3)): one-loop running of the 3D Dirac Coulomb coupling, alpha = e^2/(4 pi eps v) (HL).
# (a) velocity: exchange self-energy sigma-part, large-p expansion e^2 int d^3p/(2pi)^3 (k.p^)p^/p^3 = (e^2/6pi^2) k ln -> dv/v = (2 alpha/3 pi) dl;
# (b) charge: static interband bubble of one Weyl node, -sum 2|<k+q,+|k,->|^2/(v(k+k')) -> -(q^2/12 pi^2 v) ln, i.e. eps = 1 + N_W (alpha/3 pi) ln
#     = 1 + N_D (2 alpha/3 pi) ln; hence d alpha/dl = -(2(N_D + 1)/3 pi) alpha^2, = -4 alpha^2/3 pi at N_D = 1 (1101.2210 Eq. (4) [FT]).
thS, phS, kS, qS, aS, vS = sp.symbols('theta phi k q alpha v', positive=True)
ang_v = sp.integrate(sp.integrate(sp.cos(thS)**2*sp.sin(thS), (thS, 0, sp.pi)), (phS, 0, 2*sp.pi))/(2*sp.pi)**3   # coefficient of e^2 k ln
coef_v = sp.simplify(ang_v*4*sp.pi*aS*vS/vS)                                                                         # e^2 = 4 pi alpha v
kvec = sp.Matrix([kS*sp.sin(thS), 0, kS*sp.cos(thS)]); kpq = kvec + sp.Matrix([0, 0, qS])
cosk = (kvec.dot(kpq))/(kS*sp.sqrt(kpq.dot(kpq)))
ov2 = sp.series((1 - cosk)/2, qS, 0, 3).removeO()                                                   # |overlap|^2 to O(q^2)
integrand = sp.simplify(sp.series(-2*ov2/(vS*(kS + sp.sqrt(kpq.dot(kpq)))), qS, 0, 3).removeO().coeff(qS, 2))
ang_c = sp.simplify(sp.integrate(sp.integrate(integrand*kS**3*sp.sin(thS), (thS, 0, sp.pi)), (phS, 0, 2*sp.pi))/(2*sp.pi)**3)
coef_c_weyl = sp.simplify(-ang_c*4*sp.pi*aS*vS)                                                     # eps - 1 = -v_C Pi, coefficient of ln per Weyl node
check("C13a [ERR] velocity renormalisation dv/(v dl) = 2 alpha/3 pi (1101.2210 Eq. (3) at Delta_V = 0)", sp.simplify(coef_v - 2*aS/(3*sp.pi)) == 0, str(coef_v))
check("C13b [ERR] charge part: alpha/3 pi per Weyl node = 2 alpha/3 pi per Dirac node; total 2(N_D+1)/3 pi, = 4/3 pi at N_D = 1",
      sp.simplify(coef_c_weyl - aS/(3*sp.pi)) == 0 and sp.simplify(2*coef_c_weyl + coef_v - 4*aS/(3*sp.pi)) == 0, str(coef_c_weyl))
lD = sp.symbols('l', positive=True); aF = sp.Function('a')
solRG = sp.dsolve(sp.Eq(aF(lD).diff(lD), -sp.Rational(4, 3)/sp.pi*aF(lD)**2), aF(lD), ics={aF(0): sp.Rational(91, 100)}).rhs
a_bench = float(solRG.subs(lD, sp.log(1000))); a_old = 0.91/(1 + 2*0.91/(3*np.pi)*np.log(1e3))
check("C13c [ERR] benchmark alpha0 = 0.91, N_D = 1, Lambda/omega = 1e3: alpha = 0.248, alpha^2 = 0.062 (CW3: 0.39, 0.15)",
      abs(a_bench - 0.248) < 1e-3 and abs(a_bench**2 - 0.0616) < 5e-4 and abs(a_old - 0.390) < 1e-3, f"alpha = {a_bench:.4f}, alpha^2 = {a_bench**2:.4f}")

# ---------------------------------------------------------------------------------------------
# [ERR] C14 (VER-CW3 V8, LE-80 (ii)): Williamson/Bogoliubov normal modes need a positive-definite quadratic form.
# H = (h x^2 + p^2)/2: J H is diagonalisable with eigenvalues +-i sqrt(h) for h > 0; at h = 0 (Goldstone / Q = 0 acoustic zero mode)
# it is a nilpotent Jordan block: no oscillator, no number operator, so the hybrid-quanta sectors need the zero modes gapped or removed.
hS = sp.symbols('h', nonnegative=True); Jm = sp.Matrix([[0, 1], [-1, 0]])
JH = lambda hv: Jm*sp.diag(hv, 1)
check("C14 [ERR] symplectic diagonalisation exists for h > 0, fails (Jordan block) at h = 0",
      JH(sp.Rational(1, 4)).is_diagonalizable() and not JH(0).is_diagonalizable() and set(JH(sp.Rational(1, 4)).eigenvals()) == {sp.I/2, -sp.I/2})

ok = all(r for _, r in RES)
print(f"\n{sum(r for _, r in RES)}/{len(RES)} PASS")
sys.exit(0 if ok else 1)
