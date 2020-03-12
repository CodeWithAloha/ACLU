#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'aclu')
# need to use URI to set retryWrites
MONGO_URI = "mongodb://{}:{}@{}:{}/{}?retryWrites=false".format(MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST, MONGO_PORT,
                                                                MONGO_DBNAME)

print(MONGO_HOST)
print(MONGO_PORT)
print(MONGO_USERNAME)
print(MONGO_PASSWORD)
print(MONGO_DBNAME)

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
MONGO_QUERY_BLACKLIST = []
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
        'organization': {
            'type': 'uuid',
            'data_relation': {
                'resource': 'organizations',
                'field': '_id',
                'embeddable': True
            }
        },
        'type': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True
        },
        'geojson': {
            'type': 'feature'
        },
        'last_imported_at': {
            'type': 'datetime'
        }
    }
}

park_features = {
    'item_url': 'regex("[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}")',
    'schema': {
        '_id': {'type': 'uuid'},
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True
        },
        'organization': {
            'type': 'uuid',
            'data_relation': {
                'resource': 'organizations',
                'field': '_id',
                'embeddable': True
            }
        },
        'type': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True
        },
        'geojson': {
            'type': 'feature'
        },
        'last_imported_at': {
            'type': 'datetime'
        }
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


feature_park_restrictions = {
    'item_url': 'regex("[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}")',
    'schema': {
        '_id': {'type': 'uuid'},
        'feature_id': {
            'type': 'uuid',
            'required': True
        },
        "restrictions": {
            'type': "dict",
            'schema': {
                'hours_start': { # 0000 - 2359
                    'type': 'number',
                    'required': False
                },
                'hours_end': { # 0000 - 2359
                    'type': 'number',
                    'required': False
                },
                'days': { # blacklist
                    'type': 'list',
                    'allowed': ['Su', 'M', 'T', 'W', 'Th', 'F', 'Sa'],
                    'required': False
                },
                'fed_holidays': { # keys are uuid's of fed holidays,  vals are bool
                    'type': 'boolean',
                    'required': False
                },
                'state_holiday': {
                    'type': 'boolean',
                    'required': False
                }
            }
        }
    }
}


DOMAIN = {
    'organizations': organizations,
    'features': features,
    'park_features': park_features,
    'holidays': holidays
}
