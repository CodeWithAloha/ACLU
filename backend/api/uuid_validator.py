#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eve.io.mongo import Validator
from uuid import UUID


class UUIDValidator(Validator):
    """
    Extends the base mongo validator adding support for the uuid data-type
    """
    def _validate_type_uuid(self, field, value):
        try:
            UUID(value)
        except ValueError:
            pass

# vim: fenc=utf-8
# vim: filetype=python
