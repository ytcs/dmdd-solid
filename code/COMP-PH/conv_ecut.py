import qe, json, sys
A = dict(Si=10.263, Ge=10.692, C=6.741, SiC=8.239, GaAs=10.683, LiF=7.609, NaF=8.757)
res = {}
for m in sys.argv[1:]:
    res[m] = []
    for ec in [30,40,50,60,70,80,90,100,120]:
        w = f"{qe.WORK}/{m}/ecut"
        log, rc, dt = qe.pw(f"COMP-PH-{m}-ecut{ec}", qe.pw_input(m,'scf',A[m],ec,8,w), f"scf_{ec}", w)
        E,P = qe.etot(log); res[m].append((ec,E,P,round(dt,1)))
        print(m, ec, E, P, round(dt,1), flush=True)
json.dump(res, open(f"conv_ecut_{'_'.join(sys.argv[1:])}.json",'w'), indent=1)
