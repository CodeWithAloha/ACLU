#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017
#
# Distributed under terms of the MIT license.

import click
import json


@click.command()
@click.option('--source', default="./2017-07-13.tmk.geojson", help="Source file to split")
@click.option('--destination', default="./tmp", help="Destination folder for files")
@click.option('--count_per_file', default=10000, help="Number of polygons per file")
def split(source, destination, count_per_file):
  geojson = json.loads(open(source, 'r').read())
  for start, index in [(x, x // count_per_file) for x in range(0, len(geojson['features']), count_per_file)]:
    chunked_geojson = {"type": "FeatureCollection",
                       "name": "oahtmk",
                       "crs": {"type": "name",
                               "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
                       'features': geojson['features'][start:start + count_per_file]}
    filename = f"{destination}/{index}.geojson"
    with open(filename, 'w') as output:
      output.write(json.dumps(chunked_geojson))


if __name__ == "__main__":
  split()
