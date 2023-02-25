#!/usr/bin/env python3
import json
from sys import stdin
for line in stdin:
    print(json.dumps({"text": line.strip()}))
