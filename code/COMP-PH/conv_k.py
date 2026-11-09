import qe, json, sys
A = dict(Si=10.263, Ge=10.692, C=6.741, SiC=8.239, GaAs=10.683, LiF=7.609, NaF=8.757)
m = sys.argv[1]; ec = int(sys.argv[2]); res=[]
for k in [4,6,8,10,12]:
    w = f"{qe.WORK}/{m}/kconv"
    log, rc, dt = qe.pw(f"COMP-PH-{m}-k{k}", qe.pw_input(m,'scf',A[m],ec,k,w), f"scf_k{k}", w)
    E,P = qe.etot(log); res.append((k,E,P,round(dt,1))); print(m,k,E,P,round(dt,1),flush=True)
json.dump(res, open(f"conv/k_{m}.json",'w'), indent=1)
