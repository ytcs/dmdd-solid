import subprocess, re, numpy as np, os
BIN='/root/mamba/envs/qe/bin'; PS='/root/pseudo/sg15'
env=dict(os.environ, PATH=BIN+':'+os.environ['PATH'], OMP_NUM_THREADS='1')
def pw(name, calc, a_ang, ecut, kblock, nbnd=None, extra=''):
    a_bohr=a_ang/0.529177210903
    inp=f"""&control
 calculation='{calc}', verbosity='high', prefix='si', outdir='./out_{name}', pseudo_dir='{PS}', tprnfor=.true., tstress=.true.
/
&system
 ibrav=2, celldm(1)={a_bohr:.10f}, nat=2, ntyp=1, ecutwfc={ecut}, ecutrho={4*ecut}, occupations='fixed'{', nbnd=%d'%nbnd if nbnd else ''}
/
&electrons
 conv_thr=1.0d-12
/
{extra}
ATOMIC_SPECIES
 Si 28.0855 Si_ONCV_PBE-1.2.upf
ATOMIC_POSITIONS crystal
 Si 0.00 0.00 0.00
 Si 0.25 0.25 0.25
{kblock}
"""
    open(f'{name}.in','w').write(inp)
    out=subprocess.run(['mpirun','--allow-run-as-root','-np','4','pw.x','-nk','2','-in',f'{name}.in'],capture_output=True,text=True,env=env).stdout
    open(f'{name}.out','w').write(out); return out
K12="K_POINTS automatic\n 12 12 12 0 0 0"
# 1. vc-relax at 60 Ry
o=open('relax.out').read()
alat=[float(x) for x in re.findall(r'celldm\(1\)=\s*([\d.]+)',o)]
cells=re.findall(r'CELL_PARAMETERS \(alat=\s*([\d.]+)\)\n\s*([-\d. ]+)\n',o)
a0=float(cells[-1][0]); v=[abs(float(x)) for x in cells[-1][1].split()]
a_rel=2*v[0]*a0*0.529177210903  # fcc: a1=(-1,0,1)/2 * a
print('relaxed a (Angstrom):', round(a_rel,4))
def bands(name,a,ecut):
    pw(name+'_scf','scf',a,ecut,K12)
    # Gamma-X line, steps 0.005 * 2pi/a, in units of 2pi/a (tpiba)
    ks=np.arange(0,1.0+1e-9,0.005)
    kb="K_POINTS tpiba\n %d\n"%len(ks)+"\n".join(f" {k:.4f} 0 0 1" for k in ks)
    os.system(f'rm -rf out_{name}_nscf; cp -r out_{name}_scf out_{name}_nscf')
    inp=open(f'{name}_scf.in').read().replace("calculation='scf'","calculation='bands'").replace(f"out_{name}_scf",f"out_{name}_nscf").replace("occupations='fixed'","occupations='fixed', nbnd=8").replace(K12,kb)
    open(f'{name}_bands.in','w').write(inp)
    out=subprocess.run(['mpirun','--allow-run-as-root','-np','4','pw.x','-nk','4','-in',f'{name}_bands.in'],capture_output=True,text=True,env=env).stdout
    open(f'{name}_bands.out','w').write(out)
    blocks=re.findall(r'k =([-\d. ]+)\(.*?\n\n(.*?)\n\n',out,re.S)
    E=np.array([[float(x) for x in re.findall(r'-?\d+\.\d+',b[1])][:8] for b in blocks])
    vbm=E[0,3]; cb=E[:,4]; i=int(np.argmin(cb))
    Eg=cb[i]-vbm; kc=ks[i]; Edir=E[0,4]-vbm
    # parabola fit, 9 points
    res={}
    for npt in (9,13,17):
        h=npt//2; sl=slice(i-h,i+h+1)
        kk=ks[sl]*2*np.pi/(a/0.529177210903); ee=cb[sl]/27.211386245988
        c=np.polyfit(kk,ee,2); res[npt]=1/(2*c[0])
    return Eg,kc,Edir,res
Eg,kc,Ed,m=bands('rel',a_rel,60)
print(f'PBE at a={a_rel:.4f}: indirect gap {Eg:.4f} eV at k_c={kc:.3f}, direct Gamma gap {Ed:.3f} eV, m_par (9,13,17 pts) '+', '.join(f'{v:.3f}' for v in m.values()))
Eg2,kc2,Ed2,_=bands('meas',5.431,40)
print(f'PBE at a=5.431 (40 Ry): indirect gap {Eg2:.4f} eV at k_c={kc2:.3f}')
