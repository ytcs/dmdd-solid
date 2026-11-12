import re,numpy as np,subprocess,os
BIN='/root/mamba/envs/qe/bin'; env=dict(os.environ,PATH=BIN+':'+os.environ['PATH'],OMP_NUM_THREADS='1')
ks=np.round(np.arange(0.76,0.921,0.002),4)
s=open('rel_bands.in').read()
s=re.sub(r'K_POINTS tpiba.*',"K_POINTS tpiba\n %d\n"%len(ks)+"\n".join(f" {k:.4f} 0 0 1" for k in ks)+"\n",s,flags=re.S)
s=s.replace('out_rel_nscf','out_rel_fine'); open('fine.in','w').write(s)
os.system('rm -rf out_rel_fine; cp -r out_rel_scf out_rel_fine')
out=subprocess.run(['mpirun','--allow-run-as-root','-np','4','pw.x','-nk','4','-in','fine.in'],capture_output=True,text=True,env=env).stdout
open('fine.out','w').write(out)
blocks=re.findall(r'k =([-\d. ]+)\(.*?\n\n(.*?)\n\n',out,re.S)
cb=np.array([[float(x) for x in re.findall(r'-?\d+\.\d+',b[1])][4] for b in blocks])
a=5.4773/0.529177210903; Ha=27.211386245988
i=int(np.argmin(cb)); print('grid min',ks[i])
# refined min via quartic on +-0.04
for half in (0.01,0.02,0.03,0.04,0.06):
  m=np.abs(ks-ks[i])<=half+1e-9
  kk=ks[m]*2*np.pi/a; ee=cb[m]/Ha
  c2=np.polyfit(kk,ee,2); c4=np.polyfit(kk,ee,4)
  k0=-c2[1]/(2*c2[0])
  # curvature of quartic at its min
  r=np.roots(np.polyder(c4)); r=r[np.isreal(r)].real; k0q=r[np.argmin(np.abs(r-k0))]
  curv=np.polyval(np.polyder(c4,2),k0q)
  print(f'window ±{half}: n={m.sum()} parabola m={1/(2*c2[0]):.4f} kmin={k0*a/2/np.pi:.4f}; quartic m={1/curv:.4f}')
