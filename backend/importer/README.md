# Importing and syncing data

## Requirements

* Docker ([Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac); Linux :neckbeard:)
* [jq](https://stedolan.github.io/jq/) -- for jq command
* [httpie](https://httpie.org/) -- for http command
* [gdal](https://gdal.org/) -- for ogr2ogr command
* Python 2.7.9


## Spinning up VMs
See [README.md](../README.md) for instructions on starting and stopping VMs.


### Importing data
The following instructions assume that data will be imported into the 
dev VMs. 

## Importing parks data into mongodb
Run
 
    python import_park_hours.py -o ./park_hours.json --force

to get parks data. Then run the following to import parks data. Replace the 
file names in the invocation as needed.

    python import_parks.py \
      --park_features_path="./2019.05.01.parks.geojson" \
      --park_hours_path="./park_hours.json" \
      --park_amenities_path="2019.05.01.park_amenities.geojson" \
      --api_base_url="http://localhost:50050"

This may take up a few hours to complete.  

## Import TMKs 

Run the following to import TMKS. Replace the file names
in the invocation as needed. 

    python import_tmks.py \
      --tmk_features_path="../data/tmk/20170713/2017-07-13.tmk.geojson" \
      --api_base_url="http://localhost:50050"` 
    

This may take up a few hours to complete.



