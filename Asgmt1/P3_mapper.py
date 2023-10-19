#!/usr/bin/python3

import sys
import re
import csv

""" for line in sys.stdin:
    if (line[0] != 'D'):
        words = re.sub(r'-[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,', '\t', line)
        words = re.sub(r',(.*)\n', '', words)
    
        print(words) """

csvfile = csv.reader(sys.stdin)

next(csvfile) # Skip header

for line in csvfile:
    date = re.sub(r'-\w+', '', line[0])
    print (date + '\t' + line[6])

