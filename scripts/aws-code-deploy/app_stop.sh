#!/bin/bash
# Stop running docker
cd /var/project-aclu/
sudo docker stop $(docker ps -aqf "name=aclu-api")