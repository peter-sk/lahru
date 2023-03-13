#!/usr/bin/env python
from json import loads
from sys import stdin
for line in stdin:
    loads(line.strip())
