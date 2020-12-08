
import pyspark
from pyspark import SQLContext, SparkContext, SparkConf
from pyspark.sql import *
from pyspark.sql.functions import udf
from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql.functions import *
from math import *


conf = pyspark.SparkConf()
sc = pyspark.SparkContext.getOrCreate(conf)
spark = SQLContext(sc)

print("this is a test !")
#columns = ["x", "y"]
#data = [(5, 3), (8, 5), (5, 7), (3, 6)]
#df = spark.createDataFrame(data).toDF(*columns)
#df.show()


#def distance(x, y):
#    return sqrt(((x - y) ^ 2) + ((y + x) ^ 2))


#distance_udf = udf(lambda a, b: distance(a, b), DoubleType())
#df = df.select('x', 'y', distance_udf('x', 'y').alias('distance'))
