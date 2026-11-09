"""COMP-PH input generator / runner. All multi-core jobs go through code/run-heavy.sh (lock)."""
import os, subprocess, re, time, json, sys
CODE = "/home/user/dmdd-solid/code/COMP-PH"
WORK = "/root/work/COMP-PH"
HEAVY = "/home/user/dmdd-solid/code/run-heavy.sh"
PSEUDO = "/root/pseudo/sg15"
MASS = dict(Si=28.0855, Ge=72.630, C=12.0107, Ga=69.723, As=74.9216, Li=6.94, F=18.9984, Na=22.98977, Al=26.98154, O=15.999)
PP = {e: f"{e}_ONCV_PBE-1.2.upf" for e in MASS}

# structures: ibrav, celldm/a, atoms (crystal coords)
STRUCT = {
 'Si':   dict(ibrav=2, species=['Si'], atoms=[('Si',0,0,0),('Si',.25,.25,.25)]),
 'Ge':   dict(ibrav=2, species=['Ge'], atoms=[('Ge',0,0,0),('Ge',.25,.25,.25)]),
 'C':    dict(ibrav=2, species=['C'],  atoms=[('C',0,0,0),('C',.25,.25,.25)]),
 'SiC':  dict(ibrav=2, species=['Si','C'], atoms=[('Si',0,0,0),('C',.25,.25,.25)]),
 'GaAs': dict(ibrav=2, species=['Ga','As'], atoms=[('Ga',0,0,0),('As',.25,.25,.25)]),
 'LiF':  dict(ibrav=2, species=['Li','F'], atoms=[('Li',0,0,0),('F',.5,.5,.5)]),
 'NaF':  dict(ibrav=2, species=['Na','F'], atoms=[('Na',0,0,0),('F',.5,.5,.5)]),
}

def pw_input(mat, calc, alat, ecut, k, outdir, prefix=None, extra_sys='', extra_ctrl='', kblock=None, nbnd=None, conv='1.0d-12', extra=''):
    s = STRUCT[mat]; prefix = prefix or mat
    sp = '\n'.join(f"  {e} {MASS[e]} {PP[e]}" for e in s['species'])
    at = '\n'.join(f"  {a} {x} {y} {z}" for a,x,y,z in s['atoms'])
    nb = f"\n  nbnd = {nbnd}" if nbnd else ''
    kb = kblock or f"K_POINTS automatic\n  {k} {k} {k} 0 0 0"
    return f"""&control
  calculation='{calc}', prefix='{prefix}', outdir='{outdir}', pseudo_dir='{PSEUDO}', tprnfor=.true., tstress=.true.{extra_ctrl}
/
&system
  ibrav={s['ibrav']}, celldm(1)={alat}, nat={len(s['atoms'])}, ntyp={len(s['species'])}, ecutwfc={ecut}{nb}{extra_sys}
/
&electrons
  conv_thr={conv}, mixing_beta=0.7
/
{extra}ATOMIC_SPECIES
{sp}
ATOMIC_POSITIONS crystal
{at}
{kb}
"""

def run(label, cmd, cwd, log):
    t=time.time()
    with open(log,'w') as f:
        r = subprocess.run([HEAVY, label] + cmd, cwd=cwd, stdout=f, stderr=subprocess.STDOUT)
    return r.returncode, time.time()-t

def pw(label, inp_text, name, cwd, np=4):
    os.makedirs(cwd, exist_ok=True)
    inp = os.path.join(cwd, name+'.in'); open(inp,'w').write(inp_text)
    log = os.path.join(cwd, name+'.out')
    rc, dt = run(label, ['mpirun','-np',str(np),'pw.x','-nk',str(min(np,4)),'-in',inp], cwd, log)
    return log, rc, dt

def etot(log):
    t = open(log).read()
    E = re.findall(r'!\s+total energy\s+=\s+(\S+)', t)
    P = re.findall(r'P=\s*(\S+)', t)
    return (float(E[-1]) if E else None, float(P[-1]) if P else None)
