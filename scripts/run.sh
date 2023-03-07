#!/bin/bash
CUDA_VISIBLE_DEVICES=0,1,2,3 NCCL_BUFFSIZE=16777216 NCCL_DEBUG=INFO NCCL_P2P_LEVEL=NVL NCCL_SOCKET_IFNAME=lo OMP_NUM_THREADS=4 torchrun --standalone --nnodes=1 -
-nproc_per_node=4 train.py --model gpt2-da-small --epochs 50 --steps 100 small
