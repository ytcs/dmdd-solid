cd /home/user/dmdd-solid/code/COMP-PH
python3 wan.py Si 60 10.3507 14 16 0 4.0 > /root/work/COMP-PH/wan14.log 2>&1
python3 chain.py Ge phgrid 80 8 10.692 q4 4
python3 chain.py Ge phG 80 10 10.692 G80k10
python3 chain.py Ge phgrid 80 8 10.692 q6 6
