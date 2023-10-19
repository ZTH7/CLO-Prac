#!/usr/bin/python3

import sys

previous = None
sum = ""

for line in sys.stdin:
    key, value = line.split('\t')
    # value = re.sub(r'\n', '', value)
    if key != previous:
        if previous is not None:
            print("Rating: " + previous + ' ' + sum)
        previous = key
        sum = ""
    
    sum += " " + value

print("Rating: " + previous + ' ' + sum)
