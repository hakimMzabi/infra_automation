DROP TABLE IF EXISTS spotify_data;
CREATE EXTERNAL TABLE spotify_data
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION "hdfs://d271ee89-3c06-4d40-b9d6-d3c1d65feb57.priv.instances.scw.cloud:8020/user/datagang/project/infra_automation"
TBLPROPERTIES ('avro.schema.utl'="hdfs://d271ee89-3c06-4d40-b9d6-d3c1d65feb57.priv.instances.scw.cloud:8020/user/datagang/schema/spotify_data.avsc");