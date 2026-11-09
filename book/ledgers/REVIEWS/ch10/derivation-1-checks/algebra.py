import sympy as sp
# D.30 longitudinal collection
vL,w,q,D,Snn=sp.symbols('v_L omega q Delta S_nn')
expr=(vL**2 - 2*vL*(w/q) + (w/q)**2)*Snn
print('D30 longitudinal:', sp.simplify(expr.subs(vL,(w+D)/q) - (D/q)**2*Snn))
# 10.9 ratio expansion
me,M,om=sp.symbols('m_e m omega',positive=True); qq=M-om
r=qq*(2*me*M*(2*me+M)-2*me**2*qq-qq**2*(2*me+M))/(2*me**2*M**2)
ser=sp.series(r.subs(me,1/sp.Symbol('e')),sp.Symbol('e'),0,2).removeO()
print('10.9 ratio O(1):',sp.factor(ser.coeff(sp.Symbol('e'),0)),' O(1/m_e):',sp.factor(ser.coeff(sp.Symbol('e'),1)))
# vector contraction (1+w/q)^2 with q=M-w
print('(1+w/q)^2 - (M/q)^2 =',sp.simplify((1+om/qq)**2-(M/qq)**2))
# Elliott matching and threshold
a,Eb,mu,Dl,n,eps=sp.symbols('a E_b mu Delta n epsilon',positive=True)
twomu32=1/(a**3*Eb**sp.Rational(3,2))
xi=sp.sqrt(Eb/Dl); cont=twomu32*sp.sqrt(Dl)/(4*sp.pi**2)*2*sp.pi*xi/(1-sp.exp(-2*sp.pi*xi))
print('continuum at edge:',sp.simplify(sp.limit(cont,Dl,0,'+')),' line density:',sp.simplify((1/(sp.pi*a**3*n**3))/(2*Eb/n**3)))
thr=sp.solve(sp.Eq(sp.zeta(3)/(sp.pi*a**3), twomu32*eps**sp.Rational(3,2)/(6*sp.pi**2)),eps)[0]
print('threshold eps/E_b =',sp.N(sp.simplify(thr/Eb)))
print('Fermi factor at 10 E_b:',sp.N((2*sp.pi*xi/(1-sp.exp(-2*sp.pi*xi))).subs(Dl,10*Eb)),' at 6.8 E_b:',sp.N((2*sp.pi*xi/(1-sp.exp(-2*sp.pi*xi))).subs(Dl,6.8*Eb)))
# hydrogen R_n1 small r and p-state weight
r_,aa=sp.symbols('r a',positive=True)
for N in [2,3,4]:
    R=sp.assoc_laguerre(N-2,3,2*r_/(N*aa))  # unnormalized; use sympy hydrogen
    Rn1=sp.physics.hydrogen.R_nl(N,1,r_,1/aa) if False else None
from sympy.physics.hydrogen import R_nl
for N in [2,3,4]:
    c=sp.limit(R_nl(N,1,r_,1)/r_,r_,0)   # a=1 (Z=1, Bohr radius 1)
    print('R_n1 coeff n=',N, sp.nsimplify(c), ' formula', sp.Rational(2,3)*sp.sqrt(sp.Rational(N**2-1,N**5)), ' equal:', sp.simplify(c-sp.Rational(2,3)*sp.sqrt(sp.Rational(N**2-1,N**5)))==0)
C2=(sp.Rational(4,9))*(n**2-1)/(n**5*a**5)
print('|g.gradF|^2/|g|^2 =',sp.simplify(C2*sp.Rational(3,4)/sp.pi))
print('2p vs 1s ratio factor (n=2):',sp.simplify((C2*sp.Rational(3,4)/sp.pi).subs(n,2)/(1/(sp.pi*a**3))))
# 10.5-res single oscillator
E0,C,wv=sp.symbols('E_0 C w',positive=True)
full=C*wv*(1/(E0-om)+1/(E0+om)); res=C*wv/(E0-om)
print('res/full:',sp.simplify(res/full))
print('omega->0 L overstatement:',sp.simplify(((1+ (sp.Symbol('e1')-1))/(1+(sp.Symbol('e1')-1)/2))**2))
# 10.5-coupling
De,K,rho=sp.symbols('Delta K rho',positive=True)
Om2=sp.expand((De+K)**2-K**2); print('Omega^2:',sp.factor(Om2),' series:',sp.series(sp.sqrt(Om2),K,0,3))
chi0=-2*rho**2/De; chi=sp.simplify(chi0/(1-K*chi0/rho**2)); print('coupled static:',chi,' ratio TD/full:',sp.simplify((-2*rho**2/(De+K))/chi))
# Hoelder exponents
nn=sp.symbols('n'); rr=2/(1+nn); ss=2/(1-nn); print('1/r+1/s =',sp.simplify(1/rr+1/ss),' powers:',sp.simplify(rr*(1+nn)/2),sp.simplify(ss*(1-nn)/2))
# 10.3 pole slope and Z_L
x_,wp,vF,Q=sp.symbols('x omega_p v_F q',positive=True)
e1=1-wp**2/om**2*(1+sp.Rational(3,5)*Q**2*vF**2/om**2)
d=sp.diff(e1,om); X=sp.Rational(3,5)*Q**2*vF**2/om**2
print('slope check:',sp.simplify(d-2*wp**2/om**3*(1+2*X)))
# band half width
rv=sp.symbols('r',positive=True); print('2sqrt r/(1+r)=0.1 roots:',[sp.N(s) for s in sp.solve(sp.Eq(2*sp.sqrt(rv),sp.Rational(1,10)*(1+rv)),rv)], ' (sqrt r+1)^2=1.1:',sp.N(sp.solve(sp.Eq((sp.sqrt(rv)+1)**2,sp.Rational(11,10)),rv)[0]))
print('(sqrt(25.3)-1)^2 =',sp.N((sp.sqrt(sp.Rational(253,10))-1)**2))
