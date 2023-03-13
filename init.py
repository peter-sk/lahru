#!/usr/bin/env python
import bz2
from json import loads
from sys import argv
from tqdm import tqdm
from transformers import AutoModel, AutoTokenizer
args = argv[1:]
if args:
    tokenizer = AutoTokenizer.from_pretrained("gpt2-xl")
    fs = [(arg,bz2.open(arg)) for arg in args]
    def iterator(fs):
        for n, f in tqdm(fs, desc="Processing corpora"):
            for line in tqdm(f, desc="Processing courpus "+n):
                yield loads(line)["text"]
    tokenizer = tokenizer.train_new_from_iterator(iterator(fs), tokenizer.vocab_size)
else:
    tokenizer = AutoTokenizer.from_pretrained("gpt2-large-da")
tokenizer.pad_token = '.'
tokenizer.padding_side = 'right'
tokenizer.save_pretrained("gpt2-large-da")
model = AutoModel.from_pretrained("gpt2-large")
model.save_pretrained("gpt2-large-da")
