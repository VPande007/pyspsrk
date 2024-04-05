from create_session import *
from ingestion import *
from processsing import *


def main():
    spark = create_session()
    df = ingetion(spark)
    d = process(df)




if __name__ == "__main__":
    main()