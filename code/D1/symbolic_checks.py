"""D1 (R1) tiny symbolic + dimensional checks (sympy only, no numerics).

S1  Pauli/exchange: on shell, the hole paths C, D equal paths A, B with m occupied.
S2  q=0 cancellation of the delta_{mn} part of rho (number operator gives no transition).
S3  Partial-fraction identities behind length->velocity (C1) and the commutator limit (C7).
S4  Dimensions (powers of energy, hbar=c=1) of eps2^PA and dR/domega.
"""
import sympy as sp

ev, ec, em, w, wQ, g, r = sp.symbols('e_v e_c e_m omega omega_Q g rho', real=True)
s = sp.symbols('s')  # s=+1 emission, s=-1 absorption (phonon energy s*omega_Q given to lattice)
onshell = {w: ec - ev + s*wQ}

# S1 ------------------------------------------------------------------------
# path D (phonon first creates c-hole at m occ, DM fills hole from v): sign -1 (fermion exchange)
D = -r*g/(-(ec - em + s*wQ))                 # amplitude/(E_i - E_I), with the -1 sign
A = g*r/(ev + w - em)                        # path A form with same m
print('S1a (D - A on shell):', sp.simplify((D - A).subs(onshell)))
C = -g*r/(w - ec + em)                       # path C: DM first (m occ -> c), phonon moves hole m->v
B = r*g/(ev - em - s*wQ)                     # path B form
print('S1b (C - B on shell):', sp.simplify((C - B).subs(onshell)))

# S2 ------------------------------------------------------------------------
gcv = sp.Symbol('g_cv')
A_diag = gcv*1/(ev + w - ev)                 # path A, m=v, rho_vv(q=0)=1
B_diag = 1*gcv/(ev - ec - s*wQ)              # path B, m=c, rho_cc(q=0)=1
print('S2 (q=0 delta part):', sp.simplify((A_diag + B_diag).subs(onshell)))

# S3 ------------------------------------------------------------------------
Ei, Em, Ef, wG = sp.symbols('E_i E_m E_f omega_G')
os3 = {Ef: Ei + w - wG}
lhsA = 1/((Em - Ei)*(Ei + w - Em)); rhsA = (1/w)*(1/(Em - Ei) + 1/(Ei + w - Em))
lhsB = 1/((Ef - Em)*(Ei - Em - wG)); rhsB = (1/w)*(1/(Ei - Em - wG) - 1/(Ef - Em))
print('S3a:', sp.simplify(lhsA - rhsA), ' S3b:', sp.simplify((lhsB - rhsB).subs(os3)))
# commutator form G_ab=(E_b-E_a)A_ab:  pathA weight (Em-Ef)/(Ei+w-Em) = -1 + wG/(Ei+w-Em)
print('S3c:', sp.simplify(((Em - Ef)/(Ei + w - Em) - (-1 + wG/(Ei + w - Em))).subs(os3)),
      ' S3d:', sp.simplify((Ei - Em)/(Ei - Em - wG) - (1 + wG/(Ei - Em - wG))))

# S4 ------------------------------------------------------------------------
# dimension = power of energy
dim = dict(alpha=0, Omega=-3, q=1, rho=0, g=1, denom=-1, delta=-1,
           rho_chi=4, m_chi=1, rho_T=4, sigma=-2, mu=1, F=0, e2=0, L=0)
M = dim['rho'] + dim['g'] + dim['denom']
eps2 = dim['alpha'] - dim['Omega'] - 2*dim['q'] + 2*M + dim['delta']   # 8pi^2 alpha/(Omega q^2)|M|^2 delta
print('S4 dim[M2] =', M, ' dim[eps2_PA] =', eps2)
S = 2*dim['q'] - dim['e2'] + dim['L']
gv = dim['delta']                              # int d^3v f(v) delta(omega - q.v + q^2/2m)
dRdw = dim['rho_chi'] - dim['m_chi'] - dim['rho_T'] + dim['sigma'] - 2*dim['mu'] + 3*dim['q'] + gv + S
print('S4 dim[dR/domega] =', dRdw, '(expected -1: 1/(time*mass*energy))')
