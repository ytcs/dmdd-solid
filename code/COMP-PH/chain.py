"""Per-material chain. usage: python3 chain.py MAT STEP [args]
steps: relax ecut k a0 | scf ecut k a | bands ecut k a nbnd | phG ecut k a tag | phgrid ecut k a nq | q2r nq | matdyn nq"""
import qe, sys, os, re, json, subprocess, time
m, step = sys.argv[1], sys.argv[2]; a = sys.argv[3:]
W = f"{qe.WORK}/{m}"; os.makedirs(W, exist_ok=True)
REC = f"{qe.CODE}/conv/chain_{m}.log"
def rec(*x):
    open(REC,'a').write(' '.join(str(y) for y in x)+'\n'); print(*x, flush=True)

if step == 'relax':
    ec,k,a0 = int(a[0]),int(a[1]),float(a[2])
    w=f"{W}/relax"
    txt = qe.pw_input(m,'vc-relax',a0,ec,k,w,extra='&ions\n/\n&cell\n  press_conv_thr=0.05\n/\n',conv='1.0d-12')
    txt = txt.replace("tstress=.true.","tstress=.true., etot_conv_thr=1d-7, forc_conv_thr=1d-5")
    log,rc,dt = qe.pw(f"COMP-PH-{m}-relax", txt, 'vcrelax', w)
    t=open(log).read()
    cd = re.findall(r'CELL_PARAMETERS \(alat=\s*(\S+)\)\n\s*(\S+)', t)
    alat=float(cd[-1][0]); a1=abs(float(cd[-1][1]))
    anew = alat*a1*2  # ibrav=2: a1=(-1/2,0,1/2)
    rec('relax', m, 'ecut',ec,'k',k,'a_bohr',round(anew,4),'a_A',round(anew*0.529177,4),'P', re.findall(r'P=\s*(\S+)',t)[-1], 'wall',round(dt,1))
elif step == 'scf':
    ec,k,al = int(a[0]),int(a[1]),float(a[2])
    log,rc,dt = qe.pw(f"COMP-PH-{m}-scf", qe.pw_input(m,'scf',al,ec,k,f"{W}/tmp"), 'scf', W)
    E,P=qe.etot(log); t=open(log).read()
    rec('scf',m,ec,k,al,'E',E,'P',P,re.findall(r'(highest.*)\n',t)[-1].strip(),'wall',round(dt,1))
elif step == 'bands':
    ec,k,al,nb = int(a[0]),int(a[1]),float(a[2]),int(a[3])
    # path L-G-X-W-K-G in tpiba (ibrav=2)
    kb = "K_POINTS tpiba_b\n6\n 0.5 0.5 0.5 40\n 0 0 0 50\n 1 0 0 20\n 1 0.5 0 15\n 0.75 0.75 0 45\n 0 0 0 1\n"
    log,rc,dt = qe.pw(f"COMP-PH-{m}-bands", qe.pw_input(m,'bands',al,ec,k,f"{W}/tmp",kblock=kb,nbnd=nb), 'bands', W)
    rec('bands',m,'rc',rc,'wall',round(dt,1))
elif step in ('phG','phgrid'):
    ec,k,al = int(a[0]),int(a[1]),float(a[2])
    tag = a[3]
    w = f"{W}/ph_{tag}"
    log,rc,dt = qe.pw(f"COMP-PH-{m}-scf-{tag}", qe.pw_input(m,'scf',al,ec,k,w), 'scf', w)
    if step=='phG':
        inp = f"&inputph\n  prefix='{m}', outdir='{w}', fildyn='{m}.dynG', tr2_ph=1.0d-16, epsil=.true.\n/\n0.0 0.0 0.0\n"
    else:
        nq=int(a[4])
        inp = f"&inputph\n  prefix='{m}', outdir='{w}', fildyn='{m}.dyn', tr2_ph=1.0d-16, ldisp=.true., nq1={nq}, nq2={nq}, nq3={nq}\n/\n"
    open(f"{w}/ph.in",'w').write(inp)
    t0=time.time()
    rc2,dt2 = qe.run(f"COMP-PH-{m}-{step}-{tag}", ['mpirun','-np','4','ph.x','-nk','4','-in',f"{w}/ph.in"], w, f"{w}/ph.out")
    rec(step,m,tag,'ecut',ec,'k',k,'a',al,'rc',rc2,'wall_ph',round(dt2,1))
