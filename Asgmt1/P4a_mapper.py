#!/usr/bin/python3

import sys
import csv

""" for line in sys.stdin:
    if (line[0] != 'u'):
        words = re.sub(r'^[^,]*,|,[^.]*$\n', '', line)
        words = re.sub(r',', '\t', words)
    
        print(words)
 """

csvfile = csv.reader(sys.stdin)

next(csvfile) # Skip header

for line in csvfile:
    print(line[1] + '\t' + line[2])