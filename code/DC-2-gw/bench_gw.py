"""DC-2-gw optimisation benchmark: time Yambo G0W0 settings on Ge k 4^3 and report QP shifts. usage: bench_gw.py"""
import re,subprocess,time,os,json
W='/home/ytc/paer-work/work/DC-2-gw/bench/run'; os.chdir(W)
D='/home/ytc/paer-work/mamba/envs/yambod/bin/yambo'; S='/home/ytc/paer-work/mamba/envs/yambo/bin/yambo'
base=open('base.in').read()
def mk(n,bx,bg,ry,term='none'):
    t=base
    t=re.sub(r'(% BndsRnXp\n\s*)1 \| *\d+ \|',rf'\g<1>1 | {bx} |',t)
    t=re.sub(r'(% GbndRnge\n\s*)1 \| *\d+ \|',rf'\g<1>1 | {bg} |',t)
    t=re.sub(r'NGsBlkXp=\s*\d+\s+RL',f'NGsBlkXp= {ry} Ry',t)
    t=re.sub(r'(%QPkrange[^\n]*\n)1\|8\|1\|200\|',r'\g<1>1|8|21|36|',t)
    t=re.sub(r'(% LongDrXp\n)[^\n]*',r'\g<1> 1.000000 | 1.000000 | 1.000000 |',t)
    t=re.sub(r'GTermKind= "none"',f'GTermKind= "{term}"',t)
    open(n+'.in','w').write(t)
V=[('b200r6',200,200,6,'none',D),('b100r6',100,100,6,'none',D),('b100r6BG',100,100,6,'BG',D),('b200r4',200,200,4,'none',D),('b200r6sp',200,200,6,'none',S),('b100x200',100,200,6,'none',D),('b150r6BG',150,150,6,'BG',D)]
env=dict(os.environ,OMP_NUM_THREADS='1')
env['PATH']='/home/ytc/paer-work/mamba/envs/yambod/bin:'+env['PATH']
out={}
for n,bx,bg,ry,term,exe in V:
    mk(n,bx,bg,ry,term); t0=time.time()
    r=subprocess.run(f'mpirun --mca btl self,vader -np 3 {exe} -F {n}.in -J {n}',shell=True,env=env,capture_output=True,text=True)
    dt=time.time()-t0
    q=[f for f in os.listdir('.') if f.startswith('o-'+n) and 'qp' in f]
    E={}
    if q:
        for l in open(q[0]):
            p=l.split()
            if l.startswith('#') or len(p)<4: continue
            E[(int(float(p[0])),int(float(p[1])))]=float(p[2])+float(p[3])
    out[n]=dict(wall=round(dt,1),nE=len(E),E={f'{k[0]}_{k[1]}':v for k,v in E.items()})
    print(n,'wall',round(dt,1),'rc',r.returncode,'nE',len(E),flush=True)
    json.dump(out,open('bench.json','w'),indent=0)
print('BENCH_DONE')
