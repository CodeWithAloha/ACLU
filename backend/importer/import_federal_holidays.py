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
import sys
import uuid

from utilities import post_holiday


logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer.federal_holidays")


@click.command()
@click.option('--federal_ics_path', help='Path to federal ICS file', required=True, type=click.Path(exists=True))
@click.option('--api_base_url', default='http://localhost:50050', help='API base url. Defaults to http://localhost:50050')
def import_federal_holidays(federal_ics_path, api_base_url):
    with open(federal_ics_path, 'rb') as fp:
        data = fp.read()
    cal = icalendar.Calendar.from_ical(data)

    for event in cal.walk('vevent'):
        f = _construct_holiday_json(event)
        post_holiday(api_base_url, f)

    return sys.exit(0)


def _construct_holiday_json(event):
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

    return {
        "_id": str(uuid.uuid4()),
        "name": event.get('summary'),
        "type": "federal",
        "holiday_start_at": start.strftime('%a, %d %b %Y %H:%M:%S GMT'),
        "holiday_end_at": end.strftime('%a, %d %b %Y %H:%M:%S GMT')
    }


if __name__ == '__main__':
    import_federal_holidays()


# vim: fenc=utf-8
# vim: filetype=python
