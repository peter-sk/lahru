#!/usr/bin/env python3
from sys import stderr as e, stdin as i, stdout as o
from tqdm import tqdm
from transformers import GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("flax-community/dansk-gpt-wiki")
for line in tqdm(i.readlines(), desc="splitting lines"):
    line = line.strip()
    f = 0
    t = min(20480,len(line))
#    print(f"f = {f}   t = {t} I", file=e)
    tokens = tokenizer.tokenize(line)
    while len(tokens) > 1024:
        t -= 1
        while line[t-2:t] != ". " and t-f > 1024:
            t -= 1
        print(f"f = {f}   t = {t} S", file=e)
        tokens = tokenizer.tokenize(line[f:t])
        if len(tokens) <= 1024:
            print(line[f:t],file=o)
            f = t
            t = min(f+20480,len(line))
            print(f"f = {f}   t = {t} N",file=e)
            tokens = tokenizer.tokenize(line[f:t])
    if f < t:
        print(line[f:t],file=o)
