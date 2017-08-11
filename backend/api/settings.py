#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'user')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'user')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'aclu')

features = {
    'item_url': 'regex("[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}")',
    'schema': {
        '_id': {'type': 'uuid'},
        'organization': {
            'type': 'object',
            'schema': {
                '_id': {'type': 'uuid'},
            }
        },
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True,
        },
        'ownership': {
            'type': 'string',
            'allowed': ["city", "state", "private", "federal", "military"],
        },
        'last_imported_at': {
            'type': 'datetime',
        },
    }
}


DOMAIN = {
    'features': features
}
