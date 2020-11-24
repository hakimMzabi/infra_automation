#!/bin/bash

hdfs dfs -put datagang/infra_automation/* project/automation_project/
oozie job -oozie http://d271ee89-3c06-4d40-b9d6-d3c1d65feb57.priv.instances.scw.cloud:11000/oozie -config job.properties -submit