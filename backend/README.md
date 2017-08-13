# Data

Please see the [data schema](Schema.md) for more details.

# Installation

## Requirements

* Docker

## Running API

```
cd docker
docker-compose build
docker-compose up -d
curl localhost:5000/aloha
```

# Common tasks

## Converting parks data to geojson

To create geojson, from the backend directory, run the following:

```
docker run -v "$(pwd)":/data geodata/gdal \
    ogr2ogr -f GeoJSON -t_srs crs:84 \
    2017-07-19.parks.geojson \
    "data/parks/2017.07.19 - Parks__Oahu/Parks__Oahu.shp"
```

## Running data importer

TBD

## Seeding organization data with jq, httpie

```
jq -r '.[] | tostring' ./data/seed/organizations.json | while read line
do
  echo ${line} | http --print=HhBb POST http://localhost:5000/organizations/
  printf '\n\n'
done;
```

# TODO

Here's a list of things we need to do.

 - Verify that the schema is correct. It was a first pass, so probably needs to
   change.
