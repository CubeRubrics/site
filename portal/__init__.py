#!/usr/bin/env python3
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
with CubeRubric. If not, see <https://www.gnu.org/licenses/>.
"""
import os
import sys
import yaml
import logging
import datetime

from flask import Flask
from flask import render_template
from flask import abort

import mongoengine as me

from markupsafe import escape

# Activate Flask app
app = Flask(__name__)
app.config['DEBUG'] = True

logger = app.logger

# NOTE: Beginning of routes / url paths
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


@app.route('/analysis/<page_name>')
def analysis_page(page_name: str):
    if page_name in ('tutorial', 'algorithms', 'scramble'):
        return render_template('analysis.html', page=page_name)

    else:
        abort(404, f"No analysis page for {page_name} found")
