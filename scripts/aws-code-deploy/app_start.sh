#!/bin/bash
cd /var/project-aclu/
docker run -p 50050:50050 --name "aclu-api" "705750910119.dkr.ecr.us-west-2.amazonaws.com/aclu:latest"