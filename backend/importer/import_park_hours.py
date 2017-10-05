"""Scraper for park hours"""

import os
import logging
import logging.config
import requests
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
    mapping = {}
    for table in soup('table'):
        # skip table heading
        for tr in table('tr')[1:]:
            cells = tr('td')
            park = cells[0]('span')
            times = cells[1]('span')
            num_park_spans = len(park)
            num_times_spans = len(times)

            if num_park_spans == num_times_spans:
                for p, t in zip(park, times):
                    mapping[p.text.strip()] = t.text.strip()
            elif num_park_spans > num_times_spans:
                name = park[0].text.strip()
                for index, span in enumerate(park[1:]):
                    if index < num_times_spans and index < 1:
                        val = times[index].text.strip()
                mapping[name] = val
            elif num_park_spans < num_times_spans:
                for index, span in enumerate(times[:1]):
                    if index < num_park_spans:
                        # name
                        name = park[index].text.strip()
                    # strip out Winter hours for now
                    span.text.strip()
                val = times[num_times_spans - 1].text.strip()
                mapping[name] = val.replace('(Winter)', '')
    return mapping


if __name__ == '__main__':
    import_park_hours()
