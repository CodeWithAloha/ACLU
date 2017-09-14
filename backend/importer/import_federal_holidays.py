#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017
#
# Distributed under terms of the MIT license.

import click
import datetime
import icalendar
import logging
import logging.config
import os
import requests
import sys
import uuid

logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer.federal_holidays")


API_BASE_URL = "http://localhost:50050"
API_BASE_URL_FORMAT = "{0}/{{0}}".format(API_BASE_URL)


@click.command()
@click.option('--federal_ics_path', default=None, help='Path to federal ICS file')
def import_federal_holidays(federal_ics_path=None):
    if federal_ics_path and os.path.isfile(os.path.realpath(federal_ics_path)):
        with open(federal_ics_path, 'rb') as fp:
            data = fp.read()
        cal = icalendar.Calendar.from_ical(data)
        for event in cal.walk('vevent'):
            calendar_start = event.decoded('dtstart')
            start = datetime.datetime(
                year=calendar_start.year,
                month=calendar_start.month,
                day=calendar_start.day,
                hour=0,
                minute=0,
                second=0)
            end = datetime.datetime(
                year=start.year,
                month=start.month,
                day=start.day,
                hour=23,
                minute=59,
                second=59)
            f = {
                "_id": str(uuid.uuid4()),
                "name": event.get('summary'),
                "type": "federal",
                "holiday_start_at": start.strftime('%a, %d %b %Y %H:%M:%S GMT'),
                "holiday_end_at": end.strftime('%a, %d %b %Y %H:%M:%S GMT')
            }
            _post_holiday(f)
        return sys.exit(0)
    else:
        logger.error("Please input a valid, federal ics file")
        return sys.exit(100)


def _post_holiday(holiday_as_json):
    resource_base_url = _get_resource_url('holidays')
    r = requests.post(resource_base_url, json=holiday_as_json)
    if r.status_code == 201:
        logger.info("Successfully uploaded holiday(id=" + holiday_as_json["_id"] + ")")
    else:
        logger.info("Unsuccessful: " + r.content)


def _get_resource_url(resource_name):
    return API_BASE_URL_FORMAT.format(resource_name)


if __name__ == '__main__':
    import_federal_holidays()


# vim: fenc=utf-8
# vim: filetype=python
