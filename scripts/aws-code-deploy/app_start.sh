#!/bin/bash
# Start dockers
cd /var/project-aclu/
sudo docker-compose up -d

# Create the spatial index
docker exec $(docker ps -aqf "name=aclu-db") mongo aclu --eval "db.features.ensureIndex({'geojson.geometry': '2dsphere'})"

# seed db. We do this on every run now because we are on a stage site!
cd backend/etc
sudo chmod +x seed_fake_park_data.sh
./seed_fake_park_data.sh