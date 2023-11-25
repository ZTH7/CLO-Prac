#!/usr/bin/python3

import sys
import re
from pyspark import SparkConf, SparkContext

args = sys.argv
conf = SparkConf().setAppName('P1')
sc = SparkContext(conf = conf)

if len(args) < 3:
    print("Falta argumentos")
    exit(-1)

words = sc.textFile(args[2]).filter(lambda line : (len(re.findall(r'\b' + re.escape(args[1]) + r'\b', line, flags=re.IGNORECASE)) != 0))

for line in words.collect():
    print(line)
