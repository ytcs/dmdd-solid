v=794.5/299792.458; me=510999.
def opt(Q,Ex,M):
    best=None
    for i in range(4000):
        x=Q*(1-i/4000); D=x*v-Ex-(Q-x)**2/(2*M*me)
        if D<=0: continue
        m=x*x/(2*D)
        if best is None or m<best[0]: best=(m,x)
    return best
for lab,Q,Ex in [('Si G=0',1940.5,1.1553),('Ge G=0',1898.0,0.7399),('Si Umk',3247.0,1.1553)]:
    print(lab,'pinned m=%.4f'%(Q**2/(2*(Q*v-Ex))/1e6),'abs lower 2E/v^2=%.4f'%(2*Ex/v**2/1e6))
    for M in [0.8,1.2,1.5,2.0]:
        m,x=opt(Q,Ex,M); print('  M=%.1f: m_min=%.3f MeV at q=%.0f eV, dq=%.0f eV, E_kin=%.3f eV'%(M,m/1e6,x,Q-x,(Q-x)**2/(2*M*me)))
print('Ge direct E=0.898: 2E/v^2 = %.3f MeV at q=%.0f eV'%(2*0.898/v**2/1e6,2*0.898/v))
print('Si direct E=3.40: %.3f'%(2*3.40/v**2/1e6))
# 2002.06937 log ratio check for fast DM v=0.1, E=16.6 eV
import math
qmin=16.6/0.1; print('log ratio', math.log(5000/qmin)/math.log(1900/qmin), (5/1.9)**2)
