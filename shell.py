#!/usr/bin/env python

import os
import readline
from pprint import pprint
from datetime import datetime, timedelta
from flask import *

from talisman import app, db
from talisman.user.models import *


os.environ['PYTHONINSPECT'] = 'True'
