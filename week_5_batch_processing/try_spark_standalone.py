import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, TimestampType
from pyspark.sql.functions import col, to_date

spark = SparkSession.builder \
    .master("spark://localhost:7077") \
    .appName('test') \
    .getOrCreate()


df = spark.read \
    .parquet('fhv_trip/2019/10/')


df.printSchema()

# To filter on 2019-10-15
df = df.withColumn("pickup_date",to_date("pickup_datetime"))
filterred_trip = df.filter(col("pickup_date") == "2019-10-15")
filterred_trip.show()


# Find the longest trip
df = df.withColumn("duration_seconds", (col("dropOff_datetime").cast("long") - col("pickup_datetime").cast("long")))
longest_trip = df.orderBy(col("duration_seconds").desc()).first()

duration_seconds = longest_trip["duration_seconds"]
duration_hours = duration_seconds / 3600

# Least frequent pickup location zone
zone_df = spark.read.csv('taxi_zone_lookup.csv', header=True, inferSchema=True)

pickup_counts_df = df.groupBy("PUlocationID").count()

result_df = pickup_counts_df.join(zone_df, pickup_counts_df["PUlocationID"] == zone_df["LocationID"])

least_frequent_zone = result_df.orderBy(col("count")).first()

# Display the result
print("Least frequent pickup location zone:")
least_frequent_zone

