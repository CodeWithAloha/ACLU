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
import re
import sys
from bs4 import BeautifulSoup

logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer.park_hours")

PARK_URL = "https://www.honolulu.gov/parks/default/park-closure-hours.html"


def import_park_hours():
    return parse_park_hours_html_text(get_html_text(PARK_URL))


"""
    Scrapes the park closure site and returns a dictionary of times
    @return mapping { Dictionary<Park { string }, Time { String } > }
"""


def parse_park_closure_times(timestr):
    if not timestr:
        return None
    # online regex playground for this data here: https://regex101.com/r/vR9Gr1/1
    timere = re.compile(
        "((?P<close_word>[A-Za-z]+)|(?P<close_hour>1[0-2]|0?[1-9]):(?P<close_minutes>[0-5][0-9]) (?P<close_ap>[ap])\.m\.)(?P<separator> +(to|-) +)((?P<open_word>[A-Za-z]+)|(?P<open_hour>1[0-2]|0?[1-9]):(?P<open_minutes>[0-5][0-9]) (?P<open_ap>[ap])\.m\.?)(?P<notes>.*)")
    parsed = timere.match(timestr.strip())
    if not parsed:
        return [timestr]

    result = None
    d = parsed.groupdict()
    if d["close_hour"]:
        close_military_time = int(
            d["close_hour"]) * 100 + int(d["close_minutes"]) + (0 if d["close_ap"] == 'a' else 1200)
        open_military_time = int(
            d["open_hour"]) * 100 + int(d["open_minutes"]) + (0 if d["open_ap"] == 'a' else 1200)
        result = {"close": close_military_time, "open": open_military_time}
    elif d["close_word"] and d["open_word"]:
        result = {"close": d["close_word"], "open": d["open_word"]}

    if d["notes"].strip():
        result["notes"] = d["notes"].strip()

    return result


def parse_park_hours_html_text(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    mapping = {}
    for table in soup('table'):
        # skip table heading
        for tr in table('tr')[1:]:
            cells = tr('td')
            park = cells[0]('span')
            times = cells[1]('span')

            # Trim strings and discard empty ones
            park = [e for e in [e.text.strip() for e in park] if e]
            times = [e for e in [e.text.strip() for e in times] if e]

            # Expand times list to match park times
            while len(park) > len(times):
                times = [""] + times

            # Expand park description list to match times
            while len(times) > len(park):
                park.append(park[-1])

            # Assume first line of park description is name
            entry = {'name': park[0], 'hours': {}}

            # then modify first description to be canonical 'park' for entry_hours
            park[0] = "park"

            for desc, time_text in zip(park, times):
                closure_times = parse_park_closure_times(time_text)
                if desc and closure_times:
                    desc = desc.strip("- ")
                    entry['hours'][desc] = closure_times

            mapping[entry["name"]] = entry["hours"]
    return mapping


def get_html_text(url_or_path):
    # if param looks like a url, fetch it
    if url_or_path.lower().startswith("http"):
        return requests.get(url_or_path).text
    # if not, try to read it from a path
    with open(url_or_path, "r") as f:
        return f.read()
    # else return empty string
    return ""


def main(argv):
    url_or_path = argv[1] if len(argv) > 1 else PARK_URL
    html_text = get_html_text(url_or_path)
    park_hours = parse_park_hours_html_text(html_text)
    json_text = json.dumps(park_hours)
    print(json_text)
    return 0


if __name__ == '__main__':
    try:
        result = main(sys.argv)
    except:
        result = -1
        raise
    sys.exit(result)
