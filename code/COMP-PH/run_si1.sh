set -x
cd /home/user/dmdd-solid/code/COMP-PH
python3 -c "
import qe,json
A=10.263; res=[]
for k in [12,14]:
    w=qe.WORK+'/Si/kconv'
    log,rc,dt=qe.pw(f'COMP-PH-Si-k{k}',qe.pw_input('Si','scf',A,60,k,w),f'scf_k{k}',w)
    print('Si',k,qe.etot(log),round(dt,1),flush=True)
"
python3 chain.py Si relax 60 12 10.263
