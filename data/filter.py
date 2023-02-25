#!/usr/bin/env python3
from sys import stdin as i, stdout as o
for line in i:
    words = line.strip().split()
    if len(words) > 3 and "." in line:
        print(' '.join(words), file=o)
