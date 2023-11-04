#!/usr/bin/python3

import sys
from pyspark import SparkConf, SparkContext

args = sys.argv
conf = SparkConf().setAppName('P1')
sc = SparkContext(conf = conf)

if len(args) < 3:
    print("Falta argumentos")
    exit(-1)

words = sc.textFile(args[2]).filter(lambda line : (line.count(args[1]) != 0))

print(words.collect())
