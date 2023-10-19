#!/usr/bin/python3

import sys
import re

previous = None
sum = ""

for line in sys.stdin:
    key, value = line.split('\t')

    if key != previous:
        if previous is not None:
            print("Rating: " + previous + '\n' + sum)
        previous = key
        sum = ""
    
    sum += value.strip() + " "

print("Rating: " + previous + '\n' + sum)
