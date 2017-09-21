#!/bin/bash

# Start up the dockers
sudo sg vagrant <<\DEVOPS_BLOCK
    cd /var/project-aclu/backend
    docker-compose up -d
DEVOPS_BLOCK

# Create the spatial index
docker exec -it $(docker ps -aqf "name=aclu-db") mongo aclu --eval "db.features.ensureIndex({'geojson.geometry': '2dsphere'})"

# Start up the nodes
cd /var/project-aclu/frontend
yarn
yarn run dev
