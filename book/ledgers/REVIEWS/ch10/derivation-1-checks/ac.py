import numpy as np
exec(open('elf.py').read().split("for m in [1e6")[0])
OP2=0.5133**2; cLA=8.43/299792.458; m=1e6
for q in [500,1000,2000]:
    w=np.linspace(1e-3,q*(vesc+ve),200000); mx=np.max(w*eta(w/q+q/(2*m)))
    st=np.interp(q,Qg,d['step_lf'])
    r=OP2*eta(np.array([cLA+q/(2*m)]))[0]/(cLA*q*mx*st)
    print(q,r)
