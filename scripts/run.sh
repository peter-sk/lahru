#!/bin/bash
CUDA_VISIBLE_DEVICES=0,1,2,3 NCCL_BUFFSIZE=16777216 NCCL_DEBUG=INFO NCCL_P2P_LEVEL=NVL NCCL_SOCKET_IFNAME=eth0 OMP_NUM_THREADS=4 torchrun --standalone --nproc_per_node=4 --nnodes=2 --node_rank=0 --master_addr=10.42.18.19 --master_port=1234 train.py --model gpt2-da-large --epochs 50 --steps 100 large
