"""DC-93: CsI C11, C12, C44 by strain-stress (CsCl cell, inversion at both sites: no internal relaxation).
usage: elastic.py WORKDIR NP. Writes results.json and a convergence record next to this script."""
import numpy as np, subprocess, re, json, os, sys
W, NP = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
BIN = '/home/ytc/paer-work/mamba/envs/qe/bin'
PS = '/home/ytc/paer-work/pseudo/sg15'
AB = 0.529177210903; RYB3_GPA = 14710.507
M_CS, M_I = 132.90545, 126.90447
def inp(tag, a, F, ecut, k, dft, calc='scf'):
    d = f"input_dft='{dft}'," if dft != 'pbe' else ''
    cell = '\n'.join(' '.join(f'{x:.10f}' for x in r) for r in (a*np.array(F)))
    extra = "&ions\n/\n&cell\n press_conv_thr=0.05\n/\n" if calc == 'vc-relax' else ''
    return f"""&control
 calculation='{calc}', prefix='{tag}', outdir='{W}/tmp_{tag}', pseudo_dir='{PS}', tstress=.true., tprnfor=.true., disk_io='none',
 etot_conv_thr=1d-7, forc_conv_thr=1d-5
/
&system
 ibrav=0, nat=2, ntyp=2, ecutwfc={ecut}, {d}
/
&electrons
 conv_thr=1d-11, mixing_beta=0.5
/
{extra}CELL_PARAMETERS bohr
{cell}
ATOMIC_SPECIES
 Cs {M_CS} Cs_ONCV_PBE-1.2.upf
 I {M_I} I_ONCV_PBE-1.2.upf
ATOMIC_POSITIONS crystal
 Cs 0 0 0
 I .5 .5 .5
K_POINTS automatic
 {k} {k} {k} 1 1 1
"""
def run(tag, txt):
    p = f'{W}/{tag}.in'; open(p, 'w').write(txt); o = f'{W}/{tag}.out'
    if not (os.path.exists(o) and 'JOB DONE' in open(o).read()):
        env = dict(os.environ, OMP_NUM_THREADS='1', PATH=BIN+':'+os.environ['PATH'])
        subprocess.run(['mpirun', '--mca', 'btl', 'self,vader', '-np', NP, 'pw.x', '-in', p], stdout=open(o, 'w'), stderr=subprocess.DEVNULL, env=env, cwd=W)
    return open(o).read()
def stress(t):
    b = t.split('total   stress')[-1].split('\n')[1:4]
    return np.array([[float(x) for x in l.split()[0:3]] for l in b])*RYB3_GPA   # Ry/bohr^3 columns (kbar columns are rounded); printed sign: + = compressive
def etot(t): return float(re.findall(r'!\s+total energy\s+=\s+(\S+)', t)[-1])
def cij(a, ecut, k, dft, tag, eps=(0.005, 0.01)):
    I = np.eye(3); r = {}
    s0 = stress(run(f'{tag}_0', inp(f'{tag}_0', a, I, ecut, k, dft)))
    r['P0_GPa'] = float(np.trace(s0)/3)
    out = []
    for e in eps:
        S = {}
        for sg in (+1, -1):
            n = f"{tag}_x{sg*e:+.3f}"; F = I + np.diag([sg*e, 0, 0])
            S['x', sg] = stress(run(n, inp(n, a, F, ecut, k, dft)))
            n = f"{tag}_s{sg*e:+.3f}"; F = I.copy(); F[1, 2] = F[2, 1] = sg*e/2
            S['s', sg] = stress(run(n, inp(n, a, F, ecut, k, dft)))
        dx = -(S['x', 1]-S['x', -1])/(2*e); ds = -(S['s', 1]-S['s', -1])/(2*e)
        out.append(dict(eps=e, C11=dx[0, 0], C12=(dx[1, 1]+dx[2, 2])/2, C44=ds[1, 2]))
    r['by_eps'] = out
    r.update({c: out[0][c] for c in ('C11', 'C12', 'C44')})
    return r
def sound(C11, C12, C44, a_A):
    rho = (M_CS+M_I)*1.66053907e-27/(a_A*1e-10)**3
    def v(n):
        n = np.array(n, float); n /= np.linalg.norm(n)
        G = np.array([[(C11-C44)*n[i]*n[j]*(i != j and 0 or 0) for j in range(3)] for i in range(3)])
        for i in range(3):
            for j in range(3):
                G[i, j] = (C12+C44)*n[i]*n[j] if i != j else C11*n[i]**2+C44*(1-n[i]**2)
        return np.sqrt(np.linalg.eigvalsh(G)*1e9/rho)/1e3
    B = (C11+2*C12)/3
    return dict(rho_kg_m3=rho, B=B, floor_km_s=float(np.sqrt(B*1e9/rho)/1e3), A_zener=2*C44/(C11-C12),
                v100=v([1, 0, 0]).tolist(), v110=v([1, 1, 0]).tolist(), v111=v([1, 1, 1]).tolist())
A_EXP = 4.567/AB     # RT value [UNVERIFIED secondary]; cond-mat/9408044 Table I quotes 4.56 A
res = {}
# convergence at a_exp, PBE
conv = {}
for ecut, k in ((60, 6), (80, 6), (100, 6), (80, 4), (80, 8)):
    t = run(f'cv{ecut}k{k}', inp(f'cv{ecut}k{k}', A_EXP, np.eye(3), ecut, k, 'pbe'))
    conv[f'{ecut}/{k}'] = dict(E_Ry=etot(t), P_GPa=float(np.trace(stress(t))/3))
res['conv'] = conv; print(conv, flush=True)
ECUT, K = 80, 6
for dft in ('pbe', 'pbesol'):
    t = run(f'{dft}_rx', inp(f'{dft}_rx', A_EXP, np.eye(3), ECUT, K, dft, 'vc-relax'))
    m = re.findall(r'CELL_PARAMETERS \(alat=\s*(\S+)\)\n\s*(\S+)', t)
    arel = float(m[-1][0])*float(m[-1][1]) if m else None
    if not m:
        m = re.findall(r'CELL_PARAMETERS \(bohr\)\n\s*(\S+)', t); arel = float(m[-1])
    res[dft] = dict(a_relaxed_A=arel*AB)
    for lab, a in (('a_relaxed', arel), ('a_exp', A_EXP)):
        r = cij(a, ECUT, K, dft, f'{dft}_{lab}')
        r['sound'] = sound(r['C11'], r['C12'], r['C44'], a*AB)
        res[dft][lab] = r; print(dft, lab, {k: r[k] for k in ('P0_GPa', 'C11', 'C12', 'C44')}, r['sound']['B'], flush=True)
    json.dump(res, open(f'{HERE}/results.json', 'w'), indent=1, default=float)
print('DC93_DONE')
