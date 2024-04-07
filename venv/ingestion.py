def ingetion(spark):
    df = spark.read.text("hh")
    print("hiio")
    return df