"""
mm_util.py
~~~~~~~~~~~~

Module of misfit functionality. A place for Micro-Manager and client-side
translation to occur.

:copyright: (c) 2012 by Albert Boehmler
:license: GNU Affero General Public License, see LICENSE for more details.

"""

import settings

def get_property_type_str(prop_type):
    if prop_type == 1:
        return "String"
    elif prop_type == 2:
        return "Float"
    elif prop_type == 3:
        return "Integer"
    else:
        return "Undefined"

def from_js_boolean(js_bool):
    if js_bool == "false":
        return False
    return True
