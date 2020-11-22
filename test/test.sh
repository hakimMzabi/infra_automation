#!/bin/bash

hdfs dfs -mkdir lab
hdfs dfs -mkdir lab/data/

hdfs dfs -mkdir project
hdfs dfs -mkdir project/data/

hdfs dfs -mkdir project/automation_project
hdfs dfs -put datagang/infra_automation/* project/automation_project/

oozie job -oozie http://localhost:11000/oozie -config job.properties -submit