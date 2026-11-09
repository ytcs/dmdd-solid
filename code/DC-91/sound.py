"""DC-91: sound speeds (small-q slopes) and omega_max from the 4^3 force constants. Run in code/DC-91/out."""
import re,subprocess,os,numpy as np,json
AB=0.529177; res={}
ref={'C':(17.5,12.8),'SiC-3C':(11.0,8.9),'LiF':(6.5,4.9),'NaF':(6.2,3.3)}
for m in ['C','SiC-3C','LiF','NaF']:
    a=float(re.search(r'celldm\(1\)\s*=\s*([\d.]+)',open(f'{m}/scf.in').read()).group(1))
    fc=[f for f in os.listdir(m) if f.endswith('.fc')][0]
    hdr=lambda o:f"&input\n asr='crystal', flfrc='{fc}', flfrq='{o}', fldos=' ', fleig=' ', q_in_band_form=.false.\n/\n"
    open(f'{m}/s.in','w').write(hdr('s.freq')+"3\n0.02 0 0\n0.02 0.02 0\n0.02 0.02 0.02\n"); subprocess.run(['matdyn.x','-in','s.in'],cwd=m,stdout=open(f'{m}/s.out','w'))
    rd=lambda f,n:np.array([float(x) for x in ' '.join(open(f).read().split('\n')[1:]).split()][:n*10]).reshape(n,10)[:,4:]
    W=rd(f'{m}/s.freq',3); qs=[.02,.02*2**.5,.02*3**.5]; r=[]
    for i,q in enumerate(qs):
        r.append(np.sort(W[i,:3])*2.99792458e10*2*np.pi/(q*2*np.pi/(a*AB*1e-10))/1e3)
    g=np.array([(i,j,k) for i in range(9) for j in range(9) for k in range(9)])/8.
    open(f'{m}/d.in','w').write(hdr('d.freq')+f"{len(g)}\n"+''.join(f"{x:.4f} {y:.4f} {z:.4f}\n" for x,y,z in g)); subprocess.run(['matdyn.x','-in','d.in'],cwd=m,stdout=open(f'{m}/d.out','w'))
    wm=rd(f'{m}/d.freq',len(g)).max()*.123984
    res[m]=dict(v100=r[0].tolist(),v110=r[1].tolist(),v111=r[2].tolist(),w_max_meV=float(wm))
    print(m,'[100]',np.round(r[0],2),'[110]',np.round(r[1],2),'[111]',np.round(r[2],2),'wmax %.1f'%wm,'ref100 LA,TA',ref[m])
    for f in ('d.freq','d.in','d.out','s.in','s.out','s.freq'):
        if os.path.exists(f'{m}/{f}'): os.remove(f'{m}/{f}')
json.dump(res,open('sound.json','w'),indent=1)
