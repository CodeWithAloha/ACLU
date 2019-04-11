
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017
#
# Distributed under terms of the MIT license.

import click
import json
import logging
import requests
import time

logger = logging.getLogger("aclu_importer.utilities")

@click.command()
@click.option('--source', default="./2017-07-13.tmk.geojson", help="Source GEOJson file to import to Mapbox")
@click.option('--dataset', default="", help="Mapbox Dataset ID")
@click.option('--token', default="", help="Mapbox token")
@click.option('--chunksize', default=100, help="Chunk Size of features to import")
def import_to_mapbox(source, dataset, token, chunksize):
    geojson_file = open(source, 'r')
    geojson = json.load(geojson_file)
    geojson_file.close()
    for i in range(int(len(geojson['features']) / chunksize)):
        features = []
        for j in range(chunksize):
            feature_index = (i * chunksize) + j
            # print(geojson['features'][feature_index])
            geojson['features'][feature_index]['id'] = str(geojson['features'][feature_index]['properties']['TMK'])
            features.append(geojson['features'][feature_index])
        post_features(features, i, dataset, token)
        time.sleep(1)
def post_features(features, chunk, dataset='cjti6i86d01r9t5m3rtn863mr', token='tk.eyJ1IjoiZmVsaW1hcnRpbmEiLCJleHAiOjE1NTM2NzQxNjIsImlhdCI6MTU1MzY3MDU2MSwic2NvcGVzIjpbImVzc2VudGlhbHMiLCJzY29wZXM6bGlzdCIsIm1hcDpyZWFkIiwibWFwOndyaXRlIiwidXNlcjpyZWFkIiwidXNlcjp3cml0ZSIsInVwbG9hZHM6cmVhZCIsInVwbG9hZHM6bGlzdCIsInVwbG9hZHM6d3JpdGUiLCJzdHlsZXM6dGlsZXMiLCJzdHlsZXM6cmVhZCIsImZvbnRzOnJlYWQiLCJzdHlsZXM6d3JpdGUiLCJzdHlsZXM6bGlzdCIsInRva2VuczpyZWFkIiwidG9rZW5zOndyaXRlIiwiZGF0YXNldHM6bGlzdCIsImRhdGFzZXRzOnJlYWQiLCJkYXRhc2V0czp3cml0ZSIsInRpbGVzZXRzOmxpc3QiLCJ0aWxlc2V0czpyZWFkIiwidGlsZXNldHM6d3JpdGUiLCJ2aXNpb246cmVhZCIsInN0eWxlczpkcmFmdCIsImZvbnRzOmxpc3QiLCJmb250czp3cml0ZSIsImZvbnRzOm1ldGFkYXRhIiwiZGF0YXNldHM6c3R1ZGlvIiwiY3VzdG9tZXJzOndyaXRlIiwiYW5hbHl0aWNzOnJlYWQiXSwiY2xpZW50IjoibWFwYm94LmNvbSIsImxsIjoxNTUwNzIyODMyNzM3LCJpdSI6bnVsbH0.1J9nBZqBPg8zQBhEV1Kqgw'):
    try:
        # print(features[0]['id'])
        # print(features[0]['type'])
        # resource_base_url1 = 'https://api.mapbox.com/datasets/v1/felimartina/{}/features?access_token={}'.format(dataset, token)
        resource_base_url = 'https://api.mapbox.com/datasets/v1/felimartina/cjti6i86d01r9t5m3rtn863mr/features?access_token=tk.eyJ1IjoiZmVsaW1hcnRpbmEiLCJleHAiOjE1NTM2NzQxNjIsImlhdCI6MTU1MzY3MDU2MSwic2NvcGVzIjpbImVzc2VudGlhbHMiLCJzY29wZXM6bGlzdCIsIm1hcDpyZWFkIiwibWFwOndyaXRlIiwidXNlcjpyZWFkIiwidXNlcjp3cml0ZSIsInVwbG9hZHM6cmVhZCIsInVwbG9hZHM6bGlzdCIsInVwbG9hZHM6d3JpdGUiLCJzdHlsZXM6dGlsZXMiLCJzdHlsZXM6cmVhZCIsImZvbnRzOnJlYWQiLCJzdHlsZXM6d3JpdGUiLCJzdHlsZXM6bGlzdCIsInRva2VuczpyZWFkIiwidG9rZW5zOndyaXRlIiwiZGF0YXNldHM6bGlzdCIsImRhdGFzZXRzOnJlYWQiLCJkYXRhc2V0czp3cml0ZSIsInRpbGVzZXRzOmxpc3QiLCJ0aWxlc2V0czpyZWFkIiwidGlsZXNldHM6d3JpdGUiLCJ2aXNpb246cmVhZCIsInN0eWxlczpkcmFmdCIsImZvbnRzOmxpc3QiLCJmb250czp3cml0ZSIsImZvbnRzOm1ldGFkYXRhIiwiZGF0YXNldHM6c3R1ZGlvIiwiY3VzdG9tZXJzOndyaXRlIiwiYW5hbHl0aWNzOnJlYWQiXSwiY2xpZW50IjoibWFwYm94LmNvbSIsImxsIjoxNTUwNzIyODMyNzM3LCJpdSI6bnVsbH0.1J9nBZqBPg8zQBhEV1Kqgw'
        # print(resource_base_url1)
        # print(resource_base_url)
        r = requests.post(resource_base_url, json={'put':features})
        if r.status_code == 200:
            print("Successfully uploaded chunk {0}".format(chunk))
            return id
        else:
            print(r.status_code)
            print("Unsuccessful chunk {0}: ".format(str(chunk)))
            print(r.content)
            return None
    except Exception as e:
        logging.error('Error ', exc_info=e)
        return None

if __name__ == "__main__":
    import_to_mapbox()

