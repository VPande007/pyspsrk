def ingetion(spark):
    df = spark.read.text("hh")
    return df