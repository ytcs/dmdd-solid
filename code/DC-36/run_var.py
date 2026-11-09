"""Variations at fixed u: isolated bodies (no nesting), fully diffuse faces, closed Invar can (parametric: R=90 mm, H=90 mm, rho=8.0)."""
import numpy as np, micro as M
us=[100.,200.,300.,400.,600.,1000.]
HOUS=dict(R=90.,H=90.,rho=8.0)
rows=[]
for u in us:
    r=[u]
    a,e,_,_=M.harmonic(M.SUEP,u,N=1000000,nth=4,seed=int(u)+1); r+=[a[0],a[1],a[1]-a[0]]
    a0,_,_,_=M.harmonic(M.SUEP[:1],u,N=1000000,nth=4,seed=int(u)+2); a1,_,_,_=M.harmonic(M.SUEP[1:],u,N=1000000,nth=4,seed=int(u)+3); r+=[a0[0],a1[0],a1[0]-a0[0]]
    a,e,_,_=M.harmonic(M.SUEP,u,N=1000000,nth=4,seed=int(u)+4,diffuse=1.); r+=[a[0],a[1],a[1]-a[0]]
    a,e,_,_=M.harmonic(M.SUEP,u,N=3000000,nth=4,seed=int(u)+5,housing=HOUS); r+=[a[0],a[1],a[1]-a[0],np.hypot(e[0],e[1])]
    rows.append(r); print(' '.join('%.4g'%x for x in r),flush=True)
np.savetxt('results/force_variations.csv',rows,delimiter=',',header='u,nested a_in,a_out,Da, isolated a_in,a_out,Da, diffuse a_in,a_out,Da, can a_in,a_out,Da,err')
