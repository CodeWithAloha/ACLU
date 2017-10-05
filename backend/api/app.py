#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017 Ryan Kanno <ryankanno@localkinegrinds.com>
#
# Distributed under terms of the MIT license.

from eve import Eve
import os
from uuid_encoder import UUIDEncoder
from uuid_validator import UUIDValidator

host = '0.0.0.0'
port = int(os.environ.get('PORT')) if 'PORT' in os.environ else 50050

app = Eve(json_encoder=UUIDEncoder, validator=UUIDValidator)

if __name__ == '__main__':
    app.run(host=host, port=port)

# vim: fenc=utf-8
# vim: filetype=python
