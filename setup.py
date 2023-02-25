#!/usr/bin/env python3
from transformers import GPT2Tokenizer,GPT2LMHeadModel
model_name = 'flax-community/dansk-gpt-wiki'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.pad_token = '.'
tokenizer.padding_side = 'left'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer.save_pretrained('gpt2-da')
model.save_pretrained('gpt2-da')
