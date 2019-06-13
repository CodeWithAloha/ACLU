#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017
#
# Distributed under terms of the MIT license.

import click
import datetime
import logging
import logging.config
import multiprocessing
import os
import sys
import uuid


from utilities import get_features_from_geojson
from utilities import get_organization
from utilities import get_pyeve_formatted_datetime
from utilities import post_feature


logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer.tmks")


@click.command()
@click.option('--tmk_features_path', help='Path to tmk features file being imported.', required=True, type=click.Path(exists=True))
@click.option('--api_base_url', default='http://localhost:50050', help='API base url. Defaults to http://localhost:50050')
def import_tmk(tmk_features_path, api_base_url):

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    
    organization = get_organization(api_base_url, "Private")
    
    numFeatures = 0
    if organization:
        for feature in get_features_from_geojson(tmk_features_path):
            numFeatures += 1
            f = _construct_tmk_feature_json(feature, organization)
            pool.apply_async(post_feature, [api_base_url, f])

    print(numFeatures)
    pool.close()
    pool.join()

    return sys.exit(0)


def _construct_tmk_feature_json(feature, organization):
    id = str(uuid.uuid4())
    name = "TMK " + str(feature['properties']['TMK'])
    feature['properties']['NAME'] = name
    feature['properties']['ID'] = id
    feature['properties']['RESTRICTIONS'] = {}
    feature['properties']['OWNERSHIP'] = 'PRIVATE'
    feature['properties']['TYPE'] = 'tmk'
    feature['properties']['ORGANIZATION'] = organization["_id"]
    feature['properties']['FEATURE_TYPE'] = 'TMK'
    
    return {
        "_id": id,
        "geojson": feature,
        "name": name,
        "last_imported_at": get_pyeve_formatted_datetime(datetime.datetime.utcnow())
    }


if __name__ == '__main__':
    import_tmk()

# vim: fenc=utf-8
# vim: filetype=python
