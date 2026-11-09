import sympy as sp
q,Z,e,ne,neR,nk,me,M,D=sp.symbols('q Z e n_e n_eR n_k m_e M Dn',positive=True)
M3_WP0 = -q**2*Z*e**2*nk*(neR+2*ne)/(3*me*M)          # WP0-v3 (4.7')
k3 = q**2/(2*M**2)*Z*e**2*neR/3                          # WP2-v3 (5.2')
J8 = -2*nk*(M/me)*k3*(1+2*ne/neR)                        # WP3-v3 J8(ii)
print('J8 - WP0:', sp.simplify(J8-M3_WP0))
WP2 = nk*q**2*Z*e**2*(neR+2*ne)/(3*M**2)                 # WP2 (5.2'') at q->0+
print('WP2 - (-(me/M)M3):', sp.simplify(WP2-(-(me/M)*M3_WP0)))
C26c = -(me/M)*M3_WP0/(2*nk)*neR/(neR+2*ne)
print('C26c - k3:', sp.simplify(C26c-k3))
# window numbers
c=299792.458; v=794.5/c; me_eV=510998.95
def mmin(E): return 2*E*1e-6/v**2
print('floors', mmin(1.170), mmin(0.744), 'Ex replica Si', mmin(1.1553+0.0135),'cont', mmin(1.170+0.0135), 'ZB TA',mmin(1.188))
# WP1 [E13] Si G=0 parabolic
keV=1e3
for name,Q0,Mx,Ex in [('Si G0',1.94e3,1.19*me_eV,1.1553),('Si G0 Mx1.41',1.94e3,1.41*me_eV,1.1553),('Ge L',1.90e3,2.09*me_eV,0.7399)]:
    Q=(2*Mx*Ex+Q0**2)/(Mx*v+Q0); E=Ex+(Q0-Q)**2/(2*Mx); m=Q**2/(2*(Q*v-E))
    print(name,'Q=%.3f keV m=%.4f MeV'%(Q/1e3,m/1e6))
import math
for mx in [1.19,1.41]:
    Qw=math.sqrt(2*mx*me_eV*0.3); print('Qw',mx,Qw*0.5068e-3,'A^-1')
for w in [0.023,0.025]:
    print('Ge xR=1 q keV',math.sqrt(2*72.63*931.494e6*w)/1e3)
print('PAER prior',0.85*math.exp(-0.75),0.85*math.exp(0.75))
