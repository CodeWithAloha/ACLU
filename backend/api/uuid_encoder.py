#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eve.io.base import BaseJSONEncoder
from uuid import UUID


class UUIDEncoder(BaseJSONEncoder):
    """ JSONEconder subclass used by the json render function.
    This is different from BaseJSONEoncoder since it also addresses
    encoding of UUID
    """

    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        else:
            # delegate rendering to base class method (the base class
            # will properly render ObjectIds, datetimes, etc.)
            return super(UUIDEncoder, self).default(obj)

# vim: fenc=utf-8
# vim: filetype=python
