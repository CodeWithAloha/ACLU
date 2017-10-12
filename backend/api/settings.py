#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'aclu')

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
MONGO_QUERY_BLACKLIST = ['$where']
ALLOW_CUSTOM_FIELDS_IN_GEOJSON = True

X_DOMAINS = '*'

features = {
    'item_url': 'regex("[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}")',
    'schema': {
        '_id': {'type': 'uuid'},
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True
        },
        "restrictions": {
            'type': "dict",
            'schema': {
                'datetime_start': {
                    'type': 'datetime',
                },
                'datetime_end': {
                    'type': 'datetime'
                },
                'days': {
                    'type': 'list',
                    'allowed': ['Su', 'M', 'T', 'W', 'Th', 'F', 'Sa']
                },
                'fed_holidays_datetime_start': {
                    'type': 'datetime',
                    'required': False
                },
                'fed_holidays_datetime_end': {
                    'type': 'datetime',
                    'required': False
                },
                'state_holiday_datetime_start': {
                    'type': 'datetime',
                    'required': False
                },
                'state_holiday_datetime_end': {
                    'type': 'datetime',
                    'required': False
                }
            }
        },
        'organization': {
            'type': 'uuid',
            'data_relation': {
                'resource': 'organizations',
                'field': '_id',
                'embeddable': True
            }
        },
        'geojson': {
            'type': 'feature'
        },
        'last_imported_at': {
            'type': 'datetime'
        },
    }
}

organizations = {
    'item_url': 'regex("[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}")',
    'allowed_filters': ['name'],
    'schema': {
        '_id': {'type': 'uuid'},
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True
        }
    }
}

holidays = {
    'item_url': 'regex("[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}")',
    'schema': {
        '_id': {'type': 'uuid'},
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True
        },
        'type': {
            'type': 'string',
            'allowed': ["federal", "state", "city"],
            'required': True
        },
        'holiday_start_at': {
            'type': 'datetime',
            'unique': True,
            'required': True
        },
        'holiday_end_at': {
            'type': 'datetime',
            'required': True
        }
    }
}

DOMAIN = {
    'organizations': organizations,
    'features': features,
    'holidays': holidays
}
