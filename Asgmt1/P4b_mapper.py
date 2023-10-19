#!/usr/bin/python3

import sys
import re

text = ""

for line in sys.stdin:
    key, value = line.split("\t")
    text += (key + "\t" + value)

print(text, end='')
