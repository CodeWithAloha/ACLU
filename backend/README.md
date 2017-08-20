# Development

## Requirements

* Docker ([Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac); Linux :neckbeard:)

## Running

```
$ make dev
$ curl http://localhost:5000/aloha
```

# Data

Please see the [data schema](Schema.md) for more details.

# Common tasks

## Converting parks data to geojson

To create geojson, from the backend directory, run the following:

```
docker run -v "$(pwd)":/data geodata/gdal \
    ogr2ogr -f GeoJSON -t_srs crs:84 \
    2017-07-19.parks.geojson \
    "data/parks/2017.07.19 - Parks__Oahu/Parks__Oahu.shp"
```

## Seeding organization data with jq, httpie

```
jq -r '.[] | tostring' ./data/seed/organizations.json | while read line
do
  echo ${line} | http --print=HhBb POST http://localhost:5000/organizations/
  printf '\n\n'
done;
```

## Running data importer

 - Bring up the Dockers via make (if you need to rebuild, make sure to rebuild as the make script won't do that for you)
 - Run the command "Converting parks data to geojson" to get the 2017-07-19.parks.geojson file
 - Copy that file into the importer directory
 - Run the command above to seed the organizations
 - ``` python import.py ``` to bring in the parks data
 - http get localhost:5000/features
 - PROFIT

# TODO

Here's a list of things we need to do.

 - Verify that the schema is correct. It was a first pass, so probably needs to
   change.
