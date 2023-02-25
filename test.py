#!/usr/bin/env python3
from transformers import pipeline
p = pipeline('text-generation',model='gpt2-da')
q = pipeline('text-generation',model='flax-community/dansk-gpt-wiki')
print(p("Jeg spiser ingen morgendmad. Derfor synes jeg det vigtigste måltid er enten aftensmad eller"))
print(q("Jeg spiser ingen morgendmad. Derfor synes jeg det vigtigste måltid er enten aftensmad eller"))
