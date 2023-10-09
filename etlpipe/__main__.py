#!/usr/bin/env python
"""
Copyright 2023 Patrick Ingham, Crystal Calvert

This file is part of CubeRubric.

CubeRubric is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

CubeRubric is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with Cuberubric. If not, see <https://www.gnu.org/licenses/>.
"""
import os
import sys
import yaml
import logging
import datetime

import mongoengine as me
import csv
import argparse

# Create command arguments
parser = argparse.ArgumentParser()

parser.add_argument('-d', '--data-dir',
                    help='Path to directory for data storage',
                    type=str, default='/data/cuberubric')

parser.add_argument('-N', '--name',
                    help='Name of the mongoDB',
                    type=str, default='wca')

parser.add_argument('-H', '--host',
                    help='Host address of the mongoDB',
                    type=str, default='localhost')

parser.add_argument('-P', '--port',
                    help='Port for the mongoDB',
                    type=int, default=27017)

parser.add_argument('--wca-api',
                    help='URL for the World Cube Association\'s public API',
                    type=str,
                    default='https://www.worldcubeassociation.org/api/v0/export/public')

# End of argument definitons
args = parser.parse_args()

DATA_DIR = os.path.join(args.data_dir)
if __name__ == '__main__':
    print('Data directory:', DATA_DIR)

