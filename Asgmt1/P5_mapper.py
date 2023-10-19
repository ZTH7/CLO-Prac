#!/usr/bin/python3

import sys
import csv

def is_numeric_string(value):
    try:
        # Try converting to int and float
        int_value = int(value)
        float_value = float(value)
        
        # If both conversions succeed, it's a number
        return True
    except ValueError:
        # If either conversion fails, it's not a number
        return False


csvfile = csv.reader(sys.stdin)

next(csvfile) # Skip header

for line in csvfile:
    if is_numeric_string(line[4]):
        print(line[3] + '\t'+ line[4])
