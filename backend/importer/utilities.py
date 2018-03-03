#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017
#
# Distributed under terms of the MIT license.

import json
import logging
import requests


logger = logging.getLogger("aclu_importer.utilities")


def get_organization(api_base_url, org_name):
    logger.debug(
        "Attempting to get an Organization (name={0})".format(org_name))

    try:
        resource_base_url = _get_api_resource_url(
            api_base_url,
            'organizations')

        resource_payload = _get_regex_payload("name", org_name)
        r = requests.get(resource_base_url, params=resource_payload)
        if r.status_code == 200:
            json_resp = r.json()
            if (len(json_resp["_items"])) == 1:
                return json_resp["_items"][0]
    except Exception as e:
        logger.error(e)
        return None


def post_feature(api_base_url, feature_as_json):
    try:
        resource_base_url = _get_api_resource_url(api_base_url, 'features')
        r = requests.post(resource_base_url, json=feature_as_json)
        if r.status_code == 201:
            id = feature_as_json["_id"]
            logger.info("Successfully uploaded Feature (id={0})".format(id))
            return id
        else:
            logger.info("Unsuccessful: " + r.content)
            return None
    except:
        logger.error("Error trying to post Feature")
        return None


def post_park_restriction(api_base_url, park_restriction_as_json):
    try:
        resource_base_url = _get_api_resource_url(api_base_url, 'feature_park_restrictions')
        r = requests.post(resource_base_url, json=park_restriction_as_json)
        if r.status_code == 201:
            id = park_restriction_as_json["_id"]
            logger.info("Successfully uploaded Park Restriction (id={0})".format(id))
            return id
        else:
            logger.info("Unsuccessful: " + r.content)
            return None
    except:
        logger.error("Error trying to post Park Restriction")
        return None


def post_holiday(api_base_url, holiday_as_json):
    try:
        resource_base_url = _get_api_resource_url(api_base_url, 'holidays')
        r = requests.post(resource_base_url, json=holiday_as_json)
        if r.status_code == 201:
            id = holiday_as_json["_id"]
            logger.info("Successfully uploaded Holiday (id={0})".format(id))
        else:
            logger.info("Unsuccessful: " + r.content)
    except:
        logger.error("Error trying to post Holiday")


def get_pyeve_formatted_datetime(a_dt):
    return a_dt.strftime('%a, %d %b %Y %H:%M:%S GMT')


def get_features_from_geojson(geojson_path):
    with open(geojson_path) as geojson:
        feature_collection = json.load(geojson)
        if 'features' in feature_collection:
            for feature in feature_collection["features"]:
                yield feature


def _get_api_resource_url(api_base_url, resource):
    return "{0}/{1}".format(api_base_url, resource)


def _get_regex_payload(field, field_query):
    regex_payload = {field: {'$regex': ".*" + field_query + ".*"}}
    return {'where': json.dumps(regex_payload)}


# vim: fenc=utf-8
# vim: filetype=python
