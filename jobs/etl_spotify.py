from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import pyspark.sql.functions as F

spark = SparkSession.builder \
    .master('local[1]') \
    .appName('SparkByExamples.com') \
    .getOrCreate()
sc = spark.sparkContext

data_path_lake = "d271ee89-3c06-4d40-b9d6-d3c1d65feb57.priv.instances.scw.cloud:8020/user/datagang/lab/spotify"
df = spark.read.option("header", True).csv("./data_sp.csv")

#spark.read.format("com.databricks.spark.avro").load(data_path_lake)
df_selection = df.select("artist", "album", "track_number", "name", "danceability", "energy", "valence", "popularity")

df_groubed = df_selection.groupBy("artist").agg(F.max("popularity"))
df_groubed.write.format("com.databricks.spark.avro").save(data_path_lake)
#df_groubed.show()
"""
save
"""