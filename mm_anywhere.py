"""
mm_anywhere.py
~~~~~~~~~~~~

This module supports starts the MMAnywhere service.

:copyright: (c) 2012 by Albert Boehmler
:license: GNU Affero General Public License, see LICENSE for more details.

"""

# initialize Micro-Manager
import sys, os, settings

cwd = os.getcwd()
os.chdir(settings.MM_DIR)
sys.path.append(settings.MM_DIR)
sys.path.append(cwd)

import MMCorePy
settings.mm_core = MMCorePy.CMMCore()
settings.mm_core.loadSystemConfiguration(settings.SYSTEM_CONFIGURATION)
os.chdir(cwd)

# initialize web application
from flask import Flask
from devices import devices
from configurations import configurations
from mm_app_core import mm_app_core
from acq import acq

app = Flask(__name__)
app.register_blueprint(devices, url_prefix='/devices')
app.register_blueprint(configurations, url_prefix='/configurations')
app.register_blueprint(acq, url_prefix='/acq')
app.register_blueprint(mm_app_core, url_prefix='/mm-app-core')
app.register_blueprint(mm_app_core, url_prefix='/')

print "Starting"

# start web application
app.run(debug=settings.DEBUG_MODE_ON,
        host=settings.MM_ANYWHERE_HOST_NAME,
        port=settings.MM_ANYWHERE_PORT)
