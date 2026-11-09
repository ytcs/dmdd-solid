"""ERR-CW1 iteration 2 of the local DFT re-minimisation: 3x3x3 stencils (h = 0.02) re-centred at the iteration-1 optimum of each variant
(out/errata_qe.json: k_e + dk_e, k_h + dk_h), plus Gamma and k_c for the gap.  usage: errata_kset2.py errata_qe.json labels1.json variant kfile labels2.json"""
import json, sys, itertools, numpy as np
R=json.load(open(sys.argv[1])); L=json.load(open(sys.argv[2])); v=sys.argv[3]; r=R[v]; h=L['h']
kh=np.array(L['k_h'])+r['dk_h']; ke=np.array(L['k_e'])+r['dk_e']
pts=[('G',[0,0,0]),('kc',[0.8429,0,0]),('axv',[0.052,0,0]),('axc',[0.6609,0,0])]
for s in itertools.product((-1,0,1),repeat=3): pts.append((f'h{s[0]:+d}{s[1]:+d}{s[2]:+d}',list(kh+h*np.array(s))))
for s in itertools.product((-1,0,1),repeat=3): pts.append((f'e{s[0]:+d}{s[1]:+d}{s[2]:+d}',list(ke+h*np.array(s))))
pts+=[('qsv',L['qstar']['k_v']),('qsc',list(np.array(L['qstar']['k_v'])+L['qstar']['q']))]
open(sys.argv[4],'w').write(f"{len(pts)}\n"+'\n'.join(f"{k[0]:.10f} {k[1]:.10f} {k[2]:.10f} 1" for _,k in pts)+'\n')
json.dump(dict(L,labels=[l for l,_ in pts],k_h=kh.tolist(),k_e=ke.tolist()),open(sys.argv[5],'w'),indent=1)
