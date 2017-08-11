# Data

Please see the [data schema](Schema.md) for more details.

# Installation

## Requirements

* Docker

## Running API

```cd docker```
```docker-compose build```
```docker-compose up -d```
```curl localhost:5000/aloha```

## Converting parks data to geojson

To create geojson, from the backend directory, run the following:

```docker run -v "$(pwd)":/data geodata/gdal ogr2ogr -f GeoJSON -t_srs crs:84 2017-07-19.parks.geojson "data/parks/2017.07.19 - Parks__Oahu/Parks__Oahu.shp"```
