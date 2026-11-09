"""q2r + matdyn: high-symmetry frequencies vs INS, path dispersion. usage: disp.py MAT phdir"""
import sys, os, subprocess, numpy as np, json
m, d = sys.argv[1], sys.argv[2]
env=dict(os.environ,PATH='/root/mamba/envs/qe/bin:'+os.environ['PATH'])
# INS (THz): Nilsson & Nelin, Si PRB 6, 3777 (1972) (296 K); Ge PRB 3, 364 (1971) (80 K). DOIs verified via lit.py; numbers [UNVERIFIED: tabulation as recalled, not re-read from the PDF]
INS={'Si':{'G_O':15.53,'X_TA':4.49,'X_LA':12.32,'X_TO':13.90,'L_TA':3.43,'L_LA':11.35,'L_LO':12.60,'L_TO':14.68},
     'Ge':{'G_O':9.12,'X_TA':2.38,'X_LA':7.14,'X_TO':8.17,'L_TA':1.86,'L_LA':6.63,'L_LO':7.27,'L_TO':8.55}}
open(f"{d}/q2r.in",'w').write(f"&input\n fildyn='{m}.dyn', zasr='crystal', flfrc='{m}.fc'\n/\n")
subprocess.run(['q2r.x','-in','q2r.in'],cwd=d,env=env,stdout=open(f"{d}/q2r.out",'w'),check=True)
pts=[(0,0,0),(1,0,0),(.5,.5,.5)]
open(f"{d}/hs.in",'w').write(f"&input\n asr='crystal', flfrc='{m}.fc', flfrq='hs.freq', q_in_band_form=.false.\n/\n3\n"+''.join(f"{a} {b} {c}\n" for a,b,c in pts))
subprocess.run(['matdyn.x','-in','hs.in'],cwd=d,env=env,stdout=open(f"{d}/hs.out",'w'),check=True)
def rd(f,n):
    t=open(f).read().split('\n'); nb=int(t[0].split('nbnd=')[1].split(',')[0]); tok=' '.join(t[1:]).split()
    return np.array([float(x) for x in tok[:n*(4+nb)]]).reshape(n,4+nb)[:,4:]
w=rd(f"{d}/hs.freq",3)/33.35641   # THz
G,X,L=w
calc={'G_O':G[3],'X_TA':X[0],'X_LA':X[2],'X_TO':X[4],'L_TA':L[0],'L_LA':L[2],'L_LO':L[3],'L_TO':L[4]}
out={k:(float(calc[k]),INS[m][k],float(calc[k]/INS[m][k]-1)) for k in calc}
for k,v in out.items(): print(f"{k}: calc {v[0]:.3f} THz ({v[0]*4.135667:.2f} meV)  INS {v[1]:.2f}  dev {100*v[2]:+.1f}%")
# path G-X-W-K-G-L, 2pi/a
open(f"{d}/path.in",'w').write(f"&input\n asr='crystal', flfrc='{m}.fc', flfrq='path.freq', q_in_band_form=.true.\n/\n6\n0 0 0 60\n1 0 0 30\n1 0.5 0 20\n0.75 0.75 0 60\n0 0 0 50\n0.5 0.5 0.5 1\n")
subprocess.run(['matdyn.x','-in','path.in'],cwd=d,env=env,stdout=open(f"{d}/path.out",'w'),check=True)
json.dump(out,open(f"{d}/hs_vs_INS.json",'w'),indent=1)
