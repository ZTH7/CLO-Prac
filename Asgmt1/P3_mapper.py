#!/usr/bin/python3

import sys
import re

for line in sys.stdin:
    if (line[0] != 'D'):
        words = re.sub(r'-[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,', '\t', line)
        words = re.sub(r',(.*)\n', '', words)
    
        print(words)
