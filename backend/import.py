#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017 Ryan Kanno <ryankanno@localkinegrinds.com>
#
# Distributed under terms of the MIT license.


import logging
import logging.config
import os

logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.conf'))
logger = logging.getLogger("aclu_importer")


def main(argv):
    pass


if __name__ == '__main__':
    main(None)


# vim: fenc=utf-8
# vim: filetype=python
