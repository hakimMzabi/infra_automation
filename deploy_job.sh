#!/usr/bin/sh
spark-submit --master yarn --queue default  --driver-memory=2g --executor-memory=2g --num-executors=2 $(dirname $0)/jobs/Extr_load_spotify.py