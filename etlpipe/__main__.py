#!/usr/bin/env python
"""
etlpipe - Extraction, Transformation and Loading Pipeline

Moving raw data from various sources into the mongoDB

---

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

import urllib3
import csv
import argparse
from dateutil.parser import parse as parsedt

from git import Repo

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

    wca_dir = os.path.join(DATA_DIR, 'wca')
    if not os.path.exists(wca_dir):
        print(f'Creating WCA download directory {wca_dir}')
        os.makedirs(wca_dir)

    wca_data_dir = os.path.join(wca_dir, 'pub')
    wca_meta_dir = os.path.join(wca_dir, 'meta')
    for dir_path in (wca_data_dir, wca_meta_dir):
        if not osi.path.exists(dir_path):
            os.makedirs(dir_path)
    
    # FIXME: Ensure this initializes a repository right in the right place
    repo = Repo.init(wca_data_dir, initial_branch='main')
    print(repo.active_branch)

    print(f'Downloading public export data from {args.wca_api} to {wca_data_dir}')
    wca_resp = urllib3.request('GET', args.wca_api)
    print(f'Status of WCA site is {wca_resp.status}')
    if wca_resp.status == 200:
        print('Data:')
        raw_export_meta = wca_resp.data.decode()
        print(raw_export_meta)
        print()
        export_meta = yaml.safe_load(raw_export_meta)
        export_date = export_meta.get('export_date')
        if export_date is None:
            print('Error, no export_date in WCA metadata. exiting')
            exit()

        elif not isinstance(export_meta['export_date'], datetime.datetime):
            print(f'Warning, export_date="{export_date}" of type {type(export_date)}, converting to datetime')
            _dt_raw = str(export_meta['export_date']).strip()
            export_date = parsedt(_dt_raw)

        export_meta['export_date'] = export_date

        # TODO: Log datetime to a file and determine if a new download is needed

        print('YAML Data:')
        print(yaml.dump(export_meta))

    else:
        print(f'WCA site returned status of {wca_resp.status}, aborting download')
