"""Angular curvature gamma_w(Q) of the lowest TA branch about [100]: w(Q,th) = w0(Q)(1+gamma th^2), tilt in (001) and (011) planes."""
import numpy as np, subprocess, os, sys, json
fc,al=sys.argv[1],float(sys.argv[2]); d=os.path.dirname(fc); tp=2*np.pi/al/0.529177  # 1/A per 2pi/a
env=dict(os.environ,PATH='/root/mamba/envs/qe/bin:'+os.environ['PATH'])
Qs=[0.1,0.2,0.3,0.4,0.5,0.6]; ths=[0,0.02,0.04,0.06]; pl={'(001)':np.array([0,1.,0]),'(011)':np.array([0,1,1.])/np.sqrt(2)}
pts=[]
for p,e in pl.items():
    for Q in Qs:
        for t in ths: pts.append(Q/tp*(np.cos(t)*np.array([1.,0,0])+np.sin(t)*e))
open(f"{d}/gam.in",'w').write(f"&input\n asr='crystal', flfrc='{fc}', flfrq='{d}/gam.freq', q_in_band_form=.false.\n/\n{len(pts)}\n"+''.join(f"{a:.8f} {b:.8f} {c:.8f}\n" for a,b,c in pts))
subprocess.run(['matdyn.x','-in','gam.in'],cwd=d,env=env,stdout=open(f"{d}/gam.out",'w'),check=True)
t=open(f"{d}/gam.freq").read().split('\n'); nb=int(t[0].split('nbnd=')[1].split(',')[0]); tok=' '.join(t[1:]).split()
w=np.array([float(x) for x in tok[:len(pts)*(4+nb)]]).reshape(len(pts),4+nb)[:,4]*0.123984
res={}; i=0; th2=np.array(ths)**2
for p in pl:
    for Q in Qs:
        y=w[i:i+len(ths)]; i+=len(ths); g=np.polyfit(th2,y/y[0]-1,1)[0]; res[f"{p} Q={Q}"]=(round(float(y[0]),3),round(float(g),3))
for k,v in res.items(): print(k,'w0 meV',v[0],'gamma_w',v[1])
json.dump(res,open(f"{d}/gamma.json",'w'),indent=1)
