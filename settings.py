"""
settings.py
~~~~~~~~~~~~
 
This module supports configuring the MMAnywhere device server. If you have to
do much (any?) configuration outside of this file to get a basic server up and
running, something needs to be fixed. 
 
:copyright: (c) 2012 by Albert Boehmler
:license: GNU Affero General Public License, see LICENSE for more details.
"""

import ConfigParser
parser = ConfigParser.SafeConfigParser()
parser.read("mm_anywhere.ini")

# the Micro-Manager directory to run from - where the MMCorePy.py is located
MM_DIR = parser.get("mm_anywhere", "MM_DIR")

# the Micro-Manager configuration file to use
SYSTEM_CONFIGURATION = parser.get("mm_anywhere", "SYSTEM_CONFIGURATION")

# host name to use for server (see http://flask.pocoo.org/docs/api/)
MM_ANYWHERE_HOST_NAME = parser.get("mm_anywhere", "MM_ANYWHERE_HOST_NAME")

# which port to host from
MM_ANYWHERE_PORT = int(parser.get("mm_anywhere", "MM_ANYWHERE_PORT"))

# which directory to use to store data
MM_ANYWHERE_HOST_DATA_PATH = parser.get("mm_anywhere", "MM_ANYWHERE_HOST_DATA_PATH")

DEBUG_MODE_ON = bool(parser.get("mm_anywhere", "DEBUG_MODE_ON"))
