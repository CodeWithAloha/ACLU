"""Scraper for park hours"""

import os
import logging
import logging.config
import urllib.request
from bs4 import BeautifulSoup

logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer.park_hours")

PARK_URL = "https://www.honolulu.gov/parks/default/park-closure-hours.html"

def import_park_hours():
    """Import park hours"""
    page = urllib.request.urlopen(PARK_URL)
    soup = BeautifulSoup(page, "html.parser")
    for table in soup('table'):
        # skip table heading
        for tr in table('tr')[1:]:
            cells = tr('td')
            park = cells[0]('span')
            times = cells[1]('span')
            num_park_spans = len(park)
            num_times_spans = len(times)
            # TODO needs further cleanup because of:
            # br inside spans
            # empty spans
            # dashes that need to stripped from "- name"
            if num_park_spans == num_times_spans:
                for p, t in zip(park, times):
                    print(p.text.strip())
                    print(t.text.strip())
            # assuming spans are offset by 1
            elif num_park_spans > num_times_spans:
                print(park[0].text.strip())
                for index, span in enumerate(park[1:]):
                    print(span.text.strip())
                    if index < num_times_spans:
                        print(times[index].text.strip())
            elif num_park_spans < num_times_spans:
                for index, span in enumerate(times[:1]):
                    if index < num_park_spans:
                        print(park[index].text.strip())
                    print(span.text.strip())
                print(times[num_times_spans - 1].text.strip())

if __name__ == '__main__':
    import_park_hours()