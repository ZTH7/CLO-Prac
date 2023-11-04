#!/usr/bin/python3

import sys
import re
from pyspark import SparkConf, SparkContext

args = sys.argv
conf = SparkConf().setAppName('P2')
sc = SparkContext(conf = conf)

words = sc.textFile('access_log') \
   .flatMap(lambda line: re.sub(r' - - (.*)', ' ', line).split()) \
   .map(lambda word: (word.lower(), 1)) \
   .reduceByKey(lambda a, b: a + b)

print(words.collect())
