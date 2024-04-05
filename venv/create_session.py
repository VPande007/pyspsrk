from pyspark.sql import SparkSession

def create_session():
    spark = SparkSession.builder \
        .appName("DataSkewHandling") \
        .getOrCreate()
    return spark