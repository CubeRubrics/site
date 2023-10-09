#!/usr/bin/env python
"""
ODM - Object-Document Mapper

Translating between python objects and mongoDB documents

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


