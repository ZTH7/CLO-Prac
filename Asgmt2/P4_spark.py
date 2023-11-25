#!/usr/bin/python3

import math
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("P4").getOrCreate()

csvfile = spark.read.option("header", "true").csv("ratings.csv")

csvfile = csvfile.withColumn("rating", col("rating").cast("float"))

csvfile = csvfile.groupBy('movieId').avg('rating')

csvfile = csvfile.withColumn("avg(rating)", udf((lambda line : math.trunc(float(line)) + 1))("avg(rating)")).sort('avg(rating)')

csvfile.show()
