#!/usr/bin/python3

import sys
import csv

csvfile = csv.reader(sys.stdin)

next(csvfile)   # Skip header

for line in csvfile:
   print(line[1] + '\t' + line[2])
