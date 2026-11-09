import sympy as sp, itertools
# all 48 O_h matrices; T_d subset = signed perms with det(perm-part)... T_d: elements of O_h that map the tetrahedron {(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)} to itself
mats=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        M=sp.zeros(3)
        for i in range(3): M[i,p[i]]=s[i]
        mats.append(M)
tet=[sp.Matrix(v) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
def inTd(M): return all(any((M*v-w).norm()==0 for w in tet) for v in tet)
tau=sp.Matrix([1,1,1])/4   # atom origin, a=1
x,y,z=sp.symbols('x y z'); X=sp.Matrix([x,y,z])
basis=[y*z,z*x,x*y]  # T2g
def rep(M,f):  # (P_R f)(r)=f(R^-1 r)
    Ri=M.inv(); r=Ri*X
    return sp.expand(f.subs({x:r[0],y:r[1],z:r[2]},simultaneous=True))
def char(M):
    tr=0
    for i,f in enumerate(basis):
        g=rep(M,f); tr+=sp.Poly(g,x,y,z).coeff_monomial(basis[i])
    return tr
qhat=sp.Matrix([1,0,0])
for G in [sp.Matrix([0,0,0]),sp.Matrix([-2,0,0]),sp.Matrix([2,0,0])]:
    tot=0; ops=[M for M in mats if (M*qhat-qhat).norm()==0]
    for M in ops:
        t=sp.zeros(3,1) if inTd(M) else tau
        ph=sp.exp(-sp.I*2*sp.pi*(G.T*t)[0])
        tot+=char(M)*ph
    print("G=",list(G)," #ops",len(ops)," multiplicity of Delta1 in e^{i(q+G)r}Gamma25':",sp.nsimplify(tot/len(ops)))
