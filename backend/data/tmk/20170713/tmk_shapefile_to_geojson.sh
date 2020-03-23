#!/bin/sh

echo ">> Making tmp directory"

mkdir -p ./tmp

mkdir -p ./tmp/geojsons

unzip "$1".zip -d ./tmp

echo ">> Converting shapfiles to geojson"
tmk_file=$(basename $1)
base_file=$(echo "$tmk_file" | rev | cut -f 1- -d. | rev)

docker run -v "$(pwd)":/data geodata/gdal ogr2ogr -f GeoJSON -t_srs crs:84 "$base_file".geojson "/data/tmp/$base_file.shp"

echo ">> Chunking geojson file"

python geojson_chunker.py --source "./$base_file.geojson" --destination "./tmp/geojsons" --count_per_file 3000


# curl "https://api.mapbox.com/datasets/v1/felimartina/cjti6i86d01r9t5m3rtn863mr/features?access_token=tk.eyJ1IjoiZmVsaW1hcnRpbmEiLCJleHAiOjE1NTMxNTQ2ODEsImlhdCI6MTU1MzE1MTA4MCwic2NvcGVzIjpbImVzc2VudGlhbHMiLCJzY29wZXM6bGlzdCIsIm1hcDpyZWFkIiwibWFwOndyaXRlIiwidXNlcjpyZWFkIiwidXNlcjp3cml0ZSIsInVwbG9hZHM6cmVhZCIsInVwbG9hZHM6bGlzdCIsInVwbG9hZHM6d3JpdGUiLCJzdHlsZXM6dGlsZXMiLCJzdHlsZXM6cmVhZCIsImZvbnRzOnJlYWQiLCJzdHlsZXM6d3JpdGUiLCJzdHlsZXM6bGlzdCIsInRva2VuczpyZWFkIiwidG9rZW5zOndyaXRlIiwiZGF0YXNldHM6bGlzdCIsImRhdGFzZXRzOnJlYWQiLCJkYXRhc2V0czp3cml0ZSIsInRpbGVzZXRzOmxpc3QiLCJ0aWxlc2V0czpyZWFkIiwidGlsZXNldHM6d3JpdGUiLCJ2aXNpb246cmVhZCIsInN0eWxlczpkcmFmdCIsImZvbnRzOmxpc3QiLCJmb250czp3cml0ZSIsImZvbnRzOm1ldGFkYXRhIiwiZGF0YXNldHM6c3R1ZGlvIiwiY3VzdG9tZXJzOndyaXRlIiwiYW5hbHl0aWNzOnJlYWQiXSwiY2xpZW50IjoibWFwYm94LmNvbSIsImxsIjoxNTUwNzIyODMyNzM3LCJpdSI6bnVsbH0.ywnmQ33w5c0muE7Isw08ig" \
#   -X POST \
#   -H "Content-Type: application/json" \
#   -d @0.1.geojson

# python mapbox_importer.py --source "./2017-07-13.tmk.geojson" --chunksize 100





# docker run -v "$(pwd)":/data geodata/gdal ogr2ogr -f GeoJSON -t_srs crs:84 2019.05.01.parks.geojson "/data/parks/2019.05.01_Parks/Parks.shp"
# docker run -v "$(pwd)":/data geodata/gdal ogr2ogr -f GeoJSON -t_srs crs:84 2019.05.01.park_amanities.geojson "/data/parks/2019.05.01_Park_Amenities/Park_Amenities.shp"

# /usr/bin/ogr2ogr -f GeoJSON -t_srs crs:84 \
# "importer/2019.05.01.parks.geojson" \
# "data/parks/2019.05.01_Parks/Parks.shp"
