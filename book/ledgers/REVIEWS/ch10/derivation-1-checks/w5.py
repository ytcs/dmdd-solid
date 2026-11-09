import numpy as np
rng=np.random.default_rng(1)
n=2; Gs=np.array([[i,j,l] for i in range(-n,n+1) for j in range(-n,n+1) for l in range(-n,n+1)],float)*2*np.pi
NG=len(Gs); m=1.0
def build_V(kind):
    V={}
    for a in range(NG):
        for b in range(NG):
            d=tuple(np.round((Gs[a]-Gs[b])/(2*np.pi)).astype(int))
            if d==(0,0,0): continue
            md=tuple(-x for x in d)
            if d in V: continue
            amp=rng.normal()*3
            if kind=='PT':   # real and even: inversion + time reversal
                V[d]=amp; V[md]=amp
            elif kind=='Tonly': # V(-G)=V(G)^*, complex: T but no P
                ph=np.exp(1j*rng.uniform(0,2*np.pi)); V[d]=amp*ph; V[md]=np.conj(amp*ph)
            elif kind=='Ponly': # V(-G)=V(G) complex: P (with complex local? not hermitian generally) -> use nonlocal-free magnetic flux instead
                V[d]=amp; V[md]=amp
    return V
def H(k,V,B=0.0):
    M=np.zeros((NG,NG),complex)
    for a in range(NG):
        p=k+Gs[a]; M[a,a]=p@p/(2*m)
        for b in range(NG):
            if a!=b: M[a,b]=V[tuple(np.round((Gs[a]-Gs[b])/(2*np.pi)).astype(int))]
    return M
def W5(V,k,q,nocc=4):
    e1,c1=np.linalg.eigh(H(k,V)); e2,c2=np.linalg.eigh(H(k+q,V))
    tot=0
    for v in range(nocc):
        for c in range(nocc,NG):
            f=np.vdot(c2[:,c],c1[:,v])
            fv=np.array([np.vdot(c2[:,c],c1[:,v]*(-(k+Gs)[:,ax])/m) for ax in range(3)])
            B5=1j*(q/m)@np.cross(fv,np.conj(fv))*0+1j*(q/m)@np.cross(f*0+fv,np.conj(fv))
            # Catena: B5 = i (q/m).(f_vec x f_vec^*)
            tot+=B5
    return tot
k=np.array([0.31,0.17,0.05])*2*np.pi; q=np.array([0.23,-0.11,0.37])*2*np.pi
for kind in ['PT','Tonly']:
    V=build_V(kind)
    w=W5(V,k,q); wm=W5(V,-k,-q)
    # also size scale
    print(kind,'W5(k,q)=',w,' W5(-k,-q)=',wm)
