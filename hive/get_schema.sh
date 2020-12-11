#!/bin/bash

data_source_path=$(hdfs dfs -ls -t $(1)/infra_automation | grep avro | head -1 | awk '{print $8}')
hadoop jar $(2) getschema ${data_source_path} | hadoop fs -put -f -$(3)/spotify_data.avsc