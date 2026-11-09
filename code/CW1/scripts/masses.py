"""LE-24/29: Si band masses (PBE, a_exp, 40 Ry, no SOC) from the pass-1 nscf (inputs/k_pass1.txt): k_c and m_l from a parabola through the
7 points around the CBM on [100] (step 0.005), m_t from (0.85, t, 0), t = 0.01-0.03; hole masses from Gamma + d along [100], [110], [111],
d = 0.01-0.03 (2pi/a); E = c k^2 fits (k in bohr^-1, E in Ha => m = 1/(2c)). Writes the raw eigenvalues too. usage: masses.py savedir out.json"""
import numpy as np, sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from eig import read
k,E=read(sys.argv[1]); t=2*np.pi/10.2631; Ha=27.211386; vbm=E[0,3]
ax=slice(1,30); kx=k[ax,0]; ec=E[ax,4]; i=int(np.argmin(ec)); p=np.polyfit(kx[i-3:i+4],ec[i-3:i+4],2)
res=dict(kc=float(-p[1]/(2*p[0])), Eg_PBE=float(np.polyval(p,-p[1]/(2*p[0]))-vbm), m_l=float(t**2/(2*p[0]/Ha)))
e085=E[1+14,4]; tt=np.array([.01,.02,.03]); res['m_t']=float(t**2/(2*np.polyfit(tt**2,E[30:33,4]-e085,1)[0]/Ha))
for j,lab in enumerate(['100','110','111']):
    idx=[33+3*n+j for n in range(3)]
    res['holes_'+lab]=[float(-t**2/(2*np.polyfit(tt**2,E[idx,b]-vbm,1)[0]/Ha)) for b in (1,2,3)]
res['raw']=dict(k=k.tolist(),E=E.tolist())
json.dump(res,open(sys.argv[2],'w')); print({a:b for a,b in res.items() if a!='raw'})
