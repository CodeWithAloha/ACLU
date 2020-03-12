#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017
#
# Distributed under terms of the MIT license.

import json
import logging
import re

import requests


logger = logging.getLogger("aclu_importer.utilities")


def get_organization(api_base_url, org_name):
    logger.debug(f"Attempting to get an Organization (name={org_name})")

    try:
        resource_base_url = _get_api_resource_url(
            api_base_url,
            'organizations')
        print(resource_base_url)
        resource_payload = _get_regex_payload("name", org_name)
        r = requests.get(resource_base_url, params=resource_payload)
        if r.status_code == 200:
            json_resp = r.json()
            if (len(json_resp["_items"])) == 1:
                return json_resp["_items"][0]
    except Exception as e:
        print(e)
        logger.error(e)
        return None


def get_features_from_tmk(api_base_url, tmk):
    logger.debug(f"Attempting to get an entry with TMK={tmk})")
    try:
        resource_base_url = _get_api_resource_url(
            api_base_url,
            'features')
        resource_payload = {'where': json.dumps({"name": f"TMK {tmk}"})}
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
            feature_id = feature_as_json["_id"]
            logger.info(f"Successfully uploaded Feature (id={feature_id})")
            return id
        else:
            logger.error(r.status_code)
            logger.info("Unsuccessful feature upload")
            return None
    except Exception as e:
        logger.error("Error trying to post Feature")
        logger.error(e)
        return None


def post_park_restriction(api_base_url, park_restriction_as_json):
    try:
        resource_base_url = _get_api_resource_url(api_base_url, 'park_features')
        r = requests.post(resource_base_url, json=park_restriction_as_json)
        logger.info(f"url = {resource_base_url}")
        if r.status_code == 201:
            restriction_id = park_restriction_as_json["_id"]
            logger.info(f"Successfully uploaded Park Restriction (id={restriction_id})")
            return id
        else:
            logger.info("Unsuccessful: " + r.text)
            return None
    except Exception as e:
        logger.error("Error trying to post Park Restriction")
        logger.error(e, exc_info=True)
        return None


def post_holiday(api_base_url, holiday_as_json):
    try:
        resource_base_url = _get_api_resource_url(api_base_url, 'holidays')
        r = requests.post(resource_base_url, json=holiday_as_json)
        if r.status_code == 201:
            holiday_id = holiday_as_json["_id"]
            logger.info(f"Successfully uploaded Holiday (id={holiday_id})")
        else:
            logger.info("Unsuccessful: " + r.content)
    except Exception as e:
        logger.error("Error trying to post Holiday")
        logger.error(e)


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


unicode_re = re.compile(r'\W', re.ASCII)


def normalize_string(input_string: str) -> str:
    """
    Code to convert Hawaiian uncode to ascii, in particular remove kahakos and okinas

    :param input_string: string to clean
    :return: string with kahakos and okinas removed
    """
    trans_input = "Āāēīōōū"
    trans_output = "Aaeioou"
    trans_table = str.maketrans(trans_input, trans_output)
    # need to remove the okina, the translations require a 1 to 1 replacement
    # so do it with a replace
    new_input = input_string.translate(trans_table)
    new_input = new_input.lower()
    return unicode_re.sub('', new_input, re.ASCII)


# vim: fenc=utf-8
# vim: filetype=python
