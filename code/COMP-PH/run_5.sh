cd /home/user/dmdd-solid/code/COMP-PH
until ! pgrep -f "run_4.sh" >/dev/null; do sleep 20; done
python3 chain.py Ge phG 80 10 10.692 G80k10
python3 chain.py Ge phgrid 80 8 10.692 q4 4
python3 chain.py Ge phgrid 80 8 10.692 q6 6
