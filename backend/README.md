# Development

## Requirements

* Docker ([Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac); Linux :neckbeard:)
* [jq](https://stedolan.github.io/jq/) -- for jq command
* [httpie](https://httpie.org/) -- for http command
* [gdal](https://gdal.org/) -- for ogr2ogr command
* Python 2.7.9

## Running

As a note, to run the database, you need a .env file in this directory that
contains the database environment variables. Please ask someone in the channel
#cfh-aclu for the file. If you want to run mongodb locally, uncomment the
mongo image settings to use the bitnami mongodb image.

```
$ make dev
$ curl http://localhost:50050/aloha
```

# Data

Please see the [data schema](Schema.md) for more details.

# Common tasks

## Environment variables

Many of the commands and files below assume that the following environment
variables are set:

* MONGO_HOST (use aclu-db to match the docker compose container name)
* MONGO_PORT (27017 should be used)
* MONGO_USERNAME
* MONGO_PASSWORD
* MONGO_DBNAME 

If `MONGO_HOST` or `MONGO_PORT` are not set to `aclu-db` or `27017` respectively
, you will need to change the docker-compose configs and probably several of the
scripts in order to get things to run.

## Converting tmk data to geojson

To create tmk geojson, from the backend directory, run the following script:

```
cd ./data/tmk/20170713/
./tmk_shapefile_to_geojson.sh
```

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
  echo ${line} | http --print=HhBb POST http://localhost:50050/organizations/
  printf '\n\n'
done;
```

After seeding the organization data, you can retrieve them via

```http get http://localhost:50050/organizations```

## Importing data

**Note / Warning:**

If you aren't running in a virtualenv on your local machine, we would suggest
you do so before you run the seed_*_data.sh scripts. There are some (dangerous) assumptions
being made about the environment you're running - one of them being that you're
running in a virtualenv so that running pip won't pollute your system env. If
this isn't the case, and you've already run the script, we're sorries. With
that said, you might want to review the seed_*_data.sh scripts in /etc to see
exactly what assumptions are being made. If you're planning to run this in
Virtualbox / Vagrant, then you can ignore this as polluting that environment is
less dangerous (but should at some point still be installed into a virtualenv
in the box) so that the environments are closer to one another.

### Vagrant

If you are in the Vagrant box, issue the following:

 - /<path>/<to>/vagrant ssh
 - /var/project-aclu/backend/etc/seed_fake_park_data.sh

### Docker

 - Bring up the Dockers via make (if you need to rebuild, make sure to rebuild as the make script won't do that for you)
 - ```./etc/seed_fake_park_data.sh```

The seed_fake_park_data.sh script should perform the following:

 - Run the command "Converting parks data to geojson" to convert the parks data into a 2017-07-19.parks.geojson file placed into the importer directory
 - Run the command above to seed the organizations
 - ```cd importer; pip install -r requirements.txt```
 - ```python import_parks.py --feature_collection_path <path_to/2017-07-19.parks.geojson>``` to bring in the parks data

To see that the script worked:

 - http get localhost:50050/features
 - PROFIT

While you can run this seed file multiple times, it isn't idempotent. The state of the world under this script will be shifting, but the only thing it should be doing is adding more features to hand-crafted organization.

## Sample spatial query to return a feature

This should get you data around Kapiolani Park.

```
http get http://localhost:50050/features/?where={"geojson.geometry":{"$near":{"$geometry":{"type":"Point", "coordinates":[-157.823231, 21.269304]}, "$maxDistance": 250}}}
```

If you see a 500 error come through, see below to create a spatial index before you can issue a spatial query above.

You'll also probably see an error being leaked through the docker container that looks something like the following:

```
pymongo.errors.OperationFailure: error processing query: ns=aclu.features limit=25Tree: GEONEAR  field=geojson maxdist=250 isNearSphere=0
aclu-api | Sort: {}
aclu-api | Proj: { ownership: 1, restrictions: 1, _created: 1, _id: 1, name: 1, last_imported_at: 1, _updated: 1, geojson: 1, organization: 1, _etag: 1 }
aclu-api |  planner returned error: unable to find index for $geoNear query
```

## Helpful Mongo commands

### Creating the spatial index


```docker exec -it <db_container_id> mongo --username ${MONGO_USERNAME} --password ${MONGO_PASSWORD} ${MONGO_DBNAME} --eval "db.features.ensureIndex({'geojson.geometry': '2dsphere'})"```

### Dropping entire collection

```docker exec -it <db_container_id> mongo aclu --eval "db.features.drop()"```
```docker exec -it c322bf76719f mongo aclu --eval "db.features.drop()"```

# Tests

```PYTHONPATH=. ptw --poll --clear --afterrun 'true && echo "Last test run at: " `date`' .```

# TODO

Here's a list of things we need to do.

 - Verify that the schema is correct. It was a first pass, so probably needs to change.
 - Fix this README as I used it as a notepad. :D
 - Add Postman endpoints
 - Need to bring in more feature properties as possible first class properties
   wrt the data schmea
 - Need to setup a fixed virtualenv for this in the Vagrant box along with on
   the dev machine. Right now, that pip install call will pollute your
   environment if you don't have a virtualenv setup - so sorry if that's
   unexpected. Will update with a warning atop.
 - Need to decide if we want to run this via python3 or python2. Currently
   running all in python2

