cd /home/user/dmdd-solid/code/COMP-PH
A=10.3507
python3 chain.py Si phG 60 12 $A G60k12
python3 chain.py Si phG 60 14 $A G60k14
python3 chain.py Si phG 60 14 10.263 G60k14aexp
python3 chain.py Si phgrid 60 8 $A q6 6
python3 chain.py Si phgrid 60 8 10.263 q4aexp 4
python3 chain.py Si phgrid 60 8 10.3507 q8 8
