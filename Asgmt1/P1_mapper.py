#!/usr/bin/python3

import sys
import re

args = sys.argv

if len(args) < 2:
    print("Falta argumentos")

for line in sys.stdin:
    if line.count(args[1]) != 0:
        words = re.sub(r'\n', '', line)
        print(words)
