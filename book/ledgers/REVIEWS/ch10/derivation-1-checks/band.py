import numpy as np
exec(open('elf.py').read().split("for m in [1e6")[0])
m=100e6; Qm,Wm=np.meshgrid(Qg,W)
s=np.trapezoid(Qm**3*eta(Wm/Qm+Qm/(2*m))*d['lf'],Qg,axis=1); s[W<1.11]=0
b=(W>=4.2)&(W<=9.5); print('share 4.2-9.5', np.trapezoid(s*b,W)/np.trapezoid(s,W))
