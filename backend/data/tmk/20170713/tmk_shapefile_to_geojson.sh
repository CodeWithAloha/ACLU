#!/bin/sh

echo ">> Making tmp directory"

mkdir -p ./tmp

echo ">> Downloading TMK zip file from Google Drive to ./tmp/20170713.tmk_state.shp.zip"

python tmk_google_downloader.py --destination "./tmp/20170713.tmk_state.shp.zip"

echo ">> Completed TMK zip file download: ./tmp/20170713.tmk_state.shp.zip"

echo ">> Unzipping ./tmp/20170713.tmk_state.shp.zip to ./tmp"

unzip ./tmp/20170713.tmk_state.shp.zip -d ./tmp

echo ">> Converting shapfiles to geojson"

docker run -v "$(pwd)":/data geodata/gdal ogr2ogr -f GeoJSON -t_srs crs:84 2017-07-13.tmk.geojson "/data/tmp/tmk_state.shp"
