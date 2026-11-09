import numpy as np
I2=np.eye(2);Z=np.zeros((2,2))
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.array([[1,0],[0,-1]])
g0=np.block([[I2,Z],[Z,-I2]]).astype(complex)
gs=[np.block([[Z,s],[-s,Z]]).astype(complex) for s in (sx,sy,sz)]
G=[g0]+gs; g5=1j*G[0]@G[1]@G[2]@G[3]
eta=np.diag([1,-1,-1,-1.])
def sl(p): return sum(eta[m,m]*p[m]*G[m] for m in range(4))
def bar(M): return g0@M.conj().T@g0
me=1.0
def rate(ma,kind):
    p=np.array([me,0,0,0.]);k=np.array([ma,0,0,0.])
    w=ma*(ma+2*me)/(2*(ma+me)); kp=np.array([w,0,0,w]); pp=p+k-kp
    s=(ma+me)**2; u=me**2-2*me*w
    P1=(sl(p+k)+me*np.eye(4))/(s-me**2); P2=(sl(p-kp)+me*np.eye(4))/(u-me**2)
    tot=0
    if kind=='V':
        for mu in range(4):
            for nu in range(4):
                Gam=G[nu]@P1@G[mu]+G[mu]@P2@G[nu]
                tot+=eta[mu,mu]*eta[nu,nu]*np.trace((sl(pp)+me*np.eye(4))@Gam@(sl(p)+me*np.eye(4))@bar(Gam))
        avg=tot.real/3/2   # e^4 zeta^2 =1
    else:
        for nu in range(4):
            Gam=G[nu]@P1@g5+g5@P2@G[nu]
            tot+=-eta[nu,nu]*np.trace((sl(pp)+me*np.eye(4))@Gam@(sl(p)+me*np.eye(4))@bar(Gam))
        avg=tot.real/2     # e^2 g^2 =1
    # sum over photon pols: -g_{nu nu'}; for V also -g_{mu mu'}: product (+1)eta eta
    Gam_rate=avg*w/(32*np.pi*ma*me*(ma+me))
    return avg,Gam_rate,w
for x in [0.01,0.1957,1,5]:
    aV,GV,w=rate(x,'V'); aA,GA,_=rate(x,'A')
    bookV=1/(24*np.pi*me**2)*(x+2)*(x**2+2*x+2)/(x+1)**3
    bookA=1/(16*np.pi)*x**2*(x+2)/(x+1)**3
    pubA=1/(16*np.pi)*x**2*(x+2)**2/(x+1)**4
    MV=4/3*(x**2+2*x+2)/(x+1)
    print(f"x={x}: |M|^2V avg={aV:.6g} book={MV:.6g} ; GV/book={GV/bookV:.6f} ; GA/book={GA/bookA:.6f} GA/pub={GA/pubA:.6f} ; GammaV(16pi form)/exact={aV*w/(16*np.pi*x*(x+1))/GV:.3f}")
print('--- ALP |M|^2 vs Hochberg Eq.(15)')
for x in [0.01,0.1957,1,5]:
    aA,GA,w=rate(x,'A'); me=1; ma=x; om=ma; wp=w
    h15=ma**2/4*((ma**4-4*ma**2*me**2+4*me**2*om**2)/(me*wp*(ma**2+2*me*om))+ma**2/wp**2+4*ma**2*me**2/(ma**2+2*me*om)**2+(4*me*wp-8*me*om)/(ma**2+2*me*om))
    print(x,aA,h15,aA/h15)
print('--- normalization check vs Eq.(9) and Eq.(15)/m_a^2')
for x in [0.01,0.1957,1,5]:
    aV,_,w=rate(x,'V'); aA,_,_=rate(x,'A'); me=1; m=x; om=m; wp=w
    h9=1/6*((2*me**2+m**2)/wp**2*0+ (2*me**2+m**2)/wp**2 + 4*me*wp/(2*me*om+m**2) + 4*(2*me**2+m**2)*(me**2+2*me*om+m**2)/(2*me*om+m**2)**2 + (m**4+4*me**2*(om**2-m**2)-8*me**3*(om+me))/(me*wp*(2*me*om+m**2)))
    h15=1/4*((m**4-4*m**2*me**2+4*me**2*om**2)/(me*wp*(m**2+2*me*om))+m**2/wp**2+4*m**2*me**2/(m**2+2*me*om)**2+(4*me*wp-8*me*om)/(m**2+2*me*om))
    print(x, 'V mine/Eq9',aV/h9, ' A mine/Eq15',aA/h15)
