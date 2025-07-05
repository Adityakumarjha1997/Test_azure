from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.types import *

data = [(1,"A"),(2,"B"),(3,"C")]

sch = StructType([StructField("id", IntegerType()), StructField("name", StringType())])

spark   =  SparkSession.builder.appName("sds").getOrCreate()

df = spark.createDataFrame(data, schema= sch)

df.show()