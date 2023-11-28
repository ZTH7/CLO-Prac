#!/usr/bin/python3

import re
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("P3").getOrCreate()

csvfile = spark.read.option("header", "", "true").csv("GOOGLE.csv")

csvfile = csvfile.withColumn("Close", col("Close").cast("float"))

csvfile = csvfile.withColumn("Date", udf((lambda line : re.sub(r'-(.*)', '', line)))("Date"))

csvfile = csvfile.groupBy('Date').avg('Close').sort('Date')

csvfile.show()

spark.stop()
