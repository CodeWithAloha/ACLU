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

from utilities import get_features_from_geojson
from utilities import get_organization
from utilities import get_pyeve_formatted_datetime
from utilities import post_feature
from utilities import post_park_restriction


logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer.parks")


@click.command()
@click.option('--park_features_path', help='Path to park features file being imported.', required=True, type=click.Path(exists=True))
@click.option('--api_base_url', default='http://localhost:50050', help='API base url. Defaults to http://localhost:50050')
def import_park_features(park_features_path, api_base_url):

    start_time = timer()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    organization = get_organization(api_base_url, "Park")

    if organization:

        park_hours = _get_park_hours("../data/parks/2017.10.20_Honolulu-Park-Hours/park-closure-hours.json")

        for feature in get_features_from_geojson(park_features_path):
            pool.apply_async(
                _post_park_feature_and_restriction,
                [api_base_url, organization, feature, park_hours])

    pool.close()
    pool.join()

    end_time = timer()

    logger.info("import_park_features took {} seconds".format(end_time -
                                                              start_time))

    return sys.exit(0)


def _post_park_feature_and_restriction(api_base_url,
                                       organization,
                                       feature,
                                       park_hours):
    f = _construct_park_feature_json(feature, organization)
    feature_id = post_feature(api_base_url, f)
    r = _construct_park_restriction_json(feature, feature_id, park_hours)
    post_park_restriction(api_base_url, r)


def _construct_park_feature_json(feature, organization):

    park_name = feature['properties']['name']

    f = {
        "_id": str(uuid.uuid4()),
        "geojson": feature,
        "organization": organization["_id"],
        "name": park_name,
        "type": "park",
        "ownership": "city",
        "last_imported_at": get_pyeve_formatted_datetime(datetime.datetime.utcnow())
    }

    return f


def _construct_park_restriction_json(feature, feature_id, park_hours=None):

    park_name = feature['properties']['name']

    f = {
        "_id": str(uuid.uuid4()),
        "feature_id": feature_id,
    }

    _attach_park_hours(f, park_name, park_hours)

    return f


def _attach_park_hours(f, park_name, park_hours):
    try:
        hours = park_hours.get(park_name, False)
        if hours:
            logger.info("Setting park hours for {0}".format(park_name))
            hours_parts = hours.get('park')
            f['restrictions'] = {}
            f['restrictions']['hours_start'] = int(hours_parts.get('open'))
            f['restrictions']['hours_end'] = int(hours_parts.get('close'))
        else:
            logger.error("No park hours for " + park_name)
    except Exception as e:
        logger.error("Error occurred trying to attach park hour restrictions: "
                     + str(e))


def _get_park_hours(park_hours_path=None):
    try:
        with open(park_hours_path) as parks_file:
            return json.load(parks_file)
    except:
        logger.error("Error occurred trying to retrieve park hours.")
        return None


if __name__ == '__main__':
    import_park_features()

# vim: fenc=utf-8
# vim: filetype=python
