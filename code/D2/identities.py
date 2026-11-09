"""D2 tiny symbolic checks (theory-only mode; no numerical evaluation).
(1) q=0: A1+A2 = 0 on shell (N conserved).
(2) Rigid-shift (C7) identity: with g_mn = lam*(e_m-e_n)*d_mn and w0->0,
    A1+A2 = lam*([d,rho]_f0 - d_ff rho_f0 + rho_f0 d_00)   (generic 3-level algebra).
(3) Dimensions of eps2 = (pi e^2/(q^2 V)) * sum |<f|n_q|0>|^2 delta(w-E).
"""
import sympy as sp
# (1)
g, ec, ev, wQ = sp.symbols('g e_c e_v w_Q')
w = ec - ev + wQ                                   # on shell, emission, q=0
A1 = g*1/(w - ev + ev)                             # m=v term, rho_vv(k,0)=1
A2 = 1*g/(ev - ec - wQ)                            # m=c term, rho_cc(k,0)=1
print('(1) q=0 cancellation:', sp.simplify(A1 + A2))
# (2)
n = 3; lam, w0 = sp.symbols('lam w0')
e = sp.symbols('e0:3')
d = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'd{i}{j}'))
r = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'r{i}{j}'))
gm = sp.Matrix(n, n, lambda i, j: lam*(e[i]-e[j])*d[i, j])
f, i0 = 2, 0
om = e[f] + w0 - e[i0]
A1 = sum(gm[f, m]*r[m, i0]/(om - e[m] + e[i0]) for m in range(n))
A2 = sum(r[f, m]*gm[m, i0]/(e[i0] - e[m] - w0) for m in range(n))
lhs = sp.limit(sp.simplify(A1 + A2), w0, 0)
rhs = lam*((d*r - r*d)[f, i0] - d[f, f]*r[f, i0] + r[f, i0]*d[i0, i0])
print('(2) rigid-shift identity residual:', sp.simplify(lhs - rhs))
# (3) natural units: [E]=[q]=M, [Omega]=M^-3, e^2 dimensionless, V=N*Omega,
# sum_f |<f|n_q|0>|^2 ~ N (one term per k for each fixed band/phonon label), [delta]=M^-1
M, N = sp.symbols('M N', positive=True)
dim = (1/(M**2 * N*M**-3)) * N * M**-1
print('(3) [eps2] =', sp.simplify(dim), '(dimensionless, N-independent)')
