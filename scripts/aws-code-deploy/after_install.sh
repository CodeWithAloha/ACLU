# Build website
cd /var/project-aclu/frontend
yarn
yarn build

# Docker compose
cd /var/project-aclu/backend
docker-compose build

# Create the spatial index
docker exec -it $(docker ps -aqf "name=aclu-db") mongo aclu --eval "db.features.ensureIndex({'geojson.geometry': '2dsphere'})"
