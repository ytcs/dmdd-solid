"""Wannier sp3 interpolation for Si/Ge. usage: wan.py MAT ecut a nk nbnd excl froz_max_rel(eV above VBM)"""
import qe, sys, os, re, subprocess, numpy as np
m=sys.argv[1]; ec=int(sys.argv[2]); al=float(sys.argv[3]); nk=int(sys.argv[4]); nb=int(sys.argv[5]); excl=int(sys.argv[6]); froz=float(sys.argv[7])
w=f"{qe.WORK}/{m}/wan"; os.makedirs(w,exist_ok=True)
env=dict(os.environ, PATH='/root/mamba/envs/qe/bin:'+os.environ['PATH'], OMP_NUM_THREADS='1')
log,rc,dt=qe.pw(f"COMP-PH-{m}-wscf", qe.pw_input(m,'scf',al,ec,12,w), 'scf', w)
vbm=float(re.findall(r'highest occupied, lowest unoccupied level \(ev\):\s+(\S+)',open(log).read())[-1]) if 'lowest unocc' in open(log).read() else float(re.findall(r'highest occupied level \(ev\):\s+(\S+)',open(log).read())[-1])
ks=[(i/nk,j/nk,l/nk) for i in range(nk) for j in range(nk) for l in range(nk)]
kb="K_POINTS crystal\n%d\n"%len(ks)+''.join(f" {a:.8f} {b:.8f} {c:.8f} 1.0\n" for a,b,c in ks)
txt=qe.pw_input(m,'nscf',al,ec,12,w,kblock=kb,nbnd=nb,extra_sys=", nosym=.true., noinv=.true.",conv='1.0d-10')
txt=txt.replace("&electrons","&electrons\n  diago_full_acc=.true.,")
log,rc,dt2=qe.pw(f"COMP-PH-{m}-wnscf",txt,'nscf',w)
s=qe.STRUCT[m]; el=s['species'][0]
nw=8; nbw=nb-excl
cell=f"{-al/2} 0 {al/2}\n{0} {al/2} {al/2}\n{-al/2} {al/2} 0"
win=f"""num_wann = {nw}
num_bands = {nbw}
{('exclude_bands = 1-%d' % excl) if excl else ''}
dis_win_max = {vbm+froz+8.0}
dis_froz_max = {vbm+froz}
dis_num_iter = 400
num_iter = 200
write_hr = .true.
use_ws_distance = .true.
begin projections
{el}:sp3
end projections
begin unit_cell_cart
bohr
{cell}
end unit_cell_cart
begin atoms_frac
{el} 0 0 0
{el} 0.25 0.25 0.25
end atoms_frac
mp_grid = {nk} {nk} {nk}
begin kpoints
"""+''.join(f"{a:.8f} {b:.8f} {c:.8f}\n" for a,b,c in ks)+"end kpoints\n"
open(f"{w}/{m}.win",'w').write(win)
subprocess.run(['wannier90.x','-pp',m],cwd=w,env=env,check=True)
open(f"{w}/pw2wan.in",'w').write(f"&inputpp\n outdir='{w}', prefix='{m}', seedname='{m}', write_mmn=.true., write_amn=.true., write_unk=.false.\n/\n")
qe.run(f"COMP-PH-{m}-pw2wan",['mpirun','-np','4','pw2wannier90.x','-in',f"{w}/pw2wan.in"],w,f"{w}/pw2wan.out")
subprocess.run(['wannier90.x',m],cwd=w,env=env,check=True)
print('VBM',vbm,'nscf wall',dt2)
