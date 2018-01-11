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
import os
import requests
import sys
import uuid


logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer.parks")


@click.command()
@click.option('--park_features_path', help='Path to park features file being imported.', required=True, type=click.Path(exists=True))
@click.option('--api_base_url', default='http://localhost:50050', help='API base url. Defaults to http://localhost:50050')
def import_park_features(park_features_path, api_base_url):

    organization = _get_organization(api_base_url, "Park")

    if organization:

        park_hours = _get_park_hours("../data/parks/2017.10.20_Honolulu-Park-Hours/park-closure-hours.json")

        for feature in _features_from_path(park_features_path):
            f = _construct_park_feature_json(feature, organization, park_hours)
            _post_features(api_base_url, f)

    return sys.exit(0)


def _construct_park_feature_json(feature, organization, park_hours=None):
    park_name = feature['properties']['name']
    f = {
        "_id": str(uuid.uuid4()),
        "geojson": feature,
        "restrictions": {},
        "organization": organization["_id"],
        "name": park_name,
        "last_imported_at": datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    }

    try:
        hours = park_hours.get(park_name, False)
        if hours:
            logger.info("Setting park hours for {0}".format(park_name))
            hours_parts = hours.get('park')
            f['restrictions']['hours_start'] = int(hours_parts.get('open'))
            f['restrictions']['hours_end'] = int(hours_parts.get('close'))
    except:
        pass

    return f


def _get_park_hours(park_hours_path=None):
    try:
        with open(park_hours_path) as parks_file:
            return json.load(parks_file)
    except:
        logger.error("Error occurred trying to retrieve park hours.")
        return None


def _get_api_resource_url(api_base_url, resource):
    return "{0}/{1}".format(api_base_url, resource)


def _features_from_path(feature_collection_path=None):
    with open(feature_collection_path) as json_data:
        feature_collection = json.load(json_data)
        if 'features' in feature_collection:
            for feature in feature_collection["features"]:
                yield feature


def _post_features(api_base_url, feature_as_json):
    resource_base_url = _get_api_resource_url(api_base_url, 'features')
    r = requests.post(resource_base_url, json=feature_as_json)
    if r.status_code == 201:
        logger.info("Successfully uploaded feature(id=" +
                    feature_as_json["_id"] + ")")
    else:
        logger.info("Unsuccessful: " + r.content)


def _get_organization(api_base_url, organization_name):
    resource_base_url = _get_api_resource_url(api_base_url, 'organizations')
    resource_payload = _get_regex_payload("name", organization_name)
    r = requests.get(resource_base_url, params=resource_payload)
    if r.status_code == 200:
        json_resp = r.json()
        if (len(json_resp["_items"])) == 1:
            return json_resp["_items"][0]
    return None


def _get_regex_payload(field, field_query):
    regex_payload = {field: {'$regex': ".*" + field_query + ".*"}}
    return {'where': json.dumps(regex_payload)}


if __name__ == '__main__':
    import_park_features()

# vim: fenc=utf-8
# vim: filetype=python
