from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import pyspark.sql.functions as F

spark = SparkSession.builder \
    .master('local[1]') \
    .appName('SparkByExamples.com') \
    .getOrCreate()
sc = spark.sparkContext

data_path_lake = "/user/datagang/lab/*"
data_path_prod = "/user/datagang/data/"

df = spark.read.format("com.databricks.spark.avro").load(data_path_lake)
df_selection = df.select("artist", "album", "track_number", "name", "danceability", "energy", "valence", "popularity")

df_groubed = df_selection.groupBy("artist").agg(F.max("popularity"))
df_groubed.write.format("com.databricks.spark.avro").save(data_path_prod)
