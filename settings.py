"""
settings.py
~~~~~~~~~~~~

This module supports configuring the MMAnywhere device server. If you have to
do much (any?) configuration outside of this file to get a basic server up and
running, something needs to be fixed. 

:copyright: (c) 2012 by Albert Boehmler
:license: GNU Affero General Public License, see LICENSE for more details.

"""

# the Micro-Manager directory to run from - where the MMCorePy.py is located
MM_DIR = "C:/Users/ajb/DevTools/Micro-Manager-1.4-32bit"

# the Micro-Manager configuration file to use
SYSTEM_CONFIGURATION = "C:/Users/ajb/micro-manager/Micro-Manager-1.4.cfg"

# host name to use for server (see http://flask.pocoo.org/docs/api/)
MM_ANYWHERE_HOST_NAME="0.0.0.0"

# which port to host from
MM_ANYWHERE_PORT = 5000

# which directory to use to store data
MM_ANYWHERE_HOST_DATA_PATH = "."

DEBUG_MODE_ON = True
