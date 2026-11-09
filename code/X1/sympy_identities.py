"""R3/X1 sympy identities (runtime < 5 s).
S1  lab-frame soft ratio = Galilean piece + lattice-frame ratio:
      (D + v P)/(v + s c) == P + (D - s c P)/(v + s c)
S2  Froehlich intraband pair (g_nn = (iC/Q) rho_nn(Q), denominators a + Q v_c and -a - Q v_v, a = +-w_LO):
      the 1/Q pieces cancel (pair neutrality) and the O(1) remainder is
      -(iC/a) [ dRho_cov + rho * (v_c - v_v)/a ],  dRho_cov = d_k rho - i(A_c - A_v) rho
S3  IR power counting of the soft sideband weight  int d^dQ |M|^2 (n+1)  for couplings
      deformation (g ~ l Q), piezoelectric (g ~ l), Froehlich (g ~ 1/Q, gapped), acoustic l^2 = 1/(2 M c Q).
"""
import sympy as sp

D, v, P, c, s = sp.symbols('D v P c s', real=True)
print('S1:', sp.simplify((D + v*P)/(v + s*c) - (P + (D - s*c*P)/(v + s*c))))

Q, C, a, vc, vv, Ac, Av, r, dr = sp.symbols('Q C a v_c v_v A_c A_v rho drho', real=True)
expr = (sp.I*C/Q)*((1 + sp.I*Q*Ac)*r/(a + Q*vc) - (r + Q*dr)*(1 + sp.I*Q*Av)/(a + Q*vv))
lim = sp.limit(expr, Q, 0)
target = -(sp.I*C/a)*((dr - sp.I*(Ac - Av)*r) + r*(vc - vv)/a)
print('S2: 1/Q coefficient =', sp.simplify(sp.series(expr, Q, 0, 1).removeO().coeff(Q, -1)),
      '; O(1) remainder - target =', sp.simplify(lim - target))

d, x = sp.symbols('d x', positive=True)
# |M|^2 ~ l^2 * (coupling ratio)^2 ; ratio = g/(Q*x) for gapless acoustic
for name, M2 in [('deformation', (1/Q)*(Q/Q)**2), ('piezoelectric', (1/Q)*(1/Q)**2)]:
    for T in ('T=0', 'T>0'):
        integrand = sp.simplify(Q**(d-1)*M2*(1 if T == 'T=0' else 1/Q))
        print(f'S3: {name:13s} {T}: dQ integrand ~ {sp.powsimp(integrand)}  (IR-finite iff exponent > -1)')
