#!/usr/bin/env python3
from sys import stderr as e, stdin as i, stdout as o
from tqdm import tqdm
from transformers import GPT2TokenizerFast
tokenizer = GPT2TokenizerFast.from_pretrained("flax-community/dansk-gpt-wiki")
for line in tqdm(i, desc="splitting lines"):
    line = line.strip()
    tokens = tokenizer(line)
    tokens_tokens = tokens.tokens()
    tokens_word_ids = tokens.word_ids()
    len_tokens = len(tokens['input_ids'])
    f = 0
    t = min(f+1024+1, len_tokens)
    while t-f > 1024:
        while tokens_tokens[t-1] != "." and t-f > 128:
            t -= 1
#        print(f"f = {f}   t = {t} S", file=e)
        if t > f:
            print(line[tokens.word_to_chars(tokens_word_ids[f])[0]:tokens.word_to_chars(tokens_word_ids[t-1])[1]],file=o)
        f = t
        t = min(f+1024+1, len_tokens)
    if t > f:
#        print(f"f = {f}   t = {t} N", file=e)
        print(line[tokens.word_to_chars(tokens.word_ids()[f])[0]:tokens.word_to_chars(tokens.word_ids()[t-1])[1]],file=o)
