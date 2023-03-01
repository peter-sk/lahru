#!/bin/bash
while /bin/true
do
  (
    date
    echo
    df -h | grep " /$"
    echo
    du -sh ~/.cache gpt2-da-* data/*.jsonl .git 2>/dev/null
    echo
    nvidia-smi | grep 300W
    echo
    top -b -n 1 | grep jps | grep -v " S   0.0" | grep -v " top" | sort -n -k 1
  ) > /tmp/monitor.out
  clear
  cat /tmp/monitor.out
  sleep 5
done
