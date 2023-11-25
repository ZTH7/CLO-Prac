#!/usr/bin/python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("P5").getOrCreate()

csvfile = spark.read.option(header="true", inferSchema="true").csv("Meteorite_Landings.csv")

csvfile = csvfile.dropna(subset=["mass (g)"])

csvfile = csvfile.withColumn("mass (g)", col("mass (g)").cast("float"))

csvfile = csvfile.groupBy('recclass').avg('mass (g)').sort('avg(mass (g))')

csvfile.show()