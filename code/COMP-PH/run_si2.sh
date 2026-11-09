set -e
cd /home/user/dmdd-solid/code/COMP-PH
A=$(grep "^relax Si" conv/chain_Si.log | tail -1 | awk '{for(i=1;i<=NF;i++) if($i=="a_bohr") print $(i+1)}')
echo "Si a=$A"
python3 chain.py Si scf 60 10 $A
python3 chain.py Si bands 60 10 $A 12
python3 chain.py Si phG 60 10 $A G60
python3 chain.py Si phG 80 10 $A G80
python3 chain.py Si phG 60 8 $A G60k8
python3 chain.py Si phgrid 60 8 $A q4 4
python3 wan.py Si 60 $A 10 16 0 4.0
