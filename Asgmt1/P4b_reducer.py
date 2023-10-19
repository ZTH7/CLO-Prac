#!/usr/bin/python3

import sys
import re

previous = None
sum = ""

for line in sys.stdin:
    key, value = line.split('\t')
    
    if key != previous:
        if previous is not None:
            print("Range " + previous + ':' + sum + '\n')
        previous = key
        sum = ""
    
    sum += " " + value.replace('\n', '')

print("Range " + previous + ':' + sum + '\n')
