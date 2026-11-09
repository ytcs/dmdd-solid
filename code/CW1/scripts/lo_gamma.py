"""LE-27: on/off-axis location of the Si LO minimum for the (2bar00) PAER class. Q* = K_pk - q with K_pk = k_c + (2bar00) on the [100] axis;
omega_LO(Q, theta) from the COMP-PH 8^3 DFPT force constants (a_PBE, matdyn.x serial, asr='crystal'); fits omega = w0(Q)(1 + gamma th^2) in the
(001) and (011) tilt planes and evaluates the WP3-v3 dispersive criterion gamma > -(|K|/2|q|) r, r = v_g d_K / w0 (r < 0 for LO).
usage: lo_gamma.py fc out.json  (run in a scratch dir)"""
import numpy as np, subprocess, os, sys, json
fc,out=sys.argv[1],sys.argv[2]; al=10.3507; tp=2*np.pi/al/0.529177
env=dict(os.environ,PATH='/root/mamba/envs/qe/bin:'+os.environ['PATH'])
Qs=[0.03,0.06,0.10,0.15,0.20,0.25]; ths=[0,0.03,0.06]; pl={'001':np.array([0,1.,0]),'011':np.array([0,1,1.])/np.sqrt(2)}
pts=[]
for Q in Qs:
    for p,u in pl.items():
        for t in ths: pts.append((np.cos(t)*np.array([1.,0,0])+np.sin(t)*u)*Q/tp)
open('lo.in','w').write(f"&input\n asr='crystal', flfrc='{fc}', flfrq='lo.freq', q_in_band_form=.false.\n/\n{len(pts)}\n"+'\n'.join(' '.join(f'{x:.8f}' for x in v) for v in pts)+'\n')
subprocess.run(['matdyn.x','-in','lo.in'],env=env,stdout=open('lo.out','w'),check=True)
L=open('lo.freq').read().split('\n')[1:]; vals=[float(x) for l in L for x in l.split()]
w=[];i=0
while i<len(vals):
    i+=4; w.append(vals[i:i+6]); i+=6
w=np.array(w)*0.12398   # cm^-1 -> meV
res={}; k=0
for Q in Qs:
    for p in pl:
        lo=[]
        o=np.sort(w[k])[3:]; d_=np.abs(np.diff(o)); j=0 if d_[0]>d_[1] else 2   # on axis: the non-degenerate optical branch is LO (Delta_2')
        ref=o[j]
        for t in ths:
            oo=np.sort(w[k])[3:]; lo.append(oo[np.argmin(abs(oo-ref))]); ref=lo[-1]; k+=1
        res[f'{Q}_{p}']=dict(w0=lo[0],gamma=float(np.polyfit(np.array(ths)**2,np.array(lo)/lo[0]-1,1)[0]),all=w[k-3].tolist())
json.dump(res,open(out,'w'),indent=1); print(json.dumps({a:(b['w0'],b['gamma']) for a,b in res.items()},indent=1))
