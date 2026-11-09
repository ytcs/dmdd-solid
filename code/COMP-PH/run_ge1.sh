cd /home/user/dmdd-solid/code/COMP-PH
python3 -c "
import qe,re
w=qe.WORK+'/Ge/gapcheck'
for a in [10.692]:
    log,rc,dt=qe.pw('COMP-PH-Ge-gapscf',qe.pw_input('Ge','scf',a,80,10,w,nbnd=20),'scf',w)
    kb='K_POINTS tpiba\n3\n 0 0 0 1\n 0.5 0.5 0.5 1\n 1 0 0 1\n'
    log,rc,dt=qe.pw('COMP-PH-Ge-gapnscf',qe.pw_input('Ge','bands',a,80,10,w,kblock=kb,nbnd=20),'bands',w)
    print(open(log).read().split('End of band structure calculation')[1][:3000])
"
