from pyspark.sql import SparkSession
spark = SparkSession.builder \
                    .master('local[1]') \
                    .appName('SparkByExamples.com') \
                    .getOrCreate()

print("this is a test !")
# columns = ["x", "y"]
# data = [(5, 3), (8, 5), (5, 7), (3, 6)]
# df = spark.createDataFrame(data).toDF(*columns)
# df.show()


# def distance(x, y):
#    return sqrt(((x - y) ^ 2) + ((y + x) ^ 2))


# distance_udf = udf(lambda a, b: distance(a, b), DoubleType())
# df = df.select('x', 'y', distance_udf('x', 'y').alias('distance'))
