from pyspark.sql.functions import *

def process(df):
    df = df.withColumn("list", split(col("value"), " "))
    df = df.withColumn("words", explode(col("list")))
    df = df.groupBy("words").count()
    d = df.show()
    return d
