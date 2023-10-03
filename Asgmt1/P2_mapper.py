#!/usr/bin/python3

import sys
import re

for line in sys.stdin:
    words = re.sub(r' - - (.*)\n', ' ', line).split()
    
    for word in words:
        print(word.lower() + "\t1")
