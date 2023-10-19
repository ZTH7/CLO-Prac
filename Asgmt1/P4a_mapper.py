#!/usr/bin/python3

import sys
import re

for line in sys.stdin:
    if (line[0] != 'u'):
        words = re.sub(r'^[^,]*,|,[^.]*$\n', '', line)
        words = re.sub(r',', '\t', words)
    
        print(words)