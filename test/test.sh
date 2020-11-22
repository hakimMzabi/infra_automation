#!/bin/bash

mkdir datagang/lab/
mkdir datagang/lab/data/

mkdir datagang/project/
mkdir datagang/project/data/

mkdir datagang/project/automation_project
hdfs dfs -put datagang/infra_automation/* datagang/project/automation_project/

oozie job -oozie http://localhost:11000/oozie -config job.properties -submit