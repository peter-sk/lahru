#!/usr/bin/env python
import bz2
from json import loads
from sys import argv
from tqdm import tqdm
from transformers import AutoModel, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2-xl")
args = argv[1:]
if args:
    fs = [(arg,bz2.open(arg)) for arg in args]
    def iterator(fs):
        for n, f in tqdm(fs, desc="Processing corpora"):
            for line in tqdm(f, desc="Processing courpus "+n):
                yield loads(line)["text"]
    tokenizer = tokenizer.train_new_from_iterator(iterator(fs), tokenizer.vocab_size)
    tokenizer.save_pretrained("gpt2-xl-da")
model = AutoModel.from_pretrained("gpt2-xl")
model.save_pretrained("gpt2-xl-da")