#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017
#
# Distributed under terms of the MIT license.

import click
import datetime
import json
import logging
import logging.config
import multiprocessing
import os
import sys
from timeit import default_timer as timer
import uuid
import traceback

from utilities import get_features_from_geojson
from utilities import get_organization
from utilities import get_pyeve_formatted_datetime
from utilities import post_feature
from utilities import post_park_restriction


logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer.parks")


@click.command()
@click.option('--api_base_url', default='http://localhost:50050', help='API base url. Defaults to http://localhost:50050')
@click.option('--park_features_path', help='Path to park features file being imported.')
@click.option('--park_hours_path', help='Path to park hours file')
@click.option('--park_amenities_path', help='Path to park amenities file')
def import_park_features(api_base_url, park_features_path, park_hours_path, park_amenities_path):

    start_time = timer()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    organization = get_organization(api_base_url, "Parks")
    
    num_features = 0

    park_amenities_json = None
    if organization:

        park_hours = _get_park_hours(park_hours_path)
        
        park_amenities_json = _get_park_amenities(park_amenities_path)

        for feature in get_features_from_geojson(park_features_path):
            num_features += 1
            pool.apply_async(
                _post_park_feature_and_restriction,
                [api_base_url, organization, feature, park_hours, park_amenities_json])
    pool.close()
    pool.join()

    end_time = timer()
    logger.info("import_park_features took {} seconds and imported {} park features".format(end_time - start_time, num_features))
    return sys.exit(0)


def _post_park_feature_and_restriction(api_base_url,
                                       organization,
                                       feature,
                                       park_hours,
                                       park_amenities_json):
    f = _construct_park_feature_json(feature, organization, park_hours, park_amenities_json)
    feature_id = post_feature(api_base_url, f)

def _construct_park_feature_json(feature, organization, park_hours, park_amenities_json):
    park_name = feature['properties']['PARK_NAME']
    id = str(uuid.uuid4())

    # It is standard to add attributes to geojson properties
    feature['properties']['NAME'] = park_name
    feature['properties']['ID'] = id
    feature['properties']['RESTRICTIONS'] = {}
    feature['properties']['OWNERSHIP'] = 'CITY'
    feature['properties']['TYPE'] = 'park'
    feature['properties']['ORGANIZATION'] = organization["_id"]
    feature['properties']['FEATURE_TYPE'] = 'PARK'

    f = {
        "_id": id,
        "geojson": feature,
        "name": park_name,
        "last_imported_at": get_pyeve_formatted_datetime(datetime.datetime.utcnow())
    }

    _attach_park_hours_restrictions(f, park_name, park_hours)
    _attach_data_from_park_amenities_file(f, park_name, park_amenities_json)
    return f


def _attach_park_hours_restrictions(f, park_name, park_hours):
    try:
        hours = park_hours.get(park_name, False)
        if hours:
            logger.info("Setting park hours for {0}".format(park_name))
            hours_parts = hours.get('park')
            hours = {
              'hours_start': int(hours_parts.get('open')),
              'hours_end': int(hours_parts.get('close'))
            }
            f['geojson']['properties']['RESTRICTIONS']['hours'] = hours
        else:
            logger.error("No park hours for " + park_name)
    except Exception as e:
        logger.error("Error occurred trying to attach park hour restrictions: "
                     + str(e))
        logger.error(traceback.format_exc())

def _attach_data_from_park_amenities_file(f, park_name, park_amenities_json):
    try:
        if park_amenities_json is None:
            logger.error('Missing amenities for park: ' + park_name)
            return
        for amenities in park_amenities_json['features']:
          if amenities['properties']['PARK_NAME'] == park_name:
            break
          else:
              amenities = None

        # amenities = find(lambda amenity: amenity.PARK_NAME == park_name, park_amenities_json.features)
        if amenities:
            logger.info("Setting park amenities for {0}".format(park_name))
            # Amenities file comes with park address!!!
            f['geojson']['properties']['ADDRESS'] = amenities['properties']['FIRST_NAME']
            f['geojson']['properties']['CITY'] = amenities['properties']['FIRST_CITY']
            f['geojson']['properties']['ZIP'] = amenities['properties']['FIRST_ZIP']
            f['geojson']['properties']['STATE'] = "HI"

            # remove unnecessary known attributes
            del amenities['properties']['OBJECTID']
            del amenities['properties']['PARK_CAT']
            del amenities['properties']['TMK']
            del amenities['properties']['PARK_NAME']
            del amenities['properties']['MAIN_DIST']
            del amenities['properties']['LINK_ID']
            del amenities['properties']['LEGAL_ACRE']
            del amenities['properties']['TOTAL_ACRE']
            del amenities['properties']['TOTAL_SQFT']
            del amenities['properties']['TOTAL_ROOM']
            del amenities['properties']['MAINT_DIST']
            del amenities['properties']['NEIGHBORHO']
            del amenities['properties']['COUNCIL']
            del amenities['properties']['FIRST_CITY']
            del amenities['properties']['FIRST_NAME']
            del amenities['properties']['FIRST_ZIP']
            del amenities['properties']['PHONE']
            del amenities['properties']['PARK_TYPE']

            for amenity in amenities['properties']:
                amenities['properties'][amenity] = amenities['properties'][amenity] == 'T' or amenities['properties'][amenity] == 'TRUE' or amenities['properties'][amenity] == 1 or amenities['properties'][amenity] == '1'

            f['geojson']['properties']['AMENITIES'] = amenities['properties']
        else:
            logger.error("No record in amenities file for park " + park_name)
    except Exception as e:
        logger.error("Error occurred trying to add info from amenities file for park: " + park_name)
        logger.error(e)
        logger.error(traceback.format_exc())


def _get_park_hours(park_hours_path=None):
    try:
        with open(park_hours_path) as parks_file:
            return json.load(parks_file)
    except:
        logger.error("Error occurred trying to retrieve park hours.")
        return None

def _get_park_amenities(park_amenities_path=None):
    try:
        with open(park_amenities_path) as amenities_file:
            print(amenities_file)
            return json.load(amenities_file)
    except Exception as e:
        logger.error("Error occurred trying to retrieve park amenities.")
        logger.error(e)
        return None


if __name__ == '__main__':
    import_park_features()

# vim: fenc=utf-8
# vim: filetype=python
