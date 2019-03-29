#!/bin/sh

echo ">> Making tmp directory"

mkdir -p ./tmp

mkdir -p ./tmp/geojsons

echo ">> Downloading TMK zip file from Google Drive to ./tmp/20170713.tmk_state.shp.zip"

python tmk_google_downloader.py --destination "./tmp/20170713.tmk_state.shp.zip"

echo ">> Completed TMK zip file download: ./tmp/20170713.tmk_state.shp.zip"

echo ">> Unzipping ./tmp/20170713.tmk_state.shp.zip to ./tmp"

unzip ./tmp/20170713.tmk_state.shp.zip -d ./tmp

echo ">> Converting shapfiles to geojson"

docker run -v "$(pwd)":/data geodata/gdal ogr2ogr -f GeoJSON -t_srs crs:84 2017-07-13.tmk.geojson "/data/tmp/tmk_state.shp"

echo ">> Chunking geojson file"

python geojson_chunker.py --source "./2017-07-13.tmk.geojson" --destination "./tmp/geojsons" --count_per_file 3000


# curl "https://api.mapbox.com/datasets/v1/felimartina/cjti6i86d01r9t5m3rtn863mr/features?access_token=tk.eyJ1IjoiZmVsaW1hcnRpbmEiLCJleHAiOjE1NTMxNTQ2ODEsImlhdCI6MTU1MzE1MTA4MCwic2NvcGVzIjpbImVzc2VudGlhbHMiLCJzY29wZXM6bGlzdCIsIm1hcDpyZWFkIiwibWFwOndyaXRlIiwidXNlcjpyZWFkIiwidXNlcjp3cml0ZSIsInVwbG9hZHM6cmVhZCIsInVwbG9hZHM6bGlzdCIsInVwbG9hZHM6d3JpdGUiLCJzdHlsZXM6dGlsZXMiLCJzdHlsZXM6cmVhZCIsImZvbnRzOnJlYWQiLCJzdHlsZXM6d3JpdGUiLCJzdHlsZXM6bGlzdCIsInRva2VuczpyZWFkIiwidG9rZW5zOndyaXRlIiwiZGF0YXNldHM6bGlzdCIsImRhdGFzZXRzOnJlYWQiLCJkYXRhc2V0czp3cml0ZSIsInRpbGVzZXRzOmxpc3QiLCJ0aWxlc2V0czpyZWFkIiwidGlsZXNldHM6d3JpdGUiLCJ2aXNpb246cmVhZCIsInN0eWxlczpkcmFmdCIsImZvbnRzOmxpc3QiLCJmb250czp3cml0ZSIsImZvbnRzOm1ldGFkYXRhIiwiZGF0YXNldHM6c3R1ZGlvIiwiY3VzdG9tZXJzOndyaXRlIiwiYW5hbHl0aWNzOnJlYWQiXSwiY2xpZW50IjoibWFwYm94LmNvbSIsImxsIjoxNTUwNzIyODMyNzM3LCJpdSI6bnVsbH0.ywnmQ33w5c0muE7Isw08ig" \
#   -X POST \
#   -H "Content-Type: application/json" \
#   -d @0.1.geojson

python mapbox_importer.py --source "./2017-07-13.tmk.geojson" --chunksize 100