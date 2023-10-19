#!/usr/bin/python3

import sys

text = ""

for line in sys.stdin:
    key, value = line.split('\t')
    text += (key + "\t" + value)

print(text)
