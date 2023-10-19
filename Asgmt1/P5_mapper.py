#!/usr/bin/python3

import sys
import csv

csvfile = csv.reader(sys.stdin)

next(csvfile)   # Skip header

for line in csvfile:
   if line[3] != '' and line[4] != '':
      print(line[3] + '\t' + line[4])
