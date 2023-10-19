#!/usr/bin/python3

import sys
import csv
import re

csvfile = csv.reader(sys.stdin)

next(csvfile)   # Skip header

for line in csvfile:
   print(re.sub(r'-(.*)', '', line[0]) + '\t' + line[5])
