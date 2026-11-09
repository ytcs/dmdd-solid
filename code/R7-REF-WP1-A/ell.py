import sympy as sp
from sympy.physics.hydrogen import R_nl
r,x,y,z=sp.symbols('r x y z',real=True)
for n in [2,3,4]:
    R=R_nl(n,1,r,1)  # a=1
    c=sp.limit(R/r,r,0)        # R ~ c r
    # psi_{n1m} ~ c * r Y_1m ; sum_m |d_z psi(0)|^2 = c^2 * sum_m |d_z (r Y_1m)|^2 = c^2*3/(4pi) (only m=0 contributes, r Y10 = sqrt(3/4pi) z)
    val=sp.simplify(c**2*sp.Rational(3,1)/(4*sp.pi))
    print(n, val, sp.simplify(val/((n**2-1)/(sp.pi*n**5))))
