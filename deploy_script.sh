#!/bin/bash
hdfs dfs -rm -r  /user/datagang/project/infra_automation/*
hdfs dfs -put /datagang/infra_automation /user/datagang/project/

oozie job -oozie http://d271ee89-3c06-4d40-b9d6-d3c1d65feb57.priv.instances.scw.cloud:11000/oozie -config job.properties -run