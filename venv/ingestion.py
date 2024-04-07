def ingetion(spark):
    df = spark.read.text("hh")
    print("hi")
    return df