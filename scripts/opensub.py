#!/usr/bin/env python3
from string import ascii_lowercase as alp
from datasets import load_dataset as ld
ls = ["pt_br", "ze_en", "ze_zh", "zh_cn", "zh_tw"]
o = open("opensubtitles.txt","wt")
for a in alp:
    for b in alp:
        ls.append(a+b)
for l in ls:
    dss = []
    try:
        dss.append(ld("open_subtitles", lang1="da", lang2=l))
    except:
        pass
    try:
        dss.append(ld("open_subtitles", lang2="da", lang1=l))
    except:
        pass
    for ds in dss:
        print(ds)
        for x in ds['train']['translation']:
            print(x['da'].strip(),file=o)
o.close()
