#!/bin/bash

oozie job -oozie http://$(hostname -f):11000/oozie -config oozie/job.properties -run