import numpy as np
exec(open('elf.py').read().split("for m in [1e6")[0])
q0=al*me
m=10e6
Qm,Wm=np.meshgrid(Qg,W)
def spec(key):
    integ=Qm**3*eta(Wm/Qm+Qm/(2*m))*d[key]; s=np.trapezoid(integ,Qg,axis=1); s[W<1.11]=0; return s
for k in ['ip','lf']:
    s=spec(k); print(k,'mean w',np.trapezoid(s*W,W)/np.trapezoid(s,W),' peak',W[np.argmax(s)])
def perq(key):
    integ=Qm**3*eta(Wm/Qm+Qm/(2*m))*d[key]*(Wm>=1.11); return np.trapezoid(integ,W,axis=0)
ip,rp,lf=perq('ip'),perq('rpa'),perq('lf')
for qq in [2000,q0,8000,10000]:
    i=np.argmin(abs(Qg-qq)); print(f"q={Qg[i]:.0f}: head IP/RPA {ip[i]/rp[i]:.3g}  LF RPA/LF {rp[i]/lf[i]:.3g}  step_lf {d['step_lf'][i]:.3f} eps_lf(0) {1/(1-d['step_lf'][i]):.3f} eps_rpa(0) {1/(1-d['step_rpa'][i]):.3f}")
for qq in [500,1000,5000]:
    i=np.argmin(abs(Qg-qq)); print(qq,Qg[i],'step_lf',d['step_lf'][i],'eps00 noLF',1/(1-d['step_rpa'][i]))
i=np.argmin(abs(Qg-q0))
for w in [3,5,10]:
    j=np.argmin(abs(W-w)); print('q0 w',W[j],'ip/L',d['ip'][j,i]/d['lf'][j,i])
print('q0 peaks: ip',W[np.argmax(d['ip'][:,i])],' L',W[np.argmax(d['lf'][:,i])])
i=np.argmin(abs(Qg-10000)); ne=8/Om; fs=np.trapezoid(W*d['lf'][:,i],W)/(np.pi/2*4*np.pi*al*ne/me); print('fsum share <89 eV at 10keV', fs, Qg[i])
