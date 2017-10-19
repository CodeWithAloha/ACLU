#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017
#
# Distributed under terms of the MIT license.
"""Scraper for park hours"""

import os
import logging
import logging.config
import requests
import json
from bs4 import BeautifulSoup

logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer.park_hours")

PARK_URL = "https://www.honolulu.gov/parks/default/park-closure-hours.html"

"""
    Scrapes the park closure site and returns a dictionary of times
    TODO: handle outliers
    @return mapping { Dictionary<Park { string }, Time { String } > } 
"""


def import_park_hours():
    """Import park hours"""
    page = requests.get(PARK_URL)
    soup = BeautifulSoup(page.text, "html.parser")
    mapping = []
    NAME = "name"
    OPEN = "open"
    HOURS = "hours"
    CLOSE = "close"
    for table in soup('table'):
        # skip table heading
        for tr in table('tr')[1:]:
            cells = tr('td')
            park = cells[0]('span')
            times = cells[1]('span')
            park = [e.text.strip() for e in park]
            times = [e.text.strip() for e in times]
            entry = {}
            while len(park) > len(times):
                times = [""] + times
            while len(times) > len(park):
                park.append(park[-1])

            entry[NAME] = park[0]
            hours = {}
            for p, t in zip(park, times):
                if " to " in t:
                    t = t.split(" to ")
                else:
                    t = t.split('-')
                t = [e.strip() for e in t]
                hours[p] = t
            entry['hours'] = hours
            mapping.append(entry)
    return mapping


if __name__ == '__main__':
    print(json.dumps(import_park_hours()))
