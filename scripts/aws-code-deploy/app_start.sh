#!/bin/bash
# Start dockers
cd /var/project-aclu/
sudo docker-compose up -d

# Create the spatial index
docker exec $(docker ps -aqf "name=aclu-db") mongo aclu --eval "db.features.ensureIndex({'geojson.geometry': '2dsphere'})"

# Cleanup previous run of the db feed
cd backend
sudo rm -f importer/2017-07-19.parks.geojson
# Seed db. We do this on every run now because we are on a stage site!
cd etc
sudo chmod +x seed_fake_park_data.sh
./seed_fake_park_data.sh