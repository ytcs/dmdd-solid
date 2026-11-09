cd /home/user/dmdd-solid/code/COMP-PH
until grep -q "phgrid Ge q4" conv/chain_Ge.log; do sleep 10; done
python3 chain.py Ge phG 80 10 10.692 G80k10
