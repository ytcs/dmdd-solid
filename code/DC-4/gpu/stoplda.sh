#!/usr/bin/env bash
# Stop job.sh when PBE ends, so the pod does not run LDA (LDA runs locally for free).
until grep -q PBE_DONE /root/job.log; do sleep 20; done
ps -eo pid,args | awk '$2=="bash" && $3=="/root/job.sh"{print $1}' | xargs -r kill
sleep 2; pkill -x pw.x
echo "LDA stage stopped $(date -Is)" >> /root/job.log
