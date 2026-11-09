"""Write QE inputs for CW1 (Si, a_exp = 10.2631 bohr, SG15 Si_ONCV_PBE-1.2, PBE). usage: mk.py ecut stage"""
import sys, numpy as np
ecut, stage = sys.argv[1], sys.argv[2]
head = lambda calc, nb, extra='': f"""&control
  calculation='{calc}', prefix='si', outdir='./out{ecut}', pseudo_dir='/root/pseudo/sg15'
/
&system
  ibrav=2, celldm(1)=10.2631, nat=2, ntyp=1, ecutwfc={ecut}, nbnd={nb}{extra}
/
&electrons
  conv_thr=1d-12, diago_full_acc=.true.
/
ATOMIC_SPECIES
Si 28.0855 Si_ONCV_PBE-1.2.upf
ATOMIC_POSITIONS alat
Si 0.00 0.00 0.00
Si 0.25 0.25 0.25
"""
if stage == 'scf':
    print(head('scf', 8) + "K_POINTS automatic\n8 8 8 0 0 0")
    sys.exit()
ks = [k for k in open(sys.argv[3]).read().split('\n') if k.strip()]
print(head('nscf', int(sys.argv[4]), ', nosym=.true., noinv=.true.') + f"K_POINTS tpiba\n{len(ks)}\n" + '\n'.join(k + ' 1' for k in ks))
