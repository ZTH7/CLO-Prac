#!/usr/bin/python3

import sys
import math

previous = None
sum = 0
count = 0

for line in sys.stdin:
    key, value = line.split('\t')
    
    if key != previous:
        if previous is not None:
            print(str(math.trunc(sum / count)) + '\t' + previous)
        previous = key
        sum = 0
        count = 0
    
    sum = sum + float(value)
    count += 1

print(str(math.trunc(sum / count)) + '\t' + previous)
