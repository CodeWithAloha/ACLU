docker network create aclu-network --driver bridge
docker run -d --name=aclu-mongodb \
    -v /Users/pipe/mongodb-data:/bitnami \
    --network aclu-network \
    -p 27017:27017 \
    -e MONGODB_USERNAME=aclu \
    -e MONGODB_PASSWORD=Aclu123! \
    -e MONGODB_DATABASE=aclu \
    bitnami/mongodb:latest


docker run -d --name=aclu-api \
  --network aclu-network \
  -p 50050:50050 \
  -e MONGO_HOST=aclu-mongodb \
  -e MONGO_PORT=27017 \
  -e MONGO_USERNAME=aclu \
  -e MONGO_PASSWORD=Aclu123! \
  -e MONGO_DBNAME=aclu \
  aclu-api

cd ./backend/importer
python import_park_hours.py -o ./park_hours.json --force

python import_parks.py \
  --park_features_path "./2019.05.01.parks.geojson" \
  --park_hours_path="./park_hours.json" \
  --park_amenities_path="2019.05.01.park_amenities.geojson"

