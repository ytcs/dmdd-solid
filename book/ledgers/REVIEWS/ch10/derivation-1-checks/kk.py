import numpy as np
d=np.load('/home/user/dmdd-solid/book/figscripts/ch10/si_elf_binned.npz')
W,Q,e2=d['omega'],d['q'],d['e2lf']; step=d['step_lf']
wf=np.linspace(1e-4,W[-1],20001)
def eps1(i,w,res=False):
    y=np.interp(wf,W,e2[:,i])
    if res:
        den=wf-w; 
    else:
        den=(wf**2-w**2)/wf
    # principal value: subtract singular part
    if w>0:
        yw=np.interp(w,W,e2[:,i]) if not res else np.interp(w,W,e2[:,i])
        if res:
            I=np.trapezoid((y-yw)/den,wf)+yw*np.log(abs((wf[-1]-w)/(wf[0]-w)))
            return 1+I/np.pi
        else:
            g=y*wf/(wf+w); gw=np.interp(w,W,e2[:,i])*w/(2*w)
            I=np.trapezoid((g-gw)/(wf-w),wf)+gw*np.log(abs((wf[-1]-w)/(wf[0]-w)))
            return 1+2/np.pi*I
    return 1+2/np.pi*np.trapezoid(y/wf,wf)
q0=3728.9
for qq in [493,1390,q0,6700,8000]:
    i=np.argmin(abs(Q-qq)); e0=eps1(i,0); est=1/(1-step[i])
    for w in [1.3]:
        a=eps1(i,w); b=eps1(i,w,True); e2w=np.interp(w,W,e2[:,i])
        print(f"q={Q[i]:.0f}: eps(q,0) KK {e0:.3f} table {est:.3f}; w={w}: eps1 {a:.3f} res {b:.3f} L ratio {(a*a+e2w**2)/(b*b+e2w**2):.3f}")
