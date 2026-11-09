"""Write FORMULATED small-cell Gamma-DFPT (+4^3 q grid for sound speeds) inputs in the qe-rtsc rtsc/bench layout
(@PSEUDO@ placeholder, outdir './', stages scf -> ph as rtsc/bench/run-fork.sh / phq.sh; nscf/epw stages not used)."""
import os
M=dict(Si=28.0855,C=12.0107,Ga=69.723,As=74.9216,Li=6.94,F=18.9984,Na=22.98977,Al=26.98154,O=15.999)
fcc=lambda a,s1,s2,p2: dict(ibrav=2,cd=f"celldm(1) = {a}",sp=[s1,s2],at=[(s1,0,0,0),(s2,)+p2],k=10)
S={
 'C':      dict(fcc(6.741,'C','C',(.25,.25,.25)),ecut=100,ntyp=1),
 'SiC-3C': dict(fcc(8.239,'Si','C',(.25,.25,.25)),ecut=90),
 'GaAs':   dict(fcc(10.683,'Ga','As',(.25,.25,.25)),ecut=140),
 'LiF':    dict(fcc(7.609,'Li','F',(.5,.5,.5)),ecut=90),
 'NaF':    dict(fcc(8.757,'Na','F',(.5,.5,.5)),ecut=90),
 'SiC-4H': dict(ibrav=4,cd="celldm(1) = 5.8071, celldm(3) = 3.2714",sp=['Si','C'],ecut=90,k=8,
    at=[('Si',0,0,0),('Si',1/3,2/3,.25),('Si',0,0,.5),('Si',2/3,1/3,.75),('C',0,0,.1875),('C',1/3,2/3,.4375),('C',0,0,.6875),('C',2/3,1/3,.9375)]),
 'Al2O3':  dict(ibrav=5,cd="celldm(1) = 9.6905, celldm(4) = 0.5697",sp=['Al','O'],ecut=100,k=6,
    at=[('Al',.3520,.3520,.3520),('Al',.6480,.6480,.6480),('Al',.8520,.8520,.8520),('Al',.1480,.1480,.1480),
        ('O',.5560,-.0560,.25),('O',-.0560,.25,.5560),('O',.25,.5560,-.0560),('O',.4440,1.0560,.75),('O',1.0560,.75,.4440),('O',.75,.4440,1.0560)]),
}
root='formulated'
for name,s in S.items():
    d=f"{root}/{name}"; os.makedirs(d,exist_ok=True); pre=name.replace('-','')
    sp=sorted(set(s['sp']),key=s['sp'].index)
    spec=''.join(f" {e} {M[e]} {e}_ONCV_PBE-1.2.upf\n" for e in sp)
    at=''.join(f" {a} {x:.6f} {y:.6f} {z:.6f}\n" for a,x,y,z in s['at'])
    k=s['k']
    for calc in ('vc-relax','scf'):
        txt=f"""&control
    calculation = '{calc}'
    prefix = '{pre}'
    pseudo_dir = '@PSEUDO@'
    outdir = './'
    tstress = .true.
    tprnfor = .true.
/
&system
    ibrav = {s['ibrav']}
    {s['cd']}
    nat = {len(s['at'])}
    ntyp = {len(sp)}
    ecutwfc = {s['ecut']}
/
&electrons
    conv_thr = 1.0d-12
    mixing_beta = 0.7
/
{"&ions\n/\n&cell\n    press_conv_thr = 0.05\n/\n" if calc=='vc-relax' else ''}ATOMIC_SPECIES
{spec}ATOMIC_POSITIONS crystal
{at}K_POINTS automatic
{k} {k} {k if s['ibrav']==2 else (k//3 if s['ibrav']==4 else k)} 0 0 0
"""
        open(f"{d}/{'relax' if calc=='vc-relax' else 'scf'}.in",'w').write(txt)
    am=''.join(f"  amass({i+1}) = {M[e]}\n" for i,e in enumerate(sp))
    open(f"{d}/ph.in",'w').write(f"&inputph\n  prefix = '{pre}'\n  fildyn = '{pre}.dyn'\n{am}  outdir = './'\n  ldisp = .true.\n  nq1 = 4, nq2 = 4, nq3 = {4 if s['ibrav']==2 else (2 if s['ibrav']==4 else 4)}\n  tr2_ph = 1.0d-16\n  reduce_io = .true.\n/\n")
    open(f"{d}/phG.in",'w').write(f"&inputph\n  prefix = '{pre}'\n  fildyn = '{pre}.dynG'\n{am}  outdir = './'\n  epsil = .true.\n  tr2_ph = 1.0d-16\n/\n0.0 0.0 0.0\n")
    open(f"{d}/q2r.in",'w').write(f"&input\n  fildyn = '{pre}.dyn', zasr = 'crystal', flfrc = '{pre}.fc'\n/\n")
    open(f"{d}/matdyn.in",'w').write(f"&input\n  asr = 'crystal', flfrc = '{pre}.fc', flfrq = '{pre}.slopes.freq', q_in_band_form = .false.\n/\n"
        "6\n 0.02 0 0\n 0.04 0 0\n 0.02 0.02 0\n 0.04 0.04 0\n 0.02 0.02 0.02\n 0.04 0.04 0.04\n")
print('written')
