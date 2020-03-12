#!/usr/bin/env python3
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
import csv

from utilities import get_features_from_tmk
from utilities import get_pyeve_formatted_datetime
from utilities import post_feature
from utilities import post_park_restriction
from utilities import normalize_string

logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer.parks")


@click.command()
@click.option('--api_base_url', default='http://localhost:50050',
              help='API base url. Defaults to http://localhost:50050')
@click.option('--park_hours_path', help='Path to park hours file')
def import_park_features(api_base_url, park_hours_path):
    start_time = timer()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    # get park info
    num_parks = 0
    park_hours = _get_park_hours(park_hours_path)
    with open('parks.csv', 'r') as csv_file:
        parks_csv = csv.DictReader(csv_file)
        for row in parks_csv:
            num_parks += 1
            _post_park_hours(api_base_url, park_hours, row)
            # pool.apply_async(
            #     _post_park_hours,
            #     [api_base_url, park_hours, row])
    pool.close()
    pool.join()

    end_time = timer()
    logger.info(f"import_park_features took {end_time - start_time} seconds and processed {num_parks} parks")
    return sys.exit(0)


def _post_park_hours(api_base_url, park_hours, park_data):
    logger.debug("_post_park_hours")
    # feature = get_features_from_tmk(api_base_url, park_data['TMK'])
    # if feature is None:
    #     logger.debug(f"no feature with tmk {park_data['TMK']}, skipping")
    #     return
    # logger.warning(f"feature = {feature}")
    feature = _construct_park_feature_json(park_data,  park_hours)
    #logger.warning(f"{feature}")
    feature_id = post_park_restriction(api_base_url, feature)


def _construct_park_feature_json(park_data, park_hours, feature=None):
    park_name = park_data['PARK_NAME']
    feature_id = str(uuid.uuid4())

    if feature is None:
        feature = {'properties': {}}

    # It is standard to add attributes to geojson properties
    # null point as a placeholder
    feature['geometry'] = {'type': 'Point', 'coordinates': [0, 0]}
    feature['type'] = "Feature"
    feature['properties']['NAME'] = park_name
    feature['properties']['ID'] = feature_id
    feature['properties']['RESTRICTIONS'] = {}
    feature['properties']['OWNERSHIP'] = 'CITY'
    feature['properties']['TYPE'] = 'park'
    feature['properties']['FEATURE_TYPE'] = 'PARK'

    f = {
        "_id": feature_id,
        "geojson": feature,
        "name": park_name,
        "tmk": park_data['TMK'],
        "last_imported_at": get_pyeve_formatted_datetime(datetime.datetime.utcnow()),
        "type": "park"

    }

    logger.info(f)
    _attach_park_hours_restrictions(f, park_name, park_hours)
    logger.info(f)
    return f


def _attach_park_hours_restrictions(f, park_name, park_hours):
    try:
        hours = park_hours.get(normalize_string(park_name), False)

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


def _get_park_hours(park_hours_path=None):
    try:
        with open(park_hours_path) as parks_file:
            return json.load(parks_file)
    except IOError as e:
        logger.error("Error occurred trying to retrieve park hours.")
        logger.error(e)
        return None


if __name__ == '__main__':
    import_park_features()

# vim: fenc=utf-8
# vim: filetype=python
